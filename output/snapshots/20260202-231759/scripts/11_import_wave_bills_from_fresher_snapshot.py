#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

from _lib import (
    DB_PATH,
    connect_db,
    fiscal_years_from_manifest,
    get_source,
    load_manifest,
    load_rules,
    match_vendor_key,
    normalize_vendor,
    sha256_file,
)


def ensure_source_file(conn: sqlite3.Connection, source_key: str, cfg: dict) -> int:
    conn.execute(
        """
        INSERT INTO source_files (source_key, kind, path, sha256, semantics)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(source_key) DO UPDATE SET
          kind=excluded.kind,
          path=excluded.path,
          sha256=excluded.sha256,
          semantics=excluded.semantics
        """,
        (
            source_key,
            str(cfg.get("kind") or ""),
            str(cfg.get("path") or ""),
            str(cfg.get("sha256") or ""),
            str(cfg.get("semantics") or ""),
        ),
    )
    conn.commit()
    row = conn.execute("SELECT id FROM source_files WHERE source_key = ?", (source_key,)).fetchone()
    return int(row["id"])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--source-key", default="fresher_debits_db_snapshot")
    ap.add_argument("--reset", action="store_true", help="Delete existing Wave bills and allocations before import.")
    ap.add_argument("--start-date", default=None, help="Inclusive YYYY-MM-DD (default: manifest FY min start).")
    ap.add_argument("--end-date", default=None, help="Inclusive YYYY-MM-DD (default: manifest FY max end).")
    ap.add_argument("--all", action="store_true", help="Import all rows (ignore date filter).")
    args = ap.parse_args()

    manifest = load_manifest()
    rules = load_rules()

    fys = fiscal_years_from_manifest(manifest)
    default_start = min((fy.start_date for fy in fys), default=None)
    default_end = max((fy.end_date for fy in fys), default=None)

    start_date = args.start_date or default_start
    end_date = args.end_date or default_end

    src = get_source(manifest, args.source_key)
    path = Path(str(src["path"]))
    if not path.exists():
        raise SystemExit(f"Missing source file: {path}")

    sha_expected = str(src.get("sha256") or "").strip()
    if sha_expected:
        sha_actual = sha256_file(path)
        if sha_actual != sha_expected:
            raise SystemExit(f"sha256 mismatch for {path}: expected {sha_expected} actual {sha_actual}")

    fresher = sqlite3.connect(path)
    fresher.row_factory = sqlite3.Row

    conn = connect_db(args.db)
    try:
        source_file_id = ensure_source_file(conn, args.source_key, src)

        if args.reset:
            conn.execute("DELETE FROM bill_allocations")
            conn.execute("DELETE FROM bill_detail_links")
            conn.execute("DELETE FROM wave_bills")
            conn.commit()

        if args.all:
            query = """
              SELECT
                id,
                invoice_date,
                vendor_raw,
                vendor_normalized,
                vendor_category,
                total_cents,
                tax_cents,
                net_cents,
                invoice_number,
                source_row
              FROM wave_bills
              ORDER BY id
            """
            params: tuple[str, ...] = ()
        else:
            if not start_date or not end_date:
                raise SystemExit(
                    "Missing start/end date filter. Either add fiscal_years to manifest, "
                    "pass --start-date/--end-date, or use --all."
                )
            query = """
              SELECT
                id,
                invoice_date,
                vendor_raw,
                vendor_normalized,
                vendor_category,
                total_cents,
                tax_cents,
                net_cents,
                invoice_number,
                source_row
              FROM wave_bills
              WHERE invoice_date >= ? AND invoice_date <= ?
              ORDER BY id
            """
            params = (str(start_date), str(end_date))

        rows = fresher.execute(query, params).fetchall()

        inserted = 0
        for r in rows:
            fresher_id = int(r["id"])
            invoice_date = (r["invoice_date"] or "").strip()
            vendor_raw = (r["vendor_raw"] or "").strip()
            vendor_norm = (r["vendor_normalized"] or "").strip() or normalize_vendor(vendor_raw)
            vendor_key = match_vendor_key(vendor_raw, rules)
            vendor_category = (r["vendor_category"] or "").strip() or None

            total_cents = int(r["total_cents"] or 0)
            tax_cents = int(r["tax_cents"] or 0)
            net_cents = int(r["net_cents"] or 0)
            invoice_number = (r["invoice_number"] or "").strip() or None
            source_row = int(r["source_row"]) if r["source_row"] is not None else None

            conn.execute(
                """
                INSERT INTO wave_bills
                  (id, invoice_date, vendor_raw, vendor_norm, vendor_key, vendor_category,
                   invoice_number, total_cents, tax_cents, net_cents, source_file_id, source_row,
                   source_system, source_record_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    fresher_id,
                    invoice_date,
                    vendor_raw,
                    vendor_norm,
                    vendor_key,
                    vendor_category,
                    invoice_number,
                    total_cents,
                    tax_cents,
                    net_cents,
                    source_file_id,
                    source_row,
                    "FRESHER",
                    str(fresher_id),
                ),
            )
            inserted += 1

        conn.commit()

    finally:
        conn.close()
        fresher.close()

    print("FRESHER WAVE BILL IMPORT COMPLETE")
    print(f"- db: {args.db}")
    print(f"- source: {path}")
    if args.all:
        print("- scope: all")
    else:
        print(f"- scope: {start_date} → {end_date}")
    print(f"- rows inserted: {inserted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
