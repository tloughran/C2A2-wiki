---
title: Durable Conversational Memory
pathway_id: durable_memory
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue, recursive_episode]
enables: [apprentice_mode, agent_developed_participant]
isme_critical: no
---

# Pathway 16: Durable Conversational Memory

## Purpose

A persistent layer so visitors can pick up where the conversation left off — across sessions, across months. "You and I discussed Hoffman's interface theory at ISME; you raised a question about whether interface-realism collapses into idealism, and we left it open." That continuity affordance is small in cost and large in value.

It is also the system's historical self-knowledge. The system remembers its own dialogues and grows by them. Returning visitors are not strangers; they are participants whose prior threads exist as substrate for the next exchange.

## Function set

Four pieces:

1. **Per-visitor identity.** Each visitor has a stable identifier (account, email, anonymous-but-cookie-recognized, or whatever the chosen sign-in mechanism produces). The identifier is the index under which prior dialogue persists.

2. **Conversation persistence.** All dialogue exchanges (Pathway 01), probe events (Pathway 03), plot generations (Pathway 05), and apprentice-curriculum state (Pathway 15) persist per-visitor in a durable store. The store is queryable: "show me what we discussed last," "find the thread about Hoffman."

3. **Resume affordance.** On return, the visitor is greeted with a brief summary of prior threads and an offer to resume any. "We had three open threads: interface theory and idealism, McGilchrist on attention, and the c282 outreach plan. Which would you like to take up?" The visitor picks, or starts fresh.

4. **Selective forgetting.** Visitors can request that specific threads be removed. The system also auto-prunes threads older than a configurable horizon (e.g., 18 months) unless the visitor pins them.

## What's a durable store? *(apprentice note)*

A durable store is a database that persists across server restarts, machine power-downs, and time. In contrast to in-memory state (which vanishes when the broker process restarts) or session state (which vanishes when the visitor closes the tab), a durable store keeps records intact across months and years. On Cloudflare specifically, three options exist: **D1** (a SQL database, good for queryable structured data like dialogue history), **KV** (a fast key-value store, good for lookups), and **Durable Objects** (per-visitor stateful actors, good for active session state). Most projects use a mix.

## Architecture sketch

```
per-visitor durable store
├─ identity index
├─ dialogue exchanges (with timestamps, vault attestations)
├─ probe events
├─ generated plots and visualizations
├─ apprentice-curriculum state
└─ pinned threads

resume flow:
   visitor returns
        ↓
   summary of prior threads
        ↓
   visitor picks: resume X / start fresh / explore other threads
        ↓
   prior context loaded into the active dialogue session

selective forgetting:
   visitor request → mark threads removed (soft delete, then purged)
   auto-prune → threads older than 18 mo without pin → purged
```

## Decisions taken

- **Per-visitor identity, with anonymous mode allowed.** Stable identity supports continuity but is opt-in for anonymous public visitors; anonymous mode operates without persistence.

- **Persistence covers all dialogue surfaces.** Not just text exchanges, but probes, plots, and curriculum state. Returning visitors find the whole context, not just the words.

- **Resume is presented as choice, not forced.** Returning visitors get a summary and pick which thread (or none) to take up. Continuity is offered, not imposed.

- **Selective forgetting is non-optional.** Visitors can delete threads; the system honors deletion. Privacy plus the right kind of conversational humility.

- **Auto-prune protects against accumulation.** Old threads age out unless pinned. The store doesn't grow without bound; the live conversational substrate stays manageable.

## Open questions

- **Identity mechanism.** Email + magic link? GitHub OAuth? Anonymous-cookie identity for casual visits, upgradable on sign-in? Strawman: cookie for anonymous, email-magic-link for persistent. Worth Tom's judgment.

- **Storage substrate on Cloudflare.** D1 (SQL on Workers), KV (key-value), or Durable Objects (per-visitor stateful actors). D1 fits the relational query needs; KV is fast for simple lookups; Durable Objects suit per-visitor session state. Probably some mix.

- **Cross-device continuity.** A visitor who used the system on a laptop in March and returns on a phone in October — do they see the same thread history? Yes if signed in; no if anonymous-cookie. The trade-off lives at the identity layer.

- **Threads visible across visitors.** Can two visitors who participated in the same group dialogue (in-room + Zoom) see each other's view? Probably not by default; group sessions get a shared thread with redacted speaker attribution unless explicitly opt-in.

## Edges

- **broker (00):** durable store accessed broker-side; per-visitor identity is the broker's auth surface.
- **voice_dialogue (01):** every exchange persists; resume flow loads prior context into the current session.
- **probing_channel (03):** probe events persist; visitors returning see "you spent most of last session looking at Levin's morphogenesis cluster."
- **whiteboard (05):** plots persist (pinned ones in the vault, others in the per-visitor store).
- **apprentice_mode (15):** apprentice curriculum state lives here; resumption is what makes multi-month apprenticeship workable.
- **agent_developed_participant (17):** durable memory is also the system's own historical self-knowledge — the substrate the agent's continuity of character rests on.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork), in the dream-along: "Not just session archives, but a persistent layer so the same visitor returning months later can pick up where the conversation left off." Tom: "you've nailed it." The continuity affordance was named as essential infrastructure for the other pathways to compound rather than restart.

## Status

Drafted in prose. Implementation order: (a) identity layer (anonymous cookie + email-magic-link), (b) durable store schema and storage substrate, (c) resume-flow UI, (d) selective-forgetting flows, (e) auto-prune scheduler. Builds on broker; integrates with most other pathways as a substrate layer.
