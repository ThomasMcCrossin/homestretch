# HST reconciliation report (ledger vs CRA)

This report compares the **ledger net GST/HST balance** (GIFI 2680) to a CRA period-derived payable *model* at each fiscal year-end.

Inputs:
- CRA period-derived year-end model: `output/cra_hst_summary.md`
- Ledger: `output/trial_balance_<FY>.csv` and `output/gifi_totals_<FY>.csv`
- Sales tax journals: `output/shopify_sales_tax_journal_detail.csv`
- ITC start-date adjustment: `output/itc_start_date_adjustment_detail.csv`

## Summary

| FY | FY end | Ledger net HST payable | CRA payable est. | Diff (ledger - CRA) |
|---|---|---:|---:|---:|
| FY2024 | 2024-05-31 | 6766.89 | 6214.37 | 552.52 |
| FY2025 | 2025-05-31 | 2663.01 | 3346.30 | -683.29 |

## Notes

- Ledger GST/HST is represented by **GIFI 2680** (net of all accounts mapped to 2680, including 2200/2210).
- Sales tax is credited to 2200 via `scripts/87_build_shopify_sales_tax_journals.py`, using Shopify monthly report taxes, starting at `tax.itc_start_date`.
- Pre-start-date bill tax that was previously treated as ITC is reclassed into expense accounts via `scripts/88_build_itc_start_date_adjustment.py`.
