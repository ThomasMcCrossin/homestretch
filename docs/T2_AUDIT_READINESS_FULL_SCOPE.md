# T2 Audit‑Readiness Review (Full‑Scope)
## 14587430 Canada Inc. (o/a Curly’s Canteen) — FY2024 & FY2025

**Date prepared:** 2026‑01‑26  
**Scope:** CRA/T2 filing readiness for fiscal years:
- **FY2024:** 2023‑06‑01 → 2024‑05‑31 (`manifest/sources.yml`)
- **FY2025:** 2024‑06‑01 → 2025‑05‑31 (`manifest/sources.yml`)

**Important limitations (read this first):**
- This is an internal, “audit‑style” critique of the numbers and supporting evidence inside this repo. It is **not** a formal audit/review engagement and **not** professional tax advice.
- This project is built around frozen reconciliation “facts”. Per `docs/STATUS.md`, nothing under `/home/clarencehub/Fresh/` or `/home/clarencehub/curlys-books/` should be modified as part of this work; any accounting fixes should be **new rows** (not edits) if/when they are made.

---

## 1) Executive Summary (Go/No‑Go)

### Go / No‑Go: **CONDITIONAL GO**
The mechanical pipeline is strong (bank coverage, deterministic imports, reproducible outputs). You are close. The remaining risk is concentrated in a handful of areas where CRA (or an accountant) would ask for explicit support or a management decision.

**Primary conditions to be comfortable filing:**
1. **Inventory**: confirm FY2024 estimate and FY2025 cutoff approach (count date ≠ year‑end) (`output/inventory_journal_summary.md`).
2. **Payroll completeness + shareholder compensation**: resolve/confirm whether shareholder‑labeled payroll items are truly payroll vs dividends; explain negative payroll liability balances (`output/payroll_summary.md`, `output/trial_balance_FY2024.csv`, `output/trial_balance_FY2025.csv`).
3. **HST bridge**: provide a clean bridge from ledger HST (GIFI 2680) to CRA (including “Non‑reporting period” items, interest/penalties, and timing/proration assumptions) (`output/hst_reconciliation_report.md`, `output/cra_hst_summary.md`, `output/cra_hst_period_summary.csv`).
4. **Shareholder balances presentation**: decide how to present net debit balances in “due‑to” accounts (reclass to due‑from, or explicitly explain why not) and confirm dividend documentation (board resolution / shareholder records) (`output/readiness_report.md`, `output/due_from_shareholder_breakdown.md`, `output/trial_balance_FY2025.csv`).
5. **Small gateway gaps (PayPal/manual/gift cards)**: decide how to represent these (asset / clearing / owner draw / immaterial exclusion) and document the policy (`output/shopify_gateway_totals_by_fy.csv`).

**Interpretation note (answers the “why do numbers look FY‑only?” confusion):**
- The FY reports are **year‑end snapshots**. Balance‑sheet accounts (cash, AP, HST payable, due‑to/due‑from shareholder, etc.) **roll forward**; income‑statement accounts (sales/expenses) **reset** each fiscal year.

---

## 2) What Looks Strong (audit‑friendly)

### A) Frozen source‑of‑truth and reproducibility
- Reconciliation work is captured as a **frozen snapshot** (hash‑verifiable) and imported into `db/t2_final.db` (`docs/STATUS.md`).
- Outputs are deterministic and traceable back to snapshot tables + override YAML.

### B) Bank coverage (hard requirement) is complete
- Bank transactions in scope: **1,357**; missing journalized bank lines: **0** (`output/readiness_report.md`).

### C) T2 schedule exports exist and are coherent
- Schedule 100 / 125 exports exist for both FYs (`output/gifi_schedule_100_FY2024.csv`, `output/gifi_schedule_125_FY2025.csv`, etc.).
- Net income matches Schedule 125 and the trial balances (`output/trial_balance_FY2024.csv`, `output/trial_balance_FY2025.csv`).

### D) Shopify payout math is internally consistent (fees not “double counted”)
- The repo explicitly treats Shopify payouts as **net-to-bank** and books fees separately; the arithmetic check passes (`output/shopify_gateway_vs_payouts_audit.md`).

---

## 3) Top‑Risk Findings (what could still blow up filing)

### 3.1 Inventory (COGS / gross margin sensitivity) — **CRITICAL**

**What we see**
- FY2024 closing inventory is explicitly an **estimate** (source file name includes “Estimated”) and FY2025 is based on a **count on 2025‑05‑16**, not on year‑end 2025‑05‑31 (`output/inventory_journal_summary.md`; source paths in `manifest/sources.yml`).
- Closing inventory increases materially: **$2,847** → **$10,015** (`output/inventory_journal_summary.md`).
- Gross margin moves materially: ~**42%** in FY2024 to ~**54%** in FY2025 (Schedule 125: `output/gifi_schedule_125_FY2024.csv`, `output/gifi_schedule_125_FY2025.csv`).

**Why an auditor/CRA reviewer cares**
- Inventory is the single biggest judgement lever in a merchandising business. Small changes move COGS, taxable income, and HST ITCs (if mis‑timed).
- A mid‑month count used for year‑end requires a **cutoff narrative** (purchases/sales between count and year‑end).

**What would make this “ready”**
- A short working paper that answers:
  - “Why is FY2024 inventory estimated; what was the basis?”
  - “Why is the FY2025 count date (May 16) appropriate for May 31? Were purchases between May 16‑31 material?”
  - “Valuation basis: cost / lower of cost & NRV; whether consistent year‑to‑year.”

---

### 3.2 Payroll completeness + liability signs — **HIGH**

**What we see**
- FY‑level payroll summary (exports + CRA + bank) shows meaningful “delta” signals (`output/payroll_summary.md`), and the trial balance payroll liability accounts are **debit balances** at year end:
  - FY2024: 2700/2710/2720 are net **debits** (prepaid/over‑remitted presentation) (`output/trial_balance_FY2024.csv`).
  - FY2025: 2700/2710/2720 are net **debits** (larger) (`output/trial_balance_FY2025.csv`).
- CRA remittances are being journalized and allocated across CPP/EI/Tax by ratios (`output/payroll_remittance_journal_summary.md`, `output/payroll_remittance_journal_detail.csv`).
- Overlapping months show big divergences between working papers vs employee exports in late 2024 (notably 2024‑11 and 2024‑12) (`output/payroll_summary.md` “Overlapping months” section).

**Why this matters**
- Debit balances in payroll liabilities are not “wrong”, but they are **unusual** and will be asked about. They are commonly caused by:
  - payroll exports incomplete (missing employees / pay periods),
  - incorrect accrual timing at year‑end,
  - remittances categorized incorrectly (bank items treated as payroll remits but actually vendor PADs; this repo already flags some) (`output/payroll_summary.md`).

**Specific high‑risk sub‑issue: shareholder compensation classification**
- There are bank overrides tagging specific payments as `SHAREHOLDER_PAYROLL` (`output/payroll_summary.md`).
- This is a tax‑sensitive classification: payroll vs dividend affects T4/T5 and CRA payroll account expectations.

**What would make this “ready”**
- Confirm a single “payroll source of truth” by month for FY2024 and FY2025 (employee exports vs monthly working papers vs backfill) and explicitly accept the choice.
- Ensure shareholder compensation is internally consistent (if dividend: keep dividend; if payroll: ensure payroll export / accrual exists and T4 support is expected).

---

### 3.3 Tips: policy changed year‑to‑year; bank must explain tips — **HIGH**

**Management representation (from you, not from the repo):**
- 2023: tips not explicitly paid (handled informally).
- Late 2024 (some Dec pay periods): tips were added into a taxable “gross/vacation” base and deductions were taken.
- 2025 pay periods: tips were paid **on top of net pay**, with **no deductions**.

**What the repo currently shows**
- The repo runs a tips vs bank audit and concludes **tips payable is $0** (no separate tips liability was needed) (`output/tips_payout_journal_summary.md`).
- Tip audits indicate that, depending on the export style, some tips behave like:
  - **TIPS_ADDED_PRE_DEDUCTIONS** (tips added into taxable pay, deductions taken), and/or
  - **TIPS_EMBEDDED_IN_GROSS** (tips already embedded in gross; tips column informational),
  - and for 2025 pay periods, tips appear as **net + tips** in the curlys-books backfill (paid on top of net) (`output/tips_vs_bank_audit.md`, `output/tips_vs_bank_audit_curlysbooks.csv`).

**Audit risk**
- If tips are truly paid out each pay period, the bank outflow (e‑transfers) should explain the tips amounts. If the repo shows tips but the bank doesn’t match “net + tips” where it should, then:
  - tips are being double‑counted or mis‑read, or
  - bank items are mis‑categorized / missing, or
  - tips were paid via non‑bank method.

**What would make this “ready”**
- For the 2025 pay periods where tips are “on top of net”, demonstrate that the payroll e‑transfer total equals **net + tips** (with timing tolerance).
- For the 2024 “tips inside taxable gross” periods, confirm exports reflect that (i.e., don’t add tips again on top of net).

---

### 3.4 GST/HST: ledger doesn’t tie cleanly to CRA at year‑end — **HIGH**

**What we see**
- Ledger net HST payable (GIFI 2680) vs CRA period-derived year-end model:
  - FY2024: ledger **$6,766.89** vs CRA model **$6,214.37** → **+$552.52** (ledger higher)
  - FY2025: ledger **$2,663.01** vs CRA model **$3,346.30** → **‑$683.29** (ledger lower)
  (`output/hst_reconciliation_report.md`, `output/hst_reconciliation_report.csv`)

**Important context**
- This repo uses a hard **ITC start date** of **2024‑02‑26** (HST registration/collection start), with:
  - Shopify sales tax journal entries credited to 2200 starting that date (`output/shopify_sales_tax_journal_summary.md`, `output/shopify_sales_tax_journal_detail.csv`)
  - an ITC start‑date adjustment that moves **$7,413.25** of pre‑start tax out of ITC and into expense (`output/itc_start_date_adjustment_summary.md`).
- Management representation (from you): Shopify’s “Taxes” amounts **before 2024‑02‑26** were not actually tax collected; they are **part of sales**. This repo’s approach (only crediting HST payable starting 2024‑02‑26) is consistent with that representation.

**“Non‑reporting period” payment**
- CRA export includes a **$2,000** payment labelled “Non‑reporting period” (an internal CRA staging bucket in the export).
- This repo explains that $2,000 as part of a combined shareholder reimbursement (bank e‑transfer `bank_txn_id=909` where the remainder is posted to HST payable as “HST paid by shareholder”) (`output/wave_reimbursement_remainder_analysis.md`, `docs/issue_hst_reimbursement_909.md`).

**Why this still needs a bridge**
- CRA exports include interest/penalties/administrative adjustments and quarter‑based postings; fiscal year ends mid‑quarter.
- Even if everything is “correct enough”, differences of ~$1k are large enough that you want a clean explanation ready.

**What would make this “ready”**
- A single bridge schedule:
  1) opening payable (if any),
  2) + tax collected per books (by month),
  3) − ITCs claimed per books (by month),
  4) ± CRA adjustments/interest/penalties (in‑scope),
  5) − payments (bank + shareholder‑paid),
  = closing payable.

---

### 3.5 Shareholder accounts: presentation + documentation risk — **HIGH**

**What we see at FY ends (Schedule 100 / TB)**
- FY2024: due‑to shareholders total **$2,368** (GIFI 2781) (`output/gifi_schedule_100_FY2024.csv`).
- FY2025: due‑to shareholders total **$1,026** (GIFI 2781) and due‑from shareholder **$2,041** (GIFI 1301) (`output/gifi_schedule_100_FY2025.csv`).
- Due‑from shareholder breakdown shows net **$2,041.36**, best‑effort attributed to **Thomas**, driven by:
  - bank debits posted to 2500: **$11,000**
  - bank inflows posted to 2500: **‑$9,000**
  - mileage/fuel adjustment: **+$41.36**
  (`output/due_from_shareholder_breakdown.md`)

**Why Dwayne’s large “draws” don’t automatically imply “due from shareholder”**
- If those withdrawals were treated as **dividends**, they are distributions of after‑tax profit (equity), not loans/receivables.
- “Due from shareholder” is used when the company has paid amounts that should be repaid (loan/advance) rather than declared as compensation/distribution.

**Presentation risk: debit balance in a due‑to account**
- If a “due‑to shareholder” account (2781) goes **debit**, it is normally presented as a **due‑from** (asset) unless you have a documented netting policy and legal right of offset.

**Documentation risk**
- The repo books FY2025 **dividends declared** of **$36,900** (account 3400) (`output/trial_balance_FY2025.csv`) and retained earnings rollforward reflects that (`output/gifi_retained_earnings_FY2025.csv`).
- If dividends are the intended treatment, keep:
  - a dividend declaration/resolution,
  - date/amount/recipient detail (shareholder working paper),
  - consistency vs bank outflows categorized as dividends.
- **Share capital**: Schedule 100 currently shows **no share capital balance** (i.e., effectively $0). If corporate records indicate issued share capital (even a nominal $100), decide whether to post it so the balance sheet presentation matches the legal/corporate reality.

---

## 4) Medium‑Risk Findings (should be consciously accepted)

### 4.1 Vendor profile splits are heuristic (sample is outside FY scope)
- Vendor profiles are derived from `curlys-books` receipts in **2025‑08 → 2026‑01** and applied to FY2024/FY2025 (`output/vendor_profiles.md`).
- This is acceptable as an estimation technique, but auditors will often test high‑spend vendors (Costco especially).

**Action:** either (a) accept as an estimate with disclosure in working papers, or (b) improve profiles using in‑period receipts if available.

### 4.2 “Pending Receipt – No ITC (9100)” is large enough to be questioned
- FY2024: **$3,748.64**; FY2025: **$3,508.12** (`output/trial_balance_FY2024.csv`, `output/trial_balance_FY2025.csv`).

**Risk:** unsupported expenses can be challenged as personal; no ITCs claimed reduces HST support questions but does not solve deductibility questions.

### 4.3 Major vendor invoice‑list completeness (GFS/Capital) is uneven
- GFS: 5 PAD payments missing invoice lists; 3 partial lists (including 2024‑02‑09 and 2024‑04‑05, which you have remittance detail for) (`output/major_vendors_gfs_capital_status.md`).
- Capital: 12 PAD payments missing invoice lists (`output/major_vendors_gfs_capital_status.md`).

**Risk:** not a “numbers don’t add” problem (bank is journalized), but a **supporting‑detail** problem (invoice‑level substantiation).

### 4.4 Credit‑card purchases: there’s a narrative mismatch to clean up
- The repo *does* post **credit card purchase journals** (2,079 posted; 139 skipped as matched to Wave bills) (`output/cc_purchase_journal_summary.md`).
- `output/readiness_report.md` still contains a statement that CC purchases are intentionally not journalized. Treat that as **stale narrative**, not a current design decision.

---

## 5) Low‑Risk / Mostly Clean Items

- Wave bill payment matching residuals are immaterial (net ~**$‑5.18**) (`output/readiness_report.md`).
- Fixed‑asset balances are **optional** depending on the book overlay mode:
  - **Option 2 (tax‑only):** no fixed‑asset balances on Schedule 100; CCA is assessed via the tax asset register (Schedule 8).
  - **Option 1 (book overlay):** fixed assets appear on Schedule 100 (e.g., 1740/1741) and book amortization appears on Schedule 125, while Schedule 8 remains the tax CCA source.
- AII / half‑year rule precedence (tax layer): if `half_year_rule` is false, no half‑year rule applies; if `half_year_rule` is true and `aii_eligible` is true with available‑for‑use between 2024‑01‑01 and 2027‑12‑31, the half‑year rule is suspended; otherwise the half‑year rule applies.
- Cash float logic is explicit and reconciles:
  - float withdrawals total **$2,624.50**
  - float returned via cash deposits **$2,324.50**
  - ending float target **$300**
  (`output/bank_inflow_journal_summary.md`, `output/bank_debit_journal_summary.md`, `output/cash_deposit_float_allocation.csv`)

---

## 6) Direct Answers to Your Specific Confusions

### 6.1 “What is ‘Due from shareholder’?”
It’s an **asset/receivable**: amounts the company expects a shareholder to repay (loan/advance/personal expenses paid by the company), unless explicitly reclassified as compensation or dividends.

In this repo, the due‑from balance is **$2,041.36** at FY2025 end, largely explained by **$11,000** of bank debits posted to 2500, partially offset by a **$9,000** bank inflow repayment, plus mileage netting (`output/due_from_shareholder_breakdown.md`).

### 6.2 “Dwayne had ~$34k draws; why would he owe it back?”
If those payments are booked as **dividends** (as this repo does for FY2025 in account 3400), they do not create a receivable.  
A shareholder would “owe it back” only if the payments were booked/treated as **loans/advances** rather than dividends/compensation.

### 6.3 “What does CRA mean by ‘Non‑reporting period’?”
In CRA account exports, “Non‑reporting period” commonly appears when a payment/credit is received but not applied to a filed reporting period yet (or is transferred between periods later). In this repo, it corresponds to a **$2,000** shareholder‑paid HST amount that is reimbursed/recognized in the GL as HST payable support (`output/wave_reimbursement_remainder_analysis.md`, `docs/issue_hst_reimbursement_909.md`).

### 6.4 “Why is there ‘cash’ outside the bank account?”
This repo deliberately carries an estimated **cash on hand / change float** at year‑end (target **$300**) and models cash withdrawals + later deposit “returns” so the float doesn’t artificially inflate income (`overrides/journalization_config.yml`, `output/bank_inflow_journal_summary.md`).

If your real float is typically $200‑$400 and you have no strict policy, $300 is a reasonable midpoint — but it should be treated as a **management estimate**.

### 6.5 “So how much is the bank over/under due to PayPal/cash?”
What the repo can support from the Shopify gateway export:
- PayPal gateway net payments are **$1,077.82** (FY2024) and **$570.18** (FY2025) (`output/shopify_gateway_totals_by_fy.csv`).
- Gateway exports also show small “manual” and “gift_card” totals (`output/shopify_gateway_totals_by_fy.csv`) which require policy:
  - **manual** is typically real receipts but may not be part of Shopify Payments payouts,
  - **gift_card** redemptions are **not revenue** at redemption (they reduce a gift card liability), but if you never booked gift card liability then it can look like “missing deposits”.
- There are no bank inflows explicitly identified as PayPal deposits (`output/bank_inflow_journal_summary.md`).

Therefore, unless those PayPal funds were withdrawn/cleared some other way (owner transfer, expenses, etc.), the “cash outside bank” could include **up to ~$1.6k** sitting in PayPal (asset) or otherwise removed from the business. This needs an explicit policy decision and documentation.

**Cash (POS) deposits vs Shopify cash gateway (sanity check):**
- The repo books cash sales via bank cash deposits (and separately reclasses a portion to HST payable). Because Shopify “net payments by gateway” is **transaction‑date** based and bank deposits are **deposit‑date** based, this won’t tie perfectly at fiscal cutoffs — but it is still a useful “shape” check.
- Using the repo’s recorded cash receipts (cash sales credited to revenue + cash portion of sales‑tax reclass) as a proxy for gross cash deposits:
  - **FY2024:** Shopify cash net **$71,585.06** vs proxy cash deposits **$70,301.45** → delta **$1,283.61** (`output/shopify_gateway_totals_by_fy.csv`, `output/trial_balance_FY2024.csv`, `output/shopify_sales_tax_journal_detail.csv`)
  - **FY2025:** Shopify cash net **$89,562.06** vs proxy cash deposits **$89,140.85** → delta **$421.21** (`output/shopify_gateway_totals_by_fy.csv`, `output/trial_balance_FY2025.csv`, `output/shopify_sales_tax_journal_detail.csv`)
- Those deltas are much more consistent with **timing/float/misc.** than with “missing tens of thousands”. If you want this nailed down, it becomes a formal cash‑to‑till reconciliation exercise (outside the scope of this memo).

---

## 7) Pre‑Journalization / Pre‑Filing Checklist (practical)

Treat this as a “sign‑off checklist” before you finalize journals/T2:

### Inventory
- Decide FY2024 inventory estimate basis (and document).
- Decide whether FY2025 May‑16 count is acceptable for May‑31 year‑end; if not, determine an adjustment approach.

### Payroll + tips
- Confirm shareholder compensation classification (payroll vs dividend) for the noted transactions (`output/payroll_summary.md`).
- Confirm tips policy by year matches how the exports are interpreted (2024 tips in taxable base vs 2025 tips on top of net).
- Reconcile why payroll liabilities show debit balances at year‑end (missing payroll exports vs timing vs classification).

### HST
- Prepare a one‑page bridge tying ledger HST payable to CRA (include shareholder‑paid/non‑reporting period, and identify any interest/penalties in‑scope).
- Confirm the chosen ITC policy pre‑2024‑02‑26 (this repo currently excludes all pre‑start ITCs and reclasses that tax to expense).

### Shareholders / equity
- Decide whether to book nominal share capital (if it exists in corporate records).
- Confirm dividend support (resolution and recipient breakdown).
- Decide presentation for any debit balance in a due‑to shareholder account (reclass to due‑from or explain netting).

### Expenses / receipts
- Decide how to treat “Pending Receipt – No ITC (9100)” in an audit narrative (attempt to recover receipts vs accept as unsupported expense vs personal add‑back).
- For GFS/Capital PAD invoice lists missing/partial, decide the level of invoice‑level substantiation you want before filing.

### Shopify gateways (PayPal/manual/gift cards)
- Decide whether to:
  - record PayPal as a separate cash account at year‑end, or
  - treat PayPal as withdrawn by shareholder (and document), or
  - treat as immaterial and exclude (not recommended unless explicitly accepted).

---

## 8) How to Run (CCA + Schedule 1)

Run order matters because Schedule 1 pulls from Schedule 8:
1) `python3 scripts/91b_build_cca_schedule_8.py`
2) `python3 scripts/91_build_t2_schedule_exports.py`
3) `python3 scripts/93_snapshot_project_state.py`
4) `python3 UfileToFill/ufile_packet/tools/build_packet_from_snapshot.py --snapshot output/snapshots/<stamp>`
5) `python3 UfileToFill/ufile_packet/tools/build_year_artifacts.py`

Inspect these outputs:
- `output/schedule_8_FY2024.csv`, `output/schedule_8_FY2025.csv`
- `output/cca_asset_register_resolved.csv` (audit trail, half‑year applied)
- `output/schedule_1_FY2024.csv`, `output/schedule_1_FY2025.csv`

---

## 9) Evidence Map (quick pointers)

If someone asks “where did that number come from?”, start here:
- Readiness snapshot: `output/readiness_report.md`
- Trial balances: `output/trial_balance_FY2024.csv`, `output/trial_balance_FY2025.csv`
- GIFI schedules: `output/gifi_schedule_100_FY2024.csv`, `output/gifi_schedule_125_FY2025.csv`
- Inventory: `output/inventory_journal_summary.md`
- Payroll: `output/payroll_summary.md`, `output/payroll_component_totals_by_fy.md`, `output/payroll_remittance_journal_detail.csv`
- Tips: `output/tips_vs_bank_audit.md`
- HST bridge: `output/hst_reconciliation_report.md`, `output/cra_hst_summary.md`
- Shareholder due‑from: `output/due_from_shareholder_breakdown.md`
- CC purchases: `output/cc_purchase_journal_summary.md`
- Major vendors (GFS/Capital): `output/major_vendors_gfs_capital_status.md`
