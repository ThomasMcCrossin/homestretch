#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, load_yaml


DEFAULT_FIXES_PATH = PROJECT_ROOT / "overrides" / "data_fixes.yml"
MANUAL_MATCH_METHOD = "T2_FINAL_MANUAL_CC_PAYMENT_TRANSFER_OVERRIDE"


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def next_wave_match_id_start(conn) -> int:
    row = conn.execute("SELECT MAX(CAST(id AS INTEGER)) AS max_id FROM fresher_debits__wave_matches").fetchone()
    return int(row["max_id"] or 0)


@dataclass(frozen=True)
class DeleteCounts:
    bill_allocations: int
    wave_matches: int
    split_payments: int
    wave_bill_funding: int
    bank_allocations: int
    journal_entries: int
    journal_entry_lines: int


def delete_wave_bill(conn, wave_bill_id: int) -> DeleteCounts:
    # bill_allocations
    row = conn.execute("SELECT COUNT(*) AS n FROM bill_allocations WHERE wave_bill_id = ?", (wave_bill_id,)).fetchone()
    bill_alloc_n = int(row["n"] or 0)
    conn.execute("DELETE FROM bill_allocations WHERE wave_bill_id = ?", (wave_bill_id,))

    # wave match/link tables
    row = conn.execute(
        "SELECT COUNT(*) AS n FROM fresher_debits__wave_matches WHERE CAST(wave_bill_id AS INTEGER) = ?",
        (wave_bill_id,),
    ).fetchone()
    wave_matches_n = int(row["n"] or 0)
    conn.execute("DELETE FROM fresher_debits__wave_matches WHERE CAST(wave_bill_id AS INTEGER) = ?", (wave_bill_id,))

    row = conn.execute(
        "SELECT COUNT(*) AS n FROM fresher_debits__split_payments WHERE CAST(wave_bill_id AS INTEGER) = ?",
        (wave_bill_id,),
    ).fetchone()
    split_payments_n = int(row["n"] or 0)
    conn.execute("DELETE FROM fresher_debits__split_payments WHERE CAST(wave_bill_id AS INTEGER) = ?", (wave_bill_id,))

    row = conn.execute(
        "SELECT COUNT(*) AS n FROM fresher_debits__wave_bill_funding WHERE CAST(wave_bill_id AS INTEGER) = ?",
        (wave_bill_id,),
    ).fetchone()
    wave_bill_funding_n = int(row["n"] or 0)
    conn.execute("DELETE FROM fresher_debits__wave_bill_funding WHERE CAST(wave_bill_id AS INTEGER) = ?", (wave_bill_id,))

    row = conn.execute(
        """
        SELECT COUNT(*) AS n
        FROM fresher_debits__bank_allocations
        WHERE target_type = 'WAVE_BILL' AND CAST(target_id AS INTEGER) = ?
        """,
        (wave_bill_id,),
    ).fetchone()
    bank_alloc_n = int(row["n"] or 0)
    conn.execute(
        """
        DELETE FROM fresher_debits__bank_allocations
        WHERE target_type = 'WAVE_BILL' AND CAST(target_id AS INTEGER) = ?
        """,
        (wave_bill_id,),
    )

    # journal entries that cite this bill (any type)
    jids = [
        str(r["id"])
        for r in conn.execute(
            """
            SELECT id
            FROM journal_entries
            WHERE source_bill_id = ?
               OR (source_record_id = ? AND source_record_type IN ('wave_bill_accrual', 'wave_bill_cc_settlement'))
            """,
            (str(wave_bill_id), str(wave_bill_id)),
        ).fetchall()
    ]
    journal_entries_n = len(jids)
    journal_entry_lines_n = 0
    if jids:
        row = conn.execute(
            f"SELECT COUNT(*) AS n FROM journal_entry_lines WHERE journal_entry_id IN ({','.join('?' for _ in jids)})",
            tuple(jids),
        ).fetchone()
        journal_entry_lines_n = int(row["n"] or 0)
        conn.execute(
            f"DELETE FROM journal_entry_lines WHERE journal_entry_id IN ({','.join('?' for _ in jids)})",
            tuple(jids),
        )
        conn.execute(
            f"DELETE FROM journal_entries WHERE id IN ({','.join('?' for _ in jids)})",
            tuple(jids),
        )

    # finally the wave bill itself
    conn.execute("DELETE FROM wave_bills WHERE id = ?", (wave_bill_id,))

    return DeleteCounts(
        bill_allocations=bill_alloc_n,
        wave_matches=wave_matches_n,
        split_payments=split_payments_n,
        wave_bill_funding=wave_bill_funding_n,
        bank_allocations=bank_alloc_n,
        journal_entries=journal_entries_n,
        journal_entry_lines=journal_entry_lines_n,
    )


def dedupe_bank_allocations(conn) -> int:
    """
    Delete exact duplicates in fresher_debits__bank_allocations:
      (target_type, bank_txn_id, target_id, amount_cents) duplicates.

    Keeps the lowest integer id when possible; otherwise keeps the earliest created_at.
    """
    rows = conn.execute(
        """
        SELECT
          bank_txn_id,
          target_type,
          target_id,
          amount_cents,
          COUNT(*) AS n
        FROM fresher_debits__bank_allocations
        GROUP BY bank_txn_id, target_type, target_id, amount_cents
        HAVING COUNT(*) > 1
        """
    ).fetchall()

    deleted = 0
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"] or "").strip()
        target_type = str(r["target_type"] or "").strip()
        target_id = str(r["target_id"] or "").strip()
        amount_cents = str(r["amount_cents"] or "").strip()
        if not (bank_txn_id and target_type and target_id and amount_cents):
            continue

        dups = conn.execute(
            """
            SELECT id, created_at
            FROM fresher_debits__bank_allocations
            WHERE bank_txn_id = ?
              AND target_type = ?
              AND target_id = ?
              AND amount_cents = ?
            """,
            (bank_txn_id, target_type, target_id, amount_cents),
        ).fetchall()
        if len(dups) <= 1:
            continue

        def sort_key(row) -> tuple[int, str]:
            # Prefer numeric id ordering; fall back to created_at.
            try:
                return (int(str(row["id"])), str(row["created_at"] or ""))
            except ValueError:
                return (10**18, str(row["created_at"] or ""))

        dups_sorted = sorted(dups, key=sort_key)
        keep_id = str(dups_sorted[0]["id"])
        delete_ids = [str(x["id"]) for x in dups_sorted[1:]]

        conn.execute(
            f"DELETE FROM fresher_debits__bank_allocations WHERE id IN ({','.join('?' for _ in delete_ids)})",
            tuple(delete_ids),
        )
        deleted += len(delete_ids)

        # Sanity: ensure we still have the kept row.
        still = conn.execute(
            "SELECT COUNT(*) AS n FROM fresher_debits__bank_allocations WHERE id = ?",
            (keep_id,),
        ).fetchone()
        if int(still["n"] or 0) != 1:
            raise RuntimeError(
                f"Deduplication failed for bank_allocations key: {bank_txn_id=} {target_type=} {target_id=} {amount_cents=}"
            )

    return deleted


def add_cc_payment_transfer_link(
    conn,
    *,
    wave_match_id: str,
    bank_txn_id: str,
    wave_bill_id: int,
    reason: str,
) -> tuple[str, str, str]:
    bank = conn.execute(
        """
        SELECT txn_date, CAST(debit_cents AS INTEGER) AS debit_cents, txn_type, used
        FROM fresher_debits__bank_transactions
        WHERE id = ?
        """,
        (str(bank_txn_id),),
    ).fetchone()
    if not bank:
        raise ValueError(f"Missing bank_txn_id={bank_txn_id}")
    if str(bank["txn_type"] or "").strip() != "CC_PAYMENT":
        raise ValueError(f"bank_txn_id={bank_txn_id} is not txn_type=CC_PAYMENT")
    if str(bank["used"] or "").strip() != "1":
        raise ValueError(f"bank_txn_id={bank_txn_id} is not used=1 (out of scope)")

    bill = conn.execute(
        "SELECT invoice_date, vendor_raw, total_cents FROM wave_bills WHERE id = ?",
        (int(wave_bill_id),),
    ).fetchone()
    if not bill:
        raise ValueError(f"Missing wave_bill_id={wave_bill_id}")

    bank_date = str(bank["txn_date"] or "")
    invoice_date = str(bill["invoice_date"] or "")
    bank_amt = int(bank["debit_cents"] or 0)
    bill_total = int(bill["total_cents"] or 0)

    bdate = parse_iso(bank_date)
    idate = parse_iso(invoice_date)
    date_diff_days = ""
    if bdate and idate:
        date_diff_days = str((bdate - idate).days)

    amount_diff_cents = str(bank_amt - bill_total)

    # Optional cc_txn_id: if the bill has a CC_PURCHASE match, carry it through (helps auditability).
    cc_txn_row = conn.execute(
        """
        SELECT cc_txn_id
        FROM fresher_debits__wave_matches
        WHERE match_type = 'CC_PURCHASE'
          AND CAST(wave_bill_id AS INTEGER) = ?
          AND cc_txn_id IS NOT NULL AND TRIM(cc_txn_id) <> ''
        ORDER BY CAST(id AS INTEGER) ASC
        LIMIT 1
        """,
        (int(wave_bill_id),),
    ).fetchone()
    cc_txn_id = str(cc_txn_row["cc_txn_id"] or "").strip() if cc_txn_row else ""

    existing = conn.execute(
        """
        SELECT 1
        FROM fresher_debits__wave_matches
        WHERE match_type = 'CC_PAYMENT_TRANSFER'
          AND CAST(wave_bill_id AS INTEGER) = ?
          AND bank_txn_id = ?
        LIMIT 1
        """,
        (int(wave_bill_id), str(bank_txn_id)),
    ).fetchone()
    if existing:
        return ("skipped_exists", bank_date, invoice_date)

    notes = (
        "t2-final manual CC_PAYMENT_TRANSFER override; "
        f"bank_txn_id={bank_txn_id}; bank_date={bank_date}; bank_amount_cents={bank_amt}; "
        f"wave_bill_id={wave_bill_id}; invoice_date={invoice_date}; vendor_raw={str(bill['vendor_raw'] or '')}; "
        f"reason={reason}"
    )
    conn.execute(
        """
        INSERT INTO fresher_debits__wave_matches (
          id, wave_bill_id, match_type,
          bank_txn_id, cc_txn_id, cc_payment_txn_id,
          confidence, match_method,
          date_diff_days, amount_diff_cents, notes
        ) VALUES (?, ?, 'CC_PAYMENT_TRANSFER', ?, ?, ?, 'HIGH', ?, ?, ?, ?)
        """,
        (
            str(wave_match_id),
            str(int(wave_bill_id)),
            str(bank_txn_id),
            cc_txn_id,
            str(bank_txn_id),
            MANUAL_MATCH_METHOD,
            date_diff_days,
            amount_diff_cents,
            notes,
        ),
    )

    # Return for reporting
    return ("inserted", bank_date, invoice_date)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--fixes", type=Path, default=DEFAULT_FIXES_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--dry-run", action="store_true", help="Compute actions but do not write to DB.")
    args = ap.parse_args()

    fixes = load_yaml(args.fixes)
    if int(fixes.get("version") or 0) != 1:
        raise SystemExit(f"Unsupported fixes version in {args.fixes}")

    deletes = fixes.get("wave_bills_delete") or []
    adds = fixes.get("cc_payment_transfer_add") or []
    dedupe = bool(fixes.get("dedupe_bank_allocations"))

    if deletes and not isinstance(deletes, list):
        raise SystemExit("wave_bills_delete must be a list")
    if adds and not isinstance(adds, list):
        raise SystemExit("cc_payment_transfer_add must be a list")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_md = args.out_dir / "data_fixes_applied.md"
    out_csv = args.out_dir / "data_fixes_applied.csv"

    conn = connect_db(args.db)
    try:
        conn.execute("BEGIN")

        deleted_alloc_dupes = 0
        if dedupe:
            deleted_alloc_dupes = dedupe_bank_allocations(conn)

        delete_results: list[dict[str, str]] = []
        for item in deletes:
            if not isinstance(item, dict):
                continue
            wave_bill_id = int(item.get("wave_bill_id") or 0)
            reason = str(item.get("reason") or "").strip()
            if wave_bill_id <= 0:
                continue

            exists = conn.execute("SELECT 1 FROM wave_bills WHERE id = ?", (wave_bill_id,)).fetchone()
            if not exists:
                delete_results.append(
                    {
                        "action": "wave_bill_delete",
                        "wave_bill_id": str(wave_bill_id),
                        "status": "skipped_missing",
                        "reason": reason,
                    }
                )
                continue

            counts = delete_wave_bill(conn, wave_bill_id)
            delete_results.append(
                {
                    "action": "wave_bill_delete",
                    "wave_bill_id": str(wave_bill_id),
                    "status": "deleted",
                    "reason": reason,
                    "bill_allocations_deleted": str(counts.bill_allocations),
                    "wave_matches_deleted": str(counts.wave_matches),
                    "split_payments_deleted": str(counts.split_payments),
                    "wave_bill_funding_deleted": str(counts.wave_bill_funding),
                    "bank_allocations_deleted": str(counts.bank_allocations),
                    "journal_entries_deleted": str(counts.journal_entries),
                    "journal_entry_lines_deleted": str(counts.journal_entry_lines),
                }
            )

        max_match_id = next_wave_match_id_start(conn)
        add_results: list[dict[str, str]] = []
        for item in adds:
            if not isinstance(item, dict):
                continue
            bank_txn_id = str(item.get("bank_txn_id") or "").strip()
            wave_bill_id = int(item.get("wave_bill_id") or 0)
            reason = str(item.get("reason") or "").strip()
            if not bank_txn_id or wave_bill_id <= 0:
                continue

            max_match_id += 1
            status, bank_date, invoice_date = add_cc_payment_transfer_link(
                conn,
                wave_match_id=str(max_match_id),
                bank_txn_id=bank_txn_id,
                wave_bill_id=wave_bill_id,
                reason=reason,
            )
            add_results.append(
                {
                    "action": "cc_payment_transfer_add",
                    "bank_txn_id": bank_txn_id,
                    "wave_bill_id": str(wave_bill_id),
                    "status": status,
                    "bank_date": bank_date,
                    "invoice_date": invoice_date,
                    "reason": reason,
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

    # Write report outputs
    rows_for_csv = []
    rows_for_csv.extend(delete_results)
    rows_for_csv.extend(add_results)

    if rows_for_csv:
        fieldnames = sorted({k for r in rows_for_csv for k in r.keys()})
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for r in rows_for_csv:
                w.writerow(r)

    lines: list[str] = []
    lines.append("# Data fixes applied\n\n")
    lines.append(f"- fixes_file: {args.fixes}\n")
    lines.append(f"- dry_run: {1 if args.dry_run else 0}\n")
    lines.append(f"- dedupe_bank_allocations_deleted_rows: {deleted_alloc_dupes}\n\n")

    lines.append("## Wave bill deletions\n\n")
    if delete_results:
        for r in delete_results:
            status = r.get("status")
            wid = r.get("wave_bill_id")
            reason = (r.get("reason") or "").strip()
            if status == "deleted":
                lines.append(
                    f"- wave_bill_id {wid}: deleted "
                    f"(bill_alloc={r.get('bill_allocations_deleted')}, "
                    f"wave_matches={r.get('wave_matches_deleted')}, "
                    f"split_payments={r.get('split_payments_deleted')}, "
                    f"funding={r.get('wave_bill_funding_deleted')}, "
                    f"bank_alloc={r.get('bank_allocations_deleted')}, "
                    f"journal_entries={r.get('journal_entries_deleted')}) — {reason}\n"
                )
            else:
                lines.append(f"- wave_bill_id {wid}: {status} — {reason}\n")
    else:
        lines.append("- (none)\n")

    lines.append("\n## CC payment transfer links added\n\n")
    if add_results:
        for r in add_results:
            lines.append(
                f"- bank_txn_id {r.get('bank_txn_id')} → wave_bill_id {r.get('wave_bill_id')}: {r.get('status')} "
                f"(bank_date={r.get('bank_date')}, invoice_date={r.get('invoice_date')}) — {r.get('reason')}\n"
            )
    else:
        lines.append("- (none)\n")

    lines.append("\nOutputs:\n\n")
    lines.append(f"- {out_md}\n")
    if rows_for_csv:
        lines.append(f"- {out_csv}\n")

    out_md.write_text("".join(lines), encoding="utf-8")

    print("DATA FIXES COMPLETE")
    print(f"- out: {out_md}")
    if rows_for_csv:
        print(f"- out_csv: {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
