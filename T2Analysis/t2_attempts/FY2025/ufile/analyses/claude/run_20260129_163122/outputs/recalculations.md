# Independent Recalculations — FY2025 UFile Attempt

**Generated:** 2026-01-29
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
| 9220 | Utilities | 465 |
| 9225 | Telephone and telecommunications | 465 |
| 9270 | Other expenses | 3,782 |
| 9275 | Delivery, freight and express | 136 |
| 9281 | Vehicle expenses | 4,038 |

### Sum of detail expense lines:

```
  798 + 408 + 3,610 + 1,951 + 6,694 + 3,903 + 1,878 + 353
+ 7,137 + 981 + 54,899 + 5,348 + 479 + 465 + 465 + 3,782 + 136 + 4,038
= 97,325
```

### Comparison:

| Source | 9367 Value |
|--------|------------|
| Attempt (manual entry) | 89,155 |
| UFile internal calculation | 97,325 |
| Project expected | 96,860 |

**Discrepancy explained:**
- Attempt manually entered $89,155 (source unknown — possibly an earlier calculation)
- UFile summed details = $97,325
- Difference from attempt = $97,325 - $89,155 = **$8,170** (matches diagnostic)

**Additional finding:**
- Attempt has BOTH 9220 (Utilities) = $465 AND 9225 (Telephone) = $465
- Project only expects 9225 = $465; NO 9220 entry
- This duplication adds $465 to UFile's calculated total
- $97,325 - $465 = $96,860 = Project expected value

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

### Using attempt's manually-entered total expenses:

```
Net Income = Total Revenue - Total Expenses
           = 230,907 - 194,853
           = 36,054
```

**Result:** Net income per attempt = $36,054 ✓ (internally consistent with attempt data)

### Using properly calculated total expenses:

```
Total Expenses = COGS + Operating Expenses (correct)
               = 105,698 + 96,860
               = 202,558

Net Income = 230,907 - 202,558 = 28,349
```

**Result:** Project expected net income = $28,349

### Net income discrepancy:

| Source | Net Income |
|--------|------------|
| Attempt | 36,054 |
| Project | 28,349 |
| Difference | 7,705 |

**Explanation:**
- $7,705 = $96,860 (correct OpEx) - $89,155 (attempt OpEx manual entry)
- The under-reported operating expenses inflated net income by $7,705

---

## 5. Equity Verification (Schedule 100)

### From attempt:

| GIFI | Description | Amount |
|------|-------------|--------|
| 3500 | Common shares | 100 |
| 3600 | Retained earnings | 44,158 |
| 3620 | Total shareholder equity | 44,258 |

### Equity calculation:

```
Total Equity = Common shares + Retained earnings
             = 100 + 44,158
             = 44,258
```

**Result:** Attempt's 3620 is internally consistent ✓

### Project expected:

| GIFI | Description | Amount |
|------|-------------|--------|
| 3500 | Common shares | 100 |
| 3600 | Retained earnings | 8,104 |
| 3620 | Total shareholder equity | 8,204 |

**Equity discrepancy:** $44,258 - $8,204 = **$36,054**

---

## 6. Balance Sheet Equation Test

### Attempt values:

```
Total Assets (2599)                    = 25,977
Total Liabilities (3499)               = 17,773
Total Shareholder Equity (3620)        = 44,258
Liabilities + Equity                   = 62,031

Balance test: 25,977 ≠ 62,031
Difference: 36,054
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

### From attempt:

| GIFI | Description | Amount |
|------|-------------|--------|
| 3660 | RE Start | 8,104 |
| 3680 | Net income | 36,054 |
| 3849 | RE End | 44,158 |

### Attempt rollforward:

```
RE End = RE Start + Net Income
       = 8,104 + 36,054
       = 44,158 ✓
```

**Note:** Attempt is internally consistent BUT uses wrong inputs.

### Project expected:

| GIFI | Description | Amount |
|------|-------------|--------|
| 3660 | RE Start | 16,656 |
| 3680 | Net income | 28,349 |
| 3700 | Dividends declared | 36,900 |
| 3740 | Rounding adjustment | -1 |
| 3849 | RE End | 8,104 |

### Project rollforward:

```
RE End = RE Start + Net Income - Dividends + Other
       = 16,656 + 28,349 - 36,900 - 1
       = 8,104 ✓
```

### Retained earnings discrepancies:

| Line | Attempt | Project | Difference | Issue |
|------|---------|---------|------------|-------|
| 3660 RE Start | 8,104 | 16,656 | -8,552 | Wrong value (used FY2025 ending instead of FY2024 ending) |
| 3680 Net income | 36,054 | 28,349 | +7,705 | Flows from Schedule 125 error |
| 3700 Dividends | (missing) | 36,900 | -36,900 | Not entered |
| 3740 Rounding | (missing) | -1 | -1 | Not entered |
| 3849 RE End | 44,158 | 8,104 | +36,054 | Result of above errors |

---

## 8. Summary of Root Cause Arithmetic

The $36,054 balance sheet imbalance can be traced as follows:

```
RE End (attempt)    = 44,158
RE End (correct)    = 8,104
Difference          = 36,054

Breakdown:
  Wrong RE Start:     8,104 - 16,656 = -8,552
  Wrong Net Income:  36,054 - 28,349 = +7,705
  Missing Dividends:      0 - 36,900 = -36,900
  Missing Rounding:       0 - (-1)   = +1

  Net effect on RE: -8,552 + 7,705 - (-36,900) - (-1)
                  = -8,552 + 7,705 + 36,900 + 1
                  = 36,054 ✓ (matches the imbalance)
```

---

## 9. 3640 Consistency Check

### Attempt:

| GIFI | Description | Amount |
|------|-------------|--------|
| 2599 | Total assets | 25,977 |
| 3499 | Total liabilities | 17,773 |
| 3620 | Total equity | 44,258 |
| 3640 | Total L+E | 62,031 |

**Check:** 3499 + 3620 = 17,773 + 44,258 = 62,031 = 3640 ✓

**Problem:** 3640 (62,031) ≠ 2599 (25,977)

### Project:

**Check:** 3499 + 3620 = 17,773 + 8,204 = 25,977 = 3640 = 2599 ✓

---

## Conclusion

All discrepancies trace to UFile entry errors:

1. **Manual entry on 9367** ($89,155 instead of auto-calculate) → wrong OpEx → wrong Net Income
2. **Duplicate expense entry** (9220 + 9225 both have $465) → overstated OpEx by $465 in UFile's calculation
3. **Wrong RE Start** (3660 = $8,104 instead of $16,656)
4. **Missing dividends** (3700 = $36,900 not entered)
5. **Missing rounding adjustment** (3740 = -$1 not entered)

The project-expected values are internally consistent and balance correctly.
