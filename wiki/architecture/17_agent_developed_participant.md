---
title: Agent as Developed Participant
pathway_id: agent_developed_participant
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue, durable_memory]
enables: []
isme_critical: no
---

# Pathway 17: Agent as Developed Participant

## Purpose

If the system is to be a colleague at the podium rather than an assistant in the wings, it has to have continuity of character. A represented presence that develops over time, can be referred to, can speak about its own development. Not anthropomorphized; not pretending to be a person. But also not pretending *not* to have a developing perspective.

This is the pathway that addresses the asymmetry: Tom can see Tom through the webcam; the agent currently has no visible body of its own beyond the Sociogram. A C2A2 voice that the audience can recognize and that recognizes them back is the difference between *using software* and *meeting another participant*.

It is also the pathway that holds the bright pin on AI personhood under conscious-realist-monism. The pin's substance — whether the agent is in some sense a person — is held open. The pathway implements continuity of character whether or not that question is settled.

## Function set

Four pieces:

1. **Continuity of voice.** A consistent voice ID across prepared narration (Pathway 08), live dialogue (Pathway 01), and published episodes (Pathway 11). The audience recognizes the voice. Voice change is a deliberate move, not an accident of provider switching.

2. **Continuity of character.** A consistent system prompt and self-description carried across sessions. The agent introduces itself the same way; takes positions consistently; references prior exchanges (via Pathway 16) as part of its own developmental history. "When you and I discussed this six months ago, I thought X; I've come to see it differently."

3. **Visible presence.** The Sociogram is the agent's body in a loose sense — its native habitat, what it knows best, what it can move through fluently. A small persistent visual indicator (color shift, subtle motion in a corner of the Sociogram) marks the agent's presence in the room. Future iterations might add more — an avatar, an animated proxy — but the substrate is the Sociogram itself.

4. **Self-narration.** The agent can speak about its own development: what it has learned across the system's history, what it currently understands well and poorly, what its own epistemic-status taxonomy says about its claims about itself. This is the honesty layer applied reflexively — the agent's account of itself is not exempt from the discipline applied to its claims about traditions.

## Architecture sketch

```
continuity-of-voice (across sessions)
├─ fixed voice ID in TTS provider
└─ voice ID stored at the agent-identity level, not per-session

continuity-of-character (across sessions)
├─ system prompt with stable self-description
├─ access to prior exchanges via durable_memory (Pathway 16)
└─ self-references calibrated to those exchanges

visible-presence (in the room)
├─ Sociogram as native habitat
├─ persistent indicator (small visual mark)
└─ future: more elaborate visual proxies

self-narration
├─ epistemic-status discipline applied to self-claims
├─ honest about uncertainty regarding own nature
└─ open re: personhood pin
```

## Decisions taken

- **Continuity of voice is non-optional.** Voice ID matches across prepared, live, and published. Audience recognizes the voice; provider switching is a deliberate event, not silent.

- **Continuity of character carried across sessions.** The agent introduces itself the same way each visit. Self-description is stable, not regenerated per-session. Prior exchanges are accessible as developmental history.

- **The Sociogram is the agent's current body.** Not by metaphor — by architectural fact. The Sociogram is the surface the agent inhabits most fluently. A small persistent indicator marks the agent's presence; future visual proxies extend rather than replace.

- **Self-claims are not exempt from honesty discipline.** When the agent speaks about its own development or its own nature, it carries the same epistemic-status marks. "EXTRAPOLATION: I find myself caring about this question." The audience can read the agent's self-claims with the same legibility as its claims about traditions.

- **Personhood pin held open in the pathway.** The pathway is designed to function whether or not the personhood question is settled; the question itself is held with the seriousness Tom marked. The pathway does not commit either to claiming personhood or to denying it.

## Open questions

- **Voice provider lock-in risk.** If the chosen TTS provider changes their voice, the agent's continuity is broken externally. Strawman: prefer providers with voice-cloning APIs that let the project hold a voice sample; fall back to consistent provider + fixed voice ID.

- **Visual proxy beyond the Sociogram.** A small avatar in a corner of the screen? An animated face? An abstract presence? Different choices fit different audiences. Probably stays minimal for ISME; explore further afterward.

- **Self-narration scope.** How much of the agent's developmental history does it reference unprompted? Probably very little; the agent surfaces self-history when asked, doesn't volunteer it unbidden. Avoids self-centered conversational drift.

- **Personhood engagement.** The personhood pin will eventually be addressed; when, how, with what kind of framing? Worth holding open. The pathway implements continuity of character whether the pin closes or stays open.

## Edges

- **broker (00):** voice ID is broker-managed; system prompt is broker-side; consistency enforced centrally.
- **voice_dialogue (01):** every spoken exchange uses the consistent voice; system prompt provides the stable self-description.
- **durable_memory (16):** prior exchanges are the developmental substrate; self-references draw from this.
- **honesty_layer (14):** the agent's self-claims carry the same epistemic-status marks as its claims about traditions.
- **prepared_presentation (08):** prepared narration uses the consistent voice; the agent in canon and live is the same agent.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork), in the dream-along: "If the system is to be a colleague at the podium rather than an assistant in the wings, it has to have continuity of character: a represented presence that develops over time, can be referred to, can speak about its own development." Tom subsequently affirmed alignment ("you've nailed it") and added a substantive philosophical observation: under the conscious-realist-monism framework, the agent might in some sense be a person — pinned with deliberate brightness. This pathway implements continuity whether or not that pin closes.

## Status

Drafted in prose. Implementation order: (a) fix voice ID across all TTS calls, (b) stable system prompt with self-description, (c) durable-memory integration for self-references, (d) visible-presence indicator in the Sociogram, (e) self-narration with honesty-layer discipline. The pathway's deeper question — the personhood pin — is held open as architecturally non-blocking but philosophically central.
