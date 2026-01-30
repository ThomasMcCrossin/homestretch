from __future__ import annotations

import sqlite3
from pathlib import Path


SOT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = SOT_ROOT / "db" / "t2_sot.db"
MIGRATIONS_DIR = SOT_ROOT / "migrations"


def connect_db(path: Path = DB_PATH) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def apply_migrations(conn: sqlite3.Connection) -> None:
    MIGRATIONS_DIR.mkdir(parents=True, exist_ok=True)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS schema_migrations (
          version INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          applied_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
        """
    )
    applied = {
        int(r["version"])
        for r in conn.execute("SELECT version FROM schema_migrations ORDER BY version").fetchall()
    }

    migration_files = sorted(MIGRATIONS_DIR.glob("*.sql"))
    for path in migration_files:
        stem = path.stem
        # Expect files like 001_init.sql
        try:
            version = int(stem.split("_", 1)[0])
        except Exception as e:  # noqa: BLE001 - CLI tool
            raise RuntimeError(f"Invalid migration filename (expected NNN_name.sql): {path.name}") from e
        if version in applied:
            continue
        sql = path.read_text(encoding="utf-8")
        conn.executescript(sql)
        conn.execute(
            "INSERT INTO schema_migrations(version, name) VALUES (?, ?)",
            (version, path.name),
        )
        conn.commit()

