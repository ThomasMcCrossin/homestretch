# Shareholder audit package — FY2025
Entity: **14587430 Canada Inc. (Curly's Canteen)**
BN: **748003142RC0001**
Period: **2024-06-01 to 2025-05-31**
Snapshot source: `output/snapshots/20260202-213000/output/`
Packet generated at: `2026-02-02T21:07:00Z`
This folder is **working-paper support**. It is not necessarily entered into UFile unless a screen explicitly asks.
## Year-end highlights
| Item | Amount (dollars) |
|---|---|
| Schedule 100 due from shareholder (GIFI 1301) | 2,041 |
| Schedule 100 due to shareholders (GIFI 2781) | 5,011 |
| Dividends declared (retained earnings rollforward 3700) | 36,900 |

## Dividends
Tie-out:
- Trial balance: account `3400` (dividends declared)
- Retained earnings rollforward: `GIFI 3700`
- UFile screens:
  - Retained earnings rollforward: enter `3700`
  - Dividends paid: enter taxable dividends paid (eligible = 0 unless you have eligible dividends)

Evidence:
- `dividends_support.csv`

## Loans / due-to / due-from (shareholder continuity)
This captures dated loan events (if any), the FY mileage/fuel net position, and year-end balances.

Evidence:
- `shareholder_continuity.csv`

Year-end TB balances (for reference):
| Account | Name | Net |
|---|---|---|
| 2400 | Due to Shareholder - Thomas | $-3,403.90 |
| 2410 | Due to Shareholder - Dwayne | $-1,606.68 |
| 2500 | Due from Shareholder | $2,041.36 |

## Mileage / fuel reimbursement support
Evidence:
- `mileage_fuel_support.csv`

## Payroll-related transactions involving Thomas McCrossin (defensive)
Evidence:
- `payroll_thomas_support.csv`

Note: These are payroll-related reimbursements / funding transactions involving Thomas (e.g., payroll remittance payments/reimbursements). This does **not** necessarily mean wages were paid to Thomas as an employee.

## Related review memos (same FY)
- `inventory_margin_memo.html` (inventory/margin support)
- `fixed_asset_cca_continuity.html` (book vs tax CCA continuity)
- `payables_breakdown.html` (A/P + HST/payroll breakdown)
