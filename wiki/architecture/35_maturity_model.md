---
title: Developmental Maturity Model — The Ladder the Metrics Are Keyed To
pathway_id: maturity_model
status: drafted
created: 2026-09-01
depends_on: [cortical_column, active_inquiry]
enables: []
isme_critical: no
---

# Pathway 35: Developmental Maturity Model

## Purpose

C2A2 is a test of an architectural influence — a claim that wiring many tradition-craft
rationalities together produces some kind of fecundity. A test needs a way to measure
progress, and eventually to predict, tune, and optimize against downsides. That requires
a declared path toward developmental maturity, with stages and measurable benchmarks,
and measurement starting immediately rather than once the system is "ready."

**This pathway is different from the other three in the arc: it is already running.**
The nightly metrics snapshots report a stage and gate their own metrics on it.
`architecture/metrics/2026-08-23_snapshot.md` reads `Stage: 1`, and two of its metric
lines read `N/A until Stage 2` and `N/A until Stage 3`. The measurement apparatus is
keyed to a ladder that, until now, appeared nowhere in the published Road Ahead. A
reader of the DevPath could not learn that C2A2 has a declared staircase, which rung it
stands on, or what unlocks the next.

**Pathway 35 publishes the ladder the measurements already use.** It is documentation
catching up with running behavior, which is why its status is `drafted` rather than
`outlined`.

## The health metric r

```
r = intra-tradition consensus rate / cross-tradition hypothesis survival rate
```

The numerator comes from Pathway 31 (the fraction of proposed items reaching ≥2/3
agreement inside a tradition). The denominator comes from Pathway 33 (the fraction of
cross-tradition probes receiving CONFIRM). **Neither is measurable today**, which is
exactly what the snapshot's two `N/A` lines are reporting.

**r must be statistically greater than 1** — traditions must be more internally coherent
than they are externally agreeable. The three-way reading:

- **r ≈ 1** → the traditions are not distinct. They agree with everything; there is no
  real internal identity to speak of, and the whole premise of many rationalities fails.
- **r → ∞** → echo chambers. Traditions so internally rigid they reject all external
  input. Internally coherent, externally useless.
- **r statistically > 1** → healthy. Genuine internal coherence *and* productive
  external dialogue.

**The null hypothesis matters as much as the ratio.** Significance is measured against
the null that internal and external agreement rates are equal — that tradition
boundaries do not matter. If that null cannot be rejected, the traditions are not
functioning as genuinely distinct perspectives, whatever r's point value happens to be.
A raw r above 1 with no significance behind it is not evidence.

## The stages

```
Stage 0 — Infrastructure:
  Self-awareness agents deployed. Provenance protocol active. Baseline metrics captured.
  Benchmark: all Phase 0 deliverables complete.

Stage 1 — Grounding:
  First 14a/14b cycle complete. First 15a/15b searches returned. First 15c dispositions
  issued. 15d monitoring schedule established.
  Benchmark: >=5 assumptions + >=5 presumptions surfaced, tested, and dispositioned.
  >=1 item INCORPORATED into validated premises. PRS displacement vectors implemented.
  Lateral channels operational. Self-awareness cycle time baselined.

Stage 2 — Intra-tradition consensus:
  Pilot cluster tripled. Consensus mechanism operational.
  Benchmark: consensus rate measurable (target: >0.6 agreement). Tripled agents
  producing differentiated assessments.

Stage 3 — Cross-tradition dialogue:
  Active inquiry cycle operational on consensus outputs.
  Benchmark: cross-tradition hypothesis survival rate measurable. First r measurement
  recorded. r statistically > 1.

Stage 4 — Full network:
  All 11 traditions tripled (33 agents). Voting protocol operational.
  Benchmark: r measured across full network. Connection density > 5.0 per tradition.
  >=2 paradigm-shift candidates confirmed.

Stage 5 — Maturity:
  Stable r in healthy range. System generating novel knowledge (NOVEL flags).
  Benchmark: connecting-meme typology emerging. C2A2 demonstrably functioning as a
  Thousand Brains system. Environment model established for health optimization.
```

## Where the system actually stands, and one discrepancy to resolve

The 2026-08-23 snapshot reports **Stage 1**, glossed there as *"network assembled and
operating; no intra-tradition consensus mechanism live."*

That gloss and the Stage 1 definition above are **not the same statement**. The ladder's
Stage 1 ("Grounding") requires PRS displacement vectors implemented and lateral channels
operational — that is, Pathways 34 and 32, neither of which is built. Read strictly
against the benchmark, the system has not completed Stage 1; read against the snapshot's
gloss, it has. The two have drifted apart, plausibly because the ladder was never
published where the nightly reporting could be checked against it.

**This discrepancy is recorded, not resolved.** Resolving it means deciding which
document is authoritative and amending the other — a judgment call that belongs to a
review pass, not to the act of publishing the ladder. Publishing it is what makes the
drift visible in the first place.

## The voting layer

Revised change 7 also specified a voting layer on the Master Agent's integration run:
each cross-program item accumulates a vote count, and items crossing a threshold
(3+ agents independently flagging the same connection) auto-promote to the Pattern
Detector. This is the mechanism by which convergence gets *counted* rather than
noticed. It is carried here with r because the two arrived together, and because vote
counts and consensus rates are measurements of the same underlying thing.

## Cost and risk

- **Stage definitions will need revision as we learn.** Stages 4 and 5 are frankly
  speculative and their benchmarks may need recalibration. A ladder that is never
  amended is a ladder nobody is checking against.
- **r needs sample size.** Both rates require enough items for significance testing;
  early r values will be noisy and should be reported with that caveat attached.
- **r is only meaningful once both rates exist.** Until Pathways 31 and 33 run, this
  pathway is documentation and stage-tracking only.

## Success criterion (Rule 4)

**The published ladder must be the one the nightly snapshots actually use.** Concretely:
the stage reported in the metrics snapshot should be derivable from this file's
benchmarks by someone reading only this file and the snapshot — and where it is not, as
with the Stage 1 discrepancy above, the gap should be visible rather than silent. The
pathway fails if the ladder becomes a second, decorative document that drifts from the
measurements while looking authoritative.

## Edges

- **Pathway 31 (Cortical column architecture):** supplies r's numerator; defines Stage 2.
- **Pathway 33 (Active cross-tradition inquiry):** supplies r's denominator; defines
  Stage 3.
- **Pathway 32 (Lateral tradition channels):** named in the Stage 1 benchmark.
- **Pathway 34 (PRS displacement phrasings):** named in the Stage 1 benchmark, and its
  connecting-meme typology is a Stage 5 benchmark.
- **Metrics snapshots** (`architecture/metrics/`): the running consumer of this ladder,
  nightly.
- **Measurement framework** (`architecture/measurement_framework.md`): r joins the
  candidate detector signals under the constitutional aim.

## Provenance

Lifted from **revised changes 7 and 8** of the 2026-04-09 Thousand Brains redesign
proposal (revised 2026-04-10), which together specified the voting layer, the definition
and three-way interpretation of r, the null hypothesis it is tested against, and the
full Stage 0–5 ladder with benchmarks. Elevated to a Dev Pathway on 2026-09-01 during
the incorporation audit, which found the ladder live and measured nightly but absent
from the published pathway inventory — the sharpest gap the audit turned up. This
pathway adds the Stage 1 discrepancy between the ladder's benchmark and the snapshot's
gloss, recorded for a later review pass.

Source document: [C2A2 Redesign Proposal (revised)](../review/C2A2_redesign_proposal_2026-04-09_revised.md)

Related: [Pathway 31 — Cortical column architecture](31_cortical_column_architecture.md) · [Pathway 32 — Lateral tradition channels](32_lateral_channels.md) · [Pathway 33 — Active cross-tradition inquiry](33_active_inquiry.md) · [Pathway 34 — PRS displacement phrasings](34_prs_displacement.md) · [Pathway inventory](pathways.md)
