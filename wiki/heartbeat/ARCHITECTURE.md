# AI Heartbeat — Multi-Community Architecture

*Captured 2026-06-17 from the "AI Heartbeat Tool: Multi-Community Architecture
Vision" note. This is the Heartbeat chapter's architecture doc. It records the
**target** vision, a **critical assessment** of it, and a **phased roadmap** that
gets there by the simplest viable path. It does not authorize building federated
infrastructure now — see "Scope boundary" below.*

Related: [[AGENTS.md]] (maintainer schema), [[INTEGRATION_BRIEF.md]] (discovery +
next slices), [[INTEGRATION.md]] (Explorer tab wiring), `data/README.md` (snapshot
contract).

---

## 1. The vision (as stated)

Move the Heartbeat from a single, admin-only, local instance to a system that is
**shareable and replicable across communities** — each with its own lens,
preferences, and data — that can *optionally* contribute to a shared knowledge
graph.

Stated needs: authentication across instances; per-community preferences and
memory; computation persistence (durable summaries/rankings, historically
searchable); federated search across local instances (with p2p protocols such as
IPFS / ActivityPub floated); privacy and permissions (local data ownership,
selective contribution, encryption in transit, user consent, role-based access); a
shared searchable knowledge graph built from community stars, comments, and
aggregated rankings with months/years of historical depth; and a design that
"assumes ten-thousand instances from the start."

## 2. Assessment

**What is sound and should anchor the design.**
Local-first data ownership, selective contribution, role-based access, computation
persistence, and historical depth all align directly with the C2A2 community model
(self-first articulation, opt-in visibility). These are the right invariants and
should be locked early because they constrain everything downstream.

**What is premature and should be resisted now.**
"Design for ten-thousand instances from the start," IPFS/ActivityPub p2p, and a
live federated-search server are over-engineering against the current state (one
local instance, sample data). Building them now would directly contradict two
prior, deliberate decisions in this project: the Heartbeat tab is **static-first /
GitHub-Pages-safe**, and full security + scalability were **explicitly deferred**
("a question we are putting off, but not without understanding"). The simplicity
rule applies: pick protocols when there are ≥2 real instances that need to
interoperate, not before. Premature choice of IPFS vs ActivityPub is a guess we
would likely pay to undo.

**The reframe that resolves the tension: separate reads from writes.**
Almost everything valuable here is a **read**: digests, summaries, rankings,
historical search. Reads can be served as **static JSON snapshots** — no auth, no
server, Pages-safe — and "federation" can begin as a thin client-side aggregator
over a *registry of snapshot URLs*. Only **writes** (stars, comments, per-user
preference persistence, shared-graph contributions) need auth, consent, and a real
backend. Gating writes — not reads — collapses most of the vision into work that is
buildable now without any of the heavy infrastructure.

**The actual gating dependency is policy, not code.**
The privacy/consent model and permission hierarchy are cheap to *specify* now and
must exist **before any write path or shared-graph contribution ships**. This is
the one piece of the vision worth doing on paper immediately, because it bounds
every later phase.

## 3. Invariants (lock these regardless of phase)

- **Local ownership by default.** A community's sources, preferences, summaries,
  and review history live in its own instance. Nothing leaves without an explicit,
  per-item sharing decision.
- **Reads public/static, writes authenticated.** The public surface is read-only
  static data; mutation requires identity + role + consent.
- **Selective, minimal contribution.** Only stars, public comments/rationale,
  aggregate rankings, and public topic links may enter a shared graph — never
  personal preferences, private notes, or contact data. (Mirrors `AGENTS.md`
  federation model.)
- **Provenance always.** Every shared item carries its source citation and the
  instance/role/policy-version that released it.
- **Append-only where agents are concurrent.** Stable IDs, deterministic text.

## 4. Phased roadmap (simplest viable path to the vision)

> **Reorder, 2026-06-17 (Tom):** the immediate goal is to be *useful to others
> besides the author*, which requires **sign-in and per-user preferences** — even
> before federating. So multi-user-on-a-single-instance is pulled **ahead of** the
> federation MVP. The read-vs-write split (§2) makes this reorder cheap: accounts
> gate only writes; the read surface stays static throughout.

**Phase 0 — Static surface. _(done)_**
Static tab; `data/digest.json` snapshot with embedded fallback; Pages-safe. The
JSON schema in `data/README.md` is, in effect, the first public **read contract**.

**Phase 1 — Durable, regenerated snapshots. _(next slice)_**
Deterministic `export_digest.py` mapping the runtime's `/api/digest` → the
`digest.json` schema (a plain field-map, no model judgment); schedule it; flip
`seed:false`. Add a `registry.json` listing snapshot URLs (initially one: this
instance). This is "computation persistence" + "historical depth" at zero infra
cost — keep dated snapshots, not just the latest.

**Phase 2 — Multi-user on a single instance: sign-in + preferences. _(current focus)_**
Be useful to others. One shared preference **schema** (`data/preferences.schema.json`)
defines each reader's lens: sources, tags, relevance threshold, ranking, digest
cadence, consent boundaries.
- **2a — Client-side preferences _(done, Pages-safe)._** The lens is implemented in
  the browser and stored per-device (localStorage); it filters and ranks the live
  signal list immediately, with no backend. This is what `app.js` does now.
- **2b — Accounts + sync _(applied 2026-06-17)._** Magic-link sign-in via Supabase
  Auth (in the existing `C2A2-wiki` project) persists the *same* schema to a per-user
  `user_preferences` row under row-level security (migration applied; `auth.js`
  wired). The local lens upgrades to a synced lens at sign-in with no UI change, and
  degrades to per-device when the SDK is absent. Remaining: configure Auth redirect
  URLs (see `backend/AUTH_ADR.md`). Consent booleans ship in the schema (default
  false) and still gate every future contribution path before Phase 3.

**Phase 3 — Selective contribution + shared graph. _(after accounts)_**
Stars, public comments with rationale, and aggregate rankings flow to a shared
searchable graph under consent + role-based access. Personal preferences and private
notes never leave the instance by default.

**Phase 4 — Federation, scale & p2p. _(deferred / revisit trigger)_**
Begin as a client-side aggregator over a `registry.json` of instance snapshot URLs
(no server, still Pages-safe) — the honest MVP of "query across instances and
aggregate." Only later: real multi-instance infrastructure, encryption-in-transit
hardening, and any p2p/discovery protocol (IPFS / ActivityPub / other). **Trigger to
revisit:** ≥ a small number (say 3–5) of independently operated real communities
actually running instances and needing to interoperate. "Design for 10k" is
satisfied by keeping the read path static, stateless, and registry-driven — *not* by
building 10k-scale machinery now.

## 5. Scope boundary (what this doc does and does not authorize)

- **Authorizes now:** the documentation above; Phase 1's deterministic exporter +
  registry; Phase 2's client-side aggregator — all static/Pages-safe.
- **Does NOT authorize now:** standing up auth, a write backend, encryption
  infrastructure, or any p2p protocol. Those are Phase 3+ and need an explicit
  go-ahead plus the consent/role spec finalized first.

## 6. Open decisions for Tom

1. **Home of this doc.** It currently lives in the Heartbeat chapter. If it should
   become a canonical numbered Pathway in `/architecture/`, that's an editorial
   act on ground truth — say the word and I'll propose a number and backfill the
   `pathways.md` inventories.
2. **Auth strategy (Phase 3).** OAuth provider vs self-hosted vs federated
   identity — deferred until Phase 3 is actually approached; flagged here so it
   isn't silently assumed.
3. **Registry format (Phase 1/2).** A plain `registry.json` of instance snapshot
   URLs is proposed as the federation substrate; confirm before Phase 2.
