from __future__ import annotations

import csv
import hashlib
import os
import re
import sqlite3
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_FLOOR, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Iterable

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PROJECT_ROOT / "manifest" / "sources.yml"
RULES_PATH = PROJECT_ROOT / "overrides" / "vendor_profile_rules.yml"
DB_PATH = PROJECT_ROOT / "db" / "t2_final.db"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping YAML at {path}")
    return data


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def normalize_vendor(vendor_raw: str) -> str:
    v = (vendor_raw or "").lower()
    v = re.sub(r"[^\w\s]", " ", v)
    v = " ".join(v.split())
    return v


def extract_invoice_number(vendor_raw: str) -> str | None:
    """
    Best-effort extraction from Wave "Vendor / Details" strings like:
    - "Capital Foods - Bill 2548372"
    - "Mondoux - Bill 8100248"
    - "GFS - Bill 9007044619"
    """
    text = (vendor_raw or "").strip()
    if not text:
        return None
    m = re.search(r"\bBill\s+([0-9][0-9A-Za-z\\/-]+)\b", text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r"\bOrder\s*#\s*([0-9][0-9A-Za-z\\/-]+)\b", text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None


def dollars_to_cents(value: str | float | int | None) -> int:
    if value is None:
        return 0
    if isinstance(value, (int, float)):
        d = Decimal(str(value))
    else:
        s = str(value).strip()
        if not s:
            return 0
        s = s.replace(",", "")
        neg = False
        if s.startswith("(") and s.endswith(")"):
            neg = True
            s = s[1:-1].strip()
        try:
            d = Decimal(s)
        except InvalidOperation as e:
            raise ValueError(f"Invalid numeric value: {value!r}") from e
        if neg:
            d = -d
    cents = (d * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return int(cents)


def connect_db(path: Path = DB_PATH) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def load_manifest() -> dict[str, Any]:
    return load_yaml(MANIFEST_PATH)


def load_rules() -> dict[str, Any]:
    return load_yaml(RULES_PATH)


def get_source(manifest: dict[str, Any], key: str) -> dict[str, Any]:
    sources = manifest.get("sources") or {}
    src = sources.get(key)
    if not isinstance(src, dict):
        raise KeyError(f"Missing source '{key}' in manifest")
    return src


def iter_csv_rows(path: Path) -> Iterable[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k: (v if v is not None else "") for k, v in row.items()}


@dataclass(frozen=True)
class FiscalYear:
    fy: str
    start_date: str
    end_date: str


def fiscal_years_from_manifest(manifest: dict[str, Any]) -> list[FiscalYear]:
    fys = manifest.get("fiscal_years") or {}
    out: list[FiscalYear] = []
    for fy, cfg in fys.items():
        if not isinstance(cfg, dict):
            continue
        start = str(cfg.get("start_date") or "").strip()
        end = str(cfg.get("end_date") or "").strip()
        if start and end:
            out.append(FiscalYear(fy=str(fy), start_date=start, end_date=end))
    out.sort(key=lambda x: x.start_date)
    return out


def match_vendor_key(vendor_raw: str, rules: dict[str, Any]) -> str | None:
    norm = (vendor_raw or "").lower()
    matchers = (rules.get("wave_vendor_matchers") or {}) if isinstance(rules.get("wave_vendor_matchers"), dict) else {}
    for vendor_key, needles in matchers.items():
        if not isinstance(needles, list):
            continue
        for needle in needles:
            if needle and str(needle).lower() in norm:
                return str(vendor_key)
    return None


def allocation_rounding(amount_cents: int, weights: list[tuple[str, float]]) -> list[tuple[str, int]]:
    """
    Allocate amount_cents across keys using weights (sum ~= 1.0), ensuring exact cent total.
    Deterministic remainder distribution (largest fractional remainder first, then key order).
    """
    if amount_cents == 0 or not weights:
        return [(k, 0) for k, _ in weights]

    total_weight = sum(w for _, w in weights)
    if total_weight <= 0:
        raise ValueError("Weights must sum to > 0")

    scaled = [(k, w / total_weight) for k, w in weights]
    raw = [(k, amount_cents * w) for k, w in scaled]

    floors: list[tuple[str, int]] = [(k, int(Decimal(str(x)).to_integral_value(rounding=ROUND_FLOOR))) for k, x in raw]
    floor_sum = sum(v for _, v in floors)
    remainder = amount_cents - floor_sum

    if remainder == 0:
        return floors

    # Fractional parts for deterministic distribution.
    fracs = []
    for k, x in raw:
        frac = float(Decimal(str(x)) - Decimal(int(Decimal(str(x)).to_integral_value(rounding=ROUND_FLOOR))))
        fracs.append((k, frac))

    fracs.sort(key=lambda t: (-t[1], t[0]))

    alloc = {k: v for k, v in floors}
    for i in range(abs(remainder)):
        k = fracs[i % len(fracs)][0]
        alloc[k] += 1 if remainder > 0 else -1

    return [(k, alloc[k]) for k, _ in weights]
