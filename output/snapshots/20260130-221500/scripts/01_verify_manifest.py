#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path

from _lib import MANIFEST_PATH, get_source, load_manifest, sha256_file


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

    print("MANIFEST CHECK PASSED")
    print(f"- manifest: {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
