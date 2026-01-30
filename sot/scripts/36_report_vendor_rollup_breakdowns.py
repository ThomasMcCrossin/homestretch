#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from _lib import DB_PATH, SOT_ROOT, apply_migrations, connect_db


DEFAULT_VENDORS = [
    "costco bill",
    "walmart bill",
    "canadian tire bill",
    "pharmasave bill",
    "atlantic superstore bill",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--output", type=Path, default=SOT_ROOT / "output" / "vendor_rollup_breakdowns.md")
    ap.add_argument("--vendor", action="append", default=[], help="counterparties.normalized_name value")
    args = ap.parse_args()

    vendors = [v.strip().lower() for v in args.vendor if v.strip()] or DEFAULT_VENDORS
    args.output.parent.mkdir(parents=True, exist_ok=True)

    conn = connect_db(args.db)
    try:
        apply_migrations(conn)

        with args.output.open("w", encoding="utf-8") as f:
            f.write("# Vendor rollup breakdowns\n\n")
            f.write("This report summarizes `document_lines` aggregated into `account_rollups`.\n\n")

            for vendor in vendors:
                bills = conn.execute(
                    """
                    SELECT COUNT(*) AS n, SUM(d.total_cents) AS total_cents
                    FROM documents d
                    JOIN counterparties c ON c.id=d.counterparty_id
                    WHERE c.normalized_name=?
                    """,
                    (vendor,),
                ).fetchone()
                n_bills = int(bills["n"])
                total_cents = bills["total_cents"]
                total_cents_int = int(total_cents) if total_cents is not None else 0

                f.write(f"## {vendor}\n\n")
                f.write(f"- bills: {n_bills}\n")
                f.write(f"- total: {total_cents_int / 100:.2f}\n\n")

                if n_bills == 0:
                    continue

                rollups = conn.execute(
                    """
                    SELECT COALESCE(arm.rollup_code,'(unmapped)') AS rollup_code,
                           COALESCE(ar.rollup_name,'(unmapped)') AS rollup_name,
                           SUM(dl.amount_cents) AS cents
                    FROM documents d
                    JOIN counterparties c ON c.id=d.counterparty_id
                    JOIN document_lines dl ON dl.document_id=d.id
                    LEFT JOIN account_rollup_members arm ON arm.account_code=dl.account_code
                    LEFT JOIN account_rollups ar ON ar.rollup_code=arm.rollup_code
                    WHERE c.normalized_name=?
                    GROUP BY COALESCE(arm.rollup_code,'(unmapped)'), COALESCE(ar.rollup_name,'(unmapped)')
                    ORDER BY ABS(cents) DESC
                    """,
                    (vendor,),
                ).fetchall()

                f.write("| rollup | amount | % of total |\n")
                f.write("|---|---:|---:|\n")
                for r in rollups:
                    cents = int(r["cents"]) if r["cents"] is not None else 0
                    pct = (cents / total_cents_int * 100) if total_cents_int else 0
                    f.write(f"| {r['rollup_code']} — {r['rollup_name']} | {cents / 100:.2f} | {pct:.2f}% |\n")
                f.write("\n")

                top_accounts = conn.execute(
                    """
                    SELECT dl.account_code, COALESCE(coa.account_name,'') AS account_name, SUM(dl.amount_cents) AS cents
                    FROM documents d
                    JOIN counterparties c ON c.id=d.counterparty_id
                    JOIN document_lines dl ON dl.document_id=d.id
                    LEFT JOIN chart_of_accounts coa ON coa.account_code=dl.account_code
                    WHERE c.normalized_name=?
                    GROUP BY dl.account_code, account_name
                    ORDER BY ABS(cents) DESC
                    LIMIT 12
                    """,
                    (vendor,),
                ).fetchall()
                f.write("Top accounts:\n\n")
                f.write("| account_code | amount | name |\n")
                f.write("|---:|---:|---|\n")
                for r in top_accounts:
                    cents = int(r["cents"]) if r["cents"] is not None else 0
                    f.write(f"| {r['account_code']} | {cents / 100:.2f} | {r['account_name']} |\n")
                f.write("\n")

    finally:
        conn.close()

    print("VENDOR ROLLUP REPORT WRITTEN")
    print(f"- md: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
