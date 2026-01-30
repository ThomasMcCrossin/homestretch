#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    connect_db,
    fiscal_years_from_manifest,
    get_source,
    load_manifest,
    load_rules,
    sha256_file,
)


METHOD_ALLOC = "FRESHER_CATEGORIES_ALLOC"
METHOD_TAX_ITC = "FRESHER_CATEGORIES_TAX_ITC"


@dataclass(frozen=True)
class AllocRow:
    wave_bill_id: int
    invoice_date: str
    wave_account: str
    account_code: str
    amount_cents: int
    match_methods: str
    sources: str


@dataclass(frozen=True)
class BillInfo:
    id: int
    invoice_date: str
    vendor_raw: str
    vendor_category: str | None
    invoice_number: str | None
    total_cents: int
    tax_cents: int
    net_cents: int


@dataclass(frozen=True)
class ImportStats:
    csv_rows_read: int = 0
    csv_distinct_bills: int = 0
    bills_skipped_out_of_scope: int = 0
    bills_missing_in_db: int = 0
    bills_skipped_already_allocated: int = 0
    bills_skipped_allocation_mismatch: int = 0
    bills_skipped_missing_account_code: int = 0
    bills_imported: int = 0
    allocation_rows_inserted: int = 0
    tax_itc_rows_inserted: int = 0


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
    conn.commit()
    row = conn.execute("SELECT id FROM source_files WHERE source_key = ?", (source_key,)).fetchone()
    return int(row["id"])


def read_allocations_csv(path: Path) -> tuple[list[AllocRow], dict[int, int], dict[int, str]]:
    rows: list[AllocRow] = []
    sums: dict[int, int] = {}
    invoice_dates: dict[int, str] = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            wave_bill_id_raw = (r.get("wave_bill_id") or "").strip()
            if not wave_bill_id_raw:
                continue
            try:
                wave_bill_id = int(wave_bill_id_raw)
            except ValueError:
                continue

            account_code = (r.get("account_code") or "").strip()
            amount_raw = (r.get("amount_cents") or "").strip()
            try:
                amount_cents = int(amount_raw)
            except ValueError:
                continue

            invoice_date = (r.get("invoice_date") or "").strip()

            row = AllocRow(
                wave_bill_id=wave_bill_id,
                invoice_date=invoice_date,
                wave_account=(r.get("wave_account") or "").strip(),
                account_code=account_code,
                amount_cents=amount_cents,
                match_methods=(r.get("match_methods") or "").strip(),
                sources=(r.get("sources") or "").strip(),
            )
            rows.append(row)
            sums[wave_bill_id] = sums.get(wave_bill_id, 0) + amount_cents
            if wave_bill_id not in invoice_dates and invoice_date:
                invoice_dates[wave_bill_id] = invoice_date
    return rows, sums, invoice_dates


def load_bill_info(conn: sqlite3.Connection, bill_ids: list[int]) -> dict[int, BillInfo]:
    if not bill_ids:
        return {}
    out: dict[int, BillInfo] = {}
    chunk = 500
    for i in range(0, len(bill_ids), chunk):
        sub = bill_ids[i : i + chunk]
        placeholders = ",".join(["?"] * len(sub))
        rows = conn.execute(
            f"""
            SELECT id, invoice_date, vendor_raw, vendor_category, invoice_number,
                   total_cents, tax_cents, net_cents
            FROM wave_bills
            WHERE id IN ({placeholders})
            """,
            sub,
        ).fetchall()
        for r in rows:
            bill_id = int(r["id"])
            out[bill_id] = BillInfo(
                id=bill_id,
                invoice_date=str(r["invoice_date"] or ""),
                vendor_raw=str(r["vendor_raw"] or ""),
                vendor_category=(str(r["vendor_category"]).strip() if r["vendor_category"] else None),
                invoice_number=(str(r["invoice_number"]).strip() if r["invoice_number"] else None),
                total_cents=int(r["total_cents"] or 0),
                tax_cents=int(r["tax_cents"] or 0),
                net_cents=int(r["net_cents"] or 0),
            )
    return out


def bill_has_allocations(conn: sqlite3.Connection, wave_bill_id: int) -> bool:
    row = conn.execute("SELECT 1 FROM bill_allocations WHERE wave_bill_id = ? LIMIT 1", (wave_bill_id,)).fetchone()
    return bool(row)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--source-key", default="fresher_categories_wave_bill_allocations_csv")
    ap.add_argument("--start-date", default=None, help="Inclusive YYYY-MM-DD (default: manifest FY min start).")
    ap.add_argument("--end-date", default=None, help="Inclusive YYYY-MM-DD (default: manifest FY max end).")
    ap.add_argument("--all", action="store_true", help="Import all rows (ignore date filter).")
    ap.add_argument(
        "--reset",
        action="store_true",
        help=f"Delete existing allocations created by this importer (method={METHOD_ALLOC}/{METHOD_TAX_ITC}) before import.",
    )
    ap.add_argument(
        "--skip-existing",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Skip bills that already have any bill_allocations rows (default: true).",
    )
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    manifest = load_manifest()
    rules = load_rules()
    fys = fiscal_years_from_manifest(manifest)
    default_start = min((fy.start_date for fy in fys), default=None)
    default_end = max((fy.end_date for fy in fys), default=None)

    start_date = args.start_date or default_start
    end_date = args.end_date or default_end

    if not args.all and (not start_date or not end_date):
        raise SystemExit(
            "Missing start/end date filter. Either add fiscal_years to manifest, "
            "pass --start-date/--end-date, or use --all."
        )

    tax_cfg = rules.get("tax") or {}
    hst_itc_code = str(tax_cfg.get("hst_itc_account_code") or "2210").strip()

    src = get_source(manifest, args.source_key)
    csv_path = Path(str(src.get("path") or "")).expanduser()
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing source file: {csv_path}")

    sha_expected = str(src.get("sha256") or "").strip()
    if sha_expected:
        sha_actual = sha256_file(csv_path)
        if sha_actual != sha_expected:
            raise SystemExit(f"sha256 mismatch for {csv_path}: expected {sha_expected} actual {sha_actual}")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary = args.out_dir / "fresher_categories_allocations_import_summary.md"
    out_skipped = args.out_dir / "fresher_categories_allocations_import_skipped.csv"

    alloc_rows, sums, invoice_dates = read_allocations_csv(csv_path)
    bill_ids = sorted(sums.keys())

    conn = connect_db(args.db)
    stats = ImportStats(csv_rows_read=len(alloc_rows), csv_distinct_bills=len(bill_ids))

    skipped_rows: list[dict[str, str]] = []

    try:
        ensure_source_file(conn, args.source_key, src)

        if args.reset and not args.dry_run:
            conn.execute("DELETE FROM bill_allocations WHERE method IN (?, ?)", (METHOD_ALLOC, METHOD_TAX_ITC))
            conn.commit()

        coa_codes = {str(r["account_code"]) for r in conn.execute("SELECT account_code FROM chart_of_accounts").fetchall()}
        bill_info = load_bill_info(conn, bill_ids)

        conn.execute("BEGIN")

        for wave_bill_id in bill_ids:
            info = bill_info.get(wave_bill_id)
            if info is None:
                invoice_date_hint = invoice_dates.get(wave_bill_id, "")
                is_out_of_scope = (
                    (not args.all)
                    and invoice_date_hint
                    and start_date
                    and end_date
                    and (invoice_date_hint < str(start_date) or invoice_date_hint > str(end_date))
                )
                if is_out_of_scope:
                    stats = ImportStats(
                        csv_rows_read=stats.csv_rows_read,
                        csv_distinct_bills=stats.csv_distinct_bills,
                        bills_skipped_out_of_scope=stats.bills_skipped_out_of_scope + 1,
                        bills_missing_in_db=stats.bills_missing_in_db,
                        bills_skipped_already_allocated=stats.bills_skipped_already_allocated,
                        bills_skipped_allocation_mismatch=stats.bills_skipped_allocation_mismatch,
                        bills_skipped_missing_account_code=stats.bills_skipped_missing_account_code,
                        bills_imported=stats.bills_imported,
                        allocation_rows_inserted=stats.allocation_rows_inserted,
                        tax_itc_rows_inserted=stats.tax_itc_rows_inserted,
                    )
                    skipped_rows.append(
                        {
                            "wave_bill_id": str(wave_bill_id),
                            "reason": "out_of_scope_bill_in_csv",
                            "invoice_date": invoice_date_hint,
                            "vendor_raw": "",
                            "vendor_category": "",
                            "invoice_number": "",
                            "details": f"scope={start_date}→{end_date}",
                        }
                    )
                    continue

                stats = ImportStats(
                    csv_rows_read=stats.csv_rows_read,
                    csv_distinct_bills=stats.csv_distinct_bills,
                    bills_skipped_out_of_scope=stats.bills_skipped_out_of_scope,
                    bills_missing_in_db=stats.bills_missing_in_db + 1,
                    bills_skipped_already_allocated=stats.bills_skipped_already_allocated,
                    bills_skipped_allocation_mismatch=stats.bills_skipped_allocation_mismatch,
                    bills_skipped_missing_account_code=stats.bills_skipped_missing_account_code,
                    bills_imported=stats.bills_imported,
                    allocation_rows_inserted=stats.allocation_rows_inserted,
                    tax_itc_rows_inserted=stats.tax_itc_rows_inserted,
                )
                skipped_rows.append(
                    {
                        "wave_bill_id": str(wave_bill_id),
                        "reason": "missing_in_t2_final_db",
                        "invoice_date": invoice_date_hint,
                        "vendor_raw": "",
                        "vendor_category": "",
                        "invoice_number": "",
                        "details": "",
                    }
                )
                continue

            if not args.all and start_date and end_date and (info.invoice_date < str(start_date) or info.invoice_date > str(end_date)):
                stats = ImportStats(
                    csv_rows_read=stats.csv_rows_read,
                    csv_distinct_bills=stats.csv_distinct_bills,
                    bills_skipped_out_of_scope=stats.bills_skipped_out_of_scope + 1,
                    bills_missing_in_db=stats.bills_missing_in_db,
                    bills_skipped_already_allocated=stats.bills_skipped_already_allocated,
                    bills_skipped_allocation_mismatch=stats.bills_skipped_allocation_mismatch,
                    bills_skipped_missing_account_code=stats.bills_skipped_missing_account_code,
                    bills_imported=stats.bills_imported,
                    allocation_rows_inserted=stats.allocation_rows_inserted,
                    tax_itc_rows_inserted=stats.tax_itc_rows_inserted,
                )
                skipped_rows.append(
                    {
                        "wave_bill_id": str(wave_bill_id),
                        "reason": "out_of_scope_bill_in_db",
                        "invoice_date": info.invoice_date,
                        "vendor_raw": info.vendor_raw,
                        "vendor_category": info.vendor_category or "",
                        "invoice_number": info.invoice_number or "",
                        "details": f"scope={start_date}→{end_date}",
                    }
                )
                continue

            if args.skip_existing and bill_has_allocations(conn, wave_bill_id):
                stats = ImportStats(
                    csv_rows_read=stats.csv_rows_read,
                    csv_distinct_bills=stats.csv_distinct_bills,
                    bills_skipped_out_of_scope=stats.bills_skipped_out_of_scope,
                    bills_missing_in_db=stats.bills_missing_in_db,
                    bills_skipped_already_allocated=stats.bills_skipped_already_allocated + 1,
                    bills_skipped_allocation_mismatch=stats.bills_skipped_allocation_mismatch,
                    bills_skipped_missing_account_code=stats.bills_skipped_missing_account_code,
                    bills_imported=stats.bills_imported,
                    allocation_rows_inserted=stats.allocation_rows_inserted,
                    tax_itc_rows_inserted=stats.tax_itc_rows_inserted,
                )
                skipped_rows.append(
                    {
                        "wave_bill_id": str(wave_bill_id),
                        "reason": "already_has_bill_allocations",
                        "invoice_date": info.invoice_date,
                        "vendor_raw": info.vendor_raw,
                        "vendor_category": info.vendor_category or "",
                        "invoice_number": info.invoice_number or "",
                        "details": "",
                    }
                )
                continue

            bill_sum = sums.get(wave_bill_id, 0)
            if bill_sum != info.net_cents:
                stats = ImportStats(
                    csv_rows_read=stats.csv_rows_read,
                    csv_distinct_bills=stats.csv_distinct_bills,
                    bills_skipped_out_of_scope=stats.bills_skipped_out_of_scope,
                    bills_missing_in_db=stats.bills_missing_in_db,
                    bills_skipped_already_allocated=stats.bills_skipped_already_allocated,
                    bills_skipped_allocation_mismatch=stats.bills_skipped_allocation_mismatch + 1,
                    bills_skipped_missing_account_code=stats.bills_skipped_missing_account_code,
                    bills_imported=stats.bills_imported,
                    allocation_rows_inserted=stats.allocation_rows_inserted,
                    tax_itc_rows_inserted=stats.tax_itc_rows_inserted,
                )
                skipped_rows.append(
                    {
                        "wave_bill_id": str(wave_bill_id),
                        "reason": "allocation_sum_mismatch_vs_net",
                        "invoice_date": info.invoice_date,
                        "vendor_raw": info.vendor_raw,
                        "vendor_category": info.vendor_category or "",
                        "invoice_number": info.invoice_number or "",
                        "details": f"net_cents={info.net_cents} alloc_sum_cents={bill_sum} diff_cents={bill_sum - info.net_cents}",
                    }
                )
                continue

            rows_for_bill = [r for r in alloc_rows if r.wave_bill_id == wave_bill_id]
            if not rows_for_bill:
                skipped_rows.append(
                    {
                        "wave_bill_id": str(wave_bill_id),
                        "reason": "no_rows_in_csv_for_bill",
                        "invoice_date": info.invoice_date,
                        "vendor_raw": info.vendor_raw,
                        "vendor_category": info.vendor_category or "",
                        "invoice_number": info.invoice_number or "",
                        "details": "",
                    }
                )
                continue

            missing_codes = sorted({r.account_code for r in rows_for_bill if r.account_code and r.account_code not in coa_codes})
            blank_codes = any(not r.account_code for r in rows_for_bill)
            if missing_codes or blank_codes:
                stats = ImportStats(
                    csv_rows_read=stats.csv_rows_read,
                    csv_distinct_bills=stats.csv_distinct_bills,
                    bills_skipped_out_of_scope=stats.bills_skipped_out_of_scope,
                    bills_missing_in_db=stats.bills_missing_in_db,
                    bills_skipped_already_allocated=stats.bills_skipped_already_allocated,
                    bills_skipped_allocation_mismatch=stats.bills_skipped_allocation_mismatch,
                    bills_skipped_missing_account_code=stats.bills_skipped_missing_account_code + 1,
                    bills_imported=stats.bills_imported,
                    allocation_rows_inserted=stats.allocation_rows_inserted,
                    tax_itc_rows_inserted=stats.tax_itc_rows_inserted,
                )
                skipped_rows.append(
                    {
                        "wave_bill_id": str(wave_bill_id),
                        "reason": "missing_or_blank_account_code",
                        "invoice_date": info.invoice_date,
                        "vendor_raw": info.vendor_raw,
                        "vendor_category": info.vendor_category or "",
                        "invoice_number": info.invoice_number or "",
                        "details": f"missing={ '|'.join(missing_codes) } blank={blank_codes}",
                    }
                )
                continue

            if args.dry_run:
                stats = ImportStats(
                    csv_rows_read=stats.csv_rows_read,
                    csv_distinct_bills=stats.csv_distinct_bills,
                    bills_skipped_out_of_scope=stats.bills_skipped_out_of_scope,
                    bills_missing_in_db=stats.bills_missing_in_db,
                    bills_skipped_already_allocated=stats.bills_skipped_already_allocated,
                    bills_skipped_allocation_mismatch=stats.bills_skipped_allocation_mismatch,
                    bills_skipped_missing_account_code=stats.bills_skipped_missing_account_code,
                    bills_imported=stats.bills_imported + 1,
                    allocation_rows_inserted=stats.allocation_rows_inserted + len(rows_for_bill),
                    tax_itc_rows_inserted=stats.tax_itc_rows_inserted + (1 if info.tax_cents else 0),
                )
                continue

            for r in rows_for_bill:
                notes = (
                    f"source_key={args.source_key}; "
                    f"wave_account={r.wave_account}; "
                    f"match_methods={r.match_methods}; "
                    f"sources={r.sources}"
                ).strip()
                conn.execute(
                    """
                    INSERT INTO bill_allocations (wave_bill_id, account_code, amount_cents, method, notes)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (wave_bill_id, r.account_code, r.amount_cents, METHOD_ALLOC, notes),
                )

            tax_itc_inserted = 0
            if info.tax_cents:
                conn.execute(
                    """
                    INSERT INTO bill_allocations (wave_bill_id, account_code, amount_cents, method, notes)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        wave_bill_id,
                        hst_itc_code,
                        info.tax_cents,
                        METHOD_TAX_ITC,
                        f"source_key={args.source_key}; HST ITC from wave_bills.tax_cents",
                    ),
                )
                tax_itc_inserted = 1

            stats = ImportStats(
                csv_rows_read=stats.csv_rows_read,
                csv_distinct_bills=stats.csv_distinct_bills,
                bills_skipped_out_of_scope=stats.bills_skipped_out_of_scope,
                bills_missing_in_db=stats.bills_missing_in_db,
                bills_skipped_already_allocated=stats.bills_skipped_already_allocated,
                bills_skipped_allocation_mismatch=stats.bills_skipped_allocation_mismatch,
                bills_skipped_missing_account_code=stats.bills_skipped_missing_account_code,
                bills_imported=stats.bills_imported + 1,
                allocation_rows_inserted=stats.allocation_rows_inserted + len(rows_for_bill),
                tax_itc_rows_inserted=stats.tax_itc_rows_inserted + tax_itc_inserted,
            )

        if args.dry_run:
            conn.rollback()
        else:
            conn.commit()

    finally:
        conn.close()

    skipped_rows.sort(key=lambda r: (r["reason"], r["invoice_date"], int(r["wave_bill_id"]) if r["wave_bill_id"].isdigit() else 0))

    with out_summary.open("w", encoding="utf-8") as f:
        f.write("# Fresher/categories → t2_final.db bill_allocations import\n\n")
        f.write(f"- source_key: `{args.source_key}`\n")
        f.write(f"- csv_path: `{csv_path}`\n")
        f.write(f"- db: `{args.db}`\n")
        f.write(f"- method_alloc: `{METHOD_ALLOC}`\n")
        f.write(f"- method_tax_itc: `{METHOD_TAX_ITC}`\n")
        f.write(f"- hst_itc_account_code: `{hst_itc_code}`\n")
        if args.all:
            f.write("- scope: `all`\n")
        else:
            f.write(f"- scope: `{start_date} → {end_date}`\n")
        f.write(f"- dry_run: `{args.dry_run}`\n")
        f.write(f"- reset: `{args.reset}`\n")
        f.write(f"- skip_existing: `{args.skip_existing}`\n\n")
        f.write("## Counts\n\n")
        f.write(f"- csv_rows_read: {stats.csv_rows_read}\n")
        f.write(f"- csv_distinct_bills: {stats.csv_distinct_bills}\n")
        f.write(f"- bills_imported: {stats.bills_imported}\n")
        f.write(f"- allocation_rows_inserted: {stats.allocation_rows_inserted}\n")
        f.write(f"- tax_itc_rows_inserted: {stats.tax_itc_rows_inserted}\n")
        f.write(f"- bills_skipped_out_of_scope: {stats.bills_skipped_out_of_scope}\n")
        f.write(f"- bills_skipped_already_allocated: {stats.bills_skipped_already_allocated}\n")
        f.write(f"- bills_skipped_allocation_mismatch: {stats.bills_skipped_allocation_mismatch}\n")
        f.write(f"- bills_skipped_missing_account_code: {stats.bills_skipped_missing_account_code}\n")
        f.write(f"- bills_missing_in_db: {stats.bills_missing_in_db}\n\n")
        f.write("## Outputs\n\n")
        f.write(f"- skipped: `{out_skipped}`\n")

    with out_skipped.open("w", encoding="utf-8", newline="") as f:
        fieldnames = ["wave_bill_id", "reason", "invoice_date", "vendor_raw", "vendor_category", "invoice_number", "details"]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(skipped_rows)

    print("FRESHER/CATEGORIES ALLOCATIONS IMPORT COMPLETE")
    print(f"- summary: {out_summary}")
    print(f"- skipped: {out_skipped}")
    print(f"- bills_imported: {stats.bills_imported}")
    print(f"- allocation_rows_inserted: {stats.allocation_rows_inserted}")
    print(f"- tax_itc_rows_inserted: {stats.tax_itc_rows_inserted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
