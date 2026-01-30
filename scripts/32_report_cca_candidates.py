#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from decimal import Decimal
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest


def cents_to_dollars(cents: int) -> str:
    return f"{Decimal(cents) / Decimal(100):.2f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--threshold", type=float, default=300.0, help="Minimum net amount in dollars to list as a candidate (default: 300).")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    scope_start = min(fy.start_date for fy in fys)
    scope_end = max(fy.end_date for fy in fys)
    threshold_cents = int(Decimal(str(args.threshold)) * Decimal(100))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = args.out_dir / "cca_candidates.csv"

    flag_account_codes = {"5300"}

    conn = connect_db(args.db)
    try:
        wave_rows = conn.execute(
            """
            SELECT id, invoice_date, vendor_raw, total_cents, tax_cents, net_cents
            FROM wave_bills
            WHERE invoice_date BETWEEN ? AND ?
              AND CAST(net_cents AS INTEGER) >= ?
            ORDER BY invoice_date, id
            """,
            (scope_start, scope_end, threshold_cents),
        ).fetchall()

        cc_rows = conn.execute(
            """
            SELECT je.id, je.entry_date, je.description,
                   SUM(CAST(jel.debit_cents AS INTEGER)) AS debit_cents
            FROM journal_entries je
            JOIN journal_entry_lines jel ON jel.journal_entry_id = je.id
            WHERE je.source_record_type = 'credit_card_purchases'
              AND je.entry_date BETWEEN ? AND ?
            GROUP BY je.id, je.entry_date, je.description
            HAVING SUM(CAST(jel.debit_cents AS INTEGER)) >= ?
            ORDER BY je.entry_date, je.id
            """,
            (scope_start, scope_end, threshold_cents),
        ).fetchall()

        with out_csv.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "source_type",
                    "record_id",
                    "date",
                    "vendor",
                    "total_cents",
                    "total_dollars",
                    "allocation_breakdown",
                    "flags",
                ]
            )

            for r in wave_rows:
                allocs = conn.execute(
                    """
                    SELECT account_code, SUM(CAST(amount_cents AS INTEGER)) AS amount_cents
                    FROM bill_allocations
                    WHERE wave_bill_id = ?
                    GROUP BY account_code
                    ORDER BY ABS(SUM(CAST(amount_cents AS INTEGER))) DESC
                    """,
                    (int(r["id"]),),
                ).fetchall()
                breakdown = "; ".join(f"{a['account_code']}:{a['amount_cents']}" for a in allocs if a["account_code"])

                flags = []
                if any(a["account_code"] in flag_account_codes for a in allocs if a["account_code"]):
                    flags.append("likely_equipment_account_code")
                vendor_raw = str(r["vendor_raw"] or "")
                if "nayax" in vendor_raw.lower():
                    flags.append("vendor_keyword:nayax")

                w.writerow(
                    [
                        "wave_bill",
                        r["id"],
                        r["invoice_date"],
                        vendor_raw,
                        int(r["net_cents"] or 0),
                        cents_to_dollars(int(r["net_cents"] or 0)),
                        breakdown,
                        ",".join(flags),
                    ]
                )

            for r in cc_rows:
                lines = conn.execute(
                    """
                    SELECT account_code, SUM(CAST(debit_cents AS INTEGER)) AS amount_cents
                    FROM journal_entry_lines
                    WHERE journal_entry_id = ?
                      AND CAST(debit_cents AS INTEGER) > 0
                    GROUP BY account_code
                    ORDER BY ABS(SUM(CAST(debit_cents AS INTEGER))) DESC
                    """,
                    (r["id"],),
                ).fetchall()
                breakdown = "; ".join(f"{a['account_code']}:{a['amount_cents']}" for a in lines if a["account_code"])

                flags = []
                if any(a["account_code"] in flag_account_codes for a in lines if a["account_code"]):
                    flags.append("likely_equipment_account_code")
                desc = str(r["description"] or "")
                if "nayax" in desc.lower():
                    flags.append("vendor_keyword:nayax")

                w.writerow(
                    [
                        "cc_purchase",
                        r["id"],
                        r["entry_date"],
                        desc,
                        int(r["debit_cents"] or 0),
                        cents_to_dollars(int(r["debit_cents"] or 0)),
                        breakdown,
                        ",".join(flags),
                    ]
                )
    finally:
        conn.close()

    print("CCA CANDIDATE REPORT BUILT")
    print(f"- out: {out_csv}")
    print(f"- threshold: ${args.threshold:.2f}")
    print(f"- scope: {scope_start} to {scope_end}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
