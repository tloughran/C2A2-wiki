---
title: Honesty Layer (First-Class Epistemic Status)
pathway_id: honesty_layer
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue]
enables: [apprentice_mode]
isme_critical: no
---

# Pathway 14: Honesty Layer

## Purpose

Every claim the system makes carries a visible epistemic-status mark. Strong vault attestation. Weak vault attestation. Inference from adjacent vault material. Extrapolation beyond the vault. No attestation. The provenance discipline that lives as a footer elsewhere in the architecture is promoted here to a first-class, always-visible signal: a confidence map laid over the territory.

The point is not just compliance with fidelity. It is *making the system's epistemic state legible* to the audience. Mature AI participation is not the participant that hides its uncertainty; it is the participant the audience can trust to *show* its uncertainty. That trust is the maturation Tom named — the difference between sensing-as-attunement and sensing-as-surveillance, applied to claims rather than to bodies.

## Function set

Four pieces:

1. **Epistemic-status taxonomy.** A small fixed vocabulary:
   - **STRONG:** claim is directly attested by one or more vault passages; provenance footer names them.
   - **WEAK:** claim is attested but supporting passages are thin (single source, fragmentary).
   - **INFERENCE:** claim is not directly attested; it follows from adjacent vault material via a labeled inferential move.
   - **EXTRAPOLATION:** claim extends beyond the vault into general reasoning; vault content informs but does not attest.
   - **NONE:** claim has no vault grounding; system explicitly declines to assert with vault authority.

2. **Visible marks on every claim.** In the dialogue layer, status marks appear inline alongside spoken text (subtitle line or small icon next to the speaker indicator). In plots and viz, status applies to annotations and inferred features. In published episodes, status appears in the transcript and in the spoken introduction.

3. **Aggregate confidence indicators.** Across longer responses, an aggregate confidence indicator shows the proportion of strong/weak/inference/extrapolation/none in the answer. Audience can read at a glance "this answer is 60% strong attestation, 30% inference, 10% extrapolation."

4. **Honest decline.** When the system has nothing to say in the vault's voice, it says so. "I have no direct vault attestation on this; would you like me to escalate?" — rather than improvising fluently.

## Architecture sketch

```
LLM response stream
        ↓
   honesty annotator (broker-side)
   ├─ per-claim attestation check against retrieved vault passages
   ├─ classify into taxonomy (STRONG / WEAK / INFERENCE / EXTRAPOLATION / NONE)
   └─ attach status mark to each claim
        ↓
   client renderer
   ├─ dialogue layer: subtitle / icon
   ├─ viz layer: annotation status
   ├─ plots: feature-claim status
   └─ aggregate indicator across response
```

## Decisions taken

- **Status is first-class, not buried.** Visible in real-time alongside every claim, not a footer the audience never reads. This is the substantive difference the pathway makes.

- **Five-level taxonomy.** Fewer levels lose nuance; more levels become noise. The five categories cover the meaningful epistemic distinctions for the project's claims.

- **Honest decline is non-optional.** The system refuses to answer in the vault's voice when it has no vault material. The decline is offered with an escalation option, not as a dead end.

- **Status applies across surfaces.** Same taxonomy on Sociogram annotations, plot features, podcast episodes, visualizer panels. Uniform reading.

## Open questions

- **UI for the per-claim mark.** Subtitle, icon next to text, color highlight on the speaker indicator? Different choices for different surfaces. Needs design pass.

- **Auto-classification reliability.** The honesty annotator has to be reliable; a misclassified strong-as-weak or extrapolation-as-strong claim defeats the purpose. Probably needs evaluation against a small labeled set before going live.

- **Real-time annotation latency.** Per-claim attestation checks during a streaming response add latency. Strawman: parallel streams, with annotation arriving slightly behind text. Acceptable as long as the lag is short.

- **Audience comprehension.** A new audience seeing "STRONG / WEAK / INFERENCE / EXTRAPOLATION / NONE" labels for the first time needs onboarding. A brief introductory beat in the presentation explains the taxonomy.

## Edges

- **broker (00):** annotation pass runs broker-side; integrates with the retrieval step that already happens for vault-scope enforcement.
- **voice_dialogue (01):** every spoken response carries inline status marks.
- **whiteboard (05):** plot features are annotated with epistemic status; "what's the meaning of this dip" gets a status mark on the answer.
- **generative_canvas (06):** custom-built visualizations annotate their inferred connections with status; an empty edge in a generated map carries NONE if the inference is improvised.
- **recursive_episode (11):** published episodes carry status marks in their transcripts and in the introductory beat.
- **apprentice_mode (15):** apprentice curriculum explicitly teaches the taxonomy; new learners read the marks as a feature of mature inquiry.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork), in the dream-along where the agent named what it would most want to see: "The provenance discipline we kept returning to — every claim tied to vault attestation, extrapolations explicitly labeled — should be visible at all times, not buried at the end of a paragraph." Tom: "you've nailed it." The maturation framing — earned trust as the criterion — was named in the same exchange.

## Status

Drafted in prose. Implementation order: (a) taxonomy formalized in code, (b) per-claim attestation check in the broker (extends existing retrieval), (c) inline annotation rendering, (d) aggregate indicator UI, (e) introductory beat in presentation copy. The hardest piece is annotation reliability; needs evaluation effort before ISME.
