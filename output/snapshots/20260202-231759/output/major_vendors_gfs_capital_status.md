# Major Vendor Status: GFS + Capital

- Generated: `2026-01-22T15:35:08`
- DB: `/home/clarencehub/t2-final-fy2024-fy2025/db/t2_final.db`

## What this report covers (and what it does NOT)

- ✅ What exists: Wave bill facts + bank matching + PAD grouping + invoice-number/amount lists (when available).
- ❌ Not present yet: item-level invoice categories (COGS subcategories / supplies / etc). Nothing in the current DB stores GFS/Capital invoice line items with account codes.

## Snapshot Summary

| vendor | wave bills | wave total | wave tax | accounted wave bills | bank-linked | off-bank | PAD payments | PAD total | PAD invoice lines | PAD invoices linked to wave |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `GFS` | 134 | $77,525.00 | $1,169.53 | 134 | 130 | 4 | 69 | $71,734.90 | 107 | 105 |
| `CAPITAL` | 28 | $23,325.95 | $1,487.16 | 28 | 25 | 3 | 20 | $18,021.29 | 8 | 7 |

## Matching breakdown (Wave → Bank)

### GFS

| match_type | match_method | count |
|---|---|---:|
| `PAD_INVOICE` | `PAD_GFS_SUBSET_2` | 40 |
| `PAD_INVOICE` | `PAD_GFS_SUBSET_1` | 34 |
| `PAD_INVOICE` | `PAD_GFS_SUBSET_3` | 27 |
| `PAD_INVOICE` | `PAD_GFS_SUBSET_4` | 8 |
| `SHAREHOLDER_REIMBURSE` | `OLD_DB_NOTE_INVOICE` | 5 |
| `CASH_PAID` | `USER_MANUAL` | 4 |
| `PAD_INVOICE` | `PAD_GFS_EFT_FILE_4` | 4 |
| `INTERCOMPANY_PURCHASE` | `EMAIL_NOTE_INVOICE` | 2 |
| `PAD_INVOICE` | `PAD_GFS_EFT_FILE_3` | 2 |
| `SHAREHOLDER_REIMBURSE` | `USER_MANUAL` | 2 |
| `SPLIT_PAYMENT` | `USER_MANUAL` | 2 |
| `PAD_INVOICE` | `PAD_GFS_EFT_FILE_2` | 1 |
| `SHAREHOLDER_REIMBURSE` | `SHAREHOLDER_ET_0D` | 1 |

### CAPITAL

| match_type | match_method | count |
|---|---|---:|
| `PAD_INVOICE` | `PAD_CAPITAL_SUBSET_1` | 14 |
| `PAD_INVOICE` | `PAD_CAPITAL_SUBSET_2` | 6 |
| `CASH_PAID` | `USER_MANUAL` | 2 |
| `CC_PURCHASE` | `USER_MANUAL` | 2 |
| `PAD_INVOICE` | `MANUAL_PAD_MATCH` | 2 |
| `PAD_INVOICE` | `MANUAL_CAPITAL_PAP` | 1 |
| `SHAREHOLDER_REIMBURSE` | `USER_MANUAL` | 1 |

## PAD invoice list completeness

### GFS

- PAD payments: **69** (distinct bank txns: **69**)
- Payments missing invoice lists: **5**
- Payments with partial invoice lists (sum mismatch): **3**

#### Payments with NO invoice list captured

| payment_date | pad_payment_id | bank_txn_id | payment_total |
|---|---:|---:|---:|
| `2023-09-15` | `1` | `1665` | $363.18 |
| `2024-08-16` | `83` | `1070` | $236.65 |
| `2024-11-08` | `84` | `853` | $1,846.43 |
| `2025-02-28` | `85` | `513` | $2,124.95 |
| `2025-03-21` | `86` | `440` | $971.93 |

#### Payments with PARTIAL invoice lists (sum mismatch)

| payment_date | pad_payment_id | bank_txn_id | payment_total | invoice_sum | diff | invoice_count | captured_invoice_numbers |
|---|---:|---:|---:|---:|---:|---:|---|
| `2024-02-09` | `80` | `1320` | $1,391.33 | $877.39 | $513.94 | 1 | `9006298062` |
| `2024-04-05` | `82` | `1171` | $1,835.54 | $791.12 | $1,044.42 | 1 | `9007911798` |
| `2024-04-12` | `81` | `1154` | $1,213.34 | $1,263.91 | $-50.57 | 1 | `9008171261` |

#### PAD invoice lines not linked to Wave bills

| payment_date | pad_payment_id | invoice_number | amount | notes |
|---|---:|---|---:|---|
| `2025-03-07` | `55` | `9019510794` | $887.23 | possible Wave bill(s) by amount with blank invoice_number: id=625 date=2025-02-21 |
| `2025-03-14` | `56` | `9019803957` | $645.76 | possible Wave bill(s) by amount with blank invoice_number: id=636 date=2025-02-27 |

### CAPITAL

- PAD payments: **20** (distinct bank txns: **20**)
- Payments missing invoice lists: **12**
- Payments with partial invoice lists (sum mismatch): **0**

#### Payments with NO invoice list captured

| payment_date | pad_payment_id | bank_txn_id | payment_total |
|---|---:|---:|---:|
| `2024-10-16` | `69` | `936` | $1,290.47 |
| `2024-10-30` | `70` | `882` | $336.04 |
| `2024-11-13` | `87` | `836` | $935.34 |
| `2024-11-27` | `71` | `801` | $2,291.95 |
| `2024-12-18` | `88` | `721` | $100.61 |
| `2025-01-02` | `89` | `694` | $820.06 |
| `2025-01-08` | `72` | `670` | $1,625.25 |
| `2025-01-29` | `73` | `601` | $829.51 |
| `2025-02-05` | `77` | `588` | $1,003.96 |
| `2025-03-05` | `74` | `500` | $1,250.74 |
| `2025-03-26` | `75` | `427` | $1,110.97 |
| `2025-04-09` | `78` | `400` | $1,472.06 |

#### PAD invoice lines not linked to Wave bills

| payment_date | pad_payment_id | invoice_number | amount | notes |
|---|---:|---|---:|---|
| `2024-02-07` | `63` | `2542817` | $938.90 |  |

