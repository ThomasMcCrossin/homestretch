# SOT Status (FY2024–FY2025 T2)

This is the current status of the **new, ground-up SOT DB** under `sot/`.

## What exists now

### Schema
- `sot/migrations/001_init.sql` defines the SOT schema (facts + reconciliation layer + settlements + accounting tables).

### Import + canonicalization scripts
- `sot/scripts/10_import_from_t2_final_db.py`
  - Imports **read-only** from `../db/t2_final.db` into `sot/db/*.db`.
  - Writes `sot/output/import_summary.md`.
- `sot/scripts/20_build_canonical_allocations.py`
  - Builds `txn_document_allocations.role='CANONICAL'` for bank txns in FY2024–FY2025.
  - Never invents new amounts; it only re-encodes existing settlement/detail links into consistent allocation rows.
- `sot/scripts/21_report_bank_coverage.py`
  - Writes `sot/output/bank_canonical_coverage_summary.md`
  - Writes `sot/output/bank_canonical_needs_review.csv`
- `sot/scripts/30_list_wave_vendor_dates.py`
  - Lets you list Wave bill dates for specific vendors (used for tracking down physical receipts).

## Latest outputs produced

### Import summary
See: `sot/output/import_summary.md`

Known issue discovered during import:
- (none currently surfaced by the importer warnings)

### Bank coverage report
See: `sot/output/bank_canonical_coverage_summary.md`

Interpretation notes:
- “`unexplained: 0`” means *every bank txn had at least one* settlement link, cc payment link, or classification — it does **not** mean everything is clean/CRA-ready.
- The “partial remainder” list is the actionable review queue (duplicates, mixed-purpose e-transfers, etc.).

### Vendor dates for physical receipt lookup
See: `sot/output/wave_vendor_dates_canadiantire_dollarama_wholesaleclub.csv`
- This output already surfaced a real problem: some vendors have duplicate Wave bills (e.g., identical Canadian Tire gas bills) which leads to double-allocation unless corrected as a data decision.

## What’s still needed for T2 filing

### 1) Categorization / chart of accounts
The SOT DB has `document_lines` and `chart_of_accounts`, and we have started populating them:
- `sot/scripts/31_import_chart_of_accounts.py` imports the curlys-books chart-of-accounts export.
- `sot/scripts/32_import_bill_allocations_as_document_lines.py` imports vendor-profile allocations (for a subset of Wave bills).
- `sot/scripts/33_apply_vendor_profile_overrides.py` applies explicit manual profiles (currently Walmart + Canadian Tire).
- `sot/scripts/34_build_default_account_rollups.py` creates a small “Wave-style” rollup layer for reporting.

Current gap:
- Many documents still have **no** `document_lines` (see `sot/output/document_line_coverage_summary.md`).

### 2) Tax cross-checks (HST / payroll)
Next step is to compare:
- Wave tax captured in bills
vs
- CRA filing exports (HST + payroll remits)

This should be done as a report and then represented as explicit documents/allocations (no silent plugs).

### 3) Journalization → Trial Balance → GIFI schedules
Not started in SOT yet.
The intent is to:
- generate journal entries deterministically from canonical allocations + classifications + inventory adjustments,
- build FY2024/FY2025 TB snapshots,
- map to GIFI using the `curlys-books/t2-filing-fy2024-fy2025/gifi_chunks/` references.
