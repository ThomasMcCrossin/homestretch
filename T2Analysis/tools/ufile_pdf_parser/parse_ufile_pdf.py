#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


AMOUNT_RE = re.compile(r"^\(?-?\$?[\d,]+\)?$")


def normalize_amount(s: str) -> str:
    # Remove stray spaces, currency symbols, and handle parentheses.
    ss = s.strip().replace("$", "")
    ss = ss.replace(" ", "")
    if ss.startswith("(") and ss.endswith(")"):
        ss = "-" + ss[1:-1]
    return ss


@dataclass(frozen=True)
class Row:
    code: str
    description: str
    amount: str
    page: int
    section: str


def group_words_into_lines(words: list[dict[str, Any]], y_tol: float = 2.0) -> list[list[dict[str, Any]]]:
    # pdfplumber returns word dicts with keys like text, x0, x1, top, bottom.
    # We group by approximate 'top' position.
    lines: list[list[dict[str, Any]]] = []
    for w in sorted(words, key=lambda d: (float(d.get("top", 0.0)), float(d.get("x0", 0.0)))):
        placed = False
        top = float(w.get("top", 0.0))
        for line in lines:
            if abs(float(line[0].get("top", 0.0)) - top) <= y_tol:
                line.append(w)
                placed = True
                break
        if not placed:
            lines.append([w])
    for line in lines:
        line.sort(key=lambda d: float(d.get("x0", 0.0)))
    return lines


def detect_section(page_text: str) -> str:
    t = page_text.upper()
    if "NOTES AND DIAGNOSTICS" in t:
        return "diagnostics"
    if "SCHEDULE 100" in t and "BALANCE SHEET INFORMATION" in t:
        return "schedule_100"
    if "SCHEDULE 125" in t and "INCOME STATEMENT INFORMATION" in t:
        return "schedule_125"
    # In the UFile export we’ve seen, retained earnings is printed as a block within Schedule 100 pages.
    if "RETAINED EARNINGS/DEFICIT" in t:
        return "retained_earnings"
    return "other"


def parse_gifi_lines_from_words(lines: list[list[dict[str, Any]]], page_number: int, section: str) -> list[Row]:
    rows: list[Row] = []
    for line in lines:
        texts = [str(w.get("text", "")).strip() for w in line if str(w.get("text", "")).strip()]
        if not texts:
            continue

        # Heuristic: GIFI rows include a 4-digit code as a standalone token.
        code_idx = None
        for i, tok in enumerate(texts):
            if re.fullmatch(r"\d{4}", tok):
                code_idx = i
                break
        if code_idx is None:
            continue

        # Amount is usually the rightmost numeric-looking token.
        amount_idx = None
        for j in range(len(texts) - 1, -1, -1):
            if AMOUNT_RE.match(texts[j]):
                amount_idx = j
                break
        if amount_idx is None or amount_idx <= code_idx:
            continue

        code = texts[code_idx]
        description_tokens = texts[code_idx + 1 : amount_idx]
        # Skip obvious “header” rows that aren’t a line item (e.g., code present but no description).
        if not description_tokens:
            continue

        description = " ".join(description_tokens)
        amount = normalize_amount(texts[amount_idx])
        if not re.fullmatch(r"-?[\d,]+", amount):
            continue

        rows.append(Row(code=code, description=description, amount=amount, page=page_number, section=section))
    return rows


def parse_retained_earnings_from_text(page_text: str, page_number: int) -> list[Row]:
    rows: list[Row] = []
    # Capture the retained earnings block in a loose way, then look for 4-digit codes with amounts.
    if "RETAINED EARNINGS/DEFICIT" not in page_text.upper():
        return rows

    # Common retained earnings codes we care about.
    wanted = {"3660", "3680", "3700", "3740", "3849", "3600", "3500", "3620"}
    for m in re.finditer(r"(?m)^\s*(\d{4})\s+.*?([-]?\(?[\d,]+\)?)\s*$", page_text):
        code = m.group(1)
        if code not in wanted:
            continue
        amt = normalize_amount(m.group(2))
        if not re.fullmatch(r"-?[\d,]+", amt):
            continue
        # Keep description blank here; retained earnings line labels vary in export formatting.
        rows.append(Row(code=code, description="", amount=amt, page=page_number, section="retained_earnings"))
    return rows


def parse_diagnostics_from_text(full_text: str) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for line in full_text.splitlines():
        s = line.strip()
        if not s:
            continue
        if "GIFI-FIELD" in s or re.search(r"\bDiagnostics page\b", s, re.IGNORECASE):
            out.append({"line": s})
        elif re.search(r"\b(ineligible|error|warning)\b", s, re.IGNORECASE):
            out.append({"line": s})
    return out


def write_rows_csv(path: Path, rows: Iterable[Row]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["code", "description", "amount", "page", "section"])
        for r in rows:
            w.writerow([r.code, r.description, r.amount, r.page, r.section])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True, help="Path to UFile-exported PDF")
    ap.add_argument("--out", required=True, help="Output directory under T2Analysis/")
    args = ap.parse_args()

    pdf_path = Path(args.pdf).resolve()
    out_dir = Path(args.out).resolve()

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "text").mkdir(parents=True, exist_ok=True)
    (out_dir / "tables").mkdir(parents=True, exist_ok=True)

    try:
        import pdfplumber  # type: ignore
    except Exception as e:
        raise SystemExit(
            "pdfplumber is required. Create a venv and install requirements.txt. "
            f"Import error: {e}"
        )

    pdf_hash = sha256_file(pdf_path)
    meta = {
        "parser": "T2Analysis/tools/ufile_pdf_parser/parse_ufile_pdf.py",
        "parser_version": "1",
        "source_pdf": str(pdf_path),
        "source_sha256": pdf_hash,
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    full_text_parts: list[str] = []
    schedule_100_rows: list[Row] = []
    schedule_125_rows: list[Row] = []
    retained_rows: list[Row] = []

    with pdfplumber.open(str(pdf_path)) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            full_text_parts.append(text)
            (out_dir / "text" / "pages").mkdir(parents=True, exist_ok=True)
            (out_dir / "text" / "pages" / f"page_{i:03d}.txt").write_text(text + "\n", encoding="utf-8")

            section = detect_section(text)
            words = page.extract_words(use_text_flow=True, keep_blank_chars=False) or []
            lines = group_words_into_lines(words)

            if section == "schedule_100":
                schedule_100_rows.extend(parse_gifi_lines_from_words(lines, i, section))
                retained_rows.extend(parse_retained_earnings_from_text(text, i))
            elif section == "schedule_125":
                schedule_125_rows.extend(parse_gifi_lines_from_words(lines, i, section))
            else:
                retained_rows.extend(parse_retained_earnings_from_text(text, i))

    full_text = "\n\n".join(full_text_parts)
    (out_dir / "text" / "full_text.txt").write_text(full_text + "\n", encoding="utf-8")

    write_rows_csv(out_dir / "tables" / "schedule_100.csv", schedule_100_rows)
    write_rows_csv(out_dir / "tables" / "schedule_125.csv", schedule_125_rows)
    write_rows_csv(out_dir / "tables" / "retained_earnings.csv", retained_rows)

    diag = parse_diagnostics_from_text(full_text)
    with (out_dir / "tables" / "diagnostics.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["line"])
        for d in diag:
            w.writerow([d["line"]])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

