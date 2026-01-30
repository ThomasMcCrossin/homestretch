# UFile PDF parser (T2Analysis)

Goal: create a deterministic, reviewable parsed representation of UFile-exported T2 PDFs (diagnostics + GIFI tables) so LLMs can reference **structured artifacts** instead of “reading the PDF”.

## Safety

- This tool must only write under `T2Analysis/`.
- It should never modify accounting data, DBs, or snapshots.

## Usage

Create a venv and run the parser:

```bash
python3 -m venv T2Analysis/tools/ufile_pdf_parser/.venv
T2Analysis/tools/ufile_pdf_parser/.venv/bin/pip install -r T2Analysis/tools/ufile_pdf_parser/requirements.txt

T2Analysis/tools/ufile_pdf_parser/.venv/bin/python \
  T2Analysis/tools/ufile_pdf_parser/parse_ufile_pdf.py \
  --pdf T2Analysis/t2_attempts/FY2025/ufile/exports/latest/ufile_return.pdf \
  --out T2Analysis/t2_attempts/FY2025/ufile/parses/latest
```

## Outputs

The output directory contains:
- `meta.json` (parser version + source hash)
- `text/full_text.txt`
- `text/pages/page_XXX.txt`
- `tables/schedule_100.csv`
- `tables/schedule_125.csv`
- `tables/retained_earnings.csv`
- `tables/diagnostics.csv`

These files are intended to be compared back to the PDF until trusted.
