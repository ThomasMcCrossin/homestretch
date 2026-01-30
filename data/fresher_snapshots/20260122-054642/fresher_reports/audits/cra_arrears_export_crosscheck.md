# CRA Arrears Export Cross-check

DB: `/home/clarencehub/Fresh/Fresher/canteen_reconciliation_v2.db`

CRA arrears CSV: `/home/clarencehub/Fresh/CanteenCRAAsOfDec0625/CanteenArrearsTransactions.csv`

## Outputs

- CSV: `/home/clarencehub/Fresh/Fresher/output/audits/cra_arrears_export_crosscheck.csv`
- MD: `/home/clarencehub/Fresh/Fresher/output/audits/cra_arrears_export_crosscheck.md`

## Summary

- Arrears rows parsed: `9`
- CR rows matched to bank: `2`
- Unmatched arrears payments: `1`

## Suggested Bank Verifications

| bank_txn_id | bank_date | bank_amount | arrears_received | arrears_amount | arrears_label |
|---:|---|---:|---|---:|---|
| 458 | 2025-03-17 | 27.29 | 2025-03-17 | 27.29 | Arrears payment |

## Arrears Payments (CR)

| received | amount | label | bank_txn_id | bank_date | bank_desc |
|---|---:|---|---:|---|---|
| 2025-03-21 | 0.02 | Administrative Adjustment 2024 |  |  |  |
| 2025-03-17 | 27.29 | Arrears payment | 458 | 2025-03-17 | Electronic Funds Transfer DEBIT MEMO EMPTX-4517739 GPFS-GOVERNMENT PAYMENT |
| 2024-02-26 | 72.02 | Arrears payment | 1277 | 2024-02-26 | Internet Banking E-TRANSFER104897933797 Thomas McCrossin 4506*********695 |

## Unmatched Arrears Payments

- 2025-03-21 0.02 Administrative Adjustment 2024

