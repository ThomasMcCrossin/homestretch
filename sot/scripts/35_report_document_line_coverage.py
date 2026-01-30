#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from _lib import DB_PATH, SOT_ROOT, apply_migrations, connect_db


FY2024_START = "2023-06-01"
FY2025_END = "2025-05-31"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--output-dir", type=Path, default=SOT_ROOT / "output")
    args = ap.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_md = args.output_dir / "document_line_coverage_summary.md"
    out_csv = args.output_dir / "documents_missing_lines.csv"

    conn = connect_db(args.db)
    try:
        apply_migrations(conn)

        total_docs = conn.execute(
            "SELECT COUNT(*) AS n FROM documents WHERE doc_date >= ? AND doc_date <= ?",
            (FY2024_START, FY2025_END),
        ).fetchone()["n"]
        docs_with_lines = conn.execute(
            """
            SELECT COUNT(DISTINCT d.id) AS n
            FROM documents d
            JOIN document_lines dl ON dl.document_id=d.id
            WHERE d.doc_date >= ? AND d.doc_date <= ?
            """,
            (FY2024_START, FY2025_END),
        ).fetchone()["n"]

        missing_rows = conn.execute(
            """
            SELECT d.id AS document_id, d.doc_date, d.doc_type, d.total_cents, d.tax_cents, d.net_cents,
                   d.source_record_id, c.normalized_name AS counterparty
            FROM documents d
            LEFT JOIN counterparties c ON c.id=d.counterparty_id
            LEFT JOIN document_lines dl ON dl.document_id=d.id
            WHERE dl.id IS NULL
              AND d.doc_date >= ? AND d.doc_date <= ?
            ORDER BY d.doc_date, d.id
            """
            ,
            (FY2024_START, FY2025_END),
        ).fetchall()

        by_vendor_missing = conn.execute(
            """
            SELECT COALESCE(c.normalized_name, '(none)') AS vendor, COUNT(*) AS n, SUM(d.total_cents) AS total_cents
            FROM documents d
            LEFT JOIN counterparties c ON c.id=d.counterparty_id
            LEFT JOIN document_lines dl ON dl.document_id=d.id
            WHERE dl.id IS NULL
              AND d.doc_date >= ? AND d.doc_date <= ?
            GROUP BY vendor
            ORDER BY n DESC
            LIMIT 50
            """
            ,
            (FY2024_START, FY2025_END),
        ).fetchall()

        with out_md.open("w", encoding="utf-8") as f:
            f.write("# Document line coverage\n\n")
            f.write(f"- scope: {FY2024_START} → {FY2025_END}\n")
            f.write(f"- documents_total: {total_docs}\n")
            f.write(f"- documents_with_lines: {docs_with_lines}\n")
            f.write(f"- documents_missing_lines: {len(missing_rows)}\n\n")
            f.write("## Top vendors missing lines\n\n")
            f.write("| vendor | missing_docs | missing_total |\n")
            f.write("|---|---:|---:|\n")
            for r in by_vendor_missing:
                total = r["total_cents"]
                total_s = "" if total is None else f"{int(total) / 100:.2f}"
                f.write(f"| {r['vendor']} | {r['n']} | {total_s} |\n")

        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "document_id",
                    "doc_date",
                    "doc_type",
                    "counterparty",
                    "total_cents",
                    "tax_cents",
                    "net_cents",
                    "source_record_id",
                ]
            )
            for r in missing_rows:
                w.writerow(
                    [
                        r["document_id"],
                        r["doc_date"],
                        r["doc_type"],
                        r["counterparty"],
                        r["total_cents"],
                        r["tax_cents"],
                        r["net_cents"],
                        r["source_record_id"],
                    ]
                )
    finally:
        conn.close()

    print("DOCUMENT LINE COVERAGE REPORT WRITTEN")
    print(f"- md: {out_md}")
    print(f"- csv: {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
