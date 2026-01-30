# Diagnostics Catalogue — FY2025 UFile Attempt 002

**Generated:** 2026-01-29
**Source:** messages.txt + diagnostics.csv (parsed from UFile PDF attempt)
**ATTEMPT_ID:** attempt_002

---

## Summary

| Category | Count |
|----------|-------|
| **Blocking** | 2 |
| **Non-Blocking (Warnings)** | 5 |
| **Total** | 7 |

---

## UFile Messages → Screen Mapping

### Blocking Errors

| # | Message Text | UFile Screen | Field(s) Affected | Fix Action |
|---|-------------|--------------|-------------------|------------|
| 1 | "GIFI 100 does not balance (GIFI field 2599 does not equal GIFI fields 3499+3620)" | Schedule 100 (GIFI Balance Sheet) | 2599, 3499, 3620, 3600 | Fix retained earnings via Dividends Paid screen |
| 2 | "BAR CODE RETURN (BCR) VALIDITY CHECKS FAILED — No bar codes were generated" | N/A (downstream) | — | Fix blocking errors first |
| 3 | "You cannot currently EFILE your federal return — The federal BCR is not being generated" | EFILE tab | — | Fix blocking errors first |

### Non-Blocking Warnings

| # | Message Text | UFile Screen | Field(s) Affected | Fix Action |
|---|-------------|--------------|-------------------|------------|
| 4 | "An amount entered in GIFI fields 3700 or 3701 on GIFI – Balance sheet page, the section 'Dividends paid' is missing. Click here to verify your data." | **Dividends paid** screen (under Corporate Data → Dividends paid) | 3700 (GIFI) + Dividends Paid screen fields | **Enter dividends on the Dividends Paid screen**: Taxable dividends paid = $36,900; Eligible portion = $0 |
| 5 | "Tax year presumed to be 365 days according to begin date of operations or incorporation date." | Identification of the Corporation | Tax year dates | No action needed (correct) |
| 6 | "There is no entry in the income source section; all income is considered as active business income." | Income source section (Schedule 7 / Income allocation) | Income source selection | Optional: select "Active business income" explicitly |
| 7 | "Dividends declared have been entered in GIFI but dividends paid has not been entered." | **Dividends paid** screen | Dividends Paid screen | **Enter dividends on the Dividends Paid screen** |
| 8 | "No instalments required since total tax instalments calculated are less than or equal to $3,000." | Instalments | — | Informational; no action |
| 9 | "GIFI-Field 3849 does not match internal subtotal calculation. GIFI-Field 3849:$45005 Calculation:$8104 Difference:$36901" | Schedule 100 (Retained Earnings section) | 3849, 3660, 3680, 3700, 3740 | **Do NOT manually enter 3849**; ensure retained earnings rollforward is correct and Dividends Paid screen is completed |
| 10 | "GIFI sch. 100 - total assets does not equal total liabilities plus shareholder equity. GIFI-Field 2599:$25977 (GIFI-Field 3499 + GIFI-Field 3620): $62878 Difference:$36901" | Schedule 100 | 2599, 3499, 3620 | Fix retained earnings (root cause is missing Dividends Paid screen entry) |

---

## Root Cause Analysis

### The Critical Issue: Dividends Paid Screen Not Completed

The attempt shows:
- 3700 (Dividends declared) = -$36,900 on the GIFI balance sheet page
- But UFile's internal RE calculation ignores this because **the "Dividends paid" screen was not completed**

**UFile Behavior:**
- Entering 3700 on the GIFI balance sheet alone does NOT tell UFile to deduct dividends from retained earnings
- You must ALSO complete the "Dividends paid" screen under Corporate Data for UFile to recognize the dividend distribution
- Without this, UFile computes: RE End = $16,656 + $28,349 = $45,005 (ignoring the $36,900 dividend)

**Correct Flow:**
1. Complete "Dividends paid" screen: Taxable dividends paid = $36,900
2. UFile will then compute: RE End = $16,656 + $28,349 - $36,900 - $1 = $8,104
3. Balance sheet will balance: $25,977 = $17,773 + $8,204

---

## Detailed Message Explanations

### Message 4 & 7: "Dividends paid is missing"

**Plain English:** You entered a dividend amount on the GIFI balance sheet (line 3700), but you didn't complete the dedicated "Dividends paid" screen. UFile requires both.

**UFile Screen:** Interview → Corporate Data → Dividends paid (or similar path depending on UFile version)

**Values to Enter:**
| Field | Value |
|-------|-------|
| Taxable dividends paid during the year | 36,900 |
| Eligible portion of taxable dividends | 0 |
| Capital dividends (Section 83(2)) | 0 |
| Capital gains dividend | 0 |

### Message 9: "GIFI-Field 3849 does not match"

**Plain English:** UFile calculated retained earnings ending balance as $8,104, but the GIFI schedule shows $45,005. The difference ($36,901) equals the missing dividend deduction ($36,900) plus rounding ($1).

**Root Cause:** The Dividends Paid screen is not completed, so UFile's internal rollforward doesn't subtract dividends.

**Fix:** Complete the Dividends Paid screen (see above). Do NOT manually type 3849 or 3600.

### Message 10: "Total assets does not equal total liabilities plus shareholder equity"

**Plain English:**
- Total assets (2599) = $25,977
- Total liabilities (3499) = $17,773
- Total equity (3620) = $45,105 (computed as $100 shares + $45,005 RE)
- Sum of L+E = $62,878
- Assets ≠ L+E by $36,901

**Root Cause:** Same as above — retained earnings is overstated because dividends weren't deducted.

---

## Priority Summary

| Priority | Issue | Fix |
|----------|-------|-----|
| **1 (Critical)** | Dividends Paid screen not completed | Complete Dividends Paid screen with $36,900 taxable dividends |
| 2 (Low) | Income source not selected | Optional: select "Active business income" |

---

## Comparison to Attempt 001

| Issue | Attempt 001 | Attempt 002 |
|-------|-------------|-------------|
| Manual entry on 9367 | YES ($89,155) | NO (correct $96,860) |
| Duplicate 9220/9225 | YES ($465 each) | NO (only 9225) |
| Wrong RE Start (3660) | YES ($8,104 instead of $16,656) | NO (correct $16,656) |
| Dividends not on screen | YES | **YES (still missing)** |
| Balance sheet imbalance | YES ($36,054) | YES ($36,901) |

**Progress:** Attempt 002 fixed three of the four issues from Attempt 001. The only remaining issue is completing the Dividends Paid screen.
