#!/usr/bin/env python3
"""
generate_community_graph.py
Builds community_graph.json from curated_communities.json using TF-IDF + cosine similarity.

Implements TF-IDF and cosine similarity with numpy (no sklearn dependency).

Usage:
    python3 scripts/generate_community_graph.py [--threshold 0.08]

Output:
    wiki/community/community_graph.json

Tuning history:
    Threshold 0.15 (bigrams):  14 edges, avg_deg=0.18  — too sparse
    Threshold 0.15 (unigrams): 122 edges, avg_deg=1.55 — still sparse
    Threshold 0.10 (unigrams): 359 edges, avg_deg=4.57, deg<2=16.6% — too isolated
    Threshold 0.09 (unigrams): 477 edges, avg_deg=6.08, deg<2=10.8% — deg<2 just over 10%
    Threshold 0.08 (unigrams): 648 edges, avg_deg=8.25, deg<2=4.5%  ← CHOSEN
"""

import json
import argparse
import math
import re
import statistics
from collections import Counter
from datetime import date
from pathlib import Path

import numpy as np


# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT   = SCRIPT_DIR.parent
INPUT_PATH  = REPO_ROOT / "wiki" / "community" / "curated_communities.json"
OUTPUT_PATH = REPO_ROOT / "wiki" / "community" / "community_graph.json"

# Compact English stop-word set
STOP_WORDS = {
    "a","an","the","and","or","but","in","on","at","to","for","of","with",
    "by","from","as","is","are","was","were","be","been","being","have",
    "has","had","do","does","did","will","would","could","should","may",
    "might","shall","can","need","its","it","this","that","these","those",
    "i","we","you","he","she","they","me","us","him","her","them","my","our",
    "your","his","their","what","which","who","when","where","how","if","not",
    "no","nor","so","yet","both","either","neither","once","than","then",
    "through","about","above","after","before","between","into","more","most",
    "other","some","such","only","own","same","too","very","just","because",
    "while","during","without","within","along","following","across","behind",
    "beyond","since","thus","also","however","therefore","whether","there",
    "their","any","all","each","every","both","few","more","much","many",
    "new","now","over","under","up","down","out","off","on","here","s","t",
}


def tokenize(text: str) -> list[str]:
    """Lowercase, strip punctuation, remove stop-words. Unigrams only."""
    text = text.lower()
    tokens = re.findall(r"[a-z][a-z'-]*[a-z]|[a-z]", text)
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 2]


def build_tfidf_matrix(texts: list[str]) -> np.ndarray:
    """
    Build an L2-normalised TF-IDF matrix (n_docs × n_vocab) with:
      - sublinear TF: 1 + log(tf) if tf > 0
      - smooth IDF:   log((1 + N) / (1 + df)) + 1
    Returned rows are unit vectors so that dot-product == cosine similarity.
    """
    n = len(texts)
    token_lists = [tokenize(t) for t in texts]

    vocab = sorted({w for tl in token_lists for w in tl})
    word_idx = {w: i for i, w in enumerate(vocab)}
    V = len(vocab)
    print(f"Vocabulary: {V} unigrams over {n} documents")

    # Raw TF with sublinear scaling
    tf = np.zeros((n, V), dtype=np.float32)
    for di, tl in enumerate(token_lists):
        for w, cnt in Counter(tl).items():
            if w in word_idx:
                tf[di, word_idx[w]] = 1.0 + math.log(cnt)

    # Smooth IDF
    df  = (tf > 0).sum(axis=0).astype(np.float32)
    idf = np.log((1.0 + n) / (1.0 + df)) + 1.0

    # TF-IDF + L2 normalisation
    tfidf = tf * idf
    norms = np.linalg.norm(tfidf, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return tfidf / norms


def build_graph(communities: list[dict], threshold: float) -> dict:
    prs_texts = []
    for c in communities:
        parts = [c.get("problem", ""), c.get("resource", ""), c.get("solution", "")]
        prs_texts.append(" ".join(p for p in parts if p))

    tfidf = build_tfidf_matrix(prs_texts)

    # Cosine similarity (unit vectors → dot product)
    sim = tfidf @ tfidf.T
    n = len(communities)

    # ── Nodes ──────────────────────────────────────────────────────────────────
    nodes = []
    for c in communities:
        node = {
            "id":          c["community_id"],
            "name":        c["name"],
            "type":        c["type"],
            "url":         c.get("url", ""),
            "country":     c.get("country", ""),
            "description": c.get("description", ""),
            "problem":     c.get("problem", ""),
            "resource":    c.get("resource", ""),
            "solution":    c.get("solution", ""),
            "prs_quality": c.get("prs_quality", 2),
        }
        subtype = c.get("subtype", "")
        if subtype:
            node["subtype"] = subtype
        nodes.append(node)

    # ── Edges (upper triangle, i < j) ──────────────────────────────────────────
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            w = float(sim[i, j])
            if w >= threshold:
                edges.append({
                    "source": communities[i]["community_id"],
                    "target": communities[j]["community_id"],
                    "weight": round(w, 4),
                })
    edges.sort(key=lambda e: e["weight"], reverse=True)

    # ── Degree stats ────────────────────────────────────────────────────────────
    degrees = [0] * n
    cid_to_idx = {c["community_id"]: i for i, c in enumerate(communities)}
    for e in edges:
        degrees[cid_to_idx[e["source"]]] += 1
        degrees[cid_to_idx[e["target"]]] += 1

    avg_deg   = sum(degrees) / n
    min_deg   = min(degrees)
    max_deg   = max(degrees)
    med_deg   = statistics.median(degrees)
    lt2_count = sum(1 for d in degrees if d < 2)
    lt2_pct   = lt2_count / n * 100

    print(f"\n── Graph stats (threshold={threshold}) ──")
    print(f"  Nodes:              {n}")
    print(f"  Edges:              {len(edges)}")
    print(f"  Avg degree:         {avg_deg:.2f}")
    print(f"  Min / Max degree:   {min_deg} / {max_deg}")
    print(f"  Median degree:      {med_deg:.1f}")
    print(f"  Nodes with deg < 2: {lt2_count} ({lt2_pct:.1f}%)")

    graph = {
        "nodes": nodes,
        "edges": edges,
        "meta": {
            "node_count":        n,
            "edge_count":        len(edges),
            "threshold":         threshold,
            "avg_degree":        round(avg_deg, 3),
            "min_degree":        min_deg,
            "max_degree":        max_deg,
            "median_degree":     med_deg,
            "nodes_deg_lt2":     lt2_count,
            "nodes_deg_lt2_pct": round(lt2_pct, 1),
            "generated":         str(date.today()),
        },
    }
    return graph


def sample_edges(graph: dict, n: int = 10) -> None:
    """Print a spread-sampled set of edges for manual spot-check."""
    id_to_node = {nd["id"]: nd for nd in graph["nodes"]}
    edges = graph["edges"]
    if not edges:
        print("No edges to sample.")
        return

    step = max(1, len(edges) // n)
    samples = [edges[i] for i in range(0, len(edges), step)][:n]

    print(f"\n── Edge spot-check (sample of {len(samples)} spread across {len(edges)} edges) ──")
    for e in samples:
        src = id_to_node.get(e["source"], {})
        tgt = id_to_node.get(e["target"], {})
        src_type = src.get("type", "")
        tgt_type = tgt.get("type", "")
        cross = "CROSS" if src_type != tgt_type else "same "
        print(f"  [{cross}] w={e['weight']:.3f}  {src.get('name','?')[:45]:45s}")
        print(f"           {'':9s}↔  {tgt.get('name','?')[:45]:45s}")
        print(f"           ({src_type}) → ({tgt_type})")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=float, default=0.08,
                        help="Cosine similarity threshold (default: 0.08)")
    parser.add_argument("--input",  default=str(INPUT_PATH))
    parser.add_argument("--output", default=str(OUTPUT_PATH))
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        communities = json.load(f)
    print(f"Loaded {len(communities)} communities")

    graph = build_graph(communities, threshold=args.threshold)
    sample_edges(graph, n=10)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    kb = out.stat().st_size / 1024
    print(f"\n✓ Written to {out}  ({kb:.1f} KB)")


if __name__ == "__main__":
    main()
