#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db


NET_TIPS_INCLUSION_TOLERANCE_CENTS = 2
BANK_MATCH_TOLERANCE_CENTS = 5


@dataclass(frozen=True)
class TipRowAudit:
    employee_name: str
    pay_period_end: str
    tips_cents: int
    net_pay_cents: int
    net_tip_relationship: str  # TIPS_ADDED_PRE_DEDUCTIONS | TIPS_EMBEDDED_IN_GROSS | AMBIG
    bank_net_match_txn_id: str
    bank_net_match_date: str
    bank_net_match_amount_cents: str
    bank_net_plus_tips_match_txn_id: str
    bank_net_plus_tips_match_date: str
    bank_net_plus_tips_match_amount_cents: str
    bank_tips_match_txn_id: str
    bank_tips_match_date: str
    bank_tips_match_amount_cents: str


@dataclass(frozen=True)
class CurlysbooksPayPeriodAudit:
    period_number: int
    end_date: str
    pay_date: str
    payroll_net_cents: int
    payroll_tips_cents: int
    payroll_net_plus_tips_cents: int
    bank_employee_payroll_cents: int
    bank_shareholder_payroll_cents: int
    bank_total_payroll_cents: int
    diff_cents: int


def cents_to_dollars(cents: int) -> str:
    return f"{Decimal(cents) / Decimal(100):.2f}"


def classify_net_tip_relationship(
    *,
    gross_pay_cents: int,
    vacation_pay_cents: int,
    tips_cents: int,
    net_pay_cents: int,
    federal_tax_cents: int,
    provincial_tax_cents: int,
    employee_cpp_cents: int,
    employee_ei_cents: int,
) -> str:
    deductions = federal_tax_cents + provincial_tax_cents + employee_cpp_cents + employee_ei_cents
    net_if_gross_excludes_tips_and_tips_added = gross_pay_cents + vacation_pay_cents + tips_cents - deductions
    if abs(net_pay_cents - net_if_gross_excludes_tips_and_tips_added) <= NET_TIPS_INCLUSION_TOLERANCE_CENTS:
        # Tips were added to taxable pay (i.e., tips are part of gross+vacation+tips and deductions were taken).
        return "TIPS_ADDED_PRE_DEDUCTIONS"

    net_if_gross_includes_tips = gross_pay_cents + vacation_pay_cents - deductions
    if abs(net_pay_cents - net_if_gross_includes_tips) <= NET_TIPS_INCLUSION_TOLERANCE_CENTS:
        # Tips are already embedded in the gross figure (tips column is informational), so net already includes tips.
        return "TIPS_EMBEDDED_IN_GROSS"

    return "AMBIG"


def find_bank_etransfer_match(
    conn: sqlite3.Connection,
    *,
    name_hint: str,
    target_cents: int,
    center_date: date,
    window_days: int,
) -> tuple[str, str, str]:
    """
    Find the closest-matching E_TRANSFER bank debit line near center_date.
    Returns (bank_txn_id, txn_date, debit_cents) or ("", "", "").
    """
    start = (center_date - timedelta(days=window_days)).isoformat()
    end = (center_date + timedelta(days=window_days)).isoformat()
    first = (name_hint or "").split()[0].strip()
    if not first:
        first = name_hint.strip()

    rows = conn.execute(
        """
        SELECT id, txn_date, description, CAST(debit_cents AS INTEGER) AS debit_cents
        FROM fresher_debits__bank_transactions
        WHERE txn_date BETWEEN ? AND ?
          AND txn_type = 'E_TRANSFER'
          AND debit_cents != ''
          AND description LIKE ?
          AND ABS(CAST(debit_cents AS INTEGER) - ?) <= ?
        ORDER BY ABS(CAST(debit_cents AS INTEGER) - ?) ASC, txn_date ASC
        LIMIT 1
        """,
        (start, end, f"%{first}%", target_cents, BANK_MATCH_TOLERANCE_CENTS, target_cents),
    ).fetchone()
    if not rows:
        return "", "", ""
    return str(rows["id"]), str(rows["txn_date"]), str(int(rows["debit_cents"] or 0))


def sum_bank_payroll_in_window(
    conn: sqlite3.Connection,
    *,
    center_date: date,
    window_days: int,
) -> tuple[int, int]:
    """
    Sum bank E_TRANSFER debits classified as EMPLOYEE_PAYROLL / SHAREHOLDER_PAYROLL in a date window.
    Returns (employee_payroll_cents, shareholder_payroll_cents).
    """
    start = (center_date - timedelta(days=window_days)).isoformat()
    end = (center_date + timedelta(days=window_days)).isoformat()
    row = conn.execute(
        """
        WITH ranked AS (
          SELECT
            bank_txn_id,
            txn_category,
            ROW_NUMBER() OVER (
              PARTITION BY bank_txn_id
              ORDER BY CAST(verified AS INTEGER) DESC, CAST(id AS INTEGER) ASC
            ) AS rn
          FROM fresher_debits__bank_txn_classifications
        )
        SELECT
          COALESCE(SUM(CASE WHEN c.txn_category = 'EMPLOYEE_PAYROLL' THEN CAST(t.debit_cents AS INTEGER) ELSE 0 END), 0) AS employee_cents,
          COALESCE(SUM(CASE WHEN c.txn_category = 'SHAREHOLDER_PAYROLL' THEN CAST(t.debit_cents AS INTEGER) ELSE 0 END), 0) AS shareholder_cents
        FROM fresher_debits__bank_transactions t
        JOIN ranked c ON c.bank_txn_id = t.id AND c.rn = 1
        WHERE t.txn_date BETWEEN ? AND ?
          AND t.txn_type = 'E_TRANSFER'
          AND t.debit_cents != ''
          AND CAST(t.debit_cents AS INTEGER) > 0
          AND c.txn_category IN ('EMPLOYEE_PAYROLL', 'SHAREHOLDER_PAYROLL')
        """,
        (start, end),
    ).fetchone()
    return int(row["employee_cents"] or 0), int(row["shareholder_cents"] or 0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--start", default="2023-06-01")
    ap.add_argument("--end", default="2025-05-31")
    ap.add_argument("--window-days", type=int, default=3)
    args = ap.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = args.out_dir / "tips_vs_bank_audit.csv"
    out_md = args.out_dir / "tips_vs_bank_audit.md"
    out_cb_csv = args.out_dir / "tips_vs_bank_audit_curlysbooks.csv"

    conn = connect_db(args.db)
    try:
        rows = conn.execute(
            """
            SELECT
              employee_name,
              pay_period_end,
              gross_pay_cents,
              vacation_pay_cents,
              tips_cents,
              net_pay_cents,
              federal_tax_cents,
              provincial_tax_cents,
              employee_cpp_cents,
              employee_ei_cents
            FROM payroll_employee_pay_periods
            WHERE tips_cents > 0
              AND pay_period_end BETWEEN ? AND ?
            ORDER BY pay_period_end, employee_name
            """,
            (args.start, args.end),
        ).fetchall()

        audits: list[TipRowAudit] = []

        for r in rows:
            employee = str(r["employee_name"] or "").strip()
            pay_end = str(r["pay_period_end"])
            pay_end_d = date.fromisoformat(pay_end)
            tips = int(r["tips_cents"] or 0)
            net = int(r["net_pay_cents"] or 0)
            rel = classify_net_tip_relationship(
                gross_pay_cents=int(r["gross_pay_cents"] or 0),
                vacation_pay_cents=int(r["vacation_pay_cents"] or 0),
                tips_cents=tips,
                net_pay_cents=net,
                federal_tax_cents=int(r["federal_tax_cents"] or 0),
                provincial_tax_cents=int(r["provincial_tax_cents"] or 0),
                employee_cpp_cents=int(r["employee_cpp_cents"] or 0),
                employee_ei_cents=int(r["employee_ei_cents"] or 0),
            )

            bank_net_id, bank_net_date, bank_net_amt = find_bank_etransfer_match(
                conn,
                name_hint=employee,
                target_cents=net,
                center_date=pay_end_d,
                window_days=args.window_days,
            )
            bank_net_plus_id, bank_net_plus_date, bank_net_plus_amt = find_bank_etransfer_match(
                conn,
                name_hint=employee,
                target_cents=net + tips,
                center_date=pay_end_d,
                window_days=args.window_days,
            )
            bank_tip_id, bank_tip_date, bank_tip_amt = find_bank_etransfer_match(
                conn,
                name_hint=employee,
                target_cents=tips,
                center_date=pay_end_d,
                window_days=args.window_days,
            )

            audits.append(
                TipRowAudit(
                    employee_name=employee,
                    pay_period_end=pay_end,
                    tips_cents=tips,
                    net_pay_cents=net,
                    net_tip_relationship=rel,
                    bank_net_match_txn_id=bank_net_id,
                    bank_net_match_date=bank_net_date,
                    bank_net_match_amount_cents=bank_net_amt,
                    bank_net_plus_tips_match_txn_id=bank_net_plus_id,
                    bank_net_plus_tips_match_date=bank_net_plus_date,
                    bank_net_plus_tips_match_amount_cents=bank_net_plus_amt,
                    bank_tips_match_txn_id=bank_tip_id,
                    bank_tips_match_date=bank_tip_date,
                    bank_tips_match_amount_cents=bank_tip_amt,
                )
            )

        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "employee_name",
                    "pay_period_end",
                    "tips_cents",
                    "tips_amount",
                    "net_pay_cents",
                    "net_pay_amount",
                    "net_tip_relationship",
                    "bank_net_match_txn_id",
                    "bank_net_match_date",
                    "bank_net_match_amount_cents",
                    "bank_net_plus_tips_match_txn_id",
                    "bank_net_plus_tips_match_date",
                    "bank_net_plus_tips_match_amount_cents",
                    "bank_tips_match_txn_id",
                    "bank_tips_match_date",
                    "bank_tips_match_amount_cents",
                ]
            )
            for a in audits:
                w.writerow(
                    [
                        a.employee_name,
                        a.pay_period_end,
                        a.tips_cents,
                        cents_to_dollars(a.tips_cents),
                        a.net_pay_cents,
                        cents_to_dollars(a.net_pay_cents),
                        a.net_tip_relationship,
                        a.bank_net_match_txn_id,
                        a.bank_net_match_date,
                        a.bank_net_match_amount_cents,
                        a.bank_net_plus_tips_match_txn_id,
                        a.bank_net_plus_tips_match_date,
                        a.bank_net_plus_tips_match_amount_cents,
                        a.bank_tips_match_txn_id,
                        a.bank_tips_match_date,
                        a.bank_tips_match_amount_cents,
                    ]
                )

        total = len(audits)
        # For employee-export tip rows (FY2024-style tips in these CSVs), tips are already included
        # in the net pay figure (either because tips were added pre-deductions, or because they're
        # embedded in gross). So the expected bank e-transfer amount is net pay, not net+tips.
        expected_net_matched = sum(1 for a in audits if a.bank_net_match_txn_id)
        net_plus_matched = sum(1 for a in audits if a.bank_net_plus_tips_match_txn_id)
        tips_matched = sum(1 for a in audits if a.bank_tips_match_txn_id)
        tips_total_cents = sum(a.tips_cents for a in audits)
        tips_added_pre_deductions = sum(a.tips_cents for a in audits if a.net_tip_relationship == "TIPS_ADDED_PRE_DEDUCTIONS")
        tips_embedded_in_gross = sum(a.tips_cents for a in audits if a.net_tip_relationship == "TIPS_EMBEDDED_IN_GROSS")
        amb_tips = sum(a.tips_cents for a in audits if a.net_tip_relationship == "AMBIG")

        cb_rows = conn.execute(
            """
            SELECT
              p.period_number,
              p.end_date,
              p.pay_date,
              COALESCE(SUM(r.total_net_cents), 0) AS net_cents,
              COALESCE(SUM(r.total_tips_cents), 0) AS tips_cents
            FROM curlysbooks_pay_periods p
            LEFT JOIN curlysbooks_payroll_runs r
              ON r.pay_period_id = p.pay_period_id
             AND r.calculated_by = 'backfill_csv_2025_corp'
            WHERE p.entity = 'corp'
              AND p.tax_year = 2025
              AND p.end_date BETWEEN ? AND ?
            GROUP BY p.pay_period_id
            ORDER BY p.period_number
            """,
            (args.start, args.end),
        ).fetchall()

        cb_audits: list[CurlysbooksPayPeriodAudit] = []
        for r in cb_rows:
            tips = int(r["tips_cents"] or 0)
            if tips <= 0:
                continue
            pay_date = str(r["pay_date"] or "").strip()
            if not pay_date:
                continue
            pay_date_d = date.fromisoformat(pay_date)
            net = int(r["net_cents"] or 0)
            payroll_total = net + tips
            bank_emp, bank_sh = sum_bank_payroll_in_window(
                conn, center_date=pay_date_d, window_days=args.window_days
            )
            bank_total = bank_emp + bank_sh
            cb_audits.append(
                CurlysbooksPayPeriodAudit(
                    period_number=int(r["period_number"] or 0),
                    end_date=str(r["end_date"] or ""),
                    pay_date=pay_date,
                    payroll_net_cents=net,
                    payroll_tips_cents=tips,
                    payroll_net_plus_tips_cents=payroll_total,
                    bank_employee_payroll_cents=bank_emp,
                    bank_shareholder_payroll_cents=bank_sh,
                    bank_total_payroll_cents=bank_total,
                    diff_cents=bank_total - payroll_total,
                )
            )

        with out_cb_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "period_number",
                    "end_date",
                    "pay_date",
                    "payroll_net_cents",
                    "payroll_net_amount",
                    "payroll_tips_cents",
                    "payroll_tips_amount",
                    "payroll_net_plus_tips_cents",
                    "payroll_net_plus_tips_amount",
                    "bank_employee_payroll_cents",
                    "bank_employee_payroll_amount",
                    "bank_shareholder_payroll_cents",
                    "bank_shareholder_payroll_amount",
                    "bank_total_payroll_cents",
                    "bank_total_payroll_amount",
                    "diff_cents",
                    "diff_amount",
                ]
            )
            for a in cb_audits:
                w.writerow(
                    [
                        a.period_number,
                        a.end_date,
                        a.pay_date,
                        a.payroll_net_cents,
                        cents_to_dollars(a.payroll_net_cents),
                        a.payroll_tips_cents,
                        cents_to_dollars(a.payroll_tips_cents),
                        a.payroll_net_plus_tips_cents,
                        cents_to_dollars(a.payroll_net_plus_tips_cents),
                        a.bank_employee_payroll_cents,
                        cents_to_dollars(a.bank_employee_payroll_cents),
                        a.bank_shareholder_payroll_cents,
                        cents_to_dollars(a.bank_shareholder_payroll_cents),
                        a.bank_total_payroll_cents,
                        cents_to_dollars(a.bank_total_payroll_cents),
                        a.diff_cents,
                        cents_to_dollars(a.diff_cents),
                    ]
                )

        cb_total = len(cb_audits)
        cb_exact = sum(1 for a in cb_audits if a.diff_cents == 0)
        cb_tips_total_cents = sum(a.payroll_tips_cents for a in cb_audits)

        with out_md.open("w", encoding="utf-8") as f:
            f.write("# Tips vs bank audit\n\n")

            f.write("## A) Employee exports (per-employee tip rows)\n\n")
            f.write("Scope:\n")
            f.write(f"- pay_period_end: {args.start} → {args.end}\n")
            f.write(f"- bank match window: ±{args.window_days} days\n")
            f.write(f"- bank amount tolerance: ±${cents_to_dollars(BANK_MATCH_TOLERANCE_CENTS)}\n\n")
            f.write("## Summary\n\n")
            f.write(f"- Tip rows: {total}\n")
            f.write(f"- Expected bank matches (net pay): {expected_net_matched}/{total}\n")
            f.write(f"- Net+tips bank matches (diagnostic only): {net_plus_matched}/{total}\n")
            f.write(f"- Tips-amount bank matches (diagnostic only): {tips_matched}/{total}\n")
            f.write(f"- Total tips in these rows: ${cents_to_dollars(tips_total_cents)}\n\n")
            f.write("How tips are represented in these export rows:\n\n")
            f.write("- `TIPS_ADDED_PRE_DEDUCTIONS`: tips were added to taxable pay (gross+vacation+tips) and then deductions were taken.\n")
            f.write("- `TIPS_EMBEDDED_IN_GROSS`: tips are already embedded in the gross figure; the tips column is informational.\n")
            f.write("\nTip totals by representation:\n\n")
            f.write(f"- TIPS_ADDED_PRE_DEDUCTIONS: ${cents_to_dollars(tips_added_pre_deductions)}\n")
            f.write(f"- TIPS_EMBEDDED_IN_GROSS: ${cents_to_dollars(tips_embedded_in_gross)}\n")
            f.write(f"- AMBIG: ${cents_to_dollars(amb_tips)}\n\n")
            f.write("Interpretation:\n\n")
            f.write("- For these per-employee export rows, **tips are already included in the net pay amount**, so the payroll e-transfer is expected to match **net pay**, not **net+tips**.\n")
            f.write("- FY2025 behavior (tips paid on top of net with no deductions) is audited in section B using curlys-books pay-period totals.\n\n")
            f.write("Detail CSV:\n")
            f.write(f"- `{out_csv}`\n")

            f.write("\n## B) curlys-books backfill (pay-period totals)\n\n")
            f.write("This section checks whether bank payroll e-transfers match `total_net + total_tips`.\n\n")
            f.write("Scope:\n")
            f.write(f"- pay_period_end: {args.start} → {args.end}\n")
            f.write(f"- bank match window (centered on pay_date): ±{args.window_days} days\n\n")
            f.write("Summary:\n\n")
            f.write(f"- Pay periods with tips: {cb_total}\n")
            f.write(f"- Exact bank matches (employee+shareholder payroll): {cb_exact}/{cb_total}\n")
            f.write(f"- Total tips in these periods: ${cents_to_dollars(cb_tips_total_cents)}\n\n")
            f.write("Detail CSV:\n")
            f.write(f"- `{out_cb_csv}`\n")

    finally:
        conn.close()

    print("TIPS VS BANK AUDIT BUILT")
    print(f"- out: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
