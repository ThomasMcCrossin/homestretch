#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"


@dataclass(frozen=True)
class WaveBill:
    id: int
    invoice_date: str
    vendor_raw: str
    vendor_key: str | None
    invoice_number: str | None
    total_cents: int


@dataclass(frozen=True)
class Allocation:
    account_code: str
    amount_cents: int
    method: str | None
    notes: str | None


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def scope_window(fys: list[FiscalYear]) -> tuple[str, str]:
    start = min(fy.start_date for fy in fys)
    end = max(fy.end_date for fy in fys)
    return start, end


def fetch_wave_bills(
    conn,
    *,
    start_date: str,
    end_date: str,
    vendor_keys: list[str] | None = None,
) -> list[WaveBill]:
    vendor_clause = ""
    params: list[str] = [start_date, end_date]
    if vendor_keys:
        placeholders = ",".join("?" for _ in vendor_keys)
        vendor_clause = f" AND vendor_key IN ({placeholders})"
        params.extend([str(v) for v in vendor_keys])

    rows = conn.execute(
        f"""
        SELECT id, invoice_date, vendor_raw, vendor_key, invoice_number, total_cents
        FROM wave_bills
        WHERE invoice_date >= ? AND invoice_date <= ? {vendor_clause}
        ORDER BY invoice_date, id
        """,
        params,
    ).fetchall()
    out: list[WaveBill] = []
    for r in rows:
        out.append(
            WaveBill(
                id=int(r["id"]),
                invoice_date=str(r["invoice_date"]),
                vendor_raw=str(r["vendor_raw"] or ""),
                vendor_key=(str(r["vendor_key"]) if r["vendor_key"] else None),
                invoice_number=(str(r["invoice_number"]) if r["invoice_number"] else None),
                total_cents=int(r["total_cents"] or 0),
            )
        )
    return out


def fetch_allocations(conn, *, wave_bill_id: int) -> list[Allocation]:
    rows = conn.execute(
        """
        SELECT account_code, amount_cents, method, notes
        FROM bill_allocations
        WHERE wave_bill_id = ?
        ORDER BY id
        """,
        (wave_bill_id,),
    ).fetchall()
    return [
        Allocation(
            account_code=str(r["account_code"]),
            amount_cents=int(r["amount_cents"] or 0),
            method=(str(r["method"]) if r["method"] else None),
            notes=(str(r["notes"]) if r["notes"] else None),
        )
        for r in rows
    ]


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--vendor-key", action="append", dest="vendor_keys", help="Limit rebuild to a vendor_key (repeatable).")
    ap.add_argument("--reset", action="store_true", help="Delete existing wave bill accrual journal entries before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    accounts = cfg.get("accounts", {}) if isinstance(cfg.get("accounts"), dict) else {}
    ap_code = str(accounts.get("accounts_payable_code") or "2000").strip()
    source_cfg = (cfg.get("journal_sources") or {}).get("wave_bill_accrual") if isinstance(cfg.get("journal_sources"), dict) else {}
    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "wave_bill_accrual")
    entry_type = str((source_cfg or {}).get("entry_type") or "ACCRUAL")

    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "wave_bill_accrual_journal_summary.md"
    out_detail_csv = args.out_dir / "wave_bill_accrual_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        vendor_keys = [str(v).strip() for v in (args.vendor_keys or []) if str(v).strip()]
        bills = fetch_wave_bills(conn, start_date=start_date, end_date=end_date, vendor_keys=vendor_keys or None)

        if args.reset:
            if vendor_keys:
                bill_ids = [str(b.id) for b in bills]
                if bill_ids:
                    placeholders = ",".join("?" for _ in bill_ids)
                    conn.execute(
                        f"""
                        DELETE FROM journal_entries
                        WHERE source_system = ? AND source_record_type = ?
                          AND source_record_id IN ({placeholders})
                        """,
                        (source_system, source_record_type, *bill_ids),
                    )
            else:
                conn.execute(
                    """
                    DELETE FROM journal_entries
                    WHERE source_system = ? AND source_record_type = ?
                    """,
                    (source_system, source_record_type),
                )

        detail_rows: list[dict[str, str]] = []
        skipped: list[tuple[int, str]] = []

        inserted = 0
        total_alloc_cents = 0

        for bill in bills:
            allocs = fetch_allocations(conn, wave_bill_id=bill.id)
            if not allocs:
                skipped.append((bill.id, "missing_allocations"))
                detail_rows.append(
                    {
                        "wave_bill_id": str(bill.id),
                        "invoice_date": bill.invoice_date,
                        "vendor": bill.vendor_raw,
                        "invoice_number": bill.invoice_number or "",
                        "bill_total_cents": str(bill.total_cents),
                        "allocation_total_cents": "",
                        "ap_line_cents": "",
                        "journal_entry_id": "",
                        "status": "skipped_missing_allocations",
                    }
                )
                continue

            alloc_total = sum(a.amount_cents for a in allocs)
            if alloc_total == 0:
                skipped.append((bill.id, "zero_allocation_total"))
                detail_rows.append(
                    {
                        "wave_bill_id": str(bill.id),
                        "invoice_date": bill.invoice_date,
                        "vendor": bill.vendor_raw,
                        "invoice_number": bill.invoice_number or "",
                        "bill_total_cents": str(bill.total_cents),
                        "allocation_total_cents": "0",
                        "ap_line_cents": "",
                        "journal_entry_id": "",
                        "status": "skipped_zero_allocations",
                    }
                )
                continue

            je_id = f"WAVE_BILL_ACCRUAL_{bill.id}"
            desc_parts = [bill.vendor_raw.strip()]
            if bill.invoice_number:
                desc_parts.append(f"Invoice {bill.invoice_number}")
            description = " - ".join(p for p in desc_parts if p)
            notes = f"wave_bill_id={bill.id}; allocation_total_cents={alloc_total}"

            conn.execute(
                """
                INSERT OR REPLACE INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id,
                  source_bill_id, notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    bill.invoice_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    str(bill.id),
                    str(bill.id),
                    notes,
                ),
            )

            line_number = 1
            debit_total = 0
            credit_total = 0

            for alloc in allocs:
                if alloc.amount_cents == 0:
                    continue
                debit_cents = alloc.amount_cents if alloc.amount_cents > 0 else 0
                credit_cents = -alloc.amount_cents if alloc.amount_cents < 0 else 0
                if debit_cents:
                    debit_total += debit_cents
                if credit_cents:
                    credit_total += credit_cents
                line_desc = alloc.method or ""
                if alloc.notes:
                    line_desc = f"{line_desc} {alloc.notes}".strip()
                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:{line_number}",
                        je_id,
                        line_number,
                        alloc.account_code,
                        debit_cents,
                        credit_cents,
                        line_desc or None,
                    ),
                )
                line_number += 1

            net = debit_total - credit_total
            ap_debit = 0
            ap_credit = 0
            if net > 0:
                ap_credit = net
                credit_total += ap_credit
            elif net < 0:
                ap_debit = -net
                debit_total += ap_debit

            if ap_debit or ap_credit:
                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:{line_number}",
                        je_id,
                        line_number,
                        ap_code,
                        ap_debit,
                        ap_credit,
                        "Accounts payable (wave bill)",
                    ),
                )
                line_number += 1

            if debit_total != credit_total:
                conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
                conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))
                skipped.append((bill.id, "unbalanced"))
                detail_rows.append(
                    {
                        "wave_bill_id": str(bill.id),
                        "invoice_date": bill.invoice_date,
                        "vendor": bill.vendor_raw,
                        "invoice_number": bill.invoice_number or "",
                        "bill_total_cents": str(bill.total_cents),
                        "allocation_total_cents": str(alloc_total),
                        "ap_line_cents": str(net),
                        "journal_entry_id": "",
                        "status": "skipped_unbalanced",
                    }
                )
                continue

            inserted += 1
            total_alloc_cents += alloc_total
            detail_rows.append(
                {
                    "wave_bill_id": str(bill.id),
                    "invoice_date": bill.invoice_date,
                    "vendor": bill.vendor_raw,
                    "invoice_number": bill.invoice_number or "",
                    "bill_total_cents": str(bill.total_cents),
                    "allocation_total_cents": str(alloc_total),
                    "ap_line_cents": str(net),
                    "journal_entry_id": je_id,
                    "status": "posted",
                }
                )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "wave_bill_id",
                "invoice_date",
                "vendor",
                "invoice_number",
                "bill_total_cents",
                "allocation_total_cents",
                "ap_line_cents",
                "journal_entry_id",
                "status",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Wave bill accrual journal summary\n\n")
            f.write(f"- Scope: {start_date} → {end_date}\n")
            f.write(f"- Bills in scope: {len(bills)}\n")
            f.write(f"- Journal entries posted: {inserted}\n")
            f.write(f"- Total allocated amount: ${cents_to_dollars(total_alloc_cents)}\n")
            if skipped:
                f.write(f"- Skipped: {len(skipped)}\n")
                f.write("\n## Skipped bills (first 20)\n\n")
                for bill_id, reason in skipped[:20]:
                    f.write(f"- wave_bill_id {bill_id}: {reason}\n")

        conn.commit()

    finally:
        conn.close()

    print("WAVE BILL ACCRUAL JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {inserted} / {len(bills)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
