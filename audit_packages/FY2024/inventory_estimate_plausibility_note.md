# FY2024 inventory estimate plausibility note (exploration only)

Purpose: document reasonable explanations for why management believes FY2024 ending inventory could be higher than the recorded estimate.
This note does **not** change any filed numbers by itself.

Period: **2023-06-10 to 2024-05-31**
Snapshot source: `output/snapshots/20260201-183000/output/`

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

## Disposables policy note (why this matters)
- In this project’s FY2024 estimate sheet, **disposables are treated as inventory** (they map into Inventory - Food).
- If you conceptually treat disposables as "supplies" rather than inventory, that would tend to **reduce** the inventory number, not increase it.
- Therefore, a higher FY2024 inventory belief is most consistent with **missing items/locations** rather than a disposables policy mismatch.

## Evidence pointers
- Estimate sheet: `/home/clarencehub/curlys-books/t2-filing-fy2024-fy2025/data/Canteen Inventory May 31 2024 - Estimated.csv`
- Inventory JE evidence: `output/snapshots/20260201-183000/output/inventory_journal_detail.csv` and `output/snapshots/20260201-183000/output/inventory_journal_detail.csv`

## If you choose to restate later (not tonight)
- Update the FY2024 estimate sheet total and category subtotals to reflect the missing stock, update the manifest hash, and regenerate outputs.
- This will cascade deterministically into FY2025 opening inventory (carryforward consistency).
