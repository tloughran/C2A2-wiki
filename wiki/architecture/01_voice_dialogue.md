---
title: Voice + Vault-Grounded Dialogue
pathway_id: voice_dialogue
status: drafted
created: 2026-05-13
depends_on: [broker]
enables: [ambient_viz, probing_channel, prepared_presentation, durable_memory, recursive_episode]
isme_critical: yes
---

# Pathway 01: Voice + Vault-Grounded Dialogue

## Purpose

This is the user-facing centerpiece: someone speaks; the agent answers verbally; the agent's answers are grounded in vault content. Every other pathway in the project either supports this loop or extends it. For ISME, this is the experience the audience encounters first.

The defining constraint is fidelity to the vault. The agent does not improvise beyond what the vault attests; when retrieval comes back empty, the system declines politely and says so, rather than confabulating. That's the line that makes the system credible to MacIntyreans — the eleven thinkers' traditions are represented as they exist in the vault, not as the open internet happens to render them.

## Function set

The voice dialogue loop has six stages, each streamed:

1. **Speech-to-text (STT).** The user's microphone audio is streamed to an STT provider (Deepgram, Cartesia, etc.) and emitted as a token-by-token transcript. Streaming matters — the agent starts working before the user finishes speaking.

2. **Topic extraction.** A lightweight pass (small model or rule-based) over the incoming transcript produces a list of vault topics being mentioned, with weights. These topics feed the ambient viz layer (Pathway 02) so the visualization begins drifting toward what's being discussed before the response arrives.

3. **Retrieval.** Once a meaningful clause has arrived, the question is embedded and matched against the vault's embedding index. Top-k passages are returned with their source node IDs and excerpts. Empty retrieval is itself a signal — it tells the system the question is off-scope.

4. **LLM call.** The retrieved passages plus a system prompt enforcing vault-scope and refusal grammar plus the user's question are sent to the LLM (Groq for fastest, Gemini Flash for balance, Haiku for higher quality). The response is streamed token by token.

5. **Text-to-speech (TTS).** Tokens are streamed into a TTS provider (Cartesia Sonic for fastest first-audio, ElevenLabs streaming for warmer voice). Audio is streamed back to the user. Voice ID is consistent across prepared and live (Pathway 08 seam discipline).

6. **Logging.** The full exchange — user transcript, retrieved passages, agent response, timestamps — is appended to the session archive and eventually re-ingested into the vault as new content (Pathway 11).

## Architecture sketch

```
mic → STT (streaming) → broker
                          ├→ topic extraction → ambient_viz (Pathway 02)
                          ├→ retrieval (Vectorize over vault)
                          ├→ LLM call (Groq/Gemini/Haiku) ─streaming→ broker
                          ├→ TTS (Cartesia/ElevenLabs) ─streaming→ speakers
                          └→ session-archive logger → eventual vault re-ingest
```

## Decisions taken

- **Streaming end-to-end.** No buffer holds a full response before passing along. Every hop forwards as it receives. This is the discipline that makes ~600 ms–1 s first-audible-word achievable on Cloudflare Workers (Pathway 00).

- **Retrieval gates the LLM call.** If retrieval returns no vault passages above a similarity threshold, the system does not call the LLM in answer mode — it returns a polite "I don't have direct vault material on that; would you like me to escalate to a web search?" That keeps the model from improvising beyond the vault. The escalation path runs through the broker's phone-confirmation gate.

- **System prompt enforces refusal grammar.** Even on retrieval hits, the model is instructed: ground claims in retrieved passages, label any extrapolation, decline off-topic politely with a short pivot.

- **Voice ID consistency.** The TTS voice used for live response is identical to the voice used for prepared narration (Pathway 08). The audience cannot hear which paragraph is canned and which is improvised.

- **Logging is non-optional.** Every exchange logs. The session archive is the substrate for Pathways 11 (recursive episode publishing) and 16 (durable conversational memory).

## Open questions

- **Hot-mic vs. push-to-talk vs. wake-word on stage.** Hot-mic risks the agent triggering on ambient speech; push-to-talk breaks conversational rhythm; wake-word ("Sarah, …") is a third option. Needs an ISME-rehearsal decision.

- **Interrupted speech handling.** If the user starts speaking while the agent is responding, does the agent stop mid-word, finish the current word, or continue? Interrupt-and-listen is the conversational norm but technically the trickiest.

- **Multi-speaker disambiguation.** Tom + audience questioner share the room. Does the system tag who is speaking? Speaker-diarization is available in some STT providers but adds latency.

- **Retrieval similarity threshold.** Where does the line sit between "in-vault" (proceed with LLM call) and "needs escalation" (offer web search)? Too low = improvisation; too high = false declines. Probably empirical, tuned during rehearsal.

## Edges

- **broker (00):** all LLM, STT, TTS, retrieval calls route through. Vault-scope enforcement and escalation gating live in the broker.
- **ambient_viz (02):** emits mention(topic, weight) signals as STT produces text; the viz drifts before the response arrives.
- **probing_channel (03):** voice mentions become probes in the unified probe stream.
- **prepared_presentation (08):** shares voice ID and refusal grammar; the seam between live and prepared is invisible because both use the same dialogue layer.
- **honesty_layer (14):** every claim in the agent's response carries an epistemic-status mark (strong attestation / weak / extrapolation / no attestation).
- **durable_memory (16):** exchanges persist; the same visitor returning months later can resume.
- **recursive_episode (11):** substantive exchanges become podcast episodes that re-enter the vault.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- This pathway emerged as the first concrete dream-piece in the session: "I'd like to speak to it, ask it any questions based on what's available in the vault, and have it answer verbally." Refined across the conversation with the retrieval+refusal discipline, the no-API-key-each-time constraint, and the streaming-everywhere engineering implication.

## Status

Drafted in prose. Implementation blocked on broker latency validation (Pathway 00 open question) and provider selection. Provider strawmen: Cartesia STT, Gemini Flash LLM (or Groq for fastest), Cartesia Sonic TTS. Rehearsable on a local prototype before the ISME demo.
