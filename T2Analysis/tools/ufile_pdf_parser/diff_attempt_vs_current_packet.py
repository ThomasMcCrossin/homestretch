#!/usr/bin/env python3
"""
Diff a UFile-exported attempt PDF against the current packet (tables/) and emit an HTML+MD report.

This is operator-focused:
- "Attempt" = what UFile currently prints (from the PDF)
- "Expected" = what this repo's packet says should be entered (tables/ schedule_*.csv)

Outputs default to tracked locations under:
- T2Analysis/t2_attempts/<FY>/ufile/parses/attempt_<N>/
- T2Analysis/diffs/<FY>_attempt_<N>_vs_current_packet.(md|html)

You can still opt into legacy output for local-only review.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
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
DEFAULT_DIFF_DIR = PROJECT_ROOT / "T2Analysis" / "diffs"
DEFAULT_PARSE_ROOT = PROJECT_ROOT / "T2Analysis" / "t2_attempts"


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


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return path.read_text()


def _parse_amount_token(tok: str) -> int | None:
    return parse_int_amount(tok)


def extract_attempt_schedule_1(pages_dir: Path, *, wanted_codes: set[str]) -> dict[str, int]:
    """
    Extract Schedule 1 line codes/amounts (A, 104, 121, 206, 403, 500, 510, C, etc.)
    from the parsed page text.
    """
    out: dict[str, int] = {}
    for page_path in sorted(pages_dir.glob("page_*.txt")):
        t = _read_text(page_path)
        if "Schedule 1" not in t and "T2 SCH 1" not in t:
            continue
        for line in t.splitlines():
            s = line.strip()
            if not s:
                continue
            # Tokenize and look for (code, amount) pairs. UFile often repeats the amount in two columns.
            toks = [x for x in re.split(r"\s+", s) if x]
            amt_idxs: list[int] = [i for i, tok in enumerate(toks) if _parse_amount_token(tok) is not None]
            if not amt_idxs:
                continue

            # 1) Letter codes (A/B/C/...) are typically printed at end of line: "... 18,456 A".
            last_tok = toks[-1]
            if last_tok in wanted_codes and re.fullmatch(r"[A-Z]", last_tok):
                if len(toks) >= 2:
                    amt = _parse_amount_token(toks[-2])
                    if amt is not None:
                        out[last_tok] = amt
                        continue

            # 2) Numeric codes: find the last wanted code and take the last amount after it.
            picked: tuple[str, int] | None = None
            for i, tok in enumerate(toks):
                if tok in wanted_codes and re.fullmatch(r"\d{3}", tok):
                    # Guardrail: UFile sometimes prints phrases like "Amount A plus line 500 ..."
                    # where "500" is referenced but the line amount is elsewhere.
                    # Real Schedule 1 line numbers are printed near the end of the line.
                    if i < max(0, len(toks) - 6):
                        continue
                    after_amts = [ai for ai in amt_idxs if ai > i]
                    if after_amts:
                        a = _parse_amount_token(toks[after_amts[-1]])
                        if a is not None:
                            picked = (tok, a)
            if picked:
                code, amt = picked
                out[code] = amt

    return out


@dataclass(frozen=True)
class Schedule8Row:
    row_no: str
    class_no: str | None
    acquisition_cost: int | None
    cca_claim: int | None
    closing_ucc: int | None


def extract_attempt_schedule_8(pages_dir: Path) -> tuple[dict[str, dict[str, int]], int | None]:
    """
    Extract Schedule 8 by aggregating per-property rows into per-class totals.

    Returns:
      - per-class dict: {class_no: {"additions": int, "cca_claim": int}}
      - total CCA claimed (line 403 / total column 23), if found
    """
    # Map row -> (class, acquisition_cost)
    row_meta: dict[str, tuple[str, int]] = {}
    for page_path in sorted(pages_dir.glob("page_*.txt")):
        t = _read_text(page_path)
        if "CCA calculation" not in t or "Class" not in t or "Cost of acquisitions" not in t:
            continue
        for line in t.splitlines():
            m = re.match(r"^\s*(\d+)\.\s+(\d{1,3})\s+([\d,]+)\s*$", line)
            if not m:
                continue
            row_no, class_no, cost_txt = m.group(1), m.group(2), m.group(3)
            cost = _parse_amount_token(cost_txt)
            if cost is None:
                continue
            row_meta[row_no] = (class_no, cost)
        if row_meta:
            break

    # Map row -> cca claim + closing ucc (from the "continued" page with rate/cca/closing).
    row_claims: dict[str, tuple[int, int]] = {}
    total_cca: int | None = None
    for page_path in sorted(pages_dir.glob("page_*.txt")):
        t = _read_text(page_path)
        if "CCA rate %" not in t or "UCC at the end of the" not in t:
            continue
        for line in t.splitlines():
            m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
            if not m:
                continue
            row_no = m.group(1)
            nums = [_parse_amount_token(tok) for tok in re.findall(r"[\d,]+", m.group(2))]
            nums = [n for n in nums if n is not None]
            if len(nums) < 3:
                continue
            # Heuristic: last two numeric tokens are CCA claim and closing UCC.
            cca = nums[-2]
            closing = nums[-1]
            row_claims[row_no] = (cca, closing)
        # Totals line: "Totals 865"
        for line in t.splitlines():
            m2 = re.match(r"^\s*Totals\s+([\d,]+)\s*$", line.strip())
            if m2:
                total_cca = _parse_amount_token(m2.group(1))
                break
        if row_claims:
            break

    by_class: dict[str, dict[str, int]] = {}
    for row_no, (class_no, cost) in row_meta.items():
        cca = row_claims.get(row_no, (None, None))[0]
        if class_no not in by_class:
            by_class[class_no] = {"additions": 0, "cca_claim": 0}
        by_class[class_no]["additions"] += cost
        if cca is not None:
            by_class[class_no]["cca_claim"] += cca

    # If totals are missing, infer from by-class aggregation.
    if total_cca is None and by_class:
        total_cca = sum(v.get("cca_claim", 0) for v in by_class.values())

    return by_class, total_cca


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fy", required=True, help="FY key (e.g., FY2024)")
    ap.add_argument("--pdf", type=Path, required=True, help="UFile exported PDF (attempt)")
    ap.add_argument("--attempt", default=None, help="Attempt number/label (e.g., 008). Used for output filenames.")
    ap.add_argument("--name", default=None, help="Optional human label for output filenames (overrides --attempt).")
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_DIFF_DIR, help="Output directory for MD/HTML diffs.")
    ap.add_argument("--parse-dir", type=Path, default=None, help="Where to write/read the parsed PDF output.")
    ap.add_argument("--legacy-out", action="store_true", help="Also write a copy of the diff under legacy/.")
    args = ap.parse_args()

    fy = str(args.fy).strip()
    pdf = args.pdf.expanduser().resolve()
    if not pdf.exists():
        raise SystemExit(f"Missing PDF: {pdf}")

    packet = json.loads(PACKET_PATH.read_text(encoding="utf-8"))
    if fy not in packet.get("years", {}):
        raise SystemExit(f"FY not found in packet: {fy}")

    if args.name:
        attempt_label = str(args.name).strip().replace(" ", "_")
    elif args.attempt:
        raw = str(args.attempt).strip()
        attempt_label = f"attempt_{raw}" if raw.isdigit() else raw
    else:
        attempt_label = str(pdf.stem).strip().replace(" ", "_")

    out_dir = args.out_dir.expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    out_md = out_dir / f"{fy}_{attempt_label}_vs_current_packet.md"
    out_html = out_dir / f"{fy}_{attempt_label}_vs_current_packet.html"

    # Parse the PDF into structured tables.
    if args.parse_dir is not None:
        parse_dir = args.parse_dir.expanduser().resolve()
    else:
        # Default parse dir mirrors our attempt layout.
        attempt_dir_name = f"attempt_{attempt_label}" if not str(attempt_label).startswith("attempt_") else attempt_label
        parse_dir = DEFAULT_PARSE_ROOT / fy / "ufile" / "parses" / attempt_dir_name
    parse_dir.mkdir(parents=True, exist_ok=True)

    subprocess.check_call([str(PARSER_VENV), str(PARSE_TOOL), "--pdf", str(pdf), "--out", str(parse_dir)])
    subprocess.check_call([str(PARSER_VENV), str(VERIFY_TOOL), "--parse-dir", str(parse_dir)])

    parsed_100 = read_parsed_csv(parse_dir / "tables" / "schedule_100.csv")
    parsed_125 = read_parsed_csv(parse_dir / "tables" / "schedule_125.csv")
    parsed_re = read_parsed_csv(parse_dir / "tables" / "retained_earnings.csv")

    exp_100 = read_csv_map(TABLES_DIR / f"schedule_100_{fy}.csv")
    exp_125 = read_csv_map(TABLES_DIR / f"schedule_125_{fy}.csv")
    exp_1 = read_csv_map(TABLES_DIR / f"schedule_1_{fy}.csv")

    # Retained earnings expected comes from packet (we don't currently have a tables/retained_earnings csv).
    year = packet["years"][fy]
    exp_re = year.get("retained_earnings", {})
    exp_s8 = year.get("schedule_8", {})

    pages_dir = parse_dir / "text" / "pages"
    wanted_s1 = set(exp_1.keys())
    parsed_1_int = extract_attempt_schedule_1(pages_dir, wanted_codes=wanted_s1) if pages_dir.exists() else {}
    parsed_8_by_class, parsed_8_total = extract_attempt_schedule_8(pages_dir) if pages_dir.exists() else ({}, None)

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

    # Schedule 1: compare parsed ints to tables/schedule_1_FY*.csv.
    md.append("## Schedule 1 (Net income for tax purposes)")
    md.append("")
    md.append("| Code | Description | Attempt | Expected | Delta (expected - attempt) | Notes |")
    md.append("|---|---|---:|---:|---:|---|")
    for code in sorted(set(parsed_1_int.keys()) | set(exp_1.keys()), key=lambda s: (len(s), s)):
        a = parsed_1_int.get(code)
        e = exp_1.get(code, {}).get("Amount") if isinstance(exp_1.get(code), dict) else None
        e_int = int(e) if e not in (None, "") else None
        delta = (e_int - a) if (a is not None and e_int is not None) else None
        desc = str(exp_1.get(code, {}).get("Description") or "") if isinstance(exp_1.get(code), dict) else ""
        notes = []
        if a is None and e_int is not None:
            notes.append("missing in attempt")
        if a is not None and e_int is None:
            notes.append("extra in attempt")
        if delta not in (None, 0):
            notes.append("mismatch")
        md.append(f"| {code} | {desc} | {money(a)} | {money(e_int)} | {money(delta) if delta is not None else ''} | {'; '.join(notes)} |")
    md.append("")

    # Schedule 8: class summary + total CCA claimed
    md.append("## Schedule 8 (CCA) — class summary")
    md.append("")
    md.append("| Class | Attempt additions | Expected additions | Attempt CCA | Expected CCA | Notes |")
    md.append("|---:|---:|---:|---:|---:|---|")
    exp_classes = (exp_s8.get("classes") or {}) if isinstance(exp_s8, dict) else {}
    all_classes = sorted(set(parsed_8_by_class.keys()) | set(exp_classes.keys()), key=lambda s: int(s) if str(s).isdigit() else 9999)
    for cls in all_classes:
        a_add = parsed_8_by_class.get(cls, {}).get("additions")
        a_cca = parsed_8_by_class.get(cls, {}).get("cca_claim")
        e_add = exp_classes.get(cls, {}).get("additions") if isinstance(exp_classes.get(cls), dict) else None
        e_cca = exp_classes.get(cls, {}).get("cca_claim") if isinstance(exp_classes.get(cls), dict) else None
        notes = []
        if a_add is not None and e_add is not None and a_add != e_add:
            notes.append("additions mismatch")
        if a_cca is not None and e_cca is not None and a_cca != e_cca:
            notes.append("cca mismatch")
        md.append(f"| {cls} | {money(a_add)} | {money(e_add)} | {money(a_cca)} | {money(e_cca)} | {'; '.join(notes)} |")
    md.append("")
    if parsed_8_total is not None or (isinstance(exp_s8, dict) and exp_s8.get("summary")):
        exp_total = None
        if isinstance(exp_s8, dict):
            exp_total = (exp_s8.get("summary") or {}).get("total_cca_claim")
        md.append(f"- Schedule 8 total CCA (attempt): `{money(parsed_8_total)}`")
        md.append(f"- Schedule 8 total CCA (expected): `{money(exp_total)}`")
        md.append("")

    # Retained earnings rollforward: compare to packet's retained_earnings block.
    md.extend(diff_table("Retained earnings rollforward", parsed_re, exp_re))

    md_text = "\n".join(md).strip() + "\n"
    out_md.write_text(md_text, encoding="utf-8")
    out_html.write_text(render_html(f"UFile diff {fy}", md_text), encoding="utf-8")

    if args.legacy_out:
        legacy_base = LEGACY_DIR / fy / attempt_label
        legacy_base.mkdir(parents=True, exist_ok=True)
        (legacy_base / "diff.md").write_text(md_text, encoding="utf-8")
        (legacy_base / "diff.html").write_text(render_html(f"UFile diff {fy}", md_text), encoding="utf-8")

    print("DIFF BUILT")
    print(f"- md: {out_md}")
    print(f"- html: {out_html}")
    print(f"- parse: {parse_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
