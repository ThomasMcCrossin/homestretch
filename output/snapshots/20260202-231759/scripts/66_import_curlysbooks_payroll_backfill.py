#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import io
import sqlite3
import subprocess
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, connect_db, dollars_to_cents, get_source, load_manifest


def run_psql_copy(curlys_books_path: Path, select_sql: str) -> str:
    copy_sql = f"COPY ({select_sql}) TO STDOUT WITH CSV HEADER"
    cmd = [
        "docker",
        "compose",
        "exec",
        "-T",
        "postgres",
        "psql",
        "-U",
        "curlys_admin",
        "-d",
        "curlys_books",
        "-v",
        "ON_ERROR_STOP=1",
        "-c",
        copy_sql,
    ]
    res = subprocess.run(cmd, cwd=curlys_books_path, check=True, capture_output=True, text=True)
    return res.stdout


def parse_csv(text: str) -> list[dict[str, str]]:
    buf = io.StringIO(text)
    reader = csv.DictReader(buf)
    return [{k: (v if v is not None else "").strip() for k, v in row.items()} for row in reader]


def ensure_source_file(conn: sqlite3.Connection, *, source_key: str, kind: str, path: str, semantics: str) -> int:
    conn.execute(
        """
        INSERT INTO source_files (source_key, kind, path, sha256, semantics)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(source_key) DO UPDATE SET
          kind=excluded.kind,
          path=excluded.path,
          sha256=excluded.sha256,
          semantics=excluded.semantics
        """,
        (source_key, kind, path, None, semantics),
    )
    row = conn.execute("SELECT id FROM source_files WHERE source_key = ?", (source_key,)).fetchone()
    if not row:
        raise SystemExit(f"Failed to persist source_files row for {source_key}")
    return int(row["id"])


def as_int(value: str | None) -> int | None:
    s = (value or "").strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def as_cents(value: str | None) -> int:
    s = (value or "").strip()
    if not s:
        return 0
    return dollars_to_cents(s)


@dataclass(frozen=True)
class ImportCounts:
    pay_periods: int
    payroll_runs: int
    ytd_rows: int


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--entity", default="corp")
    ap.add_argument("--tax-year", type=int, default=2025)
    ap.add_argument("--calculated-by", default="backfill_csv_2025_corp")
    ap.add_argument("--reset", action="store_true", help="Delete existing rows for this entity/tax year before import.")
    args = ap.parse_args()

    manifest = load_manifest()
    curlys_src = get_source(manifest, "curlys_books")
    curlys_books_path = Path(str(curlys_src["path"]))

    conn = connect_db(args.db)
    try:
        with conn:
            source_file_id = ensure_source_file(
                conn,
                source_key=f"curlys_books_payroll_backfill_{args.entity}_{args.tax_year}",
                kind="postgres_query",
                path=str(curlys_books_path),
                semantics=(
                    "Canonical payroll backfill imported from curlys-books Postgres: "
                    f"shared.pay_periods + curlys_corp.payroll_runs (calculated_by={args.calculated_by!r}) "
                    f"+ shared.ytd_accumulations for entity={args.entity!r} tax_year={args.tax_year}."
                ),
            )

            if args.reset:
                conn.execute(
                    "DELETE FROM curlysbooks_payroll_runs WHERE pay_period_id IN (SELECT pay_period_id FROM curlysbooks_pay_periods WHERE entity = ? AND tax_year = ?)",
                    (args.entity, args.tax_year),
                )
                conn.execute(
                    "DELETE FROM curlysbooks_pay_periods WHERE entity = ? AND tax_year = ?",
                    (args.entity, args.tax_year),
                )
                conn.execute(
                    "DELETE FROM curlysbooks_ytd_accumulations WHERE entity = ? AND tax_year = ?",
                    (args.entity, args.tax_year),
                )

            # 1) Pay periods
            pay_periods_sql = f"""
              SELECT
                id::text AS pay_period_id,
                entity,
                tax_year,
                period_number,
                pay_frequency,
                start_date::text AS start_date,
                end_date::text AS end_date,
                pay_date::text AS pay_date,
                status,
                COALESCE(closed_at::text, '') AS closed_at,
                COALESCE(created_at::text, '') AS created_at
              FROM shared.pay_periods
              WHERE entity = {sql_quote(args.entity)}
                AND tax_year = {args.tax_year}
              ORDER BY period_number
            """
            pp_csv = run_psql_copy(curlys_books_path, pay_periods_sql)
            pp_rows = parse_csv(pp_csv)

            for r in pp_rows:
                conn.execute(
                    """
                    INSERT INTO curlysbooks_pay_periods (
                      source_file_id, pay_period_id, entity, tax_year, period_number, pay_frequency,
                      start_date, end_date, pay_date, status, closed_at, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(pay_period_id) DO UPDATE SET
                      source_file_id=excluded.source_file_id,
                      entity=excluded.entity,
                      tax_year=excluded.tax_year,
                      period_number=excluded.period_number,
                      pay_frequency=excluded.pay_frequency,
                      start_date=excluded.start_date,
                      end_date=excluded.end_date,
                      pay_date=excluded.pay_date,
                      status=excluded.status,
                      closed_at=excluded.closed_at,
                      created_at=excluded.created_at
                    """,
                    (
                        source_file_id,
                        r.get("pay_period_id") or "",
                        r.get("entity") or "",
                        int(r.get("tax_year") or 0),
                        as_int(r.get("period_number")) or None,
                        (r.get("pay_frequency") or "") or None,
                        (r.get("start_date") or "") or None,
                        (r.get("end_date") or "") or None,
                        (r.get("pay_date") or "") or None,
                        (r.get("status") or "") or None,
                        (r.get("closed_at") or "") or None,
                        (r.get("created_at") or "") or None,
                    ),
                )

            # 2) Payroll runs (filtered to backfill)
            runs_sql = f"""
              SELECT
                r.id::text AS payroll_run_id,
                r.pay_period_id::text AS pay_period_id,
                r.run_number,
                r.status,
                COALESCE(r.calculated_by, '') AS calculated_by,
                COALESCE(r.calculated_at::text, '') AS calculated_at,
                r.employee_count,
                COALESCE(r.total_gross, 0)::text AS total_gross,
                COALESCE(r.total_vacation_pay, 0)::text AS total_vacation_pay,
                COALESCE(r.total_tips, 0)::text AS total_tips,
                COALESCE(r.total_cpp, 0)::text AS total_cpp,
                COALESCE(r.total_cpp2, 0)::text AS total_cpp2,
                COALESCE(r.total_ei, 0)::text AS total_ei,
                COALESCE(r.total_federal_tax, 0)::text AS total_federal_tax,
                COALESCE(r.total_provincial_tax, 0)::text AS total_provincial_tax,
                COALESCE(r.total_deductions, 0)::text AS total_deductions,
                COALESCE(r.total_net, 0)::text AS total_net,
                COALESCE(r.total_employer_cpp, 0)::text AS total_employer_cpp,
                COALESCE(r.total_employer_cpp2, 0)::text AS total_employer_cpp2,
                COALESCE(r.total_employer_ei, 0)::text AS total_employer_ei,
                COALESCE(r.total_employer_cost, 0)::text AS total_employer_cost
              FROM curlys_corp.payroll_runs r
              JOIN shared.pay_periods p ON p.id = r.pay_period_id
              WHERE p.entity = {sql_quote(args.entity)}
                AND p.tax_year = {args.tax_year}
                AND r.calculated_by = {sql_quote(args.calculated_by)}
              ORDER BY p.period_number, r.run_number
            """
            runs_csv = run_psql_copy(curlys_books_path, runs_sql)
            run_rows = parse_csv(runs_csv)

            for r in run_rows:
                conn.execute(
                    """
                    INSERT INTO curlysbooks_payroll_runs (
                      source_file_id, payroll_run_id, pay_period_id, run_number, status,
                      calculated_by, calculated_at, employee_count,
                      total_gross_cents, total_vacation_pay_cents, total_tips_cents,
                      total_cpp_cents, total_cpp2_cents, total_ei_cents,
                      total_federal_tax_cents, total_provincial_tax_cents,
                      total_deductions_cents, total_net_cents,
                      total_employer_cpp_cents, total_employer_cpp2_cents, total_employer_ei_cents,
                      total_employer_cost_cents
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(payroll_run_id) DO UPDATE SET
                      source_file_id=excluded.source_file_id,
                      pay_period_id=excluded.pay_period_id,
                      run_number=excluded.run_number,
                      status=excluded.status,
                      calculated_by=excluded.calculated_by,
                      calculated_at=excluded.calculated_at,
                      employee_count=excluded.employee_count,
                      total_gross_cents=excluded.total_gross_cents,
                      total_vacation_pay_cents=excluded.total_vacation_pay_cents,
                      total_tips_cents=excluded.total_tips_cents,
                      total_cpp_cents=excluded.total_cpp_cents,
                      total_cpp2_cents=excluded.total_cpp2_cents,
                      total_ei_cents=excluded.total_ei_cents,
                      total_federal_tax_cents=excluded.total_federal_tax_cents,
                      total_provincial_tax_cents=excluded.total_provincial_tax_cents,
                      total_deductions_cents=excluded.total_deductions_cents,
                      total_net_cents=excluded.total_net_cents,
                      total_employer_cpp_cents=excluded.total_employer_cpp_cents,
                      total_employer_cpp2_cents=excluded.total_employer_cpp2_cents,
                      total_employer_ei_cents=excluded.total_employer_ei_cents,
                      total_employer_cost_cents=excluded.total_employer_cost_cents
                    """,
                    (
                        source_file_id,
                        r.get("payroll_run_id") or "",
                        r.get("pay_period_id") or "",
                        as_int(r.get("run_number")) or None,
                        (r.get("status") or "") or None,
                        (r.get("calculated_by") or "") or None,
                        (r.get("calculated_at") or "") or None,
                        as_int(r.get("employee_count")) or None,
                        as_cents(r.get("total_gross")),
                        as_cents(r.get("total_vacation_pay")),
                        as_cents(r.get("total_tips")),
                        as_cents(r.get("total_cpp")),
                        as_cents(r.get("total_cpp2")),
                        as_cents(r.get("total_ei")),
                        as_cents(r.get("total_federal_tax")),
                        as_cents(r.get("total_provincial_tax")),
                        as_cents(r.get("total_deductions")),
                        as_cents(r.get("total_net")),
                        as_cents(r.get("total_employer_cpp")),
                        as_cents(r.get("total_employer_cpp2")),
                        as_cents(r.get("total_employer_ei")),
                        as_cents(r.get("total_employer_cost")),
                    ),
                )

            # 3) YTD accumulations (year-level cross-check)
            ytd_sql = f"""
              SELECT
                y.id::text AS accumulation_id,
                y.employee_id::text AS employee_id,
                COALESCE(e.first_name, '') AS first_name,
                COALESCE(e.last_name, '') AS last_name,
                y.entity,
                y.tax_year,
                COALESCE(y.gross_earnings, 0)::text AS gross_earnings,
                COALESCE(y.cpp_contributions, 0)::text AS cpp_contributions,
                COALESCE(y.cpp2_contributions, 0)::text AS cpp2_contributions,
                COALESCE(y.ei_contributions, 0)::text AS ei_contributions,
                COALESCE(y.federal_tax, 0)::text AS federal_tax,
                COALESCE(y.provincial_tax, 0)::text AS provincial_tax,
                COALESCE(y.employer_cpp, 0)::text AS employer_cpp,
                COALESCE(y.employer_cpp2, 0)::text AS employer_cpp2,
                COALESCE(y.employer_ei, 0)::text AS employer_ei,
                COALESCE(y.tips_received, 0)::text AS tips_received,
                COALESCE(y.vacation_pay_accrued, 0)::text AS vacation_pay_accrued,
                COALESCE(y.vacation_pay_taken, 0)::text AS vacation_pay_taken,
                COALESCE(y.updated_at::text, '') AS updated_at
              FROM shared.ytd_accumulations y
              JOIN shared.employees e ON e.id = y.employee_id
              WHERE y.entity = {sql_quote(args.entity)}
                AND y.tax_year = {args.tax_year}
              ORDER BY e.last_name, e.first_name
            """
            ytd_csv = run_psql_copy(curlys_books_path, ytd_sql)
            ytd_rows = parse_csv(ytd_csv)
            for r in ytd_rows:
                name = (r.get("first_name") or "").strip() + " " + (r.get("last_name") or "").strip()
                name = name.strip() or None
                conn.execute(
                    """
                    INSERT INTO curlysbooks_ytd_accumulations (
                      source_file_id, accumulation_id, employee_id, employee_name,
                      entity, tax_year,
                      gross_earnings_cents, cpp_contributions_cents, cpp2_contributions_cents,
                      ei_contributions_cents, federal_tax_cents, provincial_tax_cents,
                      employer_cpp_cents, employer_cpp2_cents, employer_ei_cents,
                      tips_received_cents, vacation_pay_accrued_cents, vacation_pay_taken_cents,
                      updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(accumulation_id) DO UPDATE SET
                      source_file_id=excluded.source_file_id,
                      employee_id=excluded.employee_id,
                      employee_name=excluded.employee_name,
                      entity=excluded.entity,
                      tax_year=excluded.tax_year,
                      gross_earnings_cents=excluded.gross_earnings_cents,
                      cpp_contributions_cents=excluded.cpp_contributions_cents,
                      cpp2_contributions_cents=excluded.cpp2_contributions_cents,
                      ei_contributions_cents=excluded.ei_contributions_cents,
                      federal_tax_cents=excluded.federal_tax_cents,
                      provincial_tax_cents=excluded.provincial_tax_cents,
                      employer_cpp_cents=excluded.employer_cpp_cents,
                      employer_cpp2_cents=excluded.employer_cpp2_cents,
                      employer_ei_cents=excluded.employer_ei_cents,
                      tips_received_cents=excluded.tips_received_cents,
                      vacation_pay_accrued_cents=excluded.vacation_pay_accrued_cents,
                      vacation_pay_taken_cents=excluded.vacation_pay_taken_cents,
                      updated_at=excluded.updated_at
                    """,
                    (
                        source_file_id,
                        r.get("accumulation_id") or "",
                        r.get("employee_id") or "",
                        name,
                        r.get("entity") or "",
                        int(r.get("tax_year") or 0),
                        as_cents(r.get("gross_earnings")),
                        as_cents(r.get("cpp_contributions")),
                        as_cents(r.get("cpp2_contributions")),
                        as_cents(r.get("ei_contributions")),
                        as_cents(r.get("federal_tax")),
                        as_cents(r.get("provincial_tax")),
                        as_cents(r.get("employer_cpp")),
                        as_cents(r.get("employer_cpp2")),
                        as_cents(r.get("employer_ei")),
                        as_cents(r.get("tips_received")),
                        as_cents(r.get("vacation_pay_accrued")),
                        as_cents(r.get("vacation_pay_taken")),
                        (r.get("updated_at") or "") or None,
                    ),
                )

    finally:
        conn.close()

    counts = ImportCounts(pay_periods=len(pp_rows), payroll_runs=len(run_rows), ytd_rows=len(ytd_rows))
    print("CURLYS-BOOKS PAYROLL BACKFILL IMPORT COMPLETE")
    print(f"- db: {args.db}")
    print(f"- entity: {args.entity}")
    print(f"- tax_year: {args.tax_year}")
    print(f"- calculated_by: {args.calculated_by}")
    print(f"- pay_periods: {counts.pay_periods}")
    print(f"- payroll_runs: {counts.payroll_runs}")
    print(f"- ytd_rows: {counts.ytd_rows}")
    return 0


def sql_quote(value: str) -> str:
    return "'" + (value or "").replace("'", "''") + "'"


if __name__ == "__main__":
    raise SystemExit(main())
