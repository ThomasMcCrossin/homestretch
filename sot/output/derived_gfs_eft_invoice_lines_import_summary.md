# Derived GFS EFT invoice docs → document_lines import

- db: `/home/clarencehub/t2-final-fy2024-fy2025/sot/db/t2_sot.db`
- scope: `2023-06-01 → 2025-05-31`
- mapping: `/home/clarencehub/t2-final-fy2024-fy2025/overrides/invoice_pdf_mappings.yml`
- dry_run: `False`
- reset: `False`

## Counts

- derived_docs_missing_lines_considered: 9
- derived_docs_filled: 9
- document_lines_inserted: 17
- skipped_or_fallbacked: 0

## Notes

- Uses GFS invoice PDFs when available; otherwise falls back to a single 5099 line equal to the doc total.
- This targets `source_record_id LIKE derived__gfs_eft_invoice:%` documents only.

