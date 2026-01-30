#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from statistics import median

from _lib import DB_PATH, PROJECT_ROOT, connect_db, dollars_to_cents, get_source, load_manifest, load_yaml, sha256_file


@dataclass(frozen=True)
class EmployeeImportResult:
    source_key: str
    employee_name: str
    rows_upserted: int
    rows_skipped: int


def ensure_source_file(conn: sqlite3.Connection, source_key: str, cfg: dict) -> int:
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
        (
            source_key,
            str(cfg.get("kind") or ""),
            str(cfg.get("path") or ""),
            str(cfg.get("sha256") or ""),
            str(cfg.get("semantics") or ""),
        ),
    )
    row = conn.execute("SELECT id FROM source_files WHERE source_key = ?", (source_key,)).fetchone()
    if not row:
        raise SystemExit(f"Failed to persist source_files row for {source_key}")
    return int(row["id"])


def verify_source(cfg: dict) -> Path:
    path = Path(str(cfg.get("path") or "")).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Missing source file: {path}")
    expected = str(cfg.get("sha256") or "").strip()
    if expected:
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"sha256 mismatch for {path}: expected {expected} actual {actual}")
    return path


def parse_pay_period_end(value: str) -> str | None:
    s = (value or "").strip()
    if not s:
        return None
    # Examples:
    #   Sun Nov 05 2023 00:00:00 GMT-0300 (Atlantic Daylight Time)
    #   Mon Oct 30 2023 00:00:00 GMT-0300 (Atlantic Daylight Time)
    parts = s.split()
    if len(parts) < 4:
        return None
    head = " ".join(parts[:4])  # "Sun Nov 05 2023"
    try:
        d = datetime.strptime(head, "%a %b %d %Y").date()
    except ValueError:
        return None
    return d.isoformat()


def parse_money_cents(value: str) -> int:
    s = (value or "").strip()
    if not s:
        return 0
    s = s.replace("$", "").replace(",", "").strip()
    if not s:
        return 0
    return dollars_to_cents(s)


def normalize_employee_name(file_stem: str) -> str:
    s = re.sub(r"\s+", " ", (file_stem or "").strip())
    s = re.sub(r"canteen.*$", "", s, flags=re.IGNORECASE).strip()
    # Strip season/year markers commonly present in filenames (e.g. "(24-25)", "2023-24").
    s = re.sub(r"\([^)]*\)", "", s).strip()
    s = re.sub(r"\b20[0-9]{2}\s*-\s*(?:20)?[0-9]{2}\b", "", s).strip()
    s = re.sub(r"\s+", " ", s).strip()
    return s or file_stem


def load_employee_date_overrides(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    data = load_yaml(path)
    raw = data.get("employee_pay_period_date_overrides")
    if not isinstance(raw, dict):
        return {}
    out: dict[str, dict] = {}
    for source_key, cfg in raw.items():
        if not isinstance(cfg, dict):
            continue
        out[str(source_key).strip()] = dict(cfg)
    return out


def parse_pay_period_value(row: dict[str, str]) -> str | None:
    pay_period = (
        (row.get("Pay Period") or "").strip()
        or (row.get("Weekly Pay Period") or "").strip()
        or None
    )
    if not pay_period:
        # Some exports have a numeric header for the first column (example: "4") which contains the period #.
        keys = list(row.keys())
        if keys and str(keys[0]).strip().isdigit():
            pay_period = (row.get(keys[0]) or "").strip() or None
    return pay_period


def as_int(value: str | None) -> int | None:
    s = (value or "").strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def extract_period_pairs(csv_path: Path) -> list[tuple[int, date]]:
    pairs: list[tuple[int, date]] = []
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            period_raw = parse_pay_period_value(row)
            period = as_int(period_raw)
            if period is None:
                continue
            pp_end = parse_pay_period_end(row.get("Pay Period End") or "")
            if not pp_end:
                continue
            pairs.append((period, date.fromisoformat(pp_end)))
    # Deduplicate by choosing the most recent observed date per period within this file.
    dedup: dict[int, date] = {}
    for period, end_date in pairs:
        if period not in dedup or end_date > dedup[period]:
            dedup[period] = end_date
    return sorted(dedup.items(), key=lambda x: x[0])


def infer_days_per_period(pairs: list[tuple[int, date]]) -> int | None:
    if len(pairs) < 3:
        return None
    ratios: list[float] = []
    for (p0, d0), (p1, d1) in zip(pairs, pairs[1:]):
        dp = p1 - p0
        if dp <= 0:
            continue
        dd = (d1 - d0).days
        if dd <= 0:
            continue
        ratios.append(dd / dp)
    if len(ratios) < 2:
        return None
    r = median(ratios)
    # Most of these exports are weekly (7) or biweekly (14).
    if abs(r - 7) <= 1:
        return 7
    if abs(r - 14) <= 1:
        return 14
    return None


@dataclass(frozen=True)
class PayPeriodCalendar:
    base_source_key: str
    folder: Path
    days_per_period: int
    known: dict[int, date]

    def end_date_for_period(self, period_number: int) -> date | None:
        if period_number in self.known:
            return self.known[period_number]
        if not self.known:
            return None
        # Use the closest known period as an anchor for deterministic extrapolation.
        anchor_period = min(self.known.keys(), key=lambda p: (abs(p - period_number), p))
        anchor_date = self.known[anchor_period]
        delta_periods = period_number - anchor_period
        return anchor_date + timedelta(days=self.days_per_period * delta_periods)


def import_employee_payroll_csv(
    conn: sqlite3.Connection,
    *,
    source_key: str,
    employee_name: str,
    source_file_id: int,
    csv_path: Path,
    reset: bool,
    calendar: PayPeriodCalendar | None = None,
    row_overrides: dict[int, dict] | None = None,
) -> EmployeeImportResult:
    if reset:
        conn.execute("DELETE FROM payroll_employee_pay_periods WHERE source_file_id = ?", (source_file_id,))

    rows_upserted = 0
    rows_skipped = 0
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=2):
            override = (row_overrides or {}).get(int(idx))
            if override and override.get("exclude"):
                rows_skipped += 1
                continue

            pay_period = parse_pay_period_value(row)
            pay_period_int = as_int(pay_period)

            pp_end = parse_pay_period_end(row.get("Pay Period End") or "")
            if calendar and pay_period_int is not None:
                cal_end = calendar.end_date_for_period(pay_period_int)
                if cal_end is not None:
                    pp_end = cal_end.isoformat()

            if override and override.get("pay_period_end"):
                pp_end = str(override["pay_period_end"]).strip() or pp_end

            if not pp_end:
                rows_skipped += 1
                continue

            tips_cents = parse_money_cents(row.get("Tips") or "")
            gross_cents = parse_money_cents(row.get("Gross Pay") or "")
            net_pay_cents = parse_money_cents(row.get("Net Pay") or "")
            if gross_cents == 0 and tips_cents == 0 and net_pay_cents == 0:
                rows_skipped += 1
                continue

            if override and override.get("pay_period") is not None:
                pay_period = str(override["pay_period"]).strip() or pay_period

            vacation_cents = parse_money_cents(row.get("Vacation Pay") or "")
            federal_cents = parse_money_cents(row.get("Federal Tax") or "")
            provincial_cents = parse_money_cents(row.get("Provincial Tax") or "")

            employee_cpp_cents = parse_money_cents(row.get("Employee CPP Deductions") or "")
            employer_cpp_cents = parse_money_cents(row.get("Employer CPP Deductions") or "")
            employee_ei_cents = parse_money_cents(row.get("Employee EI Deductions") or "")
            employer_ei_cents = parse_money_cents(row.get("Employer EI Contributions") or "")

            our_remit_cents = parse_money_cents(row.get("Our Remittance") or "")

            conn.execute(
                """
                INSERT INTO payroll_employee_pay_periods (
                  source_file_id, source_row, employee_name, pay_period, pay_period_end,
                  gross_pay_cents, vacation_pay_cents, tips_cents,
                  federal_tax_cents, provincial_tax_cents,
                  employee_cpp_cents, employer_cpp_cents,
                  employee_ei_cents, employer_ei_cents,
                  net_pay_cents, our_remittance_cents
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(source_file_id, source_row) DO UPDATE SET
                  employee_name=excluded.employee_name,
                  pay_period=excluded.pay_period,
                  pay_period_end=excluded.pay_period_end,
                  gross_pay_cents=excluded.gross_pay_cents,
                  vacation_pay_cents=excluded.vacation_pay_cents,
                  tips_cents=excluded.tips_cents,
                  federal_tax_cents=excluded.federal_tax_cents,
                  provincial_tax_cents=excluded.provincial_tax_cents,
                  employee_cpp_cents=excluded.employee_cpp_cents,
                  employer_cpp_cents=excluded.employer_cpp_cents,
                  employee_ei_cents=excluded.employee_ei_cents,
                  employer_ei_cents=excluded.employer_ei_cents,
                  net_pay_cents=excluded.net_pay_cents,
                  our_remittance_cents=excluded.our_remittance_cents
                """,
                (
                    source_file_id,
                    idx,
                    employee_name,
                    pay_period,
                    pp_end,
                    gross_cents,
                    vacation_cents,
                    tips_cents,
                    federal_cents,
                    provincial_cents,
                    employee_cpp_cents,
                    employer_cpp_cents,
                    employee_ei_cents,
                    employer_ei_cents,
                    net_pay_cents,
                    our_remit_cents,
                ),
            )
            rows_upserted += 1

    return EmployeeImportResult(
        source_key=source_key,
        employee_name=employee_name,
        rows_upserted=rows_upserted,
        rows_skipped=rows_skipped,
    )


MONTH_NAME_TO_NUM = {
    "january": 1,
    "janurary": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def infer_year_from_source_key(source_key: str) -> int | None:
    # source keys often contain underscores, which are "word" characters; use a simple match
    # instead of word boundaries so keys like "payroll_monthly_totals_2024_csv" work.
    m = re.search(r"(20[0-9]{2})", source_key)
    if m:
        return int(m.group(1))
    return None


def import_monthly_totals_csv(
    conn: sqlite3.Connection,
    *,
    source_key: str,
    source_file_id: int,
    csv_path: Path,
    year: int,
    reset: bool,
) -> int:
    if reset:
        conn.execute("DELETE FROM payroll_monthly_totals WHERE source_file_id = ?", (source_file_id,))

    inserted = 0
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=2):
            month_raw = (row.get("Month") or "").strip()
            if not month_raw:
                continue
            month_key = month_raw.strip().lower()
            if month_key in ("total", "total q4"):
                continue
            month = MONTH_NAME_TO_NUM.get(month_key)
            if not month:
                continue

            # Support both formats (2024 and 2025 working papers).
            gross = row.get("Gross Payroll") or row.get("Gross_Pay") or ""
            remittance = row.get("Total Remittance") or row.get("Remittance") or ""
            employer_taxes = row.get("Total Employer Taxes") or row.get("Employer Share (EI, CPP)") or ""
            net_pay_plus_tips = row.get("Net Pay + Tips") or ""

            gross_cents = parse_money_cents(gross)
            remittance_cents = parse_money_cents(remittance)
            employer_cents = parse_money_cents(employer_taxes)
            net_plus_tips_cents = parse_money_cents(net_pay_plus_tips)

            conn.execute(
                """
                INSERT INTO payroll_monthly_totals (
                  source_file_id, source_row, year, month,
                  gross_pay_cents, remittance_cents, employer_taxes_cents, net_pay_plus_tips_cents
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(year, month) DO UPDATE SET
                  source_file_id=excluded.source_file_id,
                  source_row=excluded.source_row,
                  gross_pay_cents=excluded.gross_pay_cents,
                  remittance_cents=excluded.remittance_cents,
                  employer_taxes_cents=excluded.employer_taxes_cents,
                  net_pay_plus_tips_cents=excluded.net_pay_plus_tips_cents
                """,
                (
                    source_file_id,
                    idx,
                    year,
                    month,
                    gross_cents,
                    remittance_cents,
                    employer_cents,
                    net_plus_tips_cents,
                ),
            )
            inserted += 1

    return inserted


def load_row_overrides(cfg: dict) -> dict[int, dict]:
    raw = cfg.get("row_overrides")
    if not isinstance(raw, dict):
        return {}
    out: dict[int, dict] = {}
    for k, v in raw.items():
        if not isinstance(v, dict):
            continue
        try:
            idx = int(str(k).strip())
        except ValueError:
            continue
        out[idx] = dict(v)
    return out


def build_pay_period_calendars(
    manifest: dict,
    employee_keys: list[str],
    *,
    date_overrides: dict[str, dict],
    enabled_source_keys: set[str],
) -> tuple[dict[str, PayPeriodCalendar], dict[tuple[str, int], PayPeriodCalendar]]:
    sources = manifest.get("sources") or {}
    if not isinstance(sources, dict):
        return {}, {}

    # Candidate selection: per (folder, days_per_period), pick the source with the latest observed end_date.
    candidates: dict[tuple[str, int], tuple[str, Path, date, dict[int, date]]] = {}
    # Per-source chosen calendar (resolved later).
    source_to_group: dict[str, tuple[str, int]] = {}

    for key in employee_keys:
        cfg = get_source(manifest, key)
        csv_path = verify_source(cfg)
        pairs = extract_period_pairs(csv_path)
        days = infer_days_per_period(pairs)
        if days is None:
            continue
        folder = str(csv_path.parent.resolve())
        group = (folder, days)
        observed: dict[int, date] = {p: d for p, d in pairs}
        max_date = max(observed.values()) if observed else date.min

        # If this source has a row override that explicitly sets a pay period end to something
        # that would otherwise affect inference, it should not influence calendar selection.
        # (We still allow it to use a calendar.)
        _ = date_overrides.get(key, {})

        if group not in candidates:
            candidates[group] = (key, csv_path, max_date, observed)
        else:
            cur_key, _cur_path, cur_max, cur_obs = candidates[group]
            if max_date > cur_max or (max_date == cur_max and len(observed) > len(cur_obs)):
                candidates[group] = (key, csv_path, max_date, observed)
        if key in enabled_source_keys:
            source_to_group[key] = group

    group_calendars: dict[tuple[str, int], PayPeriodCalendar] = {}
    for group, (base_key, base_path, _max_date, observed) in candidates.items():
        folder, days = group
        group_calendars[group] = PayPeriodCalendar(
            base_source_key=base_key,
            folder=Path(folder),
            days_per_period=days,
            known=dict(observed),
        )

    source_calendars: dict[str, PayPeriodCalendar] = {}
    for key, group in source_to_group.items():
        cal = group_calendars.get(group)
        if cal:
            source_calendars[key] = cal

    return source_calendars, group_calendars


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing imported payroll rows for these sources.")
    ap.add_argument("--employee-source-prefix", default="payroll_employee_")
    ap.add_argument("--monthly-source-prefix", default="payroll_monthly_totals_")
    args = ap.parse_args()

    manifest = load_manifest()
    sources = manifest.get("sources") or {}
    if not isinstance(sources, dict):
        raise SystemExit("Invalid manifest structure: sources must be a mapping")

    employee_keys = sorted(k for k in sources.keys() if str(k).startswith(args.employee_source_prefix))
    monthly_keys = sorted(k for k in sources.keys() if str(k).startswith(args.monthly_source_prefix))

    date_overrides_path = PROJECT_ROOT / "overrides" / "payroll_employee_date_overrides.yml"
    date_overrides = load_employee_date_overrides(date_overrides_path)

    conn = connect_db(args.db)
    try:
        with conn:
            enabled_calendar_sources = {
                k
                for k in employee_keys
                if isinstance(date_overrides.get(k, {}), dict)
                and bool(date_overrides.get(k, {}).get("use_pay_period_calendar"))
            }
            source_calendars, _group_calendars = build_pay_period_calendars(
                manifest,
                employee_keys,
                date_overrides=date_overrides,
                enabled_source_keys=enabled_calendar_sources,
            )

            # Employee-level imports
            employee_results: list[EmployeeImportResult] = []
            for key in employee_keys:
                cfg = get_source(manifest, key)
                csv_path = verify_source(cfg)
                source_file_id = ensure_source_file(conn, key, cfg)
                employee_name = normalize_employee_name(csv_path.stem)
                override = date_overrides.get(key, {})
                row_overrides = load_row_overrides(override)
                employee_results.append(
                    import_employee_payroll_csv(
                        conn,
                        source_key=key,
                        employee_name=employee_name,
                        source_file_id=source_file_id,
                        csv_path=csv_path,
                        reset=args.reset,
                        calendar=source_calendars.get(key),
                        row_overrides=row_overrides,
                    )
                )

            # Monthly rollups
            monthly_inserted = 0
            for key in monthly_keys:
                cfg = get_source(manifest, key)
                csv_path = verify_source(cfg)
                source_file_id = ensure_source_file(conn, key, cfg)
                year = infer_year_from_source_key(key)
                if not year:
                    raise SystemExit(f"Could not infer year from source key: {key}")
                monthly_inserted += import_monthly_totals_csv(
                    conn,
                    source_key=key,
                    source_file_id=source_file_id,
                    csv_path=csv_path,
                    year=year,
                    reset=args.reset,
                )

    finally:
        conn.close()

    print("PAYROLL EXPORT IMPORT COMPLETE")
    print(f"- db: {args.db}")
    print(f"- employee_sources: {len(employee_keys)}")
    print(f"- monthly_sources: {len(monthly_keys)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
