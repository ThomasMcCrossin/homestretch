# GFS PAD audit: EFT notice lines vs Wave invoices

- Scope: 2023-06-01 → 2025-05-31
- Bank-linked EFT notices in scope: 70
- Detail CSV: `output/gfs_pad_invoice_mismatches_detail.csv`

## Missing invoices (by EFT notice)

- Notices with missing Wave invoices: 0


## Wave bill payment mismatches (cross-check)

- Bank txns in both EFT links and wave-bill-payment mismatch list: 0


## Unmatched EFT notices (no bank link)

- Unmatched notices in scope (by due_date): 4

- due_date 2023-06-09: notice_id 9f85a148-d69a-566c-a266-17536cf9df4f count=1 total=$155.00 file=EFT Notification_4.XLS
- due_date 2023-06-23: notice_id 52882265-d98f-56f9-a2e5-146c8955cd6a count=1 total=$265.68 file=EFT Notification_2.XLS
- due_date 2023-06-30: notice_id bce2e106-cef0-5d53-88ac-4c33ec43e914 count=2 total=$242.54 file=EFT Notification_3.XLS
- due_date 2023-08-25: notice_id e4cf8b8e-d598-5202-af4f-6fa1d4122bdf count=2 total=$1281.55 file=EFT Notification_1.XLS
