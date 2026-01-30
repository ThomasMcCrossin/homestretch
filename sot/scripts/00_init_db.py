#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from _lib import DB_PATH, apply_migrations, connect_db


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    args = ap.parse_args()

    conn = connect_db(args.db)
    try:
        apply_migrations(conn)
    finally:
        conn.close()

    print("SOT DB INIT COMPLETE")
    print(f"- db: {args.db}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

