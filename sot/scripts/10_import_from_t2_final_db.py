#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Any

from _lib import SOT_ROOT, apply_migrations, connect_db


SOURCE_SYSTEM = "T2_FINAL_DB"

FY2024_START = "2023-06-01"
FY2025_END = "2025-05-31"


def in_scope(date_str: str | None) -> bool:
    if not date_str:
        return False
    d = str(date_str).strip()
    if not d:
        return False
    return FY2024_START <= d <= FY2025_END


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_int(v: Any) -> int | None:
    if v is None:
        return None
    if isinstance(v, int):
        return v
    s = str(v).strip()
    if not s:
        return None
    return int(s)


def normalize_name(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\\s+", " ", s).strip()
    return s


def source_record(table: str, record_id: str) -> str:
    return f"{table}:{record_id}"


class Importer:
    def __init__(self, *, src: sqlite3.Connection, dst: sqlite3.Connection, output_dir: Path) -> None:
        self.src = src
        self.dst = dst
        self.output_dir = output_dir
        self.warnings: list[str] = []
        self.counts: Counter[str] = Counter()

        self.entity_id: int | None = None
        self.source_db_file_id: int | None = None

        self.accounts_by_code: dict[str, int] = {}
        self.cash_account_id: int | None = None

        self.txn_id_by_bank_txn_id: dict[str, int] = {}
        self.txn_id_by_cc_txn_id: dict[str, int] = {}
        self.txn_amount_by_txn_id: dict[int, int] = {}

        self.doc_id_by_wave_bill_id: dict[str, int] = {}
        self.doc_id_by_invoice_number: dict[str, int] = {}

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def insert_one(self, sql: str, params: tuple[Any, ...]) -> int:
        cur = self.dst.execute(sql, params)
        return int(cur.lastrowid)

    def upsert_entity(self, entity_key: str, name: str) -> int:
        row = self.dst.execute("SELECT id FROM entities WHERE entity_key=?", (entity_key,)).fetchone()
        if row:
            return int(row["id"])
        return self.insert_one("INSERT INTO entities(entity_key, name) VALUES (?, ?)", (entity_key, name))

    def upsert_source_file(
        self, *, source_key: str, kind: str, path: str, sha256: str | None, semantics: str | None
    ) -> int:
        row = self.dst.execute("SELECT id FROM source_files WHERE source_key=?", (source_key,)).fetchone()
        if row:
            return int(row["id"])
        return self.insert_one(
            "INSERT INTO source_files(source_key, kind, path, sha256, semantics) VALUES (?, ?, ?, ?, ?)",
            (source_key, kind, path, sha256, semantics),
        )

    def insert_account(self, *, entity_id: int, account_key: str, account_type: str, name: str, notes: str | None) -> int:
        return self.insert_one(
            """
            INSERT INTO accounts(entity_id, account_key, account_type, name, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (entity_id, account_key, account_type, name, notes),
        )

    def insert_txn(
        self,
        *,
        entity_id: int,
        account_id: int,
        txn_date: str,
        description: str,
        amount_cents: int,
        debit_cents: int | None,
        credit_cents: int | None,
        txn_type: str | None,
        counterparty_raw: str | None,
        reference: str | None,
        source_record_id: str,
        source_file_id: int | None,
        raw: dict[str, Any],
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO account_transactions(
              entity_id, account_id, txn_date, description, amount_cents,
              debit_cents, credit_cents, txn_type, counterparty_raw, reference,
              source_system, source_record_id, source_file_id, raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                entity_id,
                account_id,
                txn_date,
                description,
                amount_cents,
                debit_cents,
                credit_cents,
                txn_type,
                counterparty_raw,
                reference,
                SOURCE_SYSTEM,
                source_record_id,
                source_file_id,
                json.dumps(raw, ensure_ascii=False, sort_keys=True),
            ),
        )

    def upsert_counterparty(self, *, name: str, kind: str) -> int:
        norm = normalize_name(name)
        row = self.dst.execute(
            "SELECT id FROM counterparties WHERE normalized_name=? AND kind=?",
            (norm, kind),
        ).fetchone()
        if row:
            return int(row["id"])
        return self.insert_one(
            "INSERT INTO counterparties(name, normalized_name, kind) VALUES (?, ?, ?)",
            (name.strip(), norm, kind),
        )

    def insert_document(
        self,
        *,
        entity_id: int,
        counterparty_id: int | None,
        doc_type: str,
        doc_date: str | None,
        due_date: str | None,
        doc_number: str | None,
        total_cents: int | None,
        tax_cents: int | None,
        net_cents: int | None,
        status: str | None,
        source_record_id: str,
        source_file_id: int | None,
        raw: dict[str, Any],
        notes: str | None,
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO documents(
              entity_id, counterparty_id, doc_type, doc_date, due_date, doc_number,
              total_cents, tax_cents, net_cents, status,
              source_system, source_record_id, source_file_id, raw_json, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                entity_id,
                counterparty_id,
                doc_type,
                doc_date,
                due_date,
                doc_number,
                total_cents,
                tax_cents,
                net_cents,
                status,
                SOURCE_SYSTEM,
                source_record_id,
                source_file_id,
                json.dumps(raw, ensure_ascii=False, sort_keys=True),
                notes,
            ),
        )

    def insert_txn_classification(
        self,
        *,
        txn_id: int,
        namespace: str,
        category: str,
        counterparty_id: int | None,
        explanation: str | None,
        confidence: int | None,
        is_verified: bool,
        role: str,
        method: str | None,
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO txn_classifications(
              txn_id, namespace, category, counterparty_id, explanation,
              confidence, is_verified, role, method
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                txn_id,
                namespace,
                category,
                counterparty_id,
                explanation,
                confidence,
                1 if is_verified else 0,
                role,
                method,
            ),
        )

    def insert_txn_document_allocation(
        self,
        *,
        txn_id: int,
        document_id: int,
        amount_cents: int,
        allocation_type: str,
        confidence: int | None,
        is_verified: bool,
        role: str,
        method: str | None,
        notes: str | None,
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO txn_document_allocations(
              txn_id, document_id, amount_cents, allocation_type,
              confidence, is_verified, role, method, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                txn_id,
                document_id,
                amount_cents,
                allocation_type,
                confidence,
                1 if is_verified else 0,
                role,
                method,
                notes,
            ),
        )

    def insert_txn_link(
        self,
        *,
        from_txn_id: int,
        to_txn_id: int,
        link_type: str,
        amount_cents: int,
        confidence: int | None,
        is_verified: bool,
        role: str,
        method: str | None,
        notes: str | None,
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO txn_links(
              from_txn_id, to_txn_id, link_type, amount_cents,
              confidence, is_verified, role, method, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                from_txn_id,
                to_txn_id,
                link_type,
                amount_cents,
                confidence,
                1 if is_verified else 0,
                role,
                method,
                notes,
            ),
        )

    def insert_settlement_batch(
        self,
        *,
        entity_id: int,
        counterparty_id: int | None,
        settlement_type: str,
        statement_date: str | None,
        due_date: str | None,
        total_cents: int,
        source_record_id: str,
        source_file_id: int | None,
        raw: dict[str, Any],
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO settlement_batches(
              entity_id, counterparty_id, settlement_type,
              statement_date, due_date, total_cents,
              source_system, source_record_id, source_file_id, raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                entity_id,
                counterparty_id,
                settlement_type,
                statement_date,
                due_date,
                total_cents,
                SOURCE_SYSTEM,
                source_record_id,
                source_file_id,
                json.dumps(raw, ensure_ascii=False, sort_keys=True),
            ),
        )

    def insert_settlement_line(
        self,
        *,
        batch_id: int,
        line_no: int,
        external_doc_number: str | None,
        line_type: str,
        amount_cents: int,
        txn_date: str | None,
        due_date: str | None,
        description: str | None,
        linked_document_id: int | None,
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO settlement_lines(
              batch_id, line_no, external_doc_number, line_type, amount_cents,
              txn_date, due_date, description, linked_document_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                batch_id,
                line_no,
                external_doc_number,
                line_type,
                amount_cents,
                txn_date,
                due_date,
                description,
                linked_document_id,
            ),
        )

    def insert_settlement_batch_txn_link(
        self,
        *,
        batch_id: int,
        txn_id: int,
        link_type: str,
        confidence: int | None,
        is_verified: bool,
        notes: str | None,
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO settlement_batch_txn_links(
              batch_id, txn_id, link_type, confidence, is_verified, notes
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (batch_id, txn_id, link_type, confidence, 1 if is_verified else 0, notes),
        )

    def insert_cash_deposit_group(
        self, *, entity_id: int, group_date: str, effective_cash_deposit_cents: int, notes: str | None
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO cash_deposit_groups(entity_id, group_date, effective_cash_deposit_cents, notes)
            VALUES (?, ?, ?, ?)
            """,
            (entity_id, group_date, effective_cash_deposit_cents, notes),
        )

    def insert_cash_deposit_group_txn(
        self, *, cash_deposit_group_id: int, txn_id: int, role: str, notes: str | None
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO cash_deposit_group_txns(cash_deposit_group_id, txn_id, role, notes)
            VALUES (?, ?, ?, ?)
            """,
            (cash_deposit_group_id, txn_id, role, notes),
        )

    def insert_gateway_report(
        self,
        *,
        entity_id: int,
        report_start: str | None,
        report_end: str | None,
        report_name: str | None,
        source_record_id: str,
        source_file_id: int | None,
        raw: dict[str, Any],
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO gateway_reports(
              entity_id, report_start, report_end, report_name,
              source_system, source_record_id, source_file_id, raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                entity_id,
                report_start,
                report_end,
                report_name,
                SOURCE_SYSTEM,
                source_record_id,
                source_file_id,
                json.dumps(raw, ensure_ascii=False, sort_keys=True),
            ),
        )

    def insert_gateway_report_row(
        self,
        *,
        report_id: int,
        source_row: str | None,
        payment_gateway: str | None,
        net_payments_cents: int | None,
        gross_payments_cents: int | None,
        refunded_payments_cents: int | None,
        raw: dict[str, Any],
    ) -> int:
        return self.insert_one(
            """
            INSERT INTO gateway_report_rows(
              report_id, source_row, payment_gateway,
              net_payments_cents, gross_payments_cents, refunded_payments_cents,
              raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                report_id,
                source_row,
                payment_gateway,
                net_payments_cents,
                gross_payments_cents,
                refunded_payments_cents,
                json.dumps(raw, ensure_ascii=False, sort_keys=True),
            ),
        )

    def run(self, *, entity_key: str, entity_name: str, source_db_path: Path, source_sha256: str) -> None:
        self.dst.execute("BEGIN")

        self.entity_id = self.upsert_entity(entity_key, entity_name)
        self.source_db_file_id = self.upsert_source_file(
            source_key=f"t2_final.db:{source_sha256}",
            kind="SQLITE_DB",
            path=str(source_db_path),
            sha256=source_sha256,
            semantics="Frozen reconciliation snapshot DB (read-only import source).",
        )

        assert self.entity_id is not None
        assert self.source_db_file_id is not None

        self.import_accounts()
        self.import_bank_transactions()
        self.import_cc_transactions()
        self.import_wave_bills()
        self.import_cash_reimbursements()
        self.import_evidence_allocations()
        self.import_cc_chain_links()
        self.import_txn_classifications()
        self.import_shopify_payouts()
        self.import_gateway_reports()
        self.import_cash_deposit_groups()
        self.import_gfs_eft()
        self.import_pad_payments()

        self.dst.commit()

    def import_accounts(self) -> None:
        assert self.entity_id is not None

        for r in self.src.execute("SELECT * FROM fresher_debits__accounts ORDER BY id"):
            at = (r["account_type"] or "").strip().lower()
            account_type = {
                "bank": "BANK",
                "credit_card": "CREDIT_CARD",
                "debit_card": "DEBIT_CARD",
            }.get(at, at.upper() or "OTHER")
            code = str(r["code"])
            self.accounts_by_code[code] = self.insert_account(
                entity_id=self.entity_id,
                account_key=code,
                account_type=account_type,
                name=str(r["name"]),
                notes=None,
            )

        if "CANTEEN_BANK" not in self.accounts_by_code:
            raise SystemExit("Expected fresher_debits__accounts to include CANTEEN_BANK")

        self.cash_account_id = self.insert_account(
            entity_id=self.entity_id,
            account_key="CASH_TILL",
            account_type="CASH",
            name="Cash Till (pseudo-account)",
            notes="Represents off-bank cash payments/reimbursements used in reconciliation.",
        )

    def import_bank_transactions(self) -> None:
        assert self.entity_id is not None
        assert self.source_db_file_id is not None

        bank_account_id = self.accounts_by_code["CANTEEN_BANK"]
        for r in self.src.execute("SELECT * FROM fresher_debits__bank_transactions ORDER BY CAST(id AS INTEGER)"):
            txn_date = str(r["txn_date"] or "").strip()
            if not in_scope(txn_date):
                continue
            bank_txn_id = str(r["id"])
            debit = parse_int(r["debit_cents"]) or 0
            credit = parse_int(r["credit_cents"]) or 0
            amount = int(credit) - int(debit)
            txn_id = self.insert_txn(
                entity_id=self.entity_id,
                account_id=bank_account_id,
                txn_date=txn_date,
                description=str(r["description"]),
                amount_cents=amount,
                debit_cents=debit if debit else None,
                credit_cents=credit if credit else None,
                txn_type=(r["txn_type"] or None),
                counterparty_raw=(r["vendor_parsed"] or r["etransfer_recipient"] or None),
                reference=(r["reference_number"] or None),
                source_record_id=source_record("fresher_debits__bank_transactions", bank_txn_id),
                source_file_id=self.source_db_file_id,
                raw=dict(r),
            )
            self.txn_id_by_bank_txn_id[bank_txn_id] = txn_id
            self.txn_amount_by_txn_id[txn_id] = amount
            self.counts["account_transactions"] += 1

    def import_cc_transactions(self) -> None:
        assert self.entity_id is not None
        assert self.source_db_file_id is not None

        acct_code_by_account_id = {str(r["id"]): str(r["code"]) for r in self.src.execute("SELECT id, code FROM fresher_debits__accounts")}
        for r in self.src.execute("SELECT * FROM fresher_debits__cc_transactions ORDER BY CAST(id AS INTEGER)"):
            txn_date = str(r["txn_date"] or "").strip()
            if not in_scope(txn_date):
                continue
            cc_txn_id = str(r["id"])
            acct_code = acct_code_by_account_id.get(str(r["account_id"]))
            if not acct_code:
                self.warn(f"cc_txn_id={cc_txn_id}: unknown account_id={r['account_id']}")
                continue
            account_id = self.accounts_by_code.get(acct_code)
            if not account_id:
                self.warn(f"cc_txn_id={cc_txn_id}: missing mapped account for code={acct_code}")
                continue
            debit = parse_int(r["debit_cents"]) or 0
            credit = parse_int(r["credit_cents"]) or 0
            amount = int(credit) - int(debit)
            txn_id = self.insert_txn(
                entity_id=self.entity_id,
                account_id=account_id,
                txn_date=txn_date,
                description=str(r["description"]),
                amount_cents=amount,
                debit_cents=debit if debit else None,
                credit_cents=credit if credit else None,
                txn_type=(r["txn_type"] or None),
                counterparty_raw=(r["merchant_parsed"] or None),
                reference=None,
                source_record_id=source_record("fresher_debits__cc_transactions", cc_txn_id),
                source_file_id=self.source_db_file_id,
                raw=dict(r),
            )
            self.txn_id_by_cc_txn_id[cc_txn_id] = txn_id
            self.txn_amount_by_txn_id[txn_id] = amount
            self.counts["account_transactions"] += 1

    def import_wave_bills(self) -> None:
        assert self.entity_id is not None
        assert self.source_db_file_id is not None

        for r in self.src.execute("SELECT * FROM fresher_debits__wave_bills ORDER BY CAST(id AS INTEGER)"):
            invoice_date = str(r["invoice_date"] or "").strip()
            if not in_scope(invoice_date):
                continue
            wave_bill_id = str(r["id"])
            vendor = str(r["vendor_normalized"] or r["vendor_raw"] or "").strip() or "UNKNOWN"
            counterparty_id = self.upsert_counterparty(name=vendor, kind="VENDOR")

            invoice_number = str(r["invoice_number"] or "").strip() or None
            total = parse_int(r["total_cents"])
            doc_type = "CREDIT_MEMO" if (total is not None and total < 0) else "BILL"
            doc_id = self.insert_document(
                entity_id=self.entity_id,
                counterparty_id=counterparty_id,
                doc_type=doc_type,
                doc_date=invoice_date or None,
                due_date=None,
                doc_number=invoice_number,
                total_cents=total,
                tax_cents=parse_int(r["tax_cents"]),
                net_cents=parse_int(r["net_cents"]),
                status=None,
                source_record_id=source_record("fresher_debits__wave_bills", wave_bill_id),
                source_file_id=self.source_db_file_id,
                raw=dict(r),
                notes=(r["vendor_category"] or None),
            )

            self.doc_id_by_wave_bill_id[wave_bill_id] = doc_id
            if invoice_number:
                self.doc_id_by_invoice_number[invoice_number] = doc_id
            self.counts["documents"] += 1

    def import_cash_reimbursements(self) -> None:
        assert self.entity_id is not None
        assert self.source_db_file_id is not None
        assert self.cash_account_id is not None

        wave_bill_by_id = {
            str(r["id"]): r
            for r in self.src.execute("SELECT id, invoice_date, total_cents FROM fresher_debits__wave_bills")
        }

        for r in self.src.execute("SELECT * FROM fresher_debits__cash_reimbursements ORDER BY CAST(id AS INTEGER)"):
            wave_bill_id = str(r["wave_bill_id"])
            doc_id = self.doc_id_by_wave_bill_id.get(wave_bill_id)
            if not doc_id:
                # Out-of-scope Wave bills are intentionally not imported.
                continue
            bill_row = wave_bill_by_id.get(wave_bill_id)
            txn_date = str(r["reimbursement_date"] or (bill_row["invoice_date"] if bill_row else None) or "1970-01-01")
            if not in_scope(txn_date):
                continue

            amt = parse_int(r["amount_cents"]) or 0
            txn_amount = -abs(int(amt))
            txn_id = self.insert_txn(
                entity_id=self.entity_id,
                account_id=self.cash_account_id,
                txn_date=txn_date,
                description=f"CASH_REIMBURSE: {r['notes'] or ''}".strip(),
                amount_cents=txn_amount,
                debit_cents=abs(int(amt)) if amt else None,
                credit_cents=None,
                txn_type="CASH_REIMBURSE",
                counterparty_raw=(r["reimbursed_to"] or None),
                reference=None,
                source_record_id=source_record("fresher_debits__cash_reimbursements", str(r["id"])),
                source_file_id=self.source_db_file_id,
                raw=dict(r),
            )
            self.txn_amount_by_txn_id[txn_id] = txn_amount
            self.counts["account_transactions"] += 1

            self.insert_txn_document_allocation(
                txn_id=txn_id,
                document_id=doc_id,
                amount_cents=txn_amount,
                allocation_type="PAYMENT",
                confidence=100,
                is_verified=True,
                role="EVIDENCE",
                method="fresher_debits__cash_reimbursements",
                notes=(r["notes"] or None),
            )
            self.counts["txn_document_allocations"] += 1

    def import_evidence_allocations(self) -> None:
        # wave_bill_funding (bank only)
        for r in self.src.execute(
            """
            SELECT * FROM fresher_debits__wave_bill_funding
            WHERE funding_type IN ('BANK_DIRECT','BANK_SPLIT','BANK_CC_CHAIN')
            ORDER BY CAST(id AS INTEGER)
            """
        ):
            wave_bill_id = str(r["wave_bill_id"])
            doc_id = self.doc_id_by_wave_bill_id.get(wave_bill_id)
            if not doc_id:
                # Out-of-scope Wave bills are intentionally not imported.
                continue
            bank_txn_id = str(r["bank_txn_id"] or "").strip()
            if not bank_txn_id:
                self.warn(f"wave_bill_funding id={r['id']}: missing bank_txn_id for bank funding")
                continue
            txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id)
            if not txn_id:
                # Bank txns outside FY scope are intentionally not imported.
                continue
            amt = parse_int(r["amount_cents"]) or 0
            txn_amt = self.txn_amount_by_txn_id.get(txn_id, 0)
            sign = -1 if txn_amt < 0 else 1
            alloc_amount = sign * abs(int(amt))
            self.insert_txn_document_allocation(
                txn_id=txn_id,
                document_id=doc_id,
                amount_cents=alloc_amount,
                allocation_type="PAYMENT",
                confidence=None,
                is_verified=False,
                role="EVIDENCE",
                method="fresher_debits__wave_bill_funding",
                notes=(r["notes"] or None),
            )
            self.counts["txn_document_allocations"] += 1

        # split_payments
        for r in self.src.execute("SELECT * FROM fresher_debits__split_payments ORDER BY CAST(id AS INTEGER)"):
            wave_bill_id = str(r["wave_bill_id"])
            doc_id = self.doc_id_by_wave_bill_id.get(wave_bill_id)
            if not doc_id:
                # Out-of-scope Wave bills are intentionally not imported.
                continue
            txn_type = str(r["txn_type"]).upper()
            txn_lookup_id = str(r["txn_id"])
            if txn_type == "BANK":
                txn_id = self.txn_id_by_bank_txn_id.get(txn_lookup_id)
            elif txn_type == "CC":
                txn_id = self.txn_id_by_cc_txn_id.get(txn_lookup_id)
            else:
                self.warn(f"split_payments id={r['id']}: unknown txn_type={txn_type}")
                continue
            if not txn_id:
                # Txns outside FY scope are intentionally not imported.
                continue
            amt = parse_int(r["amount_cents"]) or 0
            txn_amt = self.txn_amount_by_txn_id.get(txn_id, 0)
            sign = -1 if txn_amt < 0 else 1
            alloc_amount = sign * abs(int(amt))
            self.insert_txn_document_allocation(
                txn_id=txn_id,
                document_id=doc_id,
                amount_cents=alloc_amount,
                allocation_type="PAYMENT",
                confidence=100,
                is_verified=True,
                role="EVIDENCE",
                method="fresher_debits__split_payments",
                notes=None,
            )
            self.counts["txn_document_allocations"] += 1

        # bank_allocations (known to be inconsistent; imported for completeness only)
        for r in self.src.execute(
            "SELECT * FROM fresher_debits__bank_allocations WHERE target_type='WAVE_BILL' ORDER BY CAST(id AS INTEGER)"
        ):
            wave_bill_id = str(r["target_id"])
            doc_id = self.doc_id_by_wave_bill_id.get(wave_bill_id)
            if not doc_id:
                # Out-of-scope Wave bills are intentionally not imported.
                continue
            bank_txn_id = str(r["bank_txn_id"])
            txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id)
            if not txn_id:
                # Bank txns outside FY scope are intentionally not imported.
                continue
            amt = parse_int(r["amount_cents"]) or 0
            txn_amt = self.txn_amount_by_txn_id.get(txn_id, 0)
            sign = -1 if txn_amt < 0 else 1
            alloc_amount = sign * abs(int(amt))
            self.insert_txn_document_allocation(
                txn_id=txn_id,
                document_id=doc_id,
                amount_cents=alloc_amount,
                allocation_type="OTHER",
                confidence=None,
                is_verified=False,
                role="EVIDENCE",
                method="fresher_debits__bank_allocations",
                notes=(r["notes"] or None),
            )
            self.counts["txn_document_allocations"] += 1

        # wave_matches (use txn amount for CC matches; bill total for bank matches)
        wave_bill_totals = {str(r["id"]): (parse_int(r["total_cents"]) or 0) for r in self.src.execute("SELECT id, total_cents FROM fresher_debits__wave_bills")}
        for r in self.src.execute("SELECT * FROM fresher_debits__wave_matches ORDER BY CAST(id AS INTEGER)"):
            wave_bill_id = str(r["wave_bill_id"])
            doc_id = self.doc_id_by_wave_bill_id.get(wave_bill_id)
            if not doc_id:
                # Orphaned match row: the underlying Wave bill no longer exists in the snapshot.
                # For T2 filing purposes we skip silently (no allocations can be created).
                continue
            cc_txn_id_raw = str(r["cc_txn_id"] or "").strip()
            bank_txn_id_raw = str(r["bank_txn_id"] or "").strip()
            note = f"match_type={r['match_type']} method={r['match_method']} conf={r['confidence']} notes={r['notes'] or ''}".strip()

            if cc_txn_id_raw:
                txn_id = self.txn_id_by_cc_txn_id.get(cc_txn_id_raw)
                if not txn_id:
                    continue
                alloc_amount = self.txn_amount_by_txn_id.get(txn_id)
                if alloc_amount is None:
                    alloc_amount = -abs(int(wave_bill_totals.get(wave_bill_id, 0)))
                self.insert_txn_document_allocation(
                    txn_id=txn_id,
                    document_id=doc_id,
                    amount_cents=int(alloc_amount),
                    allocation_type="PAYMENT",
                    confidence=None,
                    is_verified=False,
                    role="EVIDENCE",
                    method="fresher_debits__wave_matches",
                    notes=note,
                )
                self.counts["txn_document_allocations"] += 1
                continue

            if bank_txn_id_raw:
                txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id_raw)
                if not txn_id:
                    continue
                total = int(wave_bill_totals.get(wave_bill_id, 0))
                txn_amt = self.txn_amount_by_txn_id.get(txn_id, 0)
                sign = -1 if txn_amt < 0 else 1
                alloc_amount = sign * abs(total)
                self.insert_txn_document_allocation(
                    txn_id=txn_id,
                    document_id=doc_id,
                    amount_cents=alloc_amount,
                    allocation_type="PAYMENT",
                    confidence=None,
                    is_verified=False,
                    role="EVIDENCE",
                    method="fresher_debits__wave_matches",
                    notes=note,
                )
                self.counts["txn_document_allocations"] += 1

    def import_cc_chain_links(self) -> None:
        # cc_payment_links: bank debit -> cc payment credit
        for r in self.src.execute("SELECT * FROM fresher_debits__cc_payment_links ORDER BY CAST(id AS INTEGER)"):
            bank_txn_id = str(r["bank_txn_id"])
            cc_txn_id = str(r["cc_txn_id"])
            from_txn = self.txn_id_by_bank_txn_id.get(bank_txn_id)
            to_txn = self.txn_id_by_cc_txn_id.get(cc_txn_id)
            if not from_txn or not to_txn:
                continue
            amt = parse_int(r["amount_cents"]) or 0
            from_amt = self.txn_amount_by_txn_id.get(from_txn, 0)
            sign = -1 if from_amt < 0 else 1
            link_amount = sign * abs(int(amt))
            self.insert_txn_link(
                from_txn_id=from_txn,
                to_txn_id=to_txn,
                link_type="BANK_TO_CARD_PAYMENT",
                amount_cents=link_amount,
                confidence=100,
                is_verified=True,
                role="EVIDENCE",
                method="fresher_debits__cc_payment_links",
                notes=f"card_last4={r['card_last4']} date_diff_days={r['date_diff_days']}",
            )
            self.counts["txn_links"] += 1

        # cc_credit_allocations: cc payment credit -> cc purchase debit (allocation)
        for r in self.src.execute("SELECT * FROM fresher_debits__cc_credit_allocations ORDER BY CAST(id AS INTEGER)"):
            credit_cc_txn_id = str(r["credit_cc_txn_id"])
            debit_cc_txn_id = str(r["debit_cc_txn_id"])
            from_txn = self.txn_id_by_cc_txn_id.get(credit_cc_txn_id)
            to_txn = self.txn_id_by_cc_txn_id.get(debit_cc_txn_id)
            if not from_txn or not to_txn:
                continue
            amt = parse_int(r["allocated_cents"]) or 0
            self.insert_txn_link(
                from_txn_id=from_txn,
                to_txn_id=to_txn,
                link_type="CARD_PAYMENT_TO_PURCHASE",
                amount_cents=abs(int(amt)),
                confidence=None,
                is_verified=False,
                role="EVIDENCE",
                method="fresher_debits__cc_credit_allocations",
                notes=f"method={r['method']} bank_txn_id={r['bank_txn_id']}",
            )
            self.counts["txn_links"] += 1

    def import_txn_classifications(self) -> None:
        # debit-side
        for r in self.src.execute("SELECT * FROM fresher_debits__bank_txn_classifications ORDER BY CAST(id AS INTEGER)"):
            bank_txn_id = str(r["bank_txn_id"])
            txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id)
            if not txn_id:
                # Bank txns outside FY scope are intentionally not imported.
                continue
            explanation = (r["explanation"] or "").strip() or None
            wave_bill_ids = (r["wave_bill_ids"] or "").strip()
            if wave_bill_ids:
                explanation = (explanation + " | wave_bill_ids=" + wave_bill_ids).strip(" |")
            verified = str(r["verified"]) == "1"
            self.insert_txn_classification(
                txn_id=txn_id,
                namespace="FRESHER_DEBITS",
                category=str(r["txn_category"]),
                counterparty_id=None,
                explanation=explanation,
                confidence=100 if verified else None,
                is_verified=verified,
                role="EVIDENCE",
                method="fresher_debits__bank_txn_classifications",
            )
            self.counts["txn_classifications"] += 1

        # credit-side (mapped via credit_bank_items → bank_txn_id)
        bank_txn_id_by_credit_bank_item_id = {
            str(r["id"]): str(r["bank_txn_id"])
            for r in self.src.execute("SELECT id, bank_txn_id FROM fresher_credits__credit_bank_items")
            if r["bank_txn_id"]
        }
        for r in self.src.execute("SELECT * FROM fresher_credits__credit_item_classifications ORDER BY created_at, id"):
            bank_item_id = str(r["bank_item_id"])
            bank_txn_id = bank_txn_id_by_credit_bank_item_id.get(bank_item_id)
            if not bank_txn_id:
                continue
            txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id)
            if not txn_id:
                # Bank txns outside FY scope are intentionally not imported.
                continue
            counterparty_raw = (r["counterparty"] or "").strip()
            counterparty_id = self.upsert_counterparty(name=counterparty_raw, kind="OTHER") if counterparty_raw else None
            verified = str(r["is_verified"]) == "1"
            self.insert_txn_classification(
                txn_id=txn_id,
                namespace="FRESHER_CREDITS",
                category=str(r["category"]),
                counterparty_id=counterparty_id,
                explanation=(r["explanation"] or None),
                confidence=parse_int(r["confidence"]),
                is_verified=verified,
                role="EVIDENCE",
                method=(r["classification_method"] or None),
            )
            self.counts["txn_classifications"] += 1

    def import_shopify_payouts(self) -> None:
        assert self.entity_id is not None
        assert self.source_db_file_id is not None

        shopify_counterparty_id = self.upsert_counterparty(name="Shopify Payments", kind="PLATFORM")
        payout_batch_id_by_payout_id: dict[str, int] = {}

        for r in self.src.execute("SELECT * FROM fresher_credits__shopify_payouts ORDER BY payout_date, id"):
            payout_date = str(r["payout_date"] or "").strip()
            if not in_scope(payout_date):
                continue
            payout_id = str(r["id"])
            total = parse_int(r["total_cents"]) or 0
            batch_id = self.insert_settlement_batch(
                entity_id=self.entity_id,
                counterparty_id=shopify_counterparty_id,
                settlement_type="SHOPIFY_PAYOUT",
                statement_date=payout_date or None,
                due_date=payout_date or None,
                total_cents=int(total),
                source_record_id=source_record("fresher_credits__shopify_payouts", payout_id),
                source_file_id=self.source_db_file_id,
                raw=dict(r),
            )
            payout_batch_id_by_payout_id[payout_id] = batch_id
            self.counts["settlement_batches"] += 1

            # Decomposition lines (signed so sum == total)
            charges = parse_int(r["charges_cents"]) or 0
            refunds = parse_int(r["refunds_cents"]) or 0
            fees = parse_int(r["fees_cents"]) or 0
            adjustments = parse_int(r["adjustments_cents"]) or 0

            components = [
                ("CHARGES", int(charges)),
                ("REFUNDS", -abs(int(refunds))),
                ("ADJUSTMENTS", int(adjustments)),
                ("FEES", -abs(int(fees))),
            ]
            line_no = 1
            for line_type, amount in components:
                if amount == 0:
                    continue
                self.insert_settlement_line(
                    batch_id=batch_id,
                    line_no=line_no,
                    external_doc_number=None,
                    line_type=line_type,
                    amount_cents=int(amount),
                    txn_date=payout_date or None,
                    due_date=payout_date or None,
                    description=None,
                    linked_document_id=None,
                )
                line_no += 1
                self.counts["settlement_lines"] += 1

        for r in self.src.execute("SELECT * FROM fresher_credits__shopify_payout_bank_links ORDER BY matched_at, id"):
            payout_id = str(r["payout_id"])
            batch_id = payout_batch_id_by_payout_id.get(payout_id)
            if not batch_id:
                # Likely out-of-scope payout; ignore.
                continue
            bank_txn_id = str(r["bank_txn_id"] or "").strip()
            if not bank_txn_id:
                self.warn(f"shopify_payout_bank_links id={r['id']}: missing bank_txn_id")
                continue
            txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id)
            if not txn_id:
                self.warn(f"shopify_payout_bank_links id={r['id']}: unknown/inaccessible bank_txn_id={bank_txn_id}")
                continue
            self.insert_settlement_batch_txn_link(
                batch_id=batch_id,
                txn_id=txn_id,
                link_type=str(r["match_method"] or "MATCH"),
                confidence=parse_int(r["match_confidence"]),
                is_verified=True,
                notes=(r["match_notes"] or None),
            )
            self.counts["settlement_batch_txn_links"] += 1

    def import_gateway_reports(self) -> None:
        assert self.entity_id is not None
        assert self.source_db_file_id is not None

        report_id_by_src: dict[str, int] = {}
        for r in self.src.execute(
            "SELECT * FROM fresher_credits__shopify_net_payment_gateway_reports ORDER BY report_start, id"
        ):
            report_start = str(r["report_start"] or "").strip()
            report_end = str(r["report_end"] or "").strip()
            if not (in_scope(report_start) and in_scope(report_end)):
                continue
            rid = str(r["id"])
            report_id = self.insert_gateway_report(
                entity_id=self.entity_id,
                report_start=report_start or None,
                report_end=report_end or None,
                report_name=(r["report_name"] or None),
                source_record_id=source_record("fresher_credits__shopify_net_payment_gateway_reports", rid),
                source_file_id=self.source_db_file_id,
                raw=dict(r),
            )
            report_id_by_src[rid] = report_id
            self.counts["gateway_reports"] += 1

        for r in self.src.execute(
            "SELECT * FROM fresher_credits__shopify_net_payment_gateway_rows ORDER BY report_id, source_row, id"
        ):
            src_report_id = str(r["report_id"])
            report_id = report_id_by_src.get(src_report_id)
            if not report_id:
                # Likely out-of-scope report; ignore.
                continue
            self.insert_gateway_report_row(
                report_id=report_id,
                source_row=(r["source_row"] or None),
                payment_gateway=(r["payment_gateway"] or None),
                net_payments_cents=parse_int(r["net_payments_cents"]),
                gross_payments_cents=parse_int(r["gross_payments_cents"]),
                refunded_payments_cents=parse_int(r["refunded_payments_cents"]),
                raw=dict(r),
            )
            self.counts["gateway_report_rows"] += 1

    def import_cash_deposit_groups(self) -> None:
        assert self.entity_id is not None

        bank_txn_id_by_credit_bank_item_id = {
            str(r["id"]): str(r["bank_txn_id"])
            for r in self.src.execute("SELECT id, bank_txn_id FROM fresher_credits__credit_bank_items")
            if r["bank_txn_id"]
        }

        for r in self.src.execute("SELECT * FROM fresher_credits__cash_deposit_groups ORDER BY group_date"):
            group_date = str(r["group_date"] or "").strip()
            if not in_scope(group_date):
                continue
            group_id = self.insert_cash_deposit_group(
                entity_id=self.entity_id,
                group_date=group_date,
                effective_cash_deposit_cents=parse_int(r["effective_cash_deposit_cents"]) or 0,
                notes=(r["notes"] or None),
            )
            self.counts["cash_deposit_groups"] += 1

            def link_items(item_ids_json: str, role: str) -> None:
                try:
                    ids = json.loads(item_ids_json or "[]")
                except Exception:
                    self.warn(f"cash_deposit_groups group_date={r['group_date']}: invalid JSON for {role}: {item_ids_json}")
                    return
                for bank_item_id in ids:
                    bank_txn_id = bank_txn_id_by_credit_bank_item_id.get(str(bank_item_id))
                    if not bank_txn_id:
                        self.warn(
                            f"cash_deposit_groups group_date={r['group_date']}: bank_item_id missing bank_txn_id {bank_item_id}"
                        )
                        continue
                    txn_id = self.txn_id_by_bank_txn_id.get(str(bank_txn_id))
                    if not txn_id:
                        self.warn(f"cash_deposit_groups group_date={r['group_date']}: unknown bank_txn_id={bank_txn_id}")
                        continue
                    self.insert_cash_deposit_group_txn(
                        cash_deposit_group_id=group_id,
                        txn_id=txn_id,
                        role=role,
                        notes=None,
                    )
                    self.counts["cash_deposit_group_txns"] += 1

            link_items(str(r["deposit_bank_item_ids"]), "DEPOSIT")
            link_items(str(r["correction_bank_item_ids"]), "CORRECTION")

            m = re.search(r"internal_transfer_out_bank_txn_id=(\\d+)", str(r["notes"] or ""))
            if m:
                bank_txn_id = m.group(1)
                txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id)
                if txn_id:
                    self.insert_cash_deposit_group_txn(
                        cash_deposit_group_id=group_id,
                        txn_id=txn_id,
                        role="INTERNAL_TRANSFER_OUT",
                        notes="Referenced by cash deposit group note",
                    )
                    self.counts["cash_deposit_group_txns"] += 1
                else:
                    self.warn(
                        f"cash_deposit_groups group_date={r['group_date']}: internal_transfer_out_bank_txn_id not found {bank_txn_id}"
                    )

    def import_gfs_eft(self) -> None:
        assert self.entity_id is not None
        assert self.source_db_file_id is not None

        gfs_counterparty_id = self.upsert_counterparty(name="Gordon Food Service Canada Ltd", kind="VENDOR")

        batch_id_by_notification_id: dict[str, int] = {}
        source_file_id_by_hash: dict[str, int] = {}

        for r in self.src.execute("SELECT * FROM fresher_credits__gfs_eft_notifications ORDER BY due_date, id"):
            nid = str(r["id"])
            due_date = str(r["due_date"] or "").strip()
            if not in_scope(due_date):
                continue
            file_hash = str(r["file_hash_sha256"] or "").strip()
            file_id = self.source_db_file_id
            if file_hash:
                file_id = source_file_id_by_hash.get(file_hash) or self.upsert_source_file(
                    source_key=f"gfs_eft:{file_hash}",
                    kind="GFS_EFT",
                    path=str(r["file_path"] or ""),
                    sha256=file_hash,
                    semantics=f"GFS EFT notification file {r['file_name']}",
                )
                source_file_id_by_hash[file_hash] = file_id

            total = parse_int(r["total_net_cents"]) or 0
            batch_id = self.insert_settlement_batch(
                entity_id=self.entity_id,
                counterparty_id=gfs_counterparty_id,
                settlement_type="GFS_EFT",
                statement_date=due_date or None,
                due_date=due_date or None,
                total_cents=int(total),
                source_record_id=source_record("fresher_credits__gfs_eft_notifications", nid),
                source_file_id=file_id,
                raw=dict(r),
            )
            batch_id_by_notification_id[nid] = batch_id
            self.counts["settlement_batches"] += 1

        # Lines + placeholder docs for missing Wave invoice_number
        placeholder_doc_by_invoice_number: dict[str, int] = {}
        for nid, batch_id in batch_id_by_notification_id.items():
            rows = self.src.execute(
                "SELECT * FROM fresher_credits__gfs_eft_notification_lines WHERE notification_id=? ORDER BY id",
                (nid,),
            ).fetchall()
            for idx, r in enumerate(rows, start=1):
                invoice_number = str(r["invoice_number"] or "").strip() or None
                net = parse_int(r["net_amount_cents"]) or 0
                line_type = "CREDIT_MEMO" if net < 0 else "INVOICE"

                tran_date = str(r["tran_date"] or "").strip()
                if not tran_date or not in_scope(tran_date):
                    continue

                linked_doc_id: int | None = None
                if invoice_number and invoice_number in self.doc_id_by_invoice_number:
                    linked_doc_id = self.doc_id_by_invoice_number[invoice_number]
                elif invoice_number:
                    linked_doc_id = placeholder_doc_by_invoice_number.get(invoice_number)
                    if not linked_doc_id:
                        placeholder_doc_type = "CREDIT_MEMO" if net < 0 else "BILL"
                        linked_doc_id = self.insert_document(
                            entity_id=self.entity_id,
                            counterparty_id=gfs_counterparty_id,
                            doc_type=placeholder_doc_type,
                            doc_date=tran_date or None,
                            due_date=(r["due_date"] or None),
                            doc_number=invoice_number,
                            total_cents=int(net),
                            tax_cents=None,
                            net_cents=int(net),
                            status=None,
                            source_record_id=source_record("derived__gfs_eft_invoice", invoice_number),
                            source_file_id=self.source_db_file_id,
                            raw={"source": "gfs_eft_notification_line", **dict(r)},
                            notes="Placeholder created because Wave bill missing for this GFS EFT invoice.",
                        )
                        placeholder_doc_by_invoice_number[invoice_number] = linked_doc_id
                        self.counts["documents"] += 1

                self.insert_settlement_line(
                    batch_id=batch_id,
                    line_no=idx,
                    external_doc_number=invoice_number,
                    line_type=line_type,
                    amount_cents=int(net),
                    txn_date=tran_date or None,
                    due_date=(r["due_date"] or None),
                    description=(r["customer_po"] or None),
                    linked_document_id=linked_doc_id,
                )
                self.counts["settlement_lines"] += 1

        # Notification ↔ bank txn links
        bank_txn_id_by_credit_bank_item_id = {
            str(r["id"]): str(r["bank_txn_id"])
            for r in self.src.execute("SELECT id, bank_txn_id FROM fresher_credits__credit_bank_items")
            if r["bank_txn_id"]
        }
        for r in self.src.execute("SELECT * FROM fresher_credits__gfs_eft_bank_links ORDER BY matched_at, id"):
            nid = str(r["notification_id"])
            batch_id = batch_id_by_notification_id.get(nid)
            if not batch_id:
                # Likely out-of-scope notification; ignore.
                continue
            bank_item_id = str(r["bank_item_id"])
            bank_txn_id = bank_txn_id_by_credit_bank_item_id.get(bank_item_id)
            if not bank_txn_id:
                self.warn(f"gfs_eft_bank_links id={r['id']}: missing bank_txn_id for bank_item_id={bank_item_id}")
                continue
            txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id)
            if not txn_id:
                self.warn(f"gfs_eft_bank_links id={r['id']}: unknown/inaccessible bank_txn_id={bank_txn_id}")
                continue
            self.insert_settlement_batch_txn_link(
                batch_id=batch_id,
                txn_id=txn_id,
                link_type=str(r["match_method"] or "MATCH"),
                confidence=parse_int(r["match_confidence"]),
                is_verified=True,
                notes=(r["notes"] or None),
            )
            self.counts["settlement_batch_txn_links"] += 1

    def import_pad_payments(self) -> None:
        assert self.entity_id is not None
        assert self.source_db_file_id is not None

        batch_id_by_payment_id: dict[str, int] = {}
        for r in self.src.execute("SELECT * FROM fresher_debits__pad_payments ORDER BY payment_date, id"):
            payment_date = str(r["payment_date"] or "").strip()
            if not in_scope(payment_date):
                continue
            pid = str(r["id"])
            vendor = str(r["vendor"])
            counterparty_id = self.upsert_counterparty(name=vendor, kind="VENDOR")
            total = parse_int(r["total_cents"]) or 0

            source_pdf = str(r["source_pdf"] or "")
            pdf_file_id = self.source_db_file_id
            if source_pdf:
                pdf_file_id = self.upsert_source_file(
                    source_key=f"pad_pdf:{vendor}:{pid}",
                    kind="PAD_PDF",
                    path=source_pdf,
                    sha256=None,
                    semantics=f"PAD payment PDF for {vendor}",
                )

            batch_id = self.insert_settlement_batch(
                entity_id=self.entity_id,
                counterparty_id=counterparty_id,
                settlement_type=f"{vendor}_PAD",
                statement_date=payment_date or None,
                due_date=payment_date or None,
                total_cents=int(total),
                source_record_id=source_record("fresher_debits__pad_payments", pid),
                source_file_id=pdf_file_id,
                raw=dict(r),
            )
            batch_id_by_payment_id[pid] = batch_id
            self.counts["settlement_batches"] += 1

            bank_txn_id = str(r["bank_txn_id"])
            txn_id = self.txn_id_by_bank_txn_id.get(bank_txn_id)
            if txn_id:
                self.insert_settlement_batch_txn_link(
                    batch_id=batch_id,
                    txn_id=txn_id,
                    link_type="BANK_PAD_DEBIT",
                    confidence=100,
                    is_verified=True,
                    notes=None,
                )
                self.counts["settlement_batch_txn_links"] += 1
            else:
                self.warn(f"pad_payments id={pid}: unknown bank_txn_id={bank_txn_id}")

        for pid, batch_id in batch_id_by_payment_id.items():
            rows = self.src.execute(
                "SELECT * FROM fresher_debits__pad_invoices WHERE pad_payment_id=? ORDER BY CAST(id AS INTEGER)",
                (pid,),
            ).fetchall()
            for idx, r in enumerate(rows, start=1):
                invoice_number = str(r["invoice_number"] or "").strip() or None
                amt = parse_int(r["amount_cents"]) or 0
                wave_bill_id = str(r["wave_bill_id"] or "").strip()
                linked_doc = self.doc_id_by_wave_bill_id.get(wave_bill_id) if wave_bill_id else None
                self.insert_settlement_line(
                    batch_id=batch_id,
                    line_no=idx,
                    external_doc_number=invoice_number,
                    line_type="INVOICE",
                    amount_cents=abs(int(amt)),
                    txn_date=None,
                    due_date=None,
                    description=None,
                    linked_document_id=linked_doc,
                )
                self.counts["settlement_lines"] += 1

    def write_summary(self, *, source_db: Path, target_db: Path) -> Path:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        out = self.output_dir / "import_summary.md"

        lines: list[str] = []
        lines.append("# SOT Import Summary")
        lines.append("")
        lines.append(f"- source_db: `{source_db}`")
        lines.append(f"- target_db: `{target_db}`")
        lines.append("")
        lines.append("## Counts")
        lines.append("")
        for key in sorted(self.counts.keys()):
            lines.append(f"- {key}: {self.counts[key]}")
        lines.append("")
        lines.append("## Warnings")
        lines.append("")
        if not self.warnings:
            lines.append("- (none)")
        else:
            for w in self.warnings:
                lines.append(f"- {w}")
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return out


def init_or_reset_target(db_path: Path, reset: bool) -> sqlite3.Connection:
    if reset and db_path.exists():
        db_path.unlink()
    conn = connect_db(db_path)
    apply_migrations(conn)
    return conn


def main() -> int:
    default_source_db = SOT_ROOT.parent / "db" / "t2_final.db"
    default_target_db = SOT_ROOT / "db" / "t2_sot.db"
    default_output_dir = SOT_ROOT / "output"

    ap = argparse.ArgumentParser()
    ap.add_argument("--source-db", type=Path, default=default_source_db)
    ap.add_argument("--db", type=Path, default=default_target_db)
    ap.add_argument("--output-dir", type=Path, default=default_output_dir)
    ap.add_argument("--reset", action="store_true")
    ap.add_argument("--entity-key", default="CANTEEN")
    ap.add_argument("--entity-name", default="Canteen (Corp)")
    args = ap.parse_args()

    if args.source_db.resolve() == args.db.resolve():
        raise SystemExit("--source-db and --db must be different files")
    if not args.source_db.exists():
        raise SystemExit(f"Source DB not found: {args.source_db}")

    source_sha = sha256_file(args.source_db)

    src = sqlite3.connect(args.source_db)
    src.row_factory = sqlite3.Row
    dst = init_or_reset_target(args.db, args.reset)
    try:
        importer = Importer(src=src, dst=dst, output_dir=args.output_dir)
        importer.run(
            entity_key=args.entity_key,
            entity_name=args.entity_name,
            source_db_path=args.source_db,
            source_sha256=source_sha,
        )
        summary = importer.write_summary(source_db=args.source_db, target_db=args.db)
    finally:
        dst.close()
        src.close()

    print("SOT IMPORT COMPLETE")
    print(f"- summary: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
