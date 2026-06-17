---
title: Community Heartbeat — Shareable Multi-Community AI-Education Signal System
pathway_id: community_heartbeat
status: drafted
created: 2026-06-17
depends_on: [durable_memory, honesty_layer, broker]
enables: [optional_interoperability, portability_toolkit]
isme_critical: no
---

# Pathway 30: Community Heartbeat

## Purpose

The AI Heartbeat turns the fast, lossy stream of AI developments into durable,
searchable, locally governed *education memory* for a community. Pathway 30 is the
pathway that takes it from a single, admin-only, local tool to something **useful to
people other than its author** — and eventually replicable across many communities
that each keep their own lens, preferences, and data while optionally contributing to
a shared knowledge graph.

It is the Community-AI-Education face of the system (the Explorer's second chapter),
the analogue for *current AI developments* of what the tradition wikis are for the
thinkers: raw sources stay immutable, agent runs compile durable synthesis, and a
human-governed wiki layer preserves what the community *learned* — not just what
happened this week. This directly serves the C2A2 education claim (keeping abreast of
the pace of AI development is itself the curriculum) and the broader
accelerator/detector aim (a community articulating and maintaining a shared,
information-rich lens on a fast-moving field).

## The reframe that orders the work

Almost everything valuable in the Heartbeat is a **read** — digests, summaries,
rankings, historical search. Reads can be served as static JSON snapshots: no auth,
no server, GitHub-Pages-safe. Only **writes** — sign-in, per-user preferences,
stars, comments, shared-graph contribution — need identity, consent, and a backend.

Separating reads from writes is what lets the pathway advance without prematurely
building federation infrastructure. It also fixes the build order: *multi-user on a
single instance (sign-in + preferences) comes before federation*, because being
useful to others requires accounts long before it requires cross-instance protocols.

## Function set

1. **Static signal surface (Phase 0 — done).** The Explorer tab renders metrics and
   top education signals from a static `data/digest.json` snapshot with an embedded
   fallback, so it works on Pages and over `file://`. Schema in
   `wiki/heartbeat/data/README.md`.

2. **Durable, regenerated snapshots (Phase 1).** A deterministic exporter maps the
   Heartbeat runtime's `/api/digest` into the snapshot schema (a plain field map — no
   model judgment, per Rule 5 of the project's working agreement). Dated snapshots are
   kept, giving historical depth at zero infrastructure cost. Ties to durable memory
   (Pathway 16): summaries are durable artifacts, searched historically, not rederived.

3. **Sign-in + per-user preferences (Phase 2 — current focus).** Each reader gets an
   account and a *lens*: which sources, tags, and relevance thresholds they care
   about; how signals are ranked; digest cadence; and consent boundaries. Preferences
   are defined once as a schema (`preferences.schema.json`) implemented client-side
   first (per-device, localStorage) and then persisted per-account against the
   existing Supabase project (`C2A2-wiki`, auth provisioned, 0 users). Honesty-layer
   marking (Pathway 14) distinguishes machine-inferred summaries from
   community-claimed interpretations.

4. **Selective contribution + shared graph (Phase 3).** Stars, public comments with
   rationale, and aggregate rankings can flow to a shared, searchable knowledge graph
   under explicit consent and role-based access. Personal preferences and private
   notes never leave the instance by default.

5. **Federation (Phase 4 — deferred).** Multi-instance interoperability, beginning as
   a client-side aggregator over a registry of snapshot URLs (no p2p), and only later
   any IPFS/ActivityPub-style protocol — and only once several real communities are
   independently running instances and need to interoperate. "Design for 10k
   instances" is honored by keeping the read path static and registry-driven, not by
   building 10k-scale machinery now.

## Architecture sketch

- **Read path:** runtime `/api/digest` → `export_digest.py` → `data/digest.json`
  (dated snapshots) → static tab. Pages-safe.
- **Write path:** Supabase Auth (sign-in) + a `user_preferences` row per `auth.uid()`
  under row-level security, additive to the broker tables already in the project. The
  same preference schema backs both the client-side store and the account store, so
  the local lens "upgrades" to a synced lens at sign-in with no UI change.
- **Governance:** the consent + role model (owner / admin / editor / reader / public)
  is specified *before* any write path ships. Maintainer conventions live in
  `wiki/heartbeat/AGENTS.md`; the full vision, assessment, and phased scope boundary
  live in `wiki/heartbeat/ARCHITECTURE.md`, which governs what may be built now.

## Status

Phase 0 shipped (static tab, JSON-driven with fallback). Phase 2 in progress: the
preference schema and a working client-side preferences panel are built; account
sign-in and server persistence are designed and staged against the existing Supabase
project (migration + ADR written, not yet applied — awaiting Tom's go-ahead on
sign-in method). Phases 3–4 are documented and deferred.

## Edges

- **Pathway 16 (Durable memory):** the Heartbeat's dated snapshots and persisted
  summaries are a concrete instance of durable, historically searchable memory.
- **Pathway 14 (Honesty layer):** signal summaries and inferred tags carry
  grounding/provenance marks distinct from community-claimed interpretation.
- **Pathway 00 (Broker):** auth and per-user state reuse the same Supabase project
  the broker already runs in; the `user_preferences` table is additive and does not
  touch the broker's rate-limit tables.
- **Pathway 18 (Portability toolkit) / 19 (Optional interoperability):** federation
  (Phase 4) is the Heartbeat-specific realization of optional, opt-in interoperability
  across community instances.
- **Bright pin — User notification options:** digest cadence/channel in the preference
  schema is the Heartbeat's slice of the broader notification question.

## Provenance

Source dialogue: the "RC Karpathy Wiki" Cowork thread, 2026-06-17. Tom supplied
ChatGPT's `C2A2_Heartbeat_Explorer_Update` bundle and the "Multi-Community
Architecture Vision" note; the tab was reworked to be JSON-driven, the vision was
assessed and captured in `wiki/heartbeat/ARCHITECTURE.md`, and Tom then directed that
it be elevated to a Dev Pathway and that sign-in + preferences be built ahead of
federation ("useful to others besides myself"). See `wiki/heartbeat/` for the
implementing chapter.
