#!/usr/bin/env python3
"""
Validate `packet.json` against the current snapshot outputs (read-only).

This tool is intentionally dependency-free (no jsonschema) and focuses on:
- Amount equality between packet schedules and snapshot CSVs
- Basic tie-check sanity (already included in packet cross_checks)
- Evidence path existence checks
"""

from __future__ import annotations

import csv
import json
import re
import sys
from decimal import Decimal
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "packet.json"


def load_packet() -> dict:
    return json.loads(PACKET_PATH.read_text())


def load_valid_gifi_codes() -> set[str]:
    """
    Treat the UFile copy/paste GIFI lists as the source-of-truth for which GIFI codes are valid.

    This intentionally catches cases where earlier hardcoded mappings accidentally used codes
    from other industries/schedules (e.g., farming-only codes).
    """

    paths = [
        PROJECT_ROOT / "UfileToFill" / "GIFI" / "BalanceSheet.txt",
        PROJECT_ROOT / "UfileToFill" / "GIFI" / "IncomeStatement.txt",
    ]
    pattern = re.compile(r"^\s*(\d{4})\s+")
    codes: set[str] = set()
    for path in paths:
        if not path.exists():
            raise SystemExit(f"Missing GIFI reference list: {path}")
        for raw in path.read_text(encoding="utf-8").splitlines():
            m = pattern.match(raw)
            if not m:
                continue
            codes.add(m.group(1))
    return codes


def load_gifi_csv(path: Path) -> dict[str, int]:
    out: dict[str, int] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = (row.get("GIFI_Code") or row.get("gifi_code") or "").strip()
            if not code:
                continue
            amount_raw = (row.get("Amount") or row.get("amount") or "").strip()
            if amount_raw == "":
                continue
            out[code] = int(Decimal(amount_raw))
    return out


def load_schedule_1_csv(path: Path) -> dict[str, int]:
    out: dict[str, int] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = (row.get("Code") or row.get("Line") or row.get("line") or "").strip()
            if not code:
                continue
            amount_raw = (row.get("Amount") or row.get("amount") or "").strip()
            if amount_raw == "":
                continue
            out[code] = int(Decimal(amount_raw))
    return out


def load_book_fixed_asset_summary(path: Path) -> dict[str, dict[str, int]]:
    if not path.exists():
        return {}
    out: dict[str, dict[str, int]] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fy = str(row.get("fiscal_year") or "").strip()
            if not fy:
                continue
            out[fy] = {
                "capitalized_asset_count": int(row.get("capitalized_asset_count") or 0),
                "expensed_additions_dollars": int(row.get("expensed_additions_dollars") or 0),
                "book_amortization_dollars": int(row.get("book_amortization_dollars") or 0),
            }
    return out


def load_book_fixed_asset_audit(path: Path) -> dict[str, list[dict]]:
    if not path.exists():
        return {}
    out: dict[str, list[dict]] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fy = str(row.get("fiscal_year") or "").strip()
            if not fy:
                continue
            out.setdefault(fy, []).append(row)
    return out


def compare_dicts(label: str, a: dict[str, int], b: dict[str, int]) -> list[str]:
    def sort_key(code: str) -> tuple[int, object]:
        if code == "A":
            return (-2, 0)
        if code == "C":
            return (2, 0)
        if code.isdigit():
            return (0, int(code))
        return (1, code)

    issues: list[str] = []
    all_keys = sorted(set(a) | set(b), key=sort_key)
    for k in all_keys:
        if a.get(k) != b.get(k):
            issues.append(f"{label}: {k}: snapshot={a.get(k)} packet={b.get(k)}")
    return issues


def is_path_like(value: str) -> bool:
    if "..." in value:
        return False
    if value.strip() == "":
        return False
    # crude heuristic: treat paths with slashes as path-like
    return "/" in value or value.endswith(".md") or value.endswith(".csv") or value.endswith(".pdf")


def main() -> int:
    packet = load_packet()
    valid_gifi_codes = load_valid_gifi_codes()
    snapshot_rel = Path(packet["meta"]["snapshot_source"])
    snapshot_dir = (PROJECT_ROOT / snapshot_rel).resolve()

    if not snapshot_dir.exists():
        print(f"FAIL: snapshot_source not found: {snapshot_dir}", file=sys.stderr)
        return 2

    issues: list[str] = []
    invalid_codes: list[str] = []
    completeness: list[str] = []

    book_summary = load_book_fixed_asset_summary(snapshot_dir / "book_fixed_asset_overlay_summary.csv")
    book_audit = load_book_fixed_asset_audit(snapshot_dir / "book_fixed_asset_overlay_audit.csv")

    # --- Completeness checks (non-GIFI UFile screens) ---
    entity = packet.get("entity", {})
    entity_screens = entity.get("ufile_screens") if isinstance(entity, dict) else None
    if not isinstance(entity_screens, dict):
        completeness.append("entity.ufile_screens missing (tax preparer / addresses / officers).")
    else:
        for key in ("tax_preparer", "head_office_address", "other_addresses", "corporate_officers"):
            if key not in entity_screens:
                completeness.append(f"entity.ufile_screens missing key: {key}")

    for fy in ["FY2024", "FY2025"]:
        year = packet.get("years", {}).get(fy, {})
        year_screens = year.get("ufile_screens") if isinstance(year, dict) else None
        if not isinstance(year_screens, dict):
            completeness.append(f"{fy}: years[{fy}].ufile_screens missing (Identification / Refund-Balance owing / Dividends, etc.).")
        else:
            for key in (
                "corporate_history",
                "identification_of_corporation",
                "refund_or_balance_owing",
                "transactions_with_shareholders_officers_employees",
            ):
                if key not in year_screens:
                    completeness.append(f"{fy}: ufile_screens missing key: {key}")

            ident = year_screens.get("identification_of_corporation", {})
            if isinstance(ident, dict):
                # Active years should have GIFI enabled.
                if ident.get("has_gifi_financials") is not True:
                    completeness.append(f"{fy}: identification_of_corporation.has_gifi_financials should be true (or UFile may wipe GIFI entries).")
                if ident.get("is_first_federal_return") is not False:
                    completeness.append(f"{fy}: identification_of_corporation.is_first_federal_return should be false (2023 stub already filed).")

            # If dividends were declared, ensure the dividends paid screen is present and matches.
            retained = year.get("retained_earnings", {}) if isinstance(year, dict) else {}
            div_declared = int((retained.get("3700") or {}).get("amount") or 0) if isinstance(retained, dict) else 0
            dividends = year_screens.get("dividends_paid", {}) if isinstance(year_screens, dict) else {}
            if div_declared != 0:
                if not isinstance(dividends, dict) or dividends.get("has_dividends") is not True:
                    completeness.append(f"{fy}: dividends declared (retained earnings 3700={div_declared}) but ufile_screens.dividends_paid.has_dividends is not true.")
                else:
                    paid = int(dividends.get("taxable_dividends_paid") or 0)
                    if paid != div_declared:
                        completeness.append(f"{fy}: dividends_paid.taxable_dividends_paid ({paid}) != retained earnings 3700 ({div_declared}).")
                    eligible = int(dividends.get("eligible_dividend_portion") or 0)
                    if eligible < 0 or eligible > paid:
                        completeness.append(f"{fy}: dividends_paid.eligible_dividend_portion ({eligible}) must be between 0 and taxable_dividends_paid ({paid}).")

                    # If eligible dividends are designated, GRIP screen should exist (UFile prompts it).
                    if eligible > 0:
                        grip = year_screens.get("general_rate_income_pool", {}) if isinstance(year_screens, dict) else {}
                        if not isinstance(grip, dict) or "grip_end_prior_year" not in grip:
                            completeness.append(f"{fy}: eligible dividends portion > 0 but general_rate_income_pool is missing or incomplete.")

            cca_screen = year_screens.get("capital_cost_allowance", {}) if isinstance(year_screens, dict) else {}
            has_cca = cca_screen.get("has_cca") if isinstance(cca_screen, dict) else None
            schedule_8 = year.get("schedule_8", {}) if isinstance(year, dict) else {}
            classes = schedule_8.get("classes", {}) if isinstance(schedule_8, dict) else {}
            if has_cca is True and not classes:
                completeness.append(f"{fy}: capital_cost_allowance.has_cca is true but schedule_8 classes are missing/empty.")
            if classes:
                sch1 = year.get("schedule_1", {}) if isinstance(year, dict) else {}
                if "403" not in sch1:
                    completeness.append(f"{fy}: schedule_8 present but schedule_1 missing code 403 (CCA claim).")

                expensed_additions = book_summary.get(fy, {}).get("expensed_additions_dollars")
                if expensed_additions is None:
                    if "206" not in sch1:
                        completeness.append(f"{fy}: schedule_8 present but schedule_1 missing code 206 (capital items expensed).")
                elif expensed_additions > 0:
                    if "206" not in sch1:
                        completeness.append(
                            f"{fy}: expensed capital additions present but schedule_1 missing code 206 (expected {expensed_additions})."
                        )
                    else:
                        actual_206 = int((sch1.get("206") or {}).get("amount") or 0)
                        if actual_206 != expensed_additions:
                            completeness.append(
                                f"{fy}: schedule_1 code 206 ({actual_206}) != expensed additions total ({expensed_additions})."
                            )

            book_amort = book_summary.get(fy, {}).get("book_amortization_dollars") if book_summary else None
            if book_amort and book_amort > 0:
                sch1 = year.get("schedule_1", {}) if isinstance(year, dict) else {}
                if "104" not in sch1:
                    completeness.append(f"{fy}: book amortization recorded but schedule_1 missing code 104.")
                else:
                    actual_104 = int((sch1.get("104") or {}).get("amount") or 0)
                    if actual_104 != book_amort:
                        completeness.append(f"{fy}: schedule_1 code 104 ({actual_104}) != book amortization total ({book_amort}).")

            cap_count = book_summary.get(fy, {}).get("capitalized_asset_count") if book_summary else 0
            if cap_count and cap_count > 0:
                schedule_100 = year.get("schedule_100", {}) if isinstance(year, dict) else {}
                asset_codes = set()
                accum_codes = set()
                for row in book_audit.get(fy, []):
                    code = str(row.get("book_asset_gifi_code") or "").strip()
                    if code:
                        asset_codes.add(code)
                    accum = str(row.get("book_accum_amort_gifi_code") or "").strip()
                    if accum and int(row.get("amortization_dollars") or 0) != 0:
                        accum_codes.add(accum)
                if not asset_codes:
                    asset_codes = {"1740"}
                has_asset_line = any(int((schedule_100.get(code) or {}).get("amount") or 0) != 0 for code in asset_codes)
                if not has_asset_line:
                    completeness.append(f"{fy}: book fixed assets present but schedule_100 missing fixed-asset lines.")
                if accum_codes:
                    has_accum = any(int((schedule_100.get(code) or {}).get("amount") or 0) != 0 for code in accum_codes)
                    if not has_accum:
                        completeness.append(f"{fy}: book amortization recorded but schedule_100 missing accumulated amortization lines.")

    for fy in ["FY2024", "FY2025"]:
        snap_100 = load_gifi_csv(snapshot_dir / f"gifi_schedule_100_{fy}.csv")
        pkt_100 = {k: int(v["amount"]) for k, v in packet["years"][fy]["schedule_100"].items()}
        issues += compare_dicts(f"{fy} schedule_100", snap_100, pkt_100)

        snap_125 = load_gifi_csv(snapshot_dir / f"gifi_schedule_125_{fy}.csv")
        pkt_125 = {k: int(v["amount"]) for k, v in packet["years"][fy]["schedule_125"].items()}
        issues += compare_dicts(f"{fy} schedule_125", snap_125, pkt_125)

        snap_1 = load_schedule_1_csv(snapshot_dir / f"schedule_1_{fy}.csv")
        pkt_1 = {k: int(v["amount"]) for k, v in packet["years"][fy]["schedule_1"].items()}
        issues += compare_dicts(f"{fy} schedule_1", snap_1, pkt_1)

        snap_re = load_gifi_csv(snapshot_dir / f"gifi_retained_earnings_{fy}.csv")
        pkt_re = {k: int(v["amount"]) for k, v in packet["years"][fy]["retained_earnings"].items()}
        issues += compare_dicts(f"{fy} retained_earnings", snap_re, pkt_re)

        for code in sorted(set(pkt_100) | set(pkt_125) | set(pkt_re), key=lambda x: int(x)):
            if code not in valid_gifi_codes:
                invalid_codes.append(f"{fy}: invalid GIFI code in packet: {code}")

    # Evidence checks (best-effort; only check path-like entries)
    missing: list[str] = []
    for ev in packet.get("evidence_index", []):
        p = ev.get("path", "")
        if isinstance(p, str) and is_path_like(p):
            pp = (PROJECT_ROOT / p).resolve()
            if not pp.exists():
                missing.append(f"evidence_index missing: {p}")

    for j in packet.get("known_judgments", []):
        p = j.get("evidence")
        if isinstance(p, str) and is_path_like(p):
            pp = (PROJECT_ROOT / p).resolve()
            if not pp.exists():
                missing.append(f"known_judgments missing: {p}")

    if issues:
        print("AMOUNT MISMATCHES:", file=sys.stderr)
        for line in issues:
            print(f"- {line}", file=sys.stderr)

    if invalid_codes:
        print("INVALID GIFI CODES:", file=sys.stderr)
        for line in invalid_codes:
            print(f"- {line}", file=sys.stderr)

    if completeness:
        print("COMPLETENESS ISSUES:", file=sys.stderr)
        for line in completeness:
            print(f"- {line}", file=sys.stderr)

    if missing:
        print("MISSING EVIDENCE PATHS:", file=sys.stderr)
        for line in missing:
            print(f"- {line}", file=sys.stderr)

    if issues:
        return 2
    if invalid_codes:
        return 2
    if completeness:
        return 2
    if missing:
        return 1

    print("OK: packet amounts match snapshot; evidence paths present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
