---
title: Prepared Presentation in the Wings
pathway_id: prepared_presentation
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue, ambient_viz]
enables: []
isme_critical: yes
---

# Pathway 08: Prepared Presentation in the Wings

## Purpose

A complete presentation, narrated and visualized by AI, sits ready in the wings — summonable by natural language ("let's cover the final four points in 5 minutes") and deliverable with the same voice and visual grammar the live agent uses. The prepared canon is the lifeboat that survives network failure on stage; it is also the deliberate companion that lets the human presenter move at the audience's pace rather than the model's.

The architectural commitment: the canon is *inhabited, not deployed*. Scripted moments — reading a passage from Aquinas aloud, walking through a sequence of prepared sub-beats — are first-class dialogue acts, not fall-throughs to canned mode. The audience cannot detect a script *as a script*.

## Function set

The prepared canon has four moving parts:

1. **Composite point structure.** Each "point" in the prepared run is composite, with sub-beats. A point about Levin's bioelectric framework might have sub-beats for (a) the problem morphogenesis poses, (b) the bioelectric resource, (c) the empirical track record, (d) the cross-tradition implication. Each sub-beat carries its own narration audio (pre-rendered with the same voice ID as live) and its own viz script (attention biases for the Sociogram and any custom viz).

2. **Dispatcher.** The natural-language interpreter that maps requests to plays. "Cover the final four points in five minutes" parses to a target segment-range and a wall-clock budget. The dispatcher checks the budget against the prepared content and either accepts it as-is, proposes a fit (drop sub-beats, accelerate pacing), or asks before starting ("three of these fit cleanly; want the fourth abbreviated, or shall I drop one?").

3. **Hybrid-flow seam.** The canonical run can be interleaved with live improvisation at any sub-beat boundary. Verbal bridges ("now, on the question of…") cover the transition; the voice ID, refusal grammar, and provenance discipline are identical across prepared and live, so the seam is invisible.

4. **Offline lifeboat.** The full canon — audio plus a deterministic JSON of viz steps — is bundled with the client page, so it plays without the broker reachable. The prepared run survives a network drop; only live improvisation needs the broker.

## Architecture sketch

```
prepared canon (bundled with page)
├─ point[1..N]
│   └─ sub-beat[1..M]
│       ├─ narration audio (pre-rendered, same voice ID as live)
│       └─ viz script (mention signals, attractor biases, optional strong commands)
│
dispatcher (voice/text input)
├─ parse request → {target_range, wall_clock_budget}
├─ fit check → propose drop / abbreviate / accept
└─ playback engine → walk sub-beats with timing
    └─ at each sub-beat boundary: hybrid seam available
```

## Decisions taken

- **Composite sub-beat granularity.** Atomic points are too coarse for time-fitting; sub-beats let the dispatcher shed parts of a point rather than drop whole points. Authoring is more work; runtime is dramatically more flexible.

- **Wall-clock budget is a first-class input.** Generalizes Tom's Rule 6 (token budgets are not advisory) to seconds of stage time. Breaches are surfaced before starting, not hidden by silent overrun.

- **Voice ID consistency.** Prepared narration and live TTS share the same voice. The audience cannot hear which paragraph was authored when.

- **Provenance discipline carries.** Every prepared sub-beat carries the same vault-attestation footer that live answers do. The agent never speaks unattributed content, prepared or improvised.

- **Offline-capable canon.** Audio and viz JSON ship with the page. Broker downtime degrades to "prepared only" rather than to silence.

- **Scripted reading is inhabited, not deployed.** A passage read aloud at the agent's initiative or the presenter's is a deliberate dialogue act with its own framing — not a fall-through.

## Open questions

- **Authoring loop.** How does Tom inspect, edit, and rehearse the prepared canon before the show? Probably a small UI surface — list of points, list of sub-beats per point, audio playback, viz preview, edit-in-place for narration text plus regenerate audio. Needs to exist before ISME.

- **Co-pilot view on phone.** During the live presentation, a phone-side view showing current segment, time remaining, improvise-vs-prepared status, and time-budget margin. Useful but not strictly required if Tom can read it off the main screen.

- **Hybrid-transition announcement.** When the live agent decides to step out of the prepared run mid-point, does it announce ("let me take a moment on this") or transition silently? Probably announce — invisible-seam doesn't mean undetectable transition; it means transitions feel native to the presenter rather than to UI.

- **How many points to prepare.** Strawman: 20-minute keynote = ~6–8 composite points, each ~3 minutes. ISME slot length will determine the actual number.

## Edges

- **broker (00):** prepared canon survives broker downtime; broker mediates the live improvisation that interleaves.
- **voice_dialogue (01):** shares voice ID, refusal grammar, and provenance discipline. The same agent speaks prepared and live.
- **ambient_viz (02):** prepared viz scripts emit the same `mention(topic, weight)` signals the live agent does; the viz interprets identically.
- **perspective_lattice (04):** prepared canon draws on eager-tier overviews; sub-beat narration text references vault content the lattice has already materialized.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- This pathway emerged from Tom's vision: "a complete presentation, narrated and visualized by AI, should be prepared and sitting in the wings. If there's 5 minutes left for 4 points, 'let's cover the final four points of the presentation in 5 minutes' should cue it." The composite-sub-beat granularity emerged as the answer to time-fitting under a wall-clock budget. The "inhabited not deployed" framing came mid-conversation from Tom's correction that scripted reading is sometimes the right move.

## Status

Drafted in prose. Implementation requires (a) the composite point/sub-beat schema, (b) the dispatcher with fit-checking, (c) pre-rendered narration audio pipeline (Cartesia or ElevenLabs), (d) the playback engine with hybrid-seam capability, (e) the offline bundle. Rehearsable on a local prototype well before ISME.
