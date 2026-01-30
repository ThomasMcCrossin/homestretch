# FY2024 Inventory Estimate - Independent Audit Review

**Prepared by:** Senior Corporate Accountant (20+ years foodservice/retail COGS experience)
**Date:** 2026-01-27
**Entity:** Canteen Operations (Corp)
**Fiscal Years:** FY2024 (2023-06-01 to 2024-05-31), FY2025 (2024-06-01 to 2025-05-31)

---

## 1. Executive Summary

### Recommended FY2024 Ending Inventory Value

| Metric | Value |
|--------|-------|
| **Recommended FY2024 Ending Inventory** | **$7,500** |
| Current Recorded Estimate | $2,847.23 |
| Recommended Adjustment | +$4,652.77 |
| Confidence Level | **Moderate** (65-75%) |
| Primary Method | Weighted average of COGS flow/gross margin (Method A) and weeks-on-hand calibration (Method B) |

### Rationale

The current FY2024 ending inventory estimate of $2,847.23 appears **understated** based on:

1. **Gross margin inconsistency**: FY2024 shows 42.2% gross margin vs FY2025's 54.4% - a 12.2 point swing unusual for same business
2. **Weeks-on-hand analysis**: Current estimate implies only 1.1 weeks inventory, while FY2025 shows 3.5 weeks
3. **Operational implausibility**: June/July 2024 purchases totaled only $387; insufficient to support operations without carryover inventory
4. **Source documentation**: FY2024 inventory explicitly marked "Estimated" in source filename

The recommended estimate of **$7,500** is:
- Conservative (lower end of $7,500-$8,700 range)
- Results in 44.8% gross margin (reasonable for mixed convenience/foodservice)
- Represents ~3.0 weeks on hand
- CRA defensible

**Note:** An existing review (`inventory_estimate_review.md`) recommends retaining the $2,847.23 figure. This independent analysis reaches a different conclusion; management should consider both perspectives.

---

## 2. Evidence and Analysis

### 2.1 Data Sources Inspected (Read-Only)

| Source | Description |
|--------|-------------|
| `db/t2_final.db` | Primary SQLite database |
| `output/trial_balance_FY2024.csv` | FY2024 trial balance |
| `output/trial_balance_FY2025.csv` | FY2025 trial balance |
| `output/inventory_journal_detail.csv` | Inventory journal entries |
| `output/inventory_journal_summary.md` | Inventory source documentation |
| `output/vendor_profiles.md` | Vendor allocation profiles |
| `output/gifi_schedule_125_FY2024.csv` | GIFI income statement FY2024 |
| `output/gifi_schedule_125_FY2025.csv` | GIFI income statement FY2025 |
| `wave_bills` table | All vendor invoices |
| `bill_allocations` table | COGS/expense allocations |
| `journal_entries` / `journal_entry_lines` | Complete journal record |

### 2.2 Key Financial Data

| Metric | FY2024 | FY2025 |
|--------|--------|--------|
| Total Sales (Net) | $181,235 | $230,907 |
| Total COGS | $104,748 | $105,286 |
| **Gross Margin** | **42.2%** | **54.4%** |
| Ending Inventory | $2,847 | $10,015 |
| Total Purchases (Wave Bills) | $129,448 | $146,792 |
| COGS-related Purchases | $100,771 | $111,008 |
| **Weeks on Hand** | **1.1** | **3.5** |

### 2.3 Red Flags Identified

1. **Revenue grew 27.4% but COGS grew only 0.5%** - mathematically inconsistent without inventory adjustment
2. **June-July 2024 purchases of only $387** - business couldn't operate without carryover stock
3. **FY2024 source file explicitly labeled "Estimated"**

---

## 3. Quantitative Approaches

### Method A: Gross Margin Consistency

| Target GM | Implied COGS | Implied Inventory |
|-----------|-------------|-------------------|
| 42.2% (current) | $104,748 | $2,847 |
| 45.0% | $99,679 | **$7,916** |
| 48.0% | $94,242 | $13,353 |
| 54.4% (match FY25) | $82,643 | $24,952 |

**Method A suggests: $7,000-$8,000**

### Method B: Weeks-on-Hand Calibration

FY2025 ending inventory = 3.5 weeks of purchases. Applying to FY2024:

| Weeks on Hand | Implied FY2024 Inventory |
|---------------|-------------------------|
| 2.5 weeks | $6,223 |
| 3.0 weeks | **$7,468** |
| 3.5 weeks | $8,713 |
| 4.0 weeks | $9,958 |

**Method B suggests: $7,500-$8,700**

### Method C: Vendor Mix Analysis (Supporting)

Major inventory vendors (GFS 36%, Costco 31%, Capital 8%) supply products with typical 2.5-4 week turnover, supporting ~3 weeks on hand estimate.

---

## 4. Reconciliation Table

| Metric | FY2024 Current | FY2024 Proposed | FY2025 |
|--------|----------------|-----------------|--------|
| Sales | $181,235 | $181,235 | $230,907 |
| COGS | $104,748 | $100,095 | $105,286 |
| **Gross Margin** | **42.2%** | **44.8%** | **54.4%** |
| Ending Inventory | $2,847 | **$7,500** | $10,015 |
| **Weeks on Hand** | **1.1** | **3.0** | **3.5** |

---

## 5. Stress Test: Sensitivity Analysis

| Inv Estimate | Gross Margin | Weeks on Hand | Net Income Impact |
|-------------|-------------|---------------|-------------------|
| $2,847 (current) | 42.2% | 1.1 | — |
| $5,000 | 43.4% | 2.0 | +$2,153 |
| $6,000 | 43.9% | 2.4 | +$3,153 |
| **$7,500 (recommended)** | **44.8%** | **3.0** | **+$4,653** |
| $8,700 | 45.4% | 3.5 | +$5,853 |
| $10,000 | 46.1% | 4.0 | +$7,153 |

---

## 6. Recommended Journal Entry (Not Executed)

**Entry Date:** 2024-05-31
**Description:** FY2024 ending inventory revision per audit review

| Account | Account Name | Debit | Credit |
|---------|-------------|-------|--------|
| 1200 | Inventory - Food | $2,810.27 | — |
| 1210 | Inventory - Beverage | $511.80 | — |
| 1230 | Inventory - Retail Goods | $1,330.70 | — |
| 5000 | COGS - Food | — | $2,810.27 |
| 5010 | COGS - Beverage | — | $511.80 |
| 5030 | COGS - Retail Goods | — | $1,330.70 |
| | **Total** | **$4,652.77** | **$4,652.77** |

---

## 7. Questions to Management

1. Was any physical count performed at May 31, 2024? Documentation?
2. What inventory existed when operations began June 2023?
3. Is this a seasonal operation (school year, sports season)?
4. How did operations continue June-July 2024 with only $387 in new purchases?
5. Any known shrinkage/spoilage events in FY2024?
6. Were bulk purchases made in late FY2024?
7. Did product mix or pricing change significantly between years?
8. How was FY2025 count performed (full physical, cycle, estimate)?
9. Inventory valuation method (cost, LCM)?
10. Any offsite storage locations excluded from counts?

---

## 8. Auditor's Conclusion

The current FY2024 ending inventory of $2,847.23 is likely understated. Based on convergent evidence from gross margin analysis, weeks-on-hand calibration, and operational plausibility testing, a revised estimate of **$7,500** is recommended.

This estimate is **conservative** (lower end of reasonable range) and **CRA defensible** given documented methodology and industry-reasonable results.

---

*End of Report*
