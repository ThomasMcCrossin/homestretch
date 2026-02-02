#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest


@dataclass(frozen=True)
class PayrollComponentTotals:
    fy: str
    source: str
    start_date: str
    end_date: str
    periods: int
    min_period_end: str | None
    max_period_end: str | None

    gross_pay_cents: int
    vacation_pay_cents: int
    tips_cents: int

    federal_tax_cents: int
    provincial_tax_cents: int
    employee_cpp_cents: int
    employee_cpp2_cents: int
    employee_ei_cents: int

    employer_cpp_cents: int
    employer_cpp2_cents: int
    employer_ei_cents: int

    net_pay_cents: int
    reported_total_deductions_cents: int | None
    reported_total_employer_cost_cents: int | None

    @property
    def employee_deductions_cents(self) -> int:
        return (
            self.federal_tax_cents
            + self.provincial_tax_cents
            + self.employee_cpp_cents
            + self.employee_cpp2_cents
            + self.employee_ei_cents
        )

    @property
    def employer_taxes_cents(self) -> int:
        return self.employer_cpp_cents + self.employer_cpp2_cents + self.employer_ei_cents

    @property
    def remittance_cents(self) -> int:
        return self.employee_deductions_cents + self.employer_taxes_cents

    @property
    def net_pay_plus_tips_cents(self) -> int:
        return self.net_pay_cents + self.tips_cents


def cents_to_dollars(cents: int) -> str:
    return f"{Decimal(cents) / Decimal(100):.2f}"


def fetch_employee_export_totals(
    conn: sqlite3.Connection,
    *,
    fy: FiscalYear,
    start_date: str,
    end_date: str,
) -> PayrollComponentTotals:
    row = conn.execute(
        """
        SELECT
          COUNT(*) AS periods,
          MIN(pay_period_end) AS min_period_end,
          MAX(pay_period_end) AS max_period_end,
          SUM(gross_pay_cents) AS gross_pay_cents,
          SUM(vacation_pay_cents) AS vacation_pay_cents,
          SUM(tips_cents) AS tips_cents,
          SUM(federal_tax_cents) AS federal_tax_cents,
          SUM(provincial_tax_cents) AS provincial_tax_cents,
          SUM(employee_cpp_cents) AS employee_cpp_cents,
          SUM(employee_ei_cents) AS employee_ei_cents,
          SUM(employer_cpp_cents) AS employer_cpp_cents,
          SUM(employer_ei_cents) AS employer_ei_cents,
          SUM(net_pay_cents) AS net_pay_cents
        FROM payroll_employee_pay_periods
        WHERE pay_period_end >= ? AND pay_period_end <= ?
        """,
        (start_date, end_date),
    ).fetchone()

    return PayrollComponentTotals(
        fy=fy.fy,
        source="employee_exports",
        start_date=start_date,
        end_date=end_date,
        periods=int(row["periods"] or 0),
        min_period_end=(str(row["min_period_end"]) if row["min_period_end"] else None),
        max_period_end=(str(row["max_period_end"]) if row["max_period_end"] else None),
        gross_pay_cents=int(row["gross_pay_cents"] or 0),
        vacation_pay_cents=int(row["vacation_pay_cents"] or 0),
        tips_cents=int(row["tips_cents"] or 0),
        federal_tax_cents=int(row["federal_tax_cents"] or 0),
        provincial_tax_cents=int(row["provincial_tax_cents"] or 0),
        employee_cpp_cents=int(row["employee_cpp_cents"] or 0),
        employee_cpp2_cents=0,
        employee_ei_cents=int(row["employee_ei_cents"] or 0),
        employer_cpp_cents=int(row["employer_cpp_cents"] or 0),
        employer_cpp2_cents=0,
        employer_ei_cents=int(row["employer_ei_cents"] or 0),
        net_pay_cents=int(row["net_pay_cents"] or 0),
        reported_total_deductions_cents=None,
        reported_total_employer_cost_cents=None,
    )


def fetch_curlysbooks_backfill_totals(
    conn: sqlite3.Connection,
    *,
    fy: FiscalYear,
    start_date: str,
    end_date: str,
    entity: str,
    tax_year: int,
    calculated_by: str,
) -> PayrollComponentTotals:
    row = conn.execute(
        """
        SELECT
          COUNT(*) AS periods,
          MIN(pp.end_date) AS min_period_end,
          MAX(pp.end_date) AS max_period_end,
          SUM(r.total_gross_cents) AS gross_pay_cents,
          SUM(r.total_vacation_pay_cents) AS vacation_pay_cents,
          SUM(r.total_tips_cents) AS tips_cents,
          SUM(r.total_federal_tax_cents) AS federal_tax_cents,
          SUM(r.total_provincial_tax_cents) AS provincial_tax_cents,
          SUM(r.total_cpp_cents) AS employee_cpp_cents,
          SUM(r.total_cpp2_cents) AS employee_cpp2_cents,
          SUM(r.total_ei_cents) AS employee_ei_cents,
          SUM(r.total_employer_cpp_cents) AS employer_cpp_cents,
          SUM(r.total_employer_cpp2_cents) AS employer_cpp2_cents,
          SUM(r.total_employer_ei_cents) AS employer_ei_cents,
          SUM(r.total_deductions_cents) AS total_deductions_cents,
          SUM(r.total_net_cents) AS net_pay_cents,
          SUM(r.total_employer_cost_cents) AS total_employer_cost_cents
        FROM curlysbooks_payroll_runs r
        JOIN curlysbooks_pay_periods pp ON pp.pay_period_id = r.pay_period_id
        WHERE pp.entity = ?
          AND pp.tax_year = ?
          AND r.calculated_by = ?
          AND pp.end_date >= ? AND pp.end_date <= ?
        """,
        (entity, tax_year, calculated_by, start_date, end_date),
    ).fetchone()

    return PayrollComponentTotals(
        fy=fy.fy,
        source="curlysbooks_backfill",
        start_date=start_date,
        end_date=end_date,
        periods=int(row["periods"] or 0),
        min_period_end=(str(row["min_period_end"]) if row["min_period_end"] else None),
        max_period_end=(str(row["max_period_end"]) if row["max_period_end"] else None),
        gross_pay_cents=int(row["gross_pay_cents"] or 0),
        vacation_pay_cents=int(row["vacation_pay_cents"] or 0),
        tips_cents=int(row["tips_cents"] or 0),
        federal_tax_cents=int(row["federal_tax_cents"] or 0),
        provincial_tax_cents=int(row["provincial_tax_cents"] or 0),
        employee_cpp_cents=int(row["employee_cpp_cents"] or 0),
        employee_cpp2_cents=int(row["employee_cpp2_cents"] or 0),
        employee_ei_cents=int(row["employee_ei_cents"] or 0),
        employer_cpp_cents=int(row["employer_cpp_cents"] or 0),
        employer_cpp2_cents=int(row["employer_cpp2_cents"] or 0),
        employer_ei_cents=int(row["employer_ei_cents"] or 0),
        net_pay_cents=int(row["net_pay_cents"] or 0),
        reported_total_deductions_cents=int(row["total_deductions_cents"] or 0),
        reported_total_employer_cost_cents=int(row["total_employer_cost_cents"] or 0),
    )


def sum_rows(fy: FiscalYear, rows: list[PayrollComponentTotals]) -> PayrollComponentTotals:
    if not rows:
        raise ValueError("No rows to sum")

    return PayrollComponentTotals(
        fy=fy.fy,
        source="combined",
        start_date=fy.start_date,
        end_date=fy.end_date,
        periods=sum(r.periods for r in rows),
        min_period_end=min([d for d in (r.min_period_end for r in rows) if d], default=None),
        max_period_end=max([d for d in (r.max_period_end for r in rows) if d], default=None),
        gross_pay_cents=sum(r.gross_pay_cents for r in rows),
        vacation_pay_cents=sum(r.vacation_pay_cents for r in rows),
        tips_cents=sum(r.tips_cents for r in rows),
        federal_tax_cents=sum(r.federal_tax_cents for r in rows),
        provincial_tax_cents=sum(r.provincial_tax_cents for r in rows),
        employee_cpp_cents=sum(r.employee_cpp_cents for r in rows),
        employee_cpp2_cents=sum(r.employee_cpp2_cents for r in rows),
        employee_ei_cents=sum(r.employee_ei_cents for r in rows),
        employer_cpp_cents=sum(r.employer_cpp_cents for r in rows),
        employer_cpp2_cents=sum(r.employer_cpp2_cents for r in rows),
        employer_ei_cents=sum(r.employer_ei_cents for r in rows),
        net_pay_cents=sum(r.net_pay_cents for r in rows),
        reported_total_deductions_cents=None,
        reported_total_employer_cost_cents=None,
    )


def write_csv(out_csv: Path, rows: list[PayrollComponentTotals]) -> None:
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "fy",
                "source",
                "start_date",
                "end_date",
                "periods",
                "min_period_end",
                "max_period_end",
                "gross_pay_cents",
                "vacation_pay_cents",
                "tips_cents",
                "net_pay_cents",
                "net_pay_plus_tips_cents",
                "federal_tax_cents",
                "provincial_tax_cents",
                "employee_cpp_cents",
                "employee_cpp2_cents",
                "employee_ei_cents",
                "employer_cpp_cents",
                "employer_cpp2_cents",
                "employer_ei_cents",
                "employee_deductions_cents",
                "employer_taxes_cents",
                "remittance_cents",
                "reported_total_deductions_cents",
                "reported_total_employer_cost_cents",
            ]
        )
        for r in rows:
            w.writerow(
                [
                    r.fy,
                    r.source,
                    r.start_date,
                    r.end_date,
                    r.periods,
                    r.min_period_end or "",
                    r.max_period_end or "",
                    r.gross_pay_cents,
                    r.vacation_pay_cents,
                    r.tips_cents,
                    r.net_pay_cents,
                    r.net_pay_plus_tips_cents,
                    r.federal_tax_cents,
                    r.provincial_tax_cents,
                    r.employee_cpp_cents,
                    r.employee_cpp2_cents,
                    r.employee_ei_cents,
                    r.employer_cpp_cents,
                    r.employer_cpp2_cents,
                    r.employer_ei_cents,
                    r.employee_deductions_cents,
                    r.employer_taxes_cents,
                    r.remittance_cents,
                    (r.reported_total_deductions_cents if r.reported_total_deductions_cents is not None else ""),
                    (r.reported_total_employer_cost_cents if r.reported_total_employer_cost_cents is not None else ""),
                ]
            )


def write_md(out_md: Path, rows: list[PayrollComponentTotals]) -> None:
    by_fy: dict[str, list[PayrollComponentTotals]] = {}
    for r in rows:
        by_fy.setdefault(r.fy, []).append(r)

    lines: list[str] = []
    lines.append("# Payroll component totals (CPP/EI/tax splits)")
    lines.append("")
    lines.append("This report is intended to support payroll journal entries (wages, employer taxes, and payroll liabilities).")
    lines.append("")

    for fy, fy_rows in sorted(by_fy.items()):
        combined = next((r for r in fy_rows if r.source == "combined"), None)
        lines.append(f"## {fy}")
        lines.append("")
        if combined:
            lines.append(f"- Gross pay: ${cents_to_dollars(combined.gross_pay_cents)}")
            lines.append(f"- Tips: ${cents_to_dollars(combined.tips_cents)}")
            lines.append(f"- Employer taxes (CPP/EI/CPP2): ${cents_to_dollars(combined.employer_taxes_cents)}")
            lines.append(f"- Employee deductions (CPP/EI/CPP2 + tax): ${cents_to_dollars(combined.employee_deductions_cents)}")
            lines.append(f"- Remittance total (employee + employer): ${cents_to_dollars(combined.remittance_cents)}")
            lines.append(f"- Net pay + tips: ${cents_to_dollars(combined.net_pay_plus_tips_cents)}")
        lines.append("")
        lines.append("| source | periods | period_end_range | gross | tips | employer_taxes | employee_deductions | remittance | net+tips |")
        lines.append("|---|---:|---|---:|---:|---:|---:|---:|---:|")
        for r in sorted([x for x in fy_rows if x.source != "combined"], key=lambda x: x.source):
            rng = ""
            if r.min_period_end or r.max_period_end:
                rng = f"{r.min_period_end or ''} → {r.max_period_end or ''}".strip()
            lines.append(
                f"| {r.source} | {r.periods} | {rng} | ${cents_to_dollars(r.gross_pay_cents)} | ${cents_to_dollars(r.tips_cents)} | ${cents_to_dollars(r.employer_taxes_cents)} | ${cents_to_dollars(r.employee_deductions_cents)} | ${cents_to_dollars(r.remittance_cents)} | ${cents_to_dollars(r.net_pay_plus_tips_cents)} |"
            )
        lines.append("")

    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--entity", default="corp")
    ap.add_argument("--tax-year", type=int, default=2025)
    ap.add_argument("--calculated-by", default="backfill_csv_2025_corp")
    ap.add_argument(
        "--curlysbooks-start-date",
        default="2025-01-01",
        help="Date (inclusive) from which curlys-books backfill should be treated as canonical",
    )
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = args.out_dir / "payroll_component_totals_by_fy.csv"
    out_md = args.out_dir / "payroll_component_totals_by_fy.md"

    boundary_date = date.fromisoformat(str(args.curlysbooks_start_date).strip() or "2025-01-01")

    conn = connect_db(args.db)
    try:
        all_rows: list[PayrollComponentTotals] = []
        for fy in fys:
            fy_start = date.fromisoformat(fy.start_date)
            fy_end = date.fromisoformat(fy.end_date)

            parts: list[PayrollComponentTotals] = []

            emp_end = min(fy_end, boundary_date - timedelta(days=1))
            if fy_start <= emp_end:
                emp = fetch_employee_export_totals(
                    conn,
                    fy=fy,
                    start_date=fy_start.isoformat(),
                    end_date=emp_end.isoformat(),
                )
                parts.append(emp)
                all_rows.append(emp)

            cb_start = max(fy_start, boundary_date)
            if cb_start <= fy_end:
                cb = fetch_curlysbooks_backfill_totals(
                    conn,
                    fy=fy,
                    start_date=cb_start.isoformat(),
                    end_date=fy_end.isoformat(),
                    entity=str(args.entity),
                    tax_year=int(args.tax_year),
                    calculated_by=str(args.calculated_by),
                )
                parts.append(cb)
                all_rows.append(cb)

            if parts:
                all_rows.append(sum_rows(fy, parts))

        write_csv(out_csv, all_rows)
        write_md(out_md, all_rows)
    finally:
        conn.close()

    print("PAYROLL COMPONENT TOTALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out_csv: {out_csv}")
    print(f"- out_md: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

