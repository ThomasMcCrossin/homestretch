#!/usr/bin/env python3
"""
Check that a UFile-exported PDF "package" actually contains the schedule forms
that the project expects to be present for a given FY.

Why:
- UFile can reference schedules (e.g., "from Schedule 8") without printing the
  actual schedule forms in the exported PDF, depending on export/print settings
  and whether the schedule has any entered details.
- We want a deterministic, automatable check to catch "missing schedule forms"
  before filing or sharing a "full package" PDF.

This tool is read-only w.r.t. accounting DB and project outputs. It may create a
temporary parse bundle under /tmp if a parse dir is not supplied.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PARSER = PROJECT_ROOT / "T2Analysis" / "tools" / "ufile_pdf_parser" / "parse_ufile_pdf.py"


@dataclass(frozen=True)
class ScheduleCheck:
    schedule: str
    required: bool
    found: bool
    reason: str


def _read_year_packet(packet_path: Path, fy: str) -> tuple[dict, dict]:
    obj = json.loads(packet_path.read_text(encoding="utf-8"))
    # Year packet layout: {"year": { "FY2024": {...} }, "entity": {...}}
    year = None
    if isinstance(obj.get("year"), dict) and fy in obj["year"]:
        year = obj["year"][fy]
    elif isinstance(obj.get("years"), dict) and fy in obj["years"]:
        # Combined packet layout: {"years": {...}}
        year = obj["years"][fy]
    if not isinstance(year, dict):
        raise SystemExit(f"Could not locate FY '{fy}' in packet: {packet_path}")
    entity = obj.get("entity") if isinstance(obj.get("entity"), dict) else {}
    return entity, year


def _schedule_required(entity: dict, year: dict) -> dict[str, tuple[bool, str]]:
    positions = year.get("positions") if isinstance(year.get("positions"), dict) else {}

    def pos_bool(key: str) -> bool:
        v = positions.get(key, {})
        if isinstance(v, dict):
            return bool(v.get("value"))
        return False

    corp_type = str(entity.get("corp_type") or "").strip()

    # Schedule 8: required if we are claiming any CCA / have an asset register.
    schedule_8 = year.get("schedule_8") if isinstance(year.get("schedule_8"), dict) else {}
    sch8_has_classes = bool((schedule_8.get("classes") or {}) if isinstance(schedule_8.get("classes"), dict) else False)
    req_s8 = pos_bool("cca_required") or sch8_has_classes
    why_s8 = "CCA required per packet (positions.cca_required or schedule_8.classes)."

    # Schedule 88: required if internet income / website disclosure is true.
    req_s88 = pos_bool("internet_income_line_180")
    why_s88 = "Internet income / website disclosure required per packet (positions.internet_income_line_180)."

    # Schedule 3: only if dividends were paid (Part IV / dividend disclosure).
    ufile_screens = year.get("ufile_screens") if isinstance(year.get("ufile_screens"), dict) else {}
    dividends_paid = ufile_screens.get("dividends_paid") if isinstance(ufile_screens.get("dividends_paid"), dict) else {}
    has_dividends = bool(dividends_paid.get("has_dividends")) if isinstance(dividends_paid, dict) else False
    req_s3 = has_dividends
    why_s3 = "Dividends paid screen indicates dividends (ufile_screens.dividends_paid.has_dividends)."

    # Schedule 7: CCPC claiming SBD typically generates/uses Schedule 7. We use a simple rule:
    # - CCPC AND positive Schedule 1 code C.
    schedule_1 = year.get("schedule_1") if isinstance(year.get("schedule_1"), dict) else {}
    s1_c = int(schedule_1.get("C", {}).get("amount") or 0) if isinstance(schedule_1.get("C"), dict) else 0
    req_s7 = corp_type == "CCPC" and s1_c > 0
    why_s7 = "CCPC with positive taxable/net income (Schedule 1 code C > 0) typically requires Schedule 7 (SBD)."

    return {
        "3": (req_s3, why_s3),
        "7": (req_s7, why_s7),
        "8": (req_s8, why_s8),
        "88": (req_s88, why_s88),
    }


def _has_schedule_form(full_text: str, sched_num: str) -> bool:
    # UFile headers observed include variants like "T2 SCH 3" and "T2 SCH33".
    # We only treat the explicit schedule *form header* as presence.
    pat = re.compile(rf"\bT2\s+SCH\s*{re.escape(sched_num)}\b", re.IGNORECASE)
    return bool(pat.search(full_text))


def _load_full_text(pdf: Path, parse_dir: Path | None) -> tuple[str, Path | None]:
    if parse_dir is not None:
        full_text_path = parse_dir / "text" / "full_text.txt"
        if not full_text_path.exists():
            raise SystemExit(f"Parse dir missing full text: {full_text_path}")
        return full_text_path.read_text(encoding="utf-8", errors="replace"), parse_dir

    if not PARSER.exists():
        raise SystemExit(f"Missing PDF parser: {PARSER}")

    with tempfile.TemporaryDirectory(prefix="ufile-parse-", dir="/tmp") as td:
        out_dir = Path(td)
        cmd = ["python3", str(PARSER), "--pdf", str(pdf), "--out", str(out_dir)]
        subprocess.check_call(cmd, cwd=str(PROJECT_ROOT))
        full_text = (out_dir / "text" / "full_text.txt").read_text(encoding="utf-8", errors="replace")
        # Temp dir is deleted after this function returns.
        return full_text, None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True, help="Path to a UFile-exported PDF package")
    ap.add_argument("--fy", required=True, help="FY key, e.g. FY2024")
    ap.add_argument(
        "--packet",
        default=None,
        help="Packet path. Default: UfileToFill/ufile_packet/years/<FY>/packet.json",
    )
    ap.add_argument(
        "--parse-dir",
        default=None,
        help="Optional existing parse bundle dir containing text/full_text.txt (avoids re-parsing PDF).",
    )
    args = ap.parse_args()

    fy = str(args.fy).strip()
    pdf = Path(args.pdf).resolve()
    parse_dir = Path(args.parse_dir).resolve() if args.parse_dir else None

    packet_path = (
        Path(args.packet).resolve()
        if args.packet
        else (PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "years" / fy / "packet.json")
    )

    if not packet_path.exists():
        raise SystemExit(f"Packet not found: {packet_path}")
    if not pdf.exists():
        raise SystemExit(f"PDF not found: {pdf}")

    entity, year = _read_year_packet(packet_path, fy)
    req = _schedule_required(entity, year)

    full_text, used_parse_dir = _load_full_text(pdf, parse_dir)

    checks: list[ScheduleCheck] = []
    for sched_num, (required, reason) in req.items():
        found = _has_schedule_form(full_text, sched_num)
        checks.append(ScheduleCheck(schedule=sched_num, required=required, found=found, reason=reason))

    # Output: human-friendly table + exit code for CI-style use.
    missing_required = [c for c in checks if c.required and not c.found]

    print("UFILE EXPORT COMPLETENESS CHECK")
    print(f"- fy: {fy}")
    print(f"- pdf: {pdf}")
    if parse_dir:
        print(f"- parse_dir: {parse_dir}")
    else:
        print("- parsed_in: (temporary parse)")
    print("")
    print("Schedule  Required  Found  Note")
    print("--------  --------  -----  ----")
    for c in checks:
        req_txt = "yes" if c.required else "no"
        found_txt = "yes" if c.found else "no"
        note = c.reason if c.required else "Not required by packet."
        print(f"{c.schedule:>8}  {req_txt:>8}  {found_txt:>5}  {note}")

    if missing_required:
        print("")
        print("FAIL: missing required schedule forms in the exported PDF:")
        for c in missing_required:
            print(f"- Schedule {c.schedule} (required): not found as a 'T2 SCH {c.schedule}' form header in the PDF text.")
        return 2

    print("")
    print("PASS: all required schedule forms were found in the exported PDF.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
