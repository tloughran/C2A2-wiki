#!/usr/bin/env python3
"""
Commentary Explorer — bundle builder.

Reads:
  - source markdown commentary (3rvme-style: YAML frontmatter + Annotation Index by page)
  - chapters.json (page-range map)
  - tradition wiki files, PRS triplet files, Summa Contemporary syntheses (satellites)

Emits:
  - bundle.json (single self-contained JSON, ready to be inlined into HTML)

Usage:
  python3 build_bundle.py SOURCE_MD CHAPTERS_JSON OUT_JSON \
      --wiki-root <path>  --summa-root <path>  [--include-transcripts]
"""

import argparse, json, pathlib, re, sys
from collections import defaultdict
import unicodedata

# ---------- thinker registry ---------------------------------------------------

# (id, surname patterns, full-name patterns, color)
# Color palette matches CLAUDE.md "muted" set so the look matches wiki_narration.html
THINKERS = [
    ("levin",       ["Levin"],                       ["Michael Levin"],         "#C45B5B"),
    ("friston",     ["Friston"],                     ["Karl Friston"],          "#5A8EAF"),
    ("hoffman",     ["Hoffman"],                     ["Donald Hoffman"],        "#C08B3E"),
    ("kastrup",     ["Kastrup"],                     ["Bernardo Kastrup"],      "#8B5DAB"),
    ("mcgilchrist", ["McGilchrist"],                 ["Iain McGilchrist"],      "#3D9E89"),
    ("hawkins",     ["Hawkins"],                     ["Jeff Hawkins"],          "#B87D3E"),
    ("wolfram",     ["Wolfram"],                     ["Stephen Wolfram"],       "#4A5E6D"),
    ("carroll",     ["Carroll"],                     ["Sean Carroll"],          "#4E8A5E"),
    ("arkanihamed", ["Arkani-Hamed", "Arkani Hamed"],["Nima Arkani-Hamed"],     "#A85D3A"),
    ("fredrickson", ["Fredrickson"],                 ["Barbara Fredrickson"],   "#C47A9A"),
    ("stump",       ["Stump"],                       ["Eleonore Stump"],        "#A8923A"),
    ("rohr",        ["Rohr"],                        ["Richard Rohr"],          "#9A7A5A"),
    ("wright",      ["Wright"],                      ["N. T. Wright", "NT Wright"], "#5A72A8"),
    ("loughran",    ["Loughran"],                    ["Tom Loughran", "Thomas Loughran"], "#4A8A7A"),
    # MacIntyre is the book's author — no satellite; self-references should be skipped
]

# Extra match keys grafted onto specific thinker satellites. Stump represents
# the modern Thomistic program, so historical-figure mentions (Aquinas,
# Aristotle, Augustine, etc.) plumb to her satellite. This is the biggest
# source of legitimate edges from TRV interpretation text, since the AI
# commentator names these figures constantly even though it never names the
# C2A2 contemporary thinkers.
EXTRA_THINKER_KEYS = {
    "stump": [
        "Aquinas", "Aquinas's",
        "Thomism", "Thomist", "Thomistic",
        "Aristotle", "Aristotelian", "Aristotelianism",
        "Augustine", "Augustinian", "Augustinianism",
    ],
    # Loughran tradition: Tom's own notes will house historical-figure
    # commentary (per 2026-05-07 conversation). Route the same historical
    # references AND the genealogical thinkers (Nietzsche/Foucault) to this
    # satellite so they show up under Loughran whenever Tom adds content.
    "loughran": [
        "Aquinas", "Aquinas's",
        "Aristotle", "Aristotelian", "Aristotelianism",
        "Augustine", "Augustinian", "Augustinianism",
        "Nietzsche", "Nietzschean",
        "Foucault", "Foucauldian",
        "MacIntyre",  # Tom is annotating MacIntyre's text — fair to host meta-commentary in Loughran
    ],
}

# Topic phrases too generic to use as match keys (single common English words
# that produce false-positive collisions). Day titles equal to one of these
# are dropped from the satellite's match keys; the satellite still exists
# but only matches via other signals if any are added later.
GENERIC_TITLE_BLOCKLIST = {
    "Introduction", "The Soul", "Genesis", "Creation", "Truth", "Life",
    "Evolution", "Knowledge After Death",
}

# Aquinas / Aristotle / Nietzsche / Augustine — historical figures referenced in TRV.
# We don't have wiki files for these (Stump represents the Thomist tradition), but we
# can flag mentions and route them to Stump (Aquinas) when no other context exists.
# For now we just track them as edges to Stump for Aquinas-related mentions.
HISTORICAL_TO_THINKER = {
    "aquinas":   "stump",      # Stump's analytic Thomism
    "aristotle": "stump",      # treated under Aquinas/Stump for now
    "augustine": "stump",
    "nietzsche": None,         # no current satellite for genealogy thinkers
    "foucault":  None,
}

# ---------- helpers ------------------------------------------------------------

def read_text(p):
    return pathlib.Path(p).read_text(encoding="utf-8")

def write_json(p, obj):
    pathlib.Path(p).write_text(json.dumps(obj, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

def slugify(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s.strip().lower())
    return re.sub(r"-+", "-", s).strip("-")

# ---------- OCR anchor matching -----------------------------------------------

# Tesseract OCR introduces column-drift, broken words, and stray characters,
# so exact substring matches frequently fail. We build a normalized version of
# the OCR text (alpha+digits only, lowercased) plus a position map from
# normalized indices back to original indices. Then we look for the anchor
# normalized the same way. If the full anchor doesn't match, we try the first
# N distinctive words, then progressively shorter prefixes.

def _normalize_for_match(text):
    """Return (normalized_str, [original_index_for_each_norm_char])."""
    norm = []
    pos = []
    for i, ch in enumerate(text):
        if ch.isalnum():
            norm.append(ch.lower())
            pos.append(i)
    return "".join(norm), pos

def _normalize_anchor(anchor):
    if not anchor: return ""
    a = anchor.strip()
    if a.startswith("_") and a.endswith("_"):
        a = a[1:-1]
    a = a.strip()
    # alphanumerics only, lowercased
    return "".join(ch.lower() for ch in a if ch.isalnum())

def find_anchor_in_ocr(ocr_text, anchor, content=None):
    """Find the anchor (or content as fallback) in the OCR text.
    Returns dict {start, end, matched_norm_len, fuzziness} on hit, else None.
    fuzziness in [0,1]: 0 = exact full match, higher = shorter prefix used.
    """
    if not ocr_text: return None
    norm_ocr, pos_map = _normalize_for_match(ocr_text)
    candidates = []
    if content: candidates.append(content)
    if anchor: candidates.append(anchor)
    for cand in candidates:
        norm_a = _normalize_anchor(cand)
        if not norm_a: continue
        # Try full normalized match
        idx = norm_ocr.find(norm_a)
        if idx >= 0 and pos_map:
            start = pos_map[idx]
            end = pos_map[min(idx + len(norm_a) - 1, len(pos_map)-1)] + 1
            return {"start": start, "end": end, "matched_norm_len": len(norm_a), "fuzziness": 0.0}
        # Progressive shrinking — drop trailing words until we find a match
        # Words here means runs of normalized text separated by original whitespace.
        # Easier: find anchor's word-tokens in the original anchor and shrink suffix.
        words = re.findall(r"[A-Za-z0-9]+", cand.strip("_ "))
        for take in range(len(words) - 1, 1, -1):  # take >= 2 words
            partial = "".join(w.lower() for w in words[:take])
            idx = norm_ocr.find(partial)
            if idx >= 0:
                start = pos_map[idx]
                end = pos_map[min(idx + len(partial) - 1, len(pos_map)-1)] + 1
                fuzziness = 1 - (take / max(len(words), 1))
                return {"start": start, "end": end, "matched_norm_len": len(partial), "fuzziness": round(fuzziness, 2)}
    return None

# ---------- source parser ------------------------------------------------------

ANN_FIELD = re.compile(r"^- \*\*([a-zA-Z_]+):\*\*\s*(.*)$", re.M)

def parse_source(src_md):
    """Parse the commentary markdown into:
       { meta: {...}, pages: { page:int -> {summary:str, annotations:[ann]} } }
    """
    text = src_md
    meta = {}
    fm = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    if fm:
        for line in fm.group(1).splitlines():
            m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line.strip())
            if m:
                meta[m.group(1)] = m.group(2).strip().strip('"')
        text = text[fm.end():]

    pages = {}
    # Split on '### Page N'
    page_iter = list(re.finditer(r"^### Page (\d+)\s*$", text, flags=re.M))
    for i, m in enumerate(page_iter):
        page_no = int(m.group(1))
        start = m.end()
        end = page_iter[i+1].start() if i+1 < len(page_iter) else len(text)
        block = text[start:end]
        # summary
        sm = re.search(r"^> \*\*Page summary:\*\*\s*(.+?)(?=\n\n|\n#)", block, flags=re.S | re.M)
        summary = ""
        if sm:
            summary = re.sub(r"\s+", " ", sm.group(1)).strip()
        # annotations
        anns = []
        ann_iter = list(re.finditer(r"^#### Ann (\d+\.\d+)\s*$", block, flags=re.M))
        for j, am in enumerate(ann_iter):
            ann_id = am.group(1)
            astart = am.end()
            aend = ann_iter[j+1].start() if j+1 < len(ann_iter) else len(block)
            abody = block[astart:aend]
            fields = {}
            for fm2 in ANN_FIELD.finditer(abody):
                k, v = fm2.group(1), fm2.group(2).strip()
                # strip leading backticks
                v = re.sub(r"^`(.+)`$", r"\1", v)
                fields[k] = v
            fields["id"] = ann_id
            anns.append(fields)
        pages[page_no] = {"summary": summary, "annotations": anns}
    return {"meta": meta, "pages": pages}

# ---------- satellite registry -------------------------------------------------

def collect_satellites(wiki_root, summa_root, include_transcripts=False):
    """Walk the satellite directories and collect every candidate target.
       Returns: list of dicts with id, kind, title, body_md, path, match_keys (list of patterns).
    """
    sats = []

    # Tradition wikis
    tw_dir = pathlib.Path(wiki_root) / "traditions"
    for sub in sorted(tw_dir.iterdir()) if tw_dir.exists() else []:
        if not sub.is_dir(): continue
        wiki_md = sub / "wiki.md"
        prs_md  = sub / "prs_triplets.md"
        thinker_id = sub.name
        thinker_color = next((c for (tid, _, _, c) in THINKERS if tid == thinker_id), "#888")
        thinker_label = next((full[0] if full else surn[0] for (tid, surn, full, _) in THINKERS if tid == thinker_id), thinker_id)
        # match keys (for this thinker)
        keys = []
        for (tid, surn, full, _) in THINKERS:
            if tid == thinker_id:
                keys = list(surn) + list(full)
                break
        # Graft on extra historical-figure keys for select thinkers (e.g., Stump → Aquinas)
        keys = list(keys) + EXTRA_THINKER_KEYS.get(thinker_id, [])
        if wiki_md.exists():
            sats.append({
                "id": f"thinker-{thinker_id}",
                "kind": "thinker",
                "title": thinker_label,
                "color": thinker_color,
                "body_md": wiki_md.read_text(encoding="utf-8"),
                "path": str(wiki_md),
                "match_keys": keys,
                "thinker": thinker_id,
            })
        if prs_md.exists():
            sats.append({
                "id": f"prs-{thinker_id}",
                "kind": "prs",
                "title": f"{thinker_label} — PRS Triplets",
                "color": thinker_color,
                "body_md": prs_md.read_text(encoding="utf-8"),
                "path": str(prs_md),
                "match_keys": keys,  # same keys; differentiate kind on edge weight
                "thinker": thinker_id,
            })

    # Summa Contemporary syntheses
    syn_dir = pathlib.Path(summa_root) / "vault" / "synthesis"
    if syn_dir.exists():
        for f in sorted(syn_dir.glob("Day-*-*Contemporary.md")):
            # Filename: "Day-007 - The Beatific Vision - Contemporary.md"
            m = re.match(r"Day-(\d+)\s*-\s*(.+?)\s*-\s*Contemporary\.md$", f.name)
            if not m: continue
            day = int(m.group(1)); topic = m.group(2).strip()
            # Use ONLY full-phrase matching for Summa Day titles. Tokenizing
            # leads to false-positive matches on common English words like
            # "will", "free", "good", "knowledge", "truth" that appear constantly
            # in MacIntyre annotations without actually referring to the day.
            # Multi-word topic phrases are distinctive enough as whole strings.
            keys = [topic]
            # Drop overly-generic title phrases that collide with everyday English
            if topic in GENERIC_TITLE_BLOCKLIST:
                keys = []
            sats.append({
                "id": f"summa-day-{day:03d}",
                "kind": "summa",
                "title": f"Summa Day {day:03d} — {topic}",
                "color": "#C9A84C",  # Master color
                "body_md": f.read_text(encoding="utf-8"),
                "path": str(f),
                "match_keys": keys,
                "day": day,
                "topic": topic,
            })
            if include_transcripts:
                # paired transcript
                tf = pathlib.Path(summa_root) / "vault" / "transcripts" / f"Day-{day:03d} - {topic}.md"
                if tf.exists():
                    sats.append({
                        "id": f"summa-tx-{day:03d}",
                        "kind": "summa-transcript",
                        "title": f"Summa Day {day:03d} (Transcript) — {topic}",
                        "color": "#C9A84C",
                        "body_md": tf.read_text(encoding="utf-8"),
                        "path": str(tf),
                        "match_keys": keys,
                        "day": day,
                    })

    return sats

# ---------- edge extraction ----------------------------------------------------

def page_to_chapter(chapter_list):
    m = {}
    for ch in chapter_list:
        a, b = ch["pdf_pages"]
        for p in range(a, b+1):
            m[p] = ch["id"]
    return m

def find_satellite_hits(text, satellites):
    """Return list of (sat_id, matched_key) for every satellite whose match_keys
       appear (whole-word, case-insensitive) in text."""
    hits = []
    if not text: return hits
    for sat in satellites:
        for k in sat["match_keys"]:
            # whole-word, case-insensitive
            pattern = r"\b" + re.escape(k) + r"\b"
            if re.search(pattern, text, flags=re.I):
                hits.append((sat["id"], k))
                break  # one hit per satellite per text-blob is enough
    return hits

# ---------- main ---------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source_md")
    ap.add_argument("chapters_json")
    ap.add_argument("out_json")
    ap.add_argument("--wiki-root", required=True)
    ap.add_argument("--summa-root", required=True)
    ap.add_argument("--include-transcripts", action="store_true")
    ap.add_argument("--ocr-json", help="Optional ocr_text.json keyed by PDF page → string. "
                                       "If supplied, each page in the bundle gets an ocr_text field "
                                       "and each annotation gets an ocr_match {start,end,fuzziness}.")
    args = ap.parse_args()

    ocr_pages = {}
    if args.ocr_json:
        ocr_pages = json.loads(read_text(args.ocr_json))
        print(f"[ocr] loaded {len(ocr_pages)} OCR pages from {args.ocr_json}", file=sys.stderr)

    print(f"[parse] source: {args.source_md}", file=sys.stderr)
    src = parse_source(read_text(args.source_md))
    chap_doc = json.loads(read_text(args.chapters_json))
    chapters = chap_doc["chapters"]

    print(f"[parse] {len(src['pages'])} pages, "
          f"{sum(len(p['annotations']) for p in src['pages'].values())} annotations",
          file=sys.stderr)

    print(f"[scan] satellites in {args.wiki_root} and {args.summa_root}", file=sys.stderr)
    sats = collect_satellites(args.wiki_root, args.summa_root, args.include_transcripts)
    print(f"[scan] {len(sats)} satellites collected", file=sys.stderr)

    # Page -> chapter map
    p2c = page_to_chapter(chapters)

    # Build edges: chapter -> satellite, with evidence (annotation refs)
    edge_evidence = defaultdict(lambda: defaultdict(list))  # [chap_id][sat_id] -> [{page, ann_id, key, snippet}]
    for page_no, page in src["pages"].items():
        chap_id = p2c.get(page_no)
        if not chap_id: continue
        # Search at the annotation level so we can store evidence per annotation
        for ann in page["annotations"]:
            blob_parts = [
                ann.get("interpretation", ""),
                ann.get("rc_relevance", ""),
                ann.get("content", ""),
                ann.get("anchor_text", ""),
            ]
            blob = " ".join(blob_parts)
            hits = find_satellite_hits(blob, sats)
            for (sat_id, key) in hits:
                # Self-skip: don't link MacIntyre book to a hypothetical MacIntyre satellite
                # (we excluded macintyre from THINKERS already, but be defensive)
                if sat_id.endswith("-macintyre"): continue
                snippet_src = ann.get("interpretation") or ann.get("rc_relevance") or blob
                snippet = re.sub(r"\s+", " ", snippet_src)[:240]
                edge_evidence[chap_id][sat_id].append({
                    "page": page_no,
                    "ann": ann.get("id"),
                    "key": key,
                    "snippet": snippet,
                })

    # Compress to edges
    edges = []
    for chap_id, sat_map in edge_evidence.items():
        for sat_id, evs in sat_map.items():
            edges.append({
                "from": chap_id,
                "to": sat_id,
                "weight": len(evs),
                "evidence": evs[:25],  # cap evidence list per edge
            })
    edges.sort(key=lambda e: (-e["weight"], e["from"], e["to"]))

    # Build chapters with embedded pages, OCR text, and per-annotation matches
    match_stats = {"total": 0, "exact": 0, "fuzzy": 0, "miss": 0}
    chapters_out = []
    for ch in chapters:
        a, b = ch["pdf_pages"]
        ch_pages = []
        for p in range(a, b+1):
            if p in src["pages"]:
                pdata = src["pages"][p]
                ocr = ocr_pages.get(str(p), "")
                # Locate each annotation's anchor inside the page OCR
                anns_out = []
                for ann in pdata["annotations"]:
                    ann2 = dict(ann)
                    if ocr:
                        m = find_anchor_in_ocr(ocr, ann.get("anchor_text"), ann.get("content"))
                        if m:
                            ann2["ocr_match"] = m
                            match_stats["total"] += 1
                            if m["fuzziness"] == 0.0: match_stats["exact"] += 1
                            else: match_stats["fuzzy"] += 1
                        else:
                            match_stats["total"] += 1
                            match_stats["miss"] += 1
                    anns_out.append(ann2)
                ch_pages.append({
                    "page": p,
                    "summary": pdata["summary"],
                    "ocr_text": ocr,
                    "annotations": anns_out,
                })
        chapters_out.append({
            "id": ch["id"],
            "number": ch["number"],
            "title": ch["title"],
            "pdf_pages": ch["pdf_pages"],
            "title_confidence": ch.get("title_confidence", "inferred"),
            "annotated_page_count": len(ch_pages),
            "annotation_count": sum(len(p["annotations"]) for p in ch_pages),
            "pages": ch_pages,
        })

    # Only include satellites that have at least one edge — keeps the graph
    # focused on connections that actually exist. The full satellite catalog
    # is retained in source files; uncomment the filter to include all.
    connected = {e["to"] for e in edges}
    satellites_out = []
    for s in sats:
        if s["id"] not in connected:
            continue
        satellites_out.append({
            "id": s["id"],
            "kind": s["kind"],
            "title": s["title"],
            "color": s.get("color", "#888"),
            "body_md": s["body_md"],
            "source_path": s["path"],
            "thinker": s.get("thinker"),
            "day": s.get("day"),
        })

    bundle = {
        "schema": "commentary-explorer/1",
        "source": {
            "filename": pathlib.Path(args.source_md).name,
            "title": src["meta"].get("title", ""),
            "author": src["meta"].get("author", ""),
            "year": src["meta"].get("year", ""),
            "annotation_count": int(src["meta"].get("annotation_count", "0") or 0),
            "pages_with_annotations": int(src["meta"].get("pages_with_annotations", "0") or 0),
            "scan_file": src["meta"].get("scan_file", ""),
            "pdf_offset_from_book": chap_doc.get("_meta", {}).get("source_pdf_offset_from_book"),
        },
        "chapters": chapters_out,
        "satellites": satellites_out,
        "edges": edges,
    }
    write_json(args.out_json, bundle)
    print(f"[write] {args.out_json}", file=sys.stderr)

    # Print edge summary to stderr
    print("\n[summary]  Edges per chapter:", file=sys.stderr)
    for ch in chapters_out:
        ch_edges = [e for e in edges if e["from"] == ch["id"]]
        top = sorted(ch_edges, key=lambda e: -e["weight"])[:6]
        top_str = ", ".join(f"{e['to'].split('-',1)[1]}({e['weight']})" for e in top)
        print(f"  {ch['id']:>8}: {len(ch_edges):>3} edges, top: {top_str}", file=sys.stderr)

    if ocr_pages:
        t = match_stats["total"]
        if t:
            print(f"\n[ocr-match]  total={t}  exact={match_stats['exact']} ({100*match_stats['exact']//t}%)  "
                  f"fuzzy={match_stats['fuzzy']} ({100*match_stats['fuzzy']//t}%)  "
                  f"missed={match_stats['miss']} ({100*match_stats['miss']//t}%)", file=sys.stderr)

if __name__ == "__main__":
    main()
