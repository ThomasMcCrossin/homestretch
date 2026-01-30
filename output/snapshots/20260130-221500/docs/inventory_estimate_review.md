# Inventory estimate review (senior accountant lens) — FY2024 closing inventory

Scope:
- FY2024: 2023-06-01 → 2024-05-31
- FY2025: 2024-06-01 → 2025-05-31
- Objective: recommend a **defensible FY2024 ending inventory estimate** (and sanity-check FY2025, which management believes is accurate).

## Sources inspected (read-only)

Project outputs:
- `output/trial_balance_FY2024.csv`
- `output/trial_balance_FY2025.csv`
- `output/inventory_journal_summary.md`
- `output/inventory_journal_detail.csv`

Inventory count sheets (supporting evidence):
- `/home/clarencehub/curlys-books/t2-filing-fy2024-fy2025/data/Canteen Inventory May 31 2024 - Estimated.csv`
- `/home/clarencehub/curlys-books/t2-filing-fy2024-fy2025/data/Canteen Inventory May 16 2025 - Sheet1.csv`

SQLite source-of-truth (read-only queries):
- `/home/clarencehub/t2-final-fy2024-fy2025/db/t2_final.db`
  - Tables: `chart_of_accounts`, `journal_entries`, `journal_entry_lines`

## Executive summary (recommendation)

**Recommended FY2024 closing inventory (at cost): $2,847.23**

Why this is the best number today:
- It is supported by an **itemized management estimate sheet** dated exactly at FY2024 year-end (2024-05-31), with category subtotals and line items.
- Analytical cross-checks against FY2024 purchase patterns and the business’s seasonal “end-of-season” context do **not** contradict this magnitude.
- Alternative “ratio-based” methods (calibrating from FY2025) produce wide ranges that are **less defensible** than the documented FY2024 estimate, because FY2025 includes a very large retail/snacks stock position that does not appear comparable to the first year.

Confidence: **Medium** (good documentary support, but still an estimate; improved to “High” if a contemporaneous count method/cutoff memo exists).

## What is already booked (current inventory balances)

Inventory accounts used:
- `1200` Inventory – Food
- `1210` Inventory – Beverage
- `1220` Inventory – Supplements
- `1230` Inventory – Retail Goods

Per trial balance:
- FY2024 closing inventory total: **$2,847.23**
  - Food: $1,718.73
  - Beverage: $312.50
  - Retail: $816.00
  - Supplements: $0.00
- FY2025 closing inventory total: **$10,015.47**
  - Food: $4,673.66
  - Beverage: $930.75
  - Retail: $4,411.06
  - Supplements: $0.00

Note on category mapping: the inventory import maps “Beverages” → `1210`, “Snacks/Retail” → `1230`, “Supplements” → `1220`, and **everything else** (Dry Food / Condiments / Frozen / Disposables, etc.) → `1200`.

## Step 1 — Sales and COGS totals (sanity check)

Computed from posted journals (net of inventory adjustments):

FY2024:
- Revenue: **$181,234.87**
- COGS: **$104,712.94**
- Gross margin: **42.2%**

FY2025:
- Revenue: **$230,906.57**
- COGS: **$105,298.48**
- Gross margin: **54.4%**

Key observation:
- The gross margin shift (≈ +12 points) is **too large** to be “fixed” by a small inventory estimate alone; it more likely reflects a combination of pricing/mix changes and/or classification differences (e.g., some FY2024 costs posted to COGS that became supplies/other expense in FY2025, or vice versa).
- Therefore, the inventory estimate should be anchored primarily in **count evidence**, not forced to “make GM look like FY2025”.

## Step 2 — What “purchases” look like in the books (COGS accrual stream)

The best purchases proxy in this system is the **Wave bill accrual postings** to COGS-type accounts (`gifi_code=8518`), because that is where inventory-like spending is recognized by invoice date.

Annual COGS purchases proxy (Wave bills only):

FY2024 total: **$102,029.43**
- Food: $77,498.72
- Beverage: $8,666.87
- Retail: $12,765.22
- Supplements: $1,840.67
- Freight: $554.11
- Deposits: $703.84

FY2025 total: **$112,454.51**
- Food: $82,244.29
- Beverage: $15,078.24
- Retail: $11,836.46
- Supplements: $1,848.69
- Freight: $297.34
- Deposits: $1,149.49

Seasonality signal:
- Purchases (and sales) are concentrated roughly Sep–Mar, with very low activity by April/May in FY2025.

## Step 3 — Year-end context and cutoff considerations (foodservice reality)

Foodservice/retail reality that matters here:
- Year-end is **end-of-season** for many canteen operations; you can (a) run down stock aggressively, leaving low inventory, or (b) end with “leftovers” (notably snacks/disposables) that carry into the next season.
- Frozen and perishable categories typically cannot be carried as heavily as retail snacks; disposables can.
- End-of-season dynamics can make “weeks on hand” look artificially high if the business stops purchasing and slows sales near year end.

FY2025 cutoff note:
- FY2025 inventory sheet is dated **2025-05-16** but posted as of **2025-05-31**.
- Purchases posted after 2025-05-16 through 2025-05-31 in the COGS accrual stream are small (≈ **$390.71**), so the dating difference is likely not material for an estimate-level filing.

## Method A (preferred) — Use the FY2024 management estimate sheet, then test reasonableness

FY2024 source is explicitly an “ESTIMATED TOTAL” but it is **itemized** by:
- Dry Food, Condiments, Beverages, Frozen, Disposables, Snacks
- with quantities and unit costs for many SKUs
- with notes explaining why amounts are scaled down vs FY2025 and “playoff exit stock”

This is exactly the type of support a CRA reviewer expects if a formal count is unavailable: dated schedule + cost basis + reasonable explanation.

Reasonableness tests:
- FY2024 last 12 weeks purchases proxy (2024-03-09..2024-05-31): **$20,645.99**
  - Closing inventory $2,847 is ~**13.8%** of this late-season purchase run-rate.
- FY2024 last 20 weeks purchases proxy (2024-01-13..2024-05-31): **$44,088.91**
  - Closing inventory $2,847 is ~**6.5%** of this run-rate.

Interpretation:
- A ~$2.8k closing position is consistent with a first-year operation that ended the season without a large retail overstock.

## Method B — Purchases/COGS “weeks on hand” calibration (use carefully)

If you compute “weeks on hand” as: closing inventory ÷ (annual purchases ÷ 52),
you get:

- FY2024: $2,847 ÷ ($102,029 ÷ 52) ≈ **1.45 weeks**
- FY2025: $10,015 ÷ ($112,455 ÷ 52) ≈ **4.63 weeks**

This large FY2025 result is explained by **retail/snacks overstock** at year end:
- FY2025 retail inventory is $4,411 against annual retail purchases of $11,836 → **37%** of annual retail purchases sitting in inventory at year end.
- That is not a “typical steady-state” benchmark; it’s a business-specific outcome (expanded retail offering and/or end-of-season carryover).

So, using FY2025 as a direct ratio template for FY2024 is not recommended without additional context, because it would overstate FY2024 inventory.

## Selection and suggested range

Given the evidence:
- **Recommended point estimate:** **$2,847.23** (use the FY2024 estimate sheet)
- **Reasonable sensitivity range for discussion:** **$2,500 – $5,500**
  - Lower bound reflects “aggressive run-down + conservative estimate”.
  - Upper bound reflects “under-counted disposables/food carryover”, roughly aligning FY2024 food/beverage carry rates closer to FY2025 levels, while **not** importing FY2025’s exceptional retail/snacks overstock.

If you want to tighten that range materially, the fastest high-impact evidence would be:
- any dated purchase invoices near 2024-05-31 indicating major stock on hand (especially disposables/snacks), and/or
- a short management memo describing the May 2024 playoff exit, what was left, and what was disposed of.

## Reconciliation table (how inventory affects COGS)

All numbers are dollars, based on posted journals.

FY2024:
- Purchases proxy (Wave bill COGS accruals): **$102,029.43**
- ITC start-date adjustment posted into COGS (project-specific): **$5,530.74**
- Closing inventory adjustment (credit COGS): **$(2,847.23)**
- Net COGS reported: **$104,712.94**

FY2025:
- Purchases proxy (Wave bill COGS accruals): **$112,454.51**
- Opening inventory (debit COGS): **$2,847.23**
- Closing inventory (credit COGS): **$(10,015.47)**
- Other small COGS adjustment (manual): **$12.21**
- Net COGS reported: **$105,298.48**

## Recommended journal entry format (not executed)

This project already uses the classic “closing inventory” approach:

At FY2024 end (2024-05-31), to record closing inventory at cost:
- Dr `1200/1210/1220/1230` Inventory (by category totals)
- Cr `5000/5010/5020/5030` COGS (reduce expense)

At FY2025 start (2024-06-01), to reverse opening inventory:
- Dr `5000/5010/5020/5030` COGS
- Cr `1200/1210/1220/1230` Inventory

## Questions to management (max 10)

1) For FY2024: was the May 31, 2024 estimate built from an actual walk-through count, or derived by scaling FY2025? Any photos/count notes?
2) Were there any offsite storage areas (home/garage) holding inventory at 2024-05-31 that were excluded?
3) Were disposables treated as “inventory on hand” intentionally? If not, should some be reclassified to supplies/prepaids consistently across years?
4) Was any stock written off at season end (expired food, damaged snacks, spoiled frozen)? If yes, approximate amount and category.
5) For FY2025: why was retail/snacks inventory so high at May 16 (carryover strategy, bulk buy, slow turnover, etc.)?
6) Were there any consignment/returnable arrangements (e.g., ability to return unopened cases) that would affect “inventory at cost” vs NRV?
7) Any known major deliveries immediately before/after 2024-05-31 that could cause cutoff error?
8) Are bottle/container deposits included in inventory counts, and if yes, is that consistent with how deposits are handled in sales/COGS?
9) Did product mix materially change (more retail goods, fewer food items) from FY2024 to FY2025?
10) If CRA asked: what is the inventory valuation method (cost basis used per line, and whether any lower-of-cost-or-market adjustments were made)?

