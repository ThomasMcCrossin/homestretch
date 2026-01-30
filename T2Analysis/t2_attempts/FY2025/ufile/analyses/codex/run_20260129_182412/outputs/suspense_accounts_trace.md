# Suspense / placeholder accounts trace (FY2025, attempt_002)

These accounts are flagged heuristically by name patterns (pending/suspense/no ITC/etc.).

| Account code | Account name | Account type | GIFI code | Net (dollars) | Notes |
|---:|---|---|---:|---:|---|
| 9100 | Pending Receipt - No ITC | expense | 9270 | 3,508.12 | vendor_profile_estimate allocs=3,489.29 |

## Notes
- `9100 Pending Receipt - No ITC` is a known placeholder-style bucket that is fed by `VENDOR_PROFILE_ESTIMATE` allocations (see `9270_trace.md`).
- If these balances are expected (e.g., deliberate accrual/placeholder), document rationale; otherwise, they indicate categorization gaps to resolve upstream.
