#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import io
import sqlite3
import subprocess
from datetime import datetime
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, get_source, load_manifest


def run_psql_copy(curlys_books_path: Path, select_sql: str) -> str:
    copy_sql = f"COPY ({select_sql}) TO STDOUT WITH CSV HEADER"
    cmd = [
        "docker",
        "compose",
        "exec",
        "-T",
        "postgres",
        "psql",
        "-U",
        "curlys_admin",
        "-d",
        "curlys_books",
        "-v",
        "ON_ERROR_STOP=1",
        "-c",
        copy_sql,
    ]
    res = subprocess.run(cmd, cwd=curlys_books_path, check=True, capture_output=True, text=True)
    return res.stdout


def parse_csv(text: str) -> list[dict[str, str]]:
    buf = io.StringIO(text)
    reader = csv.DictReader(buf)
    return [{k: (v or "").strip() for k, v in row.items()} for row in reader]


def ensure_output_dir() -> Path:
    out_dir = PROJECT_ROOT / "data" / "curlys_books_exports" / datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


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
    ap.add_argument("--entity", default="corp")
    ap.add_argument("--reset", action="store_true", help="Clear existing chart_of_accounts before import.")
    args = ap.parse_args()

    manifest = load_manifest()
    curlys_src = get_source(manifest, "curlys_books")
    curlys_books_path = Path(str(curlys_src["path"]))

    conn = connect_db(args.db)
    try:
        ensure_source_file(conn, "curlys_books", curlys_src)

        if args.reset:
            conn.execute("DELETE FROM chart_of_accounts")
            conn.commit()

        select_sql = """
          SELECT
            account_code,
            account_name,
            account_type,
            COALESCE(parent_code, '') AS parent_code,
            COALESCE(gifi_code, '') AS gifi_code,
            COALESCE(t2125_line, '') AS t2125_line,
            COALESCE(is_active::text, '') AS is_active,
            COALESCE(requires_receipt::text, '') AS requires_receipt,
            COALESCE(is_tax_account::text, '') AS is_tax_account,
            COALESCE(created_at::text, '') AS created_at,
            COALESCE(updated_at::text, '') AS updated_at
          FROM curlys_corp.chart_of_accounts
          ORDER BY account_code
        """
        csv_text = run_psql_copy(curlys_books_path, select_sql)
        rows = parse_csv(csv_text)

        out_dir = ensure_output_dir()
        exported_path = out_dir / "chart_of_accounts.csv"
        exported_path.write_text(csv_text, encoding="utf-8")

        inserted = 0
        for r in rows:
            account_code = r.get("account_code") or ""
            if not account_code:
                continue
            conn.execute(
                """
                INSERT INTO chart_of_accounts
                  (account_code, account_name, account_type, parent_code, gifi_code, t2125_line,
                   is_active, requires_receipt, is_tax_account, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(account_code) DO UPDATE SET
                  account_name=excluded.account_name,
                  account_type=excluded.account_type,
                  parent_code=excluded.parent_code,
                  gifi_code=excluded.gifi_code,
                  t2125_line=excluded.t2125_line,
                  is_active=excluded.is_active,
                  requires_receipt=excluded.requires_receipt,
                  is_tax_account=excluded.is_tax_account,
                  created_at=excluded.created_at,
                  updated_at=excluded.updated_at
                """,
                (
                    account_code,
                    r.get("account_name") or "",
                    r.get("account_type") or "",
                    (r.get("parent_code") or "") or None,
                    (r.get("gifi_code") or "") or None,
                    (r.get("t2125_line") or "") or None,
                    1 if (r.get("is_active") or "").lower() == "true" else 0,
                    1 if (r.get("requires_receipt") or "").lower() == "true" else 0,
                    1 if (r.get("is_tax_account") or "").lower() == "true" else 0,
                    (r.get("created_at") or "") or None,
                    (r.get("updated_at") or "") or None,
                ),
            )
            inserted += 1

        conn.commit()
    finally:
        conn.close()

    print("CHART OF ACCOUNTS IMPORT COMPLETE")
    print(f"- exported csv: {exported_path}")
    print(f"- rows upserted: {inserted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

