# CC payment → purchase candidates by window (mapped cards, no edits)

Window = max days between CC purchase and bank payment (purchase must be before payment).

- 7d: strict 1:1 with wave 0 | purchase no wave 22 | ambiguous 1 | no purchase 33
- 14d: strict 1:1 with wave 0 | purchase no wave 25 | ambiguous 1 | no purchase 30
- 30d: strict 1:1 with wave 1 | purchase no wave 36 | ambiguous 1 | no purchase 18
- 60d: strict 1:1 with wave 0 | purchase no wave 32 | ambiguous 8 | no purchase 16
- 90d: strict 1:1 with wave 0 | purchase no wave 33 | ambiguous 8 | no purchase 15
