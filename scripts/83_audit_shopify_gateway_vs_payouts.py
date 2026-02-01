#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest


@dataclass(frozen=True)
class GatewayReport:
    id: str
    report_name: str
    report_start: str
    report_end: str


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"

def round_percent(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def select_non_overlapping_reports(reports: list[GatewayReport]) -> list[GatewayReport]:
    """
    The gateway exports include a few overlapping 'wide' reports (ex: 2023-06-01→2024-06-01)
    plus narrower quarterly/monthly ones. For a FY, we want a partition-like set so totals are not
    double-counted.

    Heuristic: remove any report that strictly contains another report.
    """
    kept: list[GatewayReport] = []
    for r in reports:
        is_superset = False
        for other in reports:
            if other is r:
                continue
            if r.report_start <= other.report_start and r.report_end >= other.report_end:
                if r.report_start < other.report_start or r.report_end > other.report_end:
                    is_superset = True
                    break
        if not is_superset:
            kept.append(r)
    kept.sort(key=lambda x: (x.report_start, x.report_end, x.report_name))
    return kept


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
    out_md = args.out_dir / "shopify_gateway_vs_payouts_audit.md"
    out_selected_reports_csv = args.out_dir / "shopify_gateway_reports_selected.csv"
    out_gateway_totals_csv = args.out_dir / "shopify_gateway_totals_by_fy.csv"
    out_sales_channel_totals_csv = args.out_dir / "shopify_sales_channel_totals_by_fy.csv"
    out_internet_percent_csv = args.out_dir / "shopify_internet_sales_percent_by_fy.csv"

    conn = connect_db(args.db)
    try:
        all_reports = [
            GatewayReport(
                id=str(r["id"]),
                report_name=str(r["report_name"] or ""),
                report_start=str(r["report_start"]),
                report_end=str(r["report_end"]),
            )
            for r in conn.execute(
                """
                SELECT id, report_name, report_start, report_end
                FROM fresher_credits__shopify_net_payment_gateway_reports
                ORDER BY report_start, report_end
                """
            ).fetchall()
        ]

        # Pre-aggregate gateway rows by report and gateway.
        gateway_rows = conn.execute(
            """
            SELECT
              g.report_id,
              lower(COALESCE(NULLIF(TRIM(g.payment_gateway), ''), 'unknown')) AS payment_gateway,
              lower(COALESCE(NULLIF(TRIM(g.order_sales_channel), ''), 'unknown')) AS order_sales_channel,
              SUM(CAST(g.transactions_count AS INTEGER)) AS tx_count,
              SUM(CAST(g.gross_payments_cents AS INTEGER)) AS gross_cents,
              SUM(CAST(g.refunded_payments_cents AS INTEGER)) AS refunded_cents,
              SUM(CAST(g.net_payments_cents AS INTEGER)) AS net_cents
            FROM fresher_credits__shopify_net_payment_gateway_rows g
            GROUP BY g.report_id, payment_gateway, order_sales_channel
            """
        ).fetchall()

        by_report_gateway: dict[str, dict[str, dict[str, int]]] = {}
        # by_report_gateway[report_id][gateway] -> sums across channels
        by_report_channel: dict[str, dict[str, dict[str, int]]] = {}
        # by_report_channel[report_id][order_sales_channel] -> sums across gateways
        for r in gateway_rows:
            report_id = str(r["report_id"])
            gateway = str(r["payment_gateway"] or "unknown")
            channel = str(r["order_sales_channel"] or "unknown")
            d = by_report_gateway.setdefault(report_id, {}).setdefault(
                gateway, {"tx_count": 0, "gross_cents": 0, "refunded_cents": 0, "net_cents": 0}
            )
            d["tx_count"] += int(r["tx_count"] or 0)
            d["gross_cents"] += int(r["gross_cents"] or 0)
            d["refunded_cents"] += int(r["refunded_cents"] or 0)
            d["net_cents"] += int(r["net_cents"] or 0)

            c = by_report_channel.setdefault(report_id, {}).setdefault(
                channel, {"tx_count": 0, "gross_cents": 0, "refunded_cents": 0, "net_cents": 0}
            )
            c["tx_count"] += int(r["tx_count"] or 0)
            c["gross_cents"] += int(r["gross_cents"] or 0)
            c["refunded_cents"] += int(r["refunded_cents"] or 0)
            c["net_cents"] += int(r["net_cents"] or 0)

        # Payout consistency checks (does not try to align to gateway timing).
        payout_rows = conn.execute(
            """
            SELECT
              payout_date,
              CAST(charges_cents AS INTEGER) AS charges,
              CAST(refunds_cents AS INTEGER) AS refunds,
              CAST(adjustments_cents AS INTEGER) AS adjustments,
              CAST(fees_cents AS INTEGER) AS fees,
              CAST(total_cents AS INTEGER) AS total
            FROM fresher_credits__shopify_payouts
            """
        ).fetchall()

    finally:
        conn.close()

    # Output CSVs first for easy diffing.
    selected_rows: list[dict[str, str]] = []
    gateway_totals_rows: list[dict[str, str]] = []
    channel_totals_rows: list[dict[str, str]] = []
    internet_percent_rows: list[dict[str, str]] = []

    with out_md.open("w", encoding="utf-8") as f:
        f.write("# Shopify audit: gateway exports vs payout-based GL\n\n")
        f.write("This is a sanity-check report. It does **not** replace payout-linked bank deposits as the GL source-of-truth.\n\n")
        f.write("Key point:\n")
        f.write("- Payouts are **deposit-date** based and represent what hit the bank.\n")
        f.write("- Gateway exports are **transaction-date** based and include payment methods like `cash` and `gift_card` that never appear in payouts.\n")
        f.write("- Therefore, gateway totals will not tie 1:1 to payouts without a timing/coverage model.\n\n")

        for fy in fys:
            in_fy = [r for r in all_reports if r.report_start >= fy.start_date and r.report_end <= fy.end_date]
            selected = select_non_overlapping_reports(in_fy)

            f.write(f"## {fy.fy} ({fy.start_date} → {fy.end_date})\n\n")
            f.write(f"- Gateway reports available (within FY): {len(in_fy)}\n")
            f.write(f"- Gateway reports selected (non-overlapping heuristic): {len(selected)}\n\n")

            if selected:
                f.write("Selected reports:\n\n")
                for r in selected:
                    selected_rows.append(
                        {
                            "fy": fy.fy,
                            "report_id": r.id,
                            "report_start": r.report_start,
                            "report_end": r.report_end,
                            "report_name": r.report_name,
                        }
                    )
                    f.write(f"- {r.report_start} → {r.report_end}: {r.report_name}\n")
                f.write("\n")

            # Aggregate gateway totals across selected reports.
            totals_by_gateway: dict[str, dict[str, int]] = {}
            for r in selected:
                by_gw = by_report_gateway.get(r.id, {})
                for gw, sums in by_gw.items():
                    t = totals_by_gateway.setdefault(gw, {"tx_count": 0, "gross_cents": 0, "refunded_cents": 0, "net_cents": 0})
                    for k in ("tx_count", "gross_cents", "refunded_cents", "net_cents"):
                        t[k] += int(sums.get(k) or 0)

            totals_by_channel: dict[str, dict[str, int]] = {}
            for r in selected:
                by_ch = by_report_channel.get(r.id, {})
                for ch, sums in by_ch.items():
                    t = totals_by_channel.setdefault(ch, {"tx_count": 0, "gross_cents": 0, "refunded_cents": 0, "net_cents": 0})
                    for k in ("tx_count", "gross_cents", "refunded_cents", "net_cents"):
                        t[k] += int(sums.get(k) or 0)

            if totals_by_gateway:
                f.write("Gateway totals (selected reports only):\n\n")
                top = sorted(totals_by_gateway.items(), key=lambda kv: abs(kv[1]["net_cents"]), reverse=True)
                for gw, sums in top:
                    gateway_totals_rows.append(
                        {
                            "fy": fy.fy,
                            "payment_gateway": gw,
                            "tx_count": str(sums["tx_count"]),
                            "gross_payments": cents_to_dollars(sums["gross_cents"]),
                            "refunded_payments": cents_to_dollars(sums["refunded_cents"]),
                            "net_payments": cents_to_dollars(sums["net_cents"]),
                            "gross_cents": str(sums["gross_cents"]),
                            "refunded_cents": str(sums["refunded_cents"]),
                            "net_cents": str(sums["net_cents"]),
                        }
                    )
                    f.write(
                        f"- {gw}: tx={sums['tx_count']} gross=${cents_to_dollars(sums['gross_cents'])} "
                        f"refunded=${cents_to_dollars(sums['refunded_cents'])} net=${cents_to_dollars(sums['net_cents'])}\n"
                    )
                f.write("\n")
            else:
                f.write("Gateway totals: none (no selected reports).\n\n")

            if totals_by_channel:
                f.write("Sales channel totals (selected reports only):\n\n")
                top_ch = sorted(totals_by_channel.items(), key=lambda kv: abs(kv[1]["net_cents"]), reverse=True)
                for ch, sums in top_ch:
                    channel_totals_rows.append(
                        {
                            "fy": fy.fy,
                            "order_sales_channel": ch,
                            "tx_count": str(sums["tx_count"]),
                            "gross_payments": cents_to_dollars(sums["gross_cents"]),
                            "refunded_payments": cents_to_dollars(sums["refunded_cents"]),
                            "net_payments": cents_to_dollars(sums["net_cents"]),
                            "gross_cents": str(sums["gross_cents"]),
                            "refunded_cents": str(sums["refunded_cents"]),
                            "net_cents": str(sums["net_cents"]),
                        }
                    )
                    f.write(
                        f"- {ch}: tx={sums['tx_count']} gross=${cents_to_dollars(sums['gross_cents'])} "
                        f"refunded=${cents_to_dollars(sums['refunded_cents'])} net=${cents_to_dollars(sums['net_cents'])}\n"
                    )
                f.write("\n")

                online_channels = {"online store", "shop"}
                online_net = sum(int(v.get("net_cents") or 0) for ch, v in totals_by_channel.items() if ch in online_channels)
                total_net = sum(int(v.get("net_cents") or 0) for v in totals_by_channel.values())
                percent = Decimal("0")
                if total_net:
                    percent = round_percent(Decimal(online_net) * Decimal(100) / Decimal(total_net))
                internet_percent_rows.append(
                    {
                        "fy": fy.fy,
                        "online_channels": ",".join(sorted(online_channels)),
                        "online_net_payments": cents_to_dollars(online_net),
                        "total_net_payments": cents_to_dollars(total_net),
                        "online_net_cents": str(int(online_net)),
                        "total_net_cents": str(int(total_net)),
                        "percent_gross_revenue_from_internet": str(percent),
                    }
                )
                f.write("Internet revenue % (from gateway exports):\n\n")
                f.write(f"- Online channels (treated as internet): {', '.join(sorted(online_channels))}\n")
                f.write(f"- Online net payments: ${cents_to_dollars(online_net)}\n")
                f.write(f"- Total net payments (all channels): ${cents_to_dollars(total_net)}\n")
                f.write(f"- % gross revenue from internet (Online Store + Shop): {percent}\n\n")

            # Payout totals in FY (deposit-date).
            charges = refunds = adjustments = fees = total = 0
            formula_total = 0
            formula_diff = 0
            payout_count = 0
            for p in payout_rows:
                payout_date = str(p["payout_date"] or "")
                if not (fy.start_date <= payout_date <= fy.end_date):
                    continue
                payout_count += 1
                c = int(p["charges"] or 0)
                r = int(p["refunds"] or 0)
                a = int(p["adjustments"] or 0)
                fe = int(p["fees"] or 0)
                t = int(p["total"] or 0)
                charges += c
                refunds += r
                adjustments += a
                fees += fe
                total += t
                ft = c + r + a - fe
                formula_total += ft
                formula_diff += (t - ft)

            f.write("Payout totals in FY (payout_date, deposit-date):\n\n")
            f.write(f"- Payout count: {payout_count}\n")
            f.write(f"- charges_cents: ${cents_to_dollars(charges)}\n")
            f.write(f"- refunds_cents: ${cents_to_dollars(refunds)}\n")
            f.write(f"- adjustments_cents: ${cents_to_dollars(adjustments)}\n")
            f.write(f"- fees_cents: ${cents_to_dollars(fees)}\n")
            f.write(f"- total_cents: ${cents_to_dollars(total)}\n")
            f.write(f"- Check: (charges + refunds + adjustments - fees) = ${cents_to_dollars(formula_total)}; diff vs total = ${cents_to_dollars(formula_diff)}\n\n")

            gw_shopify_net = totals_by_gateway.get("shopify_payments", {}).get("net_cents", 0)
            gw_cash_net = totals_by_gateway.get("cash", {}).get("net_cents", 0)
            if gw_shopify_net:
                payout_net_sales = charges + refunds + adjustments
                f.write("Comparison (sanity check only):\n\n")
                f.write(f"- Gateway `shopify_payments` net (transaction-date): ${cents_to_dollars(int(gw_shopify_net))}\n")
                f.write(f"- Payout (charges+refunds+adjustments) (deposit-date): ${cents_to_dollars(payout_net_sales)}\n")
                f.write(f"- Delta: ${cents_to_dollars(int(gw_shopify_net) - payout_net_sales)}\n\n")
            if gw_cash_net:
                f.write("Reminder:\n\n")
                f.write(f"- Gateway `cash` net (${cents_to_dollars(int(gw_cash_net))}) is POS cash and should be captured via cash deposits / cash-on-hand, not Shopify payouts.\n\n")

        f.write("## Interpretation notes\n\n")
        f.write("- Using payouts for GL does **not** double-count fees: payouts are net-to-bank, and we book fees separately to reconcile to gross sales.\n")
        f.write("- Gateway exports are useful to sanity-check the *shape* of sales by payment method, and to catch missing cash deposits, but they should not replace payout-linked bank deposits for GL.\n")

    with out_selected_reports_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = ["fy", "report_id", "report_start", "report_end", "report_name"]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(selected_rows)

    with out_gateway_totals_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "fy",
            "payment_gateway",
            "tx_count",
            "gross_payments",
            "refunded_payments",
            "net_payments",
            "gross_cents",
            "refunded_cents",
            "net_cents",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(gateway_totals_rows)

    with out_sales_channel_totals_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "fy",
            "order_sales_channel",
            "tx_count",
            "gross_payments",
            "refunded_payments",
            "net_payments",
            "gross_cents",
            "refunded_cents",
            "net_cents",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(channel_totals_rows)

    with out_internet_percent_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "fy",
            "online_channels",
            "online_net_payments",
            "total_net_payments",
            "online_net_cents",
            "total_net_cents",
            "percent_gross_revenue_from_internet",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(internet_percent_rows)

    print("SHOPIFY GATEWAY VS PAYOUTS AUDIT BUILT")
    print(f"- out: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
