#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"
DEFAULT_CC_OVERRIDE_PATH = PROJECT_ROOT / "overrides" / "wave_bill_cc_settlement_overrides.yml"

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

REIMBURSEMENT_MATCH_TYPES = {
    "SHAREHOLDER_REIMBURSE",
    "E_TRANSFER_REIMBURSE",
}


@dataclass(frozen=True)
class MatchRow:
    wave_bill_id: int
    match_type: str
    bank_txn_id: str
    cc_txn_id: str


@dataclass(frozen=True)
class ManualCCOverride:
    wave_bill_id: int
    entry_date: str
    shareholder_code: str
    reason: str


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def load_manual_cc_overrides(path: Path) -> dict[int, ManualCCOverride]:
    if not path.exists():
        return {}
    data = load_yaml(path)
    raw = data.get("manual_cc_paid")
    if not isinstance(raw, list):
        return {}
    out: dict[int, ManualCCOverride] = {}
    for entry in raw:
        if not isinstance(entry, dict):
            continue
        wave_bill_id_raw = str(entry.get("wave_bill_id") or "").strip()
        if not wave_bill_id_raw:
            continue
        try:
            wave_bill_id = int(wave_bill_id_raw)
        except ValueError:
            continue
        entry_date = str(entry.get("entry_date") or "").strip()
        shareholder_code = str(entry.get("shareholder_code") or "").strip()
        reason = str(entry.get("reason") or "").strip()
        if not entry_date:
            continue
        out[wave_bill_id] = ManualCCOverride(
            wave_bill_id=wave_bill_id,
            entry_date=entry_date,
            shareholder_code=shareholder_code,
            reason=reason,
        )
    return out


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def scope_window(fys: list[FiscalYear]) -> tuple[str, str]:
    start = min(fy.start_date for fy in fys)
    end = max(fy.end_date for fy in fys)
    return start, end


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def fetch_wave_bill_totals(conn) -> dict[int, int]:
    rows = conn.execute("SELECT id, CAST(total_cents AS INTEGER) AS total_cents FROM wave_bills").fetchall()
    return {int(r["id"]): int(r["total_cents"] or 0) for r in rows}


def fetch_cc_txn_dates(conn) -> dict[str, str]:
    rows = conn.execute(
        """
        SELECT id, txn_date
        FROM fresher_debits__cc_transactions
        WHERE txn_date IS NOT NULL AND TRIM(txn_date) <> ''
        """
    ).fetchall()
    return {str(r["id"]): str(r["txn_date"]) for r in rows}


def fetch_bank_txn_dates(conn) -> dict[str, str]:
    rows = conn.execute(
        """
        SELECT id, txn_date
        FROM fresher_debits__bank_transactions
        WHERE txn_date IS NOT NULL AND TRIM(txn_date) <> ''
        """
    ).fetchall()
    return {str(r["id"]): str(r["txn_date"]) for r in rows}


def fetch_cc_payment_link_bank_ids(conn) -> set[str]:
    rows = conn.execute(
        """
        SELECT DISTINCT bank_txn_id
        FROM fresher_debits__cc_payment_links
        WHERE bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        """
    ).fetchall()
    return {str(r["bank_txn_id"]).strip() for r in rows if str(r["bank_txn_id"] or "").strip()}


def fetch_split_cc_payments(conn) -> dict[int, list[tuple[str, int]]]:
    """
    Returns {wave_bill_id: [(cc_txn_id, amount_cents), ...]} for bills that have explicit
    split payment rows where txn_type='CC'.
    """
    rows = conn.execute(
        """
        SELECT wave_bill_id, txn_id AS cc_txn_id, CAST(amount_cents AS INTEGER) AS amount_cents
        FROM fresher_debits__split_payments
        WHERE txn_type = 'CC'
          AND wave_bill_id IS NOT NULL AND TRIM(wave_bill_id) <> ''
          AND txn_id IS NOT NULL AND TRIM(txn_id) <> ''
        ORDER BY CAST(wave_bill_id AS INTEGER), CAST(amount_cents AS INTEGER) DESC
        """
    ).fetchall()
    out: dict[int, list[tuple[str, int]]] = {}
    for r in rows:
        try:
            wave_bill_id = int(str(r["wave_bill_id"]).strip())
        except ValueError:
            continue
        cc_txn_id = str(r["cc_txn_id"] or "").strip()
        if not cc_txn_id:
            continue
        amount_cents = int(r["amount_cents"] or 0)
        if amount_cents <= 0:
            continue
        out.setdefault(wave_bill_id, []).append((cc_txn_id, amount_cents))
    return out


def fetch_wave_matches(conn) -> list[MatchRow]:
    rows = conn.execute(
        """
        SELECT wave_bill_id, match_type, COALESCE(bank_txn_id, '') AS bank_txn_id, COALESCE(cc_txn_id, '') AS cc_txn_id
        FROM fresher_debits__wave_matches
        WHERE match_type IN ('CC_PURCHASE', 'CC_PAYMENT_TRANSFER')
        ORDER BY CAST(wave_bill_id AS INTEGER), match_type, CAST(COALESCE(cc_txn_id, '0') AS INTEGER)
        """
    ).fetchall()
    out: list[MatchRow] = []
    for r in rows:
        out.append(
            MatchRow(
                wave_bill_id=int(r["wave_bill_id"]),
                match_type=str(r["match_type"] or "").strip(),
                bank_txn_id=str(r["bank_txn_id"] or "").strip(),
                cc_txn_id=str(r["cc_txn_id"] or "").strip(),
            )
        )
    return out


def fetch_match_types_by_bill(conn) -> dict[int, set[str]]:
    rows = conn.execute("SELECT wave_bill_id, match_type FROM fresher_debits__wave_matches").fetchall()
    out: dict[int, set[str]] = {}
    for r in rows:
        bid = int(r["wave_bill_id"])
        out.setdefault(bid, set()).add(str(r["match_type"] or "").strip())
    return out


def fetch_non_cc_bank_paid_bill_ids(conn, *, cc_payment_bank_ids: set[str]) -> set[int]:
    out: set[int] = set()

    rows = conn.execute(
        """
        SELECT wave_bill_id, txn_id AS bank_txn_id
        FROM fresher_debits__split_payments
        WHERE txn_type = 'BANK'
          AND txn_id IS NOT NULL AND TRIM(txn_id) <> ''
        """
    ).fetchall()
    for r in rows:
        bank_id = str(r["bank_txn_id"] or "").strip()
        if bank_id and bank_id not in cc_payment_bank_ids:
            out.add(int(r["wave_bill_id"]))

    rows = conn.execute(
        """
        SELECT wave_bill_id, bank_txn_id
        FROM fresher_debits__wave_bill_funding
        WHERE bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        """
    ).fetchall()
    for r in rows:
        bank_id = str(r["bank_txn_id"] or "").strip()
        if bank_id and bank_id not in cc_payment_bank_ids:
            out.add(int(r["wave_bill_id"]))

    rows = conn.execute(
        """
        SELECT target_id AS wave_bill_id, bank_txn_id
        FROM fresher_debits__bank_allocations
        WHERE target_type = 'WAVE_BILL'
          AND bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
          AND target_id IS NOT NULL AND TRIM(target_id) <> ''
        """
    ).fetchall()
    for r in rows:
        bank_id = str(r["bank_txn_id"] or "").strip()
        if bank_id and bank_id not in cc_payment_bank_ids:
            out.add(int(r["wave_bill_id"]))

    rows = conn.execute(
        f"""
        SELECT wave_bill_id, bank_txn_id
        FROM fresher_debits__wave_matches
        WHERE match_type IN ({','.join('?' for _ in sorted(DIRECT_VENDOR_PAYMENT_MATCH_TYPES))})
          AND bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        """,
        tuple(sorted(DIRECT_VENDOR_PAYMENT_MATCH_TYPES)),
    ).fetchall()
    for r in rows:
        bank_id = str(r["bank_txn_id"] or "").strip()
        if bank_id and bank_id not in cc_payment_bank_ids:
            out.add(int(r["wave_bill_id"]))

    return out


def fetch_reimbursed_bill_ids(conn) -> set[int]:
    rows = conn.execute(
        f"""
        SELECT DISTINCT wave_bill_id
        FROM fresher_debits__wave_matches
        WHERE match_type IN ({','.join('?' for _ in sorted(REIMBURSEMENT_MATCH_TYPES))})
        """,
        tuple(sorted(REIMBURSEMENT_MATCH_TYPES)),
    ).fetchall()
    return {int(r["wave_bill_id"]) for r in rows}


def fetch_cc_paid_bill_evidence_from_bank_links(conn, *, cc_payment_bank_ids: set[str]) -> list[MatchRow]:
    out: list[MatchRow] = []
    if not cc_payment_bank_ids:
        return out

    # Bank allocations created from CC payment -> CC purchase -> wave bill allocation pipelines.
    rows = conn.execute(
        f"""
        SELECT target_id AS wave_bill_id, bank_txn_id, amount_cents
        FROM fresher_debits__bank_allocations
        WHERE target_type = 'WAVE_BILL'
          AND bank_txn_id IN ({','.join('?' for _ in cc_payment_bank_ids)})
        """,
        tuple(sorted(cc_payment_bank_ids)),
    ).fetchall()
    for r in rows:
        out.append(
            MatchRow(
                wave_bill_id=int(r["wave_bill_id"]),
                match_type="CC_PAYMENT_ALLOC",
                bank_txn_id=str(r["bank_txn_id"] or "").strip(),
                cc_txn_id="",
            )
        )

    rows = conn.execute(
        f"""
        SELECT wave_bill_id, bank_txn_id, amount_cents
        FROM fresher_debits__wave_bill_funding
        WHERE bank_txn_id IN ({','.join('?' for _ in cc_payment_bank_ids)})
        """,
        tuple(sorted(cc_payment_bank_ids)),
    ).fetchall()
    for r in rows:
        out.append(
            MatchRow(
                wave_bill_id=int(r["wave_bill_id"]),
                match_type="CC_PAYMENT_FUNDING",
                bank_txn_id=str(r["bank_txn_id"] or "").strip(),
                cc_txn_id="",
            )
        )

    rows = conn.execute(
        f"""
        SELECT wave_bill_id, txn_id AS bank_txn_id, amount_cents
        FROM fresher_debits__split_payments
        WHERE txn_type = 'BANK'
          AND txn_id IN ({','.join('?' for _ in cc_payment_bank_ids)})
        """,
        tuple(sorted(cc_payment_bank_ids)),
    ).fetchall()
    for r in rows:
        out.append(
            MatchRow(
                wave_bill_id=int(r["wave_bill_id"]),
                match_type="CC_PAYMENT_SPLIT",
                bank_txn_id=str(r["bank_txn_id"] or "").strip(),
                cc_txn_id="",
            )
        )

    return out


def infer_shareholder_code_for_transfer(
    *,
    bank_txn_id: str,
    cc_payment_bank_ids: set[str],
    thomas_code: str,
    dwayne_code: str,
) -> tuple[str, str]:
    if bank_txn_id and bank_txn_id in cc_payment_bank_ids:
        return (dwayne_code, "cc_payment_links")
    # No evidence this is a Dwayne card payment in the snapshot.
    return ("", "no_cc_payment_link")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--cc-overrides", type=Path, default=DEFAULT_CC_OVERRIDE_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing CC settlement journals before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")
    start_date, end_date = scope_window(fys)

    cfg = load_config(args.config)
    manual_overrides = load_manual_cc_overrides(args.cc_overrides)
    accounts_cfg = cfg.get("accounts", {}) if isinstance(cfg.get("accounts"), dict) else {}
    payroll_cfg = cfg.get("payroll", {}) if isinstance(cfg.get("payroll"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("wave_bill_cc_settlement") if isinstance(cfg.get("journal_sources"), dict) else {}

    ap_code = str(accounts_cfg.get("accounts_payable_code") or "2000").strip()
    thomas_payable_code = str(payroll_cfg.get("due_to_shareholder_thomas_code") or "2400").strip()
    dwayne_payable_code = str(payroll_cfg.get("due_to_shareholder_dwayne_code") or "2410").strip()

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "wave_bill_cc_settlement")
    entry_type = str((source_cfg or {}).get("entry_type") or "SETTLEMENT")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "wave_bill_cc_settlement_journal_summary.md"
    out_detail_csv = args.out_dir / "wave_bill_cc_settlement_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )

        bill_totals = fetch_wave_bill_totals(conn)
        cc_txn_dates = fetch_cc_txn_dates(conn)
        bank_txn_dates = fetch_bank_txn_dates(conn)
        cc_payment_bank_ids = fetch_cc_payment_link_bank_ids(conn)
        split_cc_payments_by_bill = fetch_split_cc_payments(conn)
        match_types_by_bill = fetch_match_types_by_bill(conn)
        reimbursed_bill_ids = fetch_reimbursed_bill_ids(conn)
        non_cc_bank_paid_bill_ids = fetch_non_cc_bank_paid_bill_ids(conn, cc_payment_bank_ids=cc_payment_bank_ids)

        matches = fetch_wave_matches(conn)
        matches.extend(fetch_cc_paid_bill_evidence_from_bank_links(conn, cc_payment_bank_ids=cc_payment_bank_ids))
        matches_by_bill: dict[int, list[MatchRow]] = {}
        for m in matches:
            matches_by_bill.setdefault(m.wave_bill_id, []).append(m)
        for wave_bill_id in sorted(manual_overrides.keys()):
            matches_by_bill.setdefault(
                wave_bill_id,
                [],
            ).append(
                MatchRow(
                    wave_bill_id=wave_bill_id,
                    match_type="CC_PAYMENT_MANUAL",
                    bank_txn_id="",
                    cc_txn_id="",
                )
            )

        posted = 0
        skipped_out_of_scope = 0
        skipped_conflicting_payment_evidence = 0
        skipped_missing_bill_total = 0
        skipped_missing_cc_payment_link = 0
        used_manual_override = 0
        skipped_manual_override = 0
        posted_split_cc = 0
        skipped_split_missing_cc_txn_date = 0
        skipped_split_out_of_scope = 0
        detail_rows: list[dict[str, str]] = []

        for bill_id in sorted(matches_by_bill.keys()):
            total_cents = int(bill_totals.get(int(bill_id), 0))
            if total_cents == 0:
                skipped_missing_bill_total += 1
                continue

            # Bills with explicit split CC payment rows need partial AP clearance.
            # The standard path clears the full bill total, which is wrong for CC+bank splits.
            if int(bill_id) in split_cc_payments_by_bill:
                continue

            if int(bill_id) in reimbursed_bill_ids:
                skipped_conflicting_payment_evidence += 1
                continue
            if int(bill_id) in non_cc_bank_paid_bill_ids:
                skipped_conflicting_payment_evidence += 1
                continue

            bill_matches = matches_by_bill[bill_id]
            best: MatchRow | None = None
            for m in bill_matches:
                if m.match_type == "CC_PURCHASE":
                    best = m
                    break
            if best is None:
                for m in bill_matches:
                    if m.match_type == "CC_PAYMENT_MANUAL":
                        best = m
                        break
            if best is None:
                for m in bill_matches:
                    if m.match_type == "CC_PAYMENT_TRANSFER":
                        best = m
                        break
            if best is None:
                for m in bill_matches:
                    if m.match_type == "CC_PAYMENT_ALLOC":
                        best = m
                        break
            if best is None:
                for m in bill_matches:
                    if m.match_type == "CC_PAYMENT_FUNDING":
                        best = m
                        break
            if best is None:
                for m in bill_matches:
                    if m.match_type == "CC_PAYMENT_SPLIT":
                        best = m
                        break
            if best is None:
                continue

            entry_date = ""
            shareholder_code = dwayne_payable_code
            shareholder_basis = ""

            if best.match_type == "CC_PURCHASE":
                entry_date = cc_txn_dates.get(best.cc_txn_id, "")
                shareholder_code = dwayne_payable_code
                shareholder_basis = "cc_purchase_assumed_dwayne"
            elif best.match_type == "CC_PAYMENT_MANUAL":
                manual = manual_overrides.get(int(bill_id))
                if not manual:
                    skipped_manual_override += 1
                    continue
                entry_date = manual.entry_date
                shareholder_code = manual.shareholder_code or dwayne_payable_code
                shareholder_basis = f"manual_override:{manual.reason or 'cc_payment_manual'}"
                used_manual_override += 1
            else:
                entry_date = bank_txn_dates.get(best.bank_txn_id, "")
                shareholder_code, shareholder_basis = infer_shareholder_code_for_transfer(
                    bank_txn_id=best.bank_txn_id,
                    cc_payment_bank_ids=cc_payment_bank_ids,
                    thomas_code=thomas_payable_code,
                    dwayne_code=dwayne_payable_code,
                )
                if not shareholder_code:
                    skipped_missing_cc_payment_link += 1
                    continue

            if not entry_date or entry_date < start_date or entry_date > end_date:
                skipped_out_of_scope += 1
                continue

            je_id = f"WAVE_BILL_CC_SETTLE_{bill_id}"
            description = f"Wave bill settlement (paid via credit card) - bill {bill_id}"
            notes = (
                f"wave_bill_id={bill_id}; match_type={best.match_type}; bank_txn_id={best.bank_txn_id}; cc_txn_id={best.cc_txn_id}; "
                f"bill_total_cents={total_cents}; shareholder_code={shareholder_code}; shareholder_basis={shareholder_basis}"
            )

            conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
            conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

            conn.execute(
                """
                INSERT INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id,
                  source_bill_id, notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    entry_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    str(bill_id),
                    str(bill_id),
                    notes,
                ),
            )

            conn.execute(
                """
                INSERT INTO journal_entry_lines (
                  id, journal_entry_id, line_number,
                  account_code, debit_cents, credit_cents, description
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    f"{je_id}:1",
                    je_id,
                    1,
                    ap_code,
                    total_cents,
                    0,
                    "Clear AP: bill paid via shareholder credit card",
                ),
            )
            conn.execute(
                """
                INSERT INTO journal_entry_lines (
                  id, journal_entry_id, line_number,
                  account_code, debit_cents, credit_cents, description
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    f"{je_id}:2",
                    je_id,
                    2,
                    shareholder_code,
                    0,
                    total_cents,
                    "Due to shareholder: credit card payment of vendor bill",
                ),
            )

            posted += 1
            detail_rows.append(
                {
                    "wave_bill_id": str(bill_id),
                    "entry_date": entry_date,
                    "bill_total": cents_to_dollars(total_cents),
                    "bill_total_cents": str(total_cents),
                    "settlement_amount": cents_to_dollars(total_cents),
                    "settlement_amount_cents": str(total_cents),
                    "match_type": best.match_type,
                    "bank_txn_id": best.bank_txn_id,
                    "cc_txn_id": best.cc_txn_id,
                    "shareholder_code": shareholder_code,
                    "shareholder_basis": shareholder_basis,
                    "journal_entry_id": je_id,
                }
            )

        # Post partial settlements for bills with split CC payments.
        # These clear AP only for the CC portion (not the full bill total).
        for bill_id in sorted(split_cc_payments_by_bill.keys()):
            bill_total_cents = int(bill_totals.get(int(bill_id), 0))
            if bill_total_cents == 0:
                skipped_missing_bill_total += 1
                continue

            # Group split CC amounts by cc_txn_date to keep fiscal cutoffs honest.
            split_pairs = split_cc_payments_by_bill.get(int(bill_id)) or []
            split_cc_txn_ids = sorted({cc for cc, _ in split_pairs})
            by_date: dict[str, int] = {}
            for cc_txn_id, amount_cents in split_pairs:
                cc_date = cc_txn_dates.get(str(cc_txn_id), "")
                if not cc_date:
                    skipped_split_missing_cc_txn_date += 1
                    continue
                by_date[cc_date] = by_date.get(cc_date, 0) + int(amount_cents)

            for cc_date, amount_cents in sorted(by_date.items()):
                if not cc_date or cc_date < start_date or cc_date > end_date:
                    skipped_split_out_of_scope += 1
                    continue
                if amount_cents <= 0:
                    continue

                je_id = f"WAVE_BILL_CC_SETTLE_SPLIT_{bill_id}_{cc_date}"
                description = f"Wave bill settlement (split CC payment) - bill {bill_id}"
                notes = (
                    f"wave_bill_id={bill_id}; match_type=SPLIT_CC_PAYMENT; cc_txn_date={cc_date}; split_cc_txn_ids={','.join(split_cc_txn_ids)}; "
                    f"split_cc_amount_cents={amount_cents}; bill_total_cents={bill_total_cents}; shareholder_code={dwayne_payable_code}; "
                    f"shareholder_basis=split_payments_cc"
                )

                conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
                conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

                conn.execute(
                    """
                    INSERT INTO journal_entries (
                      id, entry_date, entry_type, description,
                      source_system, source_record_type, source_record_id,
                      source_bill_id, notes, is_posted
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
                    """,
                    (
                        je_id,
                        cc_date,
                        entry_type,
                        description,
                        source_system,
                        source_record_type,
                        str(bill_id),
                        str(bill_id),
                        notes,
                    ),
                )

                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:1",
                        je_id,
                        1,
                        ap_code,
                        int(amount_cents),
                        0,
                        "Clear AP (partial): split credit card payment",
                    ),
                )
                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:2",
                        je_id,
                        2,
                        dwayne_payable_code,
                        0,
                        int(amount_cents),
                        "Due to shareholder: split credit card payment of vendor bill",
                    ),
                )

                posted_split_cc += 1
                detail_rows.append(
                    {
                        "wave_bill_id": str(bill_id),
                        "entry_date": cc_date,
                        "bill_total": cents_to_dollars(bill_total_cents),
                        "bill_total_cents": str(bill_total_cents),
                        "settlement_amount": cents_to_dollars(int(amount_cents)),
                        "settlement_amount_cents": str(int(amount_cents)),
                        "match_type": "SPLIT_CC_PAYMENT",
                        "bank_txn_id": "",
                        "cc_txn_id": ",".join(split_cc_txn_ids),
                        "shareholder_code": dwayne_payable_code,
                        "shareholder_basis": "split_payments_cc",
                        "journal_entry_id": je_id,
                    }
                )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "wave_bill_id",
                "entry_date",
                "bill_total",
                "bill_total_cents",
                "settlement_amount",
                "settlement_amount_cents",
                "match_type",
                "bank_txn_id",
                "cc_txn_id",
                "shareholder_code",
                "shareholder_basis",
                "journal_entry_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Wave bill CC settlement journals (AP → due-to-shareholder)\n\n")
            f.write(f"- Scope: {start_date} → {end_date}\n")
            f.write(f"- Posted: {posted}\n")
            f.write(f"- Posted split CC settlements: {posted_split_cc}\n")
            f.write(f"- Manual overrides used: {used_manual_override}\n")
            f.write(f"- Skipped (out of scope): {skipped_out_of_scope}\n")
            f.write(f"- Skipped (bill already has other payment evidence): {skipped_conflicting_payment_evidence}\n")
            f.write(f"- Skipped (missing/zero bill total): {skipped_missing_bill_total}\n")
            f.write(f"- Skipped (no CC payment link evidence): {skipped_missing_cc_payment_link}\n")
            if skipped_split_missing_cc_txn_date:
                f.write(f"- Skipped split CC (missing cc txn date): {skipped_split_missing_cc_txn_date}\n")
            if skipped_split_out_of_scope:
                f.write(f"- Skipped split CC (out of scope): {skipped_split_out_of_scope}\n")
            if skipped_manual_override:
                f.write(f"- Skipped (manual override missing): {skipped_manual_override}\n")
            f.write("\nNotes:\n")
            f.write("- This posts only AP-clearing entries for bills marked as credit-card-paid in the snapshot.\n")
            f.write("- Split CC payments clear AP partially using `fresher_debits__split_payments`.\n")
            f.write("- Bank CC payments are handled separately by bank debit journals (clearing due-to-shareholder).\n")

        conn.commit()

    finally:
        conn.close()

    print("WAVE BILL CC SETTLEMENT JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
