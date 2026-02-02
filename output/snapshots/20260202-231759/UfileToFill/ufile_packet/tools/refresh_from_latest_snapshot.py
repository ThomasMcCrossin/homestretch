#!/usr/bin/env python3
"""
Refresh `packet.json` + rebuild year artifacts using the latest snapshot under `output/snapshots/`.

This is the “one command” operator workflow to keep:
- `UfileToFill/ufile_packet/packet.json`
- `UfileToFill/ufile_packet/years/FY*/UFILet2_FILL_GUIDE.md`
in sync with the newest accounting outputs.

Safety:
- Does not touch the accounting DB.
- Reads snapshot CSVs only.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SNAPSHOTS_DIR = PROJECT_ROOT / "output" / "snapshots"
TOOLS_DIR = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "tools"


def find_latest_snapshot_dir() -> Path:
    if not SNAPSHOTS_DIR.exists():
        raise SystemExit(f"Missing snapshots dir: {SNAPSHOTS_DIR}")
    # Preferred names: YYYYMMDD-HHMMSS (lexicographically sortable)
    stamp_re = re.compile(r"^\d{8}-\d{6}$")
    candidates = [p for p in SNAPSHOTS_DIR.iterdir() if p.is_dir() and stamp_re.match(p.name)]
    if not candidates:
        raise SystemExit(f"No timestamped snapshots found in: {SNAPSHOTS_DIR}")
    return sorted(candidates, key=lambda p: p.name)[-1]


def run(cmd: list[str]) -> None:
    subprocess.check_call(cmd, cwd=str(PROJECT_ROOT))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", type=Path, default=None, help="Optional explicit snapshot dir (defaults to latest).")
    ap.add_argument("--fy", action="append", dest="fys", help="Limit to specific FY keys (repeatable). Default: all in packet.")
    args = ap.parse_args()

    snapshot = args.snapshot.resolve() if args.snapshot else find_latest_snapshot_dir()
    build_packet = TOOLS_DIR / "build_packet_from_snapshot.py"
    validate = TOOLS_DIR / "validate_packet.py"
    build_year = TOOLS_DIR / "build_year_artifacts.py"

    cmd = ["python3", str(build_packet), "--snapshot", str(snapshot)]
    for fy in args.fys or []:
        cmd += ["--fy", str(fy)]
    run(cmd)
    run(["python3", str(validate)])
    run(["python3", str(build_year)])

    print("UFILE PACKET REFRESH COMPLETE")
    print(f"- snapshot: {snapshot}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

