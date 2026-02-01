# Fixed assets and CCA continuity — FY2025

Period: **2024-06-01 to 2025-05-31**
Snapshot source: `output/snapshots/20260201-183000/output/`

## Key point
- Book fixed assets (GIFI 1740/1741/8670) and tax CCA (Schedule 8) are reconciled using the same asset register.
- If a UFile-exported PDF appears to show missing additions, the usual cause is that the **Capital cost allowance** screen was not completed for that class (UFile may omit the schedule from the package).

## Schedule 8 continuity (by class)
| Class | Description | Opening UCC | Additions | CCA claim | Closing UCC |
|---|---|---|---|---|---|
| 8 | General equipment | 1320 | 557 | 375 | 1502 |
| 12 | Tools and utensils under $500 | 0 | 663 | 663 | 0 |
| 50 | Computer hardware and systems software | 470 | 0 | 259 | 211 |

## Asset additions (by invoice / asset)
| Asset ID | Description | Available for use | Class | Cost | Source breakdown |
|---|---|---|---|---|---|
| nayax_card_reader_2025_02_24 | Nayax card reader for vending machine | 2025-02-24 | 8 | 557 | wave_bill_allocation: bill_id=628 invoice_date=2025-02-24 vendor=Nayax - Bill account=5300 amount_cents=55743 alloc_total_cents=55743 |
| shopify_card_reader_2024_11_12 | Shopify card reader hardware | 2024-11-12 | 12 | 479 | wave_bill_allocation: bill_id=473 invoice_date=2024-11-12 vendor=Shopify - Bill account=6600 amount_cents=45900 alloc_total_cents=45900 | wave_bill_allocation: bill_id=473 invoice_date=2024-11-12 vendor=Shopify - Bill account=6550 amount_cents=2000 alloc_total_cents=2000 |
| walmart_coffee_grinder_2024_09_17 | Coffee grinder (Walmart) | 2024-09-17 | 12 | 184 | wave_bill_allocation: bill_id=371 invoice_date=2024-09-17 vendor=Walmart - Bill account=6600 amount_cents=18367 alloc_total_cents=18367 |

Evidence:
- `output/snapshots/20260201-183000/output/schedule_8_FY2025.csv`
- `output/snapshots/20260201-183000/output/cca_asset_register_resolved.csv`
