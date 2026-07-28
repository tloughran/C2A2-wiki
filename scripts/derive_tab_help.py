#!/usr/bin/env python3
"""derive_tab_help.py — regenerate explorer.html tab help from knowledge/.

Canonical-source rule (wiki/architecture/voice_guide_state_bus.md): the voice
guide's per-page knowledge in wiki/voice_guide/knowledge/*.md is the single
source of truth. The explorer's own "?" help text — the `var descriptions = {...}`
map in explorer.html — must be DERIVED from it, never hand-maintained in parallel
(that parallel maintenance is the drift the whole state-bus contract exists to kill).

For each knowledge file with `affordance_state: default` and a `tab`, this script
sets descriptions[<tab>].body to that file's `## Purpose` section, whitespace-
collapsed to one line. Tabs with no default knowledge file are left untouched, so
partial rollout is safe. `title:` is never touched. No network, no git.

The janitor's `voice_knowledge_help_drift` check flags when a tab's help has
drifted from its Purpose; run this to reconcile.

    python3 scripts/derive_tab_help.py            # rewrite explorer.html in place
    python3 scripts/derive_tab_help.py --check    # exit 1 if any tab would change
    python3 scripts/derive_tab_help.py --dry-run  # print what would change; no write
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPLORER = ROOT / "wiki" / "explorer.html"
KNOWLEDGE_DIR = ROOT / "wiki" / "voice_guide" / "knowledge"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.split("#", 1)[0].strip()
    return fm, m.group(2)


def purpose_line(body: str) -> str | None:
    """The `## Purpose` section as one whitespace-collapsed line, or None."""
    m = re.search(r"##\s+Purpose\s*\n(.*?)(?:\n##\s|\Z)", body, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def _js_escape(s: str) -> str:
    """Escape for a single-quoted JS string literal (backslash then quote)."""
    return s.replace("\\", "\\\\").replace("'", "\\'")


def derive_map() -> dict[str, str]:
    """{tab data-src: derived help body} from every default knowledge file."""
    out: dict[str, str] = {}
    if not KNOWLEDGE_DIR.is_dir():
        return out
    for path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        fm, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm.get("affordance_state") != "default":
            continue
        tab = fm.get("tab")
        p = purpose_line(body)
        if tab and p:
            out[tab] = p
    return out


def apply_to_html(html: str, derived: dict[str, str]) -> tuple[str, list[str]]:
    """Return (new_html, changed_tabs). Only rewrites the body of tabs present in
    both `derived` and the descriptions map; leaves titles and other tabs intact."""
    changed: list[str] = []
    for tab, new_body in derived.items():
        pat = re.compile(
            r"('" + re.escape(tab) + r"':\s*\{\s*title:\s*'(?:[^'\\]|\\.)*',\s*"
            r"body:\s*')((?:[^'\\]|\\.)*)(')", re.S)
        m = pat.search(html)
        if not m:
            continue  # tab not in the descriptions map (or shape changed) — skip
        if m.group(2) == _js_escape(new_body):
            continue  # already in sync
        html = html[:m.start(2)] + _js_escape(new_body) + html[m.end(2):]
        changed.append(tab)
    return html, changed


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    html = EXPLORER.read_text(encoding="utf-8")
    derived = derive_map()
    if not derived:
        print("no default knowledge files with a Purpose — nothing to derive")
        return 0
    new_html, changed = apply_to_html(html, derived)
    if mode == "--check":
        if changed:
            print("OUT OF SYNC — these tabs would change: " + ", ".join(changed))
            return 1
        print("explorer help is in sync with knowledge/ (%d tab(s))" % len(derived))
        return 0
    if not changed:
        print("already in sync (%d tab(s) checked)" % len(derived))
        return 0
    if mode == "--dry-run":
        for t in changed:
            print("would update %s -> %s" % (t, derived[t][:70]))
        return 0
    EXPLORER.write_text(new_html, encoding="utf-8")
    print("updated explorer.html help for: " + ", ".join(changed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
