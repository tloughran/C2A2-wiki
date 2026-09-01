---
title: Lateral Tradition Channels — Heterarchy Alongside Hierarchy
pathway_id: lateral_channels
status: outlined
created: 2026-09-01
depends_on: [broker, cortical_column]
enables: [active_inquiry]
isme_critical: no
---

# Pathway 32: Lateral Tradition Channels

## Purpose

The neocortex's power comes from non-hierarchical long-range connections running
*alongside* the hierarchical ones, not instead of them. C2A2 today routes every
cross-tradition signal through the Master Agent. That is a star topology: every edge
between two traditions is really two edges through a hub. Where a pair of traditions
already exchanges dense, repeated signal, the hub is pure latency and pure
serialization.

Pathway 32 adds **direct agent-to-agent channels** for those dense pairs, while the
Master Agent retains full read access to every channel. Heterarchy is added; hierarchy
is not removed.

## The change

Create `wiki/lateral/`, one file per active pair. Agents write cross-tradition flags
directly to the channels they are party to. The Master Agent still reads all channels
on its integration run, so nothing becomes invisible to it — the change is that the
Master Agent stops being on the *write* path for these pairs, not that it stops seeing
them.

## Start narrow — the mitigation is the design

The obvious failure of a heterarchy is noise: N traditions admit N(N-1)/2 possible
channels, most of which would carry nothing worth reading, and each of which is one
more surface to audit. So the pathway opens **only the four confirmed explanatory
bridge pairs**:

- Levin × Friston
- Kastrup × Friston
- Stump × Levin
- Kastrup × McGilchrist

These are not chosen for convenience; they are the pairs where a bridge essay already
exists, meaning the density is observed rather than assumed. Expansion happens only
after measured signal quality on these four justifies it. A channel that carries
nothing gets closed, not kept for symmetry.

## Cost and risk

- **Auditability drops.** A single Master inbox is one place to look; four channels are
  five. The Master Agent's full read access is what keeps this bounded, and it is a
  requirement, not a nicety — a lateral channel the Master cannot read would trade
  visibility for speed, which this pathway explicitly refuses.
- **Noise risk if over-opened.** Answered by the four-pair start above.
- Cheap in tokens relative to Pathway 31: this is routing, not additional assessment.

## Success criterion (Rule 4)

Lateral routing is justified only if it moves signal that the hub was actually
delaying or dropping. Concretely: **flags written to a lateral channel should reach a
useful downstream state (a bridge update, a Pattern Detector promotion, a logged
dissent) at a rate at least as high as hub-routed flags between the same pair, and the
pair's signal latency should measurably fall.** If lateral flags are merely duplicating
what the hub already carried, the channel is overhead and should be closed.

## Edges

- **Pathway 31 (Cortical column architecture):** consensus outputs are what deserve
  lateral routing; raw single-agent proposals do not. 31 is what makes a lateral
  message worth sending.
- **Pathway 33 (Active cross-tradition inquiry):** inquiry probes and their
  CONFIRM / REVISE / REJECT replies are the natural traffic for these channels. 33
  routes over 32.
- **Pathway 00 (Broker):** channel creation and access stay under broker
  vault-scope enforcement; a lateral channel is not an exemption from gating.
- **Pathway 07 (Unsaid-edges map):** the pairs with *no* channel are as informative as
  the ones with; an empty lateral map is a program-generating fact.

## Provenance

Lifted from **revised change 4** of the 2026-04-09 Thousand Brains redesign proposal
(revised 2026-04-10), which specified the `wiki/lateral/` shape, the Master-Agent
read-access requirement, and the four-bridge-pair start-narrow mitigation. Elevated to
a Dev Pathway on 2026-09-01 during the incorporation audit, which found the change had
never landed — `wiki/lateral/` does not exist. This pathway adds the falsifiable
success criterion and the dependency ordering behind Pathway 31.

Source document: [C2A2 Redesign Proposal (revised)](../review/C2A2_redesign_proposal_2026-04-09_revised.md)

Related: [Pathway 31 — Cortical column architecture](31_cortical_column_architecture.md) · [Pathway 33 — Active cross-tradition inquiry](33_active_inquiry.md) · [Pathway inventory](pathways.md)
