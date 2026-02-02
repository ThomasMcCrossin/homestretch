# Payroll summary (from exports + CRA + bank)

This report is derived from:
- `payroll_employee_pay_periods` (employee-level 2023 CSVs)
- `payroll_monthly_totals` (monthly working papers 2024/2025)
- `cra_payroll_account_transactions` (CRA payroll account export)
- `fresher_debits__bank_transactions` + `fresher_debits__bank_txn_classifications`

## Fiscal year totals (unified)

| FY | gross_pay | employer_taxes | remittance | net_pay (derived) | tips (if available) | bank payroll paid | delta |
|---|---:|---:|---:|---:|---:|---:|---:|
| FY2024 | $22337.44 | $1463.00 | $4429.51 | $20060.49 | $241.29 | $19384.12 | $-676.37 |
| FY2025 | $51816.73 | $3609.84 | $10998.09 | $45457.45 | $2714.46 | $47513.90 | $3.25 |

Notes:
- `bank payroll paid` is based on bank `txn_date` (cash-basis timing) and only includes bank items categorized as `EMPLOYEE_PAYROLL`/`SHAREHOLDER_PAYROLL`.
- The `delta` is a reconciliation signal only; large differences can be caused by tips paid outside the bank, pay-period timing across month-end/year-end, or incomplete payroll exports.

- Anthony 2024 bank vs export net: bank $14053.79 vs export $13902.56 (delta $151.23). Includes 2024-01-02 payment $177.19 not in export.

## Bank category overrides (applied)

| bank_txn_id | date | amount | evidence_category | override_category | note |
|---|---:|---:|---|---|---|
| 346 | 2025-05-22 | $9000.00 | OWNER_DRAW | DIVIDEND | Shareholder distribution treated as dividend (see SHAREHOLDER_INFORMATION.txt from prior work). |
| 364 | 2025-04-28 | $2900.00 | OWNER_DRAW | DIVIDEND | Shareholder distribution treated as dividend (see SHAREHOLDER_INFORMATION.txt from prior work). |
| 377 | 2025-04-21 | $20000.00 | OWNER_DRAW | DIVIDEND | Shareholder distribution treated as dividend (see SHAREHOLDER_INFORMATION.txt from prior work). |
| 676 | 2025-01-08 | $1000.00 | OWNER_DRAW | SHAREHOLDER_PAYROLL | E-transfer to Thomas that rounds out $4,000 net payroll split across 2024-12-20 ($1,500), 2024-12-31 ($1,500), 2025-01-08 ($1,000). |
| 688 | 2025-01-06 | $5000.00 | OWNER_DRAW | DIVIDEND | Shareholder distribution treated as dividend (see SHAREHOLDER_INFORMATION.txt from prior work). |
| 1085 | 2024-06-17 | $4321.07 | PAYROLL | SHAREHOLDER_PAYROLL | Cheque payroll payment to Thomas (matches Thomas payroll export net pay for pay period ending 2024-06-17). |


## Payroll remittance payable at fiscal year-end (May 31)

### FY2024 (2023-06-01 → 2024-05-31)

- Estimated source deductions payable at 2024-05-31: $0.00

### FY2025 (2024-06-01 → 2025-05-31)

- Estimated source deductions payable at 2025-05-31: $257.17
- CRA corroboration: `Payment May 2025` received `2025-06-04`

## Remittance vs CRA (by payroll month)

This compares `payroll_monthly_totals.remittance_cents` against CRA credits labelled `Payment <Month> <Year>`.

| payroll_month | working_paper_remittance | cra_payments | delta |
|---|---:|---:|---:|
| 2024-02 | $825.95 | $1124.63 | $298.68 |
| 2024-11 | $2703.41 | $2289.89 | $-413.52 |
| 2024-12 | $3210.32 | $2572.87 | $-637.45 |

## CRA ↔ bank matching notes

- CRA credit rows (payments/adjustments): 25
- Matched to bank by (date_received, amount): 22
- Grouped matches found (multiple CRA credits reimbursed as one bank txn):
  - 2024-01-22: 2 CRA credits → $1541.41 matched bank `1365` (PAYROLL_REIMBURSE)

## Unmatched bank remittance-side txns (PAYROLL_REMIT/PAYROLL_REIMBURSE)

These bank transactions are categorized as payroll remittance/reimbursement but did not match any CRA credit by (date_received, amount).
They are usually either vendor PADs misclassified as payroll, or GPFS service charges.

- Pepsico-like PADs: 8 txns, $7250.25
- GPFS service charges: 4 txns, $12.00
- Other: 0 txns, $0.00

## Overlapping months (multiple sources)

These months appear in 2+ sources. By default, the unified ledger prefers `curlysbooks_backfill` when present, then employee exports, then monthly working papers.

| month | curlysbooks gross | employee gross | working gross | curlysbooks vs working net+tips delta |
|---|---:|---:|---:|---:|
| 2024-01 |  | $2088.25 | $2027.48 |  |
| 2024-02 |  | $3467.50 | $3606.20 |  |
| 2024-03 |  | $4897.00 | $5092.88 |  |
| 2024-04 |  | $3179.00 | $3306.16 |  |
| 2024-06 |  | $5384.60 | $0.00 |  |
| 2024-09 |  | $3618.38 | $3763.11 |  |
| 2024-10 |  | $5257.63 | $5467.94 |  |
| 2024-11 |  | $5698.00 | $11310.52 |  |
| 2024-12 |  | $11576.26 | $12638.94 |  |
| 2025-01 | $5264.87 |  | $5062.38 | $0.00 |
| 2025-02 | $4043.91 |  | $3888.38 | $0.00 |
| 2025-03 | $6044.88 |  | $5812.38 | $35.25 |
| 2025-04 | $3831.37 |  | $3684.01 | $0.00 |
| 2025-05 | $1096.83 |  | $1054.64 | $0.00 |

## Outputs

- `/home/clarencehub/t2-final-fy2024-fy2025/output/payroll_monthly_ledger.csv`
- `/home/clarencehub/t2-final-fy2024-fy2025/output/payroll_cra_account_matches.csv`
- `/home/clarencehub/t2-final-fy2024-fy2025/output/payroll_remittance_vs_cra_by_month.csv`
