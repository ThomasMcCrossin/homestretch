#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"
DEFAULT_BANK_OVERRIDE_PATH = PROJECT_ROOT / "overrides" / "bank_txn_category_overrides.yml"


@dataclass(frozen=True)
class BankTxn:
    id: str
    txn_date: str
    debit_cents: int
    description: str


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def load_bank_txn_category_override_entries(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    data = load_yaml(path)
    raw = data.get("bank_txn_category_overrides")
    if not isinstance(raw, dict):
        return {}
    out: dict[str, dict] = {}
    for bank_txn_id, cfg in raw.items():
        if not isinstance(cfg, dict):
            continue
        to_cat = str(cfg.get("to_category") or "").strip()
        if not to_cat:
            continue
        entry = dict(cfg)
        entry["to_category"] = to_cat
        out[str(bank_txn_id).strip()] = entry
    return out


def fetch_bank_txn_categories(conn) -> dict[str, str]:
    """
    Prefer verified classifications when multiple exist.
    Returns bank_txn_id -> txn_category
    """
    rows = conn.execute(
        """
        SELECT id, bank_txn_id, txn_category, verified
        FROM fresher_debits__bank_txn_classifications
        ORDER BY CAST(verified AS INTEGER) DESC, CAST(id AS INTEGER) ASC
        """
    ).fetchall()
    out: dict[str, str] = {}
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"] or "").strip()
        if not bank_txn_id or bank_txn_id in out:
            continue
        out[bank_txn_id] = str(r["txn_category"] or "").strip()
    return out


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def scope_window(fys: list[FiscalYear]) -> tuple[str, str]:
    start = min(fy.start_date for fy in fys)
    end = max(fy.end_date for fy in fys)
    return start, end


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"

def is_credit_card_payment(conn, bank_txn_id: str) -> bool:
    row = conn.execute(
        """
        SELECT 1
        FROM fresher_debits__cc_payment_links
        WHERE bank_txn_id = ?
        LIMIT 1
        """,
        (str(bank_txn_id),),
    ).fetchone()
    return bool(row)


def fetch_bank_txns(conn, *, start_date: str, end_date: str) -> dict[str, BankTxn]:
    rows = conn.execute(
        """
        SELECT id, txn_date, CAST(debit_cents AS INTEGER) AS debit_cents, description
        FROM fresher_debits__bank_transactions
        WHERE txn_date >= ? AND txn_date <= ?
          AND CAST(debit_cents AS INTEGER) > 0
        """,
        (start_date, end_date),
    ).fetchall()
    out: dict[str, BankTxn] = {}
    for r in rows:
        out[str(r["id"])] = BankTxn(
            id=str(r["id"]),
            txn_date=str(r["txn_date"]),
            debit_cents=int(r["debit_cents"] or 0),
            description=str(r["description"] or ""),
        )
    return out


def fetch_wave_match_groups(conn) -> dict[str, list[int]]:
    """
    Wave matches are used here only as a fallback evidence source for *direct vendor payments*
    that cleared AP from the bank.

    Important exclusions:
    - CC_PAYMENT_TRANSFER: bank txn is paying a credit card, not the vendor. Those bills should be
      reclassed AP -> due-to-shareholder, and the bank txn should clear due-to-shareholder.
    - CC_PURCHASE: the bill was paid at the time of the CC purchase, not by bank.
    - SHAREHOLDER_REIMBURSE / E_TRANSFER_* reimbursements are handled elsewhere.
    """
    rows = conn.execute(
        """
        SELECT bank_txn_id, wave_bill_id, match_method
        FROM fresher_debits__wave_matches
        WHERE bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
          AND match_type IN (
            'PAD_INVOICE',
            'BILL_PAYMENT',
            'BANK_DEBIT',
            'SPLIT_PAYMENT',
            'VENDOR_ETRANSFER',
            'E_TRANSFER_VENDOR',
            'E_TRANSFER',
            'CHEQUE',
            'CASH_PAID'
          )
        ORDER BY CAST(bank_txn_id AS INTEGER) ASC, CAST(wave_bill_id AS INTEGER) ASC, CAST(id AS INTEGER) ASC
        """
    ).fetchall()
    grouped_raw: dict[str, list[tuple[str, int]]] = {}
    for r in rows:
        bank_id = str(r["bank_txn_id"]).strip()
        if not bank_id:
            continue
        bill_id = int(r["wave_bill_id"])
        method = str(r["match_method"] or "").strip().upper()
        grouped_raw.setdefault(bank_id, []).append((method, bill_id))

    grouped: dict[str, list[int]] = {}
    for bank_id, matches in grouped_raw.items():
        manual = [bid for method, bid in matches if method.startswith("MANUAL")]
        chosen = manual if manual else [bid for _, bid in matches]
        out: list[int] = []
        seen: set[int] = set()
        for bid in chosen:
            if bid in seen:
                continue
            seen.add(bid)
            out.append(bid)
        grouped[bank_id] = out

    return grouped


def fetch_split_payment_allocations(conn) -> list[tuple[str, int, int]]:
    """
    Returns rows of (bank_txn_id, wave_bill_id, amount_cents) derived from
    fresher_debits__split_payments where txn_type='BANK'.
    """
    rows = conn.execute(
        """
        SELECT txn_id AS bank_txn_id, wave_bill_id, amount_cents
        FROM fresher_debits__split_payments
        WHERE txn_type = 'BANK'
          AND txn_id IS NOT NULL AND TRIM(txn_id) <> ''
        ORDER BY CAST(txn_id AS INTEGER) ASC, CAST(wave_bill_id AS INTEGER) ASC
        """
    ).fetchall()
    out: list[tuple[str, int, int]] = []
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"]).strip()
        if not bank_txn_id:
            continue
        out.append((bank_txn_id, int(r["wave_bill_id"]), int(r["amount_cents"] or 0)))
    return out


def fetch_wave_bill_funding_allocations(conn) -> list[tuple[str, int, int]]:
    """
    Returns rows of (bank_txn_id, wave_bill_id, amount_cents) derived from
    fresher_debits__wave_bill_funding where bank_txn_id is present.
    """
    rows = conn.execute(
        """
        SELECT bank_txn_id, wave_bill_id, amount_cents
        FROM fresher_debits__wave_bill_funding
        WHERE bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        ORDER BY CAST(bank_txn_id AS INTEGER) ASC, CAST(wave_bill_id AS INTEGER) ASC
        """
    ).fetchall()
    out: list[tuple[str, int, int]] = []
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"]).strip()
        if not bank_txn_id:
            continue
        out.append((bank_txn_id, int(r["wave_bill_id"]), int(r["amount_cents"] or 0)))
    return out


def fetch_gfs_eft_notice_allocations(conn, *, start_date: str, end_date: str) -> list[tuple[str, int, int]]:
    """
    For GFS PAD debits, the EFT notice lines are authoritative about which invoices/credits
    make up the PAD amount. We use them as additional evidence, without mutating the frozen
    Fresher debits-side tables.

    Returns (bank_txn_id, wave_bill_id, amount_cents) for PAD debits only (credits-side amount_cents < 0),
    and only when the invoice number exists as a wave_bills row.
    """
    rows = conn.execute(
        """
        SELECT
          b.bank_txn_id AS bank_txn_id,
          wb.id AS wave_bill_id,
          CAST(nl.net_amount_cents AS INTEGER) AS amount_cents
        FROM fresher_credits__gfs_eft_bank_links l
        JOIN fresher_credits__credit_bank_items b ON b.id = l.bank_item_id
        JOIN fresher_credits__gfs_eft_notification_lines nl ON nl.notification_id = l.notification_id
        JOIN wave_bills wb ON wb.invoice_number = nl.invoice_number
        WHERE b.txn_date >= ? AND b.txn_date <= ?
          AND CAST(b.amount_cents AS INTEGER) < 0
        ORDER BY CAST(b.bank_txn_id AS INTEGER) ASC, CAST(wb.id AS INTEGER) ASC
        """,
        (start_date, end_date),
    ).fetchall()
    out: list[tuple[str, int, int]] = []
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"] or "").strip()
        if not bank_txn_id:
            continue
        out.append((bank_txn_id, int(r["wave_bill_id"]), int(r["amount_cents"] or 0)))
    return out


def fetch_bank_allocation_rows(conn) -> list[tuple[str, int, int]]:
    """
    Returns rows of (bank_txn_id, wave_bill_id, amount_cents) derived from
    fresher_debits__bank_allocations where target_type='WAVE_BILL'.
    """
    rows = conn.execute(
        """
        SELECT bank_txn_id, target_id AS wave_bill_id, amount_cents
        FROM fresher_debits__bank_allocations
        WHERE target_type = 'WAVE_BILL'
          AND bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        ORDER BY CAST(bank_txn_id AS INTEGER) ASC, CAST(target_id AS INTEGER) ASC
        """
    ).fetchall()
    out: list[tuple[str, int, int]] = []
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"]).strip()
        if not bank_txn_id:
            continue
        out.append((bank_txn_id, int(r["wave_bill_id"]), int(r["amount_cents"] or 0)))
    return out


def fetch_wave_bill_totals(conn) -> dict[int, int]:
    rows = conn.execute("SELECT id, total_cents FROM wave_bills").fetchall()
    return {int(r["id"]): int(r["total_cents"] or 0) for r in rows}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--bank-overrides", type=Path, default=DEFAULT_BANK_OVERRIDE_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing wave bill payment journal entries before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    accounts = cfg.get("accounts", {}) if isinstance(cfg.get("accounts"), dict) else {}
    bank_code = str(accounts.get("bank_account_code") or "1000").strip()
    ap_code = str(accounts.get("accounts_payable_code") or "2000").strip()
    source_cfg = (cfg.get("journal_sources") or {}).get("wave_bill_payment") if isinstance(cfg.get("journal_sources"), dict) else {}
    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "wave_bill_payment")
    entry_type = str((source_cfg or {}).get("entry_type") or "PAYMENT")

    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "wave_bill_payment_journal_summary.md"
    out_detail_csv = args.out_dir / "wave_bill_payment_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                """
                DELETE FROM journal_entries
                WHERE source_system = ? AND source_record_type = ?
                """,
                (source_system, source_record_type),
            )

        bank_txns = fetch_bank_txns(conn, start_date=start_date, end_date=end_date)
        bank_categories = fetch_bank_txn_categories(conn)
        bank_override_entries = load_bank_txn_category_override_entries(args.bank_overrides)
        bill_totals = fetch_wave_bill_totals(conn)

        allocations_by_bank: dict[str, dict[int, tuple[int, str]]] = {}

        def add_alloc(bank_txn_id: str, wave_bill_id: int, amount_cents: int, method: str) -> None:
            bank_txn_id = str(bank_txn_id or "").strip()
            if not bank_txn_id:
                return
            allocations_by_bank.setdefault(bank_txn_id, {})
            if wave_bill_id in allocations_by_bank[bank_txn_id]:
                return
            allocations_by_bank[bank_txn_id][wave_bill_id] = (int(amount_cents or 0), method)

        # Explicit evidence first (amount_cents provided):
        #
        # Important: when both SPLIT_PAYMENTS and WAVE_BILL_FUNDING exist for the same bank_txn,
        # prefer WAVE_BILL_FUNDING and ignore SPLIT_PAYMENTS. The snapshot can contain a few
        # split rows that were later superseded/corrected via wave_bill_funding, and keeping both
        # leads to double-linking (bank debit appears to pay two bills).
        funding_rows = list(fetch_wave_bill_funding_allocations(conn))
        funding_bank_ids = {str(bank_txn_id).strip() for bank_txn_id, _, _ in funding_rows if str(bank_txn_id).strip()}

        for bank_txn_id, wave_bill_id, amount_cents in fetch_split_payment_allocations(conn):
            if str(bank_txn_id).strip() in funding_bank_ids:
                continue
            add_alloc(bank_txn_id, wave_bill_id, amount_cents, "SPLIT_PAYMENTS")

        for bank_txn_id, wave_bill_id, amount_cents in funding_rows:
            add_alloc(bank_txn_id, wave_bill_id, amount_cents, "WAVE_BILL_FUNDING")

        for bank_txn_id, wave_bill_id, amount_cents in fetch_bank_allocation_rows(conn):
            add_alloc(bank_txn_id, wave_bill_id, amount_cents, "BANK_ALLOCATIONS")

        # Credits-side evidence: GFS EFT notice invoice lines (authoritative invoice list for GFS PADs).
        for bank_txn_id, wave_bill_id, amount_cents in fetch_gfs_eft_notice_allocations(conn, start_date=start_date, end_date=end_date):
            add_alloc(bank_txn_id, wave_bill_id, amount_cents, "GFS_EFT_NOTICE")

        # Fallback evidence (no explicit amount): use bill totals.
        match_groups = fetch_wave_match_groups(conn)
        for bank_id, bill_ids in match_groups.items():
            if bank_id in allocations_by_bank:
                continue
            for bid in bill_ids:
                add_alloc(bank_id, int(bid), bill_totals.get(int(bid), 0), "WAVE_MATCHES")

        detail_rows: list[dict[str, str]] = []
        skipped = 0
        skipped_reimbursement = 0
        skipped_cc_payment = 0
        inserted = 0
        mismatched = 0

        for bank_id, bill_map in sorted(allocations_by_bank.items(), key=lambda kv: int(kv[0]) if str(kv[0]).isdigit() else kv[0]):
            bank = bank_txns.get(bank_id)
            if not bank:
                skipped += 1
                continue

            if bank.debit_cents <= 0:
                skipped += 1
                continue

            if is_credit_card_payment(conn, bank_id):
                skipped_cc_payment += 1
                continue

            cat = bank_categories.get(bank_id, "")
            override = bank_override_entries.get(bank_id)
            if override:
                expected_date = str(override.get("txn_date") or "").strip()
                expected_debit = override.get("debit_cents")
                if (not expected_date or expected_date == bank.txn_date) and (
                    expected_debit is None or str(expected_debit).strip() == "" or int(expected_debit) == bank.debit_cents
                ):
                    cat = str(override.get("to_category") or cat).strip()

            if cat in ("REIMBURSEMENT", "RENT_REIMBURSEMENT", "HST_REIMBURSEMENT"):
                skipped_reimbursement += 1
                continue

            bill_ids = sorted(bill_map.keys())
            methods = sorted({bill_map[bid][1] for bid in bill_ids})

            raw_alloc_by_bill: dict[int, int] = {bid: int(bill_map[bid][0] or 0) for bid in bill_ids}
            raw_total = sum(raw_alloc_by_bill.values())
            bill_total_sum = sum(int(bill_totals.get(int(bid), 0)) for bid in bill_ids)

            # Some Fresher snapshot link tables record the *bank split amount* duplicated across each linked bill,
            # which makes raw_total = bank_amount * N. In those cases, bill totals often exactly sum to the bank debit
            # and should be used as the payment clearing basis.
            used_total = raw_total
            used_total_source = "ALLOCATED_AMOUNTS"
            if raw_total != bank.debit_cents and bill_total_sum == bank.debit_cents:
                used_total = bill_total_sum
                used_total_source = "BILL_TOTALS_OVERRIDE"

            diff = bank.debit_cents - used_total
            if diff != 0:
                mismatched += 1

            je_id = f"WAVE_BILL_PAYMENT_{bank_id}"
            description = f"Wave bill payment - bank txn {bank_id}"
            notes = (
                f"methods={','.join(methods)}; used_total_source={used_total_source}; "
                f"bank_txn_id={bank_id}; bill_ids={','.join(str(x) for x in bill_ids)}; "
                f"raw_allocated_total_cents={raw_total}; bill_total_sum_cents={bill_total_sum}; "
                f"used_bill_total_cents={used_total}; bank_debit_cents={bank.debit_cents}; diff_cents={diff}"
            )

            conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
            conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

            conn.execute(
                """
                INSERT INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id,
                  source_bank_line_id, notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    bank.txn_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    str(bank_id),
                    str(bank_id),
                    notes,
                ),
            )

            # If bank > used_total, do not over-clear AP. Put the remainder into prepaid until we
            # identify missing invoices/credits that make up the payment.
            line_number = 1
            ap_debit = bank.debit_cents
            remainder = 0
            prepaid_code = "1300"
            if diff > 0:
                ap_debit = used_total
                remainder = diff

            conn.execute(
                """
                INSERT INTO journal_entry_lines (
                  id, journal_entry_id, line_number,
                  account_code, debit_cents, credit_cents, description
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    f"{je_id}:{line_number}",
                    je_id,
                    line_number,
                    ap_code,
                    ap_debit,
                    0,
                    "Accounts payable cleared (wave bill payment)",
                ),
            )
            line_number += 1

            if remainder:
                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:{line_number}",
                        je_id,
                        line_number,
                        prepaid_code,
                        remainder,
                        0,
                        "Payment above matched bill totals (prepaid/unknown invoices)",
                    ),
                )
                line_number += 1

            conn.execute(
                """
                INSERT INTO journal_entry_lines (
                  id, journal_entry_id, line_number,
                  account_code, debit_cents, credit_cents, description
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    f"{je_id}:{line_number}",
                    je_id,
                    line_number,
                    bank_code,
                    0,
                    bank.debit_cents,
                    bank.description or "Bank payment",
                ),
            )

            inserted += 1
            detail_rows.append(
                {
                    "bank_txn_id": bank_id,
                    "bank_date": bank.txn_date,
                    "bank_debit_cents": str(bank.debit_cents),
                    "matched_wave_bill_ids": ",".join(str(x) for x in bill_ids),
                    "match_methods": ",".join(methods),
                    "matched_bill_total_cents": str(used_total),
                    "diff_cents": str(diff),
                    "journal_entry_id": je_id,
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "bank_txn_id",
                "bank_date",
                "bank_debit_cents",
                "matched_wave_bill_ids",
                "match_methods",
                "matched_bill_total_cents",
                "diff_cents",
                "journal_entry_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Wave bill payment journal summary\n\n")
            f.write(f"- Scope: {start_date} → {end_date}\n")
            f.write(f"- Bank txns with bill funding evidence: {len(allocations_by_bank)}\n")
            f.write(f"- Journal entries posted: {inserted}\n")
            f.write(f"- Skipped (bank txn not in scope): {skipped}\n")
            f.write(f"- Skipped reimbursements (handled elsewhere): {skipped_reimbursement}\n")
            f.write(f"- Skipped credit card payments (handled elsewhere): {skipped_cc_payment}\n")
            f.write(f"- Payments with bill total mismatch: {mismatched}\n")
            if detail_rows:
                f.write("\n## First few mismatches\n\n")
                shown = 0
                for row in detail_rows:
                    if row["diff_cents"] == "0":
                        continue
                    f.write(
                        f"- bank_txn_id {row['bank_txn_id']}: bank ${cents_to_dollars(int(row['bank_debit_cents']))} "
                        f"vs bills ${cents_to_dollars(int(row['matched_bill_total_cents']))} (diff ${cents_to_dollars(int(row['diff_cents']))})\n"
                    )
                    shown += 1
                    if shown >= 10:
                        break

        conn.commit()

    finally:
        conn.close()

    print("WAVE BILL PAYMENT JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {inserted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
