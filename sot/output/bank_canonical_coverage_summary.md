# Bank Coverage (Canonical Allocations)

Scope: 2023-06-01 → 2025-05-31

Definitions:
- `canonical_sum`: sum of `txn_document_allocations.amount_cents` where `role='CANONICAL'` for the bank txn.
- Some bank txns are “explained” via classifications or settlement links but intentionally have no document allocations yet.

## Summary

- bank_txns_total: 1357
- fully_allocated_to_docs: 503
- partially_allocated_to_docs: 26
- no_doc_allocations: 828
  - explained_non_doc: 828
  - unexplained: 0

## Largest Partial Remainders (Top 25)

- 2024-10-22 txn_id=570 bank=-3,000.00 canonical_sum=-1,000.00 remainder=-2,000.00 settlements=- cc_link=0 cats=FRESHER_DEBITS:HST_REIMBURSEMENT desc=Internet Banking E-TRANSFER105192346999 Thomas McCrossin 4506*********695
- 2024-10-22 txn_id=575 bank=-42.86 canonical_sum=-85.72 remainder=42.86 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000223097 MASTERCARD, BMO 4506*********695
- 2024-10-02 txn_id=638 bank=-183.67 canonical_sum=-211.22 remainder=27.55 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000202078 MASTERCARD, NEO FINANCIAL 4506*********695
- 2025-03-26 txn_id=93 bank=-30.00 canonical_sum=-21.80 remainder=-8.20 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000221281 MASTERCARD, NEO FINANCIAL 4506*********695
- 2025-02-27 txn_id=179 bank=-137.26 canonical_sum=-130.89 remainder=-6.37 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000129964 MASTERCARD, BMO 4506*********695
- 2024-11-06 txn_id=518 bank=-106.99 canonical_sum=-113.32 remainder=6.33 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000222084 MASTERCARD, TRIANGLE -CDN 4506*********695
- 2024-12-16 txn_id=385 bank=-761.05 canonical_sum=-766.33 remainder=5.28 settlements=- cc_link=0 cats=FRESHER_DEBITS:PAYROLL_REMIT desc=Electronic Funds Transfer MISC PAYMENT 121520241655670 THE PEPSI BOTTL
- 2025-02-10 txn_id=236 bank=-77.48 canonical_sum=-73.65 remainder=-3.83 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000125304 MASTERCARD, NEO FINANCIAL 4506*********695
- 2024-03-11 txn_id=890 bank=-48.12 canonical_sum=-51.16 remainder=3.04 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000230574 MASTERCARD, NEO FINANCIAL 4506*********695
- 2024-12-16 txn_id=390 bank=-30.51 canonical_sum=-31.44 remainder=0.93 settlements=- cc_link=1 cats=- desc=Internet Banking INTERNET TRANSFER000000200410 5268*********154
- 2024-03-11 txn_id=894 bank=-9.27 canonical_sum=-10.17 remainder=0.90 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000208669 MASTERCARD, NEO FINANCIAL 4506*********695
- 2024-11-06 txn_id=520 bank=-56.97 canonical_sum=-56.57 remainder=-0.40 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000104079 MASTERCARD, BMO 4506*********695
- 2024-04-16 txn_id=810 bank=-123.25 canonical_sum=-123.49 remainder=0.24 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000126929 MASTERCARD, BMO 4506*********695
- 2024-07-02 txn_id=742 bank=-155.64 canonical_sum=-155.54 remainder=-0.10 settlements=- cc_link=0 cats=FRESHER_DEBITS:VENDOR_PAYMENT desc=Internet Banking INTERNET BILL PMT000000119753 SYSCO - MONCTON 4506*********695
- 2024-03-06 txn_id=914 bank=-298.92 canonical_sum=-298.89 remainder=-0.03 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000212347 MASTERCARD, BMO 4506*********695
- 2024-04-22 txn_id=792 bank=-484.99 canonical_sum=-484.96 remainder=-0.03 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking E-TRANSFER104965874591 Dwayne Ripley 4506*********695
- 2023-11-08 txn_id=1182 bank=-1,232.52 canonical_sum=-1,232.51 remainder=-0.01 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking E-TRANSFER104772599167 Dwayne Ripley 4506*********695
- 2024-02-22 txn_id=951 bank=-133.36 canonical_sum=-133.35 remainder=-0.01 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000231401 MASTERCARD, BMO 4506*********695
- 2024-03-14 txn_id=879 bank=-135.51 canonical_sum=-135.50 remainder=-0.01 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000237939 MASTERCARD, BMO 4506*********695
- 2024-10-22 txn_id=578 bank=-25.28 canonical_sum=-25.29 remainder=0.01 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000117116 MASTERCARD, NEO FINANCIAL 4506*********695
- 2024-12-16 txn_id=388 bank=-21.25 canonical_sum=-21.24 remainder=-0.01 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000201989 MASTERCARD, BMO 4506*********695
- 2025-01-16 txn_id=312 bank=-129.40 canonical_sum=-129.39 remainder=-0.01 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000209957 MASTERCARD, BMO 4506*********695
- 2025-02-27 txn_id=183 bank=-63.01 canonical_sum=-63.00 remainder=-0.01 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking INTERNET BILL PMT000000132835 MASTERCARD, TRIANGLE -CDN 4506*********695
- 2025-02-27 txn_id=188 bank=-73.64 canonical_sum=-73.65 remainder=0.01 settlements=- cc_link=0 cats=FRESHER_DEBITS:REIMBURSEMENT desc=Internet Banking E-TRANSFER105354218363 Thomas McCrossin 4506*********695
- 2025-03-17 txn_id=123 bank=-195.45 canonical_sum=-195.46 remainder=0.01 settlements=- cc_link=1 cats=- desc=Internet Banking INTERNET TRANSFER000000233002 4500*********318

## Largest Unexplained (Top 25)

- (none)
