#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from _lib import DB_PATH, SOT_ROOT, apply_migrations, connect_db


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument(
        "--ignore-wave-bills",
        type=Path,
        default=SOT_ROOT / "overrides" / "ignore_wave_bills.json",
        help="JSON list of fresher_debits__wave_bills.id values to ignore.",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ignore_ids: list[str] = []
    if args.ignore_wave_bills.exists():
        ignore_ids = json.loads(args.ignore_wave_bills.read_text(encoding="utf-8"))
        ignore_ids = [str(x).strip() for x in ignore_ids if str(x).strip()]

    conn = connect_db(args.db)
    try:
        apply_migrations(conn)
        conn.execute("BEGIN")

        applied = 0
        missing: list[str] = []

        for wave_bill_id in ignore_ids:
            source_record_id = f"fresher_debits__wave_bills:{wave_bill_id}"
            row = conn.execute(
                "SELECT id FROM documents WHERE source_system=? AND source_record_id=?",
                ("T2_FINAL_DB", source_record_id),
            ).fetchone()
            if not row:
                missing.append(wave_bill_id)
                continue
            doc_id = int(row["id"])

            exists = conn.execute(
                "SELECT 1 FROM document_flags WHERE document_id=? AND flag='IGNORE'",
                (doc_id,),
            ).fetchone()
            if exists:
                continue

            if args.dry_run:
                print(f"WOULD IGNORE: wave_bill_id={wave_bill_id} document_id={doc_id}")
            else:
                conn.execute(
                    "INSERT INTO document_flags(document_id, flag, notes) VALUES (?, 'IGNORE', ?)",
                    (doc_id, f"Ignored via overrides file ({args.ignore_wave_bills.name})"),
                )
                applied += 1
                print(f"IGNORED: wave_bill_id={wave_bill_id} document_id={doc_id}")

        if not args.dry_run:
            conn.commit()
        else:
            conn.rollback()

    finally:
        conn.close()

    if missing:
        print("")
        print("WARNING: Some wave_bill_ids were not found in SOT documents:")
        for wid in missing:
            print(f"- {wid}")

    print("")
    print("OVERRIDES APPLY COMPLETE")
    print(f"- db: {args.db}")
    print(f"- overrides: {args.ignore_wave_bills}")
    print(f"- applied_ignore_flags: {applied if not args.dry_run else 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

