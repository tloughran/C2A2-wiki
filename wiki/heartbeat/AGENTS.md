# C2A2 Heartbeat Wiki Maintainer Schema

This directory is the Community AI Education heartbeat chapter for the C2A2 Explorer.
Treat it as a Karpathy-style LLM wiki surface:

1. Raw sources are immutable inputs.
2. The compiled wiki is markdown maintained by agents and reviewed by humans.
3. This schema defines conventions, write boundaries, and update workflows.

## Layer Model

- `raw/` - source snapshots, RSS exports, papers, meeting notes, transcripts, and operator notes. Do not rewrite source files after ingest.
- `wiki/` - compiled markdown pages: source notes, topic pages, community lens pages, decision records, contradiction logs, and indexes.
- `index.html`, `styles.css`, `app.js` - public GitHub Pages-safe shell for the Explorer tab.
- `INTEGRATION_BRIEF.md` - discovery notes, latest reference paths, and next implementation sequence.
- `ARCHITECTURE.md` - the multi-community target vision, its critical assessment, and the phased roadmap (read-vs-write split; federation as a registry of static snapshots before any p2p). Consult before proposing infra changes; it defines the scope boundary for what may be built now.
- `AGENTS.md` - this schema. Update it when conventions change.

## Page Types

- Source note: one page per source item or digest run, with citations and source metadata.
- Topic page: synthesis across many source notes.
- Community lens page: how one community filters, ranks, and interprets signals.
- Decision record: an operator or governance decision with rationale and provenance.
- Contradiction log: tensions, disagreements, stale claims, and unresolved questions.
- Index page: navigation and current status.

## Ingest Workflow

1. Read the raw source or digest export.
2. Create or update the relevant source note.
3. Search existing wiki pages before writing new claims.
4. Update topic pages, community lens pages, and contradiction logs as needed.
5. Preserve citations and provenance.
6. Append a dated note to the log or index.
7. Update the static Explorer shell only when public-facing structure changes.

## Safety Rules

- Never invent source claims.
- Mark inferred summaries separately from community-claimed interpretations.
- Do not publish private user preferences, personal data, or community-private notes.
- Keep public exports narrow: stars, comments, aggregate rankings, and citations only when consent allows.
- Prefer append-only logs for concurrent agent work.
- Use deterministic text and stable IDs where possible.

## Federation Model

Each community instance owns its local data. Shared graph contribution should be explicit,
permissioned, and minimal:

- allowed: high-value source stars, public comments/rationale, aggregate rank signals, public topic links
- not allowed by default: personal preferences, private notes, contact data, nonpublic community deliberation

## Static Shell Contract

The tab must work from GitHub Pages without a live API. Live Heartbeat data can be added by
publishing a static JSON snapshot or by routing through an authenticated backend later.
