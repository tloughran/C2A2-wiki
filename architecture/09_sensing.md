---
title: Multi-Modal Sensing
pathway_id: sensing
status: drafted
created: 2026-05-13
depends_on: [broker, probing_channel]
enables: []
isme_critical: no
---

# Pathway 09: Multi-Modal Sensing

## Purpose

The system reads the room. Speaker-facing camera detects the interlocutor's micro-expressions, attention, and the visible signs of "about to ask a question." Audience-facing camera produces aggregate engagement signals — where attention is going, density of confusion or interest, the rhythm of "got it" vs. "lost the thread." Together these give the agent and the human presenter a feedback channel that lets the conversation breathe with the room rather than barrel past it.

This is also where the system's ethics show. Sensing technology applied carelessly is surveillance; applied with discipline it is attunement. For a MacIntyrean audience, the medium has to model the respect-for-persons that the project's message articulates — or the message contradicts itself.

## Function set

Two sensing channels, each with its own pipeline:

1. **Speaker-facing channel.** One face at high fidelity (~30 fps webcam feed). Edge-processed (MediaPipe FaceLandmarker or similar) into structured signals: attention direction, eye-openness, smile-presence, brow-furrow, head-tilt. Used by the agent to time its responses ("you're thinking — let me wait"), to detect a question forming, to read sustained engagement vs. drift.

2. **Audience-facing channel.** Many faces at low per-face fidelity (one wide-angle webcam or a phone camera on a stand). Edge-processed into aggregate scalars only: room engagement score, confusion density, attention-direction heatmap, lean-forward density. Raw faces never leave the device. Individual-face data is never transmitted unless explicitly opted in.

3. **Aggregation in the broker (Pathway 00).** The broker receives only the aggregate scalars from each sensing device. The agent and the presenter's co-pilot view subscribe to the aggregate stream. The broker's sensing-aggregator job is documented in Pathway 00.

4. **Silent-active-listener treatment.** Engagement signals include positive presence — sustained eye contact with screen, leaning-forward, held stillness — not just speech or motion. The system reads these as first-class engagement, never as absence of engagement.

## What's edge processing? *(apprentice note)*

"Edge processing" means the analysis happens on the device that captured the data, rather than on a server somewhere else. So for the audience camera, the face-detection and engagement-scoring happen on the phone or Pi that owns the camera; only the aggregate numbers ("room engagement = 0.78") leave the device. Raw video never travels. This is the technical implementation of the respect-for-persons commitment — privacy isn't a policy, it's an architectural fact about where the data physically goes.

## Architecture sketch

```
speaker camera ──► edge processor (MediaPipe) ──► structured signals
                                                       ↓
                                                broker (sensing aggregator)
                                                       ↓
audience camera ──► edge processor ──► aggregate scalars ──► broker
                                                       ↓
                                            ├─ agent dialogue layer (timing, intent reading)
                                            ├─ presenter co-pilot view (room read)
                                            └─ probing_channel (Pathway 03): aggregate
                                                                              audience attention
                                                                              becomes a probe source
```

## Decisions taken

- **Edge-processed, faces never transmitted.** Non-negotiable for the MacIntyrean audience. Aggregate scalars only by default.

- **Two channels, two pipelines.** Speaker-facing and audience-facing serve different jobs; they share the broker's aggregation point but their adapters and signal shapes differ.

- **Individual-level interaction only on visible opt-in.** A designated questioner can elevate their channel from aggregate to individual ("the agent saw a question on your face"), but only with explicit consent and clear visible feedback that they are being seen.

- **Silent active listening counts.** Engagement detection includes positive presence; quiet does not mean disengaged. The grammar of the agent's response respects that — collective held attention is a moment to slow down, not speed up.

- **Sensing is a probe source.** Aggregate audience attention contributes events to the probing channel (Pathway 03), feeding both the dialogue layer and the ambient viz layer. The viz drifts toward what the room is collectively attending to.

## Open questions

- **Edge-processing target hardware.** Browser-side MediaPipe on the speaker's laptop is the simplest path. The audience-facing camera might need a dedicated device (a phone or small Pi) to keep edge processing isolated from the main demo machine.

- **Threshold for "confusion detected."** What facial signals reliably indicate confusion across a diverse audience? Worth caution: cross-cultural variation in expression is large. Strawman: aggregate brow-furrow + reduced nodding + averted gaze, but to be validated before drawing inferences from it.

- **Privacy disclosure UI.** What does the audience see that tells them sensing is active? A visible indicator on the main screen, language in the introduction, a one-page explainer on the project website. Probably all three.

- **Opt-in mechanism.** How does an individual audience member opt in to elevated sensing during the presentation? A QR code that links to a brief consent flow? A phone tap on a "see me" button? Needs design before public deployment.

## Edges

- **broker (00):** broker is the aggregation point for edge-processed sensing scalars; raw face data never reaches it.
- **probing_channel (03):** aggregate audience attention becomes a probe source; the dialogue layer and the viz layer both see "room is attending to X."
- **voice_dialogue (01):** speaker-channel signals time the agent's responses; "you're thinking" → agent pauses; "you look puzzled" → agent offers clarification.
- **prepared_presentation (08):** room-read informs the dispatcher's pacing decisions ("the room is losing it; cut to the next major point").
- **space_time_peeling (10):** Zoom video tiles are another audience-camera-equivalent channel; same edge-processing discipline applies.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- Emerged from Tom's "lunatic fringe" beat — webcam input and audience sensing — and the immediate follow-up that the tech exists but the *grammar* doesn't. The privacy discipline (edge-processing, aggregate-only by default, opt-in for individual) was named as non-negotiable for the MacIntyrean room. The "silent active listeners" framing was Tom's, surfaced as the engagement category most worth foregrounding.

## Status

Drafted in prose. Implementation order: (a) browser-side MediaPipe pipeline for speaker channel, (b) audience-facing setup with edge processing on a separate device, (c) aggregate-only signal transport into the broker, (d) opt-in flow for elevated individual sensing. ISME-grade is achievable, but the disclosure UI needs to land cleanly first; rushing the privacy layer would undercut the project's pitch.
