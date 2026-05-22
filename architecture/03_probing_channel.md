---
title: Probing Channel
pathway_id: probing_channel
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue, ambient_viz]
enables: [generative_canvas, sensing]
isme_critical: yes
---

# Pathway 03: Probing Channel

## Purpose

The system has one uniform input shape for "the user is paying attention to this," regardless of how the attention was expressed. Voice, mouse click, touch, future gesture, future gaze — all funnel into a single probe-event stream that the dialogue layer and the ambient viz layer both subscribe to.

This is a small but architecturally consequential decision. Without it, every new input modality (eye tracking, AR wand, room sensing) forks the dialogue layer. With it, the dialogue layer is modality-agnostic; new probe sources plug in via adapters without touching the agent's grammar.

## Function set

The probing channel has three moving parts:

1. **Unified probe-event shape.** Every probe — regardless of source — produces an event of the form:

   ```
   {
     element_id:   <vault-node-id, edge-id, plot-element-id, or canvas-region-id>,
     element_type: "node" | "edge" | "plot_element" | "canvas_region",
     intensity:    0.0–1.0,
     source:       "voice" | "mouse" | "touch" | "gaze" | "gesture" | "sensing" | …,
     timestamp:    <ms since session start>
   }
   ```

   The agent never asks "where did this come from?"; it just receives "attention is on X."

2. **Input adapters.** Each input source has a small adapter that produces probe events:
   - *Voice adapter:* receives STT transcripts (Pathway 01), identifies vault elements mentioned, emits probe events with intensity proportional to centrality of mention.
   - *Mouse/touch adapter:* standard click and hover handlers on the Sociogram, plots, canvas. Click = high intensity; hover = low intensity ramping with dwell time.
   - *Gaze/gesture adapter (future):* eye-tracker or hand-tracking SDK plugs in here; same output shape.
   - *Sensing adapter (Pathway 09):* aggregate audience attention contributes probe events too.

3. **Subscribers.** Both the dialogue layer (Pathway 01) and the ambient viz layer (Pathway 02) subscribe to the probe stream:
   - Dialogue layer: "user is attending to X" — the agent can pick up the thread in conversation ("you're looking at Hoffman; want me to compare his interface theory with Levin's?").
   - Viz layer: probe events also bias the viz layer's attention — clicking a node is functionally similar to mentioning it in conversation.

## Architecture sketch

```
input sources                     adapters                  unified stream
─────────────────                  ────────                  ──────────────
mic ──────────────────► voice adapter ─────────┐
mouse / touch ────────► mouse adapter ─────────┤
eye tracker (future) ─► gaze adapter ──────────┼──► probe stream
hand tracker (future)─► gesture adapter ───────┤        ↓
room sensing (P.09) ──► sensing adapter ───────┘     subscribers:
                                                         ├─ dialogue layer (P.01)
                                                         └─ ambient viz layer (P.02)
```

## Decisions taken

- **Single uniform event shape.** Source field carries provenance of the probe; the agent receives "attention is on X" without modality-specific logic.

- **Probes are signals, not commands.** Clicking a node doesn't force the viz to do anything; it raises the node's attention weight. The viz layer interprets through the same bias mechanism it uses for voice mentions.

- **Probes go to both layers.** Dialogue picks up "attention is on X" and may incorporate it into the conversation. Viz picks up the same signal and biases its drift. Both layers can react independently.

- **Hardware extensibility.** New input modalities plug in via adapters without touching the dialogue layer. When eye tracking or an AR wand becomes available, the dialogue grammar doesn't need rewriting.

## Open questions

- **Threshold and recency.** The agent shouldn't react to every probe — the user looks at lots of things in a few seconds. What's the threshold (intensity + dwell + relevance) above which the agent interjects "want to talk about that?" vs. just notes the probe quietly? Probably tuned in rehearsal.

- **Probe log persistence.** Should probe events persist to the session archive for later analysis? Useful for reflexive instrumentation (Pathway 13, under-development visualizer) but worth a privacy consideration for public users.

- **Cross-modal coordination.** What if the user is looking at one node but talking about another? Different intensities, both real attentions. The dialogue layer needs to handle the divergence — probably by prioritizing voice over passive probes, but worth marking explicitly.

- **Probe origin attribution in transcripts.** When an exchange is logged (Pathway 01) or published as an episode (Pathway 11), should probe events appear in the transcript? "User clicked Levin/morphogenesis" alongside the spoken words helps reconstruct the full exchange but adds clutter.

## Edges

- **broker (00):** voice probes arrive via the broker's STT + topic-extraction pipeline.
- **voice_dialogue (01):** voice mentions are the most common probe source; STT and topic extraction feed the voice adapter.
- **ambient_viz (02):** probe events bias the viz layer just like voice mentions do; click and look behave the same as say.
- **generative_canvas (06):** custom-built visualizations subscribe to the probe stream too — elements in a freshly built D3 simplex or Plotly chart raise probes the same way Sociogram nodes do.
- **sensing (09):** room sensing is itself a probe source — collective audience attention contributes aggregate probe events.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- This pathway emerged from the ambient-viz dream piece, with Tom's specific aside about "future generation physical prompter" — meaning whatever input hardware comes next (gaze, gesture, wand). The unified probe shape is the architectural answer that keeps the dialogue layer from forking when new input modalities arrive.

## Status

Drafted in prose. Implementation is light: define the event shape, write the voice adapter (which mostly reuses topic extraction from Pathway 01), write the mouse adapter (mostly reuses existing Sociogram click handlers), publish the probe stream as a small event bus. Other adapters plug in as hardware becomes available.
