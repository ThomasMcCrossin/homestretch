#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path

from _lib import MANIFEST_PATH, PROJECT_ROOT, get_source, load_manifest, sha256_file


def main() -> int:
    manifest = load_manifest()
    sources = manifest.get("sources") or {}
    if not isinstance(sources, dict):
        raise SystemExit(f"Invalid manifest structure: {MANIFEST_PATH}")

    errors: list[str] = []

    for source_key, cfg in sources.items():
        if not isinstance(cfg, dict):
            errors.append(f"{source_key}: not a mapping")
            continue
        kind = (cfg.get("kind") or "").strip()
        path_str = (cfg.get("path") or "").strip()
        sha_expected = (cfg.get("sha256") or "").strip()

        if not path_str:
            errors.append(f"{source_key}: missing path")
            continue

        path = Path(path_str)
        if not path.exists():
            errors.append(f"{source_key}: missing file/dir at {path}")
            continue

        if kind == "csv" and not sha_expected:
            errors.append(f"{source_key}: missing sha256 (run sha256sum {path})")

        if sha_expected and path.is_file():
            sha_actual = sha256_file(path)
            if sha_actual != sha_expected:
                errors.append(f"{source_key}: sha256 mismatch: expected {sha_expected} actual {sha_actual}")

        if kind == "docker_compose_project":
            compose_file = path / "docker-compose.yml"
            if not compose_file.exists():
                errors.append(f"{source_key}: expected docker-compose.yml at {compose_file}")

    if errors:
        print("MANIFEST CHECK FAILED\n")
        for e in errors:
            print(f"- {e}")
        return 1

    # Guardrail: FY2024 inventory should be repo-local so an old external estimate file can't accidentally re-enter the pipeline.
    try:
        inv_src = get_source(manifest, "inventory_count_fy2024_may31_estimated_csv")
        inv_path = Path(str(inv_src.get("path") or "")).expanduser()
        if inv_path.exists():
            try:
                inv_rel = inv_path.resolve().is_relative_to(PROJECT_ROOT.resolve())
            except Exception:
                inv_rel = str(inv_path.resolve()).startswith(str(PROJECT_ROOT.resolve()))
            if not inv_rel:
                print("MANIFEST WARNING:")
                print(
                    f"- inventory_count_fy2024_may31_estimated_csv points outside this repo: {inv_path}"
                )
                print("- This is allowed, but increases risk of regressions to deprecated inventory sheets.")
    except Exception:
        # Non-fatal; manifest validation should not fail due to missing optional guardrails.
        pass

    print("MANIFEST CHECK PASSED")
    print(f"- manifest: {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
