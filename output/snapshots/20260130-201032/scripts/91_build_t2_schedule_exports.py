#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import re

from _lib import PROJECT_ROOT, FiscalYear, fiscal_years_from_manifest, load_manifest


@dataclass(frozen=True)
class TbLine:
    account_code: str
    account_type: str
    gifi_code: str
    net_cents: int


def load_tb(path: Path) -> list[TbLine]:
    rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
    out: list[TbLine] = []
    for r in rows:
        out.append(
            TbLine(
                account_code=str(r.get("account_code") or "").strip(),
                account_type=str(r.get("account_type") or "").strip(),
                gifi_code=str(r.get("gifi_code") or "").strip(),
                net_cents=int(r.get("net_cents") or 0),
            )
        )
    return out


def load_gifi_totals(path: Path) -> dict[str, int]:
    rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
    out: dict[str, int] = {}
    for r in rows:
        code = str(r.get("gifi_code") or "").strip()
        if not code:
            continue
        out[code] = int(r.get("net_cents") or 0)
    return out


def round_to_dollar(amount: Decimal) -> int:
    return int(amount.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def round_cents_to_dollar(cents: int) -> int:
    return round_to_dollar(Decimal(int(cents)) / Decimal(100))


def write_gifi_csv(rows: list[tuple[str, str, int]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["GIFI_Code", "Description", "Amount"])
        for code, desc, amt in rows:
            w.writerow([code, desc, str(int(amt))])


def write_schedule_1_csv(rows: list[tuple[str, str, int]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Line", "Description", "Amount"])
        for line, desc, amt in rows:
            w.writerow([line, desc, str(int(amt))])


def load_gifi_descriptions() -> dict[str, str]:
    """
    Load CRA GIFI code descriptions from the UFile copy/paste reference lists.

    This makes the schedule exports resilient to earlier hardcoded mappings (e.g., farming-only codes like 9801).
    """

    out: dict[str, str] = {}
    paths = [
        PROJECT_ROOT / "UfileToFill" / "GIFI" / "BalanceSheet.txt",
        PROJECT_ROOT / "UfileToFill" / "GIFI" / "IncomeStatement.txt",
    ]

    pattern = re.compile(r"^\s*(\d{4})\s+(.+\S)\s*$")
    for path in paths:
        if not path.exists():
            raise SystemExit(f"Missing GIFI reference list: {path}")
        for raw in path.read_text(encoding="utf-8").splitlines():
            m = pattern.match(raw)
            if not m:
                continue
            code = m.group(1)
            label = m.group(2).strip()
            # Keep first seen; lists may contain duplicates due to repeated sections.
            out.setdefault(code, label)
    return out


def desc(code: str, *, gifi_desc: dict[str, str]) -> str:
    return gifi_desc.get(code, "")


def net_income_cents_from_tb(tb: list[TbLine]) -> int:
    pl_sum = sum(r.net_cents for r in tb if r.account_type in ("revenue", "expense"))
    return -pl_sum


def meals_cents_from_tb(tb: list[TbLine]) -> int:
    return sum(r.net_cents for r in tb if r.gifi_code == "8523")


def cra_penalties_cents_from_tb(tb: list[TbLine]) -> int:
    # Penalties are posted to a dedicated expense account (9150) so we can add-back deterministically.
    return sum(r.net_cents for r in tb if r.account_code == "9150")


def dividends_cents_from_tb(tb: list[TbLine]) -> int:
    # Dividends declared are tracked in account 3400 (equity). Debits increase net_cents.
    return sum(r.net_cents for r in tb if r.account_code == "3400")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    args = ap.parse_args()

    gifi_desc = load_gifi_descriptions()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    args.out_dir.mkdir(parents=True, exist_ok=True)

    retained_end_by_fy: dict[str, int] = {}
    retained_start_by_fy: dict[str, int] = {}
    net_income_by_fy: dict[str, int] = {}

    # First pass: build schedules and retain retained_end for chaining.
    for fy in fys:
        tb_path = args.out_dir / f"trial_balance_{fy.fy}.csv"
        gifi_path = args.out_dir / f"gifi_totals_{fy.fy}.csv"
        if not tb_path.exists() or not gifi_path.exists():
            raise SystemExit(
                f"Missing {tb_path} or {gifi_path}. Run: python3 scripts/80_build_trial_balance.py"
            )

        tb = load_tb(tb_path)
        gifi_net = load_gifi_totals(gifi_path)

        # Net income (exact cents)
        net_income_cents = net_income_cents_from_tb(tb)
        net_income_dollars = round_cents_to_dollar(net_income_cents)
        net_income_by_fy[fy.fy] = net_income_dollars

        # Balance sheet components (rounded to dollars per line item)
        cash = round_cents_to_dollar(int(gifi_net.get("1001", 0)))
        inv_cents = sum(int(gifi_net.get(code, 0)) for code in ("1120", "1121", "1122", "1123", "1124", "1125", "1126", "1127"))
        inv = round_cents_to_dollar(inv_cents)
        due_from_sh = round_cents_to_dollar(int(gifi_net.get("1301", 0)))
        other_asset_codes = ("1481", "1482", "1483", "1484", "1485", "1486")
        other_assets_by_code: dict[str, int] = {}
        for code in other_asset_codes:
            cents = int(gifi_net.get(code, 0))
            amt = round_cents_to_dollar(cents)
            if amt != 0:
                other_assets_by_code[code] = amt

        total_assets = cash + inv + due_from_sh + sum(other_assets_by_code.values())

        payables = round_cents_to_dollar(abs(int(gifi_net.get("2620", 0))))
        taxes = round_cents_to_dollar(abs(int(gifi_net.get("2680", 0))))
        due_to_sh = round_cents_to_dollar(abs(int(gifi_net.get("2781", 0))))
        total_liabilities = payables + taxes + due_to_sh

        # Share capital is taken from the ledger (GIFI 3500) if present; otherwise 0.
        # We do not assume an amount here without evidence, to avoid shifting balance sheet reality.
        share_capital = round_cents_to_dollar(abs(int(gifi_net.get("3500", 0))))

        retained_end = total_assets - total_liabilities - share_capital
        total_equity = share_capital + retained_end
        total_liab_equity = total_liabilities + total_equity

        retained_end_by_fy[fy.fy] = retained_end

        # Retained earnings start is chained from previous year.
        prior_fys = [x for x in fys if x.end_date < fy.start_date]
        if not prior_fys:
            retained_start = 0
        else:
            prev = prior_fys[-1].fy
            retained_start = retained_end_by_fy.get(prev, 0)
        retained_start_by_fy[fy.fy] = retained_start

        # Schedule 100 (Balance Sheet)
        s100_rows: list[tuple[str, str, int]] = [
            ("1001", desc("1001", gifi_desc=gifi_desc), cash),
            ("1121", desc("1121", gifi_desc=gifi_desc), inv),
        ]
        if due_from_sh:
            s100_rows.append(("1301", desc("1301", gifi_desc=gifi_desc), due_from_sh))
        for code in sorted(other_assets_by_code.keys(), key=lambda x: int(x)):
            s100_rows.append((code, desc(code, gifi_desc=gifi_desc), other_assets_by_code[code]))
        s100_rows.append(("2599", desc("2599", gifi_desc=gifi_desc), total_assets))

        if due_to_sh:
            s100_rows.append(("2781", desc("2781", gifi_desc=gifi_desc), due_to_sh))
        if taxes:
            s100_rows.append(("2680", desc("2680", gifi_desc=gifi_desc), taxes))
        if payables:
            s100_rows.append(("2620", desc("2620", gifi_desc=gifi_desc), payables))
        s100_rows.append(("3499", desc("3499", gifi_desc=gifi_desc), total_liabilities))

        if share_capital:
            s100_rows.append(("3500", desc("3500", gifi_desc=gifi_desc), share_capital))
        s100_rows.append(("3600", desc("3600", gifi_desc=gifi_desc), retained_end))
        s100_rows.append(("3620", desc("3620", gifi_desc=gifi_desc), total_equity))
        s100_rows.append(("3640", desc("3640", gifi_desc=gifi_desc), total_liab_equity))

        # Schedule 125 (Income Statement)
        revenue = round_cents_to_dollar(abs(int(gifi_net.get("8000", 0))))
        cogs = round_cents_to_dollar(abs(int(gifi_net.get("8518", 0))))
        gross_profit = revenue - cogs

        skip_codes = {
            "1001",
            "1120",
            "1121",
            "1301",
            "1481",
            "1482",
            "1483",
            "1484",
            "1485",
            "1486",
            "2599",
            "2620",
            "2680",
            "2781",
            "3499",
            "3500",
            "3600",
            "3620",
            "3640",
            "3660",
            "3680",
            "3700",
            "3740",
            "3849",
            "8000",
            "8299",
            "8518",
            "8519",
            "9367",
            "9368",
            "9999",
        }
        expense_codes = sorted(
            [code for code, cents in gifi_net.items() if code not in skip_codes and int(cents) != 0],
            key=lambda c: int(c) if c.isdigit() else 10**9,
        )

        opex_rows: list[tuple[str, str, int]] = []
        total_opex = 0
        for code in expense_codes:
            cents = int(gifi_net.get(code, 0))
            # Skip income-like (credit) amounts for now; this project expects operating expenses here.
            if cents < 0:
                continue
            amt = round_cents_to_dollar(cents)
            if amt == 0:
                continue
            opex_rows.append((code, desc(code, gifi_desc=gifi_desc) or f"GIFI {code}", amt))
            total_opex += amt

        total_expenses = cogs + total_opex
        net_income = revenue - total_expenses

        s125_rows: list[tuple[str, str, int]] = [
            ("8000", desc("8000", gifi_desc=gifi_desc), revenue),
            ("8299", desc("8299", gifi_desc=gifi_desc), revenue),
            ("8518", desc("8518", gifi_desc=gifi_desc), cogs),
            ("8519", desc("8519", gifi_desc=gifi_desc), gross_profit),
        ]
        s125_rows.extend(opex_rows)
        s125_rows.extend(
            [
                ("9367", desc("9367", gifi_desc=gifi_desc), total_opex),
                ("9368", desc("9368", gifi_desc=gifi_desc), total_expenses),
                ("9999", desc("9999", gifi_desc=gifi_desc), net_income),
            ]
        )

        # Retained earnings schedule (corporations only)
        dividends_dollars = round_cents_to_dollar(dividends_cents_from_tb(tb))
        retained_adjust = retained_end - (retained_start + net_income - dividends_dollars)
        re_rows: list[tuple[str, str, int]] = [
            ("3660", desc("3660", gifi_desc=gifi_desc), retained_start),
            ("3680", desc("3680", gifi_desc=gifi_desc), net_income),
        ]
        if dividends_dollars:
            re_rows.append(("3700", desc("3700", gifi_desc=gifi_desc), dividends_dollars))
        if retained_adjust != 0:
            re_rows.append(("3740", f"{desc('3740', gifi_desc=gifi_desc)} (rounding)", retained_adjust))
        re_rows.append(("3849", desc("3849", gifi_desc=gifi_desc), retained_end))

        # Schedule 1 (Net income for tax purposes): 50% M&E add-back.
        meals_cents = meals_cents_from_tb(tb)
        meals_dollars = round_cents_to_dollar(meals_cents)
        meals_addback = round_to_dollar(Decimal(meals_dollars) / Decimal(2))
        penalties_dollars = round_cents_to_dollar(cra_penalties_cents_from_tb(tb))
        penalties_addback = penalties_dollars
        taxable_income = net_income + meals_addback + penalties_addback
        sch1_rows: list[tuple[str, str, int]] = [
            ("300", "Net income per financial statements", net_income),
            ("117", "50% of meals and entertainment", meals_addback),
            ("311", "Penalties and fines (CRA)", penalties_addback),
            ("400", "Net income for tax purposes", taxable_income),
        ]

        # Write outputs
        write_gifi_csv(s100_rows, args.out_dir / f"gifi_schedule_100_{fy.fy}.csv")
        write_gifi_csv(s125_rows, args.out_dir / f"gifi_schedule_125_{fy.fy}.csv")
        write_gifi_csv(re_rows, args.out_dir / f"gifi_retained_earnings_{fy.fy}.csv")
        write_gifi_csv(s100_rows + s125_rows + re_rows, args.out_dir / f"ufile_gifi_{fy.fy}.csv")
        write_schedule_1_csv(sch1_rows, args.out_dir / f"schedule_1_{fy.fy}.csv")

        # Small sanity check: balance sheet must balance in dollars.
        if total_assets != total_liab_equity:
            raise SystemExit(
                f"Balance sheet out of balance for {fy.fy}: total_assets={total_assets} != total_liab_equity={total_liab_equity}"
            )

    print("T2 SCHEDULE EXPORTS BUILT")
    print(f"- out_dir: {args.out_dir}")
    for fy in fys:
        print(f"- {fy.fy}: ufile_gifi_{fy.fy}.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
