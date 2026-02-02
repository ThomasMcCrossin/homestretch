#!/usr/bin/env python3
"""
Generate a repo-local FY2024 ending inventory estimate CSV using FY2025 physical count items as the basis.

Why:
- FY2024 did not have a physical count; management wants a defensible estimate.
- We use FY2025 item list composition and scale it down to land in a target band.
- Quantities are rounded to whole numbers for most items (we allow decimals only if the FY2025 source uses decimals).

Output:
- data/inventory/Canteen Inventory May 31 2024 - Estimate from FY2025 Items.csv
- output/inventory_estimate_fy2024_from_fy2025_audit.csv
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR
from pathlib import Path

from _lib import PROJECT_ROOT, get_source, load_manifest


OUT_CSV_DEFAULT = PROJECT_ROOT / "data" / "inventory" / "Canteen Inventory May 31 2024 - Estimate from FY2025 Items.csv"
OUT_AUDIT_DEFAULT = PROJECT_ROOT / "output" / "inventory_estimate_fy2024_from_fy2025_audit.csv"


def d(s: str | int | float | Decimal) -> Decimal:
    if isinstance(s, Decimal):
        return s
    return Decimal(str(s))


def cents(x: Decimal) -> int:
    return int((x * Decimal(100)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def dollars_from_cents(c: int) -> str:
    return f"{Decimal(c) / Decimal(100):.2f}"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(1024 * 1024)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


@dataclass
class Item:
    product: str
    category: str
    qty: Decimal
    unit_cost: Decimal
    total: Decimal
    allow_decimal_qty: bool

    @property
    def key(self) -> tuple[str, str]:
        return (self.category, self.product)


def read_fy2025_items(path: Path) -> tuple[int, list[Item]]:
    """
    Returns (grand_total_cents, items).
    Expects FY2025 sheet format (includes '/Unit Cost' and a grand total row at the top).
    """
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    grand_total_cents = 0
    items: list[Item] = []

    for r in rows:
        product = (r.get("Product") or "").strip()
        category = (r.get("Category") or "").strip()
        total_s = (r.get("Total") or "").strip()
        qty_s = (r.get("Quantity") or "").strip()

        # Grand total row: blank product/category, Total set.
        if not product and not category and total_s:
            grand_total_cents = cents(d(total_s))
            continue

        # Category subtotal rows: blank product, category set.
        if not product:
            continue

        if not total_s or not qty_s:
            continue

        qty = d(qty_s)
        allow_decimal_qty = qty != qty.to_integral_value()

        unit_cost_s = (r.get("/Unit Cost") or r.get("Unit Cost") or "").strip()
        if unit_cost_s:
            unit_cost = d(unit_cost_s)
        else:
            # Fallback: compute from total/qty.
            unit_cost = (d(total_s) / qty) if qty else Decimal("0")

        total = d(total_s)
        items.append(
            Item(
                product=product,
                category=category,
                qty=qty,
                unit_cost=unit_cost,
                total=total,
                allow_decimal_qty=allow_decimal_qty,
            )
        )

    if grand_total_cents <= 0:
        grand_total_cents = sum(cents(it.total) for it in items)
    return grand_total_cents, items


def round_qty(item: Item, scaled_qty: Decimal) -> Decimal:
    if item.allow_decimal_qty:
        # Keep 2 decimals max for weighed/bulk-like quantities.
        return scaled_qty.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return scaled_qty.quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def build_initial_scaled(items: list[Item], *, scale: Decimal) -> dict[tuple[str, str], dict]:
    out: dict[tuple[str, str], dict] = {}
    for it in items:
        scaled_qty = it.qty * scale
        new_qty = round_qty(it, scaled_qty)
        if new_qty <= 0:
            continue
        new_total = (new_qty * it.unit_cost).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        out[it.key] = {
            "category": it.category,
            "product": it.product,
            "qty": new_qty,
            "unit_cost": it.unit_cost,
            "total": new_total,
            "notes": [],
        }
        if new_qty != scaled_qty:
            out[it.key]["notes"].append("rounded qty")
    return out


def current_total_cents(lines: dict[tuple[str, str], dict]) -> int:
    return sum(cents(v["total"]) for v in lines.values())


def settle_to_band(
    lines: dict[tuple[str, str], dict],
    *,
    target_center_cents: int,
    lower_cents: int,
    upper_cents: int,
    max_steps: int = 5000,
) -> None:
    """
    Adjust by +/-1 unit on integer-qty items to land within [lower_cents, upper_cents] deterministically.
    """
    def in_band(total: int) -> bool:
        return lower_cents <= total <= upper_cents

    total = current_total_cents(lines)
    if in_band(total):
        return

    # Only adjust integer-qty items.
    keys = [k for k, v in lines.items() if v["qty"] == v["qty"].to_integral_value()]
    keys = sorted(keys, key=lambda k: (k[0].lower(), k[1].lower()))

    for _ in range(max_steps):
        total = current_total_cents(lines)
        if in_band(total):
            return

        diff = target_center_cents - total  # positive means we need to increase total
        want_increase = diff > 0
        need = abs(diff)

        candidates = []
        for k in keys:
            v = lines.get(k)
            if not v:
                continue
            qty = v["qty"]
            if want_increase:
                pass
            else:
                if qty <= 0:
                    continue
                if qty == 0:
                    continue
                if qty == 1:
                    # allow subtracting to zero (drop line) if needed, but prefer not to.
                    pass
            unit = cents(v["unit_cost"])
            if unit <= 0:
                continue
            # Score: closeness to remaining need, then smaller unit for fine tuning, then stable tie-break.
            score = (abs(need - unit), unit, k[0].lower(), k[1].lower())
            candidates.append((score, k))

        if not candidates:
            break

        candidates.sort()
        k = candidates[0][1]
        v = lines[k]
        if want_increase:
            v["qty"] = v["qty"] + Decimal(1)
            v["total"] = (v["qty"] * v["unit_cost"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            v["notes"].append("tolerance settle +1")
        else:
            v["qty"] = v["qty"] - Decimal(1)
            if v["qty"] <= 0:
                # Drop the line entirely.
                del lines[k]
                continue
            v["total"] = (v["qty"] * v["unit_cost"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            v["notes"].append("tolerance settle -1")

    total = current_total_cents(lines)
    raise SystemExit(
        f"Could not settle inventory total into band: total=${dollars_from_cents(total)} "
        f"target_center=${dollars_from_cents(target_center_cents)} band=[{dollars_from_cents(lower_cents)},{dollars_from_cents(upper_cents)}]"
    )


def write_estimate_csv(
    *,
    out_path: Path,
    lines: dict[tuple[str, str], dict],
    target_center_cents: int,
    lower_cents: int,
    upper_cents: int,
) -> int:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    by_cat: dict[str, list[dict]] = {}
    for v in lines.values():
        by_cat.setdefault(str(v["category"]), []).append(v)

    # Deterministic ordering: by category name then product.
    for cat in by_cat:
        by_cat[cat] = sorted(by_cat[cat], key=lambda r: str(r["product"]).lower())

    grand_total = current_total_cents(lines)

    with out_path.open("w", encoding="utf-8", newline="") as f:
        fieldnames = ["Product", "Category", "Quantity", "Unit Cost", "Total", "Notes"]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerow(
            {
                "Product": "",
                "Category": "",
                "Quantity": "",
                "Unit Cost": "",
                "Total": dollars_from_cents(grand_total),
                "Notes": (
                    "ESTIMATE: FY2024 ending inventory derived from FY2025 physical count item list, scaled down; "
                    f"target_center=${dollars_from_cents(target_center_cents)} band=[{dollars_from_cents(lower_cents)},{dollars_from_cents(upper_cents)}]."
                ),
            }
        )

        for cat in sorted(by_cat.keys(), key=lambda s: s.lower()):
            cat_total_cents = sum(cents(v["total"]) for v in by_cat[cat])
            w.writerow(
                {
                    "Product": "",
                    "Category": cat,
                    "Quantity": "",
                    "Unit Cost": "",
                    "Total": dollars_from_cents(cat_total_cents),
                    "Notes": "Scaled from FY2025 item list; quantities rounded where applicable.",
                }
            )
            for v in by_cat[cat]:
                qty = v["qty"]
                qty_s = str(int(qty)) if qty == qty.to_integral_value() else f"{qty:.2f}"
                unit_cost_s = f"{Decimal(v['unit_cost']):.6f}".rstrip("0").rstrip(".")
                notes = "; ".join(dict.fromkeys(v["notes"]))  # stable de-dupe, preserve order
                w.writerow(
                    {
                        "Product": v["product"],
                        "Category": v["category"],
                        "Quantity": qty_s,
                        "Unit Cost": unit_cost_s,
                        "Total": f"{Decimal(v['total']):.2f}",
                        "Notes": notes,
                    }
                )
    return grand_total


def write_audit_csv(
    *,
    out_path: Path,
    fy2025_path: Path,
    fy2025_total_cents: int,
    target_center_cents: int,
    lower_cents: int,
    upper_cents: int,
    scale: Decimal,
    lines: dict[tuple[str, str], dict],
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    total = current_total_cents(lines)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "fy",
            "source_fy2025_path",
            "source_fy2025_total",
            "target_center",
            "target_lower",
            "target_upper",
            "scale_factor",
            "result_total",
            "category",
            "product",
            "qty",
            "unit_cost",
            "line_total",
            "notes",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for k in sorted(lines.keys(), key=lambda x: (x[0].lower(), x[1].lower())):
            v = lines[k]
            qty = v["qty"]
            qty_s = str(int(qty)) if qty == qty.to_integral_value() else f"{qty:.2f}"
            w.writerow(
                {
                    "fy": "FY2024",
                    "source_fy2025_path": str(fy2025_path),
                    "source_fy2025_total": dollars_from_cents(fy2025_total_cents),
                    "target_center": dollars_from_cents(target_center_cents),
                    "target_lower": dollars_from_cents(lower_cents),
                    "target_upper": dollars_from_cents(upper_cents),
                    "scale_factor": f"{scale:.8f}",
                    "result_total": dollars_from_cents(total),
                    "category": v["category"],
                    "product": v["product"],
                    "qty": qty_s,
                    "unit_cost": f"{Decimal(v['unit_cost']):.6f}".rstrip("0").rstrip("."),
                    "line_total": f"{Decimal(v['total']):.2f}",
                    "notes": "; ".join(dict.fromkeys(v["notes"])),
                }
            )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-csv", type=Path, default=OUT_CSV_DEFAULT)
    ap.add_argument("--out-audit", type=Path, default=OUT_AUDIT_DEFAULT)
    ap.add_argument("--target-center", type=int, default=513700, help="Target center in cents (default: $5,137.00).")
    ap.add_argument("--tolerance", type=int, default=5000, help="Tolerance in cents (default: $50.00).")
    args = ap.parse_args()

    manifest = load_manifest()
    fy2025_src = get_source(manifest, "inventory_count_fy2025_may16_csv")
    fy2025_path = Path(str(fy2025_src.get("path") or "")).expanduser()
    if not fy2025_path.exists():
        raise SystemExit(f"FY2025 inventory source missing: {fy2025_path}")

    target_center_cents = int(args.target_center)
    tol = int(args.tolerance)
    lower_cents = target_center_cents - tol
    upper_cents = target_center_cents + tol

    fy2025_total_cents, items = read_fy2025_items(fy2025_path)
    scale = (Decimal(target_center_cents) / Decimal(fy2025_total_cents)) if fy2025_total_cents else Decimal("0")

    lines = build_initial_scaled(items, scale=scale)
    settle_to_band(
        lines,
        target_center_cents=target_center_cents,
        lower_cents=lower_cents,
        upper_cents=upper_cents,
    )
    result_total_cents = write_estimate_csv(
        out_path=args.out_csv,
        lines=lines,
        target_center_cents=target_center_cents,
        lower_cents=lower_cents,
        upper_cents=upper_cents,
    )
    write_audit_csv(
        out_path=args.out_audit,
        fy2025_path=fy2025_path,
        fy2025_total_cents=fy2025_total_cents,
        target_center_cents=target_center_cents,
        lower_cents=lower_cents,
        upper_cents=upper_cents,
        scale=scale,
        lines=lines,
    )

    print("FY2024 INVENTORY ESTIMATE (FROM FY2025) GENERATED")
    print(f"- out_csv: {args.out_csv}")
    print(f"- out_csv_sha256: {sha256_file(args.out_csv)}")
    print(f"- out_audit: {args.out_audit}")
    print(f"- fy2025_source: {fy2025_path}")
    print(f"- fy2025_total: ${dollars_from_cents(fy2025_total_cents)}")
    print(f"- target_center: ${dollars_from_cents(target_center_cents)} (tol +/- ${dollars_from_cents(tol)})")
    print(f"- result_total: ${dollars_from_cents(result_total_cents)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

