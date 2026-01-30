#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"
DEFAULT_BANK_OVERRIDE_PATH = PROJECT_ROOT / "overrides" / "bank_txn_category_overrides.yml"


@dataclass(frozen=True)
class MonthlyComponentTotals:
    cpp_cents: int
    ei_cents: int
    tax_cents: int

    @property
    def remittance_cents(self) -> int:
        return self.cpp_cents + self.ei_cents + self.tax_cents


MONTH_NAME_TO_NUM = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def parse_cra_payment_month(label: str) -> tuple[int, int] | None:
    s = (label or "").strip()
    m = re.match(r"^Payment\s+([A-Za-z]+)\s+(20[0-9]{2})\b", s)
    if not m:
        return None
    month_name = m.group(1).strip().lower()
    year = int(m.group(2))
    month = MONTH_NAME_TO_NUM.get(month_name)
    if not month:
        return None
    return (year, month)


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


def fetch_bank_txn_categories(conn) -> dict[str, str]:
    rows = conn.execute(
        """
        SELECT id, bank_txn_id, txn_category, verified
        FROM fresher_debits__bank_txn_classifications
        ORDER BY CAST(verified AS INTEGER) DESC, CAST(id AS INTEGER) ASC
        """
    ).fetchall()
    out: dict[str, str] = {}
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"])
        if bank_txn_id in out:
            continue
        out[bank_txn_id] = str(r["txn_category"])
    return out


def fetch_bank_match_for_amount(conn, *, txn_date: str, amount_cents: int) -> tuple[str, str | None, str] | None:
    if not txn_date or not amount_cents:
        return None
    row = conn.execute(
        """
        SELECT
          t.id AS bank_txn_id,
          c.txn_category AS txn_category,
          t.description AS description
        FROM fresher_debits__bank_transactions t
        LEFT JOIN fresher_debits__bank_txn_classifications c ON c.bank_txn_id = t.id
        WHERE t.txn_date = ?
          AND CAST(t.debit_cents AS INTEGER) = ?
        ORDER BY
          CASE
            WHEN c.txn_category IN ('PAYROLL_REMIT', 'PAYROLL_REIMBURSE') THEN 0
            ELSE 1
          END,
          t.id
        LIMIT 1
        """,
        (txn_date, amount_cents),
    ).fetchone()
    if not row:
        return None
    return (str(row["bank_txn_id"]), (str(row["txn_category"]) if row["txn_category"] is not None else None), str(row["description"] or ""))


def fetch_monthly_components(conn) -> dict[tuple[int, int], MonthlyComponentTotals]:
    # Employee exports: group by pay_period_end month.
    rows = conn.execute(
        """
        SELECT
          substr(pay_period_end, 1, 4) AS yyyy,
          substr(pay_period_end, 6, 2) AS mm,
          SUM(employee_cpp_cents + employer_cpp_cents) AS cpp_cents,
          SUM(employee_ei_cents + employer_ei_cents) AS ei_cents,
          SUM(federal_tax_cents + provincial_tax_cents) AS tax_cents
        FROM payroll_employee_pay_periods
        GROUP BY yyyy, mm
        """
    ).fetchall()
    employee = {
        (int(r["yyyy"]), int(r["mm"])): MonthlyComponentTotals(
            cpp_cents=int(r["cpp_cents"] or 0),
            ei_cents=int(r["ei_cents"] or 0),
            tax_cents=int(r["tax_cents"] or 0),
        )
        for r in rows
    }

    # Curlysbooks backfill: use end_date month.
    rows = conn.execute(
        """
        SELECT
          substr(p.end_date, 1, 4) AS yyyy,
          substr(p.end_date, 6, 2) AS mm,
          SUM(r.total_cpp_cents + r.total_cpp2_cents + r.total_employer_cpp_cents + r.total_employer_cpp2_cents) AS cpp_cents,
          SUM(r.total_ei_cents + r.total_employer_ei_cents) AS ei_cents,
          SUM(r.total_federal_tax_cents + r.total_provincial_tax_cents) AS tax_cents
        FROM curlysbooks_payroll_runs r
        JOIN curlysbooks_pay_periods p ON p.pay_period_id = r.pay_period_id
        WHERE p.entity = 'corp'
          AND p.tax_year = 2025
          AND r.calculated_by = 'backfill_csv_2025_corp'
        GROUP BY yyyy, mm
        """
    ).fetchall()
    backfill = {
        (int(r["yyyy"]), int(r["mm"])): MonthlyComponentTotals(
            cpp_cents=int(r["cpp_cents"] or 0),
            ei_cents=int(r["ei_cents"] or 0),
            tax_cents=int(r["tax_cents"] or 0),
        )
        for r in rows
    }

    # Prefer backfill when present, else employee exports.
    combined: dict[tuple[int, int], MonthlyComponentTotals] = {}
    for key in set(employee.keys()) | set(backfill.keys()):
        combined[key] = backfill.get(key) or employee.get(key) or MonthlyComponentTotals(0, 0, 0)
    return combined


def allocate_amount(amount_cents: int, components: MonthlyComponentTotals) -> dict[str, int]:
    total = components.remittance_cents
    if total <= 0:
        return {"cpp": 0, "ei": 0, "tax": 0}

    parts = [
        ("cpp", components.cpp_cents),
        ("ei", components.ei_cents),
        ("tax", components.tax_cents),
    ]
    raw = [(k, amount_cents * v / total) for k, v in parts]
    floors = {k: int(x) for k, x in raw}
    remainder = amount_cents - sum(floors.values())
    fracs = sorted(((k, x - int(x)) for k, x in raw), key=lambda t: (-t[1], t[0]))
    for i in range(abs(remainder)):
        k = fracs[i % len(fracs)][0]
        floors[k] += 1 if remainder > 0 else -1
    return floors


def sum_components_for_year(monthly: dict[tuple[int, int], MonthlyComponentTotals], *, year: int) -> MonthlyComponentTotals:
    cpp = 0
    ei = 0
    tax = 0
    for (yyyy, _mm), c in monthly.items():
        if yyyy != year:
            continue
        cpp += int(c.cpp_cents or 0)
        ei += int(c.ei_cents or 0)
        tax += int(c.tax_cents or 0)
    return MonthlyComponentTotals(cpp_cents=cpp, ei_cents=ei, tax_cents=tax)


def shareholder_account_from_description(desc: str, *, thomas_code: str, dwayne_code: str, default_code: str) -> str:
    d = (desc or "").lower()
    if "dwayne" in d:
        return dwayne_code
    if "thomas" in d:
        return thomas_code
    return default_code


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def find_subset_sum_indices(amounts: list[int], target: int) -> list[int] | None:
    """
    Small helper for matching multiple CRA credits to a single bank reimbursement.
    Returns indices of `amounts` that sum to `target`, or None if no exact match.
    """
    n = len(amounts)
    if target <= 0 or n == 0:
        return None

    # Exact single hit fast-path.
    for i, amt in enumerate(amounts):
        if amt == target:
            return [i]

    # Backtracking (n is expected to be tiny per date).
    indexed = sorted(list(enumerate(amounts)), key=lambda t: (-t[1], t[0]))

    def rec(pos: int, remaining: int, chosen: list[int]) -> list[int] | None:
        if remaining == 0:
            return chosen
        if remaining < 0 or pos >= n:
            return None
        idx, amt = indexed[pos]
        if amt <= remaining:
            out = rec(pos + 1, remaining - amt, chosen + [idx])
            if out is not None:
                return out
        return rec(pos + 1, remaining, chosen)

    return rec(0, target, [])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--bank-overrides", type=Path, default=DEFAULT_BANK_OVERRIDE_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing payroll remittance journals before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    scope_start = min(fy.start_date for fy in fys)
    scope_end = max(fy.end_date for fy in fys)

    cfg = load_config(args.config)
    payroll_cfg = cfg.get("payroll", {}) if isinstance(cfg.get("payroll"), dict) else {}
    bank_cfg = cfg.get("bank_debits", {}) if isinstance(cfg.get("bank_debits"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("payroll_summary") if isinstance(cfg.get("journal_sources"), dict) else {}

    liability_cpp_code = str(payroll_cfg.get("payroll_liability_cpp_code") or "2700").strip()
    liability_ei_code = str(payroll_cfg.get("payroll_liability_ei_code") or "2710").strip()
    liability_tax_code = str(payroll_cfg.get("payroll_liability_tax_code") or "2720").strip()
    bank_code = str((cfg.get("accounts") or {}).get("bank_account_code") or "1000").strip()
    thomas_code = str(payroll_cfg.get("due_to_shareholder_thomas_code") or "2400").strip()
    dwayne_code = str(payroll_cfg.get("due_to_shareholder_dwayne_code") or "2410").strip()
    default_shareholder_code = str(payroll_cfg.get("remit_unmatched_credit_code") or thomas_code).strip()
    interest_expense_bank_code = str(bank_cfg.get("interest_expense_bank_code") or "8100").strip()

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = "payroll_remittance"
    entry_type = "PAYMENT"

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "payroll_remittance_journal_summary.md"
    out_detail_csv = args.out_dir / "payroll_remittance_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                """
                DELETE FROM journal_entries
                WHERE source_system = ? AND source_record_type = ?
                """,
                (source_system, source_record_type),
            )

        bank_overrides = load_bank_txn_category_override_entries(args.bank_overrides)
        bank_categories = fetch_bank_txn_categories(conn)
        monthly_components = fetch_monthly_components(conn)

        detail_rows: list[dict[str, str]] = []
        posted = 0
        skipped = 0
        reimburse_posted = 0

        # CRA credits -> payroll remittance clearing.
        # We only build journals within the project fiscal-year scope.
        cra_rows = conn.execute(
            """
            SELECT id, date_posted, date_received, transaction_label, amount_cents, cr_dr
            FROM cra_payroll_account_transactions
            WHERE cr_dr IS NOT NULL AND amount_cents IS NOT NULL
            ORDER BY date_posted, source_row
            """
        ).fetchall()

        used_bank_txn_ids: set[str] = set()

        # Pre-index bank transactions by txn_date to support group-matching
        # (multiple CRA credits reimbursed via one shareholder e-transfer).
        bank_txns_by_date: dict[str, list[tuple[str, int, str, str]]] = {}
        rows = conn.execute(
            """
            SELECT id, txn_date, description, CAST(debit_cents AS INTEGER) AS debit_cents
            FROM fresher_debits__bank_transactions
            WHERE txn_date >= ? AND txn_date <= ?
              AND CAST(debit_cents AS INTEGER) > 0
            ORDER BY txn_date, CAST(id AS INTEGER)
            """,
            (scope_start, scope_end),
        ).fetchall()
        for r in rows:
            bank_txn_id = str(r["id"])
            txn_date = str(r["txn_date"] or "")
            debit_cents = int(r["debit_cents"] or 0)
            desc = str(r["description"] or "")
            cat = str(bank_categories.get(bank_txn_id, "") or "").strip()
            if bank_txn_id in bank_overrides:
                cat = str(bank_overrides[bank_txn_id].get("to_category") or cat or "").strip()
            bank_txns_by_date.setdefault(txn_date, []).append((bank_txn_id, debit_cents, cat, desc))

        # First pass: decide matching for each CRA credit, without inserting.
        cra_records: list[dict[str, object]] = []
        for r in cra_rows:
            if str(r["cr_dr"] or "").strip().upper() != "CR":
                continue
            amount_cents = int(r["amount_cents"] or 0)
            if amount_cents <= 0:
                continue
            label = str(r["transaction_label"] or "")
            label_norm = label.strip()
            month_key = parse_cra_payment_month(label_norm)
            allocation_label = ""
            components = None
            if month_key:
                components = monthly_components.get(month_key)
                allocation_label = f"{month_key[0]}-{month_key[1]:02d}"
            elif label_norm == "Late year-end payment 2024":
                components = sum_components_for_year(monthly_components, year=2024)
                allocation_label = "2024-YE"
            elif label_norm == "Arrears payment":
                components = None
                allocation_label = "ARREARS"
            else:
                skipped += 1
                continue

            if components and components.remittance_cents <= 0:
                skipped += 1
                continue

            date_received = str(r["date_received"] or "") or None
            entry_date = (date_received or str(r["date_posted"] or "")).strip()
            if not entry_date or entry_date < scope_start or entry_date > scope_end:
                # Outside project fiscal-year scope.
                continue

            # Attempt exact match to a same-day bank transaction.
            bank_txn_id = ""
            bank_txn_category = ""
            bank_desc = ""
            credit_account = default_shareholder_code
            match_kind = "UNMATCHED_DEFAULT"

            if date_received:
                candidates = bank_txns_by_date.get(date_received) or []
                # Find exact amount match (stable: lowest id for the day).
                for (bid, debit_c, cat, desc) in candidates:
                    if debit_c != amount_cents:
                        continue
                    bank_txn_id, bank_txn_category, bank_desc = bid, cat, desc
                    break

                if bank_txn_id:
                    if bank_txn_category == "PAYROLL_REMIT":
                        credit_account = bank_code
                        used_bank_txn_ids.add(bank_txn_id)
                        match_kind = "EXACT_BANK_PAYMENT"
                    elif bank_txn_category == "PAYROLL_REIMBURSE":
                        credit_account = shareholder_account_from_description(
                            bank_desc,
                            thomas_code=thomas_code,
                            dwayne_code=dwayne_code,
                            default_code=default_shareholder_code,
                        )
                        match_kind = "EXACT_BANK_REIMBURSE"
                    else:
                        # Unknown exact match category; keep default credit account but keep trace.
                        match_kind = "EXACT_BANK_OTHER"

            cra_records.append(
                {
                    "cra_id": str(r["id"]),
                    "date_received": date_received or "",
                    "entry_date": entry_date,
                    "label_norm": label_norm,
                    "amount_cents": amount_cents,
                    "allocation_label": allocation_label,
                    "components": components,
                    "bank_txn_id": bank_txn_id,
                    "bank_txn_category": bank_txn_category,
                    "credit_account": credit_account,
                    "match_kind": match_kind,
                }
            )

        # Second pass: for each day, if there is a PAYROLL_REIMBURSE bank txn whose amount equals
        # the sum of multiple unmatched CRA credits, treat those CRA credits as paid personally
        # and reimbursed via that bank txn (credit the correct shareholder payable).
        cra_by_date: dict[str, list[dict[str, object]]] = {}
        for rec in cra_records:
            date_received = str(rec.get("date_received") or "").strip()
            if not date_received:
                continue
            cra_by_date.setdefault(date_received, []).append(rec)

        for txn_date, recs in cra_by_date.items():
            # Only consider CRA recs that are still unmatched.
            unmatched = [r for r in recs if r.get("match_kind") == "UNMATCHED_DEFAULT"]
            if not unmatched:
                continue
            reimburse_txns = [
                (bid, amt, desc)
                for (bid, amt, cat, desc) in (bank_txns_by_date.get(txn_date) or [])
                if cat == "PAYROLL_REIMBURSE"
            ]
            if not reimburse_txns:
                continue

            # Greedy: match largest reimbursement first.
            reimburse_txns.sort(key=lambda t: (-t[1], t[0]))
            remaining = unmatched[:]
            for bank_txn_id, bank_amt, bank_desc in reimburse_txns:
                amounts = [int(r["amount_cents"]) for r in remaining]
                idxs = find_subset_sum_indices(amounts, bank_amt)
                if not idxs:
                    continue
                shareholder_code = shareholder_account_from_description(
                    bank_desc,
                    thomas_code=thomas_code,
                    dwayne_code=dwayne_code,
                    default_code=default_shareholder_code,
                )
                # Apply assignment.
                matched_set = {remaining[i]["cra_id"] for i in idxs}
                for r in remaining:
                    if r["cra_id"] not in matched_set:
                        continue
                    r["bank_txn_id"] = bank_txn_id
                    r["bank_txn_category"] = "PAYROLL_REIMBURSE"
                    r["credit_account"] = shareholder_code
                    r["match_kind"] = "GROUP_REIMBURSE_SUM"
                # Remove matched from remaining.
                remaining = [r for r in remaining if r["cra_id"] not in matched_set]
                if not remaining:
                    break

        # Insert CRA-derived payroll remittance journals.
        for rec in cra_records:
            amount_cents = int(rec["amount_cents"])
            label_norm = str(rec["label_norm"])
            allocation_label = str(rec["allocation_label"])
            components = rec.get("components")
            entry_date = str(rec["entry_date"])
            bank_txn_id = str(rec.get("bank_txn_id") or "")
            bank_txn_category = str(rec.get("bank_txn_category") or "")
            credit_account = str(rec.get("credit_account") or default_shareholder_code)

            je_id = f"PAYROLL_REMITTANCE_CRA_{rec['cra_id']}"
            description = f"CRA payroll payment {label_norm}".strip()
            notes = (
                f"cra_id={rec['cra_id']}; label={label_norm}; payroll_bucket={allocation_label}; "
                f"amount_cents={amount_cents}; bank_txn_id={bank_txn_id}; bank_txn_category={bank_txn_category}; "
                f"match_kind={rec.get('match_kind')}"
            )

            conn.execute(
                """
                INSERT INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id, source_bank_line_id, notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    entry_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    str(rec["cra_id"]),
                    (bank_txn_id if credit_account == bank_code else None),
                    notes,
                ),
            )

            line_number = 1
            cpp_cents = 0
            ei_cents = 0
            tax_cents = 0

            if label_norm == "Arrears payment":
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
                        interest_expense_bank_code,
                        amount_cents,
                        0,
                        "Payroll arrears payment (interest/penalty)",
                    ),
                )
                line_number += 1
            else:
                allocations = allocate_amount(amount_cents, components or MonthlyComponentTotals(0, 0, 0))
                cpp_cents = allocations["cpp"]
                ei_cents = allocations["ei"]
                tax_cents = allocations["tax"]
                for code, amt, label_name in [
                    (liability_cpp_code, cpp_cents, "CPP liability"),
                    (liability_ei_code, ei_cents, "EI liability"),
                    (liability_tax_code, tax_cents, "Income tax liability"),
                ]:
                    if amt == 0:
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
                            code,
                            amt,
                            0,
                            label_name,
                        ),
                    )
                    line_number += 1

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
                    credit_account,
                    0,
                    amount_cents,
                    "Payroll remittance payment",
                ),
            )

            posted += 1
            detail_rows.append(
                {
                    "cra_id": str(rec["cra_id"]),
                    "date_received": str(rec.get("date_received") or ""),
                    "transaction_label": label_norm,
                    "amount_cents": str(amount_cents),
                    "payroll_month": allocation_label,
                    "cpp_cents": str(cpp_cents),
                    "ei_cents": str(ei_cents),
                    "tax_cents": str(tax_cents),
                    "credit_account": credit_account,
                    "bank_txn_id": bank_txn_id,
                    "bank_txn_category": bank_txn_category,
                    "journal_entry_id": je_id,
                }
            )

        # Reimbursement bank txns -> clear due to shareholder.
        rows = conn.execute(
            """
            SELECT t.id, t.txn_date, CAST(t.debit_cents AS INTEGER) AS debit_cents, t.description
            FROM fresher_debits__bank_transactions t
            JOIN fresher_debits__bank_txn_classifications c ON c.bank_txn_id = t.id
            WHERE c.txn_category = 'PAYROLL_REIMBURSE'
              AND t.txn_date >= ? AND t.txn_date <= ?
            ORDER BY t.txn_date, t.id
            """,
            (scope_start, scope_end),
        ).fetchall()

        for r in rows:
            bank_txn_id = str(r["id"])
            if bank_txn_id in used_bank_txn_ids:
                continue
            amount_cents = int(r["debit_cents"] or 0)
            if amount_cents <= 0:
                continue
            desc = str(r["description"] or "")
            shareholder_code = shareholder_account_from_description(
                desc, thomas_code=thomas_code, dwayne_code=dwayne_code, default_code=default_shareholder_code
            )
            je_id = f"PAYROLL_REIMBURSE_{bank_txn_id}"
            conn.execute(
                """
                INSERT INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id, source_bank_line_id, notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    str(r["txn_date"]),
                    "PAYMENT",
                    "Payroll remittance reimbursement",
                    source_system,
                    source_record_type,
                    f"bank_txn:{bank_txn_id}",
                    bank_txn_id,
                    f"bank_txn_id={bank_txn_id}; shareholder_account={shareholder_code}",
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
                    shareholder_code,
                    amount_cents,
                    0,
                    "Due to shareholder (payroll remittance)",
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
                    bank_code,
                    0,
                    amount_cents,
                    desc or "Bank reimbursement",
                ),
            )
            reimburse_posted += 1

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "cra_id",
                "date_received",
                "transaction_label",
                "amount_cents",
                "payroll_month",
                "cpp_cents",
                "ei_cents",
                "tax_cents",
                "credit_account",
                "bank_txn_id",
                "bank_txn_category",
                "journal_entry_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Payroll remittance journals\n\n")
            f.write(f"- Scope: {scope_start} → {scope_end}\n")
            f.write(f"- CRA payment journals posted: {posted}\n")
            f.write(f"- CRA rows skipped (non-payment or missing month): {skipped}\n")
            f.write(f"- Reimbursement journals posted: {reimburse_posted}\n")
            f.write("\nNotes:\n")
            f.write("- CRA `Payment <Month> <Year>` credits are allocated across CPP/EI/Tax using monthly payroll component ratios.\n")
            f.write("- If a CRA payment matches a bank txn categorized `PAYROLL_REMIT`, credit is bank.\n")
            f.write("- If it matches `PAYROLL_REIMBURSE` (or no bank match), credit is due-to-shareholder (default). Reimbursements clear that payable.\n")

        conn.commit()

    finally:
        conn.close()

    print("PAYROLL REMITTANCE JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted} CRA payments, {reimburse_posted} reimbursements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
