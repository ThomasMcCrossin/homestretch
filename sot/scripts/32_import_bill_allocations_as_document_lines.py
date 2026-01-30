#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict

from _lib import DB_PATH, SOT_ROOT, apply_migrations, connect_db


@dataclass(frozen=True)
class ImportStats:
    allocations_read: int = 0
    documents_touched: int = 0
    lines_inserted: int = 0
    missing_documents: int = 0
    total_mismatches: int = 0


def default_source_db() -> Path:
    return SOT_ROOT.parent / "db" / "t2_final.db"


def load_wave_bill_doc_map(conn: sqlite3.Connection) -> dict[str, int]:
    out: dict[str, int] = {}
    rows = conn.execute(
        """
        SELECT id, source_record_id
        FROM documents
        WHERE source_system='T2_FINAL_DB'
          AND source_record_id LIKE 'fresher_debits__wave_bills:%'
        """
    ).fetchall()
    for r in rows:
        doc_id = int(r["id"])
        source_record_id = str(r["source_record_id"])
        wave_bill_id = source_record_id.split(":", 1)[1]
        out[wave_bill_id] = doc_id
    return out


def fetch_account_names(conn: sqlite3.Connection) -> dict[str, str]:
    rows = conn.execute("SELECT account_code, account_name FROM chart_of_accounts").fetchall()
    return {str(r["account_code"]): str(r["account_name"]) for r in rows}


def normalize_method(method: str) -> str:
    m = method.strip().upper()
    if m == "VENDOR_PROFILE_ESTIMATE":
        return "PROFILE_ESTIMATE"
    if m == "TAX_ITC":
        return "TAX_ITC"
    return method.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--source-db", type=Path, default=default_source_db())
    ap.add_argument("--reset", action="store_true", help="Delete all existing document_lines first.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.source_db.exists():
        raise FileNotFoundError(f"Source DB not found: {args.source_db}")

    dst = connect_db(args.db)
    src = sqlite3.connect(args.source_db)
    src.row_factory = sqlite3.Row

    stats = ImportStats()

    try:
        apply_migrations(dst)
        dst.execute("BEGIN")

        if args.reset:
            if args.dry_run:
                print("WOULD: DELETE FROM document_lines (reset)")
            else:
                dst.execute("DELETE FROM document_lines")

        doc_by_wave_bill_id = load_wave_bill_doc_map(dst)
        account_names = fetch_account_names(dst)

        alloc_rows = src.execute(
            """
            SELECT
              ba.id AS alloc_id,
              wb.source_record_id AS fresher_wave_bill_id,
              ba.account_code,
              ba.amount_cents,
              ba.method AS alloc_method,
              ba.profile_id,
              ba.receipt_id,
              ba.notes
            FROM bill_allocations ba
            JOIN wave_bills wb ON wb.id = ba.wave_bill_id
            ORDER BY wb.source_record_id, ba.id
            """
        ).fetchall()

        stats = ImportStats(
            allocations_read=len(alloc_rows),
            documents_touched=0,
            lines_inserted=0,
            missing_documents=0,
            total_mismatches=0,
        )

        grouped: DefaultDict[str, list[sqlite3.Row]] = defaultdict(list)
        for r in alloc_rows:
            grouped[str(r["fresher_wave_bill_id"])].append(r)

        # Replace existing lines for documents we touch (idempotent).
        touched_doc_ids: list[int] = []
        for wave_bill_id in grouped.keys():
            doc_id = doc_by_wave_bill_id.get(wave_bill_id)
            if doc_id is None:
                stats = ImportStats(
                    allocations_read=stats.allocations_read,
                    documents_touched=stats.documents_touched,
                    lines_inserted=stats.lines_inserted,
                    missing_documents=stats.missing_documents + 1,
                    total_mismatches=stats.total_mismatches,
                )
                continue
            touched_doc_ids.append(doc_id)

        if touched_doc_ids and not args.reset:
            # Delete in chunks to avoid huge placeholder lists.
            chunk = 500
            for i in range(0, len(touched_doc_ids), chunk):
                sub = touched_doc_ids[i : i + chunk]
                placeholders = ",".join(["?"] * len(sub))
                if args.dry_run:
                    print(f"WOULD: DELETE document_lines for {len(sub)} documents")
                else:
                    dst.execute(f"DELETE FROM document_lines WHERE document_id IN ({placeholders})", sub)

        # Insert lines
        for wave_bill_id, rows in sorted(grouped.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else kv[0]):
            doc_id = doc_by_wave_bill_id.get(wave_bill_id)
            if doc_id is None:
                continue

            line_no = 0
            for r in rows:
                line_no += 1
                account_code = str(r["account_code"]).strip()
                amount_cents = int(r["amount_cents"])
                raw_method = str(r["alloc_method"])
                method = normalize_method(raw_method)
                alloc_id = int(r["alloc_id"])
                profile_id = r["profile_id"]
                receipt_id = r["receipt_id"]
                src_notes = r["notes"]

                description = account_names.get(account_code)
                notes_parts = [f"t2_final.bill_allocations:{alloc_id}", f"wave_bill_id={wave_bill_id}"]
                if profile_id is not None:
                    notes_parts.append(f"profile_id={profile_id}")
                if receipt_id is not None:
                    notes_parts.append(f"receipt_id={receipt_id}")
                notes_parts.append(f"source_method={raw_method}")
                if src_notes:
                    notes_parts.append(f"source_notes={str(src_notes).strip()}")
                notes = "; ".join(notes_parts)

                if args.dry_run:
                    continue

                dst.execute(
                    """
                    INSERT INTO document_lines(
                      document_id, line_no, description,
                      account_code, amount_cents, tax_cents,
                      method, notes
                    )
                    VALUES (?, ?, ?, ?, ?, NULL, ?, ?)
                    """,
                    (doc_id, line_no, description, account_code, amount_cents, method, notes),
                )
                stats = ImportStats(
                    allocations_read=stats.allocations_read,
                    documents_touched=stats.documents_touched,
                    lines_inserted=stats.lines_inserted + 1,
                    missing_documents=stats.missing_documents,
                    total_mismatches=stats.total_mismatches,
                )

            stats = ImportStats(
                allocations_read=stats.allocations_read,
                documents_touched=stats.documents_touched + 1,
                lines_inserted=stats.lines_inserted,
                missing_documents=stats.missing_documents,
                total_mismatches=stats.total_mismatches,
            )

        if not args.dry_run and touched_doc_ids:
            placeholders = ",".join(["?"] * len(touched_doc_ids))
            mismatch_rows = dst.execute(
                f"""
                SELECT d.id AS document_id, d.total_cents, SUM(dl.amount_cents) AS lines_sum_cents
                FROM documents d
                JOIN document_lines dl ON dl.document_id=d.id
                WHERE d.id IN ({placeholders})
                GROUP BY d.id
                HAVING d.total_cents IS NOT NULL AND lines_sum_cents != d.total_cents
                """,
                touched_doc_ids,
            ).fetchall()
            stats = ImportStats(
                allocations_read=stats.allocations_read,
                documents_touched=stats.documents_touched,
                lines_inserted=stats.lines_inserted,
                missing_documents=stats.missing_documents,
                total_mismatches=len(mismatch_rows),
            )

        if args.dry_run:
            dst.rollback()
        else:
            dst.commit()

    finally:
        dst.close()
        src.close()

    print("BILL ALLOCATIONS → DOCUMENT LINES IMPORT COMPLETE")
    print(f"- db: {args.db}")
    print(f"- source_db: {args.source_db}")
    print(f"- allocations_read: {stats.allocations_read}")
    print(f"- documents_touched: {stats.documents_touched}")
    print(f"- document_lines_inserted: {stats.lines_inserted if not args.dry_run else 0}")
    print(f"- missing_documents: {stats.missing_documents}")
    print(f"- total_mismatches: {stats.total_mismatches if not args.dry_run else 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

