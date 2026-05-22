---
title: Perspective Lattice
pathway_id: perspective_lattice
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue]
enables: [unsaid_edges, prepared_presentation, apprentice_mode, recursive_episode]
isme_critical: no
---

# Pathway 04: Perspective Lattice

## Purpose

This is the system's bite-size-overview engine: a structured way to ask for and receive a quick, fidelity-preserving summary at almost any granularity — one thinker, one T-T relationship, one PRS triplet, one problem, one resource, one solution, one Summa article — viewed from any of the eleven thinker-perspectives or from the whole-system perspective.

The pathway exists because the dialogue layer (Pathway 01) needs fast access to coherent overviews. Without precomputed structure, every "give me a quick read on X from Y's perspective" question would re-summarize from scratch, with variable fidelity. With this lattice, the most common questions are answered in milliseconds from pre-baked content; the less common ones are generated lazily and cached; only the most peripheral are improvised fresh.

## Function set

The lattice is organized along several axes:

1. **Granularity axis:** thinker, T-T pair, central topic, PRS triplet, resource, problem, solution, R→S move, problem-goal-constitution, Summa part (I / I-II / II-II / III), Summa question, Summa article — in both the transcripted-in-a-year version and the contemporary-commentary version.

2. **Perspective axis:** twelve vantage points. The eleven thinker-perspectives (Levin, Friston, Hoffman, Hawkins, McGilchrist, Fredrickson, Stump, Carroll, Arkani-Hamed, Wolfram, Kastrup) plus the whole-system perspective.

3. **Computation tier:** every overview is one of three:
   - *Eager:* pre-built ahead of time, cached on disk, served in <100 ms.
   - *Lazy:* generated on first request, cached for the session or persisted to the vault.
   - *Fresh:* computed every request, never cached, used for question-specific answers.

## The tiering decision

The combinatorics force the tiering. 12 perspectives × 1647 vault nodes is already ~20K overview cells; add 55 pairwise T-T relationships, ~77 PRS triplets, and Summa with ~512 questions × multiple articles × 2 versions, and the lattice exceeds 50K cells. Pre-building all of them would consume budget and storage for content most users will never request.

The tier assignment (strawman, to be refined):

| Tier | What's pre-built |
|------|------------------|
| **Eager** | Per-thinker pages (11). Central T-T relationships (~15–20). PRS triplets (~77). Summa part-level summaries (4 parts × 2 versions = 8). Summa question-level summaries for high-traffic questions. |
| **Lazy** | Article-level Summa entries. Peripheral T-T pairs. Per-resource / per-problem / per-solution overviews. Goal-constitution descriptions for individual problems. R→S move descriptions. |
| **Fresh** | Specific question answers (the actual user-asked question). Cross-references that haven't been materialized. Any overview where the user's framing differs meaningfully from the cached one. |

## Architecture sketch

```
agentic anticipation pipeline (runs offline / scheduled)
        ↓
    eager-tier content
    ├─ per-thinker pages
    ├─ central T-T relationships
    ├─ PRS triplets
    └─ Summa part / question summaries
        ↓
   stored in vault, served from cache

runtime request:
   dialogue_layer asks for overview(granularity, target, perspective)
        ↓
   lattice service
   ├─ hit eager cache? → return
   ├─ hit lazy cache? → return
   ├─ generate lazy? → generate, cache, return
   └─ fresh generation → generate, return (no cache)
        ↓
   provenance footer attached to every overview
```

## Decisions taken

- **Three-tier precompute strategy.** Not "precompute everything" (storage and time explosion) and not "improvise everything" (latency and fidelity loss). Tiering keeps the demo responsive while keeping fidelity high.

- **Fidelity via provenance.** Every overview carries a footer naming the actual vault nodes and passage excerpts it drew from. Empty provenance → "no direct vault attestation" label rather than silent confabulation. Same discipline as Pathway 01.

- **Eager content is itself vault content.** Pre-built overviews live in the vault as their own markdown nodes, with the tradition / structure-group tagging that lets them appear in the Sociogram. The lattice doesn't sit outside the vault; it's a layer within it.

- **Edges are first-class.** T-T relationship overviews (the connecting tissue between two thinkers) get their own pages, not just attribute tags on existing thinker pages. Pathway 02 already biases edges; Pathway 07 will surface the empty ones.

- **Lazy cache scoped per session, then promoted.** A lazy overview generated for one visitor is useful for the next, so cached generations persist beyond the originating session (subject to invalidation when the underlying vault content changes).

- **Eager-tier content lives in the vault** at `wiki/Perspectives/` (decided 2026-05-13). Each cell is its own markdown node with a Perspectives structure-group tag. This makes overviews first-class wiki citizens, discoverable through the Sociogram and retrievable by the voice agent — including the agent answering questions *about* the lattice itself.

## Open questions

- **Invalidation.** When a vault node changes, which overviews need regenerating? Naive answer: any overview that cited it. Requires tracking citations per overview — straightforward if we lean on the provenance footer.

- **Generation budget.** Eager-tier pre-build is non-trivial compute. Probably a daily scheduled task (piggybacking on the existing 8 AM wiki agent) that regenerates stale cells.

- **Perspective uniformity.** Should every cell be viewable from every perspective, or do some combinations not make sense (e.g., "Summa II-II Q.47 from Levin's perspective" may have no vault attestation)? Probably some combinations should return "no perspective attestation in vault" rather than forced inference.

## Edges

- **broker (00):** lattice service runs broker-side; retrieval index serves the lazy and fresh tiers.
- **voice_dialogue (01):** dialogue layer is the primary consumer; "give me a quick read on X from Y's perspective" hits the lattice.
- **unsaid_edges (07):** unsaid-edges map is a direct dual of the lattice — every cell with no attestation is candidate research-program territory.
- **prepared_presentation (08):** prepared canon draws on eager-tier overviews for fast access during the live demo.
- **apprentice_mode (15):** the apprentice curriculum walks newcomers through the lattice in a structured order, surfacing the tradition's shape progressively.
- **recursive_episode (11):** generated overviews can become podcast episodes; the episode then re-enters the vault, enriching the lattice.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- This pathway emerged from Tom's enumeration of granularities he'd want quickly: "one for each thinker (T), each T-T relationship, each central topic, each PRS, each resource (R) and the range of problems (P) it drives or promises to drive to solution (S); how each Problem is goal-constituted." The tiering decision (eager / lazy / fresh) crystallized when the combinatorics were spelled out — 12 perspectives × 1647 nodes already pushes 20K cells before Summa enters.

## Status

Drafted in prose. Implementation begins with (a) defining the cell schema for the lattice, (b) writing the eager-tier generator (an agent that produces per-thinker, central T-T, and PRS overviews), (c) building the lattice service that routes runtime requests to the right tier. The daily 8 AM scheduled task could absorb the eager-regeneration job.
