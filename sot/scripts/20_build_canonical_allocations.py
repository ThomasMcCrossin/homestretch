#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict

from _lib import DB_PATH, apply_migrations, connect_db


FY2024_START = "2023-06-01"
FY2025_END = "2025-05-31"

_IGNORED_DOC_IDS: set[int] = set()


@dataclass(frozen=True)
class CanonicalBuildStats:
    canonical_allocations_inserted: int = 0
    bank_txns_considered: int = 0
    bank_txns_with_canonical_allocations: int = 0
    bank_txns_from_settlement: int = 0
    bank_txns_from_cc_chain: int = 0
    bank_txns_from_direct_evidence: int = 0


def in_scope(txn_date: str) -> bool:
    return FY2024_START <= txn_date <= FY2025_END


def delete_existing_canonical(conn: sqlite3.Connection) -> None:
    conn.execute("DELETE FROM txn_document_allocations WHERE role='CANONICAL'")

def ignored_document_ids(conn: sqlite3.Connection) -> set[int]:
    rows = conn.execute(
        "SELECT document_id FROM document_flags WHERE flag='IGNORE' GROUP BY document_id"
    ).fetchall()
    return {int(r["document_id"]) for r in rows}


def fetch_bank_txns(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute(
        """
        SELECT at.id, at.txn_date, at.amount_cents, at.description
        FROM account_transactions at
        JOIN accounts a ON a.id = at.account_id
        WHERE a.account_type = 'BANK'
        ORDER BY at.txn_date, at.id
        """
    ).fetchall()


def settlement_batches_by_txn(conn: sqlite3.Connection) -> dict[int, list[tuple[str, int]]]:
    out: DefaultDict[int, list[tuple[str, int]]] = defaultdict(list)
    rows = conn.execute(
        """
        SELECT sbl.txn_id, sb.id AS batch_id, sb.settlement_type
        FROM settlement_batch_txn_links sbl
        JOIN settlement_batches sb ON sb.id = sbl.batch_id
        """
    ).fetchall()
    for r in rows:
        out[int(r["txn_id"])].append((str(r["settlement_type"]), int(r["batch_id"])))
    return dict(out)


def evidence_doc_allocations(
    conn: sqlite3.Connection, *, txn_id: int, methods: list[str]
) -> list[tuple[int, int, str, int]]:
    q = """
    SELECT document_id, amount_cents, method, is_verified
    FROM txn_document_allocations
    WHERE txn_id = ? AND role = 'EVIDENCE' AND method IN ({})
    ORDER BY is_verified DESC, ABS(amount_cents) DESC
    """.format(",".join(["?"] * len(methods)))
    params = (txn_id, *methods)
    rows = conn.execute(q, params).fetchall()
    return [(int(r["document_id"]), int(r["amount_cents"]), str(r["method"]), int(r["is_verified"])) for r in rows]


def insert_canonical_alloc(
    conn: sqlite3.Connection,
    *,
    txn_id: int,
    document_id: int,
    amount_cents: int,
    method: str,
    notes: str | None = None,
    is_verified: bool = False,
) -> None:
    conn.execute(
        """
        INSERT INTO txn_document_allocations(
          txn_id, document_id, amount_cents, allocation_type,
          confidence, is_verified, role, method, notes
        )
        VALUES (?, ?, ?, 'PAYMENT', NULL, ?, 'CANONICAL', ?, ?)
        """,
        (txn_id, document_id, amount_cents, 1 if is_verified else 0, method, notes),
    )


def build_from_settlement(conn: sqlite3.Connection, *, bank_txn_id: int, bank_amount_cents: int, batch_ids: list[int]) -> int:
    # Allocate across settlement lines with linked documents.
    #
    # Convention in this project: settlement line amounts are signed as they appear on the settlement notice
    # (invoices positive, credit memos negative). Bank statement lines represent cash movement in the opposite
    # direction, so the canonical bank->document allocation is `-settlement_line.amount_cents`.
    inserted = 0
    for batch_id in batch_ids:
        rows = conn.execute(
            """
            SELECT linked_document_id, amount_cents
            FROM settlement_lines
            WHERE batch_id = ? AND linked_document_id IS NOT NULL
            ORDER BY line_no
            """,
            (batch_id,),
        ).fetchall()
        for r in rows:
            doc_id = int(r["linked_document_id"])
            if doc_id in _IGNORED_DOC_IDS:
                continue
            line_amount = int(r["amount_cents"])
            insert_canonical_alloc(
                conn,
                txn_id=bank_txn_id,
                document_id=doc_id,
                amount_cents=-line_amount,
                method="SETTLEMENT_LINES",
                notes=f"batch_id={batch_id}",
                is_verified=False,
            )
            inserted += 1
    return inserted


def build_from_cc_chain(conn: sqlite3.Connection, *, bank_txn_id: int, bank_amount_cents: int) -> int:
    sign = -1 if bank_amount_cents < 0 else 1

    # bank -> cc_payment
    cc_payments = conn.execute(
        """
        SELECT to_txn_id
        FROM txn_links
        WHERE from_txn_id = ? AND link_type = 'BANK_TO_CARD_PAYMENT' AND role = 'EVIDENCE'
        """,
        (bank_txn_id,),
    ).fetchall()
    if not cc_payments:
        return 0

    doc_amounts: DefaultDict[int, int] = defaultdict(int)

    for (cc_payment_txn_id,) in cc_payments:
        # cc_payment -> purchases with allocated cents
        purchase_allocs = conn.execute(
            """
            SELECT to_txn_id, amount_cents
            FROM txn_links
            WHERE from_txn_id = ? AND link_type = 'CARD_PAYMENT_TO_PURCHASE' AND role = 'EVIDENCE'
            """,
            (int(cc_payment_txn_id),),
        ).fetchall()
        for pr in purchase_allocs:
            purchase_txn_id = int(pr["to_txn_id"])
            allocated_cents = int(pr["amount_cents"])
            # purchase -> documents (evidence)
            alloc_rows = conn.execute(
                """
                SELECT document_id, amount_cents
                FROM txn_document_allocations
                WHERE txn_id = ? AND role = 'EVIDENCE'
                """,
                (purchase_txn_id,),
            ).fetchall()
            weights = [
                (int(ar["document_id"]), abs(int(ar["amount_cents"])))
                for ar in alloc_rows
                if int(ar["amount_cents"]) != 0 and int(ar["document_id"]) not in _IGNORED_DOC_IDS
            ]
            total_w = sum(w for _, w in weights)
            if total_w <= 0:
                continue
            remaining = allocated_cents
            for idx, (doc_id, w) in enumerate(weights):
                if idx == len(weights) - 1:
                    portion = remaining
                else:
                    portion = (allocated_cents * w) // total_w
                    remaining -= portion
                doc_amounts[doc_id] += portion

    inserted = 0
    for doc_id, cents in sorted(doc_amounts.items()):
        if cents == 0:
            continue
        insert_canonical_alloc(
            conn,
            txn_id=bank_txn_id,
            document_id=doc_id,
            amount_cents=sign * cents,
            method="CC_CHAIN_DERIVED",
            notes=None,
            is_verified=False,
        )
        inserted += 1
    return inserted


def build_from_direct_evidence(conn: sqlite3.Connection, *, bank_txn_id: int) -> int:
    priority_methods = [
        ["fresher_debits__split_payments"],
        ["fresher_debits__wave_bill_funding"],
        ["fresher_debits__wave_matches"],
    ]
    for methods in priority_methods:
        q = """
        SELECT tda.document_id, tda.amount_cents, tda.method, tda.is_verified, d.total_cents
        FROM txn_document_allocations tda
        JOIN documents d ON d.id = tda.document_id
        WHERE tda.txn_id = ? AND tda.role = 'EVIDENCE' AND tda.method IN ({})
        ORDER BY tda.is_verified DESC, ABS(tda.amount_cents) DESC, tda.id
        """.format(",".join(["?"] * len(methods)))
        raw_rows = conn.execute(q, (bank_txn_id, *methods)).fetchall()
        if not raw_rows:
            continue

        # Dedupe by document_id and drop obviously-invalid allocations (allocation > document total).
        chosen: dict[int, tuple[int, str, int]] = {}
        for rr in raw_rows:
            doc_id = int(rr["document_id"])
            if doc_id in _IGNORED_DOC_IDS:
                continue
            amount_cents = int(rr["amount_cents"])
            doc_total = rr["total_cents"]
            if doc_total is not None:
                doc_total_cents = int(doc_total)
                if abs(amount_cents) > abs(doc_total_cents) + 1:
                    continue
            if doc_id in chosen:
                continue
            chosen[doc_id] = (amount_cents, str(rr["method"]), int(rr["is_verified"]))

        if not chosen:
            continue

        inserted = 0
        for doc_id, (amount_cents, method, is_verified_int) in chosen.items():
            insert_canonical_alloc(
                conn,
                txn_id=bank_txn_id,
                document_id=doc_id,
                amount_cents=amount_cents,
                method=f"DIRECT_EVIDENCE:{method}",
                notes=None,
                is_verified=bool(is_verified_int),
            )
            inserted += 1
        return inserted
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing CANONICAL allocations first.")
    args = ap.parse_args()

    conn = connect_db(args.db)
    try:
        apply_migrations(conn)
        conn.execute("BEGIN")
        global _IGNORED_DOC_IDS
        _IGNORED_DOC_IDS = ignored_document_ids(conn)
        if args.reset:
            delete_existing_canonical(conn)

        stats = CanonicalBuildStats()
        by_txn = settlement_batches_by_txn(conn)

        for r in fetch_bank_txns(conn):
            txn_id = int(r["id"])
            txn_date = str(r["txn_date"])
            if not in_scope(txn_date):
                continue

            bank_amount = int(r["amount_cents"])
            stats = CanonicalBuildStats(**{**stats.__dict__, "bank_txns_considered": stats.bank_txns_considered + 1})

            settlement = by_txn.get(txn_id, [])
            settlement_types = [t for t, _ in settlement]
            settlement_ids_by_type: DefaultDict[str, list[int]] = defaultdict(list)
            for t, bid in settlement:
                settlement_ids_by_type[t].append(bid)

            inserted = 0
            if "GFS_EFT" in settlement_ids_by_type:
                inserted = build_from_settlement(
                    conn,
                    bank_txn_id=txn_id,
                    bank_amount_cents=bank_amount,
                    batch_ids=settlement_ids_by_type["GFS_EFT"],
                )
                if inserted:
                    stats = CanonicalBuildStats(
                        **{
                            **stats.__dict__,
                            "bank_txns_from_settlement": stats.bank_txns_from_settlement + 1,
                        }
                    )
            elif any(t.endswith("_PAD") for t in settlement_types):
                pad_batch_ids: list[int] = []
                for t, bids in settlement_ids_by_type.items():
                    if t.endswith("_PAD"):
                        pad_batch_ids.extend(bids)
                inserted = build_from_settlement(
                    conn,
                    bank_txn_id=txn_id,
                    bank_amount_cents=bank_amount,
                    batch_ids=pad_batch_ids,
                )
                if inserted:
                    stats = CanonicalBuildStats(
                        **{
                            **stats.__dict__,
                            "bank_txns_from_settlement": stats.bank_txns_from_settlement + 1,
                        }
                    )
            else:
                inserted = build_from_cc_chain(conn, bank_txn_id=txn_id, bank_amount_cents=bank_amount)
                if inserted:
                    stats = CanonicalBuildStats(
                        **{**stats.__dict__, "bank_txns_from_cc_chain": stats.bank_txns_from_cc_chain + 1}
                    )
                else:
                    inserted = build_from_direct_evidence(conn, bank_txn_id=txn_id)
                    if inserted:
                        stats = CanonicalBuildStats(
                            **{**stats.__dict__, "bank_txns_from_direct_evidence": stats.bank_txns_from_direct_evidence + 1}
                        )

            if inserted:
                stats = CanonicalBuildStats(
                    **{
                        **stats.__dict__,
                        "canonical_allocations_inserted": stats.canonical_allocations_inserted + inserted,
                        "bank_txns_with_canonical_allocations": stats.bank_txns_with_canonical_allocations + 1,
                    }
                )

        conn.commit()

    finally:
        conn.close()

    print("CANONICAL BUILD COMPLETE")
    print(f"- db: {args.db}")
    print(f"- canonical_allocations_inserted: {stats.canonical_allocations_inserted}")
    print(f"- bank_txns_considered: {stats.bank_txns_considered}")
    print(f"- bank_txns_with_canonical_allocations: {stats.bank_txns_with_canonical_allocations}")
    print(f"- bank_txns_from_settlement: {stats.bank_txns_from_settlement}")
    print(f"- bank_txns_from_cc_chain: {stats.bank_txns_from_cc_chain}")
    print(f"- bank_txns_from_direct_evidence: {stats.bank_txns_from_direct_evidence}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
