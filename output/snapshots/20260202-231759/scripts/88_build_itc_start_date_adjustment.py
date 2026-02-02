#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    connect_db,
    fiscal_years_from_manifest,
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

def allocate_proportional_cents(total_cents: int, parts: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    Allocate total_cents proportionally across parts (account_code, basis_cents), ensuring exact cent total.
    Deterministic rounding: ROUND_HALF_UP for all but last; last receives the remaining cents.
    """
    positive = [(acct, int(basis)) for acct, basis in parts if int(basis) > 0]
    if total_cents <= 0 or not positive:
        return [(acct, 0) for acct, _ in parts]

    total_basis = sum(basis for _, basis in positive)
    if total_basis <= 0:
        return [(acct, 0) for acct, _ in parts]

    remaining = int(total_cents)
    out: list[tuple[str, int]] = []
    for i, (acct, basis) in enumerate(positive):
        if i == len(positive) - 1:
            alloc = remaining
        else:
            alloc_dec = (Decimal(basis) * Decimal(total_cents) / Decimal(total_basis)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
            alloc = int(alloc_dec)
            if alloc < 0:
                alloc = 0
            if alloc > remaining:
                alloc = remaining
            remaining -= alloc
        out.append((acct, alloc))

    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing ITC start-date adjustment journals before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    revenue_cfg = cfg.get("revenue", {}) if isinstance(cfg.get("revenue"), dict) else {}
    tax_cfg = cfg.get("tax", {}) if isinstance(cfg.get("tax"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("itc_start_date_adjustment") if isinstance(cfg.get("journal_sources"), dict) else {}

    income_to_review_code = str(revenue_cfg.get("income_to_review_code") or "4090").strip()
    hst_itc_code = str(tax_cfg.get("hst_itc_code") or "2210").strip()
    itc_start_date = str(tax_cfg.get("itc_start_date") or "2024-02-26").strip()
    itc_start = date.fromisoformat(itc_start_date)

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "itc_start_date_adjustment")
    entry_type = str((source_cfg or {}).get("entry_type") or "ADJUSTMENT")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "itc_start_date_adjustment_summary.md"
    out_detail_csv = args.out_dir / "itc_start_date_adjustment_detail.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )

        posted = 0
        detail_rows: list[dict[str, str]] = []

        for fy in fys:
            fy_start = date.fromisoformat(fy.start_date)
            fy_end = date.fromisoformat(fy.end_date)

            if itc_start <= fy_start:
                continue

            pre_end = min(fy_end, itc_start - timedelta(days=1))
            if pre_end < fy_start:
                continue

            bills = conn.execute(
                """
                SELECT id, invoice_date, tax_cents, total_cents, vendor_norm, invoice_number
                FROM wave_bills
                WHERE invoice_date >= ? AND invoice_date <= ?
                  AND CAST(tax_cents AS INTEGER) > 0
                ORDER BY invoice_date, id
                """,
                (fy_start.isoformat(), pre_end.isoformat()),
            ).fetchall()

            if not bills:
                continue

            # Accumulate additional expense per account_code by reallocating the pre-start ITC tax.
            expense_totals: dict[str, int] = {}
            total_tax = 0
            bills_with_missing_allocations = 0

            for b in bills:
                bill_id = int(b["id"])
                tax_cents = int(b["tax_cents"] or 0)
                if tax_cents <= 0:
                    continue

                alloc_rows = conn.execute(
                    """
                    SELECT account_code, amount_cents
                    FROM bill_allocations
                    WHERE wave_bill_id = ?
                    ORDER BY account_code
                    """,
                    (bill_id,),
                ).fetchall()

                non_tax_allocs_raw = [
                    (str(r["account_code"]).strip(), int(r["amount_cents"] or 0))
                    for r in alloc_rows
                    if str(r["account_code"]).strip() != hst_itc_code
                ]
                by_acct: dict[str, int] = {}
                for acct, amt in non_tax_allocs_raw:
                    by_acct[acct] = by_acct.get(acct, 0) + int(amt)
                non_tax_allocs = [(acct, amt) for acct, amt in by_acct.items()]
                non_tax_total = sum(v for _, v in non_tax_allocs)

                if non_tax_total <= 0:
                    # No usable allocation basis: push tax to income_to_review for transparency.
                    expense_totals[income_to_review_code] = expense_totals.get(income_to_review_code, 0) + tax_cents
                    bills_with_missing_allocations += 1
                    total_tax += tax_cents
                    continue

                allocs = allocate_proportional_cents(tax_cents, parts=non_tax_allocs)
                if not allocs:
                    expense_totals[income_to_review_code] = expense_totals.get(income_to_review_code, 0) + tax_cents
                    bills_with_missing_allocations += 1
                    total_tax += tax_cents
                    continue

                for acct, amt in allocs:
                    if amt == 0:
                        continue
                    expense_totals[acct] = expense_totals.get(acct, 0) + int(amt)

                total_tax += tax_cents

            if total_tax == 0:
                continue

            je_id = f"ITC_START_DATE_ADJUST_{fy.fy}"
            description = f"ITC start-date adjustment (pre-{itc_start_date} tax is expense) - {fy.fy}"
            notes = (
                f"itc_start_date={itc_start_date}; fy={fy.fy}; pre_start_end={pre_end.isoformat()}; "
                f"bills={len(bills)}; bills_missing_alloc_basis={bills_with_missing_allocations}; total_tax_cents={total_tax}"
            )

            conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
            conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

            conn.execute(
                """
                INSERT OR REPLACE INTO journal_entries (
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
            for acct in sorted(expense_totals.keys(), key=lambda x: (int(x) if x.isdigit() else 10**9, x)):
                amt = int(expense_totals[acct] or 0)
                if amt == 0:
                    continue
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
                        acct,
                        amt,
                        0,
                        "Pre-ITC-start-date sales tax (treated as expense)",
                    ),
                )
                debit_total += amt
                line_number += 1

            if debit_total != total_tax:
                raise SystemExit(f"Unbalanced ITC start-date adjustment {je_id}: debits={debit_total} tax_total={total_tax}")

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
                    hst_itc_code,
                    0,
                    total_tax,
                    "Remove ITC for pre-start-date bills (tax not claimable)",
                ),
            )

            posted += 1
            detail_rows.append(
                {
                    "fy": fy.fy,
                    "entry_date": fy.end_date,
                    "itc_start_date": itc_start_date,
                    "pre_start_end_date": pre_end.isoformat(),
                    "bills_count": str(len(bills)),
                    "bills_missing_alloc_basis": str(bills_with_missing_allocations),
                    "tax_reclassed_cents": str(total_tax),
                    "tax_reclassed": cents_to_dollars(total_tax),
                    "journal_entry_id": je_id,
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "fy",
                "entry_date",
                "itc_start_date",
                "pre_start_end_date",
                "bills_count",
                "bills_missing_alloc_basis",
                "tax_reclassed_cents",
                "tax_reclassed",
                "journal_entry_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# ITC start-date adjustment\n\n")
            f.write(f"- ITC start date: {itc_start_date}\n")
            f.write(f"- Journal entries posted: {posted}\n")
            if detail_rows:
                total = sum(int(r["tax_reclassed_cents"]) for r in detail_rows)
                f.write(f"- Total tax moved out of {hst_itc_code}: ${cents_to_dollars(total)}\n")

        conn.commit()

    finally:
        conn.close()

    print("ITC START-DATE ADJUSTMENT BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
