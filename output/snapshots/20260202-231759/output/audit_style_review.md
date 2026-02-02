# Audit-style review (internal) — FY2024 & FY2025

This is an “audit-style” critique of the accounting outputs in this repo. It is **not** an audit or review engagement and does not replace professional judgement. Conclusions are based only on the data and reports available inside this project (bank/Wave/CRA/Shopify/mileage sources).

Interpretation note:
- The FY sections are **year-end snapshots**. Balance sheet accounts (cash, AP, shareholder balances, HST payable, etc.) **roll forward**; income statement accounts reset per FY.

## 1) Executive snapshot (reasonableness)

**FY2024 (2023-06-01 → 2024-05-31)**
- Sales (GIFI 8000): **$181,235** (`output/gifi_schedule_125_FY2024.csv`)
- COGS (GIFI 8518): **$104,748** → gross margin ~**42%**
- Net income: **$17,771** (`output/readiness_report.md`)
- Cash (1000+1070): **$26,292**; Inventory: **$2,847** (`output/readiness_report.md:16`, `output/inventory_journal_summary.md:6`)
- HST payable (ledger): **$6,767** vs CRA model **$6,214** (diff **+$553**) (`output/hst_reconciliation_report.md`)

**FY2025 (2024-06-01 → 2025-05-31)**
- Sales (GIFI 8000): **$230,907** (`output/gifi_schedule_125_FY2025.csv`)
- COGS (GIFI 8518): **$105,286** → gross margin ~**54%**
- Net income: **$35,285** (`output/readiness_report.md`)
- Dividends paid (bank-driven): **$36,900** (account 3400; reduces retained earnings) (`output/trial_balance_FY2025.csv:19`)
- Cash (1000+1070): **$12,472**; Inventory: **$10,015** (`output/readiness_report.md:25`, `output/inventory_journal_summary.md:7`)
- HST payable (ledger): **$2,663** vs CRA model **$3,346** (diff **-$683**) (`output/hst_reconciliation_report.md`)

Overall, the sales/Shopify reconciliation shape is plausible and internally consistent (gross sales built from payout components; sales tax reclass removes HST from revenue), but there are several **audit-risk** items where the numbers may be directionally right while still lacking support or containing structural issues.

## 2) Strengths (what an auditor would like)

- **Deterministic build + audit trail**: outputs are reproducible from a frozen snapshot + override YAMLs; this supports auditability.
- **Bank line coverage**: debit-side bank transactions are fully journalized (no missing bank lines in scope) (`output/readiness_report.md:7`).
- **Wave → GL traceability**: expenses flow from Wave bills with explicit allocation rows (including tax/ITC lines), plus a separate shareholder reimbursement reclass layer.
- **Shopify fee and sales math checks**: payout-derived charges/refunds/fees are arithmetically consistent and cross-checked against gateway exports (`output/shopify_gateway_vs_payouts_audit.md`).

## 3) High-risk / likely-to-be-queried areas

### A) Inventory is the single biggest judgement lever (COGS/gross margin)
- FY2024 ending inventory is explicitly an **estimate**; FY2025 inventory count is **not exactly at year-end** (count date 2025-05-16, year-end 2025-05-31) (`output/inventory_journal_summary.md`).
- Gross margin jumps from ~42% → ~55%. That can happen operationally, but it’s also consistent with **inventory valuation/cutoff** (closing inventory increased materially: $2.8k → $10.0k).
- Auditor expectation: documented count sheets, valuation basis (FIFO/avg), and cutoff explanation for purchases/sales between count date and year-end.

### B) GST/HST payable does not tie to CRA as-of-year-end
- FY2024: ledger shows **$553** more payable than the CRA period-derived model; FY2025: ledger shows **$683** less (`output/hst_reconciliation_report.md`).
- The system uses a deliberate ITC start date and a sales-tax reclass from revenue; that’s coherent, but differences of this size would still be examined.
- Bank_txn `909` is a combined reimbursement: **$3,000** e-transfer to Thomas where **$1,000** matches Wave bills and the remaining **$2,000** is posted to HST payable as “HST paid by shareholder (reimbursed)” (`output/wave_reimbursement_remainder_analysis.md:34`).
- CRA labels the related $2,000 payment as **“Non-reporting period”** on 2024-10-22 (the payment appears to sit in a non-reporting bucket before being transferred to a reporting period). This is usually a *presentation/timing* artifact in CRA exports, not inherently suspicious.
- Auditor expectation: a line-by-line bridge from CRA account transactions to GL HST payable at year-end (including how “Non-reporting period” items are treated).

### C) Shareholder accounts presentation and evidence
- FY2025 has both:
  - `2500` Due from shareholder: **$2,041 DR** (Thomas loan $2,000 + mileage/fuel net $41) (`output/due_from_shareholder_breakdown.md`)
  - `2410` Due to shareholder – Dwayne: **$1,607 CR** (mileage + meals net payable) (`output/readiness_report.md`)
- Dividends: FY2025 bank distributions were reclassified as **dividends paid** (not owner draws). That’s reasonable for a corporation, but auditors will require: dividend resolution, shareholder register consistency, and downstream slips (T5) if applicable.

### D) Payroll liabilities and tips payable structure
- Payroll remittances are allocated across CPP/EI/Tax based on payroll data; the approach is deterministic, but the year-end payroll liability accounts show **debit balances** (i.e., “over-remitted” vs accrual) rather than payable balances:
  - FY2024: 2700/2710/2720 net DR ≈ **$516**
  - FY2025: 2700/2710/2720 net DR ≈ **$1,964**
- Tips payable (`2310`) is **$0**; employee-export tips are treated as payroll-paid (either explicitly added into net pay, or already included in gross pay), supported by `output/tips_vs_bank_audit.md:3`.
- Tips paid “on top of net pay” in early 2025 are treated as part of **net pay payable** (cleared by payroll e-transfers), supported by `output/tips_vs_bank_audit_curlysbooks.csv`.
- Auditor expectation: confirm tip policy and payroll export semantics (employee exports appear to mix “TIPS_ADDED_PRE_DEDUCTIONS” and “TIPS_EMBEDDED_IN_GROSS” representations).

## 4) Medium-risk / “review for classification” areas

- **Vendor profile splits** (Costco/Pharmasave/Superstore/Walmart) are heuristic (sample-based) and can misclassify COGS vs supplies vs personal; auditors will sample high-dollar vendors and request receipts.
- **Pending Receipt / No ITC (9100)** is material enough to draw questions (~$3.7k FY2024, ~$3.5k FY2025); auditors may treat this as higher personal/unsupported risk.
- **Meals estimate with no receipts** is booked as M&E with a 50% add-back. CRA could still deny if unsupported; keep it clearly labeled as an estimate (`output/shareholder_meals_estimate_summary.md` + `output/schedule_1_FY*.csv`).

## 5) Low-risk / “looks clean” items

- Wave bill payment matching residuals are immaterial (net **-$5.18**) (`output/readiness_report.md:34`).
- GFS EFT notice vs invoice coverage looks complete for bank-linked notices; remaining unmatched notices are explicitly listed (`output/gfs_pad_invoice_mismatches_audit.md`).

## 6) Specific “does this make sense?” comments

- Cash-on-hand (`1070`) is treated as an estimated **year-end float** (currently **$300**) and is cleared back to bank via allocating portions of cash deposits as “return of float” (`output/cash_deposit_float_allocation.csv`, `output/bank_inflow_journal_summary.md:20`).
- Sales growth FY2024 → FY2025 (~+$50.6k) is plausible. Gross margin improvement is plausible but is the #1 area to validate because it is highly sensitive to **inventory + classification**.
- Wage expense roughly doubles (from ~$23k to ~$50k); that often tracks staffing changes. Confirm payroll completeness vs CRA export (already partially tied via remittance model).
- Interest/bank charges (GIFI 8710) are higher in FY2025; if card usage increased or processing fees increased, this makes sense.

## 7) Auditor-style “requests for support” (what to gather before filing)

1. Inventory support: count sheet methodology, cutoff notes, valuation method, and why 2025-05-16 is appropriate for 2025-05-31.
2. HST reconciliation: explain the FY-end differences and the treatment of bank_txn 909 / CRA “Non-reporting period” items; confirm CRA account shows the same payments.
3. Share capital: shareholder document says **$100** share capital, but the ledger shows none posted; decide whether to post and how (and ensure Schedule 100 reflects it).
4. Shareholder balances: decide presentation (netting vs separate due-to/due-from) and confirm dividends/resolutions.
5. Payroll: explain negative year-end payroll liability balances; confirm tips treatment is correct and supported (tips payable should be $0 if tips are fully paid via payroll e-transfers).
6. Completeness on card-funded purchases: if Wave bills are the expense source-of-truth, confirm that all card purchases were captured as Wave bills (spot-check card payment months).

## 8) Where to look (key project reports)

- Readiness summary: `output/readiness_report.md`
- Trial balances: `output/trial_balance_FY2024.csv`, `output/trial_balance_FY2025.csv`
- GIFI schedules: `output/gifi_schedule_100_FY2024.csv`, `output/gifi_schedule_125_FY2025.csv` (etc.)
- HST bridge: `output/hst_reconciliation_report.md`
- Shareholder receivable: `output/due_from_shareholder_breakdown.md`
- Wave reimbursement remainder analysis: `output/wave_reimbursement_remainder_analysis.md`
- Inventory journals: `output/inventory_journal_summary.md`
