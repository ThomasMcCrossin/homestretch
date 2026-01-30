#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from pathlib import Path

import yaml

from _lib import DB_PATH, connect_db, get_source, load_manifest, sha256_file


def quote_ident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def sanitize_table_name(name: str) -> str:
    name = name.strip()
    name = re.sub(r"[^a-zA-Z0-9_]+", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    if not name:
        raise ValueError("Empty table name after sanitization")
    return name


def load_snapshot_manifest(path: Path) -> dict:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Invalid snapshot manifest: {path}")
    files = payload.get("files")
    if not isinstance(files, list):
        raise ValueError(f"Invalid snapshot manifest files list: {path}")
    return payload


def expected_sha256_from_snapshot(payload: dict, relpath: str) -> str | None:
    for entry in payload.get("files") or []:
        if not isinstance(entry, dict):
            continue
        if str(entry.get("relpath") or "") == relpath:
            sha = str(entry.get("sha256") or "").strip()
            return sha or None
    return None


def iter_snapshot_csv_files(snapshot_root: Path) -> list[tuple[str, Path, str]]:
    out: list[tuple[str, Path, str]] = []
    for scope in ("debits", "credits"):
        dir_path = snapshot_root / "tables" / scope
        if not dir_path.exists():
            continue
        for p in sorted(dir_path.glob("*.csv")):
            rel = p.relative_to(snapshot_root).as_posix()
            out.append((scope, p, rel))
    return out


def create_table_from_header(conn: sqlite3.Connection, table_name: str, header: list[str]) -> None:
    cols = []
    for col in header:
        c = (col or "").strip()
        if not c:
            raise ValueError(f"Empty column name in header for {table_name}")
        cols.append(f"{quote_ident(c)} TEXT")
    cols_sql = ", ".join(cols)
    conn.execute(f"DROP TABLE IF EXISTS {quote_ident(table_name)}")
    conn.execute(f"CREATE TABLE {quote_ident(table_name)} ({cols_sql})")


def import_csv_to_table(conn: sqlite3.Connection, table_name: str, csv_path: Path) -> int:
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if not header:
            raise ValueError(f"Empty CSV (no header): {csv_path}")

        create_table_from_header(conn, table_name, header)

        placeholders = ", ".join(["?"] * len(header))
        col_sql = ", ".join(quote_ident(c.strip()) for c in header)
        sql = f"INSERT INTO {quote_ident(table_name)} ({col_sql}) VALUES ({placeholders})"

        n = 0
        for row in reader:
            if len(row) != len(header):
                raise ValueError(
                    f"Row length mismatch in {csv_path} (expected {len(header)} cols, got {len(row)})"
                )
            conn.execute(sql, row)
            n += 1
        return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--snapshot-manifest-source-key", default="fresher_snapshot_manifest")
    ap.add_argument("--verify-files", action="store_true", help="Verify sha256 of each imported CSV against snapshot manifest.")
    ap.add_argument(
        "--only",
        action="append",
        default=[],
        help="Only import specific tables (repeatable). Example: --only bank_transactions --only credit_bank_items",
    )
    args = ap.parse_args()

    manifest = load_manifest()
    src = get_source(manifest, args.snapshot_manifest_source_key)
    manifest_path = Path(str(src.get("path") or "")).expanduser()
    if not manifest_path.exists():
        raise SystemExit(f"Missing snapshot manifest: {manifest_path}")

    expected_manifest_sha = str(src.get("sha256") or "").strip()
    if expected_manifest_sha:
        actual_manifest_sha = sha256_file(manifest_path)
        if actual_manifest_sha != expected_manifest_sha:
            raise SystemExit(
                f"Snapshot manifest sha256 mismatch: expected {expected_manifest_sha} actual {actual_manifest_sha}"
            )

    payload = load_snapshot_manifest(manifest_path)
    snapshot_root = Path(str(payload.get("snapshot_root") or manifest_path.parent))

    only = {sanitize_table_name(x) for x in (args.only or [])}

    csv_files = iter_snapshot_csv_files(snapshot_root)
    if not csv_files:
        raise SystemExit(f"No snapshot CSV tables found under: {snapshot_root / 'tables'}")

    conn = connect_db(args.db)
    try:
        conn.execute("BEGIN")
        imported = 0
        for scope, csv_path, rel in csv_files:
            stem = sanitize_table_name(csv_path.stem)
            if only and stem not in only:
                continue

            table_name = f"fresher_{scope}__{stem}"

            if args.verify_files:
                expected = expected_sha256_from_snapshot(payload, rel)
                if not expected:
                    raise SystemExit(f"No expected sha256 found in snapshot manifest for: {rel}")
                actual = sha256_file(csv_path)
                if actual != expected:
                    raise SystemExit(f"sha256 mismatch for {rel}: expected {expected} actual {actual}")

            count = import_csv_to_table(conn, table_name, csv_path)
            print(f"- imported {scope}/{csv_path.name} -> {table_name}: {count} rows")
            imported += 1

        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()

    print("FRESHER SNAPSHOT TABLE IMPORT COMPLETE")
    print(f"- db: {args.db}")
    print(f"- snapshot_manifest: {manifest_path}")
    print(f"- tables imported: {imported}")
    if only:
        print(f"- only: {sorted(only)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

