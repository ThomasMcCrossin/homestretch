# UFile screen coverage map (FY2024 + FY2025)

This maps what exists in `UfileToFill/` to where the **actual filing values** live.

Rule: use the year fill guide as the “enter-this” source:
- `UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md`
- `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`

## Identification / setup

- `UfileToFill/Identification of the Corporation/*`
  - Values are in each year’s `UFILet2_FILL_GUIDE.md` under **Identification of the corporation**.

- `UfileToFill/Head Office Address/*`
  - Values are in each year’s `UFILet2_FILL_GUIDE.md` under **Head office address**.

- `UfileToFill/Other Addresses/*`
  - Values are in each year’s `UFILet2_FILL_GUIDE.md` under **Mailing address** + **Location of books & records**.

- `UfileToFill/Corporate Officers/*`
  - Values are in each year’s `UFILet2_FILL_GUIDE.md` under **Corporate officers / directors**.

- `UfileToFill/Tax Preparer/*`
  - Values are in each year’s `UFILet2_FILL_GUIDE.md` under **Tax preparer**.

## GIFI + tax schedules (amounts)

- `UfileToFill/GIFI/*`
  - Reference only (catalog of codes).
  - Filing values come from the year fill guides and the packet tables:
    - `UfileToFill/ufile_packet/tables/schedule_100_FY2024.csv`
    - `UfileToFill/ufile_packet/tables/schedule_125_FY2024.csv`
    - `UfileToFill/ufile_packet/tables/schedule_1_FY2024.csv`
    - `UfileToFill/ufile_packet/tables/schedule_100_FY2025.csv`
    - `UfileToFill/ufile_packet/tables/schedule_125_FY2025.csv`
    - `UfileToFill/ufile_packet/tables/schedule_1_FY2025.csv`

## Prior-year carryforward / UFile-only screens

- `UfileToFill/Corporate History/corporateHistory.txt`
  - Values are in each year’s `UFILet2_FILL_GUIDE.md` under **Corporate history carryforward**.
  - Structured values are also stored in `packet.json` at:
    - `years.FY2024.ufile_screens.corporate_history`
    - `years.FY2025.ufile_screens.corporate_history`

- `UfileToFill/Transaction with shareholders, officers, or employees/transactionswiththem.txt`
  - Values are in each year’s `UFILet2_FILL_GUIDE.md` under **Transactions with shareholders/officers/employees**.

- `UfileToFill/Dividends Paid/*` and `UfileToFill/General Rate Income Pool/*`
  - FY2025 only (dividends exist).
  - Values are in `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md` under **Dividends paid** + **GRIP**.

## Expected empty / “No” screens

These exist in `UfileToFill/` but are expected to be **No / empty** for these years, unless you know otherwise:

- `UfileToFill/Loss carry forwards and loss carry backs/*`
- `UfileToFill/Charitable Donations/*`
- `UfileToFill/Reserves/*`
- `UfileToFill/Capital Cost Allowance/*`
- `UfileToFill/Non Deperciable Capital Property/*`
- `UfileToFill/Deferred Income Plans/*`
- `UfileToFill/Status Change for the Corporation/*`

Each year fill guide includes an “Other UFile screens” section confirming these as “No”.

