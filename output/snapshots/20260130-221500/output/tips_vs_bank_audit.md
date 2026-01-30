# Tips vs bank audit

## A) Employee exports (per-employee tip rows)

Scope:
- pay_period_end: 2023-06-01 → 2025-05-31
- bank match window: ±3 days
- bank amount tolerance: ±$0.05

## Summary

- Tip rows: 13
- Expected bank matches (net pay): 11/13
- Net+tips bank matches (diagnostic only): 0/13
- Tips-amount bank matches (diagnostic only): 0/13
- Total tips in these rows: $902.55

How tips are represented in these export rows:

- `TIPS_ADDED_PRE_DEDUCTIONS`: tips were added to taxable pay (gross+vacation+tips) and then deductions were taken.
- `TIPS_EMBEDDED_IN_GROSS`: tips are already embedded in the gross figure; the tips column is informational.

Tip totals by representation:

- TIPS_ADDED_PRE_DEDUCTIONS: $569.15
- TIPS_EMBEDDED_IN_GROSS: $333.40
- AMBIG: $0.00

Interpretation:

- For these per-employee export rows, **tips are already included in the net pay amount**, so the payroll e-transfer is expected to match **net pay**, not **net+tips**.
- FY2025 behavior (tips paid on top of net with no deductions) is audited in section B using curlys-books pay-period totals.

Detail CSV:
- `/home/clarencehub/t2-final-fy2024-fy2025/output/tips_vs_bank_audit.csv`

## B) curlys-books backfill (pay-period totals)

This section checks whether bank payroll e-transfers match `total_net + total_tips`.

Scope:
- pay_period_end: 2023-06-01 → 2025-05-31
- bank match window (centered on pay_date): ±3 days

Summary:

- Pay periods with tips: 16
- Exact bank matches (employee+shareholder payroll): 12/16
- Total tips in these periods: $2053.20

Detail CSV:
- `/home/clarencehub/t2-final-fy2024-fy2025/output/tips_vs_bank_audit_curlysbooks.csv`
