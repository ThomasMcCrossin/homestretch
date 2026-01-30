# Independent recomputation (from parsed attempt amounts only)

## Schedule 125 (Income statement) recomputation

- Total revenue (8299): 230,907
- COGS (8518): 105,698
- Gross profit (computed): 8299 - 8518 = 230,907 - 105,698 = 125,209
- Gross profit (8519 on return): 125,209

### COGS movement check

- Opening inventory (8300): 2,847
- Purchases (8320): 112,866
- Closing inventory (8500 parsed): -10,015 (PDF shows parentheses; treat as -10,015)
- COGS from movement: 8300 + 8320 - abs(8500) = 2,847 + 112,866 - 10,015 = 105,698
- COGS (8518 on return): 105,698

### Operating expenses check

- Total operating expenses (9367 on return): 89,155
- Sum of populated expense detail lines (excluding totals like 9367/9368): 97,325
- Difference (detail sum - 9367): 8,170

### Net income check

- Net income (9999 on return): 36,054
- Net income recomputed using 9367: 8519 - 9367 = 125,209 - 89,155 = 36,054
- Net income recomputed using detail sum: 8519 - sum(expenses) = 125,209 - 97,325 = 27,884

## Schedule 100 (Balance sheet) recomputation

- Total assets (2599): 25,977
- Total liabilities (3499): 17,773
- Total shareholder equity (3620): 44,258
- Total liabilities and shareholder equity (3640): 62,031

### Equity and balance equation

- Equity recompute: 3500 + 3600 = 100 + 44,158 = 44,258 (compare to 3620=44,258)
- Liabilities + equity recompute: 3499 + 3620 = 17,773 + 44,258 = 62,031 (compare to 3640=62,031)
- Balance check: 3640 - 2599 = 62,031 - 25,977 = 36,054

### Retained earnings rollforward (as shown inside Schedule 100)

- Opening RE (3660): 8,104
- Net income/loss (3680): 36,054
- Closing RE (3849): 44,158
- Closing RE recompute (3660 + 3680): 44,158
