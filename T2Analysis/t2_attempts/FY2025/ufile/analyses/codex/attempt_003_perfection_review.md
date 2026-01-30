# FY2025 — UFile Attempt 3 “perfection” review

Source files:
- PDF: `taxattemps/FY2025/Attempt 3/2025 - 14587430 Canada Inc. - My copy - Tax return (2).pdf`
- Messages: `taxattemps/FY2025/Attempt 3/messages.txt`
- Parsed text: `T2Analysis/t2_attempts/FY2025/ufile/parses/attempt_003/text/`

## Status

Attempt 3 is **balanced** (no BCR/GIFI balance failures) and UFile says it can be filed electronically.

## Remaining warnings (and what to do)

### 1) “Taxable dividends paid in current yr; enter eligible dividends paid on the GRIP page.”

This warning is triggered because taxable dividends were paid and UFile wants the GRIP/eligible-dividend fields to be explicitly consistent.

Evidence in the exported return:
- Schedule 55 line 100 “Total taxable dividends paid in the tax year” shows **3,700**:
  - Parsed page: `T2Analysis/t2_attempts/FY2025/ufile/parses/attempt_003/text/pages/page_039.txt:27`
- Schedule 3 line 450 shows **3,700** taxable dividends paid to other than connected corporations:
  - Parsed page: `T2Analysis/t2_attempts/FY2025/ufile/parses/attempt_003/text/pages/page_033.txt:27`

Why this matters:
- The accounting packet for FY2025 currently has dividends declared (GIFI 3700) of **36,900**.
- The exported return’s retained earnings rollforward shows dividends declared of **36,900**:
  - Schedule 100 rollforward line `3700` shows **-36,900** in Attempt 3 (sign is presentation):
    - Parsed table: `T2Analysis/t2_attempts/FY2025/ufile/parses/attempt_003/tables/schedule_100.csv` (code `3700`)

This creates a **material inconsistency** unless it is intentional:
- “Dividends declared” (retained earnings) = **36,900**
- “Taxable dividends paid” (Schedule 3/55) = **3,700**

That combination is only “perfect” if the difference is tracked as **dividends payable** at year-end, which would normally appear as a liability. (It is not broken out explicitly in the Schedule 100 lines.)

Action needed (pick one and be consistent):
1) If dividends paid in FY2025 are actually **36,900**:
   - On the **Dividends paid** screen: set taxable dividends paid = **36,900** and eligible portion = **0**.
   - On the **GRIP** screen: ensure eligible dividends paid is **0** / GRIP is **0** (unless you are designating eligible dividends).
   - Re-export as Attempt 4 and re-parse to confirm Schedule 3/55 reflect 36,900.
2) If dividends paid in FY2025 are actually **3,700**:
   - Then the retained earnings rollforward “dividends declared” should likely not be **36,900** (or you need a clear dividends-payable presentation at year-end).
   - This would require reconciling to the accounting packet (outside UFile-only changes).

### 2) “Tax year presumed to be 365 days according to begin date of operations or incorporation date.”

This is typically informational. FY2025 is 2024-06-01 → 2025-05-31 (365 days). Confirm:
- Incorporation date is correct (2022-12-08).
- Beginning date of operations remains the historical start (2023-06-10), not something inside FY2025.

If those are correct, this warning is usually harmless.

### 3) “There is no entry in the income source section; all income is considered as active business income.”

For this corporation, treating income as active business income is expected. If you want the return to be maximally explicit, find the “income source” screen in UFile and select “active business income” (if it provides a selection).

### 4) “No instalments required … <= $3,000.”

Informational; no action.

## Notes (you said you haven’t written much yet)

Recommended minimal “Notes to financial statements” (paste-ready starter):
- Financial statements are management-prepared, unaudited, and prepared on an accrual basis at historical cost.
- Inventory is stated at cost. FY2025 closing inventory is based on a physical count near year-end; FY2024 closing inventory is an estimate based on available records.
- GST/HST registration became effective 2024-02-26; no GST/HST was collected prior to that date. Some Shopify reports may label pre-registration amounts as “tax”; these amounts are treated as sales/pricing, not GST/HST.

