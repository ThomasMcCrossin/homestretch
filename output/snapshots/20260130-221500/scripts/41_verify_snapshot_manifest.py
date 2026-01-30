#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import yaml

from _lib import PROJECT_ROOT


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--manifest",
        type=Path,
        default=PROJECT_ROOT / "data" / "fresher_snapshots" / "LATEST.txt",
        help="Path to snapshot_manifest.yml, or LATEST.txt pointer (default).",
    )
    args = ap.parse_args()

    manifest_path = args.manifest
    if manifest_path.name == "LATEST.txt":
        if not manifest_path.exists():
            raise SystemExit(f"Missing latest pointer: {manifest_path}")
        snapshot_id = manifest_path.read_text(encoding="utf-8").strip()
        if not snapshot_id:
            raise SystemExit(f"Empty latest pointer: {manifest_path}")
        manifest_path = manifest_path.parent / snapshot_id / "snapshot_manifest.yml"

    if not manifest_path.exists():
        raise SystemExit(f"Missing snapshot manifest: {manifest_path}")

    payload = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or "files" not in payload:
        raise SystemExit(f"Invalid snapshot manifest: {manifest_path}")

    snapshot_root = Path(str(payload.get("snapshot_root") or manifest_path.parent))
    files = payload.get("files") or []
    if not isinstance(files, list):
        raise SystemExit(f"Invalid files list in snapshot manifest: {manifest_path}")

    errors: list[str] = []
    checked = 0

    for entry in files:
        if not isinstance(entry, dict):
            continue
        rel = str(entry.get("relpath") or "").strip()
        expected = str(entry.get("sha256") or "").strip()
        if not rel or not expected:
            continue
        path = snapshot_root / rel
        if not path.exists():
            errors.append(f"missing: {rel}")
            continue
        actual = sha256_file(path)
        if actual != expected:
            errors.append(f"sha mismatch: {rel} expected={expected} actual={actual}")
            continue
        checked += 1

    if errors:
        print("SNAPSHOT VERIFY FAILED\n")
        for e in errors[:50]:
            print(f"- {e}")
        if len(errors) > 50:
            print(f"... ({len(errors) - 50} more)")
        return 1

    print("SNAPSHOT VERIFY PASSED")
    print(f"- manifest: {manifest_path}")
    print(f"- files checked: {checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

