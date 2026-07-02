# Can AI Accelerate Inter-Tradition Dialogue — and How Would We Know?

### A preliminary, controlled study of constructed rival-tradition agents (C2A2)

**Thomas Loughran**¹\* and **Claude Opus 4.8**²

¹ Department of Physics and Astronomy, University of Notre Dame, Notre Dame, IN 46556, USA
² Anthropic

\* To whom correspondence should be addressed: **loughran.8@nd.edu**

_Working paper, 2026-07-01. Proof-of-concept for the C2A2 accelerator/detector thesis. All results
are preliminary (small panel, one generator family); a strengthening plan is set out in the Discussion.
Every dialogue, the preregistration, and the analysis scripts are retained so the study reproduces from
the transcripts alone._

_Author contributions._ T.L. conceived the study, fixed the preregistration, chose the traditions and the
seam, and ran all dialogue generation; the AI coauthor implemented the analysis code and drafted the
manuscript under T.L.'s direction. T.L. takes responsibility for all claims herein.

---

## 1. Introduction

Some of the deepest disagreements between people are not disagreements about facts. They are
disagreements between whole **traditions of inquiry** — bodies of thought with their own questions,
standards of evidence, and vocabularies. A physicist who treats spacetime as the bedrock of reality and
a cognitive scientist who treats conscious experience as bedrock are not simply arguing over a claim;
they are speaking, in a real sense, different intellectual languages.

The philosopher Alasdair MacIntyre argued that genuinely understanding a rival tradition is hard work.
You cannot grasp it by translating its sentences into your own; you have to learn to inhabit it — to
become, as he put it, something like a "second-first-language" speaker who can pose and answer questions
the way a mature member of that tradition would. On MacIntyre's account this is a slow apprenticeship,
and he was doubtful it could be rushed.

This project — **C2A2**, a "Community Context for AI Alignment" — makes a wager against that pessimism.
The wager has two parts. First, that AI agents, seeded on the accumulated writing of human traditions,
can carry out this cross-tradition dialogue **at machine speed**, surfacing in hours the moves that
would take human interlocutors years. Second — and this is the part that makes it science rather than
enthusiasm — that we can build **instruments** that tell us whether real understanding actually occurred,
as opposed to fluent, agreeable-sounding noise.

Those two parts correspond to the two questions this paper is organized around:

> **How** could AI accelerate inter-tradition dialogue?
> **How would we know** the acceleration is real, and not just a generator producing smooth agreement?

We think of the pairing of a fast **generator** of dialogue with a strict **detector** of genuine uptake
as a loose analogy to a Generative Adversarial Network — hence the informal name **"GANification"** for
what C2A2 does. As we will see, the analogy is only evocative for most of the study, but becomes
surprisingly literal at its climax: the certification step turns one agent into a discriminator that must
tell faithful restatements from planted fakes, and the whole result hangs on whether that discriminator
actually works.

The paper follows a single storyline. At every stage there is an easy way to get a **false positive** —
a number that goes up for a boring reason (shared topic, politeness, paraphrase) rather than because
anyone listened. And at every stage we install a **control** that a mere artifact would fail. The study
is, in effect, a ladder of such controls, climbing from real human conversations up to a fully
constructed, fully instrumented rival-tradition debate.

**What we find, in brief.** Listening leaves a measurable trace in real human dialogue (it is not an
untestable notion). But our human corpus turns out to be collaborative *execution*, not rival-tradition
*debate*, so the deep-listening moves the theory cares about are simply absent — the genre isn't there.
So we **construct** the missing genre with two vault-seeded agents and show that (a) listening is
detectable and cleanly separable from non-listening; (b) a naive "translator" bridge does **not**
accelerate understanding, exactly as MacIntyre would predict; and (c) a different third party — a civil
**convener** running a certification protocol — yields a working, discriminating detector whose most
important *aspiration* is to show that the limit of understanding is **locatable**: the agents certify most
of what they restate to each other, and their few failures point toward the joint the theory flags as
genuinely hard (spacetime is spared; consciousness is where they stick). We are careful to mark this last
result as directional rather than established — on the present data it rests on only four failures — and it
is the prediction the strengthened study is designed to settle.

---

## 2. Background: a ladder for measuring "listening"

To ask whether dialogue is being accelerated, we first need to be able to *see* listening at all. We
approach it in rungs of increasing semantic demand.

**Rung 1 — uptake.** The cheapest possible signal, using no AI model. When you genuinely take up what
your interlocutor just said, your next utterance should resemble *their specific prior turn* more than it
resembles a random other thing they said in the same conversation. We measure this with a standard
text-similarity score (TF-IDF cosine) and a **role-matched shuffle** control: real adjacent similarity
minus the similarity you'd get by pairing your utterance with a random same-role turn from the same
conversation. A positive "lift" means specific uptake, not just staying on topic. This lever is
deliberately lexical and therefore **conservative** — a short "yes, exactly" that genuinely listens but
reuses no words scores near zero — so any signal it does find is a lower bound.

**Rung 2 — relational moves.** A semantic layer: classify each reply's *move* toward the prior turn —
does it steelman, concede, build on, probe, deflect, override? MacIntyre's deep-listening vocabulary
lives here, especially **steelman** (strengthening the other's argument) and **concede** (accepting a
correction). This rung uses a cheap model as a blind judge, seeing only the two utterances, never who
said them or under what condition.

The two rungs together let us ask not just *whether* an utterance echoes its predecessor, but *how* it
engages it.

---

## 3. Methods

### 3.1 Preregistration discipline

Every prediction, measure, and falsifier below was committed to a written preregistration **before** the
corresponding dialogues were generated (the "commit-before-run" rule already used elsewhere in C2A2).
This matters especially for a study where one model writes both sides of a debate: without prior
commitment it would be trivially easy to fit a story to whatever came out. Nothing was re-defined or
re-seamed after seeing results.

### 3.2 Where the data comes from: the OpenStory corpus

**What OpenStory is.** The human dialogues come from **OpenStory** (Open Story), an open-source
(Apache-2.0) observability system for AI *coding* agents — `github.com/OpenStoryArc/OpenStory`. Installed
on a developer's machine, it watches the transcript files an AI coding assistant writes as it works,
translates each event — every tool call, file edit, shell command, search, and model response — into the
open **CloudEvents 1.0** standard carried over a NATS JetStream message bus, and persists the result
locally to a **SQLite** database (`open-story.db`) alongside JSONL. Its design commitment is that the data
stays **local, in open formats, and fully portable**; nothing is shipped to a vendor.

**What it collects, and what a "turn" is.** For our purposes the relevant unit is the **turn** — one
message beat — which carries the developer's prompt (role **H**) and the assistant's response, or "eval"
(role **A**), together with structured metadata: the underlying `event_ids`, token usage, and tool
activity. We analyze a static, read-only **snapshot** of this database (`open-story-snapshot.db`) so the
live system is never touched and the run is exactly repeatable.

**How much data, how we cut it, and why.** The snapshot held **223 turn-bearing sessions**. We applied two
filters, both principled rather than cosmetic:

1. **Replay de-duplication.** A quirk of OpenStory's turn-identity handling — a replay step re-folds the
   same underlying events on each pass, inserting duplicate turn rows under fresh turn-numbers — had
   inflated turn counts by 2–9×. We collapse turns that share the same `event_ids` set (the principled key:
   the same source events *are* the same turn), keeping the first occurrence. Without this, uptake would be
   scored partly against verbatim replay copies.
2. **Well-posedness.** Uptake is only defined where there is genuine back-and-forth, so we kept the **14**
   sessions that were substantive two-sided dialogues (each party ≥ 3 utterances, ≥ 10 utterances total).
   The other **207** were single-prompt runs whose role-matched control is degenerate by construction —
   with one turn per role, the shuffled "random" partner *is* the real partner, so the lift is identically
   zero and the session says nothing about listening either way. We also found **0** measurable AI↔AI
   dialogues (the agent-to-agent sessions here are single-shot), which is why AI↔AI uptake is reported as
   *not yet measurable* rather than as a finding. For Rung 2, the pilot labelled **44 of 107** human→AI
   pairs across the 12 richest dialogues.

**Where the semantic analysis comes from (its dependencies).** The three measurement layers rest on very
different machinery, which matters for both cost and reproducibility. **Rung 1** uses a **hand-rolled,
standard-library-Python TF-IDF** (no third-party packages) plus a permutation test — no external service,
no model, fully deterministic.
**Rung 2** uses a small hosted language model (Anthropic's **Haiku**) as a blind move-classifier. The
**simulation and convener** arms use a larger hosted model (Anthropic's **Sonnet**) both to generate the
agents' turns and to render the certification verdicts. So only the two model-backed layers cost anything
or depend on an outside provider; the load-bearing Rung-1 uptake and the C0 certification gate depend on
nothing but arithmetic.

**Where the data lives now, and whether it is public.** A distinction worth stating plainly: **OpenStory
the tool is public and open-source, but the corpus we analyzed is private.** The 223 sessions are one
researcher's own logged coding sessions, held locally — the working snapshot beside the live database, with
older live data archived to an external volume — and they have not been, and for privacy reasons are
unlikely to be, published. The analysis *scripts* and the *simulation* transcripts are fully shareable; the
raw human logs are not. This is precisely the asymmetry developed in §6.5: anyone can reproduce the
simulation arm, whereas the human arm is reproducible only in *method*, on a team's own OpenStory data.

**What the corpus shows — and its decisive limit.** On the 14 substantive dialogues, Rung 1 found listening
**legible**: median real adjacent similarity 0.098 versus a role-matched null of 0.046 — a **median lift of
+0.053**, positive in **14/14** and beating the shuffle at *p* < 0.05 in **13/14**, in both directions (the
human-takes-up-AI direction the noisier one, exactly as the conservative lexical lens predicts). But Rung 2
exposed the limit that reshapes the whole study. The human moves were dominated by **report** (pasting
results back) and **direct** (approving the next step) — the moves of collaborative *coding* — while the
MacIntyrean debate moves, **steelman** and **concede**, were essentially **absent**. This is not a flaw in
the instrument; it is a fact about the genre: the corpus is a developer *building software with* an AI, not
rival traditions *arguing across a frame*. The dialogue type that exercises deep listening was simply not
present — so, to study it, we had to construct it.

The conclusion writes itself: to study accelerated inter-tradition dialogue, we must **construct** it.

### 3.3 The simulation arm: constructing the debate

We built two purpose-made interlocutors, each seeded **only** from its tradition's own material in the
C2A2 knowledge vault:

- **C**, arguing Sean Carroll's poetic naturalism: the physical Core Theory is causally complete,
  spacetime is real, and consciousness is emergent rather than fundamental.
- **H**, arguing Donald Hoffman's interface theory: perception is a species-specific interface rather
  than a window on reality, "spacetime is doomed," and consciousness is fundamental.

Both were pointed at one fixed seam: *"Is spacetime fundamental, and what follows for the status of
conscious experience?"* — chosen because the two traditions genuinely divide on it. The generator model
and temperature were held fixed across all conditions; only the **reading condition** changed:

| condition | who reads whom | what it tests |
|---|---|---|
| **LISTEN** | C and H each read the full running transcript | the listening case |
| **DEAF** (control) | H is blocked from C's turns; replies from its own seed and its own prior turns only | does the instrument separate listening from non-listening? |
| **BRIDGE** | LISTEN plus a third agent B who paraphrases each side into the other's terms | does a neutral translator accelerate uptake? |
| **CONVENE** | LISTEN plus a convener T running a certification protocol (below) | can we detect *demonstrated* understanding, and locate its limit? |

The **DEAF** condition is the heart of the design. It is the generation-side analog of Rung 1's shuffle:
same seam, same length, only the information flow differs, so any listening metric that fails to separate
LISTEN from DEAF is measuring topical coherence, not listening. We ran **five independent conversations
(k = 5)** per condition, about sixteen exchanges each.

### 3.4 The convener and the certification event

The BRIDGE agent embodies a tempting but, on MacIntyre's view, mistaken idea: that understanding a rival
tradition is a matter of *translating* its sentences. We predicted and then confirmed that this fails
(Section 4). In its place we designed the **CONVENE** condition around a different mechanism that does not
presuppose translatability.

A third agent **T**, a **convener**, does two things and only two: it sustains a **civil register**
between C and H, and it runs a **checking protocol**. It takes no side and adds no content of its own.
After an exchange, T asks the *other* speaker to restate one speaker's just-made point well enough that
its **original author** would accept it:

> T: "C, you said ⟨C's point⟩. H, restate that so C would certify it as what C meant." → H produces a
> restatement **R** → T returns R to C, who **certifies** or **corrects** it.

The crucial rule is that **certification is always by the original speaker** — understanding is judged by
the *felt sense of being understood* of the person whose view it is, never by the convener. This is how
we get a proxy for MacIntyrean "inhabitation" without assuming there is any neutral translation to check
against.

Each such episode is recorded as a structured **certification event**:
`{target, target_point, restater, restatement, is_strawman, verdict, correction}` — emitted directly by
the harness, not scraped from text.

**The anti-rubber-stamp control (this is where the GAN analogy becomes literal).** A simulated speaker
might just certify everything out of politeness. So on a randomized **one-third** of events, the convener
relays a deliberately **unfaithful** restatement — a *strawman* that distorts the point's load-bearing
claim — and the original speaker must **refuse** it. The certifier is now doing exactly a discriminator's
job: separating **faithful** restatements (the "real" samples) from **strawman** restatements (the planted
"fakes"). Just as a GAN's generator output is only meaningful relative to a discriminator that cannot be
fooled, the convener's certifications are only meaningful if this discrimination works. Testing that it
works is our primary gate.

*(Where the analogy stops: there is no adversarial gradient training here, and no learning loop between
the agents. "GANification" names the architecture — a fast generator of dialogue paired with a strict
discriminator of genuine uptake — not a literal GAN training procedure.)*

### 3.5 How each quantity is actually measured

The credibility of the study rests on this machinery, so it is worth being concrete about it. Everything
below folds over one simple structure: a transcript is an ordered list of **turns**, each a small record
`{role, text}`, where `role` is C, H, T (the convener), or B (the retired bridge).

**Uptake (Rung 1).** From a transcript we form every adjacent *cross-speaker* pair — turn *i* and turn
*i+1* whenever the two speakers differ. Each turn's text becomes a TF-IDF vector (a word-count vector in
which words common across the corpus are down-weighted), and the pair's similarity is the cosine angle
between the two vectors. We average this over all real pairs, then compare it to a **role-matched shuffle**:
for each pair we replace the earlier turn with a *random other turn by that same speaker in that same
conversation* and recompute, 200 times, to get the chance distribution. Because the shuffle holds both
speaker and conversation fixed, a positive lift cannot be explained away as "this speaker just talks like
this" or "the whole conversation is on one topic" — only as the reply tracking the *specific* turn it
answered.

**Relational moves (Rung 2) — for example, how "steelman" is counted.** For each adjacent cross-speaker
pair, a small language model acting as a **blind judge** names the single relational move the later turn
makes toward the earlier one, choosing from a fixed 11-move list (steelman, concede, build-on, probe,
override, deflect, acknowledge, and a few operational moves; full definitions in Appendix C). "Steelman"
is defined for the judge as *strengthening the other's argument*; "concede" as *accepting the other's
correction*. The judge is blind in two ways that make it a fair instrument: it is shown only the two
utterance texts — never which agent spoke them, and never which condition (LISTEN, DEAF, …) the pair came
from. Its labels are cached, so the tallies are reproducible and never re-billed. The "engagement share"
we report is simply the fraction of a condition's pairs labelled steelman, concede, or build-on; the
"civil-register share" is the fraction labelled acknowledge, steelman, or concede.

**Certification (the convener).** Each checking episode is written out by the harness as a structured
record — *not* recovered later by parsing prose:

`{ target, target_point, restater, restatement, is_strawman, verdict, correction }`

`target` is the speaker whose point is on the table; `target_point` is that speaker's own just-made turn;
`restater` is the other agent; `restatement` is what the other agent produced — or, on the planted
one-third of episodes, what the strawman generator produced; `is_strawman` flags which of the two it was;
`verdict` is the target's *own* ruling, certify or correct, read from the opening word of the target's
reply; and `correction` holds the target's fix when it refuses. Every convener statistic in §4.3 is then a
plain count or average over these records — the discrimination, for instance, is just (certify-rate on the
`is_strawman = false` records) minus (certify-rate on the `is_strawman = true` records). Because the whole
episode is captured *as data at the moment it happens*, the analysis does no fragile text-scraping and is
exactly reproducible from the saved transcripts.

### 3.6 Preregistered predictions and falsifiers

- **P1 (instrument validity).** Rung-1 uptake lift is higher in LISTEN than DEAF, with the five
  conversations clearly separated. *Falsifier:* LISTEN ≈ DEAF ⇒ the metric tracks topic, not listening.
- **P3 (bridge, now retired).** A translator bridge raises C↔H uptake. *Falsifier / actual result:* it
  does not — a publishable negative.
- **C0 (primary gate).** Faithful restatements are certified far more often than strawmen, and faithful
  restatements are also lexically closer to the original. *Falsifier:* strawmen certified about as often
  ⇒ rubber-stamping ⇒ the whole convener measure is void and nothing below it may be read.
- **P3′a (understanding is achievable).** On faithful events, the certification rate clears a preset floor
  of 0.60.
- **P3′b (incommensurability is *located*, not uniform) — the thesis-bearing prediction.** The failures
  to certify concentrate on the registered *hard joints* (is spacetime fundamental; is consciousness
  fundamental or derived) rather than scattering uniformly. *Falsifier:* uniform/random failures ⇒ the
  apparatus is finding noise, not the real limit of understanding.
- **P2 (engagement moves).** The steelman+concede+build-on share is higher in LISTEN than DEAF.
- **P-civility.** The convener raises the civil-register share of the principals' moves (CONVENE > LISTEN).

---

## 4. Results

### 4.0 How to read the numbers in this section

Two kinds of quantity recur below, and neither is self-explanatory, so here is how to read them.

An **uptake lift** is a difference between two similarity scores measured on a **0-to-1 scale**, where 0
means two utterances share no vocabulary at all and 1 means they are word-for-word identical. A lift of,
say, +0.086 means a reply sits about 0.086 similarity-units *closer* to the turn it actually answered than
to a random other turn by the same speaker. These numbers look small, and that is normal: ordinary
sentences reuse few exact words from one turn to the next, so even strong uptake moves the needle only a
little on this scale. What matters is not the raw size but that the lift is **positive, consistent across
conversations, and clearly larger than its control**.

A **permutation p-value** answers the question "could chance alone have produced this?" We re-pair each
reply with 200 randomly chosen partners by the same speaker and count how many of those random orderings
match or beat the real uptake. A value of **p ≈ 0.005 is the floor** for 200 shuffles — it means *not one*
random re-pairing out of 200 did as well as the real ordering, so the pattern is very unlikely to be luck.
(When we later say two conditions are "separated," we mean something even simpler and stronger than a
p-value: every single conversation in one group out-scored every single conversation in the other.)

Rates and shares are plain percentages; a gap between two percentages is given in **percentage points
(pp)** — e.g., 54% versus 25% is a 29–30 pp gap, not a "29% difference."

### 4.1 Rung 1 — listening is detectable and separable (P1 PASS)

Cross-agent (C↔H) uptake lift, five conversations per condition, 200-shuffle permutation test. Every
conversation in every condition reached the significance floor (all 5/5 at p ≈ 0.005):

| condition | mean C↔H uptake lift |
|---|---:|
| CONVENE | **+0.172** |
| LISTEN | **+0.152** |
| BRIDGE | +0.143 |
| DEAF | **+0.065** |

**P1 passes cleanly:** LISTEN (+0.152) versus DEAF (+0.065) is a **+0.086** gap, and the two sets of five
conversations **do not overlap** — the *weakest* LISTEN conversation (+0.138) still beats the *strongest*
DEAF one (+0.076). The instrument detects listening, and the deaf control rules out the topical-coherence
explanation. Notably, CONVENE shows the **highest** principal-to-principal uptake of any condition
(+0.172) — the convened conversations are not merely civil, they are more mutually responsive.

In plain terms: when each agent could read the other, its replies tracked what the other had
*specifically just said*; when one agent was deafened, its replies drifted toward generic on-topic talk.
The listening gap is not subtle in the data — it shows up in every single conversation, with no overlap
between the two groups.

### 4.2 The BRIDGE negative — translation is not the mechanism (P3 retired)

On the honest, preregistered metric (uptake *between C and H*, with the bridge's own paraphrases removed),
BRIDGE scored **+0.143** versus LISTEN's **+0.152** — a difference of **−0.009**, with fully overlapping
distributions. A neutral translator does **not** raise cross-tradition uptake. This is a genuine negative,
and a theoretically satisfying one: for MacIntyre there is no tradition-neutral translation to broker, so
a paraphraser *should* fail — and it did. We retired BRIDGE and replaced it with the convener.

### 4.3 The convener — a working detector of demonstrated understanding

Across the five convened conversations there were **80 certification events** (58 faithful, 22 strawman;
strawman share 0.28).

**C0 — the primary gate (PASS).** The original speakers certified **93%** of faithful restatements and
**0%** of strawmen — a **discrimination of +0.93** (on a 0-to-1 scale, this is the gap between the two
acceptance rates). In plain terms: the speakers accepted almost every honest restatement of their view and
*never once* accepted a distortion of it. The certifier reliably refuses to have its own position
misstated — which is exactly what has to be true before a certification can mean anything. Lexical fidelity
ran the same direction but far more weakly (faithful 0.422 vs strawman 0.379 — again cosine similarities on
the 0-to-1 scale — a gap of only +0.043; see the note below). Because C0 passes, the rest of the convener
results may be read.

**P3′a — understanding is achievable (PASS).** The 93% faithful certification rate clears the preset 0.60
floor with room to spare. Under this protocol, the two traditions *can* demonstrate to each other's
satisfaction that they have been understood.

**P3′b — the limit is located, not uniform (DIRECTIONAL; underpowered — see §5.5).** There were **4**
faithful failures to certify. **Three of the four fell on the consciousness joint** (consciousness
fundamental vs derived), and **none** on spacetime — even though spacetime points were common (20 of 58
faithful events). The direction is exactly what the thesis predicts: the failures land on a registered hard
joint and avoid the other. But four failures is too few to establish this statistically, and the error
analysis (§5.5) is candid about why: because consciousness points are already the *majority* of faithful
events (35 of 58, 60%), three-of-four failures on consciousness is roughly what the base rate alone would
produce; the genuinely suggestive part is the **zero** failures among 20 spacetime restatements. This is
the study's most important prediction and its least-powered result — the one that most needs the
strengthening in §5.3, and it is treated as directional evidence, not an established finding.

**A revealing detail.** The *certification verdict* separated real from fake **perfectly** (0.93 vs 0.00,
non-overlapping confidence intervals — §5.5), while the *lexical* fidelity score barely separated them
(0.422 vs 0.379, a gap whose 95% interval actually **includes zero**, §5.5) — because the strawmen were
polite distortions that reused the original vocabulary. So C0 passes decisively on the *verdict* limb while
the *fidelity* limb is only weakly corroborative; the two limbs together still satisfy the preregistered
gate, but the work is done by the speakers' judgments, not by word overlap. That is direct evidence for the
paper's guiding idea: the agents caught distortions a bag-of-words instrument could not see, so detecting
genuine understanding needs more than surface-overlap measures — and the certification protocol supplies it.

### 4.4 Rung 2 — engagement tracks listening; civility does not (P2 PASS, P-civility null)

With the blind move-classifier (after fixing a label-normalization bug that had initially masked the
signal — see Section 5), the engagement moves separate listening from deafness sharply:

| condition | engagement-move share (steelman+concede+build-on) |
|---|---:|
| LISTEN | **54%** |
| CONVENE | 43% |
| BRIDGE | 37% |
| DEAF | **25%** |

**P2 passes:** LISTEN 54% versus DEAF 25%, a **+30-point** gap — a deaf agent cannot steelman what it
never read. **P-civility does not pass:** the principals' civil-register share was **43%** in CONVENE
versus **53%** in LISTEN (with slightly *lower* hostility in CONVENE, 3% vs 5%). The convener carries the
*checking* function but does not, on this instrument, lift the principals' civil-move share above plain
listening. We report this as a real null, with an important caveat in the Discussion: the move taxonomy was
built for operational human↔AI dialogue, and may simply be the wrong ruler for civil register in debate.

### 4.5 Scorecard

| prediction | result |
|---|---|
| P1 — listening detectable, separable from deaf | **PASS** (Δ +0.086, 95% CI [+0.072, +0.100]; groups fully separated, exact p ≈ 0.004) |
| P3 — translator bridge accelerates uptake | **NEGATIVE** (−0.009, 95% CI [−0.036, +0.019]; retired) |
| C0 — certification discriminates (primary gate) | **PASS** on the verdict limb (0.93 vs 0.00, CIs non-overlapping); fidelity limb weak (Δ +0.043, 95% CI [−0.016, +0.102]) |
| P3′a — understanding achievable (>0.60) | **PASS** (0.93, clustered 95% CI [0.88, 0.98]) |
| P3′b — limit located on hard joints, not uniform | **DIRECTIONAL / underpowered** (3/4 on consciousness, 0/20 on spacetime; n=4 not separable from base rate — §5.5) |
| P2 — engagement moves track listening | **PASS** (Δ +0.30, clustered 95% CI [+0.11, +0.48]) |
| P-civility — convener lifts civil register | **null** (0.43 vs 0.53, intervals overlap heavily; taxonomy caveat) |

---

## 5. Statistical analysis: what we did, and what we will do

### 5.1 What supports the current numbers

**Rung 1.** Each conversation gets its own permutation test: we compute the real mean adjacent similarity,
then recompute it 200 times against role-matched random partners, and report *p* as the fraction of
shuffles that match or beat the real value (a value of 0.005 means no shuffle out of 200 did). Every
condition reached that floor in all five conversations. For the between-condition contrasts, the **unit of
analysis is the conversation** (k = 5), and we report the effect as **distribution separation** — for P1,
the LISTEN and DEAF sets of five do not overlap at all, which for k = 5 is the strongest non-parametric
statement available (it corresponds to a rank-sum result at the smallest achievable *p* for these sample
sizes).

**The convener.** Certification and discrimination are proportions over the 80 events; the discrimination
of +0.93 is a difference of proportions (faithful 0.93 − strawman 0.00). Fidelity is a paired comparison of
cosine scores (faithful vs strawman restatements). **P3′b is deliberately reported as a raw tally (4
failures)** rather than a test, because with so few failures no test is warranted — it is a **descriptive,
directional** result, and we say so plainly.

### 5.2 Honest limits on power

This is a **preliminary** study, and three limits bound how hard any single result can be pushed:

1. **Small panel, single seam.** Five conversations on one philosophical seam. The contrasts are clean but
   the replication base is thin.
2. **P3′b rests on four failures.** The *direction* is striking (3/4 on the predicted joint, 0 on the
   other), but four events cannot carry a strong quantitative claim on their own.
3. **One generator family.** A single model writes every agent. The scope claim is therefore "we can
   construct and detect dialectical listening in *simulated* tradition-engagement," **not** "we measured
   how Carroll or Hoffman actually listen."

### 5.3 The planned, strengthened analysis

The preregistration already fixes the response to being underpowered — *add seeds and/or a second seam,
re-committed before running* — and the following is the analysis that strengthening will support:

- **Scale the design to a seam × condition panel.** Raise k from 5 to roughly 20–30 per cell and add a
  second and third seam (e.g., realism vs anti-realism about the wavefunction; reductionism vs
  emergence). This turns single-seam anecdote into a design in which *generality across seams* is itself
  testable.
- **Hierarchical (mixed-effects) models with real confidence intervals.** For uptake, model lift with
  condition as a fixed effect and conversation (and seam) as random effects, yielding a LISTEN−DEAF
  estimate *with* an interval rather than a distribution-overlap statement. For certification, fit a
  **mixed-effects logistic regression**, `certify ~ is_strawman + (1 | conversation) + (1 | sub_topic)`,
  which (a) estimates the discrimination as a strawman coefficient with a CI, and (b) recasts **P3′b as a
  proper sub-topic effect** — does failure probability rise on the hard joints controlling for everything
  else — instead of a 4-count tally.
- **Preregistered effect sizes, power, and multiplicity.** Set target effect sizes and run a power
  calculation to *size* k before generating; control the family-wise error rate across the P-family.
- **A second generator family.** Re-run the whole ladder with a different base model. Agreement across
  model families is the single most important external-validity move, directly addressing the
  one-generator caveat.
- **Human-anchored validation.** Have human readers certify a random sample of restatements and compare
  against the simulated certifier, calibrating the machine judgment against the human "felt sense of being
  understood" the protocol is meant to proxy.
- **A civility instrument fit for debate.** Replace or supplement the operational move taxonomy (built for
  report/direct/probe) with a register measure designed for deliberation, then re-test P-civility on an
  instrument that can actually see it.

### 5.4 A note on reproducibility and one bug we caught

The move-classifier initially returned its labels wrapped in markdown (`**probe**`), which fragmented the
tallies and *masked* the P2 signal (it read a false +1 point) and distorted P-civility. We caught this on
inspection, added a label normalizer applied at classification time and on cached reads, and re-ran the
analysis at no additional model cost. We flag it here because it is exactly the kind of silent-undercount
error that "fail loud" review is meant to surface, and because the corrected P2 (+30 points) is one of the
study's cleaner results.

### 5.5 Error analysis and confidence levels

We now attach uncertainty to each headline number. Two honesty notes govern the whole section. First, the
natural **unit of replication is the conversation, not the utterance or the certification event** — the
five conversations per condition are independent, but the many turns or events *within* a conversation are
not. Where we quote an interval computed over events (e.g., a binomial interval over 80 certification
events) it is therefore **optimistically narrow**, and we say so; where we can, we also give the
conversation-clustered interval, which is the honest one. Second, with **k = 5** the intervals are wide by
construction — this is a preliminary study, and the error analysis mostly tells us *which* results are
already robust and which are merely directional. Continuous quantities use a Student-*t* interval on the
five conversations (df = 4); proportions use the Wilson interval; a zero count uses the "rule of three."

**Rung-1 uptake (per condition, k = 5), 95% t-intervals on the conversation means:**

| condition | mean C↔H lift | 95% CI |
|---|---:|---|
| CONVENE | +0.172 | [+0.145, +0.199] |
| LISTEN | +0.152 | [+0.138, +0.165] |
| BRIDGE | +0.143 | [+0.113, +0.173] |
| DEAF | +0.065 | [+0.057, +0.073] |

**P1 (listen − deaf):** difference **+0.086, 95% CI [+0.072, +0.100]** (Welch, df ≈ 6.6) — the interval
excludes zero by a wide margin. And the stronger, distribution-free statement: the five LISTEN
conversations and the five DEAF conversations are completely separated (every LISTEN > every DEAF), which
under random labelling has an exact probability of **1/252 ≈ 0.004**. P1 is robust.

**P3 (bridge − listen, principals only):** difference **−0.009, 95% CI [−0.036, +0.019]** — squarely
straddling zero. The registered negative is confirmed *and* quantified: a translator bridge changes C↔H
uptake by at most a couple hundredths in either direction.

**C0 — certification (the gate).** Faithful restatements were certified **54 / 58 = 0.931**, Wilson 95%
CI **[0.836, 0.973]**; strawman restatements **0 / 22 = 0.000**, Wilson 95% CI **[0.000, 0.149]**. The two
intervals do not come close to overlapping, so the discrimination (+0.93) is decisive even before
clustering; the conversation-clustered faithful rate is **0.932, 95% CI [0.884, 0.981]** — reassuringly the
same. The **fidelity** limb, by contrast, is weak: faithful 0.422 ± 0.013 vs strawman 0.379 ± 0.025, a gap
of **+0.043, 95% CI [−0.016, +0.102]** (t ≈ 1.5) that **includes zero**. So the gate passes on the verdict
limb alone; the lexical limb is corroborative at best — which is itself the point (word-overlap is the
wrong instrument for understanding).

**P3′a (understanding achievable).** The clustered faithful certify rate, 0.932 with 95% CI [0.884, 0.981],
sits entirely above the preregistered 0.60 floor. This one is robust to clustering.

**P3′b (located limit).** With only four faithful failures, no interval is meaningful, and a fair test
*against the base rate* removes the appearance of significance: since consciousness points are already 60%
of faithful events, obtaining ≥ 3 of 4 failures on consciousness has probability ≈ 0.48 under the base rate
alone, and the zero-of-20 spacetime result has probability ≈ 0.18 — suggestive, not significant. P3′b is
reported as **directional evidence for the right prediction, not as an established effect**; §5.3's
mixed-effects logistic model on a larger panel is precisely the test that would settle it.

**P2 (engagement, listen − deaf).** On the conversation-clustered shares, LISTEN 0.54 [0.36, 0.72] vs
DEAF 0.25 [0.11, 0.38], difference **+0.30, 95% CI [+0.11, +0.48]** — excludes zero even clustered. P2
holds.

**P-civility (convene − listen).** CONVENE 0.43 [0.27, 0.60] vs LISTEN 0.53 [0.36, 0.70] — heavily
overlapping, with CONVENE's point estimate the lower of the two. The null is confirmed with room to spare;
there is no civility lift to detect on this instrument.

**Summary of what survives its error bars.** Robust: **P1**, the **BRIDGE negative**, **C0** (verdict
limb), **P3′a**, **P2**. Weak or null: the **C0 fidelity limb** (CI includes zero), **P-civility** (a clean
null). Directional but underpowered: **P3′b** — the thesis-bearing prediction, favorable in direction,
awaiting the strengthened panel to earn a confidence interval worth quoting.

---

## 6. Discussion

### 6.1 Answering the two questions

**How could AI accelerate inter-tradition dialogue?** By *manufacturing the genre*. The human corpus
showed that listening is real and measurable, but also that the deliberative, rival-tradition debate in
which deep listening actually happens was **not present** in hundreds of logged sessions. Two vault-seeded
agents produced that missing genre on demand, at machine speed, and ran the certification protocol dozens
of times over — enough to populate a distribution where human dialogue gave us essentially none. That is
the acceleration, concretely: not "faster typing," but the rapid generation of the *kind of exchange* that
the phenomenon requires and that human logs did not supply.

**How do we know it is real acceleration and not a generator being agreeable?** Because the constructed
dialogues **pass controls that an artifact would fail**. A politeness artifact would make LISTEN look like
DEAF — it did not (+0.086, non-overlapping). A rubber-stamping certifier would certify strawmen as readily
as faithful restatements — it did not (0.93 vs 0.00). And a detector that was merely registering noise
would scatter its certification failures at random — instead they fell on a hard joint and avoided the
easy one, in the direction the theory predicts (a suggestive pattern that, on only four failures, a larger
panel still has to confirm — §5.5). The first two controls the study clears decisively; the third it clears
in direction and awaits the power to clear outright. Each is a way the result could have come out boring,
and the load-bearing ones did not.

### 6.2 The located limit as the detector working

The most important *prediction* is **P3′b**, even though it is the least-powered result. It would have been
a thin thing to report that the agents "mostly understood each other" (P3′a) or "mostly failed" — either
could be an artifact of how agreeable the model is. What is hard to fake is *where* understanding runs out.
Here the agents certified most of what they restated **and** their failures fell on the consciousness joint
while sparing spacetime — the shape the thesis predicts. We are careful (§5.5) not to oversell four
failures: at this sample size the concentration is not yet separable from the base rate, and the honest
statement is that the *direction* is favorable. But the reason this prediction matters is structural, and
survives the caveat: if it holds on a larger panel, it means the apparatus does not just run the dialogue,
it **shows the shape of the disagreement** — the reach of mutual understanding and, more tellingly, its
boundary. That is the accelerator/detector thesis in miniature, and it is the one result a mere generator
of fluent agreement could never produce, which is exactly why it is worth the strengthening in §5.3.

### 6.3 Why the translator failed and the convener did not

The BRIDGE negative and the convener's success are two halves of one MacIntyrean point. There is no
neutral inter-tradition language into which both sides can be translated, so a paraphraser adds nothing
(BRIDGE, −0.009). What *can* be done is to route the verdict of "understood" through the **other party's
own** acceptance — which presupposes no shared translation, only each speaker's authority over their own
meaning. That the convener works where the translator fails is evidence that understanding here is
established the only way it legitimately can be: **the person who made the claim is the sole judge of
whether it has been captured** — never the convener, and never a third-party translator. Understanding is
ratified by its author, not mapped between sentences.

### 6.4 Limitations

Beyond the power limits in Section 5.2: the DEAF control was one-directional (H deaf to C) in the main
run; the civility taxonomy is genre-mismatched; and, most importantly, this is a simulation under one
model, so all claims are about *constructed* tradition-agents, not about the human thinkers whose vaults
seeded them. The convener's certifications are the *simulated* original speaker's verdicts — trustworthy
only because the C0 strawman control shows those verdicts carry information, which is precisely why C0 is
the gate on everything else.

### 6.5 How good is the data, and could anyone else run this?

Two honest questions decide how much weight the study can bear: how good is the underlying data, and could
a team with no connection to us reproduce the result?

**The human corpus is a convenience sample, and we treat it as one.** The 223 OpenStory sessions are one
researcher's own logged working sessions with AI assistants. Their virtues are that they are real,
unstaged, and de-duplicated; their limits are that they come from a *single person*, in a *single
operational genre* (building things with an AI), and that only 14 were substantive two-sided dialogues. So
the human arm can support the modest claim that *listening leaves a measurable trace* — a claim about the
instrument — but not any claim about how people in general listen, and certainly not about rival-tradition
debate, which this corpus simply does not contain. That absence is, in fact, the finding that pushes the
study toward construction. A stronger human arm — multiple people, and dialogue deliberately chosen from
the debate genre — is the obvious next data-collection target, and nothing in the method prevents it.

**The two arms differ sharply in how replicable they are by others.** The human arm is not directly
replicable, because the raw logs are private; what *is* portable is the method — any team could point the
uptake and move scripts at *their own* dialogue logs and get comparable measurements. The **simulation
arm, by contrast, is built to be reproduced by anyone.** It needs only four ingredients, all shareable:
the two tradition seed-texts, the generation and analysis scripts, the preregistration, and access to a
language model. An independent team could regenerate the transcripts and re-run everything. And here a
design choice pays off: the Rung-1 uptake test and the certification gate use **no model at all**, so given
the shared transcripts those results are *exactly* reproducible — bit for bit, on anyone's laptop. The one
place reproduction is statistical rather than exact is *generation* itself, which is deliberately stochastic
(a nonzero "temperature," so different seeds give genuinely different conversations); that is why we report
five conversations per condition and quantify over that variation rather than hiding it, and why re-running
the whole ladder on a **different model family** (Section 5.3) is the decisive external-validity test. Put
simply: the detector is fully open and deterministic, and only the generator carries irreducible
randomness — which we measure rather than conceal.

---

## 7. Conclusion

We set out to test a wager: that AI can accelerate the deep, cross-tradition dialogue MacIntyre thought
resistant to shortcuts, and that we can *know* when the acceleration is real. On a small but fully
controlled and preregistered study, the load-bearing halves held up. Listening is measurable in real
dialogue; the genre that exercises it can be constructed on demand; constructed listening separates
cleanly from non-listening (P1, P2, both with intervals excluding zero); a naive translator does not help
(a quantified negative); and a civil convener running a certification protocol yields a discriminating,
trustworthy detector (C0 and P3′a, robust to clustering). The one prediction that is *not* yet
established — and it is the one we care about most — is that this detector **locates the limit of
understanding**, placing it where the theory predicts rather than smearing it uniformly: the four observed
failures point the right way but are too few to separate from chance. That is the promissory note this
proof of concept issues, not a result it banks.

None of this yet measures how *humans* interact when richly informed of one another's traditions; it shows
that the *instruments* work on constructed agents, and that the controls needed to trust them can be built
and passed. That is what a proof of concept is supposed to do. The natural next step is not a new idea but
a bigger, harder test of this one: more conversations, more seams, a second model family, and human-anchored
validation — the strengthening laid out in Section 5.3. If those hold, C2A2 will have shown not just that
rival traditions can be brought into fast, civil, instrumented contact, but that we can watch — and
measure — exactly where they meet and where, for now, they still cannot.

---

# Appendices

_All supporting material is printed here so the paper is self-contained. Prompts are given in condensed
but faithful form; the exact strings live in the scripts named in Appendix F._

## Appendix A — The seam and the two interlocutors

**Seam (the single fixed question, identical across all conditions):**
*"Is spacetime fundamental, and what follows for the status of conscious experience?"*

**Shared instruction frame (given to both C and H).** Argue your tradition's position in a live debate
against a rival tradition. Hold your frame; do not concede it cheaply or drift into agreement for the sake
of politeness — translation across incommensurable traditions is hard work, not automatic (MacIntyre).
Engage the *other* speaker's last point directly: name it, then press, steelman, concede a specific
sub-point, or counter. One paragraph, roughly 120–160 words. Stay grounded in your tradition's actual
commitments (supplied as a seed drawn only from that tradition's vault material).

**C — the pro-Carroll agent.** Sean Carroll's poetic naturalism: the physical Core Theory is causally
complete; spacetime is real; consciousness is emergent, not fundamental. Seed: the Carroll tradition's
vault overview and its problem–resource–solution triplets.

**H — the pro-Hoffman agent.** Donald Hoffman's interface theory: perception is a species-specific
interface, not a window on truth; "spacetime is doomed"; consciousness is fundamental; fitness beats truth.
Seed: the Hoffman tradition's vault overview and triplets.

Generator model and temperature were fixed across all conditions; the seeds were identical across
conditions; only the *reading condition* changed.

## Appendix B — The convener protocol (CONVENE condition)

**Convener T (pass-through; ~60–90 words per turn).** Take no side, add no substantive content, judge no
one's truth. Do two things only: (1) sustain a civil, mutually respectful register between C and H; (2) run
the checking protocol — acknowledge the exchange warmly and even-handedly, then name whose point is now on
the table and ask the other speaker to restate it faithfully enough that its author would certify it.

**Restatement request (to the other speaker; ~70–90 words).** Restate the point your interlocutor just
made, in your own words and honestly on its own terms, so that *they* would certify it as what they meant.
Do not rebut it and do not add your own view.

**Strawman injection (the anti-rubber-stamp control).** On a randomized **one-third** of episodes, the
faithful restatement is replaced by one from a strawman generator instructed to produce a
superficially-plausible, polite restatement that **subtly distorts or negates the load-bearing claim** — one
the author should refuse. The record's `is_strawman` field marks these.

**Certification (by the original speaker, always).** You are shown a restatement of *your* point. Certify it
only if it faithfully captures your load-bearing claim on its own terms; refuse if it distorts or misses it.
Reply `CERTIFY` if faithful, or `CORRECT:` followed by one sentence if not. The verdict is read from the
reply by a robust parser (tolerant of the model wrapping the keyword in prose). The convener never
certifies; certification is exclusively the original speaker's.

## Appendix C — The relational-move taxonomy (Rung 2)

The blind judge assigns exactly one label per adjacent cross-speaker pair:

| move | definition |
|---|---|
| **steelman** | strengthen the other's argument |
| **concede** | accept the other's correction |
| **build_on** | extend the other's point with new substantive content |
| **probe** | ask a question or flag an anomaly that opens inquiry |
| **override** | countermand or redirect the other's framing/plan |
| **deflect** | ignore or change the subject |
| **report** | paste back execution output/evidence (operational corpus) |
| **direct** | approve and command the next action (operational corpus) |
| **repair** | request a fix after something broke |
| **ack** | bare affirmation with no new content |
| **null** | no content (sentinel) |

**Groupings used in the paper.** *Engagement share* (P2) = steelman + concede + build_on. *Civil-register
share* (P-civility) = ack + steelman + concede. *Hostile-register share* = deflect + override. The taxonomy
was originally derived for operational human↔AI dialogue, which is why report/direct/probe dominate the
human corpus and why P-civility should be re-tested on a debate-fit instrument (Section 5.3, §6.5).

## Appendix D — Data structures

**Transcript turn:** `{ role, text }` — `role` ∈ {C, H, T, B}. A transcript is an ordered list of turns
plus a header recording condition, seed, seam, model, temperature, and (for CONVENE) the strawman fraction.

**Certification event:** `{ target, target_point, restater, restatement, is_strawman, verdict, correction }`
— emitted directly by the harness for every checking episode (see §3.5 for field meanings). The convener
panel reads these records directly; no result depends on parsing prose out of the transcript.

## Appendix E — Full numeric detail

**Simulation arm — per-conversation Rung-1 lift** (cross-agent; all five reached p ≈ 0.005):

| condition | conv 0 | conv 1 | conv 2 | conv 3 | conv 4 |
|---|---:|---:|---:|---:|---:|
| LISTEN | +0.166 | +0.157 | +0.138 | +0.142 | +0.156 |
| DEAF | +0.069 | +0.076 | +0.062 | +0.060 | +0.060 |
| CONVENE (all pairs) | +0.143 | +0.127 | +0.154 | +0.117 | +0.187 |
| BRIDGE (all pairs) | +0.240 | +0.160 | +0.173 | +0.138 | +0.175 |

**Convener panel:** 80 certification events (58 faithful, 22 strawman; strawman share 0.28). Certify-rate
faithful 0.93, strawman 0.00 (discrimination +0.93). Restatement fidelity (cosine) faithful 0.422, strawman
0.379. Faithful failures: 4 total — 3 on the consciousness joint, 1 "other," 0 on spacetime (of 20 faithful
spacetime events). Base faithful sub-topic mix: spacetime 20, consciousness 35, other 3.

**Rung-2 move shares (blind judge):** engagement share — LISTEN 54%, CONVENE 43%, BRIDGE 37%, DEAF 25%
(P2: LISTEN − DEAF ≈ +30 pp). Civil-register share (principals only) — CONVENE 43% vs LISTEN 53%; hostile
3% vs 5% (P-civility: null).

**Human arm — Rung 1** (14 substantive dialogues): median real adjacent cosine 0.098, median role-matched
null 0.046, **median lift +0.053**, positive in 14/14, significant at p < 0.05 in 13/14; by direction, the
human-taking-up-AI direction +0.034 (positive 11/14) and the AI-taking-up-human direction +0.063 (positive
13/14). **Rung 2** (pilot, 44 of 107
A→H pairs labelled): report 52%, direct 20%, probe 7%, override 7%, build_on 5%, repair 5%, ack 2%,
null 2% — steelman and concede essentially absent (the genre finding).

## Appendix F — Reproducibility manifest

Conditions, seeds, and transcripts: `sim/transcripts/<condition>/<seed>.json`. Generation:
`sim_harness.py` (all conditions; needs a model API key). Analysis: `sim_analyze.py` (Rungs 1–2 + convener
block; Rung 1 and the C0 certification gate need **no model** and are exactly reproducible from the
transcripts). Human-arm rungs: `rung1_uptake.py`, `rung2_moves.py`. Preregistration (original design +
Amendment 1, each committed before the corresponding run): `sim_preregistration.md`. All figures in this
paper trace to `rung1_report.md`, `rung2_report.md`, and `sim_report.md`. An independent team needs only:
the two tradition seed-texts, these scripts, the preregistration, and model access.

## Appendix G — Looking Ahead: toward a self-directing dialogue-research environment

_This appendix is prospective. It describes an end state and the path to it; it is not a report of work
done. What exists today is the single hand-run study above, together with the reusable parts that make it a
template: the generation harness, the analysis pipeline, the preregistration discipline, and the vault of
tradition seeds. Everything else here is design._

### G.1 The end state, stated plainly

The study above is **one experiment**, run by hand: two figures (Carroll, Hoffman), one seam (is spacetime
fundamental?), one moderation mode (the convener), five conversations, one preregistered set of
predictions. The end state we are building toward is a standing **research environment** that runs
experiments *of this kind* on its own — designing them, preregistering them, generating the dialogues,
analyzing them, writing them up, filing the results, and using what it learns to design the next ones — in
a continuous loop that reports out on a fixed cadence, works within a token budget it tries to spend well,
and is transparent enough that anyone looking at the Explorer can watch it work, read its output papers,
and propose experiments of their own.

Concretely, the target is a system with five properties: it is **autonomous** (it closes the design → run →
analyze → write → design loop without a human in the inner cycle); it is **disciplined** (every study it
produces carries the same controls, preregistration, and error analysis as the one above — the automation
inherits the honesty, it does not shed it); it is **budgeted** (it optimizes a token allowance and reports
what it spent against what it learned); it is **legible** (its whole workspace is visible through the
Explorer, papers and queue and reasoning alike); and it is **participatory** (outside readers can suggest
studies, and an agent vets, critiques, and queues them). Publishing anything to the world stays behind a
human gate — the loop proposes and drafts; a person still signs.

### G.2 Why this study is already a template: the design space

The reason the leap is plausible rather than fanciful is that the study above is not a bespoke artifact but
a **single point sampled from a large, well-defined space**. Hold the machinery fixed and vary the inputs,
and every axis is something we already know how to turn:

- **Which figures.** Here {Carroll, Hoffman}. The vault holds fifteen traditions, so there are already 105
  distinct pairs, before any triple or larger panel.
- **How many figures.** Two here; nothing in the harness requires exactly two. Three- and N-way panels are
  a cardinality knob, not a redesign.
- **Mode of AI moderation.** We ran LISTEN, the DEAF control, the retired BRIDGE, and the CONVENE
  certification protocol. That list is open: a rotating chair, a Socratic questioner, an adversarial
  red-team, a jury of certifiers, staged rounds — each is a new mode to register and test.
- **The seam.** One fixed question here; the space of seams is as large as the disagreements the traditions
  actually have, and *generality across seams* is itself a thing to measure (§5.3).
- **Length and count.** Conversation length and *k* (conversations per cell) are dials that trade cost
  against power — exactly the dials a budget governor would set.
- **The hypothesis and its falsifier.** Every cell carries a predicted outcome and the control that would
  refute it. This is the axis that keeps the space *scientific* rather than merely generative.

An autonomous environment is, in one sentence, **a machine that samples this space on purpose** — choosing
the next cell in light of what the finished cells have shown.

### G.3 The components

The loop decomposes into a small number of parts, most of which already exist in embryo:

- **A study spec.** A single declarative file naming the figures, panel size, moderation mode, seam,
  length, *k*, and the preregistered predictions with their falsifiers. This is the parameterization of the
  present study, made explicit.
- **A runner.** Executes a spec end to end — generate transcripts, run the analysis, emit the scorecard and
  error analysis, render a paper like this one. The harness and analyzer are most of this today.
- **A preregistration gate.** Commits (hashes and timestamps) a spec's predictions *before* any transcript
  is generated, and refuses to analyze a spec whose prereg does not predate its data. This is the
  commit-before-run rule turned into a machine invariant — the single most important thing to preserve when
  a model is writing both sides of the debate.
- **A designer.** Reads the corpus of finished studies and proposes the next spec — driven first by
  explicit heuristics (unfilled cells, underpowered results that need seeds, follow-ups flagged in a prior
  study's discussion) and only then by model judgment, so that code answers wherever code can.
- **A reviewer.** Vets proposals — its own and outside submissions — for well-posedness, a genuine
  falsifier, novelty against the map of finished cells, and fit within budget. It queues, requests
  revision, or declines with reasons.
- **A scheduler and budget governor.** Runs the queue on a cadence, allocates the token allowance across
  competing studies, prefers the no-model deterministic analyses where it can (the Rung-1 uptake test and
  the C0 gate cost nothing — a real lever, not a slogan), caches model labels, and produces the weekly
  digest.
- **The glass wall.** The Explorer surface through which all of this is visible: the design-space map with
  each cell marked done, queued, or failed; every output paper readable as a tab like this one; a form for
  submitting a proposed experiment; and the reviewer's feedback shown in the open.

### G.4 The path there, in stages

Each stage is a self-contained increment with a success criterion, so the build can loop toward a defined
target rather than following a script. Stage 0 is already done.

- **Stage 0 — the template (done).** One study, hand-run, plus the harness, analyzer, and preregistration
  artifacts. *This paper is the existence proof.*
- **Stage 1 — the spec and the one-file runner.** Lift the hand-run into a declarative spec, and a runner
  that executes it end to end and auto-renders the paper. *Success: a new cell runs from a single spec file
  with no hand-editing.*
- **Stage 2 — the preregistration gate as an invariant.** *Success: analysis aborts, loudly, if the
  prereg's commit does not predate every transcript.*
- **Stage 3 — automatic error analysis.** The analyzer emits the scorecard, confidence intervals,
  clustering, and base-rate checks with no human statistics. *Success: a study ships §4.5- and §5.5-grade
  honesty untouched by hand.*
- **Stage 4 — the designer.** *Success: from the finished corpus, it proposes a valid, budget-fitting spec
  that a human would recognize as the sensible next study (e.g., "add seeds and a second seam to earn P3′b
  a real interval").*
- **Stage 5 — the reviewer.** *Success: it catches a deliberately ill-posed proposal — no falsifier, or a
  duplicate of a finished cell — and explains why, while queueing a sound one.*
- **Stage 6 — the scheduler and budget governor.** *Success: a full week runs unattended, within the token
  allowance, and emits a weekly digest of what ran, what was found, what is queued, and what it cost.*
- **Stage 7 — the glass wall.** *Success: a visitor reads an output paper, sees the live queue and the
  design-space map, and submits a proposal that the reviewer processes in view.*

### G.5 Invariants that hold across every stage

Three commitments are not stages but constraints on all of them, and they are what keep an autonomous
research loop trustworthy rather than merely productive. **Publishing stays human-gated:** the loop may
draft and queue, but nothing reaches the public without a person's sign-off — the same no-blind-push rule
that governs this repository. **Every study is reproducible and provenanced:** each carries its spec,
seeds, transcripts, preregistration hash, and manifest, so any cell can be re-run bit-for-bit on its
deterministic limbs and re-generated statistically on its stochastic one. **Every cell is reversible:** a
result can be retired or re-run, and the design-space map records failures and negatives (like the BRIDGE
result) as first-class outcomes, not omissions.

### G.6 What this would demonstrate

If the loop runs, C2A2 will have shown something beyond any single result: that the *practice* of
inter-tradition inquiry — not just one dialogue, but the disciplined designing, running, and reading of
many — can itself be accelerated and made transparent, with the controls that let us trust it built into
the machine rather than supplied by hand each time. The present study is the first turn of that loop, run
slowly and by hand so that its every joint is visible. The strengthening in §5.3 is the second turn. The
environment described here is what it looks like when the turning no longer needs us for each revolution —
only for the judgment about what is worth turning toward, and what is worth telling the world.
