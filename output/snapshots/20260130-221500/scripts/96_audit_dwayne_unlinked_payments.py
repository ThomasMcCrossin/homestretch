#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest


@dataclass(frozen=True)
class UnlinkedCCPayment:
    bank_txn_id: str
    bank_date: str
    card_last4: str
    amount_cents: int
    wave_bill_candidates: list[tuple[int, str, str]]
    purchase_context: list[str]


def scope_window(fys: list[FiscalYear]) -> tuple[str, str]:
    start = min(fy.start_date for fy in fys)
    end = max(fy.end_date for fy in fys)
    return start, end


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def parse_iso(d: str) -> date | None:
    s = (d or "").strip()
    if not s:
        return None
    return date.fromisoformat(s)


def fetch_unlinked_cc_payments(conn, *, start_date: str, end_date: str) -> list[UnlinkedCCPayment]:
    """
    CC payments from the bank that have **no** linked Wave bill via any of:
    - match_type='CC_PAYMENT_TRANSFER' (bank_txn_id), or
    - fresher_debits__bank_allocations (target_type='WAVE_BILL'), or
    - fresher_debits__wave_bill_funding, or
    - fresher_debits__split_payments (txn_type='BANK'), or
    - fresher_debits__wave_matches.cc_payment_txn_id (any match_type)

    NOTE: We intentionally do NOT attempt fuzzy/FIFO matching here. This is a strict “no supporting link exists”
    exception list.
    """

    cc_payment_bank_ids = {
        str(r["bank_txn_id"]).strip()
        for r in conn.execute(
            """
            SELECT DISTINCT bank_txn_id
            FROM fresher_debits__cc_payment_links
            WHERE bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
            """
        ).fetchall()
        if str(r["bank_txn_id"] or "").strip()
    }

    # Gather supporting links from multiple tables.
    linked_bank_ids: set[str] = set()
    linked_bank_ids.update(
        str(r["bank_txn_id"]).strip()
        for r in conn.execute(
            """
            SELECT DISTINCT bank_txn_id
            FROM fresher_debits__wave_matches
            WHERE match_type='CC_PAYMENT_TRANSFER'
              AND bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
            """
        ).fetchall()
        if str(r["bank_txn_id"] or "").strip()
    )
    linked_bank_ids.update(
        str(r["bank_txn_id"]).strip()
        for r in conn.execute(
            """
            SELECT DISTINCT bank_txn_id
            FROM fresher_debits__bank_allocations
            WHERE target_type='WAVE_BILL'
              AND bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
              AND target_id IS NOT NULL AND TRIM(target_id) <> ''
            """
        ).fetchall()
        if str(r["bank_txn_id"] or "").strip()
    )
    linked_bank_ids.update(
        str(r["bank_txn_id"]).strip()
        for r in conn.execute(
            """
            SELECT DISTINCT bank_txn_id
            FROM fresher_debits__wave_bill_funding
            WHERE bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
            """
        ).fetchall()
        if str(r["bank_txn_id"] or "").strip()
    )
    linked_bank_ids.update(
        str(r["txn_id"]).strip()
        for r in conn.execute(
            """
            SELECT DISTINCT txn_id
            FROM fresher_debits__split_payments
            WHERE txn_type='BANK'
              AND txn_id IS NOT NULL AND TRIM(txn_id) <> ''
            """
        ).fetchall()
        if str(r["txn_id"] or "").strip()
    )
    linked_bank_ids.update(
        str(r["cc_payment_txn_id"]).strip()
        for r in conn.execute(
            """
            SELECT DISTINCT cc_payment_txn_id
            FROM fresher_debits__wave_matches
            WHERE cc_payment_txn_id IS NOT NULL AND TRIM(cc_payment_txn_id) <> ''
            """
        ).fetchall()
        if str(r["cc_payment_txn_id"] or "").strip()
    )

    rows = conn.execute(
        """
        SELECT
          b.id AS bank_txn_id,
          b.txn_date AS bank_date,
          COALESCE(b.card_last4, '') AS card_last4,
          CAST(b.debit_cents AS INTEGER) AS bank_debit_cents
        FROM fresher_debits__bank_transactions b
        WHERE b.used='1'
          AND b.txn_date >= ? AND b.txn_date <= ?
          AND b.txn_type='CC_PAYMENT'
          AND CAST(b.debit_cents AS INTEGER) > 0
          AND b.id IN (SELECT DISTINCT bank_txn_id FROM fresher_debits__cc_payment_links)
        ORDER BY CAST(b.debit_cents AS INTEGER) DESC, b.txn_date, CAST(b.id AS INTEGER)
        """,
        (start_date, end_date),
    ).fetchall()

    # Pre-index CC purchases by amount for lightweight context.
    purchases_by_amount: dict[int, list[tuple[str, str, str, str]]] = defaultdict(list)
    for r in conn.execute(
        """
        SELECT id, txn_date, COALESCE(card_last4, '') AS card_last4,
               COALESCE(merchant_parsed, '') AS merchant_parsed,
               COALESCE(description, '') AS description,
               CAST(debit_cents AS INTEGER) AS debit_cents
        FROM fresher_debits__cc_transactions
        WHERE txn_type='PURCHASE'
          AND debit_cents IS NOT NULL AND TRIM(debit_cents) <> ''
        """
    ).fetchall():
        try:
            amt = int(r["debit_cents"] or 0)
        except (TypeError, ValueError):
            continue
        if amt <= 0:
            continue
        purchases_by_amount[amt].append(
            (
                str(r["id"]),
                str(r["txn_date"] or ""),
                str(r["card_last4"] or ""),
                str(r["merchant_parsed"] or r["description"] or ""),
            )
        )

    out: list[UnlinkedCCPayment] = []
    for r in rows:
        amt = int(r["bank_debit_cents"] or 0)
        bank_txn_id = str(r["bank_txn_id"])
        if bank_txn_id not in cc_payment_bank_ids:
            # Not a CC payment we can attribute to a tracked card.
            continue
        if bank_txn_id in linked_bank_ids:
            continue

        purchase_context: list[str] = []
        bank_dt = parse_iso(str(r["bank_date"]))
        if bank_dt:
            lo = bank_dt - timedelta(days=7)
            hi = bank_dt + timedelta(days=7)
            for cc_id, cc_dt, card_last4, merchant in sorted(purchases_by_amount.get(amt, []), key=lambda x: x[1]):
                try:
                    pdt = parse_iso(cc_dt)
                except Exception:
                    pdt = None
                if not pdt or pdt < lo or pdt > hi:
                    continue
                merchant_trim = (merchant or "").strip()
                merchant_trim = merchant_trim[:80] + "..." if len(merchant_trim) > 83 else merchant_trim
                purchase_context.append(f"{cc_dt} card {card_last4} cc_txn {cc_id} :: {merchant_trim}")

        candidates_rows = conn.execute(
            """
            SELECT id, invoice_date, vendor_raw
            FROM wave_bills
            WHERE total_cents = ?
            ORDER BY invoice_date, id
            """,
            (amt,),
        ).fetchall()
        candidates = [(int(x["id"]), str(x["invoice_date"]), str(x["vendor_raw"] or "")) for x in candidates_rows]
        out.append(
            UnlinkedCCPayment(
                bank_txn_id=bank_txn_id,
                bank_date=str(r["bank_date"]),
                card_last4=str(r["card_last4"] or ""),
                amount_cents=amt,
                wave_bill_candidates=candidates,
                purchase_context=purchase_context,
            )
        )
    return out


def fetch_unmatched_dwayne_reimbursements(conn, *, start_date: str, end_date: str) -> list[dict[str, str]]:
    """
    Bank e-transfers to Dwayne that clear 2410 but have no wave_bill_reimbursement journal.
    """
    rows = conn.execute(
        """
        SELECT b.id AS bank_txn_id, b.txn_date, CAST(b.debit_cents AS INTEGER) AS debit_cents, b.description, b.notes
        FROM fresher_debits__bank_transactions b
        WHERE b.txn_date >= ? AND b.txn_date <= ?
          AND CAST(b.debit_cents AS INTEGER) > 0
          AND LOWER(COALESCE(b.description, '')) LIKE '%dwayne%'
        ORDER BY b.txn_date, CAST(b.id AS INTEGER)
        """,
        (start_date, end_date),
    ).fetchall()

    out: list[dict[str, str]] = []
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"])
        # Must be posted to 2410 (due to Dwayne) via bank_debits.
        posted = conn.execute(
            """
            SELECT 1
            FROM journal_entries je
            JOIN journal_entry_lines jl ON jl.journal_entry_id = je.id
            WHERE je.source_record_type = 'bank_debits'
              AND je.source_record_id = ?
              AND jl.account_code = '2410'
              AND CAST(jl.debit_cents AS INTEGER) > 0
            LIMIT 1
            """,
            (bank_txn_id,),
        ).fetchone()
        if not posted:
            continue

        reimb = conn.execute(
            """
            SELECT 1
            FROM journal_entries je
            WHERE je.source_record_type = 'wave_bill_reimbursement'
              AND je.source_record_id = ?
            LIMIT 1
            """,
            (bank_txn_id,),
        ).fetchone()
        if reimb:
            continue

        out.append(
            {
                "bank_txn_id": bank_txn_id,
                "bank_date": str(r["txn_date"]),
                "amount": cents_to_dollars(int(r["debit_cents"] or 0)),
                "notes": str(r["notes"] or ""),
            }
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")
    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_md = args.out_dir / "dwayne_unlinked_payments_report.md"
    out_csv = args.out_dir / "dwayne_unlinked_cc_payments.csv"

    conn = connect_db(args.db)
    try:
        unlinked_cc = fetch_unlinked_cc_payments(conn, start_date=start_date, end_date=end_date)
        unmatched_reimb = fetch_unmatched_dwayne_reimbursements(conn, start_date=start_date, end_date=end_date)
    finally:
        conn.close()

    total_unlinked_cents = sum(x.amount_cents for x in unlinked_cc)
    no_wave = [x for x in unlinked_cc if not x.wave_bill_candidates]
    has_wave = [x for x in unlinked_cc if x.wave_bill_candidates]

    fy_amounts = defaultdict(int)
    for x in unlinked_cc:
        fy = "FY2024" if x.bank_date <= "2024-05-31" else "FY2025"
        fy_amounts[fy] += x.amount_cents

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "bank_txn_id",
                "bank_date",
                "card_last4",
                "amount",
                "purchase_context_count",
                "purchase_context",
                "wave_bill_candidates_count",
                "wave_bill_candidates",
            ],
        )
        w.writeheader()
        for x in unlinked_cc:
            w.writerow(
                {
                    "bank_txn_id": x.bank_txn_id,
                    "bank_date": x.bank_date,
                    "card_last4": x.card_last4,
                    "amount": cents_to_dollars(x.amount_cents),
                    "purchase_context_count": str(len(x.purchase_context)),
                    "purchase_context": "; ".join(x.purchase_context[:3]),
                    "wave_bill_candidates_count": str(len(x.wave_bill_candidates)),
                    "wave_bill_candidates": "; ".join(
                        f"{bid} ({dt}) {vendor}" for bid, dt, vendor in x.wave_bill_candidates[:5]
                    ),
                }
            )

    lines: list[str] = []
    lines.append("# Dwayne: bank payments not linked to Wave bills (audit)\n\n")
    lines.append(f"Scope: {start_date} → {end_date}\n\n")
    lines.append("## Summary\n\n")
    lines.append(f"- Unlinked CC payments: {len(unlinked_cc)} totaling ${total_unlinked_cents/100:.2f}\n")
    lines.append(
        f"  - No Wave bill candidates by exact amount: {len(no_wave)} totaling ${sum(x.amount_cents for x in no_wave)/100:.2f}\n"
    )
    lines.append(
        f"  - Has Wave bill candidates by exact amount: {len(has_wave)} totaling ${sum(x.amount_cents for x in has_wave)/100:.2f}\n"
    )
    lines.append(f"- FY2024 unlinked CC total: ${fy_amounts['FY2024']/100:.2f}\n")
    lines.append(f"- FY2025 unlinked CC total: ${fy_amounts['FY2025']/100:.2f}\n")

    lines.append("\n## Unmatched reimbursements to Dwayne (no Wave reimbursement journal)\n\n")
    if unmatched_reimb:
        lines.append("bank_txn_id | bank_date | amount | notes\n")
        lines.append("-|-|-|-|\n")
        for r in unmatched_reimb:
            note = (r.get("notes") or "").strip()
            if len(note) > 120:
                note = note[:117] + "..."
            lines.append(f"{r['bank_txn_id']} | {r['bank_date']} | ${r['amount']} | {note}\n")
    else:
        lines.append("- None detected.\n")

    lines.append("\n## Unlinked CC payments (detail)\n\n")
    lines.append("bank_txn_id | bank_date | card | amount | cc_purchase_context | wave_bill_candidates\n")
    lines.append("-|-|-|-|-|-\n")
    for x in unlinked_cc:
        if x.purchase_context:
            ctx = "; ".join(x.purchase_context[:2])
            if len(x.purchase_context) > 2:
                ctx += f" (+{len(x.purchase_context)-2} more)"
        else:
            ctx = "(none)"
        if x.wave_bill_candidates:
            cand = ", ".join(f"{bid}({dt})" for bid, dt, _ in x.wave_bill_candidates[:3])
            if len(x.wave_bill_candidates) > 3:
                cand += f" (+{len(x.wave_bill_candidates)-3} more)"
        else:
            cand = "(none)"
        lines.append(
            f"{x.bank_txn_id} | {x.bank_date} | {x.card_last4 or ''} | ${cents_to_dollars(x.amount_cents)} | {ctx} | {cand}\n"
        )

    out_md.write_text("".join(lines), encoding="utf-8")

    print("Dwayne unlinked payments audit built")
    print(f"- out: {out_md}")
    print(f"- out_csv: {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
