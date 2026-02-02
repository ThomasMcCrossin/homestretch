# FY2024 payroll delta walkthrough (bank vs employee exports)
Scope: 2023-06-01 → 2024-05-31 (FY2024)
## Topline
- Payroll net from employee exports (sum of `payroll_employee_pay_periods.net_pay_cents`): $20,060.49
- Bank payroll paid (sum of bank debits categorized `EMPLOYEE_PAYROLL`/`SHAREHOLDER_PAYROLL`): $19,384.12
- Delta (bank - exports): $-676.37

## Delta by employee
| employee | export rows | export net | bank txns | bank paid | delta (bank-export) |
|---|---:|---:|---:|---:|---:|
| Tyson | 23 | $3,356.47 | 13 | $2,455.44 | $-901.03 |
| Jesse Goodwin | 24 | $4,733.29 | 28 | $5,191.25 | $457.96 |
| Anthony | 13 | $9,697.75 | 16 | $9,600.94 | $-96.81 |
| Maddison | 3 | $272.98 | 2 | $136.49 | $-136.49 |
| Thomas McCrossin | 1 | $2,000.00 | 1 | $2,000.00 | $0.00 |

## Detail: Tyson
Export net total: $3,356.47 across 23 rows.
Bank payroll total: $2,455.44 across 13 e-transfers.

### Export rows
| pay_period_end | net | tips |
|---|---:|---:|
| 2023-10-30 | $73.44 | $0.00 |
| 2023-11-05 | $73.44 | $0.00 |
| 2023-11-12 | $65.28 | $0.00 |
| 2023-11-19 | $81.60 | $0.00 |
| 2023-11-26 | $89.76 | $0.00 |
| 2023-12-10 | $89.76 | $0.00 |
| 2023-12-17 | $114.24 | $0.00 |
| 2023-12-31 | $65.28 | $0.00 |
| 2024-01-07 | $73.21 | $0.00 |
| 2024-01-14 | $115.02 | $0.00 |
| 2024-01-21 | $161.59 | $0.00 |
| 2024-01-28 | $279.05 | $0.00 |
| 2024-02-04 | $169.75 | $0.00 |
| 2024-02-11 | $240.85 | $0.00 |
| 2024-02-18 | $285.98 | $0.00 |
| 2024-02-25 | $246.11 | $0.00 |
| 2024-03-03 | $111.62 | $0.00 |
| 2024-03-10 | $168.79 | $0.00 |
| 2024-03-17 | $169.75 | $0.00 |
| 2024-03-24 | $151.02 | $0.00 |
| 2024-04-07 | $119.31 | $0.00 |
| 2024-04-14 | $233.39 | $0.00 |
| 2024-04-21 | $178.23 | $80.43 |

### Bank e-transfers (categorized payroll)
| bank_txn_id | txn_date | amount | description |
|---:|---|---:|---|
| 1364 | 2024-01-22 | $101.59 | Internet Banking E-TRANSFER104858509989 Tyson Ogden 4506*********695 |
| 1353 | 2024-01-29 | $279.05 | Internet Banking E-TRANSFER104865799646 Tyson Ogden 4506*********695 |
| 1329 | 2024-02-05 | $169.75 | Internet Banking E-TRANSFER104875370018 Tyson Ogden 4506*********695 |
| 1315 | 2024-02-12 | $240.85 | Internet Banking E-TRANSFER104882731877 Tyson Ogden 4506*********695 |
| 1307 | 2024-02-19 | $285.98 | Internet Banking E-TRANSFER104890506040 Tyson Ogden 4506*********695 |
| 1279 | 2024-02-26 | $246.11 | Internet Banking E-TRANSFER104897758549 Tyson Ogden 4506*********695 |
| 1260 | 2024-03-04 | $111.62 | Internet Banking E-TRANSFER104907440516 Tyson Ogden 4506*********695 |
| 1240 | 2024-03-11 | $168.79 | Internet Banking E-TRANSFER104915418489 Tyson Ogden 4506*********695 |
| 1212 | 2024-03-18 | $169.75 | Internet Banking E-TRANSFER104923379550 Tyson Ogden 4506*********695 |
| 1199 | 2024-03-25 | $151.02 | Internet Banking E-TRANSFER104931365257 Tyson Ogden 4506*********695 |
| 1165 | 2024-04-08 | $119.31 | Internet Banking E-TRANSFER104949259856 Tyson Ogden 4506*********695 |
| 1153 | 2024-04-15 | $233.39 | Internet Banking E-TRANSFER104956790047 Tyson Ogden 4506*********695 |
| 1133 | 2024-04-22 | $178.23 | Internet Banking E-TRANSFER104965863474 Tyson Ogden 4506*********695 |

## Detail: Jesse Goodwin
Export net total: $4,733.29 across 24 rows.
Bank payroll total: $5,191.25 across 28 e-transfers.

### Export rows
| pay_period_end | net | tips |
|---|---:|---:|
| 2023-09-17 | $88.63 | $0.00 |
| 2023-09-24 | $121.73 | $0.00 |
| 2023-10-01 | $276.25 | $0.00 |
| 2023-10-08 | $279.64 | $0.00 |
| 2023-10-15 | $177.07 | $0.00 |
| 2023-10-22 | $279.64 | $0.00 |
| 2023-10-29 | $326.33 | $0.00 |
| 2023-11-05 | $372.16 | $0.00 |
| 2023-11-12 | $278.15 | $0.00 |
| 2023-11-19 | $177.07 | $0.00 |
| 2023-11-26 | $221.33 | $0.00 |
| 2023-12-03 | $159.96 | $0.00 |
| 2023-12-10 | $194.62 | $0.00 |
| 2023-12-17 | $146.10 | $0.00 |
| 2023-12-31 | $0.00 | $0.00 |
| 2024-02-25 | $73.19 | $0.00 |
| 2024-03-03 | $212.16 | $0.00 |
| 2024-03-10 | $223.32 | $0.00 |
| 2024-03-17 | $189.45 | $0.00 |
| 2024-03-24 | $263.63 | $0.00 |
| 2024-03-31 | $49.09 | $0.00 |
| 2024-04-07 | $73.19 | $0.00 |
| 2024-04-14 | $257.05 | $0.00 |
| 2024-04-21 | $293.53 | $80.43 |

### Bank e-transfers (categorized payroll)
| bank_txn_id | txn_date | amount | description |
|---:|---|---:|---|
| 1669 | 2023-09-13 | $127.50 | Internet Banking E-TRANSFER104706966492 Jesse Goodwin 4506*********695 |
| 1663 | 2023-09-18 | $222.21 | Internet Banking E-TRANSFER104711459740 Jesse Goodwin 4506*********695 |
| 1647 | 2023-09-26 | $118.37 | Internet Banking E-TRANSFER104721160190 Jesse Goodwin 4506*********695 |
| 1627 | 2023-10-03 | $263.60 | Internet Banking E-TRANSFER104729656149 Jesse Goodwin 4506*********695 |
| 1622 | 2023-10-10 | $266.46 | Internet Banking E-TRANSFER104738217873 Jesse Goodwin 4506*********695 |
| 1612 | 2023-10-16 | $170.36 | Internet Banking E-TRANSFER104745792680 Jesse Goodwin 4506*********695 |
| 1566 | 2023-10-23 | $266.46 | Internet Banking E-TRANSFER104753522688 Jesse Goodwin 4506*********695 |
| 1546 | 2023-10-30 | $310.03 | Internet Banking E-TRANSFER104761015300 Jesse Goodwin 4506*********695 |
| 1524 | 2023-11-06 | $352.29 | Internet Banking E-TRANSFER104770772373 Jesse Goodwin 4506*********695 |
| 1511 | 2023-11-14 | $264.97 | Internet Banking E-TRANSFER104777335173 Jesse Goodwin 4506*********695 |
| 1498 | 2023-11-20 | $170.36 | Internet Banking E-TRANSFER104786114758 Jesse Goodwin 4506*********695 |
| 1488 | 2023-11-27 | $211.95 | Internet Banking E-TRANSFER104793606121 Jesse Goodwin 4506*********695 |
| 1465 | 2023-12-04 | $159.96 | Internet Banking E-TRANSFER104803134889 Jesse Goodwin 4506*********695 |
| 1448 | 2023-12-11 | $72.25 | Internet Banking E-TRANSFER104810499570 Jesse Goodwin 4506*********695 |
| 1449 | 2023-12-11 | $194.62 | Internet Banking E-TRANSFER104810499235 Jesse Goodwin 4506*********695 |
| 1438 | 2023-12-19 | $146.10 | Internet Banking E-TRANSFER104820383740 Jesse Goodwin 4506*********695 |
| 1366 | 2024-01-22 | $41.01 | Internet Banking E-TRANSFER104858391441 Jesse Goodwin 4506*********695 |
| 1367 | 2024-01-22 | $91.45 | Internet Banking E-TRANSFER104858380497 Jesse Goodwin 4506*********695 |
| 1362 | 2024-01-23 | $114.82 | Internet Banking E-TRANSFER104858861737 Jesse Goodwin 4506*********695 |
| 1280 | 2024-02-26 | $73.19 | Internet Banking E-TRANSFER104897754454 Jesse Goodwin 4506*********695 |
| 1258 | 2024-03-04 | $200.02 | Internet Banking E-TRANSFER104907463546 Jesse Goodwin 4506*********695 |
| 1239 | 2024-03-11 | $223.32 | Internet Banking E-TRANSFER104915419606 Jesse Goodwin 4506*********695 |
| 1213 | 2024-03-18 | $189.45 | Internet Banking E-TRANSFER104923378867 Jesse Goodwin 4506*********695 |
| 1198 | 2024-03-25 | $263.63 | Internet Banking E-TRANSFER104931371857 Jesse Goodwin 4506*********695 |
| 1179 | 2024-04-02 | $49.09 | Internet Banking E-TRANSFER104941596099 Jesse Goodwin 4506*********695 |
| 1164 | 2024-04-08 | $73.19 | Internet Banking E-TRANSFER104949460167 Jesse Goodwin 4506*********695 |
| 1152 | 2024-04-15 | $257.05 | Internet Banking E-TRANSFER104956793038 Jesse Goodwin 4506*********695 |
| 1134 | 2024-04-22 | $297.54 | Internet Banking E-TRANSFER104965851361 Jesse Goodwin 4506*********695 |

## Detail: Anthony
Export net total: $9,697.75 across 13 rows.
Bank payroll total: $9,600.94 across 16 e-transfers.

### Export rows
| pay_period_end | net | tips |
|---|---:|---:|
| 2023-11-05 | $352.29 | $0.00 |
| 2023-11-26 | $362.67 | $0.00 |
| 2023-12-03 | $473.50 | $0.00 |
| 2023-12-24 | $495.00 | $0.00 |
| 2023-12-31 | $177.19 | $0.00 |
| 2024-01-15 | $618.10 | $0.00 |
| 2024-01-29 | $621.34 | $0.00 |
| 2024-02-12 | $726.68 | $0.00 |
| 2024-02-26 | $1,300.03 | $0.00 |
| 2024-03-11 | $1,305.38 | $0.00 |
| 2024-03-25 | $1,356.21 | $0.00 |
| 2024-04-08 | $1,065.27 | $0.00 |
| 2024-04-22 | $844.09 | $80.43 |

### Bank e-transfers (categorized payroll)
| bank_txn_id | txn_date | amount | description |
|---:|---|---:|---|
| 1509 | 2023-11-14 | $271.40 | Internet Banking E-TRANSFER104778530123 Anthony MacDonald 4506*********695 |
| 1485 | 2023-11-28 | $372.67 | Internet Banking E-TRANSFER104794962670 Anthony MacDonald 4506*********695 |
| 1444 | 2023-12-12 | $473.50 | Internet Banking E-TRANSFER104812195714 Anthony MacDonald 4506*********695 |
| 1430 | 2023-12-27 | $495.00 | Internet Banking E-TRANSFER104829071636 Anthony MacDonald 4506*********695 |
| 1418 | 2024-01-02 | $177.19 | Internet Banking E-TRANSFER104836337121 Anthony MacDonald 4506*********695 |
| 1380 | 2024-01-16 | $592.18 | Internet Banking E-TRANSFER104852080756 Anthony MacDonald 4506*********695 |
| 1352 | 2024-01-29 | $621.34 | Internet Banking E-TRANSFER104865850951 Anthony MacDonald 4506*********695 |
| 1314 | 2024-02-12 | $726.68 | Internet Banking E-TRANSFER104882810534 Anthony MacDonald 4506*********695 |
| 1278 | 2024-02-26 | $893.62 | Internet Banking E-TRANSFER104897816385 Anthony MacDonald 4506*********695 |
| 1266 | 2024-02-28 | $17.59 | Internet Banking E-TRANSFER104900212635 Anthony MacDonald 4506*********695 |
| 1228 | 2024-03-11 | $1,305.38 | Internet Banking E-TRANSFER104915499803 Anthony MacDonald 4506*********695 |
| 1238 | 2024-03-11 | $388.82 | Internet Banking E-TRANSFER104915452214 Anthony MacDonald 4506*********695 |
| 1196 | 2024-03-25 | $79.04 | Internet Banking E-TRANSFER104931388437 Anthony MacDonald 4506*********695 |
| 1197 | 2024-03-25 | $1,277.17 | Internet Banking E-TRANSFER104931384681 Anthony MacDonald 4506*********695 |
| 1163 | 2024-04-08 | $1,065.27 | Internet Banking E-TRANSFER104949471403 Anthony MacDonald 4506*********695 |
| 1132 | 2024-04-22 | $844.09 | Internet Banking E-TRANSFER104965874006 Anthony MacDonald 4506*********695 |

## What this tells us
- The FY2024 delta is **not** a single missing payment; it is the net of **employee-by-employee mismatches** between the early-season CSV exports and the bank e-transfer history.
- In particular, the 2023-season CSVs (e.g. `/home/clarencehub/Fresh/dump/2023Canteen/*.csv`) contain non-standard rows/notes and (in some cases) cross-entity fields (e.g. “Rambler Hours”). Those exports do not always represent a clean “this exact net amount was paid by this bank transfer”.
- From an auditability standpoint, the bank e-transfers are cleanly present and categorized; the question is whether the **employee export rows** are the right source-of-truth for FY2024 payroll accruals, or whether we should treat portions of those exports as out-of-scope / non-canteen / non-payroll adjustments.
