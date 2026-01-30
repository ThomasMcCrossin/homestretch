# Fresher/categories → t2_final.db bill_allocations import

- source_key: `fresher_categories_wave_bill_allocations_csv`
- csv_path: `/home/clarencehub/Fresh/Fresher/categories/output/wave_bill_account_allocations_with_vendor_splits_and_export_categories_and_missing_profiles.csv`
- db: `/home/clarencehub/t2-final-fy2024-fy2025/db/t2_final.db`
- method_alloc: `FRESHER_CATEGORIES_ALLOC`
- method_tax_itc: `FRESHER_CATEGORIES_TAX_ITC`
- hst_itc_account_code: `2210`
- scope: `2023-06-01 → 2025-05-31`
- dry_run: `False`
- reset: `True`
- skip_existing: `True`

## Counts

- csv_rows_read: 1253
- csv_distinct_bills: 755
- bills_imported: 424
- allocation_rows_inserted: 485
- tax_itc_rows_inserted: 279
- bills_skipped_out_of_scope: 1
- bills_skipped_already_allocated: 293
- bills_skipped_allocation_mismatch: 37
- bills_skipped_missing_account_code: 0
- bills_missing_in_db: 0

## Outputs

- skipped: `/home/clarencehub/t2-final-fy2024-fy2025/output/fresher_categories_allocations_import_skipped.csv`
