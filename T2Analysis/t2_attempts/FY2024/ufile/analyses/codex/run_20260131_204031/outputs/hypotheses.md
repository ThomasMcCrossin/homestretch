# Hypotheses / conclusions

## What is wrong vs the project?
- Core Schedule 100/125 numbers in this attempt appear internally consistent (balance sheet balances; net income math checks).
- The only clear “issue” surfaced in the PDF is a **CCA class missing** warning (from UFile Messages).

## Most likely root cause for the CCA warning
- UFile has a depreciation/CCA amount present, but no CCA class selected for at least one asset/addition.
- Fix in UI is to enter Schedule 8 details on the **Capital cost allowance** screen (pick Class 8 and enter additions/claim), rather than typing CCA somewhere else.

## Project cross-check (Schedule 8 exists)
- Project Schedule 8 total CCA claim: `330`
- Classes: `8`

## Operator / entry mechanics
- Prefer entering only **detail lines** from the fill guide and leave totals/subtotals blank (UFile will calculate them).
- For COGS: UFile often wants 8300/8320/8500; the project exports 8518 directly, but the fill guide derives and provides the breakdown to reduce UFile quirks.
