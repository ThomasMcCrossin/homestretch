#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    FiscalYear,
    allocation_rounding,
    connect_db,
    dollars_to_cents,
    fiscal_years_from_manifest,
    get_source,
    load_manifest,
    load_yaml,
)


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"


@dataclass(frozen=True)
class MonthlySalesRow:
    month: date  # first day of month
    gross_sales_cents: int
    net_sales_cents: int
    taxes_cents: int
    returns_cents: int
    orders: int


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def parse_iso_month(s: str) -> date:
    # Shopify export uses YYYY-MM-01 strings.
    return date.fromisoformat(str(s).strip())


def days_in_month(d: date) -> int:
    next_month = (d.replace(day=28) + timedelta(days=4)).replace(day=1)
    return (next_month - d.replace(day=1)).days


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def iter_monthly_sales_rows(path: Path) -> list[MonthlySalesRow]:
    rows: list[MonthlySalesRow] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            month = parse_iso_month(r.get("Month") or "")
            rows.append(
                MonthlySalesRow(
                    month=month,
                    gross_sales_cents=dollars_to_cents(r.get("Gross sales")),
                    net_sales_cents=dollars_to_cents(r.get("Net sales")),
                    taxes_cents=dollars_to_cents(r.get("Taxes")),
                    returns_cents=dollars_to_cents(r.get("Returns")),
                    orders=int(float(r.get("Orders") or 0)),
                )
            )
    return rows


def sum_taxes_by_month(rows: list[MonthlySalesRow]) -> dict[date, int]:
    out: dict[date, int] = {}
    for r in rows:
        out[r.month] = out.get(r.month, 0) + int(r.taxes_cents or 0)
    return out


def prorate_month_value(month: date, *, value_cents: int, start_date: date) -> int:
    """
    Prorate the given month total to only include days from start_date onward,
    when start_date falls within that month. Deterministic integer cents.
    """
    if start_date.year != month.year or start_date.month != month.month:
        return int(value_cents)
    dim = days_in_month(month)
    if dim <= 0:
        return int(value_cents)
    # Inclusive of start_date day.
    days_in_scope = dim - start_date.day + 1
    if days_in_scope <= 0:
        return 0
    if days_in_scope >= dim:
        return int(value_cents)
    return int(round(int(value_cents) * days_in_scope / dim))


def taxes_in_range(
    taxes_by_month: dict[date, int],
    *,
    start_date: date,
    end_date: date,
    prorate_start_month: bool,
) -> int:
    total = 0
    for month, cents in taxes_by_month.items():
        if month < start_date.replace(day=1) or month > end_date.replace(day=1):
            continue
        if month.year == start_date.year and month.month == start_date.month and prorate_start_month:
            total += prorate_month_value(month, value_cents=cents, start_date=start_date)
        else:
            total += int(cents or 0)
    return total


def fetch_gross_sales_basis(conn, *, start_date: str, end_date: str, shopify_sales_code: str, cash_sales_code: str) -> tuple[int, int]:
    """
    Compute gross sales credits (in cents) for Shopify payouts vs cash deposits from bank inflow journals.
    These are used as weights to allocate the Shopify-reported tax total across the two revenue accounts.
    """
    row = conn.execute(
        """
        SELECT
          SUM(CASE WHEN je.id LIKE 'BANK_INFLOW_SHOPIFY_PAYOUT_%' AND jl.account_code = ? THEN CAST(jl.credit_cents AS INTEGER) ELSE 0 END) AS shopify_credits,
          SUM(CASE WHEN je.id LIKE 'BANK_INFLOW_CASH_DEPOSIT_%' AND jl.account_code = ? THEN CAST(jl.credit_cents AS INTEGER) ELSE 0 END) AS cash_credits
        FROM journal_entries je
        JOIN journal_entry_lines jl ON jl.journal_entry_id = je.id
        WHERE je.source_record_type = 'bank_inflows'
          AND je.entry_date >= ? AND je.entry_date <= ?
        """,
        (shopify_sales_code, cash_sales_code, start_date, end_date),
    ).fetchone()
    shopify = int(row["shopify_credits"] or 0) if row else 0
    cash = int(row["cash_credits"] or 0) if row else 0
    return shopify, cash


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing Shopify sales tax journals before insert.")
    ap.add_argument("--manifest-source-key", default="shopify_sales_by_month_bulk_csv")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    revenue_cfg = cfg.get("revenue", {}) if isinstance(cfg.get("revenue"), dict) else {}
    tax_cfg = cfg.get("tax", {}) if isinstance(cfg.get("tax"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("shopify_sales_tax") if isinstance(cfg.get("journal_sources"), dict) else {}

    shopify_sales_code = str(revenue_cfg.get("shopify_sales_code") or "4100").strip()
    cash_sales_code = str(revenue_cfg.get("cash_deposit_sales_code") or "4000").strip()
    income_to_review_code = str(revenue_cfg.get("income_to_review_code") or "4090").strip()

    hst_payable_code = str(tax_cfg.get("hst_payable_code") or "2200").strip()
    itc_start_date = str(tax_cfg.get("itc_start_date") or "2024-02-26").strip()
    itc_start = date.fromisoformat(itc_start_date)

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "shopify_sales_tax")
    entry_type = str((source_cfg or {}).get("entry_type") or "ADJUSTMENT")

    src = get_source(manifest, args.manifest_source_key)
    report_path = Path(str(src.get("path") or "")).expanduser()
    if not report_path.exists():
        raise SystemExit(f"Shopify sales report not found: {report_path}")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "shopify_sales_tax_journal_summary.md"
    out_detail_csv = args.out_dir / "shopify_sales_tax_journal_detail.csv"

    monthly_rows = iter_monthly_sales_rows(report_path)
    taxes_by_month = sum_taxes_by_month(monthly_rows)

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )

        detail_rows: list[dict[str, str]] = []
        posted = 0

        for fy in fys:
            fy_start = date.fromisoformat(fy.start_date)
            fy_end = date.fromisoformat(fy.end_date)

            # Apply ITC/tax start date guardrail.
            eff_start = max(fy_start, itc_start)
            if eff_start > fy_end:
                continue

            taxes_total = taxes_in_range(
                taxes_by_month,
                start_date=eff_start,
                end_date=fy_end,
                prorate_start_month=True,
            )
            if taxes_total == 0:
                continue

            shopify_basis, cash_basis = fetch_gross_sales_basis(
                conn,
                start_date=eff_start.isoformat(),
                end_date=fy_end.isoformat(),
                shopify_sales_code=shopify_sales_code,
                cash_sales_code=cash_sales_code,
            )

            basis_total = shopify_basis + cash_basis
            if basis_total <= 0:
                # If no basis is found, allocate all tax to the primary Shopify sales code.
                alloc_shopify = taxes_total
                alloc_cash = 0
            else:
                allocs = allocation_rounding(
                    taxes_total,
                    weights=[
                        ("shopify", float(shopify_basis)),
                        ("cash", float(cash_basis)),
                    ],
                )
                alloc_map = {k: v for k, v in allocs}
                alloc_shopify = int(alloc_map.get("shopify") or 0)
                alloc_cash = int(alloc_map.get("cash") or 0)

            je_id = f"SHOPIFY_SALES_TAX_{fy.fy}"
            description = f"Shopify sales tax reclass (sales -> HST payable) - {fy.fy}"
            notes = (
                f"source={report_path}; manifest_key={args.manifest_source_key}; "
                f"itc_start_date={itc_start_date}; effective_start={eff_start.isoformat()}; "
                f"taxes_total_cents={taxes_total}; basis_shopify_cents={shopify_basis}; basis_cash_cents={cash_basis}; "
                f"allocated_shopify_cents={alloc_shopify}; allocated_cash_cents={alloc_cash}"
            )

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
                (
                    je_id,
                    fy.end_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    fy.fy,
                    notes,
                ),
            )

            line_number = 1
            debit_total = 0

            if alloc_shopify:
                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:{line_number}",
                        je_id,
                        line_number,
                        shopify_sales_code,
                        alloc_shopify,
                        0,
                        "Sales tax collected (Shopify) - reclass out of revenue",
                    ),
                )
                debit_total += alloc_shopify
                line_number += 1

            if alloc_cash:
                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:{line_number}",
                        je_id,
                        line_number,
                        cash_sales_code,
                        alloc_cash,
                        0,
                        "Sales tax collected (cash) - reclass out of revenue",
                    ),
                )
                debit_total += alloc_cash
                line_number += 1

            # Guardrail: if rounding left a tiny difference, push it to income_to_review (still debited).
            if debit_total != taxes_total:
                diff = taxes_total - debit_total
                if diff != 0:
                    conn.execute(
                        """
                        INSERT INTO journal_entry_lines (
                          id, journal_entry_id, line_number,
                          account_code, debit_cents, credit_cents, description
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            f"{je_id}:{line_number}",
                            je_id,
                            line_number,
                            income_to_review_code,
                            diff if diff > 0 else 0,
                            abs(diff) if diff < 0 else 0,
                            "Rounding diff from sales tax allocation (review)",
                        ),
                    )
                    if diff > 0:
                        debit_total += diff
                    else:
                        debit_total -= abs(diff)
                    line_number += 1

            conn.execute(
                """
                INSERT INTO journal_entry_lines (
                  id, journal_entry_id, line_number,
                  account_code, debit_cents, credit_cents, description
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    f"{je_id}:{line_number}",
                    je_id,
                    line_number,
                    hst_payable_code,
                    0,
                    taxes_total,
                    "HST collected on sales (per Shopify sales report)",
                ),
            )

            posted += 1
            detail_rows.append(
                {
                    "fy": fy.fy,
                    "entry_date": fy.end_date,
                    "itc_start_date": itc_start_date,
                    "effective_start_date": eff_start.isoformat(),
                    "taxes_cents": str(taxes_total),
                    "taxes": cents_to_dollars(taxes_total),
                    "basis_shopify_cents": str(shopify_basis),
                    "basis_shopify": cents_to_dollars(shopify_basis),
                    "basis_cash_cents": str(cash_basis),
                    "basis_cash": cents_to_dollars(cash_basis),
                    "allocated_shopify_cents": str(alloc_shopify),
                    "allocated_shopify": cents_to_dollars(alloc_shopify),
                    "allocated_cash_cents": str(alloc_cash),
                    "allocated_cash": cents_to_dollars(alloc_cash),
                    "journal_entry_id": je_id,
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "fy",
                "entry_date",
                "itc_start_date",
                "effective_start_date",
                "taxes_cents",
                "taxes",
                "basis_shopify_cents",
                "basis_shopify",
                "basis_cash_cents",
                "basis_cash",
                "allocated_shopify_cents",
                "allocated_shopify",
                "allocated_cash_cents",
                "allocated_cash",
                "journal_entry_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Shopify sales tax journals\n\n")
            f.write(f"- Source report: `{report_path}` (manifest key `{args.manifest_source_key}`)\n")
            f.write(f"- ITC/HST start date: {itc_start_date}\n")
            f.write(f"- Journal entries posted: {posted}\n")
            if detail_rows:
                total = sum(int(r["taxes_cents"]) for r in detail_rows)
                f.write(f"- Total sales tax credited to {hst_payable_code}: ${cents_to_dollars(total)}\n")

        conn.commit()

    finally:
        conn.close()

    print("SHOPIFY SALES TAX JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

