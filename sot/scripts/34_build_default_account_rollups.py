#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, apply_migrations, connect_db


@dataclass(frozen=True)
class RollupStats:
    rollups_upserted: int = 0
    members_inserted: int = 0


ROLLUPS: list[tuple[str, str, str]] = [
    ("COGS", "COGS", "All curlys-books accounts with GIFI 8518 (cost of sales)."),
    ("OFFICE_SUPPLIES", "Office supplies", "Wave-style rollup."),
    ("SUPPLIES", "Supplies (other)", "Wave-style rollup (incl. janitorial where applicable)."),
    ("REPAIRS_MAINTENANCE", "Repairs & maintenance", "Wave-style rollup."),
    ("SMALL_EQUIPMENT", "Small tools & equipment", "Wave-style rollup (under capitalization threshold)."),
    ("RENT", "Rent", "Wave-style rollup."),
    ("BANK_FEES", "Bank fees", "Wave-style rollup."),
    ("HST_ITC", "HST ITC receivable", "Tax rollup (ITCs)."),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--reset", action="store_true", help="Clear existing rollups/members first.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = connect_db(args.db)
    stats = RollupStats()
    try:
        apply_migrations(conn)
        conn.execute("BEGIN")

        if args.reset:
            if args.dry_run:
                print("WOULD: DELETE FROM account_rollup_members; DELETE FROM account_rollups")
            else:
                conn.execute("DELETE FROM account_rollup_members")
                conn.execute("DELETE FROM account_rollups")

        for code, name, notes in ROLLUPS:
            if args.dry_run:
                continue
            conn.execute(
                """
                INSERT INTO account_rollups(rollup_code, rollup_name, notes)
                VALUES (?, ?, ?)
                ON CONFLICT(rollup_code) DO UPDATE SET
                  rollup_name=excluded.rollup_name,
                  notes=excluded.notes
                """,
                (code, name, notes),
            )
            stats = RollupStats(rollups_upserted=stats.rollups_upserted + 1, members_inserted=stats.members_inserted)

        if args.dry_run:
            conn.rollback()
            print("ACCOUNT ROLLUPS DRY-RUN COMPLETE")
            return 0

        # Deterministic mappings (can be refined later via explicit overrides).
        # COGS via T2125 line 8518 (curlys-books export)
        conn.execute(
            """
            INSERT OR IGNORE INTO account_rollup_members(account_code, rollup_code, method, notes)
            SELECT account_code, 'COGS', 'AUTO_T2125', 't2125_line=8518'
            FROM chart_of_accounts
            WHERE t2125_line='8518'
            """
        )
        # Fixed single-account rollups
        fixed = [
            ("6600", "OFFICE_SUPPLIES"),
            ("5200", "SUPPLIES"),
            ("5202", "SUPPLIES"),
            ("5204", "SUPPLIES"),
            ("5205", "SUPPLIES"),
            ("5206", "SUPPLIES"),
            ("5209", "SUPPLIES"),
            ("6300", "REPAIRS_MAINTENANCE"),
            ("6350", "SMALL_EQUIPMENT"),
            ("6100", "RENT"),
            ("6000", "BANK_FEES"),
            ("2210", "HST_ITC"),
        ]
        for account_code, rollup_code in fixed:
            conn.execute(
                """
                INSERT OR IGNORE INTO account_rollup_members(account_code, rollup_code, method, notes)
                VALUES (?, ?, 'MANUAL', 'default mapping')
                """,
                (account_code, rollup_code),
            )

        members = conn.execute("SELECT COUNT(*) AS n FROM account_rollup_members").fetchone()
        stats = RollupStats(rollups_upserted=stats.rollups_upserted, members_inserted=int(members["n"]))

        conn.commit()
    finally:
        conn.close()

    print("DEFAULT ACCOUNT ROLLUPS BUILT")
    print(f"- db: {args.db}")
    print(f"- rollups_upserted: {stats.rollups_upserted}")
    print(f"- members_total: {stats.members_inserted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
