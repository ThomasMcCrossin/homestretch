# Fixed assets and CCA continuity — FY2024

Period: **2023-06-10 to 2024-05-31**
Snapshot source: `output/snapshots/20260202-231500/output/`

## Key point
- Book fixed assets (GIFI 1740/1741/8670) and tax CCA (Schedule 8) are reconciled using the same asset register.
- If a UFile-exported PDF appears to show missing additions, the usual cause is that the **Capital cost allowance** screen was not completed for that class (UFile may omit the schedule from the package).

## Schedule 8 continuity (by class)
| Class | Description | Opening UCC | Additions | CCA claim | Closing UCC |
|---|---|---|---|---|---|
| 8 | General equipment | 0 | 1650 | 330 | 1320 |
| 50 | Computer hardware and systems software | 0 | 648 | 178 | 470 |

## Asset additions (by invoice / asset)
| Asset ID | Description | Available for use | Class | Cost | Source breakdown |
|---|---|---|---|---|---|
| ams_lb9_vending_machine_2024_02_20 | AMS-LB9 vending machine (Electric Kitty) | 2024-02-20 | 8 | 1100 | wave_bill_allocation: bill_id=221 invoice_date=2024-02-20 vendor=Electric Kitty - Bill account=6600 amount_cents=110000 alloc_total_cents=110000 |
| costco_freezer_2024_03_13 | Hisense freezer (Costco) | 2024-03-13 | 8 | 550 | wave_bill_allocation: bill_id=256 invoice_date=2024-03-13 vendor=Costco - Bill account=6600 amount_cents=54999 alloc_total_cents=54999 |
| costco_ipad_air_2023_12_08 | iPad Air 5 64GB (Costco) | 2023-12-08 | 50 | 648 | wave_bill_allocation: bill_id=143 invoice_date=2023-12-08 vendor=Costco - Bill 22134500703182312081530 account=6600 amount_cents=64839 alloc_total_cents=64839 |

Evidence:
- `output/snapshots/20260202-231500/output/schedule_8_FY2024.csv`
- `output/snapshots/20260202-231500/output/cca_asset_register_resolved.csv`
