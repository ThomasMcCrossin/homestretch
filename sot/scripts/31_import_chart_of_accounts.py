#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, SOT_ROOT, apply_migrations, connect_db


def _parse_bool(v: str | None) -> int | None:
    if v is None:
        return None
    s = str(v).strip().lower()
    if not s:
        return None
    if s in {"1", "true", "t", "yes", "y"}:
        return 1
    if s in {"0", "false", "f", "no", "n"}:
        return 0
    raise ValueError(f"Unrecognized boolean value: {v!r}")


def _norm(v: str | None) -> str | None:
    if v is None:
        return None
    s = str(v).strip()
    return s or None


@dataclass(frozen=True)
class UpsertStats:
    rows_processed: int = 0
    rows_upserted: int = 0


def default_chart_csv() -> Path:
    project_root = SOT_ROOT.parent
    exports_dir = project_root / "data" / "curlys_books_exports"
    if not exports_dir.exists():
        raise FileNotFoundError(f"curlys-books exports directory not found: {exports_dir}")
    candidates = sorted([p for p in exports_dir.iterdir() if p.is_dir()])
    if not candidates:
        raise FileNotFoundError(f"No exports found in: {exports_dir}")
    latest = candidates[-1]
    csv_path = latest / "chart_of_accounts.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"chart_of_accounts.csv not found in: {latest}")
    return csv_path


def upsert_chart_of_accounts(conn: sqlite3.Connection, csv_path: Path) -> UpsertStats:
    stats = UpsertStats()
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            stats = UpsertStats(rows_processed=stats.rows_processed + 1, rows_upserted=stats.rows_upserted)
            account_code = _norm(row.get("account_code"))
            account_name = _norm(row.get("account_name"))
            if not account_code or not account_name:
                continue

            account_type = _norm(row.get("account_type"))
            parent_code = _norm(row.get("parent_code"))
            gifi_code = _norm(row.get("gifi_code"))
            t2125_line = _norm(row.get("t2125_line"))
            is_active = _parse_bool(row.get("is_active"))
            requires_receipt = _parse_bool(row.get("requires_receipt"))
            is_tax_account = _parse_bool(row.get("is_tax_account"))

            conn.execute(
                """
                INSERT INTO chart_of_accounts(
                  account_code, account_name, account_type, gifi_code,
                  parent_code, t2125_line, is_active, requires_receipt, is_tax_account
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(account_code) DO UPDATE SET
                  account_name=excluded.account_name,
                  account_type=excluded.account_type,
                  gifi_code=excluded.gifi_code,
                  parent_code=excluded.parent_code,
                  t2125_line=excluded.t2125_line,
                  is_active=excluded.is_active,
                  requires_receipt=excluded.requires_receipt,
                  is_tax_account=excluded.is_tax_account
                """,
                (
                    account_code,
                    account_name,
                    account_type,
                    gifi_code,
                    parent_code,
                    t2125_line,
                    is_active,
                    requires_receipt,
                    is_tax_account,
                ),
            )
            stats = UpsertStats(rows_processed=stats.rows_processed, rows_upserted=stats.rows_upserted + 1)
    return stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--csv", type=Path, default=None, help="Path to curlys-books chart_of_accounts.csv")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    csv_path = args.csv or default_chart_csv()

    conn = connect_db(args.db)
    try:
        apply_migrations(conn)
        conn.execute("BEGIN")
        stats = upsert_chart_of_accounts(conn, csv_path)
        if args.dry_run:
            conn.rollback()
        else:
            conn.commit()
    finally:
        conn.close()

    print("CHART OF ACCOUNTS IMPORT COMPLETE")
    print(f"- db: {args.db}")
    print(f"- csv: {csv_path}")
    print(f"- rows_processed: {stats.rows_processed}")
    print(f"- rows_upserted: {stats.rows_upserted if not args.dry_run else 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

