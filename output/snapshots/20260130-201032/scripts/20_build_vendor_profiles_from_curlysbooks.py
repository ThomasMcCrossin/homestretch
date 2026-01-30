#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import io
import sqlite3
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    connect_db,
    dollars_to_cents,
    get_source,
    load_manifest,
    load_rules,
)


CURB_SOURCE = "curlys_books_pg"
PROFILE_METHOD = "CURB_PG_SAMPLE"
MANUAL_PROFILE_METHOD = "MANUAL_OVERRIDE"


def pg_quote_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


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
    return [{k: (v or "").strip() for k, v in row.items()} for row in reader]


def ensure_output_dir() -> Path:
    out_dir = PROJECT_ROOT / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def reset_external_receipts(conn: sqlite3.Connection, entity: str, vendor_names: list[str]) -> None:
    placeholders = ",".join("?" for _ in vendor_names)
    params = [CURB_SOURCE, entity, *vendor_names]
    conn.execute(
        f"""
        DELETE FROM external_receipts
        WHERE source = ?
          AND entity = ?
          AND vendor IN ({placeholders})
        """,
        params,
    )


def reset_vendor_profiles(conn: sqlite3.Connection, entity: str, vendor_key: str) -> None:
    conn.execute(
        """
        DELETE FROM vendor_profiles
        WHERE vendor_key = ?
          AND entity = ?
          AND method = ?
        """,
        (vendor_key, entity, PROFILE_METHOD),
    )


def upsert_external_receipt(conn: sqlite3.Connection, row: dict[str, str]) -> int:
    receipt_uuid = row["receipt_id"]
    entity = row["entity"]
    vendor = row["vendor"]
    receipt_date = row["receipt_date"]
    subtotal_cents = dollars_to_cents(row.get("subtotal") or "0")
    tax_cents = dollars_to_cents(row.get("tax_total") or "0")
    total_cents = dollars_to_cents(row.get("total") or "0")

    receipt_number = row.get("receipt_number") or ""
    invoice_number = row.get("invoice_number") or ""
    status = row.get("status") or ""

    conn.execute(
        """
        INSERT INTO external_receipts
          (source, source_receipt_id, entity, vendor, receipt_date,
           subtotal_cents, tax_cents, total_cents,
           receipt_number, invoice_number, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(source, source_receipt_id) DO UPDATE SET
          entity=excluded.entity,
          vendor=excluded.vendor,
          receipt_date=excluded.receipt_date,
          subtotal_cents=excluded.subtotal_cents,
          tax_cents=excluded.tax_cents,
          total_cents=excluded.total_cents,
          receipt_number=excluded.receipt_number,
          invoice_number=excluded.invoice_number,
          status=excluded.status
        """,
        (
            CURB_SOURCE,
            receipt_uuid,
            entity,
            vendor,
            receipt_date,
            subtotal_cents,
            tax_cents,
            total_cents,
            receipt_number or None,
            invoice_number or None,
            status or None,
        ),
    )
    rec = conn.execute(
        "SELECT id FROM external_receipts WHERE source = ? AND source_receipt_id = ?",
        (CURB_SOURCE, receipt_uuid),
    ).fetchone()
    return int(rec["id"])


def upsert_external_line_item(conn: sqlite3.Connection, sqlite_receipt_id: int, row: dict[str, str]) -> None:
    line_number = int(row["line_number"])
    description = row.get("description") or ""
    line_total_cents = dollars_to_cents(row.get("line_total") or "0")
    account_code = (row.get("account_code") or "").strip() or None

    conn.execute(
        """
        INSERT INTO external_receipt_line_items
          (receipt_id, line_number, description, line_total_cents, account_code)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(receipt_id, line_number) DO UPDATE SET
          description=excluded.description,
          line_total_cents=excluded.line_total_cents,
          account_code=excluded.account_code
        """,
        (sqlite_receipt_id, line_number, description, line_total_cents, account_code),
    )


@dataclass(frozen=True)
class VendorProfileSummary:
    vendor_key: str
    entity: str
    method: str
    curlys_vendor_names: list[str]
    receipts: int
    line_items: int
    sample_total_cents: int
    uncategorized_cents: int
    start_date: str | None
    end_date: str | None
    splits: list[tuple[str, float, int]]  # (account_code, percent, sample_amount_cents)


def build_profile_from_sqlite(
    conn: sqlite3.Connection,
    *,
    vendor_key: str,
    entity: str,
    vendor_names: list[str],
    min_date: str | None,
    max_date: str | None,
    exclude_account_codes: list[str],
) -> VendorProfileSummary:
    placeholders = ",".join("?" for _ in vendor_names)
    params = [CURB_SOURCE, entity, *vendor_names]
    date_clause = ""
    if min_date:
        date_clause += " AND r.receipt_date >= ?"
        params.append(min_date)
    if max_date:
        date_clause += " AND r.receipt_date <= ?"
        params.append(max_date)

    exclude_clause = ""
    exclude_params: list[str] = []
    included_code_clause = "(li.account_code IS NULL OR TRIM(li.account_code) = '')"
    if exclude_account_codes:
        exclude_placeholders = ",".join("?" for _ in exclude_account_codes)
        exclude_clause = f" AND li.account_code NOT IN ({exclude_placeholders})"
        exclude_params = [str(c) for c in exclude_account_codes]
        included_code_clause = f"(li.account_code IS NULL OR TRIM(li.account_code) = '' OR li.account_code NOT IN ({exclude_placeholders}))"

    stats = conn.execute(
        f"""
        SELECT
          COUNT(DISTINCT r.id) AS receipts,
          COALESCE(SUM(CASE WHEN li.line_total_cents > 0 AND {included_code_clause} THEN 1 ELSE 0 END), 0) AS line_items,
          MIN(r.receipt_date) AS start_date,
          MAX(r.receipt_date) AS end_date,
          COALESCE(SUM(CASE WHEN li.line_total_cents > 0 AND {included_code_clause} THEN li.line_total_cents ELSE 0 END), 0) AS sum_line_total,
          COALESCE(SUM(CASE WHEN li.line_total_cents > 0 AND (li.account_code IS NULL OR TRIM(li.account_code) = '') THEN li.line_total_cents ELSE 0 END), 0) AS uncategorized
        FROM external_receipts r
        LEFT JOIN external_receipt_line_items li ON li.receipt_id = r.id
        WHERE r.source = ?
          AND r.entity = ?
          AND r.vendor IN ({placeholders})
          {date_clause}
        """,
        # included_code_clause is interpolated twice (line_items + sum_line_total), so its placeholders appear twice.
        (exclude_params * 2) + params,
    ).fetchone()

    receipts = int(stats["receipts"] or 0)
    line_items = int(stats["line_items"] or 0)
    sample_total_cents = int(stats["sum_line_total"] or 0)
    uncategorized_cents = int(stats["uncategorized"] or 0)
    start_date = stats["start_date"]
    end_date = stats["end_date"]

    totals = conn.execute(
        f"""
        SELECT li.account_code AS account_code, SUM(li.line_total_cents) AS amount_cents
        FROM external_receipts r
        JOIN external_receipt_line_items li ON li.receipt_id = r.id
        WHERE r.source = ?
          AND r.entity = ?
          AND r.vendor IN ({placeholders})
          {date_clause}
          AND li.line_total_cents > 0
          AND li.account_code IS NOT NULL
          AND TRIM(li.account_code) <> ''
          {exclude_clause}
        GROUP BY li.account_code
        ORDER BY amount_cents DESC, account_code ASC
        """,
        params + exclude_params,
    ).fetchall()

    categorized_total = sum(int(r["amount_cents"] or 0) for r in totals)
    splits: list[tuple[str, float, int]] = []
    if categorized_total != 0:
        for r in totals:
            account_code = str(r["account_code"])
            amt = int(r["amount_cents"] or 0)
            splits.append((account_code, float(amt / categorized_total), amt))

    return VendorProfileSummary(
        vendor_key=vendor_key,
        entity=entity,
        method=PROFILE_METHOD,
        curlys_vendor_names=vendor_names,
        receipts=receipts,
        line_items=line_items,
        sample_total_cents=sample_total_cents,
        uncategorized_cents=uncategorized_cents,
        start_date=str(start_date) if start_date else None,
        end_date=str(end_date) if end_date else None,
        splits=splits,
    )

def build_manual_profile_from_rules(
    rules: dict,
    *,
    vendor_key: str,
    default_entity: str,
) -> VendorProfileSummary | None:
    manual = rules.get("manual_vendor_profiles") or {}
    if not isinstance(manual, dict):
        return None
    cfg = manual.get(vendor_key)
    if not isinstance(cfg, dict):
        return None

    entity = str(cfg.get("entity") or default_entity).strip() or default_entity
    method = str(cfg.get("method") or MANUAL_PROFILE_METHOD).strip() or MANUAL_PROFILE_METHOD
    splits_cfg = cfg.get("splits") or {}
    if not isinstance(splits_cfg, dict) or not splits_cfg:
        raise SystemExit(f"manual_vendor_profiles.{vendor_key}.splits must be a non-empty mapping")

    splits: list[tuple[str, float, int]] = []
    total = 0.0
    for account_code, pct in splits_cfg.items():
        code = str(account_code).strip()
        if not code:
            continue
        try:
            p = float(pct)
        except Exception as e:  # noqa: BLE001 - CLI tool
            raise SystemExit(f"Invalid percent for manual_vendor_profiles.{vendor_key}.splits[{account_code!r}]") from e
        if p <= 0:
            continue
        total += p
        splits.append((code, p, 0))

    if not splits:
        raise SystemExit(f"manual_vendor_profiles.{vendor_key}.splits produced no positive percent entries")
    if abs(total - 1.0) > 1e-6:
        raise SystemExit(f"manual_vendor_profiles.{vendor_key}.splits must sum to 1.0 (got {total})")

    splits.sort(key=lambda t: (-t[1], t[0]))
    return VendorProfileSummary(
        vendor_key=vendor_key,
        entity=entity,
        method=method,
        curlys_vendor_names=[],
        receipts=0,
        line_items=0,
        sample_total_cents=0,
        uncategorized_cents=0,
        start_date=None,
        end_date=None,
        splits=splits,
    )


def insert_profile(conn: sqlite3.Connection, profile: VendorProfileSummary) -> int:
    conn.execute(
        """
        INSERT INTO vendor_profiles
          (vendor_key, entity, method, sample_receipts, sample_line_items, sample_total_cents,
           sample_start_date, sample_end_date, uncategorized_cents)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            profile.vendor_key,
            profile.entity,
            profile.method,
            profile.receipts,
            profile.line_items,
            profile.sample_total_cents,
            profile.start_date,
            profile.end_date,
            profile.uncategorized_cents,
        ),
    )
    row = conn.execute("SELECT last_insert_rowid() AS id").fetchone()
    profile_id = int(row["id"])

    for account_code, percent, sample_amount_cents in profile.splits:
        conn.execute(
            """
            INSERT INTO vendor_profile_splits
              (profile_id, account_code, percent, sample_amount_cents)
            VALUES (?, ?, ?, ?)
            """,
            (profile_id, account_code, percent, sample_amount_cents),
        )
    return profile_id


def fetch_account_names(curlys_books_path: Path, account_codes: list[str]) -> dict[str, str]:
    if not account_codes:
        return {}
    codes_sql = ",".join(pg_quote_literal(c) for c in sorted(set(account_codes)))
    sql = f"""
      SELECT account_code, account_name
      FROM curlys_corp.chart_of_accounts
      WHERE account_code IN ({codes_sql})
      ORDER BY account_code
    """
    rows = parse_csv(run_psql_copy(curlys_books_path, sql))
    out: dict[str, str] = {}
    for r in rows:
        code = r.get("account_code") or ""
        name = r.get("account_name") or ""
        if code:
            out[code] = name
    return out


def write_markdown_report(
    *,
    output_path: Path,
    curlys_books_path: Path,
    entity: str,
    min_date: str | None,
    max_date: str | None,
    profiles: list[VendorProfileSummary],
    account_names: dict[str, str],
    min_receipts_warning: int,
) -> None:
    lines: list[str] = []
    lines.append("# Vendor Allocation Profiles")
    lines.append("")
    lines.append(f"- Generated: {datetime.now().isoformat(timespec='seconds')}")
    lines.append(f"- Source (read-only): `{curlys_books_path}` (plus optional manual overrides)")
    lines.append(f"- Receipt entity filter: `{entity}`")
    if min_date or max_date:
        lines.append(f"- Date filter: {min_date or '…'} → {max_date or '…'}")
    lines.append("")

    for p in profiles:
        lines.append(f"## {p.vendor_key}")
        lines.append("")
        lines.append(f"- method: `{p.method}`")
        lines.append(f"- curlys-books vendor names: {', '.join(f'`{v}`' for v in p.curlys_vendor_names)}")
        if p.method == MANUAL_PROFILE_METHOD:
            lines.append("- source: manual override (`overrides/vendor_profile_rules.yml`)")
        else:
            lines.append(f"- sample receipts: **{p.receipts}**")
            lines.append(f"- sample line items: **{p.line_items}**")
        if p.start_date and p.end_date:
            lines.append(f"- sample date range: `{p.start_date}` → `{p.end_date}`")
        if p.method != MANUAL_PROFILE_METHOD:
            lines.append(f"- sample line-item total: **${p.sample_total_cents/100:.2f}**")
            if p.uncategorized_cents:
                lines.append(f"- uncategorized line-item total: **${p.uncategorized_cents/100:.2f}**")
            if p.receipts and p.receipts < min_receipts_warning:
                lines.append(f"- warning: sample size < {min_receipts_warning} receipts (treat as heuristic)")
        lines.append("")

        if not p.splits:
            lines.append("_No account-coded line items found for this vendor in the sample._")
            lines.append("")
            continue

        lines.append("| account_code | account_name | percent | sample_amount |")
        lines.append("|---:|---|---:|---:|")
        for account_code, percent, sample_amount_cents in p.splits:
            name = account_names.get(account_code, "")
            lines.append(
                f"| `{account_code}` | {name} | {percent*100:.2f}% | ${sample_amount_cents/100:.2f} |"
            )
        lines.append("")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--entity", default="corp")
    ap.add_argument("--vendor-key", action="append", dest="vendor_keys", help="Limit to a specific vendor key.")
    ap.add_argument("--min-date", default=None, help="Optional YYYY-MM-DD filter for receipt date.")
    ap.add_argument("--max-date", default=None, help="Optional YYYY-MM-DD filter for receipt date.")
    ap.add_argument("--reset", action="store_true", help="Delete existing imported samples + profiles before rebuild.")
    ap.add_argument("--min-receipts-warning", type=int, default=10)
    args = ap.parse_args()

    manifest = load_manifest()
    rules = load_rules()
    curlys_src = get_source(manifest, "curlys_books")
    curlys_books_path = Path(str(curlys_src["path"]))

    eligible_vendor_keys = rules.get("eligible_vendor_keys") or []
    if not isinstance(eligible_vendor_keys, list) or not eligible_vendor_keys:
        raise SystemExit("No eligible_vendor_keys configured in overrides/vendor_profile_rules.yml")

    vendor_keys = args.vendor_keys or [str(v) for v in eligible_vendor_keys]

    curlys_vendor_map = rules.get("curlys_books_vendor_names") or {}
    if not isinstance(curlys_vendor_map, dict):
        raise SystemExit("Invalid curlys_books_vendor_names mapping in overrides/vendor_profile_rules.yml")

    conn = connect_db(args.db)
    profiles: list[VendorProfileSummary] = []
    account_codes_seen: set[str] = set()
    try:
        profile_filters = rules.get("profile_filters") or {}
        if not isinstance(profile_filters, dict):
            raise SystemExit("Invalid profile_filters mapping in overrides/vendor_profile_rules.yml")
        global_exclude = profile_filters.get("global_exclude_account_codes") or []
        if global_exclude and not isinstance(global_exclude, list):
            raise SystemExit("profile_filters.global_exclude_account_codes must be a list")
        exclude_by_vendor = profile_filters.get("exclude_account_codes_by_vendor_key") or {}
        if exclude_by_vendor and not isinstance(exclude_by_vendor, dict):
            raise SystemExit("profile_filters.exclude_account_codes_by_vendor_key must be a mapping")

        for vendor_key in vendor_keys:
            manual_profile = build_manual_profile_from_rules(rules, vendor_key=vendor_key, default_entity=args.entity)
            if manual_profile:
                # Ensure idempotent manual profile regeneration.
                reset_vendor_profiles(conn, manual_profile.entity, vendor_key)
                conn.execute(
                    """
                    DELETE FROM vendor_profiles
                    WHERE vendor_key = ?
                      AND entity = ?
                      AND method = ?
                    """,
                    (vendor_key, manual_profile.entity, manual_profile.method),
                )
                profile_id = insert_profile(conn, manual_profile)
                conn.commit()
                for account_code, _, _ in manual_profile.splits:
                    account_codes_seen.add(account_code)
                print(f"PROFILE BUILT: {vendor_key} (profile_id={profile_id}, method={manual_profile.method})")
                profiles.append(manual_profile)
                continue

            vendor_names = curlys_vendor_map.get(vendor_key) or []
            if not isinstance(vendor_names, list) or not vendor_names:
                print(f"SKIP {vendor_key}: no curlys-books vendor names configured")
                continue

            vendor_names_sql = ",".join(pg_quote_literal(v) for v in vendor_names)
            where_clauses = [
                f"r.vendor IN ({vendor_names_sql})",
                f"r.entity = {pg_quote_literal(args.entity)}",
                "r.is_refund IS DISTINCT FROM TRUE",
            ]
            if args.min_date:
                where_clauses.append(f"r.date >= {pg_quote_literal(args.min_date)}::date")
            if args.max_date:
                where_clauses.append(f"r.date <= {pg_quote_literal(args.max_date)}::date")
            where_sql = " AND ".join(where_clauses)

            receipts_sql = f"""
              SELECT
                r.id::text AS receipt_id,
                r.entity AS entity,
                r.vendor AS vendor,
                r.date::text AS receipt_date,
                r.subtotal::text AS subtotal,
                COALESCE(r.tax_total, 0)::text AS tax_total,
                r.total::text AS total,
                COALESCE(r.receipt_number, '') AS receipt_number,
                COALESCE(r.invoice_number, '') AS invoice_number,
                COALESCE(r.status, '') AS status
              FROM curlys_corp.receipts r
              WHERE {where_sql}
              ORDER BY r.date, r.id
            """
            line_items_sql = f"""
              SELECT
                li.receipt_id::text AS receipt_id,
                li.line_number::text AS line_number,
                COALESCE(li.description, '') AS description,
                li.line_total::text AS line_total,
                COALESCE(li.account_code, '') AS account_code
              FROM curlys_corp.receipt_line_items li
              JOIN curlys_corp.receipts r ON r.id = li.receipt_id
              WHERE {where_sql}
              ORDER BY li.receipt_id, li.line_number
            """

            if args.reset:
                reset_external_receipts(conn, args.entity, vendor_names)
                conn.commit()

            receipt_rows = parse_csv(run_psql_copy(curlys_books_path, receipts_sql))
            if not receipt_rows:
                print(f"NO RECEIPTS for {vendor_key} ({', '.join(vendor_names)})")
                continue

            uuid_to_sqlite_id: dict[str, int] = {}
            for r in receipt_rows:
                sqlite_id = upsert_external_receipt(conn, r)
                uuid_to_sqlite_id[r["receipt_id"]] = sqlite_id

            li_rows = parse_csv(run_psql_copy(curlys_books_path, line_items_sql))
            for li in li_rows:
                rid = li["receipt_id"]
                sqlite_rid = uuid_to_sqlite_id.get(rid)
                if not sqlite_rid:
                    continue
                upsert_external_line_item(conn, sqlite_rid, li)

            reset_vendor_profiles(conn, args.entity, vendor_key)
            vendor_exclude = []
            vendor_ex_cfg = exclude_by_vendor.get(vendor_key) if isinstance(exclude_by_vendor, dict) else None
            if vendor_ex_cfg:
                if not isinstance(vendor_ex_cfg, list):
                    raise SystemExit(f"profile_filters.exclude_account_codes_by_vendor_key.{vendor_key} must be a list")
                vendor_exclude = [str(x).strip() for x in vendor_ex_cfg if str(x).strip()]
            exclude_account_codes = sorted({*(str(x).strip() for x in (global_exclude or []) if str(x).strip()), *vendor_exclude})

            profile = build_profile_from_sqlite(
                conn,
                vendor_key=vendor_key,
                entity=args.entity,
                vendor_names=vendor_names,
                min_date=args.min_date,
                max_date=args.max_date,
                exclude_account_codes=exclude_account_codes,
            )
            profile_id = insert_profile(conn, profile)
            conn.commit()

            for account_code, _, _ in profile.splits:
                account_codes_seen.add(account_code)

            print(f"PROFILE BUILT: {vendor_key} (profile_id={profile_id}, receipts={profile.receipts}, line_items={profile.line_items})")
            profiles.append(profile)

    finally:
        conn.close()

    account_names = fetch_account_names(curlys_books_path, sorted(account_codes_seen))
    out_dir = ensure_output_dir()
    output_path = out_dir / "vendor_profiles.md"
    write_markdown_report(
        output_path=output_path,
        curlys_books_path=curlys_books_path,
        entity=args.entity,
        min_date=args.min_date,
        max_date=args.max_date,
        profiles=profiles,
        account_names=account_names,
        min_receipts_warning=args.min_receipts_warning,
    )
    print(f"REPORT WRITTEN: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
