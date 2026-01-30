# Independent Recalculations — FY2025 UFile Attempt 002

**Generated:** 2026-01-29
**ATTEMPT_ID:** attempt_002
**Method:** All calculations use only parsed attempt amounts unless otherwise noted.

---

## 1. Operating Expenses Verification (Schedule 125)

### Detail expense lines from attempt (parsed CSV):

| GIFI | Description | Amount |
|------|-------------|--------|
| 8520 | Advertising and promotion | 798 |
| 8523 | Meals and entertainment | 408 |
| 8622 | Employer's portion of employee benefits | 3,610 |
| 8690 | Insurance | 1,951 |
| 8710 | Interest and bank charges | 6,694 |
| 8810 | Office expenses | 3,903 |
| 8813 | Data processing | 1,878 |
| 8860 | Professional fees | 353 |
| 8911 | Real estate rental | 7,137 |
| 8960 | Repairs and maintenance | 981 |
| 9060 | Salaries and wages | 54,899 |
| 9130 | Supplies | 5,348 |
| 9131 | Small tools | 479 |
| 9225 | Telephone and telecommunications | 465 |
| 9270 | Other expenses | 3,782 |
| 9275 | Delivery, freight and express | 136 |
| 9281 | Vehicle expenses | 4,038 |

### Sum of detail expense lines:

```
  798 + 408 + 3,610 + 1,951 + 6,694 + 3,903 + 1,878 + 353
+ 7,137 + 981 + 54,899 + 5,348 + 479 + 465 + 3,782 + 136 + 4,038
= 96,860
```

### Comparison:

| Source | 9367 Value |
|--------|------------|
| Attempt (9367) | 96,860 |
| Sum of detail lines | 96,860 |
| Project expected | 96,860 |

**Result:** Operating expenses MATCH ✓ (issue from Attempt 001 was fixed)

---

## 2. Cost of Goods Sold (COGS) Verification

### From attempt:

| GIFI | Description | Amount |
|------|-------------|--------|
| 8300 | Opening inventory | 2,847 |
| 8320 | Purchases / cost of materials | 112,866 |
| 8500 | Closing inventory | (10,015) |
| 8518 | Cost of sales | 105,698 |

### COGS calculation:

```
COGS = Opening + Purchases - Closing
     = 2,847 + 112,866 - 10,015
     = 105,698
```

**Result:** COGS = $105,698 ✓ (matches 8518 in attempt and project)

---

## 3. Gross Profit Verification

### Calculation:

```
Gross Profit = Total Revenue - COGS
             = 230,907 - 105,698
             = 125,209
```

**Result:** Gross profit = $125,209 ✓ (matches 8519 in attempt)

---

## 4. Net Income Verification

### Using attempt's total expenses:

```
Total Expenses = COGS + Operating Expenses
               = 105,698 + 96,860
               = 202,558

Net Income = Total Revenue - Total Expenses
           = 230,907 - 202,558
           = 28,349
```

**Result:** Net income = $28,349 ✓ (matches 9999 in attempt and project)

---

## 5. Equity Verification (Schedule 100)

### From attempt:

| GIFI | Description | Amount |
|------|-------------|--------|
| 3500 | Common shares | 100 |
| 3600 | Retained earnings | 45,005 |
| 3620 | Total shareholder equity | 45,105 |

### Equity calculation (attempt):

```
Total Equity = Common shares + Retained earnings
             = 100 + 45,005
             = 45,105 ✓ (internally consistent)
```

### Project expected:

| GIFI | Description | Amount |
|------|-------------|--------|
| 3500 | Common shares | 100 |
| 3600 | Retained earnings | 8,104 |
| 3620 | Total shareholder equity | 8,204 |

**Equity discrepancy:** $45,105 - $8,204 = **$36,901**

---

## 6. Balance Sheet Equation Test

### Attempt values:

```
Total Assets (2599)                    = 25,977
Total Liabilities (3499)               = 17,773
Total Shareholder Equity (3620)        = 45,105
Liabilities + Equity                   = 62,878

Balance test: 25,977 ≠ 62,878
Difference: 36,901
```

**Result:** DOES NOT BALANCE ✗

### Project expected values:

```
Total Assets (2599)                    = 25,977
Total Liabilities (3499)               = 17,773
Total Shareholder Equity (3620)        = 8,204
Liabilities + Equity                   = 25,977

Balance test: 25,977 = 25,977
```

**Result:** Project values BALANCE ✓

---

## 7. Retained Earnings Rollforward Verification

### From attempt (GIFI Schedule 100):

| GIFI | Description | Amount |
|------|-------------|--------|
| 3660 | RE Start | 16,656 |
| 3680 | Net income | 28,349 |
| 3700 | Dividends declared | (36,900) |
| 3740 | Other items | (1) |
| 3849 | RE End | 45,005 |

### Attempt rollforward (what UFile computed):

```
RE End (UFile calc) = RE Start + Net Income
                    = 16,656 + 28,349
                    = 45,005

Note: UFile IGNORED the 3700 and 3740 entries!
```

**Why?** Dividends were entered on the GIFI balance sheet but the "Dividends Paid" screen was not completed.

### Correct rollforward:

```
RE End = RE Start + Net Income - Dividends + Other
       = 16,656 + 28,349 - 36,900 - 1
       = 8,104 ✓
```

### Retained earnings discrepancy:

| Item | Attempt | UFile Internal | Correct | Issue |
|------|---------|----------------|---------|-------|
| 3660 RE Start | 16,656 | 16,656 | 16,656 | ✓ |
| 3680 Net income | 28,349 | 28,349 | 28,349 | ✓ |
| 3700 Dividends | (36,900) | NOT APPLIED | (36,900) | ✗ Not on Dividends Paid screen |
| 3740 Rounding | (1) | NOT APPLIED | (1) | ✗ Not applied |
| 3849 RE End | 45,005 | 45,005 | 8,104 | ✗ +$36,901 |

---

## 8. Summary of Root Cause Arithmetic

The $36,901 balance sheet imbalance:

```
RE End (attempt)    = 45,005
RE End (correct)    = 8,104
Difference          = 36,901

Breakdown:
  Missing Dividends:    0 - (-36,900) = +36,900
  Missing Rounding:     0 - (-1)      = +1

  Net effect on RE: +36,900 + 1 = +36,901 ✓ (matches the imbalance)
```

---

## 9. 3640 Consistency Check

### Attempt:

| GIFI | Description | Amount |
|------|-------------|--------|
| 2599 | Total assets | 25,977 |
| 3499 | Total liabilities | 17,773 |
| 3620 | Total equity | 45,105 |
| 3640 | Total L+E | 62,878 |

**Check:** 3499 + 3620 = 17,773 + 45,105 = 62,878 = 3640 ✓

**Problem:** 3640 (62,878) ≠ 2599 (25,977)

### Project:

**Check:** 3499 + 3620 = 17,773 + 8,204 = 25,977 = 3640 = 2599 ✓

---

## 10. Improvements from Attempt 001

| Issue | Attempt 001 | Attempt 002 | Status |
|-------|-------------|-------------|--------|
| 9367 manual entry | $89,155 (wrong) | $96,860 (correct) | **FIXED** |
| 9220 duplicate | $465 | Not present | **FIXED** |
| 3660 RE Start | $8,104 (wrong) | $16,656 (correct) | **FIXED** |
| Dividends on screen | Not entered | Not entered | **STILL BROKEN** |

---

## Conclusion

**Attempt 002 is much closer to correct than Attempt 001:**
- Schedule 125 (income statement) is now fully correct
- Retained earnings rollforward inputs (3660, 3680, 3700, 3740) are correct
- The only remaining issue is that the "Dividends Paid" UFile screen was not completed

**Fix:** Complete the "Dividends Paid" screen with:
- Taxable dividends paid: $36,900
- Eligible portion: $0
