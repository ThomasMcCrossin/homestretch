#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, sha256_file


def copytree(src: Path, dst: Path, *, ignore_names: set[str] | None = None) -> None:
    ignore_names = ignore_names or set()
    if dst.exists():
        raise SystemExit(f"Refusing to overwrite existing snapshot path: {dst}")

    def _ignore(_dir: str, names: list[str]) -> set[str]:
        return {n for n in names if n in ignore_names}

    shutil.copytree(src, dst, ignore=_ignore)


def iter_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for p in sorted(root.rglob("*")):
        if p.is_file():
            out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-root", type=Path, default=PROJECT_ROOT / "output" / "snapshots")
    ap.add_argument(
        "--name",
        default=datetime.now().strftime("%Y%m%d-%H%M%S"),
        help="Snapshot folder name (default: YYYYMMDD-HHMMSS)",
    )
    args = ap.parse_args()

    out_root = args.out_root
    out_root.mkdir(parents=True, exist_ok=True)
    snap_dir = out_root / str(args.name)
    snap_dir.mkdir(parents=True, exist_ok=False)

    # Copy deterministic project artifacts (exclude input data snapshots).
    # Output is copied excluding its own snapshots folder to avoid recursion.
    copytree(PROJECT_ROOT / "docs", snap_dir / "docs")
    copytree(PROJECT_ROOT / "manifest", snap_dir / "manifest")
    copytree(PROJECT_ROOT / "overrides", snap_dir / "overrides")
    copytree(PROJECT_ROOT / "scripts", snap_dir / "scripts")
    copytree(PROJECT_ROOT / "UfileToFill", snap_dir / "UfileToFill")
    copytree(PROJECT_ROOT / "output", snap_dir / "output", ignore_names={"snapshots"})

    # Copy SQLite DB
    shutil.copy2(DB_PATH, snap_dir / "t2_final.db")

    # Manifest of copied files (sha256 + size + relative path)
    manifest_lines: list[str] = []
    for p in iter_files(snap_dir):
        rel = p.relative_to(snap_dir).as_posix()
        h = sha256_file(p)
        size = p.stat().st_size
        manifest_lines.append(f"{h}  {size}  {rel}")

    (snap_dir / "snapshot_manifest.txt").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

    print("PROJECT SNAPSHOT CREATED")
    print(f"- path: {snap_dir}")
    print(f"- files: {len(manifest_lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
