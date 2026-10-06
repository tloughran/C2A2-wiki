#!/usr/bin/env python3
"""Generate all six page tables from the one v2 manifest, and diff them.

Why this exists
---------------
`explorer_manifest_audit_2026-10-04.md` section 8 proposes a v2 manifest with a
single `identity` block per surface and makes one falsifiable claim about it:

    "Every one of them can be *generated* from this block: TABS from `route`,
    destinations.json from `identity` + `items`, descriptions from `explain`,
    KNOWLEDGE from `narration.knowledge_file`, FIND_TABS from
    `capability.find_contract`. That is the acceptance test for v2: no
    hand-maintained page table survives it."

This script is that test. It reads `wiki/voice_guide/manifests.v2.json`, emits
each of the six tables, parses the SIX LIVE TABLES out of the files that hold
them, and diffs. It modifies nothing.

The rule that makes the test mean anything
------------------------------------------
A difference is NOT to be resolved by adding a special case here. Every
derivation below is stated as one rule applied uniformly to all 24 pages. Where
a live table could only be reproduced by a per-page exception, this script emits
the rule's output and REPORTS the difference; the exception is then argued, in
prose, in `architecture/manifest_schema_acceptance_test_2026-10-04.md`, as either
a schema insufficiency, a stale table, or a deliberate divergence. A clean diff
bought with a special case would make the test pass and prove nothing.

The six, and where they really live (verified 2026-10-04, not taken from the audit)
----------------------------------------------------------------------------------
    TABS            wiki/explorer.html                `var TABS = [...]`
    manifests tabs  wiki/voice_guide/manifests.json   `.tabs` (9 keys)
    descriptions    wiki/explorer.html                `var descriptions = {...}` in showHelp
    KNOWLEDGE       wiki/explorer.html                `var KNOWLEDGE = {...}`
    destinations    wiki/voice_guide/destinations.json `.tabs` (13 rows)
    FIND_TABS       scripts/test_voice_shell.cjs      `const FIND_TABS = [...]`

Two of the six are already partly generated, which the audit does not say:
`destinations.json` is written whole by `build_destinations.py` from `var TABS`,
and `descriptions[].body` is rewritten by `derive_tab_help.py` from the knowledge
files. Only the membership and the titles are hand-maintained there.

Usage
-----
    python3 scripts/generate_page_tables.py --diff          # the acceptance test
    python3 scripts/generate_page_tables.py --emit tabs     # print one table
    python3 scripts/generate_page_tables.py --emit all      # print all six
    python3 scripts/generate_page_tables.py --list-rules    # the derivation rules

Exit code: 0 if every table matches, 1 if any differs. The expected result on
first run is 1; see the acceptance-test document for what each difference means.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_V2 = ROOT / "wiki" / "voice_guide" / "manifests.v2.json"
EXPLORER = ROOT / "wiki" / "explorer.html"
MANIFESTS_V1 = ROOT / "wiki" / "voice_guide" / "manifests.json"
DESTINATIONS = ROOT / "wiki" / "voice_guide" / "destinations.json"
VOICE_TEST = ROOT / "scripts" / "test_voice_shell.cjs"
KNOWLEDGE_DIR = ROOT / "wiki" / "voice_guide" / "knowledge"

UNKNOWN = "unknown"

RULES = """\
R-TABS         one row per page with route.kind in {tab, chapter}, manifest order.
               kind  = 'chapter' if route.kind == 'chapter'
                       else 'edu' if route.row == 'row2-edu' else 'tools'
               id    = route.button_id        (chapters only)
               src   = route.data_src         (tabs only)
               words = ', '.join(identity.aka)

R-MANIFESTS    one entry per page with coverage.v1_present, keyed identity.key.
               aka = identity.aka ; tier = identity.tier

R-DESCRIPTIONS one entry per page with explain.shell_entry, plus one per
               sections[] entry keyed '__section:<name>'.
               key   = identity.path without the 'wiki/' prefix
               title = explain.title
               body  = the '## Purpose' section of narration.knowledge_file,
                       whitespace-collapsed -- the same derivation
                       derive_tab_help.py already performs.

R-KNOWLEDGE    key = basename(identity.path), value = knowledge file stem.
               Membership follows how the shell USES the table: it looks the
               active frame's basename up, so every page that can BE the active
               frame must be present -- route.kind in {tab, chapter} always,
               null when it has no knowledge file. Other route kinds appear only
               if a knowledge file actually exists. (Derived from the consumer at
               explorer.html, not chosen to flatter the diff: the same rule
               predicts rc_sandbox's literal null AND community_cards' presence.)

R-DESTINATIONS same membership as R-TABS.
               id = identity.key ; label = identity.title ; aka = identity.aka

R-FIND_TABS    one row per page with capability.find_expected == 'full'.
               row = [route.data_src, capability.find_probe, True]
               NOTE: find_expected and find_probe are schema revisions R5/R6 --
               they do not exist in section 8, and their values were read off the
               live FIND_TABS table because nothing else in the project records
               them. This diff therefore tests EXPRESSIVENESS only. It is not
               independent evidence, and is reported as such.
"""


# ---------------------------------------------------------------- loading


def load_v2() -> dict:
    return json.loads(MANIFEST_V2.read_text(encoding="utf-8"))


def purpose_line(knowledge_file: str | None) -> str | None:
    """The '## Purpose' section of a knowledge file as one collapsed line.

    Same extraction as derive_tab_help.py, deliberately: the body of a
    descriptions entry is already generated from this today.
    """
    if not knowledge_file or knowledge_file == UNKNOWN:
        return None
    path = ROOT / "wiki" / knowledge_file
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    body = re.sub(r"^---\n.*?\n---\n?", "", text, flags=re.S)
    m = re.search(r"##\s+Purpose\s*\n(.*?)(?:\n##\s|\Z)", body, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def _rel(path: str) -> str:
    return path[len("wiki/"):] if path.startswith("wiki/") else path


def _is_tabbish(page: dict) -> bool:
    return page["identity"]["route"]["kind"] in ("tab", "chapter")


# ---------------------------------------------------------------- emitters


def gen_tabs(v2: dict) -> list[dict]:
    out = []
    for key, page in v2["pages"].items():
        ident = page["identity"]
        route = ident["route"]
        if not _is_tabbish(page):
            continue
        if route["kind"] == "chapter":
            kind = "chapter"
        else:
            kind = "edu" if route.get("row") == "row2-edu" else "tools"
        row: dict = {"key": key, "kind": kind}
        if kind == "chapter":
            row["id"] = route.get("button_id")
        else:
            row["src"] = route.get("data_src")
        aka = ident.get("aka")
        row["words"] = ", ".join(aka) if isinstance(aka, list) else UNKNOWN
        out.append(row)
    return out


def gen_manifests(v2: dict) -> dict:
    out = {}
    for key, page in v2["pages"].items():
        if not page.get("coverage", {}).get("v1_present"):
            continue
        out[key] = {"aka": page["identity"].get("aka"),
                    "tier": page["identity"].get("tier")}
    return out


def gen_descriptions(v2: dict) -> dict:
    out = {}
    for name, sec in v2.get("sections", {}).items():
        if sec.get("explain", {}).get("shell_entry"):
            out["__section:" + name] = {"title": sec["explain"].get("title"),
                                        "body": None}
    for _key, page in v2["pages"].items():
        explain = page.get("explain") or {}
        if explain == UNKNOWN or not explain.get("shell_entry"):
            continue
        narration = page.get("narration") or {}
        kf = narration.get("knowledge_file") if narration != UNKNOWN else None
        out[_rel(page["identity"]["path"])] = {
            "title": explain.get("title"),
            "body": purpose_line(kf),
        }
    return out


def gen_knowledge(v2: dict) -> tuple[dict, list[str]]:
    """The KNOWLEDGE map, plus any basename collisions the rule produces."""
    out: dict = {}
    collisions: list[str] = []
    for key, page in v2["pages"].items():
        narration = page.get("narration") or {}
        if narration == UNKNOWN:
            continue
        kf = narration.get("knowledge_file")
        if kf == UNKNOWN:
            continue
        if not _is_tabbish(page) and kf is None:
            continue
        base = Path(page["identity"]["path"]).name
        value = Path(kf).name[:-len(".md")] if kf else None
        if base in out and out[base] != value:
            collisions.append(
                "%s: %r (from %s) collides with the existing %r"
                % (base, value, key, out[base]))
        out[base] = value
    return out, collisions


def gen_destinations(v2: dict) -> list[dict]:
    out = []
    for key, page in v2["pages"].items():
        if not _is_tabbish(page):
            continue
        ident = page["identity"]
        out.append({"id": key, "label": ident.get("title"),
                    "aka": ident.get("aka")})
    return out


def gen_find_tabs(v2: dict) -> list[list]:
    out = []
    for _key, page in v2["pages"].items():
        cap = page.get("capability") or {}
        if cap == UNKNOWN or cap.get("find_expected") != "full":
            continue
        out.append([page["identity"]["route"].get("data_src"),
                    cap.get("find_probe"), True])
    return out


# ---------------------------------------------------------------- live parsers


def _balanced(text: str, marker: str, open_ch: str, close_ch: str) -> str:
    """The balanced literal following `marker`, honoring JS string quoting."""
    start = text.index(open_ch, text.index(marker))
    depth = 0
    quote = None
    esc = False
    for j in range(start, len(text)):
        c = text[j]
        if quote:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == quote:
                quote = None
            continue
        if c in "\"'":
            quote = c
        elif c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return text[start:j + 1]
    raise ValueError("unterminated literal after " + marker)


def live_tabs() -> list[dict]:
    """`var TABS` from explorer.html, field by field."""
    block = _balanced(EXPLORER.read_text(encoding="utf-8"), "var TABS = ", "[", "]")
    rows = []
    for obj in re.findall(r"\{[^{}]*\}", block):
        row: dict = {}
        for field in ("key", "kind", "id", "src", "words"):
            m = re.search(field + r":\s*'([^']*)'", obj)
            if m:
                row[field] = m.group(1)
        rows.append(row)
    return rows


def live_manifests() -> dict:
    tabs = json.loads(MANIFESTS_V1.read_text(encoding="utf-8"))["tabs"]
    return {k: {"aka": v.get("aka"), "tier": v.get("tier")}
            for k, v in tabs.items() if not k.startswith("_")}


def _js_unescape(s: str) -> str:
    """Undo a single-quoted JS string literal's escapes.

    NOT `unicode_escape`: that decodes byte-by-byte and corrupts every
    multi-byte UTF-8 character in the file (it reported two false body
    mismatches before this was fixed -- the repo's own
    `derive_tab_help.py --check` is what caught the discrepancy).
    """
    s = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)
    return re.sub(r"\\(.)", lambda m: m.group(1), s)


def live_descriptions() -> dict:
    """`var descriptions` from showHelp. Parsed as JS object literals."""
    block = _balanced(EXPLORER.read_text(encoding="utf-8"),
                      "var descriptions = ", "{", "}")
    out = {}
    # Each entry is   'key': {\n title: '...',\n body: '...'\n },
    for m in re.finditer(r"'((?:[^'\\]|\\.)*)':\s*\{(.*?)\n    \}", block, re.S):
        key = _js_unescape(m.group(1))
        inner = m.group(2)
        vals = {}
        for field in ("title", "body"):
            fm = re.search(field + r":\s*'((?:[^'\\]|\\.)*)'", inner, re.S)
            if fm:
                vals[field] = _js_unescape(fm.group(1))
        out[key] = {"title": vals.get("title"), "body": vals.get("body")}
    return out


def live_knowledge() -> dict:
    block = _balanced(EXPLORER.read_text(encoding="utf-8"),
                      "var KNOWLEDGE = ", "{", "}")
    out = {}
    for m in re.finditer(r"'([^']+)':\s*(?:'([^']*)'|null)", block):
        out[m.group(1)] = m.group(2)
    return out


def live_destinations() -> list[dict]:
    return json.loads(DESTINATIONS.read_text(encoding="utf-8"))["tabs"]


def live_find_tabs() -> list[list]:
    block = _balanced(VOICE_TEST.read_text(encoding="utf-8"),
                      "const FIND_TABS = ", "[", "]")
    rows = []
    for m in re.finditer(r"\[\s*'([^']*)'\s*,\s*'([^']*)'\s*,\s*(true|false)\s*\]",
                         block):
        rows.append([m.group(1), m.group(2), m.group(3) == "true"])
    return rows


# ---------------------------------------------------------------- diffing


def _keyset_diff(name: str, gen_keys: list, live_keys: list) -> list[str]:
    g, l = list(gen_keys), list(live_keys)
    msgs = []
    only_gen = [k for k in g if k not in l]
    only_live = [k for k in l if k not in g]
    if only_gen:
        msgs.append("  rows only in GENERATED (%d): %s" % (len(only_gen), only_gen))
    if only_live:
        msgs.append("  rows only in LIVE      (%d): %s" % (len(only_live), only_live))
    shared_g = [k for k in g if k in l]
    shared_l = [k for k in l if k in g]
    if shared_g != shared_l and not only_gen and not only_live:
        msgs.append("  same rows, DIFFERENT ORDER: generated %s vs live %s"
                    % (shared_g, shared_l))
    return msgs


def _field_diff(rows_gen: dict, rows_live: dict, fields: list[str]) -> list[str]:
    msgs = []
    for key in rows_gen:
        if key not in rows_live:
            continue
        for f in fields:
            a, b = rows_gen[key].get(f), rows_live[key].get(f)
            if a != b:
                msgs.append("  %s.%s: generated=%r  live=%r" % (key, f, a, b))
    return msgs


def diff_all(v2: dict) -> int:
    failures = 0

    def report(name: str, msgs: list[str], n_gen: int, n_live: int) -> None:
        nonlocal failures
        head = "%-14s generated %d rows, live %d rows" % (name, n_gen, n_live)
        if not msgs:
            print(head + "  -- EXACT MATCH")
            return
        failures += 1
        print(head + "  -- %d difference group(s)" % len(msgs))
        for m in msgs:
            print(m)

    # 1. TABS
    g, l = gen_tabs(v2), live_tabs()
    gd = {r["key"]: r for r in g}
    ld = {r["key"]: r for r in l}
    msgs = _keyset_diff("TABS", [r["key"] for r in g], [r["key"] for r in l])
    msgs += _field_diff(gd, ld, ["kind", "id", "src", "words"])
    report("TABS", msgs, len(g), len(l))

    # 2. manifests.json .tabs
    g2, l2 = gen_manifests(v2), live_manifests()
    msgs = _keyset_diff("manifests", list(g2), list(l2))
    msgs += _field_diff(g2, l2, ["aka", "tier"])
    report("manifests", msgs, len(g2), len(l2))

    # 3. descriptions
    g3, l3 = gen_descriptions(v2), live_descriptions()
    msgs = _keyset_diff("descriptions", list(g3), list(l3))
    msgs += _field_diff(g3, l3, ["title"])
    body_mismatch = [k for k in g3 if k in l3 and g3[k]["body"] != l3[k]["body"]]
    if body_mismatch:
        msgs.append("  body differs on %d shared rows: %s"
                    % (len(body_mismatch), body_mismatch))
    report("descriptions", msgs, len(g3), len(l3))

    # 4. KNOWLEDGE
    g4, collisions = gen_knowledge(v2)
    l4 = live_knowledge()
    msgs = _keyset_diff("KNOWLEDGE", list(g4), list(l4))
    for k in g4:
        if k in l4 and g4[k] != l4[k]:
            msgs.append("  %s: generated=%r  live=%r" % (k, g4[k], l4[k]))
    for c in collisions:
        msgs.append("  KEY COLLISION under the basename rule: " + c)
    report("KNOWLEDGE", msgs, len(g4), len(l4))

    # 5. destinations
    g5, l5 = gen_destinations(v2), live_destinations()
    gd5 = {r["id"]: r for r in g5}
    ld5 = {r["id"]: r for r in l5}
    msgs = _keyset_diff("destinations", [r["id"] for r in g5], [r["id"] for r in l5])
    msgs += _field_diff(gd5, ld5, ["label", "aka"])
    report("destinations", msgs, len(g5), len(l5))

    # 6. FIND_TABS
    g6, l6 = gen_find_tabs(v2), live_find_tabs()
    gd6 = {r[0]: {"needle": r[1], "expect": r[2]} for r in g6}
    ld6 = {r[0]: {"needle": r[1], "expect": r[2]} for r in l6}
    msgs = _keyset_diff("FIND_TABS", [r[0] for r in g6], [r[0] for r in l6])
    msgs += _field_diff(gd6, ld6, ["needle", "expect"])
    report("FIND_TABS", msgs, len(g6), len(l6))

    print()
    print("%d of 6 tables differ from the generated form." % failures)
    return 1 if failures else 0


# ---------------------------------------------------------------- main


EMITTERS = {
    "tabs": lambda v2: gen_tabs(v2),
    "manifests": lambda v2: gen_manifests(v2),
    "descriptions": lambda v2: gen_descriptions(v2),
    "knowledge": lambda v2: gen_knowledge(v2)[0],
    "destinations": lambda v2: gen_destinations(v2),
    "find_tabs": lambda v2: gen_find_tabs(v2),
}


def main() -> int:
    args = sys.argv[1:]
    if "--list-rules" in args:
        print(RULES)
        return 0
    v2 = load_v2()
    if "--emit" in args:
        which = args[args.index("--emit") + 1]
        names = list(EMITTERS) if which == "all" else [which]
        for n in names:
            if n not in EMITTERS:
                print("unknown table %r; one of %s" % (n, list(EMITTERS)),
                      file=sys.stderr)
                return 2
            print("---- " + n + " ----")
            print(json.dumps(EMITTERS[n](v2), indent=2, ensure_ascii=False))
        return 0
    if "--diff" in args or not args:
        return diff_all(v2)
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
