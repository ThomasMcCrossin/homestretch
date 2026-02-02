from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from _lib import load_yaml


AIIP_ELIGIBILITY_START = date(2018, 11, 21)  # acquired after Nov 20, 2018
AIIP_ELIGIBILITY_END_EXCLUSIVE = date(2028, 1, 1)  # available for use before 2028


DEFAULT_BOOK_TREATMENT = "expense"
DEFAULT_BOOK_ASSET_GIFI_CODE = "1740"
DEFAULT_BOOK_ACCUM_AMORT_GIFI_CODE = "1741"
DEFAULT_BOOK_AMORT_EXPENSE_GIFI_CODE = "8670"
DEFAULT_BOOK_DEPR_POLICY = "none"

CCA_CLASS_RATES: dict[str, Decimal] = {
    "8": Decimal("0.20"),
    "12": Decimal("1.00"),
    "50": Decimal("0.55"),
}

CCA_CLASS_DESC: dict[str, str] = {
    "8": "General equipment",
    "12": "Tools and utensils under $500",
    "50": "Computer hardware and systems software",
}


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
    aii_eligible: bool
    source_components: list[AssetComponent]
    claim_percent_of_max: Decimal
    half_year_rule: bool
    notes: str | None
    book_treatment: str
    book_asset_gifi_code: str
    book_accum_amort_gifi_code: str
    book_amort_expense_gifi_code: str
    book_depr_policy: str
    useful_life_years: Decimal | None
    book_start_date: str | None


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
    half_year_applied: bool
    aii_factor: Decimal
    first_year_base_factor: Decimal


def round_to_dollar(amount: Decimal) -> int:
    return int(amount.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def round_cents_to_dollar(cents: int) -> int:
    return round_to_dollar(Decimal(int(cents)) / Decimal(100))


def _normalize_book_treatment(raw: str) -> str:
    treatment = (raw or "").strip().lower()
    if treatment in ("", "none"):
        return DEFAULT_BOOK_TREATMENT
    if treatment not in {"expense", "capitalize"}:
        raise SystemExit(f"Invalid book_treatment: {raw!r} (expected 'expense' or 'capitalize')")
    return treatment


def _normalize_book_policy(raw: str) -> str:
    policy = (raw or "").strip().lower()
    if policy in ("", "none"):
        return "none"
    if policy not in {"none", "mirror_tax", "straight_line"}:
        raise SystemExit(
            f"Invalid book_depr_policy: {raw!r} (expected 'none', 'mirror_tax', or 'straight_line')"
        )
    return policy


def _normalize_gifi_code(raw: str | None, default: str) -> str:
    code = (raw or "").strip() or default
    return code


def load_assets(path: Path) -> tuple[dict, list[Asset]]:
    data = load_yaml(path)
    if not isinstance(data.get("assets"), list):
        raise SystemExit("overrides/cca_assets.yml must include an assets list")

    policy = data.get("policy") if isinstance(data.get("policy"), dict) else {}
    default_claim = Decimal(str(policy.get("default_claim_percent_of_max", "1.0")))
    default_half_year = bool(policy.get("default_half_year_rule", True))
    default_aii_eligible = bool(policy.get("default_aii_eligible", True))
    default_book_treatment = _normalize_book_treatment(str(policy.get("default_book_treatment", DEFAULT_BOOK_TREATMENT)))
    default_book_asset = _normalize_gifi_code(policy.get("default_book_asset_gifi_code"), DEFAULT_BOOK_ASSET_GIFI_CODE)
    default_book_accum = _normalize_gifi_code(
        policy.get("default_book_accum_amort_gifi_code"), DEFAULT_BOOK_ACCUM_AMORT_GIFI_CODE
    )
    default_book_amort = _normalize_gifi_code(
        policy.get("default_book_amort_expense_gifi_code"), DEFAULT_BOOK_AMORT_EXPENSE_GIFI_CODE
    )
    default_book_depr_policy = _normalize_book_policy(str(policy.get("default_book_depr_policy", DEFAULT_BOOK_DEPR_POLICY)))

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
        aii_eligible = bool(raw.get("aii_eligible", default_aii_eligible))

        book_treatment = _normalize_book_treatment(str(raw.get("book_treatment", default_book_treatment)))
        book_asset_gifi_code = _normalize_gifi_code(raw.get("book_asset_gifi_code"), default_book_asset)
        book_accum_amort_gifi_code = _normalize_gifi_code(raw.get("book_accum_amort_gifi_code"), default_book_accum)
        book_amort_expense_gifi_code = _normalize_gifi_code(
            raw.get("book_amort_expense_gifi_code"), default_book_amort
        )
        book_depr_policy = _normalize_book_policy(str(raw.get("book_depr_policy", default_book_depr_policy)))
        useful_life_years = raw.get("useful_life_years")
        if useful_life_years is not None:
            useful_life_years = Decimal(str(useful_life_years))

        book_start_date = str(raw.get("book_start_date") or "").strip() or None

        if book_treatment == "expense" and book_depr_policy != "none":
            raise SystemExit(
                f"CCA asset {asset_id} has book_treatment=expense but book_depr_policy={book_depr_policy}; "
                "set book_depr_policy to 'none' or switch book_treatment to 'capitalize'."
            )

        if book_depr_policy == "straight_line" and useful_life_years in (None, Decimal("0")):
            raise SystemExit(f"CCA asset {asset_id} missing useful_life_years (required for straight_line)")

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
                aii_eligible=aii_eligible,
                source_components=comps,
                claim_percent_of_max=claim_percent,
                half_year_rule=half_year_rule,
                notes=str(raw.get("notes") or "").strip() or None,
                book_treatment=book_treatment,
                book_asset_gifi_code=book_asset_gifi_code,
                book_accum_amort_gifi_code=book_accum_amort_gifi_code,
                book_amort_expense_gifi_code=book_amort_expense_gifi_code,
                book_depr_policy=book_depr_policy,
                useful_life_years=useful_life_years,
                book_start_date=book_start_date,
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


def has_leap_day(start: date, end: date) -> bool:
    year = start.year
    while year <= end.year:
        try:
            leap = date(year, 2, 29)
        except ValueError:
            year += 1
            continue
        if start <= leap <= end:
            return True
        year += 1
    return False


def days_in_fy(fy) -> tuple[int, int, Decimal]:
    start = date.fromisoformat(fy.start_date)
    end = date.fromisoformat(fy.end_date)
    days = (end - start).days + 1
    denom = 366 if has_leap_day(start, end) else 365
    if days > denom:
        raise SystemExit(f"Fiscal year {fy.fy} has {days} days (exceeds {denom}); check manifest dates.")
    factor = Decimal(days) / Decimal(denom)
    if days < denom and factor >= Decimal("1"):
        raise SystemExit(f"Fiscal year {fy.fy} proration factor invalid: days={days}, denom={denom}.")
    return days, denom, factor


def aii_factor(asset: Asset, afu_date: date) -> Decimal:
    """
    Accelerated Investment Incentive (AII) "enhancement factor" for half-year property.

    This repo uses a simplified model aligned to how UFile prints Schedule 8:
    - If the asset is not AII eligible, factor = 1.0.
    - If AFU is outside the AII eligibility window, factor = 1.0.
    - Otherwise, phase-based factors (AFU date):
      - < 2024-01-01: 3.0
      - 2024-01-01 .. 2025-12-31: 2.0
      - 2026-01-01 .. 2027-12-31: 1.5
    """

    if not asset.aii_eligible:
        return Decimal("1.0")
    if afu_date < AIIP_ELIGIBILITY_START or afu_date >= AIIP_ELIGIBILITY_END_EXCLUSIVE:
        return Decimal("1.0")
    if afu_date < date(2024, 1, 1):
        return Decimal("3.0")
    if afu_date < date(2026, 1, 1):
        return Decimal("2.0")
    return Decimal("1.5")


def first_year_base_factor(asset: Asset, afu_date: date) -> Decimal:
    """
    Return the multiplier applied to acquisition cost when computing the first-year CCA base.

    - If half_year_rule is false -> 1.0
    - If half_year_rule is true -> 0.5 * aii_factor (AII factor defaults to 1.0 when ineligible)
    """

    if not asset.half_year_rule:
        return Decimal("1.0")
    return Decimal("0.5") * aii_factor(asset, afu_date)


def half_year_applies(asset: Asset, afu_date: date) -> bool:
    """
    Precedence rules:
    - If half_year_rule is false, never apply the half-year rule.
    - If AII enhancement applies (factor > 1.0), the half-year rule is not applied in its normal 50% form.
    - Otherwise, apply the standard half-year rule.
    """

    if not asset.half_year_rule:
        return False
    if aii_factor(asset, afu_date) > Decimal("1.0"):
        return False
    return True
