#!/usr/bin/env python3

from __future__ import annotations

import sqlite3
from pathlib import Path

from _lib import DB_PATH, MANIFEST_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest


def apply_migrations(conn: sqlite3.Connection) -> None:
    migrations_dir = PROJECT_ROOT / "db" / "migrations"
    migrations_dir.mkdir(parents=True, exist_ok=True)

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS migrations (
          id INTEGER PRIMARY KEY,
          filename TEXT NOT NULL UNIQUE,
          applied_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
        """
    )

    applied = {r[0] for r in conn.execute("SELECT filename FROM migrations")}

    for path in sorted(migrations_dir.glob("*.sql")):
        if path.name in applied:
            continue
        sql = path.read_text(encoding="utf-8")
        conn.executescript(sql)
        conn.execute("INSERT INTO migrations (filename) VALUES (?)", (path.name,))
        conn.commit()


def load_fiscal_years(conn: sqlite3.Connection) -> None:
    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit(f"No fiscal years found in {MANIFEST_PATH}")

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS fiscal_years (
          fy TEXT PRIMARY KEY,
          start_date TEXT NOT NULL,
          end_date TEXT NOT NULL
        )
        """
    )
    for fy in fys:
        conn.execute(
            """
            INSERT INTO fiscal_years (fy, start_date, end_date)
            VALUES (?, ?, ?)
            ON CONFLICT(fy) DO UPDATE SET start_date=excluded.start_date, end_date=excluded.end_date
            """,
            (fy.fy, fy.start_date, fy.end_date),
        )
    conn.commit()


def main() -> int:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = connect_db()
    try:
        apply_migrations(conn)
        load_fiscal_years(conn)
    finally:
        conn.close()

    print("DB INIT COMPLETE")
    print(f"- db: {DB_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

