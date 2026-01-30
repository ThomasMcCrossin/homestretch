# FY2025 — UFile Attempt 2 vs current packet (post-Costco fix)

This compares the last exported UFile T2 PDF you entered (**Attempt 2**) against the current packet/guides after the Costco `9100` renormalization.

**Attempt 2 evidence**
- Parsed tables: `T2Analysis/t2_attempts/FY2025/ufile/parses/attempt_002/tables/`

**Current packet evidence**
- Year packet: `UfileToFill/ufile_packet/years/FY2025/packet.json`
- Fill guide: `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`

## UFile-entered lines that changed (Schedule 125)

UFile derives cost of sales internally from the 8300/8320/8500 block.

| Code | Description | Attempt 2 (PDF) | Current (guide) | Delta |
|---:|---|---:|---:|---:|
| 8320 | Purchases / cost of materials | 112,866 | 117,452 | +4,586 |
| 9130 | Supplies | 5,348 | 4,629 | -719 |
| 8960 | Repairs and maintenance | 981 | 603 | -378 |
| 9270 | Other expenses | 3,782 | 293 | -3,489 |

**Sign convention note:** the PDF prints `8500` as a negative line item (e.g., “-10,015”), but in the UFile entry screen you type **10,015**.

## Display-only (auto-calculated) lines that changed (Schedule 125)

These are not typically typed directly; they should follow from the entered lines.

| Code | Description | Attempt 2 (PDF) | Current (packet) | Delta |
|---:|---|---:|---:|---:|
| 8518 | Cost of sales | 105,698 | 110,284 | +4,586 |
| 8519 | Gross profit / loss | 125,209 | 120,623 | -4,586 |
| 9367 | Total operating expenses | 96,860 | 92,274 | -4,586 |

Sanity: the 8320 increase is offset by decreases in 9270/9130/8960 and flows through 8518/8519/9367.

## Balance sheet differences observed in Attempt 2 (Schedule 100)

Attempt 2 had the known BCR issue where retained earnings / totals didn’t tie (difference **36,901**). The current packet expects that to be resolved by relying on UFile’s rollforward screens (retained earnings 3660/3680/3700/3740/3849) rather than manually typing `3600/3849`.

| Code | Description | Attempt 2 (PDF) | Current (packet) | Delta |
|---:|---|---:|---:|---:|
| 3600 | Retained earnings / deficit | 45,005 | 8,104 | -36,901 |
| 3620 | Total shareholder equity | 45,105 | 8,204 | -36,901 |
| 3640 | Total liabilities and shareholder equity | 62,878 | 25,977 | -36,901 |

Retained earnings rollforward lines (3660/3680/3700/3849) match between Attempt 2 and the packet; the mismatch was the Schedule 100 typed totals.

