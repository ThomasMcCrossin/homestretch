# T2 Source-of-Truth (SOT) DB

This folder contains a **fresh SQLite schema** intended to become the *single source of truth* for FY2024 + FY2025 T2 filing outputs.

Why this exists:
- The original reconciliation work (debits + credits) was successful but **spread across multiple DBs + scripts**.
- Some relationships exist in *different* tables (`wave_matches` vs `wave_bill_funding` vs credit-side EFT allocations), which makes it easy to misread “missing” vs “off-bank” vs “linked by settlement notice”.
- For T2 filing, we want one DB that:
  - preserves all **raw facts** immutably (bank/card lines, bills, settlement notices),
  - stores all reconciliation work as **explicit link rows** (splits, chains, allocations),
  - supports downstream **journalization → trial balance → GIFI** without “balancing by force”.

This SOT DB is **not** designed to mirror `curlys-books` Postgres. It is designed to be **auditable, deterministic, and complete enough to file**.

## Quick start

1) Initialize DB:
- `python3 sot/scripts/00_init_db.py`

2) Import the frozen reconciliation snapshot (read-only input):
- `python3 sot/scripts/10_import_from_t2_final_db.py --reset`

3) Apply overrides (duplicates / known-bad docs):
- `python3 sot/scripts/15_apply_overrides.py`

4) Import chart of accounts + bill category breakdowns:
- `python3 sot/scripts/31_import_chart_of_accounts.py`
- `python3 sot/scripts/32_import_bill_allocations_as_document_lines.py --reset`
- `python3 sot/scripts/33_apply_vendor_profile_overrides.py`
- `python3 sot/scripts/34_build_default_account_rollups.py --reset`

5) Build canonical allocations for bank coverage:
- `python3 sot/scripts/20_build_canonical_allocations.py --reset`

6) Generate readiness reports:
- `python3 sot/scripts/21_report_bank_coverage.py`
- `python3 sot/scripts/35_report_document_line_coverage.py`

Outputs and validation reports will be written to `sot/output/`.

## Docs

- `sot/ARCHITECTURE.md` — schema conventions, roles, invariants.
- `sot/STATUS.md` — current state + what remains to file the T2.
