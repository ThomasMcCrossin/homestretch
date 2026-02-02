#!/usr/bin/env python3
"""
One-command operator workflow to refresh the UFile packet + fill guides from the *current* project state.

This script:
  1) (Optionally) rebuilds the key CSV outputs needed by the packet builder (Schedule 8, book overlay, Schedule exports)
  2) Creates a new deterministic project snapshot under output/snapshots/<stamp>/
  3) Rebuilds UfileToFill/ufile_packet/packet.json from that snapshot
  4) Validates the packet
  5) Rebuilds per-year artifacts (packet.json + UFILet2 fill guides) under UfileToFill/ufile_packet/years/

Why:
  - build_year_artifacts.py only reads UfileToFill/ufile_packet/packet.json.
  - build_packet_from_snapshot.py reads snapshot CSVs, so if the latest snapshot doesn't include Schedule 8 / overlays,
    CCA won't appear in the packet or the fill guides.

Safety:
  - Does not touch Fresher snapshots.
  - Does not write outside the repository working tree.
  - Does not modify source-of-truth input files (manifest/overrides) other than reading them indirectly.
"""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
TOOLS_DIR = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "tools"
SNAPSHOTS_DIR = PROJECT_ROOT / "output" / "snapshots"


def run(cmd: list[str]) -> None:
    subprocess.check_call(cmd, cwd=str(PROJECT_ROOT))


def default_stamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--name",
        default=None,
        help="Snapshot folder name under output/snapshots/ (default: YYYYMMDD-HHMMSS).",
    )
    ap.add_argument("--fy", action="append", dest="fys", help="Limit to specific FY keys (repeatable). Default: all in packet.")
    ap.add_argument(
        "--skip-build-outputs",
        action="store_true",
        help="Skip rebuilding outputs (Schedule 8 / book overlay / schedule exports) before snapshotting.",
    )
    ap.add_argument(
        "--skip-snapshot",
        action="store_true",
        help="Skip creating a new project snapshot; rebuild packet directly from output/ (less auditable).",
    )
    args = ap.parse_args()

    stamp = str(args.name or default_stamp())

    if not args.skip_build_outputs:
        # Rebuild journals + trial balance first so downstream schedules are always based on current numbers.
        run(["python3", "scripts/90_build_inventory_journals.py", "--reset"])
        run(["python3", "scripts/80_build_trial_balance.py"])
        run(["python3", "scripts/82_build_readiness_report.py"])

        run(["python3", "scripts/83_audit_shopify_gateway_vs_payouts.py"])
        run(["python3", "scripts/91b_build_cca_schedule_8.py"])
        run(["python3", "scripts/91c_build_book_fixed_asset_overlay.py"])
        run(["python3", "scripts/91_build_t2_schedule_exports.py", "--book-fixed-assets", "overlay"])

    if args.skip_snapshot:
        snapshot_root = PROJECT_ROOT / "output"
    else:
        SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        run(["python3", "scripts/93_snapshot_project_state.py", "--name", stamp])
        snapshot_root = SNAPSHOTS_DIR / stamp

    build_packet = TOOLS_DIR / "build_packet_from_snapshot.py"
    validate = TOOLS_DIR / "validate_packet.py"
    build_year = TOOLS_DIR / "build_year_artifacts.py"
    build_shareholder_audit = TOOLS_DIR / "build_shareholder_audit_packages.py"
    build_review_pack = TOOLS_DIR / "build_review_remediation_pack.py"

    cmd = ["python3", str(build_packet), "--snapshot", str(snapshot_root)]
    for fy in args.fys or []:
        cmd += ["--fy", str(fy)]
    run(cmd)
    run(["python3", str(validate)])
    run(["python3", str(build_year)])
    run(["python3", str(build_shareholder_audit)])
    run(["python3", str(build_review_pack)])

    print("UFILE PACKET REFRESH COMPLETE")
    print(f"- snapshot_source: {snapshot_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
