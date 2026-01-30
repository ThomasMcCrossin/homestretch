# CRA Payroll Export Cross-check

DB: `/home/clarencehub/Fresh/Fresher/canteen_reconciliation_v2.db`

CRA payroll CSV: `/home/clarencehub/Fresh/CanteenCRAAsOfDec0625/CanteenPayrollTransactions.csv`

## Outputs

- CSV: `/home/clarencehub/Fresh/Fresher/output/audits/cra_payroll_export_crosscheck.csv`
- MD: `/home/clarencehub/Fresh/Fresher/output/audits/cra_payroll_export_crosscheck.md`

## Summary

- CRA rows parsed: `34`
- CRA rows matched to bank: `22`
- Matched as direct CRA debits: `13`
- Matched as reimbursements: `9`
- Unmatched CRA rows: `12`

## Suggested Bank Verifications

These bank transactions are currently unverified but have an exact CRA payroll export match:

| bank_txn_id | current_category | entity | bank_date | bank_amount | CRA line |
|---:|---|---|---|---:|---|
| 279 | PAYROLL_REMIT | CORP | 2025-08-07 | 42.57 | Payment July 2025 (2025-08-07) |
| 330 | PAYROLL_REMIT | CORP | 2025-06-04 | 257.17 | Payment May 2025 (2025-06-04) |
| 352 | PAYROLL_REMIT | CORP | 2025-05-06 | 929.60 | Payment Apr 2025 (2025-05-06) |
| 387 | PAYROLL_REMIT | CORP | 2025-04-14 | 1240.32 | Payment Mar 2025 (2025-04-14) |
| 458 | PAYROLL_REMIT | CORP | 2025-03-17 | 27.29 | Arrears payment (2025-03-17) |
| 503 | PAYROLL_REMIT | CORP | 2025-03-04 | 589.74 | Payment Feb 2025 (2025-03-04) |
| 504 | PAYROLL_REMIT | CORP | 2025-03-04 | 772.79 | Late year-end payment 2024 (2025-03-04) |
| 568 | PAYROLL_REMIT | CORP | 2025-02-11 | 796.00 | Payment Jan 2025 (2025-02-11) |
| 657 | PAYROLL_REMIT | CORP | 2025-01-15 | 2572.87 | Payment Dec 2024 (2025-01-15) |
| 761 | PAYROLL_REMIT | CORP | 2024-12-05 | 2289.89 | Payment Nov 2024 (2024-12-05) |
| 965 | PAYROLL_REIMBURSE | THOMAS | 2024-10-07 | 416.18 | Payment Sept 2024 (2024-10-07) |
| 1122 | PAYROLL_REIMBURSE | THOMAS | 2024-05-01 | 732.90 | Payment Apr 2024 (2024-05-01) |
| 1178 | PAYROLL_REIMBURSE | THOMAS | 2024-04-02 | 1249.27 | Payment Mar 2024 (2024-04-02) |
| 1365 | PAYROLL_REIMBURSE | DWAYNE | 2024-01-22 | 1541.41 | Payment Sept 2023 late (2024-01-22) |

## Key Matches (Payments)

| CRA received | CRA transactions | CRA amount | bank_txn_id | bank_date | bank_desc |
|---|---|---:|---:|---|---|
| 2024-01-22 | Payment Sept 2023 late | 22.10 | 1365 | 2024-01-22 | Internet Banking E-TRANSFER104858423983 Dwayne Ripley 4506*********695 |
| 2024-01-22 | Payment Dec 2023 late | 1519.31 | 1365 | 2024-01-22 | Internet Banking E-TRANSFER104858423983 Dwayne Ripley 4506*********695 |
| 2024-02-26 | Arrears payment | 72.02 | 1277 | 2024-02-26 | Internet Banking E-TRANSFER104897933797 Thomas McCrossin 4506*********695 |
| 2024-02-26 | Payment Jan 2024 | 292.23 | 1276 | 2024-02-26 | Internet Banking E-TRANSFER104897934333 Thomas McCrossin 4506*********695 |
| 2024-03-06 | Payment Feb 2024 | 566.16 | 1255 | 2024-03-06 | Internet Banking E-TRANSFER104910150312 Thomas McCrossin 4506*********695 |
| 2024-03-11 | Payment Feb 2024 | 558.47 | 1237 | 2024-03-11 | Internet Banking E-TRANSFER104915459750 Thomas McCrossin 4506*********695 |
| 2024-04-02 | Payment Mar 2024 | 1249.27 | 1178 | 2024-04-02 | Internet Banking E-TRANSFER104941665380 Thomas McCrossin 4506*********695 |
| 2024-05-01 | Payment Apr 2024 | 732.90 | 1122 | 2024-05-01 | Internet Banking E-TRANSFER104977727931 Thomas McCrossin 4506*********695 |
| 2024-10-07 | Payment Sept 2024 | 416.18 | 965 | 2024-10-07 | Internet Banking E-TRANSFER105173064541 Thomas McCrossin 4506*********695 |
| 2024-11-05 | Payment Oct 2024 | 830.06 | 862 | 2024-11-05 | Electronic Funds Transfer DEBIT MEMO EMPTX-4836406 GPFS-GOVERNMENT PAYMENT |
| 2024-12-05 | Payment Nov 2024 | 2289.89 | 761 | 2024-12-05 | Electronic Funds Transfer DEBIT MEMO EMPTX-4036939 GPFS-GOVERNMENT PAYMENT |
| 2025-01-15 | Payment Dec 2024 | 2572.87 | 657 | 2025-01-15 | Electronic Funds Transfer DEBIT MEMO EMPTX-5907647 GPFS-GOVERNMENT PAYMENT |
| 2025-02-11 | Payment Jan 2025 | 796.00 | 568 | 2025-02-11 | Electronic Funds Transfer DEBIT MEMO EMPTX- 992230 GPFS-GOVERNMENT PAYMENT |
| 2025-03-04 | Payment Feb 2025 | 589.74 | 503 | 2025-03-04 | Electronic Funds Transfer DEBIT MEMO EMPTX-3387504 GPFS-GOVERNMENT PAYMENT |
| 2025-03-04 | Late year-end payment 2024 | 772.79 | 504 | 2025-03-04 | Electronic Funds Transfer DEBIT MEMO EMPBD-3385149 GPFS-GOVERNMENT PAYMENT |
| 2025-03-17 | Arrears payment | 27.29 | 458 | 2025-03-17 | Electronic Funds Transfer DEBIT MEMO EMPTX-4517739 GPFS-GOVERNMENT PAYMENT |
| 2025-04-14 | Payment Mar 2025 | 1240.32 | 387 | 2025-04-14 | Electronic Funds Transfer DEBIT MEMO EMPTX-3019812 GPFS-GOVERNMENT PAYMENT |
| 2025-05-06 | Payment Apr 2025 | 929.60 | 352 | 2025-05-06 | Electronic Funds Transfer DEBIT MEMO EMPTX-5083390 GPFS-GOVERNMENT PAYMENT |
| 2025-06-04 | Payment May 2025 | 257.17 | 330 | 2025-06-04 | Electronic Funds Transfer DEBIT MEMO EMPTX-3975377 GPFS-GOVERNMENT PAYMENT |
| 2025-08-07 | Payment July 2025 | 42.57 | 279 | 2025-08-07 | Electronic Funds Transfer DEBIT MEMO EMPTX-6704667 GPFS-GOVERNMENT PAYMENT |
| 2025-11-24 | Payment Sept 2025 late | 648.54 | 28 | 2025-11-24 | Electronic Funds Transfer DEBIT MEMO EMPTX-1472904 GPFS-GOVERNMENT PAYMENT |
| 2025-11-24 | Payment Oct 2025 late | 917.68 | 27 | 2025-11-24 | Electronic Funds Transfer DEBIT MEMO EMPTX-1473888 GPFS-GOVERNMENT PAYMENT |

## Unmatched CRA Rows

| CRA posted | CRA received | CR/DR | amount | transactions |
|---|---|---|---:|---|
| 2025-11-28 |  | DR | 29.23 | Assessed late remitting penalty |
| 2025-11-28 |  | DR | 14.85 | Assessed late remitting penalty |
| 2025-09-15 | 2025-09-15 | CR | 116.58 | Payment Aug 2025 |
| 2025-07-15 | 2025-07-15 | CR | 34.02 | Payment June 2025 |
| 2025-03-21 |  | CR | 0.02 | Administrative Adjustment 2024 |
| 2025-03-21 | 2025-03-10 | DR | 0.04 | Interest charged on              27.27Dr |
| 2025-03-10 |  | DR | 27.27 | Assessed late remitting penalty |
| 2025-02-11 |  | DR | 10280.82 | T4 Type Information Return  2024 |
| 2024-04-24 |  | DR | 43.98 | Balance adjustment to 2023 |
| 2024-02-27 | 2024-01-23 | DR | 0.67 | Interest charged on              71.35Dr |
| 2024-01-23 |  | DR | 71.35 | Assessed late remitting penalty |
| 2024-01-22 |  | DR | 1497.43 | T4 Type Information Return  2023 |

