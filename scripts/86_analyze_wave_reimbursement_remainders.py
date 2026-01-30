#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db


@dataclass(frozen=True)
class DetailRow:
    bank_txn_id: str
    bank_date: str
    evidence_category: str
    category: str
    shareholder_account: str
    bank_debit_cents: int
    allocated_to_bills_cents: int
    remainder_cents: int
    match_methods: str
    matched_wave_bill_ids: str


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--detail-csv", type=Path, default=PROJECT_ROOT / "output" / "wave_bill_reimbursement_journal_detail.csv")
    args = ap.parse_args()

    if not args.detail_csv.exists():
        raise SystemExit(f"Missing {args.detail_csv}. Run: python3 scripts/77_build_wave_bill_reimbursement_journals.py")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_md = args.out_dir / "wave_reimbursement_remainder_analysis.md"

    raw = list(csv.DictReader(args.detail_csv.open()))
    rows: list[DetailRow] = []
    for r in raw:
        rows.append(
            DetailRow(
                bank_txn_id=str(r.get("bank_txn_id") or "").strip(),
                bank_date=str(r.get("bank_date") or "").strip(),
                evidence_category=str(r.get("evidence_category") or "").strip(),
                category=str(r.get("category") or "").strip(),
                shareholder_account=str(r.get("shareholder_account") or "").strip(),
                bank_debit_cents=int(r.get("bank_debit_cents") or 0),
                allocated_to_bills_cents=int(r.get("allocated_to_bills_cents") or 0),
                remainder_cents=int(r.get("remainder_cents") or 0),
                match_methods=str(r.get("match_methods") or "").strip(),
                matched_wave_bill_ids=str(r.get("matched_wave_bill_ids") or "").strip(),
            )
        )

    conn = connect_db(args.db)
    try:
        bank_ids = [r.bank_txn_id for r in rows if r.bank_txn_id]
        if not bank_ids:
            raise SystemExit("No bank_txn_id rows found in reimbursement detail.")

        q = f"""
        SELECT id, txn_date, txn_type, description, vendor_parsed, manual_classification, notes
        FROM fresher_debits__bank_transactions
        WHERE id IN ({','.join('?' for _ in bank_ids)})
        """
        bank_info = {str(r["id"]): dict(r) for r in conn.execute(q, tuple(bank_ids)).fetchall()}

        # wave bill lookup
        bill_ids: set[int] = set()
        for r in rows:
            for part in (r.matched_wave_bill_ids or "").split(","):
                part = part.strip()
                if part.isdigit():
                    bill_ids.add(int(part))
        bill_info: dict[int, dict] = {}
        if bill_ids:
            q2 = f"""
            SELECT id, vendor_norm, invoice_date, invoice_number, total_cents
            FROM wave_bills
            WHERE id IN ({','.join('?' for _ in bill_ids)})
            """
            bill_info = {int(r["id"]): dict(r) for r in conn.execute(q2, tuple(sorted(bill_ids))).fetchall()}

    finally:
        conn.close()

    net = sum(r.remainder_cents for r in rows)
    pos = sum(r.remainder_cents for r in rows if r.remainder_cents > 0)
    neg = sum(r.remainder_cents for r in rows if r.remainder_cents < 0)

    by_category = defaultdict(int)
    by_manual = defaultdict(int)
    by_txn_type = defaultdict(int)
    for r in rows:
        by_category[r.category] += r.remainder_cents
        bi = bank_info.get(r.bank_txn_id, {})
        by_manual[str(bi.get("manual_classification") or "")] += r.remainder_cents
        by_txn_type[str(bi.get("txn_type") or "")] += r.remainder_cents

    top_abs = sorted(rows, key=lambda r: abs(r.remainder_cents), reverse=True)[:25]
    top_pos = [r for r in sorted(rows, key=lambda r: r.remainder_cents, reverse=True) if r.remainder_cents > 0][:25]
    top_neg = [r for r in sorted(rows, key=lambda r: r.remainder_cents) if r.remainder_cents < 0][:25]

    def fmt_bank(r: DetailRow) -> str:
        bi = bank_info.get(r.bank_txn_id, {})
        desc = str(bi.get("description") or "")
        txn_type = str(bi.get("txn_type") or "")
        manual = str(bi.get("manual_classification") or "")
        return f"{r.bank_txn_id} ({r.bank_date}) {txn_type} manual={manual} :: {desc}"

    def fmt_bills(r: DetailRow) -> str:
        parts = []
        for part in (r.matched_wave_bill_ids or "").split(","):
            part = part.strip()
            if not part.isdigit():
                continue
            bid = int(part)
            b = bill_info.get(bid)
            if not b:
                continue
            parts.append(f"bill{bid}:{b.get('vendor_norm')}:{b.get('invoice_date')}:{cents_to_dollars(int(b.get('total_cents') or 0))}")
        return " | ".join(parts)

    with out_md.open("w", encoding="utf-8") as f:
        f.write("# Wave reimbursement remainder analysis\n\n")
        f.write("This report explains the diagnostic field `remainder_cents = bank_reimbursement - linked_bill_totals` from `output/wave_bill_reimbursement_journal_detail.csv`.\n\n")
        f.write("Interpretation:\n")
        f.write("- `remainder_cents > 0`: reimbursement included extra amount not tied to Wave bills (often HST/fees/combined transfers).\n")
        f.write("- `remainder_cents < 0`: linked Wave bills exceed the reimbursement; corp still owes the shareholder (partial reimbursement or mismatched links).\n\n")
        if any(r.bank_txn_id == "909" for r in rows):
            f.write("Special case note (bank_txn 909):\n")
            f.write(
                "- The $2,000 positive remainder on `bank_txn_id=909` is an **HST payment to CRA** that was reimbursed to Thomas as part of the same $3,000 transfer.\n"
            )
            f.write(
                "- CRA labels this as a **\"Non-reporting period\"** payment and later transfers it into the **2024-03-31** reporting period; this is normal CRA presentation/timing in account exports.\n\n"
            )

        f.write("## Totals\n\n")
        f.write(f"- Rows: {len(rows)}\n")
        f.write(f"- Net remainder: ${cents_to_dollars(net)}\n")
        f.write(f"- Positive remainder total: ${cents_to_dollars(pos)}\n")
        f.write(f"- Negative remainder total: ${cents_to_dollars(neg)}\n\n")

        f.write("## By Category (net remainder)\n\n")
        for k, v in sorted(by_category.items(), key=lambda kv: abs(kv[1]), reverse=True):
            f.write(f"- {k or '(blank)'}: ${cents_to_dollars(v)}\n")
        f.write("\n")

        f.write("## By Bank Manual Classification (net remainder)\n\n")
        for k, v in sorted(by_manual.items(), key=lambda kv: abs(kv[1]), reverse=True):
            f.write(f"- {k or '(blank)'}: ${cents_to_dollars(v)}\n")
        f.write("\n")

        f.write("## Largest Remainders (by absolute value)\n\n")
        for r in top_abs:
            f.write(
                f"- remainder ${cents_to_dollars(r.remainder_cents)} | bank ${cents_to_dollars(r.bank_debit_cents)} "
                f"| bills ${cents_to_dollars(r.allocated_to_bills_cents)} | {fmt_bank(r)}\n"
            )
            bills = fmt_bills(r)
            if bills:
                f.write(f"  - {bills}\n")
        f.write("\n")

        f.write("## Largest Positive Remainders\n\n")
        for r in top_pos:
            f.write(f"- remainder ${cents_to_dollars(r.remainder_cents)} | {fmt_bank(r)}\n")
        f.write("\n")

        f.write("## Largest Negative Remainders\n\n")
        for r in top_neg:
            f.write(f"- remainder ${cents_to_dollars(r.remainder_cents)} | {fmt_bank(r)}\n")
            bills = fmt_bills(r)
            if bills:
                f.write(f"  - {bills}\n")

    print("WAVE REIMBURSEMENT REMAINDER ANALYSIS BUILT")
    print(f"- out: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
