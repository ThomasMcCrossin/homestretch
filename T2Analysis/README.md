# T2Analysis (run isolation + traceability)

This directory is the **only place** where exploratory scripts, extracted text/OCR, and LLM-generated analyses should write files.

Goals:
- Keep UFile exports and accounting outputs **unchanged** (read-only)
- Prevent Claude/Codex outputs from getting mixed together
- Make every exploration reproducible via saved prompts + a run folder containing inputs and work products

## Structure

- `prompts/`
  - Stored prompts used for explorations (Claude/Codex), versioned by filename and date as needed.
- `t2_attempts/`
  - Per-year attempt artifacts and analysis run folders.
- `templates/`
  - Optional templates for run READMEs and reports.
- `tools/`
  - Optional helper scripts for creating run directories (must write under `T2Analysis/` only).

## Rule of thumb

If a tool/script would write anywhere outside `T2Analysis/`, don’t run it that way—redirect outputs into a run folder under `T2Analysis/t2_attempts/...`.

