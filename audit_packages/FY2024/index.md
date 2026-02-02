# Shareholder audit package — FY2024
Entity: **14587430 Canada Inc. (Curly's Canteen)**
BN: **748003142RC0001**
Period: **2023-06-10 to 2024-05-31**
Snapshot source: `output/snapshots/20260201-183000/output/`
Packet generated at: `2026-02-01T18:35:36Z`
This folder is **working-paper support**. It is not necessarily entered into UFile unless a screen explicitly asks.
## Year-end highlights
| Item | Amount (dollars) |
|---|---|
| Schedule 100 due from shareholder (GIFI 1301) | 0 |
| Schedule 100 due to shareholders (GIFI 2781) | 3,578 |
| Dividends declared (retained earnings rollforward 3700) | 0 |

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
| 2400 | Due to Shareholder - Thomas | $-2,669.99 |
| 2410 | Due to Shareholder - Dwayne | $-908.16 |

## Mileage / fuel reimbursement support
Evidence:
- `mileage_fuel_support.csv`

FY-scoped overlays applied (defensive disclosure for working papers only):

| Shareholder | Fuel adjustment (cents) | Notes |
|---|---|---|
| Thomas | 6096 |  |

## Payroll-related transactions involving Thomas McCrossin (defensive)
Evidence:
- `payroll_thomas_support.csv`

Note: These are payroll-related reimbursements / funding transactions involving Thomas (e.g., payroll remittance payments/reimbursements). This does **not** necessarily mean wages were paid to Thomas as an employee.

## Related review memos (same FY)
- `inventory_margin_memo.html` (inventory/margin support)
- `inventory_estimate_plausibility_note.html` (FY2024 only; explores why inventory may feel higher)
- `fixed_asset_cca_continuity.html` (book vs tax CCA continuity)
- `payables_breakdown.html` (A/P + HST/payroll breakdown)
