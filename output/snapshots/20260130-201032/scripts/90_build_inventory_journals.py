#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    FiscalYear,
    connect_db,
    dollars_to_cents,
    fiscal_years_from_manifest,
    get_source,
    load_manifest,
    load_yaml,
)


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def category_to_inventory_account(category: str) -> str:
    c = (category or "").strip().lower()
    if c == "beverages":
        return "1210"  # Inventory - Beverage
    if c == "supplements":
        return "1220"  # Inventory - Supplements
    if c in ("snacks", "retail", "retail goods", "retail_goods"):
        return "1230"  # Inventory - Retail Goods
    # Default bucket (dry food/condiments/frozen/disposables/etc)
    return "1200"  # Inventory - Food


def inventory_account_to_cogs_account(inv_account: str) -> str:
    mapping = {
        "1200": "5000",  # COGS - Food
        "1210": "5010",  # COGS - Beverage
        "1220": "5020",  # COGS - Supplements
        "1230": "5030",  # COGS - Retail Goods
    }
    return mapping.get(str(inv_account), "5000")


def parse_inventory_category_totals(path: Path) -> tuple[int, dict[str, int]]:
    """
    Returns (grand_total_cents, totals_by_inventory_account_cents).

    Uses category subtotal rows where Product is blank and Category is set.
    Grand total is taken from the first row where Category is blank and Total is set (or from sum of categories).
    """
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Find grand total candidates (blank category)
    grand_total_cents = 0
    for r in rows:
        cat = (r.get("Category") or "").strip()
        product = (r.get("Product") or "").strip()
        total = (r.get("Total") or "").strip()
        if cat == "" and product == "" and total:
            grand_total_cents = dollars_to_cents(total)
            if grand_total_cents:
                break

    # Category totals
    by_inv: dict[str, int] = {}
    for r in rows:
        cat = (r.get("Category") or "").strip()
        product = (r.get("Product") or "").strip()
        total = (r.get("Total") or "").strip()
        if not cat or product:
            continue
        if not total:
            continue
        cents = dollars_to_cents(total)
        if cents <= 0:
            continue
        inv_acct = category_to_inventory_account(cat)
        by_inv[inv_acct] = by_inv.get(inv_acct, 0) + cents

    if grand_total_cents <= 0 and by_inv:
        grand_total_cents = sum(by_inv.values())

    # If category sums exist but don't match the grand total, keep the grand total as truth
    # and push any remainder into Inventory - Food for determinism.
    if grand_total_cents > 0 and by_inv:
        diff = grand_total_cents - sum(by_inv.values())
        if diff != 0:
            by_inv["1200"] = by_inv.get("1200", 0) + diff

    # If we couldn't parse category totals, fall back to a single bucket.
    if grand_total_cents > 0 and not by_inv:
        by_inv["1200"] = grand_total_cents

    # Drop any zero entries after diff adjustment.
    by_inv = {k: v for k, v in by_inv.items() if v != 0}
    return grand_total_cents, by_inv


def post_inventory_entry(
    conn,
    *,
    je_id: str,
    entry_date: str,
    entry_type: str,
    description: str,
    notes: str,
    source_system: str,
    source_record_type: str,
    source_record_id: str,
    lines: list[tuple[str, int, int, str]],
) -> None:
    conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
    conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

    conn.execute(
        """
        INSERT INTO journal_entries (
          id, entry_date, entry_type, description,
          source_system, source_record_type, source_record_id,
          notes, is_posted
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0)
        """,
        (je_id, entry_date, entry_type, description, source_system, source_record_type, source_record_id, notes),
    )

    debit_total = 0
    credit_total = 0
    for i, (account_code, debit_cents, credit_cents, line_desc) in enumerate(lines, start=1):
        conn.execute(
            """
            INSERT INTO journal_entry_lines (
              id, journal_entry_id, line_number,
              account_code, debit_cents, credit_cents, description
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (f"{je_id}:{i}", je_id, i, account_code, int(debit_cents), int(credit_cents), line_desc or None),
        )
        debit_total += int(debit_cents)
        credit_total += int(credit_cents)

    if debit_total != credit_total:
        conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
        conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))
        raise SystemExit(f"Unbalanced inventory JE {je_id}: debits={debit_total} credits={credit_total}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing inventory journals before insert.")
    ap.add_argument("--inv-fy2024-source-key", default="inventory_count_fy2024_may31_estimated_csv")
    ap.add_argument("--inv-fy2025-source-key", default="inventory_count_fy2025_may16_csv")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    by_fy = {fy.fy: fy for fy in fys}
    if "FY2024" not in by_fy or "FY2025" not in by_fy:
        raise SystemExit("Expected FY2024 and FY2025 in manifest fiscal_years")

    cfg = load_config(args.config)
    source_cfg = (cfg.get("journal_sources") or {}).get("inventory") if isinstance(cfg.get("journal_sources"), dict) else {}
    accounts_cfg = cfg.get("accounts", {}) if isinstance(cfg.get("accounts"), dict) else {}

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "inventory")
    entry_type = str((source_cfg or {}).get("entry_type") or "ADJUSTMENT")

    fy2024 = by_fy["FY2024"]
    fy2025 = by_fy["FY2025"]

    inv24_path = Path(str(get_source(manifest, args.inv_fy2024_source_key).get("path") or ""))
    inv25_path = Path(str(get_source(manifest, args.inv_fy2025_source_key).get("path") or ""))

    inv24_total, inv24_by_inv = parse_inventory_category_totals(inv24_path)
    inv25_total, inv25_by_inv = parse_inventory_category_totals(inv25_path)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "inventory_journal_summary.md"
    out_detail_csv = args.out_dir / "inventory_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )

        detail_rows: list[dict[str, str]] = []
        posted = 0

        # FY2024 closing inventory (asset up / COGS down)
        if inv24_total > 0:
            lines: list[tuple[str, int, int, str]] = []
            for inv_acct, cents in sorted(inv24_by_inv.items()):
                cogs = inventory_account_to_cogs_account(inv_acct)
                if cents > 0:
                    lines.append((inv_acct, cents, 0, "Closing inventory (FY2024)"))
                    lines.append((cogs, 0, cents, "COGS adjustment for closing inventory (FY2024)"))

            je_id = "INVENTORY_CLOSE_FY2024"
            notes = f"source={inv24_path}; inventory_total_cents={inv24_total}"
            post_inventory_entry(
                conn,
                je_id=je_id,
                entry_date=fy2024.end_date,
                entry_type=entry_type,
                description="Closing inventory adjustment (FY2024)",
                notes=notes,
                source_system=source_system,
                source_record_type=source_record_type,
                source_record_id=fy2024.fy,
                lines=lines,
            )
            posted += 1
            detail_rows.append(
                {
                    "fy": fy2024.fy,
                    "entry_date": fy2024.end_date,
                    "entry_kind": "CLOSE",
                    "inventory_total": cents_to_dollars(inv24_total),
                    "journal_entry_id": je_id,
                }
            )

        # FY2025 opening inventory reversal (COGS up / asset down)
        if inv24_total > 0:
            lines = []
            for inv_acct, cents in sorted(inv24_by_inv.items()):
                cogs = inventory_account_to_cogs_account(inv_acct)
                if cents > 0:
                    lines.append((cogs, cents, 0, "Opening inventory (FY2025)"))
                    lines.append((inv_acct, 0, cents, "Reverse prior closing inventory (FY2025 opening)"))

            je_id = "INVENTORY_OPEN_FY2025"
            notes = f"source_opening={inv24_path}; opening_inventory_total_cents={inv24_total}"
            post_inventory_entry(
                conn,
                je_id=je_id,
                entry_date=fy2025.start_date,
                entry_type=entry_type,
                description="Opening inventory adjustment (FY2025)",
                notes=notes,
                source_system=source_system,
                source_record_type=source_record_type,
                source_record_id=fy2025.fy,
                lines=lines,
            )
            posted += 1
            detail_rows.append(
                {
                    "fy": fy2025.fy,
                    "entry_date": fy2025.start_date,
                    "entry_kind": "OPEN",
                    "inventory_total": cents_to_dollars(inv24_total),
                    "journal_entry_id": je_id,
                }
            )

        # FY2025 closing inventory
        if inv25_total > 0:
            lines = []
            for inv_acct, cents in sorted(inv25_by_inv.items()):
                cogs = inventory_account_to_cogs_account(inv_acct)
                if cents > 0:
                    lines.append((inv_acct, cents, 0, "Closing inventory (FY2025)"))
                    lines.append((cogs, 0, cents, "COGS adjustment for closing inventory (FY2025)"))

            je_id = "INVENTORY_CLOSE_FY2025"
            notes = f"source={inv25_path}; inventory_total_cents={inv25_total}; note=inventory_count_date_2025-05-16"
            post_inventory_entry(
                conn,
                je_id=je_id,
                entry_date=fy2025.end_date,
                entry_type=entry_type,
                description="Closing inventory adjustment (FY2025)",
                notes=notes,
                source_system=source_system,
                source_record_type=source_record_type,
                source_record_id=fy2025.fy,
                lines=lines,
            )
            posted += 1
            detail_rows.append(
                {
                    "fy": fy2025.fy,
                    "entry_date": fy2025.end_date,
                    "entry_kind": "CLOSE",
                    "inventory_total": cents_to_dollars(inv25_total),
                    "journal_entry_id": je_id,
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = ["fy", "entry_date", "entry_kind", "inventory_total", "journal_entry_id"]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Inventory journals\n\n")
            f.write(f"- FY2024 closing inventory source: `{inv24_path}`\n")
            f.write(f"- FY2025 closing inventory source: `{inv25_path}`\n")
            f.write(f"- Journal entries posted: {posted}\n")
            f.write(f"- FY2024 closing inventory total: ${cents_to_dollars(inv24_total)}\n")
            f.write(f"- FY2025 closing inventory total: ${cents_to_dollars(inv25_total)}\n")

        conn.commit()

    finally:
        conn.close()

    print("INVENTORY JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

