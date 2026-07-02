#!/usr/bin/env python3
"""
rung1_uptake.py - Rung 1 of the listening ladder: is "uptake" legible in the
OpenStory substrate WITHOUT any model spend?

Read-only and idempotent by construction: opens a STATIC snapshot of
open-story.db (mode=ro&immutable=1) and writes a markdown report + a JSON of
per-session uptake curves. Run it as often as you like, on any snapshot, on any
machine. It never touches the live DB and uses NO model (pure-numpy TF-IDF).

    python3 rung1_uptake.py [snapshot.db] [out_dir]

Defaults read the snapshot beside the live DB and write next to this script.

------------------------------------------------------------------------------
WHAT "UPTAKE" MEANS HERE, AND WHY THIS IS THE RIGHT FIRST TEST
------------------------------------------------------------------------------
A `turn` in this corpus is one message beat. Human prompts and AI responses
live in separate, alternating turns (sometimes combined in one). So we first
reconstruct each session's dialogue STREAM: flatten human-then-eval per turn,
in turn_number order, dropping empties -> an ordered list of (role, text)
utterances, role in {H, A}.

"Uptake" = does utterance n+1 take up what utterance n introduced. We measure it
as cosine similarity between adjacent utterances (TF-IDF, computed per session so
the vocabulary is the conversation's own). Two directions matter:
  A->H : the next HUMAN prompt takes up the prior AI response  (is the human
         listening / does the dialogue build) -- the load-bearing signal.
  H->A : the AI response takes up the human prompt (near-guaranteed; a sanity
         floor more than a finding).

THE VERDICT IS NOT "similarity is high." A whole session about one topic has high
similarity everywhere. The real question is whether ADJACENCY carries specific
uptake above chance. The control must be ROLE-MATCHED: adjacent pairs are always
cross-role (a short human prompt next to a long AI eval, few shared words), so an
all-pairs floor that mixes in same-role pairs (two long AI evals on one topic,
much shared vocabulary) is confounded and will look artificially high. Instead:

  For each adjacent cross-role pair -- the later utterance "taking up" the earlier
  one -- compare its real cosine to the SAME later utterance paired with a RANDOM
  opposite-role utterance from elsewhere in the same session.
    lift = mean(real adjacent cosine) - mean(role-matched random-partner cosine)
  Positive lift = an utterance resembles its ACTUAL predecessor more than a random
  same-conversation utterance of the same role, i.e. specific uptake, not topic.
  A permutation p reassigns every partner at random N times; p = fraction of
  reassignments whose mean >= the real adjacent mean.

HONEST LIMIT (and exactly what Rung 2 would buy): TF-IDF is lexical. A short
human backchannel that genuinely listens -- "yes; let's check", "pushed, no
conflict" -- shares few words with a long AI answer and will score ~0 here. So
this metric is a CONSERVATIVE LOWER BOUND on uptake. If listening is visible even
through a lexical lens, that is a strong green light for Rung 2 (model-as-judgment).
If it is not, we have learned cheaply that seeing listening needs semantics, and
we know precisely why.
"""
import sqlite3, json, sys, os, re, math, random, datetime
from collections import Counter

DEFAULT_DB = os.path.expanduser(
    "~/Documents/Non-Claude Projects/OpenStory/data/open-story-snapshot.db")
HERE = os.path.dirname(os.path.abspath(__file__))

SHUFFLES = 200
SEED = 1729                 # deterministic: same snapshot -> same numbers
MIN_UTT = 4                 # need >=4 utterances for a meaningful control
REF_MARKERS = re.compile(
    r"\b(you (said|mentioned|noted|wrote|asked|suggested|proposed)|as you|"
    r"your (point|answer|response|reply|suggestion|plan|fix)|"
    r"that('?s| is| was)?|this (one|fix|change|approach)|earlier|above|"
    r"the (former|latter)|like you|per your)\b", re.I)

STOP = set("""a an the and or but if then else of to in on at for with without from by as is are was were
be been being it its this that these those i you he she we they them us me my your our their his her
do does did done have has had not no yes so just like can could would should will shall may might must
about into over under again more most very there here what which who whom whose how when where why
ok okay let lets let's now still also too than out up down off back also per re""".split())

TOKEN = re.compile(r"[a-z0-9][a-z0-9'\-]+")

def content(x):
    if isinstance(x, dict): return x.get("content") or x.get("text") or ""
    if isinstance(x, str):  return x
    return ""

def toks(s):
    return [t for t in TOKEN.findall(s.lower()) if len(t) >= 3 and t not in STOP]

def tfidf_vectors(docs):
    """Pure-numpy TF-IDF over a list of token-lists. Returns L2-normalized rows
    (list of dict term->weight) -- sparse dicts, so cosine is a dict dot."""
    N = len(docs)
    df = Counter()
    for d in docs:
        for t in set(d): df[t] += 1
    idf = {t: math.log((N + 1) / (c + 1)) + 1.0 for t, c in df.items()}
    vecs = []
    for d in docs:
        tf = Counter(d)
        v = {t: (1 + math.log(c)) * idf[t] for t, c in tf.items()}
        nrm = math.sqrt(sum(w * w for w in v.values())) or 1.0
        vecs.append({t: w / nrm for t, w in v.items()})
    return vecs

def cos(a, b):
    if len(a) > len(b): a, b = b, a
    return sum(w * b.get(t, 0.0) for t, w in a.items())

def build_stream(rows):
    """rows: [(turn_number, data_json)] -> ordered [(role, text)] utterances.

    Dedups replay-duplicated turns first. The S7 recrystallize replay re-folds the
    same events on each pass, inserting duplicate turn rows with FRESH turn_numbers
    (insert_turn keys on turn:{sid}:{n}, so a changed n accumulates instead of
    replacing). Measured 2-9x inflation across every session. We collapse turn rows
    whose event_ids tuple was already seen (the principled key: same source events =
    same turn), keeping the first occurrence in turn_number order. Falls back to a
    (human,eval) content signature when event_ids is absent."""
    seen = set()
    stream = []
    for _, d in sorted(rows, key=lambda r: r[0]):
        j = json.loads(d)
        ev = tuple(j.get("event_ids") or [])
        h = content(j.get("human")).strip()
        e = content(j.get("eval")).strip()
        key = ev if ev else ("noeid", h[:120], e[:120])
        if key in seen:
            continue
        seen.add(key)
        if h: stream.append(("H", h))
        if e: stream.append(("A", e))
    return stream

def session_metrics(stream, rng):
    texts = [t for _, t in stream]
    roles = [r for r, _ in stream]
    vecs = tfidf_vectors([toks(t) for t in texts])
    n = len(vecs)
    by_role = {"H": [i for i in range(n) if roles[i] == "H"],
               "A": [i for i in range(n) if roles[i] == "A"]}
    adj = [cos(vecs[i], vecs[i + 1]) for i in range(n - 1)]            # the raw curve
    adj_roles = [roles[i] + ">" + roles[i + 1] for i in range(n - 1)]
    # cross-role adjacent pairs: (later, earlier, direction "A>H" / "H>A")
    pairs = [(i + 1, i, adj_roles[i]) for i in range(n - 1)
             if roles[i] != roles[i + 1]]
    real = [cos(vecs[later], vecs[earlier]) for later, earlier, _ in pairs]
    real_mean = (sum(real) / len(real)) if real else 0.0
    # role-matched null: re-pair each 'later' with a random opposite-role partner
    null_means = []
    for _ in range(SHUFFLES):
        acc = []
        for later, earlier, _ in pairs:
            pool = by_role[roles[earlier]]
            if len(pool) < 2:
                acc.append(cos(vecs[later], vecs[earlier])); continue
            j = earlier
            while j == later or j == earlier:        # genuinely different partner
                j = pool[rng.randrange(len(pool))]
                if len(pool) == 1: break
            acc.append(cos(vecs[later], vecs[j]))
        if acc: null_means.append(sum(acc) / len(acc))
    null_mean = (sum(null_means) / len(null_means)) if null_means else 0.0
    pval = ((sum(1 for m in null_means if m >= real_mean) + 1) /
            (len(null_means) + 1)) if null_means else 1.0
    # direction lifts (real - role-matched-null), computed per direction
    def dir_lift(tag):
        idx = [k for k, (_, _, d) in enumerate(pairs) if d == tag]
        if not idx: return None
        rmean = sum(real[k] for k in idx) / len(idx)
        nmean = 0.0
        for _ in range(SHUFFLES):
            acc = []
            for k in idx:
                later, earlier, _ = pairs[k]
                pool = by_role[roles[earlier]]
                j = earlier
                if len(pool) >= 2:
                    while j == later or j == earlier:
                        j = pool[rng.randrange(len(pool))]
                acc.append(cos(vecs[later], vecs[j]))
            nmean += sum(acc) / len(acc)
        nmean /= SHUFFLES
        return {"real": rmean, "null": nmean, "lift": rmean - nmean, "n": len(idx)}
    # explicit-reference rate on A->H pairs (next human refers back to AI)
    ah = [(later, earlier) for later, earlier, d in pairs if d == "A>H"]
    refs = 0
    for later, earlier in ah:
        htext = texts[later]
        overlap = sum(1 for t in (set(toks(texts[earlier])) & set(toks(htext))) if t in vecs[earlier])
        if REF_MARKERS.search(htext) or overlap >= 2:
            refs += 1
    # "substantive" = a real two-sided dialogue where uptake is well-posed: each
    # role appears >=3 times, >=10 utterances, AND the role-matched null is
    # non-degenerate (real_mean != null_mean). The degenerate case -- where they
    # are exactly equal -- is the automated/repetitive scheduled-run signature:
    # near-identical utterances mean every random partner is the same as the real
    # one, so lift==0 by construction. Those sessions say nothing about listening
    # and must not be averaged in.
    min_role = min(len(by_role["H"]), len(by_role["A"]))
    substantive = (min_role >= 3 and n >= 10 and abs(real_mean - null_mean) > 1e-9)
    return {
        "n_utt": n, "min_role": min_role, "substantive": substantive,
        "curve": [round(x, 4) for x in adj], "curve_roles": adj_roles,
        "real_mean": real_mean, "null_mean": null_mean,
        "lift": real_mean - null_mean, "shuffle_p": pval,
        "AtoH": dir_lift("A>H"), "HtoA": dir_lift("H>A"),
        "ah_pairs": len(ah), "ah_ref_rate": (refs / len(ah)) if ah else None,
    }

def main():
    db = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DB
    outdir = sys.argv[2] if len(sys.argv) > 2 else HERE
    if not os.path.exists(db):
        sys.exit(f"snapshot not found: {db}\nMake one with sqlite3 .backup (see probe_substrate.py header).")
    c = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    q = lambda s, *a: c.execute(s, a).fetchall()

    sess = q("SELECT session_id, COUNT(*) n FROM turns GROUP BY session_id")
    turn_bearing = len(sess)
    rng = random.Random(SEED)
    results = {}
    skipped_short = 0
    for sid, _ in sess:
        rows = q("SELECT turn_number, data FROM turns WHERE session_id=?", sid)
        stream = build_stream(rows)
        if len(stream) < MIN_UTT:
            skipped_short += 1
            continue
        m = session_metrics(stream, rng)
        m["is_agent"] = sid.startswith("agent-")
        results[sid] = m

    # ---- aggregate verdict ----
    R_all = list(results.values())
    measured = len(R_all)
    R = [r for r in R_all if r["substantive"]]          # the real two-sided dialogues
    n_sub = len(R)
    med = lambda xs: sorted(xs)[len(xs) // 2] if xs else float("nan")
    mean = lambda xs: (sum(xs) / len(xs)) if xs else float("nan")
    lifts = [r["lift"] for r in R]
    pos_lift = sum(1 for x in lifts if x > 0)
    sig = sum(1 for r in R if r["shuffle_p"] < 0.05)
    med_lift = med(lifts)
    med_real = med([r["real_mean"] for r in R])
    med_null = med([r["null_mean"] for r in R])
    ah = [r["AtoH"]["lift"] for r in R if r["AtoH"] is not None]
    ha = [r["HtoA"]["lift"] for r in R if r["HtoA"] is not None]
    ah_pos = sum(1 for x in ah if x > 0)
    ha_pos = sum(1 for x in ha if x > 0)
    refrates = [r["ah_ref_rate"] for r in R if r["ah_ref_rate"] is not None]
    # all-population numbers, for honesty about how the median washes out
    all_pos = sum(1 for r in R_all if r["lift"] > 0)
    all_med = med([r["lift"] for r in R_all])

    L = []
    p = L.append
    p("# Rung 1 - Uptake: is listening legible without a model?\n")
    p(f"_Generated {datetime.datetime.now():%Y-%m-%d %H:%M} from `{os.path.basename(db)}` "
      f"(read-only). Deterministic: TF-IDF, {SHUFFLES} shuffles, seed {SEED}. No model._\n")
    p("## Population\n")
    p(f"- turn-bearing sessions: **{turn_bearing}**")
    p(f"- with a usable dialogue stream (>= {MIN_UTT} utterances): **{measured}**")
    p(f"- skipped (too short for a control, < {MIN_UTT} utterances): **{skipped_short}**")
    p(f"- **substantive two-sided dialogues** (each role >=3 utts, >=10 utts total): "
      f"**{n_sub}** -- these are the only sessions where uptake is well-posed; the rest are "
      f"single-prompt runs whose role-matched null is degenerate (lift==0 by construction).")
    p(f"- of measured, AI<->AI (`agent-*`): **{sum(1 for r in R_all if r['is_agent'])}** "
      f"(agent sessions are single-shot in this corpus; AI<->AI uptake is not yet measurable)\n")
    p("## The verdict (real predecessor vs. role-matched random partner)\n")
    p("`lift = mean(real adjacent cosine) - mean(role-matched random-partner cosine)`. "
      "Positive lift means an utterance resembles its ACTUAL predecessor more than a random "
      "same-role utterance from the same conversation -- specific uptake, not just shared topic. "
      f"**Reported on the {n_sub} substantive dialogues.**\n")
    p(f"- median real adjacent cosine: **{med_real:.3f}**")
    p(f"- median role-matched null cosine: **{med_null:.3f}**")
    p(f"- median **lift**: **{med_lift:+.3f}**")
    p(f"- dialogues with positive lift: **{pos_lift}/{n_sub}** ({100*pos_lift/n_sub:.0f}%)")
    p(f"- dialogues where real beats role-matched null at p<0.05: **{sig}/{n_sub}** "
      f"({100*sig/n_sub:.0f}%)")
    p(f"- _(for contrast, across all {measured} measured incl. degenerate runs: median lift "
      f"{all_med:+.3f}, positive {all_pos}/{measured} -- the degenerate runs wash the median to ~0)_\n")
    p("## Direction (each is real - role-matched null, on substantive dialogues)\n")
    p(f"- mean **A->H** uptake lift (next human takes up the AI - the listening signal): "
      f"**{mean(ah):+.3f}**, positive in **{ah_pos}/{len(ah)}**")
    p(f"- mean **H->A** uptake lift (AI takes up the human - sanity floor): "
      f"**{mean(ha):+.3f}**, positive in **{ha_pos}/{len(ha)}**")
    p(f"- explicit back-reference rate on A->H pairs (marker or rare-term overlap): "
      f"**{mean(refrates):.0%}**\n")
    p("## Per-session (substantive dialogues, top 20 by utterance count)\n")
    p("| session | utt | real | null | lift | p | A->H lift | H->A lift | ref% |")
    p("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    sub_items = [(sid, r) for sid, r in results.items() if r["substantive"]]
    top = sorted(sub_items, key=lambda kv: kv[1]["n_utt"], reverse=True)[:20]
    for sid, r in top:
        dl = lambda v: "-" if v is None else f"{v['lift']:+.3f}"
        p(f"| `{sid[:14]}` | {r['n_utt']} | {r['real_mean']:.3f} | {r['null_mean']:.3f} | "
          f"{r['lift']:+.3f} | {r['shuffle_p']:.3f} | {dl(r['AtoH'])} | {dl(r['HtoA'])} | "
          f"{'-' if r['ah_ref_rate'] is None else format(r['ah_ref_rate'],'.0%')} |")
    p("\n## Honest limit\n")
    p("TF-IDF is lexical, so short human backchannels that genuinely listen but reuse few "
      "words score ~0. This makes every number above a **conservative lower bound** on uptake. "
      "It also bears asymmetrically on direction: **H->A** (the AI reusing the human's own "
      "vocabulary to answer) is lexically easy to see, while **A->H** (a brief human reply "
      "taking up a long AI answer) is exactly where lexical goes blind. So A->H being the "
      "noisier, sometimes-negative direction is expected -- and it is precisely the signal "
      "Rung 2's semantic judgment would buy. Signal present even through this lens is strong "
      "evidence; weak A->H is not evidence of absence.\n")

    report = os.path.join(outdir, "rung1_report.md")
    with open(report, "w") as f:
        f.write("\n".join(L) + "\n")
    curves = os.path.join(outdir, "rung1_uptake.json")
    with open(curves, "w") as f:
        json.dump({"generated": str(datetime.datetime.now()), "db": os.path.basename(db),
                   "shuffles": SHUFFLES, "seed": SEED, "sessions": results}, f, indent=1)
    print(f"wrote {report}")
    print(f"wrote {curves}")
    print(f"{n_sub} substantive dialogues of {measured} measured ({turn_bearing} turn-bearing); "
          f"median lift {med_lift:+.3f}; positive {pos_lift}/{n_sub}; sig(p<.05) {sig}/{n_sub}; "
          f"A->H mean {mean(ah):+.3f} ({ah_pos}/{len(ah)}+); H->A mean {mean(ha):+.3f} ({ha_pos}/{len(ha)}+)")

if __name__ == "__main__":
    main()
