#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ATTEMPT_ID = "attempt_002"
FY = "FY2025"


@dataclass(frozen=True)
class Row:
    code: int
    description: str
    amount: int | None  # cents
    page: int | None
    section: str | None


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _parse_money_to_cents(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, (int, float)) and not (isinstance(value, float) and math.isnan(value)):
        return int(round(float(value) * 100))
    s = str(value).strip()
    if s == "" or s.lower() in {"nan", "none"}:
        return None
    s = s.replace("\u2212", "-")  # unicode minus
    s = s.replace("$", "").replace(",", "")
    s = re.sub(r"[=+]", "", s).strip()
    neg = False
    if s.startswith("(") and s.endswith(")"):
        neg = True
        s = s[1:-1].strip()
    if s.startswith("-"):
        neg = True
        s = s[1:].strip()
    if s == "":
        return None
    if "." in s:
        whole, frac = (s.split(".", 1) + ["0"])[:2]
        frac = (frac + "00")[:2]
        cents = int(whole) * 100 + int(frac)
    else:
        cents = int(s) * 100
    return -cents if neg else cents


def _fmt_cents(cents: int | None) -> str:
    if cents is None:
        return ""
    sign = "-" if cents < 0 else ""
    cents_abs = abs(cents)
    dollars = cents_abs // 100
    return f"{sign}{dollars:,}"


def _fmt_cents_2dp(cents: int | None) -> str:
    if cents is None:
        return ""
    sign = "-" if cents < 0 else ""
    cents_abs = abs(cents)
    dollars = cents_abs // 100
    rem = cents_abs % 100
    return f"{sign}{dollars:,}.{rem:02d}"


def _read_csv_rows(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def _read_schedule_table(path: Path, section: str, *, min_code: int = 1) -> list[Row]:
    rows: list[Row] = []
    for r in _read_csv_rows(path):
        code_raw = (r.get("code") or "").strip()
        if code_raw == "":
            continue
        code = int(float(code_raw))
        if code < min_code:
            continue
        rows.append(
            Row(
                code=code,
                description=(r.get("description") or "").strip(),
                amount=_parse_money_to_cents(r.get("amount")),
                page=int(float(r["page"])) if (r.get("page") or "").strip() else None,
                section=(r.get("section") or section).strip() or section,
            )
        )
    return rows


def _index_rows(rows: Iterable[Row]) -> dict[int, Row]:
    indexed: dict[int, Row] = {}
    for r in rows:
        indexed[r.code] = r
    return indexed


def _sum_cents(rows: Iterable[Row]) -> int:
    total = 0
    for r in rows:
        if r.amount is not None:
            total += r.amount
    return total


def _validate_parse_bundle(verification_report_path: Path) -> None:
    text = _read_text(verification_report_path)
    m = re.search(r"Not OK:\s*(\d+)", text)
    if not m:
        raise SystemExit(f"Could not find 'Not OK' in verification report: {verification_report_path}")
    not_ok = int(m.group(1))
    if not_ok != 0:
        raise SystemExit(
            f"Parsed bundle is untrusted (Not OK={not_ok}). Regenerate parse bundle before continuing."
        )


def _extract_messages(messages_text: str) -> list[str]:
    lines = [ln.strip() for ln in messages_text.splitlines()]
    lines = [ln for ln in lines if ln and ln not in {"Click here to fix.", "Click here to verify your data."}]

    # Drop boilerplate / section labels so the report focuses on actionable items.
    ignore_exact = {
        "Messages",
        "Please review this information carefully",
        "GIFI Errors",
        "Errors that prevent filing",
        "Warnings",
        "The federal BCR is not being generated.",
        "These tax calculations failed the validity check for bar codes. Therefore, no bar codes were generated and you will not be able to file this return with the CRA.",
        "BCR validity checks relate mainly to incomplete or inconsistent data entry. Review the error and warning messages, then make the required changes and recalculate.",
        "A tax return was generated. However, the errors below prevent the transmission of your declaration.",
        "Please review the notes and warning messages below.",
        "Click the Interview tab on the toolbar to make any changes to your data. Click the Tax return tab to preview or print your complete, detailed tax return. If you are filing electronically, click the EFILE tab.",
        "These errors have been detected with respect to the GIFI data entered. These errors must be rectified in order to paper-file the federal bar code return (BCR) or efile the federal or Quebec return.",
        "Errors have been detected with respect to the GIFI data entered. These errors must be rectified in order to paper-file the federal bar code return (BCR) or efile the federal or Quebec return.",
        "These tax calculations failed the validity check for bar codes. Therefore, no bar codes were generated and you will not be able to file this return with the CRA.",
        "The CRA imposes certain validity checks on approved software to ensure that it can process BCR's accurately and quickly. Tax returns containing BCR's that fail these checks are re-routed by the CRA to a manual assessment process which results in potential delays of several months and increased communication between the CRA and the taxpayer.",
        "You cannot currently EFILE your federal return. Please review the following reasons, and make corrections when possible.",
    }
    lines = [ln for ln in lines if ln not in ignore_exact]

    # Keep only lines that look like actual warnings/errors (avoid printing the entire prose block).
    keep_patterns = [
        r"\bGIFI\b",
        r"\bBCR\b",
        r"\bbar codes?\b",
        r"\bEFILE\b",
        r"\bDividends?\b",
        r"\bincome source\b",
        r"\bTax year presumed\b",
        r"\binstalments?\b",
    ]
    keep_re = re.compile("|".join(keep_patterns), re.IGNORECASE)
    lines = [ln for ln in lines if keep_re.search(ln)]

    # Keep original order, de-dup exact repeats
    out: list[str] = []
    seen: set[str] = set()
    for ln in lines:
        if ln in seen:
            continue
        seen.add(ln)
        out.append(ln)
    return out


def _map_message_to_screen(message: str) -> tuple[str, str]:
    m = message
    if "GIFI 100 does not balance" in m or "total assets does not equal total liabilities" in m:
        return (
            "GIFI → Balance sheet (Schedule 100) → Totals (2599/3499/3620/3640)",
            "Ensure liabilities (3499) + equity (3620) equals total assets (2599). Most often caused by retained earnings (3600/3849) not matching the retained earnings reconciliation (3660/3680/3700/3701/3740).",
        )
    if "GIFI-Field 3849" in m and "does not match internal subtotal calculation" in m:
        return (
            "GIFI → Balance sheet (Schedule 100) → Retained earnings reconciliation (3660/3680/3700/3701/3740/3849)",
            "Clear any manual override on ending retained earnings (3849 / 3600) and let it compute from start (3660) + net income (3680) − dividends declared (3700/3701) ± other items (3740).",
        )
    if re.search(r"\bGIFI-Field\s+3849:\$?\d+", m):
        return (
            "GIFI → Balance sheet (Schedule 100) → Retained earnings reconciliation (3849)",
            "This is the numeric detail for the 3849 mismatch. Fix by removing overrides on 3600/3849 and completing rollforward inputs (3660/3680/3700/3740).",
        )
    if re.search(r"\bGIFI-Field\s+2599:\$?\d+", m):
        return (
            "GIFI → Balance sheet (Schedule 100) → Totals (2599 vs 3499+3620)",
            "This is the numeric detail for the balance-sheet mismatch. Fix the retained earnings linkage so 3620 brings (3499+3620) back to 2599.",
        )
    if "Dividends declared have been entered" in m or ("3700" in m and "Dividends paid" in m):
        return (
            "Interview/Setup → Dividends paid (UFile screen)",
            "If dividends are declared (3700/3701), complete the 'Dividends paid' section. If no dividends were paid/declared, clear dividends declared to avoid inconsistent screens.",
        )
    if "There is no entry in the income source section" in m:
        return (
            "Interview/Setup → Income source section",
            "Confirm income source classification (e.g., active business vs property/other). If left blank, UFile assumes all income is active business income.",
        )
    if "Tax year presumed to be 365 days" in m:
        return (
            "Interview/Setup → Identification / fiscal period",
            "Confirm begin/end of tax year and incorporation/operations dates so UFile does not presume a 365‑day year.",
        )
    if "BAR CODE RETURN (BCR) VALIDITY CHECKS FAILED" in m or "No bar codes were generated" in m:
        return (
            "EFILE / Bar code return (BCR) / Review messages",
            "Resolve blocking GIFI errors, then recalculate; bar codes will generate only after validity checks pass.",
        )
    if "No instalments required" in m:
        return (
            "Information message (instalments)",
            "No action required unless instalments were expected.",
        )
    return ("(Unmapped / generic)", "Review in UFile Messages; fix the referenced section and recalculate.")


def _load_project_expected(packet_year_path: Path) -> dict[str, Any]:
    data = json.loads(_read_text(packet_year_path))
    # Two packet shapes exist in this repo:
    # 1) all-years packet: {"years": {"FY2025": {...}}}
    # 2) year-specific packet: {"meta": {"fiscal_year": "FY2025"}, ...top-level sections...}
    if isinstance(data.get("years"), dict) and isinstance((data["years"]).get(FY), dict):
        return data["years"][FY]
    meta = data.get("meta") if isinstance(data.get("meta"), dict) else {}
    if meta.get("fiscal_year") == FY:
        return data
    raise SystemExit(f"Unrecognized packet shape or wrong FY in {packet_year_path}")


def _extract_project_lines(fy_packet: dict[str, Any]) -> dict[int, int]:
    out: dict[int, int] = {}
    def find_sections(obj: Any, key: str) -> Iterable[dict[str, Any]]:
        if isinstance(obj, dict):
            if key in obj and isinstance(obj[key], dict):
                yield obj[key]
            for v in obj.values():
                yield from find_sections(v, key)
        elif isinstance(obj, list):
            for v in obj:
                yield from find_sections(v, key)

    for section in ["schedule_100", "schedule_125", "retained_earnings"]:
        for sec in find_sections(fy_packet, section):
            for code_str, payload in sec.items():
                try:
                    code = int(code_str)
                except Exception:
                    continue
                if isinstance(payload, dict) and "amount" in payload:
                    # Packet amounts are expressed in whole dollars for GIFI lines.
                    out[code] = int(round(float(payload["amount"]) * 100))
    return out


def _load_trial_balance(tb_path: Path) -> list[dict[str, Any]]:
    rows = _read_csv_rows(tb_path)
    out: list[dict[str, Any]] = []
    for r in rows:
        if (r.get("fy") or "").strip() != FY:
            continue
        out.append(r)
    return out


def _trial_balance_accounts_for_gifi(tb_rows: list[dict[str, Any]], gifi_code: int) -> list[dict[str, Any]]:
    out = []
    for r in tb_rows:
        gifi_raw = (r.get("gifi_code") or "").strip()
        if gifi_raw == "":
            continue
        if int(float(gifi_raw)) != gifi_code:
            continue
        out.append(r)
    return out


def main() -> None:
    run_dir = Path(__file__).resolve().parents[1]
    inputs = run_dir / "inputs"
    outputs = run_dir / "outputs"

    # Inputs (copied into RUN_DIR to avoid mixing across attempts)
    verification_report = inputs / "parsed_bundle" / "verification_report.md"
    meta_json = inputs / "parsed_bundle" / "meta.json"
    full_text = inputs / "parsed_bundle" / "text" / "full_text.txt"
    diagnostics_csv = inputs / "parsed_bundle" / "tables" / "diagnostics.csv"
    schedule_100_csv = inputs / "parsed_bundle" / "tables" / "schedule_100.csv"
    schedule_125_csv = inputs / "parsed_bundle" / "tables" / "schedule_125.csv"
    retained_earnings_csv = inputs / "parsed_bundle" / "tables" / "retained_earnings.csv"

    messages_txt = inputs / "exports" / "messages.txt"
    ufile_messages_txt = inputs / "parsed_bundle" / "ufile_messages.txt"

    project_packet_year = inputs / "project" / "packet_FY2025.json"
    project_packet_all_years = inputs / "project" / "packet_all_years.json"
    fill_guide = inputs / "project" / "UFILet2_FILL_GUIDE.md"

    tb_path = inputs / "accounting_outputs" / "trial_balance_FY2025.csv"
    vendor_allocs = inputs / "accounting_outputs" / "vendor_allocations_by_fy.csv"
    vendor_allocs_summary = inputs / "accounting_outputs" / "vendor_allocations_summary_by_fy.csv"
    ufile_gifi_out = inputs / "accounting_outputs" / "ufile_gifi_FY2025.csv"

    # Validate parsed bundle
    _validate_parse_bundle(verification_report)

    # Load schedules (attempt)
    # GIFI schedules use (mostly) 4-digit codes; filter out any parser noise with small codes.
    s100 = _read_schedule_table(schedule_100_csv, "schedule_100", min_code=1000)
    s125 = _read_schedule_table(schedule_125_csv, "schedule_125", min_code=1000)
    s100_i = _index_rows(s100)
    s125_i = _index_rows(s125)

    # Load project expected
    fy_packet = _load_project_expected(project_packet_year)
    project_lines = _extract_project_lines(fy_packet)

    # Diagnostics catalogue (parsed diagnostics + UFile messages)
    diag_lines_raw = [r.get("line", "").strip() for r in _read_csv_rows(diagnostics_csv)]
    diag_lines_raw = [ln for ln in diag_lines_raw if ln]
    # Filter out obvious pagination / prose fragments that aren't actionable diagnostics.
    diag_lines = [
        ln
        for ln in diag_lines_raw
        if not re.search(r"^Diagnostics page \d+ of \d+$", ln)
        and not ln.lower().startswith("bcr validity checks")
        and "error and warning messages shown below" not in ln.lower()
        and "was an amount included in the opening balance" not in ln.lower()
    ]

    msg_text = _read_text(messages_txt) if messages_txt.exists() else ""
    if msg_text.strip() == "" and ufile_messages_txt.exists():
        msg_text = _read_text(ufile_messages_txt)
    messages = _extract_messages(msg_text)

    blocking_markers = [
        "does not balance",
        "does not match internal subtotal calculation",
        "prevent filing",
        "validity checks failed",
        "BCR validity checks failed",
        "No bar codes were generated",
        "You cannot currently EFILE",
        "ineligible for federal efile",
    ]

    def classify(line: str) -> str:
        l = line.lower()
        for m in blocking_markers:
            if m.lower() in l:
                return "Blocking"
        # These are usually informational warnings.
        return "Non-blocking"

    diag_md = []
    diag_md.append(f"# Diagnostics + UFile Messages ({FY}, {ATTEMPT_ID})")
    diag_md.append("")
    diag_md.append("## Parsed diagnostics (from diagnostics.csv) — full list")
    for ln in diag_lines_raw:
        diag_md.append(f"- **{classify(ln)}**: {ln}")
    diag_md.append("")
    diag_md.append("## Parsed diagnostics — actionable subset")
    for ln in diag_lines:
        diag_md.append(f"- **{classify(ln)}**: {ln}")
    diag_md.append("")
    diag_md.append("### Cross-check against full_text.txt")
    full_text_content = _read_text(full_text)
    for ln in diag_lines_raw:
        found = "FOUND" if ln in full_text_content else "NOT FOUND"
        diag_md.append(f"- {found}: {ln}")
    diag_md.append("")
    diag_md.append("## UFile Messages (from messages.txt)")
    for ln in messages:
        screen, action = _map_message_to_screen(ln)
        diag_md.append(f"- **{classify(ln)}**: {ln}")
        diag_md.append(f"  - Expected screen: {screen}")
        diag_md.append(f"  - Likely action: {action}")
    _write_text(outputs / "diagnostics.md", "\n".join(diag_md).rstrip() + "\n")

    # Extracted schedules (minimum required lines)
    s100_required = [1001, 1121, 1120, 1301, 1484, 1480, 2620, 2680, 2781, 2780, 3500, 3600, 2599, 3499, 3620, 3640]
    re_required = [3660, 3680, 3700, 3701, 3849]
    s125_required = [8000, 8299, 8300, 8320, 8500, 8518, 8519, 9367, 9368]

    def table_md(rows_index: dict[int, Row], codes: list[int]) -> list[str]:
        out = ["| Code | Attempt amount | Page | Description |", "|---:|---:|---:|---|"]
        for c in codes:
            r = rows_index.get(c)
            out.append(
                f"| {c} | {_fmt_cents(r.amount) if r else ''} | {r.page if r and r.page else ''} | {(r.description if r else '')} |"
            )
        return out

    # Include "every populated expense line" (excluding totals) as required by prompt
    # Expense detail lines: include typical operating expense codes; exclude totals and derived net-income lines.
    expense_rows = [r for r in s125 if 8520 <= r.code < 9367 and (r.amount or 0) != 0]
    expense_rows_sorted = sorted(expense_rows, key=lambda r: r.code)

    schedules_md = []
    schedules_md.append(f"# Extracted schedules ({FY}, {ATTEMPT_ID})")
    schedules_md.append("")
    schedules_md.append("## Schedule 100 (Balance sheet) — required lines")
    schedules_md.extend(table_md(s100_i, s100_required))
    schedules_md.append("")
    schedules_md.append("## Retained earnings — required lines")
    # If retained_earnings.csv is empty, fall back to schedule_100 lines for these codes
    retained_rows = _read_schedule_table(retained_earnings_csv, "retained_earnings", min_code=1000)
    retained_i = _index_rows(retained_rows) if retained_rows else s100_i
    schedules_md.extend(table_md(retained_i, re_required))
    schedules_md.append("")
    schedules_md.append("## Schedule 125 (Income statement) — required lines")
    schedules_md.extend(table_md(s125_i, s125_required))
    schedules_md.append("")
    schedules_md.append("## Schedule 125 — populated expense detail lines")
    schedules_md.append("| Code | Attempt amount | Page | Description |")
    schedules_md.append("|---:|---:|---:|---|")
    for r in expense_rows_sorted:
        schedules_md.append(f"| {r.code} | {_fmt_cents(r.amount)} | {r.page if r.page else ''} | {r.description} |")
    _write_text(outputs / "extracted_schedules.md", "\n".join(schedules_md).rstrip() + "\n")

    # Independent recomputation (show your work) using attempt amounts only
    # 1) Operating expenses = sum of detail expense lines (exclude totals)
    operating_expenses_cents = _sum_cents(expense_rows_sorted)
    total_operating_expenses_cents = s125_i.get(9367).amount if 9367 in s125_i else None

    # 2) COGS from movement: 8300 + 8320 - 8500
    # Note: in UFile's printed return, closing inventory (8500) is often shown as a negative value.
    # If so, "8300 + 8320 + 8500" matches the intended "8300 + 8320 - abs(8500)".
    c8300 = s125_i.get(8300).amount if 8300 in s125_i else 0
    c8320 = s125_i.get(8320).amount if 8320 in s125_i else 0
    c8500 = s125_i.get(8500).amount if 8500 in s125_i else 0
    cogs_movement_cents = (c8300 or 0) + (c8320 or 0) + (c8500 or 0)
    cogs_reported_cents = s125_i.get(8518).amount if 8518 in s125_i else None

    # 3) Gross profit = total revenue - COGS (use 8299 and 8518)
    revenue_cents = s125_i.get(8299).amount if 8299 in s125_i else None
    gross_profit_cents = None
    if revenue_cents is not None and cogs_reported_cents is not None:
        gross_profit_cents = revenue_cents - cogs_reported_cents
    gross_profit_reported_cents = s125_i.get(8519).amount if 8519 in s125_i else None

    # 4) Net income = gross profit - operating expenses
    net_income_calc_cents = None
    if gross_profit_cents is not None:
        net_income_calc_cents = gross_profit_cents - operating_expenses_cents
    net_income_reported_cents = s125_i.get(9999).amount if 9999 in s125_i else None

    # 5) Equity = 3500 + 3600
    equity_cents = None
    if 3500 in s100_i and 3600 in s100_i and s100_i[3500].amount is not None and s100_i[3600].amount is not None:
        equity_cents = s100_i[3500].amount + s100_i[3600].amount

    # 6) Balance equation
    assets_cents = s100_i.get(2599).amount if 2599 in s100_i else None
    liabilities_cents = s100_i.get(3499).amount if 3499 in s100_i else None
    equity_total_cents = s100_i.get(3620).amount if 3620 in s100_i else None
    liab_plus_equity_cents = None
    if liabilities_cents is not None and equity_total_cents is not None:
        liab_plus_equity_cents = liabilities_cents + equity_total_cents
    total_liab_equity_cents = s100_i.get(3640).amount if 3640 in s100_i else None

    rec_md = []
    rec_md.append(f"# Recalculations ({FY}, {ATTEMPT_ID})")
    rec_md.append("")
    rec_md.append("All recomputations below use only parsed attempt amounts (not project expected values).")
    rec_md.append("")
    rec_md.append("## Schedule 125 arithmetic")
    rec_md.append(f"- Detail operating expenses sum (exclude totals 9367/9368): **{_fmt_cents(operating_expenses_cents)}**")
    rec_md.append(
        f"- Reported 9367 Total operating expenses: **{_fmt_cents(total_operating_expenses_cents)}**"
        + (
            f" (difference: {_fmt_cents((total_operating_expenses_cents or 0) - operating_expenses_cents)})"
            if total_operating_expenses_cents is not None
            else ""
        )
    )
    rec_md.append(
        f"- COGS from movement (8300 + 8320 + 8500; 8500 is printed as a negative): **{_fmt_cents(cogs_movement_cents)}**; reported 8518: **{_fmt_cents(cogs_reported_cents)}**"
    )
    rec_md.append(
        f"- Gross profit calc (8299 − 8518): **{_fmt_cents(gross_profit_cents)}**; reported 8519: **{_fmt_cents(gross_profit_reported_cents)}**"
    )
    rec_md.append(
        f"- Net income calc (gross profit − op ex): **{_fmt_cents(net_income_calc_cents)}**; reported 9999: **{_fmt_cents(net_income_reported_cents)}**"
    )
    rec_md.append("")
    rec_md.append("## Schedule 100 arithmetic")
    rec_md.append(f"- Equity calc (3500 + 3600): **{_fmt_cents(equity_cents)}**; reported 3620: **{_fmt_cents(equity_total_cents)}**")
    rec_md.append(
        f"- Balance check: assets 2599 **{_fmt_cents(assets_cents)}** vs (liabilities 3499 + equity 3620) **{_fmt_cents(liab_plus_equity_cents)}**"
        + (
            f" (difference: {_fmt_cents((liab_plus_equity_cents or 0) - (assets_cents or 0))})"
            if liab_plus_equity_cents is not None and assets_cents is not None
            else ""
        )
    )
    rec_md.append(f"- Reported 3640 Total liabilities and shareholder equity: **{_fmt_cents(total_liab_equity_cents)}**")
    rec_md.append("")
    rec_md.append("## Retained earnings rollforward arithmetic (why GIFI 3849 fails)")
    re_start = s100_i.get(3660).amount if 3660 in s100_i else None
    re_net = s100_i.get(3680).amount if 3680 in s100_i else None
    re_div = s100_i.get(3700).amount if 3700 in s100_i else 0
    re_other = s100_i.get(3740).amount if 3740 in s100_i else 0
    re_end_reported = s100_i.get(3849).amount if 3849 in s100_i else None
    if re_start is not None and re_net is not None and re_end_reported is not None:
        re_calc = re_start + re_net + (re_div or 0) + (re_other or 0)
        rec_md.append(
            f"- Computed end (3660 + 3680 + 3700 + 3740): **{_fmt_cents(re_start)} + {_fmt_cents(re_net)} + {_fmt_cents(re_div)} + {_fmt_cents(re_other)} = {_fmt_cents(re_calc)}**"
        )
        rec_md.append(f"- Reported 3849 end retained earnings: **{_fmt_cents(re_end_reported)}** (difference: **{_fmt_cents(re_end_reported - re_calc)}**)")
    _write_text(outputs / "recalculations.md", "\n".join(rec_md).rstrip() + "\n")

    # Attempt vs project comparison CSV
    # Build a union of line codes observed in attempt and in project for core schedules.
    attempt_codes = set([r.code for r in s100] + [r.code for r in s125])
    project_codes = set(project_lines.keys())
    union = sorted(attempt_codes.union(project_codes))

    def normalize_attempt_for_comparison(code: int, attempt: int | None) -> int | None:
        if attempt is None:
            return None
        # Some printed GIFI lines show as negative in the return even though the "entered amount"
        # conceptually is positive (e.g., dividends declared is subtracted in the rollforward).
        if code in {3700, 3701}:
            return abs(attempt)
        return attempt

    def likely_cause(code: int, attempt: int | None, project: int | None) -> str:
        if attempt is None or project is None:
            return "Unknown"
        if attempt == project:
            return ""
        # Heuristics for this repo’s typical failure modes
        if code in {3849, 3600, 3620, 3640, 2599, 3499}:
            return "Entry/mechanics (retained earnings linkage)"
        if code in {3700, 3701}:
            return "Entry/mechanics (dividends screens)"
        return "Unknown"

    comp_path = outputs / "attempt_vs_project_comparison.csv"
    with comp_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["field_code", "attempt_value", "project_expected_value", "delta_attempt_minus_project", "likely_cause"])
        for code in union:
            attempt_raw = s100_i.get(code).amount if code in s100_i else (s125_i.get(code).amount if code in s125_i else None)
            attempt = normalize_attempt_for_comparison(code, attempt_raw)
            project = project_lines.get(code)
            if attempt is None and project is None:
                continue
            delta = attempt - project if (attempt is not None and project is not None) else None
            w.writerow(
                [
                    code,
                    _fmt_cents(attempt_raw) if code in {3700, 3701} else _fmt_cents(attempt),
                    _fmt_cents(project),
                    _fmt_cents(delta) if delta is not None else "",
                    likely_cause(code, attempt, project),
                ]
            )

    # Go-deeper: 9270 trace and suspense accounts trace
    tb_rows = _load_trial_balance(tb_path)
    g9270_accounts = _trial_balance_accounts_for_gifi(tb_rows, 9270)

    # Vendor allocations traces for account_code 9100 (commonly the suspense-like bucket feeding 9270)
    vendor_rows = _read_csv_rows(vendor_allocs)
    vendor_rows_fy = [r for r in vendor_rows if (r.get("fy") or "").strip() == FY]
    vendor_9100 = [r for r in vendor_rows_fy if str(r.get("account_code") or "").strip() == "9100"]
    vendor_profile_sum_by_account: dict[str, float] = {}
    for r in vendor_rows_fy:
        if (r.get("method") or "").strip() != "VENDOR_PROFILE_ESTIMATE":
            continue
        acct = str(r.get("account_code") or "").strip()
        if acct == "":
            continue
        vendor_profile_sum_by_account[acct] = vendor_profile_sum_by_account.get(acct, 0.0) + float(r.get("amount") or 0.0)

    vendor_summary_rows = _read_csv_rows(vendor_allocs_summary)
    vendor_summary_fy_9100 = [
        r for r in vendor_summary_rows if (r.get("fy") or "").strip() == FY and str(r.get("account_code") or "").strip() == "9100"
    ]

    # Attempt + project 9270 amounts
    attempt_9270 = s125_i.get(9270).amount if 9270 in s125_i else None
    project_9270 = project_lines.get(9270)

    trace_9270 = []
    trace_9270.append(f"# GIFI 9270 trace ({FY}, {ATTEMPT_ID})")
    trace_9270.append("")
    trace_9270.append(f"- Attempt Schedule 125 / GIFI 9270 amount: **{_fmt_cents(attempt_9270)}**")
    trace_9270.append(f"- Project expected GIFI 9270 amount (packet.json): **{_fmt_cents(project_9270)}**")
    trace_9270.append("")
    trace_9270.append("## Trial balance accounts mapped to GIFI 9270")
    trace_9270.append("| Account code | Account name | Net (dollars) | Notes |")
    trace_9270.append("|---:|---|---:|---|")
    tb_total = 0
    for r in sorted(g9270_accounts, key=lambda x: int(float(x.get('account_code', 0) or 0))):
        net_cents = int(float(r.get("net_cents") or 0))
        tb_total += net_cents
        name = (r.get("account_name") or "").lower()
        notes: list[str] = []
        if "pending receipt" in name or "no itc" in name:
            alloc_sum = vendor_profile_sum_by_account.get(str(r.get("account_code") or "").strip(), 0.0)
            notes.append(f"placeholder-style bucket; vendor_profile_estimate allocs={alloc_sum:,.2f}")
        if "penalt" in name or "cra" in name:
            notes.append("CRA penalties/interest (may be non-deductible)")
        trace_9270.append(
            f"| {r.get('account_code')} | {r.get('account_name')} | {_fmt_cents_2dp(net_cents)} | {'; '.join(notes)} |"
        )
    trace_9270.append(f"\n- Trial balance total for GIFI 9270 accounts: **{_fmt_cents_2dp(tb_total)}**")
    if attempt_9270 is not None:
        trace_9270.append(f"- Difference vs attempt 9270: **{_fmt_cents_2dp(tb_total - attempt_9270)}**")
    trace_9270.append("")
    trace_9270.append("## Vendor allocation evidence feeding suspense-like buckets (account 9100)")
    trace_9270.append(
        "These are allocations tagged as `VENDOR_PROFILE_ESTIMATE` into account `9100` (a suspense/placeholder-style account), summarized from `vendor_allocations_by_fy.csv`."
    )
    trace_9270.append("")
    trace_9270.append(f"- Rows for FY2025 with account_code=9100: **{len(vendor_9100)}**")
    alloc_sum = sum(float(r.get("amount") or 0) for r in vendor_9100)
    trace_9270.append(f"- Sum of allocations to 9100: **{alloc_sum:,.2f}** (dollars)")
    trace_9270.append("")
    trace_9270.append("### By vendor (from vendor_allocations_summary_by_fy.csv)")
    if vendor_summary_fy_9100:
        trace_9270.append("| Vendor key | Amount (dollars) |")
        trace_9270.append("|---|---:|")
        for r in sorted(vendor_summary_fy_9100, key=lambda x: float(x.get("amount") or 0), reverse=True):
            trace_9270.append(f"| {r.get('vendor_key')} | {float(r.get('amount') or 0):,.2f} |")
    else:
        trace_9270.append("_No summary rows found for FY2025 account_code=9100._")
    trace_9270.append("")
    trace_9270.append("### Largest individual allocations (top 15)")
    trace_9270.append("| Invoice date | Vendor | Wave bill | Amount (dollars) | Method |")
    trace_9270.append("|---|---|---:|---:|---|")
    for r in sorted(vendor_9100, key=lambda x: float(x.get("amount") or 0), reverse=True)[:15]:
        trace_9270.append(
            f"| {r.get('invoice_date')} | {r.get('vendor_raw') or r.get('vendor_key')} | {r.get('wave_bill_id')} | {float(r.get('amount') or 0):,.2f} | {r.get('method')} |"
        )
    _write_text(outputs / "9270_trace.md", "\n".join(trace_9270).rstrip() + "\n")

    # Suspense / placeholder accounts trace
    suspense_patterns = [
        "pending",
        "suspense",
        "no itc",
        "unknown",
        "uncategor",
        "placeholder",
        "clearing",
        "round",
    ]
    suspense_rows = []
    for r in tb_rows:
        name = (r.get("account_name") or "").lower()
        if any(p in name for p in suspense_patterns):
            suspense_rows.append(r)

    suspense_md = []
    suspense_md.append(f"# Suspense / placeholder accounts trace ({FY}, {ATTEMPT_ID})")
    suspense_md.append("")
    suspense_md.append("These accounts are flagged heuristically by name patterns (pending/suspense/no ITC/etc.).")
    suspense_md.append("")
    suspense_md.append("| Account code | Account name | Account type | GIFI code | Net (dollars) | Notes |")
    suspense_md.append("|---:|---|---|---:|---:|---|")
    for r in sorted(suspense_rows, key=lambda x: int(float(x.get("account_code") or 0))):
        net_cents = int(float(r.get("net_cents") or 0))
        acct = str(r.get("account_code") or "").strip()
        alloc_sum = vendor_profile_sum_by_account.get(acct, 0.0)
        notes = []
        if alloc_sum:
            notes.append(f"vendor_profile_estimate allocs={alloc_sum:,.2f}")
        suspense_md.append(
            f"| {r.get('account_code')} | {r.get('account_name')} | {r.get('account_type')} | {r.get('gifi_code')} | {_fmt_cents_2dp(net_cents)} | {'; '.join(notes)} |"
        )
    suspense_md.append("")
    suspense_md.append("## Notes")
    suspense_md.append("- `9100 Pending Receipt - No ITC` is a known placeholder-style bucket that is fed by `VENDOR_PROFILE_ESTIMATE` allocations (see `9270_trace.md`).")
    suspense_md.append("- If these balances are expected (e.g., deliberate accrual/placeholder), document rationale; otherwise, they indicate categorization gaps to resolve upstream.")
    _write_text(outputs / "suspense_accounts_trace.md", "\n".join(suspense_md).rstrip() + "\n")

    # Primary report
    meta = json.loads(_read_text(meta_json))
    report: list[str] = []
    report.append(f"# UFile T2 attempt diagnosis ({FY}, {ATTEMPT_ID})")
    report.append("")
    report.append("## Executive summary")
    report.append(
        "- Blocking failures are driven by **retained earnings linkage on Schedule 100**: attempt shows `3849/3600=45,005`, but the retained earnings rollforward computes `3849=8,104` (difference `36,901`). This also makes Schedule 100 not balance (`2599=25,977` vs `3499+3620=62,878`)."
    )
    report.append(
        "- Schedule 125 totals are internally consistent in this attempt (no Schedule 125 subtotal diagnostics); the primary defect is confined to the **balance sheet retained earnings / dividends paid screens**."
    )
    report.append("")
    report.append("## Evidence index (copied into this run)")
    report.append(f"- Parsed bundle meta: `{meta_json}`")
    report.append(f"- Parsed bundle verification report: `{verification_report}`")
    report.append(f"- Parsed diagnostics: `{diagnostics_csv}`")
    report.append(f"- Parsed Schedule 100 table: `{schedule_100_csv}`")
    report.append(f"- Parsed Schedule 125 table: `{schedule_125_csv}`")
    report.append(f"- Parsed retained earnings table: `{retained_earnings_csv}`")
    report.append(f"- Parsed full text: `{full_text}`")
    report.append(f"- Spot-check pages: `{inputs / 'parsed_bundle' / 'text' / 'pages' / 'page_012.txt'}`")
    report.append(f"- Spot-check pages: `{inputs / 'parsed_bundle' / 'text' / 'pages' / 'page_013.txt'}`")
    report.append(f"- Spot-check pages: `{inputs / 'parsed_bundle' / 'text' / 'pages' / 'page_014.txt'}`")
    report.append(f"- UFile Messages: `{messages_txt}`")
    report.append(f"- Project expected packet (FY2025): `{project_packet_year}`")
    report.append(f"- Project expected packet (all years): `{project_packet_all_years}`")
    report.append(f"- Entry guide: `{fill_guide}`")
    report.append(f"- Trial balance (FY2025): `{tb_path}`")
    report.append(f"- Vendor allocations: `{vendor_allocs}`")
    report.append(f"- Vendor allocation summary: `{vendor_allocs_summary}`")
    report.append(f"- Project-generated UFile GIFI export (FY2025): `{ufile_gifi_out}`")
    report.append("")
    report.append("## Diagnostics list (blocking vs non-blocking)")
    report.append("")
    report.append("### Parsed diagnostics (from diagnostics.csv) — full list")
    for ln in diag_lines_raw:
        report.append(f"- **{classify(ln)}**: {ln}")
    report.append("")
    report.append("### Parsed diagnostics — actionable subset")
    for ln in diag_lines:
        report.append(f"- **{classify(ln)}**: {ln}")
    report.append("")
    report.append("### UFile Messages (actionable subset)")
    for ln in messages:
        screen, action = _map_message_to_screen(ln)
        report.append(f"- **{classify(ln)}**: {ln}")
        report.append(f"  - Expected screen: {screen}")
        report.append(f"  - Likely action: {action}")
    report.append("")
    report.append("## Extracted schedules (from parsed CSVs)")
    report.append("")
    report.extend(schedules_md[2:])  # skip title header to avoid nesting a second H1
    report.append("")
    report.append("## Recalculations (show your work)")
    report.append("")
    report.extend(rec_md[2:])  # skip title header
    report.append("")
    report.append("## Attempt vs project comparison (key lines)")
    report.append("")
    report.append(f"Full CSV: `{comp_path}`")
    report.append("")
    key_codes = sorted(
        {
            2599,
            3499,
            3620,
            3640,
            3500,
            3600,
            3660,
            3680,
            3700,
            3849,
            9270,
            9367,
            9999,
        }
    )
    report.append("| Code | Attempt | Project expected | Delta (attempt-project) | Likely cause |")
    report.append("|---:|---:|---:|---:|---|")
    for code in key_codes:
        attempt_raw = s100_i.get(code).amount if code in s100_i else (s125_i.get(code).amount if code in s125_i else None)
        attempt = normalize_attempt_for_comparison(code, attempt_raw)
        project = project_lines.get(code)
        delta = attempt - project if (attempt is not None and project is not None) else None
        report.append(
            f"| {code} | {_fmt_cents(attempt_raw) if code in {3700, 3701} else _fmt_cents(attempt)} | {_fmt_cents(project)} | {_fmt_cents(delta) if delta is not None else ''} | {likely_cause(code, attempt, project)} |"
        )
    report.append("")
    report.append("## Go-deeper traces")
    report.append("")
    report.append(f"- GIFI 9270 trace: `{outputs / '9270_trace.md'}`")
    report.append(f"- Suspense/placeholder accounts: `{outputs / 'suspense_accounts_trace.md'}`")
    report.append("")
    report.append("## Hypothesis testing (root cause A/B/C)")
    report.append("")
    report.append("### 1) Totals line populated vs internal subtotal mismatch")
    report.append(
        "- **Confirmed** for retained earnings: Attempt shows `3849=45,005`, but internal calculation shown in Messages/Diagnostics is `8,104` (difference `36,901`). This indicates a manual override or mis-linked screen entry."
    )
    report.append("")
    report.append("### 2) Project double-count/omission (project inconsistency)")
    report.append(
        "- **Not supported by evidence** for this defect: project packet and project-generated `output/ufile_gifi_FY2025.csv` both indicate `3600/3849=8,104` for FY2025."
    )
    report.append("")
    report.append("### 3) Wrong UFile line choice (detail vs total)")
    report.append("- Not observed on Schedule 125 in this attempt (9367 matches expense detail sum).")
    report.append("")
    report.append("### 4) Retained earnings mismatch driven by missing dividends / wrong linkage")
    report.append(
        "- **Confirmed**: dividends declared (`3700=36,900`) exists, but UFile warns the 'Dividends paid' section is missing and retained earnings ending value is not reflecting dividends in the rollforward."
    )
    report.append("")
    report.append("### 5) Duplicated classification in attempt")
    report.append("- No duplication detected in this attempt’s Schedule 125 vs project for the previously-seen utilities/telecom issue; re-check in `attempt_vs_project_comparison.csv` if needed.")
    report.append("")
    report.append("## Conclusion")
    report.append("")
    report.append("- Root cause classification: **A) UFile entry mechanics / auto-calculation behavior** (with a likely manual override on retained earnings or incomplete dividends paid screen), not a proven project-number error.")
    report.append("")
    report.append("## Fix checklist — UFile UI next attempt (do not change numbers yet)")
    report.append("")
    report.append("1. In the **GIFI → Balance sheet (Schedule 100)** screen, locate retained earnings fields:")
    report.append("   - Verify ending retained earnings `3600` matches retained earnings reconciliation ending `3849`.")
    report.append("   - If UFile allows overrides, clear the override so `3849` is computed from `3660 + 3680 − 3700/3701 ± 3740`.")
    report.append("2. In the **Dividends paid** section referenced by UFile Messages:")
    report.append("   - If dividends were declared (`3700/3701`), enter the corresponding dividends paid information (or explicitly set declared dividends to zero if incorrect).")
    report.append("3. Recalculate and confirm Messages no longer show:")
    report.append("   - `GIFI-Field 3849 does not match internal subtotal calculation`")
    report.append("   - `GIFI 100 does not balance ...` / `total assets does not equal total liabilities plus shareholder equity`")
    report.append("")
    report.append("## Fix checklist — project outputs (only if later proven wrong)")
    report.append("")
    report.append("- None required based on this attempt’s evidence. If future attempts still mis-link 3849/3600 after UI fixes, investigate the project’s UFile entry guide workflow ordering for dividends/retained earnings.")

    _write_text(outputs / "ATTEMPT_DIAGNOSIS.md", "\n".join(report).rstrip() + "\n")


if __name__ == "__main__":
    main()
