#!/usr/bin/env bash
set -euo pipefail

# Create a new UFile attempt bundle (exports + parsed) under T2Analysis.
#
# Usage:
#   ./T2Analysis/tools/new_ufile_attempt.sh FY2025 /path/to/ufile_export.pdf
#
# Writes ONLY under:
#   T2Analysis/t2_attempts/<FY>/ufile/{exports,parses}/attempt_NNN/

FY="${1:?FY required (FY2024 or FY2025)}"
PDF_IN="${2:?Path to UFile PDF export required}"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PDF_IN_ABS="$(python3 - <<PY
import os,sys
print(os.path.abspath(sys.argv[1]))
PY
"${PDF_IN}")"

EXPORTS_ROOT="${ROOT}/T2Analysis/t2_attempts/${FY}/ufile/exports"
PARSES_ROOT="${ROOT}/T2Analysis/t2_attempts/${FY}/ufile/parses"

mkdir -p "${EXPORTS_ROOT}" "${PARSES_ROOT}"

next_n() {
  local n=1
  if ls -1 "${EXPORTS_ROOT}"/attempt_* >/dev/null 2>&1; then
    n="$(ls -1 "${EXPORTS_ROOT}"/attempt_* | sed -E 's/.*attempt_([0-9]+).*/\\1/' | sort -n | tail -n 1)"
    n="$((10#${n} + 1))"
  fi
  printf "%03d" "${n}"
}

N="$(next_n)"
ATTEMPT_DIR="attempt_${N}"

EXPORT_DIR="${EXPORTS_ROOT}/${ATTEMPT_DIR}"
PARSE_DIR="${PARSES_ROOT}/${ATTEMPT_DIR}"

mkdir -p "${EXPORT_DIR}" "${PARSE_DIR}"

cp "${PDF_IN_ABS}" "${EXPORT_DIR}/ufile_return.pdf"
sha256sum "${EXPORT_DIR}/ufile_return.pdf" > "${EXPORT_DIR}/sha256.txt"
pdfinfo "${EXPORT_DIR}/ufile_return.pdf" > "${EXPORT_DIR}/pdfinfo.txt" || true

VENV="${ROOT}/T2Analysis/tools/ufile_pdf_parser/.venv"
PYBIN="${VENV}/bin/python"

if [[ ! -x "${PYBIN}" ]]; then
  echo "Parser venv missing. Create it first:"
  echo "  python3 -m venv T2Analysis/tools/ufile_pdf_parser/.venv"
  echo "  T2Analysis/tools/ufile_pdf_parser/.venv/bin/pip install -r T2Analysis/tools/ufile_pdf_parser/requirements.txt"
  exit 2
fi

"${PYBIN}" "${ROOT}/T2Analysis/tools/ufile_pdf_parser/parse_ufile_pdf.py" \
  --pdf "${EXPORT_DIR}/ufile_return.pdf" \
  --out "${PARSE_DIR}"

"${PYBIN}" "${ROOT}/T2Analysis/tools/ufile_pdf_parser/verify_parse.py" \
  --parse-dir "${PARSE_DIR}"

echo "Created:"
echo "  ${EXPORT_DIR}"
echo "  ${PARSE_DIR}"

