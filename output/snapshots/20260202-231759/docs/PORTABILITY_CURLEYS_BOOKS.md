# Portability: t2-final ⇄ curlys-books (accounts + journal entries)

This project is designed so the **account codes** and **journal entry structures** can be moved into `curlys-books` with minimal translation later.

## Canonical identifiers

### `account_code` is the primary key everywhere

- We treat `curlys-books` account codes (e.g. `5004`, `2210`, `1050`) as the canonical identifiers.
- `t2-final` never invents account codes in code.
- If a new account is needed (e.g. a “suspense”/rounding account), add it in `curlys-books` first, then re-import the chart of accounts into `t2-final`.

## Chart of accounts

### curlys-books source

`curlys-books` has:
- `curlys_corp.chart_of_accounts`
  - includes `account_code`, `account_name`, `account_type`, and also `gifi_code` + `t2125_line` mappings.

### t2-final mirror

`t2-final` mirrors this table shape in SQLite:
- `chart_of_accounts` (created by migration `db/migrations/003_accounting_tables.sql`)
- Imported by:
  - `scripts/50_import_chart_of_accounts_from_curlysbooks.py`

The import also writes a timestamped CSV snapshot under:
- `data/curlys_books_exports/<timestamp>/chart_of_accounts.csv`

## Journal entries

### curlys-books structure

`curlys-books` uses:
- `curlys_corp.journal_entries`
- `curlys_corp.journal_entry_lines`

Key portability constraint: journal lines reference accounts by **`account_code`**, not by a separate account ID.

### t2-final structure

`t2-final` creates SQLite tables with the same core intent:
- `journal_entries`
- `journal_entry_lines`

Notes:
- `t2-final` stores amounts as **integer cents** (`debit_cents`, `credit_cents`) for deterministic totals.
- When exporting to `curlys-books`, cents are converted to decimal dollars for Postgres `numeric`.

## What “bank linking” is for (and why it still matters)

GIFI schedules are derived from a **trial balance**, which is derived from **journal lines**.

Bank/wave/shopify “links” are not directly used to compute GIFI totals — they exist to:
- prevent double-counting (e.g. Wave bills + bank payments),
- prove completeness (“every bank line is explained or queued for review”),
- preserve CRA auditability (provenance back to bank statements, settlement notices, etc.).

Once we generate journal lines, the link tables become an audit trail rather than a computation dependency.

