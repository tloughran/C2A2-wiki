---
title: Voice Guide — State Bus & Knowledge Contract
pathway_id: voice_guide_state_bus
status: drafted
created: 2026-07-19
depends_on: [broker]
enables: [voice_dialogue, grounded_interface_answers, whole_system_navigation]
isme_critical: yes
---

# Voice Guide: State Bus & Knowledge Contract

## Why this exists

The realtime voice guide currently has **zero perception of the page**. Its whole world is
two text blobs (a hardcoded prompt + the FAQ). Asked "what is the large blue region?", it has
no data — and realtime models answer rather than admit ignorance. It fabricates.

This violates the project's own fidelity discipline. Pathway 00 says empty retrieval must
produce a visible "no direct vault attestation" label **rather than free improvisation**. The
text pipeline honors that; the voice guide does not. Fixing that is the point of this contract.

## The core principle: stable vs volatile

> **Knowledge files describe MEANING. The bus reports STATE. Neither may do the other's job.**

This is the load-bearing decision. Everything else follows from it.

- **Stable / semantic** → lives in `knowledge/` markdown, authored by a human, deepened by the
  weekly FAQ agent. *What a tab is for. What blue MEANS (the Friston tradition). What kinds of
  question this view can answer.*
- **Volatile / live** → comes from the bus at request time, never from prose. *Node counts,
  active filters, what is selected, which categories dominate the current view.*

**Knowledge files are FORBIDDEN from asserting volatile facts.** This is not style — it is the
fix for a live bug: the seeded FAQ says the Sociogram has "over sixteen hundred" nodes, the tab
help says 1,600+, CLAUDE.md says 2,638, and the live counter reads 3,992. Stale prose stated as
current fact is fabrication by another route.

## Protocol (shell ↔ tab, postMessage)

The shell (`explorer.html`) owns the guide; each tab is an iframe document. Two directions:

**Query** — shell asks the active tab:
```js
{ source: 'c2a2-voice', type: 'describe_view', requestId: '<uuid>' }
```
**Response** — tab replies:
```js
{ source: 'c2a2-tab', type: 'view_descriptor', requestId: '<uuid>', payload: { /* see below */ } }
```
**Push** — tab volunteers a change (debounced ≥250ms), so the guide is not stale mid-conversation:
```js
{ source: 'c2a2-tab', type: 'view_changed', payload: { /* same shape */ } }
```
**Command** — shell drives the tab:
```js
{ source: 'c2a2-voice', type: 'command', verb: 'focus', args: {...}, requestId }
→ { source: 'c2a2-tab', type: 'command_result', requestId, ok: true, detail: '...' }
```

## View descriptor schema

```jsonc
{
  "tab": "wiki_narration.html",
  "title": "Sociogram",
  "view": "graph",                    // subview/mode, if the tab has one
  "supported": true,                  // false => tab has not implemented the bus
  "state": {
    "selected": { "id": "...", "label": "...", "kind": "node" },   // or null
    "filters":  { "traditions": ["Friston"], "structure": ["Master"] },
    "counts":   { "visibleNodes": 3992, "totalNodes": 3992,
                  "visibleEdges": 2500, "totalEdges": 107856 },
    "legend":   [ { "label": "Friston", "color": "#5A8EAF", "role": "tradition" } ],
    "dominant": [ { "label": "Friston", "color": "#5A8EAF", "share": 0.31 } ]
  },
  "capabilities": ["focus", "isolate", "search", "select_node"]
}
```

`dominant` answers *"what is the big cluster?"* **truthfully** — share of currently-visible nodes
per category, computed by the tab that actually knows. This is why grounded state beats vision: a
screenshot would make a model *guess*; the app knows the category and its share.

### Color is NOT an identifier (added 2026-07-20 — learned the hard way)

The first draft of this document used "the app knows blue is Friston" as its worked example.
**That was itself a fabrication**, and it was wrong: the blue region the user was actually looking
at was **Architecture**, not Friston. Measured CIE76 distance between those two swatches is
**ΔE 7.7 — the closest pair in the entire palette.** Eight pairs fall under ΔE 15:

| Pair | ΔE |
|---|---|
| Friston `#5A8EAF` / Architecture `#5B7FA5` | 7.7 |
| Hoffman `#C08B3E` / Hawkins `#B87D3E` | 8.0 |
| Stump `#A8923A` / Master `#C9A84C` | 10.3 |
| Kastrup `#8B5DAB` / Agents `#8B6DAE` | 10.4 |
| McGilchrist `#3D9E89` / Loughran `#4A8A7A` | 10.9 |
| Wright `#5A72A8` / Architecture `#5B7FA5` | 11.8 |

Root cause: **two orthogonal taxonomies (thinker tradition, structure group) are encoded on one
visual channel**, forcing 17 categories onto a single hue scale. Kastrup/Agents shows the collision
crossing taxonomies — a colour can name a thinker *or* a structure group.

Consequences for this contract:

1. **The bus speaks in semantic labels, never colours.** `dominant` and `selected` return category
   names; `color` is decoration for the UI, not an identifier. Never key logic on it.
2. **The guide must refuse to resolve a colour to a category.** Correct behaviour when a user says
   "the big blue region": name the categories that share that colour and ask which they mean —
   *then* use `dominant` to say which is actually largest on screen right now.
3. **A voice interface imposes a requirement the mouse never did: the encoding must be
   *speakable*.** "The blue one" must be unambiguous out loud. Today it is not.

### Recommended fix — 🔒 DECISION RESERVED TO TOM (2026-07-20)

**No agent should choose the visual vocabulary.** Tom has explicitly reserved the shape/colour
language for himself; this is a design call about how the system *reads*, not an implementation
detail. Treat what follows as a **constraint on consolidation**, not a spec to build.

Split the two taxonomies onto **two visual channels** — e.g. shape for one, colour for the other —
giving a two-parameter read-out per node. This cuts the required hue count dramatically, makes
each node verbally addressable ("the blue squares"), and survives colour-vision deficiency, which
a 17-hue single-channel scheme does not.

**Therefore: do NOT consolidate the current palette into a canonical file as-is.** Freezing it
would canonise an artifact of construction haste. Separate **identity** (the taxonomy: which
traditions and structure groups exist, `has_satellite`, etc. — stable) from **encoding** (how a
category maps to colour/shape — a revisable policy). Same stable/volatile discipline as the rest
of this contract, applied one level up.

## Graceful degradation (non-negotiable)

A tab that has not implemented the bus returns `{ supported: false }`. The guide must then say
it cannot see that view — **never** improvise. Partial adoption must never reopen the
fabrication hole.

## Tool surface exposed to the model

| Tool | Source | Notes |
|---|---|---|
| `where_am_i()` | shell only | Always available — the shell knows the active tab without tab cooperation. |
| `describe_view()` | bus | Returns the descriptor, or `supported:false`. |
| `switch_tab(tab)` | shell | Already shipped. |
| `find_destination(query)` | index | Later — ~4,000 Sociogram nodes cannot fit in a prompt. |
| `navigate(id)` | bus command | Later — drives the tab's own focus/isolate/search verbs. |

## Knowledge directory (canonical source)

```
wiki/voice_guide/
  knowledge/
    00_project.md          # what C2A2 is, the 14 traditions (stable)
    tabs/<tab-key>.md      # per tab: purpose, color semantics, answerable questions,
                           #          and an explicit "must not claim" list
  voice_guide_faq.json     # generated/deepened by scripts/voice_faq.py
  destinations.json        # navigation index (later)
```

**Canonical-source rule:** `knowledge/` is the single source of truth.
- `scripts/voice_faq.py` scans `knowledge/`, **not** the `descriptions` map inside `explorer.html`.
- The explorer's tab help text is **derived** from `knowledge/` by a build step.

Without this rule we simply rebuild today's four-source mess (hardcoded `instructions()`, the
`TABS` array, the `descriptions` map, and the broker scope prompt) inside a new folder.

Each tab file carries frontmatter:
```yaml
tab_key: wiki_narration.html
title: Sociogram
volatile: bus            # reminder: counts/filters/selection come from the bus, never this file
```

## Rollout order

0. **Anti-fabrication rule** in the guide instructions. *(done 2026-07-19)*
1. **This contract.** *(this document)*
2. **Knowledge directory**, authored to the stable/volatile line + canonical-source rule.
3. **Bus implemented for the Sociogram only**, end to end — the tab that triggered the complaint
   and the richest state. Prove the loop before scaling.
4. Roll out to remaining tabs; add `find_destination` + `navigate`.

## Open questions

- Does `voice_guide_faq.json` move under `wiki/voice_guide/`? (Path change breaks the guide's
  current `fetch`; do it with the step-2 build step, not before.)
- Should `view_changed` pushes re-inject into the live realtime session, or only be read on the
  next `describe_view()` call? Pushing costs tokens every change; pulling risks a stale answer.
  Leaning **pull-on-demand + push only on tab switch**.
