#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, apply_migrations, connect_db


FY2024_START = "2023-06-01"
FY2025_END = "2025-05-31"


def cents_to_dollars(cents: int) -> str:
    return f"{cents/100:,.2f}"


@dataclass(frozen=True)
class BankTxnRow:
    txn_id: int
    txn_date: str
    amount_cents: int
    description: str
    canonical_sum_cents: int
    canonical_count: int
    settlement_types: str
    has_cc_payment_link: bool
    classifications: str


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--output-dir", type=Path, default=DB_PATH.parent.parent / "output")
    args = ap.parse_args()

    conn = connect_db(args.db)
    try:
        apply_migrations(conn)

        canon = {
            int(r["txn_id"]): (int(r["s"] or 0), int(r["n"]))
            for r in conn.execute(
                """
                SELECT txn_id, SUM(amount_cents) AS s, COUNT(*) AS n
                FROM txn_document_allocations
                WHERE role='CANONICAL'
                GROUP BY txn_id
                """
            ).fetchall()
        }

        settlement = {
            int(r["txn_id"]): str(r["types"] or "")
            for r in conn.execute(
                """
                SELECT sbl.txn_id, GROUP_CONCAT(DISTINCT sb.settlement_type) AS types
                FROM settlement_batch_txn_links sbl
                JOIN settlement_batches sb ON sb.id=sbl.batch_id
                GROUP BY sbl.txn_id
                """
            ).fetchall()
        }

        cc_payment_link = {
            int(r["txn_id"]): True
            for r in conn.execute(
                """
                SELECT from_txn_id AS txn_id
                FROM txn_links
                WHERE link_type='BANK_TO_CARD_PAYMENT' AND role='EVIDENCE'
                GROUP BY from_txn_id
                """
            ).fetchall()
        }

        classifications = {
            int(r["txn_id"]): str(r["cats"] or "")
            for r in conn.execute(
                """
                SELECT txn_id, GROUP_CONCAT(DISTINCT namespace || ':' || category) AS cats
                FROM txn_classifications
                GROUP BY txn_id
                """
            ).fetchall()
        }

        rows: list[BankTxnRow] = []
        for r in conn.execute(
            """
            SELECT at.id, at.txn_date, at.amount_cents, at.description
            FROM account_transactions at
            JOIN accounts a ON a.id=at.account_id
            WHERE a.account_type='BANK'
              AND at.txn_date >= ? AND at.txn_date <= ?
            ORDER BY at.txn_date, at.id
            """,
            (FY2024_START, FY2025_END),
        ).fetchall():
            txn_id = int(r["id"])
            s, n = canon.get(txn_id, (0, 0))
            rows.append(
                BankTxnRow(
                    txn_id=txn_id,
                    txn_date=str(r["txn_date"]),
                    amount_cents=int(r["amount_cents"]),
                    description=str(r["description"]),
                    canonical_sum_cents=int(s),
                    canonical_count=int(n),
                    settlement_types=settlement.get(txn_id, ""),
                    has_cc_payment_link=cc_payment_link.get(txn_id, False),
                    classifications=classifications.get(txn_id, ""),
                )
            )

    finally:
        conn.close()

    total = len(rows)
    fully = [r for r in rows if r.canonical_count and r.canonical_sum_cents == r.amount_cents]
    partial = [r for r in rows if r.canonical_count and r.canonical_sum_cents != r.amount_cents]
    zero = [r for r in rows if r.canonical_count == 0]

    # Unallocated-but-explained (by settlement / cc link / classifications)
    explained_non_doc = [
        r
        for r in zero
        if (r.settlement_types or r.has_cc_payment_link or r.classifications)
    ]
    unexplained = [r for r in zero if r not in explained_non_doc]

    # Largest issues by absolute remainder
    def remainder_abs(r: BankTxnRow) -> int:
        return abs(r.amount_cents - r.canonical_sum_cents)

    partial_sorted = sorted(partial, key=remainder_abs, reverse=True)
    unexplained_sorted = sorted(unexplained, key=lambda r: abs(r.amount_cents), reverse=True)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    md_path = args.output_dir / "bank_canonical_coverage_summary.md"
    csv_path = args.output_dir / "bank_canonical_needs_review.csv"

    md_lines: list[str] = []
    md_lines.append("# Bank Coverage (Canonical Allocations)")
    md_lines.append("")
    md_lines.append(f"Scope: {FY2024_START} → {FY2025_END}")
    md_lines.append("")
    md_lines.append("Definitions:")
    md_lines.append("- `canonical_sum`: sum of `txn_document_allocations.amount_cents` where `role='CANONICAL'` for the bank txn.")
    md_lines.append("- Some bank txns are “explained” via classifications or settlement links but intentionally have no document allocations yet.")
    md_lines.append("")
    md_lines.append("## Summary")
    md_lines.append("")
    md_lines.append(f"- bank_txns_total: {total}")
    md_lines.append(f"- fully_allocated_to_docs: {len(fully)}")
    md_lines.append(f"- partially_allocated_to_docs: {len(partial)}")
    md_lines.append(f"- no_doc_allocations: {len(zero)}")
    md_lines.append(f"  - explained_non_doc: {len(explained_non_doc)}")
    md_lines.append(f"  - unexplained: {len(unexplained)}")
    md_lines.append("")
    md_lines.append("## Largest Partial Remainders (Top 25)")
    md_lines.append("")
    for r in partial_sorted[:25]:
        rem = r.amount_cents - r.canonical_sum_cents
        md_lines.append(
            f"- {r.txn_date} txn_id={r.txn_id} bank={cents_to_dollars(r.amount_cents)} "
            f"canonical_sum={cents_to_dollars(r.canonical_sum_cents)} remainder={cents_to_dollars(rem)} "
            f"settlements={r.settlement_types or '-'} cc_link={int(r.has_cc_payment_link)} cats={r.classifications or '-'} "
            f"desc={r.description}"
        )
    if not partial_sorted:
        md_lines.append("- (none)")
    md_lines.append("")
    md_lines.append("## Largest Unexplained (Top 25)")
    md_lines.append("")
    for r in unexplained_sorted[:25]:
        md_lines.append(
            f"- {r.txn_date} txn_id={r.txn_id} bank={cents_to_dollars(r.amount_cents)} desc={r.description}"
        )
    if not unexplained_sorted:
        md_lines.append("- (none)")
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "txn_date",
                "txn_id",
                "bank_amount_cents",
                "canonical_sum_cents",
                "remainder_cents",
                "canonical_count",
                "settlement_types",
                "has_cc_payment_link",
                "classifications",
                "description",
            ]
        )
        for r in (partial_sorted + unexplained_sorted):
            w.writerow(
                [
                    r.txn_date,
                    r.txn_id,
                    r.amount_cents,
                    r.canonical_sum_cents,
                    r.amount_cents - r.canonical_sum_cents,
                    r.canonical_count,
                    r.settlement_types,
                    int(r.has_cc_payment_link),
                    r.classifications,
                    r.description,
                ]
            )

    print("REPORT COMPLETE")
    print(f"- md: {md_path}")
    print(f"- csv: {csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

