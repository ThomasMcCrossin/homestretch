# CRA/T2 Filing Readiness Review
## 14587430 Canada Inc. (o/a Curly's Canteen)
### Fiscal Years Ending May 31, 2024 (FY2024) and May 31, 2025 (FY2025)

> **Note (2026-01-27):** This document predates several fixes in this repo (notably the `2410` Dwayne CC prepay issue, tip audit wording, and the CRA HST year-end proration model). Use `output/readiness_report.md`, `output/hst_reconciliation_report.md`, `docs/issue_2410_dwayne_cc_prepay.md`, and `docs/issue_hst_reimbursement_909.md` as the current source of truth for balances and issue status.

**Review Date:** 2026-01-26
**Reviewer:** Claude (Audit-Style Review)
**Scope:** Full-scope T2 readiness assessment including HST, payroll, shareholders, GIFI schedules, and journal quality

---

## 1. Executive Summary (Key Findings)

1. **Bank coverage is complete**: 1,357 bank transactions journalized with zero gaps (`output/readiness_report.md:7-9`).
2. **Trial balances are mathematically balanced**: Both FY2024 and FY2025 produce coherent Schedules 100/125 that tie to the GL.
3. **Gross margin swing is material**: FY2024 ~42% vs FY2025 ~55% - driven by inventory increase ($2.8k to $10.0k) - requires cutoff/valuation support.
4. **HST payable does not tie to CRA at year-end**: FY2024 ledger overstates by $1,283; FY2025 understates by $979 (`output/hst_reconciliation_report.md:15-16`).
5. **$2,000 "Non-reporting period" HST payment** (bank txn 909) is properly journalized to HST payable but requires explanation for CRA reconciliation.
6. **Pre-2024-02-26 Shopify "Taxes" treated as sales** (not HST payable) - correct per owner context but should be documented.
7. **ITC start-date adjustment of $7,413.25** moved out of ITC account - appropriately reclassifies pre-registration tax to expense.
8. **Payroll liability accounts show debit (over-remitted) balances**: FY2024 $516 DR; FY2025 $1,964 DR - unusual and requires explanation.
9. **CRA payroll late penalties and interest exist**: Late remitting penalties assessed 2024-01-23 ($71.35), 2025-03-10 ($27.27), 2025-11-28 ($29.23 + $14.85) - not journalized as expense.
10. **Share capital ($100) is not posted** to GL despite SHAREHOLDER_INFORMATION.txt stating it exists.
11. **Dividends journalized = $36,900** but SHAREHOLDER_INFORMATION says draws = $37,900 (difference: $1,000 categorized as SHAREHOLDER_PAYROLL).
12. **Due-to-shareholder Dwayne shows $1,063 DR** (debit in a payable account) - should be reclassified to due-from-shareholder or offset.
13. **Vendor profile splits are heuristic-based**: Small sample sizes for Pharmasave (4 receipts) and Superstore (3 receipts) - material misclassification risk.
14. **"Pending Receipt - No ITC" (9100) balances**: $3,749 FY2024 / $3,508 FY2025 - requires receipt recovery or permanent add-back decision.
15. **Inventory FY2025 count is May 16, not May 31**: 15-day cutoff gap requires purchase/sale activity confirmation.
16. **PayPal gateway sales ($1,078 FY2024 / $570 FY2025)** - not deposited to bank, confirmed as expected "cash-like" flow but needs documentation.
17. **Meals & Entertainment add-back computed**: 50% of M&E flows to Schedule 1 correctly (`output/schedule_1_FY2024.csv:3`, `output/schedule_1_FY2025.csv:3`).
18. **Tips are treated as included in payroll e-transfers** - tips payable account is $0 (`output/tips_payout_journal_summary.md:9`).
19. **GFS invoice-level coverage is strong**: Zero missing Wave invoices for bank-linked EFT notices (`output/gfs_pad_invoice_mismatches_audit.md:9`).
20. **Capital Foodservice has 12 PAD payments missing invoice lists** - less rigorous than GFS but bank amounts are journalized.
21. **Rent expense cutoff error**: May 2024 rent ($350) is in FY2025 because invoice was dated June 30, 2024 - violates accrual accounting.

---

## 2. Go / No-Go Decision: CONDITIONAL GO

**Recommendation:** Proceed to final T2 filing **with conditions**.

### Rationale

The accounting framework is mechanically sound, deterministic, and well-documented. However, several items require explicit owner acknowledgment or working paper support before CRA submission:

| Category | Status | Blocking? |
|----------|--------|-----------|
| Bank coverage | Complete | No |
| Revenue recognition | Reasonable | No |
| COGS/inventory | Requires cutoff support | **Yes** (documentation) |
| HST reconciliation | Explainable differences | No (with working paper) |
| Payroll remittances | Complete (with late penalties) | No |
| Shareholder accounts | Presentation issues | **Yes** (re-class decision) |
| GIFI mapping | Coherent | No |
| Share capital | Missing from GL | **Yes** (decision required) |

### Conditions for Final Filing

1. Owner must confirm FY2025 inventory count timing is acceptable (May 16 count for May 31 year-end)
2. Owner must decide on Dwayne's $1,063 DR balance presentation (reclass to due-from or offset)
3. Owner must confirm whether to post $100 share capital to account 3000
4. CRA late penalties/interest should be journalized or explicitly excluded
5. Rent cutoff adjustment required: accrue $350 May 2024 rent into FY2024 (currently in FY2025)

---

## 3. Critical Blockers (Ranked)

### CRITICAL-1: Inventory Cutoff and Valuation (Affects Schedule 125 COGS)
**Severity:** CRITICAL
**Schedules Affected:** Schedule 125, Schedule 100 (inventory asset)
**Evidence:** `manifest/sources.yml:76-80`, `output/inventory_journal_summary.md:4-7`

**Issue:**
- FY2024 inventory is an estimate. In this repo, FY2024 is now backed by a repo-local estimate sheet derived from the FY2025 physical-count item list:
  - `data/inventory/Canteen Inventory May 31 2024 - Estimate from FY2025 Items.csv`
  - generator audit: `output/inventory_estimate_fy2024_from_fy2025_audit.csv`
- FY2025 inventory count date is **May 16, 2025** but year-end is **May 31, 2025**
- Inventory increased from $2,847 to $10,015 (+$7,168), representing 65% of gross margin improvement
- No documented valuation method (FIFO/average cost) or cutoff adjustment

**Why It Matters:**
- Gross margin swing (42% to 55%) is auditor red-flag territory
- Without cutoff documentation, CRA could challenge COGS timing
- Material inventory estimation could constitute misstatement

**Recommendation:**
- Document that FY2024 was estimated and why
- Confirm no material purchases/sales between May 16-31, 2025 (or compute adjustment)
- Record valuation basis (cost, lower of cost/NRV)
- Keep count sheets/photos as support

---

### CRITICAL-2: Shareholder Account Presentation - Dwayne DR Balance (Affects Schedule 100)
**Severity:** CRITICAL
**Schedules Affected:** Schedule 100 (GIFI 2781/1301)
**Evidence:** `output/trial_balance_FY2025.csv:12`, `output/readiness_report.md:28`

**Issue:**
- Account 2410 "Due to Shareholder - Dwayne" has a **$1,062.85 DR** balance at FY2025 year-end
- A debit balance in a payable account means the shareholder owes the corporation, not vice versa
- This should be presented as GIFI 1301 (Due from shareholder), not GIFI 2781 (Due to shareholder)
- Current GIFI mapping shows net $1,026 CR for 2781 - masking the underlying DR balance

**Why It Matters:**
- Improper netting of shareholder balances is a common CRA inquiry point
- Creates risk of s.15(1) shareholder benefit questions if not properly presented
- Balance sheet presentation would be misleading to third parties

**Recommendation:**
- Reclassify 2410 DR balance to 2500 (Due from shareholder), OR
- Net against Thomas's due-to balance with explicit offset journal entry
- Document the choice in working papers

---

### CRITICAL-3: Share Capital Not Posted (Affects Schedule 100)
**Severity:** CRITICAL
**Schedules Affected:** Schedule 100 (GIFI 3500)
**Evidence:** `output/gifi_schedule_100_FY2024.csv` (missing GIFI 3500), SHAREHOLDER_INFORMATION.txt:27

**Issue:**
- SHAREHOLDER_INFORMATION.txt states: "Share Capital: $100.00" with 100 shares issued
- GL account 3000 (Common Shares) shows $0 balance in both years
- Schedule 100 has no GIFI 3500 (Common Shares) line

**Why It Matters:**
- Corporation cannot legally have zero share capital if shares are issued
- CRA T2 requires share structure disclosure
- Omission could trigger inquiry about incorporation status

**Recommendation:**
- Post journal entry: DR 1000 Cash $100 / CR 3000 Common Shares $100 (dated June 1, 2023)
- Alternatively, if paid-up capital was via services, document the contribution structure
- Must appear on Schedule 100

---

## 4. High-Priority Issues

### HIGH-1: HST Reconciliation Differences
**Severity:** HIGH
**Schedules Affected:** GST/HST Return, Schedule 100 (GIFI 2680)
**Evidence:** `output/hst_reconciliation_report.md:13-16`, `output/cra_hst_period_summary.csv`

**Issue:**
| FY | Ledger HST Payable | CRA Estimate | Difference |
|----|-------------------|--------------|------------|
| FY2024 | $6,756.83 | $5,473.77 | +$1,283.06 (overstated) |
| FY2025 | $2,251.44 | $3,230.72 | -$979.28 (understated) |

**Components:**
- $2,000 "Non-reporting period" payment (bank txn 909) is journalized as shareholder reimbursement for HST paid - posted to 2200
- Pre-ITC-start-date adjustment ($7,413.25) correctly moves tax to expense

**Why It Matters:**
- Auditors will expect a line-by-line HST reconciliation
- Differences of $1,000+ require explanation
- "Non-reporting period" CRA label may confuse reviewers

**Recommendation:**
- Prepare HST bridge working paper showing: returns filed + payments made + adjustments = payable
- Document that $2,000 was Thomas paying HST on behalf of corp before formal registration
- Differences may relate to timing (CRA quarters vs fiscal year-end) - document this

---

### HIGH-2: Payroll Liability Debit Balances (Over-Remitted)
**Severity:** HIGH
**Schedules Affected:** Schedule 100 (GIFI 2620)
**Evidence:** `output/trial_balance_FY2024.csv:12-14`, `output/trial_balance_FY2025.csv:14-16`

**Issue:**
| Account | FY2024 Balance | FY2025 Balance |
|---------|---------------|----------------|
| 2700 CPP | $258.68 DR | $1,180.00 DR |
| 2710 EI | $11.60 DR | $427.72 DR |
| 2720 Tax | $246.07 DR | $356.26 DR |
| **Net** | **$516.35 DR** | **$1,963.98 DR** |

**Why It Matters:**
- Debit balances in payroll liability accounts suggest over-remittance to CRA
- Could indicate: (a) remittance timing mismatch, (b) payroll accrual issues, or (c) misclassification
- Auditors expect payable balances at year-end, not prepaid

**Recommendation:**
- Verify payroll period-end cutoff (are May payroll liabilities properly accrued?)
- If genuinely over-remitted, reclassify to prepaid (GIFI 1484) or leave with explanation
- Cross-check with CRA payroll account balance

---

### HIGH-3: CRA Penalties and Interest Not Journalized
**Severity:** HIGH
**Schedules Affected:** Schedule 125 (expenses)
**Evidence:** `output/payroll_cra_account_matches.csv:5,22-24,34-35`

**Issue:**
- CRA assessed late remitting penalties totaling approximately $100+ across both FYs
- Interest charges also assessed on arrears
- These amounts are visible in CRA export but not journalized as expense

**Documented Penalties:**
- 2024-01-23: Late remitting penalty $71.35
- 2025-03-10: Penalty $27.27, Interest $0.04
- 2025-11-28: Penalties $29.23 + $14.85

**Why It Matters:**
- Penalties and interest are real costs that reduce retained earnings
- CRA will see these on their records; books should match
- GIFI 8710 (Interest and bank charges) should include CRA interest

**Recommendation:**
- Journal entry to record penalties (GIFI 9270 or separate penalty account) and interest (GIFI 8710)
- Alternatively, explicitly document as immaterial and excluded

---

### HIGH-4: Vendor Profile Sample Sizes Are Small
**Severity:** HIGH
**Schedules Affected:** Schedule 125 (COGS vs operating expenses)
**Evidence:** `output/vendor_profiles.md:61-62,82-83`

**Issue:**
- Costco profile: 16 receipts (reasonable)
- Pharmasave profile: 4 receipts with warning "sample size < 10 receipts (treat as heuristic)"
- Atlantic Superstore profile: 3 receipts with same warning
- Walmart/Canadian Tire: Manual override (no sample backing)

**FY Impact:**
| Vendor | FY2024 Total | FY2025 Total |
|--------|-------------|-------------|
| Costco | ~$36,600 | ~$36,700 |
| Pharmasave | ~$2,200 | ~$3,100 |
| Superstore | ~$3,700 | ~$12,300 |
| Walmart | ~$1,500 | ~$1,200 |

**Why It Matters:**
- Heuristic splits could materially misclassify COGS vs. supplies vs. personal
- Superstore spend increased 3x in FY2025 - higher exposure to misclassification
- "Pending Receipt - No ITC" allocations from Costco profile are ~9.5% of spend

**Recommendation:**
- Accept as reasonable estimates with explicit acknowledgment
- If material receipts are available, refine profiles for FY2025
- Document that profiles are heuristics, not deterministic

---

### HIGH-5: Rent Expense Cutoff Error (May 2024 Rent in FY2025)
**Severity:** HIGH
**Schedules Affected:** Schedule 125 (Rent expense), Schedule 100 (Retained earnings)
**Evidence:** `data/wave/wave_bills_final.csv` (bill 323), `output/trial_balance_FY2024.csv:54`, `output/trial_balance_FY2025.csv:60`

**Issue:**
- Bill 323 dated **2024-06-30** is described as "Juen May Rent" — covering both May and June 2024
- The entire bill ($700 net + $105 HST = $805) is allocated to **FY2025** based on invoice_date
- However, **May 2024 rent** ($350 net portion) relates to **FY2024** (period ending May 31, 2024)
- This violates accrual accounting: expense should be recognized in the period it relates to, not when billed

**Financial Impact:**
| Item | Current | Correct | Adjustment |
|------|---------|---------|------------|
| FY2024 Rent (6100) | $7,885.00 | $8,235.00 | **+$350.00** |
| FY2025 Rent (6100) | $7,486.98 | $7,136.98 | **-$350.00** |
| FY2024 Net Income | $18,098 | $17,748 | -$350 |
| FY2025 Net Income | $35,568 | $35,918 | +$350 |

**Why It Matters:**
- Rent is a straightforward, easily verifiable expense — cutoff errors here suggest systemic issues
- Understates FY2024 expenses and overstates FY2025 expenses
- Auditors routinely test rent cutoff as a standard procedure
- The system is using invoice_date for expense recognition (closer to cash-basis than accrual-basis)

**Recommendation:**
- Post year-end accrual journal entry for FY2024:
  ```
  DR  6100 Rent Expense       $350.00
  DR  2210 HST ITC            $ 45.65
  CR  2000 Accounts Payable   $395.65
  Memo: Accrue May 2024 rent (billed June 30, 2024)
  ```
- Alternatively, split bill 323 so May portion is dated 2024-05-31 and June portion is dated 2024-06-30
- Review other multi-period bills for similar cutoff issues (e.g., bill 324 "July/August Rent" is correctly in FY2025)

---

## 5. Medium-Priority Issues

### MEDIUM-1: $1,000 Thomas Payment Classified as Payroll Instead of Dividend
**Severity:** MEDIUM
**Schedules Affected:** Payroll expense, Schedule 100 (retained earnings)
**Evidence:** `overrides/bank_txn_category_overrides.yml:39-41`, bank txn 676

**Issue:**
- Bank txn 676 (2025-01-08, $1,000) was overridden from OWNER_DRAW to SHAREHOLDER_PAYROLL
- Override note: "rounds out $4,000 net payroll split"
- SHAREHOLDER_INFORMATION.txt shows this as part of Thomas's $3,900 draws
- Ledger shows dividends = $36,900 but SHAREHOLDER_INFORMATION says total draws = $37,900

**Why It Matters:**
- Payroll vs. dividend has different tax treatment for both corp and shareholder
- T4 vs. T5 reporting implications
- Should be internally consistent

**Recommendation:**
- Confirm with owner: was this truly payroll (Thomas had worked hours) or a dividend mislabeled?
- If dividend, adjust override to DIVIDEND and rerun

---

### MEDIUM-2: "Pending Receipt - No ITC" Account Balances
**Severity:** MEDIUM
**Schedules Affected:** Schedule 125 (Other expenses), ITC claims
**Evidence:** `output/trial_balance_FY2024.csv:71`, `output/trial_balance_FY2025.csv:79`

**Issue:**
- Account 9100: FY2024 $3,748.64, FY2025 $3,508.12
- This represents purchases where receipts were not available and no ITC was claimed
- Includes ~9.5% of Costco vendor profile allocations

**Why It Matters:**
- Amounts without receipts could be challenged as personal expenses
- No ITC claim on $7,256 of purchases means ~$1,088 of potential unclaimed ITCs
- CRA may request substantiation for GIFI 9270 (Other expenses) amounts

**Recommendation:**
- Attempt to recover receipts where possible
- For unrecoverable: document as accepted loss and confirm no personal element
- Consider whether 50% add-back (like M&E) is appropriate for meal-like items

---

### MEDIUM-3: PayPal Funds Not Deposited in Bank
**Severity:** MEDIUM
**Schedules Affected:** Cash reconciliation
**Evidence:** `output/shopify_gateway_totals_by_fy.csv:4,9`

**Issue:**
- FY2024: PayPal net $1,077.82 (43 transactions)
- FY2025: PayPal net $570.18 (23 transactions)
- These funds appear in Shopify gateway reports but not in bank deposits

**Why It Matters:**
- Creates apparent "missing cash" if reviewer expects all sales to hit bank
- PayPal balance not shown as asset on balance sheet
- Owner context says "PayPal funds weren't deposited in-bank" - should be documented

**Recommendation:**
- Confirm PayPal funds were used for personal or withdrawn separately
- If still in PayPal at year-end, record as asset
- Document in working papers as expected variance

---

### MEDIUM-4: Capital Foodservice Invoice Detail Coverage Is Incomplete
**Severity:** MEDIUM
**Schedules Affected:** AP reconciliation
**Evidence:** `output/major_vendors_gfs_capital_status.md:88-104`

**Issue:**
- 12 of 20 Capital PAD payments have no captured invoice lists
- Only 7 Capital invoices linked to Wave bills (vs 105 for GFS)
- Total Capital exposure: $23,326 in Wave bills, $18,021 via PAD

**Why It Matters:**
- Less audit trail for Capital than for GFS
- Cannot reconcile invoice-to-payment at same level of detail
- Risk of missed invoices or duplicate payments

**Recommendation:**
- Accept as reasonable given bank amounts match Wave totals
- If Capital remittance advices are available, import for completeness
- Document as "bank-statement-level reconciliation" for Capital

---

### MEDIUM-5: Fuel Account 9200 Has Immaterial FY2024 Balance
**Severity:** MEDIUM
**Schedules Affected:** Vehicle expenses
**Evidence:** `output/trial_balance_FY2024.csv:72`

**Issue:**
- Account 9200 "Fuel Pending Mileage Conversion - No ITC" shows $77.68 in FY2024
- This account is supposed to be cleared by mileage conversion
- FY2025 shows $0 (properly converted)

**Why It Matters:**
- Suggests FY2024 mileage calculation may have had a small residual
- Could indicate timing difference in mileage log vs fuel bills

**Recommendation:**
- Confirm if $77.68 residual is acceptable or should be reclassified
- May be immaterial and acceptable as-is

---

## 6. Low-Priority Issues

### LOW-1: Four Unmatched GFS EFT Notices (Early FY2024)
**Severity:** LOW
**Evidence:** `output/gfs_pad_invoice_mismatches_audit.md:21-24`

**Issue:**
- Four GFS notices from June-August 2023 have no matching bank PAD debit
- Total: ~$1,945
- These may have been paid cash or via alternate method

**Recommendation:**
- Likely cash-paid per owner context; document and accept

---

### LOW-2: Wave Bill Payment Matching Residuals Are Immaterial
**Severity:** LOW
**Evidence:** `output/readiness_report.md:34-40`

**Issue:**
- 2 mismatches totaling -$5.18 (bank $916.69 vs bills $921.87)
- Largest single mismatch: $5.28

**Recommendation:**
- Immaterial; no action required

---

### LOW-3: Retained Earnings Schedule 3740 Shows "Rounding" Adjustment
**Severity:** LOW
**Evidence:** `output/gifi_retained_earnings_FY2025.csv:4`

**Issue:**
- Line 3740 "Other items affecting retained earnings (rounding)" = -$36,901
- This is actually the dividends ($36,900) plus rounding

**Recommendation:**
- Rename line description to "Dividends declared" for clarity
- Current GIFI code mapping is acceptable but confusing

---

## 7. Schedule-by-Schedule Checklist

### Schedule 100 (Balance Sheet)

| GIFI | Account | FY2024 | FY2025 | Status |
|------|---------|--------|--------|--------|
| 1001 | Cash | $26,292 | $12,472 | OK - ties to bank + float |
| 1120 | Inventory | $2,847 | $10,015 | **Needs cutoff support** |
| 1301 | Due from shareholder | $0 | $2,041 | OK |
| 2620 | A/P and accrued liabilities | $1,916 | $4,485 | OK (includes payroll DR) |
| 2680 | Taxes payable | $6,757 | $2,251 | **Reconciliation needed** |
| 2781 | Due to shareholder | $2,368 | $1,026 | **Dwayne DR issue** |
| 3500 | Share capital | $0 | $0 | **MISSING - add $100** |
| 3600 | Retained earnings | $18,098 | $16,766 | OK |

### Schedule 125 (Income Statement)

| GIFI | Description | FY2024 | FY2025 | Status |
|------|-------------|--------|--------|--------|
| 8000 | Trade sales | $181,235 | $230,907 | OK |
| 8518 | Cost of sales | $104,748 | $105,286 | Inventory-dependent |
| 8710 | Interest/bank charges | $2,290 | $6,347 | **Add CRA interest** |
| 8911 | Real estate rental | $7,885 | $7,487 | **Cutoff: +$350 to FY2024** |
| 9060 | Salaries and wages | $22,888 | $49,321 | OK |
| 9270 | Other expenses | $3,749 | $3,508 | Contains No-ITC items |
| 9281 | Vehicle expenses | $3,948 | $3,510 | OK |

### Schedule 1 (Net Income Reconciliation)

| Line | FY2024 | FY2025 | Status |
|------|--------|--------|--------|
| 300 Net income per F/S | $18,098 | $35,569 | OK |
| 117 50% M&E add-back | $259 | $204 | OK |
| 400 Net income for tax | $18,357 | $35,773 | OK |

---

## 8. Questions for Owner (Auditor-Style)

### Inventory
1. Was a physical count performed for FY2024 year-end, or is "Estimated" the final position?
2. For FY2025: what purchases were made between May 16-31, and were they material?
3. What valuation method is used (cost, lower of cost/NRV, FIFO, average)?

### HST/Tax
4. Confirm: before 2024-02-26, Shopify "Taxes" were pricing semantics, not HST collected?
5. The $2,000 HST payment by Thomas (bank txn 909) - was this for pre-registration period or a specific quarter?
6. Should CRA late penalties (~$140 total) be journalized, or treated as immaterial?

### Shareholders
7. Should Dwayne's $1,063 DR balance be reclassified to due-from-shareholder?
8. Was share capital of $100 contributed at incorporation? If so, can we post it?
9. Confirm: the $1,000 Thomas payment on 2025-01-08 was payroll (not dividend)?

### Cash/PayPal
10. PayPal funds (~$1,600 over 2 years) were not deposited - confirm they were used personally or withdrawn?
11. Is the $300 year-end cash float accurate? Any cash spent from till (expenses/reimbursements)?

### Receipts/Expenses
12. For "Pending Receipt - No ITC" balances (~$7,250 over 2 years) - are receipts recoverable?
13. Can you provide count sheets or photos for inventory support?

### Rent
14. Bill 323 dated June 30, 2024 covers "May + June Rent" — confirm May 2024 rent should be accrued into FY2024?
15. Why do some months show half-rent ($350/$402.50) vs full-rent ($750/$765.22)? Is this a seasonal or shared arrangement?

---

## 9. Appendix: Key Balances and Deltas

### Revenue Comparison

| Metric | FY2024 | FY2025 | Delta | % Change |
|--------|--------|--------|-------|----------|
| Total Revenue (GIFI 8000) | $181,235 | $230,907 | +$49,672 | +27.4% |
| Shopify Net Sales | $114,419 | $151,676 | +$37,257 | +32.6% |
| Cash Deposit Sales | $66,971 | $80,379 | +$13,408 | +20.0% |

*Evidence: `output/trial_balance_FY2024.csv:15-17`, `output/trial_balance_FY2025.csv:19-22`*

### Cost and Margin Comparison

| Metric | FY2024 | FY2025 | Delta | Notes |
|--------|--------|--------|-------|-------|
| COGS (GIFI 8518) | $104,748 | $105,286 | +$538 | Near-flat despite 27% revenue growth |
| Gross Profit | $76,487 | $125,621 | +$49,134 | |
| Gross Margin % | 42.2% | 54.4% | +12.2 ppt | **Requires explanation** |
| Opening Inventory | $0* | $2,847 | | *First year |
| Closing Inventory | $2,847 | $10,015 | +$7,168 | +252% |

*Evidence: `output/gifi_schedule_125_FY2024.csv:4-5`, `output/gifi_schedule_125_FY2025.csv:4-5`*

### Operating Expenses Comparison

| Category | FY2024 | FY2025 | Delta | Notes |
|----------|--------|--------|-------|-------|
| Wages (9060) | $22,888 | $49,321 | +$26,433 | +115% (staffing increase) |
| Employer taxes (8622) | $1,460 | $3,179 | +$1,719 | Proportional to wages |
| Rent (8911) | $7,885 | $7,487 | -$398 | **Cutoff error: should be $8,235 / $7,137** |
| Office/supplies (8810) | $10,481 | $11,608 | +$1,127 | |
| Interest/fees (8710) | $2,290 | $6,347 | +$4,057 | Merchant fees increase |

*Evidence: `output/gifi_schedule_125_FY2024.csv`, `output/gifi_schedule_125_FY2025.csv`*

### Balance Sheet Movement

| Account | FY2024 End | FY2025 End | Delta |
|---------|-----------|-----------|-------|
| Cash (1001) | $26,292 | $12,472 | -$13,820 |
| Inventory (1120) | $2,847 | $10,015 | +$7,168 |
| Due from SH (1301) | $0 | $2,041 | +$2,041 |
| A/P (2620) | $1,916 | $4,485 | +$2,569 |
| HST payable (2680) | $6,757 | $2,251 | -$4,506 |
| Due to SH (2781) | $2,368 | $1,026 | -$1,342 |
| Retained earnings | $18,098 | $16,766 | -$1,332 |

*Note: RE decreased due to $36,900 dividends exceeding $35,569 net income*

### HST Flow Summary

| Item | FY2024 | FY2025 | Evidence |
|------|--------|--------|----------|
| Shopify tax collected | $9,060 | $24,023 | `output/shopify_sales_tax_journal_detail.csv` |
| ITC claimed (2210 balance) | $2,303 | $11,261 | `output/trial_balance_*.csv` |
| ITC pre-start adjustment | $7,413 | $0 | `output/itc_start_date_adjustment_detail.csv` |
| Net HST payable (ledger) | $6,757 | $2,251 | `output/hst_reconciliation_report.csv` |
| Net HST payable (CRA est.) | $5,474 | $3,231 | `output/cra_hst_summary.md` |

---

## 10. Key File References

| Purpose | File Path |
|---------|-----------|
| Trial Balance FY2024 | `output/trial_balance_FY2024.csv` |
| Trial Balance FY2025 | `output/trial_balance_FY2025.csv` |
| Schedule 100 FY2024 | `output/gifi_schedule_100_FY2024.csv` |
| Schedule 100 FY2025 | `output/gifi_schedule_100_FY2025.csv` |
| Schedule 125 FY2024 | `output/gifi_schedule_125_FY2024.csv` |
| Schedule 125 FY2025 | `output/gifi_schedule_125_FY2025.csv` |
| HST Reconciliation | `output/hst_reconciliation_report.md` |
| Payroll Summary | `output/payroll_summary.md` |
| Shareholder Info | `curlys-books/t2-filing-fy2024-fy2025/output/SHAREHOLDER_INFORMATION.txt` |
| Inventory Journals | `output/inventory_journal_summary.md` |
| Vendor Profiles | `output/vendor_profiles.md` |
| Bank Override Config | `overrides/bank_txn_category_overrides.yml` |
| ITC Start Date Config | `overrides/journalization_config.yml:32` |

---

*End of Review*
