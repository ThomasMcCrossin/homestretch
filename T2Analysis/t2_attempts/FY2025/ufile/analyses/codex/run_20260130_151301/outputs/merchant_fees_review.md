# Merchant / Processing Fees Review (FY2025)

Source: `db/t2_final.db` (journal entries + Wave bills)

## FY2025 totals by account

| Account | Name | FY2025 total (debit - credit) |
|---|---|---|
| 5300 | Merchant Processing Fees | 2969.96 |
| 6210 | Payment Processing Fees | 2227.26 |

## Breakdown by source_system / source_record_type

| Account | source_system | source_record_type | FY2025 total | lines |
|---|---|---|---|---|
| 5300 | t2-final | wave_bill_accrual | 2969.96 | 8 |
| 6210 | t2-final | bank_inflows | 2227.26 | 160 |

## Largest Wave bills hitting 5300

| Entry date | Vendor | Invoice # | Amount | Journal description | Wave bill id |
|---|---|---|---|---|---|
| 2024-12-31 | Shopify - Bill 2024 CC Fees | 2024 | 2208.04 | Shopify - Bill 2024 CC Fees - Invoice 2024 | 541 |
| 2025-02-24 | Nayax - Bill |  | 557.43 | Nayax - Bill | 628 |
| 2025-03-15 | Shopify - Bill |  | 44.42 | Shopify - Bill | 655 |
| 2025-02-13 | Shopify - Bill |  | 44.09 | Shopify - Bill | 617 |
| 2025-05-14 | Shopify - Bill |  | 43.08 | Shopify - Bill | 700 |
| 2025-04-14 | Shopify - Bill |  | 43.00 | Shopify - Bill | 685 |
| 2025-04-30 | Nayax - Bill |  | 14.95 | Nayax - Bill | 693 |
| 2025-05-31 | Nayax - Bill |  | 14.95 | Nayax - Bill | 706 |

## Shopify payout fee lines hitting 6210 (largest 12)

| Entry date | Description | Amount | Source record id (bank txn) |
|---|---|---|---|
| 2024-11-14 | Shopify Payout - bank txn 833 | 118.45 | 0f5140ed-d43f-5b41-9e13-8255ab14eced |
| 2024-10-17 | Shopify Payout - bank txn 934 | 110.48 | 0798166c-c757-5029-b3b9-97d0ec5423c8 |
| 2024-10-03 | Shopify Payout - bank txn 974 | 106.58 | 3576f93c-5e3d-5cad-9f33-f2c2f9e84c79 |
| 2024-11-06 | Shopify Payout - bank txn 861 | 89.73 | 20109b54-656d-54ed-9051-204353fc0046 |
| 2025-02-20 | Shopify Payout - bank txn 545 | 85.90 | 2fd81fb3-f7fa-5b0b-89dd-dbe434436c6b |
| 2025-01-15 | Shopify Payout - bank txn 658 | 81.90 | f559b7dc-4d50-5bed-bc7f-6d380b6b2557 |
| 2025-01-29 | Shopify Payout - bank txn 602 | 74.13 | fd2300e9-8fb0-5389-b40a-956e7fb00ced |
| 2025-03-26 | Shopify Payout - bank txn 433 | 74.03 | 12b9ccb4-7d62-5bfd-a9aa-d4924c8b4a26 |
| 2024-12-11 | Shopify Payout - bank txn 746 | 70.81 | fd809d90-4c72-589b-8c6e-a89916230624 |
| 2024-10-30 | Shopify Payout - bank txn 883 | 69.23 | fd5ea264-85b9-59ac-be68-be3ca9272710 |
| 2025-03-19 | Shopify Payout - bank txn 452 | 68.06 | c5fa1078-ebf5-5851-9c38-ba6387fe1c38 |
| 2025-01-08 | Shopify Payout - bank txn 685 | 68.03 | 64739867-3b24-5cf9-9c77-504ae0f0bd21 |

## Assessment

- **Two streams are present:** 5300 is entirely sourced from `wave_bill_accrual` entries, while 6210 is entirely sourced from `bank_inflows`.
- **Potential duplication risk:** the single Wave bill **“Shopify - Bill 2024 CC Fees - Invoice 2024”** (2,208.04) is close to the *entire* FY2025 total of Shopify payout fees in 6210 (2,227.26). This suggests the Wave bill could represent an annual aggregation of Shopify processing fees that are already netted out in payouts.
- **Non-Shopify fees also appear in 5300:** multiple **Nayax** bills are included in 5300, which likely represent separate merchant terminal processing costs and would not be reflected in Shopify payouts.
