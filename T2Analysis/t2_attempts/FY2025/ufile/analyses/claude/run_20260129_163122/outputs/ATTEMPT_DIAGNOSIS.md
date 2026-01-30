# FY2025 UFile T2 Attempt Diagnosis

**Analyst:** Claude (Opus 4.5)
**Run Directory:** `T2Analysis/t2_attempts/FY2025/ufile/analyses/claude/run_20260129_163122/`
**Generated:** 2026-01-29

---

## Executive Summary

The FY2025 UFile attempt failed validation due to **UFile entry mechanics errors (Category A)**. The project-expected values are internally consistent and balance correctly; the problems arise entirely from how data was entered into UFile.

### Key Findings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| Balance sheet imbalance | $36,054 | Retained earnings mis-entered: wrong RE Start, missing dividends |
| Operating expense mismatch | $8,170 | Manual entry on 9367 instead of auto-calculation |
| Duplicate expense line | $465 | Both 9220 and 9225 populated (should only be 9225) |

### Conclusion

**Category A: UFile entry mechanics / UFile auto-calculation behavior**

No project number errors were identified. All discrepancies trace to UFile data entry mistakes.

---

## Evidence Index

| File | Description | Location |
|------|-------------|----------|
| meta.json | Parse metadata | inputs/meta.json |
| verification_report.md | Parse validation (50/50 OK) | inputs/verification_report.md |
| diagnostics.csv | Parsed diagnostic messages | inputs/diagnostics.csv |
| schedule_100.csv | Parsed balance sheet | inputs/schedule_100.csv |
| schedule_125.csv | Parsed income statement | inputs/schedule_125.csv |
| retained_earnings.csv | Parsed RE schedule | inputs/retained_earnings.csv |
| packet_fy2025.json | Project expected values | inputs/packet_fy2025.json |
| UFILet2_FILL_GUIDE.md | Entry instructions | inputs/UFILet2_FILL_GUIDE.md |

**Parse Verification:** All 50 parsed codes verified against source PDF text (100% OK).

---

## Diagnostics List

### Blocking (Prevent e-file)

1. **GIFI-FIELD 9367 subtotal mismatch**
   - Attempt: $89,155 | UFile calc: $97,325 | Diff: $8,170
   - *Cause:* Manual entry on total line instead of letting UFile auto-calculate

2. **Balance sheet does not balance**
   - 2599 (Total assets): $25,977
   - 3499 + 3620: $17,773 + $44,258 = $62,031
   - Difference: $36,054
   - *Cause:* Retained earnings overstated due to entry errors

### Non-Blocking (Warnings)

3. **Federal e-file ineligibility** — Downstream effect of blocking errors
4. **Missing INCOMESOURCE entry** — Informational; defaults correctly

---

## Extracted Schedule Tables

### Schedule 100 — Balance Sheet (Attempt)

| GIFI | Description | Attempt | Project | Delta |
|------|-------------|---------|---------|-------|
| 1001 | Cash | 12,472 | 12,472 | 0 |
| 1121 | Inventory | 10,015 | 10,015 | 0 |
| 1301 | Due from shareholder | 2,000 | 2,000 | 0 |
| 1484 | Prepaid expenses | 1,490 | 1,490 | 0 |
| **2599** | **Total assets** | **25,977** | **25,977** | **0** |
| 2620 | AP and accrued liabilities | 10,013 | 10,013 | 0 |
| 2680 | Taxes payable | 2,663 | 2,663 | 0 |
| 2781 | Due to shareholders | 5,097 | 5,097 | 0 |
| **3499** | **Total liabilities** | **17,773** | **17,773** | **0** |
| 3500 | Common shares | 100 | 100 | 0 |
| 3600 | Retained earnings | 44,158 | 8,104 | **+36,054** |
| **3620** | **Total equity** | **44,258** | **8,204** | **+36,054** |
| **3640** | **Total L+E** | **62,031** | **25,977** | **+36,054** |

**Observation:** Assets match; liabilities match; equity is overstated by $36,054.

### Retained Earnings (Attempt vs Project)

| GIFI | Description | Attempt | Project | Delta |
|------|-------------|---------|---------|-------|
| 3660 | RE Start | 8,104 | 16,656 | **-8,552** |
| 3680 | Net income | 36,054 | 28,349 | **+7,705** |
| 3700 | Dividends | — | 36,900 | **-36,900** |
| 3740 | Rounding | — | -1 | **-1** |
| 3849 | RE End | 44,158 | 8,104 | **+36,054** |

**Observation:** RE Start is wrong, dividends are missing, net income is wrong.

### Schedule 125 — Income Statement (Attempt)

| GIFI | Description | Attempt | Project | Delta |
|------|-------------|---------|---------|-------|
| 8000 | Trade sales | 230,907 | 230,907 | 0 |
| 8299 | Total revenue | 230,907 | 230,907 | 0 |
| 8300 | Opening inventory | 2,847 | 2,847 | 0 |
| 8320 | Purchases | 112,866 | 112,866 | 0 |
| 8500 | Closing inventory | (10,015) | (10,015) | 0 |
| 8518 | Cost of sales | 105,698 | 105,698 | 0 |
| 8519 | Gross profit | 125,209 | 125,209 | 0 |
| 8520 | Advertising | 798 | 798 | 0 |
| 8523 | Meals & entertainment | 408 | 408 | 0 |
| 8622 | Employee benefits | 3,610 | 3,610 | 0 |
| 8690 | Insurance | 1,951 | 1,951 | 0 |
| 8710 | Interest & bank | 6,694 | 6,694 | 0 |
| 8810 | Office expenses | 3,903 | 3,903 | 0 |
| 8813 | Data processing | 1,878 | 1,878 | 0 |
| 8860 | Professional fees | 353 | 353 | 0 |
| 8911 | Real estate rental | 7,137 | 7,137 | 0 |
| 8960 | Repairs & maintenance | 981 | 981 | 0 |
| 9060 | Salaries & wages | 54,899 | 54,899 | 0 |
| 9130 | Supplies | 5,348 | 5,348 | 0 |
| 9131 | Small tools | 479 | 479 | 0 |
| 9220 | Utilities | **465** | **0** | **+465** |
| 9225 | Telephone | 465 | 465 | 0 |
| 9270 | Other expenses | 3,782 | 3,782 | 0 |
| 9275 | Delivery/freight | 136 | 136 | 0 |
| 9281 | Vehicle expenses | 4,038 | 4,038 | 0 |
| **9367** | **Total OpEx** | **89,155** | **96,860** | **-7,705** |
| **9368** | **Total expenses** | **194,853** | **202,558** | **-7,705** |
| **9999** | **Net income** | **36,054** | **28,349** | **+7,705** |

**Observations:**
1. Revenue and COGS lines match perfectly
2. Expense detail lines match except for 9220 (duplicate entry)
3. Total operating expenses (9367) was manually entered as $89,155 instead of auto-calculated
4. The manual $89,155 is $7,705 less than the correct $96,860

---

## Recalculations (Show Your Work)

### Operating Expenses Sum (from attempt detail lines)

```
  798 + 408 + 3,610 + 1,951 + 6,694 + 3,903 + 1,878 + 353
+ 7,137 + 981 + 54,899 + 5,348 + 479 + 465 + 465 + 3,782 + 136 + 4,038
= 97,325  (UFile's internal calculation)
```

**Note:** This includes the duplicate $465 in 9220.

Correct sum (without 9220 duplicate):
```
97,325 - 465 = 96,860  (matches project)
```

### COGS Verification

```
COGS = Opening (8300) + Purchases (8320) - Closing (8500)
     = 2,847 + 112,866 - 10,015
     = 105,698 ✓
```

### Net Income (correct)

```
Net Income = Revenue - Total Expenses
           = 230,907 - (105,698 + 96,860)
           = 230,907 - 202,558
           = 28,349 ✓
```

### Retained Earnings (correct)

```
RE End = RE Start + Net Income - Dividends + Rounding
       = 16,656 + 28,349 - 36,900 - 1
       = 8,104 ✓
```

### Balance Sheet (correct)

```
Total Assets          = 25,977
Total Liabilities     = 17,773
Total Equity          = 100 + 8,104 = 8,204
L + E                 = 17,773 + 8,204 = 25,977 ✓
```

---

## Hypothesis Testing

### H1: Totals line populated but internal subtotal mismatch (9367)

**Test:** Compare attempt's 9367 manual entry to sum of detail lines.
- Attempt 9367 = $89,155 (manual entry)
- Sum of detail lines = $97,325

**Result:** CONFIRMED. User manually entered $89,155 instead of letting UFile auto-calculate.

### H2: Project double-count or omission

**Test:** Verify project operating expense sum.
```
Project 9367 = 96,860
Sum of project expense lines (excluding 9220) = 96,860 ✓
```

**Result:** NOT CONFIRMED. Project numbers are internally consistent.

### H3: Wrong UFile line choice (detail vs total)

**Test:** Check if user entered both detail and total lines.

**Result:** CONFIRMED.
- User entered all detail expense lines (8520, 8523, ... 9281)
- User ALSO manually entered 9367 = $89,155
- This is explicitly warned against in the Fill Guide

### H4: Retained earnings mismatch from missing dividends

**Test:** Check if dividends (3700) were entered.
- Attempt: No 3700 line found in parsed retained_earnings.csv
- Project expects: 3700 = $36,900

**Result:** CONFIRMED. Dividends were not entered.

### H5: Wrong RE Start value

**Test:** Compare attempt 3660 to FY2024 ending RE.
- Attempt 3660 = $8,104
- FY2024 ending RE (from packet.json) = $16,656
- FY2025 ending RE (correct) = $8,104

**Result:** CONFIRMED. User entered FY2025 ending RE as the starting value (transposition error).

### H6: Duplicate expense classification

**Test:** Check for expenses entered on multiple lines.
- 9220 (Utilities) = $465
- 9225 (Telephone/telecommunications) = $465
- Project only expects 9225 = $465; no 9220

**Result:** CONFIRMED. Same $465 entered on both lines (duplicate).

---

## Final Conclusion

### Root Cause Classification: **A — UFile Entry Mechanics**

All discrepancies trace to data entry errors in UFile, not to problems with the underlying project numbers. The project packet values are internally consistent, balance correctly, and reconcile to source documents.

### Specific Entry Errors Identified

| # | Error | Impact |
|---|-------|--------|
| 1 | Manual entry on 9367 ($89,155) instead of letting UFile auto-calculate | Under-reported OpEx by $7,705 → overstated Net Income |
| 2 | Duplicate entry: 9220 AND 9225 both = $465 | Added $465 to UFile's internal OpEx sum |
| 3 | Wrong RE Start (3660): entered $8,104 instead of $16,656 | RE Start understated by $8,552 |
| 4 | Missing dividends (3700): $36,900 not entered | RE End overstated |
| 5 | Missing rounding (3740): -$1 not entered | Minor (offsetting other items) |

### Net Effect on Retained Earnings

```
Impact = -8,552 (wrong start) + 7,705 (inflated NI) + 36,900 (missing div) + 1 (rounding)
       = +36,054 (matches balance sheet imbalance)
```

---

## Fix Checklists

### UFile UI Next Attempt (Required)

| Priority | Action | UFile Location |
|----------|--------|----------------|
| 1 | **Clear manual entry on 9367** — Delete any value typed in "Total operating expenses" and let UFile auto-calculate | Schedule 125 / GIFI screen |
| 2 | **Remove 9220 (Utilities)** — Delete the $465 entry; keep only 9225 (Telephone) = $465 | Schedule 125 / GIFI screen |
| 3 | **Correct 3660 (RE Start)** — Change from $8,104 to **$16,656** | Schedule 100 / Retained Earnings section |
| 4 | **Enter 3700 (Dividends)** — Add **$36,900** as dividends declared | Retained Earnings / Dividends screen |
| 5 | **Enter 3740 (Other adjustments)** — Add **-$1** rounding adjustment | Retained Earnings section |
| 6 | **Recalculate** — After corrections, recalculate to verify diagnostics clear | UFile menu |

### Verification Steps After Corrections

- [ ] 2599 (Total assets) = 3640 (Total L+E) = $25,977
- [ ] 3620 (Total equity) = $8,204
- [ ] 3849 (RE End) = $8,104
- [ ] 9367 auto-calculated = $96,860
- [ ] 9999 (Net income) = $28,349
- [ ] No blocking diagnostics remain

### Project Outputs Fix Checklist

**None required.** Project values are correct. No changes to packet.json or source data are needed.

---

## Appendix: Key Values Reference

### Correct Values for Re-Entry

| Field | GIFI | Correct Value |
|-------|------|---------------|
| RE Start | 3660 | 16,656 |
| Net Income | 3680 | 28,349 (auto from Schedule 125) |
| Dividends | 3700 | 36,900 |
| Rounding | 3740 | -1 |
| RE End | 3849 | 8,104 (auto-calculated) |
| Total OpEx | 9367 | 96,860 (auto-calculated) |
| Total Expenses | 9368 | 202,558 (auto-calculated) |
| Net Income | 9999 | 28,349 (auto-calculated) |

### Fill Guide Reference

The Fill Guide (`UFILet2_FILL_GUIDE.md`) explicitly warns:
> "If you see diagnostics like 'GIFI-FIELD 9367 does not match internal subtotal calculation': you typed 9367 manually; clear it and let UFile compute it from the expense lines."

And for totals:
> "Leave totals like 1599/2599/3499/3640 blank; UFile usually auto-calculates them."
