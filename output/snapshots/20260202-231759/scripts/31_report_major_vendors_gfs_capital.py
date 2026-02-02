#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db


@dataclass(frozen=True)
class VendorSummary:
    vendor_category: str
    wave_bills: int
    wave_total_cents: int
    wave_tax_cents: int

    accounted_wave_bills: int
    accounted_bank_linked_wave_bills: int
    accounted_off_bank_wave_bills: int

    pad_payments: int
    pad_payment_total_cents: int
    pad_distinct_bank_txns: int

    pad_invoice_lines: int
    pad_invoice_total_cents: int
    pad_invoice_lines_linked_to_wave: int
    pad_payments_with_invoice_lines: int
    pad_payments_without_invoice_lines: int
    pad_payments_with_partial_invoice_lists: int


def cents(c: int) -> str:
    return f"${c/100:,.2f}"


def ensure_output_dir() -> Path:
    out_dir = PROJECT_ROOT / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def fetch_vendor_summary(conn: sqlite3.Connection, vendor_category: str) -> VendorSummary:
    wave = conn.execute(
        """
        SELECT COUNT(*) AS n, COALESCE(SUM(total_cents), 0) AS total_cents, COALESCE(SUM(tax_cents), 0) AS tax_cents
        FROM wave_bills
        WHERE vendor_category = ?
        """,
        (vendor_category,),
    ).fetchone()

    total_wave = conn.execute(
        "SELECT COUNT(*) AS n FROM fresher_debits__wave_bills WHERE vendor_category = ?",
        (vendor_category,),
    ).fetchone()

    accounted = conn.execute(
        """
        SELECT COUNT(DISTINCT wb.id) AS n
        FROM fresher_debits__wave_bills wb
        LEFT JOIN fresher_debits__wave_matches wm ON wm.wave_bill_id = wb.id
        LEFT JOIN fresher_debits__wave_bill_funding f ON f.wave_bill_id = wb.id
        WHERE wb.vendor_category = ?
          AND (wm.id IS NOT NULL OR f.id IS NOT NULL)
        """,
        (vendor_category,),
    ).fetchone()

    bank_linked = conn.execute(
        """
        SELECT COUNT(DISTINCT wb.id) AS n
        FROM fresher_debits__wave_bills wb
        LEFT JOIN fresher_debits__wave_matches wm ON wm.wave_bill_id = wb.id
        LEFT JOIN fresher_debits__wave_bill_funding f ON f.wave_bill_id = wb.id
        WHERE wb.vendor_category = ?
          AND (
            (wm.bank_txn_id IS NOT NULL AND TRIM(wm.bank_txn_id) <> '')
            OR (f.bank_txn_id IS NOT NULL AND TRIM(f.bank_txn_id) <> '')
          )
        """,
        (vendor_category,),
    ).fetchone()

    pad = conn.execute(
        """
        SELECT
          COUNT(*) AS payments,
          COALESCE(SUM(CAST(total_cents AS INTEGER)), 0) AS total_cents,
          COUNT(DISTINCT bank_txn_id) AS bank_txns
        FROM fresher_debits__pad_payments
        WHERE vendor = ?
        """,
        (vendor_category,),
    ).fetchone()

    pad_invoices = conn.execute(
        """
        SELECT
          COUNT(*) AS invoice_lines,
          COALESCE(SUM(CAST(amount_cents AS INTEGER)), 0) AS total_cents,
          COALESCE(SUM(CASE WHEN wave_bill_id IS NOT NULL AND TRIM(wave_bill_id) <> '' THEN 1 ELSE 0 END), 0) AS linked_to_wave
        FROM fresher_debits__pad_invoices i
        JOIN fresher_debits__pad_payments p ON p.id = i.pad_payment_id
        WHERE p.vendor = ?
        """,
        (vendor_category,),
    ).fetchone()

    pad_by_payment = conn.execute(
        """
        SELECT
          p.id AS pad_payment_id,
          CAST(p.total_cents AS INTEGER) AS payment_cents,
          COALESCE(SUM(CAST(i.amount_cents AS INTEGER)), 0) AS invoice_cents,
          COUNT(i.id) AS invoice_count
        FROM fresher_debits__pad_payments p
        LEFT JOIN fresher_debits__pad_invoices i ON i.pad_payment_id = p.id
        WHERE p.vendor = ?
        GROUP BY p.id
        """,
        (vendor_category,),
    ).fetchall()

    payments_without = sum(1 for r in pad_by_payment if int(r["invoice_count"] or 0) == 0)
    payments_with = len(pad_by_payment) - payments_without
    payments_partial = sum(
        1 for r in pad_by_payment if int(r["invoice_count"] or 0) > 0 and int(r["payment_cents"] or 0) != int(r["invoice_cents"] or 0)
    )

    accounted_wave_bills = int(accounted["n"] or 0)
    bank_linked_wave_bills = int(bank_linked["n"] or 0)
    return VendorSummary(
        vendor_category=vendor_category,
        wave_bills=int(wave["n"] or 0),
        wave_total_cents=int(wave["total_cents"] or 0),
        wave_tax_cents=int(wave["tax_cents"] or 0),
        accounted_wave_bills=accounted_wave_bills,
        accounted_bank_linked_wave_bills=bank_linked_wave_bills,
        accounted_off_bank_wave_bills=accounted_wave_bills - bank_linked_wave_bills,
        pad_payments=int(pad["payments"] or 0),
        pad_payment_total_cents=int(pad["total_cents"] or 0),
        pad_distinct_bank_txns=int(pad["bank_txns"] or 0),
        pad_invoice_lines=int(pad_invoices["invoice_lines"] or 0),
        pad_invoice_total_cents=int(pad_invoices["total_cents"] or 0),
        pad_invoice_lines_linked_to_wave=int(pad_invoices["linked_to_wave"] or 0),
        pad_payments_with_invoice_lines=payments_with,
        pad_payments_without_invoice_lines=payments_without,
        pad_payments_with_partial_invoice_lists=payments_partial,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument(
        "--out",
        type=Path,
        default=PROJECT_ROOT / "output" / "major_vendors_gfs_capital_status.md",
    )
    args = ap.parse_args()

    out_dir = ensure_output_dir()
    out_path = args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)

    conn = connect_db(args.db)
    try:
        vendors = ["GFS", "CAPITAL"]
        summaries = [fetch_vendor_summary(conn, v) for v in vendors]

        now = datetime.now().isoformat(timespec="seconds")
        lines: list[str] = []
        lines.append("# Major Vendor Status: GFS + Capital")
        lines.append("")
        lines.append(f"- Generated: `{now}`")
        lines.append(f"- DB: `{args.db}`")
        lines.append("")
        lines.append("## What this report covers (and what it does NOT)")
        lines.append("")
        lines.append("- ✅ What exists: Wave bill facts + bank matching + PAD grouping + invoice-number/amount lists (when available).")
        lines.append(
            "- ❌ Not present yet: item-level invoice categories (COGS subcategories / supplies / etc). "
            "Nothing in the current DB stores GFS/Capital invoice line items with account codes."
        )
        lines.append("")

        lines.append("## Snapshot Summary")
        lines.append("")
        lines.append("| vendor | wave bills | wave total | wave tax | accounted wave bills | bank-linked | off-bank | PAD payments | PAD total | PAD invoice lines | PAD invoices linked to wave |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for s in summaries:
            lines.append(
                f"| `{s.vendor_category}` | {s.wave_bills} | {cents(s.wave_total_cents)} | {cents(s.wave_tax_cents)} | {s.accounted_wave_bills} | "
                f"{s.accounted_bank_linked_wave_bills} | {s.accounted_off_bank_wave_bills} | {s.pad_payments} | {cents(s.pad_payment_total_cents)} | "
                f"{s.pad_invoice_lines} | {s.pad_invoice_lines_linked_to_wave} |"
            )
        lines.append("")

        lines.append("## Matching breakdown (Wave → Bank)")
        lines.append("")
        for vendor in vendors:
            lines.append(f"### {vendor}")
            lines.append("")
            rows = conn.execute(
                """
                SELECT wm.match_type, wm.match_method, COUNT(*) AS c
                FROM fresher_debits__wave_matches wm
                JOIN fresher_debits__wave_bills wb ON wb.id = wm.wave_bill_id
                WHERE wb.vendor_category = ?
                GROUP BY wm.match_type, wm.match_method
                ORDER BY c DESC, wm.match_type, wm.match_method
                """,
                (vendor,),
            ).fetchall()
            lines.append("| match_type | match_method | count |")
            lines.append("|---|---|---:|")
            for r in rows:
                lines.append(f"| `{r['match_type']}` | `{r['match_method']}` | {int(r['c'] or 0)} |")
            lines.append("")

            unaccounted = conn.execute(
                """
                SELECT wb.id, wb.invoice_date, wb.invoice_number, wb.vendor_raw, wb.total_cents, wb.tax_cents
                FROM fresher_debits__wave_bills wb
                LEFT JOIN fresher_debits__wave_matches wm ON wm.wave_bill_id = wb.id
                LEFT JOIN fresher_debits__wave_bill_funding f ON f.wave_bill_id = wb.id
                WHERE wb.vendor_category = ?
                  AND wm.id IS NULL
                  AND f.id IS NULL
                ORDER BY wb.invoice_date, wb.id
                """,
                (vendor,),
            ).fetchall()
            if unaccounted:
                lines.append("#### Wave bills with no match/funding record (needs investigation)")
                lines.append("")
                lines.append("| wave_bill_id | invoice_date | invoice_number | total | tax | vendor_raw |")
                lines.append("|---:|---|---|---:|---:|---|")
                for r in unaccounted:
                    lines.append(
                        f"| {r['id']} | `{r['invoice_date']}` | `{(r['invoice_number'] or '').strip()}` | "
                        f"{cents(int(r['total_cents'] or 0))} | {cents(int(r['tax_cents'] or 0))} | {r['vendor_raw']} |"
                    )
                lines.append("")

        lines.append("## PAD invoice list completeness")
        lines.append("")
        for vendor in vendors:
            lines.append(f"### {vendor}")
            lines.append("")
            pad_rows = conn.execute(
                """
                SELECT
                  p.payment_date,
                  p.id AS pad_payment_id,
                  p.bank_txn_id,
                  CAST(p.total_cents AS INTEGER) AS payment_cents,
                  COALESCE(SUM(CAST(i.amount_cents AS INTEGER)), 0) AS invoice_cents,
                  COUNT(i.id) AS invoice_count
                FROM fresher_debits__pad_payments p
                LEFT JOIN fresher_debits__pad_invoices i ON i.pad_payment_id = p.id
                WHERE p.vendor = ?
                GROUP BY p.id
                ORDER BY p.payment_date
                """,
                (vendor,),
            ).fetchall()

            no_lines = [r for r in pad_rows if int(r["invoice_count"] or 0) == 0]
            partial = [
                r
                for r in pad_rows
                if int(r["invoice_count"] or 0) > 0 and int(r["payment_cents"] or 0) != int(r["invoice_cents"] or 0)
            ]

            lines.append(f"- PAD payments: **{len(pad_rows)}** (distinct bank txns: **{summaries[vendors.index(vendor)].pad_distinct_bank_txns}**)")
            lines.append(f"- Payments missing invoice lists: **{len(no_lines)}**")
            lines.append(f"- Payments with partial invoice lists (sum mismatch): **{len(partial)}**")
            lines.append("")

            if no_lines:
                lines.append("#### Payments with NO invoice list captured")
                lines.append("")
                lines.append("| payment_date | pad_payment_id | bank_txn_id | payment_total |")
                lines.append("|---|---:|---:|---:|")
                for r in no_lines:
                    lines.append(
                        f"| `{r['payment_date']}` | `{r['pad_payment_id']}` | `{r['bank_txn_id']}` | {cents(int(r['payment_cents'] or 0))} |"
                    )
                lines.append("")

            if partial:
                lines.append("#### Payments with PARTIAL invoice lists (sum mismatch)")
                lines.append("")
                lines.append("| payment_date | pad_payment_id | bank_txn_id | payment_total | invoice_sum | diff | invoice_count | captured_invoice_numbers |")
                lines.append("|---|---:|---:|---:|---:|---:|---:|---|")
                for r in partial:
                    invs = conn.execute(
                        """
                        SELECT invoice_number
                        FROM fresher_debits__pad_invoices
                        WHERE pad_payment_id = ?
                        ORDER BY invoice_number
                        """,
                        (r["pad_payment_id"],),
                    ).fetchall()
                    inv_list = ", ".join((i["invoice_number"] or "").strip() for i in invs if (i["invoice_number"] or "").strip())
                    payment_cents = int(r["payment_cents"] or 0)
                    invoice_cents = int(r["invoice_cents"] or 0)
                    diff = payment_cents - invoice_cents
                    lines.append(
                        f"| `{r['payment_date']}` | `{r['pad_payment_id']}` | `{r['bank_txn_id']}` | {cents(payment_cents)} | "
                        f"{cents(invoice_cents)} | {cents(diff)} | {int(r['invoice_count'] or 0)} | `{inv_list}` |"
                    )
                lines.append("")

            missing_wave_links = conn.execute(
                """
                SELECT p.payment_date, p.id AS pad_payment_id, i.invoice_number, i.amount_cents
                FROM fresher_debits__pad_invoices i
                JOIN fresher_debits__pad_payments p ON p.id = i.pad_payment_id
                WHERE p.vendor = ?
                  AND (i.wave_bill_id IS NULL OR TRIM(i.wave_bill_id) = '')
                ORDER BY p.payment_date, i.invoice_number
                """,
                (vendor,),
            ).fetchall()
            if missing_wave_links:
                lines.append("#### PAD invoice lines not linked to Wave bills")
                lines.append("")
                lines.append("| payment_date | pad_payment_id | invoice_number | amount | notes |")
                lines.append("|---|---:|---|---:|---|")
                for r in missing_wave_links:
                    invoice_number = (r["invoice_number"] or "").strip()
                    amt_cents = int(r["amount_cents"] or 0)
                    note = ""
                    if invoice_number and amt_cents:
                        candidates = conn.execute(
                            """
                            SELECT id, invoice_date, vendor_raw
                            FROM fresher_debits__wave_bills
                            WHERE vendor_category = ?
                              AND CAST(total_cents AS INTEGER) = ?
                              AND (invoice_number IS NULL OR TRIM(invoice_number) = '')
                            ORDER BY invoice_date DESC, id DESC
                            LIMIT 2
                            """,
                            (vendor, amt_cents),
                        ).fetchall()
                        if candidates:
                            note = "possible Wave bill(s) by amount with blank invoice_number: " + ", ".join(
                                f"id={c['id']} date={c['invoice_date']}" for c in candidates
                            )
                    lines.append(
                        f"| `{r['payment_date']}` | `{r['pad_payment_id']}` | `{invoice_number}` | {cents(amt_cents)} | {note} |"
                    )
                lines.append("")

        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    finally:
        conn.close()

    print("REPORT WRITTEN")
    print(f"- {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
