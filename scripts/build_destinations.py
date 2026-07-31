#!/usr/bin/env python3
"""build_destinations.py -- generate wiki/voice_guide/destinations.json.

Phase 3 of the voice guide (voice_guide_dev_pathway.md): the navigation index.
The guide's find_destination(query) tool needs a searchable list of everywhere it
can take the user, but the ~4,000 Sociogram nodes cannot fit in the prompt -- so
the shell fetches this index at load and searches it client-side, then navigate(id)
drives the tab's own functions (openNodeByLabel, switch_tab) to actually go there.

Source of truth, so this file never drifts from what is really reachable:
  - NODES  are parsed from the PUBLISHED wiki/wiki_narration.html (`const NODES`).
           That is exactly the roster the Sociogram displays and that
           openNodeByLabel() can open -- parsing the artifact keeps the index and
           the navigable set identical by construction (no separate extract, no
           Summa-vault dependency). Re-run this after any regen_sociogram.sh.
  - TABS   are parsed from wiki/explorer.html (`var TABS`), the same array that
           feeds the switch_tab enum. One roster, derived, not hand-copied.

Node content/references/color/size are DROPPED -- the index carries only what a
text search needs (id, label, group), keeping it a few hundred KB.

    python3 scripts/build_destinations.py            # write destinations.json
    python3 scripts/build_destinations.py --dry-run  # print counts, write nothing
"""
from __future__ import annotations
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOCIOGRAM = ROOT / "wiki" / "wiki_narration.html"
EXPLORER = ROOT / "wiki" / "explorer.html"
OUT = ROOT / "wiki" / "voice_guide" / "destinations.json"

SCHEMA = "c2a2-voice-destinations/1"


def _balanced_array(text: str, marker: str) -> str:
    """Return the `[...]` literal that follows `marker`, honoring string quoting
    so a `]` inside a node's content/references does not end the scan early."""
    start = text.index("[", text.index(marker))
    depth = 0
    instr = False
    esc = False
    for j in range(start, len(text)):
        c = text[j]
        if instr:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True
        elif c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return text[start:j + 1]
    raise ValueError("unterminated array after " + marker)


def parse_nodes() -> list[dict]:
    """The Sociogram's displayed node roster, trimmed to index fields."""
    html = SOCIOGRAM.read_text(encoding="utf-8")
    nodes = json.loads(_balanced_array(html, "const NODES = "))
    out = []
    for n in nodes:
        nid = n.get("id")
        if not nid:
            continue
        out.append({
            "id": nid,
            "label": n.get("label") or nid,
            "group": n.get("group", ""),
        })
    return out


def parse_tabs() -> list[dict]:
    """The explorer's tab roster (id + spoken aliases) from `var TABS`.

    TABS objects contain no nested brackets, so a non-greedy `[...]` is safe.
    Each object has exactly one `key:` and one `words:`; we pair them in order."""
    html = EXPLORER.read_text(encoding="utf-8")
    m = re.search(r"var TABS = (\[.*?\]);", html, re.S)
    if not m:
        raise ValueError("var TABS not found in explorer.html")
    block = m.group(1)
    keys = re.findall(r"key:\s*'([^']+)'", block)
    words = re.findall(r"words:\s*'([^']*)'", block)
    if len(keys) != len(words):
        raise ValueError("TABS key/words count mismatch: %d vs %d"
                         % (len(keys), len(words)))
    out = []
    for key, wd in zip(keys, words):
        aka = [w.strip() for w in wd.split(",") if w.strip()]
        label = aka[0].title() if aka else key.replace("_", " ").title()
        out.append({"id": key, "label": label, "aka": aka})
    return out


def build() -> dict:
    tabs = parse_tabs()
    nodes = parse_nodes()
    now = datetime.datetime.now().replace(microsecond=0).isoformat()
    return {
        "schema": SCHEMA,
        "authored_by": "build_destinations.py",
        "authored_at": now,
        "source": {
            "nodes": "wiki/wiki_narration.html (const NODES)",
            "tabs": "wiki/explorer.html (var TABS)",
        },
        "counts": {"tabs": len(tabs), "nodes": len(nodes)},
        "tabs": tabs,
        "nodes": nodes,
    }


def main() -> int:
    dry = "--dry-run" in sys.argv[1:]
    data = build()
    c = data["counts"]
    if c["tabs"] == 0 or c["nodes"] == 0:
        print("REFUSING: empty roster (tabs=%d nodes=%d) -- source parse failed"
              % (c["tabs"], c["nodes"]), file=sys.stderr)
        return 1
    payload = json.dumps(data, ensure_ascii=False, indent=None)
    print("destinations: %d tabs, %d nodes (%d KB)"
          % (c["tabs"], c["nodes"], len(payload.encode("utf-8")) // 1024))
    if dry:
        print("--dry-run: not written")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(payload, encoding="utf-8")
    print("wrote " + str(OUT.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
