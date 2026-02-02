#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from _lib import DB_PATH, connect_db, dollars_to_cents, get_source, load_manifest, sha256_file


@dataclass(frozen=True)
class SourceSpec:
    source_key: str
    table: str
    kind: str


def parse_cra_date(value: str) -> str | None:
    s = (value or "").strip().strip('"')
    if not s:
        return None
    # CRA exports are in the form: "July 05, 2024"
    try:
        d = datetime.strptime(s, "%B %d, %Y").date()
    except ValueError:
        return None
    return d.isoformat()


def parse_amount_cents(value: str) -> int:
    s = (value or "").strip()
    if not s:
        return 0
    # Remove currency formatting.
    s = s.replace("$", "").strip()
    return dollars_to_cents(s)


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
    row = conn.execute("SELECT id FROM source_files WHERE source_key = ?", (source_key,)).fetchone()
    if not row:
        raise SystemExit(f"Failed to persist source_files row for {source_key}")
    return int(row[0])


def verify_source(cfg: dict) -> Path:
    path = Path(str(cfg.get("path") or "")).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Missing source file: {path}")
    expected = str(cfg.get("sha256") or "").strip()
    if expected:
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"sha256 mismatch for {path}: expected {expected} actual {actual}")
    return path


def import_hst(conn: sqlite3.Connection, *, source_file_id: int, csv_path: Path, reset: bool) -> int:
    if reset:
        conn.execute("DELETE FROM cra_hst_account_transactions WHERE source_file_id = ?", (source_file_id,))

    inserted = 0
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=2):  # 1-based header; row numbers start at 2
            effective_raw = (row.get("Effective date") or "").strip()
            period_end_raw = (row.get("Period-end") or "").strip()
            txn = (row.get("Transactions") or "").strip()
            date_posted_raw = (row.get("Date posted") or "").strip()
            amount_raw = (row.get("$ Amount") or "").strip()
            cr_dr = (row.get("CR/DR") or "").strip() or None

            if not any([effective_raw, period_end_raw, txn, date_posted_raw, amount_raw, cr_dr]):
                continue

            effective = parse_cra_date(effective_raw)
            period_end = parse_cra_date(period_end_raw)
            date_posted = parse_cra_date(date_posted_raw)
            amount_cents = parse_amount_cents(amount_raw)

            conn.execute(
                """
                INSERT INTO cra_hst_account_transactions (
                  source_file_id, source_row, effective_date,
                  period_end, period_end_raw,
                  transaction_label, date_posted,
                  amount_cents, cr_dr
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(source_file_id, source_row) DO UPDATE SET
                  effective_date=excluded.effective_date,
                  period_end=excluded.period_end,
                  period_end_raw=excluded.period_end_raw,
                  transaction_label=excluded.transaction_label,
                  date_posted=excluded.date_posted,
                  amount_cents=excluded.amount_cents,
                  cr_dr=excluded.cr_dr
                """,
                (
                    source_file_id,
                    idx,
                    effective,
                    period_end,
                    period_end_raw.strip().strip('"') or None,
                    txn or "(blank)",
                    date_posted,
                    amount_cents,
                    cr_dr,
                ),
            )
            inserted += 1

    return inserted


def import_simple_ledger(
    conn: sqlite3.Connection,
    *,
    table: str,
    source_file_id: int,
    csv_path: Path,
    reset: bool,
) -> int:
    if reset:
        conn.execute(f"DELETE FROM {table} WHERE source_file_id = ?", (source_file_id,))

    inserted = 0
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=2):
            date_posted_raw = (row.get("Date posted") or "").strip()
            txn = (row.get("Transactions") or "").strip()
            date_received_raw = (row.get("Date received") or "").strip()
            amount_raw = (row.get("$ Amount") or "").strip()
            cr_dr = (row.get("CR/DR") or "").strip() or None

            if not any([date_posted_raw, txn, date_received_raw, amount_raw, cr_dr]):
                continue

            date_posted = parse_cra_date(date_posted_raw)
            date_received = parse_cra_date(date_received_raw)
            amount_cents = parse_amount_cents(amount_raw)

            conn.execute(
                f"""
                INSERT INTO {table} (
                  source_file_id, source_row,
                  date_posted, transaction_label, date_received,
                  amount_cents, cr_dr
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(source_file_id, source_row) DO UPDATE SET
                  date_posted=excluded.date_posted,
                  transaction_label=excluded.transaction_label,
                  date_received=excluded.date_received,
                  amount_cents=excluded.amount_cents,
                  cr_dr=excluded.cr_dr
                """,
                (
                    source_file_id,
                    idx,
                    date_posted,
                    txn or "(blank)",
                    date_received,
                    amount_cents,
                    cr_dr,
                ),
            )
            inserted += 1

    return inserted


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing CRA rows for these sources before import.")
    ap.add_argument("--hst-source-key", default="cra_hst_account_transactions_csv")
    ap.add_argument("--payroll-source-key", default="cra_payroll_account_transactions_csv")
    ap.add_argument("--arrears-source-key", default="cra_arrears_account_transactions_csv")
    args = ap.parse_args()

    manifest = load_manifest()

    sources = [
        SourceSpec(args.hst_source_key, "cra_hst_account_transactions", "hst"),
        SourceSpec(args.payroll_source_key, "cra_payroll_account_transactions", "payroll"),
        SourceSpec(args.arrears_source_key, "cra_arrears_account_transactions", "arrears"),
    ]

    conn = connect_db(args.db)
    try:
        inserted_total = 0
        with conn:
            for spec in sources:
                cfg = get_source(manifest, spec.source_key)
                csv_path = verify_source(cfg)
                source_file_id = ensure_source_file(conn, spec.source_key, cfg)

                if spec.kind == "hst":
                    inserted = import_hst(conn, source_file_id=source_file_id, csv_path=csv_path, reset=args.reset)
                else:
                    inserted = import_simple_ledger(
                        conn,
                        table=spec.table,
                        source_file_id=source_file_id,
                        csv_path=csv_path,
                        reset=args.reset,
                    )

                inserted_total += inserted

    finally:
        conn.close()

    print("CRA EXPORT IMPORT COMPLETE")
    print(f"- db: {args.db}")
    print(f"- rows upserted: {inserted_total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
