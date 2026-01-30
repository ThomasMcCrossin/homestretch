# SOT Overrides

This folder contains **explicit “data decisions”** that should affect canonical outputs **without editing the frozen source DB**.

## `ignore_wave_bills.json`

A list of `fresher_debits__wave_bills.id` values to mark as ignored in the SOT DB.

Use this for:
- duplicate Wave bills that would otherwise double-count a bank/CC payment,
- known bad rows that you want excluded from TB/GIFI outputs.

These ignores are applied by:
- `sot/scripts/15_apply_overrides.py`

## `vendor_profile_overrides.json`

Manual vendor allocation profiles (percent splits) that override any imported breakdown for matching Wave bills.

Use this for:
- mixed vendors where the automatically-derived profile is not acceptable (e.g., Walmart),
- vendors where Wave has only a single “COGS” style bill but you want a reasonable split (COGS vs office vs repairs).

Applied by:
- `sot/scripts/33_apply_vendor_profile_overrides.py`
