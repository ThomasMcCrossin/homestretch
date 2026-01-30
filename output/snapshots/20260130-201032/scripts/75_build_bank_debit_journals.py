#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date, timedelta
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


def fetch_missing_bank_debits(conn, *, start_date: str, end_date: str) -> list[BankTxn]:
    classifications = fetch_bank_txn_classifications(conn)
    rows = conn.execute(
        """
        SELECT id, txn_date, CAST(debit_cents AS INTEGER) AS debit_cents, description
        FROM fresher_debits__bank_transactions
        WHERE txn_date >= ? AND txn_date <= ?
          AND CAST(debit_cents AS INTEGER) > 0
          AND NOT EXISTS (
            SELECT 1 FROM journal_entries je
            WHERE je.source_bank_line_id = fresher_debits__bank_transactions.id
          )
        ORDER BY txn_date, CAST(id AS INTEGER)
        """,
        (start_date, end_date),
    ).fetchall()
    out: list[BankTxn] = []
    for r in rows:
        bank_txn_id = str(r["id"])
        cat, expl = classifications.get(bank_txn_id, ("", ""))
        out.append(
            BankTxn(
                id=bank_txn_id,
                txn_date=str(r["txn_date"]),
                debit_cents=int(r["debit_cents"] or 0),
                description=str(r["description"] or ""),
                txn_category=cat,
                explanation=expl,
            )
        )
    return out


def is_credit_card_payment(conn, bank_txn_id: str) -> bool:
    row = conn.execute(
        """
        SELECT 1
        FROM fresher_debits__cc_payment_links
        WHERE bank_txn_id = ?
        LIMIT 1
        """,
        (bank_txn_id,),
    ).fetchone()
    return bool(row)

def cc_payment_link_card_last4s(conn, bank_txn_id: str) -> set[str]:
    rows = conn.execute(
        """
        SELECT DISTINCT COALESCE(card_last4, '') AS card_last4
        FROM fresher_debits__cc_payment_links
        WHERE bank_txn_id = ?
        """,
        (bank_txn_id,),
    ).fetchall()
    return {str(r["card_last4"] or "").strip() for r in rows if str(r["card_last4"] or "").strip()}


def find_payroll_net_match(
    conn,
    *,
    amount_cents: int,
    txn_date: str,
    lookback_days: int = 7,
    lookahead_days: int = 7,
) -> tuple[str, str] | None:
    d = parse_iso(txn_date)
    if not d:
        return None
    start = (d - timedelta(days=lookback_days)).isoformat()
    end = (d + timedelta(days=lookahead_days)).isoformat()
    row = conn.execute(
        """
        SELECT employee_name, pay_period_end
        FROM payroll_employee_pay_periods
        WHERE net_pay_cents = ?
          AND pay_period_end >= ? AND pay_period_end <= ?
        ORDER BY pay_period_end, employee_name
        LIMIT 1
        """,
        (int(amount_cents), start, end),
    ).fetchone()
    if not row:
        return None
    return (str(row["employee_name"]), str(row["pay_period_end"]))


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
    ap.add_argument("--reset", action="store_true", help="Delete existing bank debit journals before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    accounts_cfg = cfg.get("accounts", {}) if isinstance(cfg.get("accounts"), dict) else {}
    payroll_cfg = cfg.get("payroll", {}) if isinstance(cfg.get("payroll"), dict) else {}
    revenue_cfg = cfg.get("revenue", {}) if isinstance(cfg.get("revenue"), dict) else {}
    tax_cfg = cfg.get("tax", {}) if isinstance(cfg.get("tax"), dict) else {}
    sh_cfg = cfg.get("shareholders", {}) if isinstance(cfg.get("shareholders"), dict) else {}
    bank_cfg = cfg.get("bank_debits", {}) if isinstance(cfg.get("bank_debits"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("bank_debits") if isinstance(cfg.get("journal_sources"), dict) else {}

    bank_code = str(accounts_cfg.get("bank_account_code") or "1000").strip()
    cc_payable_code = str(accounts_cfg.get("credit_card_payable_code") or "2100").strip()

    wages_payable_code = str(payroll_cfg.get("wages_payable_code") or "2000").strip()
    thomas_payable_code = str(payroll_cfg.get("due_to_shareholder_thomas_code") or "2400").strip()
    dwayne_payable_code = str(payroll_cfg.get("due_to_shareholder_dwayne_code") or "2410").strip()

    due_from_shareholder_code = str(sh_cfg.get("due_from_shareholder_code") or "2500").strip()
    dividends_declared_code = str(sh_cfg.get("dividends_declared_code") or "3400").strip()

    bank_fees_expense_code = str(bank_cfg.get("bank_fees_expense_code") or "6000").strip()
    cash_on_hand_code = str(bank_cfg.get("cash_on_hand_code") or "1070").strip()

    cash_sales_code = str(revenue_cfg.get("cash_deposit_sales_code") or "4000").strip()
    shopify_returns_code = str(revenue_cfg.get("shopify_returns_code") or "4900").strip()

    hst_payable_code = str(tax_cfg.get("hst_payable_code") or "2200").strip()

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "bank_debits")
    entry_type = str((source_cfg or {}).get("entry_type") or "PAYMENT")

    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "bank_debit_journal_summary.md"
    out_detail_csv = args.out_dir / "bank_debit_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        bank_override_entries = load_bank_txn_category_override_entries(args.bank_overrides)

        if args.reset:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )

        txns = fetch_missing_bank_debits(conn, start_date=start_date, end_date=end_date)

        supported_categories = {
            "EMPLOYEE_PAYROLL",
            "SHAREHOLDER_PAYROLL",
            "PAYROLL",
            "OWNER_DRAW",
            "DIVIDEND",
            "LOAN_ISSUED",
            "CHANGE_FLOAT",
            "BANK_FEE",
            "GST_HST_REMIT",
            "HST_REIMBURSEMENT",
            "DUCKS_REVENUE_RETURN",
            "REIMBURSEMENT",
            "RENT_REIMBURSEMENT",
            "DEPOSIT_CORRECTION",
            "UNCLASSIFIED",
            "",
        }

        posted = 0
        unsupported = 0
        detail_rows: list[dict[str, str]] = []

        for t in txns:
            if t.debit_cents <= 0:
                continue

            evidence_category = (t.txn_category or "").strip() or "UNCLASSIFIED"
            category = evidence_category
            override_entry = bank_override_entries.get(t.id)
            override_applied = False
            override_to_category = ""
            override_reason = ""
            override_mismatch = ""
            if override_entry:
                override_to_category = str(override_entry.get("to_category") or "").strip()
                expected_date = str(override_entry.get("txn_date") or "").strip()
                expected_debit = override_entry.get("debit_cents")
                mismatches: list[str] = []
                if expected_date and expected_date != t.txn_date:
                    mismatches.append(f"txn_date expected {expected_date} got {t.txn_date}")
                if expected_debit is not None and str(expected_debit).strip() != "":
                    try:
                        expected_debit_cents = int(expected_debit)
                    except ValueError:
                        mismatches.append(f"debit_cents override not int: {expected_debit}")
                    else:
                        if expected_debit_cents != t.debit_cents:
                            mismatches.append(
                                f"debit_cents expected {expected_debit_cents} got {t.debit_cents}"
                            )
                if mismatches:
                    override_mismatch = "; ".join(mismatches)
                else:
                    category = override_to_category or category
                    override_applied = True
                    override_reason = str(override_entry.get("reason") or "").strip()

            if category not in supported_categories:
                unsupported += 1
                continue

            debit_account = ""
            debit_reason = ""

            if category in ("EMPLOYEE_PAYROLL", "PAYROLL"):
                debit_account = wages_payable_code
                debit_reason = "clear_net_pay_payable"

            elif category == "SHAREHOLDER_PAYROLL":
                debit_account = wages_payable_code
                match = find_payroll_net_match(conn, amount_cents=t.debit_cents, txn_date=t.txn_date)
                if match:
                    employee_name, pay_period_end = match
                    debit_reason = f"clear_net_pay_payable_match:{employee_name}:{pay_period_end}"
                else:
                    debit_reason = "clear_net_pay_payable_shareholder_payroll"

            elif category == "DIVIDEND":
                debit_account = dividends_declared_code
                debit_reason = "dividend_paid"

            elif category in ("OWNER_DRAW", "LOAN_ISSUED"):
                debit_account = due_from_shareholder_code
                debit_reason = "due_from_shareholder"

            elif category == "CHANGE_FLOAT":
                debit_account = cash_on_hand_code
                debit_reason = "cash_float"

            elif category == "BANK_FEE":
                debit_account = bank_fees_expense_code
                debit_reason = "bank_fees"

            elif category == "GST_HST_REMIT":
                debit_account = hst_payable_code
                debit_reason = "hst_payment"

            elif category == "DUCKS_REVENUE_RETURN":
                debit_account = shopify_returns_code
                debit_reason = "contra_revenue_ducks_ticket_remit"

            elif category == "REIMBURSEMENT":
                debit_account = shareholder_account_from_text(
                    f"{t.description} {t.explanation}",
                    thomas_code=thomas_payable_code,
                    dwayne_code=dwayne_payable_code,
                    default_code=thomas_payable_code,
                )
                debit_reason = "clear_due_to_shareholder"

            elif category in ("RENT_REIMBURSEMENT", "HST_REIMBURSEMENT"):
                debit_account = shareholder_account_from_text(
                    f"{t.description} {t.explanation}",
                    thomas_code=thomas_payable_code,
                    dwayne_code=dwayne_payable_code,
                    default_code=thomas_payable_code,
                )
                debit_reason = "clear_due_to_shareholder"

            elif category == "DEPOSIT_CORRECTION":
                debit_account = cash_sales_code
                debit_reason = "contra_cash_deposit"

            elif category == "UNCLASSIFIED":
                if is_credit_card_payment(conn, t.id):
                    # Personal credit card(s) used for business: bank is paying the card company,
                    # which clears the corp's payable to the shareholder (not a draw/loan by default).
                    debit_account = dwayne_payable_code
                    cards = ",".join(sorted(cc_payment_link_card_last4s(conn, t.id)))
                    debit_reason = f"cc_payment_clear_due_to_shareholder:{cards}" if cards else "cc_payment_clear_due_to_shareholder"
                else:
                    debit_account = due_from_shareholder_code
                    debit_reason = "unclassified_default_due_from_shareholder"

            else:
                debit_account = due_from_shareholder_code
                debit_reason = "fallback_due_from_shareholder"

            je_id = f"BANK_DEBIT_{t.id}"
            label = category.replace("_", " ").title()
            if category == "DIVIDEND":
                label = "Dividend paid"
            elif category in ("OWNER_DRAW", "LOAN_ISSUED"):
                label = "Shareholder Advance (Due from shareholder)"
            description = f"{label} - bank txn {t.id}"
            notes = (
                f"bank_txn_id={t.id}; category={category}; evidence_category={evidence_category}; "
                f"override_applied={override_applied}; override_to_category={override_to_category}; "
                f"override_mismatch={override_mismatch}; override_reason={override_reason}; debit_reason={debit_reason}; "
                f"debit_cents={t.debit_cents}; explanation={t.explanation}"
            )

            conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
            conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

            conn.execute(
                """
                INSERT INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id,
                  source_bank_line_id, notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    t.txn_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    t.id,
                    t.id,
                    notes,
                ),
            )

            # Two-line entry by design: debit intent + credit bank.
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
                    debit_account,
                    t.debit_cents,
                    0,
                    t.explanation or debit_reason or category,
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
                    t.debit_cents,
                    t.description or "Bank debit",
                ),
            )

            posted += 1
            detail_rows.append(
                {
                    "bank_txn_id": t.id,
                    "bank_date": t.txn_date,
                    "evidence_category": evidence_category,
                    "category": category,
                    "override_applied": "1" if override_applied else "0",
                    "override_to_category": override_to_category,
                    "amount_cents": str(t.debit_cents),
                    "amount": cents_to_dollars(t.debit_cents),
                    "debit_account": debit_account,
                    "debit_reason": debit_reason,
                    "journal_entry_id": je_id,
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "bank_txn_id",
                "bank_date",
                "evidence_category",
                "category",
                "override_applied",
                "override_to_category",
                "amount_cents",
                "amount",
                "debit_account",
                "debit_reason",
                "journal_entry_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Bank debit journals\n\n")
            f.write(f"- Scope: {start_date} → {end_date}\n")
            f.write(f"- Missing bank debits in scope: {len(txns)}\n")
            f.write(f"- Posted: {posted}\n")
            f.write(f"- Unsupported (ignored): {unsupported}\n")
            f.write("\n## Categories posted\n\n")
            counts: dict[str, int] = {}
            for r in detail_rows:
                counts[r["category"]] = counts.get(r["category"], 0) + 1
            for cat, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
                f.write(f"- {cat}: {n}\n")

        conn.commit()

    finally:
        conn.close()

    print("BANK DEBIT JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
