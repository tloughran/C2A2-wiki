---
title: Space-and-Time Peeling (Zoom + YouTube)
pathway_id: space_time_peeling
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue, sensing]
enables: [recursive_episode, outreach_automation]
isme_critical: no
---

# Pathway 10: Space-and-Time Peeling (Zoom + YouTube)

## Purpose

Peel away the constraints of physical location and synchronous time. Remote participants join via Zoom; the conference is broadcast live to YouTube; YouTube comments stay open as a bounded async response channel for a publicized window after the presentation ends. The system handles the channel attribution so the agent always knows where an utterance arrived from and modulates its grammar accordingly.

The pipeline is well within the buildable zone — Tom has run Zoom-to-YouTube broadcasts before. The architectural piece is integrating the agent layer *into* that pipeline cleanly.

## Function set

Four channels with distinct feedback fidelities:

1. **In-room audience.** Full sensing (face, voice, gesture per Pathway 09). Highest-fidelity feedback.

2. **Zoom attendees.** Video tiles (low-fi facial signals if they opt in), voice, chat. Mid-fidelity. The agent treats Zoom voice questions identically to room-mic questions for response purposes but attributes the channel.

3. **YouTube live viewers.** Chat only, one-way video. Lower fidelity but potentially high volume. Chat questions become input to the agent at a rate-limited cadence.

4. **YouTube async.** After the live stream ends, comments accumulate over the announced response window. The agent monitors and responds asynchronously, with vault grounding and provenance, for the bounded period.

5. **Channel attribution layer.** Every utterance entering the system carries a channel tag: `room` | `zoom-{user_id}` | `youtube-live` | `youtube-async-{video_id}-{comment_id}`. The dialogue layer reads the tag and adjusts grammar (length, tone, latency) accordingly. Silence in chat does not mean what silence in a face means.

## Architecture sketch

```
room mic ──┐
Zoom audio ┼──► STT → broker → dialogue layer (with channel tag)
                                       ↓
YouTube chat ─► chat-poll adapter → broker → dialogue layer
                                       ↓
YouTube comments (async) ─► comment-poll adapter → broker → dialogue layer

C2A2 page (shared screen)
       ↓
Zoom screen share
       ↓
YouTube Live broadcast → YouTube video published

post-stream:
   announced response window (e.g., 14 days)
   ├─ agent monitors comments
   ├─ responds with vault grounding
   └─ window closes; agent posts farewell ("listening here through July 24th")
```

## Decisions taken

- **Channel attribution is first-class.** The agent always knows where an utterance arrived from; grammar adjusts accordingly (longer text for YouTube async, shorter for live room exchange).

- **Bounded async window, announced.** The agent's responsiveness on YouTube has a publicized expiration. After the window closes, the conversation reverts to ordinary asynchronous publishing.

- **Zoom integration via screen share.** The C2A2 page is the shared screen; Zoom restreams to YouTube. No bespoke streaming infrastructure needed; the agent layer rides along.

- **Sensing applies to Zoom tiles too.** Audience-camera discipline (Pathway 09) extends to Zoom video tiles. Edge-processed on the attendee's device when they opt in; aggregate-only otherwise.

## Open questions

- **Rate-limiting YouTube live chat.** A popular stream can flood the chat channel. The agent needs a triage policy — surface the most upvoted questions, throttle responses, or batch ("answering five chat questions in one go").

- **Async window length.** Two weeks is a strawman. Could be tied to the conference's natural response cycle (e.g., until ISME's published proceedings deadline).

- **Comment moderation.** Public YouTube comments include trolls. The agent should not engage with bad-faith content; needs a refusal grammar for off-topic, abusive, or adversarial comments. Probably the same refusal grammar Pathway 01 uses for off-vault questions, generalized.

- **Provenance in comment replies.** The agent's YouTube comment replies should include the same vault-attestation footer that live answers do. Format question: how does that look as a YouTube comment? A short URL back to the vault source is probably cleanest.

## Edges

- **broker (00):** all channels route through; rate-limiting and refusal grammar are broker-side.
- **voice_dialogue (01):** room and Zoom voice use the same STT/LLM/TTS pipeline; only channel attribution differs.
- **sensing (09):** Zoom video tiles are sensed under the same edge-processed, aggregate-only discipline.
- **recursive_episode (11):** the live broadcast can itself become a published podcast; YouTube async comments feed back into the vault as new content.
- **outreach_automation (12):** YouTube comments that propose substantive engagement become candidate outreach moments.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- Tom: "Why should the audience have to be present in the presentation at all. We should peel away limitations of space and time. … We could push this to YouTube as you can do with a Zoom call, and I have done in the past." The channel-fidelity differentiation emerged in the same turn; the bounded async window came as the "publicized amount of time" affordance.

## Status

Drafted in prose. Implementation reuses Tom's existing Zoom + YouTube rig; the new pieces are (a) channel-attribution layer in the broker, (b) chat-poll adapter for YouTube live, (c) comment-poll adapter for YouTube async, (d) the announced-window UI on the published video page. None blocks ISME but all extend reach significantly after.
