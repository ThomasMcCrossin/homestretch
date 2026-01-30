# Wave reimbursement remainder analysis

This report explains the diagnostic field `remainder_cents = bank_reimbursement - linked_bill_totals` from `output/wave_bill_reimbursement_journal_detail.csv`.

Interpretation:
- `remainder_cents > 0`: reimbursement included extra amount not tied to Wave bills (often HST/fees/combined transfers).
- `remainder_cents < 0`: linked Wave bills exceed the reimbursement; corp still owes the shareholder (partial reimbursement or mismatched links).

Special case note (bank_txn 909):
- The $2,000 positive remainder on `bank_txn_id=909` is an **HST payment to CRA** that was reimbursed to Thomas as part of the same $3,000 transfer.
- CRA labels this as a **"Non-reporting period"** payment and later transfers it into the **2024-03-31** reporting period; this is normal CRA presentation/timing in account exports.

## Totals

- Rows: 187
- Net remainder: $1980.83
- Positive remainder total: $2018.92
- Negative remainder total: $-38.09

## By Category (net remainder)

- HST_REIMBURSEMENT: $2000.00
- REIMBURSEMENT: $-19.17
- RENT_REIMBURSEMENT: $0.00

## By Bank Manual Classification (net remainder)

- HST_REIMBURSEMENT: $2000.00
- CC_PAYMENT: $-19.20
- REIMBURSEMENT: $0.04
- (blank): $-0.01
- STAFF_EXPENSE: $0.00
- PAYROLL_ETRANSFER: $0.00
- VENDOR_PAYMENT: $0.00

## Largest Remainders (by absolute value)

- remainder $2000.00 | bank $3000.00 | bills $1000.00 | 909 (2024-10-22) E_TRANSFER manual=HST_REIMBURSEMENT :: Internet Banking E-TRANSFER105192346999 Thomas McCrossin 4506*********695
  - bill720:gfs cash cheese curds cogs 1:2024-10-22:500.00 | bill721:gfs cash cheese curds cogs 2:2024-10-22:500.00
- remainder $-27.55 | bank $183.67 | bills $211.22 | 977 (2024-10-02) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000202078 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill371:walmart bill:2024-09-17:211.22
- remainder $8.20 | bank $30.00 | bills $21.80 | 432 (2025-03-26) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000221281 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill645:value village bill:2025-03-08:21.80
- remainder $6.37 | bank $137.26 | bills $130.89 | 518 (2025-02-27) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000129964 MASTERCARD, BMO 4506*********695
  - bill631:circle k bill:2025-02-25:130.89
- remainder $-6.33 | bank $106.99 | bills $113.32 | 857 (2024-11-06) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000222084 MASTERCARD, TRIANGLE -CDN 4506*********695
  - bill385:circle k bill:2024-09-25:113.32
- remainder $3.83 | bank $77.48 | bills $73.65 | 575 (2025-02-10) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000125304 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill612:esso bill:2025-02-12:73.65
- remainder $-3.04 | bank $48.12 | bills $51.16 | 1229 (2024-03-11) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000230574 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill230:ali express bill:2024-02-26:51.16
- remainder $-0.90 | bank $9.27 | bills $10.17 | 1233 (2024-03-11) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000208669 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill154:ali express bill:2024-01-04:10.17
- remainder $0.40 | bank $56.97 | bills $56.57 | 859 (2024-11-06) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000104079 MASTERCARD, BMO 4506*********695
  - bill452:christmas discounters bill:2024-10-30:56.57
- remainder $-0.24 | bank $123.25 | bills $123.49 | 1149 (2024-04-16) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000126929 MASTERCARD, BMO 4506*********695
  - bill296:shell gas bill:2024-04-14:123.49
- remainder $0.03 | bank $484.99 | bills $484.96 | 1131 (2024-04-22) E_TRANSFER manual=REIMBURSEMENT :: Internet Banking E-TRANSFER104965874591 Dwayne Ripley 4506*********695
  - bill301:curly s sports and supplements bill 2576869:2024-04-22:484.96
- remainder $0.03 | bank $298.92 | bills $298.89 | 1253 (2024-03-06) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000212347 MASTERCARD, BMO 4506*********695
  - bill240:costco bill:2024-03-05:298.89
- remainder $-0.01 | bank $50.33 | bills $50.34 | 473 (2025-03-17) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000223687 MASTERCARD, BMO 4506*********695
  - bill640:circle k bill:2025-03-07:50.34
- remainder $0.01 | bank $63.01 | bills $63.00 | 522 (2025-02-27) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000132835 MASTERCARD, TRIANGLE -CDN 4506*********695
  - bill624:circle k bill:2025-02-21:63.00
- remainder $-0.01 | bank $73.64 | bills $73.65 | 527 (2025-02-27) E_TRANSFER manual= :: Internet Banking E-TRANSFER105354218363 Thomas McCrossin 4506*********695
  - bill612:esso bill:2025-02-12:73.65
- remainder $0.01 | bank $129.40 | bills $129.39 | 651 (2025-01-16) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000209957 MASTERCARD, BMO 4506*********695
  - bill557:shell gas bill:2025-01-09:129.39
- remainder $0.01 | bank $21.25 | bills $21.24 | 727 (2024-12-16) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000201989 MASTERCARD, BMO 4506*********695
  - bill531:stacked bill:2024-12-13:21.24
- remainder $-0.01 | bank $25.28 | bills $25.29 | 917 (2024-10-22) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000117116 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill336:temu bill:2024-08-19:25.29
- remainder $0.01 | bank $135.51 | bills $135.50 | 1218 (2024-03-14) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000237939 MASTERCARD, BMO 4506*********695
  - bill257:shell gas bill:2024-03-13:135.50
- remainder $0.01 | bank $133.36 | bills $133.35 | 1290 (2024-02-22) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000231401 MASTERCARD, BMO 4506*********695
  - bill205:circle k bill:2024-02-14:133.35
- remainder $0.01 | bank $1232.52 | bills $1232.51 | 1521 (2023-11-08) E_TRANSFER manual=REIMBURSEMENT :: Internet Banking E-TRANSFER104772599167 Dwayne Ripley 4506*********695
  - bill121:curly s sports and supplements bill d17:2023-11-07:1232.51
- remainder $0.00 | bank $104.99 | bills $104.99 | 367 (2025-04-24) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000239278 MASTERCARD, BMO 4506*********695
  - bill684:irving bill:2025-04-11:104.99
- remainder $0.00 | bank $118.34 | bills $118.34 | 370 (2025-04-24) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000225017 MASTERCARD, BMO 4506*********695
  - bill688:shell gas bill:2025-04-21:118.34
- remainder $0.00 | bank $51.90 | bills $51.90 | 403 (2025-04-08) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000123427 MASTERCARD, BMO 4506*********695
  - bill677:irving bill:2025-04-01:51.90
- remainder $0.00 | bank $113.51 | bills $113.51 | 405 (2025-04-08) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000131945 MASTERCARD, BMO 4506*********695
  - bill682:irving bill:2025-04-08:113.51

## Largest Positive Remainders

- remainder $2000.00 | 909 (2024-10-22) E_TRANSFER manual=HST_REIMBURSEMENT :: Internet Banking E-TRANSFER105192346999 Thomas McCrossin 4506*********695
- remainder $8.20 | 432 (2025-03-26) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000221281 MASTERCARD, NEO FINANCIAL 4506*********695
- remainder $6.37 | 518 (2025-02-27) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000129964 MASTERCARD, BMO 4506*********695
- remainder $3.83 | 575 (2025-02-10) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000125304 MASTERCARD, NEO FINANCIAL 4506*********695
- remainder $0.40 | 859 (2024-11-06) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000104079 MASTERCARD, BMO 4506*********695
- remainder $0.03 | 1131 (2024-04-22) E_TRANSFER manual=REIMBURSEMENT :: Internet Banking E-TRANSFER104965874591 Dwayne Ripley 4506*********695
- remainder $0.03 | 1253 (2024-03-06) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000212347 MASTERCARD, BMO 4506*********695
- remainder $0.01 | 522 (2025-02-27) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000132835 MASTERCARD, TRIANGLE -CDN 4506*********695
- remainder $0.01 | 651 (2025-01-16) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000209957 MASTERCARD, BMO 4506*********695
- remainder $0.01 | 727 (2024-12-16) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000201989 MASTERCARD, BMO 4506*********695
- remainder $0.01 | 1218 (2024-03-14) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000237939 MASTERCARD, BMO 4506*********695
- remainder $0.01 | 1290 (2024-02-22) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000231401 MASTERCARD, BMO 4506*********695
- remainder $0.01 | 1521 (2023-11-08) E_TRANSFER manual=REIMBURSEMENT :: Internet Banking E-TRANSFER104772599167 Dwayne Ripley 4506*********695

## Largest Negative Remainders

- remainder $-27.55 | 977 (2024-10-02) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000202078 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill371:walmart bill:2024-09-17:211.22
- remainder $-6.33 | 857 (2024-11-06) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000222084 MASTERCARD, TRIANGLE -CDN 4506*********695
  - bill385:circle k bill:2024-09-25:113.32
- remainder $-3.04 | 1229 (2024-03-11) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000230574 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill230:ali express bill:2024-02-26:51.16
- remainder $-0.90 | 1233 (2024-03-11) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000208669 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill154:ali express bill:2024-01-04:10.17
- remainder $-0.24 | 1149 (2024-04-16) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000126929 MASTERCARD, BMO 4506*********695
  - bill296:shell gas bill:2024-04-14:123.49
- remainder $-0.01 | 473 (2025-03-17) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000223687 MASTERCARD, BMO 4506*********695
  - bill640:circle k bill:2025-03-07:50.34
- remainder $-0.01 | 527 (2025-02-27) E_TRANSFER manual= :: Internet Banking E-TRANSFER105354218363 Thomas McCrossin 4506*********695
  - bill612:esso bill:2025-02-12:73.65
- remainder $-0.01 | 917 (2024-10-22) BILL_PAYMENT manual=CC_PAYMENT :: Internet Banking INTERNET BILL PMT000000117116 MASTERCARD, NEO FINANCIAL 4506*********695
  - bill336:temu bill:2024-08-19:25.29
