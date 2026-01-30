# T2 Final (FY2024 + FY2025) — Clean Filing Workspace

This folder is intentionally **separate** from:
- `/home/clarencehub/Fresh/` (experimental reconciliation work)
- `/home/clarencehub/curlys-books/` (production app + Postgres source of truth)

Goals:
- Build **deterministic**, **auditable** FY2024 + FY2025 corporate outputs (TB → GIFI schedules) using **immutable inputs** + **explicit overrides**.
- Avoid “balance-by-force” and avoid hiding logic in one-off SQL patches.

Scope in this repo (first milestone):
- Import reconciled Wave bills (final state) from the frozen Fresher snapshot.
- Derive **vendor allocation profiles** from categorized receipts in `curlys-books` (Postgres) for:
  - Costco
  - Pharmasave
  - Atlantic Superstore
  - Walmart
- Apply those profiles to Wave bills **only for vendors assumed to have been entered as pure COGS**, and only when no more-detailed breakdown is available.

Next milestone (freezing reconciliation decisions as data):
- Snapshot the full Fresher debit + credit reconciliation outcome into immutable data files so downstream TB/GIFI generation does not depend on Fresher scripts or SQL patches.
  - See: `docs/FRESHER_SNAPSHOT.md`
  - Current status: `docs/STATUS.md`
  - Run: `python3 scripts/40_snapshot_fresher_state.py`

Next milestone (single-DB workflow):
- Mirror all frozen Fresher tables into `t2_final.db` as `fresher_debits__*` / `fresher_credits__*` so you can query everything from one SQLite file.
  - Run: `python3 scripts/13_import_fresher_snapshot_tables.py --verify-files`

Portability milestone (align with curlys-books primitives):
- Mirror `curlys-books` chart of accounts + journal entry structures in SQLite.
  - See: `docs/PORTABILITY_CURLEYS_BOOKS.md`
  - Run: `python3 scripts/50_import_chart_of_accounts_from_curlysbooks.py`

## Quickstart

1) Verify sources + hashes:
   - `python3 scripts/01_verify_manifest.py`

2) Initialize DB:
   - `python3 scripts/00_init_db.py`

3) Snapshot Fresher reconciliation end-state (immutable “reconciliation-as-data”):
   - `python3 scripts/40_snapshot_fresher_state.py`

4) Import reconciled Wave bills from the frozen snapshot:
   - `python3 scripts/11_import_wave_bills_from_fresher_snapshot.py --reset`
   - Default scope is FY2024+FY2025 (per `manifest/sources.yml`). Use `--all` to import everything in the snapshot DB.

5) (Optional but recommended) Strengthen CC payment → Wave bill linkage evidence:
   - `python3 scripts/79_import_cc_payment_fifo_allocations.py --reset`
   - Note: if you later re-run `python3 scripts/13_import_fresher_snapshot_tables.py`, it drops/recreates the `fresher_*__*`
     tables, so re-run this FIFO import afterwards.

5) Extract receipt category splits from `curlys-books` and build vendor profiles:
   - `python3 scripts/20_build_vendor_profiles_from_curlysbooks.py --reset`

6) Apply profiles to Wave bills (FY2024/FY2025):
   - `python3 scripts/30_apply_vendor_profiles_to_wave_bills.py --fy FY2024 --fy FY2025`

7) Review outputs:
   - `output/vendor_profiles.md`
   - `output/vendor_allocations_by_fy.csv`
   - `output/vendor_allocations_summary_by_fy.csv`

## Files you will edit (by design)

- `manifest/sources.yml` — explicit list of inputs + sha256.
- `overrides/vendor_profile_rules.yml` — which vendors are eligible + exclusions.

Everything else should be generated from those files.

## Notes / guardrails

- Vendor profiles are only as good as the curlys-books sample size. `output/vendor_profiles.md` always reports sample counts + sample date ranges (so you can judge reliability).
- Exclusions: because many Wave ledger descriptions omit the invoice number, prefer excluding by `source_row` (stable row index in the CSV as long as the sha256 stays the same).
