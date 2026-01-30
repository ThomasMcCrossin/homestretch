#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, get_source, load_manifest


@dataclass(frozen=True)
class PeriodSummary:
    period_end: str
    net_tax_cents: int
    net_tax_date_posted: str | None
    payment_cents: int
    payment_effective_date: str | None
    payment_date_posted: str | None
    failure_to_file_penalty_cents: int
    arrears_interest_cents: int
    administrative_adjustment_cents: int
    other_cents: int


def cents_to_dollars(cents: int) -> str:
    return f"{Decimal(cents) / Decimal(100):.2f}"


def signed_cents(amount_cents: int, cr_dr: str | None) -> int:
    return -amount_cents if (cr_dr or "").strip().upper() == "CR" else amount_cents


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def build_period_summaries(conn: sqlite3.Connection) -> list[PeriodSummary]:
    rows = conn.execute(
        """
        SELECT
          period_end,
          effective_date,
          date_posted,
          transaction_label,
          amount_cents,
          cr_dr
        FROM cra_hst_account_transactions
        WHERE period_end IS NOT NULL
        ORDER BY period_end, COALESCE(date_posted, ''), COALESCE(effective_date, ''), source_row
        """
    ).fetchall()

    # Group by period_end.
    grouped: dict[str, list[sqlite3.Row]] = {}
    for r in rows:
        pe = str(r["period_end"])
        grouped.setdefault(pe, []).append(r)

    out: list[PeriodSummary] = []
    for period_end, rs in grouped.items():
        # Net tax: choose the latest debit-side net tax row (ignore explicit credit reversals).
        net_candidates = [
            r
            for r in rs
            if (r["transaction_label"] or "").strip() == "Net Tax"
            and int(r["amount_cents"] or 0) > 0
            and (r["cr_dr"] or "").strip().upper() != "CR"
        ]
        net_tax_cents = 0
        net_tax_date_posted: str | None = None
        if net_candidates:
            net_candidates.sort(
                key=lambda r: (
                    str(r["date_posted"] or ""),
                    str(r["effective_date"] or ""),
                )
            )
            chosen = net_candidates[-1]
            net_tax_cents = int(chosen["amount_cents"] or 0)
            net_tax_date_posted = str(chosen["date_posted"] or "") or None

        payment_rows = [r for r in rs if (r["transaction_label"] or "").strip() == "Payment" and int(r["amount_cents"] or 0)]
        payment_cents = sum(int(r["amount_cents"] or 0) for r in payment_rows)
        payment_effective_date = None
        payment_date_posted = None
        if payment_rows:
            # Usually one payment; pick the earliest effective date for readability.
            payment_rows.sort(key=lambda r: (str(r["effective_date"] or ""), str(r["date_posted"] or "")))
            payment_effective_date = str(payment_rows[0]["effective_date"] or "") or None
            payment_date_posted = str(payment_rows[0]["date_posted"] or "") or None

        penalty_cents = 0
        interest_cents = 0
        admin_cents = 0
        other_cents = 0

        for r in rs:
            label = (r["transaction_label"] or "").strip()
            amt = int(r["amount_cents"] or 0)
            if amt == 0:
                continue
            s = signed_cents(amt, r["cr_dr"])
            if label == "Failure to file penalty":
                penalty_cents += s
            elif label == "Arrears Interest":
                interest_cents += s
            elif label == "Administrative adjustment":
                admin_cents += s
            elif label in ("Net Tax", "Payment", "Payment Applied", "Previous Balance", "Interim Balance", "Balance"):
                continue
            else:
                other_cents += s

        out.append(
            PeriodSummary(
                period_end=period_end,
                net_tax_cents=net_tax_cents,
                net_tax_date_posted=net_tax_date_posted,
                payment_cents=payment_cents,
                payment_effective_date=payment_effective_date,
                payment_date_posted=payment_date_posted,
                failure_to_file_penalty_cents=penalty_cents,
                arrears_interest_cents=interest_cents,
                administrative_adjustment_cents=admin_cents,
                other_cents=other_cents,
            )
        )

    out.sort(key=lambda p: p.period_end)
    return out


def match_bank_txn_id_for_payment(conn: sqlite3.Connection, *, payment_date: str, payment_cents: int) -> str | None:
    if not payment_date or not payment_cents:
        return None

    rows = conn.execute(
        """
        SELECT t.id
        FROM fresher_debits__bank_transactions t
        JOIN fresher_debits__bank_txn_classifications c ON c.bank_txn_id = t.id
        WHERE t.txn_date = ?
          AND CAST(t.debit_cents AS INTEGER) = ?
          AND c.txn_category = 'GST_HST_REMIT'
        ORDER BY t.id
        """,
        (payment_date, payment_cents),
    ).fetchall()
    if not rows:
        return None
    return str(rows[0][0])


def parse_iso_month(s: str) -> date:
    # Shopify export uses YYYY-MM-01 strings.
    return date.fromisoformat(str(s).strip())


def load_shopify_monthly_taxes(manifest: dict, *, source_key: str) -> dict[date, int]:
    """
    Load Shopify 'Sales by month Bulk' taxes by month (YYYY-MM-01 -> cents).

    Used only as a *weighting heuristic* for prorating CRA quarter net tax to a fiscal year-end
    that lands mid-quarter (May 31). This addresses the practical reality that June can be a
    dead month (very low activity), so a fixed 2/3 proration can be misleading.
    """
    src = get_source(manifest, source_key)
    path = Path(str(src.get("path") or "")).expanduser()
    if not path.exists():
        return {}

    out: dict[date, int] = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            month_raw = r.get("Month") or ""
            if not month_raw:
                continue
            try:
                month = parse_iso_month(month_raw)
            except Exception:
                continue
            taxes = str(r.get("Taxes") or "").strip()
            s = taxes.replace("$", "").replace(",", "").strip()
            if s in ("", "-"):
                cents = 0
            else:
                try:
                    cents = int((Decimal(s) * Decimal(100)).quantize(Decimal("1")))
                except Exception:
                    cents = 0
            out[month] = out.get(month, 0) + cents
    return out


def prorate_apr_may_portion(net_tax_cents: int, *, year: int, shopify_taxes_by_month: dict[date, int]) -> int:
    """
    Corporate FY ends May 31; CRA quarter ending June 30 spans Apr+May+Jun.

    Default (old): naive 2/3 proration.
    New: Shopify-tax-weighted proration:
      Apr-May share = (taxes_Apr + taxes_May) / (taxes_Apr + taxes_May + taxes_Jun)

    Falls back to 2/3 if weights are unavailable.
    """
    if net_tax_cents == 0:
        return 0
    apr = int(shopify_taxes_by_month.get(date(year, 4, 1), 0) or 0)
    may = int(shopify_taxes_by_month.get(date(year, 5, 1), 0) or 0)
    jun = int(shopify_taxes_by_month.get(date(year, 6, 1), 0) or 0)
    denom = apr + may + jun
    if denom <= 0:
        return int((Decimal(net_tax_cents) * Decimal(2) / Decimal(3)).quantize(Decimal("1")))
    num = apr + may
    return int((Decimal(net_tax_cents) * Decimal(num) / Decimal(denom)).quantize(Decimal("1")))


def hst_payable_at_fy_end(
    fy: FiscalYear,
    *,
    periods: list[PeriodSummary],
    shopify_taxes_by_month: dict[date, int],
) -> tuple[int, list[tuple[str, int]]]:
    end = date.fromisoformat(fy.end_date)
    components: list[tuple[str, int]] = []
    total = 0

    # 1) Full-period net tax for periods ended on/before FY end that are not yet paid by FY end.
    for p in periods:
        pe = parse_iso(p.period_end)
        if not pe or pe > end:
            continue
        paid = False
        if p.payment_effective_date:
            pd = parse_iso(p.payment_effective_date)
            paid = bool(pd and pd <= end)
        if paid:
            continue
        if p.net_tax_cents:
            components.append((p.period_end, p.net_tax_cents))
            total += p.net_tax_cents

    # 2) Partial quarter (Apr-May portion) for the CRA period ending June 30 of the same calendar year.
    june_30 = date(end.year, 6, 30)
    june_period = next((p for p in periods if parse_iso(p.period_end) == june_30), None)
    if june_period and june_period.net_tax_cents:
        apr_may_cents = prorate_apr_may_portion(
            june_period.net_tax_cents, year=end.year, shopify_taxes_by_month=shopify_taxes_by_month
        )
        components.append((f"{june_period.period_end} (Apr-May portion)", apr_may_cents))
        total += apr_may_cents

    components.sort(key=lambda t: t[0])
    return total, components


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_md = args.out_dir / "cra_hst_summary.md"
    out_csv = args.out_dir / "cra_hst_period_summary.csv"

    conn = connect_db(args.db)
    try:
        periods = build_period_summaries(conn)
        shopify_taxes_by_month = load_shopify_monthly_taxes(manifest, source_key="shopify_sales_by_month_bulk_csv")

        # CSV output
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "period_end",
                    "net_tax_cents",
                    "net_tax_date_posted",
                    "payment_effective_date",
                    "payment_date_posted",
                    "payment_cents",
                    "bank_txn_id",
                    "failure_to_file_penalty_cents",
                    "arrears_interest_cents",
                    "administrative_adjustment_cents",
                    "other_cents",
                ]
            )
            for p in periods:
                bank_txn_id = None
                if p.payment_effective_date and p.payment_cents:
                    bank_txn_id = match_bank_txn_id_for_payment(
                        conn, payment_date=p.payment_effective_date, payment_cents=p.payment_cents
                    )
                w.writerow(
                    [
                        p.period_end,
                        p.net_tax_cents,
                        p.net_tax_date_posted or "",
                        p.payment_effective_date or "",
                        p.payment_date_posted or "",
                        p.payment_cents,
                        bank_txn_id or "",
                        p.failure_to_file_penalty_cents,
                        p.arrears_interest_cents,
                        p.administrative_adjustment_cents,
                        p.other_cents,
                    ]
                )

        # MD output
        lines: list[str] = []
        lines.append("# CRA HST summary (from CRA account export)")
        lines.append("")
        lines.append("This report is derived from the imported CRA export tables in `db/t2_final.db`.")
        lines.append("It is intended to support deterministic year-end HST payable modeling and remittance splitting (net tax vs interest/penalties).")
        lines.append("")
        lines.append("## Periods (Net Tax vs Payments)")
        lines.append("")
        lines.append("| period_end | net_tax | payment (bank_date) | bank_txn_id | delta (payment - net_tax) |")
        lines.append("|---|---:|---:|---:|---:|")
        for p in periods:
            delta = (p.payment_cents or 0) - (p.net_tax_cents or 0)
            bank_txn_id = ""
            if p.payment_effective_date and p.payment_cents:
                bank_txn_id = match_bank_txn_id_for_payment(
                    conn, payment_date=p.payment_effective_date, payment_cents=p.payment_cents
                ) or ""
            pay_disp = ""
            if p.payment_cents:
                pay_disp = f"${cents_to_dollars(p.payment_cents)} ({p.payment_effective_date or '?'})"
            lines.append(
                f"| {p.period_end} | ${cents_to_dollars(p.net_tax_cents)} | {pay_disp} | {bank_txn_id} | ${cents_to_dollars(delta)} |"
            )
        lines.append("")

        lines.append("## HST payable at corporate year-end (May 31)")
        lines.append("")
        for fy in fys:
            total, components = hst_payable_at_fy_end(fy, periods=periods, shopify_taxes_by_month=shopify_taxes_by_month)
            lines.append(f"### {fy.fy} ({fy.start_date} → {fy.end_date})")
            lines.append("")
            lines.append(f"- Net HST payable estimate at {fy.end_date}: ${cents_to_dollars(total)}")
            if components:
                lines.append("- Components:")
                for label, cents in components:
                    lines.append(f"  - {label}: ${cents_to_dollars(cents)}")
            lines.append("")

        lines.append("## Notes")
        lines.append("")
        lines.append("- For CRA quarters ending June 30, the Apr-May portion is prorated using Shopify monthly tax as a weighting heuristic.")
        lines.append("  - Rationale: June can be operational 'dead time', so a fixed 2/3 split can materially misstate the May 31 accrual.")
        lines.append("- If Shopify weights are missing, the fallback is a simple 2/3 proration.")
        lines.append("- FY2025 payable includes the Jan-Mar 2025 net tax if it was unpaid at May 31, 2025 (payment occurred after year-end).")
        lines.append("")
        lines.append("## Outputs")
        lines.append("")
        lines.append(f"- `{out_csv}`")
        lines.append("")

        out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    finally:
        conn.close()

    print("CRA HST SUMMARY BUILT")
    print(f"- out_md: {out_md}")
    print(f"- out_csv: {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
