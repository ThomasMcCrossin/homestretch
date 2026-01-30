#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"
DEFAULT_BANK_OVERRIDE_PATH = PROJECT_ROOT / "overrides" / "bank_txn_category_overrides.yml"


@dataclass(frozen=True)
class BankTxn:
    id: str
    txn_date: str
    debit_cents: int
    description: str
    txn_category: str
    explanation: str


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def load_bank_txn_category_override_entries(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    data = load_yaml(path)
    raw = data.get("bank_txn_category_overrides")
    if not isinstance(raw, dict):
        return {}
    out: dict[str, dict] = {}
    for bank_txn_id, cfg in raw.items():
        if not isinstance(cfg, dict):
            continue
        to_cat = str(cfg.get("to_category") or "").strip()
        if not to_cat:
            continue
        entry = dict(cfg)
        entry["to_category"] = to_cat
        out[str(bank_txn_id).strip()] = entry
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


def fetch_bank_txn_classifications(conn) -> dict[str, tuple[str, str]]:
    """
    Prefer verified classifications when multiple exist.
    Returns bank_txn_id -> (txn_category, explanation)
    """
    rows = conn.execute(
        """
        SELECT id, bank_txn_id, txn_category, explanation, verified
        FROM fresher_debits__bank_txn_classifications
        ORDER BY CAST(verified AS INTEGER) DESC, CAST(id AS INTEGER) ASC
        """
    ).fetchall()
    out: dict[str, tuple[str, str]] = {}
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"] or "").strip()
        if not bank_txn_id or bank_txn_id in out:
            continue
        out[bank_txn_id] = (str(r["txn_category"] or "").strip(), str(r["explanation"] or "").strip())
    return out


def fetch_bank_txns(conn, *, start_date: str, end_date: str) -> dict[str, BankTxn]:
    classifications = fetch_bank_txn_classifications(conn)
    rows = conn.execute(
        """
        SELECT id, txn_date, CAST(debit_cents AS INTEGER) AS debit_cents, description
        FROM fresher_debits__bank_transactions
        WHERE txn_date >= ? AND txn_date <= ?
          AND CAST(debit_cents AS INTEGER) > 0
        """,
        (start_date, end_date),
    ).fetchall()
    out: dict[str, BankTxn] = {}
    for r in rows:
        bank_txn_id = str(r["id"])
        cat, expl = classifications.get(bank_txn_id, ("", ""))
        out[bank_txn_id] = BankTxn(
            id=bank_txn_id,
            txn_date=str(r["txn_date"]),
            debit_cents=int(r["debit_cents"] or 0),
            description=str(r["description"] or ""),
            txn_category=cat,
            explanation=expl,
        )
    return out


def fetch_wave_bill_totals(conn) -> dict[int, int]:
    rows = conn.execute("SELECT id, total_cents FROM wave_bills").fetchall()
    return {int(r["id"]): int(r["total_cents"] or 0) for r in rows}


def fetch_wave_match_groups(conn) -> dict[str, list[int]]:
    """
    Wave "matches" can include both auto-suggested and manual-curated links for the same bank_txn.
    When manual matches exist for a given bank_txn_id, prefer ONLY those manual matches.

    This avoids double-linking the same bank debit to multiple bills (common when an auto-match
    was later superseded by a manual correction but not removed from the snapshot).
    """
    rows = conn.execute(
        """
        SELECT bank_txn_id, wave_bill_id, match_method
        FROM fresher_debits__wave_matches
        WHERE bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        ORDER BY CAST(bank_txn_id AS INTEGER) ASC, CAST(wave_bill_id AS INTEGER) ASC, CAST(id AS INTEGER) ASC
        """
    ).fetchall()

    grouped_raw: dict[str, list[tuple[str, int]]] = {}
    for r in rows:
        bank_id = str(r["bank_txn_id"]).strip()
        if not bank_id:
            continue
        bill_id = int(r["wave_bill_id"])
        method = str(r["match_method"] or "").strip().upper()
        grouped_raw.setdefault(bank_id, []).append((method, bill_id))

    grouped: dict[str, list[int]] = {}
    for bank_id, matches in grouped_raw.items():
        manual = [bid for method, bid in matches if method.startswith("MANUAL")]
        chosen = manual if manual else [bid for _, bid in matches]
        # Deduplicate while preserving order.
        out: list[int] = []
        seen: set[int] = set()
        for bid in chosen:
            if bid in seen:
                continue
            seen.add(bid)
            out.append(bid)
        grouped[bank_id] = out

    return grouped


def fetch_split_payment_allocations(conn) -> list[tuple[str, int, int]]:
    rows = conn.execute(
        """
        SELECT txn_id AS bank_txn_id, wave_bill_id, amount_cents
        FROM fresher_debits__split_payments
        WHERE txn_type = 'BANK'
          AND txn_id IS NOT NULL AND TRIM(txn_id) <> ''
        ORDER BY CAST(txn_id AS INTEGER) ASC, CAST(wave_bill_id AS INTEGER) ASC
        """
    ).fetchall()
    out: list[tuple[str, int, int]] = []
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"]).strip()
        if not bank_txn_id:
            continue
        out.append((bank_txn_id, int(r["wave_bill_id"]), int(r["amount_cents"] or 0)))
    return out


def fetch_wave_bill_funding_allocations(conn) -> list[tuple[str, int, int]]:
    rows = conn.execute(
        """
        SELECT bank_txn_id, wave_bill_id, amount_cents
        FROM fresher_debits__wave_bill_funding
        WHERE bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        ORDER BY CAST(bank_txn_id AS INTEGER) ASC, CAST(wave_bill_id AS INTEGER) ASC
        """
    ).fetchall()
    out: list[tuple[str, int, int]] = []
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"]).strip()
        if not bank_txn_id:
            continue
        out.append((bank_txn_id, int(r["wave_bill_id"]), int(r["amount_cents"] or 0)))
    return out


def fetch_bank_allocation_rows(conn) -> list[tuple[str, int, int]]:
    rows = conn.execute(
        """
        SELECT bank_txn_id, target_id AS wave_bill_id, amount_cents
        FROM fresher_debits__bank_allocations
        WHERE target_type = 'WAVE_BILL'
          AND bank_txn_id IS NOT NULL AND TRIM(bank_txn_id) <> ''
        ORDER BY CAST(bank_txn_id AS INTEGER) ASC, CAST(target_id AS INTEGER) ASC
        """
    ).fetchall()
    out: list[tuple[str, int, int]] = []
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"]).strip()
        if not bank_txn_id:
            continue
        out.append((bank_txn_id, int(r["wave_bill_id"]), int(r["amount_cents"] or 0)))
    return out


def shareholder_account_from_text(text: str, *, thomas_code: str, dwayne_code: str, default_code: str) -> str:
    t = (text or "").lower()
    if "dwayne" in t:
        return dwayne_code
    if "thomas" in t:
        return thomas_code
    return default_code


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--bank-overrides", type=Path, default=DEFAULT_BANK_OVERRIDE_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing wave bill reimbursement journals before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    accounts_cfg = cfg.get("accounts", {}) if isinstance(cfg.get("accounts"), dict) else {}
    payroll_cfg = cfg.get("payroll", {}) if isinstance(cfg.get("payroll"), dict) else {}
    tax_cfg = cfg.get("tax", {}) if isinstance(cfg.get("tax"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("wave_bill_reimbursement") if isinstance(cfg.get("journal_sources"), dict) else {}

    ap_code = str(accounts_cfg.get("accounts_payable_code") or "2000").strip()
    thomas_code = str(payroll_cfg.get("due_to_shareholder_thomas_code") or "2400").strip()
    dwayne_code = str(payroll_cfg.get("due_to_shareholder_dwayne_code") or "2410").strip()
    hst_payable_code = str(tax_cfg.get("hst_payable_code") or "2200").strip()
    unmapped_expense_code = "9100"  # Pending Receipt - No ITC (default, portable)

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "wave_bill_reimbursement")
    entry_type = str((source_cfg or {}).get("entry_type") or "RECLASS")

    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "wave_bill_reimbursement_journal_summary.md"
    out_detail_csv = args.out_dir / "wave_bill_reimbursement_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )

        bank_override_entries = load_bank_txn_category_override_entries(args.bank_overrides)
        bank_txns = fetch_bank_txns(conn, start_date=start_date, end_date=end_date)
        bill_totals = fetch_wave_bill_totals(conn)

        allocations_by_bank: dict[str, dict[int, tuple[int, str]]] = {}

        def add_alloc(bank_txn_id: str, wave_bill_id: int, amount_cents: int, method: str) -> None:
            bank_txn_id = str(bank_txn_id or "").strip()
            if not bank_txn_id:
                return
            allocations_by_bank.setdefault(bank_txn_id, {})
            if wave_bill_id in allocations_by_bank[bank_txn_id]:
                return
            allocations_by_bank[bank_txn_id][wave_bill_id] = (int(amount_cents or 0), method)

        for bank_txn_id, wave_bill_id, amount_cents in fetch_split_payment_allocations(conn):
            add_alloc(bank_txn_id, wave_bill_id, amount_cents, "SPLIT_PAYMENTS")

        for bank_txn_id, wave_bill_id, amount_cents in fetch_wave_bill_funding_allocations(conn):
            add_alloc(bank_txn_id, wave_bill_id, amount_cents, "WAVE_BILL_FUNDING")

        for bank_txn_id, wave_bill_id, amount_cents in fetch_bank_allocation_rows(conn):
            add_alloc(bank_txn_id, wave_bill_id, amount_cents, "BANK_ALLOCATIONS")

        match_groups = fetch_wave_match_groups(conn)
        for bank_id, bill_ids in match_groups.items():
            if bank_id in allocations_by_bank:
                continue
            for bid in bill_ids:
                add_alloc(bank_id, int(bid), bill_totals.get(int(bid), 0), "WAVE_MATCHES")

        posted = 0
        skipped = 0
        detail_rows: list[dict[str, str]] = []

        for bank_id, bill_map in sorted(allocations_by_bank.items(), key=lambda kv: int(kv[0]) if str(kv[0]).isdigit() else kv[0]):
            bank = bank_txns.get(bank_id)
            if not bank:
                continue

            evidence_category = bank.txn_category
            category = evidence_category
            override = bank_override_entries.get(bank_id)
            if override:
                expected_date = str(override.get("txn_date") or "").strip()
                expected_debit = override.get("debit_cents")
                ok_date = (not expected_date) or expected_date == bank.txn_date
                ok_amt = True
                if expected_debit is not None and str(expected_debit).strip() != "":
                    try:
                        ok_amt = int(expected_debit) == bank.debit_cents
                    except ValueError:
                        ok_amt = False
                if ok_date and ok_amt:
                    category = str(override.get("to_category") or category).strip()

            if category not in ("REIMBURSEMENT", "RENT_REIMBURSEMENT", "HST_REIMBURSEMENT"):
                continue

            bill_ids = sorted(bill_map.keys())
            methods = sorted({bill_map[bid][1] for bid in bill_ids})

            raw_alloc_by_bill: dict[int, int] = {bid: int(bill_map[bid][0] or 0) for bid in bill_ids}
            raw_total_alloc = sum(raw_alloc_by_bill.values())
            alloc_by_bill = dict(raw_alloc_by_bill)

            # If explicit allocation rows sum to more than the bank debit, treat as a split-entry bug
            # (common when the full bank debit was duplicated across multiple bills).
            # Do NOT auto-scale WAVE_MATCHES (bill-total) allocations, since those can legitimately exceed reimbursement.
            allocation_scaled = False
            if raw_total_alloc > bank.debit_cents and bank.debit_cents > 0 and "WAVE_MATCHES" not in methods:
                target = bank.debit_cents
                scaled: dict[int, int] = {}
                remaining = target
                # Proportional scaling with rounding; last bill gets remaining cents to ensure sum matches.
                for i, bid in enumerate(bill_ids):
                    amt = raw_alloc_by_bill.get(bid, 0)
                    if i == len(bill_ids) - 1:
                        scaled_amt = remaining
                    else:
                        scaled_amt = int(round(amt * target / raw_total_alloc)) if raw_total_alloc else 0
                        if scaled_amt < 0:
                            scaled_amt = 0
                        if scaled_amt > remaining:
                            scaled_amt = remaining
                        remaining -= scaled_amt
                    scaled[bid] = scaled_amt
                alloc_by_bill = scaled
                allocation_scaled = True

            total_alloc = sum(int(alloc_by_bill.get(bid, 0)) for bid in bill_ids)
            remainder = bank.debit_cents - total_alloc

            shareholder_code = shareholder_account_from_text(
                f"{bank.description} {bank.explanation}",
                thomas_code=thomas_code,
                dwayne_code=dwayne_code,
                default_code=thomas_code,
            )

            je_id = f"WAVE_BILL_REIMBURSE_{bank_id}"
            description = f"Wave bills paid by shareholder (reclass) - bank txn {bank_id}"
            notes = (
                f"bank_txn_id={bank_id}; evidence_category={evidence_category}; category={category}; "
                f"methods={','.join(methods)}; bill_ids={','.join(str(x) for x in bill_ids)}; "
                f"allocated_to_bills_cents={total_alloc}; bank_debit_cents={bank.debit_cents}; remainder_cents={remainder}; "
                f"allocation_scaled={allocation_scaled}; raw_allocated_to_bills_cents={raw_total_alloc}"
            )

            conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
            conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

            conn.execute(
                """
                INSERT INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id,
                  notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    bank.txn_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    str(bank_id),
                    notes,
                ),
            )

            line_number = 1
            debit_total = 0

            if total_alloc:
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
                        total_alloc,
                        0,
                        "Reclass AP to shareholder payable (Wave bills funded by shareholder)",
                    ),
                )
                debit_total += total_alloc
                line_number += 1

            remainder_account = ""
            if remainder > 0:
                remainder_account = hst_payable_code if category == "HST_REIMBURSEMENT" else unmapped_expense_code
                remainder_desc = "HST paid by shareholder (reimbursed)" if category == "HST_REIMBURSEMENT" else "Reimbursed amount missing wave bill mapping"
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
                        remainder_account,
                        remainder,
                        0,
                        remainder_desc,
                    ),
                )
                debit_total += remainder
                line_number += 1

            if debit_total == 0:
                # Nothing to reclass (no linked bills, and no positive remainder to model).
                conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
                conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))
                skipped += 1
                continue

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
                    shareholder_code,
                    0,
                    debit_total,
                    "Due to shareholder (funding offset)",
                ),
            )

            posted += 1
            detail_rows.append(
                {
                    "bank_txn_id": bank_id,
                    "bank_date": bank.txn_date,
                    "bank_debit_cents": str(bank.debit_cents),
                    "bank_debit": cents_to_dollars(bank.debit_cents),
                    "evidence_category": evidence_category,
                    "category": category,
                    "allocation_scaled": "1" if allocation_scaled else "0",
                    "raw_allocated_to_bills_cents": str(raw_total_alloc),
                    "raw_allocated_to_bills": cents_to_dollars(raw_total_alloc),
                    "shareholder_account": shareholder_code,
                    "matched_wave_bill_ids": ",".join(str(x) for x in bill_ids),
                    "match_methods": ",".join(methods),
                    "allocated_to_bills_cents": str(total_alloc),
                    "allocated_to_bills": cents_to_dollars(total_alloc),
                    "remainder_cents": str(remainder),
                    "remainder": cents_to_dollars(remainder),
                    "remainder_account": remainder_account,
                    "journal_entry_id": je_id,
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "bank_txn_id",
                "bank_date",
                "bank_debit_cents",
                "bank_debit",
                "evidence_category",
                "category",
                "allocation_scaled",
                "raw_allocated_to_bills_cents",
                "raw_allocated_to_bills",
                "shareholder_account",
                "matched_wave_bill_ids",
                "match_methods",
                "allocated_to_bills_cents",
                "allocated_to_bills",
                "remainder_cents",
                "remainder",
                "remainder_account",
                "journal_entry_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Wave bill reimbursement reclass journal summary\n\n")
            f.write(f"- Scope: {start_date} → {end_date}\n")
            f.write(f"- Journal entries posted: {posted}\n")
            f.write(f"- Skipped (no postings): {skipped}\n")
            if detail_rows:
                rem_total = sum(int(r.get("remainder_cents") or 0) for r in detail_rows)
                f.write(f"- Net remainder cents (bank - bill allocations): {rem_total} (${cents_to_dollars(rem_total)})\n")

        conn.commit()

    finally:
        conn.close()

    print("WAVE BILL REIMBURSEMENT JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
