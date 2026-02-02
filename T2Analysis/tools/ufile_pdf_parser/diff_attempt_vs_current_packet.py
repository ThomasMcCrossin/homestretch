#!/usr/bin/env python3
"""
Diff a UFile-exported attempt PDF against the current packet (tables/) and emit an HTML+MD report.

This is operator-focused:
- "Attempt" = what UFile currently prints (from the PDF)
- "Expected" = what this repo's packet says should be entered (tables/ schedule_*.csv)

Outputs are written under legacy/ so they won't be committed, but remain locally reviewable.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PARSER_VENV = PROJECT_ROOT / "T2Analysis" / "tools" / "ufile_pdf_parser" / ".venv" / "bin" / "python"
PARSE_TOOL = PROJECT_ROOT / "T2Analysis" / "tools" / "ufile_pdf_parser" / "parse_ufile_pdf.py"
VERIFY_TOOL = PROJECT_ROOT / "T2Analysis" / "tools" / "ufile_pdf_parser" / "verify_parse.py"

PACKET_PATH = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "packet.json"
TABLES_DIR = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "tables"

LEGACY_DIR = PROJECT_ROOT / "legacy" / "ufile_diffs"


def read_csv_map(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
    out: dict[str, dict[str, str]] = {}
    for r in rows:
        code = str(r.get("GIFI_Code") or r.get("Code") or "").strip()
        if not code:
            continue
        out[code] = r
    return out


def read_parsed_csv(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
    out: dict[str, dict[str, str]] = {}
    for r in rows:
        code = str(r.get("code") or "").strip()
        amt = str(r.get("amount") or "").strip()
        if not code:
            continue
        # Keep last seen value if duplicates exist; usually totals appear once.
        out[code] = {"code": code, "amount": amt, "page": str(r.get("page") or ""), "section": str(r.get("section") or "")}
    return out


def parse_int_amount(s: str) -> int | None:
    """
    Parse UFile printed amount strings like '33,860' or '(508 )' or ''.
    Returns int dollars, or None if blank/unparseable.
    """
    t = (s or "").strip()
    if not t:
        return None
    t = t.replace("$", "").replace(" ", "").replace(",", "")
    if t.startswith("(") and t.endswith(")"):
        t = "-" + t[1:-1]
    try:
        return int(t)
    except Exception:
        return None


def money(n: int | None) -> str:
    if n is None:
        return ""
    return f"{n:,}"


def render_html(title: str, md: str) -> str:
    # Reuse the same HTML renderer used by the fill guides for consistency/readability.
    # Import by path so this script can run from anywhere without PYTHONPATH gymnastics.
    import importlib.util

    renderer_path = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "tools" / "render_year_guide_html.py"
    # Use a unique module name and register it in sys.modules so dataclasses/type lookups work.
    import sys
    module_name = "t2_render_year_guide_html"
    spec = importlib.util.spec_from_file_location(module_name, str(renderer_path))
    if not spec or not spec.loader:
        raise SystemExit(f"Could not load HTML renderer: {renderer_path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    render_year_guide_html = getattr(mod, "render_year_guide_html")

    # Minimal fake "packet" wrapper to satisfy renderer signature.
    fake_packet: dict[str, Any] = {"meta": {"snapshot_source": ""}, "entity": {"legal_name": title}, "years": {}}
    return render_year_guide_html(fake_packet, "FYDIFF", md_guide=md)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fy", required=True, help="FY key (e.g., FY2024)")
    ap.add_argument("--pdf", type=Path, required=True, help="UFile exported PDF (attempt)")
    ap.add_argument("--name", default=None, help="Optional attempt label for output filenames")
    args = ap.parse_args()

    fy = str(args.fy).strip()
    pdf = args.pdf.expanduser().resolve()
    if not pdf.exists():
        raise SystemExit(f"Missing PDF: {pdf}")

    packet = json.loads(PACKET_PATH.read_text(encoding="utf-8"))
    if fy not in packet.get("years", {}):
        raise SystemExit(f"FY not found in packet: {fy}")

    attempt_label = str(args.name or pdf.stem).strip().replace(" ", "_")
    out_base = LEGACY_DIR / fy / attempt_label
    out_base.mkdir(parents=True, exist_ok=True)

    # Parse the PDF into structured tables.
    parse_dir = out_base / "parse"
    parse_dir.mkdir(parents=True, exist_ok=True)

    import subprocess

    subprocess.check_call([str(PARSER_VENV), str(PARSE_TOOL), "--pdf", str(pdf), "--out", str(parse_dir)])
    subprocess.check_call([str(PARSER_VENV), str(VERIFY_TOOL), "--parse-dir", str(parse_dir)])

    parsed_100 = read_parsed_csv(parse_dir / "tables" / "schedule_100.csv")
    parsed_125 = read_parsed_csv(parse_dir / "tables" / "schedule_125.csv")
    parsed_1 = read_parsed_csv(parse_dir / "tables" / "schedule_1.csv")
    parsed_re = read_parsed_csv(parse_dir / "tables" / "retained_earnings.csv")

    exp_100 = read_csv_map(TABLES_DIR / f"schedule_100_{fy}.csv")
    exp_125 = read_csv_map(TABLES_DIR / f"schedule_125_{fy}.csv")
    exp_1 = read_csv_map(TABLES_DIR / f"schedule_1_{fy}.csv")

    # Retained earnings expected comes from packet (we don't currently have a tables/retained_earnings csv).
    year = packet["years"][fy]
    exp_re = year.get("retained_earnings", {})

    def diff_table(title: str, parsed: dict[str, dict[str, str]], expected: dict[str, Any]) -> list[str]:
        lines: list[str] = []
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| Code | Description | Attempt | Expected | Delta (expected - attempt) | Notes |")
        lines.append("|---|---|---:|---:|---:|---|")

        all_codes = sorted(set(parsed.keys()) | set(expected.keys()), key=lambda s: (len(s), s))
        for code in all_codes:
            a = parse_int_amount(parsed.get(code, {}).get("amount", "")) if code in parsed else None
            if isinstance(expected.get(code), dict):
                e = expected.get(code, {}).get("Amount") or expected.get(code, {}).get("amount")
            else:
                e = expected.get(code)
            e_int = None
            if e is not None and e != "":
                try:
                    e_int = int(e)
                except Exception:
                    try:
                        e_int = parse_int_amount(str(e))
                    except Exception:
                        e_int = None

            delta = None
            if a is not None and e_int is not None:
                delta = e_int - a

            desc = ""
            if isinstance(expected.get(code), dict):
                desc = str(expected.get(code, {}).get("Description") or expected.get(code, {}).get("label") or "")
            elif isinstance(exp_re, dict) and code in exp_re:
                desc = str(exp_re.get(code, {}).get("label") or "")

            notes = []
            if a is None and e_int is not None:
                notes.append("missing in attempt")
            if a is not None and e_int is None:
                notes.append("extra in attempt")
            if delta not in (None, 0):
                notes.append("mismatch")

            lines.append(
                f"| {code} | {desc} | {money(a)} | {money(e_int)} | {money(delta) if delta is not None else ''} | {'; '.join(notes)} |"
            )

        lines.append("")
        return lines

    md: list[str] = []
    md.append(f"# UFile attempt diff vs current packet — {fy}")
    md.append("")
    md.append(f"- Attempt PDF: `{pdf}`")
    md.append(f"- Packet snapshot_source: `{packet.get('meta', {}).get('snapshot_source')}`")
    md.append("")

    md.extend(diff_table("Schedule 100 (Balance sheet)", parsed_100, exp_100))
    md.extend(diff_table("Schedule 125 (Income statement)", parsed_125, exp_125))
    md.extend(diff_table("Schedule 1 (Net income for tax purposes)", parsed_1, exp_1))
    # Retained earnings rollforward: compare to packet's retained_earnings block.
    md.extend(diff_table("Retained earnings rollforward", parsed_re, exp_re))

    md_text = "\n".join(md).strip() + "\n"
    (out_base / "diff.md").write_text(md_text, encoding="utf-8")
    (out_base / "diff.html").write_text(render_html(f"UFile diff {fy}", md_text), encoding="utf-8")

    print("DIFF BUILT")
    print(f"- out: {out_base}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
