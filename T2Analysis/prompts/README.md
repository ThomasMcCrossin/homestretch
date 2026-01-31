# Prompts

Store prompts here so we can:
- see exactly what was asked on each exploration run
- compare Claude vs Codex output apples-to-apples
- iterate safely without rewriting or losing context

## Active prompts

- Template (FY-agnostic): `T2Analysis/prompts/templates/PROMPT_UFILE_ATTEMPT_DIAGNOSIS_TEMPLATE.md`
- Render a run prompt:
  - `python3 T2Analysis/tools/render_ufile_attempt_prompt.py --fy FY2024 --attempt-id attempt_001 --agent codex --run-dir <RUN_DIR>`

## Legacy prompts

Older variants (including “extract text from PDF” versions) live under `T2Analysis/prompts/legacy/` and should not be used for new runs.

FY2025-specific prompts are retained for reference under:
- `T2Analysis/prompts/claude/`
- `T2Analysis/prompts/codex/`
