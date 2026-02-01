#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, get_source, load_manifest, load_yaml, sha256_file


FUEL_ACCOUNT_CODE = "9200"
MILEAGE_EXPENSE_ACCOUNT_CODE = "9270"
THOMAS_PAYABLE_ACCOUNT_CODE = "2400"
DWAYNE_PAYABLE_ACCOUNT_CODE = "2410"
DUE_FROM_SHAREHOLDER_ACCOUNT_CODE = "2500"
MILEAGE_ADJUSTMENTS_PATH = PROJECT_ROOT / "overrides" / "mileage_adjustments.yml"


@dataclass(frozen=True)
class FyTotals:
    trips: int = 0
    kilometres: Decimal = Decimal("0")
    mileage_claim_cents: int = 0


def cents_to_dollars(cents: int) -> str:
    return f"{Decimal(cents) / Decimal(100):.2f}"

def load_mileage_adjustments() -> dict[str, dict[str, object]]:
    """
    Load FY-scoped mileage adjustments (overlay) from overrides/.

    We keep this separate from the base mileage logs so the filing can:
    - remain reproducible/deterministic, and
    - explicitly scope one-off add-ons to a specific fiscal year (e.g., FY2024 only).
    """
    if not MILEAGE_ADJUSTMENTS_PATH.exists():
        return {}
    data = load_yaml(MILEAGE_ADJUSTMENTS_PATH)
    adj = data.get("adjustments")
    if not isinstance(adj, dict):
        return {}
    out: dict[str, dict[str, object]] = {}
    for fy, obj in adj.items():
        if not isinstance(fy, str) or not isinstance(obj, dict):
            continue
        out[fy.strip()] = obj
    return out

def thomas_additional_mileage_claim_cents(fy: str, adjustments: dict[str, dict[str, object]]) -> int:
    obj = adjustments.get(fy, {})
    raw = obj.get("thomas_additional_mileage_claim_cents", 0)
    try:
        return int(raw or 0)
    except Exception:
        return 0

def thomas_adjustment_note(fy: str, adjustments: dict[str, dict[str, object]]) -> str:
    obj = adjustments.get(fy, {})
    note = obj.get("note")
    return str(note).strip() if note is not None else ""


def read_mileage_log(path: Path, *, start_date: str, end_date: str) -> FyTotals:
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    trips = 0
    km = Decimal("0")
    claim_cents = 0
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = date.fromisoformat((row.get("date") or "").strip())
            if d < start or d > end:
                continue
            trips += 1
            km += Decimal(str(row.get("kilometres") or "0").strip() or "0")
            claim = (row.get("mileage_claim") or "").strip()
            if not claim:
                continue
            claim_cents += int((Decimal(claim) * 100).quantize(Decimal("1")))
    return FyTotals(trips=trips, kilometres=km, mileage_claim_cents=claim_cents)


def fuel_total_cents(conn: sqlite3.Connection, *, start_date: str, end_date: str) -> int:
    row = conn.execute(
        """
        SELECT SUM(ba.amount_cents) AS s
        FROM bill_allocations ba
        JOIN wave_bills wb ON wb.id = ba.wave_bill_id
        WHERE ba.account_code = ?
          AND wb.invoice_date >= ? AND wb.invoice_date <= ?
        """,
        (FUEL_ACCOUNT_CODE, start_date, end_date),
    ).fetchone()
    return int(row["s"] or 0)


def export_fuel_bills(conn: sqlite3.Connection, *, start_date: str, end_date: str, out_csv: Path) -> None:
    rows = conn.execute(
        """
        SELECT
          wb.id AS wave_bill_id,
          wb.invoice_date,
          wb.vendor_raw,
          wb.vendor_norm,
          wb.invoice_number,
          ba.amount_cents,
          ba.method,
          ba.notes
        FROM bill_allocations ba
        JOIN wave_bills wb ON wb.id = ba.wave_bill_id
        WHERE ba.account_code = ?
          AND wb.invoice_date >= ? AND wb.invoice_date <= ?
        ORDER BY wb.invoice_date, wb.id
        """,
        (FUEL_ACCOUNT_CODE, start_date, end_date),
    ).fetchall()

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "wave_bill_id",
                "invoice_date",
                "vendor_raw",
                "vendor_norm",
                "invoice_number",
                "fuel_cents",
                "method",
                "notes",
            ]
        )
        for r in rows:
            w.writerow(
                [
                    r["wave_bill_id"],
                    r["invoice_date"],
                    r["vendor_raw"],
                    r["vendor_norm"],
                    r["invoice_number"],
                    r["amount_cents"],
                    r["method"],
                    r["notes"],
                ]
            )


def write_payables_csv(
    out_csv: Path,
    *,
    fy: str,
    start_date: str,
    end_date: str,
    thomas: FyTotals,
    dwayne: FyTotals,
    fuel_cents: int,
) -> None:
    thomas_net_cents = thomas.mileage_claim_cents - fuel_cents
    dwayne_net_cents = dwayne.mileage_claim_cents

    rows = [
        {
            "fy": fy,
            "start_date": start_date,
            "end_date": end_date,
            "shareholder": "Thomas",
            "trips": thomas.trips,
            "kilometres": f"{thomas.kilometres:.2f}",
            "mileage_claim_cents": thomas.mileage_claim_cents,
            "fuel_cents": fuel_cents,
            "net_cents": thomas_net_cents,
            "direction": "DUE_TO_SHAREHOLDER" if thomas_net_cents >= 0 else "DUE_FROM_SHAREHOLDER",
        },
        {
            "fy": fy,
            "start_date": start_date,
            "end_date": end_date,
            "shareholder": "Dwayne",
            "trips": dwayne.trips,
            "kilometres": f"{dwayne.kilometres:.2f}",
            "mileage_claim_cents": dwayne.mileage_claim_cents,
            "fuel_cents": 0,
            "net_cents": dwayne_net_cents,
            "direction": "DUE_TO_SHAREHOLDER" if dwayne_net_cents >= 0 else "DUE_FROM_SHAREHOLDER",
        },
    ]

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "fy",
                "start_date",
                "end_date",
                "shareholder",
                "trips",
                "kilometres",
                "mileage_claim_cents",
                "fuel_cents",
                "net_cents",
                "direction",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_journal_csv(
    out_csv: Path,
    *,
    fy: str,
    fy_end_date: str,
    thomas_mileage_cents: int,
    dwayne_mileage_cents: int,
    fuel_cents: int,
) -> None:
    rows: list[dict[str, str]] = []

    # Thomas: convert fuel suspense to mileage expense + net to/from shareholder.
    # Fuel is assumed paid by Thomas personally (hence netting against his payable).
    thomas_net_cents = thomas_mileage_cents - fuel_cents
    ref = f"MIL-FUEL-THOMAS-{fy}"
    rows.append(
        {
            "Date": fy_end_date,
            "Account": MILEAGE_EXPENSE_ACCOUNT_CODE,
            "Debit": cents_to_dollars(thomas_mileage_cents) if thomas_mileage_cents else "",
            "Credit": "",
            "Description": f"Motor vehicle expense - mileage reimbursement (Thomas) {fy}",
            "Reference": ref,
        }
    )
    rows.append(
        {
            "Date": fy_end_date,
            "Account": FUEL_ACCOUNT_CODE,
            "Debit": "",
            "Credit": cents_to_dollars(fuel_cents) if fuel_cents else "",
            "Description": f"Clear fuel pending mileage conversion (Thomas-paid fuel) {fy}",
            "Reference": ref,
        }
    )
    if thomas_net_cents >= 0:
        rows.append(
            {
                "Date": fy_end_date,
                "Account": THOMAS_PAYABLE_ACCOUNT_CODE,
                "Debit": "",
                "Credit": cents_to_dollars(thomas_net_cents) if thomas_net_cents else "",
                "Description": f"Net due to shareholder - Thomas (mileage - fuel) {fy}",
                "Reference": ref,
            }
        )
    else:
        rows.append(
            {
                "Date": fy_end_date,
                "Account": DUE_FROM_SHAREHOLDER_ACCOUNT_CODE,
                "Debit": cents_to_dollars(-thomas_net_cents),
                "Credit": "",
                "Description": f"Net due from shareholder - Thomas (fuel exceeds mileage) {fy}",
                "Reference": ref,
            }
        )

    # Separator row (Wave import friendliness)
    rows.append({k: "" for k in rows[0].keys()})

    # Dwayne: mileage reimbursement only (no fuel netting).
    ref = f"MIL-DWAYNE-{fy}"
    rows.append(
        {
            "Date": fy_end_date,
            "Account": MILEAGE_EXPENSE_ACCOUNT_CODE,
            "Debit": cents_to_dollars(dwayne_mileage_cents) if dwayne_mileage_cents else "",
            "Credit": "",
            "Description": f"Motor vehicle expense - mileage reimbursement (Dwayne) {fy}",
            "Reference": ref,
        }
    )
    rows.append(
        {
            "Date": fy_end_date,
            "Account": DWAYNE_PAYABLE_ACCOUNT_CODE,
            "Debit": "",
            "Credit": cents_to_dollars(dwayne_mileage_cents) if dwayne_mileage_cents else "",
            "Description": f"Due to shareholder - Dwayne mileage reimbursement {fy}",
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


def upsert_mileage_fuel_journal_entry(
    conn: sqlite3.Connection,
    *,
    fy: str,
    fy_end_date: str,
    thomas_mileage_cents: int,
    thomas_base_mileage_cents: int,
    thomas_adjustment_cents: int,
    dwayne_mileage_cents: int,
    fuel_cents: int,
    thomas_log: Path,
    dwayne_log: Path,
) -> None:
    if not (thomas_mileage_cents or dwayne_mileage_cents or fuel_cents):
        return

    je_id = f"MILEAGE_FUEL_REIMBURSEMENT_{fy}"
    entry_number = f"MIL-FUEL-{fy}"
    desc = f"Shareholder mileage reimbursement (net of Thomas-paid fuel) {fy}"
    notes = (
        f"thomas_log={thomas_log}; dwayne_log={dwayne_log}; "
        f"fuel_account_code={FUEL_ACCOUNT_CODE}; fuel_assumed_thomas_only=true; "
        f"thomas_mileage_base_cents={thomas_base_mileage_cents}; thomas_mileage_adjustment_cents={thomas_adjustment_cents}; "
        f"thomas_mileage_cents={thomas_mileage_cents}; dwayne_mileage_cents={dwayne_mileage_cents}; fuel_cents={fuel_cents}; "
        f"mileage_adjustments={MILEAGE_ADJUSTMENTS_PATH.relative_to(PROJECT_ROOT) if MILEAGE_ADJUSTMENTS_PATH.exists() else '(none)'}"
    )

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
            "ADJUSTMENT",
            desc,
            "t2-final",
            "mileage_fuel_payables",
            fy,
            notes,
        ),
    )

    thomas_net_cents = thomas_mileage_cents - fuel_cents

    lines: list[tuple[str, int, str, int, int, str]] = []
    line_number = 1

    # Expenses (debits)
    if thomas_mileage_cents:
        lines.append(
            (
                f"{je_id}:{line_number}",
                line_number,
                MILEAGE_EXPENSE_ACCOUNT_CODE,
                thomas_mileage_cents,
                0,
                f"Motor vehicle expense - mileage reimbursement (Thomas) {fy}",
            )
        )
        line_number += 1

    if dwayne_mileage_cents:
        lines.append(
            (
                f"{je_id}:{line_number}",
                line_number,
                MILEAGE_EXPENSE_ACCOUNT_CODE,
                dwayne_mileage_cents,
                0,
                f"Motor vehicle expense - mileage reimbursement (Dwayne) {fy}",
            )
        )
        line_number += 1

    # Clear fuel pending conversion (credit)
    if fuel_cents:
        lines.append(
            (
                f"{je_id}:{line_number}",
                line_number,
                FUEL_ACCOUNT_CODE,
                0,
                fuel_cents,
                f"Clear fuel pending mileage conversion (Thomas-paid fuel) {fy}",
            )
        )
        line_number += 1

    # Balance sheet offsets
    if thomas_net_cents >= 0:
        if thomas_net_cents:
            lines.append(
                (
                    f"{je_id}:{line_number}",
                    line_number,
                    THOMAS_PAYABLE_ACCOUNT_CODE,
                    0,
                    thomas_net_cents,
                    f"Net due to shareholder - Thomas (mileage - fuel) {fy}",
                )
            )
            line_number += 1
    else:
        lines.append(
            (
                f"{je_id}:{line_number}",
                line_number,
                DUE_FROM_SHAREHOLDER_ACCOUNT_CODE,
                -thomas_net_cents,
                0,
                f"Net due from shareholder - Thomas (fuel exceeds mileage) {fy}",
            )
        )
        line_number += 1

    if dwayne_mileage_cents:
        lines.append(
            (
                f"{je_id}:{line_number}",
                line_number,
                DWAYNE_PAYABLE_ACCOUNT_CODE,
                0,
                dwayne_mileage_cents,
                f"Due to shareholder - Dwayne mileage reimbursement {fy}",
            )
        )

    debit_total = sum(dr for _id, _ln, _acct, dr, _cr, _d in lines)
    credit_total = sum(cr for _id, _ln, _acct, _dr, cr, _d in lines)
    if debit_total != credit_total:
        raise SystemExit(f"Unbalanced mileage/fuel journal for {fy}: debits={debit_total} credits={credit_total}")

    conn.executemany(
        """
        INSERT INTO journal_entry_lines (
          id, journal_entry_id, line_number, account_code,
          debit_cents, credit_cents, description
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [(id_, je_id, ln, acct, dr, cr, d) for (id_, ln, acct, dr, cr, d) in lines],
    )


def write_summary_md(
    out_md: Path,
    *,
    fy_rows: list[tuple[str, str, str, FyTotals, FyTotals, int]],
    fuel_detail_csv: Path,
    thomas_log: Path,
    dwayne_log: Path,
    mileage_adjust_audit_csv: Path,
) -> None:
    lines: list[str] = []
    lines.append("# Shareholder mileage reimbursement (net of fuel)")
    lines.append("")
    lines.append("This report uses:")
    lines.append(f"- Mileage logs: `{thomas_log}` and `{dwayne_log}`")
    lines.append(f"- Fuel total: account `{FUEL_ACCOUNT_CODE}` from `db/t2_final.db` allocations (see `{fuel_detail_csv}`)")
    lines.append(f"- Mileage adjustments overlay: `{mileage_adjust_audit_csv}` (FY-scoped add-ons)")
    lines.append("")

    total_due_to_thomas_cents = 0
    total_due_from_thomas_cents = 0
    total_due_to_dwayne_cents = 0

    for fy, start_date, end_date, thomas, dwayne, fuel_cents in fy_rows:
        thomas_net = thomas.mileage_claim_cents - fuel_cents
        dwayne_net = dwayne.mileage_claim_cents

        lines.append(f"## {fy} ({start_date} → {end_date})")
        lines.append("")
        lines.append(f"- Thomas mileage: ${cents_to_dollars(thomas.mileage_claim_cents)}")
        lines.append(f"- Thomas fuel (9200): ${cents_to_dollars(fuel_cents)}")
        if thomas_net >= 0:
            lines.append(f"- Thomas net: ${cents_to_dollars(thomas_net)} due to Thomas")
            total_due_to_thomas_cents += thomas_net
        else:
            lines.append(f"- Thomas net: ${cents_to_dollars(-thomas_net)} due from Thomas")
            total_due_from_thomas_cents += -thomas_net
        lines.append("")
        lines.append(f"- Dwayne mileage: ${cents_to_dollars(dwayne.mileage_claim_cents)} due to Dwayne")
        lines.append("")

        total_due_to_dwayne_cents += dwayne_net

    lines.append("## Totals (FY2024 + FY2025)")
    lines.append("")
    if total_due_to_thomas_cents:
        lines.append(f"- Thomas due to: ${cents_to_dollars(total_due_to_thomas_cents)}")
    if total_due_from_thomas_cents:
        lines.append(f"- Thomas due from: ${cents_to_dollars(total_due_from_thomas_cents)}")
    lines.append(f"- Dwayne due to: ${cents_to_dollars(total_due_to_dwayne_cents)}")
    lines.append("")
    lines.append("## Outputs")
    lines.append("")
    lines.append(f"- Fuel detail: `{fuel_detail_csv}`")
    lines.append("- Year-end journal CSVs: `output/shareholder_mileage_fuel_journal_FY2024.csv`, `output/shareholder_mileage_fuel_journal_FY2025.csv`")
    lines.append("")

    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--thomas-log-source-key", default="curlys_books_thomas_mileage_log_csv")
    ap.add_argument("--dwayne-log-source-key", default="curlys_books_dwayne_mileage_log_csv")
    args = ap.parse_args()

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

    adjustments = load_mileage_adjustments()

    conn = connect_db(args.db)
    try:
        fy_rows: list[tuple[str, str, str, FyTotals, FyTotals, int]] = []
        with conn:
            for fy in fys:
                thomas = read_mileage_log(thomas_log, start_date=fy.start_date, end_date=fy.end_date)
                dwayne = read_mileage_log(dwayne_log, start_date=fy.start_date, end_date=fy.end_date)
                fuel_cents = fuel_total_cents(conn, start_date=fy.start_date, end_date=fy.end_date)
                thomas_base_cents = thomas.mileage_claim_cents
                thomas_adj_cents = thomas_additional_mileage_claim_cents(fy.fy, adjustments)
                if thomas_adj_cents:
                    # Keep km/trip counts from the base log; the add-on is a working-paper overlay on the claim dollars.
                    thomas = FyTotals(trips=thomas.trips, kilometres=thomas.kilometres, mileage_claim_cents=thomas_base_cents + thomas_adj_cents)
                fy_rows.append((fy.fy, fy.start_date, fy.end_date, thomas, dwayne, fuel_cents))

                out_payables_csv = args.out_dir / f"shareholder_mileage_fuel_payables_{fy.fy}.csv"
                write_payables_csv(
                    out_payables_csv,
                    fy=fy.fy,
                    start_date=fy.start_date,
                    end_date=fy.end_date,
                    thomas=thomas,
                    dwayne=dwayne,
                    fuel_cents=fuel_cents,
                )

                out_journal_csv = args.out_dir / f"shareholder_mileage_fuel_journal_{fy.fy}.csv"
                write_journal_csv(
                    out_journal_csv,
                    fy=fy.fy,
                    fy_end_date=fy.end_date,
                    thomas_mileage_cents=thomas.mileage_claim_cents,
                    dwayne_mileage_cents=dwayne.mileage_claim_cents,
                    fuel_cents=fuel_cents,
                )

                upsert_mileage_fuel_journal_entry(
                    conn,
                    fy=fy.fy,
                    fy_end_date=fy.end_date,
                    thomas_mileage_cents=thomas.mileage_claim_cents,
                    thomas_base_mileage_cents=thomas_base_cents,
                    thomas_adjustment_cents=thomas_adj_cents,
                    dwayne_mileage_cents=dwayne.mileage_claim_cents,
                    fuel_cents=fuel_cents,
                    thomas_log=thomas_log,
                    dwayne_log=dwayne_log,
                )

        # Fuel audit extract for the whole scope (all FYs combined)
        scope_start = min(f.start_date for f in fys)
        scope_end = max(f.end_date for f in fys)
        out_fuel_csv = args.out_dir / "fuel_9200_wave_bills.csv"
        export_fuel_bills(conn, start_date=scope_start, end_date=scope_end, out_csv=out_fuel_csv)

        # Audit trail of mileage overlays (explicit, FY-scoped).
        out_adj_csv = args.out_dir / "mileage_adjustment_audit.csv"
        out_adj_md = args.out_dir / "mileage_adjustment_summary.md"
        with out_adj_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "fy",
                    "shareholder",
                    "base_mileage_claim_cents",
                    "adjustment_cents",
                    "adjusted_mileage_claim_cents",
                    "note",
                ]
            )
            for fy_key, _start_date, _end_date, thomas, _dwayne, _fuel_cents in fy_rows:
                base = read_mileage_log(thomas_log, start_date=_start_date, end_date=_end_date).mileage_claim_cents
                adj = thomas_additional_mileage_claim_cents(fy_key, adjustments)
                note = thomas_adjustment_note(fy_key, adjustments)
                w.writerow([fy_key, "Thomas", base, adj, base + adj, note])

        md_lines: list[str] = []
        md_lines.append("# Mileage adjustments (overlay audit)")
        md_lines.append("")
        md_lines.append("This file documents explicit FY-scoped overlays applied to mileage claims.")
        md_lines.append("These are working-paper support items and should not be pasted into financial statement notes.")
        md_lines.append("")
        md_lines.append(f"Source: `{MILEAGE_ADJUSTMENTS_PATH.relative_to(PROJECT_ROOT)}`")
        md_lines.append("")
        md_lines.append("## Thomas mileage claim overlays")
        md_lines.append("")
        # Re-read audit CSV for a stable presentation.
        md_lines.append("| FY | Base claim | Adjustment | Final claim | Note |")
        md_lines.append("|---|---:|---:|---:|---|")
        with out_adj_csv.open("r", encoding="utf-8", newline="") as f:
            rr = csv.DictReader(f)
            for r in rr:
                if (r.get("shareholder") or "") != "Thomas":
                    continue
                fy_key = r.get("fy") or ""
                base = cents_to_dollars(int(r.get("base_mileage_claim_cents") or 0))
                adj = cents_to_dollars(int(r.get("adjustment_cents") or 0))
                total = cents_to_dollars(int(r.get("adjusted_mileage_claim_cents") or 0))
                note = (r.get("note") or "").strip()
                md_lines.append(f"| {fy_key} | ${base} | ${adj} | ${total} | {note} |")
        md_lines.append("")
        out_adj_md.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

        out_md = args.out_dir / "shareholder_mileage_fuel_summary.md"
        write_summary_md(
            out_md,
            fy_rows=fy_rows,
            fuel_detail_csv=out_fuel_csv,
            thomas_log=thomas_log,
            dwayne_log=dwayne_log,
            mileage_adjust_audit_csv=out_adj_csv,
        )

    finally:
        conn.close()

    print("SHAREHOLDER MILEAGE PAYABLES BUILT")
    print(f"- out_dir: {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
