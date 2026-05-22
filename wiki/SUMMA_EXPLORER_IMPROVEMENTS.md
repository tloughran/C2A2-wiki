# Summa Explorer — Planned Improvements

*Captured: 2026-05-12*
*Companion docs: `EXPLORER_V2.md` (branch-scoped implementation notes), `EXPLORER_VISION.md` (system-level vision).*
*Scope: improvements specific to `wiki/summa_explorer.html`.*

---

## Why these two improvements ride together

The Sociogram tab inside the Summa Explorer is presently a Phase 3 placeholder (subtab `subtab-sociogram`, labelled "Sociogram — Phase 3" — see `summa_explorer.html` ~lines 383–410, 1148–1180). Standing up the Sociogram tab needs a real link graph behind it, and that graph needs to stay fresh as agents and humans add new content. Hence two staged improvements: **(1)** a continuous Linker Agent that produces the graph, and **(2)** a Sociogram tab inside the Summa Explorer that renders it. Improvement 2 depends on Improvement 1.

---

## Improvement 1 — Vault Linker Agent

### Purpose

Resolve every cross-file reference in the vault into a structured link record. The link records are the data substrate that the new Sociogram tab consumes, and they also support other agents and tooling (validated_premises checking, cross_program_index, etc.). The agent prowls **regularly and endlessly, insofar as any agents are active** — quiet when the vault is at rest, busy whenever any other agent is writing.

### Reference kinds to resolve

| Kind | Examples in source text | Link target |
|------|-------------------------|-------------|
| `wikilink` | `[[Aquinas]]`, `[[Day 7]]`, `[[Levin-tradition wiki]]` | exact-name match against vault index |
| `summa-day` | "Day 7", "Day-007", "the beatific vision Day" (title match) | `vault/synthesis/Day-NNN - … - Contemporary.md` |
| `summa-question` | "Q.87", "q. 87 a. 3", "I.q.2.a.3", "ST I-II q. 49" | `vault/refs/summa_index.json` part/question/article anchor |
| `thinker-mention` | "Levin", "Friston", "Hoffman", surname tokens for the 15 traditions | `traditions/<thinker>/wiki.md` |
| `prs-ref` | "PRS-04 in the Kastrup-tradition wiki", "PRS-01 (Hoffman)" | `traditions/<thinker>/prs_triplets.md` § anchor |
| `scripture` | "Romans 1:20", "John 1:1", "Gen 1" | `vault/refs/scripture_index.json` (new, may be auto-created from Wright synthesis text) |
| `cross` | CROSS-NNN identifiers ("CROSS-001"), FLAG-NNN | `master/cross_program_index.md`, `flags/*.md` |
| `external` | DOI / arxiv / URL | the URL itself; recorded but not embedded |

Each kind has a recogniser. The agent runs every recogniser against every changed file.

### Output data model

A single canonical store: **`vault/refs/cross_links.json`**. Schema:

```json
{
  "_meta": {
    "generated": "2026-05-12T19:14:02Z",
    "linker_version": "1.0",
    "files_scanned": 1647,
    "files_with_links": 1183,
    "total_links": 14_392
  },
  "files": {
    "vault/synthesis/Day-045 - Self-Understanding - Contemporary.md": {
      "mtime": 1747084000,
      "content_sha1": "ab12...",
      "links": [
        {
          "kind": "thinker-mention",
          "match_text": "Hoffman",
          "line": 17,
          "char_offset": 412,
          "target": "traditions/hoffman/wiki.md",
          "target_anchor": null,
          "confidence": 1.0
        },
        {
          "kind": "prs-ref",
          "match_text": "PRS-01 Kastrup-tradition wiki",
          "line": 17,
          "char_offset": 1880,
          "target": "traditions/kastrup/prs_triplets.md",
          "target_anchor": "PRS-01",
          "confidence": 0.95
        },
        {
          "kind": "summa-question",
          "match_text": "Q.87",
          "line": 9,
          "char_offset": 220,
          "target": "vault/refs/summa_index.json#STI/Q.87",
          "confidence": 1.0
        }
      ]
    }
  },
  "by_target": {
    "traditions/hoffman/wiki.md": [
      {"source": "vault/synthesis/Day-045 - …", "kind": "thinker-mention", "count": 5}
    ]
  }
}
```

The `by_target` index is the lookup the Sociogram tab needs to render edges; the per-file `links` block is what an authoring agent or human reader uses to inspect a single file's outgoing references.

### Agent behaviour

- **File watcher**: poll mode by default (60-second interval) plus an opportunistic mtime sweep at the top of each cycle. On macOS, an upgrade to FSEvents-backed watch is straightforward later.
- **Activity-gated**: the agent reads `master/incoming_dispatches.md` and `architecture/daily_sync/` to detect whether any other agent has run in the last N minutes. If yes, the linker stays in fast-poll mode; if no, it slows to a longer interval (e.g., 10 minutes) or sleeps until the next activity signal.
- **Idempotent and content-hashed**: each file's record stores `mtime` and `content_sha1`. The linker re-scans a file only if either has changed.
- **Write-safe**: never edits source files. Only writes `cross_links.json` (and any new index sidecars it produces, like `scripture_index.json`).
- **Atomic writes**: writes to `cross_links.json.tmp` then renames, so consumers never read a half-written file.
- **Conflict-resilient with the QC agent**: if Tom's `Summa.md`-driven QC agent is writing a synthesis at the moment the linker tries to re-scan it, the linker defers the scan one cycle.
- **Logs to `architecture/changelog/linker_NNNN-NN-NN.md`**: appends a one-line summary each run (files scanned, files updated, links added/removed).

### Recogniser implementation notes

The hardest recogniser is **`summa-question`**. Patterns include:
- `Q.87`, `Q. 87`, `q. 87`
- `q.87 a.3`, `Q.87 art. 3`
- `I.q.2.a.3`, `II-II.q.50.a.4` (part-question-article)
- `Question 87`, `Article 3 of Question 87`
- prose: "Aquinas's question on the soul" → matched against `summa_index.json` titles

Recommend a two-pass approach: regex for the explicit citation forms, plus a fuzzy title-match pass against the `summa_index.json` titles for the prose forms. Title-match confidence < 0.8 yields a candidate the agent flags but does not emit as a hard link.

The **`thinker-mention`** recogniser must avoid noise. Reuse the same registry already curated in `wiki/commentary-explorer/scripts/build_bundle.py` (the `THINKERS` list, plus `EXTRA_THINKER_KEYS` for historical figures and `GENERIC_TITLE_BLOCKLIST` for collisions like "Will", "Truth", "Genesis"). That registry is project-tested and should be promoted into a shared `wiki/tools/recognisers/thinker_registry.json` so both this agent and `commentary-explorer/build_bundle.py` consume it.

### File location

- Script: `wiki/agents/linker_agent.py` (alongside existing agent scripts in `wiki/agents/`)
- Launch: invoked by scheduled-tasks (matching the pattern used by `c2a2-wiki-agent-daily-run` — see memory note on its frozen ID; this one is new and free to be named cleanly, e.g., `vault-linker-continuous`).
- Run modes:
  - `--watch` (default, continuous)
  - `--once` (single sweep, useful for CI / before a wiki publish)
  - `--file PATH` (re-scan a single file, e.g., immediately after another agent writes)

### Acceptance criteria

1. `cross_links.json` produced and parseable on first run against the current vault (~1,647 files).
2. Re-run with no changes performs zero writes and exits cleanly.
3. Modifying a single file (e.g., today's synthesis) re-scans only that file and updates the global index incrementally — no full re-scan required.
4. The Sociogram tab loads `cross_links.json` in under 200 ms on first paint.
5. Linker run-time on a clean machine: under 60 seconds for the full vault.

---

## Improvement 2 — Sociogram Tab inside the Summa Explorer

Depends on Improvement 1.

### Where it lives

Already scaffolded as `subtab-sociogram` in `wiki/summa_explorer.html`, sibling of `subtab-contents`. Currently a Phase 3 placeholder. This improvement replaces the placeholder with a working force-directed graph view of the Summa and all its references.

### Visualisation scheme

**Same as the main C2A2 Sociogram** (`wiki_narration.html`):
- D3 v7 force-directed layout
- Dark theme (`#0a0a0f` background)
- Click a node → file body rendered in the existing right panel
- Hover → node label visible
- Drag to reposition; scroll/pinch to zoom
- Hold-forces / fit / labels toggles in the top-right of the graph area

The Sociogram tab inside the Summa Explorer shares the host page's right panel — clicking a node loads the corresponding file's contents into the same reader pane the Contents tab uses. No separate viewer.

### Filter checkboxes

Filter row across the top of the graph area, with these toggles:

| Toggle | Default | Node kind |
|--------|---------|-----------|
| **All** | — | meta-toggle: turn every kind on |
| **None** | — | meta-toggle: turn every kind off |
| **Parts** | ✅ on | 5 nodes — STI, STI-II, STII-II, STIII, Supplement |
| **Questions** | ✅ on | ~600 nodes — one per ST question |
| **Articles** | off | thousands — individual articles a.1, a.2, … (heavy; off by default) |
| **Thinkers** | off | 15 nodes — one per tradition |
| **PRS** | off | per-PRS-triplet nodes |
| **References** | off | scripture / external / cross-program references |
| **Other** | off | catch-all for kinds not yet categorised |

Parts and Questions on by default give a usable opening shot of the Summa's spine; the user adds layers from there.

### Node colours

Reuse the existing CLAUDE.md palette:
- Parts: gold `#C9A84C` (Master color — fits the Summa-as-canon framing)
- Questions: a slightly cooler gold `#B89A40`
- Articles: muted gold `#9A8338`
- Thinkers: per-tradition colours from the existing palette (Levin `#C45B5B`, Friston `#5A8EAF`, Hoffman `#C08B3E`, etc.)
- PRS: lighter tint of the parent thinker's colour
- References: `#5B7FA5` (Architecture blue)
- Other: `#6E6E7E` (muted grey)

### Data flow

1. Tab activates → fetch (or read from already-loaded global) `vault/refs/summa_index.json` and `vault/refs/cross_links.json`.
2. Build node list from `summa_index.json` (parts/questions/articles) + the union of distinct targets in `cross_links.json` (thinkers, PRS, references).
3. Build edge list from `cross_links.json.by_target` — one edge per (source-file, target-node) pair, weighted by occurrence count.
4. Apply filter state → hide nodes whose kind is off; hide edges where either endpoint is hidden.
5. Run D3 force simulation; render.
6. Click → load file body into the host page's right panel (same plumbing as the Contents tab).

### Edge weighting

Edge thickness ∝ `log(1 + count)` of how many times the source file references the target. Cap at a visual max of ~5 px to keep the graph legible.

### Performance budget

Worst case (all toggles on): ~3,000 nodes (parts + questions + articles + thinkers + PRS + references), edges in the low five-figures. D3 force handles this — but only if articles are off-by-default as planned. With Parts + Questions only, expect ~600 nodes and ~2,000–5,000 edges; comfortable.

Caching: parse `cross_links.json` once on tab activation, retain in a tab-scoped JS variable. Re-fetch only when the linker writes a newer file (server-modtime check; trivial because we serve via `python3 -m http.server`).

### Acceptance criteria

1. Sociogram tab loads and renders within 1 second of click.
2. All filter checkboxes work; "All" and "None" meta-toggles set every individual box correctly.
3. Click a question node → right panel renders that question's article(s) from the synthesis file, same as the Contents tab.
4. Click a thinker node → right panel renders `traditions/<thinker>/wiki.md`.
5. Click a PRS node → right panel renders the corresponding section of `traditions/<thinker>/prs_triplets.md`.
6. Tab state and filter state persist across tab-switches within a session (localStorage acceptable per the existing summa_explorer pattern; not required to persist across reloads).

---

## Suggested implementation sessions

**Session A — Linker Agent v1, recognisers and writer (~3–4 hours):**
Stand up `wiki/agents/linker_agent.py`. Implement the wikilink, thinker-mention, summa-day, prs-ref, and summa-question recognisers. Emit `cross_links.json`. Test against the present vault (1,647 files). Ship `--once` and `--watch` modes. Promote the shared thinker registry to `wiki/tools/recognisers/thinker_registry.json`.

**Session B — Sociogram tab v1 (~3 hours):**
Replace the Phase 3 placeholder in `summa_explorer.html` with the working tab. Implement the filter row, the D3 force graph, and the click→right-panel plumbing. Verify acceptance criteria 1–6.

**Session C — Polish and edge cases (~2 hours):**
- Scripture recogniser (Improvement 1's longer tail).
- Tab-state persistence in localStorage.
- A small "Refresh links" button in the Sociogram tab that triggers `linker_agent.py --once` and reloads when done (only useful when the explorer is served over HTTP, not file://).

---

## Constraints honoured

- **No external wiki dependency at runtime** — `cross_links.json` is part of the same repo as `summa_explorer.html`; no remote fetches needed.
- **Local-machine-only execution** — the linker is a Python script invoked locally or via scheduled-tasks; the Sociogram tab reads only same-origin JSON.
- **Pre-push visual review (CLAUDE.md constitutional rule)** — applies as usual: serve `summa_explorer.html` from a local HTTP server, verify both tabs, then push.

---

## Open questions to resolve before Session A starts

1. **Does the linker also write per-file sidecars** (e.g., `Day-045 - … - Contemporary.links.json`) for use by other agents, or only the central `cross_links.json`? Sidecars are convenient for per-file ops but proliferate file count. Recommend central-only for v1.
2. **Scripture index** — does it get built from Wright synthesis files alone, or from any file? Recommend: any file, but flagged by source. Wright's contributions get higher confidence.
3. **Article-level Summa anchors** — does `summa_index.json` already carry article-level structure, or only question-level? Need to inspect; if only questions, the Articles toggle in Improvement 2 will need either a deeper index or a graceful degradation message.
4. **Scheduled-tasks integration** — does the existing `c2a2-wiki-agent-daily-run` scheduler model support a continuous-watch agent, or does this need a separate launchd plist? (Memory note: don't propagate the "c282" typo to the new task ID.)
