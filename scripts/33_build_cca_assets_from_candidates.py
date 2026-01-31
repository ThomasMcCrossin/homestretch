#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml

from _lib import PROJECT_ROOT, load_yaml


DEFAULT_REVIEW_PATH = PROJECT_ROOT / "output" / "cca_candidates.csv"
DEFAULT_ASSET_PATH = PROJECT_ROOT / "overrides" / "cca_assets_from_candidates.yml"
DEFAULT_BASE_ASSET_PATH = PROJECT_ROOT / "overrides" / "cca_assets.yml"


def is_truthy(value: str) -> bool:
    v = (value or "").strip().lower()
    return v in {"yes", "y", "true", "1", "include", "keep"}


def parse_allocations(raw: str) -> list[tuple[str, int]]:
    out: list[tuple[str, int]] = []
    for part in (raw or "").split(";"):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            raise SystemExit(f"Invalid allocation_breakdown entry: {part!r} (expected account:amount_cents)")
        account, amount = part.split(":", 1)
        account = account.strip()
        amount = amount.strip()
        if not account:
            raise SystemExit(f"Invalid allocation_breakdown entry: {part!r} (missing account_code)")
        try:
            cents = int(Decimal(amount))
        except Exception as exc:
            raise SystemExit(f"Invalid amount_cents in allocation_breakdown: {part!r}") from exc
        out.append((account, cents))
    return out


def merge_components(components: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[tuple[str, int, str], int] = {}
    notes: dict[tuple[str, int, str], str | None] = {}
    for comp in components:
        key = (comp["source_type"], int(comp["wave_bill_id"]), str(comp["account_code"]))
        merged[key] = merged.get(key, 0) + int(comp["amount_cents"])
        if comp.get("notes"):
            notes[key] = str(comp.get("notes") or "")

    out: list[dict[str, Any]] = []
    for key, amount in merged.items():
        source_type, wave_bill_id, account_code = key
        row = {
            "source_type": source_type,
            "wave_bill_id": int(wave_bill_id),
            "account_code": account_code,
            "amount_cents": int(amount),
        }
        if notes.get(key):
            row["notes"] = notes[key]
        out.append(row)
    return out


def load_review_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Review file not found: {path}")
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--review", type=Path, default=DEFAULT_REVIEW_PATH, help="Reviewed candidate CSV.")
    ap.add_argument(
        "--out", type=Path, default=DEFAULT_ASSET_PATH, help="Output asset register YAML to generate."
    )
    ap.add_argument(
        "--base", type=Path, default=DEFAULT_BASE_ASSET_PATH, help="Base asset register for policy/version defaults."
    )
    ap.add_argument(
        "--require-cca-class",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Require cca_class for included rows.",
    )
    args = ap.parse_args()

    review_rows = load_review_rows(args.review)
    base = load_yaml(args.base) if args.base.exists() else {"version": 1, "policy": {}, "assets": []}

    assets_by_id: dict[str, dict[str, Any]] = {}

    for row in review_rows:
        include = is_truthy(str(row.get("include") or ""))
        if not include:
            continue

        source_type = str(row.get("source_type") or "").strip()
        record_id = str(row.get("record_id") or "").strip()
        if source_type != "wave_bill":
            raise SystemExit(
                f"Unsupported source_type for auto-ingest: {source_type!r} (record_id={record_id}). "
                "Only wave_bill allocations are supported right now."
            )
        if not record_id:
            raise SystemExit("Missing record_id for included row.")

        asset_id = str(row.get("asset_id") or "").strip()
        if not asset_id:
            raise SystemExit(f"Included row {record_id} missing asset_id.")

        description = str(row.get("asset_description") or row.get("vendor") or "").strip()
        if not description:
            raise SystemExit(f"Asset {asset_id} missing description.")

        afu_date = str(row.get("available_for_use_date") or row.get("date") or "").strip()
        if not afu_date:
            raise SystemExit(f"Asset {asset_id} missing available_for_use_date.")

        cca_class = str(row.get("cca_class") or "").strip()
        if args.require_cca_class and not cca_class:
            raise SystemExit(f"Asset {asset_id} missing cca_class.")

        components = []
        allocations = parse_allocations(str(row.get("allocation_breakdown") or ""))
        for account_code, amount_cents in allocations:
            components.append(
                {
                    "source_type": "wave_bill_allocation",
                    "wave_bill_id": int(record_id),
                    "account_code": account_code,
                    "amount_cents": int(amount_cents),
                }
            )

        asset = assets_by_id.get(asset_id)
        if not asset:
            asset = {
                "asset_id": asset_id,
                "description": description,
                "cca_class": cca_class,
                "available_for_use_date": afu_date,
                "source_components": [],
            }
            assets_by_id[asset_id] = asset

        asset["source_components"].extend(components)

        notes = str(row.get("notes") or "").strip()
        if notes:
            asset["notes"] = notes

        def set_if_present(key: str) -> None:
            value = str(row.get(key) or "").strip()
            if value:
                asset[key] = value

        set_if_present("book_treatment")
        set_if_present("book_asset_gifi_code")
        set_if_present("book_accum_amort_gifi_code")
        set_if_present("book_amort_expense_gifi_code")
        set_if_present("book_depr_policy")
        set_if_present("useful_life_years")
        set_if_present("book_start_date")
        set_if_present("claim_percent_of_max")
        set_if_present("half_year_rule")
        set_if_present("aii_eligible")

    if not assets_by_id:
        raise SystemExit("No included rows found in review file.")

    for asset in assets_by_id.values():
        asset["source_components"] = merge_components(asset.get("source_components", []))
        if not asset["source_components"]:
            raise SystemExit(f"Asset {asset['asset_id']} has no source_components after parsing.")

    out_doc = {
        "version": int(base.get("version") or 1),
        "policy": base.get("policy") or {},
        "assets": sorted(assets_by_id.values(), key=lambda a: a["asset_id"]),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(yaml.safe_dump(out_doc, sort_keys=False), encoding="utf-8")

    print("CCA ASSET REGISTER BUILT FROM CANDIDATES")
    print(f"- review: {args.review}")
    print(f"- out: {args.out}")
    print(f"- assets: {len(out_doc['assets'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
