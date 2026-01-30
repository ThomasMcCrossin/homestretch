#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


@dataclass(frozen=True)
class PayrollMonth:
    year: int
    month: int  # 1..12
    source: str  # "monthly_working_paper" | "employee_pay_periods"
    gross_pay_cents: int
    employer_taxes_cents: int
    remittance_cents: int
    net_pay_cents: int
    tips_cents: int | None
    net_pay_plus_tips_cents: int | None

    @property
    def employee_deductions_cents(self) -> int:
        return self.remittance_cents - self.employer_taxes_cents

    @property
    def compare_base_cents(self) -> int:
        return self.net_pay_plus_tips_cents if self.net_pay_plus_tips_cents is not None else self.net_pay_cents

    @property
    def ym(self) -> str:
        return f"{self.year:04d}-{self.month:02d}"


def cents_to_dollars(cents: int) -> str:
    return f"{Decimal(cents) / Decimal(100):.2f}"


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def month_start(year: int, month: int) -> date:
    return date(year, month, 1)


def fy_includes_month(fy: FiscalYear, year: int, month: int) -> bool:
    ms = month_start(year, month)
    return date.fromisoformat(fy.start_date) <= ms <= date.fromisoformat(fy.end_date)


def fetch_payroll_months_from_employee_periods(conn: sqlite3.Connection) -> dict[tuple[int, int], PayrollMonth]:
    rows = conn.execute(
        """
        SELECT
          substr(pay_period_end, 1, 4) AS yyyy,
          substr(pay_period_end, 6, 2) AS mm,
          SUM(gross_pay_cents) AS gross_pay_cents,
          SUM(tips_cents) AS tips_cents,
          SUM(employer_cpp_cents + employer_ei_cents) AS employer_taxes_cents,
          -- Some exports have blank/incorrect "Our Remittance" values; derive from components for determinism.
          SUM(
            federal_tax_cents
            + provincial_tax_cents
            + employee_cpp_cents
            + employee_ei_cents
            + employer_cpp_cents
            + employer_ei_cents
          ) AS remittance_cents,
          SUM(net_pay_cents) AS net_pay_cents
        FROM payroll_employee_pay_periods
        GROUP BY yyyy, mm
        ORDER BY yyyy, mm
        """
    ).fetchall()

    out: dict[tuple[int, int], PayrollMonth] = {}
    for r in rows:
        y = int(r["yyyy"])
        m = int(r["mm"])
        out[(y, m)] = PayrollMonth(
            year=y,
            month=m,
            source="employee_pay_periods",
            gross_pay_cents=int(r["gross_pay_cents"] or 0),
            employer_taxes_cents=int(r["employer_taxes_cents"] or 0),
            remittance_cents=int(r["remittance_cents"] or 0),
            net_pay_cents=int(r["net_pay_cents"] or 0),
            tips_cents=int(r["tips_cents"] or 0),
            net_pay_plus_tips_cents=None,
        )
    return out


def fetch_payroll_months_from_working_papers(conn: sqlite3.Connection) -> dict[tuple[int, int], PayrollMonth]:
    rows = conn.execute(
        """
        SELECT
          year,
          month,
          gross_pay_cents,
          remittance_cents,
          employer_taxes_cents,
          net_pay_plus_tips_cents
        FROM payroll_monthly_totals
        ORDER BY year, month
        """
    ).fetchall()

    out: dict[tuple[int, int], PayrollMonth] = {}
    for r in rows:
        y = int(r["year"])
        m = int(r["month"])
        gross = int(r["gross_pay_cents"] or 0)
        rem = int(r["remittance_cents"] or 0)
        employer = int(r["employer_taxes_cents"] or 0)
        net = gross - (rem - employer)
        net_plus_raw = int(r["net_pay_plus_tips_cents"] or 0)
        net_plus: int | None = net_plus_raw if net_plus_raw else None
        tips: int | None = (net_plus_raw - net) if net_plus_raw else None
        out[(y, m)] = PayrollMonth(
            year=y,
            month=m,
            source="monthly_working_paper",
            gross_pay_cents=gross,
            employer_taxes_cents=employer,
            remittance_cents=rem,
            net_pay_cents=net,
            tips_cents=tips,
            net_pay_plus_tips_cents=net_plus,
        )
    return out


def fetch_payroll_months_from_curlysbooks_backfill(
    conn: sqlite3.Connection,
    *,
    entity: str,
    tax_year: int,
    calculated_by: str,
) -> dict[tuple[int, int], PayrollMonth]:
    rows = conn.execute(
        """
        SELECT
          substr(p.end_date, 1, 4) AS yyyy,
          substr(p.end_date, 6, 2) AS mm,
          SUM(r.total_gross_cents + r.total_vacation_pay_cents) AS gross_pay_cents,
          SUM(r.total_net_cents) AS net_pay_cents,
          SUM(r.total_tips_cents) AS tips_cents,
          SUM(r.total_employer_cpp_cents + r.total_employer_cpp2_cents + r.total_employer_ei_cents) AS employer_taxes_cents,
          SUM(
            r.total_cpp_cents
            + r.total_cpp2_cents
            + r.total_ei_cents
            + r.total_federal_tax_cents
            + r.total_provincial_tax_cents
            + r.total_employer_cpp_cents
            + r.total_employer_cpp2_cents
            + r.total_employer_ei_cents
          ) AS remittance_cents
        FROM curlysbooks_payroll_runs r
        JOIN curlysbooks_pay_periods p ON p.pay_period_id = r.pay_period_id
        WHERE p.entity = ?
          AND p.tax_year = ?
          AND r.calculated_by = ?
        GROUP BY yyyy, mm
        ORDER BY yyyy, mm
        """,
        (entity, tax_year, calculated_by),
    ).fetchall()

    out: dict[tuple[int, int], PayrollMonth] = {}
    for r in rows:
        y = int(r["yyyy"])
        m = int(r["mm"])
        gross = int(r["gross_pay_cents"] or 0)
        net = int(r["net_pay_cents"] or 0)
        tips = int(r["tips_cents"] or 0)
        net_plus = net + tips if (net or tips) else None
        out[(y, m)] = PayrollMonth(
            year=y,
            month=m,
            source="curlysbooks_backfill",
            gross_pay_cents=gross,
            employer_taxes_cents=int(r["employer_taxes_cents"] or 0),
            remittance_cents=int(r["remittance_cents"] or 0),
            net_pay_cents=net,
            tips_cents=tips,
            net_pay_plus_tips_cents=net_plus,
        )
    return out


def choose_unified_months(
    *,
    employee_months: dict[tuple[int, int], PayrollMonth],
    working_paper_months: dict[tuple[int, int], PayrollMonth],
    curlysbooks_months: dict[tuple[int, int], PayrollMonth],
    prefer_employee: bool,
    prefer_working_paper: bool,
) -> tuple[list[PayrollMonth], list[tuple[PayrollMonth | None, PayrollMonth | None, PayrollMonth | None]]]:
    keys = sorted(set(employee_months.keys()) | set(working_paper_months.keys()) | set(curlysbooks_months.keys()))
    unified: list[PayrollMonth] = []
    overlaps: list[tuple[PayrollMonth | None, PayrollMonth | None, PayrollMonth | None]] = []
    for key in keys:
        emp = employee_months.get(key)
        wp = working_paper_months.get(key)
        cb = curlysbooks_months.get(key)
        if sum(1 for x in (emp, wp, cb) if x) >= 2:
            overlaps.append((cb, emp, wp))
        chosen = None
        # Priority (default):
        # 1) curlys-books backfill (canonical for 2025 corp)
        # 2) employee pay period exports (needed for CPP/EI/tax splits)
        # 3) monthly working papers (rollup-only; no split detail)
        #
        # Compatibility: `--prefer-employee` is preserved but is now effectively the default.
        if cb:
            chosen = cb
        elif prefer_working_paper and wp:
            chosen = wp
        elif prefer_employee and emp:
            chosen = emp
        elif emp:
            chosen = emp
        elif wp:
            chosen = wp
        else:
            chosen = None
        if chosen:
            unified.append(chosen)
    return unified, overlaps


def load_bank_txn_category_override_entries(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    data = load_yaml(path)
    raw = data.get("bank_txn_category_overrides")
    if not isinstance(raw, dict):
        return {}
    out: dict[str, dict] = {}
    for bank_txn_id, cfg in raw.items():
        if not isinstance(cfg, dict):
            continue
        to_cat = str(cfg.get("to_category") or "").strip()
        if not to_cat:
            continue
        entry = dict(cfg)
        entry["to_category"] = to_cat
        out[str(bank_txn_id).strip()] = entry
    return out


def fetch_bank_txn_categories(conn: sqlite3.Connection) -> dict[str, str]:
    """
    Return a single evidence txn_category per bank_txn_id.
    If multiple classifications exist, prefer verified rows, then lowest id.
    """
    rows = conn.execute(
        """
        SELECT id, bank_txn_id, txn_category, verified
        FROM fresher_debits__bank_txn_classifications
        ORDER BY CAST(verified AS INTEGER) DESC, CAST(id AS INTEGER) ASC
        """
    ).fetchall()
    out: dict[str, str] = {}
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"])
        if bank_txn_id in out:
            continue
        out[bank_txn_id] = str(r["txn_category"])
    return out


def bank_category_overrides_from_entries(entries: dict[str, dict]) -> dict[str, str]:
    return {bank_txn_id: str(cfg.get("to_category") or "").strip() for bank_txn_id, cfg in entries.items()}


def fetch_bank_txn_details(conn: sqlite3.Connection, bank_txn_ids: list[str]) -> dict[str, sqlite3.Row]:
    if not bank_txn_ids:
        return {}
    placeholders = ",".join(["?"] * len(bank_txn_ids))
    rows = conn.execute(
        f"""
        SELECT id, txn_date, CAST(debit_cents AS INTEGER) AS debit_cents, description
        FROM fresher_debits__bank_transactions
        WHERE id IN ({placeholders})
        """,
        bank_txn_ids,
    ).fetchall()
    return {str(r["id"]): r for r in rows}


def fetch_bank_payroll_paid_by_month(
    conn: sqlite3.Connection,
    *,
    category_overrides: dict[str, str],
    category_by_bank_txn_id: dict[str, str],
) -> dict[str, int]:
    payroll_categories = {"EMPLOYEE_PAYROLL", "SHAREHOLDER_PAYROLL"}

    rows = conn.execute(
        """
        SELECT
          t.id AS bank_txn_id,
          substr(t.txn_date, 1, 7) AS ym,
          CAST(t.debit_cents AS INTEGER) AS debit_cents
        FROM fresher_debits__bank_transactions t
        WHERE CAST(t.debit_cents AS INTEGER) > 0
        """
    ).fetchall()

    out: dict[str, int] = {}
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"])
        ym = str(r["ym"] or "")
        if not ym:
            continue
        debit = int(r["debit_cents"] or 0)
        if debit <= 0:
            continue

        cat = category_by_bank_txn_id.get(bank_txn_id)
        if not cat:
            continue
        cat = category_overrides.get(bank_txn_id, cat)
        if cat not in payroll_categories:
            continue

        out[ym] = out.get(ym, 0) + debit
    return out


def fetch_bank_match_for_amount(conn: sqlite3.Connection, *, txn_date: str, amount_cents: int) -> tuple[str, str | None, str] | None:
    if not txn_date or not amount_cents:
        return None
    row = conn.execute(
        """
        SELECT
          t.id AS bank_txn_id,
          c.txn_category AS txn_category,
          t.description AS description
        FROM fresher_debits__bank_transactions t
        LEFT JOIN fresher_debits__bank_txn_classifications c ON c.bank_txn_id = t.id
        WHERE t.txn_date = ?
          AND CAST(t.debit_cents AS INTEGER) = ?
        ORDER BY
          CASE
            WHEN c.txn_category IN ('PAYROLL_REMIT', 'PAYROLL_REIMBURSE') THEN 0
            ELSE 1
          END,
          t.id
        LIMIT 1
        """,
        (txn_date, amount_cents),
    ).fetchone()
    if not row:
        return None
    return (str(row["bank_txn_id"]), (str(row["txn_category"]) if row["txn_category"] is not None else None), str(row["description"] or ""))


def fetch_employee_bank_vs_export_delta(
    conn: sqlite3.Connection,
    *,
    employee_name_like: str,
    year: int,
) -> tuple[int, int, int]:
    """
    Returns: (bank_total_cents, export_net_total_cents, delta_cents)
    Bank total is based on description/recipient matches.
    Export total is based on payroll_employee_pay_periods net pay.
    """
    year_str = str(year)
    emp_row = conn.execute(
        """
        SELECT SUM(net_pay_cents) AS net_cents
        FROM payroll_employee_pay_periods
        WHERE employee_name LIKE ?
          AND substr(pay_period_end, 1, 4) = ?
        """,
        (employee_name_like, year_str),
    ).fetchone()
    export_net = int(emp_row["net_cents"] or 0) if emp_row else 0

    bank_row = conn.execute(
        """
        SELECT SUM(CAST(t.debit_cents AS INTEGER)) AS bank_cents
        FROM fresher_debits__bank_transactions t
        WHERE t.txn_date BETWEEN ? AND ?
          AND CAST(t.debit_cents AS INTEGER) > 0
          AND (
            upper(t.description) LIKE ?
            OR upper(coalesce(t.etransfer_recipient, '')) LIKE ?
          )
        """,
        (f"{year_str}-01-01", f"{year_str}-12-31", f"%{employee_name_like.strip('%').upper()}%", f"%{employee_name_like.strip('%').upper()}%"),
    ).fetchone()
    bank_total = int(bank_row["bank_cents"] or 0) if bank_row else 0
    delta = bank_total - export_net
    return bank_total, export_net, delta


def fetch_earliest_bank_payment_for_employee(
    conn: sqlite3.Connection,
    *,
    employee_name_like: str,
    year: int,
) -> tuple[str, int, str] | None:
    year_str = str(year)
    row = conn.execute(
        """
        SELECT t.txn_date, CAST(t.debit_cents AS INTEGER) AS debit_cents, t.description
        FROM fresher_debits__bank_transactions t
        WHERE t.txn_date BETWEEN ? AND ?
          AND CAST(t.debit_cents AS INTEGER) > 0
          AND (
            upper(t.description) LIKE ?
            OR upper(coalesce(t.etransfer_recipient, '')) LIKE ?
          )
        ORDER BY t.txn_date, t.id
        LIMIT 1
        """,
        (f"{year_str}-01-01", f"{year_str}-12-31", f"%{employee_name_like.strip('%').upper()}%", f"%{employee_name_like.strip('%').upper()}%"),
    ).fetchone()
    if not row:
        return None
    return (str(row["txn_date"]), int(row["debit_cents"] or 0), str(row["description"] or ""))


MONTH_NAME_TO_NUM = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


def parse_cra_payment_month(label: str) -> tuple[int, int] | None:
    # Examples:
    #   "Payment Apr 2024"
    #   "Payment Oct 2025 late"
    #   "Payment Sept 2023 late"
    s = (label or "").strip()
    m = re.match(r"^Payment\s+([A-Za-z]+)\s+(20[0-9]{2})\b", s)
    if not m:
        return None
    month_name = m.group(1).strip().lower()
    year = int(m.group(2))
    month = MONTH_NAME_TO_NUM.get(month_name)
    if not month:
        return None
    return (year, month)


def fetch_cra_payments_by_payroll_month(conn: sqlite3.Connection) -> dict[tuple[int, int], int]:
    rows = conn.execute(
        """
        SELECT transaction_label, amount_cents, cr_dr
        FROM cra_payroll_account_transactions
        WHERE cr_dr IS NOT NULL AND amount_cents IS NOT NULL
        """
    ).fetchall()
    out: dict[tuple[int, int], int] = {}
    for r in rows:
        label = str(r["transaction_label"] or "").strip()
        cr_dr = str(r["cr_dr"] or "").strip().upper()
        if cr_dr != "CR":
            continue
        key = parse_cra_payment_month(label)
        if not key:
            continue
        out[key] = out.get(key, 0) + int(r["amount_cents"] or 0)
    return out


def payroll_remittance_payable_at_fy_end(
    fy: FiscalYear,
    *,
    working_paper_months: dict[tuple[int, int], PayrollMonth],
    cra_rows: list[sqlite3.Row],
) -> tuple[int, str | None, str | None]:
    """
    Best-effort, deterministic model:
    - Use the working paper remittance for the final FY month (May).
    - Confirm payment date via CRA "Payment <Month> <Year>" label if present.
    Returns: (payable_cents, cra_date_received, cra_label)
    """
    fy_end = date.fromisoformat(fy.end_date)
    target_key = (fy_end.year, fy_end.month)
    target = working_paper_months.get(target_key)
    if not target or target.remittance_cents == 0:
        return (0, None, None)

    paid_by_fy_end = 0
    received_dates: list[str] = []
    labels: set[str] = set()

    for r in cra_rows:
        if str(r["cr_dr"] or "").strip().upper() != "CR":
            continue
        label = str(r["transaction_label"] or "").strip()
        key = parse_cra_payment_month(label)
        if key != target_key:
            continue

        recv = str(r["date_received"] or "") or None
        if recv:
            received_dates.append(recv)
        labels.add(label)

        recv_date = parse_iso(recv)
        if recv_date and recv_date <= fy_end:
            paid_by_fy_end += int(r["amount_cents"] or 0)

    payable = max(0, target.remittance_cents - paid_by_fy_end)
    received_dates.sort()
    received_summary = received_dates[0] if received_dates else None
    label_summary = sorted(labels)[0] if labels else None
    return (payable, received_summary, label_summary)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument(
        "--prefer-employee",
        action="store_true",
        help="(compat) Prefer employee exports over monthly working papers when months overlap (this is now the default when both exist).",
    )
    ap.add_argument(
        "--prefer-working-paper",
        action="store_true",
        help="Prefer monthly working papers over employee exports when months overlap.",
    )
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_md = args.out_dir / "payroll_summary.md"
    out_months_csv = args.out_dir / "payroll_monthly_ledger.csv"
    out_cra_matches_csv = args.out_dir / "payroll_cra_account_matches.csv"
    out_remit_vs_cra_csv = args.out_dir / "payroll_remittance_vs_cra_by_month.csv"

    conn = connect_db(args.db)
    try:
        overrides_path = PROJECT_ROOT / "overrides" / "bank_txn_category_overrides.yml"
        bank_override_entries = load_bank_txn_category_override_entries(overrides_path)
        bank_cat_overrides = bank_category_overrides_from_entries(bank_override_entries)
        bank_cat_by_txn_id = fetch_bank_txn_categories(conn)
        bank_override_details = fetch_bank_txn_details(conn, list(bank_cat_overrides.keys()))

        employee_months = fetch_payroll_months_from_employee_periods(conn)
        working_paper_months = fetch_payroll_months_from_working_papers(conn)
        curlysbooks_months = fetch_payroll_months_from_curlysbooks_backfill(
            conn, entity="corp", tax_year=2025, calculated_by="backfill_csv_2025_corp"
        )
        unified_months, overlaps = choose_unified_months(
            employee_months=employee_months,
            working_paper_months=working_paper_months,
            curlysbooks_months=curlysbooks_months,
            prefer_employee=bool(args.prefer_employee),
            prefer_working_paper=bool(args.prefer_working_paper),
        )

        bank_payroll_by_month = fetch_bank_payroll_paid_by_month(
            conn,
            category_overrides=bank_cat_overrides,
            category_by_bank_txn_id=bank_cat_by_txn_id,
        )

        cra_rows = conn.execute(
            """
            SELECT date_posted, transaction_label, date_received, amount_cents, cr_dr
            FROM cra_payroll_account_transactions
            ORDER BY date_posted, source_row
            """
        ).fetchall()

        cra_payments_by_month = fetch_cra_payments_by_payroll_month(conn)

        scope_start = date.fromisoformat(min(fy.start_date for fy in fys))
        scope_end = date.fromisoformat(max(fy.end_date for fy in fys))

        # Month-level ledger CSV (unified)
        with out_months_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "year",
                    "month",
                    "ym",
                    "source",
                    "gross_pay_cents",
                    "employer_taxes_cents",
                    "remittance_cents",
                    "employee_deductions_cents",
                    "net_pay_cents",
                    "net_pay_plus_tips_cents",
                    "tips_cents",
                    "bank_payroll_paid_cents",
                    "bank_delta_vs_payroll_cents",
                ]
            )
            for pm in unified_months:
                bank_paid = bank_payroll_by_month.get(pm.ym, 0)
                compare_base = pm.compare_base_cents
                w.writerow(
                    [
                        pm.year,
                        pm.month,
                        pm.ym,
                        pm.source,
                        pm.gross_pay_cents,
                        pm.employer_taxes_cents,
                        pm.remittance_cents,
                        pm.employee_deductions_cents,
                        pm.net_pay_cents,
                        pm.net_pay_plus_tips_cents or "",
                        "" if pm.tips_cents is None else pm.tips_cents,
                        bank_paid,
                        bank_paid - compare_base,
                    ]
                )

        # CRA account matches CSV (all CRA rows; match to bank by date_received+amount)
        matched_bank_txn_ids: set[str] = set()
        cra_match_rows: list[dict[str, object]] = []
        for r in cra_rows:
            date_posted = str(r["date_posted"] or "")
            date_received = str(r["date_received"] or "") or None
            amount_cents = int(r["amount_cents"] or 0)
            cr_dr = str(r["cr_dr"] or "")
            label = str(r["transaction_label"] or "")
            bank_match = None
            if cr_dr.strip().upper() == "CR" and date_received and amount_cents:
                bank_match = fetch_bank_match_for_amount(conn, txn_date=date_received, amount_cents=amount_cents)
                if bank_match:
                    matched_bank_txn_ids.add(bank_match[0])
            cra_match_rows.append(
                {
                    "date_posted": date_posted,
                    "date_received": date_received,
                    "cr_dr": cr_dr,
                    "transaction_label": label,
                    "amount_cents": amount_cents,
                    "bank_match": bank_match,
                    "bank_group_match": None,
                }
            )

        # Grouped matches: when CRA has multiple credits on the same received date but the bank shows one combined reimbursement.
        unmatched_credit_by_received: dict[str, list[dict[str, object]]] = {}
        for rec in cra_match_rows:
            if str(rec.get("cr_dr") or "").strip().upper() != "CR":
                continue
            if not rec.get("date_received") or not rec.get("amount_cents"):
                continue
            if rec.get("bank_match"):
                continue
            unmatched_credit_by_received.setdefault(str(rec["date_received"]), []).append(rec)

        grouped_match_events: list[tuple[str, int, tuple[str, str | None, str], int]] = []
        for recv_date, recs in sorted(unmatched_credit_by_received.items()):
            if len(recs) < 2:
                continue
            total = sum(int(r.get("amount_cents") or 0) for r in recs)
            bank_group_match = fetch_bank_match_for_amount(conn, txn_date=recv_date, amount_cents=total)
            if not bank_group_match:
                continue
            if bank_group_match[0] in matched_bank_txn_ids:
                continue
            for r in recs:
                r["bank_group_match"] = bank_group_match
            matched_bank_txn_ids.add(bank_group_match[0])
            grouped_match_events.append((recv_date, total, bank_group_match, len(recs)))

        with out_cra_matches_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "date_posted",
                    "date_received",
                    "cr_dr",
                    "transaction_label",
                    "amount_cents",
                    "bank_txn_id",
                    "bank_txn_category",
                    "bank_txn_description",
                    "bank_group_txn_id",
                    "bank_group_txn_category",
                    "bank_group_txn_description",
                ]
            )
            for rec in cra_match_rows:
                bank_match = rec.get("bank_match")
                bank_group_match = rec.get("bank_group_match")
                w.writerow(
                    [
                        rec.get("date_posted") or "",
                        rec.get("date_received") or "",
                        rec.get("cr_dr") or "",
                        rec.get("transaction_label") or "",
                        rec.get("amount_cents") or 0,
                        bank_match[0] if bank_match else "",
                        bank_match[1] if bank_match and bank_match[1] else "",
                        bank_match[2] if bank_match else "",
                        bank_group_match[0] if bank_group_match else "",
                        bank_group_match[1] if bank_group_match and bank_group_match[1] else "",
                        bank_group_match[2] if bank_group_match else "",
                    ]
                )

        # Bank-side remittance transactions that don't map to any CRA credit (by date+amount match).
        bank_remit_rows = conn.execute(
            """
            SELECT
              t.id AS bank_txn_id,
              t.txn_date AS txn_date,
              CAST(t.debit_cents AS INTEGER) AS debit_cents,
              c.txn_category AS txn_category,
              t.description AS description
            FROM fresher_debits__bank_txn_classifications c
            JOIN fresher_debits__bank_transactions t ON t.id = c.bank_txn_id
            WHERE c.txn_category IN ('PAYROLL_REMIT', 'PAYROLL_REIMBURSE')
            ORDER BY t.txn_date, t.id
            """
        ).fetchall()
        unmatched_bank_remit_rows = [r for r in bank_remit_rows if str(r["bank_txn_id"]) not in matched_bank_txn_ids]

        # Remittance vs CRA by month CSV (working paper vs CRA Payment <month>)
        with out_remit_vs_cra_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["year", "month", "ym", "working_paper_remittance_cents", "cra_payment_cents", "delta_cents"])
            keys = sorted(set(working_paper_months.keys()) | set(cra_payments_by_month.keys()))
            for (y, m) in keys:
                wp = working_paper_months.get((y, m))
                wp_remit = wp.remittance_cents if wp else 0
                cra_amt = cra_payments_by_month.get((y, m), 0)
                w.writerow([y, m, f"{y:04d}-{m:02d}", wp_remit, cra_amt, cra_amt - wp_remit])

        # FY totals (unified)
        fy_totals: dict[str, dict[str, int]] = {}
        for fy in fys:
            totals = {
                "gross_pay_cents": 0,
                "employer_taxes_cents": 0,
                "remittance_cents": 0,
                "net_pay_cents": 0,
                "net_pay_plus_tips_cents": 0,
                "tips_cents": 0,
                "compare_base_cents": 0,
                "bank_payroll_paid_cents": 0,
            }
            for pm in unified_months:
                if not fy_includes_month(fy, pm.year, pm.month):
                    continue
                totals["gross_pay_cents"] += pm.gross_pay_cents
                totals["employer_taxes_cents"] += pm.employer_taxes_cents
                totals["remittance_cents"] += pm.remittance_cents
                totals["net_pay_cents"] += pm.net_pay_cents
                totals["compare_base_cents"] += pm.compare_base_cents
                if pm.net_pay_plus_tips_cents is not None:
                    totals["net_pay_plus_tips_cents"] += pm.net_pay_plus_tips_cents
                if pm.tips_cents is not None:
                    totals["tips_cents"] += pm.tips_cents
                totals["bank_payroll_paid_cents"] += bank_payroll_by_month.get(pm.ym, 0)

            fy_totals[fy.fy] = totals

        # Year-end remittance payable (source deductions)
        fy_payables: dict[str, tuple[int, str | None, str | None]] = {}
        for fy in fys:
            fy_payables[fy.fy] = payroll_remittance_payable_at_fy_end(
                fy, working_paper_months=working_paper_months, cra_rows=cra_rows
            )

        # Markdown summary
        with out_md.open("w", encoding="utf-8") as f:
            f.write("# Payroll summary (from exports + CRA + bank)\n\n")
            f.write("This report is derived from:\n")
            f.write("- `payroll_employee_pay_periods` (employee-level 2023 CSVs)\n")
            f.write("- `payroll_monthly_totals` (monthly working papers 2024/2025)\n")
            f.write("- `cra_payroll_account_transactions` (CRA payroll account export)\n")
            f.write("- `fresher_debits__bank_transactions` + `fresher_debits__bank_txn_classifications`\n\n")

            f.write("## Fiscal year totals (unified)\n\n")
            f.write("| FY | gross_pay | employer_taxes | remittance | net_pay (derived) | tips (if available) | bank payroll paid | delta |\n")
            f.write("|---|---:|---:|---:|---:|---:|---:|---:|\n")
            for fy in fys:
                t = fy_totals.get(fy.fy) or {}
                gross = int(t.get("gross_pay_cents") or 0)
                employer = int(t.get("employer_taxes_cents") or 0)
                remit = int(t.get("remittance_cents") or 0)
                net = int(t.get("net_pay_cents") or 0)
                tips = int(t.get("tips_cents") or 0)
                bank_paid = int(t.get("bank_payroll_paid_cents") or 0)
                compare_base = int(t.get("compare_base_cents") or 0)
                delta = bank_paid - compare_base
                f.write(
                    f"| {fy.fy} | ${cents_to_dollars(gross)} | ${cents_to_dollars(employer)} | ${cents_to_dollars(remit)} | ${cents_to_dollars(net)} | ${cents_to_dollars(tips)} | ${cents_to_dollars(bank_paid)} | ${cents_to_dollars(delta)} |\n"
                )

            f.write("\nNotes:\n")
            f.write(
                "- `bank payroll paid` is based on bank `txn_date` (cash-basis timing) and only includes bank items categorized as `EMPLOYEE_PAYROLL`/`SHAREHOLDER_PAYROLL`.\n"
            )
            f.write(
                "- The `delta` is a reconciliation signal only; large differences can be caused by tips paid outside the bank, pay-period timing across month-end/year-end, or incomplete payroll exports.\n\n"
            )

            # Anthony 2024 sanity check note (bank vs export).
            bank_total, export_net, delta = fetch_employee_bank_vs_export_delta(
                conn, employee_name_like="Anthony%", year=2024
            )
            if bank_total or export_net:
                extra_note = ""
                if delta > 0:
                    first_payment = fetch_earliest_bank_payment_for_employee(
                        conn, employee_name_like="Anthony%", year=2024
                    )
                    if first_payment:
                        fp_date, fp_cents, _ = first_payment
                        extra_note = f" Includes {fp_date} payment ${cents_to_dollars(fp_cents)} not in export."
                f.write(
                    f"- Anthony 2024 bank vs export net: bank ${cents_to_dollars(bank_total)} vs export ${cents_to_dollars(export_net)} (delta ${cents_to_dollars(delta)}).{extra_note}\n\n"
                )

            f.write("## Bank category overrides (applied)\n\n")
            if not bank_override_entries:
                f.write("- None.\n\n")
            else:
                f.write(
                    "| bank_txn_id | date | amount | evidence_category | override_category | note |\n"
                )
                f.write("|---|---:|---:|---|---|---|\n")
                for bank_txn_id in sorted(bank_override_entries.keys(), key=lambda x: int(x) if str(x).isdigit() else str(x)):
                    entry = bank_override_entries.get(bank_txn_id, {})
                    detail = bank_override_details.get(bank_txn_id)
                    txn_date = entry.get("txn_date") or (detail["txn_date"] if detail else "")
                    debit_cents = entry.get("debit_cents")
                    if debit_cents is None and detail is not None:
                        debit_cents = detail["debit_cents"]
                    debit_cents = int(debit_cents or 0)
                    evidence_cat = bank_cat_by_txn_id.get(bank_txn_id, "")
                    override_cat = str(entry.get("to_category") or "")
                    note = str(entry.get("reason") or "")
                    f.write(
                        f"| {bank_txn_id} | {txn_date} | ${cents_to_dollars(debit_cents)} | {evidence_cat} | {override_cat} | {note} |\n"
                    )
                f.write("\n")

            f.write("\n## Payroll remittance payable at fiscal year-end (May 31)\n\n")
            for fy in fys:
                payable_cents, received_date, label = fy_payables.get(fy.fy) or (0, None, None)
                f.write(f"### {fy.fy} ({fy.start_date} → {fy.end_date})\n\n")
                f.write(f"- Estimated source deductions payable at {fy.end_date}: ${cents_to_dollars(payable_cents)}\n")
                if label or received_date:
                    f.write(f"- CRA corroboration: `{label or ''}` received `{received_date or ''}`\n")
                f.write("\n")

            f.write("## Remittance vs CRA (by payroll month)\n\n")
            f.write("This compares `payroll_monthly_totals.remittance_cents` against CRA credits labelled `Payment <Month> <Year>`.\n\n")
            # Only show notable deltas (>= $1) in markdown; full detail in CSV.
            deltas = []
            for (y, m), wp_pm in working_paper_months.items():
                ms = month_start(y, m)
                if not (scope_start <= ms <= scope_end):
                    continue
                cra_amt = cra_payments_by_month.get((y, m), 0)
                if abs(cra_amt - wp_pm.remittance_cents) >= 100:
                    deltas.append((y, m, wp_pm.remittance_cents, cra_amt, cra_amt - wp_pm.remittance_cents))
            deltas.sort()
            if not deltas:
                f.write("- No month-level remittance deltas ≥ $1.00 found.\n\n")
            else:
                f.write("| payroll_month | working_paper_remittance | cra_payments | delta |\n")
                f.write("|---|---:|---:|---:|\n")
                for y, m, wp_amt, cra_amt, d in deltas:
                    f.write(
                        f"| {y:04d}-{m:02d} | ${cents_to_dollars(wp_amt)} | ${cents_to_dollars(cra_amt)} | ${cents_to_dollars(d)} |\n"
                    )
                f.write("\n")

            f.write("## CRA ↔ bank matching notes\n\n")
            cra_credit_rows = [
                r
                for r in cra_rows
                if str(r["cr_dr"] or "").strip().upper() == "CR" and int(r["amount_cents"] or 0) != 0
            ]
            f.write(f"- CRA credit rows (payments/adjustments): {len(cra_credit_rows)}\n")
            f.write(f"- Matched to bank by (date_received, amount): {len(matched_bank_txn_ids)}\n")

            # Unmatched after both 1:1 and grouped matching.
            unresolved_credit_rows: list[tuple[str, str, int, str]] = []
            for rec in cra_match_rows:
                if str(rec.get("cr_dr") or "").strip().upper() != "CR":
                    continue
                recv = str(rec.get("date_received") or "")
                if not recv:
                    continue
                amt = int(rec.get("amount_cents") or 0)
                if amt == 0:
                    continue
                if rec.get("bank_match") or rec.get("bank_group_match"):
                    continue
                unresolved_credit_rows.append((recv, str(rec.get("transaction_label") or ""), amt, str(rec.get("date_posted") or "")))

            if grouped_match_events:
                f.write("- Grouped matches found (multiple CRA credits reimbursed as one bank txn):\n")
                for recv, total, bank_match, n in grouped_match_events:
                    f.write(
                        f"  - {recv}: {n} CRA credits → ${cents_to_dollars(total)} matched bank `{bank_match[0]}` ({bank_match[1] or ''})\n"
                    )

            if unresolved_credit_rows:
                # Filter to in-scope received dates for the markdown list.
                in_scope_unmatched = []
                for recv, label, cents, posted in unresolved_credit_rows:
                    recv_date = parse_iso(recv)
                    if recv_date and scope_start <= recv_date <= scope_end:
                        in_scope_unmatched.append((recv, label, cents, posted))
                in_scope_unmatched.sort()
                if in_scope_unmatched:
                    f.write("- Unmatched in-scope CRA credits (likely paid outside this bank ledger, or missing in bank export):\n")
                    for recv, label, cents, posted in in_scope_unmatched[:15]:
                        f.write(f"  - {recv}: ${cents_to_dollars(cents)} — {label} (posted {posted})\n")
            f.write("\n")

            if unmatched_bank_remit_rows:
                pepsi = []
                gpfs_fee = []
                other = []
                for r in unmatched_bank_remit_rows:
                    desc = str(r["description"] or "")
                    if "THE PEPSI BOTTL" in desc.upper() or "PEPSI" in desc.upper():
                        pepsi.append(r)
                    elif "GPFS-SERVICE CHARGE" in desc.upper():
                        gpfs_fee.append(r)
                    else:
                        other.append(r)

                def sum_cents(rs: list[sqlite3.Row]) -> int:
                    return sum(int(x["debit_cents"] or 0) for x in rs)

                f.write("## Unmatched bank remittance-side txns (PAYROLL_REMIT/PAYROLL_REIMBURSE)\n\n")
                f.write(
                    "These bank transactions are categorized as payroll remittance/reimbursement but did not match any CRA credit by (date_received, amount).\n"
                )
                f.write("They are usually either vendor PADs misclassified as payroll, or GPFS service charges.\n\n")
                f.write(f"- Pepsico-like PADs: {len(pepsi)} txns, ${cents_to_dollars(sum_cents(pepsi))}\n")
                f.write(f"- GPFS service charges: {len(gpfs_fee)} txns, ${cents_to_dollars(sum_cents(gpfs_fee))}\n")
                f.write(f"- Other: {len(other)} txns, ${cents_to_dollars(sum_cents(other))}\n")
                if other:
                    f.write("- First few `Other` examples:\n")
                    for r in other[:10]:
                        f.write(
                            f"  - {r['txn_date']}: ${cents_to_dollars(int(r['debit_cents'] or 0))} — {r['txn_category']} — {r['description']}\n"
                        )
                f.write("\n")

            if overlaps:
                f.write("## Overlapping months (multiple sources)\n\n")
                f.write(
                    "These months appear in 2+ sources. By default, the unified ledger prefers `curlysbooks_backfill` when present, then employee exports, then monthly working papers.\n\n"
                )
                f.write("| month | curlysbooks gross | employee gross | working gross | curlysbooks vs working net+tips delta |\n")
                f.write("|---|---:|---:|---:|---:|\n")
                scope_start_ym = scope_start.isoformat()[:7]
                scope_end_ym = scope_end.isoformat()[:7]
                for cb, emp, wp in overlaps:
                    ym = (cb or emp or wp).ym if (cb or emp or wp) else ""
                    if ym and (ym < scope_start_ym or ym > scope_end_ym):
                        continue
                    cb_g = f"${cents_to_dollars(cb.gross_pay_cents)}" if cb else ""
                    emp_g = f"${cents_to_dollars(emp.gross_pay_cents)}" if emp else ""
                    wp_g = f"${cents_to_dollars(wp.gross_pay_cents)}" if wp else ""

                    delta_net_plus = ""
                    if cb and wp:
                        delta_net_plus = f"${cents_to_dollars(cb.compare_base_cents - wp.compare_base_cents)}"

                    f.write(f"| {ym} | {cb_g} | {emp_g} | {wp_g} | {delta_net_plus} |\n")
                f.write("\n")

            f.write("## Outputs\n\n")
            f.write(f"- `{out_months_csv}`\n")
            f.write(f"- `{out_cra_matches_csv}`\n")
            f.write(f"- `{out_remit_vs_cra_csv}`\n")

    finally:
        conn.close()

    print("PAYROLL SUMMARY BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_md}")
    print(f"- prefer_employee: {bool(args.prefer_employee)}")
    print(f"- prefer_working_paper: {bool(args.prefer_working_paper)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
