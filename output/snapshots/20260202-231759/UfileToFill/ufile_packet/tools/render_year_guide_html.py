#!/usr/bin/env python3
"""
Render a readable, no-horizontal-scroll HTML view of the per-year UFILet2 fill guide.

Design goals:
- Comfortable on a 15" 1080p screen (bigger text, narrow readable measure)
- Sticky left navigation + search
- Collapsible long sections (tables) via <details>
- No external assets (offline-friendly / deterministic)
"""

from __future__ import annotations

import html as _html
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Heading:
    level: int
    title: str
    hid: str


def _slugify(text: str, used: set[str]) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if not s:
        s = "section"
    base = s
    i = 2
    while s in used:
        s = f"{base}-{i}"
        i += 1
    used.add(s)
    return s


def _format_inline(md: str) -> str:
    """
    Minimal inline formatting:
      - **bold**
      - `code`
      - _(none)_ => italic
      - [label](href)
    """
    s = _html.escape(md)

    # Inline code first (so we don't bold inside code).
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)

    # Links
    def _link(m: re.Match) -> str:
        label = m.group(1)
        href = m.group(2)
        return f'<a href="{_html.escape(href, quote=True)}">{_html.escape(label)}</a>'

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, s)

    # Bold
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)

    # Special-case _(none)_ markers (keeps us from over-applying underscore italics).
    s = s.replace("_(none)_", "<em>(none)</em>")
    return s


def _parse_table_block(lines: list[str]) -> tuple[str, int]:
    """
    Parse a markdown pipe table starting at lines[0]. Returns (html, consumed_line_count).
    """
    raw_rows: list[list[str]] = []
    i = 0
    while i < len(lines) and lines[i].lstrip().startswith("|"):
        row = lines[i].strip()
        # Strip leading/trailing |
        if row.startswith("|"):
            row = row[1:]
        if row.endswith("|"):
            row = row[:-1]
        cells = [c.strip() for c in row.split("|")]
        raw_rows.append(cells)
        i += 1

    if len(raw_rows) >= 2 and all(set(c.replace(":", "").strip()) <= {"-"} for c in raw_rows[1]):
        header = raw_rows[0]
        body = raw_rows[2:]
    else:
        header = raw_rows[0] if raw_rows else []
        body = raw_rows[1:] if raw_rows else []

    def _cell(c: str) -> str:
        return _format_inline(c)

    out: list[str] = []
    out.append('<div class="table-wrap">')
    out.append("<table>")
    if header:
        out.append("<thead><tr>")
        for c in header:
            out.append(f"<th>{_cell(c)}</th>")
        out.append("</tr></thead>")
    if body:
        out.append("<tbody>")
        for r in body:
            out.append("<tr>")
            for c in r:
                out.append(f"<td>{_cell(c)}</td>")
            out.append("</tr>")
        out.append("</tbody>")
    out.append("</table>")
    out.append("</div>")
    return "\n".join(out), i


def _md_fragment_to_html(md: str) -> str:
    """
    Minimal block renderer for our guide markdown (headings, lists, tables, paragraphs).
    """
    lines = md.splitlines()
    i = 0
    out: list[str] = []
    in_ul = False
    in_code = False
    code_lines: list[str] = []

    def _close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    while i < len(lines):
        line = lines[i].rstrip("\n")
        stripped = line.strip()

        # Fenced code blocks (```).
        if stripped.startswith("```"):
            _close_ul()
            if not in_code:
                in_code = True
                code_lines = []
            else:
                # Close code block.
                in_code = False
                code = "\n".join(code_lines).rstrip("\n")
                out.append(f"<pre><code>{_html.escape(code)}</code></pre>")
                code_lines = []
            i += 1
            continue

        if in_code:
            # Preserve raw lines inside the fenced block.
            code_lines.append(line)
            i += 1
            continue

        if not stripped:
            _close_ul()
            i += 1
            continue

        # Headings
        if stripped.startswith("### "):
            _close_ul()
            out.append(f"<h3>{_format_inline(stripped[4:])}</h3>")
            i += 1
            continue
        if stripped.startswith("#### "):
            _close_ul()
            out.append(f"<h4>{_format_inline(stripped[5:])}</h4>")
            i += 1
            continue
        if stripped.startswith("## "):
            _close_ul()
            out.append(f"<h2>{_format_inline(stripped[3:])}</h2>")
            i += 1
            continue
        if stripped.startswith("# "):
            _close_ul()
            out.append(f"<h1>{_format_inline(stripped[2:])}</h1>")
            i += 1
            continue

        # Tables
        if stripped.startswith("|"):
            _close_ul()
            table_html, consumed = _parse_table_block(lines[i:])
            out.append(table_html)
            i += consumed
            continue

        # Bullet list
        if stripped.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{_format_inline(stripped[2:])}</li>")
            i += 1
            continue

        # Paragraph (coalesce until blank / block start)
        _close_ul()
        para_lines = [stripped]
        j = i + 1
        while j < len(lines):
            nxt = lines[j].strip()
            if not nxt:
                break
            if nxt.startswith(("# ", "## ", "### ", "|", "- ")):
                break
            para_lines.append(nxt)
            j += 1
        out.append(f"<p>{_format_inline(' '.join(para_lines))}</p>")
        i = j

    _close_ul()
    # If the markdown had an unclosed code fence, render what we have.
    if in_code and code_lines:
        code = "\n".join(code_lines).rstrip("\n")
        out.append(f"<pre><code>{_html.escape(code)}</code></pre>")
    return "\n".join(out)


def _split_h2_sections(md: str) -> tuple[str, list[tuple[str, str]]]:
    """
    Returns (prefix_md, [(h2_title, h2_body_md), ...])
    """
    parts = md.splitlines()
    prefix_lines: list[str] = []
    sections: list[tuple[str, list[str]]] = []

    current_title: str | None = None
    current_body: list[str] = []
    seen_first_h2 = False

    for line in parts:
        if line.startswith("## "):
            seen_first_h2 = True
            if current_title is not None:
                sections.append((current_title, current_body))
            current_title = line[3:].strip()
            current_body = []
            continue
        if not seen_first_h2:
            prefix_lines.append(line)
        else:
            current_body.append(line)

    if current_title is not None:
        sections.append((current_title, current_body))

    return "\n".join(prefix_lines).strip() + "\n", [(t, "\n".join(b).rstrip() + "\n") for t, b in sections]


def _collapse_tables_in_section(section_html: str, *, title: str) -> str:
    """
    Wrap the *first* table in a <details> for long sections; keep content visible by default.
    """
    collapse_titles = {
        "Balance sheet (GIFI Schedule 100)",
        "Income statement (GIFI Schedule 125)",
        "Capital cost allowance (UFile screen)",
    }
    if title not in collapse_titles:
        return section_html

    idx = section_html.find("<table>")
    if idx == -1:
        return section_html

    before = section_html[:idx].rstrip()
    after = section_html[idx:]
    return (
        before
        + "\n"
        + '<details class="fold" open>\n'
        + '  <summary>Table (click to collapse)</summary>\n'
        + '  <div class="fold-body">\n'
        + after
        + "\n  </div>\n</details>\n"
    )


def render_year_guide_html(packet: dict, fy: str, *, md_guide: str) -> str:
    entity = packet.get("entity", {}) if isinstance(packet.get("entity"), dict) else {}
    years = packet.get("years", {}) if isinstance(packet.get("years"), dict) else {}
    year = years.get(fy, {}) if isinstance(years.get(fy), dict) else {}

    prefix_md, h2_sections = _split_h2_sections(md_guide)
    used_ids: set[str] = set()
    nav: list[Heading] = []

    # Title from first markdown h1 if present; else FY.
    m = re.search(r"(?m)^#\s+(.+)$", md_guide)
    title = m.group(1).strip() if m else f"UFILet2 Fill Guide — {fy}"

    # Quick badges
    pos = year.get("positions", {}) if isinstance(year.get("positions"), dict) else {}
    cca_required = (pos.get("cca_required") or {}).get("value") is True
    book_fixed = (pos.get("book_fixed_assets_present") or {}).get("value") is True

    sections_html: list[str] = []
    for sec_title, sec_body_md in h2_sections:
        sid = _slugify(sec_title, used_ids)
        nav.append(Heading(level=2, title=sec_title, hid=sid))
        body_html = _md_fragment_to_html(sec_body_md)
        body_html = _collapse_tables_in_section(body_html, title=sec_title)
        sections_html.append(f'<section class="sec" id="{sid}"><h2>{_format_inline(sec_title)}</h2>\n{body_html}\n</section>')

    prefix_html = _md_fragment_to_html(prefix_md)

    def _badge(label: str, kind: str) -> str:
        return f'<span class="badge {kind}">{_html.escape(label)}</span>'

    badges = []
    badges.append(_badge(fy, "fy"))
    if cca_required:
        badges.append(_badge("CCA", "cca"))
    if book_fixed:
        badges.append(_badge("Book fixed assets", "book"))

    legal_name = str(entity.get("legal_name") or "").strip()
    bn = str(entity.get("bn") or "").strip()
    period = (year.get("fiscal_period") or {}) if isinstance(year.get("fiscal_period"), dict) else {}
    period_txt = ""
    if period.get("start") and period.get("end"):
        period_txt = f"{period.get('start')} \u2192 {period.get('end')}"

    nav_items = "\n".join(
        f'<a class="nav-item" href="#{h.hid}" data-title="{_html.escape(h.title.lower())}">{_html.escape(h.title)}</a>'
        for h in nav
    )

    html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{_html.escape(title)}</title>
  <style>
    :root {{
      --paper: #fbf6ea;
      --paper-2: #f7f0df;
      --ink: #191713;
      --muted: #6f6558;
      --rule: #e4d8c6;
      --accent: #0b5f4e;
      --accent-2: #b54a2b;
      --shadow: 0 12px 36px rgba(18, 15, 10, 0.10);
      --shadow-soft: 0 10px 22px rgba(18, 15, 10, 0.08);
      --radius: 16px;
      --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      --serif: "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
      --sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
    }}

    * {{ box-sizing: border-box; }}
    html, body {{ height: 100%; }}
    body {{
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(1100px 900px at 18% 10%, rgba(11, 95, 78, 0.08), rgba(0,0,0,0) 60%),
        radial-gradient(900px 700px at 92% 18%, rgba(181, 74, 43, 0.08), rgba(0,0,0,0) 55%),
        linear-gradient(180deg, var(--paper), var(--paper-2));
      font-family: var(--sans);
      font-size: 18px;
      line-height: 1.5;
      overflow-x: hidden;
    }}

    @keyframes riseIn {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* subtle paper grain */
    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      opacity: 0.10;
      background-image:
        repeating-linear-gradient(0deg, rgba(0,0,0,0.035), rgba(0,0,0,0.035) 1px, transparent 1px, transparent 4px),
        repeating-linear-gradient(90deg, rgba(0,0,0,0.02), rgba(0,0,0,0.02) 1px, transparent 1px, transparent 6px);
      mix-blend-mode: multiply;
    }}

    .top {{
      padding: 22px 18px 8px;
    }}
    .top-inner {{
      max-width: 1240px;
      margin: 0 auto;
      display: flex;
      gap: 16px;
      align-items: flex-end;
      justify-content: space-between;
    }}
    .brand {{
      display: grid;
      gap: 6px;
    }}
    .brand h1 {{
      margin: 0;
      font-family: var(--serif);
      font-weight: 800;
      letter-spacing: -0.02em;
      font-size: 28px;
      line-height: 1.1;
    }}
    .brand .meta {{
      color: var(--muted);
      font-size: 14px;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .badges {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      justify-content: flex-end;
      align-items: center;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: 1px solid var(--rule);
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(255,255,255,0.55);
      box-shadow: var(--shadow-soft);
      font-size: 13px;
      color: var(--muted);
      white-space: nowrap;
    }}
    .badge.fy {{ color: var(--ink); border-color: rgba(25,23,19,0.18); }}
    .badge.cca {{ color: var(--accent); border-color: rgba(11,95,78,0.35); }}
    .badge.book {{ color: var(--accent-2); border-color: rgba(181,74,43,0.35); }}

    .shell {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 10px 18px 44px;
      display: grid;
      grid-template-columns: 320px minmax(0, 1fr);
      gap: 18px;
    }}

    .nav {{
      position: sticky;
      top: 12px;
      align-self: start;
      border: 1px solid var(--rule);
      border-radius: var(--radius);
      background: rgba(255,255,255,0.62);
      box-shadow: var(--shadow);
      overflow: hidden;
      animation: riseIn 420ms ease-out both;
    }}
    .nav-head {{
      padding: 14px 14px 10px;
      border-bottom: 1px solid var(--rule);
      background:
        linear-gradient(135deg, rgba(11,95,78,0.09), rgba(255,255,255,0) 55%),
        linear-gradient(0deg, rgba(255,255,255,0.70), rgba(255,255,255,0.70));
    }}
    .nav-title {{
      font-family: var(--serif);
      font-size: 16px;
      font-weight: 700;
      letter-spacing: 0.01em;
      margin: 0 0 10px 0;
    }}
    .search {{
      width: 100%;
      border: 1px solid rgba(25,23,19,0.18);
      border-radius: 12px;
      padding: 10px 12px;
      font-size: 14px;
      background: rgba(255,255,255,0.75);
      outline: none;
    }}
    .search:focus {{
      border-color: rgba(11,95,78,0.55);
      box-shadow: 0 0 0 4px rgba(11,95,78,0.10);
    }}
    .nav-body {{
      max-height: calc(100vh - 140px);
      overflow: auto;
      padding: 10px 8px 12px;
    }}
    .nav-item {{
      display: block;
      padding: 10px 10px;
      border-radius: 12px;
      text-decoration: none;
      color: var(--ink);
      font-size: 15px;
      line-height: 1.2;
      border: 1px solid transparent;
    }}
    .nav-item:hover {{
      background: rgba(11,95,78,0.08);
      border-color: rgba(11,95,78,0.16);
    }}
    .nav-item.active {{
      background: rgba(181,74,43,0.10);
      border-color: rgba(181,74,43,0.22);
    }}

    .doc {{
      border: 1px solid var(--rule);
      border-radius: var(--radius);
      background: rgba(255,255,255,0.66);
      box-shadow: var(--shadow);
      overflow: hidden;
      animation: riseIn 520ms ease-out both;
    }}
    .doc-inner {{
      padding: 22px 22px 26px;
      max-width: 920px;
    }}

    h1, h2, h3 {{
      font-family: var(--serif);
      margin: 0;
      letter-spacing: -0.01em;
    }}
    h1 {{
      font-size: 30px;
      line-height: 1.12;
      margin-bottom: 6px;
    }}
    h2 {{
      font-size: 22px;
      line-height: 1.18;
      margin: 22px 0 10px;
      position: relative;
      padding-left: 14px;
    }}
    h2::before {{
      content: "";
      position: absolute;
      left: 0;
      top: 0.12em;
      bottom: 0.12em;
      width: 6px;
      border-radius: 10px;
      background: linear-gradient(180deg, rgba(11,95,78,0.85), rgba(181,74,43,0.72));
      opacity: 0.85;
    }}
    h3 {{
      font-size: 18px;
      margin: 14px 0 8px;
      color: rgba(25,23,19,0.92);
    }}
    h4 {{
      font-size: 16px;
      margin: 12px 0 6px;
      color: rgba(25,23,19,0.88);
    }}
    p {{ margin: 10px 0; }}
    ul {{ margin: 10px 0 10px 22px; padding: 0; }}
    li {{ margin: 6px 0; }}
    code {{
      font-family: var(--mono);
      font-size: 0.92em;
      background: rgba(11,95,78,0.08);
      border: 1px solid rgba(11,95,78,0.20);
      padding: 2px 6px;
      border-radius: 9px;
      word-break: break-word;
      overflow-wrap: anywhere;
    }}
    pre {{
      margin: 10px 0;
      padding: 12px 14px;
      border-radius: 14px;
      background: rgba(247,240,223,0.55);
      border: 1px solid rgba(228,216,198,0.95);
      box-shadow: 0 10px 18px rgba(18,15,10,0.05);
      white-space: pre-wrap; /* no horizontal scroll */
      overflow-wrap: anywhere;
      word-break: break-word;
    }}
    pre code {{
      background: transparent;
      border: none;
      padding: 0;
    }}
    strong {{ font-weight: 800; }}
    a {{ color: var(--accent); text-decoration-thickness: 2px; text-underline-offset: 2px; }}
    a:hover {{ color: rgba(11,95,78,0.85); }}

    .table-wrap {{
      width: 100%;
      overflow: hidden;
      border-radius: 14px;
      border: 1px solid var(--rule);
      background: rgba(255,255,255,0.62);
      box-shadow: 0 8px 18px rgba(18,15,10,0.06);
      margin: 10px 0;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
    }}
    th, td {{
      padding: 10px 10px;
      border-bottom: 1px solid rgba(228,216,198,0.75);
      vertical-align: top;
      text-align: left;
      font-size: 15px;
      line-height: 1.35;
      overflow-wrap: anywhere;
      word-break: break-word;
      white-space: normal;
    }}
    th {{
      font-family: var(--sans);
      text-transform: uppercase;
      letter-spacing: 0.07em;
      font-size: 12px;
      color: rgba(25,23,19,0.70);
      background: rgba(247,240,223,0.70);
      border-bottom: 1px solid rgba(228,216,198,0.95);
    }}
    tr:last-child td {{ border-bottom: none; }}

    details.fold {{
      margin: 10px 0;
      border: 1px dashed rgba(25,23,19,0.20);
      border-radius: 14px;
      background: rgba(255,255,255,0.48);
      overflow: hidden;
    }}
    details.fold > summary {{
      cursor: pointer;
      padding: 12px 12px;
      font-family: var(--sans);
      font-size: 14px;
      color: rgba(25,23,19,0.82);
      background: linear-gradient(0deg, rgba(255,255,255,0.72), rgba(255,255,255,0.72));
      list-style: none;
    }}
    details.fold > summary::-webkit-details-marker {{ display: none; }}
    details.fold > summary::after {{
      content: "▾";
      float: right;
      color: rgba(25,23,19,0.55);
    }}
    details.fold[open] > summary::after {{ content: "▴"; }}
    .fold-body {{ padding: 0 12px 12px; }}

    @media (max-width: 980px) {{
      .shell {{
        grid-template-columns: 1fr;
      }}
      .nav {{
        position: relative;
        top: 0;
      }}
      .doc-inner {{
        padding: 18px 16px 22px;
      }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      * {{ scroll-behavior: auto !important; transition: none !important; }}
      .nav, .doc {{ animation: none !important; }}
    }}

    @media print {{
      body {{ background: white; }}
      body::before {{ display: none; }}
      .nav {{ display: none; }}
      .shell {{ grid-template-columns: 1fr; }}
      .doc {{ box-shadow: none; border: none; }}
      .doc-inner {{ max-width: none; }}
      details.fold {{ border-style: solid; }}
      details.fold[open] > summary {{ display: none; }}
    }}
  </style>
</head>
<body>
  <header class="top">
    <div class="top-inner">
      <div class="brand">
        <h1>{_html.escape(legal_name or title)}</h1>
        <div class="meta">
          {f"<span><strong>BN</strong> { _html.escape(bn) }</span>" if bn else ""}
          {f"<span><strong>Period</strong> { _html.escape(period_txt) }</span>" if period_txt else ""}
        </div>
      </div>
      <div class="badges">
        {''.join(badges)}
      </div>
    </div>
  </header>

  <div class="shell">
    <aside class="nav" aria-label="Contents">
      <div class="nav-head">
        <div class="nav-title">Contents</div>
        <input class="search" id="search" type="search" placeholder="Search sections…  (press /)" />
      </div>
      <div class="nav-body" id="nav">
        {nav_items}
      </div>
    </aside>

    <main class="doc">
      <div class="doc-inner" id="doc">
        <article>
          {prefix_html}
          {''.join(sections_html)}
        </article>
      </div>
    </main>
  </div>

  <script>
    (function() {{
      const search = document.getElementById('search');
      const nav = document.getElementById('nav');
      const items = Array.from(nav.querySelectorAll('.nav-item'));

      function applyFilter(q) {{
        const needle = (q || '').trim().toLowerCase();
        let first = null;
        for (const a of items) {{
          const t = a.dataset.title || '';
          const ok = !needle || t.includes(needle);
          a.style.display = ok ? 'block' : 'none';
          if (ok && !first) first = a;
        }}
        return first;
      }}

      search.addEventListener('input', () => applyFilter(search.value));

      // Focus search with "/"
      document.addEventListener('keydown', (e) => {{
        if (e.key === '/' && document.activeElement !== search) {{
          e.preventDefault();
          search.focus();
        }}
        if (e.key === 'Enter' && document.activeElement === search) {{
          const first = applyFilter(search.value);
          if (first) first.click();
        }}
      }});

      // Active section highlighting
      const headings = items.map(a => {{
        const id = a.getAttribute('href').slice(1);
        return {{ a, el: document.getElementById(id) }};
      }}).filter(x => x.el);

      const obs = new IntersectionObserver((entries) => {{
        entries.sort((a,b) => b.intersectionRatio - a.intersectionRatio);
        const top = entries.find(e => e.isIntersecting);
        if (!top) return;
        for (const h of headings) h.a.classList.remove('active');
        const hit = headings.find(h => h.el === top.target);
        if (hit) hit.a.classList.add('active');
      }}, {{ root: null, rootMargin: '-20% 0px -70% 0px', threshold: [0.01, 0.1, 0.25, 0.5] }});

      for (const h of headings) obs.observe(h.el);
    }})();
  </script>
</body>
</html>
"""
    return html_doc
