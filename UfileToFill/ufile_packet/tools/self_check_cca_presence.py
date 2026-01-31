#!/usr/bin/env python3
"""
Sanity check: ensure CCA/Schedule 8 content is present in the combined packet.json and appears in per-year guides.

This is intentionally lightweight (no test framework dependency).
"""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "packet.json"
YEARS_DIR = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "years"


def main() -> int:
    packet = json.loads(PACKET_PATH.read_text())
    years = packet.get("years", {})
    if not isinstance(years, dict) or not years:
        raise SystemExit("packet.json missing years")

    failures: list[str] = []
    for fy, year in sorted(years.items()):
        if not isinstance(year, dict):
            continue
        schedule_8 = year.get("schedule_8")
        has_s8 = bool(schedule_8) and isinstance(schedule_8, dict) and bool(schedule_8.get("classes"))
        pos = year.get("positions", {}) if isinstance(year.get("positions"), dict) else {}
        cca_required = (pos.get("cca_required") or {}).get("value")

        # If schedule_8 exists, cca_required should be true.
        if has_s8 and cca_required is not True:
            failures.append(f"{fy}: schedule_8 exists but positions.cca_required.value is not true")

        guide_path = YEARS_DIR / fy / "UFILet2_FILL_GUIDE.md"
        if guide_path.exists():
            guide = guide_path.read_text()
            if has_s8 and ("## Capital cost allowance (UFile screen)" not in guide or "Schedule 8 / CCA" not in guide):
                failures.append(f"{fy}: schedule_8 exists but guide missing Capital cost allowance / Schedule 8 section")

    if failures:
        raise SystemExit("CCA PRESENCE CHECK FAILED:\n- " + "\n- ".join(failures))

    print("CCA PRESENCE CHECK OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

