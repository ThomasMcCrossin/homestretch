# CRA HST Export Cross-check (RT)

DB: `/home/clarencehub/Fresh/Fresher/canteen_reconciliation_v2.db`

CRA HST CSV: `/home/clarencehub/Fresh/CanteenCRAAsOfDec0625/CanteenHST.csv`

## Outputs

- CSV: `/home/clarencehub/Fresh/Fresher/output/audits/cra_hst_export_crosscheck.csv`
- MD: `/home/clarencehub/Fresh/Fresher/output/audits/cra_hst_export_crosscheck.md`

## Summary

- HST payment rows parsed: `6`
- Matched to bank: `5`
- Unmatched HST payments: `1`

## Suggested Bank Verifications

| bank_txn_id | bank_date | bank_amount | HST period_end | HST posted | HST amount | bank_desc |
|---:|---|---:|---|---|---:|---|
| 298 | 2025-06-26 | 2999.56 | March 31, 2025 | 2025-07-02 | 2999.56 | Electronic Funds Transfer DEBIT MEMO GST34-5478726 GPFS-GOVERNMENT PAYMENT |
| 375 | 2025-04-22 | 8231.53 | December 31, 2024 | 2025-04-25 | 8231.53 | Electronic Funds Transfer DEBIT MEMO GST34-1427613 GPFS-GOVERNMENT PAYMENT |
| 798 | 2024-11-29 | 2542.18 | September 30, 2024 | 2024-12-04 | 2542.18 | Electronic Funds Transfer DEBIT MEMO GST-B-8510988 GPFS-GOVERNMENT PAYMENT |
| 834 | 2024-11-13 | 3064.77 | June 30, 2024 | 2024-11-18 | 3064.77 | Electronic Funds Transfer DEBIT MEMO GST-B-2076907 GPFS-GOVERNMENT PAYMENT |
| 835 | 2024-11-13 | 3774.16 | March 31, 2024 | 2024-11-18 | 3774.16 | Electronic Funds Transfer DEBIT MEMO GST-B-2076406 GPFS-GOVERNMENT PAYMENT |

## All HST Payments

| period_end | posted | amount | bank_txn_id | bank_date | bank_desc |
|---|---|---:|---:|---|---|
| Non-reporting period | 2024-10-22 | 2000.00 |  |  |  |
| June 30, 2024 | 2024-11-18 | 3064.77 | 834 | 2024-11-13 | Electronic Funds Transfer DEBIT MEMO GST-B-2076907 GPFS-GOVERNMENT PAYMENT |
| March 31, 2024 | 2024-11-18 | 3774.16 | 835 | 2024-11-13 | Electronic Funds Transfer DEBIT MEMO GST-B-2076406 GPFS-GOVERNMENT PAYMENT |
| September 30, 2024 | 2024-12-04 | 2542.18 | 798 | 2024-11-29 | Electronic Funds Transfer DEBIT MEMO GST-B-8510988 GPFS-GOVERNMENT PAYMENT |
| December 31, 2024 | 2025-04-25 | 8231.53 | 375 | 2025-04-22 | Electronic Funds Transfer DEBIT MEMO GST34-1427613 GPFS-GOVERNMENT PAYMENT |
| March 31, 2025 | 2025-07-02 | 2999.56 | 298 | 2025-06-26 | Electronic Funds Transfer DEBIT MEMO GST34-5478726 GPFS-GOVERNMENT PAYMENT |

## Unmatched HST Payments

| period_end | effective | posted | amount |
|---|---|---|---:|
| Non-reporting period | 2024-10-22 | 2024-10-22 | 2000.00 |

