# FY2024 inventory estimate plausibility note (exploration only)

Purpose: document reasonable explanations for why management believes FY2024 ending inventory could be higher than the recorded estimate.
This note does **not** change any filed numbers by itself.

Period: **2023-06-10 to 2024-05-31**
Snapshot source: `output/snapshots/20260202-213000/output/`

## What is currently used in the filing package
- FY2024 closing inventory used: **$2,847** (GIFI 1121; journal `INVENTORY_CLOSE_FY2024`).
- Source estimate sheet total: **$2,847.23** (`/home/clarencehub/curlys-books/t2-filing-fy2024-fy2025/data/Canteen Inventory May 31 2024 - Estimated.csv`).

### Category totals in the FY2024 estimate sheet
| Category | Total |
|---|---|
| Beverages | $312.50 |
| Condiments | $142.18 |
| Disposables | $891.38 |
| Dry Food | $198.45 |
| Frozen | $486.72 |
| Snacks | $816.00 |

## How could the true on-hand inventory be ~$4.5k–$5.5k?
- To reach **$4,500**, the estimate would need to be understated by about **$1,652.77**.
- To reach **$5,500**, the estimate would need to be understated by about **$2,652.77**.

Plausible mechanisms (non-exclusive):
- **Missing stock location**: inventory held in a satellite canteen / offsite storage not fully included in the estimate sheet.
- **Conservative scaling**: the estimate sheet notes indicate it was "scaled down" vs later year; broad conservatism can understate materially.
- **Omitted categories**: entire buckets (e.g., additional disposables, snacks, frozen, beverages) may not have been captured in the estimate.

## A defensible estimation framework (days of COGS on hand)
- FY2024 cost of sales (GIFI 8518): **$108,373** across **357** days.
- Average daily COGS: **$303.57/day**.

If ending inventory is estimated as a certain number of days of typical cost of sales:
| Target ending inventory | Implied days of COGS on hand |
|---|---|
| $4,500 | 14.8 days |
| $5,000 | 16.5 days |
| $5,500 | 18.1 days |

- For a canteen/concession operation, **~15–18 days of stock** is a coherent management-estimate range, especially if ordering is done in bulk and there is some seasonality.

### Impact on FY2024 profit (pure inventory re-estimate)
- If the only change is raising FY2024 closing inventory, **COGS decreases dollar-for-dollar** and **net income increases dollar-for-dollar**.
| Target inv | Delta vs current | Implied COGS | Implied gross profit | Implied GM% |
|---|---|---|---|---|
| $4,500 | +1,653 | $106,720 | $74,515 | 41.12% |
| $5,000 | +2,153 | $106,220 | $75,015 | 41.39% |
| $5,500 | +2,653 | $105,720 | $75,515 | 41.67% |

## FY2025 physical count context (sanity check)
- FY2025 ending inventory (physical count based): **$10,015**; FY2025 COGS: **$110,174**.
- Implied FY2025 days of inventory on hand: **33.2 days**.
- FY2025 was impacted by a known overbuy scenario; therefore a lower FY2024 days-on-hand assumption (e.g., roughly half of FY2025) can still be coherent.

## Disposables policy note (why this matters)
- In this project’s FY2024 estimate sheet, **disposables are treated as inventory** (they map into Inventory - Food).
- If you conceptually treat disposables as "supplies" rather than inventory, that would tend to **reduce** the inventory number, not increase it.
- Therefore, a higher FY2024 inventory belief is most consistent with **missing items/locations** rather than a disposables policy mismatch.

## Evidence pointers
- Estimate sheet: `/home/clarencehub/curlys-books/t2-filing-fy2024-fy2025/data/Canteen Inventory May 31 2024 - Estimated.csv`
- Inventory JE evidence: `output/snapshots/20260202-213000/output/inventory_journal_detail.csv` and `output/snapshots/20260202-213000/output/inventory_journal_detail.csv`
- Override audit (if/when used): `output/snapshots/20260202-213000/output/inventory_override_audit.csv`

## If you choose to restate later (operator-controlled)
- Prefer the repo-local override mechanism (no edits to external CSVs): set `enabled: true` and `closing_inventory_total_cents` in `overrides/inventory_overrides.yml`, then rerun the refresh workflow.
- The inventory journal builder will scale bucket allocations deterministically and emit an audit file showing source totals vs used totals.
- This will cascade deterministically into FY2025 opening inventory (carryforward consistency).
