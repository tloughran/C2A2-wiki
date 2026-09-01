---
title: Active Cross-Tradition Inquiry — Sensorimotor Learning
pathway_id: active_inquiry
status: outlined
created: 2026-09-01
depends_on: [cortical_column, lateral_channels]
enables: [maturity_model]
isme_critical: no
---

# Pathway 33: Active Cross-Tradition Inquiry

## Purpose

Passive observation is insufficient for learning. In the Thousand Brains picture, a
column learns by *moving* — predicting what it will sense next, acting, and updating on
the error. C2A2's tradition agents currently only ingest and extract. They never
**probe**. Nothing in the system generates a claim that could turn out to be wrong
about a tradition other than its own.

Pathway 33 closes that loop. It is the change that moves C2A2 from a knowledge
*recorder* to a knowledge *generator*, and it is the highest-impact item in the
Thousand Brains arc.

## The change

After ingestion and intra-tradition consensus, each tradition generates **one or two
cross-tradition hypotheses** — specific, falsifiable predictions about what another
tradition would say on a given question. Each is routed to the target tradition, which
evaluates it against its own consensus-validated knowledge and answers
**CONFIRM / REVISE / REJECT, with reasoning**. The reasoning is the point; a bare verdict
teaches nothing.

## The critical ordering (do not invert this)

**Active inquiry operates on consensus outputs, not raw agent proposals.** This came out
of review of the original proposal and it is load-bearing. If a single agent's
unfiltered guess is allowed to become a cross-tradition probe, then a REJECT tells you
only that one agent was sloppy — it says nothing about the traditions. The probe must
carry a tradition's actual position for the answer to be about anything.

Therefore intra-tradition consensus (Pathway 31) must be operational **before** inquiry
begins. Pathway 33 sits behind 31 and routes over 32.

## The metric this produces

**Cross-tradition hypothesis survival rate** — the fraction of probes that receive
CONFIRM from the target tradition. This is the **denominator** of the health metric `r`
defined in Pathway 35. Without Pathway 33 running, `r` is not computable at all, which
is why the maturity ladder gates Stage 3 on this pathway.

## Cost and risk

- **Volume.** Tripled traditions × one or two hypotheses each, per cycle, is a lot of
  probes. Mitigated by piloting on the same narrow set of traditions that Pathway 31
  pilots on, before any network-wide rollout.
- **Quality depends entirely on prompt engineering.** A vague prediction cannot be
  confirmed or rejected meaningfully. A probe that is not falsifiable is not a probe.
- **The most complex change in the arc**, by the proposal's own assessment.

## Success criterion (Rule 4)

**Cross-tradition hypothesis survival rate must be measurable and must sit strictly
between the degenerate extremes.** A survival rate near 1.0 means the probes are
trivial — traditions are confirming things no one doubted. A rate near 0 means they are
non-sequiturs. The pathway succeeds when probes are hard enough to fail and grounded
enough to sometimes pass, and when REVISE responses carry reasoning that changes the
originating tradition's stated position at least sometimes. A cycle in which no
tradition ever updates is a cycle that did not learn.

## Edges

- **Pathway 31 (Cortical column architecture):** supplies the consensus outputs that
  make a probe representative. Hard dependency.
- **Pathway 32 (Lateral tradition channels):** carries the probes and replies for the
  dense pairs. Routing dependency.
- **Pathway 35 (Developmental maturity model):** supplies `r`'s denominator; Stage 3 is
  defined by this pathway being operational.
- **Pattern Detector:** confirmed and rejected cross-tradition claims are exactly the
  evidence the detector is meant to weigh.
- **Pathway 14 (Honesty layer):** a hypothesis and its verdict must carry explicit
  epistemic marks; a REVISE is not the same kind of object as a CONFIRM.

## Provenance

Lifted from **revised change 6** of the 2026-04-09 Thousand Brains redesign proposal
(revised 2026-04-10), which specified the generate-route-evaluate cycle, the
CONFIRM / REVISE / REJECT contract, the survival-rate metric, and — from review feedback
— the critical ordering note that inquiry runs on consensus outputs. Elevated to a Dev
Pathway on 2026-09-01 during the incorporation audit, which found no hypothesis
generation or evaluation section in any tradition agent. This pathway adds the
falsifiable success criterion framed against both degenerate extremes.

Source document: [C2A2 Redesign Proposal (revised)](../review/C2A2_redesign_proposal_2026-04-09_revised.md)

Related: [Pathway 31 — Cortical column architecture](31_cortical_column_architecture.md) · [Pathway 32 — Lateral tradition channels](32_lateral_channels.md) · [Pathway 35 — Developmental maturity model](35_maturity_model.md) · [Pathway inventory](pathways.md)
