#!/usr/bin/env bash
set -euo pipefail

# Creates isolated run directories under T2Analysis for Claude and/or Codex.
# Usage:
#   ./T2Analysis/tools/new_run_dirs.sh FY2025 ufile claude
#   ./T2Analysis/tools/new_run_dirs.sh FY2024 ufile codex
#   ./T2Analysis/tools/new_run_dirs.sh FY2025 ufile both

FY="${1:?FY required (FY2024 or FY2025)}"
AREA="${2:?area required (e.g., ufile)}"
AGENT="${3:?agent required (claude|codex|both)}"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TS="$(date +"%Y%m%d_%H%M%S")"

mk_run () {
  local agent="$1"
  local run_dir="${ROOT}/T2Analysis/t2_attempts/${FY}/${AREA}/analyses/${agent}/run_${TS}"
  mkdir -p "${run_dir}/inputs" "${run_dir}/work" "${run_dir}/outputs"
  if [[ -f "${ROOT}/T2Analysis/templates/RUN_README_TEMPLATE.md" ]]; then
    cp "${ROOT}/T2Analysis/templates/RUN_README_TEMPLATE.md" "${run_dir}/README.md"
  else
    printf "# Run README\n" > "${run_dir}/README.md"
  fi
  echo "${run_dir}"
}

case "${AGENT}" in
  claude) mk_run "claude" ;;
  codex) mk_run "codex" ;;
  both)
    mk_run "claude"
    mk_run "codex"
    ;;
  *)
    echo "Unknown agent: ${AGENT} (use claude|codex|both)" >&2
    exit 2
    ;;
esac

