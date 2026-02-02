# FY2024 ending inventory estimate note (FY2025-item-based)

Purpose: document how FY2024 ending inventory was estimated for this filing.

Period: **2023-06-10 to 2024-05-31**
Snapshot source: `output/snapshots/20260202-231500/output/`

## What this file does (in plain English)
- FY2024 did not have a physical inventory count.
- Management estimated FY2024 ending inventory using the FY2025 physical-count item list as a basis, scaled down to a target band.
- Quantities were rounded to whole numbers for most items (decimals only where the FY2025 source uses decimals).

## What is used in the filing package
- FY2024 closing inventory used: **$5,129** (GIFI 1121; journal `INVENTORY_CLOSE_FY2024`).
- FY2024 estimate CSV total: **$5,129.04** (`/home/clarencehub/t2-final-fy2024-fy2025/data/inventory/Canteen Inventory May 31 2024 - Estimate from FY2025 Items.csv`).

### Category totals in the FY2024 estimate sheet
| Category | Total |
|---|---|
| Beverages | $475.38 |
| Condiments | $329.26 |
| Disposables | $1,030.83 |
| Dry Food | $367.24 |
| Frozen | $655.27 |
| Snacks | $2,271.06 |

## Estimation framework (days of COGS on hand)
- FY2024 cost of sales (GIFI 8518): **$106,091** across **357** days.
- Average daily COGS: **$297.17/day**.

For context, the implied days-on-hand at a few inventory totals is:
| Target ending inventory | Implied days of COGS on hand |
|---|---|
| $4,500 | 15.1 days |
| $5,000 | 16.8 days |
| $5,137 | 17.3 days |
| $5,500 | 18.5 days |

- The selected FY2024 estimate is intended to be in a coherent management-estimate range (roughly ~15–18 days of stock).

### Impact on FY2024 profit (pure inventory re-estimate)
- If the only change is raising FY2024 closing inventory, **COGS decreases dollar-for-dollar** and **net income increases dollar-for-dollar**.
| Target inv | Delta vs current | Implied COGS | Implied gross profit | Implied GM% |
|---|---|---|---|---|
| $4,500 | -629 | $106,720 | $74,515 | 41.12% |
| $5,000 | -129 | $106,220 | $75,015 | 41.39% |
| $5,500 | +371 | $105,720 | $75,515 | 41.67% |

## FY2025 physical count context (sanity check)
- FY2025 ending inventory (physical count based): **$10,015**; FY2025 COGS: **$112,456**.
- Implied FY2025 days of inventory on hand: **32.5 days**.
- FY2025 was impacted by a known overbuy scenario; therefore a lower FY2024 days-on-hand assumption (e.g., roughly half of FY2025) can still be coherent.

## Disposables policy note (why this matters)
- In this project’s FY2024 estimate sheet, **disposables are treated as inventory** (they map into Inventory - Food).
- If you conceptually treat disposables as "supplies" rather than inventory, that would tend to **reduce** the inventory number, not increase it.
- Therefore, a higher FY2024 inventory belief is most consistent with **missing items/locations** rather than a disposables policy mismatch.

## Evidence pointers
- Estimate sheet: `/home/clarencehub/t2-final-fy2024-fy2025/data/inventory/Canteen Inventory May 31 2024 - Estimate from FY2025 Items.csv`
- Generator script: `scripts/90a_generate_inventory_estimate_fy2024_from_fy2025.py`
- Generator audit: `/home/clarencehub/t2-final-fy2024-fy2025/output/inventory_estimate_fy2024_from_fy2025_audit.csv`
- Inventory JE evidence: `output/snapshots/20260202-231500/output/inventory_journal_detail.csv` and `output/snapshots/20260202-231500/output/inventory_journal_detail.csv`
- Override audit (if/when used): `output/snapshots/20260202-231500/output/inventory_override_audit.csv`

## If you choose to restate later (operator-controlled)
- Re-run the generator with a different target center/tolerance, update the manifest sha256, and refresh.
- This will cascade deterministically into FY2025 opening inventory (carryforward consistency).
