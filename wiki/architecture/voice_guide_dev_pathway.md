---
title: Voice Guide — Development Pathway to the Perceiving, Pathway-Aware Realtime Guide
pathway_id: voice_guide_dev_pathway
status: drafted
created: 2026-07-21
depends_on: [voice_guide_state_bus, fact_inventory, broker]
enables: [perceptive_voice_guide, pathway_navigation, grounded_realtime_dialogue]
---

# Voice Guide — Development Pathway

## The target design state (Tom, 2026-07-21)

A voice system that:

1. **Perceives the visual state from which the call is initiated** — knows the active view,
   what is selected, which filters are on, what dominates the current screen.
2. **Has deep knowledge of every pathway available from each page** — held in a **file
   repository, roughly one file per page-state**, built and maintained by **scheduled agent(s)**
   as a **check-first source of truth**.
3. **Interacts meaningfully with any active, engaged user of the explorer, all in realtime.**

This document reviews what exists, reconciles the target with the existing contract, lays out a
phased pathway, and defines the development workflow to execute it.

> **The design already exists.** `voice_guide_state_bus.md` specifies almost exactly this end
> state. The hard architectural thinking (state bus, stable/volatile line, anti-fabrication,
> colour-is-not-an-identifier, knowledge-dir canonical-source rule, graceful degradation) is
> **done**. What remains is largely **build**, plus one genuine extension of the spec (below).

---

## A. Review — what has been done

Assessed against the three target capabilities. Ground truth = the code + the contract +
`fact_inventory.md`, not session transcripts (the artifacts are the authoritative record).

### Capability 3 — realtime interaction: **DONE (transport-complete)**
Shipped and now on `voice-guide-v2`:
- OpenAI Realtime API over WebRTC, voice-to-voice, native barge-in (`gpt-realtime`, `cedar`).
- Broker-first **keyless** minting (Pathway-00 broker), visitor-key fallback only if over-limit.
- `switch_tab` function tool — the guide opens the shell's own tabs by voice.
- Assistant replies mixed into the Record graph (`addStreamToRecMix`).
- Anti-fabrication language in `instructions()`.
- FAQ v1: `scripts/voice_faq.py` (scan/status/additive-merge) + 102 seeded Q&A.

**Limit:** "meaningful" is capped until Capabilities 1 & 2 land. Today the guide can talk and
open tabs, but cannot reference what the user is looking at, and grounds answers only in a flat
FAQ blob + a hardcoded prompt.

### Capability 1 — perceive the visual state: **NOT BUILT (fully designed)**
- Current reality (contract's own words): the guide has **"zero perception of the page."** Its
  world is two text blobs. Only a *write* path exists (`switch_tab`); there is no *read* path.
- Designed but unbuilt: the **state bus** — `where_am_i()`, `describe_view()`, the view-descriptor
  schema (`selected` / `filters` / `counts` / `legend` / `dominant`), `view_changed` push,
  `supported:false` graceful degradation, and the **colour-is-not-an-identifier** discipline
  (bus speaks semantic labels, never colours; refuse to resolve "the blue region", use `dominant`).

### Capability 2 — pathway knowledge as a check-first file repository: **PROTOTYPE ONLY**
- Exists: the FAQ agent + 102 Q&A.
- Gaps vs the target:
  - **Wrong source of truth.** `voice_faq.py` scans the `var descriptions` map **inside
    `explorer.html`** (`_parse_descriptions`, line ~76), i.e. it rebuilds the four-source drift
    the contract explicitly warns against. The canonical `wiki/voice_guide/knowledge/` directory
    **does not exist yet.**
  - **Wrong granularity.** Output is one flat `voice_guide_faq.json` keyed by ~tab-feature —
    **not per page-state**, and it holds *no pathway/navigation data*.
  - **No navigation index.** `destinations.json`, `find_destination(query)`, `navigate(id)` —
    none exist. ~4,000 Sociogram nodes cannot fit in a prompt; there is no index to search.
  - **No provenance/expiry.** `merge` is additive with no `authored_by`/`authored_at`; entries
    from different models accumulate forever (known flaw).
  - **"Check-first" not enforced.** The guide injects the FAQ as a first-pass source, but has no
    page-state knowledge to check *against*, and no retrieval discipline that fails visibly on
    empty (the Pathway-00 "no attestation" label the text pipeline honours but voice does not).

### Net
| Capability | State | What's missing |
|---|---|---|
| 3 — realtime dialogue | **done** | substance ceiling until 1+2 |
| 1 — perceive visual state | **designed, unbuilt** | the state bus + per-tab descriptors |
| 2 — pathway repo, check-first | **prototype** | knowledge dir, per-state files, destinations index, provenance, check-first retrieval, scheduled maintenance |

---

## The one real extension beyond the contract: "one file per page-state"

The contract's knowledge dir is **per-tab**. Tom's spec says **"roughly one for each page state"** —
and (2026-07-21) Tom confirmed he means a grain **finer than `tab × mode`**. The reconciliation is
delicate, because most "page state" is *volatile* — and the load-bearing rule of the whole system
is **knowledge files must never assert volatile facts** (that rule is the fix for the live
fabrication bug). Finer granularity is exactly where that rule is easiest to violate.

**Reconciliation (the load-bearing decision of this pathway): granularity follows *pathways/
affordances*, not data.**

- A **page-state** is any view whose **set of available pathways/affordances materially differs**.
  This is finer than `tab × mode`: on the Sociogram, `default graph` and `node-selected` are
  *distinct states*, because a selected node exposes new pathways — traverse to a neighbour, jump
  to the node's source file, isolate its tradition — that the default graph does not.
- **Why this is drift-safe:** a state's *pathways and affordances are stable* even when its *data is
  volatile*. The file for `sociogram.node_selected` says "the right panel shows the selected node's
  rendered markdown; you can traverse an edge to a neighbour, open its source, or filter its
  tradition" — all **stable**. The *which* node, *which* neighbours, *how many* — **volatile → bus,
  never the file.** The volatile line holds unchanged; we just cut the *stable* layer more finely.
- **State-explosion guardrail:** one file **per distinct affordance-profile, NOT per
  filter-combination.** Every filter combo on the Sociogram shares one affordance profile → one
  file. A file is warranted only when the *navigable options change*. Expect a handful of states
  per tab (default / selected / sub-view), bounded — not combinatorial.
- Each file holds only **stable** content: purpose, **pathways out** (state-specific), affordances,
  `answerable_questions`, the **`must_not_claim`** list, and colour *semantics* (label→meaning,
  never "blue = X").
- **Volatile sub-state** (active filters, current selection, live counts, what dominates) is
  **assembled at runtime from the bus**, overlaid on the stable file.

So "the page state the guide knows" = **stable affordance-state file ⊕ live bus descriptor.** The
bus's `describe_view` must therefore return a **page-state key** granular enough to select the right
file (e.g. `sociogram.graph.node_selected` vs `sociogram.graph.default`) — derivable from
`(tab, view, hasSelection, …)`. This satisfies Tom's finer-than-tab intent, captures pathways
(which are inherently state-dependent) far better than per-tab files, and keeps the fabrication
hole shut.

---

## B. Development pathway (phased, with exit criteria)

Phase 0 is done. Each later phase has a hard exit criterion (Rule 4) and proves on the Sociogram
first before fan-out (contract step 3: "prove the loop before scaling").

### Phase 0 — Foundation *(DONE)*
Realtime loop, `switch_tab`, anti-fabrication, the contract, FAQ v1. On `voice-guide-v2`.

### Phase 1 — Ground-truth substrate: knowledge repository + page-state model
- Enumerate the page-state taxonomy by **distinct affordance-profile** (default / selected /
  sub-view per tab), not by tab and not by filter-combination — see the reconciliation above.
  The bus's `describe_view` must emit a page-state **key** at this grain.
- Create `wiki/voice_guide/knowledge/`: `00_project.md` + one file per page-state, with the
  frontmatter + `must_not_claim` + `pathways_out` fields.
- **Migrate `explorer.html`'s `descriptions` map into `knowledge/`** and add a build step that
  **derives** the explorer help text from `knowledge/` (canonical-source rule → kills the drift
  class at its root).
- Repoint `voice_faq.py` to scan `knowledge/`, not `explorer.html`.
- **Exit:** `knowledge/` is the sole source; explorer help + FAQ both derive from it; a janitor
  drift detector asserts no divergence and flags any page-state lacking a file.

### Phase 2 — Perception: the state bus, Sociogram end-to-end
- Shell (`explorer.html`): `where_am_i()` (shell-only, always available), `describe_view()`
  (postMessage query to active tab), `supported:false` graceful degradation. Register both as
  realtime tools.
- Sociogram tab (via `generate_visualization.py`): answer `describe_view` with the descriptor
  (`selected`/`filters`/`counts`/`legend`/`dominant`), push `view_changed` on tab switch
  (pull-on-demand per the contract's open question).
- Anti-fabrication behaviour: refuse colour→category resolution; use `dominant` for "the big cluster".
- **Exit:** live guide truthfully answers "what am I looking at / what's selected / what's the big
  cluster"; a non-bus tab yields "I can't see that view" (never improvises). Probe test enforces it.

### Phase 3 — Pathways: destinations index + navigate
- Build `destinations.json`: the **navigation graph** — from each page-state, every pathway out
  (tab→tab, and within-tab focus/isolate/search/select targets). This IS "deep knowledge of every
  pathway available from each page."
- `find_destination(query)`: index-backed semantic search over destinations + the ~4,000 nodes.
- `navigate(id)`: bus `command` verb driving the tab's own focus/isolate/search.
- **Exit:** "take me to X" resolves and drives the tab; "how do I get to Y from here" is answered
  from the index, not improvised.

### Phase 4 — Scheduled maintenance + check-first discipline
- Extend/split the weekly agent(s) into a maintenance layer: (a) **knowledge refresh** (re-derive
  `must_not_claim`/`answerable` when a view changes — hooks the `voice_faq scan` diff), (b)
  **destinations rebuild** (re-crawl pathways when routes change), (c) **FAQ deepen** (existing).
  Add **provenance/expiry** (`authored_by`/`authored_at`) — fixes the known flaw.
- **Check-first retrieval:** guide instructions + retrieval order = consult `knowledge/` +
  `destinations` **before** answering; empty retrieval → visible "no attestation" (Pathway-00).
- **Exit:** agents run on schedule, keep the repo fresh, drift detectors green, provenance stamped;
  the guide demonstrably checks-first (refuses to improvise when knowledge is absent).

### Phase 5 — Robustness: all tabs + verification harness
- Bus implemented for **every** tab (each returns a descriptor or `supported:false`).
- Verification harness: bus-contract conformance per tab, knowledge-coverage per page-state,
  destinations reachability, scripted anti-fabrication probes.
- **Exit:** every page-state has knowledge + bus + pathways; a test suite gates regressions; live
  end-to-end demo across all tabs.

### Cross-cutting constraints (every phase)
- **No-Blind-Push:** local HTTP review of `explorer.html` before any push.
- **Iframe-asset rule:** bus code is **inlined** in each tab (never a bare external `src=`).
- **fact_inventory hazards:** the canonical-source rule prevents a new drift source; add detectors.
- **Stable/volatile line:** knowledge never asserts volatile facts.
- **Palette 🔒 reserved to Tom:** the bus speaks semantic labels, never colours; the two-channel
  (shape × colour) encoding is Tom's call — a *constraint on consolidation*, not a task to build.

---

## C. Development workflow (the process)

### Increment unit
**One page-state, driven through the full stack** (knowledge file → bus descriptor → pathways →
verify), Sociogram first, then fan-out. Never build a layer horizontally across all tabs before
one vertical slice is proven end-to-end.

### Per-increment gate (Rule 4 success criteria + Rule 9 tests)
1. **Knowledge file** authored to the stable/volatile line, with a `must_not_claim` list.
2. **Bus descriptor** implemented + **conformance test** (schema-valid; asserts no volatile fact
   leaked into the knowledge file).
3. **Anti-fabrication probe** — scripted questions that MUST elicit "I can't see" / "which do you
   mean" / a grounded `dominant` answer. The test fails if the guide improvises. (This is the Rule-9
   test: it encodes *why* — fidelity — not just *what*.)
4. **Local HTTP live check** (No-Blind-Push) → Tom sign-off → push.

### Self-policing (Rule 5: code answers, not the model)
Extend the janitor with detectors: knowledge↔explorer-help divergence, knowledge-coverage gaps,
destinations reachability, FAQ provenance presence. The source-of-truth polices itself weekly.

### Scheduled agents (Phase 4)
The maintenance layer is **report-only / human-review-before-publish** (LLM-authored data → never
auto-push, per the no-blind-push carve-out logic).

### Where multi-agent fan-out helps (opt-in)
Two phases parallelize cleanly and are candidates for an orchestrated run:
- **Phase 1 authoring:** one agent per page-state, each grounded in the actual tab, drafting its
  knowledge file + `must_not_claim` to a shared schema.
- **Phase 5 conformance:** one agent per tab verifying bus-descriptor conformance + anti-fabrication
  probes in parallel.
Everything else stays a human-in-the-loop vertical increment.

### Handoff discipline
Update `handoffs/voice-guide.md` at each increment (branch, what shipped + commit, resume cue,
next scope, parked items).

---

## Immediate next step (proposed)
**Phase 1, increment 1 — the Sociogram affordance-states.** Stand up `wiki/voice_guide/knowledge/`
with `00_project.md` + the Sociogram's distinct affordance-states (at minimum
`sociogram.graph.default` and `sociogram.graph.node_selected`; add `sociogram.narration` if its
pathways differ), migrate their help text out of `explorer.html`, add the derive-help build step,
repoint `voice_faq.py`, and add the coverage/divergence detector. That single slice proves the
canonical-source rule AND the affordance-state grain before any bus code is written — and it is the
lowest-risk, highest-leverage first move (it removes a live drift source rather than adding surface).
