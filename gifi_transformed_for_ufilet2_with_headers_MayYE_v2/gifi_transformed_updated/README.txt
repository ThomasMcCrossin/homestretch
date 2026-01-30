UFileT2 GIFI import candidates (generated 202601270915)

Corporation:
  - Name: 14587430 Canada Inc.
  - Business number: 748003142
  - Corp tax account: RC0001  (full: 748003142RC0001)
Fiscal year ends (FY runs June -> May):
  - FY2024 year-end: May 31, 2024  (GIFI01 date field: 202405310900)
  - FY2025 year-end: May 31, 2025  (GIFI01 date field: 202505310900)

Files:
  - ufilet2_<FY>_<vendorstyle>_<bn9|bn15>.gfi  -> full codes (balance sheet + income statement)
  - ufilet2_<FY>_schedule100_<vendorstyle>_<bn9|bn15>.gfi -> only codes < 8000 (Schedule 100-ish)
  - ufilet2_<FY>_schedule125_<vendorstyle>_<bn9|bn15>.gfi -> only codes >= 8000 (Schedule 125-ish)
  - ufilet2_<FY>_2col.csv -> bare 2-column (code, amount) fallback

Vendor styles:
  - caseware : header mimics the CaseWare sample header structure (24 fields).
  - generic  : header uses a generic vendor string.

Notes:
  - NO amounts or codes were changed; only header metadata (business number/company name and fiscal year end) was added.
  - Lines are CRLF terminated, and each CSV line includes a trailing comma to mimic some .GFI exports.
