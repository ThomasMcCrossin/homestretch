#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from datetime import date
from decimal import Decimal
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest
from cca_assets_lib import (
    CCA_CLASS_DESC,
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


def build_schedule_8(
    resolved_assets: list[ResolvedAsset],
    fys,
) -> dict[str, dict[str, dict[str, int | str | float]]]:
    assets_by_fy: dict[str, list[ResolvedAsset]] = {}
    for asset in resolved_assets:
        assets_by_fy.setdefault(asset.fy, []).append(asset)

    schedule_by_fy: dict[str, dict[str, dict[str, int | str | float]]] = {}
    opening_ucc_by_class: dict[str, int] = {}

    for fy in fys:
        days, denom, proration_factor = days_in_fy(fy)
        fy_assets = assets_by_fy.get(fy.fy, [])
        additions_by_class: dict[str, int] = {}
        base_additions_by_class: dict[str, Decimal] = {}
        claim_percent_by_class: dict[str, Decimal] = {}

        for asset in fy_assets:
            class_key = str(asset.asset.cca_class)
            additions_by_class[class_key] = additions_by_class.get(class_key, 0) + asset.total_cost_cents
            afu = date.fromisoformat(asset.asset.available_for_use_date)
            base_factor = first_year_base_factor(asset.asset, afu)
            base_additions_by_class[class_key] = base_additions_by_class.get(class_key, Decimal("0")) + (
                Decimal(asset.total_cost_cents) / Decimal(100)
            ) * base_factor

            if class_key in claim_percent_by_class:
                if claim_percent_by_class[class_key] != asset.asset.claim_percent_of_max:
                    raise SystemExit(
                        f"CCA asset class {class_key} in {fy.fy} has mixed claim_percent_of_max values; "
                        "set a consistent value per class/year."
                    )
            else:
                claim_percent_by_class[class_key] = asset.asset.claim_percent_of_max

        classes = sorted(
            set(opening_ucc_by_class) | set(additions_by_class),
            key=lambda x: int(x) if str(x).isdigit() else 10**9,
        )
        fy_rows: dict[str, dict[str, int | str | float]] = {}
        closing_ucc_by_class: dict[str, int] = {}

        for class_key in classes:
            if class_key not in CCA_CLASS_RATES:
                raise SystemExit(f"Unknown CCA class rate for class {class_key}. Add it to the class_rates map.")
            opening = opening_ucc_by_class.get(class_key, 0)
            additions_cents = additions_by_class.get(class_key, 0)
            additions_dollars = round_cents_to_dollar(additions_cents)
            base_additions = base_additions_by_class.get(class_key, Decimal("0"))
            base = Decimal(opening) + base_additions
            rate = CCA_CLASS_RATES[class_key]
            claim_percent = claim_percent_by_class.get(class_key, Decimal("1.0"))

            cca_claim = round_to_dollar(base * rate * claim_percent * proration_factor)
            closing = opening + additions_dollars - cca_claim

            fy_rows[class_key] = {
                "class": class_key,
                "description": CCA_CLASS_DESC.get(class_key, ""),
                "rate": float(CCA_CLASS_RATES[class_key]),
                "opening_ucc": int(opening),
                "additions": int(additions_dollars),
                "dispositions": 0,
                "half_year_base": round_to_dollar(base),
                "cca_claim": int(cca_claim),
                "closing_ucc": int(closing),
            }

            closing_ucc_by_class[class_key] = closing

        if fy_assets and not fy_rows:
            raise SystemExit(
                f"Schedule 8 build failed for {fy.fy}: assets present ({len(fy_assets)}) but no class rows were produced."
            )

        schedule_by_fy[fy.fy] = fy_rows
        opening_ucc_by_class = closing_ucc_by_class

    return schedule_by_fy


def write_schedule_8_csv(rows: dict[str, dict[str, int | str | float]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "Class",
                "Description",
                "Rate",
                "Opening_UCC",
                "Additions",
                "Dispositions",
                "Half_year_base",
                "CCA_Claim",
                "Closing_UCC",
                "Note",
            ]
        )
        for class_key, row in sorted(rows.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 10**9):
            w.writerow(
                [
                    row.get("class"),
                    row.get("description"),
                    row.get("rate"),
                    row.get("opening_ucc"),
                    row.get("additions"),
                    row.get("dispositions"),
                    row.get("half_year_base"),
                    row.get("cca_claim"),
                    row.get("closing_ucc"),
                    "",
                ]
            )


def write_resolved_assets_csv(resolved: list[ResolvedAsset], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "asset_id",
                "description",
                "cca_class",
                "fiscal_year",
                "available_for_use_date",
                "total_cost_cents",
                "total_cost_dollars",
                "claim_percent_of_max",
                "aii_eligible",
                "aii_factor",
                "first_year_base_factor",
                "half_year_rule",
                "half_year_applied",
                "source_breakdown",
            ]
        )
        for ra in resolved:
            afu = date.fromisoformat(ra.asset.available_for_use_date)
            parts = []
            for comp in ra.resolved_components:
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
            w.writerow(
                [
                    ra.asset.asset_id,
                    ra.asset.description,
                    ra.asset.cca_class,
                    ra.fy,
                    ra.asset.available_for_use_date,
                    ra.total_cost_cents,
                    round_cents_to_dollar(ra.total_cost_cents),
                    str(ra.asset.claim_percent_of_max),
                    "yes" if ra.asset.aii_eligible else "no",
                    str(aii_factor(ra.asset, afu)),
                    str(first_year_base_factor(ra.asset, afu)),
                    "yes" if ra.asset.half_year_rule else "no",
                    "yes" if ra.half_year_applied else "no",
                    " | ".join(parts),
                ]
            )


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
    resolved: list[ResolvedAsset] = []
    try:
        for asset in assets:
            resolved_components: list[ResolvedComponent] = []
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

    schedule_by_fy = build_schedule_8(resolved, fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for fy in fys:
        write_schedule_8_csv(schedule_by_fy.get(fy.fy, {}), args.out_dir / f"schedule_8_{fy.fy}.csv")

    write_resolved_assets_csv(resolved, args.out_dir / "cca_asset_register_resolved.csv")

    print("CCA SCHEDULE 8 BUILT")
    print(f"- out_dir: {args.out_dir}")
    for fy in fys:
        print(f"- {fy.fy}: schedule_8_{fy.fy}.csv")
    print("- asset register: cca_asset_register_resolved.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
