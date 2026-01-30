#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    connect_db,
    fiscal_years_from_manifest,
    get_source,
    load_manifest,
    sha256_file,
)


MEALS_EXPENSE_ACCOUNT_CODE = "7110"
THOMAS_PAYABLE_ACCOUNT_CODE = "2400"
DWAYNE_PAYABLE_ACCOUNT_CODE = "2410"


@dataclass(frozen=True)
class MealsEstimate:
    moncton_trips: int
    meals_cents: int


def cents_to_dollars(cents: int) -> str:
    return f"{Decimal(cents) / Decimal(100):.2f}"


def read_moncton_trips(path: Path, *, start_date: str, end_date: str) -> int:
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    trips = 0
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = date.fromisoformat((row.get("date") or "").strip())
            if d < start or d > end:
                continue
            desc = (row.get("description") or "").strip().lower()
            if "moncton" in desc:
                trips += 1
    return trips


def upsert_meals_journal_entry(
    conn: sqlite3.Connection,
    *,
    fy: str,
    fy_end_date: str,
    per_trip_cents: int,
    thomas: MealsEstimate,
    dwayne: MealsEstimate,
) -> None:
    total_cents = thomas.meals_cents + dwayne.meals_cents
    if total_cents == 0:
        return

    je_id = f"MEALS_MONCTON_ESTIMATE_{fy}"
    entry_number = f"MEALS-MONCTON-{fy}"
    desc = f"Estimated meals & entertainment (${cents_to_dollars(per_trip_cents)}/Moncton trip; no receipts) {fy}"
    notes = f"per_trip_cents={per_trip_cents}; thomas_trips={thomas.moncton_trips}; dwayne_trips={dwayne.moncton_trips}; addback_policy=50pct"

    conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
    conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

    conn.execute(
        """
        INSERT INTO journal_entries (
          id, entry_number, entry_date, entry_type, description,
          source_system, source_record_type, source_record_id, notes,
          is_posted
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
        """,
        (
            je_id,
            entry_number,
            fy_end_date,
            "ESTIMATE",
            desc,
            "t2-final",
            "meals_estimate",
            fy,
            notes,
        ),
    )

    lines: list[tuple[str, int, str, int, int, str]] = []
    line_number = 1
    lines.append(
        (
            f"{je_id}:{line_number}",
            line_number,
            MEALS_EXPENSE_ACCOUNT_CODE,
            total_cents,
            0,
            f"Meals & entertainment estimate from Moncton trips {fy}",
        )
    )
    line_number += 1

    if thomas.meals_cents:
        lines.append(
            (
                f"{je_id}:{line_number}",
                line_number,
                THOMAS_PAYABLE_ACCOUNT_CODE,
                0,
                thomas.meals_cents,
                f"Due to shareholder - Thomas (meals estimate) {fy}",
            )
        )
        line_number += 1

    if dwayne.meals_cents:
        lines.append(
            (
                f"{je_id}:{line_number}",
                line_number,
                DWAYNE_PAYABLE_ACCOUNT_CODE,
                0,
                dwayne.meals_cents,
                f"Due to shareholder - Dwayne (meals estimate) {fy}",
            )
        )

    conn.executemany(
        """
        INSERT INTO journal_entry_lines (
          id, journal_entry_id, line_number, account_code,
          debit_cents, credit_cents, description
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [(id_, je_id, ln, acct, dr, cr, d) for (id_, ln, acct, dr, cr, d) in lines],
    )


def write_payables_csv(
    out_csv: Path,
    *,
    fy: str,
    start_date: str,
    end_date: str,
    per_trip_cents: int,
    thomas: MealsEstimate,
    dwayne: MealsEstimate,
) -> None:
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "fy",
                "start_date",
                "end_date",
                "shareholder",
                "moncton_trips",
                "per_trip_cents",
                "meals_cents",
            ],
        )
        w.writeheader()
        for shareholder, est in [("Thomas", thomas), ("Dwayne", dwayne)]:
            w.writerow(
                {
                    "fy": fy,
                    "start_date": start_date,
                    "end_date": end_date,
                    "shareholder": shareholder,
                    "moncton_trips": est.moncton_trips,
                    "per_trip_cents": per_trip_cents,
                    "meals_cents": est.meals_cents,
                }
            )


def write_journal_csv(
    out_csv: Path,
    *,
    fy: str,
    fy_end_date: str,
    thomas: MealsEstimate,
    dwayne: MealsEstimate,
) -> None:
    rows: list[dict[str, str]] = []
    total_cents = thomas.meals_cents + dwayne.meals_cents
    ref = f"MEALS-MONCTON-EST-{fy}"

    rows.append(
        {
            "Date": fy_end_date,
            "Account": MEALS_EXPENSE_ACCOUNT_CODE,
            "Debit": cents_to_dollars(total_cents) if total_cents else "",
            "Credit": "",
            "Description": f"Meals & entertainment estimate (Moncton trips) {fy}",
            "Reference": ref,
        }
    )
    if thomas.meals_cents:
        rows.append(
            {
                "Date": fy_end_date,
                "Account": THOMAS_PAYABLE_ACCOUNT_CODE,
                "Debit": "",
                "Credit": cents_to_dollars(thomas.meals_cents),
                "Description": f"Due to shareholder - Thomas (meals estimate) {fy}",
                "Reference": ref,
            }
        )
    if dwayne.meals_cents:
        rows.append(
            {
                "Date": fy_end_date,
                "Account": DWAYNE_PAYABLE_ACCOUNT_CODE,
                "Debit": "",
                "Credit": cents_to_dollars(dwayne.meals_cents),
                "Description": f"Due to shareholder - Dwayne (meals estimate) {fy}",
                "Reference": ref,
            }
        )

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["Date", "Account", "Debit", "Credit", "Description", "Reference"],
        )
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_summary_md(
    out_md: Path,
    *,
    per_trip_cents: int,
    fy_rows: list[tuple[str, str, str, MealsEstimate, MealsEstimate]],
    thomas_log: Path,
    dwayne_log: Path,
) -> None:
    per_trip = cents_to_dollars(per_trip_cents)
    lines: list[str] = []
    lines.append("# Shareholder meals estimate (Moncton trips)")
    lines.append("")
    lines.append("Assumptions:")
    lines.append(f"- ${per_trip} per Moncton trip (from mileage logs)")
    lines.append("- No supporting receipts currently (estimate only)")
    lines.append("- Tax treatment: meals & entertainment add-back = 50% of expense")
    lines.append("")
    lines.append("Sources:")
    lines.append(f"- Mileage logs: `{thomas_log}` and `{dwayne_log}`")
    lines.append("")

    for fy, start_date, end_date, thomas, dwayne in fy_rows:
        total_cents = thomas.meals_cents + dwayne.meals_cents
        addback_cents = total_cents // 2
        lines.append(f"## {fy} ({start_date} → {end_date})")
        lines.append("")
        lines.append(f"- Thomas Moncton trips: {thomas.moncton_trips} → ${cents_to_dollars(thomas.meals_cents)}")
        lines.append(f"- Dwayne Moncton trips: {dwayne.moncton_trips} → ${cents_to_dollars(dwayne.meals_cents)}")
        lines.append(f"- Total meals estimate: ${cents_to_dollars(total_cents)}")
        lines.append(f"- Add-back (50%): ${cents_to_dollars(addback_cents)}")
        lines.append("")

    lines.append("## Outputs")
    lines.append("")
    lines.append("- Year-end journal CSVs: `output/shareholder_meals_estimate_journal_FY2024.csv`, `output/shareholder_meals_estimate_journal_FY2025.csv`")
    lines.append("- Payables detail CSVs: `output/shareholder_meals_estimate_payables_FY2024.csv`, `output/shareholder_meals_estimate_payables_FY2025.csv`")
    lines.append("")
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--per-moncton-trip", type=Decimal, default=Decimal("15.00"))
    ap.add_argument("--thomas-log-source-key", default="curlys_books_thomas_mileage_log_csv")
    ap.add_argument("--dwayne-log-source-key", default="curlys_books_dwayne_mileage_log_csv")
    args = ap.parse_args()

    per_trip_cents = int((args.per_moncton_trip * 100).quantize(Decimal("1")))
    if per_trip_cents <= 0:
        raise SystemExit("--per-moncton-trip must be > 0")

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    thomas_src = get_source(manifest, args.thomas_log_source_key)
    dwayne_src = get_source(manifest, args.dwayne_log_source_key)
    thomas_log = Path(str(thomas_src.get("path") or "")).expanduser()
    dwayne_log = Path(str(dwayne_src.get("path") or "")).expanduser()

    for src, path in [(thomas_src, thomas_log), (dwayne_src, dwayne_log)]:
        if not path.exists():
            raise FileNotFoundError(f"Missing mileage log: {path}")
        expected = str(src.get("sha256") or "").strip()
        if expected:
            actual = sha256_file(path)
            if actual != expected:
                raise SystemExit(f"sha256 mismatch for {path}: expected {expected} actual {actual}")

    args.out_dir.mkdir(parents=True, exist_ok=True)

    fy_rows: list[tuple[str, str, str, MealsEstimate, MealsEstimate]] = []
    for fy in fys:
        thomas_trips = read_moncton_trips(thomas_log, start_date=fy.start_date, end_date=fy.end_date)
        dwayne_trips = read_moncton_trips(dwayne_log, start_date=fy.start_date, end_date=fy.end_date)
        thomas = MealsEstimate(moncton_trips=thomas_trips, meals_cents=thomas_trips * per_trip_cents)
        dwayne = MealsEstimate(moncton_trips=dwayne_trips, meals_cents=dwayne_trips * per_trip_cents)
        fy_rows.append((fy.fy, fy.start_date, fy.end_date, thomas, dwayne))

    conn = connect_db(args.db)
    try:
        with conn:
            for fy, _start, _end, thomas, dwayne in fy_rows:
                fy_end_date = next(f.end_date for f in fys if f.fy == fy)
                upsert_meals_journal_entry(
                    conn,
                    fy=fy,
                    fy_end_date=fy_end_date,
                    per_trip_cents=per_trip_cents,
                    thomas=thomas,
                    dwayne=dwayne,
                )
    finally:
        conn.close()

    for fy, start_date, end_date, thomas, dwayne in fy_rows:
        out_payables_csv = args.out_dir / f"shareholder_meals_estimate_payables_{fy}.csv"
        write_payables_csv(
            out_payables_csv,
            fy=fy,
            start_date=start_date,
            end_date=end_date,
            per_trip_cents=per_trip_cents,
            thomas=thomas,
            dwayne=dwayne,
        )

        out_journal_csv = args.out_dir / f"shareholder_meals_estimate_journal_{fy}.csv"
        write_journal_csv(
            out_journal_csv,
            fy=fy,
            fy_end_date=end_date,
            thomas=thomas,
            dwayne=dwayne,
        )

    out_md = args.out_dir / "shareholder_meals_estimate_summary.md"
    write_summary_md(
        out_md,
        per_trip_cents=per_trip_cents,
        fy_rows=fy_rows,
        thomas_log=thomas_log,
        dwayne_log=dwayne_log,
    )

    print("SHAREHOLDER MEALS ESTIMATE BUILT")
    print(f"- out_dir: {args.out_dir}")
    print(f"- per_trip: ${cents_to_dollars(per_trip_cents)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
