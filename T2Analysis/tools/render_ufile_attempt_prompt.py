#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = PROJECT_ROOT / "T2Analysis" / "prompts" / "templates" / "PROMPT_UFILE_ATTEMPT_DIAGNOSIS_TEMPLATE.md"


def render_template(text: str, mapping: dict[str, str]) -> str:
    out = text
    for k, v in mapping.items():
        out = out.replace("{" + k + "}", v)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fy", required=True, help="FY key, e.g. FY2024 or FY2025")
    ap.add_argument("--attempt-id", required=True, help="attempt id, e.g. attempt_001")
    ap.add_argument("--agent", required=True, choices=["codex", "claude"], help="Target agent (affects header only)")
    ap.add_argument(
        "--run-dir",
        required=True,
        help="Run directory (created by new_run_dirs.sh). Prompt will be written under <run-dir>/inputs/.",
    )
    args = ap.parse_args()

    fy = str(args.fy).strip()
    attempt_id = str(args.attempt_id).strip()
    agent = str(args.agent).strip()
    run_dir = Path(args.run_dir).resolve()

    if not TEMPLATE_PATH.exists():
        raise SystemExit(f"Missing prompt template: {TEMPLATE_PATH}")

    exports_dir = PROJECT_ROOT / "T2Analysis" / "t2_attempts" / fy / "ufile" / "exports" / attempt_id
    parse_dir = PROJECT_ROOT / "T2Analysis" / "t2_attempts" / fy / "ufile" / "parses" / attempt_id

    export_pdf = exports_dir / "ufile_return.pdf"
    messages_txt = exports_dir / "messages.txt"

    # Run dir layout
    inputs_dir = run_dir / "inputs"
    inputs_dir.mkdir(parents=True, exist_ok=True)

    mapping = {
        "REPO_ROOT": str(PROJECT_ROOT),
        "FY": fy,
        "ATTEMPT_ID": attempt_id,
        "AGENT": agent,
        "RUN_DIR": str(run_dir),
        "EXPORT_PDF": str(export_pdf),
        "MESSAGES_TXT": str(messages_txt),
        "PARSE_DIR": str(parse_dir),
    }

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    rendered = render_template(template, mapping).rstrip() + "\n"

    out_path = inputs_dir / "PROMPT.md"
    out_path.write_text(rendered, encoding="utf-8")

    # Also emit a short evidence paths file for quick copy/paste into LLM tools.
    evidence_md = "\n".join(
        [
            "# Evidence paths",
            "",
            f"- FY: `{fy}`",
            f"- attempt_id: `{attempt_id}`",
            f"- export_pdf: `{export_pdf}`",
            f"- messages: `{messages_txt}`",
            f"- parse_dir: `{parse_dir}`",
            "",
        ]
    )
    (inputs_dir / "evidence_paths.md").write_text(evidence_md, encoding="utf-8")

    print("PROMPT RENDERED")
    print(f"- out: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

