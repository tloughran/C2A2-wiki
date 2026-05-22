---
title: Ambient (Non-Imperative) Visualization Control
pathway_id: ambient_viz
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue]
enables: [probing_channel, generative_canvas, prepared_presentation]
isme_critical: yes
---

# Pathway 02: Ambient (Non-Imperative) Visualization Control

## Purpose

The Sociogram and the other visualizations in the system respond to conversation as ambient companions, not as commanded UI. The agent does not say "let me show you Levin's bioelectric work"; it just discusses Levin's bioelectric work, and the visualization drifts toward that neighborhood on its own. Three intelligences — dialogue, viz, and human — share attention rather than one driving the others.

The reason this matters: a viz that responds to commands feels like a tool being operated. A viz that responds to conversation feels like a participant. The audience experiences three participants, not a presenter using software.

## Function set

The ambient control loop has four moving parts:

1. **Topic signal stream.** The dialogue layer (Pathway 01) emits a continuous stream of `mention(topic, weight)` events as the STT transcript arrives. Topics are vault concepts — thinker names, PRS components, Summa questions, structural groups. Weight indicates intensity of mention (incidental name-drop vs. central focus).

2. **Bias layer.** The Sociogram already runs a continuous D3 force simulation. The bias layer sits on top: each active topic places a soft attractor at the centroid of vault nodes matching that topic. Multiple topics produce multiple attractors. The force simulation, with the bias attractors added, drifts the layout toward the conversation's center of gravity.

3. **Inertia and decay.** Attractors don't snap in or out. New mentions ramp in over ~0.5–1.0 seconds; old mentions decay over ~5–10 seconds unless reinforced. The result is smooth drift, never sudden focus changes. The audience's eye trains on the speaker, not on UI motion.

4. **Override channel.** Sometimes the agent or speaker genuinely needs to direct attention — "hold this view while I make a point," or "zoom into this region." These are marked verbally when invoked ("if you watch the lower-right cluster…") so they don't feel like commanded UI. The existing Hold Forces toggle in the Sociogram is the technical override.

## Architecture sketch

```
voice_dialogue STT transcript
        ↓
   topic extraction (broker-side)
        ↓
   mention(topic, weight) stream
        ↓
   bias layer (client-side, in viz)
        ├→ attractor at topic centroid
        ├→ ramp-in / decay
        └→ injected into D3 force sim
                ↓
        Sociogram renders with inertia
```

## Decisions taken

- **Soft signals as default, commands as exception.** The agent does not have a `highlight_node` imperative as its primary channel. It has `mention(topic, weight)` and `bias_attention(topic, decay)`, which inform the viz of what's being discussed. Strong commands exist but are exceptional and verbally marked.

- **D3 force simulation is the substrate.** The viz already has continuous motion. The bias layer rides on top of the existing simulation rather than replacing it.

- **Inertia and decay are first-class.** Without them, the viz feels twitchy. With them, it feels alive. Tuning of constants happens in rehearsal — too slow and the audience can't track the conversation; too fast and the motion distracts.

- **Edges are content, not just navigation.** When the dialogue is about a connection between two thinkers, the relevant edge gets biased — its rendering thickens, its tooltip surfaces. The connecting tissue between traditions is itself a participant in the attention layer.

- **Animation discipline: alive but never distracting.** Slow motion, low contrast, restraint. The presenter remains the audience's primary focus; the viz is companion, not competitor.

## Open questions

- **Decay constants.** What ramp-in and decay times produce the right "drift" rhythm? Strawman: 0.5–1.0 s ramp-in, 5–10 s decay, but rehearsal will settle the actual numbers.

- **Drift caption.** Does the viz indicate WHY it drifted? A small caption ("drifting toward Levin: morphogenesis") would make the bias visible to the audience but might also feel intrusive. Could be a toggle.

- **Strong-command override grammar.** What's the agent's vocabulary for the exceptional case where it genuinely needs to take the wheel? Strawman: `command_focus(node_or_region, hold_duration)`, used sparingly, verbally announced.

- **Accessibility.** Continuous motion can be a problem for some viewers. A "reduce motion" preference (browser-level `prefers-reduced-motion` or in-app toggle) should suppress drift and use snap transitions instead.

## Edges

- **broker (00):** topic extraction happens broker-side; mention signals arrive via the broker's signal channel.
- **voice_dialogue (01):** dialogue STT feeds topic extraction; the viz drifts before the agent's response arrives.
- **probing_channel (03):** human probes (mouse, voice, future gesture) also bias the viz layer; same target shape as agent mentions.
- **generative_canvas (06):** when a custom viz is built on the fly, it joins the ambient layer rather than running on a separate command grammar.
- **prepared_presentation (08):** prepared canon issues the same soft signals during pre-rendered segments, so the seam between live and prepared is invisible at the viz level too.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- The shift from imperative to ambient was named explicitly mid-session: "Visualizations should be responsive to live dialogue: not 'let me see this' or 'let me show this', but native migration, responsive to verbal calls but with their own life." That moved the architecture from a command vocabulary (highlight_node, set_filters) to a signal vocabulary (mention, bias_attention).

## Status

Drafted in prose. Implementation requires (a) the topic extraction step in the broker, (b) the bias-layer engine added to the existing Sociogram viz, (c) decay-constant tuning during rehearsal. The Sociogram's existing D3 force simulation provides the substrate.
