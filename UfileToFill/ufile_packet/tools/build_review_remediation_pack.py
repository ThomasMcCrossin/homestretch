#!/usr/bin/env python3
"""
Build FY-scoped review remediation artifacts (working papers) from the current packet snapshot.

This is the "make it boring" layer:
- Inventory / gross margin swing memo + tie-out
- Fixed asset / CCA continuity tables (book vs tax)
- Payables breakdown (A/P vs HST vs payroll liabs)

No accounting numbers are changed by this tool. It only generates documentation and tie-out tables.
"""

from __future__ import annotations

import csv
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from render_year_guide_html import render_year_guide_html


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "packet.json"
OUT_ROOT = PROJECT_ROOT / "audit_packages"

# Reuse manifest helpers from scripts/_lib.py (scripts isn't a package, so add it to sys.path).
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
from _lib import load_manifest, get_source  # type: ignore  # noqa: E402


def round_to_dollar(amount: Decimal) -> int:
    return int(amount.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def round_cents_to_dollar(cents: int) -> int:
    return round_to_dollar(Decimal(int(cents)) / Decimal(100))


def dollars(cents: int) -> str:
    return f"${cents/100:,.2f}"


def money(n: int) -> str:
    return f"{n:,}"


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return "_(none)_"
    out: list[str] = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


@dataclass(frozen=True)
class FyCtx:
    fy: str
    start: str
    end: str
    filing_start: str


def snapshot_dir_from_packet(packet: dict) -> Path:
    snap = str(packet.get("meta", {}).get("snapshot_source") or "").strip()
    if not snap:
        raise SystemExit("packet.json missing meta.snapshot_source")
    p = PROJECT_ROOT / snap
    if not p.exists():
        raise SystemExit(f"Snapshot directory not found: {p}")
    return p


def parse_inventory_sheet_total_and_categories(path: Path) -> tuple[Decimal, dict[str, Decimal]]:
    """
    Parses the inventory sheet format used in this project:
    - Grand total is the first row where Category and Product are blank and Total is set.
    - Category subtotals are rows where Category is set, Product is blank, and Total is set.
    """
    rows = read_csv_rows(path)
    total = Decimal("0")
    by_cat: dict[str, Decimal] = {}
    for r in rows:
        cat = str(r.get("Category") or "").strip()
        prod = str(r.get("Product") or "").strip()
        tot = str(r.get("Total") or "").strip().replace(",", "")
        if not cat and not prod and tot:
            try:
                total = Decimal(tot)
            except Exception:
                total = Decimal("0")
            break
    for r in rows:
        cat = str(r.get("Category") or "").strip()
        prod = str(r.get("Product") or "").strip()
        tot = str(r.get("Total") or "").strip().replace(",", "")
        if not cat or prod or not tot:
            continue
        try:
            amt = Decimal(tot)
        except Exception:
            continue
        by_cat[cat] = by_cat.get(cat, Decimal("0")) + amt
    return total, by_cat


def main() -> int:
    packet = json.loads(PACKET_PATH.read_text(encoding="utf-8"))
    snapshot_dir = snapshot_dir_from_packet(packet)
    snapshot_source = str(packet.get("meta", {}).get("snapshot_source") or "").strip().rstrip("/") + "/"

    years = packet.get("years", {})
    if not isinstance(years, dict) or not years:
        raise SystemExit("packet.json missing years")

    # Asset register + schedule 8 are generated in the accounting snapshot outputs.
    assets_resolved = read_csv_rows(snapshot_dir / "cca_asset_register_resolved.csv")

    # For each FY, write memos and continuity tables into audit_packages/FYxxxx/
    fy_keys = sorted(years.keys())
    first_fy = fy_keys[0] if fy_keys else ""

    manifest = load_manifest()

    for fy in fy_keys:
        year = years[fy]
        period = year.get("fiscal_period", {})
        start = str(period.get("start") or "").strip()
        end = str(period.get("end") or "").strip()
        if not start or not end:
            raise SystemExit(f"packet.json missing fiscal_period for {fy}")

        # Use operations_start_date as the filing start for the first year after incorporation/ops start.
        filing_start = start
        ident = year.get("ufile_screens", {}).get("identification_of_corporation", {})
        ops_start = str(ident.get("operations_start_date") or "").strip() if isinstance(ident, dict) else ""
        if fy == first_fy and ops_start:
            try:
                if datetime.strptime(ops_start, "%Y-%m-%d") > datetime.strptime(filing_start, "%Y-%m-%d"):
                    filing_start = ops_start
            except Exception:
                pass

        ctx = FyCtx(fy=fy, start=start, end=end, filing_start=filing_start)

        out_dir = OUT_ROOT / fy
        out_dir.mkdir(parents=True, exist_ok=True)

        # --- Inventory / gross margin memo ---
        sch100 = year.get("schedule_100", {})
        sch125 = year.get("schedule_125", {})

        def amt(d: dict, code: str) -> int:
            try:
                return int(d.get(code, {}).get("amount") or 0)
            except Exception:
                return 0

        sales = amt(sch125, "8000")
        cogs = amt(sch125, "8518")
        gp = sales - cogs
        gm = Decimal("0")
        if sales:
            gm = (Decimal(gp) * Decimal(100)) / Decimal(sales)

        closing_inv = amt(sch100, "1121") or amt(sch100, "1120")
        # Opening inventory is prior year closing if present; otherwise 0.
        opening_inv = 0
        if fy.startswith("FY") and fy[2:].isdigit():
            prior = f"FY{int(fy[2:]) - 1}"
            prior_year = years.get(prior, {})
            prior_sch100 = prior_year.get("schedule_100", {}) if isinstance(prior_year, dict) else {}
            if isinstance(prior_sch100, dict):
                try:
                    opening_inv = int(prior_sch100.get("1121", {}).get("amount") or 0) or int(prior_sch100.get("1120", {}).get("amount") or 0)
                except Exception:
                    opening_inv = 0

        purchases = cogs - opening_inv + closing_inv

        inv_rows = [
            ["Trade sales (8000)", money(sales)],
            ["Opening inventory (8300) (tie)", money(opening_inv)],
            ["Purchases (8320) (computed)", money(purchases)],
            ["Closing inventory (8500) (tie)", money(closing_inv)],
            ["Cost of sales (8518)", money(cogs)],
            ["Gross profit", money(gp)],
            ["Gross margin %", f"{gm.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}%"],
        ]

        inv_memo = []
        inv_memo.append(f"# Inventory and gross margin memo — {fy}")
        inv_memo.append("")
        inv_memo.append(f"Period: **{ctx.filing_start} to {ctx.end}**")
        inv_memo.append(f"Snapshot source: `{snapshot_source}`")
        inv_memo.append("")
        inv_memo.append("## Computation (GIFI tie-out)")
        inv_memo.append(md_table(["Item", "Amount (dollars)"], inv_rows))
        inv_memo.append("")
        inv_memo.append("## Commentary (management explanation)")
        if fy == "FY2025":
            inv_memo.append(
                "- Management expected the Amherst Ramblers to have a longer playoff run and purchased additional inventory to meet expected demand."
            )
            inv_memo.append(
                "- The team was knocked out in round 1, resulting in higher ending inventory than would be typical for the season."
            )
            inv_memo.append(
                "- Management believes the recorded inventory balance may be conservative; no adjustment has been made without additional support."
            )
            inv_memo.append(
                "- FY2025 inventory support is based on a physical count performed near year-end (May 16, 2025) plus management adjustments for immaterial movements through May 31, 2025."
            )
        elif fy == "FY2024":
            inv_memo.append(
                "- FY2024 ending inventory was estimated by management using an itemized schedule at cost (no formal physical count process in FY2024)."
            )
        else:
            inv_memo.append("- Inventory is supported by management records; see linked evidence files below.")
        inv_memo.append("")
        inv_memo.append("## Evidence (snapshot files)")
        # Only link files that exist in the snapshot directory.
        candidates = [
            "inventory_journal_detail.csv",
            "inventory_journal_detail.md",
            "inventory_journal_summary.md",
        ]
        for name in candidates:
            if (snapshot_dir / name).exists():
                inv_memo.append(f"- `{snapshot_source}{name}`")
        inv_memo.append("")

        inv_md = "\n".join(inv_memo).strip() + "\n"
        write_text(out_dir / "inventory_margin_memo.md", inv_md)
        write_text(out_dir / "inventory_margin_memo.html", render_year_guide_html(packet, fy, md_guide=inv_md))

        # --- FY2024 only: inventory estimate method note (FY2025-item-based) ---
        if fy == "FY2024":
            src = get_source(manifest, "inventory_count_fy2024_may31_estimated_csv")
            sheet_path = Path(str(src.get("path") or "")).expanduser()
            sheet_total = Decimal("0")
            by_cat: dict[str, Decimal] = {}
            if sheet_path.exists():
                sheet_total, by_cat = parse_inventory_sheet_total_and_categories(sheet_path)

            plaus = []
            plaus.append("# FY2024 ending inventory estimate note (FY2025-item-based)")
            plaus.append("")
            plaus.append("Purpose: document how FY2024 ending inventory was estimated for this filing.")
            plaus.append("")
            plaus.append(f"Period: **{ctx.filing_start} to {ctx.end}**")
            plaus.append(f"Snapshot source: `{snapshot_source}`")
            plaus.append("")
            plaus.append("## What this file does (in plain English)")
            plaus.append("- FY2024 did not have a physical inventory count.")
            plaus.append(
                "- Management estimated FY2024 ending inventory using the FY2025 physical-count item list as a basis, scaled down to a target band."
            )
            plaus.append(
                "- Quantities were rounded to whole numbers for most items (decimals only where the FY2025 source uses decimals)."
            )
            plaus.append("")
            plaus.append("## What is used in the filing package")
            plaus.append(f"- FY2024 closing inventory used: **${closing_inv:,.0f}** (GIFI 1121; journal `INVENTORY_CLOSE_FY2024`).")
            if sheet_total:
                plaus.append(f"- FY2024 estimate CSV total: **${sheet_total:,.2f}** (`{sheet_path}`).")
            plaus.append("")
            if by_cat:
                rows = [[k, f"${v:,.2f}"] for k, v in sorted(by_cat.items(), key=lambda kv: kv[0].lower())]
                plaus.append("### Category totals in the FY2024 estimate sheet")
                plaus.append(md_table(["Category", "Total"], rows))
                plaus.append("")

            # A more concrete, CRA-defensible way to think about the number is "days of cost-of-sales on hand".
            # This doesn't prove the exact amount, but it provides a coherent framework for a management estimate.
            try:
                period_days = (datetime.strptime(ctx.end, "%Y-%m-%d") - datetime.strptime(ctx.filing_start, "%Y-%m-%d")).days + 1
            except Exception:
                period_days = 0

            daily_cogs = Decimal("0")
            if period_days and cogs:
                daily_cogs = (Decimal(cogs) / Decimal(period_days)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

            plaus.append("## Estimation framework (days of COGS on hand)")
            if daily_cogs:
                plaus.append(f"- FY2024 cost of sales (GIFI 8518): **${cogs:,.0f}** across **{period_days}** days.")
                plaus.append(f"- Average daily COGS: **${daily_cogs:,.2f}/day**.")
                plaus.append("")
                plaus.append("For context, the implied days-on-hand at a few inventory totals is:")
                rows = []
                for tgt in (Decimal("4500"), Decimal("5000"), Decimal("5137"), Decimal("5500")):
                    days_on_hand = (tgt / daily_cogs).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP) if daily_cogs else Decimal("0")
                    rows.append([f"${tgt:,.0f}", f"{days_on_hand} days"])
                plaus.append(md_table(["Target ending inventory", "Implied days of COGS on hand"], rows))
                plaus.append("")
                plaus.append("- The selected FY2024 estimate is intended to be in a coherent management-estimate range (roughly ~15–18 days of stock).")
                plaus.append("")
                plaus.append("### Impact on FY2024 profit (pure inventory re-estimate)")
                plaus.append(
                    "- If the only change is raising FY2024 closing inventory, **COGS decreases dollar-for-dollar** and **net income increases dollar-for-dollar**."
                )
                impact_rows = []
                base_inv = Decimal(int(closing_inv))
                base_gp = Decimal(int(gp))
                base_cogs = Decimal(int(cogs))
                base_sales = Decimal(int(sales))
                for tgt in (Decimal("4500"), Decimal("5000"), Decimal("5500")):
                    delta = tgt - base_inv
                    new_cogs = base_cogs - delta
                    new_gp = base_gp + delta
                    new_gm = Decimal("0")
                    if base_sales:
                        new_gm = (new_gp * Decimal(100) / base_sales).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                    impact_rows.append([f"${tgt:,.0f}", f"{delta:+,.0f}", f"${new_cogs:,.0f}", f"${new_gp:,.0f}", f"{new_gm}%"])
                plaus.append(md_table(["Target inv", "Delta vs current", "Implied COGS", "Implied gross profit", "Implied GM%"], impact_rows))
            else:
                plaus.append("- (Could not compute daily COGS; missing Schedule 125 values.)")
            plaus.append("")

            # Reference FY2025 physical count context for why the FY2024 estimate could reasonably be below FY2025.
            try:
                fy2025 = years.get("FY2025", {})
                sch125_25 = fy2025.get("schedule_125", {}) if isinstance(fy2025, dict) else {}
                sch100_25 = fy2025.get("schedule_100", {}) if isinstance(fy2025, dict) else {}
                cogs25 = int(sch125_25.get("8518", {}).get("amount") or 0)
                inv25 = int(sch100_25.get("1121", {}).get("amount") or 0) or int(sch100_25.get("1120", {}).get("amount") or 0)
            except Exception:
                cogs25 = 0
                inv25 = 0

            if cogs25 and inv25:
                try:
                    period_days25 = (datetime.strptime(years["FY2025"]["fiscal_period"]["end"], "%Y-%m-%d") - datetime.strptime(years["FY2025"]["fiscal_period"]["start"], "%Y-%m-%d")).days + 1
                except Exception:
                    period_days25 = 0
                daily_cogs25 = Decimal("0")
                if period_days25:
                    daily_cogs25 = (Decimal(cogs25) / Decimal(period_days25)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                if daily_cogs25:
                    days25 = (Decimal(inv25) / daily_cogs25).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
                    plaus.append("## FY2025 physical count context (sanity check)")
                    plaus.append(
                        f"- FY2025 ending inventory (physical count based): **${inv25:,.0f}**; FY2025 COGS: **${cogs25:,.0f}**."
                    )
                    plaus.append(f"- Implied FY2025 days of inventory on hand: **{days25} days**.")
                    plaus.append(
                        "- FY2025 was impacted by a known overbuy scenario; therefore a lower FY2024 days-on-hand assumption "
                        "(e.g., roughly half of FY2025) can still be coherent."
                    )
                    plaus.append("")

            plaus.append("## Disposables policy note (why this matters)")
            plaus.append(
                "- In this project’s FY2024 estimate sheet, **disposables are treated as inventory** (they map into Inventory - Food)."
            )
            plaus.append(
                "- If you conceptually treat disposables as \"supplies\" rather than inventory, that would tend to **reduce** the inventory number, not increase it."
            )
            plaus.append(
                "- Therefore, a higher FY2024 inventory belief is most consistent with **missing items/locations** rather than a disposables policy mismatch."
            )
            plaus.append("")
            plaus.append("## Evidence pointers")
            plaus.append(f"- Estimate sheet: `{sheet_path}`")
            plaus.append(f"- Generator script: `scripts/90a_generate_inventory_estimate_fy2024_from_fy2025.py`")
            plaus.append(f"- Generator audit: `{PROJECT_ROOT / 'output' / 'inventory_estimate_fy2024_from_fy2025_audit.csv'}`")
            plaus.append(f"- Inventory JE evidence: `{snapshot_source}inventory_journal_detail.csv` and `{snapshot_source}inventory_journal_detail.csv`")
            plaus.append(f"- Override audit (if/when used): `{snapshot_source}inventory_override_audit.csv`")
            plaus.append("")
            plaus.append("## If you choose to restate later (operator-controlled)")
            plaus.append("- Re-run the generator with a different target center/tolerance, update the manifest sha256, and refresh.")
            plaus.append("- This will cascade deterministically into FY2025 opening inventory (carryforward consistency).")
            plaus.append("")

            plaus_md = "\n".join(plaus).strip() + "\n"
            write_text(out_dir / "inventory_estimate_plausibility_note.md", plaus_md)
            write_text(out_dir / "inventory_estimate_plausibility_note.html", render_year_guide_html(packet, fy, md_guide=plaus_md))

        # --- Payables breakdown memo (2620 and 2680) ---
        tb_rows = read_csv_rows(snapshot_dir / f"trial_balance_{fy}.csv")
        pay_rows = []
        for gifi_code in ("2620", "2680"):
            items = []
            total_cents = 0
            for r in tb_rows:
                if (r.get("fy") or "").strip() != fy:
                    continue
                if (r.get("gifi_code") or "").strip() != gifi_code:
                    continue
                try:
                    cents = int(r.get("net_cents") or 0)
                except Exception:
                    cents = 0
                total_cents += cents
                items.append((r.get("account_code") or "", r.get("account_name") or "", cents))

            if items:
                for acct, name, cents in sorted(items, key=lambda x: x[0]):
                    pay_rows.append([gifi_code, str(acct), str(name), dollars(cents)])
                pay_rows.append([gifi_code, "", "TOTAL (net)", dollars(total_cents)])

        pay_memo = []
        pay_memo.append(f"# Payables breakdown — {fy}")
        pay_memo.append("")
        pay_memo.append(f"Period: **{ctx.filing_start} to {ctx.end}**")
        pay_memo.append(f"Snapshot source: `{snapshot_source}`")
        pay_memo.append("")
        pay_memo.append("## What this is")
        pay_memo.append(
            "- This memo explains what is included in Schedule 100 lines **2620 (A/P and accruals)** and **2680 (taxes payable)** in this file."
        )
        pay_memo.append(
            "- In this project, **2680 is used for net HST payable** (HST payable offset by ITCs receivable), not payroll source deductions."
        )
        pay_memo.append("")
        pay_memo.append("## Breakdown (from trial balance)")
        pay_memo.append(md_table(["GIFI", "Account", "Name", "Net (cents sign)"], pay_rows))
        pay_memo.append("")
        pay_memo.append("Evidence:")
        pay_memo.append(f"- `{snapshot_source}trial_balance_{fy}.csv`")
        pay_memo.append("")

        pay_md = "\n".join(pay_memo).strip() + "\n"
        write_text(out_dir / "payables_breakdown.md", pay_md)
        write_text(out_dir / "payables_breakdown.html", render_year_guide_html(packet, fy, md_guide=pay_md))

        # --- Fixed asset / CCA continuity tables ---
        # By class: schedule_8_FYxxxx.csv
        s8_path = snapshot_dir / f"schedule_8_{fy}.csv"
        s8_rows = read_csv_rows(s8_path) if s8_path.exists() else []
        class_rows = []
        for r in s8_rows:
            cls = str(r.get("Class") or "").strip()
            if not cls:
                continue
            class_rows.append(
                [
                    cls,
                    str(r.get("Description") or ""),
                    str(r.get("Opening_UCC") or ""),
                    str(r.get("Additions") or ""),
                    str(r.get("CCA_Claim") or ""),
                    str(r.get("Closing_UCC") or ""),
                ]
            )
        class_rows.sort(key=lambda x: int(x[0]) if x[0].isdigit() else 10**9)

        # By asset: resolved asset register for this FY
        asset_rows = []
        for r in assets_resolved:
            if str(r.get("fiscal_year") or "").strip() != fy:
                continue
            asset_rows.append(
                [
                    str(r.get("asset_id") or ""),
                    str(r.get("description") or ""),
                    str(r.get("available_for_use_date") or ""),
                    str(r.get("cca_class") or ""),
                    str(r.get("total_cost_dollars") or ""),
                    str(r.get("source_breakdown") or ""),
                ]
            )
        asset_rows.sort(key=lambda x: x[0])

        fa_memo = []
        fa_memo.append(f"# Fixed assets and CCA continuity — {fy}")
        fa_memo.append("")
        fa_memo.append(f"Period: **{ctx.filing_start} to {ctx.end}**")
        fa_memo.append(f"Snapshot source: `{snapshot_source}`")
        fa_memo.append("")
        fa_memo.append("## Key point")
        fa_memo.append(
            "- Book fixed assets (GIFI 1740/1741/8670) and tax CCA (Schedule 8) are reconciled using the same asset register."
        )
        fa_memo.append(
            "- If a UFile-exported PDF appears to show missing additions, the usual cause is that the **Capital cost allowance** screen was not completed for that class (UFile may omit the schedule from the package)."
        )
        fa_memo.append("")
        fa_memo.append("## Schedule 8 continuity (by class)")
        fa_memo.append(md_table(["Class", "Description", "Opening UCC", "Additions", "CCA claim", "Closing UCC"], class_rows))
        fa_memo.append("")
        fa_memo.append("## Asset additions (by invoice / asset)")
        fa_memo.append(
            md_table(
                ["Asset ID", "Description", "Available for use", "Class", "Cost", "Source breakdown"],
                asset_rows,
            )
        )
        fa_memo.append("")
        fa_memo.append("Evidence:")
        if s8_path.exists():
            fa_memo.append(f"- `{snapshot_source}schedule_8_{fy}.csv`")
        fa_memo.append(f"- `{snapshot_source}cca_asset_register_resolved.csv`")
        fa_memo.append("")

        fa_md = "\n".join(fa_memo).strip() + "\n"
        write_text(out_dir / "fixed_asset_cca_continuity.md", fa_md)
        write_text(out_dir / "fixed_asset_cca_continuity.html", render_year_guide_html(packet, fy, md_guide=fa_md))

    print("REVIEW REMEDIATION PACK BUILT")
    print(f"- out_dir: {OUT_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
