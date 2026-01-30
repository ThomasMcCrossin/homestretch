#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest


@dataclass(frozen=True)
class Row:
    entry_date: str
    journal_entry_id: str
    source_record_type: str
    source_record_id: str
    source_bank_line_id: str
    bank_description: str
    bank_txn_category: str
    bank_txn_explanation: str
    debit_cents: int
    credit_cents: int
    line_description: str

    @property
    def net_cents(self) -> int:
        return self.debit_cents - self.credit_cents


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def infer_shareholder(text: str) -> str:
    t = (text or "").lower()
    if "dwayne" in t:
        return "Dwayne"
    if "thomas" in t:
        return "Thomas"
    return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--account-code", default="2500")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")
    scope_start = min(fy.start_date for fy in fys)
    scope_end = max(fy.end_date for fy in fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = args.out_dir / "due_from_shareholder_breakdown.csv"
    out_md = args.out_dir / "due_from_shareholder_breakdown.md"

    conn = connect_db(args.db)
    try:
        rows = conn.execute(
            """
            SELECT
              je.entry_date,
              je.id AS journal_entry_id,
              COALESCE(je.source_record_type, '') AS source_record_type,
              COALESCE(je.source_record_id, '') AS source_record_id,
              COALESCE(je.source_bank_line_id, '') AS source_bank_line_id,
              COALESCE(bt.description, '') AS bank_description,
              COALESCE(bc.txn_category, '') AS bank_txn_category,
              COALESCE(bc.explanation, '') AS bank_txn_explanation,
              CAST(jl.debit_cents AS INTEGER) AS debit_cents,
              CAST(jl.credit_cents AS INTEGER) AS credit_cents,
              COALESCE(jl.description, '') AS line_description
            FROM journal_entries je
            JOIN journal_entry_lines jl ON jl.journal_entry_id = je.id
            LEFT JOIN fresher_debits__bank_transactions bt
              ON bt.id = je.source_bank_line_id
            LEFT JOIN (
              SELECT bank_txn_id, txn_category, explanation
              FROM (
                SELECT
                  bank_txn_id,
                  txn_category,
                  explanation,
                  ROW_NUMBER() OVER (
                    PARTITION BY bank_txn_id
                    ORDER BY CAST(verified AS INTEGER) DESC, CAST(id AS INTEGER) ASC
                  ) AS rn
                FROM fresher_debits__bank_txn_classifications
              )
              WHERE rn = 1
            ) bc ON bc.bank_txn_id = je.source_bank_line_id
            WHERE je.entry_date >= ? AND je.entry_date <= ?
              AND jl.account_code = ?
            ORDER BY je.entry_date, je.id, jl.line_number
            """,
            (scope_start, scope_end, str(args.account_code).strip()),
        ).fetchall()

        detail: list[dict[str, str]] = []
        totals_by_source: dict[str, int] = defaultdict(int)
        totals_by_shareholder: dict[str, int] = defaultdict(int)
        net_total = 0

        for r in rows:
            row = Row(
                entry_date=str(r["entry_date"]),
                journal_entry_id=str(r["journal_entry_id"]),
                source_record_type=str(r["source_record_type"] or ""),
                source_record_id=str(r["source_record_id"] or ""),
                source_bank_line_id=str(r["source_bank_line_id"] or ""),
                bank_description=str(r["bank_description"] or ""),
                bank_txn_category=str(r["bank_txn_category"] or ""),
                bank_txn_explanation=str(r["bank_txn_explanation"] or ""),
                debit_cents=int(r["debit_cents"] or 0),
                credit_cents=int(r["credit_cents"] or 0),
                line_description=str(r["line_description"] or ""),
            )

            shareholder = infer_shareholder(
                f"{row.line_description} {row.bank_description} {row.bank_txn_category} {row.bank_txn_explanation}"
            )
            net_total += row.net_cents
            totals_by_source[row.source_record_type] += row.net_cents
            totals_by_shareholder[shareholder or "Unclassified"] += row.net_cents

            detail.append(
                {
                    "entry_date": row.entry_date,
                    "journal_entry_id": row.journal_entry_id,
                    "source_record_type": row.source_record_type,
                    "source_record_id": row.source_record_id,
                    "bank_txn_id": row.source_bank_line_id,
                    "bank_description": row.bank_description,
                    "bank_txn_category": row.bank_txn_category,
                    "bank_txn_explanation": row.bank_txn_explanation,
                    "shareholder": shareholder,
                    "debit": cents_to_dollars(row.debit_cents),
                    "credit": cents_to_dollars(row.credit_cents),
                    "net": cents_to_dollars(row.net_cents),
                    "line_description": row.line_description,
                }
            )

    finally:
        conn.close()

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "entry_date",
            "journal_entry_id",
            "source_record_type",
            "source_record_id",
            "bank_txn_id",
            "bank_description",
            "bank_txn_category",
            "bank_txn_explanation",
            "shareholder",
            "debit",
            "credit",
            "net",
            "line_description",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(detail)

    with out_md.open("w", encoding="utf-8") as f:
        f.write("# Due-from-shareholder breakdown (account 2500)\n\n")
        f.write(f"- Scope: {scope_start} → {scope_end}\n")
        f.write(f"- Account: {args.account_code}\n")
        f.write(f"- Net total: ${cents_to_dollars(net_total)} (debits - credits)\n")
        f.write("\n## Net by source_record_type\n\n")
        for k, v in sorted(totals_by_source.items(), key=lambda kv: (-abs(kv[1]), kv[0])):
            f.write(f"- {k or '(blank)'}: ${cents_to_dollars(v)}\n")
        f.write("\n## Net by shareholder (best-effort)\n\n")
        for k, v in sorted(totals_by_shareholder.items(), key=lambda kv: (-abs(kv[1]), kv[0])):
            f.write(f"- {k}: ${cents_to_dollars(v)}\n")
        f.write("\n## Detail\n\n")
        f.write(f"See: `{out_csv}`\n")

    print("DUE-FROM-SHAREHOLDER REPORT BUILT")
    print(f"- out: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
