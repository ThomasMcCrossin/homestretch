# Next Actions - FY2025 Merchant Fee Investigation

**Analysis Date:** 2026-01-30
**Status:** Pending verification - no source data changes made

---

## Priority 1: Verify Shopify CC Fees Bill Origin

### Question to Answer
Is the Wave bill "Shopify - Bill 2024 CC Fees" (Invoice #2024, $2,208.04) an **actual invoice from Shopify** or a **manually created summary entry** in Wave?

### Verification Steps

1. **Check Wave UI directly:**
   - Log into Wave accounting
   - Navigate to Bills > Vendor: Shopify
   - Locate bill dated 2024-12-31 with Invoice #2024
   - Determine: Is there a linked PDF/attachment? Was it manually created?

2. **Check Shopify Admin:**
   - Log into Shopify Admin
   - Navigate to Settings > Payments > View all payouts
   - Check for any annual fee invoices or summary statements
   - Look for billing statements in Settings > Billing

3. **Review source file:**
   ```
   /home/clarencehub/Fresh/dump/FY2025AccountTransactions.csv
   ```
   - Search for "CC Fees" or "Invoice 2024"
   - Determine how this transaction was originally categorized

---

## Priority 2: Determine Correct Treatment

### If Shopify CC Fees Bill is DUPLICATE (likely)

**Action:** Remove the Wave bill from expense calculation
- The $2,208.04 should be backed out of 5300 (Merchant Processing Fees)
- This will reduce GIFI 8710 from $6,694 to $4,486
- Net income increases by $2,208

**Corrected 5300 balance:** $761.92 (Nayax $587.33 + other Shopify $174.59)

### If Shopify CC Fees Bill is LEGITIMATE (unlikely)

This would mean Shopify charges fees in two ways:
1. Per-transaction fees (deducted from payouts) - captured in 6210
2. Annual/periodic invoice fees (billed separately) - captured in 5300

This is unusual for Shopify but possible if:
- There's a Shopify Payments monthly subscription
- There are third-party payment processor fees
- There are international transaction fees billed separately

---

## Priority 3: Amendment Considerations

### If Double-Count is Confirmed

**Impact Assessment:**
| Item | Current | Corrected | Change |
|------|---------|-----------|--------|
| 8710 Interest and bank charges | $6,694 | $4,486 | -$2,208 |
| Net income (9999) | $28,349 | $30,557 | +$2,208 |
| Taxable income | Higher | Lower | -$2,208 |

**Filing Implications:**
- If amendment is required, use T2-ADJ or amended T2
- Consider materiality: $2,208 on $28,349 net income = 7.8% (material)
- CRA may apply penalties/interest if tax is owed

### Recommended Workflow

1. Complete verification (Priority 1)
2. If duplicate confirmed:
   - Document finding in `docs/` (not in this analysis directory)
   - Update packet.json with corrected values
   - Create new UFile attempt with corrected 8710 value
3. If NOT duplicate:
   - Document evidence proving legitimacy
   - Current return is correct

---

## Data Integrity Notes

**DO NOT modify without verification:**
- `db/t2_final.db` - contains source journal entries
- `UfileToFill/ufile_packet/` - contains canonical packet data
- `T2Analysis/t2_attempts/FY2025/ufile/exports/` - contains filed returns

**Safe to modify:**
- This analysis directory: `T2Analysis/t2_attempts/FY2025/ufile/analyses/claude/run_20260130_151433/`
- New packet versions under `UfileToFill/ufile_packet/years/FY2025/`

---

## Summary

| Finding | Status | Next Step |
|---------|--------|-----------|
| Attempt 4 matches packet | Confirmed | No action needed |
| BCR warnings | Non-blocking | OK to file |
| Shopify CC Fees bill ($2,208) | **INVESTIGATE** | Verify origin in Wave/Shopify |
| Nayax fees ($587) | Valid | No action |
| Payout fees ($2,227) | Valid | No action |

**Key Question:** Is Wave bill 541 "Shopify - Bill 2024 CC Fees" a duplicate of the payout fees already captured, or a separate legitimate charge?

---
*This document provides recommendations only. No source data has been modified.*
