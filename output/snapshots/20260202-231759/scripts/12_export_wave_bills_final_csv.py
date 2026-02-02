#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from decimal import Decimal
from pathlib import Path

from _lib import fiscal_years_from_manifest, get_source, load_manifest, sha256_file


def cents_to_dollars_str(cents: int) -> str:
    return f"{(Decimal(cents) / Decimal(100)):.2f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-key", default="fresher_debits_db_snapshot")
    ap.add_argument("--start-date", default=None, help="Inclusive YYYY-MM-DD (default: manifest FY min start).")
    ap.add_argument("--end-date", default=None, help="Inclusive YYYY-MM-DD (default: manifest FY max end).")
    ap.add_argument("--all", action="store_true", help="Export all rows (ignore date filter).")
    ap.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "wave" / "wave_bills_final.csv",
    )
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    default_start = min((fy.start_date for fy in fys), default=None)
    default_end = max((fy.end_date for fy in fys), default=None)

    start_date = args.start_date or default_start
    end_date = args.end_date or default_end

    src = get_source(manifest, args.source_key)
    db_path = Path(str(src.get("path") or "")).expanduser()
    if not db_path.exists():
        raise SystemExit(f"Missing source DB: {db_path}")

    if not args.all and (not start_date or not end_date):
        raise SystemExit(
            "Missing start/end date filter. Either add fiscal_years to manifest, "
            "pass --start-date/--end-date, or use --all."
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        if args.all:
            query = """
              SELECT
                id,
                invoice_date,
                vendor_raw,
                invoice_number,
                vendor_category,
                total_cents,
                tax_cents,
                net_cents,
                source_row
              FROM wave_bills
              ORDER BY invoice_date, id
            """
            params: tuple[str, ...] = ()
        else:
            query = """
              SELECT
                id,
                invoice_date,
                vendor_raw,
                invoice_number,
                vendor_category,
                total_cents,
                tax_cents,
                net_cents,
                source_row
              FROM wave_bills
              WHERE invoice_date >= ? AND invoice_date <= ?
              ORDER BY invoice_date, id
            """
            params = (str(start_date), str(end_date))

        rows = conn.execute(query, params).fetchall()
    finally:
        conn.close()

    with args.out.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "fresher_wave_bill_id",
                "invoice_date",
                "vendor_raw",
                "invoice_number",
                "vendor_category",
                "total_amount",
                "tax_amount",
                "net_amount",
                "source_row",
            ]
        )
        for r in rows:
            w.writerow(
                [
                    int(r["id"]),
                    r["invoice_date"],
                    r["vendor_raw"],
                    (r["invoice_number"] or ""),
                    (r["vendor_category"] or ""),
                    cents_to_dollars_str(int(r["total_cents"] or 0)),
                    cents_to_dollars_str(int(r["tax_cents"] or 0)),
                    cents_to_dollars_str(int(r["net_cents"] or 0)),
                    "" if r["source_row"] is None else int(r["source_row"]),
                ]
            )

    print("WAVE BILLS FINAL CSV EXPORTED")
    print(f"- source_db: {db_path}")
    print(f"- out: {args.out}")
    print(f"- rows: {len(rows)}")
    if args.all:
        print("- filter: ALL")
    else:
        print(f"- filter: invoice_date between {start_date} and {end_date}")
    print(f"- sha256: {sha256_file(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
