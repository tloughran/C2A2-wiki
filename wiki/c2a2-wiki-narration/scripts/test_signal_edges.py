#!/usr/bin/env python3
"""Assertions for the Level-2 signal edge layer.

Every assertion here fails against the two ways this could have been built
wrong: guessing a claimant when a card id is ambiguous, and emitting the
asserted layer after the inferred one so 95% of it disappears into the
mention edges silently. Run:  python3 test_signal_edges.py
"""
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract_vault_data as E
import generate_visualization as G

OK = 0


def ok(label, cond):
    global OK
    if not cond:
        print("  FAIL " + label)
        sys.exit(1)
    OK += 1
    print("  ok   " + label)


def card(path, pid, tk, section):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("---\nproposal_id: %s\ntradition_key: %s\n---\n\n"
                 "## Cross-Tradition Signals\n%s\n" % (pid, tk, section))


def sig(a, b, cid, weight=2.0, strength="Moderate", date="2026-04-08", text="", source="card"):
    return {"a": a, "b": b, "card": cid, "sid": cid, "date": date, "strength": strength,
            "weight": weight, "nature": "", "source": source, "text": text,
            "action": "Active", "source_date": date}


def files_for(rels):
    return [{"filepath": r, "wikilinks": [], "references": [], "thinker_mentions": [],
             "directory": r.split("/")[0], "date": "", "title": r} for r in rels]


def build(root, signals, extra_files=(), manifest=None):
    vault = os.path.join(root, "wiki")
    os.makedirs(os.path.join(root, "prototypes", "backlog"), exist_ok=True)
    with open(os.path.join(root, "prototypes", "signals_grown.json"), "w", encoding="utf-8") as fh:
        json.dump(signals, fh)
    if manifest is not None:
        with open(os.path.join(root, "prototypes", "backlog", "backlog_manifest.json"), "w", encoding="utf-8") as fh:
            json.dump(manifest, fh)
    rels = ["traditions/%s/wiki.md" % t for t in
            ("levin", "mcgilchrist", "friston", "wolfram", "kastrup")] + list(extra_files)
    for r in rels:
        p = os.path.join(vault, r)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if not os.path.exists(p):
            open(p, "w").close()
    return vault, files_for(rels)


print("1. an ambiguous card id REFUSES rather than guessing")
root = tempfile.mkdtemp()
try:
    rels = ["inbox/proposals/approved/a_levin.md", "inbox/proposals/approved/b_wolfram.md"]
    vault, files = build(root, [sig("Levin", "McGilchrist", "PROP-DUP-001", text="nowhere in either file")],
                         extra_files=rels, manifest=[])
    card(os.path.join(vault, rels[0]), "PROP-DUP-001", "levin", "- **Levin:** unrelated prose\n")
    card(os.path.join(vault, rels[1]), "PROP-DUP-001", "wolfram", "- **Wolfram:** also unrelated\n")
    edges = E.build_signal_edges(vault, files)
    ok("two claimants, no text match -> no edges emitted", edges == [])

    print("2. text match picks the right claimant out of several")
    body = "- **McGilchrist (Strong):** dissociative identity disorder of the body maps onto hemispheres\n"
    card(os.path.join(vault, rels[0]), "PROP-DUP-001", "levin", body)
    edges = E.build_signal_edges(vault, [f for f in files], )
    ok("still refused while the record text differs", edges == [])
    vault2, files2 = build(root + "_b", [sig("Levin", "McGilchrist", "PROP-DUP-001",
                                             text="Dissociative identity disorder of the body maps onto hemispheres")],
                           extra_files=rels, manifest=[])
    card(os.path.join(vault2, rels[0]), "PROP-DUP-001", "levin", body)
    card(os.path.join(vault2, rels[1]), "PROP-DUP-001", "wolfram", "- **Wolfram:** unrelated\n")
    edges = E.build_signal_edges(vault2, files2)
    ok("the claimant whose section carries the prose wins",
       {e["source"] for e in edges} == {rels[0]})
    ok("both endpoints of the pair emitted",
       {e["target"] for e in edges} == {"traditions/levin/wiki.md", "traditions/mcgilchrist/wiki.md"})
    ok("the card's own tradition is flagged home",
       [e["home"] for e in edges if e["target"].endswith("levin/wiki.md")] == [True])
    ok("the reached tradition is not flagged home",
       [e["home"] for e in edges if e["target"].endswith("mcgilchrist/wiki.md")] == [False])

    print("3. the manifest outranks a frontmatter scan")
    vault3, files3 = build(root + "_c", [sig("Levin", "Wolfram", "PROP-DUP-001", text="x")],
                           extra_files=rels,
                           manifest=[{"card": "PROP-DUP-001", "file": rels[1]}])
    card(os.path.join(vault3, rels[0]), "PROP-DUP-001", "levin", "- **Levin:** x\n")
    card(os.path.join(vault3, rels[1]), "PROP-DUP-001", "wolfram", "- **Wolfram:** x\n")
    edges = E.build_signal_edges(vault3, files3)
    ok("manifest file used even though two documents claim the id",
       {e["source"] for e in edges} == {rels[1]})

    print("4. only source=card signals are wired")
    vault4, files4 = build(root + "_d", [
        sig("Levin", "Wolfram", "", source="index", text="i"),
        sig("Levin", "Friston", "", source="finding", text="f"),
    ], extra_files=["inbox/proposals/approved/solo.md"], manifest=[])
    edges = E.build_signal_edges(vault4, files4)
    ok("index and finding signals emit nothing", edges == [])

    print("5. records aggregate per pair")
    recs = [sig("Levin", "Wolfram", "PROP-SOLO", 2.0, "Moderate", "2026-05-01", "later and weaker"),
            sig("Levin", "Wolfram", "PROP-SOLO", 3.0, "High", "2026-04-01", "earlier and stronger")]
    vault5, files5 = build(root + "_e", recs, extra_files=["inbox/proposals/approved/solo.md"], manifest=[])
    card(os.path.join(vault5, "inbox/proposals/approved/solo.md"), "PROP-SOLO", "levin", "- x\n")
    edges = E.build_signal_edges(vault5, files5)
    wol = [e for e in edges if e["target"].endswith("wolfram/wiki.md")][0]
    ok("count is the number of records on the pair", wol["count"] == 2)
    ok("weight is the strongest record's", wol["weight"] == 3.0)
    ok("strength travels with the strongest record", wol["strength"] == "High")
    ok("date is the earliest assertion", wol["date"] == "2026-04-01")

    print("6. a missing stream is skipped, not fatal")
    vault6, files6 = build(root + "_f", [], extra_files=[], manifest=[])
    os.remove(os.path.join(root + "_f", "prototypes", "signals_grown.json"))
    ok("absent signals_grown.json returns []", E.build_signal_edges(vault6, files6) == [])

    print("7. EMISSION ORDER: an asserted pair is not swallowed by the inferred one")
    src = "inbox/proposals/approved/solo.md"
    tgt = "traditions/wolfram/wiki.md"
    data = {
        "files": files_for([src, tgt]),
        "connections": {
            "signal_edges": [{"source": src, "target": tgt, "type": "signal", "weight": 3.0,
                              "strength": "High", "date": "2026-04-01", "text": "t",
                              "card": "PROP-SOLO", "count": 1, "home": False, "bridge": "cross"}],
            "wikilink_edges": [],
            "mention_edges": [{"source": src, "target": tgt, "type": "thinker_mention", "bridge": "cross"}],
            "reference_edges": [],
        },
    }
    nodes, links = G.build_graph_data(data)[:2]
    same = [l for l in links if {l["source"], l["target"]} == {src, tgt}] if isinstance(links[0].get("source"), str) else None
    ok("the pair is emitted exactly once", len(links) == 1)
    ok("and it is typed signal, not mention", links[0]["type"] == "signal")
    ok("signal outranks wikilink in the score components", links[0]["score_type"] == 4.0)
    ok("the justification prose rides on the edge", links[0].get("sig_text") == "t")
finally:
    for d in (root, root + "_b", root + "_c", root + "_d", root + "_e", root + "_f"):
        shutil.rmtree(d, ignore_errors=True)

print("\nall %d assertions passed" % OK)
