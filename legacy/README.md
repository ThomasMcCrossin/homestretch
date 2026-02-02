# legacy/

This directory contains archived, non-authoritative artifacts from earlier filing attempts.

Goals:
- Keep the working tree clean and prevent LLMs/tools from confusing legacy attempts with the current filing packet.
- Preserve local history (PDF exports, parses, diffs, debug artifacts) without committing them.

Rules:
- Anything under legacy/ should be gitignored (except this README).
- The authoritative filing artifacts are under:
  - UfileToFill/ufile_packet/packet.json
  - UfileToFill/ufile_packet/years/FY*/UFILet2_FILL_GUIDE.(html|md)
  - audit_packages/FY*/
