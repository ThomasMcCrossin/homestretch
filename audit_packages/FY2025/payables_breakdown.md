# Payables breakdown — FY2025

Period: **2024-06-01 to 2025-05-31**
Snapshot source: `output/snapshots/20260201-183000/output/`

## What this is
- This memo explains what is included in Schedule 100 lines **2620 (A/P and accruals)** and **2680 (taxes payable)** in this file.
- In this project, **2680 is used for net HST payable** (HST payable offset by ITCs receivable), not payroll source deductions.

## Breakdown (from trial balance)
| GIFI | Account | Name | Net (cents sign) |
|---|---|---|---|
| 2620 | 2000 | Accounts Payable | $-7,135.87 |
| 2620 | 2250 | CRA Charges Payable (Interest/Penalties) | $-219.10 |
| 2620 | 2700 | Payroll Liabilities - CPP | $202.07 |
| 2620 | 2710 | Payroll Liabilities - EI | $20.86 |
| 2620 | 2720 | Payroll Liabilities - Income Tax | $-272.64 |
| 2620 |  | TOTAL (net) | $-7,404.68 |
| 2680 | 2200 | HST Payable | $-13,913.82 |
| 2680 | 2210 | HST ITC Receivable | $11,260.87 |
| 2680 |  | TOTAL (net) | $-2,652.95 |

Evidence:
- `output/snapshots/20260201-183000/output/trial_balance_FY2025.csv`
