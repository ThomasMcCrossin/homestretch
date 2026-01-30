# Next Actions (No Edits)

## If duplication is suspected (Shopify fees)
1) **Validate against Shopify payout reports** for FY2025 (2024-06-01 to 2025-05-31): sum processing fees from Shopify payouts and compare to the FY2025 total in account 6210 (2,227.26). If Shopify reports agree with 6210, treat 6210 as the primary source of truth for Shopify fees.
2) **Inspect the Wave bill “Shopify - Bill 2024 CC Fees - Invoice 2024” (2,208.04)** and confirm whether it represents the same processing fees already netted in payouts. If it does, it is likely a duplicate accrual and should be removed or reversed in a future adjustment (not in this forensic run).
3) **Check payment evidence for the Wave bill** (bank/credit-card payment). If the bill was actually paid separately (not netted in payouts), then it is a separate charge and should remain in 5300.

## If two-stream fees are legitimate
4) **Separate by vendor**: keep Nayax bills in 5300 (distinct terminal/merchant service fees), and Shopify payout fees in 6210.
5) **Document the policy**: note whether Shopify fees are captured via netted payouts (6210) or via Wave bills (5300) to prevent future double counting.

## Minimal reconciliation checklist
- Verify that total Shopify payout fees (from payout reports) equal 6210 total.
- Verify that Shopify Wave bills (e.g., 2024 CC Fees) are not the same fees already included in payout totals.
- Confirm that Nayax bills are unrelated to Shopify payouts.
