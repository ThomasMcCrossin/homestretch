# Legacy / planning notes (do not use as run prompts)

We iterated on prompt structure while designing the workflow and architecture.
This file exists so we can preserve the evolution without cluttering the “active” prompts.

## Current stance (pre-run stage)

- The UFile PDF must be parsed **before** running an agent analysis.
- Agents must use the stable parsed bundle under:
  - `T2Analysis/t2_attempts/<FY>/ufile/parses/latest/`
- Agents must not run the parser and must not rely on reading the PDF directly.

## What’s kept in legacy

Older prompt variants that:
- referenced older folder names (`attempt_001`, `v1`, etc.)
- included “extract text from PDF” steps
- were used during architecture setup

These are stored under `T2Analysis/prompts/legacy/` for reference only.

Active “run-ready” prompts are:
- `T2Analysis/prompts/claude/PROMPT_CLAUDE_UFILE_FY2025_ATTEMPT_DIAGNOSIS_v2.md`
- `T2Analysis/prompts/codex/PROMPT_CODEX_UFILE_FY2025_ATTEMPT_DIAGNOSIS_v2.md`
