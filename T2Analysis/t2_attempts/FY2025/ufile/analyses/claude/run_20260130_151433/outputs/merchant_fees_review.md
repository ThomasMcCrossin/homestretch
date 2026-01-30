# Merchant Fee Deep Dive - FY2025

**Analysis Date:** 2026-01-30
**Focus:** Reconciliation of 5300 (Merchant Processing Fees) vs 6210 (Payment Processing Fees)

---

## Summary of Findings

| Account | Description | FY2025 Total | Source | Records |
|---------|-------------|--------------|--------|---------|
| 5300 | Merchant Processing Fees | $2,969.96 | Wave bill accruals | 8 |
| 6210 | Payment Processing Fees | $2,227.26 | Bank inflows (Shopify payouts) | 160 |
| **Combined** | | **$5,197.22** | | |

Both accounts roll up to **GIFI 8710 (Interest and bank charges)** which shows $6,694 on Schedule 125.

---

## 5300 Merchant Processing Fees - Breakdown

| Date | Description | Amount | Source |
|------|-------------|--------|--------|
| 2024-12-31 | Shopify - Bill 2024 CC Fees (Invoice #2024) | $2,208.04 | Wave bill 541 |
| 2025-02-24 | Nayax - Bill | $557.43 | Wave bill 628 |
| 2025-03-15 | Shopify - Bill | $44.42 | Wave bill 655 |
| 2025-02-13 | Shopify - Bill | $44.09 | Wave bill 617 |
| 2025-05-14 | Shopify - Bill | $43.08 | Wave bill 700 |
| 2025-04-14 | Shopify - Bill | $43.00 | Wave bill 685 |
| 2025-04-30 | Nayax - Bill | $14.95 | Wave bill 693 |
| 2025-05-31 | Nayax - Bill | $14.95 | Wave bill 706 |
| **Total** | | **$2,969.96** | |

### Sub-totals by Vendor:
- **Nayax (vending machine payments):** $587.33
- **Shopify - Other bills:** $174.59
- **Shopify - Bill 2024 CC Fees:** $2,208.04

---

## 6210 Payment Processing Fees - Summary

| Source | FY2025 Total | Records |
|--------|--------------|---------|
| Shopify Payout fees (from bank inflows) | $2,227.26 | 160 |

These are fees deducted from each Shopify payout before bank deposit. Example transactions:
- 2024-11-14: $118.45 (bank txn 833)
- 2024-10-17: $110.48 (bank txn 934)
- 2024-10-03: $106.58 (bank txn 974)
- ... (160 transactions total)

### Monthly Distribution:
| Month | Amount | Count |
|-------|--------|-------|
| 2024-06 | $19.72 | 3 |
| 2024-07 | $0.20 | 1 |
| 2024-08 | $1.11 | 1 |
| 2024-09 | $180.26 | 17 |
| 2024-10 | $411.43 | 22 |
| 2024-11 | $365.46 | 20 |
| 2024-12 | $251.66 | 19 |
| 2025-01 | $334.35 | 22 |
| 2025-02 | $262.86 | 17 |
| 2025-03 | $321.82 | 20 |
| 2025-04 | $51.85 | 15 |
| 2025-05 | $26.54 | 3 |
| **Total** | **$2,227.26** | **160** |

---

## Double-Count Risk Assessment

### Red Flag: Shopify CC Fees Bill vs Payout Fees

| Item | Amount |
|------|--------|
| Shopify - Bill 2024 CC Fees (Wave bill 541) | $2,208.04 |
| Shopify Payout fees (bank inflows) | $2,227.26 |
| **Difference** | **$19.22 (0.9%)** |

**Critical Finding:** These two amounts are nearly identical, suggesting potential duplication:

1. **6210 ($2,227.26):** Captured from 160 individual Shopify payout transactions as the fee deducted before bank deposit
2. **5300 ($2,208.04):** Captured from a single Wave bill dated 2024-12-31 titled "Shopify - Bill 2024 CC Fees"

### Analysis

The "Shopify - Bill 2024 CC Fees" (Invoice #2024) appears to be a **year-end summary bill** for Shopify credit card processing fees. However, these same fees are already captured incrementally via the payout deductions in 6210.

**Why the $19.22 difference?**
- Timing: Some payouts may fall outside FY2025 date range
- Calculation basis: Bill may use different rounding or cutoff dates
- Partial year: The bill is labeled "2024" suggesting calendar year vs fiscal year

---

## Verdict: PROBABLE DOUBLE-COUNT

| Component | Status | Amount |
|-----------|--------|--------|
| Nayax fees (5300) | VALID - separate vendor | $587.33 |
| Shopify other bills (5300) | VALID - separate charges | $174.59 |
| Shopify payout fees (6210) | VALID - primary source | $2,227.26 |
| Shopify CC Fees bill (5300) | **DUPLICATE RISK** | $2,208.04 |

**If this is a double-count:**
- Overstated expenses: $2,208.04
- Understated net income: $2,208.04
- Overstated 8710 Interest and bank charges: $2,208.04

---

## Impact on Filed Return

Current Schedule 125 line 8710: **$6,694**

This includes:
| Account | Amount |
|---------|--------|
| 5300 Merchant Processing Fees | $2,969.96 |
| 6210 Payment Processing Fees | $2,227.26 |
| 6000 Bank Charges & Fees | $1,122.71 |
| 8100 Interest Expense - Bank | $374.03 |
| **Total** | **$6,693.96** |

**If 5300 Shopify CC Fees bill is removed:**
- Corrected 8710: $6,694 - $2,208 = **$4,486**
- Impact on net income: +$2,208

---

## Evidence Sources

- `db/t2_final.db` - journal_entries, journal_entry_lines, wave_bills tables
- `db/t2_final.db` - fresher_credits__shopify_payouts table
- Wave bill allocation: `bill_allocations.id = 4191`
- Match method: INVOICE_NUMBER via FY2025AccountTransactions.csv

---
*This analysis is read-only and makes no changes to source data.*
