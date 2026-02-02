#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"


@dataclass(frozen=True)
class CreditBankItem:
    bank_item_id: str
    bank_txn_id: str
    txn_date: str
    amount_cents: int
    description: str
    category: str


@dataclass(frozen=True)
class FloatEvent:
    txn_date: str
    bank_txn_id: str
    bank_txn_id_int: int
    kind: str  # WITHDRAW | DEPOSIT
    amount_cents: int


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


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

def parse_int(value: object, *, default: int = 0) -> int:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return default


def parse_int_maybe(value: object) -> int | None:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def split_tax_inclusive(amount_cents: int, *, rate: Decimal) -> tuple[int, int]:
    """
    Split a tax-inclusive amount into (net_cents, tax_cents) assuming a flat rate.
    Deterministic cent rounding using ROUND_HALF_UP on the net component.
    """
    if amount_cents == 0:
        return (0, 0)
    if rate <= 0:
        return (amount_cents, 0)
    gross = Decimal(int(amount_cents))
    denom = Decimal("1") + rate
    net = (gross / denom).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    net_cents = int(net)
    tax_cents = int(amount_cents) - net_cents
    return (net_cents, tax_cents)


def fetch_credit_bank_items(conn, *, start_date: str, end_date: str) -> list[CreditBankItem]:
    rows = conn.execute(
        """
        SELECT
          b.id AS bank_item_id,
          b.bank_txn_id AS bank_txn_id,
          b.txn_date AS txn_date,
          CAST(b.amount_cents AS INTEGER) AS amount_cents,
          b.description AS description,
          c.category AS category
        FROM fresher_credits__credit_bank_items b
        JOIN fresher_credits__credit_item_classifications c ON c.bank_item_id = b.id
        WHERE b.txn_date >= ? AND b.txn_date <= ?
        ORDER BY b.txn_date, CAST(b.bank_txn_id AS INTEGER)
        """,
        (start_date, end_date),
    ).fetchall()
    out: list[CreditBankItem] = []
    for r in rows:
        out.append(
            CreditBankItem(
                bank_item_id=str(r["bank_item_id"]),
                bank_txn_id=str(r["bank_txn_id"]),
                txn_date=str(r["txn_date"]),
                amount_cents=int(r["amount_cents"] or 0),
                description=str(r["description"] or ""),
                category=str(r["category"] or ""),
            )
        )
    return out


def fetch_shopify_payout_for_bank_txn(conn, bank_txn_id: str) -> dict | None:
    row = conn.execute(
        """
        SELECT p.*
        FROM fresher_credits__shopify_payout_bank_links l
        JOIN fresher_credits__shopify_payouts p ON p.id = l.payout_id
        WHERE l.bank_txn_id = ?
        LIMIT 1
        """,
        (bank_txn_id,),
    ).fetchone()
    if not row:
        return None
    return dict(row)

def fetch_gfs_eft_notification_id_for_bank_txn(conn, bank_txn_id: str) -> str | None:
    row = conn.execute(
        """
        SELECT l.notification_id AS notification_id
        FROM fresher_credits__gfs_eft_bank_links l
        JOIN fresher_credits__credit_bank_items b ON b.id = l.bank_item_id
        WHERE b.bank_txn_id = ?
        LIMIT 1
        """,
        (bank_txn_id,),
    ).fetchone()
    return str(row["notification_id"]) if row else None


def fetch_bank_txn_classifications(conn) -> dict[str, str]:
    """
    Prefer verified classifications when multiple exist.
    Returns bank_txn_id -> txn_category
    """
    rows = conn.execute(
        """
        SELECT id, bank_txn_id, txn_category, verified
        FROM fresher_debits__bank_txn_classifications
        ORDER BY CAST(verified AS INTEGER) DESC, CAST(id AS INTEGER) ASC
        """
    ).fetchall()
    out: dict[str, str] = {}
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"] or "").strip()
        if not bank_txn_id or bank_txn_id in out:
            continue
        out[bank_txn_id] = str(r["txn_category"] or "").strip()
    return out


def fetch_bank_txn_ids_claimed_by_non_bank_debits(conn) -> set[str]:
    """
    Bank debit lines are journalized by multiple builders (Wave payments, bank debits, etc.).
    When a bank_txn_id is already claimed by a non-bank_debits journal source, it won't be
    posted by the bank_debits journal builder, even if it has a CHANGE_FLOAT classification.
    For cash-float allocation, treat those as "not change-float withdrawals" to avoid double
    counting.
    """
    rows = conn.execute(
        """
        SELECT DISTINCT COALESCE(source_bank_line_id, '') AS bank_txn_id
        FROM journal_entries
        WHERE source_bank_line_id IS NOT NULL
          AND source_record_type <> 'bank_debits'
        """
    ).fetchall()
    out: set[str] = set()
    for r in rows:
        bank_txn_id = str(r["bank_txn_id"] or "").strip()
        if bank_txn_id:
            out.add(bank_txn_id)
    return out


def fetch_change_float_withdrawals(conn, *, start_date: str, end_date: str) -> list[FloatEvent]:
    cats = fetch_bank_txn_classifications(conn)
    claimed = fetch_bank_txn_ids_claimed_by_non_bank_debits(conn)
    rows = conn.execute(
        """
        SELECT id, txn_date, CAST(debit_cents AS INTEGER) AS debit_cents
        FROM fresher_debits__bank_transactions
        WHERE txn_date >= ? AND txn_date <= ?
          AND CAST(debit_cents AS INTEGER) > 0
        ORDER BY txn_date, CAST(id AS INTEGER)
        """,
        (start_date, end_date),
    ).fetchall()
    out: list[FloatEvent] = []
    for r in rows:
        bank_txn_id = str(r["id"] or "").strip()
        if not bank_txn_id:
            continue
        if bank_txn_id in claimed:
            continue
        if cats.get(bank_txn_id) != "CHANGE_FLOAT":
            continue
        bank_txn_id_int = parse_int_maybe(bank_txn_id)
        if bank_txn_id_int is None:
            continue
        cents = int(r["debit_cents"] or 0)
        if cents <= 0:
            continue
        out.append(
            FloatEvent(
                txn_date=str(r["txn_date"]),
                bank_txn_id=bank_txn_id,
                bank_txn_id_int=bank_txn_id_int,
                kind="WITHDRAW",
                amount_cents=cents,
            )
        )
    return out


def compute_cash_deposit_float_returns(
    cash_deposits: list[FloatEvent],
    float_withdrawals: list[FloatEvent],
    *,
    fys: list[FiscalYear],
    year_end_target_cents: int,
) -> dict[str, int]:
    """
    Allocate a portion of each CASH_DEPOSIT to "return of change float" (clears cash on hand).

    Mechanism:
    1) Full FIFO clearing: deposits clear the running float balance up to the deposit amount.
    2) Year-end target: then "undo" clearing within each FY (latest deposits first) so that
       cash-on-hand at each FY end is at least year_end_target_cents (best-effort).
    """
    deposits = [e for e in cash_deposits if e.kind == "DEPOSIT" and e.amount_cents > 0]
    withdrawals = [e for e in float_withdrawals if e.kind == "WITHDRAW" and e.amount_cents > 0]
    if not deposits or not withdrawals:
        return {}

    events = sorted(withdrawals + deposits, key=lambda e: (e.txn_date, e.bank_txn_id_int))

    float_balance = 0
    returns: dict[str, int] = {}
    for e in events:
        if e.kind == "WITHDRAW":
            float_balance += e.amount_cents
            continue
        clear = min(float_balance, e.amount_cents)
        float_balance -= clear
        returns[e.bank_txn_id] = clear

    if year_end_target_cents <= 0:
        return returns

    def balance_at(end_date_inclusive: str) -> int:
        bal = 0
        for ev in events:
            if ev.txn_date > end_date_inclusive:
                break
            if ev.kind == "WITHDRAW":
                bal += ev.amount_cents
            else:
                bal -= int(returns.get(ev.bank_txn_id, 0))
        return bal

    fys_by_end = sorted(fys, key=lambda fy: fy.end_date)
    for fy in fys_by_end:
        bal_end = balance_at(fy.end_date)
        if bal_end >= year_end_target_cents:
            continue
        delta = year_end_target_cents - bal_end

        fy_deposits = [d for d in deposits if fy.start_date <= d.txn_date <= fy.end_date]
        fy_deposits.sort(key=lambda e: (e.txn_date, e.bank_txn_id_int))
        for d in reversed(fy_deposits):
            cur = int(returns.get(d.bank_txn_id, 0))
            if cur <= 0:
                continue
            dec = min(delta, cur)
            returns[d.bank_txn_id] = cur - dec
            delta -= dec
            if delta <= 0:
                break

    return returns


def find_prior_bank_debit_same_amount(conn, *, before_date: str, amount_cents: int, lookback_days: int = 120) -> str | None:
    d = parse_iso(before_date)
    if not d:
        return None
    start = (d - timedelta(days=lookback_days)).isoformat()
    row = conn.execute(
        """
        SELECT id
        FROM fresher_debits__bank_transactions
        WHERE txn_date >= ? AND txn_date < ?
          AND CAST(debit_cents AS INTEGER) = ?
          AND lower(description) LIKE '%e-transfer%'
        ORDER BY txn_date DESC, CAST(id AS INTEGER) DESC
        LIMIT 1
        """,
        (start, before_date, int(amount_cents)),
    ).fetchone()
    if not row:
        return None
    return str(row["id"])


def find_primary_debit_account_for_bank_txn(conn, *, bank_txn_id: str, bank_code: str) -> tuple[str, str] | None:
    """
    For a previously-posted bank txn JE, find the main non-bank debit account.
    Returns (account_code, journal_entry_id).
    """
    row = conn.execute(
        """
        SELECT je.id AS journal_entry_id, jl.account_code AS account_code, jl.debit_cents AS debit_cents
        FROM journal_entries je
        JOIN journal_entry_lines jl ON jl.journal_entry_id = je.id
        WHERE je.source_bank_line_id = ?
          AND jl.account_code <> ?
          AND CAST(jl.debit_cents AS INTEGER) > 0
        ORDER BY CAST(jl.debit_cents AS INTEGER) DESC, jl.account_code
        LIMIT 1
        """,
        (bank_txn_id, bank_code),
    ).fetchone()
    if not row:
        return None
    return (str(row["account_code"]), str(row["journal_entry_id"]))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing bank inflow journals before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    accounts_cfg = cfg.get("accounts", {}) if isinstance(cfg.get("accounts"), dict) else {}
    revenue_cfg = cfg.get("revenue", {}) if isinstance(cfg.get("revenue"), dict) else {}
    tax_cfg = cfg.get("tax", {}) if isinstance(cfg.get("tax"), dict) else {}
    sh_cfg = cfg.get("shareholders", {}) if isinstance(cfg.get("shareholders"), dict) else {}
    bank_debits_cfg = cfg.get("bank_debits", {}) if isinstance(cfg.get("bank_debits"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("bank_inflows") if isinstance(cfg.get("journal_sources"), dict) else {}

    bank_code = str(accounts_cfg.get("bank_account_code") or "1000").strip()
    ap_code = str(accounts_cfg.get("accounts_payable_code") or "2000").strip()

    shopify_sales_code = str(revenue_cfg.get("shopify_sales_code") or "4100").strip()
    shopify_returns_code = str(revenue_cfg.get("shopify_returns_code") or "4900").strip()
    shopify_fees_code = str(revenue_cfg.get("shopify_fees_code") or "6210").strip()
    cash_sales_code = str(revenue_cfg.get("cash_deposit_sales_code") or "4000").strip()
    nayax_sales_code = str(revenue_cfg.get("nayax_sales_code") or "4030").strip()
    income_to_review_code = str(revenue_cfg.get("income_to_review_code") or "4090").strip()

    hst_payable_code = str(tax_cfg.get("hst_payable_code") or "2200").strip()
    hst_itc_code = str(tax_cfg.get("hst_itc_code") or "2210").strip()
    hst_rate = Decimal(str(tax_cfg.get("hst_rate") if "hst_rate" in tax_cfg else "0.15"))

    due_from_shareholder_code = str(sh_cfg.get("due_from_shareholder_code") or "2500").strip()

    cash_on_hand_code = str(bank_debits_cfg.get("cash_on_hand_code") or "1070").strip()
    cash_float_year_end_target_cents = parse_int(bank_debits_cfg.get("cash_float_year_end_target_cents"), default=0)

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "bank_inflows")
    entry_type = str((source_cfg or {}).get("entry_type") or "RECEIPT")

    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "bank_inflow_journal_summary.md"
    out_detail_csv = args.out_dir / "bank_inflow_journal_detail.csv"
    out_cash_float_csv = args.out_dir / "cash_deposit_float_allocation.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )

        items = fetch_credit_bank_items(conn, start_date=start_date, end_date=end_date)

        cash_deposit_events: list[FloatEvent] = []
        for it in items:
            if (it.category or "").strip() != "CASH_DEPOSIT":
                continue
            bank_txn_id = (it.bank_txn_id or "").strip()
            if not bank_txn_id:
                continue
            bank_txn_id_int = parse_int_maybe(bank_txn_id)
            if bank_txn_id_int is None:
                continue
            cents = int(it.amount_cents or 0)
            if cents <= 0:
                continue
            cash_deposit_events.append(
                FloatEvent(
                    txn_date=str(it.txn_date),
                    bank_txn_id=bank_txn_id,
                    bank_txn_id_int=bank_txn_id_int,
                    kind="DEPOSIT",
                    amount_cents=cents,
                )
            )

        float_withdrawals = fetch_change_float_withdrawals(conn, start_date=start_date, end_date=end_date)
        cash_deposit_float_returns: dict[str, int] = {}
        if cash_float_year_end_target_cents > 0 and cash_on_hand_code:
            cash_deposit_float_returns = compute_cash_deposit_float_returns(
                cash_deposit_events,
                float_withdrawals,
                fys=fys,
                year_end_target_cents=cash_float_year_end_target_cents,
            )

        supported_categories = {
            "SHOPIFY_PAYOUT",
            "CASH_DEPOSIT",
            "NAYAX_PAYOUT",
            "VENDOR_CREDIT_MEMO",
            "SHAREHOLDER_LOAN_REPAYMENT",
            "OTHER_INFLOW",
            "ETRANSFER_RECLAIM",
        }

        detail_rows: list[dict[str, str]] = []
        posted = 0
        skipped = 0
        unsupported = 0
        shopify_missing_payout = 0
        cash_float_rows: list[dict[str, str]] = []

        for item in items:
            if item.category not in supported_categories:
                unsupported += 1
                continue

            if not item.bank_txn_id or item.bank_txn_id.strip() == "":
                skipped += 1
                continue

            bank_txn_id = item.bank_txn_id.strip()
            amount_cents = int(item.amount_cents or 0)
            if amount_cents == 0:
                skipped += 1
                continue

            je_id = f"BANK_INFLOW_{item.category}_{bank_txn_id}"
            description = f"{item.category.replace('_', ' ').title()} - bank txn {bank_txn_id}"
            notes = f"bank_item_id={item.bank_item_id}; bank_txn_id={bank_txn_id}; category={item.category}; amount_cents={amount_cents}"

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
                    item.txn_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    item.bank_item_id,
                    bank_txn_id,
                    notes,
                ),
            )

            lines: list[tuple[str, int, int, str]] = []

            # Bank line
            if amount_cents > 0:
                lines.append((bank_code, amount_cents, 0, item.description or "Bank deposit"))
            else:
                lines.append((bank_code, 0, abs(amount_cents), item.description or "Bank withdrawal"))

            if item.category == "SHOPIFY_PAYOUT":
                payout = fetch_shopify_payout_for_bank_txn(conn, bank_txn_id)
                if not payout:
                    shopify_missing_payout += 1
                    # Fallback: treat as net Shopify sales (no fees breakdown).
                    if amount_cents > 0:
                        lines.append((shopify_sales_code, 0, amount_cents, "Shopify payout (unlinked)"))
                    else:
                        lines.append((shopify_sales_code, abs(amount_cents), 0, "Shopify payout (unlinked)"))
                else:
                    charges = int(payout.get("charges_cents") or 0)
                    refunds = int(payout.get("refunds_cents") or 0)
                    fees = int(payout.get("fees_cents") or 0)
                    adjustments = int(payout.get("adjustments_cents") or 0)
                    payout_total = int(payout.get("total_cents") or 0)

                    # Core mapping: bank = charges + refunds + adjustments - fees
                    if charges:
                        lines.append((shopify_sales_code, 0, charges, "Shopify charges (gross sales)"))
                    if refunds:
                        # refunds are stored negative in the payout export (e.g. -16000)
                        if refunds < 0:
                            lines.append((shopify_returns_code, abs(refunds), 0, "Shopify refunds (sales returns)"))
                        else:
                            lines.append((shopify_returns_code, 0, refunds, "Shopify refunds (unexpected sign)"))
                    if fees:
                        lines.append((shopify_fees_code, fees, 0, "Shopify fees"))
                    if adjustments:
                        if adjustments > 0:
                            lines.append((income_to_review_code, 0, adjustments, "Shopify adjustments"))
                        else:
                            lines.append((income_to_review_code, abs(adjustments), 0, "Shopify adjustments"))

                    if payout_total != amount_cents:
                        # Preserve bank as the truth, and carry any mismatch explicitly.
                        diff = amount_cents - payout_total
                        if diff > 0:
                            lines.append((income_to_review_code, 0, diff, "Shopify payout vs bank diff (credit)"))
                        else:
                            lines.append((income_to_review_code, abs(diff), 0, "Shopify payout vs bank diff (debit)"))

                    notes = notes + f"; payout_id={payout.get('id')}; charges={charges}; refunds={refunds}; fees={fees}; payout_total={payout_total}"
                    conn.execute("UPDATE journal_entries SET notes=? WHERE id=?", (notes, je_id))

            elif item.category == "CASH_DEPOSIT":
                if amount_cents > 0:
                    float_return_cents = int(cash_deposit_float_returns.get(bank_txn_id, 0))
                    if float_return_cents < 0:
                        float_return_cents = 0
                    if float_return_cents > amount_cents:
                        float_return_cents = amount_cents
                    cash_sales_cents = amount_cents - float_return_cents

                    if float_return_cents:
                        lines.append((cash_on_hand_code, 0, float_return_cents, "Return of change float (clears cash on hand)"))
                    if cash_sales_cents:
                        lines.append((cash_sales_code, 0, cash_sales_cents, "Cash sales deposit"))

                    notes = notes + f"; cash_float_return_cents={float_return_cents}; cash_sales_cents={cash_sales_cents}; cash_float_year_end_target_cents={cash_float_year_end_target_cents}"
                    conn.execute("UPDATE journal_entries SET notes=? WHERE id=?", (notes, je_id))

                    cash_float_rows.append(
                        {
                            "bank_txn_id": bank_txn_id,
                            "bank_date": item.txn_date,
                            "deposit_cents": str(amount_cents),
                            "deposit": cents_to_dollars(amount_cents),
                            "float_return_cents": str(float_return_cents),
                            "float_return": cents_to_dollars(float_return_cents),
                            "cash_sales_cents": str(cash_sales_cents),
                            "cash_sales": cents_to_dollars(cash_sales_cents),
                            "journal_entry_id": je_id,
                        }
                    )
                else:
                    lines.append((cash_sales_code, abs(amount_cents), 0, "Cash deposit reversal"))

            elif item.category == "NAYAX_PAYOUT":
                if amount_cents > 0:
                    net_cents, tax_cents = split_tax_inclusive(amount_cents, rate=hst_rate)
                    if net_cents:
                        lines.append((nayax_sales_code, 0, net_cents, "Nayax payout (net of HST)"))
                    if tax_cents:
                        lines.append((hst_payable_code, 0, tax_cents, "HST collected on Nayax sales"))
                else:
                    gross = abs(amount_cents)
                    net_cents, tax_cents = split_tax_inclusive(gross, rate=hst_rate)
                    if net_cents:
                        lines.append((nayax_sales_code, net_cents, 0, "Nayax payout reversal (net of HST)"))
                    if tax_cents:
                        lines.append((hst_payable_code, tax_cents, 0, "HST reversal on Nayax sales"))

            elif item.category == "VENDOR_CREDIT_MEMO":
                if amount_cents <= 0:
                    lines.append((income_to_review_code, abs(amount_cents), 0, "Vendor credit memo (unexpected sign)"))
                else:
                    # If linked to a GFS EFT notice, treat the deposit as settling a vendor credit balance
                    # (clears AP). The credit memo itself should be recorded as a negative bill (wave_bills),
                    # which will debit AP and credit expenses in the accrual layer.
                    gfs_notice_id = fetch_gfs_eft_notification_id_for_bank_txn(conn, bank_txn_id)
                    if gfs_notice_id:
                        lines.append((ap_code, 0, amount_cents, "GFS EFT vendor credit settlement (clears AP)"))
                        notes = notes + f"; gfs_eft_notification_id={gfs_notice_id}"
                        conn.execute("UPDATE journal_entries SET notes=? WHERE id=?", (notes, je_id))
                    else:
                        net_cents, tax_cents = split_tax_inclusive(amount_cents, rate=hst_rate)
                        if net_cents:
                            lines.append(("5000", 0, net_cents, "Vendor credit memo (net)"))
                        if tax_cents:
                            lines.append((hst_itc_code, 0, tax_cents, "Vendor credit memo (HST ITC reversal)"))

            elif item.category == "SHAREHOLDER_LOAN_REPAYMENT":
                if amount_cents > 0:
                    lines.append((due_from_shareholder_code, 0, amount_cents, "Shareholder loan repayment"))
                else:
                    lines.append((due_from_shareholder_code, abs(amount_cents), 0, "Shareholder loan reversal"))

            elif item.category == "OTHER_INFLOW":
                if amount_cents > 0:
                    lines.append((income_to_review_code, 0, amount_cents, "Other inflow (review)"))
                else:
                    lines.append((income_to_review_code, abs(amount_cents), 0, "Other inflow reversal (review)"))

            elif item.category == "ETRANSFER_RECLAIM":
                if amount_cents > 0:
                    original_id = find_prior_bank_debit_same_amount(conn, before_date=item.txn_date, amount_cents=amount_cents)
                    if original_id:
                        primary = find_primary_debit_account_for_bank_txn(conn, bank_txn_id=original_id, bank_code=bank_code)
                        if primary:
                            debit_account, orig_je_id = primary
                            lines.append((debit_account, 0, amount_cents, f"Reclaim reversal of bank_txn {original_id} (je {orig_je_id})"))
                            notes = notes + f"; reclaimed_original_bank_txn_id={original_id}; reclaimed_original_je_id={orig_je_id}"
                            conn.execute("UPDATE journal_entries SET notes=? WHERE id=?", (notes, je_id))
                        else:
                            lines.append((income_to_review_code, 0, amount_cents, "E-transfer reclaim (review)"))
                    else:
                        lines.append((income_to_review_code, 0, amount_cents, "E-transfer reclaim (review)"))
                else:
                    # Unexpected: a reclaim as a debit.
                    lines.append((income_to_review_code, abs(amount_cents), 0, "E-transfer reclaim (unexpected debit)"))

            # Insert lines
            debit_total = 0
            credit_total = 0
            for i, (account_code, debit_cents, credit_cents, line_desc) in enumerate(lines, start=1):
                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:{i}",
                        je_id,
                        i,
                        account_code,
                        int(debit_cents or 0),
                        int(credit_cents or 0),
                        line_desc or None,
                    ),
                )
                debit_total += int(debit_cents or 0)
                credit_total += int(credit_cents or 0)

            if debit_total != credit_total:
                # Do not silently post unbalanced entries; delete and surface.
                conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
                conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))
                raise SystemExit(f"Unbalanced bank inflow JE {je_id}: debits={debit_total} credits={credit_total}")

            posted += 1
            detail_rows.append(
                {
                    "bank_txn_id": bank_txn_id,
                    "bank_date": item.txn_date,
                    "category": item.category,
                    "amount_cents": str(amount_cents),
                    "amount": cents_to_dollars(amount_cents),
                    "journal_entry_id": je_id,
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = ["bank_txn_id", "bank_date", "category", "amount_cents", "amount", "journal_entry_id"]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        if cash_float_rows:
            with out_cash_float_csv.open("w", encoding="utf-8", newline="") as f:
                fieldnames = [
                    "bank_txn_id",
                    "bank_date",
                    "deposit_cents",
                    "deposit",
                    "float_return_cents",
                    "float_return",
                    "cash_sales_cents",
                    "cash_sales",
                    "journal_entry_id",
                ]
                w = csv.DictWriter(f, fieldnames=fieldnames)
                w.writeheader()
                w.writerows(cash_float_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Bank inflow journals\n\n")
            f.write(f"- Scope: {start_date} → {end_date}\n")
            f.write(f"- Bank items in scope: {len(items)}\n")
            f.write(f"- Posted: {posted}\n")
            f.write(f"- Unsupported (ignored): {unsupported}\n")
            f.write(f"- Skipped (missing id/zero): {skipped}\n")
            f.write(f"- Shopify payouts missing payout link: {shopify_missing_payout}\n")
            f.write("\n## Categories posted\n\n")
            counts: dict[str, int] = {}
            for r in detail_rows:
                counts[r["category"]] = counts.get(r["category"], 0) + 1
            for cat, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
                f.write(f"- {cat}: {n}\n")

            if cash_float_year_end_target_cents > 0 and cash_deposit_float_returns:
                total_withdrawals = sum(e.amount_cents for e in float_withdrawals)
                total_cleared = sum(int(cash_deposit_float_returns.get(d.bank_txn_id, 0)) for d in cash_deposit_events)
                f.write("\n## Cash deposit float clearing\n\n")
                f.write(f"- Cash on hand code: {cash_on_hand_code}\n")
                f.write(f"- Year-end float target: ${cents_to_dollars(cash_float_year_end_target_cents)}\n")
                f.write(f"- Change-float withdrawals in scope: ${cents_to_dollars(total_withdrawals)}\n")
                f.write(f"- Float returned via cash deposits: ${cents_to_dollars(total_cleared)}\n")
                for fy in sorted(fys, key=lambda fy: fy.end_date):
                    # Ending cash-on-hand from this mechanism (best-effort; excludes any other 1070 flows).
                    bal = 0
                    for ev in sorted(float_withdrawals + cash_deposit_events, key=lambda e: (e.txn_date, e.bank_txn_id_int)):
                        if ev.txn_date > fy.end_date:
                            break
                        if ev.kind == "WITHDRAW":
                            bal += ev.amount_cents
                        else:
                            bal -= int(cash_deposit_float_returns.get(ev.bank_txn_id, 0))
                    f.write(f"- {fy.fy} projected cash-on-hand from float: ${cents_to_dollars(bal)}\n")

        conn.commit()

    finally:
        conn.close()

    print("BANK INFLOW JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
