#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ParsedRow:
    code: str
    amount: str
    page: int
    section: str


def read_rows(csv_path: Path) -> list[ParsedRow]:
    out: list[ParsedRow] = []
    if not csv_path.exists():
        return out
    with csv_path.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                out.append(
                    ParsedRow(
                        code=str(row.get("code") or ""),
                        amount=str(row.get("amount") or ""),
                        page=int(row.get("page") or 0),
                        section=str(row.get("section") or ""),
                    )
                )
            except Exception:
                continue
    return out


def canonicalize_for_code_search(s: str) -> str:
    """
    UFile PDFs sometimes render digits with separators (e.g. '10 .0 .1' for '1001').
    Build a canonical form for robust code searching.
    """
    t = s
    # Collapse patterns like "1 .0" -> "10" repeatedly.
    for _ in range(6):
        t2 = re.sub(r"(\d)\s*\.\s*(\d)", r"\1\2", t)
        if t2 == t:
            break
        t = t2
    # Also remove stray spaces inside digit runs (e.g. "1 0 0 1").
    t = re.sub(r"(?<=\d)\s+(?=\d)", "", t)
    return t


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parse-dir", required=True, help="Parse output dir (contains text/ and tables/)")
    args = ap.parse_args()

    parse_dir = Path(args.parse_dir).resolve()
    pages_dir = parse_dir / "text" / "pages"
    tables_dir = parse_dir / "tables"
    meta_path = parse_dir / "meta.json"

    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}

    schedule_100 = read_rows(tables_dir / "schedule_100.csv")
    schedule_125 = read_rows(tables_dir / "schedule_125.csv")
    retained = read_rows(tables_dir / "retained_earnings.csv")

    checks: list[tuple[str, str, str]] = []

    def check_row(r: ParsedRow) -> None:
        page_file = pages_dir / f"page_{r.page:03d}.txt"
        if not page_file.exists():
            checks.append((r.section, r.code, "MISSING_PAGE_TEXT"))
            return
        text = page_file.read_text(encoding="utf-8", errors="replace")
        canon = canonicalize_for_code_search(text)
        if r.code not in canon:
            checks.append((r.section, r.code, "CODE_NOT_FOUND_ON_PAGE"))
        else:
            checks.append((r.section, r.code, "OK"))

    for r in schedule_100 + schedule_125 + retained:
        if not r.code:
            continue
        check_row(r)

    ok = sum(1 for _, _, s in checks if s == "OK")
    bad = [c for c in checks if c[2] != "OK"]

    report_lines: list[str] = []
    report_lines.append("# Parse verification report")
    report_lines.append("")
    if meta:
        report_lines.append("## Meta")
        report_lines.append("```json")
        report_lines.append(json.dumps(meta, indent=2))
        report_lines.append("```")
        report_lines.append("")
    report_lines.append("## Summary")
    report_lines.append(f"- Rows checked: {len(checks)}")
    report_lines.append(f"- OK: {ok}")
    report_lines.append(f"- Not OK: {len(bad)}")
    report_lines.append("")
    if bad:
        report_lines.append("## Non-OK rows (needs review)")
        report_lines.append("| section | code | status |")
        report_lines.append("|---|---|---|")
        for section, code, status in bad[:200]:
            report_lines.append(f"| {section} | {code} | {status} |")
        report_lines.append("")
        report_lines.append("If many rows are missing, the parser heuristics likely need adjustment for this PDF layout.")
        report_lines.append("")
    else:
        report_lines.append("All parsed codes were found on their recorded pages’ extracted text.")
        report_lines.append("")

    out_path = parse_dir / "verification_report.md"
    out_path.write_text("\n".join(report_lines).strip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
