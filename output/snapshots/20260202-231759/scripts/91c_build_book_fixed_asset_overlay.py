#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest
from cca_assets_lib import (
    CCA_CLASS_RATES,
    ResolvedAsset,
    aii_factor,
    days_in_fy,
    fy_for_date,
    first_year_base_factor,
    half_year_applies,
    load_assets,
    resolve_component,
    round_cents_to_dollar,
    round_to_dollar,
)


ASSET_REGISTER_PATH = PROJECT_ROOT / "overrides" / "cca_assets.yml"


def load_account_gifi_map(conn) -> dict[str, str]:
    rows = conn.execute(
        "SELECT account_code, COALESCE(gifi_code, '') AS gifi_code FROM chart_of_accounts"
    ).fetchall()
    out: dict[str, str] = {}
    for r in rows:
        account_code = str(r["account_code"])
        gifi_code = str(r["gifi_code"] or "").strip()
        if gifi_code:
            out[account_code] = gifi_code
    return out


def source_breakdown(resolved_components) -> str:
    parts = []
    for comp in resolved_components:
        if comp.source_type == "wave_bill_allocation":
            parts.append(
                "wave_bill_allocation: bill_id={bill_id} invoice_date={date} vendor={vendor} "
                "account={account} amount_cents={amount} alloc_total_cents={alloc}".format(
                    bill_id=comp.wave_bill_id,
                    date=comp.invoice_date,
                    vendor=comp.vendor_raw,
                    account=comp.account_code,
                    amount=comp.amount_cents,
                    alloc=comp.allocation_total_cents,
                )
            )
        else:
            parts.append(f"{comp.source_type}: amount_cents={comp.amount_cents}")
    return " | ".join(parts)


def component_breakdown(resolved_components, account_gifi: dict[str, str]) -> str:
    parts = []
    for comp in resolved_components:
        acct = comp.account_code or ""
        gifi = account_gifi.get(acct, "")
        parts.append(
            "account={account} gifi={gifi} amount_cents={amount} vendor={vendor} invoice_date={date}".format(
                account=acct,
                gifi=gifi,
                amount=comp.amount_cents,
                vendor=comp.vendor_raw or "",
                date=comp.invoice_date or "",
            )
        )
    return " | ".join(parts)


def overlap_days(start: date, end: date, fy_start: date, fy_end: date) -> int:
    start_at = max(start, fy_start)
    end_at = min(end, fy_end)
    if start_at > end_at:
        return 0
    return (end_at - start_at).days + 1


def build_mirror_tax_amortization(
    resolved: ResolvedAsset,
    *,
    book_start: date,
    fys,
) -> dict[str, int]:
    class_key = str(resolved.asset.cca_class)
    if class_key not in CCA_CLASS_RATES:
        raise SystemExit(f"Unknown CCA class rate for class {class_key}. Add it to the class_rates map.")

    book_fy = fy_for_date(fys, book_start)
    additions_dollars = round_cents_to_dollar(resolved.total_cost_cents)
    # Mirror the same first-year base logic as Schedule 8 (including AII factor where eligible).
    base_factor = first_year_base_factor(resolved.asset, book_start)

    opening = 0
    out: dict[str, int] = {}
    started = False
    for fy in fys:
        if not started:
            if fy.fy != book_fy:
                continue
            started = True
        _, _, proration_factor = days_in_fy(fy)
        additions = additions_dollars if fy.fy == book_fy else 0
        if additions:
            base_additions = Decimal(additions) * base_factor
        else:
            base_additions = Decimal("0")

        base = Decimal(opening) + base_additions
        claim_percent = resolved.asset.claim_percent_of_max
        rate = CCA_CLASS_RATES[class_key]

        cca_claim = round_to_dollar(base * rate * claim_percent * proration_factor)
        closing = opening + additions - cca_claim

        if cca_claim != 0:
            out[fy.fy] = int(cca_claim) * 100

        opening = closing

    return out


def build_straight_line_amortization(
    resolved: ResolvedAsset,
    *,
    book_start: date,
    fys,
) -> dict[str, int]:
    if resolved.asset.useful_life_years is None:
        raise SystemExit(f"CCA asset {resolved.asset.asset_id} missing useful_life_years for straight_line policy")

    total_life_days = int((resolved.asset.useful_life_years * Decimal("365")).to_integral_value(rounding=ROUND_HALF_UP))
    if total_life_days <= 0:
        raise SystemExit(f"CCA asset {resolved.asset.asset_id} has invalid useful_life_years")

    end_date = book_start + timedelta(days=total_life_days - 1)
    total_cost_dollars = Decimal(resolved.total_cost_cents) / Decimal(100)

    out: dict[str, int] = {}
    for fy in fys:
        fy_start = date.fromisoformat(fy.start_date)
        fy_end = date.fromisoformat(fy.end_date)
        days = overlap_days(book_start, end_date, fy_start, fy_end)
        if days <= 0:
            continue
        raw_dollars = total_cost_dollars * Decimal(days) / Decimal(total_life_days)
        amort_dollars = round_to_dollar(raw_dollars)
        if amort_dollars:
            out[fy.fy] = int(amort_dollars) * 100

    return out


def write_overlay_csv(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "fiscal_year",
                "asset_id",
                "entry_type",
                "gifi_code",
                "account_code",
                "net_cents",
                "net_dollars",
                "description",
                "component_note",
            ],
        )
        w.writeheader()
        w.writerows(rows)


def write_audit_csv(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "fiscal_year",
                "asset_id",
                "description",
                "book_treatment",
                "book_depr_policy",
                "book_start_date",
                "available_for_use_date",
                "total_cost_cents",
                "total_cost_dollars",
                "reclass_total_cents",
                "reclass_total_dollars",
                "amortization_cents",
                "amortization_dollars",
                "book_asset_gifi_code",
                "book_accum_amort_gifi_code",
                "book_amort_expense_gifi_code",
                "component_breakdown",
                "source_breakdown",
                "notes",
            ],
        )
        w.writeheader()
        w.writerows(rows)


def write_summary_csv(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "fiscal_year",
                "capitalized_asset_count",
                "expensed_asset_count",
                "capitalized_additions_cents",
                "capitalized_additions_dollars",
                "expensed_additions_cents",
                "expensed_additions_dollars",
                "book_amortization_cents",
                "book_amortization_dollars",
            ],
        )
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--assets", type=Path, default=ASSET_REGISTER_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    _, assets = load_assets(args.assets)

    conn = connect_db(args.db)
    try:
        account_gifi = load_account_gifi_map(conn)
        resolved: list[ResolvedAsset] = []
        for asset in assets:
            resolved_components = []
            total_cost = 0
            for comp in asset.source_components:
                resolved_comp = resolve_component(conn, asset.asset_id, comp)
                resolved_components.append(resolved_comp)
                total_cost += int(comp.amount_cents)

            dt = date.fromisoformat(asset.available_for_use_date)
            fy = fy_for_date(fys, dt)
            apply_half_year = half_year_applies(asset, dt)
            factor = aii_factor(asset, dt)
            base_factor = first_year_base_factor(asset, dt)

            resolved.append(
                ResolvedAsset(
                    asset=asset,
                    fy=fy,
                    total_cost_cents=total_cost,
                    resolved_components=resolved_components,
                    half_year_applied=apply_half_year,
                    aii_factor=factor,
                    first_year_base_factor=base_factor,
                )
            )
    finally:
        conn.close()

    overlay_by_fy: dict[str, list[dict]] = {fy.fy: [] for fy in fys}
    audit_rows: list[dict] = []

    summary_by_fy: dict[str, dict[str, int]] = {
        fy.fy: {
            "capitalized_asset_count": 0,
            "expensed_asset_count": 0,
            "capitalized_additions_cents": 0,
            "expensed_additions_cents": 0,
            "book_amortization_cents": 0,
        }
        for fy in fys
    }

    for resolved_asset in resolved:
        asset = resolved_asset.asset
        total_cost_cents = int(resolved_asset.total_cost_cents)
        total_cost_dollars = round_cents_to_dollar(total_cost_cents)

        if asset.book_treatment == "expense":
            summary_by_fy[resolved_asset.fy]["expensed_asset_count"] += 1
            summary_by_fy[resolved_asset.fy]["expensed_additions_cents"] += total_cost_cents
        else:
            summary_by_fy[resolved_asset.fy]["capitalized_asset_count"] += 1
            summary_by_fy[resolved_asset.fy]["capitalized_additions_cents"] += total_cost_cents

        if asset.book_treatment != "capitalize":
            continue

        book_start_str = asset.book_start_date or asset.available_for_use_date
        book_start_date = date.fromisoformat(book_start_str)
        book_fy = fy_for_date(fys, book_start_date)

        for comp in resolved_asset.resolved_components:
            account_code = comp.account_code or ""
            gifi_code = account_gifi.get(account_code)
            if not gifi_code:
                raise SystemExit(
                    f"CCA asset {asset.asset_id} component account {account_code!r} has no GIFI code; "
                    "apply overrides or update chart_of_accounts before building book overlay."
                )
            overlay_by_fy[book_fy].append(
                {
                    "fiscal_year": book_fy,
                    "asset_id": asset.asset_id,
                    "entry_type": "reclass_expense_credit",
                    "gifi_code": gifi_code,
                    "account_code": account_code,
                    "net_cents": -int(comp.amount_cents),
                    "net_dollars": f"{-int(comp.amount_cents) / 100:.2f}",
                    "description": asset.description,
                    "component_note": f"bill_id={comp.wave_bill_id} vendor={comp.vendor_raw}",
                }
            )

        amort_by_fy: dict[str, int] = {}
        if asset.book_depr_policy == "mirror_tax":
            amort_by_fy = build_mirror_tax_amortization(resolved_asset, book_start=book_start_date, fys=fys)
        elif asset.book_depr_policy == "straight_line":
            amort_by_fy = build_straight_line_amortization(resolved_asset, book_start=book_start_date, fys=fys)

        for fy_key, amort_cents in amort_by_fy.items():
            if amort_cents == 0:
                continue
            summary_by_fy[fy_key]["book_amortization_cents"] += amort_cents
            overlay_by_fy[fy_key].append(
                {
                    "fiscal_year": fy_key,
                    "asset_id": asset.asset_id,
                    "entry_type": "amort_expense",
                    "gifi_code": asset.book_amort_expense_gifi_code,
                    "account_code": "",
                    "net_cents": amort_cents,
                    "net_dollars": f"{amort_cents / 100:.2f}",
                    "description": f"Book amortization: {asset.description}",
                    "component_note": asset.book_depr_policy,
                }
            )

        # Balance sheet carryforward: asset cost and cumulative accumulated amortization per year.
        cumulative_amort = 0
        audit_fy_keys: list[str] = []
        started = False
        for fy in fys:
            if not started:
                if fy.fy != book_fy:
                    continue
                started = True

            audit_fy_keys.append(fy.fy)
            overlay_by_fy[fy.fy].append(
                {
                    "fiscal_year": fy.fy,
                    "asset_id": asset.asset_id,
                    "entry_type": "asset_balance",
                    "gifi_code": asset.book_asset_gifi_code,
                    "account_code": "",
                    "net_cents": total_cost_cents,
                    "net_dollars": f"{total_cost_cents / 100:.2f}",
                    "description": asset.description,
                    "component_note": "carryforward",
                }
            )

            if fy.fy in amort_by_fy:
                cumulative_amort += int(amort_by_fy[fy.fy])
            if cumulative_amort != 0:
                overlay_by_fy[fy.fy].append(
                    {
                        "fiscal_year": fy.fy,
                        "asset_id": asset.asset_id,
                        "entry_type": "accum_amort_balance",
                        "gifi_code": asset.book_accum_amort_gifi_code,
                        "account_code": "",
                        "net_cents": -cumulative_amort,
                        "net_dollars": f"{-cumulative_amort / 100:.2f}",
                        "description": asset.description,
                        "component_note": "carryforward",
                    }
                )

        component_notes = component_breakdown(resolved_asset.resolved_components, account_gifi)
        source_notes = source_breakdown(resolved_asset.resolved_components)
        for fy_key in audit_fy_keys:
            amort_cents = amort_by_fy.get(fy_key, 0)
            reclass_cents = total_cost_cents if fy_key == book_fy else 0
            audit_rows.append(
                {
                    "fiscal_year": fy_key,
                    "asset_id": asset.asset_id,
                    "description": asset.description,
                    "book_treatment": asset.book_treatment,
                    "book_depr_policy": asset.book_depr_policy,
                    "book_start_date": book_start_str,
                    "available_for_use_date": asset.available_for_use_date,
                    "total_cost_cents": total_cost_cents,
                    "total_cost_dollars": total_cost_dollars,
                    "reclass_total_cents": reclass_cents,
                    "reclass_total_dollars": round_cents_to_dollar(reclass_cents),
                    "amortization_cents": amort_cents,
                    "amortization_dollars": round_cents_to_dollar(amort_cents),
                    "book_asset_gifi_code": asset.book_asset_gifi_code,
                    "book_accum_amort_gifi_code": asset.book_accum_amort_gifi_code,
                    "book_amort_expense_gifi_code": asset.book_amort_expense_gifi_code,
                    "component_breakdown": component_notes,
                    "source_breakdown": source_notes,
                    "notes": asset.notes or "",
                }
            )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for fy in fys:
        rows = overlay_by_fy.get(fy.fy, [])
        rows_sorted = sorted(
            rows,
            key=lambda r: (
                r.get("asset_id") or "",
                r.get("entry_type") or "",
                r.get("gifi_code") or "",
                r.get("account_code") or "",
            ),
        )
        write_overlay_csv(rows_sorted, args.out_dir / f"book_fixed_asset_overlay_{fy.fy}.csv")

    audit_rows_sorted = sorted(audit_rows, key=lambda r: (r["fiscal_year"], r["asset_id"]))
    write_audit_csv(audit_rows_sorted, args.out_dir / "book_fixed_asset_overlay_audit.csv")

    summary_rows = []
    for fy in fys:
        summary = summary_by_fy.get(fy.fy, {})
        cap_cents = int(summary.get("capitalized_additions_cents") or 0)
        exp_cents = int(summary.get("expensed_additions_cents") or 0)
        amort_cents = int(summary.get("book_amortization_cents") or 0)
        summary_rows.append(
            {
                "fiscal_year": fy.fy,
                "capitalized_asset_count": int(summary.get("capitalized_asset_count") or 0),
                "expensed_asset_count": int(summary.get("expensed_asset_count") or 0),
                "capitalized_additions_cents": cap_cents,
                "capitalized_additions_dollars": round_cents_to_dollar(cap_cents),
                "expensed_additions_cents": exp_cents,
                "expensed_additions_dollars": round_cents_to_dollar(exp_cents),
                "book_amortization_cents": amort_cents,
                "book_amortization_dollars": round_cents_to_dollar(amort_cents),
            }
        )

    write_summary_csv(summary_rows, args.out_dir / "book_fixed_asset_overlay_summary.csv")

    print("BOOK FIXED ASSET OVERLAY BUILT")
    print(f"- out_dir: {args.out_dir}")
    for fy in fys:
        print(f"- {fy.fy}: book_fixed_asset_overlay_{fy.fy}.csv")
    print("- audit: book_fixed_asset_overlay_audit.csv")
    print("- summary: book_fixed_asset_overlay_summary.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
