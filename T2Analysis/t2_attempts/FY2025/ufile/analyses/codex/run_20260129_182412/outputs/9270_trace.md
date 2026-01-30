# GIFI 9270 trace (FY2025, attempt_002)

- Attempt Schedule 125 / GIFI 9270 amount: **3,782**
- Project expected GIFI 9270 amount (packet.json): **3,782**

## Trial balance accounts mapped to GIFI 9270
| Account code | Account name | Net (dollars) | Notes |
|---:|---|---:|---|
| 9100 | Pending Receipt - No ITC | 3,508.12 | placeholder-style bucket; vendor_profile_estimate allocs=3,489.29 |
| 9150 | Penalties - CRA | 273.87 | CRA penalties/interest (may be non-deductible) |

- Trial balance total for GIFI 9270 accounts: **3,781.99**
- Difference vs attempt 9270: **-0.01**

## Vendor allocation evidence feeding suspense-like buckets (account 9100)
These are allocations tagged as `VENDOR_PROFILE_ESTIMATE` into account `9100` (a suspense/placeholder-style account), summarized from `vendor_allocations_by_fy.csv`.

- Rows for FY2025 with account_code=9100: **29**
- Sum of allocations to 9100: **3,489.29** (dollars)

### By vendor (from vendor_allocations_summary_by_fy.csv)
| Vendor key | Amount (dollars) |
|---|---:|
| COSTCO | 3,489.29 |

### Largest individual allocations (top 15)
| Invoice date | Vendor | Wave bill | Amount (dollars) | Method |
|---|---|---:|---:|---|
| 2025-02-12 | Costco - Bill | 613 | 410.89 | VENDOR_PROFILE_ESTIMATE |
| 2025-01-09 | Costco - Bill | 558 | 225.89 | VENDOR_PROFILE_ESTIMATE |
| 2025-03-19 | Costco - Bill | 664 | 223.54 | VENDOR_PROFILE_ESTIMATE |
| 2025-02-05 | Costco - Bill | 603 | 217.36 | VENDOR_PROFILE_ESTIMATE |
| 2024-12-13 | Costco - Bill | 532 | 189.24 | VENDOR_PROFILE_ESTIMATE |
| 2024-10-05 | Costco - Bill | 408 | 184.81 | VENDOR_PROFILE_ESTIMATE |
| 2025-02-25 | Costco - Bill | 629 | 171.86 | VENDOR_PROFILE_ESTIMATE |
| 2025-03-09 | Costco - Bill | 647 | 167.33 | VENDOR_PROFILE_ESTIMATE |
| 2024-10-16 | Costco - Bill | 426 | 160.19 | VENDOR_PROFILE_ESTIMATE |
| 2024-11-13 | Costco - Bill | 477 | 159.40 | VENDOR_PROFILE_ESTIMATE |
| 2024-09-25 | Costco - Bill | 387 | 156.17 | VENDOR_PROFILE_ESTIMATE |
| 2024-09-18 | Costco - Bill | 373 | 150.13 | VENDOR_PROFILE_ESTIMATE |
| 2024-10-30 | Costco - Bill | 454 | 148.46 | VENDOR_PROFILE_ESTIMATE |
| 2024-10-23 | Costco - Bill | 436 | 122.08 | VENDOR_PROFILE_ESTIMATE |
| 2024-08-28 | Costco - Bill | 340 | 121.66 | VENDOR_PROFILE_ESTIMATE |
