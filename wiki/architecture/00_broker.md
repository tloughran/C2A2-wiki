---
title: Broker (Shared Infrastructure Spine)
pathway_id: broker
status: drafted
created: 2026-05-13
depends_on: []
enables: [voice_dialogue, ambient_viz, sensing, escalation, episode_publishing, outreach_automation, under_development_visualizer]
isme_critical: yes
---

# Pathway 00: Broker

## Purpose

Almost every other pathway in this project routes through a single piece of server-side infrastructure: the **broker**. It is the spine that lets the C2A2 system be public, scoped, accountable, and extensible without putting secrets, judgment, or human consent into client-side JavaScript.

The broker exists because the constraints of this project don't compose without it:

- The C2A2 page is hosted publicly (`github.com/tloughran/C2A2-wiki`). Anyone landing on it can use the voice agent, which means an LLM API key cannot live in client JS — it would be scraped within hours.
- Tom should not enter an API key each use. ("Don't depend on putting in an API key each time" — dream, 2026-05-13.)
- The voice agent must be scoped to vault topics, not free to improvise generally. Scope enforcement has to live somewhere the model can't bypass.
- External escalation (web search beyond the vault) must require human consent, gated on a phone notification.
- Sensing signals must be aggregated into anonymized scalars before they enter the dialogue layer; raw faces must never leave the device.
- Outreach (DMs to thinkers' labs, podcast invites) must be content-grounded and verifiable, not bot-spam.

A small server-side broker is the natural single integration point for all of these.

## Function set

The broker holds five jobs:

1. **API key holder.** All LLM calls go through the broker. The page never sees a key. Public visitors get to use the agent without authentication; rate-limit policy is enforced here.

2. **Vault-scope enforcer.** Every LLM call is wrapped in a retrieval step (top-k vault passages by embedding similarity) plus a system prompt that politely declines off-topic. Empty retrieval triggers a visible "no direct vault attestation" label rather than free improvisation. This is where the project's fidelity discipline lives operationally.

3. **Escalation gatekeeper.** When the agent decides web search is warranted, the broker pauses the request, fires a push to Tom's phone (mechanism options below), waits for approve/deny, and either proceeds or returns a refusal token to the agent.

4. **Sensing aggregator.** Edge-processed sensing devices report aggregate scalars (room engagement = 0.78; three pockets of confusion at the back) to the broker. Individual-face data is processed at the edge and never transmitted unless the person has explicitly opted in. This is non-negotiable for the MacIntyrean audience.

5. **Episode-publishing gate.** Outreach DMs and podcast invitations are produced with a verifiable content handle (the episode being launched, its vault attestations, the prior dialogue thread). The broker refuses to issue outreach that doesn't carry verifiable substance with it.

## Architecture sketch

```
                    client page (browser)
                          ↑↓
                  broker (serverless function)
                          │
        ┌─────────────────┼──────────────────────┐
        │                 │                      │
    LLM API       retrieval index      sensing aggregator
                  (vault embeddings)    (edge scalars in)
        │                                       │
        │                                  Tom's device
        ↓
  push-notification service ──→ Tom's phone (or co-approver)
        │
        ↓
  social-media APIs (outreach, content-grounded only)
```

## Decisions taken

- **Server-side broker, not client-only.** Public repo + no-key-entry + anyone-can-use forces this. Settled.
- **Single broker, multiple jobs.** Not five separate services. Reasons: one auth surface for Tom to operate, one place for rate-limiting, one log to inspect. Trade-off: a broker outage takes down multiple capabilities. Mitigation: prepared canon (Pathway 08) is offline-capable and survives broker downtime.
- **Edge-processed sensing, faces never transmitted.** Non-negotiable for ISME. The medium has to model the respect-for-persons the message articulates.
- **Content-grounded outreach only.** The broker refuses to emit DMs or invites without simultaneously emitting the verifiable substance (episode, attestations, dialogue thread).
- **Hosting target: Cloudflare Workers** (decided 2026-05-13, conditional on latency validation). Edge-distributed, ~10–30 ms broker-side overhead, Workers AI / Vectorize / Durable Objects available on the same platform. The latency floor for presentation-mode AI is set by LLM and TTS providers, not the broker. Paid plan ($5/mo) required for 30 s CPU limit and unlimited requests. Lock-in conditional on the streaming-latency validation pass (see Open Questions).
- **Phone confirmation channel: Twilio SMS** (decided 2026-05-13). Tom has an existing Twilio account. Pattern: one-tap signed approval link in the SMS rather than reply-keyword — no typing at the moment of approval, works on any phone, fastest path back to a paused agent request. Twilio webhook endpoint co-located on the same Cloudflare Worker as the broker. Setup work pending.

## Open questions

- **End-to-end streaming latency validation** (conditional on broker hosting decision). Confirm the full pipeline (STT → broker → retrieval → LLM → TTS) delivers first audible word in ~600 ms–1 s on Cloudflare Workers for live-presentation use. Engineering constraint: stream end-to-end, no buffering of full LLM response before TTS starts. Provider choices (Deepgram or Cartesia for STT; Groq, Gemini Flash, or Haiku for LLM; Cartesia or ElevenLabs streaming for TTS) drive the budget more than the broker does.
- **Co-approver role for escalation.** Can Tom designate a trusted approver in the front row to keep the on-stage rhythm if he's mid-sentence when an escalation is triggered? Architecturally trivial; behaviorally significant.
- **Rate-limit policy.** Public access creates an abuse surface. What policy applies to anonymous visitors vs. authenticated participants?

## Edges

- **voice_dialogue (01):** all LLM calls route through the broker; vault-scope enforcement happens here.
- **ambient_viz (02):** topic-extraction results (used to bias viz attention) are computed broker-side; the broker emits the `mention(topic, weight)` signal stream the page consumes.
- **sensing (09):** broker is the aggregation point for edge-processed sensing scalars; raw sensor data never reaches it.
- **prepared_presentation (08):** prepared canon survives broker downtime as an offline lifeboat; broker is involved only for live improvisation around the prepared run.
- **episode_publishing (11):** episode-launch and outreach DMs route through the broker so the content-substance handle is enforced.
- **outreach_automation (12):** same as above; broker refuses to issue ungrounded outreach.
- **under_development_visualizer (13):** broker's own activity logs (rate of requests, escalation approvals, outreach issued, retrieval hit-rate) become data inputs to the development visualizer's reflexive view of the system.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork), Tom on Project Mac Mini.
- The broker emerged from the question "Where does the API key live?" and grew in scope as later pathways added jobs to it. By session's end it was holding five distinct functions. The broker is the most heavily-edged pathway in the project because nearly every other pathway needs one of its capabilities.

## Status

Drafted in prose; no code yet. Hosting target and phone-channel decisions are the two practical blockers before any implementation. Both can be settled in a single short session.
