#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from _lib import PROJECT_ROOT, fiscal_years_from_manifest, load_manifest


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def to_float(s: str) -> float:
    try:
        return float(str(s).strip())
    except ValueError:
        return 0.0


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def parse_cra_payable_estimates(md_path: Path) -> dict[str, float]:
    if not md_path.exists():
        return {}
    text = md_path.read_text(encoding="utf-8")
    pat = re.compile(r"Net HST payable estimate at (\d{4}-\d{2}-\d{2}): \$(\d+[\d,]*\.\d{2})")
    out: dict[str, float] = {}
    for m in pat.finditer(text):
        out[m.group(1)] = float(m.group(2).replace(",", ""))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_md = args.out_dir / "hst_reconciliation_report.md"
    out_csv = args.out_dir / "hst_reconciliation_report.csv"

    cra_est = parse_cra_payable_estimates(args.out_dir / "cra_hst_summary.md")

    shopify_tax_detail = {}
    shopify_detail_path = args.out_dir / "shopify_sales_tax_journal_detail.csv"
    if shopify_detail_path.exists():
        for r in read_csv_rows(shopify_detail_path):
            shopify_tax_detail[str(r.get("fy") or "").strip()] = r

    itc_adj_detail = {}
    itc_detail_path = args.out_dir / "itc_start_date_adjustment_detail.csv"
    if itc_detail_path.exists():
        for r in read_csv_rows(itc_detail_path):
            itc_adj_detail[str(r.get("fy") or "").strip()] = r

    rows: list[dict[str, str]] = []

    for fy in fys:
        tb_path = args.out_dir / f"trial_balance_{fy.fy}.csv"
        gifi_path = args.out_dir / f"gifi_totals_{fy.fy}.csv"
        if not tb_path.exists() or not gifi_path.exists():
            continue

        tb = {str(r["account_code"]): r for r in read_csv_rows(tb_path)}
        gifi = {str(r["gifi_code"]): r for r in read_csv_rows(gifi_path) if str(r.get("gifi_code") or "").strip()}

        g2680 = gifi.get("2680") or {}
        g2680_balance = str(g2680.get("balance") or "").strip()
        g2680_amount = to_float(str(g2680.get("amount") or "0"))
        ledger_net_payable = g2680_amount if g2680_balance == "CR" else -g2680_amount

        acct2200 = tb.get("2200") or {}
        acct2210 = tb.get("2210") or {}

        cra_payable = cra_est.get(fy.end_date)
        diff = None if cra_payable is None else (ledger_net_payable - cra_payable)

        st = shopify_tax_detail.get(fy.fy) or {}
        itc_adj = itc_adj_detail.get(fy.fy) or {}

        rows.append(
            {
                "fy": fy.fy,
                "fy_end": fy.end_date,
                "ledger_gifi_2680_balance": g2680_balance,
                "ledger_gifi_2680_amount": f"{g2680_amount:.2f}",
                "ledger_net_hst_payable": f"{ledger_net_payable:.2f}",
                "tb_2200_balance": "CR" if to_float(acct2200.get("credit") or "0") > 0 else "DR",
                "tb_2200_amount": acct2200.get("credit") or acct2200.get("debit") or "0.00",
                "tb_2210_balance": "DR" if to_float(acct2210.get("debit") or "0") > 0 else "CR",
                "tb_2210_amount": acct2210.get("debit") or acct2210.get("credit") or "0.00",
                "shopify_tax_journal_total": str(st.get("taxes") or ""),
                "shopify_tax_effective_start": str(st.get("effective_start_date") or ""),
                "itc_pre_start_reclass_total": str(itc_adj.get("tax_reclassed") or ""),
                "cra_payable_estimate": "" if cra_payable is None else f"{cra_payable:.2f}",
                "ledger_minus_cra": "" if diff is None else f"{diff:.2f}",
            }
        )

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        fieldnames = list(rows[0].keys()) if rows else []
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if fieldnames:
            w.writeheader()
            w.writerows(rows)

    with out_md.open("w", encoding="utf-8") as f:
        f.write("# HST reconciliation report (ledger vs CRA)\n\n")
        f.write(
            "This report compares the **ledger net GST/HST balance** (GIFI 2680) to a CRA period-derived payable *model* at each fiscal year-end.\n\n"
        )
        f.write("Inputs:\n")
        f.write("- CRA period-derived year-end model: `output/cra_hst_summary.md`\n")
        f.write("- Ledger: `output/trial_balance_<FY>.csv` and `output/gifi_totals_<FY>.csv`\n")
        f.write("- Sales tax journals: `output/shopify_sales_tax_journal_detail.csv`\n")
        f.write("- ITC start-date adjustment: `output/itc_start_date_adjustment_detail.csv`\n\n")

        if not rows:
            f.write("No rows produced (missing trial balance / GIFI outputs).\n")
            return 0

        f.write("## Summary\n\n")
        f.write("| FY | FY end | Ledger net HST payable | CRA payable est. | Diff (ledger - CRA) |\n")
        f.write("|---|---|---:|---:|---:|\n")
        for r in rows:
            f.write(
                f"| {r['fy']} | {r['fy_end']} | {r['ledger_net_hst_payable']} | {r['cra_payable_estimate'] or ''} | {r['ledger_minus_cra'] or ''} |\n"
            )

        f.write("\n## Notes\n\n")
        f.write(
            "- Ledger GST/HST is represented by **GIFI 2680** (net of all accounts mapped to 2680, including 2200/2210).\n"
        )
        f.write(
            "- Sales tax is credited to 2200 via `scripts/87_build_shopify_sales_tax_journals.py`, using Shopify monthly report taxes, starting at `tax.itc_start_date`.\n"
        )
        f.write(
            "- Pre-start-date bill tax that was previously treated as ITC is reclassed into expense accounts via `scripts/88_build_itc_start_date_adjustment.py`.\n"
        )

    print("HST RECONCILIATION REPORT BUILT")
    print(f"- out_md: {out_md}")
    print(f"- out_csv: {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
