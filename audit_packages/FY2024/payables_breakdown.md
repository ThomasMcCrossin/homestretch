# Payables breakdown — FY2024

Period: **2023-06-10 to 2024-05-31**
Snapshot source: `output/snapshots/20260202-235500/output/`

## What this is
- This memo explains what is included in Schedule 100 lines **2620 (A/P and accruals)** and **2680 (taxes payable)** in this file.
- In this project, **2680 is used for net HST payable** (HST payable offset by ITCs receivable), not payroll source deductions.

## Breakdown (from trial balance)
| GIFI | Account | Name | Net (cents sign) |
|---|---|---|---|
| 2620 | 2000 | Accounts Payable | $-3,198.24 |
| 2620 | 2700 | Payroll Liabilities - CPP | $255.61 |
| 2620 | 2710 | Payroll Liabilities - EI | $9.25 |
| 2620 | 2720 | Payroll Liabilities - Income Tax | $246.07 |
| 2620 |  | TOTAL (net) | $-2,687.31 |
| 2680 | 2200 | HST Payable | $-9,060.18 |
| 2680 | 2210 | HST ITC Receivable | $2,303.35 |
| 2680 |  | TOTAL (net) | $-6,756.83 |

Evidence:
- `output/snapshots/20260202-235500/output/trial_balance_FY2024.csv`
