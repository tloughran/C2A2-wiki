#!/usr/bin/env python3
"""Regenerate data/*.json from the wiki filesystem.

Scans ../wiki/ (or --wiki-root) and produces:
  data/nodes.json        — list of {id, label, directory, date, color, group, size}
  data/links.json        — list of {source, target, type}  (indices into nodes)
  data/narrations.json   — {"YYYY-MM-DD": {brief, deep, voice}}
  data/metadata.json     — summary counts and date list

Narration preservation: if narrations.json already exists, existing entries are
kept; only dates with no entry get a generated fallback. This lets the daily
"cowork summary" content (which is richer than anything we can synthesize) stay
intact across regenerations. Pass --overwrite-narrations to force regeneration.

Usage:
    python3 tools/build_data.py                    # default: wiki at ../wiki/
    python3 tools/build_data.py --wiki-root ../wiki --out data
    python3 tools/build_data.py --overwrite-narrations
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# ---- Config ----

# Color per top-level directory. New directories get a hashed fallback color.
DIRECTORY_COLORS: dict[str, str] = {
    "agents": "#9B59B6",
    "traditions": "#3498DB",   # master color; individual traditions override below
    "architecture": "#E67E22",
    "flags": "#E74C3C",
    "decisions": "#2ECC71",
    "inbox": "#95A5A6",
    "review": "#F1C40F",
    "master": "#1ABC9C",
    "deferred": "#7F8C8D",
}

# Per-tradition colors so cross-tradition patterns read visually.
# Chosen to be distinguishable on the dark bg and distinct from the
# category colors above (agents purple, flags red, decisions green, etc.).
TRADITION_COLORS: dict[str, str] = {
    "friston":      "#3498DB",  # blue — flagship
    "hoffman":      "#E91E63",  # magenta/pink
    "levin":        "#1ABC9C",  # teal
    "kastrup":      "#8E44AD",  # violet
    "mcgilchrist":  "#00BCD4",  # cyan
    "fredrickson":  "#F39C12",  # amber
    "hawkins":      "#FF7043",  # coral
    "stump":        "#A1887F",  # warm taupe
    "carroll":      "#5DADE2",  # steel blue
    "arkanihamed":  "#F1C40F",  # gold
    "wolfram":      "#C0392B",  # warm red
}

# Directory name patterns that shouldn't become graph nodes
SKIP_PATTERNS = (
    ".obsidian", ".git", "node_modules", ".DS_Store",
    "__pycache__", ".vscode", ".idea",
)

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

# [[wikilink]] or [[path/to/file|alias]]
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")

# Max characters of markdown source to render into the detail panel.
# Keeps nodes.json bounded even for very long wiki files. The panel can
# link to the full source if anyone wants more than this.
CONTENT_PREVIEW_CHARS = 6000

# Tradition-name tokens that, when they appear in a file's body, create a
# soft "reference" link to that tradition's anchor node. Match whole-word
# lowercase after case-folding — keeps Tom's name ("Tom Loughran") from
# matching the "hram" substring in Wolfram, etc. The anchor node chosen is
# the tradition wiki file (traditions/<slug>/<Name>_Tradition_Wiki.md or
# whichever file is the natural hub).
TRADITION_MENTION_TERMS: dict[str, tuple[str, ...]] = {
    "friston":     ("friston",),
    "hoffman":     ("hoffman",),
    "levin":       ("levin",),
    "kastrup":     ("kastrup",),
    "mcgilchrist": ("mcgilchrist",),
    "fredrickson": ("fredrickson",),
    "hawkins":     ("hawkins",),
    "stump":       ("stump",),
    "carroll":     ("carroll",),
    "arkanihamed": ("arkani-hamed", "arkani hamed", "arkanihamed"),
    "wolfram":     ("wolfram",),
}


# ---- Helpers ----

def fallback_color(name: str) -> str:
    """Deterministic color for unknown directories. Pleasant dark-bg palette."""
    h = sum(ord(c) for c in name) % 360
    return f"hsl({h}, 55%, 55%)"


def extract_date(path: Path, text: str | None) -> str | None:
    """Try filename first (YYYY-MM-DD_*), then first date in text."""
    m = DATE_RE.match(path.name)
    if m:
        return m.group(1)
    if text:
        m = DATE_RE.search(text[:400])
        if m:
            return m.group(1)
    # Fall back to mtime
    try:
        ts = path.stat().st_mtime
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except OSError:
        return None


def extract_title(text: str, default: str) -> str:
    """First `# heading` in file, or provided default."""
    for line in text.splitlines()[:20]:
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return default


# Lazy-import markdown. If it's missing, we fall back to raw text preview
# (wrapped in a <pre>), which is less pretty but still readable.
_md_instance = None
def _markdown_to_html(src: str) -> str:
    global _md_instance
    try:
        import markdown  # type: ignore
        if _md_instance is None:
            _md_instance = markdown.Markdown(
                extensions=["fenced_code", "tables", "nl2br"],
                output_format="html",
            )
        _md_instance.reset()
        return _md_instance.convert(src)
    except Exception:
        # Minimal safe fallback: escape and wrap in <pre>.
        import html
        return f"<pre class=\"md-fallback\">{html.escape(src)}</pre>"


def build_content_html(text: str) -> str:
    """Render a markdown preview for the detail panel."""
    if not text:
        return ""
    snippet = text[:CONTENT_PREVIEW_CHARS]
    truncated = len(text) > CONTENT_PREVIEW_CHARS
    # Strip Obsidian-specific frontmatter (YAML between --- markers) so the
    # rendered preview starts at the prose.
    if snippet.startswith("---\n"):
        end = snippet.find("\n---\n", 4)
        if end != -1:
            snippet = snippet[end + 5 :]
    html = _markdown_to_html(snippet)
    if truncated:
        html += "<p class=\"md-truncated\"><em>… (preview truncated)</em></p>"
    return html


def should_skip(rel_path: str) -> bool:
    parts = Path(rel_path).parts
    return any(any(p == s or p.startswith(s) for s in SKIP_PATTERNS) for p in parts)


# ---- Scan ----

def scan_wiki(wiki_root: Path) -> tuple[list[dict], list[dict]]:
    files: list[Path] = []
    for path in wiki_root.rglob("*.md"):
        rel = path.relative_to(wiki_root).as_posix()
        if should_skip(rel):
            continue
        files.append(path)
    files.sort(key=lambda p: p.relative_to(wiki_root).as_posix())

    # Build nodes (first pass: path → index)
    nodes: list[dict] = []
    index_by_id: dict[str, int] = {}

    for path in files:
        rel = path.relative_to(wiki_root).as_posix()
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            text = ""

        parts = rel.split("/")
        top_dir = parts[0] if len(parts) > 1 else "root"
        directory = "/".join(parts[:-1]) if len(parts) > 1 else "root"

        # Tradition slug if this file lives under traditions/<slug>/ — used
        # for per-tradition coloring and for legend categorization.
        tradition = parts[1] if top_dir == "traditions" and len(parts) > 2 else None

        if tradition and tradition in TRADITION_COLORS:
            color = TRADITION_COLORS[tradition]
            group = f"traditions/{tradition}"
        else:
            color = DIRECTORY_COLORS.get(top_dir, fallback_color(top_dir))
            group = top_dir

        node = {
            "id": rel,
            "label": extract_title(text, path.stem.replace("_", " ").replace("-", " ")),
            "directory": directory,
            "date": extract_date(path, text),
            "color": color,
            "group": group,
            "tradition": tradition,  # null for non-tradition files
            "size": 5,
            "contentHtml": build_content_html(text),
        }
        index_by_id[rel] = len(nodes)
        nodes.append(node)

    # --- Tradition anchor discovery ---
    # Find the "hub" file for each tradition — we'll attach sibling/mention
    # links to these. Preference order:
    #   1. traditions/<slug>/*_Tradition_Wiki.md (or similar)
    #   2. traditions/<slug>/<slug>_wiki.md
    #   3. first file under traditions/<slug>/
    tradition_anchor: dict[str, int] = {}
    for rel, idx in index_by_id.items():
        parts = rel.split("/")
        if len(parts) < 3 or parts[0] != "traditions":
            continue
        slug = parts[1]
        label = nodes[idx].get("label", "").lower()
        if slug in tradition_anchor:
            # Existing anchor may be weaker — upgrade if label looks like "… Tradition Wiki"
            if "tradition wiki" in label and "tradition wiki" not in nodes[tradition_anchor[slug]].get("label", "").lower():
                tradition_anchor[slug] = idx
            continue
        tradition_anchor[slug] = idx

    # --- Build links (second pass) ---
    links: list[dict] = []
    link_seen: set[tuple[int, int]] = set()

    def add_link(src: int, tgt: int, kind: str) -> None:
        if src == tgt:
            return
        key = (src, tgt) if src < tgt else (tgt, src)
        if key in link_seen:
            return
        link_seen.add(key)
        links.append({"source": src, "target": tgt, "type": kind})

    # Pass 1: explicit [[wikilinks]]
    for path in files:
        rel = path.relative_to(wiki_root).as_posix()
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        src_idx = index_by_id[rel]
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            tgt_idx = resolve_wikilink(target, index_by_id)
            if tgt_idx is not None:
                add_link(src_idx, tgt_idx, "wikilink")

    # Pass 2: sibling links — every file in traditions/<slug>/ links back to
    # that tradition's anchor. Produces the radial cluster structure.
    for rel, idx in index_by_id.items():
        parts = rel.split("/")
        if len(parts) < 3 or parts[0] != "traditions":
            continue
        slug = parts[1]
        anchor = tradition_anchor.get(slug)
        if anchor is not None and anchor != idx:
            add_link(idx, anchor, "reference")

    # Pass 3: mention-based links — any file whose body mentions a tradition
    # name gets a soft link to that tradition's anchor. Produces the cross-
    # cluster edges. Skip files already in that tradition (redundant with
    # sibling links).
    for path in files:
        rel = path.relative_to(wiki_root).as_posix()
        try:
            text = path.read_text(encoding="utf-8", errors="replace").lower()
        except OSError:
            continue
        src_idx = index_by_id[rel]
        src_trad = nodes[src_idx].get("tradition")
        for slug, terms in TRADITION_MENTION_TERMS.items():
            if slug == src_trad:
                continue
            anchor = tradition_anchor.get(slug)
            if anchor is None:
                continue
            if any(term in text for term in terms):
                add_link(src_idx, anchor, "reference")

    return nodes, links


def resolve_wikilink(target: str, index_by_id: dict[str, int]) -> int | None:
    # Try as-is
    if target in index_by_id:
        return index_by_id[target]
    # Try with .md suffix
    if f"{target}.md" in index_by_id:
        return index_by_id[f"{target}.md"]
    # Try basename match (e.g. "Michael Levin" → "agents/01_levin_agent.md")
    lower = target.lower().replace(" ", "_")
    for key, idx in index_by_id.items():
        base = Path(key).stem.lower()
        if base == lower or base.endswith("_" + lower) or lower in base:
            return idx
    return None


# ---- Metadata ----

def build_metadata(nodes: list[dict]) -> dict:
    dir_counts = Counter(n["directory"] for n in nodes)
    tradition_dirs = {d for d in dir_counts if d.startswith("traditions/")}
    traditions_count = len({d.split("/", 1)[1] for d in tradition_dirs if "/" in d})
    findings_count = sum(c for d, c in dir_counts.items() if d == "flags" or "finding" in d.lower())
    decisions_count = sum(c for d, c in dir_counts.items() if d == "decisions" or d.startswith("decisions/"))
    # architecture/ files are not decisions per se; keep counts strict
    dates = sorted({n["date"] for n in nodes if n.get("date")})
    return {
        "total_files": len(nodes),
        "traditions_count": traditions_count,
        "findings_count": findings_count,
        "decisions_count": decisions_count,
        "dates": dates,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
    }


# ---- Narrations ----

def build_narrations(
    nodes: list[dict],
    wiki_root: Path,
    existing: dict | None = None,
    overwrite: bool = False,
) -> dict:
    """For each date with activity, produce brief/deep/voice narration.

    Priority:
      1. Existing narration (unless --overwrite-narrations)
      2. wiki/architecture/changelog/<date>_changes.md
      3. Cowork summaries in wiki/architecture/changelog/ (heuristic)
      4. Generated summary from files added/modified on that date
    """
    existing = existing or {}
    by_date: dict[str, list[dict]] = defaultdict(list)
    for n in nodes:
        if n.get("date"):
            by_date[n["date"]].append(n)

    narrations: dict[str, dict] = {}
    for date, date_nodes in sorted(by_date.items()):
        if not overwrite and date in existing and existing[date].get("brief"):
            narrations[date] = existing[date]
            continue

        brief, deep = fallback_narration(date, date_nodes, wiki_root)
        narrations[date] = {"brief": brief, "deep": deep, "voice": brief}

    # Keep pre-existing dates even if they have no nodes (manually authored)
    for date, entry in existing.items():
        if date not in narrations:
            narrations[date] = entry

    return narrations


def fallback_narration(date: str, nodes: list[dict], wiki_root: Path) -> tuple[str, str]:
    """Baseline narration: look for changelog/snapshot files; otherwise summarize."""
    changelog = wiki_root / "architecture" / "changelog" / f"{date}_changes.md"
    snapshot = wiki_root / "architecture" / "metrics" / f"{date}_snapshot.md"

    for path in (changelog, snapshot):
        if not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        # Look for a "Narrative Summary" or "Summary" section first
        for hdr in ("## Narrative Summary", "## Summary", "## Cowork summary", "## Overview"):
            idx = text.find(hdr)
            if idx >= 0:
                chunk = text[idx + len(hdr):].split("\n## ", 1)[0].strip()
                if chunk:
                    brief_lines = [l for l in chunk.splitlines() if l.strip()][:3]
                    brief = " ".join(brief_lines)[:280]
                    return brief, chunk[:1400]
        # Fallback: first 500 chars of body (skip frontmatter/header)
        body = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL).strip()
        body = re.sub(r"^#.*\n", "", body, count=1).strip()
        if body:
            brief = body.splitlines()[0][:280]
            return brief, body[:1400]

    # Pure generated fallback
    traditions = sorted({n["directory"].split("/", 1)[1]
                        for n in nodes if n["directory"].startswith("traditions/")})
    top_dirs = Counter(n["group"] for n in nodes).most_common(3)
    bits = []
    if traditions:
        bits.append(f"Activity in traditions: {', '.join(traditions)}")
    if top_dirs:
        bits.append("; " + ", ".join(f"{c} {d}" for d, c in top_dirs))
    bits.append(f" ({len(nodes)} files).")
    text = "".join(bits) if bits else f"{len(nodes)} files updated on {date}."
    return text, text


# ---- Main ----

def main() -> int:
    here = Path(__file__).resolve().parent
    project_root = here.parent            # tools/ → project root
    default_wiki = (project_root.parent / "wiki").resolve()
    default_out = (project_root / "data").resolve()

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--wiki-root", type=Path, default=default_wiki,
                    help=f"Path to wiki/ (default: {default_wiki})")
    ap.add_argument("--out", type=Path, default=default_out,
                    help=f"Output data directory (default: {default_out})")
    ap.add_argument("--overwrite-narrations", action="store_true",
                    help="Regenerate narrations.json from scratch (default: preserve existing entries)")
    args = ap.parse_args()

    wiki_root = args.wiki_root
    if not wiki_root.is_dir():
        print(f"ERROR: wiki root not found: {wiki_root}", file=sys.stderr)
        return 2

    out_dir = args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Scanning {wiki_root} ...")
    nodes, links = scan_wiki(wiki_root)
    print(f"  {len(nodes)} nodes, {len(links)} links")

    # Load existing narrations if present
    narrations_path = out_dir / "narrations.json"
    existing = {}
    if narrations_path.exists() and not args.overwrite_narrations:
        try:
            existing = json.loads(narrations_path.read_text())
            print(f"  preserving {len(existing)} existing narration entries")
        except json.JSONDecodeError:
            print("  existing narrations.json was invalid — regenerating")

    narrations = build_narrations(nodes, wiki_root, existing, args.overwrite_narrations)
    metadata = build_metadata(nodes)

    for fname, data in [
        ("nodes.json", nodes),
        ("links.json", links),
        ("narrations.json", narrations),
        ("metadata.json", metadata),
    ]:
        target = out_dir / fname
        target.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        # Show path relative to cwd when possible; fall back to absolute
        try:
            display = target.resolve().relative_to(Path.cwd())
        except ValueError:
            display = target.resolve()
        print(f"  wrote {display}  ({target.stat().st_size:,} bytes)")

    print(f"\nTotals: {metadata['total_files']} files, {metadata['traditions_count']} traditions, "
          f"{metadata['findings_count']} findings, {metadata['decisions_count']} decisions, "
          f"{len(metadata['dates'])} active dates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
