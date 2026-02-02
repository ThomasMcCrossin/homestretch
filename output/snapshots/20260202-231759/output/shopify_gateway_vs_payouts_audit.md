# Shopify audit: gateway exports vs payout-based GL

This is a sanity-check report. It does **not** replace payout-linked bank deposits as the GL source-of-truth.

Key point:
- Payouts are **deposit-date** based and represent what hit the bank.
- Gateway exports are **transaction-date** based and include payment methods like `cash` and `gift_card` that never appear in payouts.
- Therefore, gateway totals will not tie 1:1 to payouts without a timing/coverage model.

## FY2024 (2023-06-01 → 2024-05-31)

- Gateway reports available (within FY): 4
- Gateway reports selected (non-overlapping heuristic): 4

Selected reports:

- 2023-06-01 → 2023-09-30: Net payments by gateway - 2023-06-01 - 2023-09-30.csv
- 2023-10-01 → 2023-12-31: Net payments by gateway - 2023-10-01 - 2023-12-31.csv
- 2024-01-01 → 2024-03-31: Net payments by gateway - 2024-01-01 - 2024-03-31.csv
- 2024-04-01 → 2024-05-31: Net payments by gateway - 2024-04-01 - 2024-05-31.csv

Gateway totals (selected reports only):

- shopify_payments: tx=11462 gross=$120281.13 refunded=$-154.99 net=$120126.14
- cash: tx=8546 gross=$71683.02 refunded=$-97.96 net=$71585.06
- manual: tx=2 gross=$1210.95 refunded=$0.00 net=$1210.95
- paypal: tx=43 gross=$1161.82 refunded=$-84.00 net=$1077.82
- gift_card: tx=6 gross=$32.47 refunded=$0.00 net=$32.47

Sales channel totals (selected reports only):

- point of sale: tx=19679 gross=$184349.34 refunded=$-114.45 net=$184234.89
- online store: tx=351 gross=$8312.06 refunded=$-206.98 net=$8105.08
- draft orders: tx=3 gross=$1307.87 refunded=$0.00 net=$1307.87
- shop: tx=19 gross=$292.84 refunded=$0.00 net=$292.84
- shopify mobile for android: tx=1 gross=$91.76 refunded=$0.00 net=$91.76
- unknown: tx=6 gross=$15.52 refunded=$-15.52 net=$0.00

Internet revenue % (from gateway exports):

- Online channels (treated as internet): online store, shop
- Online net payments: $8397.92
- Total net payments (all channels): $194032.44
- % gross revenue from internet (Online Store + Shop): 4.33

Payout totals in FY (payout_date, deposit-date):

- Payout count: 157
- charges_cents: $120148.45
- refunds_cents: $-154.99
- adjustments_cents: $0.14
- fees_cents: $1599.31
- total_cents: $118394.29
- Check: (charges + refunds + adjustments - fees) = $118394.29; diff vs total = $0.00

Comparison (sanity check only):

- Gateway `shopify_payments` net (transaction-date): $120126.14
- Payout (charges+refunds+adjustments) (deposit-date): $119993.60
- Delta: $132.54

Reminder:

- Gateway `cash` net ($71585.06) is POS cash and should be captured via cash deposits / cash-on-hand, not Shopify payouts.

## FY2025 (2024-06-01 → 2025-05-31)

- Gateway reports available (within FY): 4
- Gateway reports selected (non-overlapping heuristic): 4

Selected reports:

- 2024-06-01 → 2024-09-30: Net payments by gateway - 2024-06-01 - 2024-09-30.csv
- 2024-10-01 → 2024-12-31: Net payments by gateway - 2024-10-01 - 2024-12-31.csv
- 2025-01-01 → 2025-03-31: Net payments by gateway - 2025-01-01 - 2025-03-31.csv
- 2025-04-01 → 2025-05-31: Net payments by gateway - 2025-04-01 - 2025-05-31.csv

Gateway totals (selected reports only):

- shopify_payments: tx=15428 gross=$166957.78 refunded=$-263.50 net=$166694.28
- cash: tx=10515 gross=$89690.86 refunded=$-128.80 net=$89562.06
- paypal: tx=23 gross=$570.18 refunded=$0.00 net=$570.18
- gift_card: tx=12 gross=$166.51 refunded=$0.00 net=$166.51
- manual: tx=1 gross=$20.00 refunded=$0.00 net=$20.00

Sales channel totals (selected reports only):

- point of sale: tx=25382 gross=$244857.18 refunded=$-212.80 net=$244644.38
- online store: tx=543 gross=$11274.55 refunded=$-19.50 net=$11255.05
- shop: tx=49 gross=$1019.20 refunded=$0.00 net=$1019.20
- draft orders: tx=3 gross=$224.00 refunded=$-160.00 net=$64.00
- shopify mobile for iphone: tx=1 gross=$20.00 refunded=$0.00 net=$20.00
- shopify mobile for android: tx=1 gross=$10.40 refunded=$0.00 net=$10.40

Internet revenue % (from gateway exports):

- Online channels (treated as internet): online store, shop
- Online net payments: $12274.25
- Total net payments (all channels): $257013.03
- % gross revenue from internet (Online Store + Shop): 4.78

Payout totals in FY (payout_date, deposit-date):

- Payout count: 160
- charges_cents: $166938.06
- refunds_cents: $-263.50
- adjustments_cents: $0.00
- fees_cents: $2227.26
- total_cents: $164447.30
- Check: (charges + refunds + adjustments - fees) = $164447.30; diff vs total = $0.00

Comparison (sanity check only):

- Gateway `shopify_payments` net (transaction-date): $166694.28
- Payout (charges+refunds+adjustments) (deposit-date): $166674.56
- Delta: $19.72

Reminder:

- Gateway `cash` net ($89562.06) is POS cash and should be captured via cash deposits / cash-on-hand, not Shopify payouts.

## Interpretation notes

- Using payouts for GL does **not** double-count fees: payouts are net-to-bank, and we book fees separately to reconcile to gross sales.
- Gateway exports are useful to sanity-check the *shape* of sales by payment method, and to catch missing cash deposits, but they should not replace payout-linked bank deposits for GL.
