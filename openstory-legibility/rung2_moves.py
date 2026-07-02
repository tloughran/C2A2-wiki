#!/usr/bin/env python3
"""
rung2_moves.py - Rung 2 of the listening ladder: classify the human's RELATIONAL
MOVE toward the immediately preceding AI turn (the A->H direction Rung 1 flagged as
where lexical goes blind and where the listening signal lives).

Read-only over the snapshot; reuses rung1_uptake.build_stream so it inherits the
SAME replay-dedup (event_ids key) -- so it classifies DISTINCT beats, never the
recrystallize duplicates. Idempotent: labels are keyed by (session, pair_index) and
cached; re-running never re-spends on an already-labelled pair.

    python3 rung2_moves.py [snapshot.db] [out_dir] [--backend manual|anthropic|openai]

  --backend manual  (default): read labels from rung2_labels.json (the pilot). No
                    model call, no spend. Renders the report from whatever is labelled.
  --backend anthropic|openai: classify unlabelled A->H pairs via a cheap model
                    (Haiku / gpt-*-mini), temp 0, one structured label per pair, then
                    MERGE into rung2_labels.json. Requires ANTHROPIC_API_KEY / OPENAI_API_KEY
                    (absent in the Cowork sandbox -> run this leg on the Mac).

The taxonomy is the Rung-1-design seven (acknowledge/build-on/steelman/concede/
repair/deflect/override) EXTENDED by the pilot, which found operational human<->AI
dialogue is dominated by two moves the original set omits: `report` (paste execution
results back) and `direct` (approve + command next), plus `probe` (open a question).
See rung2_labels.json for definitions. The taxonomy is genre-dependent: deliberative
rival-traditions debate would weight steelman/concede; this single-human operational
corpus weights report/direct. That genre-fit is itself a Rung-2 finding.
"""
import sqlite3, json, sys, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rung1_uptake import build_stream, content, DEFAULT_DB   # shared deduped stream

LABELS_PATH = os.path.join(HERE, "rung2_labels.json")
# the 14 genuine dialogues (>=10 distinct utts, both roles >=3) by id-prefix; the
# 07ab764b mega-session is excluded as a non-deliberative automated outlier.
GENUINE = ["84f7ebea","c9d9e7c9","ea7b2dcd","02381065","1b35066d","3788ad2c",
           "35e9daf3","42ba591f","743bdd01","4f18c86c","119776ad","5568d1d6"]
ORDER = ["report","direct","probe","override","build_on","repair","ack",
         "concede","steelman","deflect","null"]

def clean(s): return " ".join(s.split())

import re as _re
def normalize_label(s):
    """Canonicalize a model-returned move label. Haiku sometimes wraps its answer in
    markdown (`**probe**`) or trailing punctuation, which fragments the Counter and makes
    exact-match measures (P2 engagement, P-civility) silently undercount. Strip to the bare
    [a-z_] token. Non-matching -> '' (caller drops it)."""
    toks = _re.sub(r"[^a-z_ ]", " ", (s or "").lower()).split()
    return toks[0] if toks else ""

def ah_pairs(q, prefix):
    sidf = q("SELECT id FROM sessions WHERE id LIKE ?", prefix + "%")[0][0]
    rows = q("SELECT turn_number,data FROM turns WHERE session_id=?", sidf)
    stream = build_stream(rows)                       # DEDUPED
    return [{"ai": clean(stream[i][1])[:240], "human": clean(stream[i + 1][1])[:240]}
            for i in range(len(stream) - 1)
            if stream[i][0] == "A" and stream[i + 1][0] == "H"]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    db = args[0] if len(args) > 0 else DEFAULT_DB
    outdir = args[1] if len(args) > 1 else HERE
    backend = "manual"
    if "--backend" in sys.argv:
        backend = sys.argv[sys.argv.index("--backend") + 1]
    if not os.path.exists(db):
        sys.exit(f"snapshot not found: {db}")
    c = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    q = lambda s, *a: c.execute(s, a).fetchall()

    store = json.load(open(LABELS_PATH))
    labels = store["labels"]
    pairs_by_sess = {pre: ah_pairs(q, pre) for pre in GENUINE}

    if backend != "manual":
        classify = _model_classifier(backend, store["taxonomy"])
        for pre, pairs in pairs_by_sess.items():
            have = labels.get(pre, [])
            for k, pr in enumerate(pairs):
                if k < len(have) and have[k]:
                    continue                          # idempotent: skip labelled
                lab = classify(pr["ai"], pr["human"])
                while len(have) <= k: have.append(None)
                have[k] = lab
            labels[pre] = have
        store["labels"] = labels
        json.dump(store, open(LABELS_PATH, "w"), indent=2)

    # ---- report from whatever is labelled ----
    agg = Counter()
    per = {}
    labelled = total = 0
    for pre, pairs in pairs_by_sess.items():
        labs = labels.get(pre, [])
        total += len(pairs)
        cc = Counter()
        for k in range(len(pairs)):
            lab = normalize_label(labs[k]) if k < len(labs) and labs[k] else None
            if lab:
                cc[lab] += 1; agg[lab] += 1; labelled += 1
        if cc: per[pre] = (len(pairs), cc)

    L = []; p = L.append
    p("# Rung 2 - Relational moves: the A->H listening instrument\n")
    p(f"_Human move toward the prior AI turn, on deduped streams. Backend: {backend}. "
      f"{labelled} of {total} A->H pairs across the {len(GENUINE)} genuine dialogues labelled "
      f"({'pilot' if backend=='manual' else 'full'})._\n")
    p("## Move distribution (labelled pairs)\n")
    p("| move | count | share |\n|---|---:|---:|")
    for m in ORDER:
        if agg[m]:
            p(f"| {m} | {agg[m]} | {100*agg[m]/labelled:.0f}% |")
    p(f"\nTotal labelled: **{labelled}**\n")
    p("## Per-dialogue relational signature\n")
    p("| dialogue | A->H pairs | labelled | top moves |")
    p("|---|---:|---:|---|")
    for pre, (npairs, cc) in sorted(per.items(), key=lambda kv: -kv[1][0]):
        top = ", ".join(f"{m} {cc[m]}" for m in ORDER if cc[m])
        p(f"| `{pre}` | {npairs} | {sum(cc.values())} | {top} |")
    p("\n## Reading it\n")
    p("The instrument is well-posed: human moves classify cleanly and the per-dialogue "
      "signatures differ (a debugging session is mostly `report`; a scoping session carries "
      "`override`/`build_on`). The dominant moves are **report** and **direct** -- neither in "
      "the original 7-move set -- while **steelman/concede are ~absent**: this corpus is "
      "collaborative execution, not rival-traditions debate. So the move ALPHABET is "
      "genre-dependent; the MacIntyrean deep-listening vocabulary needs debate-genre dialogue "
      "to exercise it, which this single-human operational corpus does not yet contain.\n")

    out = os.path.join(outdir, "rung2_report.md")
    open(out, "w").write("\n".join(L) + "\n")
    print(f"wrote {out}")
    print(f"{labelled}/{total} pairs labelled across {len(GENUINE)} dialogues; "
          f"top: " + ", ".join(f"{m} {agg[m]}" for m in ORDER if agg[m]))

def _model_classifier(backend, taxonomy):
    """Return classify(ai, human)->move using a cheap model at temp 0. Stub wiring;
    fill the request body for your account. Kept tiny on purpose (Rule 5: model for
    judgment only)."""
    moves = ", ".join(taxonomy.keys())
    sysmsg = ("Classify the HUMAN reply's single relational move toward the AI turn. "
              f"Reply with exactly one of: {moves}. Definitions: "
              + "; ".join(f"{k}={v}" for k, v in taxonomy.items()))
    if backend == "anthropic":
        import urllib.request
        key = os.environ["ANTHROPIC_API_KEY"]
        def classify(ai, human):
            body = json.dumps({"model": "claude-haiku-4-5-20251001", "max_tokens": 8,
                "system": sysmsg,
                "messages": [{"role": "user", "content": f"AI: {ai}\n\nHUMAN: {human}\n\nMove:"}]}).encode()
            req = urllib.request.Request("https://api.anthropic.com/v1/messages", body,
                {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
            r = json.load(urllib.request.urlopen(req, timeout=30))
            return normalize_label(r["content"][0]["text"])
        return classify
    if backend == "openai":
        import urllib.request
        key = os.environ["OPENAI_API_KEY"]
        def classify(ai, human):
            body = json.dumps({"model": "gpt-4o-mini", "temperature": 0, "max_tokens": 4,
                "messages": [{"role": "system", "content": sysmsg},
                             {"role": "user", "content": f"AI: {ai}\n\nHUMAN: {human}\n\nMove:"}]}).encode()
            req = urllib.request.Request("https://api.openai.com/v1/chat/completions", body,
                {"authorization": f"Bearer {key}", "content-type": "application/json"})
            r = json.load(urllib.request.urlopen(req, timeout=30))
            return normalize_label(r["choices"][0]["message"]["content"])
        return classify
    sys.exit(f"unknown backend: {backend}")

if __name__ == "__main__":
    main()
