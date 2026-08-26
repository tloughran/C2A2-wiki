#!/usr/bin/env python3
"""Assertions on the wikilink resolver in extract_vault_data.py.

Every test here is driven through its FAILURE path: each one fails if the
resolver is reverted to the stem-only, first-wins lookup that shipped before
2026-08-24, or if someone "fixes" a path-qualified miss by falling back to a
bare stem lookup.

    python3 test_wikilink_resolver.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extract_vault_data as E

FAILURES = []


def check(name, cond, detail=""):
    if cond:
        print("  ok   %s" % name)
    else:
        print("  FAIL %s  %s" % (name, detail))
        FAILURES.append(name)


def mkfiles(paths):
    return [{"filepath": p, "filename": Path(p).name} for p in paths]


# A miniature vault reproducing the exact collision that made this a trap:
# fifteen tradition folders, every one of them holding a file named `wiki.md`
# and one named `prs_triplets.md`.
TRADS = ["arkanihamed", "carroll", "fredrickson", "friston", "hawkins", "hoffman",
         "kastrup", "levin", "loughran", "macintyre", "mcgilchrist", "rohr",
         "stump", "wolfram", "wright"]
PATHS = []
for t in TRADS:
    PATHS += ["traditions/%s/wiki.md" % t, "traditions/%s/prs_triplets.md" % t]
PATHS += [
    "architecture/narrative_prs_connectome.md",
    "master/cross_program_index.md",
    "inbox/2026-06-15_levin_platonic-space-ingressing-minds.md",
    "inbox/proposals/approved/2026-06-15_levin_platonic-space-ingressing-minds.md",
]
resolve, stats = E._make_link_resolver(mkfiles(PATHS))

print("1. path-qualified links resolve to the tradition they NAME")
# The whole point. Under stem-only first-wins these all returned None; under a
# naive stem-stripping "fix" they would all return arkanihamed.
for t in TRADS:
    got = resolve("traditions/%s/wiki" % t)
    check("[[traditions/%s/wiki]]" % t,
          got == "traditions/%s/wiki.md" % t,
          "got %r" % got)

print("2. THE MISROUTE TRAP -- no tradition absorbs another's links")
targets = {resolve("traditions/%s/wiki" % t) for t in TRADS}
check("fifteen distinct targets, not one", len(targets) == 15,
      "got %d distinct targets: %r" % (len(targets), sorted(targets)))
check("arkanihamed did NOT swallow the set",
      resolve("traditions/friston/wiki") != "traditions/arkanihamed/wiki.md")
check("prs_triplets collides fifteen ways too",
      len({resolve("traditions/%s/prs_triplets" % t) for t in TRADS}) == 15)

print("3. bracketed surnames resolve as AUTHORED links")
check("[[Kastrup]]", resolve("Kastrup") == "traditions/kastrup/wiki.md")
check("[[Arkani-Hamed]]", resolve("Arkani-Hamed") == "traditions/arkanihamed/wiki.md")
check("[[Karl Friston]] alias", resolve("Karl Friston") == "traditions/friston/wiki.md")
check("[[Tom Loughran]] alias", resolve("Tom Loughran") == "traditions/loughran/wiki.md")

print("4. ambiguity REFUSES rather than guessing")
# Two real files share this stem. Guessing one is how the fifteen-way misroute
# would be reintroduced, so the resolver must return None.
check("colliding stem returns None",
      resolve("2026-06-15_levin_platonic-space-ingressing-minds") is None,
      "got %r" % resolve("2026-06-15_levin_platonic-space-ingressing-minds"))
check("bare [[wiki]] is ambiguous -> None", resolve("wiki") is None)
check("bare [[prs_triplets]] is ambiguous -> None", resolve("prs_triplets") is None)

print("5. a path that names no file does NOT fall back to a stem")
# This is the specific line that must never be relaxed.
check("[[nosuchdir/wiki]] -> None", resolve("nosuchdir/wiki") is None,
      "got %r" % resolve("nosuchdir/wiki"))

print("6. ordinary unique-stem links still work (no regression)")
check("[[narrative_prs_connectome]]",
      resolve("narrative_prs_connectome") == "architecture/narrative_prs_connectome.md")
check("[[master/cross_program_index]]",
      resolve("master/cross_program_index") == "master/cross_program_index.md")

print("7. degenerate input is handled, not crashed")
check("empty", resolve("") is None)
check("whitespace", resolve("   ") is None)
check("heading anchor stripped",
      resolve("traditions/levin/wiki#Summary") == "traditions/levin/wiki.md")
check("unknown name", resolve("Definitely Not A Thinker") is None)

print("8. mention edges are de-duplicated against authored links")
# One bracketed [[Kastrup]] must not contribute at BOTH type_w 3.0 and 2.0.
files = [dict(f) for f in mkfiles(PATHS)]
for f in files:
    f["wikilinks"] = []
    f["references"] = []
    f["thinker_mentions"] = []
src = next(f for f in files if f["filepath"] == "architecture/narrative_prs_connectome.md")
src["wikilinks"] = ["Kastrup"]
src["thinker_mentions"] = ["traditions/kastrup/wiki.md"]
conn = E.build_connections(files)
wl = [e for e in conn["wikilink_edges"]
      if e["source"] == src["filepath"] and e["target"] == "traditions/kastrup/wiki.md"]
mn = [e for e in conn["mention_edges"]
      if e["source"] == src["filepath"] and e["target"] == "traditions/kastrup/wiki.md"]
check("authored edge emitted once", len(wl) == 1, "got %d" % len(wl))
check("duplicate mention edge suppressed", len(mn) == 0, "got %d" % len(mn))

print("9. self-targets are not emitted")
for f in files:
    f["wikilinks"] = []
    f["thinker_mentions"] = []
kas = next(f for f in files if f["filepath"] == "traditions/kastrup/wiki.md")
kas["wikilinks"] = ["Kastrup"]          # its own page, naming itself
conn = E.build_connections(files)
loops = [e for e in conn["wikilink_edges"] if e["source"] == e["target"]]
check("no self-loops", loops == [], "got %r" % loops[:3])

print()
if FAILURES:
    print("FAILED %d assertion(s): %s" % (len(FAILURES), ", ".join(FAILURES)))
    sys.exit(1)
print("all assertions passed")
