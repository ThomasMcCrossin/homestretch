# Independent recalculations (attempt-only)

- FY: `FY2024`
- Attempt: `attempt_001`

## Income statement checks (Schedule 125)
- Revenue (8089/8299): `181,235`
- Purchases (8320): `112,126`
- Closing inventory (8500 shown as -2,847): treat as `2,847` to subtract
- COGS (8518): `109,279`
- COGS recompute: `opening_inv(0) + purchases(112,126) - closing_inv(2,847) = 109,279`
  - Match? `True`
- Gross profit (8519): `71,956`
- Gross profit recompute: `revenue(181,235) - cogs(109,279) = 71,956`
  - Match? `True`
- Operating expenses detail sum (8520..9366): `53,981`
- Total operating expenses (9367): `53,981`
  - Detail matches 9367? `True`
- Net income (9369): `17,975` (should equal 8519 - 9367 = 17,975)

## Balance sheet checks (Schedule 100)
- Total assets (2599): `31,108`
- Total liabilities and shareholder equity (3640): `31,108`
  - Match? `True`
- Total liabilities (3499): `13,032`
- Total equity (3620): `18,076`
  - Liabilities + equity = `31,108` (should equal 3640)
  - Match? `True`
