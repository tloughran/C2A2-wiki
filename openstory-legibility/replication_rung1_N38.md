# Listening Stays Legible on a 2.7× Corpus

### A preregistered replication of Rung 1, the human-arm uptake measure (C2A2)

**Thomas Loughran**¹\* and **Claude Opus 5**²

¹ Department of Physics and Astronomy, University of Notre Dame, Notre Dame, IN 46556, USA
² Anthropic

\* To whom correspondence should be addressed: **loughran.8@nd.edu**

_Replication note, 2026-07-31._ This paper replicates **one arm** of *Can AI Accelerate
Inter-Tradition Dialogue — and How Would We Know?* (Loughran & Claude Opus 4.8, working paper,
2026-07-01), using that study's analysis instrument `rung1_uptake.py` **unmodified in every
statistic, filter, threshold, and random seed** — the sole change being a disclosed guard that
counts unreadable input rows instead of failing on them (§5.3). The original study is preserved
unedited in the adjacent tab and remains the reference for everything this paper does not re-run.

_Author contributions._ T.L. conceived the original study, owns the research question, and
directed this replication. **Claude Opus 5** wrote the pre-commitment fixing expected outcomes and
falsifiers before the analysis was executed, took the snapshot, ran the analysis, diagnosed the
single non-positive dialogue (§4), and drafted this manuscript. T.L. takes responsibility for all
claims herein.

---

## 1. What this paper is, and what it is not

The original study measured **Rung 1** — whether *listening* leaves a lexical trace in real human
dialogue that survives a role-matched control — on **14 substantive dialogues** drawn from a
snapshot of the OpenStory corpus taken 2026-06-29. That is a small number, and the study said so:
§5.2 is titled "Honest limits on power."

One month of that corpus's growth later, the same measure can be run on more data. This
paper reports that run. **N goes from 14 to 38** and the finding replicates.

**This is the only claim made here.** In particular:

- The **simulation arm** is not re-run. §3.3, §4.2 (the BRIDGE negative), §4.3 (the convener and
  the C0 certification gate), and §4.4 (Rung 2) all rest on constructed dialogues, and no new
  dialogues were generated. Their numbers stand exactly as published.
- The original study's **body is not amended**. It still reports N=14 throughout, deliberately.
  A preregistered paper that quietly swaps in better numbers after the fact has destroyed the
  thing that made it worth reading. The two documents sit side by side instead.
- This is **not a version 2**, and the tab does not call it one. It is a companion covering one
  rung of a five-part ladder.

## 2. Preregistration

The risk specific to a re-run is authoring predictions after seeing results — the failure the
original study was built to avoid, reappearing at the meta level. A pre-commitment was therefore
written and saved **before the analysis was executed**
(`rerun_prereg_2026-07-30.md`), stating four expectations and three falsifiers. At the time it was
written, the 2026-06-30 N=14 report was the only Rung 1 result in existence; an earlier attempt at
a re-run had left no artifact, so nothing newer had been seen. That was verified before running.

All four predictions held:

| # | Prediction, fixed in advance | Outcome |
|---|---|---|
| 1 | Direction holds: median real similarity exceeds the role-matched null | **Held** — median lift +0.041 |
| 2 | Per-session significance *rate* falls somewhat (larger, less curated population) | **Held** — 93% → 89% |
| 3 | Median lift shrinks or holds; should not grow much | **Held** — +0.053 → +0.041 |
| 4 | AI↔AI stays unmeasurable (agent runs are single-shot) | **Held** — 0 of 38 |

None of the three falsifiers fired: median lift was not ≤ 0, the substantive count did not come
back near 14, and it did not overshoot in a way suggesting the deduplication had failed.

**One quantity in the pre-commitment was badly wrong, and this is why it was written.** It
estimated that "roughly 172 sessions may now pass the well-posedness filter," from an
events-per-session proxy. The true figure was **38** — the proxy was off by 4.5×, because it
counted raw `message.*` events while the script counts deduplicated, turn-derived utterances
subject to a ≥4 floor. Different unit entirely. The pre-commitment named the proxy as "not the
script's filter and may be wrong" and listed the overshoot as a falsifier. That is the only reason
this paragraph is a correction on the record rather than a number that quietly never existed.

## 3. Corpus

A static snapshot, `open-story-snapshot-2026-07-30.db`, was taken from the live OpenStory database
via `sqlite3 .backup` (4.7 s, 2.9 GB) and opened read-only. No new dialogue was collected; the
growth is ordinary accumulated use.

| | 2026-06-29 (original) | 2026-07-30 (this run) |
|---|---:|---:|
| turn-bearing sessions | 223 | **947** |
| with a usable stream (≥ 4 utterances) | — | 61 |
| **substantive two-sided dialogues** | **14** | **38** |
| of those, AI↔AI (`agent-*`) | 0 | 0 |

"Substantive" is the original script's own well-posedness gate, unchanged: each role contributes
≥ 3 utterances and the dialogue runs ≥ 10 utterances total. Sessions below it are single-prompt
runs whose role-matched null is degenerate — lift is 0 by construction — so uptake is not merely
noisy there but undefined.

## 4. Results

Deterministic throughout: TF-IDF, 200 shuffles, seed 1729, no model anywhere in the measurement.
`lift = mean(real adjacent cosine) − mean(role-matched random-partner cosine)`. Positive lift means
an utterance resembles the thing actually said to it more than it resembles a random same-role
utterance from the same conversation — specific uptake, not merely shared topic.

| | N=14 (original) | **N=38 (this run)** |
|---|---:|---:|
| median real adjacent cosine | 0.098 | 0.075 |
| median role-matched null | 0.046 | 0.036 |
| **median lift** | **+0.053** | **+0.041** |
| dialogues with positive lift | 14/14 (100%) | **37/38 (97%)** |
| beating the shuffle at p < 0.05 | 13/14 (93%) | **34/38 (89%)** |
| mean A→H lift (*the listening signal*) | +0.034 (11/14) | **+0.024 (31/38)** |
| mean H→A lift (*sanity floor*) | +0.063 (13/14) | **+0.065 (37/38)** |
| A→H explicit back-reference rate | — | 65% |

The effect **attenuates and survives**. Attenuation was predicted (§2, prediction 3) and has the
expected cause: the original 14 were an unusually rich, self-selected set, and a 2.7× larger
population admits more marginal dialogue. The direction that carries the thesis — **A→H**, the
human taking up what the AI said, which is the actual listening claim — remains positive at +0.024
in 31 of 38 dialogues, with an explicit back-reference (a marker or a rare-term reuse) on 65% of
those pairs.

**The lower bound argument is unchanged and still applies.** TF-IDF is lexical, so a short human
reply that genuinely listens while reusing few words scores near zero. This bears asymmetrically:
H→A, where the AI answers by reusing the human's own vocabulary, is lexically easy to see, while
A→H — a brief human reply taking up a long AI answer — is exactly where a lexical measure goes
blind. So A→H being the noisier, weaker direction is *expected*, every number above is a
conservative floor, and weak A→H is not evidence of absence. It is the signal Rung 2's semantic
judgment is designed to buy.

### 4.1 The one non-positive dialogue

Of 38, exactly one has a non-positive lift: session `07ab764b`, with 1,063 utterances — by far the
longest in the corpus — at lift −0.002, p = 0.995, and near-zero cosines on both the real and the
null side (0.006 vs 0.008, against corpus medians of 0.075 and 0.036).

That both terms collapsed together is the diagnostic clue: it rules out "the participants stopped
listening," which would depress the real term while leaving the null where it was. Something had
gone wrong with the *documents*, not with the dialogue.

Two hypotheses were tested and both were wrong. The session spans 121 days and 324,495 events —
94× the next-largest session — so the natural guess was **topic drift**: a session id reused across
four months of unrelated work, leaving TF-IDF vectors near-orthogonal at distance. Measured
directly, that is not what happened. Similarity between utterances five deciles apart is 0.194,
against 0.223 within a decile — a ratio of **1.1×**, where a normal session of comparable structure
gives 2.2×. The session is not drifting. It is *uniformly self-similar*: everything resembles
everything, equally, regardless of distance.

The reason is visible on inspection. **Of its 530 assistant-side utterances, 429 — 81% — are the
literal string `"No response requested."`** The median assistant turn is **3 words**, against 304 in
a comparison session. Forty-four percent of the human turns are exact duplicates of another human
turn, the most frequent being an automated retry sixteen times over: *"[your previous response had
no visible output. please continue…]"*. This is not a conversation. It is a stuck agent loop, and
uptake against a placeholder is undefined.

**The defect is in our filter, not in the data.** OpenStory recorded faithfully what its client
emitted; `"No response requested."` is a real thing a coding agent writes when a system event needs
no reply. The well-posedness gate counts *utterances* and never asks whether they carry content, so
530 placeholders passed a test designed to exclude exactly this. That is our bug, inherited
unchanged from the original study, and it has now been found because a larger corpus contained an
instance extreme enough to expose it.

**It changes nothing, and the headline number keeps it in.** Removing the session — a *post hoc*
exclusion, formed after seeing the result, and marked as such — moves no reported statistic:

| | N=38, as preregistered | N=37, post hoc |
|---|---:|---:|
| median lift | +0.041 | +0.041 |
| positive | 37/38 | 37/37 |
| p < 0.05 | 34/38 | 34/37 |
| mean A→H | +0.024 | +0.025 |
| mean H→A | +0.065 | +0.066 |
| A→H back-reference | 65% | 66% |

Every headline figure in §4 therefore **retains** `07ab764b`. The sensitivity column is disclosed
for completeness, not adopted; trading a preregistered N=38 for a prettier N=37 would buy a
denominator and spend the only thing that makes the number worth anything.

**Registered now, for the next run:** the well-posedness gate should carry a *content* floor
alongside its utterance floor — a minimum median content length per role, or explicit exclusion of
known placeholder strings. Naming the criterion here, in advance of the snapshot it will first
apply to, is what converts tonight's post-hoc discovery into next time's preregistered filter.

## 5. Data quality in the source corpus

Three defects in the underlying store bear on how these numbers should be read. All three are
reported to the OpenStory developers separately; two are longstanding, one is new.

### 5.1 Turn duplication, 9.6× (longstanding)

The store holds **25,006 turn rows** that reduce to **2,445 distinct turns** — a **9.6× inflation**.
The replay path re-folds the same events on each pass and inserts duplicate rows under *fresh*
turn numbers, so writes accumulate instead of replacing. The original study diagnosed this at 2–9×
a year ago; it is still live, now at the top of that range on a corpus an order of magnitude larger.

The analysis is immune by construction: `build_stream` collapses turn rows whose `event_ids` tuple
has already been seen — same source events, same turn — before any measurement. Readers of the raw
store are not immune, and any count taken from it without deduplication is wrong by about tenfold.

### 5.2 Unreadable turn rows, 5.8% (new since June)

**1,452 of 25,006 rows (5.8%), across 191 sessions, carry an empty `data` field**, and most also
carry an empty timestamp — a turn row exists, but holds no content to score. The 2026-06-29
snapshot had **zero** such rows. This is content loss that appeared in the intervening month.

**The cause has not been determined** and is not guessed at here. What can be said is the effect on
this paper: those utterances are gone, they would otherwise have counted toward the ≥3-per-role and
≥10-total thresholds, and so the substantive count of 38 is itself a floor. Which direction this
biases the *lift* is unknown, since nothing is known about what the lost rows contained.

This was found only because the re-run **crashed** on them, and identified as new only because a
June snapshot was still on disk to compare against. A silent-skip implementation would have
produced a smaller population with no indication why.

### 5.3 The one change to the instrument

`rung1_uptake.py` was modified in exactly one respect: unreadable rows are **skipped and counted**,
and the count is printed in the report's population block. No statistic, filter, threshold, or seed
was touched. The alternative — dropping them silently — would have shrunk a reported population
with nothing on the page to say so, which is the same class of error as amending a preregistered
result.

## 6. What this licenses

The original study's central Rung 1 claim — that listening is legible in real dialogue without a
model in the loop, and separable from shared topic by a role-matched control — now rests on 38
dialogues rather than 14, with a smaller effect and one diagnosed exclusion candidate that changes
nothing.

It does **not** license anything about the simulation arm, the BRIDGE negative, the convener, or
Rung 2, none of which were re-run. It does not resolve §5.2 of the original study, whose
underpowered claim is the *located limit* (P3′b) and lives in the constructed arm. And it does not
make the human corpus into rival-tradition debate: the genre finding of the original study stands
untouched, and is in fact reinforced — a corpus of collaborative execution grew 4× and produced no
AI↔AI dialogue and no debate.

## 7. Reproducibility

Fully deterministic. Same seed, same shuffles, same script, read-only snapshot.

```
openstory-legibility/
  rung1_uptake.py                     the instrument (§5.3 guard is its only change)
  rerun_prereg_2026-07-30.md          the pre-commitment, written before execution
  rerun_2026-07-30/
    rung1_report.md                   generated report, N=38
    rung1_uptake.json                 per-session record: lift, p, A→H, H→A, back-reference
    run.log
```

The snapshot itself (2.9 GB) is not distributed. The population, thresholds, seed, and shuffle
count are all stated above and in the script, so the run reproduces from any snapshot of the same
store; the specific figures reported here are of course tied to this one.
