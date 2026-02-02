# Invoice PDF → bill_allocations import

- db: `/home/clarencehub/t2-final-fy2024-fy2025/db/t2_final.db`
- mapping: `/home/clarencehub/t2-final-fy2024-fy2025/overrides/invoice_pdf_mappings.yml`
- scope: `2023-06-01 → 2025-05-31`
- dry_run: `False`
- reset: `True`
- skip_existing: `True`

## Methods

- category: `INVOICE_PDF_CATEGORY`
- tax_itc: `INVOICE_PDF_TAX_ITC` (account `2210`)
- capital_cc_fee: `INVOICE_PDF_CC_FEE`
- adjustment: `INVOICE_PDF_ADJUSTMENT`
- fallback: `INVOICE_RULE_FALLBACK`

## Counts

- wave_bills_considered: 3
- bills_imported: 3
- allocation_rows_inserted: 5
- bills_skipped: 0

## Notes

- This importer only targets Wave bills missing allocations in scope.
- GFS uses the invoice 'Group Summary' category recap.
- Capital parses category totals + surcharges from the PDF and adds a Payment Processing Fee line when Wave totals include the ~3% CC fee era.
