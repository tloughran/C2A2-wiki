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
  - TABS   come from the PAGE MANIFEST wiki/voice_guide/manifests.v2.json, via
           generate_page_tables.gen_destinations() -- the single derivation rule
           shared with the acceptance test, so this file and that test cannot
           disagree about what the manifest means.

           They used to be parsed from wiki/explorer.html (`var TABS`), which
           carries no display label, so the label was synthesized as
           `aka[0].title()`. Title-casing a spoken alias mangles every id that
           is not plain words: "rc document explorer" -> "Rc Document Explorer",
           "trv commentary" -> "Trv Commentary", "ai heartbeat" -> "Ai
           Heartbeat", and "start here" -> "Start Here" (the page is titled
           "Start here"). The manifest carries a real `identity.title` per
           surface, so the labels are now read, not guessed.

           The manifest is also checked AGAINST `var TABS`: the two rosters must
           name the same surfaces. The manifest supplies the label; explorer.html
           remains the authority on what switch_tab can actually reach, and a
           destination the shell cannot navigate to is a bug, not a label.

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
MANIFEST_V2 = ROOT / "wiki" / "voice_guide" / "manifests.v2.json"
OUT = ROOT / "wiki" / "voice_guide" / "destinations.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_page_tables import gen_destinations  # noqa: E402

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


def explorer_tab_keys() -> list[str]:
    """The explorer's switch_tab roster (`var TABS` keys) -- the reachability
    check only. The label and aliases come from the manifest.

    TABS objects contain no nested brackets, so a non-greedy `[...]` is safe."""
    html = EXPLORER.read_text(encoding="utf-8")
    m = re.search(r"var TABS = (\[.*?\]);", html, re.S)
    if not m:
        raise ValueError("var TABS not found in explorer.html")
    return re.findall(r"key:\s*'([^']+)'", m.group(1))


def parse_tabs() -> list[dict]:
    """The navigable surface roster, labels and aliases read from the manifest.

    Refuses on any disagreement with explorer.html's `var TABS`: a surface the
    manifest labels but switch_tab cannot reach would be a destination the
    shell offers and then fails to navigate to, and a surface explorer can
    reach but the manifest omits would silently drop out of the index."""
    v2 = json.loads(MANIFEST_V2.read_text(encoding="utf-8"))
    tabs = gen_destinations(v2)

    manifest_ids = [t["id"] for t in tabs]
    live_ids = explorer_tab_keys()
    missing = [k for k in live_ids if k not in manifest_ids]
    extra = [k for k in manifest_ids if k not in live_ids]
    if missing or extra:
        raise ValueError(
            "manifest/explorer tab roster mismatch -- "
            "in explorer.html but not the manifest: %s; "
            "in the manifest but not explorer.html: %s"
            % (missing or "none", extra or "none"))

    for t in tabs:
        if not t.get("label") or not isinstance(t.get("aka"), list) or not t["aka"]:
            raise ValueError("manifest surface %r lacks a usable label/aka: %r"
                             % (t["id"], t))

    # An alias that names two surfaces is worse than a missing alias: CCL's
    # resolveTab() returns `ambiguous` on more than one exact hit, so the word
    # stops working instead of resolving imperfectly. This is NOT hypothetical --
    # the v1 manifest's `tabs` (9 surfaces, no ai_heartbeat) and explorer.html's
    # `var TABS` (14 surfaces) each spelled "pulse" unambiguously within
    # themselves, and the v2 manifest's union of the two namespaces collides.
    # Refuse rather than ship a spoken word that used to work and now errors.
    seen: dict[str, str] = {}
    clashes: list[str] = []
    for t in tabs:
        for a in t["aka"]:
            key = a.strip().lower()
            if key in seen:
                clashes.append("%r names both %s and %s"
                               % (a, seen[key], t["id"]))
            else:
                seen[key] = t["id"]
    if clashes:
        raise ValueError(
            "manifest alias collisions -- resolveTab() would answer "
            "'ambiguous' for these, so one surface must give the alias up in "
            "manifests.v2.json: " + "; ".join(clashes))
    # Emit in explorer.html's tab order, so the index reads like the tab strip.
    order = {k: i for i, k in enumerate(live_ids)}
    return sorted(tabs, key=lambda t: order[t["id"]])


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
            "tabs": "wiki/voice_guide/manifests.v2.json (pages[].identity, "
                    "via generate_page_tables.gen_destinations); roster "
                    "cross-checked against wiki/explorer.html (var TABS)",
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
