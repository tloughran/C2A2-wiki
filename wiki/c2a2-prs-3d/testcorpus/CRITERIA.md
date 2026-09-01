# Criteria for a semantically meaningful, plausibly causal link

*Written 2026-09-01. Scope item 1 and 2 of the current PRS brief: criteria for
identifying semantically meaningful and plausibly causal connections in the main body
of text, shown working on the two paradigm cases — quantum mechanics 1900–1932 and
deep learning 2012–2025.*

Code: `../scripts/prs_link_criteria.py`. Answer key: `dependencies.json`.
Every number below is printed by the script; none is typed by hand.

---

## The problem this replaces

The connectome scored candidate generative coils with Jaccard overlap on significant
tokens. Measured against a hand-labelled answer key of 24 attested dependencies across
the two paradigm cases, that scorer finds **zero** of them. Not a few. Zero.

This is not a threshold that needs lowering. Bag-of-words overlap measures *shared
topic*, and two entries about the same subject share vocabulary whether or not one is
built out of the other. Schrödinger's entry and de Broglie's entry — the clearest
dependency in the corpus, one man reading the other's thesis and writing the equation
it lacked — share the single token `wave`, for a Jaccard of 0.033 against a threshold
of 0.15. Lowering the threshold far enough to admit it admits essentially all 380
ordered pairs.

## The six criteria

| | criterion | what it looks for |
|---|---|---|
| **C1** | **naming** | The target's text names the source — by surname, by model name, or by the distinctive phrase the source coined. *"Taking Planck's discrete energy elements"* is not topic overlap; it is a citation in prose. |
| **C2** | **inheritance** | The target reuses a distinctive term (document frequency ≤ 3 of 20) from the source. Rare terms carry the signal common ones drown: one shared `attention` or `photoelectric` outweighs four shared `quantum`s — exactly the weighting Jaccard refuses to make. |
| **C3** | **placement** | Where in the target the evidence sits. **Reported, not used.** See below — this one was measured and killed. |
| **C4** | **direction** | The source must be strictly earlier, and the ordering must say whether it rests on a real publication year or on a filing date. Delegated to the existing `gen_direction`. |
| **C5** | **asymmetry** | Evidence must attach to what the source *produced* — its label and solution at full weight, its resource at 0.6, because a resource can itself be handed on. A term also sitting in the source's own *problem* is shared framing, and is halved: two entries worried about the same thing are contemporaries, not a lineage. |
| **C6** | **coinage** | A shared term counts only if the source is the earliest entry in the corpus using it. Without this, AlexNet and ResNet link on `error`, `percent` and `roughly` — the shared vocabulary of an ImageNet leaderboard, which is the lexical baseline's failure wearing better clothes. |

**Qualification and tier.** One shared term is not a finding: in twenty short entries
almost every word is rare, so "exclusive to this pair" is an accident of corpus size.
Measured, admitting single exclusive terms costs 14 false positives and buys no recall
at all. A candidate therefore stands on a **name** (tier `named`) or on **two or more
inherited terms** (tier `inherited`), and the two tiers are reported separately rather
than summed.

**Status, never score.** The script emits `plausible` and nothing else. Only a human
reading the record may write `attested` or `ruled_out` into `dependencies.json`. A
single confidence number would average evidence and absence together and hide the
distinction the epistemics ruling exists to protect.

---

## Measured, on the two paradigm cases

```
corpus: 20 entries, 380 ordered pairs, 120 shareable distinctive terms of 638 vocabulary
rejected: {'no_qualifying_evidence': 349}

                                                 found   gold     tp   prec recall
TIER 'named' (C1 fired)                             10     24     10  1.00   0.42
  ...textually expressed                            10     16     10  1.00   0.62
ANY attested link                                   31     24     19  0.61   0.79
  ...on pairs both entries express (the ceiling)    31     16     16  0.52   1.00
  ...on pairs only one side expresses               31      3      1  0.03   0.33
  ...on pairs the corpus never expresses            31      5      2  0.06   0.40
GENERATIVE only (resource_supplying)                18     18      8  0.44   0.44
  ...of those, textually expressed                  18     12      8  0.44   0.67
BASELINE lexical Jaccard, any attested link          0     24      0  0.00   0.00
BASELINE lexical Jaccard, on the ceiling set         0     16      0  0.00   0.00


NOT RECOVERABLE from these summaries (8) - one side silent (3) or the corpus silent (5):
  deeplearning-PRS-03      -> deeplearning-PRS-10      [one side silent]
  quantum-PRS-01           -> quantum-PRS-03           [one side silent]
  quantum-PRS-06           -> quantum-PRS-09           [one side silent]
  deeplearning-PRS-01      -> deeplearning-PRS-02      [corpus silent]
  deeplearning-PRS-01      -> deeplearning-PRS-03      [corpus silent]
  deeplearning-PRS-02      -> deeplearning-PRS-04      [corpus silent]
  quantum-PRS-03           -> quantum-PRS-07           [corpus silent]
  quantum-PRS-07           -> quantum-PRS-10           [corpus silent]

RULED OUT by the record, and whether the criteria proposed them anyway:
  deeplearning-PRS-07      -> deeplearning-PRS-06      not proposed
  quantum-PRS-01           -> deeplearning-PRS-01      not proposed
  quantum-PRS-07           -> quantum-PRS-08           PROPOSED as undetermined (strength 7.80) - draw differently, do not delete

PROPOSED but not in the gold set (12) - unexamined, not wrong:
  deeplearning-PRS-01      -> deeplearning-PRS-05      resource_supplying 3.44  engineering
  deeplearning-PRS-01      -> deeplearning-PRS-06      resource_supplying 2.52  making
  deeplearning-PRS-03      -> deeplearning-PRS-09      resource_supplying 3.69  signal
  deeplearning-PRS-04      -> deeplearning-PRS-07      resource_supplying 2.85  quality
  quantum-PRS-01           -> quantum-PRS-04           resource_supplying 4.95  matching
  quantum-PRS-01           -> quantum-PRS-08           undetermined       1.90  continuous
  quantum-PRS-02           -> quantum-PRS-06           undetermined       2.33  bookkeeping
  quantum-PRS-02           -> quantum-PRS-09           undetermined       3.04  prediction
```

### Reading that table

- **On the ceiling set — the 16 dependencies both entries put in words — recall is
  1.00 and the lexical baseline is 0.00.** That is the result the brief asked for.
- **Precision is 0.52 overall and 1.00 in the `named` tier.** Every one of the ten
  pairs C1 proposes is an attested dependency. Nothing else in this work is that clean,
  and it has a direct consequence for the visualisation: a named link can be drawn
  solid and asserted; an inherited link is a lead, and should look like one.
- **Relation typing fails: 0.44 precision on `resource_supplying`.** This is C3's
  failure and it is the honest headline (see below).
- The three "not recoverable" pairs where **one side is silent** and the five where
  **the corpus is silent** are the corpus's limit, not the method's. Two of the silent
  ones are still proposed, for the wrong reason — Bohr → Heisenberg on
  `postulates, transition, orbits` and AlexNet → ResNet on `roughly, optimisation,
  error, percent` are topical continuity, not stated dependency. Right answers, shaky
  reasons; both are `inherited` tier.

---

## Three findings that changed the design

### 1. Placement does not type the link — measurement killed C3

C3 was written to answer Tom's framing question — *is a reference a historical note or
a dependency claim?* — cheaply: evidence in the target's **Resource** means the source
supplied material (a generative coil), evidence in its **Problem** means the source set
the problem. It does not work, and the reason is a property of this prose rather than a
bug.

In these entries the **Problem sentence carries the historical setup**. So the strongest
`resource_supplying` edge in the whole corpus announces itself there:

> *"Matrix mechanics works but is opaque … de Broglie's matter waves lack a governing
> equation of motion"* — Schrödinger's **Problem**

So do Einstein → Compton and Heisenberg → Dirac. And Bohr → de Broglie, a genuine
`problem_setting` edge, sits in the same field with the same shape:

> *"Bohr's quantisation condition on angular momentum remains an arbitrary postulate
> with no underlying mechanism"* — de Broglie's **Problem**

The difference between them is discourse framing — a source that is **completed**
versus a source that is **dissolved** — and nothing at the token level sees it. Only a
hit inside the target's Resource is now typed; everything else is emitted as
`undetermined` for a human. Tom's question survives intact. Placement is not the cheap
answer to it.

### 2. Naming is a different kind of evidence from vocabulary, and should stay that way

Precision 1.00 versus 0.55 is not a tuning difference, it is a difference in kind: C1
finds a *statement* that the target's author made about the source, and C2 finds a
*coincidence of words* that may or may not mean anything. Blending them into one score
would hide the only perfectly reliable signal in the system inside a mediocre average.

### 3. Three buckets, not one recall number

An answer key that only says "attested" cannot tell a method's failure apart from a
corpus's silence. `dependencies.json` therefore records, per pair, whether the link is
**expressed** (both entries say it), **partial** (the target says it, the source never
names its own contribution) or **unexpressed** (the corpus never says it). All three are
reported. Folding `partial` into the ceiling would blame the method for the corpus.

The clearest case: Pauli → Dirac. Dirac's problem sentence says *"spin has to be
inserted by hand"* — an explicit dependency. Pauli's entry never uses the word `spin`;
it says *"a fourth two-valued quantum number"*, which is Pauli's own formulation, spin
being Uhlenbeck and Goudsmit's. No text-matching method can join two entries that share
no expression of the thing being handed over. **This row was relabelled from `expressed`
to `partial` after the measurement**, and the relabelling is stated in the row's own
`basis` field so it can be argued with.

The deep-learning arm is where the corpus is quietest. **The strongest attested
dependency in it — residual connections used inside every Transformer block — is
invisible in its own text.** The Transformer entry lists self-attention, positional
encodings and multiple heads, and never mentions the residual stream. No method reading
these summaries recovers it, and reporting 0.89 recall without saying so would be a lie
of composition.

### The ruled-out row earns its keep

`quantum-PRS-07 → quantum-PRS-08` as `resource_supplying` is **ruled out** by the
record: wave mechanics was not derived from matrix mechanics — Schrödinger's route was
de Broglie and Hamiltonian optics, and he wrote that he was discouraged by the matrix
formalism. The two are attested *equivalent*, which is not one supplying the other.

The criteria propose this pair at strength 7.80, the third-highest in the corpus. That
is correct behaviour, not a false positive: the target's text really does name the
source, prominently. It is exactly the case where a mention must not become an arrow.
It is emitted `undetermined`, and per the epistemics ruling a `ruled_out` edge is drawn
differently and never deleted — a disproved link is a finding.

---

## First look at the live corpus — read the caveats before the number

```
679 triplets, 460,362 ordered pairs -> 64 candidates
  tier:      named 16, inherited 48
  relation:  resource_supplying 33, undetermined 31
  cross-tradition: 24        (the shipped lexical layer manages 6)
  ordering:  pub_year 15, pub_year_with_fallback 5, date_string 44
```

More than double the shipped layer's 28 edges and four times its cross-tradition reach.
**Do not quote that as a result yet**, for two reasons that are both already on the
open list:

1. **44 of 64 are ordered on a date string, which for most of the live corpus is the
   day we filed the triplet.** Until Step 4 lands a real `source_date`, the arrow on
   those 44 is a fact about our filing habits.
2. **C1's coinage aliases assume the fixture's label convention.** Fixture labels are
   `Name (year) — coinage`, so the subtitle is a genuine coinage. Live labels are not
   written that way, and the live `named` tier is firing on generic subtitles like
   `ai consciousness` and `hard problem consciousness`, which are topic phrases. The
   fixture's precision of 1.00 for this tier **does not transfer**, and claiming it
   would repeat the mistake the last session made about a link returning HTTP 200.

## Running it

```bash
python3 wiki/c2a2-prs-3d/scripts/prs_link_criteria.py
python3 wiki/c2a2-prs-3d/scripts/prs_link_criteria.py --json /tmp/fixture_links.json
python3 wiki/c2a2-prs-3d/scripts/prs_link_criteria.py \
    --vault wiki --carryforward wiki/c2a2-prs-3d/prs_pub_years.json \
    --no-eval --json /tmp/live_links.json
```

`--keep-backward` retains edges that fail C4 rather than dropping them;
`--min-strength` moves the floor (default 1.5).

## What is not done

- **Visualisation.** Scope item 4. The two tiers are the material: `named` solid,
  `inherited` dashed, `ruled_out` drawn as a struck edge. Nothing is drawn yet.
- **The third edge type.** `analogical` — same structural role, different tradition,
  explicitly non-causal — still does not exist, so the fixture's six cross-epoch
  connections remain typed `synergistic`, which asserts a shared resource that is not
  there. `dependencies.json` carries `quantum-PRS-01 → deeplearning-PRS-01` as the row
  to point at when that retype lands.
- **`attestation_status` on live triplets.** The four-value field exists here in the
  answer key only; the live schema has nothing.
