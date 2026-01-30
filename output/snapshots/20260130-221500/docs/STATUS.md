# Status (t2-final-fy2024-fy2025)

This file is written to prevent confusion when multiple attempts/projects exist.

## Hard guardrails

- **Do not modify** anything under `/home/clarencehub/Fresh/` or `/home/clarencehub/curlys-books/` as part of T2-final work.
- Treat the “reconciliation work” as **frozen facts** via a snapshot folder with a sha256 manifest.
- Any “fixes” must be recorded as **new rows** (allocations/classifications/journal entries), not edits to imported facts.

## Canonical inputs in this project

### 1) Frozen reconciliation-as-data (Fresher snapshot)

Current snapshot:
- Snapshot manifest: `/home/clarencehub/t2-final-fy2024-fy2025/data/fresher_snapshots/20260122-054642/snapshot_manifest.yml`
- Debits DB: `/home/clarencehub/t2-final-fy2024-fy2025/data/fresher_snapshots/20260122-054642/db/canteen_reconciliation_v2.db`
- Credits DB: `/home/clarencehub/t2-final-fy2024-fy2025/data/fresher_snapshots/20260122-054642/db/credits_reconciliation.db`

Verification:
- `python3 scripts/41_verify_snapshot_manifest.py` (checks sha256 for every file listed)
- `python3 scripts/01_verify_manifest.py` (checks `manifest/sources.yml` hashes)

What this snapshot contains:
- Copied DBs (exact end-state at snapshot time)
- CSV exports of every table in both DBs
- Copied Fresher overrides
- Copied Fresher debit-side reports (`output/latest`, `output/audits`)
- Copied Fresher credit-side reports (`credits/output`)

### 2) CRA exports (authoritative, read-only)

Stored as hashed sources in `manifest/sources.yml` (paths under `/home/clarencehub/Fresh/CanteenCRAAsOfDec0625/`):
- `CanteenHST.csv` (GST/HST account transactions)
- `CanteenPayrollTransactions.csv` (payroll account transactions)
- `CanteenArrearsTransactions.csv` (arrears/penalties/interest)

## What is already implemented in t2-final

### A) Project skeleton + manifest

- Root: `/home/clarencehub/t2-final-fy2024-fy2025/`
- Manifest: `manifest/sources.yml` (paths + sha256 + semantics)

### B) “Everything we did” captured as data

- Fresher snapshot script: `scripts/40_snapshot_fresher_state.py`
- Snapshot verify script: `scripts/41_verify_snapshot_manifest.py`

This is the primary answer to: “did we lose work due to random scripts/patches?”

### C) Reconciled Wave bills imported from the snapshot (includes manual work)

- Importer: `scripts/11_import_wave_bills_from_fresher_snapshot.py`
- Imported count (FY2024+FY2025 scope): **754** `wave_bills` rows.
  - Use `--all` to import the full snapshot (currently **759** rows, includes a few FY2026-ish bills like sponsorships).
- Export as a standalone CSV (optional, for humans): `python3 scripts/12_export_wave_bills_final_csv.py`
  - Output: `/home/clarencehub/t2-final-fy2024-fy2025/data/wave/wave_bills_final.csv`
  - Default filter: only rows within FY2024+FY2025 date range (use `--all` to export everything in the snapshot DB)

### D) Vendor allocation profiles (estimated splits) for mixed vendors

Derived from `curlys-books` receipt line items (corp entity):
- Costco
- Pharmasave
- Atlantic Superstore
- Walmart (manual override profile)

Notes:
- Manual overrides live in `overrides/vendor_profile_rules.yml` under `manual_vendor_profiles`.
- When both exist, `scripts/30_apply_vendor_profiles_to_wave_bills.py` prefers `MANUAL_OVERRIDE` over `CURB_PG_SAMPLE`.
- Sample-derived profile filters live in `overrides/vendor_profile_rules.yml` under `profile_filters` (example: exclude `9900` personal; exclude Superstore `6550` delivery for FY2024/FY2025 work).

Outputs:
- `output/vendor_profiles.md` (shows sample size + date range; sample is small and labeled heuristic)
- `output/vendor_allocations_by_fy.csv` (per-bill allocations, includes HST ITC line when tax exists)
- `output/vendor_allocations_summary_by_fy.csv` (FY totals by account_code)

Bills affected:
- **271** Wave bills (COSTCO 65, PHARMASAVE 112, ATLANTIC_SUPERSTORE 61, WALMART 33).

### E) Full Fresher reconciliation tables mirrored into `t2_final.db`

To avoid re-running Fresher scripts and to keep “everything we did” queryable from one SQLite file, we import
all snapshot-exported tables into `t2_final.db` under clear prefixes:
- `fresher_debits__*` (from `tables/debits/*.csv`)
- `fresher_credits__*` (from `tables/credits/*.csv`)

Import command:
- `python3 scripts/13_import_fresher_snapshot_tables.py --verify-files`

#### Important: CC payment linkage overrides (FIFO)

There is an optional-but-useful deterministic override that increases the evidence that bank credit-card payments
are paying down Wave bills (without editing imported facts, only inserting clearly-labeled new rows):

- `python3 scripts/79_import_cc_payment_fifo_allocations.py --reset`
  - Inserts `fresher_debits__bank_allocations` rows with `notes` starting `FIFO_CC_CHAIN_OVERRIDE`.
  - Source inputs are frozen audit CSVs inside the Fresher snapshot (`dryrun_fifo_cc_payment_*`).

**Caveat:** `scripts/13_import_fresher_snapshot_tables.py` drops/recreates all `fresher_*__*` tables, so if you
re-import the snapshot tables you must re-run the FIFO import afterwards.

### F) Line-level allocations for every Wave bill (account-coded)

Goal: every Wave bill in-scope has deterministic account allocations (including tax), so we can build a TB without guessing.

Implemented:
- Vendor-profile-based splits (Costco/Pharmasave/Superstore/Walmart): `scripts/30_apply_vendor_profiles_to_wave_bills.py`
- Import allocations from the (optional) Fresher/categories pipeline: `scripts/14_import_bill_allocations_from_fresher_categories.py`
- Override/backfill allocations from invoice PDFs for key vendors (GFS + Capital): `scripts/15_import_bill_allocations_from_invoice_pdfs.py`
  - Mapping file: `overrides/invoice_pdf_mappings.yml`

Notes:
- `bill_allocations` sums to `wave_bills.total_cents` (because tax is allocated to the HST ITC account, default `2210`), not `net_cents`.
- SOT document-line coverage is currently complete (0 missing): `sot/output/document_line_coverage_summary.md`

### G) Shareholder adjustments posted as journal entries (no manual SQL)

Mileage + fuel (fuel assumed Thomas-paid; Dwayne has no fuel offset):
- Builder: `scripts/60_build_shareholder_mileage_payables.py`
- Outputs: `output/shareholder_mileage_fuel_summary.md`, `output/shareholder_mileage_fuel_journal_FY2024.csv`, `output/shareholder_mileage_fuel_journal_FY2025.csv`
- Posted to: `journal_entries` / `journal_entry_lines` in `db/t2_final.db`

Meals estimate (Moncton trips; no receipts; 50% add-back policy):
- Builder: `scripts/61_build_shareholder_meals_estimate.py`
- Outputs: `output/shareholder_meals_estimate_summary.md`, `output/shareholder_meals_estimate_journal_FY2024.csv`, `output/shareholder_meals_estimate_journal_FY2025.csv`
- Posted to: `journal_entries` / `journal_entry_lines` in `db/t2_final.db`

### H) CRA exports imported + summarized

Import:
- `python3 scripts/62_import_cra_exports.py --reset`

HST summary (supports year-end HST payable + remittance deltas):
- `python3 scripts/63_build_cra_hst_summary.py`
- Output: `output/cra_hst_summary.md` and `output/cra_hst_period_summary.csv`

### I) Payroll exports imported + summarized

Import:
- `python3 scripts/64_import_payroll_exports.py --reset`

Payroll summary (supports FY wage totals + payroll remittance reconciliation + year-end source deductions payable):
- `python3 scripts/65_build_payroll_summary.py`
- Output: `output/payroll_summary.md`
- Output tables (CSV):
  - `output/payroll_monthly_ledger.csv` (unified month ledger + bank-paid deltas)
  - `output/payroll_cra_account_matches.csv` (CRA payroll account export matched to bank by date_received+amount, incl. grouped matches)
  - `output/payroll_remittance_vs_cra_by_month.csv` (working paper remittance vs CRA `Payment <Month> <Year>`)

Key findings so far:
- FY2025 source deductions payable at 2025-05-31 is **$257.17** (CRA shows `Payment May 2025` received 2025-06-04).
- Early payroll remittances were often paid by a shareholder and reimbursed (bank category `PAYROLL_REIMBURSE`).
- A subset of bank txns categorized `PAYROLL_REMIT` are actually Pepsico PADs / GPFS service charges (flagged as unmatched vs CRA in `output/payroll_summary.md`).
- Added hashed 2024 employee payroll exports from `/home/clarencehub/Fresh/dump/2024Canteen/` to `manifest/sources.yml` (including non-standard header variants).
- Employee-level payroll imports now capture `tips_cents` (schema: `db/migrations/006_payroll_employee_tips.sql`; importer: `scripts/64_import_payroll_exports.py`).
- Use the “Overlapping months” section in `output/payroll_summary.md` to spot where employee exports diverge from monthly working papers (some months differ materially and need a conscious choice before final journals).

### J) Payroll journals posted (accrual)

- Builder: `python3 scripts/72_build_payroll_journals.py --reset`
- Outputs: `output/payroll_journal_summary.md`, `output/payroll_journal_detail.csv`
- Posted to: `journal_entries` / `journal_entry_lines` in `db/t2_final.db`
- Note: this posts payroll expenses + liabilities from exports; remittance/bank clearing entries are still pending.

### K) Payroll remittance journals posted (clearing)

- Builder: `python3 scripts/73_build_payroll_remittance_journals.py --reset`
- Outputs: `output/payroll_remittance_journal_summary.md`, `output/payroll_remittance_journal_detail.csv`
- Posted to: `journal_entries` / `journal_entry_lines` in `db/t2_final.db`
- Note: CRA `Payment <Month> <Year>` credits are allocated across CPP/EI/Tax by monthly ratios; reimbursements clear due-to-shareholder.

## GFS note (why reports can look “wrong”)

The Fresher credit-side GFS report `gfs_invoices_missing_wave.csv` was generated on 2026-01-16 and can be **stale** relative to the later Fresher DB state (snapshot on 2026-01-22).

From `credits/output/gfs_coverage_summary.json` (frozen in the snapshot):
- `bank_pad_debits_total=68` and `bank_pad_debits_unmatched=0` (all bank PAD debits in scope are linked)
- `notifications_total=74` and `notifications_unmatched=4` (four early notices have no matching bank PAD debit)

The four unmatched notices are:
- 2023-06-09
- 2023-06-23
- 2023-06-30
- 2023-08-25

These are “unmatched” because there is no corresponding bank PAD debit for those EFT notice totals (they may have been paid by cash/other method).

## T2 schedule exports (implemented)

- CRA-aligned GIFI code overrides:
  - `python3 scripts/52_apply_gifi_code_overrides.py`
  - Outputs: `output/gifi_code_overrides_applied.md`, `output/gifi_code_overrides_applied.csv`
- UFile-style exports (Schedule 100/125 + retained earnings + Schedule 1):
  - `python3 scripts/91_build_t2_schedule_exports.py`
  - Outputs: `output/ufile_gifi_<FY>.csv`, `output/gifi_schedule_100_<FY>.csv`, `output/gifi_schedule_125_<FY>.csv`, `output/gifi_retained_earnings_<FY>.csv`, `output/schedule_1_<FY>.csv`

## What is NOT implemented yet (remaining)

- Any remaining “conscious choice” items called out in `output/readiness_report.md` (e.g., optional shareholder reclasses, small Wave match mismatches).
