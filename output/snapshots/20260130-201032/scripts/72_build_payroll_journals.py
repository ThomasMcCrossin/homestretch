#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"
NET_TIPS_INCLUSION_TOLERANCE_CENTS = 2


@dataclass(frozen=True)
class PayrollTotals:
    gross_pay_cents: int
    vacation_pay_cents: int
    tips_cents: int  # total tips in source data (informational)
    tips_payable_cents: int  # tips not already included in net pay
    net_pay_cents: int
    federal_tax_cents: int
    provincial_tax_cents: int
    employee_cpp_cents: int
    employee_cpp2_cents: int
    employee_ei_cents: int
    employer_cpp_cents: int
    employer_cpp2_cents: int
    employer_ei_cents: int

    @property
    def employer_taxes_cents(self) -> int:
        return self.employer_cpp_cents + self.employer_cpp2_cents + self.employer_ei_cents

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
    def gross_plus_vacation_cents(self) -> int:
        return self.gross_pay_cents + self.vacation_pay_cents


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def sum_payroll_exports(conn, *, start_date: str, end_date: str) -> PayrollTotals:
    rows = conn.execute(
        """
        SELECT
          gross_pay_cents,
          vacation_pay_cents,
          tips_cents,
          net_pay_cents,
          federal_tax_cents,
          provincial_tax_cents,
          employee_cpp_cents,
          employee_ei_cents,
          employer_cpp_cents,
          employer_ei_cents
        FROM payroll_employee_pay_periods
        WHERE pay_period_end >= ? AND pay_period_end <= ?
        """,
        (start_date, end_date),
    ).fetchall()

    gross_pay_cents = 0
    vacation_pay_cents = 0
    tips_cents = 0
    tips_payable_cents = 0
    net_pay_cents = 0
    federal_tax_cents = 0
    provincial_tax_cents = 0
    employee_cpp_cents = 0
    employee_ei_cents = 0
    employer_cpp_cents = 0
    employer_ei_cents = 0

    for r in rows:
        gross = int(r["gross_pay_cents"] or 0)
        vacation = int(r["vacation_pay_cents"] or 0)
        tips = int(r["tips_cents"] or 0)
        net = int(r["net_pay_cents"] or 0)
        fed = int(r["federal_tax_cents"] or 0)
        prov = int(r["provincial_tax_cents"] or 0)
        emp_cpp = int(r["employee_cpp_cents"] or 0)
        emp_ei = int(r["employee_ei_cents"] or 0)
        empl_cpp = int(r["employer_cpp_cents"] or 0)
        empl_ei = int(r["employer_ei_cents"] or 0)

        gross_pay_cents += gross
        vacation_pay_cents += vacation
        tips_cents += tips
        net_pay_cents += net
        federal_tax_cents += fed
        provincial_tax_cents += prov
        employee_cpp_cents += emp_cpp
        employee_ei_cents += emp_ei
        employer_cpp_cents += empl_cpp
        employer_ei_cents += empl_ei

        if not tips:
            continue

        deductions = fed + prov + emp_cpp + emp_ei
        net_if_gross_excludes_tips = gross + vacation - deductions
        net_if_gross_excludes_tips_and_tips_added = gross + vacation + tips - deductions

        if abs(net - net_if_gross_excludes_tips_and_tips_added) <= NET_TIPS_INCLUSION_TOLERANCE_CENTS:
            # Tips are explicitly added into the net pay amount (and will be cleared by payroll e-transfers).
            continue

        if abs(net - net_if_gross_excludes_tips) <= NET_TIPS_INCLUSION_TOLERANCE_CENTS:
            # Some exports report `tips_cents` as an informational split but still include tips in `gross_pay_cents`.
            # In that case, net pay already includes tips via the gross calculation, and there is no separate tips payable.
            continue

        # Ambiguous export row; assume tips are included in net pay (no separate payable) to avoid creating
        # an unsupported cash-payout assumption.
        continue

    return PayrollTotals(
        gross_pay_cents=gross_pay_cents,
        vacation_pay_cents=vacation_pay_cents,
        tips_cents=tips_cents,
        tips_payable_cents=tips_payable_cents,
        net_pay_cents=net_pay_cents,
        federal_tax_cents=federal_tax_cents,
        provincial_tax_cents=provincial_tax_cents,
        employee_cpp_cents=employee_cpp_cents,
        employee_cpp2_cents=0,
        employee_ei_cents=employee_ei_cents,
        employer_cpp_cents=employer_cpp_cents,
        employer_cpp2_cents=0,
        employer_ei_cents=employer_ei_cents,
    )


def sum_curlysbooks_backfill(
    conn,
    *,
    start_date: str,
    end_date: str,
    entity: str,
    tax_year: int,
    calculated_by: str,
) -> PayrollTotals:
    row = conn.execute(
        """
        SELECT
          SUM(r.total_gross_cents) AS gross_pay_cents,
          SUM(r.total_vacation_pay_cents) AS vacation_pay_cents,
          SUM(r.total_tips_cents) AS tips_cents,
          SUM(r.total_net_cents) AS net_pay_cents,
          SUM(r.total_federal_tax_cents) AS federal_tax_cents,
          SUM(r.total_provincial_tax_cents) AS provincial_tax_cents,
          SUM(r.total_cpp_cents) AS employee_cpp_cents,
          SUM(r.total_cpp2_cents) AS employee_cpp2_cents,
          SUM(r.total_ei_cents) AS employee_ei_cents,
          SUM(r.total_employer_cpp_cents) AS employer_cpp_cents,
          SUM(r.total_employer_cpp2_cents) AS employer_cpp2_cents,
          SUM(r.total_employer_ei_cents) AS employer_ei_cents
        FROM curlysbooks_payroll_runs r
        JOIN curlysbooks_pay_periods p ON p.pay_period_id = r.pay_period_id
        WHERE p.entity = ?
          AND p.tax_year = ?
          AND r.calculated_by = ?
          AND p.end_date >= ? AND p.end_date <= ?
        """,
        (entity, tax_year, calculated_by, start_date, end_date),
    ).fetchone()

    gross_pay_cents = int(row["gross_pay_cents"] or 0)
    vacation_pay_cents = int(row["vacation_pay_cents"] or 0)
    tips_cents = int(row["tips_cents"] or 0)
    net_pay_cents = int(row["net_pay_cents"] or 0)
    federal_tax_cents = int(row["federal_tax_cents"] or 0)
    provincial_tax_cents = int(row["provincial_tax_cents"] or 0)
    employee_cpp_cents = int(row["employee_cpp_cents"] or 0)
    employee_cpp2_cents = int(row["employee_cpp2_cents"] or 0)
    employee_ei_cents = int(row["employee_ei_cents"] or 0)
    employer_cpp_cents = int(row["employer_cpp_cents"] or 0)
    employer_cpp2_cents = int(row["employer_cpp2_cents"] or 0)
    employer_ei_cents = int(row["employer_ei_cents"] or 0)

    employee_deductions_cents = federal_tax_cents + provincial_tax_cents + employee_cpp_cents + employee_cpp2_cents + employee_ei_cents
    net_excl_tips = (gross_pay_cents + vacation_pay_cents) - employee_deductions_cents
    # curlys-books backfill (2025 corp):
    # - `total_net` is net pay *excluding tips* (deductions are computed on gross+vacation only)
    # - `total_tips` is paid on top (no deductions) and is visible in bank e-transfers.
    #
    # So for T2 accrual purposes, treat tips as part of the net amount payable to employees (cleared by payroll e-transfers),
    # not as a separate "tips payable" liability that would require an additional payout journal.
    if abs(net_pay_cents - net_excl_tips) <= NET_TIPS_INCLUSION_TOLERANCE_CENTS:
        net_pay_cents += tips_cents
        tips_payable_cents = 0
    elif abs(net_pay_cents - (net_excl_tips + tips_cents)) <= NET_TIPS_INCLUSION_TOLERANCE_CENTS:
        tips_payable_cents = 0
    else:
        net_pay_cents += tips_cents
        tips_payable_cents = 0

    return PayrollTotals(
        gross_pay_cents=gross_pay_cents,
        vacation_pay_cents=vacation_pay_cents,
        tips_cents=tips_cents,
        tips_payable_cents=tips_payable_cents,
        net_pay_cents=net_pay_cents,
        federal_tax_cents=federal_tax_cents,
        provincial_tax_cents=provincial_tax_cents,
        employee_cpp_cents=employee_cpp_cents,
        employee_cpp2_cents=employee_cpp2_cents,
        employee_ei_cents=employee_ei_cents,
        employer_cpp_cents=employer_cpp_cents,
        employer_cpp2_cents=employer_cpp2_cents,
        employer_ei_cents=employer_ei_cents,
    )


def add_totals(a: PayrollTotals, b: PayrollTotals) -> PayrollTotals:
    return PayrollTotals(
        gross_pay_cents=a.gross_pay_cents + b.gross_pay_cents,
        vacation_pay_cents=a.vacation_pay_cents + b.vacation_pay_cents,
        tips_cents=a.tips_cents + b.tips_cents,
        tips_payable_cents=a.tips_payable_cents + b.tips_payable_cents,
        net_pay_cents=a.net_pay_cents + b.net_pay_cents,
        federal_tax_cents=a.federal_tax_cents + b.federal_tax_cents,
        provincial_tax_cents=a.provincial_tax_cents + b.provincial_tax_cents,
        employee_cpp_cents=a.employee_cpp_cents + b.employee_cpp_cents,
        employee_cpp2_cents=a.employee_cpp2_cents + b.employee_cpp2_cents,
        employee_ei_cents=a.employee_ei_cents + b.employee_ei_cents,
        employer_cpp_cents=a.employer_cpp_cents + b.employer_cpp_cents,
        employer_cpp2_cents=a.employer_cpp2_cents + b.employer_cpp2_cents,
        employer_ei_cents=a.employer_ei_cents + b.employer_ei_cents,
    )


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing payroll summary journal entries before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    payroll_cfg = cfg.get("payroll", {}) if isinstance(cfg.get("payroll"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("payroll_summary") if isinstance(cfg.get("journal_sources"), dict) else {}

    wages_expense_code = str(payroll_cfg.get("wages_expense_code") or "7000").strip()
    employer_taxes_expense_code = str(payroll_cfg.get("employer_taxes_expense_code") or "7100").strip()
    liability_cpp_code = str(payroll_cfg.get("payroll_liability_cpp_code") or "2700").strip()
    liability_ei_code = str(payroll_cfg.get("payroll_liability_ei_code") or "2710").strip()
    liability_tax_code = str(payroll_cfg.get("payroll_liability_tax_code") or "2720").strip()
    tips_payable_code = str(payroll_cfg.get("tips_payable_code") or "2310").strip()
    wages_payable_code = str(payroll_cfg.get("wages_payable_code") or "2000").strip()

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "payroll_summary")
    entry_type = str((source_cfg or {}).get("entry_type") or "ACCRUAL")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "payroll_journal_summary.md"
    out_detail_csv = args.out_dir / "payroll_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                """
                DELETE FROM journal_entries
                WHERE source_system = ? AND source_record_type = ?
                """,
                (source_system, source_record_type),
            )

        detail_rows: list[dict[str, str]] = []

        for fy in fys:
            exports = sum_payroll_exports(conn, start_date=fy.start_date, end_date=fy.end_date)
            backfill = sum_curlysbooks_backfill(
                conn,
                start_date=fy.start_date,
                end_date=fy.end_date,
                entity="corp",
                tax_year=2025,
                calculated_by="backfill_csv_2025_corp",
            )
            totals = add_totals(exports, backfill)

            if totals.gross_pay_cents == 0 and totals.employer_taxes_cents == 0:
                continue

            je_id = f"PAYROLL_SUMMARY_{fy.fy}"
            description = f"Payroll summary accrual {fy.fy}"
            wages_base_cents = totals.gross_plus_vacation_cents + totals.tips_cents
            implied_wages_cents = totals.net_pay_cents + totals.employee_deductions_cents + totals.tips_payable_cents
            variance_cents = implied_wages_cents - wages_base_cents
            notes = (
                f"gross={totals.gross_pay_cents}; vacation={totals.vacation_pay_cents}; tips={totals.tips_cents}; "
                f"tips_payable={totals.tips_payable_cents}; "
                f"net={totals.net_pay_cents}; employee_deductions={totals.employee_deductions_cents}; "
                f"employer_taxes={totals.employer_taxes_cents}; variance={variance_cents}"
            )

            conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
            conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

            conn.execute(
                """
                INSERT INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id, notes, is_posted
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
            credit_total = 0

            wages_debit = wages_base_cents + variance_cents
            if wages_debit:
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
                        wages_expense_code,
                        wages_debit,
                        0,
                        "Wages, vacation, tips (gross)",
                    ),
                )
                debit_total += wages_debit
                line_number += 1

            employer_taxes = totals.employer_taxes_cents
            if employer_taxes:
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
                        employer_taxes_expense_code,
                        employer_taxes,
                        0,
                        "Employer payroll taxes (CPP/EI/CPP2)",
                    ),
                )
                debit_total += employer_taxes
                line_number += 1

            cpp_liab = totals.employee_cpp_cents + totals.employee_cpp2_cents + totals.employer_cpp_cents + totals.employer_cpp2_cents
            if cpp_liab:
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
                        liability_cpp_code,
                        0,
                        cpp_liab,
                        "Payroll liabilities - CPP/CPP2 (employee + employer)",
                    ),
                )
                credit_total += cpp_liab
                line_number += 1

            ei_liab = totals.employee_ei_cents + totals.employer_ei_cents
            if ei_liab:
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
                        liability_ei_code,
                        0,
                        ei_liab,
                        "Payroll liabilities - EI (employee + employer)",
                    ),
                )
                credit_total += ei_liab
                line_number += 1

            tax_liab = totals.federal_tax_cents + totals.provincial_tax_cents
            if tax_liab:
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
                        liability_tax_code,
                        0,
                        tax_liab,
                        "Payroll liabilities - income tax (federal + provincial)",
                    ),
                )
                credit_total += tax_liab
                line_number += 1

            if totals.tips_payable_cents:
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
                        tips_payable_code,
                        0,
                        totals.tips_payable_cents,
                        "Tips payable",
                    ),
                )
                credit_total += totals.tips_payable_cents
                line_number += 1

            if totals.net_pay_cents:
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
                        wages_payable_code,
                        0,
                        totals.net_pay_cents,
                        "Net pay payable",
                    ),
                )
                credit_total += totals.net_pay_cents
                line_number += 1

            if debit_total != credit_total:
                conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
                conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))
                raise SystemExit(
                    f"Unbalanced payroll journal for {fy.fy}: debits={debit_total} credits={credit_total}"
                )

            detail_rows.append(
                {
                    "fy": fy.fy,
                    "journal_entry_id": je_id,
                    "gross_pay_cents": str(totals.gross_pay_cents),
                    "vacation_pay_cents": str(totals.vacation_pay_cents),
                    "tips_cents": str(totals.tips_cents),
                    "net_pay_cents": str(totals.net_pay_cents),
                    "employee_deductions_cents": str(totals.employee_deductions_cents),
                    "employer_taxes_cents": str(totals.employer_taxes_cents),
                    "variance_cents": str(variance_cents),
                    "cpp_liability_cents": str(cpp_liab),
                    "ei_liability_cents": str(ei_liab),
                    "income_tax_liability_cents": str(tax_liab),
                    "tips_payable_cents": str(totals.tips_payable_cents),
                    "net_payable_cents": str(totals.net_pay_cents),
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "fy",
                "journal_entry_id",
                "gross_pay_cents",
                "vacation_pay_cents",
                "tips_cents",
                "net_pay_cents",
                "employee_deductions_cents",
                "employer_taxes_cents",
                "variance_cents",
                "cpp_liability_cents",
                "ei_liability_cents",
                "income_tax_liability_cents",
                "tips_payable_cents",
                "net_payable_cents",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Payroll journal summary\n\n")
            f.write("This journal posts payroll expenses and liabilities from payroll exports.\n")
            f.write("It does not clear liabilities with bank remittance payments yet.\n\n")
            for row in detail_rows:
                f.write(f"## {row['fy']}\n\n")
                f.write(f"- Journal entry: `{row['journal_entry_id']}`\n")
                f.write(f"- Gross pay: ${cents_to_dollars(int(row['gross_pay_cents']))}\n")
                f.write(f"- Vacation pay: ${cents_to_dollars(int(row['vacation_pay_cents']))}\n")
                f.write(f"- Tips: ${cents_to_dollars(int(row['tips_cents']))}\n")
                f.write(f"- Tips payable: ${cents_to_dollars(int(row['tips_payable_cents']))}\n")
                f.write(f"- Employer taxes: ${cents_to_dollars(int(row['employer_taxes_cents']))}\n")
                f.write(f"- Employee deductions: ${cents_to_dollars(int(row['employee_deductions_cents']))}\n")
                f.write(f"- Variance adjustment: ${cents_to_dollars(int(row['variance_cents']))}\n")
                f.write(f"- Net payable: ${cents_to_dollars(int(row['net_payable_cents']))}\n")
                f.write("\n")

        conn.commit()

    finally:
        conn.close()

    print("PAYROLL JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
