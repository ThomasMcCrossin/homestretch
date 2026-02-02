#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml

from _lib import PROJECT_ROOT


DEFAULT_FRESHER_DIR = Path("/home/clarencehub/Fresh/Fresher")
DEFAULT_DEBITS_DB = DEFAULT_FRESHER_DIR / "canteen_reconciliation_v2.db"
DEFAULT_CREDITS_DB = DEFAULT_FRESHER_DIR / "credits" / "credits_reconciliation.db"
DEFAULT_OVERRIDES_DIR = DEFAULT_FRESHER_DIR / "overrides"
DEFAULT_REPORTS_LATEST_DIR = DEFAULT_FRESHER_DIR / "output" / "latest"
DEFAULT_REPORTS_AUDITS_DIR = DEFAULT_FRESHER_DIR / "output" / "audits"
DEFAULT_CREDITS_OUTPUT_DIR = DEFAULT_FRESHER_DIR / "credits" / "output"


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def export_table_to_csv(conn: sqlite3.Connection, table: str, out_path: Path) -> None:
    rows = conn.execute(f"SELECT * FROM {table}").fetchall()
    cols = [r[1] for r in conn.execute(f"PRAGMA table_info({table})").fetchall()]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            # sqlite3 Row/tuple; stringify None as empty to keep CSV clean
            w.writerow(["" if v is None else v for v in r])


def export_sqlite_db_tables(db_path: Path, out_dir: Path) -> list[Path]:
    conn = sqlite3.connect(db_path)
    try:
        tables = [
            r[0]
            for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
        ]
        exported: list[Path] = []
        for t in tables:
            out_path = out_dir / f"{t}.csv"
            export_table_to_csv(conn, t, out_path)
            exported.append(out_path)
        return exported
    finally:
        conn.close()


def copy_tree(src: Path, dst: Path) -> list[Path]:
    if not src.exists():
        return []
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return [p for p in dst.rglob("*") if p.is_file()]


def copy_file(src: Path, dst: Path) -> Path:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return dst


@dataclass(frozen=True)
class SnapshotFile:
    relpath: str
    sha256: str
    size_bytes: int


def write_snapshot_manifest(snapshot_root: Path, files: list[Path]) -> Path:
    items: list[SnapshotFile] = []
    for p in sorted(files, key=lambda x: str(x)):
        rel = p.relative_to(snapshot_root).as_posix()
        items.append(SnapshotFile(relpath=rel, sha256=sha256_file(p), size_bytes=p.stat().st_size))

    payload = {
        "version": 1,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "snapshot_root": snapshot_root.as_posix(),
        "files": [dict(relpath=i.relpath, sha256=i.sha256, size_bytes=i.size_bytes) for i in items],
    }
    out_path = snapshot_root / "snapshot_manifest.yml"
    out_path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fresher-dir", type=Path, default=DEFAULT_FRESHER_DIR)
    ap.add_argument("--debits-db", type=Path, default=DEFAULT_DEBITS_DB)
    ap.add_argument("--credits-db", type=Path, default=DEFAULT_CREDITS_DB)
    ap.add_argument("--overrides-dir", type=Path, default=DEFAULT_OVERRIDES_DIR)
    ap.add_argument("--reports-latest-dir", type=Path, default=DEFAULT_REPORTS_LATEST_DIR)
    ap.add_argument("--reports-audits-dir", type=Path, default=DEFAULT_REPORTS_AUDITS_DIR)
    ap.add_argument("--credits-output-dir", type=Path, default=DEFAULT_CREDITS_OUTPUT_DIR)
    ap.add_argument("--out-root", type=Path, default=PROJECT_ROOT / "data" / "fresher_snapshots")
    ap.add_argument("--snapshot-id", default=None, help="Override snapshot id (default: timestamp).")
    args = ap.parse_args()

    if not args.debits_db.exists():
        raise SystemExit(f"Missing debits DB: {args.debits_db}")
    if not args.credits_db.exists():
        raise SystemExit(f"Missing credits DB: {args.credits_db}")

    snapshot_id = args.snapshot_id or datetime.now().strftime("%Y%m%d-%H%M%S")
    snapshot_root = args.out_root / snapshot_id
    snapshot_root.mkdir(parents=True, exist_ok=False)

    all_files: list[Path] = []

    # Copy DB snapshots
    debits_db_dst = copy_file(args.debits_db, snapshot_root / "db" / args.debits_db.name)
    credits_db_dst = copy_file(args.credits_db, snapshot_root / "db" / args.credits_db.name)
    all_files.extend([debits_db_dst, credits_db_dst])

    # Export table CSVs
    all_files.extend(export_sqlite_db_tables(debits_db_dst, snapshot_root / "tables" / "debits"))
    all_files.extend(export_sqlite_db_tables(credits_db_dst, snapshot_root / "tables" / "credits"))

    # Copy overrides + reports (for audit provenance)
    all_files.extend(copy_tree(args.overrides_dir, snapshot_root / "fresher_overrides"))
    all_files.extend(copy_tree(args.reports_latest_dir, snapshot_root / "fresher_reports" / "latest"))
    all_files.extend(copy_tree(args.reports_audits_dir, snapshot_root / "fresher_reports" / "audits"))
    all_files.extend(copy_tree(args.credits_output_dir, snapshot_root / "fresher_credits_reports" / "output"))

    manifest_path = write_snapshot_manifest(snapshot_root, all_files)
    manifest_sha = sha256_file(manifest_path)

    latest_ptr = args.out_root / "LATEST.txt"
    latest_ptr.parent.mkdir(parents=True, exist_ok=True)
    latest_ptr.write_text(snapshot_id + "\n", encoding="utf-8")

    print("FRESHER SNAPSHOT CREATED")
    print(f"- snapshot: {snapshot_root}")
    print(f"- manifest: {manifest_path} (sha256={manifest_sha})")
    print(f"- latest pointer: {latest_ptr}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
