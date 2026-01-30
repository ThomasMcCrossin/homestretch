#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest


AUTO_MATCH_METHOD = "T2_FINAL_AUTO_CC_PAYMENT_TRANSFER_EXACT_AMOUNT"


@dataclass(frozen=True)
class BankPayment:
    bank_txn_id: str
    bank_date: str
    amount_cents: int
    card_last4: str


@dataclass(frozen=True)
class CandidateBill:
    wave_bill_id: int
    invoice_date: str
    total_cents: int
    vendor_raw: str
    cc_txn_id: str


def scope_window(fys: list[FiscalYear]) -> tuple[str, str]:
    start = min(fy.start_date for fy in fys)
    end = max(fy.end_date for fy in fys)
    return start, end


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def fetch_cc_payments(conn, *, start_date: str, end_date: str) -> list[BankPayment]:
    rows = conn.execute(
        """
        SELECT
          id,
          txn_date,
          CAST(debit_cents AS INTEGER) AS debit_cents,
          COALESCE(card_last4, '') AS card_last4
        FROM fresher_debits__bank_transactions
        WHERE txn_type = 'CC_PAYMENT'
          AND txn_date >= ? AND txn_date <= ?
          AND CAST(debit_cents AS INTEGER) > 0
        ORDER BY txn_date, CAST(id AS INTEGER)
        """,
        (start_date, end_date),
    ).fetchall()
    out: list[BankPayment] = []
    for r in rows:
        out.append(
            BankPayment(
                bank_txn_id=str(r["id"]),
                bank_date=str(r["txn_date"]),
                amount_cents=int(r["debit_cents"] or 0),
                card_last4=str(r["card_last4"] or ""),
            )
        )
    return out


def fetch_existing_cc_payment_linked_bank_ids(conn) -> set[str]:
    """
    Bank CC payment txns that are already linked to at least one Wave bill, via:
    - match_type='CC_PAYMENT_TRANSFER' (bank_txn_id), or
    - match_type='CC_PURCHASE' (cc_payment_txn_id)
    """
    out: set[str] = set()
    rows = conn.execute(
        """
        SELECT DISTINCT bank_txn_id
        FROM fresher_debits__wave_matches
        WHERE match_type = 'CC_PAYMENT_TRANSFER'
          AND bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        """
    ).fetchall()
    out |= {str(r["bank_txn_id"]).strip() for r in rows if str(r["bank_txn_id"] or "").strip()}

    rows = conn.execute(
        """
        SELECT DISTINCT cc_payment_txn_id
        FROM fresher_debits__wave_matches
        WHERE match_type = 'CC_PURCHASE'
          AND cc_payment_txn_id IS NOT NULL AND TRIM(cc_payment_txn_id) <> ''
        """
    ).fetchall()
    out |= {str(r["cc_payment_txn_id"]).strip() for r in rows if str(r["cc_payment_txn_id"] or "").strip()}
    return out


def fetch_existing_cc_payment_linked_bill_ids(conn) -> set[str]:
    """
    Wave bills that already have an explicit link to a CC payment, via:
    - match_type='CC_PAYMENT_TRANSFER', or
    - match_type='CC_PURCHASE' with cc_payment_txn_id populated
    """
    out: set[str] = set()
    rows = conn.execute(
        """
        SELECT DISTINCT wave_bill_id
        FROM fresher_debits__wave_matches
        WHERE match_type = 'CC_PAYMENT_TRANSFER'
        """
    ).fetchall()
    out |= {str(r["wave_bill_id"]).strip() for r in rows if str(r["wave_bill_id"] or "").strip()}

    rows = conn.execute(
        """
        SELECT DISTINCT wave_bill_id
        FROM fresher_debits__wave_matches
        WHERE match_type = 'CC_PURCHASE'
          AND cc_payment_txn_id IS NOT NULL AND TRIM(cc_payment_txn_id) <> ''
        """
    ).fetchall()
    out |= {str(r["wave_bill_id"]).strip() for r in rows if str(r["wave_bill_id"] or "").strip()}
    return out


def fetch_unlinked_cc_purchase_bills(conn, *, linked_bill_ids: set[str]) -> dict[int, list[CandidateBill]]:
    """
    Returns mapping of total_cents -> candidate bills that:
    - are in-scope Wave bills,
    - have match_type='CC_PURCHASE',
    - do NOT have cc_payment_txn_id set,
    - and do NOT already have any CC payment link (linked_bill_ids).
    """
    rows = conn.execute(
        """
        SELECT
          wm.wave_bill_id,
          wb.invoice_date,
          CAST(wb.total_cents AS INTEGER) AS total_cents,
          wb.vendor_raw,
          COALESCE(wm.cc_txn_id, '') AS cc_txn_id
        FROM fresher_debits__wave_matches wm
        JOIN wave_bills wb ON wb.id = CAST(wm.wave_bill_id AS INTEGER)
        WHERE wm.match_type = 'CC_PURCHASE'
          AND (wm.cc_payment_txn_id IS NULL OR TRIM(wm.cc_payment_txn_id) = '')
        ORDER BY wb.invoice_date, CAST(wm.wave_bill_id AS INTEGER)
        """
    ).fetchall()

    out: dict[int, list[CandidateBill]] = {}
    for r in rows:
        wave_bill_id = str(r["wave_bill_id"]).strip()
        if not wave_bill_id or wave_bill_id in linked_bill_ids:
            continue
        out.setdefault(int(r["total_cents"] or 0), []).append(
            CandidateBill(
                wave_bill_id=int(wave_bill_id),
                invoice_date=str(r["invoice_date"] or ""),
                total_cents=int(r["total_cents"] or 0),
                vendor_raw=str(r["vendor_raw"] or ""),
                cc_txn_id=str(r["cc_txn_id"] or ""),
            )
        )
    return out


def delete_auto_rows(conn) -> int:
    row = conn.execute(
        """
        SELECT COUNT(*) AS n
        FROM fresher_debits__wave_matches
        WHERE match_type = 'CC_PAYMENT_TRANSFER'
          AND match_method = ?
        """,
        (AUTO_MATCH_METHOD,),
    ).fetchone()
    n = int(row["n"] or 0) if row else 0
    conn.execute(
        """
        DELETE FROM fresher_debits__wave_matches
        WHERE match_type = 'CC_PAYMENT_TRANSFER'
          AND match_method = ?
        """,
        (AUTO_MATCH_METHOD,),
    )
    return n


def next_wave_match_id_start(conn) -> int:
    row = conn.execute("SELECT MAX(CAST(id AS INTEGER)) AS max_id FROM fresher_debits__wave_matches").fetchone()
    return int(row["max_id"] or 0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument(
        "--max-days",
        type=int,
        default=90,
        help="Only auto-link when abs(bank_date - bill_invoice_date) <= max-days.",
    )
    ap.add_argument("--reset", action="store_true", help="Delete previously inserted auto CC_PAYMENT_TRANSFER rows and rebuild.")
    ap.add_argument("--dry-run", action="store_true", help="Compute suggested links but do not write to the DB.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_detail_csv = args.out_dir / "cc_payment_transfer_links_added.csv"
    out_summary_md = args.out_dir / "cc_payment_transfer_links_added.md"

    conn = connect_db(args.db)
    try:
        conn.execute("BEGIN")

        deleted = 0
        if args.reset and not args.dry_run:
            deleted = delete_auto_rows(conn)

        payments = fetch_cc_payments(conn, start_date=start_date, end_date=end_date)
        linked_bank_ids = fetch_existing_cc_payment_linked_bank_ids(conn)
        linked_bill_ids = fetch_existing_cc_payment_linked_bill_ids(conn)
        candidates_by_amount = fetch_unlinked_cc_purchase_bills(conn, linked_bill_ids=linked_bill_ids)

        max_id = next_wave_match_id_start(conn)

        inserted_rows: list[dict[str, str]] = []
        skipped_rows: list[dict[str, str]] = []

        for p in payments:
            if p.bank_txn_id in linked_bank_ids:
                skipped_rows.append(
                    {
                        "bank_txn_id": p.bank_txn_id,
                        "bank_date": p.bank_date,
                        "bank_amount": cents_to_dollars(p.amount_cents),
                        "reason": "already_linked",
                    }
                )
                continue

            cands = candidates_by_amount.get(p.amount_cents, [])
            if not cands:
                skipped_rows.append(
                    {
                        "bank_txn_id": p.bank_txn_id,
                        "bank_date": p.bank_date,
                        "bank_amount": cents_to_dollars(p.amount_cents),
                        "reason": "no_candidate_bill",
                    }
                )
                continue

            bdate = parse_iso(p.bank_date)
            if not bdate:
                skipped_rows.append(
                    {
                        "bank_txn_id": p.bank_txn_id,
                        "bank_date": p.bank_date,
                        "bank_amount": cents_to_dollars(p.amount_cents),
                        "reason": "invalid_bank_date",
                    }
                )
                continue

            filtered: list[tuple[CandidateBill, int]] = []
            for bill in cands:
                idate = parse_iso(bill.invoice_date)
                if not idate:
                    continue
                diff_days = abs((bdate - idate).days)
                if diff_days <= int(args.max_days):
                    filtered.append((bill, diff_days))

            if len(filtered) != 1:
                reason = "ambiguous_candidates" if len(filtered) > 1 else "candidate_out_of_range"
                skipped_rows.append(
                    {
                        "bank_txn_id": p.bank_txn_id,
                        "bank_date": p.bank_date,
                        "bank_amount": cents_to_dollars(p.amount_cents),
                        "reason": reason,
                        "candidates": str(len(cands)),
                        "candidates_in_range": str(len(filtered)),
                    }
                )
                continue

            bill, abs_diff_days = filtered[0]
            idate = parse_iso(bill.invoice_date)
            if not idate:
                skipped_rows.append(
                    {
                        "bank_txn_id": p.bank_txn_id,
                        "bank_date": p.bank_date,
                        "bank_amount": cents_to_dollars(p.amount_cents),
                        "reason": "invalid_bill_date",
                    }
                )
                continue

            signed_diff = (bdate - idate).days

            max_id += 1
            match_id = str(max_id)
            notes = (
                f"t2-final auto CC_PAYMENT_TRANSFER exact amount; "
                f"bank_txn_id={p.bank_txn_id}; bank_date={p.bank_date}; bank_amount_cents={p.amount_cents}; "
                f"wave_bill_id={bill.wave_bill_id}; invoice_date={bill.invoice_date}; vendor_raw={bill.vendor_raw}; "
                f"cc_txn_id={bill.cc_txn_id}; max_days={args.max_days}"
            )

            if not args.dry_run:
                conn.execute(
                    """
                    INSERT INTO fresher_debits__wave_matches (
                      id, wave_bill_id, match_type,
                      bank_txn_id, cc_txn_id, cc_payment_txn_id,
                      confidence, match_method,
                      date_diff_days, amount_diff_cents, notes
                    ) VALUES (?, ?, 'CC_PAYMENT_TRANSFER', ?, ?, ?, 'HIGH', ?, ?, '0', ?)
                    """,
                    (
                        match_id,
                        str(bill.wave_bill_id),
                        p.bank_txn_id,
                        bill.cc_txn_id,
                        p.bank_txn_id,
                        AUTO_MATCH_METHOD,
                        str(signed_diff),
                        notes,
                    ),
                )

            linked_bank_ids.add(p.bank_txn_id)
            linked_bill_ids.add(str(bill.wave_bill_id))

            inserted_rows.append(
                {
                    "bank_txn_id": p.bank_txn_id,
                    "bank_date": p.bank_date,
                    "bank_amount_cents": str(p.amount_cents),
                    "bank_amount": cents_to_dollars(p.amount_cents),
                    "card_last4": p.card_last4,
                    "wave_bill_id": str(bill.wave_bill_id),
                    "invoice_date": bill.invoice_date,
                    "vendor_raw": bill.vendor_raw,
                    "cc_txn_id": bill.cc_txn_id,
                    "abs_date_diff_days": str(abs_diff_days),
                    "signed_date_diff_days": str(signed_diff),
                    "match_method": AUTO_MATCH_METHOD,
                }
            )

        if args.dry_run:
            conn.execute("ROLLBACK")
        else:
            conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()

    # Write outputs
    out_detail_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "bank_txn_id",
            "bank_date",
            "bank_amount_cents",
            "bank_amount",
            "card_last4",
            "wave_bill_id",
            "invoice_date",
            "vendor_raw",
            "cc_txn_id",
            "abs_date_diff_days",
            "signed_date_diff_days",
            "match_method",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in inserted_rows:
            w.writerow(r)

    lines: list[str] = []
    lines.append("# CC payment → Wave bill links added (CC_PAYMENT_TRANSFER)\n\n")
    lines.append(f"- Scope: {start_date} → {end_date}\n")
    lines.append(f"- max_days: {args.max_days}\n")
    lines.append(f"- reset_deleted_rows: {deleted}\n")
    lines.append(f"- inserted_rows: {len(inserted_rows)}\n")
    lines.append(f"- skipped_rows: {len(skipped_rows)}\n")
    if args.dry_run:
        lines.append("- dry_run: 1 (DB not modified)\n")
    lines.append("\nOutputs:\n")
    lines.append(f"- {out_detail_csv}\n")

    # Summarize skips
    by_reason: dict[str, int] = {}
    for r in skipped_rows:
        reason = (r.get("reason") or "").strip() or "unknown"
        by_reason[reason] = by_reason.get(reason, 0) + 1
    if by_reason:
        lines.append("\nSkip reasons:\n\n")
        lines.append("reason | count\n")
        lines.append("-|-\n")
        for reason, cnt in sorted(by_reason.items(), key=lambda x: (-x[1], x[0])):
            lines.append(f"{reason} | {cnt}\n")

    out_summary_md.write_text("".join(lines), encoding="utf-8")

    print("CC payment transfer links built")
    print(f"- db: {args.db}")
    print(f"- inserted: {len(inserted_rows)}")
    print(f"- out: {out_detail_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

