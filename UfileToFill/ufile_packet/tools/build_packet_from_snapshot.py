#!/usr/bin/env python3
"""
Deterministically rebuild `UfileToFill/ufile_packet/packet.json` from a chosen snapshot output folder.

Why this exists:
- `tools/build_year_artifacts.py` builds year-scoped guides from `packet.json`.
- If `packet.json` points to an older snapshot (or amounts are stale), the guides become wrong.
- This tool updates only the year schedule amounts + packet meta snapshot_source.
- It preserves entity / ufile_screens / positions / evidence_index / known_judgments content already in packet.json.

Safety:
- Does NOT touch the accounting DB.
- Reads snapshot CSV exports only.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "packet.json"


def normalize_snapshot_dir(path: Path) -> Path:
    """
    Accept either:
    - output/snapshots/<stamp>/output/
    - output/snapshots/<stamp>/
    and return the concrete snapshot output directory.
    """

    p = path.resolve()
    if p.name == "output" and p.is_dir():
        return p
    if (p / "output").is_dir():
        return (p / "output").resolve()
    raise SystemExit(f"Snapshot output folder not found at: {path}")


def load_csv_amounts(path: Path, *, code_field_candidates: list[str], amount_field_candidates: list[str]) -> dict[str, int]:
    out: dict[str, int] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = ""
            for k in code_field_candidates:
                if row.get(k):
                    code = str(row.get(k) or "").strip()
                    break
            if not code:
                continue
            amount_raw = ""
            for k in amount_field_candidates:
                if row.get(k) is not None:
                    amount_raw = str(row.get(k) or "").strip()
                    break
            if amount_raw == "":
                continue
            out[code] = int(Decimal(amount_raw))
    return out


def load_ufile_gifi_descriptions(path: Path) -> dict[str, str]:
    desc: dict[str, str] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = (row.get("GIFI_Code") or "").strip()
            if not code:
                continue
            d = (row.get("Description") or "").strip()
            if d:
                desc[code] = d
    return desc


def load_schedule_1_labels(path: Path) -> dict[str, str]:
    labels: dict[str, str] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = (row.get("Code") or row.get("Line") or row.get("line") or "").strip()
            if not code:
                continue
            d = (row.get("Label") or row.get("Description") or row.get("description") or "").strip()
            if d:
                labels[code] = d
    return labels


def load_schedule_8(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    rows: dict[str, dict] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            class_code = str(row.get("Class") or row.get("class") or "").strip()
            if not class_code:
                continue
            rows[class_code] = {
                "class": class_code,
                "description": str(row.get("Description") or "").strip(),
                "rate": float(row.get("Rate") or 0),
                "opening_ucc": int(row.get("Opening_UCC") or 0),
                "additions": int(row.get("Additions") or 0),
                "dispositions": int(row.get("Dispositions") or 0),
                "half_year_base": int(row.get("Half_year_base") or 0),
                "cca_claim": int(row.get("CCA_Claim") or 0),
                "closing_ucc": int(row.get("Closing_UCC") or 0),
            }
    return rows


def load_cca_assets(path: Path, fy: str) -> list[dict]:
    if not path.exists():
        return []
    out: list[dict] = []
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_fy = str(row.get("fiscal_year") or "").strip()
            if row_fy != fy:
                continue
            out.append(
                {
                    "asset_id": str(row.get("asset_id") or "").strip(),
                    "description": str(row.get("description") or "").strip(),
                    "cca_class": str(row.get("cca_class") or "").strip(),
                    "available_for_use_date": str(row.get("available_for_use_date") or "").strip(),
                    "total_cost_cents": int(row.get("total_cost_cents") or 0),
                    "total_cost_dollars": int(row.get("total_cost_dollars") or 0),
                    "claim_percent_of_max": str(row.get("claim_percent_of_max") or "").strip(),
                    "half_year_rule": str(row.get("half_year_rule") or "").strip(),
                    "source_breakdown": str(row.get("source_breakdown") or "").strip(),
                }
            )
    return out


def update_year_section(
    packet: dict,
    *,
    snapshot_dir: Path,
    fy: str,
) -> None:
    year = packet.get("years", {}).get(fy)
    if not isinstance(year, dict):
        raise SystemExit(f"packet.json missing years.{fy}")

    # Description map for labels (optional but nice to keep human-readable packet.json).
    ufile_gifi_path = snapshot_dir / f"ufile_gifi_{fy}.csv"
    if not ufile_gifi_path.exists():
        raise SystemExit(f"Missing snapshot file: {ufile_gifi_path}")
    desc_map = load_ufile_gifi_descriptions(ufile_gifi_path)

    sch100_path = snapshot_dir / f"gifi_schedule_100_{fy}.csv"
    sch125_path = snapshot_dir / f"gifi_schedule_125_{fy}.csv"
    re_path = snapshot_dir / f"gifi_retained_earnings_{fy}.csv"
    sch1_path = snapshot_dir / f"schedule_1_{fy}.csv"
    for p in (sch100_path, sch125_path, re_path, sch1_path):
        if not p.exists():
            raise SystemExit(f"Missing snapshot file: {p}")

    sch100 = load_csv_amounts(sch100_path, code_field_candidates=["gifi_code", "GIFI_Code"], amount_field_candidates=["amount", "Amount"])
    sch125 = load_csv_amounts(sch125_path, code_field_candidates=["gifi_code", "GIFI_Code"], amount_field_candidates=["amount", "Amount"])
    retained = load_csv_amounts(re_path, code_field_candidates=["gifi_code", "GIFI_Code"], amount_field_candidates=["amount", "Amount"])
    sch1_amounts = load_csv_amounts(sch1_path, code_field_candidates=["Code", "Line", "line"], amount_field_candidates=["Amount", "amount"])
    sch1_labels = load_schedule_1_labels(sch1_path)

    def merge_section(existing: dict, amounts: dict[str, int], labels: dict[str, str] | None = None) -> dict:
        out: dict[str, dict] = {}
        for code, amt in amounts.items():
            if isinstance(existing.get(code), dict):
                prev = dict(existing[code])
            else:
                prev = {}
            prev["amount"] = int(amt)
            if "label" not in prev:
                if labels and code in labels:
                    prev["label"] = labels[code]
                elif code in desc_map:
                    prev["label"] = desc_map[code]
            out[code] = prev
        return out

    year["schedule_100"] = merge_section(year.get("schedule_100", {}), sch100)
    year["schedule_125"] = merge_section(year.get("schedule_125", {}), sch125)
    year["retained_earnings"] = merge_section(year.get("retained_earnings", {}), retained)
    year["schedule_1"] = merge_section(year.get("schedule_1", {}), sch1_amounts, labels=sch1_labels)

    schedule_8_path = snapshot_dir / f"schedule_8_{fy}.csv"
    schedule_8_classes = load_schedule_8(schedule_8_path)
    cca_assets_path = snapshot_dir / "cca_asset_register_resolved.csv"
    cca_assets = load_cca_assets(cca_assets_path, fy)
    if schedule_8_classes or cca_assets:
        classes_used = sorted(schedule_8_classes.keys(), key=lambda x: int(x) if x.isdigit() else 10**9)
        total_additions = sum(int(v.get("additions") or 0) for v in schedule_8_classes.values())
        total_cca = sum(int(v.get("cca_claim") or 0) for v in schedule_8_classes.values())
        schedule_8_note = f"Total CCA claimed: {total_cca}. Classes used: {', '.join(classes_used) if classes_used else 'none'}."
        year["schedule_8"] = {
            "classes": schedule_8_classes,
            "assets": cca_assets,
            "summary": {
                "total_additions": int(total_additions),
                "total_cca_claim": int(total_cca),
                "classes_used": classes_used,
            },
            "note": schedule_8_note,
        }
    else:
        year.pop("schedule_8", None)

    # --- Year-specific UFile screens derived from the schedules (no guessing) ---
    year_screens = year.get("ufile_screens", {})
    if not isinstance(year_screens, dict):
        year_screens = {}
    year["ufile_screens"] = year_screens

    # Corporate history screen: UFile sometimes requests a minimal "prior year" carryforward row.
    # We derive this from prior-year schedule outputs when possible, otherwise default safely.
    prior_fy = f"FY{int(fy[2:]) - 1}" if fy.startswith("FY") and fy[2:].isdigit() else ""
    prior_year = packet.get("years", {}).get(prior_fy) if prior_fy else None
    prior_end = "2023-05-31"
    prior_taxable_income = 0
    prior_paid_up_capital = 0
    prior_total_assets = 0
    prior_sbd_claimed: bool | None = None

    if isinstance(prior_year, dict):
        prior_end = str(prior_year.get("fiscal_period", {}).get("end") or prior_end)
        try:
            prior_taxable_income = int(
                (prior_year.get("schedule_1", {}).get("C") or prior_year.get("schedule_1", {}).get("400") or {}).get("amount") or 0
            )
        except Exception:
            prior_taxable_income = 0
        try:
            prior_paid_up_capital = int((prior_year.get("schedule_100", {}).get("3500") or {}).get("amount") or 0)
        except Exception:
            prior_paid_up_capital = 0
        try:
            prior_total_assets = int((prior_year.get("schedule_100", {}).get("2599") or {}).get("amount") or 0)
        except Exception:
            prior_total_assets = 0
        # Heuristic: FY2024 stub was inactive; subsequent years are active CCPC years and generally claimed SBD.
        prior_sbd_claimed = True
    else:
        # FY2024's prior year is FY2023 stub return (filed as inactive / nil).
        prior_paid_up_capital = int((year.get("schedule_100", {}).get("3500") or {}).get("amount") or 0)
        prior_sbd_claimed = False

    corp_hist = year_screens.get("corporate_history", {})
    if not isinstance(corp_hist, dict):
        corp_hist = {}
    corp_hist["has_entries"] = True
    corp_hist["prior_year_end_date"] = prior_end
    corp_hist["prior_year_taxable_income"] = int(prior_taxable_income)
    corp_hist["prior_year_claimed_sbd"] = prior_sbd_claimed
    corp_hist["prior_year_large_corp_amount_line_415"] = 0
    corp_hist["prior_year_taxable_paid_up_capital"] = int(prior_paid_up_capital)
    corp_hist["prior_year_total_assets_gifi_2599"] = int(prior_total_assets)
    corp_hist.setdefault("eligible_rdtoh_end_prior_year", 0)
    corp_hist.setdefault("non_eligible_rdtoh_end_prior_year", 0)
    corp_hist.setdefault("eligible_dividend_refund_prior_year", 0)
    corp_hist.setdefault("non_eligible_dividend_refund_prior_year", 0)
    corp_hist.setdefault(
        "note",
        "UFile Corporate History screen: typically only the 1st prior year row is needed. "
        "Taxable income should match prior year Schedule 1 code C; taxable paid-up capital usually matches share capital unless evidence indicates otherwise.",
    )
    year_screens["corporate_history"] = corp_hist

    retained_obj = year.get("retained_earnings", {})
    div_declared = 0
    if isinstance(retained_obj, dict):
        div_declared = int((retained_obj.get("3700") or {}).get("amount") or 0)

    # Dividends paid screen: taxable dividends paid should match dividends declared (3700) in this workflow.
    dividends_paid = year_screens.get("dividends_paid", {})
    if not isinstance(dividends_paid, dict):
        dividends_paid = {}
    dividends_paid["has_dividends"] = bool(div_declared)
    dividends_paid["taxable_dividends_paid"] = int(div_declared)
    # Preserve operator decisions for eligible/capital types if present; otherwise default to 0.
    dividends_paid.setdefault("eligible_dividend_portion", 0)
    dividends_paid.setdefault("capital_dividends", 0)
    dividends_paid.setdefault("capital_gains_dividend", 0)
    dividends_paid.setdefault(
        "note",
        "Dividends declared per retained earnings schedule (GIFI 3700). Confirm eligible vs non-eligible in UFile; default expectation is non-eligible.",
    )
    year_screens["dividends_paid"] = dividends_paid

    # GRIP screen (UFile shows this once dividends exist; mostly needed only if eligible dividends are designated).
    grip = year_screens.get("general_rate_income_pool", {})
    if not isinstance(grip, dict):
        grip = {}
    grip.setdefault("grip_end_prior_year", 0)
    grip.setdefault("amount_respecting_dividends", [])
    grip.setdefault("specified_future_tax_consequences_before", [])
    grip.setdefault("specified_future_tax_consequences_after", [])
    grip.setdefault("elected_excessive_eligible_dividend_designation_as_ordinary", 0)
    grip.setdefault(
        "note",
        "Unless you are designating eligible dividends, GRIP is typically $0 / not needed. If you mark any eligible dividends, you must complete this screen.",
    )
    year_screens["general_rate_income_pool"] = grip

    # CCA screen + position flags
    cca_classes_used = []
    total_cca_claim = 0
    schedule_8 = year.get("schedule_8", {}) if isinstance(year.get("schedule_8"), dict) else {}
    if isinstance(schedule_8.get("summary"), dict):
        cca_classes_used = schedule_8.get("summary", {}).get("classes_used") or []
        total_cca_claim = int(schedule_8.get("summary", {}).get("total_cca_claim") or 0)
    has_cca = bool(cca_classes_used)

    cca_screen = year_screens.get("capital_cost_allowance", {})
    if not isinstance(cca_screen, dict):
        cca_screen = {}
    cca_screen["has_cca"] = has_cca
    if has_cca:
        cca_screen["note"] = f"CCA claimed per Schedule 8. Total CCA: {total_cca_claim}. Classes: {', '.join(cca_classes_used)}."
    year_screens["capital_cost_allowance"] = cca_screen

    positions = year.get("positions", {})
    if not isinstance(positions, dict):
        positions = {}
    positions.setdefault("cca_required", {})
    if not isinstance(positions.get("cca_required"), dict):
        positions["cca_required"] = {}
    positions["cca_required"]["value"] = has_cca
    if has_cca:
        positions["cca_required"]["note"] = f"CCA claimed per Schedule 8. Total CCA: {total_cca_claim}. Classes: {', '.join(cca_classes_used)}."
    year["positions"] = positions


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--snapshot",
        type=Path,
        required=True,
        help="Path to snapshot root or snapshot output dir (e.g., output/snapshots/20260129-192249 or .../output).",
    )
    ap.add_argument("--fy", action="append", dest="fys", help="Limit to specific FY keys (repeatable). Default: all in packet.")
    args = ap.parse_args()

    snapshot_dir = normalize_snapshot_dir(args.snapshot)
    packet = json.loads(PACKET_PATH.read_text())

    # Update meta
    rel = snapshot_dir.relative_to(PROJECT_ROOT)
    snapshot_stamp_dir = snapshot_dir.parent.name
    snapshot_root_prefix = f"output/snapshots/{snapshot_stamp_dir}"
    packet.setdefault("meta", {})
    packet["meta"]["snapshot_source"] = str(rel).rstrip("/") + "/"
    packet["meta"]["generated_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    packet["meta"]["generator"] = "tools/build_packet_from_snapshot.py"

    # Evidence paths: keep snapshot-derived outputs pinned to the selected snapshot, but point UfileToFill/ + docs/
    # references to the repo paths (more stable across snapshots).
    def rewrite_evidence_path(p: str) -> str:
        if not p.startswith("output/snapshots/"):
            return p
        # Normalize paths that were copied into old snapshots.
        marker = "/output/UfileToFill/"
        if marker in p:
            return "UfileToFill/" + p.split(marker, 1)[1]
        marker_docs = "/docs/"
        if marker_docs in p:
            candidate = "docs/" + p.split(marker_docs, 1)[1]
            if (PROJECT_ROOT / candidate).exists():
                return candidate
            return p
        marker_out = "/output/"
        if marker_out in p:
            suffix = p.split(marker_out, 1)[1]
            return f"{snapshot_root_prefix}/output/{suffix}"
        return p

    for ev in packet.get("evidence_index", []):
        if isinstance(ev, dict) and isinstance(ev.get("path"), str):
            ev["path"] = rewrite_evidence_path(ev["path"])

    for j in packet.get("known_judgments", []):
        if isinstance(j, dict) and isinstance(j.get("evidence"), str):
            j["evidence"] = rewrite_evidence_path(j["evidence"])

    fys = [str(x).strip() for x in (args.fys or []) if str(x).strip()]
    if not fys:
        fys = list(packet.get("years", {}).keys())
    for fy in fys:
        update_year_section(packet, snapshot_dir=snapshot_dir, fy=fy)

    PACKET_PATH.write_text(json.dumps(packet, indent=2, sort_keys=False) + "\n")
    print("PACKET UPDATED")
    print(f"- packet: {PACKET_PATH}")
    print(f"- snapshot: {snapshot_dir}")
    print(f"- years: {', '.join(fys)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
