#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest


def parse_float(val: str | None) -> float:
    try:
        return float(val or 0)
    except ValueError:
        return 0.0


def cents_from_amount(amount_str: str | None) -> int:
    return int(round(parse_float(amount_str) * 100))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument(
        "--audit-dir",
        type=Path,
        default=PROJECT_ROOT
        / "data"
        / "fresher_snapshots"
        / "20260122-054642"
        / "fresher_reports"
        / "audits"
        / "20260115-161413_cc_chain_audit",
    )
    ap.add_argument("--reset", action="store_true", help="Delete previously inserted FIFO override rows (notes prefix).")
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    args = ap.parse_args()

    coverage_path = args.audit_dir / "dryrun_fifo_cc_payment_bank_to_wave_coverage.csv"
    alloc_path = args.audit_dir / "dryrun_fifo_cc_payment_bank_to_wave_allocations.csv"

    if not coverage_path.exists():
        raise SystemExit(f"Missing coverage file: {coverage_path}")
    if not alloc_path.exists():
        raise SystemExit(f"Missing allocations file: {alloc_path}")

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")
    start_date = min(fy.start_date for fy in fys)
    end_date = max(fy.end_date for fy in fys)

    # Bank txns with zero current coverage but FIFO suggests allocations.
    eligible_bank_txn_ids: set[str] = set()
    with coverage_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            bank_txn_id = (r.get("bank_txn_id") or "").strip()
            bank_date = (r.get("bank_date") or "").strip()
            if not bank_txn_id or not bank_date:
                continue
            if bank_date < start_date or bank_date > end_date:
                continue
            current_alloc = parse_float(r.get("current_allocated_to_wave"))
            fifo_alloc = parse_float(r.get("fifo_allocated_to_wave"))
            if current_alloc == 0 and fifo_alloc > 0:
                eligible_bank_txn_ids.add(bank_txn_id)

    if not eligible_bank_txn_ids:
        print("No eligible bank_txn_ids found for FIFO import.")
        return 0

    conn = connect_db(args.db)
    try:
        conn.execute("BEGIN")
        if args.reset:
            conn.execute(
                """
                DELETE FROM fresher_debits__bank_allocations
                WHERE notes LIKE 'FIFO_CC_CHAIN_OVERRIDE%'
                """
            )

        existing = set()
        rows = conn.execute(
            """
            SELECT bank_txn_id, target_id
            FROM fresher_debits__bank_allocations
            WHERE target_type = 'WAVE_BILL'
            """
        ).fetchall()
        for r in rows:
            existing.add((str(r["bank_txn_id"]).strip(), str(r["target_id"]).strip()))

        max_id_row = conn.execute(
            "SELECT MAX(CAST(id AS INTEGER)) AS max_id FROM fresher_debits__bank_allocations"
        ).fetchone()
        max_id = int(max_id_row["max_id"] or 0)

        inserted_rows: list[dict[str, str]] = []
        allocated_by_bank: dict[str, int] = defaultdict(int)

        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        with alloc_path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                bank_txn_id = (r.get("bank_txn_id") or "").strip()
                if bank_txn_id not in eligible_bank_txn_ids:
                    continue
                bank_date = (r.get("bank_date") or "").strip()
                if not bank_date or bank_date < start_date or bank_date > end_date:
                    continue
                wave_bill_id = (r.get("wave_bill_id") or "").strip()
                if not wave_bill_id:
                    continue
                key = (bank_txn_id, wave_bill_id)
                if key in existing:
                    continue

                amount_cents = cents_from_amount(r.get("allocated_amount"))
                if amount_cents <= 0:
                    continue

                max_id += 1
                notes = (
                    "FIFO_CC_CHAIN_OVERRIDE "
                    f"method={r.get('method')}; "
                    f"cc_purchase_txn_id={r.get('cc_purchase_txn_id')}; "
                    f"cc_purchase_date={r.get('cc_purchase_date')}; "
                    f"cc_purchase_amount={r.get('cc_purchase_amount')}"
                )

                conn.execute(
                    """
                    INSERT INTO fresher_debits__bank_allocations (
                        id, bank_txn_id, target_type, target_id, amount_cents, notes, created_at
                    ) VALUES (?, ?, 'WAVE_BILL', ?, ?, ?, ?)
                    """,
                    (str(max_id), bank_txn_id, wave_bill_id, str(amount_cents), notes, now),
                )

                allocated_by_bank[bank_txn_id] += amount_cents
                inserted_rows.append(
                    {
                        "bank_txn_id": bank_txn_id,
                        "bank_date": bank_date,
                        "wave_bill_id": wave_bill_id,
                        "allocated_cents": amount_cents,
                        "allocated_amount": f"{amount_cents/100:.2f}",
                        "method": r.get("method") or "",
                    }
                )

        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = args.out_dir / "cc_payment_fifo_allocations_imported.csv"
    out_md = args.out_dir / "cc_payment_fifo_allocations_imported.md"

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        if inserted_rows:
            writer = csv.DictWriter(f, fieldnames=list(inserted_rows[0].keys()))
            writer.writeheader()
            for row in inserted_rows:
                writer.writerow(row)

    lines = []
    lines.append("# FIFO CC payment allocations imported\n\n")
    lines.append(f"- Eligible bank_txn_ids (zero current coverage): {len(eligible_bank_txn_ids)}\n")
    lines.append(f"- Rows inserted: {len(inserted_rows)}\n\n")
    lines.append("bank_txn_id | allocated_total\n")
    lines.append("-|-\n")
    for bank_txn_id, cents in sorted(allocated_by_bank.items(), key=lambda x: -abs(x[1]))[:30]:
        lines.append(f"{bank_txn_id} | ${cents/100:.2f}\n")
    out_md.write_text("".join(lines), encoding="utf-8")

    print("FIFO CC payment allocations imported")
    print(f"- db: {args.db}")
    print(f"- inserted rows: {len(inserted_rows)}")
    print(f"- out: {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
