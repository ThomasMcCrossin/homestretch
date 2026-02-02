#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, allocation_rounding, connect_db, fiscal_years_from_manifest, load_manifest


@dataclass(frozen=True)
class EftInvoiceLine:
    bank_txn_id: str
    bank_date: str
    bank_item_category: str
    notification_id: str
    invoice_number: str
    tran_date: str
    amount_cents: int


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--reset", action="store_true", help="Delete previously created t2-final GFS EFT bills before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")
    scope_start = min(fy.start_date for fy in fys)
    scope_end = max(fy.end_date for fy in fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = args.out_dir / "gfs_eft_missing_invoices_created.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            # Only delete bills created by this script (explicit source_record_id prefix).
            rows = conn.execute(
                """
                SELECT id
                FROM wave_bills
                WHERE source_system = 't2-final'
                  AND source_record_id LIKE 'GFS_EFT_LINE:%'
                """
            ).fetchall()
            ids = [int(r["id"]) for r in rows]
            if ids:
                conn.execute(
                    f"DELETE FROM bill_allocations WHERE wave_bill_id IN ({','.join('?' for _ in ids)})",
                    tuple(ids),
                )
                conn.execute(
                    f"DELETE FROM wave_bills WHERE id IN ({','.join('?' for _ in ids)})",
                    tuple(ids),
                )

        # Global GFS weights (fallback): numeric invoices only, exclude STUB-*.
        gfs_bill_ids_rows = conn.execute(
            """
            SELECT id, total_cents
            FROM wave_bills
            WHERE lower(vendor_norm) LIKE 'gfs%'
              AND invoice_number IS NOT NULL AND TRIM(invoice_number) <> ''
              AND invoice_number NOT LIKE 'STUB-%'
              AND total_cents > 0
              AND EXISTS (SELECT 1 FROM bill_allocations ba WHERE ba.wave_bill_id = wave_bills.id)
            """
        ).fetchall()
        gfs_bill_ids = [int(r["id"]) for r in gfs_bill_ids_rows]
        gfs_total_cents = sum(int(r["total_cents"] or 0) for r in gfs_bill_ids_rows)
        if not gfs_bill_ids or gfs_total_cents <= 0:
            raise SystemExit("No existing GFS bills with allocations found; cannot build fallback weights.")

        alloc_rows = conn.execute(
            f"""
            SELECT account_code, SUM(amount_cents) AS sum_cents
            FROM bill_allocations
            WHERE wave_bill_id IN ({','.join('?' for _ in gfs_bill_ids)})
            GROUP BY account_code
            ORDER BY account_code
            """,
            tuple(gfs_bill_ids),
        ).fetchall()
        global_weights: list[tuple[str, float]] = []
        for r in alloc_rows:
            code = str(r["account_code"] or "").strip()
            if not code:
                continue
            w = int(r["sum_cents"] or 0) / gfs_total_cents
            if w != 0:
                global_weights.append((code, float(w)))

        # EFT lines for in-scope GFS EFT-linked bank items (PAD debits + vendor credit memo deposits).
        lines: list[EftInvoiceLine] = []
        rows = conn.execute(
            """
            SELECT
              b.bank_txn_id AS bank_txn_id,
              b.txn_date AS bank_date,
              c.category AS bank_item_category,
              l.notification_id AS notification_id,
              nl.invoice_number AS invoice_number,
              nl.tran_date AS tran_date,
              CAST(nl.net_amount_cents AS INTEGER) AS amount_cents,
              CAST(b.amount_cents AS INTEGER) AS bank_amount_cents
            FROM fresher_credits__gfs_eft_bank_links l
            JOIN fresher_credits__credit_bank_items b ON b.id = l.bank_item_id
            JOIN fresher_credits__credit_item_classifications c ON c.bank_item_id = b.id
            JOIN fresher_credits__gfs_eft_notification_lines nl ON nl.notification_id = l.notification_id
            WHERE b.txn_date >= ? AND b.txn_date <= ?
              AND c.category IN ('VENDOR_PAD_DEBIT', 'VENDOR_CREDIT_MEMO')
            ORDER BY b.txn_date, CAST(b.bank_txn_id AS INTEGER), nl.invoice_number
            """,
            (scope_start, scope_end),
        ).fetchall()
        for r in rows:
            lines.append(
                EftInvoiceLine(
                    bank_txn_id=str(r["bank_txn_id"]),
                    bank_date=str(r["bank_date"]),
                    bank_item_category=str(r["bank_item_category"] or "").strip(),
                    notification_id=str(r["notification_id"]),
                    invoice_number=str(r["invoice_number"] or "").strip(),
                    tran_date=str(r["tran_date"] or ""),
                    amount_cents=int(r["amount_cents"] or 0),
                )
            )

        # Index existing wave bills by invoice_number
        existing = {
            str(r["invoice_number"]): int(r["id"])
            for r in conn.execute(
                "SELECT id, invoice_number FROM wave_bills WHERE invoice_number IS NOT NULL AND TRIM(invoice_number) <> ''"
            ).fetchall()
        }

        # Helper: compute weights from existing bills within the same notification.
        def weights_for_notification(notification_id: str) -> tuple[list[tuple[str, float]], str]:
            invs = [ln.invoice_number for ln in lines if ln.notification_id == notification_id]
            bill_ids = [existing[i] for i in invs if i in existing]
            if not bill_ids:
                return (global_weights, "GLOBAL_GFS_WEIGHTS")
            total = conn.execute(
                f"SELECT SUM(total_cents) AS s FROM wave_bills WHERE id IN ({','.join('?' for _ in bill_ids)})",
                tuple(bill_ids),
            ).fetchone()["s"]
            total = int(total or 0)
            if total == 0:
                return (global_weights, "GLOBAL_GFS_WEIGHTS")
            rows2 = conn.execute(
                f"""
                SELECT account_code, SUM(amount_cents) AS s
                FROM bill_allocations
                WHERE wave_bill_id IN ({','.join('?' for _ in bill_ids)})
                GROUP BY account_code
                ORDER BY account_code
                """,
                tuple(bill_ids),
            ).fetchall()
            weights: list[tuple[str, float]] = []
            for rr in rows2:
                code = str(rr["account_code"] or "").strip()
                if not code:
                    continue
                w = int(rr["s"] or 0) / total
                if w != 0:
                    weights.append((code, float(w)))
            if not weights:
                return (global_weights, "GLOBAL_GFS_WEIGHTS")
            return (weights, f"NOTICE_WEIGHTS:{notification_id}")

        created_rows: list[dict[str, str]] = []
        created = 0
        skipped_existing = 0

        for ln in lines:
            inv = ln.invoice_number
            if not inv:
                continue
            if inv in existing:
                skipped_existing += 1
                continue

            weights, weight_basis = weights_for_notification(ln.notification_id)
            total_cents = int(ln.amount_cents or 0)
            if total_cents == 0:
                continue

            sign = -1 if total_cents < 0 else 1
            abs_total = abs(total_cents)
            rounded = allocation_rounding(abs_total, weights)
            allocations = [(acct, sign * cents) for acct, cents in rounded if cents]
            alloc_sum = sum(c for _, c in allocations)
            if alloc_sum != total_cents:
                # Should never happen if rounding is correct; fail loudly.
                raise SystemExit(f"Allocation mismatch for {inv}: expected {total_cents} got {alloc_sum}")

            is_credit = inv.startswith("200") or total_cents < 0
            vendor_norm = f"gfs credit memo {inv}" if is_credit else f"gfs bill {inv}"
            source_record_id = f"GFS_EFT_LINE:{ln.notification_id}:{inv}"
            invoice_date = ln.tran_date or ln.bank_date

            tax_cents = sum(c for acct, c in allocations if acct == "2210")
            net_cents = total_cents - tax_cents

            conn.execute(
                """
                INSERT INTO wave_bills (
                  invoice_date, vendor_raw, vendor_norm, vendor_key,
                  invoice_number, total_cents, tax_cents, net_cents,
                  vendor_category, source_system, source_record_id
                ) VALUES (?, ?, ?, NULL, ?, ?, ?, ?, NULL, 't2-final', ?)
                """,
                (
                    invoice_date,
                    "GFS",
                    vendor_norm,
                    inv,
                    total_cents,
                    tax_cents,
                    net_cents,
                    source_record_id,
                ),
            )
            new_id = int(conn.execute("SELECT last_insert_rowid() AS id").fetchone()["id"])
            existing[inv] = new_id

            for acct, cents in allocations:
                conn.execute(
                    """
                    INSERT INTO bill_allocations (wave_bill_id, account_code, amount_cents, method, notes)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        new_id,
                        acct,
                        int(cents),
                        "GFS_EFT_IMPUTE",
                        f"invoice_number={inv}; notification_id={ln.notification_id}; bank_txn_id={ln.bank_txn_id}; weight_basis={weight_basis}",
                    ),
                )

            created += 1
            created_rows.append(
                {
                    "invoice_number": inv,
                    "wave_bill_id": str(new_id),
                    "invoice_date": invoice_date,
                    "total": cents_to_dollars(total_cents),
                    "total_cents": str(total_cents),
                    "tax_cents": str(tax_cents),
                    "net_cents": str(net_cents),
                    "bank_txn_id": ln.bank_txn_id,
                    "notification_id": ln.notification_id,
                    "weight_basis": weight_basis,
                }
            )

        with out_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "invoice_number",
                "wave_bill_id",
                "invoice_date",
                "total",
                "total_cents",
                "tax_cents",
                "net_cents",
                "bank_txn_id",
                "notification_id",
                "weight_basis",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(created_rows)

        conn.commit()

    finally:
        conn.close()

    print("GFS EFT MISSING INVOICES IMPORTED")
    print(f"- out: {out_csv}")
    print(f"- created: {created}")
    print(f"- skipped_existing: {skipped_existing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
