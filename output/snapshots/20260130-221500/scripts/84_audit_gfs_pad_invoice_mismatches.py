#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest


@dataclass(frozen=True)
class GfsInvoiceLine:
    notification_id: str
    invoice_number: str
    tran_date: str
    net_amount_cents: int


DIRECT_VENDOR_PAYMENT_MATCH_TYPES = {
    "PAD_INVOICE",
    "BILL_PAYMENT",
    "BANK_DEBIT",
    "SPLIT_PAYMENT",
    "VENDOR_ETRANSFER",
    "E_TRANSFER_VENDOR",
    "E_TRANSFER",
    "CHEQUE",
    "CASH_PAID",
}


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def scope_window(fys: list[FiscalYear]) -> tuple[str, str]:
    start = min(fy.start_date for fy in fys)
    end = max(fy.end_date for fy in fys)
    return start, end


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")
    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_md = args.out_dir / "gfs_pad_invoice_mismatches_audit.md"
    out_csv = args.out_dir / "gfs_pad_invoice_mismatches_detail.csv"

    conn = connect_db(args.db)
    try:
        # notification_id -> bank_txn_id via credits-side bank items (amount_cents negative for debits)
        bank_links = conn.execute(
            """
            SELECT
              l.notification_id AS notification_id,
              b.bank_txn_id AS bank_txn_id,
              b.txn_date AS bank_date,
              CAST(b.amount_cents AS INTEGER) AS bank_amount_cents,
              b.description AS bank_description
            FROM fresher_credits__gfs_eft_bank_links l
            JOIN fresher_credits__credit_bank_items b ON b.id = l.bank_item_id
            WHERE b.txn_date >= ? AND b.txn_date <= ?
            ORDER BY b.txn_date, CAST(b.bank_txn_id AS INTEGER)
            """,
            (start_date, end_date),
        ).fetchall()

        notifications = {
            str(r["id"]): {
                "due_date": str(r["due_date"] or ""),
                "file_name": str(r["file_name"] or ""),
                "total_net_cents": int(r["total_net_cents"] or 0),
                "transaction_count": int(r["transaction_count"] or 0),
            }
            for r in conn.execute(
                """
                SELECT id, due_date, file_name, total_net_cents, transaction_count
                FROM fresher_credits__gfs_eft_notifications
                """
            ).fetchall()
        }

        invoice_lines: list[GfsInvoiceLine] = []
        for r in conn.execute(
            """
            SELECT notification_id, invoice_number, tran_date, net_amount_cents
            FROM fresher_credits__gfs_eft_notification_lines
            ORDER BY notification_id, invoice_number
            """
        ).fetchall():
            invoice_lines.append(
                GfsInvoiceLine(
                    notification_id=str(r["notification_id"]),
                    invoice_number=str(r["invoice_number"] or "").strip(),
                    tran_date=str(r["tran_date"] or ""),
                    net_amount_cents=int(r["net_amount_cents"] or 0),
                )
            )

        # invoice_number -> list[(wave_bill_id, total_cents, vendor_key)]
        wave_by_invoice: dict[str, list[tuple[int, int, str]]] = {}
        for r in conn.execute(
            """
            SELECT id, invoice_number, total_cents, vendor_key
            FROM wave_bills
            WHERE invoice_number IS NOT NULL AND TRIM(invoice_number) <> ''
            """
        ).fetchall():
            inv = str(r["invoice_number"] or "").strip()
            if inv:
                wave_by_invoice.setdefault(inv, []).append(
                    (int(r["id"]), int(r["total_cents"] or 0), str(r["vendor_key"] or ""))
                )

        # wave_bill_payment mismatches for cross-check (already generated)
        wave_pay_mismatch_rows: dict[str, int] = {}
        wave_pay_detail = args.out_dir / "wave_bill_payment_journal_detail.csv"
        if wave_pay_detail.exists():
            for r in csv.DictReader(wave_pay_detail.open()):
                bank_txn_id = str(r.get("bank_txn_id") or "").strip()
                diff = int(r.get("diff_cents") or 0)
                if bank_txn_id and diff != 0:
                    wave_pay_mismatch_rows[bank_txn_id] = diff

        lines_by_notification: dict[str, list[GfsInvoiceLine]] = {}
        for ln in invoice_lines:
            lines_by_notification.setdefault(ln.notification_id, []).append(ln)

        detail_rows: list[dict[str, str]] = []

        for bl in bank_links:
            nid = str(bl["notification_id"])
            bank_txn_id = str(bl["bank_txn_id"])
            bank_date = str(bl["bank_date"])
            bank_amt = int(bl["bank_amount_cents"] or 0)  # debits are negative here

            notif = notifications.get(nid, {})
            notif_total = int(notif.get("total_net_cents") or 0)
            notif_count = int(notif.get("transaction_count") or 0)
            notif_due_date = str(notif.get("due_date") or "")

            lines = lines_by_notification.get(nid, [])
            line_total = sum(int(x.net_amount_cents) for x in lines)

            present_total = 0
            present_count = 0
            missing_total = 0
            missing: list[tuple[str, int]] = []
            present: list[tuple[str, int, int]] = []

            for ln in lines:
                inv = ln.invoice_number
                matches = wave_by_invoice.get(inv, [])
                # Prefer GFS-keyed Wave bills when present.
                matches_sorted = sorted(
                    matches, key=lambda t: (0 if (t[2] or "").upper().startswith("GFS") else 1, t[0])
                )
                if matches_sorted:
                    bid, cents, _ = matches_sorted[0]
                    present_total += cents
                    present_count += 1
                    present.append((inv, cents, bid))
                else:
                    missing_total += int(ln.net_amount_cents)
                    missing.append((inv, int(ln.net_amount_cents)))

            wave_diff = wave_pay_mismatch_rows.get(bank_txn_id, 0)

            detail_rows.append(
                {
                    "bank_txn_id": bank_txn_id,
                    "bank_date": bank_date,
                    "bank_amount": cents_to_dollars(bank_amt),
                    "bank_amount_cents": str(bank_amt),
                    "notification_id": nid,
                    "notification_due_date": notif_due_date,
                    "notification_total": cents_to_dollars(notif_total),
                    "notification_total_cents": str(notif_total),
                    "notification_count": str(notif_count),
                    "line_total": cents_to_dollars(line_total),
                    "line_total_cents": str(line_total),
                    "present_count": str(present_count),
                    "present_total": cents_to_dollars(present_total),
                    "present_total_cents": str(present_total),
                    "missing_count": str(len(missing)),
                    "missing_total": cents_to_dollars(missing_total),
                    "missing_total_cents": str(missing_total),
                    "wave_bill_payment_diff_cents": str(wave_diff),
                    "missing_invoices": ";".join(f"{inv}:{cents}" for inv, cents in missing),
                    "present_invoices": ";".join(f"{inv}:{cents}:bill{bid}" for inv, cents, bid in present),
                }
            )

        unmatched = conn.execute(
            """
            SELECT n.id, n.due_date, n.transaction_count, n.total_net_cents, n.file_name
            FROM fresher_credits__gfs_eft_notifications n
            WHERE NOT EXISTS (
              SELECT 1 FROM fresher_credits__gfs_eft_bank_links l WHERE l.notification_id = n.id
            )
            ORDER BY n.due_date, CAST(n.id AS INTEGER)
            """
        ).fetchall()

    finally:
        conn.close()

    detail_rows_sorted = sorted(detail_rows, key=lambda r: abs(int(r.get("missing_total_cents") or 0)), reverse=True)

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "bank_txn_id",
            "bank_date",
            "bank_amount",
            "bank_amount_cents",
            "notification_id",
            "notification_due_date",
            "notification_total",
            "notification_total_cents",
            "notification_count",
            "line_total",
            "line_total_cents",
            "present_count",
            "present_total",
            "present_total_cents",
            "missing_count",
            "missing_total",
            "missing_total_cents",
            "wave_bill_payment_diff_cents",
            "missing_invoices",
            "present_invoices",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(detail_rows_sorted)

    with out_md.open("w", encoding="utf-8") as f:
        f.write("# GFS PAD audit: EFT notice lines vs Wave invoices\n\n")
        f.write(f"- Scope: {start_date} → {end_date}\n")
        f.write(f"- Bank-linked EFT notices in scope: {len(detail_rows_sorted)}\n")
        f.write(f"- Detail CSV: `output/{out_csv.name}`\n\n")

        rows_with_missing = [r for r in detail_rows_sorted if int(r.get("missing_total_cents") or 0) != 0]
        f.write("## Missing invoices (by EFT notice)\n\n")
        f.write(f"- Notices with missing Wave invoices: {len(rows_with_missing)}\n\n")
        for r in rows_with_missing[:30]:
            bank_abs = abs(int(r["bank_amount_cents"]))
            f.write(
                f"- bank_txn_id {r['bank_txn_id']} ({r['bank_date']}): bank ${cents_to_dollars(bank_abs)}; "
                f"notice_total ${r['notification_total']}; present ${r['present_total']}; missing ${r['missing_total']}; "
                f"missing_invoices [{r['missing_invoices']}]\n"
            )

        f.write("\n## Wave bill payment mismatches (cross-check)\n\n")
        mism = [r for r in detail_rows_sorted if int(r.get("wave_bill_payment_diff_cents") or 0) != 0]
        f.write(f"- Bank txns in both EFT links and wave-bill-payment mismatch list: {len(mism)}\n\n")
        for r in mism[:25]:
            f.write(
                f"- bank_txn_id {r['bank_txn_id']}: wave_bill_payment_diff_cents={r['wave_bill_payment_diff_cents']}; "
                f"missing_total_cents={r['missing_total_cents']}\n"
            )

        f.write("\n## Unmatched EFT notices (no bank link)\n\n")
        in_scope = [u for u in unmatched if (str(u["due_date"] or "") and start_date <= str(u["due_date"]) <= end_date)]
        f.write(f"- Unmatched notices in scope (by due_date): {len(in_scope)}\n\n")
        for u in in_scope[:30]:
            f.write(
                f"- due_date {u['due_date']}: notice_id {u['id']} count={u['transaction_count']} "
                f"total=${cents_to_dollars(int(u['total_net_cents'] or 0))} file={u['file_name']}\n"
            )

    print("GFS PAD INVOICE MISMATCH AUDIT BUILT")
    print(f"- out: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

