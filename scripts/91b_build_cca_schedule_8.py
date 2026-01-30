#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


ASSET_REGISTER_PATH = PROJECT_ROOT / "overrides" / "cca_assets.yml"


@dataclass(frozen=True)
class AssetComponent:
    source_type: str
    wave_bill_id: int | None
    account_code: str | None
    amount_cents: int
    notes: str | None


@dataclass(frozen=True)
class Asset:
    asset_id: str
    description: str
    cca_class: str
    available_for_use_date: str
    source_components: list[AssetComponent]
    claim_percent_of_max: Decimal
    half_year_rule: bool
    notes: str | None


@dataclass(frozen=True)
class ResolvedComponent:
    source_type: str
    wave_bill_id: int | None
    account_code: str | None
    amount_cents: int
    invoice_date: str | None
    vendor_raw: str | None
    allocation_total_cents: int | None
    notes: str | None


@dataclass(frozen=True)
class ResolvedAsset:
    asset: Asset
    fy: str
    total_cost_cents: int
    resolved_components: list[ResolvedComponent]


def round_to_dollar(amount: Decimal) -> int:
    return int(amount.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def round_cents_to_dollar(cents: int) -> int:
    return round_to_dollar(Decimal(int(cents)) / Decimal(100))


def load_assets(path: Path) -> tuple[dict, list[Asset]]:
    data = load_yaml(path)
    if not isinstance(data.get("assets"), list):
        raise SystemExit("overrides/cca_assets.yml must include an assets list")

    policy = data.get("policy") if isinstance(data.get("policy"), dict) else {}
    default_claim = Decimal(str(policy.get("default_claim_percent_of_max", "1.0")))
    default_half_year = bool(policy.get("default_half_year_rule", True))

    assets: list[Asset] = []
    seen_ids: set[str] = set()
    for raw in data["assets"]:
        if not isinstance(raw, dict):
            continue
        asset_id = str(raw.get("asset_id") or "").strip()
        if not asset_id:
            raise SystemExit("Every CCA asset must have asset_id")
        if asset_id in seen_ids:
            raise SystemExit(f"Duplicate asset_id in CCA register: {asset_id}")
        seen_ids.add(asset_id)

        desc = str(raw.get("description") or "").strip()
        if not desc:
            raise SystemExit(f"CCA asset {asset_id} missing description")

        cca_class_raw = raw.get("cca_class")
        if cca_class_raw is None:
            raise SystemExit(f"CCA asset {asset_id} missing cca_class")
        cca_class = str(cca_class_raw).strip()

        afu = str(raw.get("available_for_use_date") or "").strip()
        if not afu:
            raise SystemExit(f"CCA asset {asset_id} missing available_for_use_date")

        comp_list = raw.get("source_components") or []
        if not isinstance(comp_list, list) or not comp_list:
            raise SystemExit(f"CCA asset {asset_id} missing source_components")

        claim_percent = Decimal(str(raw.get("claim_percent_of_max", default_claim)))
        half_year_rule = bool(raw.get("half_year_rule", default_half_year))

        comps: list[AssetComponent] = []
        for comp in comp_list:
            if not isinstance(comp, dict):
                continue
            source_type = str(comp.get("source_type") or "").strip()
            if not source_type:
                raise SystemExit(f"CCA asset {asset_id} has component missing source_type")
            wave_bill_id = comp.get("wave_bill_id")
            account_code = str(comp.get("account_code") or "").strip() or None
            amount_cents = int(comp.get("amount_cents") or 0)
            notes = str(comp.get("notes") or "").strip() or None
            comps.append(
                AssetComponent(
                    source_type=source_type,
                    wave_bill_id=int(wave_bill_id) if wave_bill_id is not None else None,
                    account_code=account_code,
                    amount_cents=amount_cents,
                    notes=notes,
                )
            )

        assets.append(
            Asset(
                asset_id=asset_id,
                description=desc,
                cca_class=cca_class,
                available_for_use_date=afu,
                source_components=comps,
                claim_percent_of_max=claim_percent,
                half_year_rule=half_year_rule,
                notes=str(raw.get("notes") or "").strip() or None,
            )
        )

    return data, assets


def resolve_component(conn, asset_id: str, comp: AssetComponent) -> ResolvedComponent:
    if comp.source_type == "wave_bill_allocation":
        if comp.wave_bill_id is None or comp.account_code is None:
            raise SystemExit(f"CCA asset {asset_id} wave_bill_allocation requires wave_bill_id + account_code")
        bill = conn.execute(
            "SELECT id, invoice_date, vendor_raw, total_cents, tax_cents, net_cents FROM wave_bills WHERE id = ?",
            (int(comp.wave_bill_id),),
        ).fetchone()
        if not bill:
            raise SystemExit(f"CCA asset {asset_id}: missing wave_bill_id={comp.wave_bill_id}")

        alloc_row = conn.execute(
            "SELECT SUM(CAST(amount_cents AS INTEGER)) AS total_cents FROM bill_allocations WHERE wave_bill_id = ? AND account_code = ?",
            (int(comp.wave_bill_id), comp.account_code),
        ).fetchone()
        alloc_total = int(alloc_row["total_cents"] or 0)
        if alloc_total < comp.amount_cents:
            raise SystemExit(
                "CCA asset {asset_id}: wave_bill_allocation mismatch for bill {bill_id} account {account} "
                "(expected >= {expected} cents, found {found} cents).".format(
                    asset_id=asset_id,
                    bill_id=comp.wave_bill_id,
                    account=comp.account_code,
                    expected=comp.amount_cents,
                    found=alloc_total,
                )
            )

        return ResolvedComponent(
            source_type=comp.source_type,
            wave_bill_id=comp.wave_bill_id,
            account_code=comp.account_code,
            amount_cents=comp.amount_cents,
            invoice_date=str(bill["invoice_date"] or ""),
            vendor_raw=str(bill["vendor_raw"] or ""),
            allocation_total_cents=alloc_total,
            notes=comp.notes,
        )

    raise SystemExit(f"CCA asset {asset_id}: unsupported source_type {comp.source_type}")


def fy_for_date(fys, dt: date) -> str:
    for fy in fys:
        start = date.fromisoformat(fy.start_date)
        end = date.fromisoformat(fy.end_date)
        if start <= dt <= end:
            return fy.fy
    raise SystemExit(f"Date {dt.isoformat()} does not fall within any fiscal year in manifest")


def build_schedule_8(
    resolved_assets: list[ResolvedAsset],
    fys,
) -> dict[str, dict[str, dict[str, int | str | float]]]:
    class_rates = {
        "8": 0.20,
        "50": 0.55,
    }
    class_desc = {
        "8": "General equipment",
        "50": "Computer hardware and systems software",
    }

    assets_by_fy: dict[str, list[ResolvedAsset]] = {}
    for asset in resolved_assets:
        assets_by_fy.setdefault(asset.fy, []).append(asset)

    schedule_by_fy: dict[str, dict[str, dict[str, int | str | float]]] = {}
    opening_ucc_by_class: dict[str, int] = {}

    for fy in fys:
        fy_assets = assets_by_fy.get(fy.fy, [])
        additions_by_class: dict[str, int] = {}
        half_year_additions_by_class: dict[str, Decimal] = {}
        claim_percent_by_class: dict[str, Decimal] = {}

        for asset in fy_assets:
            class_key = str(asset.asset.cca_class)
            additions_by_class[class_key] = additions_by_class.get(class_key, 0) + asset.total_cost_cents
            factor = Decimal("0.5") if asset.asset.half_year_rule else Decimal("1.0")
            half_year_additions_by_class[class_key] = half_year_additions_by_class.get(class_key, Decimal("0")) + (
                Decimal(asset.total_cost_cents) / Decimal(100)
            ) * factor

            if class_key in claim_percent_by_class:
                if claim_percent_by_class[class_key] != asset.asset.claim_percent_of_max:
                    raise SystemExit(
                        f"CCA asset class {class_key} in {fy.fy} has mixed claim_percent_of_max values; "
                        "set a consistent value per class/year."
                    )
            else:
                claim_percent_by_class[class_key] = asset.asset.claim_percent_of_max

        classes = sorted(set(opening_ucc_by_class) | set(additions_by_class), key=lambda x: int(x) if str(x).isdigit() else 10**9)
        fy_rows: dict[str, dict[str, int | str | float]] = {}
        closing_ucc_by_class: dict[str, int] = {}

        for class_key in classes:
            if class_key not in class_rates:
                raise SystemExit(f"Unknown CCA class rate for class {class_key}. Add it to the class_rates map.")
            opening = opening_ucc_by_class.get(class_key, 0)
            additions_cents = additions_by_class.get(class_key, 0)
            additions_dollars = round_cents_to_dollar(additions_cents)
            half_year_additions = half_year_additions_by_class.get(class_key, Decimal("0"))
            base = Decimal(opening) + half_year_additions
            rate = Decimal(str(class_rates[class_key]))
            claim_percent = claim_percent_by_class.get(class_key, Decimal("1.0"))

            cca_claim = round_to_dollar(base * rate * claim_percent)
            closing = opening + additions_dollars - cca_claim

            fy_rows[class_key] = {
                "class": class_key,
                "description": class_desc.get(class_key, ""),
                "rate": float(class_rates[class_key]),
                "opening_ucc": int(opening),
                "additions": int(additions_dollars),
                "dispositions": 0,
                "half_year_base": round_to_dollar(base),
                "cca_claim": int(cca_claim),
                "closing_ucc": int(closing),
            }

            closing_ucc_by_class[class_key] = closing

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
                "half_year_rule",
                "source_breakdown",
            ]
        )
        for ra in resolved:
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
                    "yes" if ra.asset.half_year_rule else "no",
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

            resolved.append(
                ResolvedAsset(
                    asset=asset,
                    fy=fy,
                    total_cost_cents=total_cost,
                    resolved_components=resolved_components,
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
