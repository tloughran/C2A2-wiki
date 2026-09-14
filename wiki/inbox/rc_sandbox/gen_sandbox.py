#!/usr/bin/env python3
"""gen_sandbox.py — regenerate the RC Sandbox reading document from its derivatives.

Inputs (all in this directory):
  assignments.csv        one row per cell: node, voice, about, discipline, work_order ...
  tl_sandbox_cells.json  verbatim cell text (never edited; the text IS the data)
  (node titles are embedded below: TITLES. They were authored in the lost script and
   match neither outline_v2.md nor toc_sandbox.csv verbatim; the committed .md is canonical.)

Output:
  TL_sandbox_reordered.md   (default; --out to redirect)

Rebuilt 2026-09-07: the 2026-09-04 original (~/gen_doc.py) lived in the per-session
VM home and was lost. Success criterion for the rebuild was a byte-identical diff
against the committed TL_sandbox_reordered.md; see handoffs/explorer-roadmap.md.
"""
import argparse, csv, json, re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
GEN_DATE = "2026-09-04"   # kept: the document states the date of the ordering, not of the render

# Heading text per node, in document order. Divisions (##) are I, II, III, III.2;
# everything else renders as ###. Ladder rungs carry L-numbers, not node ids.
TITLES = {
    "I": "I. THE APPARATUS — the accelerator/detector complex",
    "I.1": "I.1 The diagnosis",
    "I.2": "I.2 MacIntyre's algorithm",
    "I.2.1": "I.2.1 Traditions as the unit of rational enquiry",
    "I.2.2": "I.2.2 Epistemological crisis and its resolution",
    "I.2.3": "I.2.3 Incommensurability and vindication on the rival's own terms",
    "I.2.4": "I.2.4 Natural law and intractable dispute (the IDM / IDNL seam)",
    "I.3.1": "I.3.1 The detector — observables",
    "I.3.2": "I.3.2 The detector — scoring",
    "I.3.3": "I.3.3 The detector — provenance and the evidentiary record",
    "I.4": "I.4 The accelerator",
    "I.4.1": "I.4.1 Conditions of encounter",
    "I.4.2": "I.4.2 Rhetoric, invitation, and the bounds of argument",
    "I.4.3": "I.4.3 Community as the medium",
    "I.5": "I.5 Failure modes",
    "II": "II. SOURCES AND FIGURES",
    "II.1": "II.1 Membership — to be written, not harvested",
    "II.2": "II.2 Figures engaged",
    "II.3": "II.3 Modes of interaction",
    "II.4": "II.4 Bibliography and source pointers",
    "III": "III. THE POSITION — mind-only metaphysics and the layered account",
    "III.1": "III.1 The core claim — conscious realist monism",
    "III.1.1": "III.1.1 Against physicalist priority (incl. rivals at full strength)",
    "III.1.2": "III.1.2 Prediction, modeling, interface",
    "III.1.3": "III.1.3 Truth as an achieved relation",
    "III.2": "III.2 The layered account — the ladder",
    "III.2.0": "III.2.0 The ladder itself",
    "III.2.A": "L0 · Awareness",
    "III.2.I": "L1 · Information",
    "III.2.S": "L2 · Space-Time",
    "III.2.N": "L5 · Neuronal",
    "III.2.B": "L6 · Brain / neocortical column",
    "III.2.P": "L7 · Personal",
    "III.2.C": "L8 · Communal",
    "III.2.SO": "L9 · Social",
    "III.2.X": "III.2.X Cross-level claims",
    "III.3": "III.3 Goods, freedom, and the will",
    "III.4": "III.4 Love, community, and the person",
    "Z": "Z. HOLDING PEN — unclassified",
}
ORDER = list(TITLES)
DIVISIONS = {"I", "II", "III", "III.2"}
APPARATUS_NODES = {"X.1", "X.2"}
SILENT_VOICES = {"", "Loughran", "apparatus"}   # not shown in the provenance line, not indexed

# III.2.0 renders the ladder table (sheet rows 247-250) as three pass blocks, cells ordered
# by column then row, each labelled by its column; the pass-less III.2.0 cells follow.
PASSES = ["stimulus/apprehension", "response/inclination", "AI-reflection"]
COL_LABELS = {3: "(row label)", 4: "A Awareness", 5: "I Information", 6: "S Space-Time",
              7: "N Neuronal", 8: "B Brain/column", 9: "P Personal", 10: "C Communal",
              11: "S Social", 12: "(pass label)"}
LADDER_LEGEND = "**A** Awareness · **I** Information · **S** Space-Time · **N** Neuronal · **B** Brain/column · **P** Personal · **C** Communal · **S** Social"


def anchor(node):
    return node.lower().replace(".", "-")


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def cell_key(cid):
    m = re.match(r"r(\d+)c(\d+)", cid)
    return (int(m.group(1)), int(m.group(2)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "TL_sandbox_reordered.md"))
    a = ap.parse_args()

    rows = list(csv.DictReader(open(HERE / "assignments.csv", encoding="utf-8")))
    cells = {c["cell_id"]: c for c in json.load(open(HERE / "tl_sandbox_cells.json", encoding="utf-8"))["cells"]}

    by_node = defaultdict(list)
    for r in rows:
        by_node[r["node"]].append(r)
    for n in by_node:
        by_node[n].sort(key=lambda r: cell_key(r["cell_id"]))

    placed = [r for r in rows if r["node"] not in APPARATUS_NODES]
    fig_index, disc_index, voice_index, workorders = defaultdict(list), defaultdict(list), defaultdict(list), []

    title_of = TITLES.__getitem__

    out = []
    w = out.append
    w("# The RC Sandbox, reordered\n")
    w("Verbatim reordering of the **TL sandbox** tab of *Resurrecting Civility Master 9-4-2026.xlsx*.")
    w(f"Generated {GEN_DATE} from `assignments.csv`. **{len(placed)} cells** placed; sheet-apparatus cells (X.1/X.2) excluded.\n")
    w("> Every block below is the **unedited text of one spreadsheet cell**. Nothing is rewritten, merged or summarised. Headings, cross-references and indexes are editorial; cell text is not.\n")
    w("Provenance line under each heading: sheet row · position in row (left-to-right = order of accretion) · word count · voice, when not Loughran · ⚑ marks a note-to-self.\n")
    w("## Contents\n")
    for node in ORDER:
        depth = 2 if node.startswith("III.2.") else (1 if node == "Z" else node.count("."))
        n = len(by_node.get(node, []))
        count = f" — {n}" if n else ""
        w(f"{'  ' * depth}- [{title_of(node)}](#{anchor(node)}){count}")
    w("")

    def emit(r, label=None):
        cid = r["cell_id"]; c = cells[cid]
        sr, sc = cell_key(cid)
        prov = f"row {sr + 1} · seq {r['seq_in_row']} · {r['words']}w"
        if r["voice"] not in SILENT_VOICES:
            prov += f" · **voice: {r['voice']}**"
            voice_index[r["voice"]].append(cid)
        if r["work_order"] == "1":
            prov += " · ⚑ work-order"
            workorders.append((cid, r["node"], c["text"]))
        if r["pass"]:
            prov += f" · *{r['pass']}*"
        w(f'<a id="{cid}"></a>')
        w(f"##### `{cid}`" + (f" — {label}" if label else ""))
        w(f"<sub>{prov}</sub>\n")
        w(c["text"] + "\n")
        figs = [f.strip() for f in r["about"].split(";") if f.strip()]
        if figs:
            w("<sub>engages: " + ", ".join(f"[{f}](#fig-{slug(f)})" for f in figs) + "</sub>\n")
            for f in figs:
                fig_index[f].append(cid)
        for d in [d.strip() for d in r["discipline"].split(";") if d.strip()]:
            disc_index[d].append(cid)

    for node in ORDER:
        w(f'<a id="{anchor(node)}"></a>')
        w(f"{'##' if node in DIVISIONS else '###'} {title_of(node)}\n")
        members = by_node.get(node, [])
        if node == "III.2.0":
            w("#### The ladder table (sheet rows 247–250) — 8 rungs × 3 passes\n")
            w(LADDER_LEGEND + "\n")
            for p in PASSES:
                w(f"##### Pass: {p}\n")
                for r in sorted((r for r in members if r["pass"] == p), key=lambda r: cell_key(r["cell_id"])[::-1]):
                    emit(r, COL_LABELS[cell_key(r["cell_id"])[1]])
            w("#### Other statements of the ladder\n")
            members = [r for r in members if not r["pass"]]
        for r in members:
            emit(r)
        if node in DIVISIONS:
            w("")

    def links(ids, cap=60):
        ids = sorted(ids, key=cell_key)
        return " ".join(f"[`{i}`](#{i})" for i in ids[:cap]) + (" …" if len(ids) > cap else "")

    w('<a id="index-names"></a>')
    w("## Index of figures\n")
    for f, ids in sorted(fig_index.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        w(f'<a id="fig-{slug(f)}"></a>')
        w(f"**{f}** ({len(ids)}) — {links(ids)}\n")
    w('<a id="index-disciplines"></a>')
    w("## Index of disciplines\n")
    for d, ids in sorted(disc_index.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        w(f"**{d}** ({len(ids)}) — {links(ids)}\n")
    w('<a id="index-workorders"></a>')
    w("## Work-order register\n")
    w("Notes-to-self carried in the corpus. Each keeps its topical home; this is the collected list.\n")
    for cid, node, text in sorted(workorders, key=lambda t: cell_key(t[0])):
        w(f"- [`{cid}`](#{cid}) `{node}` — {text[:150].rstrip()}")
    w("")
    w('<a id="index-voices"></a>')
    w("## Index of non-Loughran voices\n")
    w("Quotation, transcript and testimony. A trailing `?` means attribution is inferred, not marked in the source — these need review.\n")
    for v, ids in sorted(voice_index.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        w(f"- **{v}** ({len(ids)}) — {links(ids)}")

    Path(a.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {a.out}: {len(placed)} cells, {len(out)} lines")


if __name__ == "__main__":
    main()
