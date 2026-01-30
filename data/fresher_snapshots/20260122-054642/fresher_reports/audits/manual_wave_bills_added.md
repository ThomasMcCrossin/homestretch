# Manual Wave Bill Additions (Reconciliation)

DB: `/home/clarencehub/Fresh/Fresher/canteen_reconciliation_v2.db`

Definition used here: `wave_bills.source_row IS NULL`.

## Summary

- Manual bills count: **59**
- CSV: `/home/clarencehub/Fresh/Fresher/output/audits/manual_wave_bills_added.csv`

### Totals by Fiscal Year (manual bills)

| FY | Count | Total ($) | Tax ($) | Net ($) |
|---:|------:|----------:|--------:|--------:|
| FY2024 | 29 | 10,149.08 | 46.24 | 10,102.84 |
| FY2025 | 27 | 10,745.33 | 186.92 | 10,558.41 |
| OUTSIDE_SCOPE | 3 | 4,733.91 | 0.00 | 4,733.91 |

### Breakdown by vendor_category (manual bills)

| vendor_category | Count | Total ($) | Tax ($) |
|---|---:|---:|---:|
| OTHER | 16 | 2,782.58 | 30.00 |
| GFS | 11 | 4,227.70 | 0.00 |
| BANK_FEE | 9 | 136.94 | 0.00 |
| PEPSI | 9 | 12,836.90 | 0.00 |
| CAPITAL | 4 | 2,601.64 | 203.16 |
| DOLLARAMA | 4 | 794.56 | 0.00 |
| WALMART | 3 | 214.84 | 0.00 |
| COSTCO | 1 | 150.72 | 0.00 |
| INSURANCE | 1 | 1,851.00 | 0.00 |
| PHARMASAVE | 1 | 31.44 | 0.00 |

## Implications / Caveats

- These bills do not exist in the raw Wave bill ledger CSV; they were introduced to explain bank/CC activity (placeholders, fees, credit memos, cash-paid items).
- Most manual bills have tax = $0.00. This avoids inflating ITCs, but can understate ITCs where a real receipt had HST.
- Manual bills dated OUTSIDE_SCOPE will be excluded from FY2024/FY2025 outputs unless re-dated.
- Negative totals (credit memos) reduce purchases/expenses and should be kept linked to the correct vendor period.

## Manual bills with non-zero tax

| wave_bill_id | invoice_date | vendor_category | vendor_raw | total ($) | tax ($) | invoice_number |
|---:|---:|---|---|---:|---:|---|
| 753 | 2024-02-26 | CAPITAL | Capital Foods - Bill 2548372 | 894.36 | 46.24 | 2548372 |
| 741 | 2024-10-24 | CAPITAL | Capital Foods - Bill 2590104 | 935.34 | 62.51 | 2590104 |
| 734 | 2024-12-13 | CAPITAL | Capital Foods - Bill 2598264 | 820.06 | 94.41 | 2598264 |
| 742 | 2024-12-20 | OTHER | Bowling Alley - Christmas Party | 230.00 | 30.00 | XMAS-PARTY-2024 |

## Manual bills outside FY2024/FY2025 scope

| wave_bill_id | invoice_date | vendor_category | vendor_raw | total ($) | invoice_number |
|---:|---:|---|---|---:|---|
| 764 | 2025-09-30 | PEPSI | Pepsico - Bill (AUTO PAD BT166) | 1617.14 | PEPSI-PAD-BT166 |
| 765 | 2025-10-31 | PEPSI | Pepsico - Bill (AUTO PAD BT51) | 2836.77 | PEPSI-PAD-BT51 |
| 724 | 2025-12-10 | GFS | GFS Cash - Cheese Curds | 280.00 | STUB-GFS-CASH-001 |

