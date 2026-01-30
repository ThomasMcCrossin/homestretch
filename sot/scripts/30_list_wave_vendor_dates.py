#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from _lib import DB_PATH, apply_migrations, connect_db


def parse_wave_bill_id(source_record_id: str) -> str | None:
    m = re.match(r"^fresher_debits__wave_bills:(.+)$", source_record_id or "")
    return m.group(1) if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--output", type=Path, default=DB_PATH.parent.parent / "output" / "wave_vendor_dates.csv")
    ap.add_argument(
        "--vendor",
        action="append",
        required=True,
        help="Case-insensitive substring match against Wave vendor_normalized.",
    )
    args = ap.parse_args()

    patterns = [v.strip().lower() for v in args.vendor if v.strip()]
    if not patterns:
        raise SystemExit("--vendor must be provided at least once")

    conn = connect_db(args.db)
    try:
        apply_migrations(conn)
        rows = conn.execute(
            """
            SELECT
              d.id AS document_id,
              d.doc_date,
              d.doc_number,
              d.total_cents,
              d.tax_cents,
              d.net_cents,
              d.source_record_id,
              c.name AS vendor_name,
              c.normalized_name AS vendor_norm,
              CASE
                WHEN EXISTS (
                  SELECT 1 FROM document_flags df
                  WHERE df.document_id=d.id AND df.flag='IGNORE'
                )
                THEN 1 ELSE 0
              END AS is_ignored
            FROM documents d
            JOIN counterparties c ON c.id=d.counterparty_id
            WHERE d.source_system='T2_FINAL_DB'
              AND d.source_record_id LIKE 'fresher_debits__wave_bills:%'
            ORDER BY d.doc_date, d.id
            """
        ).fetchall()
    finally:
        conn.close()

    filtered = []
    for r in rows:
        vendor_norm = (r["vendor_norm"] or "").lower()
        if any(p in vendor_norm for p in patterns):
            filtered.append(r)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "vendor",
                "doc_date",
                "doc_number",
                "total_cents",
                "tax_cents",
                "net_cents",
                "document_id",
                "wave_bill_id",
                "is_ignored",
                "vendor_normalized",
            ]
        )
        for r in filtered:
            w.writerow(
                [
                    r["vendor_name"],
                    r["doc_date"],
                    r["doc_number"],
                    r["total_cents"],
                    r["tax_cents"],
                    r["net_cents"],
                    r["document_id"],
                    parse_wave_bill_id(r["source_record_id"]),
                    r["is_ignored"],
                    r["vendor_norm"],
                ]
            )

    print("VENDOR DATES EXPORTED")
    print(f"- output: {args.output}")
    print(f"- rows: {len(filtered)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
