Wave bill overrides

- File: wave_bill_overrides.csv
- Purpose: keep documented diffs from the original Wave bill CSV
- Applied by: 01c_apply_wave_overrides.py (runs after 01_load_data.py in run_all.py)

Columns
- action: UPDATE | DELETE | INSERT
- source_row: original CSV row number when available
- invoice_number: Wave invoice number when available
- invoice_date, vendor_raw, total_cents, tax_cents, net_cents: target values
- notes: human context

Notes
- DELETE will also remove related rows in wave_matches, pad_invoices, and split_payments.
- INSERT does not set source_row so it stays decoupled from the raw CSV.
