# Diagnostics Catalogue — FY2025 UFile Attempt

**Generated:** 2026-01-29
**Source:** diagnostics.csv (parsed from UFile PDF attempt)

---

## Summary

| Category | Count |
|----------|-------|
| **Blocking** | 2 |
| **Non-Blocking (Warnings)** | 2 |
| **Total** | 4 |

---

## Blocking Diagnostics

These prevent the return from being filed electronically.

### 1. GIFI-FIELD 9367 Internal Subtotal Mismatch

**Exact Text:**
> GIFI-FIELD 9367 does not match internal subtotal calculation.
> GIFI-FIELD 9367:$89,155 Calculation:$97,325 Difference:$8,170

**Classification:** BLOCKING

**Analysis:**
- User manually entered $89,155 on line 9367 (Total operating expenses)
- UFile computed $97,325 from the detail expense lines entered
- The $8,170 difference = $97,325 - $89,155

**Root Cause:** Manual entry on a total line that UFile auto-calculates. Per the Fill Guide: "If you see diagnostics like 'GIFI-FIELD 9367 does not match internal subtotal calculation': you typed 9367 manually; clear it and let UFile compute it from the expense lines."

---

### 2. Balance Sheet Does Not Balance

**Exact Text:**
> GIFI sch. 100 - total assets does not equal total liabilities plus shareholder equity.
> GIFI-FIELD 2599:$25,977 (GIFI-FIELD 3499 + GIFI-FIELD 3620): $62,031 Difference:$36,054

**Classification:** BLOCKING

**Analysis:**
- Total assets (2599) = $25,977
- Total liabilities (3499) = $17,773
- Total shareholder equity (3620) = $44,258
- Sum of L+E = $62,031
- Assets vs L+E difference = $36,054

**Root Cause:** Retained earnings is overstated by $36,054 due to:
1. Wrong RE Start (3660): Entered $8,104 instead of $16,656
2. Wrong Net income (3680): Shows $36,054 instead of $28,349 (due to expense errors)
3. Missing dividends (3700): $36,900 not entered in retained earnings schedule

---

## Non-Blocking Diagnostics (Warnings)

### 3. Federal efile Ineligibility

**Exact Text:**
> This return is ineligible for federal efile due to the following reason(s):
> The federal BCR is not being generated.

**Classification:** NON-BLOCKING (downstream effect)

**Analysis:** This is a consequence of the blocking diagnostics above. Once the data entry errors are fixed, this warning should clear.

---

### 4. Missing INCOMESOURCE Entry

**Exact Text:**
> Missing entry for INCOMESOURCE; all income is considered as active business income.

**Classification:** NON-BLOCKING (warning)

**Analysis:** UFile defaults to treating all income as active business income, which is correct for this corporation (a CCPC operating a restaurant). This warning can be ignored or addressed by selecting the income source explicitly in UFile.

---

## Additional Observations from Full Text Review

1. **BCR VALIDITY CHECKS FAILED** — Bar codes not generated; direct consequence of the blocking errors.

2. **Taxation year presumed to be 365 days** — This is correct and not an error.

---

## Summary by Priority

| Priority | Diagnostic | Fix Required |
|----------|-----------|--------------|
| 1 (Critical) | Balance sheet imbalance ($36,054) | Fix retained earnings: correct 3660 to $16,656, enter 3700 = $36,900 |
| 2 (Critical) | 9367 subtotal mismatch ($8,170) | Clear 9367 manual entry; also remove duplicate 9220 ($465) |
| 3 (Low) | INCOMESOURCE missing | Optional: select "Active business income" in UFile |
