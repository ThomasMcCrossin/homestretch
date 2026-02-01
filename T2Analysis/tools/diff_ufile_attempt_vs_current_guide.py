#!/usr/bin/env python3
"""
Generate an operator-friendly "what changed?" diff between:
  - a prior UFile attempt (parsed evidence bundle), and
  - the current per-year fill guide (the authoritative "enter-this" source).

Goal:
- Let you update an in-progress UFile file without re-entering everything.
- Highlight what to ADD / CHANGE / CLEAR on the key screens.

Outputs:
- Markdown report
- HTML report (rendered with the same guide renderer, so it's readable on 15\" 1080p)
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def money(n: int) -> str:
    sign = "-" if n < 0 else ""
    nn = abs(int(n))
    return f"{sign}{nn:,}"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _extract_table(md: str, *, heading: str) -> list[dict[str, str]]:
    """
    Extract the first markdown pipe table after a given heading (## or ###).

    Returns list of dicts keyed by header names.
    """
    # Find the heading line exactly.
    h_pat = re.compile(rf"(?m)^{re.escape(heading)}\s*$")
    m = h_pat.search(md)
    if not m:
        raise SystemExit(f"Could not find heading in guide: {heading!r}")
    tail = md[m.end() :]

    # Find first table block.
    lines = tail.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("|"):
            start = i
            break
        if line.startswith("#"):
            break
    if start is None:
        raise SystemExit(f"Could not find table after heading: {heading!r}")

    block: list[str] = []
    for j in range(start, len(lines)):
        ln = lines[j].rstrip("\n")
        if not ln.strip():
            break
        if not ln.lstrip().startswith("|"):
            break
        block.append(ln)

    if len(block) < 2:
        return []

    # Parse markdown pipe table.
    def split_row(row: str) -> list[str]:
        r = row.strip()
        if r.startswith("|"):
            r = r[1:]
        if r.endswith("|"):
            r = r[:-1]
        return [c.strip() for c in r.split("|")]

    header = split_row(block[0])
    # block[1] is the separator row.
    out: list[dict[str, str]] = []
    for row in block[2:]:
        cells = split_row(row)
        # pad/truncate
        while len(cells) < len(header):
            cells.append("")
        cells = cells[: len(header)]
        out.append({header[i]: cells[i] for i in range(len(header))})
    return out


def _parse_amount_cell(s: str) -> int:
    ss = str(s or "").strip()
    if not ss:
        return 0
    ss = ss.replace(",", "")
    # allow leading minus
    if ss.startswith("(") and ss.endswith(")"):
        ss = "-" + ss[1:-1]
    # strip any stray non-numeric
    ss = re.sub(r"[^0-9-]", "", ss)
    if not ss or ss == "-":
        return 0
    return int(ss)


def _extract_section(md: str, *, heading: str) -> str:
    """
    Extract the body of a markdown section that starts at a heading line and
    ends at the next heading of the same or higher level.

    heading should be the full heading line, e.g. "## Income source (UFile screen)".
    """
    # Determine heading level ("#" count).
    m = re.match(r"^(#+)\s+", heading.strip())
    if not m:
        raise ValueError(f"Invalid heading: {heading!r}")
    level = len(m.group(1))

    # Find the exact heading line.
    pat = re.compile(rf"(?m)^{re.escape(heading)}\s*$")
    hit = pat.search(md)
    if not hit:
        return ""

    tail = md[hit.end() :]
    # Stop at next heading with <= level.
    stop = re.search(rf"(?m)^#{{1,{level}}}\s+", tail)
    body = tail[: stop.start()] if stop else tail
    return body.strip() + "\n"


def _extract_first_fenced_block(md: str, *, heading: str) -> str:
    """
    Extract the first fenced code block (```...```) that occurs inside the section
    starting at `heading`.

    Used for copy/paste chunks (e.g. Notes to the financial statements), so the
    diff report can include them explicitly.
    """
    body = _extract_section(md, heading=heading)
    if not body:
        return ""
    m = re.search(r"(?s)```[^\n]*\n.*?\n```", body)
    if not m:
        return ""
    return m.group(0).strip() + "\n"

def _load_attempt_table_csv(path: Path) -> dict[str, int]:
    """
    Parse attempt extracted schedule table CSV and sum amounts by 4-digit code.
    """
    out: dict[str, int] = {}
    ignore_codes = {"0002", "0003"}  # UFile header fields that can show up as pseudo-codes in the export
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            code = str(row.get("code") or "").strip()
            if not re.fullmatch(r"\d{4}", code):
                continue
            if code in ignore_codes:
                continue
            amt = _parse_amount_cell(row.get("amount") or "0")
            out[code] = out.get(code, 0) + amt
    return out


def _normalize_attempt_for_cogs(code: str, amount: int) -> int:
    # UFile often prints closing inventory (8500) as a negative in the cost-of-sales block.
    if code == "8500":
        return abs(amount)
    return amount


@dataclass(frozen=True)
class DeltaRow:
    code: str
    description: str
    attempt: int
    expected: int
    delta: int
    action: str
    note: str


def _compute_deltas(
    *,
    expected_rows: list[dict[str, str]],
    attempt_amounts: dict[str, int],
    code_col: str = "GIFI",
    auto_calculated_codes: set[str] | None = None,
) -> list[DeltaRow]:
    rows: list[DeltaRow] = []
    expected_by_code: dict[str, dict[str, str]] = {}

    for r in expected_rows:
        code = str(r.get(code_col) or "").strip()
        if not re.fullmatch(r"\d{4}", code):
            continue
        expected_by_code[code] = r

    codes = sorted(set(expected_by_code.keys()) | set(attempt_amounts.keys()), key=lambda c: int(c))
    for code in codes:
        exp_row = expected_by_code.get(code, {})
        desc = str(exp_row.get("Description") or exp_row.get("description") or "").strip()
        note = str(exp_row.get("Note") or exp_row.get("Entry rule") or "").strip()
        exp_amt = _parse_amount_cell(exp_row.get("Amount") or exp_row.get("amount") or "0")
        att_amt_raw = attempt_amounts.get(code, 0)
        att_amt = _normalize_attempt_for_cogs(code, att_amt_raw)

        delta = exp_amt - att_amt

        auto = auto_calculated_codes or set()
        if code in expected_by_code and code not in attempt_amounts:
            # Don't nag about explicit zero lines that may not print in the attempt.
            action = "OK" if exp_amt == 0 else "ADD (missing in attempt)"
        elif code not in expected_by_code and code in attempt_amounts:
            # These lines can still appear in the exported PDF even when you did not type them in UFile.
            # The operator action is: don't type/override these totals; it's OK if they print.
            action = "AUTO (do not type; ok if printed)" if code in auto else "CLEAR / DO NOT ENTER (extra in attempt)"
        elif delta != 0:
            action = "CHANGE (update amount)"
        else:
            action = "OK"

        rows.append(
            DeltaRow(
                code=code,
                description=desc,
                attempt=att_amt,
                expected=exp_amt,
                delta=delta,
                action=action,
                note=note,
            )
        )

    # Prioritize non-OK items first, then code order.
    priority = {
        "ADD (missing in attempt)": 0,
        "CHANGE (update amount)": 1,
        "MOVE (enter 2781; if rejected, keep 2780)": 2,
        "CLEAR / DO NOT ENTER (extra in attempt)": 3,
        "AUTO (do not type; ok if printed)": 4,
        "OK (fallback if 2781 rejected)": 5,
        "OK": 6,
    }
    rows.sort(key=lambda r: (priority.get(r.action, 9), int(r.code)))
    return rows


def _render_delta_table(rows: list[DeltaRow], *, limit: int | None = None) -> str:
    """
    Render a markdown table.
    """
    shown = rows if limit is None else rows[:limit]
    has_any_note = any(bool(r.note) for r in shown)
    out: list[str] = []
    if has_any_note:
        out.append("| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |")
        out.append("|---|---|---:|---:|---:|---|---|")
    else:
        out.append("| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action |")
        out.append("|---|---|---:|---:|---:|---|")
    for r in shown:
        cells = [
            r.code,
            (r.description or "").replace("\n", " ").strip(),
            money(r.attempt),
            money(r.expected),
            money(r.delta),
            r.action,
        ]
        if has_any_note:
            cells.append((r.note or "").replace("\n", " ").strip())
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fy", required=True, help="FY key (e.g. FY2024)")
    ap.add_argument("--attempt-id", required=True, help="Attempt id (e.g. attempt_001)")
    ap.add_argument(
        "--guide",
        default=None,
        help="Path to the per-year fill guide markdown. Default: UfileToFill/ufile_packet/years/<FY>/UFILet2_FILL_GUIDE.md",
    )
    ap.add_argument(
        "--parse-dir",
        default=None,
        help="Path to parsed attempt bundle dir. Default: T2Analysis/t2_attempts/<FY>/ufile/parses/<attempt-id>/",
    )
    ap.add_argument(
        "--out-base",
        default=None,
        help="Output base path (no extension). Default: UfileToFill/ufile_packet/diffs/<FY>_<attempt-id>_vs_current_guide",
    )
    args = ap.parse_args()

    fy = str(args.fy).strip()
    attempt_id = str(args.attempt_id).strip()

    guide_path = Path(args.guide).resolve() if args.guide else (PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "years" / fy / "UFILet2_FILL_GUIDE.md")
    parse_dir = Path(args.parse_dir).resolve() if args.parse_dir else (PROJECT_ROOT / "T2Analysis" / "t2_attempts" / fy / "ufile" / "parses" / attempt_id)

    out_base = (
        Path(args.out_base).resolve()
        if args.out_base
        else (PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "diffs" / f"{fy}_{attempt_id}_vs_current_guide")
    )
    out_md = out_base.with_suffix(".md")
    out_html = out_base.with_suffix(".html")

    if not guide_path.exists():
        raise SystemExit(f"Missing guide: {guide_path}")
    if not parse_dir.exists():
        raise SystemExit(f"Missing parse dir: {parse_dir}")

    guide_md = _read_text(guide_path)

    # Expected entry tables from the guide (authoritative "enter-this").
    exp_bs = _extract_table(guide_md, heading="## Balance sheet (GIFI Schedule 100)")
    exp_is = _extract_table(guide_md, heading="## Income statement (GIFI Schedule 125)")
    exp_re = _extract_table(guide_md, heading="### Retained earnings (whole dollars)")
    exp_s8 = _extract_table(guide_md, heading="### Schedule 8 / CCA")
    exp_s8_assets = _extract_table(guide_md, heading="### Schedule 8 asset additions (audit trail)")
    exp_s8_lines = _extract_table(guide_md, heading="### UFile Schedule 8 entry lines (per asset)")
    must_check_body = _extract_section(guide_md, heading="## Must-check before filing / exporting a PDF copy")
    income_source_body = _extract_section(guide_md, heading="## Income source (UFile screen)")
    cca_screen_body = _extract_section(guide_md, heading="## Capital cost allowance (UFile screen)")
    notes_fs_block = _extract_first_fenced_block(guide_md, heading="### Notes to financial statements (copy/paste)")

    # Attempt extracted tables (what was in the exported PDF, i.e. what the attempt "contained").
    att100 = _load_attempt_table_csv(parse_dir / "tables" / "schedule_100.csv")
    att125 = _load_attempt_table_csv(parse_dir / "tables" / "schedule_125.csv")

    # Retained earnings rows aren't always extracted cleanly; fall back to Schedule 100 values for the key codes.
    # (The guide wants you to enter the rollforward, not 3600 directly.)
    att_re = {k: att100.get(k, 0) for k in ("3660", "3680", "3700", "3740", "3849")}

    # PDF schedule forms presence (based on parsed full_text).
    full_text_path = parse_dir / "text" / "full_text.txt"
    full_text = _read_text(full_text_path) if full_text_path.exists() else ""
    has_s8_form = bool(re.search(r"\bT2\s+SCH\s*8\b", full_text, flags=re.IGNORECASE))
    has_s7_form = bool(re.search(r"\bT2\s+SCH\s*7\b", full_text, flags=re.IGNORECASE))

    auto_sch100 = {
        # balance sheet totals/subtotals + auto-calculated retained earnings fields
        "1599",
        "2008",
        "2009",
        "2599",
        "3139",
        "3499",
        "3620",
        "3640",
        "3600",
        "3849",
        # net income for the year can appear in multiple places; operator should enter via rollforward
        "3680",
    }
    auto_sch125 = {
        # totals/subtotals that should not be typed
        "8089",
        "8299",
        "8518",
        "8519",
        "9367",
        "9368",
        "9369",
        "9970",
        "9999",
    }

    deltas_bs = _compute_deltas(expected_rows=exp_bs, attempt_amounts=att100, code_col="GIFI", auto_calculated_codes=auto_sch100)
    deltas_is = _compute_deltas(expected_rows=exp_is, attempt_amounts=att125, code_col="GIFI", auto_calculated_codes=auto_sch125)
    deltas_re = _compute_deltas(expected_rows=exp_re, attempt_amounts=att_re, code_col="GIFI", auto_calculated_codes=set())

    # Special-case: shareholder payable is often entered as 2781, but some UFile configs reject 2781 and require 2780.
    # If the attempt used 2780 with the same amount, treat 2780 as an acceptable fallback rather than a "clear".
    bs_by_code = {r.code: r for r in deltas_bs}
    r2781 = bs_by_code.get("2781")
    r2780 = bs_by_code.get("2780")
    if r2781 and r2780:
        if r2781.expected > 0 and r2781.attempt == 0 and r2780.attempt == r2781.expected and r2780.expected == 0:
            updated: list[DeltaRow] = []
            for r in deltas_bs:
                if r.code == "2781":
                    updated.append(
                        DeltaRow(
                            code=r.code,
                            description=r.description,
                            attempt=r.attempt,
                            expected=r.expected,
                            delta=r.delta,
                            action="MOVE (enter 2781; if rejected, keep 2780)",
                            note=r.note,
                        )
                    )
                elif r.code == "2780":
                    updated.append(
                        DeltaRow(
                            code=r.code,
                            description=r.description,
                            attempt=r.attempt,
                            expected=r.expected,
                            delta=r.delta,
                            action="OK (fallback if 2781 rejected)",
                            note=r.note,
                        )
                    )
                else:
                    updated.append(r)
            deltas_bs = updated

    # Build a concise "what changed" summary from the highest-signal deltas.
    def top_changes(rows: list[DeltaRow], *, keep: int = 8) -> list[DeltaRow]:
        x = [
            r
            for r in rows
            if r.action not in ("OK", "AUTO (do not type; ok if printed)")
            and (r.expected != 0 or r.attempt != 0)
        ]
        x.sort(key=lambda r: abs(r.delta), reverse=True)
        return x[:keep]

    summary_bs = top_changes(deltas_bs)
    summary_is = top_changes(deltas_is)

    out: list[str] = []
    out.append(f"# UFile attempt vs current guide — {fy} ({attempt_id})")
    out.append("")
    out.append("This report compares your **previous UFile attempt** (from the exported PDF parse bundle) to the **current fill guide** (authoritative enter-this source).")
    out.append("")
    out.append("## Quick answer")
    out.append("- Yes: the current guides are updated to reflect the latest asset + CCA/book overlay work.")
    out.append("- Your prior attempt differs materially from the current guide (most importantly: the **Costco iPad** is now treated as a **book fixed asset** with **book amortization mirroring tax CCA**).")
    out.append("")
    out.append("## Highest-signal changes (what you will actually feel in UFile)")
    out.append("### Balance sheet / fixed assets")
    out.append(_render_delta_table(summary_bs))
    out.append("")
    out.append("### Income statement")
    out.append(_render_delta_table(summary_is))
    out.append("")

    if must_check_body or income_source_body or cca_screen_body or notes_fs_block:
        out.append("## Notes / reminders to apply (from the current guide)")
        if must_check_body:
            out.append("### Must-check before filing / exporting")
            out.append(must_check_body.rstrip())
            out.append("")
        if income_source_body:
            out.append("### Income source screen (clears INCOMESOURCE warning)")
            out.append(income_source_body.rstrip())
            out.append("")
        if notes_fs_block:
            out.append("### Notes to financial statements (copy/paste)")
            out.append("Paste into UFile (Notes checklist screen) if you are including notes with the filing copy:")
            out.append("")
            out.append(notes_fs_block.rstrip())
            out.append("")
        if cca_screen_body:
            out.append("### Capital cost allowance screen (Schedule 8 entry + audit)")
            out.append(cca_screen_body.rstrip())
            out.append("")
    out.append("## Balance sheet (GIFI Schedule 100) — full delta table")
    out.append(_render_delta_table(deltas_bs))
    out.append("")
    out.append("## Retained earnings rollforward — delta table")
    out.append(_render_delta_table(deltas_re))
    out.append("")
    out.append("## Income statement (GIFI Schedule 125) — full delta table")
    out.append(_render_delta_table(deltas_is))
    out.append("")
    out.append("## Schedule 8 / CCA (UFile Capital cost allowance screen)")
    out.append("Expected classes (from the current guide):")
    if exp_s8:
        # Render as a simple markdown table (preserves guide order)
        out.append("| Class | Description | Opening UCC | Additions | CCA claim | Closing UCC |")
        out.append("|---|---|---:|---:|---:|---:|")
        for r in exp_s8:
            out.append(
                "| "
                + " | ".join(
                    [
                        str(r.get("Class") or "").strip(),
                        str(r.get("Description") or "").strip(),
                        str(r.get("Opening UCC") or "").strip(),
                        str(r.get("Additions") or "").strip(),
                        str(r.get("CCA claim") or "").strip(),
                        str(r.get("Closing UCC") or "").strip(),
                    ]
                )
                + " |"
            )
    else:
        out.append("_(No Schedule 8 table found in the guide.)_")
    out.append("")
    if exp_s8_assets:
        out.append("Expected asset additions (audit list):")
        out.append("| Asset ID | Description | Date | Class | Cost |")
        out.append("|---|---|---|---|---:|")
        for r in exp_s8_assets:
            out.append(
                "| "
                + " | ".join(
                    [
                        str(r.get("Asset ID") or "").strip(),
                        str(r.get("Description") or "").strip(),
                        str(r.get("Date") or "").strip(),
                        str(r.get("Class") or "").strip(),
                        str(r.get("Cost") or "").strip(),
                    ]
                )
                + " |"
            )
        out.append("")
    if exp_s8_lines:
        out.append("UFile entry lines (per asset):")
        out.append("| Class | Addition description | Date acquired/available | Cost | Proceeds (if disposed) | Disposed description (if any) |")
        out.append("|---|---|---|---:|---:|---|")
        for r in exp_s8_lines:
            out.append(
                "| "
                + " | ".join(
                    [
                        str(r.get("Class") or "").strip(),
                        str(r.get("Addition description") or "").strip(),
                        str(r.get("Date acquired/available") or "").strip(),
                        str(r.get("Cost") or "").strip(),
                        str(r.get("Proceeds (if disposed)") or "").strip(),
                        str(r.get("Disposed description (if any)") or "").strip(),
                    ]
                )
                + " |"
            )
        out.append("")
    out.append("PDF package form presence (from the attempt export):")
    out.append(f"- Schedule 8 form header present in PDF? **{'Yes' if has_s8_form else 'No'}**")
    out.append(f"- Schedule 7 form header present in PDF? **{'Yes' if has_s7_form else 'No'}**")
    out.append("")
    out.append("If a schedule form is missing from the exported PDF, it usually means UFile didn’t include it in the export/print package settings (or the schedule detail wasn’t entered).")
    out.append("")
    out.append("Run the checker after your next export:")
    out.append("")
    out.append(f"```bash\npython3 T2Analysis/tools/check_ufile_export_completeness.py --fy {fy} --pdf /path/to/ufile_export.pdf\n```")
    out.append("")

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")

    # Render HTML using the existing guide renderer (same look/feel as the fill guide HTML).
    # Import locally without making UfileToFill a package.
    tools_dir = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "tools"
    sys.path.insert(0, str(tools_dir))
    from render_year_guide_html import render_year_guide_html  # type: ignore  # noqa: E402

    combined_packet = json.loads(_read_text(PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "packet.json"))
    html = render_year_guide_html(combined_packet, fy, md_guide=out_md.read_text(encoding="utf-8"))
    out_html.write_text(html, encoding="utf-8")

    print("DIFF REPORT WRITTEN")
    print(f"- md: {out_md}")
    print(f"- html: {out_html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
