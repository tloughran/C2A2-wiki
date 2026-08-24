---
title: Cortical Column Architecture — Triple-Redundant, Voting Thinker Assessment
pathway_id: cortical_column
status: outlined
created: 2026-06-24
depends_on: [agentic_metabolism, honesty_layer, broker]
enables: []
isme_critical: no
---

# Pathway 31: Cortical Column Architecture

## Purpose

A distributed-processing variant of the per-thinker assessment loop, modeled on
Jeff Hawkins' Thousand Brains framework. Today the system runs **one agent per
thinker**, and that single assessment is the system's view of the thinker's work.
Pathway 31 replaces the single assessor with **three independent "column" agents**
wired differently to the same corpus, processing in parallel, plus a fourth
**adjudicator** agent that reads all three outputs and surfaces the consensus
position. Where two or more columns agree semantically, the adjudicator emits the
agreed assessment; where they diverge, the **dissensus is itself reported** rather
than discarded.

This is the second time the system borrows a thinker in its own corpus to shape its
own architecture — Pathway 29 took Friston's free-energy principle as a metabolism
controller; Pathway 31 takes Hawkins' cortical columns as a robustness-and-voting
mechanism. That is intended, not incidental: the accelerator is meant to be built out
of the rationalities it studies.

## The Hawkins mapping (and where it must not be taken literally)

In the Thousand Brains theory the neocortex is many cortical columns each running the
same learning algorithm, each building a *complete* model of an object through its own
**reference frame**, and perception emerging from a fast **vote** across columns whose
sensory inputs differ. Two features of that picture are load-bearing here and one is a
trap:

- **Load-bearing — different reference frames.** Columns are valuable because each
  one sees the object differently. A vote across columns that all see the same thing
  the same way measures nothing.
- **Load-bearing — consensus by voting, dissent preserved.** The cortex resolves to a
  percept by agreement, but ambiguity (genuine multi-stable input) is a real state,
  not an error.
- **The trap — redundancy alone.** Three identical agents run at nonzero temperature
  are not three columns; they are one column sampled three times. Their 2-of-3
  agreement measures **stochastic variance**, not robustness, and their cost is a 3×
  tax for almost no information gain.

Avoiding the trap is the central design commitment of this pathway, below.

## What makes the three columns independent (the central decision)

The columns must differ *substantively*, not just by random seed. Candidate
wirings — at least two of these axes should vary across the three columns:

1. **Corpus slice / retrieval strategy.** Column A reads primary texts; Column B
   reads secondary and podcast-transcript material; Column C reads the thinker's
   cross-tradition reference edges (how others cite them). This is the closest analogue
   to "different sensors."
2. **Analytic frame.** Different decomposition order over the PRS structure —
   problem-first vs. solution-first vs. resource-first — so each column reconstructs
   the thinker's program along a different axis.
3. **Model / parameters.** Different base model or temperature, the weakest axis on
   its own but cheap to combine with the others.

Open question to resolve before any code: which two axes, and how do we keep them
**fixed and documented per column** so that a dissensus is attributable to a real
difference in wiring rather than drift? (Rule 1 — named, not guessed.)

## Consensus, dissensus, and the adjudicator

- **Consensus threshold:** two-thirds or greater **semantic** agreement (2 of 3). The
  adjudicator decides agreement, so "semantic" must be operationalized — entailment
  between assessments? Match at the level of PRS-triplet claims? Surface overlap is not
  enough. This definition is the adjudicator's whole contract and must be specified, not
  left to vibe.
- **Adjudicator as quality gate:** reading three assessments and classifying agreement
  is a genuine judgment call, so using the model here is correct (Rule 5 — model for
  classification, not for routing). It is the one place model judgment is licensed; the
  column fan-out, scheduling, and tallying stay deterministic.
- **Dissensus is a first-class output.** When the columns split, that is signal: it
  flags a thinker (or a sub-claim within a thinker's program) where the corpus
  under-determines the assessment, or where the reading genuinely forks. Per-thinker
  and per-claim **dissensus rate becomes a measurable detector output** — exactly the
  kind of evidence-about-how-positions-behave-under-rich-information that the
  accelerator/detector aim is after. This is the most interesting payoff of the
  pathway, beyond mere robustness.

## Cost, and why this starts as a one-track pilot

Triple columns plus an adjudicator is roughly **3–4× the agent and token load per
thinker track**. Run across all 15 traditions it collides head-on with Pathway 29
(agentic metabolism) and the project's standing token budgets. Therefore:

- **Pilot on a single thinker track first** — Hawkins himself is the natural choice
  (the architecture assessing its own source). Prove the consensus mechanism and
  measure whether triple-column assessments survive human review at a higher rate than
  the incumbent single-agent assessment **before** spending 4× across the swarm.
- **Run the fork under the metabolism controller (Pathway 29),** not outside it, so the
  3–4× draw is subject to the same backpressure and respiratory-control reallocation as
  every other agent. The cortical-column fork is precisely the kind of high-draw
  subsystem that controller exists to govern.

## Success criterion (Rule 4)

The pathway is justified only if the extra cost buys epistemic quality. Concretely:
**triple-column consensus assessments should survive Tom's review (or an independent
check) at a measurably higher rate than single-agent assessments on the same thinker,
and the reported dissensus should land on claims a human agrees are genuinely
contestable.** If consensus assessments are no more durable than single-agent ones,
the 3–4× cost is not warranted and the pathway should be parked, not scaled. The pilot
exists to falsify that claim cheaply (swarm-contract falsifiability).

## Implementation sketch

Post-ISME (the July 8–10 presentation is the gate). Sequence:

1. Snapshot-clone the current C2A2 state (full vault + agent definitions) so the fork
   starts from a known-good, reproducible baseline.
2. Fork **one** thinker track into the three-column + adjudicator shape, with the two
   independence axes fixed and documented per column.
3. Wire the adjudicator's agreement contract and dissensus reporting; route its output
   through the honesty layer (Pathway 14) so consensus vs. dissensus carries an explicit
   epistemic mark.
4. Run under the metabolism controller; measure consensus durability and dissensus
   placement against the success criterion.
5. Only on a passing pilot, generalize across thinker tracks.

(Any push of fork artifacts follows the project's no-blind-push rule.)

## Edges

- **Pathway 29 (Agentic metabolism):** the 3–4× draw is governed by, not exempt from,
  the metabolism controller; this fork is a stress-test of that backpressure design.
- **Pathway 14 (Honesty layer):** consensus and dissensus are emitted as explicit
  epistemic-status marks, not flattened into a single confident assessment.
- **Pathway 07 (Unsaid-edges map):** dissensus localizes under-determined regions of a
  thinker's program — a sibling to foregrounding empty edges as program-generating
  facts.
- **Pathway 00 (Broker):** the column fan-out and adjudicator are orchestrated through
  the broker's agent-scheduling and gating, reusing existing key-holding and
  episode-publishing controls.
- **Measurement framework** (`architecture/measurement_framework.md`): per-thinker
  dissensus rate is a new candidate detector signal under the constitutional aim.

## Provenance

Source: Tom's DEVPATH-031 proposal, supplied 2026-06-24 in the RC Karpathy Wiki Cowork
thread and elevated to a Dev Pathway. The original spec defined the three-column +
adjudicator shape, the 2-of-3 semantic-consensus threshold, dissensus reporting, the
~3× scaling estimate, and the post-July-10 / snapshot-clone-then-fork plan. This
pathway preserves that design and adds: the Thousand-Brains "different reference frames"
requirement (independence axes, against the redundancy trap), dissensus as a measurable
detector output, the cost collision with Pathway 29 and the resulting one-track-pilot
discipline, an operational definition demand on the adjudicator's agreement contract,
and an explicit falsifiable success criterion.

**Earlier origin, recorded 2026-08-24.** The DEVPATH-031 proposal was not the idea's first
appearance. This pathway descends from the 2026-04-09 Thousand Brains redesign proposal
(revised 2026-04-10), where it appears as **revised change 5** (tripling of tradition agents
for intra-tradition consensus) together with half of **revised change 7** (the 2-of-3 voting
protocol and dissent logging). It was independently resurfaced on 2026-06-24 and retargeted in
the process — from *three agents per tradition* to *three assessor columns per thinker* — and
sharpened with the requirement that columns differ by reference frame rather than random seed.
Same idea, better specified; the lineage simply went unrecorded until the incorporation audit
found it. The 2026-06-24 attribution above stands unchanged.

The remaining half of revised change 7 — the health metric `r` — is carried by
[Pathway 35](35_maturity_model.md), which also supplies the maturity ladder in which this
pathway's consensus mechanism is the Stage 2 benchmark.

See: [C2A2 Redesign Proposal (revised)](../review/C2A2_redesign_proposal_2026-04-09_revised.md)
· [[C2A2_redesign_proposal_2026-04-09_revised]]
· [[35_maturity_model]]
· [[33_active_inquiry]]
