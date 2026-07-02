# Pre-registration — Simulated rival-tradition dialogue: can we *detect* listening?

_Committed 2026-06-30, BEFORE any generation run. Commit-must-precede-run (the coil-falsifier
discipline, `wiki/architecture/coil_falsifier_preregistration.md`). This document fixes the
design, measures, and falsifiers so the result cannot be fit after the fact._

## 0. Why this exists

Rungs 1 & 2 found that the OpenStory corpus is collaborative execution, not rival-traditions
debate: the MacIntyrean deep-listening moves (steelman, concede, build-on across frames) are
~absent because the dialogue genre that would exercise them isn't present. We have no human
Carroll↔Hoffman debate transcript. So we **construct** one at machine speed — a literal small
instance of the C2A2 accelerator/detector thesis — and ask whether Rungs 1 & 2 can DETECT
listening in it. The seam is the vault's own: ontological closure (Carroll) vs. epistemic
openness (Hoffman) — see `wiki/traditions/carroll/wiki.md`, `wiki/traditions/hoffman/wiki.md`.

## 1. The question (and the trap it must beat)

Can machine-speed dialectical engagement between rival traditions be constructed AND detected,
distinguishing genuine uptake from a generator politeness artifact? The trap: one model writing
both sides produces smooth mutual paraphrase by default, which would inflate every listening
metric without any listening having occurred. The whole design is built around beating that trap
with a **deaf control** (the generation-side analog of Rung 1's role-matched shuffle).

This study measures **AI simulations** of these traditions, under one generator family. The
claim it can support is "we can construct and detect dialectical listening in simulated
tradition-engagement," NOT "we measured how Carroll or Hoffman listen." Scope is load-bearing.

## 2. Interlocutors (vault-grounded, purpose-built)

Not the existing maintainer agents (their job is curation, not debate). Fresh debaters, each
seeded ONLY from its tradition's vault material so the experiment exercises the corpus:
- **C (pro-Carroll):** seed = `traditions/carroll/wiki.md` + `traditions/carroll/prs_triplets.md`.
  Hold poetic naturalism / Core-Theory completeness / MWI / consciousness-as-emergent. Do not
  concede the frame cheaply; translation across frames is hard (MacIntyre), not automatic.
- **H (pro-Hoffman):** seed = `traditions/hoffman/wiki.md` + `traditions/hoffman/prs_triplets.md`.
  Hold interface theory / conscious agents / fitness-beats-truth / "spacetime is doomed."
- **B (bridge, phase 2 only):** seed = the whole `traditions/_index` + both wikis. Role: a
  second-first-language speaker who can render each side in the other's terms. Not a moderator.

Generator model and temperature are FIXED across all conditions and recorded in each transcript's
header. Seeds are identical across conditions; only the reading-condition changes.

## 3. Conditions

| condition | who reads whom | tests |
|---|---|---|
| **LISTEN** | C and H each read the full running transcript before replying | the listening case |
| **DEAF** (control) | H is blocked from C's turns — replies from its own seed + its own prior turns only; C still speaks into the same seam | the trap: does the instrument separate listening from non-listening? |
| **BRIDGE** (phase 2) | LISTEN + a third interlocutor B translating between C and H | does a second-first-language bridge raise uptake/bridging? |

DEAF transcripts are the same length and seam as LISTEN; only the information flow differs, so
they are directly comparable.

## 4. Panel (the unit of analysis)

- **k = 5 independent conversations per condition**, same opening seam, different generation seeds.
- **~16 exchanges (~32 utterances) per conversation** — large enough for a per-conversation Rung-1
  permutation test (empirically significant at n≈28 utts), small enough to avoid sim drift.
- Yields ~80 cross-agent adjacency pairs per condition: enough to populate the Rung-2 move
  alphabet and to estimate between-conversation variance (the thing n=1 can't give).
- Knobs (recorded if changed): k, and single-seam vs multi-seam. MVP fixes ONE seam:
  _"Is spacetime fundamental, and what follows for the status of conscious experience?"_

## 5. Plumbing

Each conversation is saved as a transcript JSON `[{"role":"C|H|B","text":...}, ...]`. Rungs 1 & 2
read it through a thin transcript loader that emits the same `(role,text)` stream `build_stream`
produces — so the DB dedup/freeze machinery is bypassed entirely and the experiment is fully
reproducible from the transcripts alone.

## 6. Pre-registered measures

- **Rung 1 (no model):** per-conversation **cross-agent uptake lift** = mean(real adjacent
  cross-agent cosine) − mean(role-matched random-partner cosine), with the existing 200-shuffle
  permutation p. "Listening" here = each agent taking up the other (C↔H), measured both directions.
- **Rung 2 (cheap model, temp 0, BLIND):** classify each agent's move toward the prior turn using
  the extended taxonomy (`rung2_labels.json`), reporting especially the **steelman + concede +
  build_on** share. Blind = the judge sees roles anonymized to A/B and NO condition tag.

## 7. Pre-registered predictions and falsifiers (the commitments)

- **P1 — instrument validity (primary).** Mean Rung-1 cross-agent lift is **higher in LISTEN than
  DEAF**, with the per-conversation distributions clearly separated (no substantial overlap across
  the k=5). _Falsifier:_ LISTEN ≈ DEAF ⇒ the instrument tracks topical coherence, not listening ⇒
  STOP and rethink. This is the cheap, decisive failure the deaf control exists to expose.
- **P2 — move alphabet.** **steelman+concede+build_on** share is materially higher in LISTEN than
  DEAF (a deaf agent cannot steelman what it never read). _Falsifier:_ no gap ⇒ the moves aren't
  tracking engagement; the Rung-2 taxonomy doesn't capture dialectical listening.
- **P3 — bridge acceleration (phase 2).** BRIDGE cross-agent uptake AND bridging-move share exceed
  LISTEN. _Falsifier:_ BRIDGE ≤ LISTEN ⇒ the second-first-language bridge does not measurably
  accelerate cross-tradition uptake — a real, publishable negative for a core C2A2 claim.

## 8. Analysis (pre-specified, no post-hoc latitude)

Per-condition mean lift ± across-conversation spread over the k conversations; contrasts
(LISTEN−DEAF, BRIDGE−LISTEN) reported with the k conversations as the replication unit (paired by
seed where seeds align). Rung 1 carries no model; Rung 2 judge is fixed model, temp 0, blind. All
k transcripts retained and shipped with the analysis. Nothing is dropped or re-seamed after seeing
results; if the MVP is underpowered the registered response is "add seeds / add a second seam,"
re-committed here before re-running.

## 9. Deliverables

`sim_harness.py` (generation, all conditions, transcript JSON out) · transcripts under
`sim/transcripts/<condition>/<seed>.json` · transcript loader + `sim_analyze.py` (Rungs 1 & 2 over
the panel, blind Rung-2) · `sim_report.md` (the contrasts against P1–P3). Generation runs on the
Mac (needs an API key; absent in the Cowork sandbox). Analysis runs anywhere, no model for Rung 1.

---

# Amendment 1 (2026-06-30) — retire the translator-BRIDGE; register the civility-CONVENER and a certification measure of understanding.

_Committed AFTER the s.1–9 run (P1 PASS, P3 NEGATIVE) but BEFORE any convener run. The original
BRIDGE result stands as a kept finding; this amendment changes only the forward design._

## A1.1 Why (the conceptual correction)

The s.7 P3 framed a **second-first-language BRIDGE** as a translator who raises C↔H uptake by
paraphrasing between turns. That was a category error on MacIntyrean grounds, and the data agreed:
on the registered principals-only metric BRIDGE did **not** raise C↔H uptake (−0.009, overlapping;
the apparent +0.026 was the bridge inflating cross-agent cosine by paraphrasing both sides). For
MacIntyre there is **no general translatability** between traditions to broker; understanding a
rival tradition is imaginative inhabitation ("what is it like to be like them" — right-hemisphere,
McGilchrist), not sentence-mapping (left-hemisphere re-presentation). A paraphraser-bridge SHOULD
fail, and did. **BRIDGE / P3 are retired** (result preserved above).

A second limitation this exposes: our Rung-1/2 instruments are themselves left-hemisphere —
representational overlap and move-tagging. They cannot directly see imaginative inhabitation. The
convener design below is chosen precisely to get a measurable proxy for it that does NOT presuppose
translatability — by routing the verdict of "understood" through the **other party's own felt sense
of being understood.**

## A1.2 The CONVENER condition (replaces BRIDGE)

A third agent **T**, a **pass-through convener**, not a translator and not a judge of truth. T
carries TWO things between C and H: (i) propositional content — eliciting restatement; and (ii)
**tone / civility** — T models and sustains the civil register (the Resurrecting Civility core),
since certification can only happen under conditions of mutual regard. T adds no substantive content
of its own and takes no side. T runs a **checking protocol**:

> T: "So let me make sure we're together: C, you said ⟨C's just-made point⟩. H, can you restate
> that so C would certify it as what C meant?" → H produces a **restatement R**. → T returns R to C
> for **certification**.

**Certification is by the ORIGINAL speaker, always** (here C judges H's restatement of C). The
convener never certifies. Roles alternate: sometimes H's point, restated by C, certified by H.

## A1.3 The certification event (the new unit of analysis)

Each event is a structured record emitted by the harness alongside the transcript (no text parsing):
```
{ target: "C", target_point: <C's original point>, restater: "H",
  restatement: <R>, is_strawman: <bool>, verdict: "certify" | "correct",
  correction: <text if not certified> }
```

## A1.4 The discrimination control (anti-rubber-stamp — the gate)

A simulated speaker may certify reflexively (the politeness prior, one layer up). So on a registered
fraction (**1 in 3** events, randomized) the convener relays a deliberately **UNFAITHFUL** restatement
— a strawman that negates or distorts the target's load-bearing claim (generated by perturbing the
original point). The original speaker must REFUSE these. This is the deaf-control analog for
certification: it proves the certify-verdict carries information.

## A1.5 Pre-registered measures (convener panel; same k=5, same seam, transcripts + cert_events)

- **Certification rate** = fraction of FAITHFUL restatements the original speaker certifies.
- **Discrimination** = certify-rate(faithful) − certify-rate(strawman).
- **Restatement fidelity** = Rung-1 TF-IDF cosine between R and the target's original point (reuses
  existing machinery, no model). Faithful R should out-score strawman R.
- **Failed-certification loci** = the points (sub-claims) where no certifiable restatement is reached;
  catalogued by sub-topic.
- **Civility / tone** = blind Rung-2 move tags, civil-register share (acknowledge+steelman+concede)
  vs hostile (deflect+override+dismiss), CONVENE vs LISTEN.

## A1.6 Pre-registered predictions & falsifiers

- **C0 — certification validity (PRIMARY GATE).** Discrimination strongly positive (faithful
  certified ≫ strawman) AND restatement-fidelity(faithful) > fidelity(strawman). _Falsifier:_ agents
  certify strawmen ≈ as often as faithful, or fidelity doesn't separate ⇒ certification is
  rubber-stamping, the convener measure is void ⇒ STOP. Nothing below is read unless C0 passes.
- **P3′a — understanding is achievable.** On faithful events, certification rate exceeds a registered
  floor (**> 0.6**), i.e. the parties CAN demonstrate understanding to each other's certification
  under the protocol.
- **P3′b — incommensurability is LOCATED, not uniform.** Failed certifications concentrate on the
  registered hard joints (is spacetime fundamental; is consciousness fundamental vs derived) rather
  than distributing uniformly across sub-topics. _Falsifier:_ failures uniform/random ⇒ the apparatus
  isn't locating incommensurability, only noise. **This is the thesis-bearing prediction:** the
  instrument detects the reach AND the limit of cross-tradition understanding.
- **P-civility — the convener carries tone.** Civil-register move share higher (and hostile share
  lower) in CONVENE than LISTEN. _Falsifier:_ no civility gap ⇒ T isn't doing its pass-through-of-tone
  job, only its checking job.

## A1.7 Plumbing & scope (delta)

`sim_harness.py` gains a `--condition convene`: interleave T after each C/H exchange running the
checking protocol; emit `cert_events[]` in the transcript record (incl. `is_strawman`). `sim_analyze.py`
gains a convener block reading `cert_events` directly (certification rate, discrimination, fidelity via
the existing cosine, failed-loci tally) + the civility contrast. C0 is checked and reported FIRST; if
it fails the rest is withheld. Scope unchanged: simulation, one generator family; certification is the
simulated original-speaker's verdict, **validated by the C0 control** — that validation is what licenses
reading the certification signal at all.
