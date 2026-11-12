---
title: The Declared Dimension Set — the contract a surface satisfies to be described, exported and subscribed to
status: proposed (for Tom's decision; nothing implemented)
created: 2026-11-11
inputs:
  - architecture/explorer_manifest_audit_2026-10-04.md (§4.3, §4.4, §4.5, §5, §6, §8)
  - architecture/manifest_schema_acceptance_test_2026-10-04.md (R1–R8, §6)
  - architecture/voice_guide_redesign.md (§3 the dimension model, §5 result contract, §6 perception)
  - voice_guide/manifests.json (v1, live) · voice_guide/manifests.v2.json (acceptance-test artifact)
  - c2a2-wiki-narration/scripts/generate_visualization.py (the only full implementation of the old contract)
  - scripts/test_voice_shell.cjs (FIND_TABS, Phase X/Y)
supersedes: nothing. Extends manifests.v2.json §8's `cut` block.
---

# The Declared Dimension Set

**What this is.** One contract that a C2A2 Explorer surface satisfies so that
*describing its current cut*, *exporting exactly what it is showing*, and
*subscribing to it* stop being three separate builds and become three readings
of one declaration.

**What it replaces.** The three-function contract (`c2a2Find` / `c2a2Clear` /
`c2a2ReadCut`) as the thing we spread to the six pending tabs. It does not
delete those functions — §5 specifies them as a derived shim.

**Status.** Design only. No runtime file was touched, no test modified, no
implementation written. Decisions reserved to Tom are collected in §9.

---

## 0. The one-paragraph version

A surface declares a short list of **named dimensions**. Each dimension says what
it is called, what kind of thing it holds, how to read it, how to write it, what
universe its values come from, and — the field that makes readers work —
**whether it narrows the set of things on the page (`narrows: true`) or merely
locates you within that set (`narrows: false`)**. The runtime returns the same
list with current values filled in, plus one `counts` block. From that single
object: the voice guide builds a sentence, the exporter builds a record set from
the `narrows` dimensions only, and a subscription stores the `narrows` vector as
a predicate and watches the surface's declared change stamp. Nothing else is
needed, and the three consumers cannot drift apart, because there is only one
thing for them to read.

---

## 1. The schema

This is an extension of `cut` in `manifests.v2.json` (audit §8). Every v2 field
survives; four are added and one existing field is given a stricter meaning.
**Nothing here is a seventh page table** — it lives inside the existing `pages.<key>.cut`
block of `manifests.v2.json`, which is the file intended to merge into
`manifests.json` at cut-over.

### 1.1 Declaration (static, in the manifest)

```jsonc
"cut": {
  "no_cut": false,                 // v2. positive assertion for prose pages (F4)
  "grain": "node",                 // [new] what one unit of this surface IS
  "dims": [
    {
      "name":   "filters",         // v2
      "kind":   "set",             // v2, extended: value | set | address | action | read
      "type":   "group-key[]",     // v2
      "label":  "traditions and structure groups",   // v2  — spoken noun
      "aka":    ["groups", "traditions"],            // v2  — what a user may call it

      "read":   "window.c2a2ReadDims().filters",     // v2 (binding or dotted path)
      "write":  "input[data-group]",                 // v2
      "source": "dom",                               // v2 — dom | data

      "universe": {                                   // [new]
        "from":  "TRADITION_GROUPS ∪ STRUCTURE_GROUPS",
        "size":  32,
        "labels": "g.label || g.key"                  // how a value is SPOKEN
      },

      "narrows":     true,          // [new] ** the discriminator. see §2 **
      "fingerprint": "semantic",    // v2 — semantic | continuous
      "default":     "captured",    // v2 §3: boot snapshot, never hand-authored
      "requires":    [],            // v2 §4.4b
      "clamps":      []             // v2 §4.4b
    }
  ],

  "address":   { "anchor_pattern": "...", "stable": true, "unique": true,
                 "hash_written": true, "scroll_tracked": false },   // v2 §4.4a
  "serialize": { "read_fn": "window.c2a2ReadDims",
                 "write_fn": "window.c2a2WriteDim",
                 "storage_key": null, "url_param": null },          // v2, retargeted

  // v1 blocks, unchanged, still consumed by the shell and the coverage gate
  "items": {}, "views": [], "frames": [], "filters": [], "families": [], "camera": {}
}
```

**`kind`**, five values, unchanged from `voice_guide_redesign.md` §3 plus the
audit's §4.4a addition:

| kind | holds | example |
|---|---|---|
| `value` | one scalar or enum | `layout`, `view`, `quoted_only` |
| `set` | a subset of a universe | `filters`, `lens.sources`, `sections` |
| `address` | a position in a corpus | `#r8c4`, `#p221-slug`, `#day-137` |
| `action` | one-way, `inverse: null` | schedule playback, `fit` on some pages |
| `read` | derived, not writable | `counts`, `_spyCur` (current heading) |

### 1.2 Runtime (what the page returns)

Two functions replace three. The page exposes:

```js
window.c2a2ReadDims()          // -> DimensionVector.  no arguments, no side effects
window.c2a2WriteDim(name, op, value)   // -> DimensionVector (the write returns the read)
```

`op` is one of `set | add | remove | clear` — the same ∪ / ∖ / := algebra
`voice_guide_redesign.md` §3 already requires, so "add without remove" stays
unrepresentable.

`DimensionVector`:

```jsonc
{
  "page":  "sociogram",            // identity.key — the ONE namespace
  "grain": "node",
  "counts": {
    "visible": 412,                // units passing every `narrows:true` dimension
    "total":   4211,               // units in the universe
    "in_view": 37,                 // optional; what is literally on screen
    "source":  "activeNodes.length / NODES.length"   // a count with no stated source is a rumour
  },
  "cut_depth": 2,                  // how many dimensions are off their captured default
  "dims": {
    "filters":   { "kind": "set",   "narrows": true,
                   "value": ["Levin", "Friston"],
                   "off":   ["Hoffman", "Kastrup", "…25 more"],
                   "universe_size": 32, "is_default": false },
    "highlight": { "kind": "value", "narrows": true,
                   "value": { "query": "bioelectric", "ids": ["…"] },
                   "universe_size": null, "is_default": false },
    "selection": { "kind": "value", "narrows": false,
                   "value": "levin-bioelectric-fields-02", "is_default": false },
    "camera":    { "kind": "value", "narrows": false, "fingerprint": "continuous",
                   "value": { "k": 1.8, "x": -220, "y": 90 }, "is_default": false },
    "layout":    { "kind": "value", "narrows": false,
                   "value": "discipline", "is_default": true }
  },
  "stamp": { "field": "_meta.generated", "value": "2026-09-28T05:12:00Z" },  // for L2
  "partial": false       // true when a dim could not be read; names it in `errors`
}
```

### 1.3 The property that §0 of the brief demands

> "412 of 4,211, cut by these dimensions" must be expressible and distinguishable
> from "nothing cut."

It is, three times over and redundantly on purpose:

- `counts.visible` vs `counts.total` — the numbers.
- `cut_depth` — 0 means *nothing is off its default*, which is the honest reading
  of "nothing cut". Non-zero means something is.
- per-dimension `is_default` — *which* dimensions, by name, so the sentence can
  say so.

Today `c2a2ReadCut()` returns `null` in exactly the state above (27 groups off,
no search). That is the bug the audit found, stated as a missing field rather
than a missing function: the old contract has no representation for a filter.

**Deliberate redundancy.** `cut_depth` is derivable from `dims[].is_default`, and
a reviewer will ask why both. Because the three consumers disagree about what
counts as "cut" and the disagreement should be *visible*: a subscription cares
only about `narrows:true` dims, narration cares about all of them, export cares
about `narrows:true` at the declared grain. One scalar that everybody reads the
same way removes a class of argument. If it ever disagrees with the per-dim
flags, that is a test failure (§6, T2c), not a judgement call.

---

## 2. Five families, one schema, one discriminator

The audit's five families (§5) are **not a partition** — the acceptance test's
R7 found three surfaces in two families each (`agent_map` chart+table,
`whos_who` prose+table, `trv_commentary` graph+reader). So `family` is a list,
and "required blocks per family" is a **union over the list**. This spec assumes
R7 is accepted. It is the one upstream decision this design depends on (§9).

The families differ in *which kinds appear* and *how `narrows` is distributed*.
They do not need different schemas.

| family | typical dims | `narrows: true` | `narrows: false` | `grain` |
|---|---|---|---|---|
| **F1 graph** (Sociogram, Connectome, Community Explorer, TRV, L2 stream) | filters, highlight, selection, camera, layout | filters, highlight | selection, camera, layout | node / triplet |
| **F2 chart** (Metabolism, Agent Map schedule) | view, metric, logy, **window** | window, metric | view, logy, playhead | series point |
| **F3 reader** (RC Doc Explorer, RC Sandbox, Curriculum, Summa Commentary, Inter-Tradition, Physics, TRV page view) | sections, text filter, flags, **address**, scroll position | sections, text filter, flags | **address, scroll position** | unit / cell / paragraph |
| **F4 prose** (Start here, What's it doing/saying, Who's Who, Community Interactions) | — (`no_cut: true`) | — | page, scroll | section |
| **F5 table** (Community Cards, Agent Map explorer, Who's Who, Heartbeat Pulse) | text filter, facet sets, sort, page size | text filter, facets | sort, page size, selected row | record |

### 2.1 Readers: why `narrows` is the whole fix

Audit §4.5 says the identity "description = export query" holds for F1/F2/F5 and
**fails for F3**, and proposes `export.records[].grain` with
`filter_by_cut: false` as the patch. That patch works but it throws away
information: it says "don't filter readers by their cut", when in fact *part* of
a reader's cut should filter the export and part should not.

RC Sandbox is the proof. Its cut, read off the page (`manifest_audit/08_rc_sandbox.md`):

| dim | kind | narrows? | why |
|---|---|---|---|
| `sections` (36 outline nodes, `.rail input[data-cut]`) | set | **yes** | unchecking a node removes its cells from the page; an export should lose them too |
| `text` (`#q`, substring over id+text) | value | **yes** | `#hits` already reports "N of 2,191" — that N *is* the export row count |
| `quoted_only` (`#fq`) | value (bool) | **yes** | a content predicate |
| `by_row` (`#fv`) | value (bool) | **no** | regroups the same elements; changes layout, not membership |
| `read_through` (`#fr`) | value (bool) | **no** | hides furniture; same cells |
| `address` (`#rNcM` / `#row-N`, written with `replaceState`) | address | **no** | where you are, not what you want out |
| `hits` / `scope` | read | — | the existing prose read-out |

So the right export from the RC Sandbox is **not** "the paragraph you are looking
at" (useless, §4.5's objection) and **not** "all 2,191 cells regardless of cut"
(`filter_by_cut: false`, which throws away a perfectly good 36-way section
filter). It is *the cells passing `sections ∧ text ∧ quoted_only`, at cell
grain, ignoring `by_row`, `read_through` and the address* — which is exactly
`assignments.csv`'s column set, the cleanest description-is-export-query case in
the whole audit.

**Restated identity, which this spec adopts:**

> The export query is the conjunction of the dimensions declared `narrows: true`,
> evaluated at `cut.grain`. It is universal across families. The reason it
> *appeared* to fail on readers is that readers are the family where most
> dimensions are `narrows: false`, and the old contract had no way to say so.

RC Document Explorer is the harder reader and shows the limit honestly:

| dim | kind | narrows? | note |
|---|---|---|---|
| `view` (toc / thinkers / solved) | value | **no** | which sidebar; the document is the same |
| `toc_filter` (`#toc-filter`) | value | **yes** | hides ToC `li`s for q > 1 char — but it filters the *ToC*, not the body |
| `thinker` (9) | value | **yes**, in the `thinkers` view only → `requires` | |
| `section` (`#pNNN-slug`) | address | **no** | and `preventDefault` means the hash is never written |
| `page` (`#page-N`, 471) | address | **no** | |
| `reading_position` (`_spyCur`) | read | — | the real "where am I" |
| `query` (`#chat-input` → `retrieveCtx`) | value | **yes** | **returns pages, not unit ids** |

Two findings fall straight out, and I am recording them rather than designing
around them:

- **F-1. The scope of `toc_filter` is not the scope of the grain.** It narrows
  headings while the grain is the paragraph. A dimension therefore needs to say
  *what it narrows*, not merely that it narrows. **Proposed field:
  `narrows_entity: "<entity name>"`,** defaulting to `cut.grain`. An export at
  paragraph grain under a heading-level filter means "paragraphs under the
  surviving headings" — expressible, but only if the relation is declared.
  Without this the RC Doc Explorer's export is ambiguous by two orders of
  magnitude (650 ToC links vs 1,106 paragraphs).
- **F-2. RC Doc Explorer cannot export at its own declared grain today.** The
  per-paragraph `unit_id`s (`tome:pPPPhHHsSS`) exist in `inbox/rc_tome/tome_units.csv`
  and only ~15 of them reached the DOM. A client-side exporter has nothing to key
  on. The schema can *declare* the grain truthfully; the page cannot *produce* it
  until the ids land in the DOM or the exporter is allowed to read the upstream
  CSV. **Proposed field: `export.records[].source: "page" | "upstream"` with a
  path** — so the manifest states the gap instead of implying a capability.

### 2.2 Charts: the dimension the page does not have

Metabolism's four knobs are interdependent (`requires` / `clamps`, v2 §4.4b
already covers this). The audit's sharper point stands and this spec repeats it:
Metabolism has **no `window` dimension** — a time-series page whose cut excludes
time. Declaring the controls that exist is not the same as declaring the state
that matters. For F2, `window` is a **required** dimension; a chart manifest
without one fails the completeness gate (§6, T7) even if every on-screen control
is covered.

### 2.3 Prose pages

`no_cut: true`, `dims: []`, and a `page`/`scroll` pair declared `narrows: false`
if anything at all. `what_is_saying`'s v1 entry already argues this in prose; the
schema lets it be data. Silence (a missing `cut` block) stays a gate failure;
`no_cut: true` is a pass.

---

## 3. The three consumers, derived from one declaration

All three read the same `DimensionVector`. No consumer reads the page.

### 3.1 Voice — a spoken sentence

Rule: walk `dims` in declared order; skip `is_default: true`; render
`narrows: true` dims as *what is shown*, `narrows: false` dims as *where you are*;
open with counts when `cut_depth > 0`.

**Sociogram**, the state the old contract could not describe:

> `c2a2ReadDims()` → counts {412, 4211}, cut_depth 2,
> filters ["Levin","Friston"] / off 27 ·
> highlight {query:"bioelectric"} · selection "levin-bioelectric-fields-02"

renders as:

> "412 of 4,211 nodes. Showing Levin and Friston only — 27 groups are off — and
> highlighting 'bioelectric'. You have the Levin bioelectric fields article open."

Compare today's `what` on the same state, which says nothing about the 27 off
groups unless `describe_view` answers within 700 ms, and today's
`c2a2ReadCut()`, which returns `null`.

**RC Sandbox**, a reader:

> "238 of 2,191 cells. Scoped to 4 of 36 outline sections, quoted cells only,
> matching 'civility'. You're at row 8, cell 4."

The clause order is not cosmetic — it is `narrows` first, address last, so the
guide can be truncated at a brevity cap without ever dropping the part that says
what is on screen.

**Prose page** (`no_cut: true`): "This is a reading page — there's nothing to
filter. You're in the second section." No apology about unsupported capability,
because the manifest asserts the absence positively.

### 3.2 Export — CSV/JSON of exactly the visible set

```
rows   = universe(cut.grain)
         filtered by every dim where narrows == true,
           each evaluated against narrows_entity (default = cut.grain)
columns = entities[grain].fields  ∪  export.records[].columns
```

**Sociogram**, same state → `c2a2_sociogram_filtered.csv`, 412 rows, grain `node`,
columns `id, label, group`. The `selection` and `camera` dims contribute
nothing, correctly: you do not want a different export because you panned.

**RC Sandbox** → 238 rows, grain `cell`, columns
`cell_id, row, seq, node, division, words, voice, figures, disciplines, date_lo, date_hi, text`
— the `assignments.csv` column set. `by_row` and `read_through` contribute
nothing; the address contributes nothing. This is the case §4.5 called
impossible; it is possible because `narrows` separates the two halves of the
reader's cut.

**RC Doc Explorer** → the export is **declared but not producible** today
(finding F-2). The manifest says `grain: "unit"`,
`source: "upstream"`, `path: "inbox/rc_tome/tome_units.csv"`, and the export
control is absent rather than wrong. A surface that can describe but not export
is a legitimate, declarable state; shipping a button that exports pages when the
grain is paragraphs is not.

**What the schema does not carry, stated as a finding rather than patched:**

- **F-3. Ordering.** CSV rows have an order and nothing declares it. F5 surfaces
  have a `sort` dimension marked `narrows: false` (sorting does not change
  membership) — but for export it absolutely does change the artifact. Either
  `sort` gets a third flag (`orders: true`) or export declares its own
  `order_by`. **Recommendation: `orders: true` as a sibling of `narrows`**, so
  the three consumers stay one declaration: narration ignores it, export uses it,
  subscription ignores it.
- **F-4. Cell-level provenance on derived values.** Several surfaces show computed
  columns (Agent Map's `events`, the Heartbeat's `relevance`). `entities[].fields`
  names them but nothing says they are derived or from what. Not blocking; flag
  for the F5 pass.

### 3.3 Subscription — a saved cut plus a change signal

A subscription is `{page, dims_predicate, grain, stamp_at_save}` where
`dims_predicate` is **only** the `narrows: true` dims with
`fingerprint: "semantic"`. Continuous dims (camera, brightness) and positional
dims are excluded by construction, which is what stops a wheel-zoom from firing
a notification.

Evaluation: when the surface's declared `change.stamp` moves, re-evaluate the
predicate over the new universe and report `added / removed` at `change.grain`,
keyed by `change.key_field`.

Worked, on the audit's own pilot (§6):

- **AI Heartbeat.** `change.grain: "signal"`, `key_field: "url"`, stamp
  `digest.json.generated_at`, 60-second client poll already implemented, and the
  cut is already a serialised read/write pair (`HB_getPrefs` / `HB_setPrefs`,
  schema'd in `preferences.schema.json`). Subscription = save the lens, diff new
  signals against it. This surface needs no new mechanism — only a `dims` block
  that points `read`/`write` at the two functions it already has.
- **Sociogram.** `change.grain: "regen"`, `key_field: null`. A subscription here
  can only honestly say *"the graph was rebuilt; your cut now matches 419 nodes,
  up 7."* It cannot say *which* 7 unless the regen emits per-node first-seen
  dates. **F-5: this is the schema's real limit on L2.** `change.grain: "regen"`
  is a positive, honest declaration (audit §6.2) and the subscription consumer
  must degrade to a count delta for those surfaces rather than pretending to a
  record feed. The gate should refuse `subscribable: true` where
  `grain == "regen"` **and** the consumer claims record-level alerts.
- **Level-2 Signal Stream.** `grain: "signal"`, `key_field: "a/b/date"`, stamp
  `prototypes/level2_build_meta.json`, `staleness_warn_days: 21`. The best of the
  three, and still nested inside a `<details>` on a page with no manifest entry.

**F-6, the join nobody has declared.** A subscription predicate is written over
*cut dimensions* and evaluated over *change records*. Nothing today says those
two are over the same entity. On the Heartbeat they are (both `signal`). On the
Sociogram the cut is over nodes and the change is over builds, and only the
`grain: regen` degradation makes that safe. **Proposed gate:
`change.grain` must equal `cut.grain`, or `change.grain == "regen"`, or the
surface declares `subscribable: false`.** Three legal states, no fourth.

---

## 4. Design for the Sociogram first

Per the brief's hard constraint. The Sociogram is the only surface with the old
contract, the only one with `describe_view`, and — at 40 MB and a generated
artifact — the most expensive one to get wrong. Everything above is written to
survive contact with it.

### 4.1 Its declaration, in full

Read off `generate_visualization.py` (`activeFilters`, `buildDescriptor`,
`SEARCH_CUT`, `groupVisibility`) and v1's `dim_coverage`:

```jsonc
"cut": {
  "no_cut": false,
  "grain": "node",
  "dims": [
    { "name": "filters", "kind": "set", "narrows": true, "fingerprint": "semantic",
      "label": "tradition and structure groups", "aka": ["groups","traditions","structure"],
      "read": "groupVisibility", "write": "input[data-group]", "source": "dom",
      "universe": { "from": "TRADITION_GROUPS ∪ STRUCTURE_GROUPS", "size": 32,
                    "labels": "g.label || g.key" },
      "default": "captured" },

    { "name": "highlight", "kind": "value", "narrows": true, "fingerprint": "semantic",
      "label": "search", "aka": ["search","find","cut"],
      "read": "SEARCH_CUT", "write": "#search-input + runSearchLocal", "source": "data",
      "universe": { "from": null, "size": null },
      "default": null },

    { "name": "selection", "kind": "value", "narrows": false, "fingerprint": "semantic",
      "label": "open article", "read": "selectedState()", "write": "node click / dismissRightPanel" },

    { "name": "camera", "kind": "value", "narrows": false, "fingerprint": "continuous",
      "label": "view", "read": "d3.zoomTransform", "write": "#btn-fit-all / zoom" },

    { "name": "layout", "kind": "value", "narrows": false, "fingerprint": "semantic",
      "label": "layout", "universe": { "from": "LAYOUTS", "size": "unknown" } }
  ],
  "address": null,
  "serialize": { "read_fn": "window.c2a2ReadDims", "write_fn": "window.c2a2WriteDim",
                 "storage_key": null, "url_param": null }
}
```

`counts.source` is `activeNodes.length / nodeTotalForScope()`, which is what
`buildDescriptor` already computes. `in_view` is `_lastInViewNodes`, already
maintained and already distinguished from `passingNodes` — a distinction this
page learned the hard way in August 2026 and which the vector preserves by name.

### 4.2 Where the surface contradicts the design — stated, not designed around

- **C-1. `getCurrentViewState()` is a second, worse reader and must go.** It
  scrapes node opacities with a `brightness * 0.4` threshold and returns `null`
  when more than 85% of nodes are lit. That is a *third* representation of the
  cut, after `SEARCH_CUT` and `buildDescriptor`, and it is the one that produced
  the "5102 nodes shown" lie the harness recorded (`test_voice_shell.cjs:2555`).
  Under this contract it is replaced by `c2a2ReadDims()`, not kept alongside.
  Keeping it would reproduce at the dimension layer exactly the two-readers
  problem the audit diagnosed at the function layer.
- **C-2. `describe_view` and `c2a2ReadDims` would overlap by about 80%.**
  `buildDescriptor()` already returns `{selected, filters, counts, legend, dominant}`.
  The honest move is that **`c2a2ReadDims()` becomes the implementation and
  `buildDescriptor()` becomes a projection of it**, keeping the postMessage road
  and its 700 ms timeout for the shell's existing consumers. Two functions, one
  source. Not three.
- **C-3. The `legend` / `dominant` payload has no home in the dimension set.**
  It is neither a dimension nor a count — it is a *summary of the visible set*.
  Rather than invent a slot, declare it where it belongs:
  `DimensionVector.summary`, an opaque, per-family, optional object that only
  narration reads. Export and subscription must ignore it. Saying "optional and
  opaque" is better than pretending it is a dimension, because a `read`-kind dim
  that nothing writes and nothing filters by would blur the one line this design
  depends on.
- **C-4. The 40 MB artifact is regenerated by a Python generator with strict
  template rules** (regular strings, `""" + json + """`, single braces, `node --check`).
  The dimension functions are ~60 lines of JS inside that template. This is
  cheap, but it means every Sociogram iteration is a full regen via
  `wiki/c2a2-wiki-narration/regen_sociogram.sh` — not an edit. Budget accordingly.
- **C-5. `layout`'s universe is undetermined.** I did not establish the enum of
  layouts from the generator. Marked `"unknown"` per `manifests.v2.json`'s own
  convention, where `"unknown"` is a positive assertion and silence is a defect.

---

## 5. Migration from the current contract

### 5.1 The shim, and why the old functions stay

`c2a2Find` / `c2a2Clear` / `c2a2ReadCut` are load-bearing *right now* in three
places: the shell's `find` dispatcher, the CCL journal (Phase X `a2` asserts the
journal entry carries the query), and the tab-box alias (Phase X `b` asserts the
tab's own search box produces an **identical** journal entry). Replacing them in
one step would take the voice shell red mid-flight and the suite could not tell a
migration from a regression.

**So they are kept, re-expressed as projections of the `highlight` dimension:**

```js
window.c2a2Find  = (t) => { const v = c2a2WriteDim('highlight','set',t);
                            const h = v.dims.highlight.value || {};
                            return { query: t, ids: h.ids || [], count: (h.ids||[]).length,
                                     label: 'nodes shown' }; };
window.c2a2Clear = ()  => { c2a2WriteDim('highlight','clear'); };
window.c2a2ReadCut = () => { const h = c2a2ReadDims().dims.highlight.value;
                             return h ? { query: h.query, ids: h.ids.slice() } : null; };
```

Three consequences, all intended:

1. The old functions keep their **exact current semantics**, including returning
   `null` when only filters are set. That is not a bug being preserved — it is a
   *scope* being made explicit: `c2a2ReadCut` reads one dimension, and after this
   change the code says so.
2. `SEARCH_CUT` stops being a free-standing global and becomes `dims.highlight`'s
   storage. One writer.
3. Phase X and Phase Y stay green unchanged throughout. That is the migration's
   safety property and §6's T0 asserts it.

### 5.2 Deprecation, and when

The shim is removed only when **all three** hold: every surface in `FIND_TABS`
implements `c2a2ReadDims`; the shell's `find` dispatcher reads the vector
directly; and `FIND_TABS` itself is generated from the manifest rather than
hand-written. Until then it is not deprecated, it is *scoped*. No date is
proposed — a date here would be a guess, and the third condition depends on the
R5/R6 question the acceptance test left open (§9).

### 5.3 Order of work

1. **Sociogram only.** Add `c2a2ReadDims` / `c2a2WriteDim` to the generator,
   fold `buildDescriptor` and delete `getCurrentViewState` (C-1, C-2), fill the
   `cut` block in `manifests.v2.json`, add the §6 tests. One tab, one regen, one
   verdict.
2. **Heartbeat second**, not a graph — because `HB_getPrefs`/`HB_setPrefs` is
   already the read/write pair and it is the family (F5) where all three
   consumers are cheapest. It is the fastest proof that the schema is not
   Sociogram-shaped.
3. **RC Sandbox third**, because it is the reader whose `narrows` split is
   cleanest and whose cut is already serialised (`localStorage.qn`). If the
   reader profile is wrong, this is where it shows.
4. Then the remaining five of the six pending rows.
5. **Only then** consider the `identity` consolidation (audit §8 step 1), which
   is independent and pays off regardless.

---

## 6. Acceptance tests, stated so they can fail

Two suites. The first is carried forward from the audit; the second is new and is
the one that must be red against today's code.

### 6.1 T1 — identity generation (carried forward, already passing)

`python3 scripts/generate_page_tables.py --diff` exits 0: all six page tables
(`TABS`, `manifests.json.tabs`, `descriptions`, `KNOWLEDGE`,
`destinations.json.tabs`, `FIND_TABS`) are generated from one `identity` key per
surface. **Status: passes today with revisions R1–R8**, per
`manifest_schema_acceptance_test_2026-10-04.md`. This spec adds one thing:
**make it a gate**, run in the CCL check (`scripts/check_voice_shell.sh`), so
the six tables cannot drift apart again between audits.

Carry forward unchanged the test document's own caveat: the `FIND_TABS` row
proves *expressiveness*, not that the information already existed — R5/R6's
values were read off `FIND_TABS` itself. Do not count it as evidence.

### 6.2 T2 — the declaration test (new; MUST fail today)

The brief's requirement: *a test that passes against today's `{query, ids}` is
not a test.* So T2 is written against the state the old contract cannot
represent.

On the Sociogram, headless, in `test_voice_shell.cjs`:

```
setup:  run `only levin friston`          (27 of 32 groups now off)
        run `clear`                        (highlight is empty — this is the trap)
        v = window.c2a2ReadDims()

T2a  v.counts.visible < v.counts.total              -- a cut exists
T2b  v.cut_depth >= 1                               -- and the page says so
T2c  cut_depth == count(dims where !is_default)     -- the redundancy agrees
T2d  v.dims.filters.is_default === false
     && v.dims.filters.off.length === 27            -- BY NAME, with the number
T2e  v.dims.highlight.is_default === true           -- and the highlight is honestly empty
T2f  window.c2a2ReadCut() === null                  -- the OLD reader still says null
                                                       and is now provably partial
```

**Against today's build: T2a–T2e all FAIL** — `window.c2a2ReadDims` is
`undefined`. T2f passes today and must keep passing, because it is the shim's
contract (§5.1). A surface that returns matched ids and nothing else fails T2d
specifically: there is no `filters` dimension to name, and no `off` list to
count. That is the discriminator the brief asked for.

### 6.3 T3 — declaration ≡ implementation

Set equality, both directions, per surface:

```
manifest.cut.dims[].name   ==   Object.keys(c2a2ReadDims().dims)
```

Fails on a page that declares a dimension it does not implement (the drift that
makes a manifest a wish-list) **and** on a page that implements one it does not
declare (the drift that makes the coverage gate meaningless). This is the
`caps` (declared) vs `capability` (observed) separation the audit insists on,
applied to dimensions instead of verbs.

### 6.4 T4 — the write returns the read

For every dim with a `write` and `kind != action`: write a non-default value,
re-read, assert the read reflects it — and where the surface clamps (MAX_NODES,
a group that refuses to toggle), assert the read reports the **clamped** value,
not the requested one. This is `voice_guide_redesign.md` §3's "the write returns
the read", made testable.

### 6.5 T5 — export fidelity

`rows(export at cut.grain) === counts.visible`, for a non-trivial cut, with
`narrows: false` dimensions perturbed between the two reads. Concretely on the
Sociogram: export, then pan and select a node, then export again — the two files
must be byte-identical. On RC Sandbox: toggle `by_row` and `read_through`
between exports; identical. **This is the test that fails if somebody wires
export to `getCurrentViewState` or to the address.**

### 6.6 T6 — no-cut honesty

On `no_cut: true` surfaces: `c2a2ReadDims()` returns `cut_depth: 0` and
`dims: {}` *and that is a pass*. A surface with **no** `c2a2ReadDims` at all is
PENDING/FAIL. Silence and an assertion of absence must not look alike — the same
principle as `manifests.v2.json`'s `"unknown"` vs `null`.

### 6.7 T7 — family completeness

Per family, required dimensions must be present: F2 requires `window` (§2.2);
F3 requires an `address` block; F5 requires `sort` and `pagination`; F1 requires
`filters` and `camera`. With R7 (family as a list), the requirement is the
**union** over the list, so `agent_map` must satisfy both F2's and F5's.

### 6.8 What none of these test

- Nothing here verifies a *spoken* sentence; narration quality stays a human
  check, as it is today.
- Nothing verifies a subscription end-to-end, because nothing subscribes to
  anything yet (audit §6). T-sub is deferred with that layer, stated rather than
  faked.
- T5 compares row counts and file identity, not column correctness. A wrong
  column set passes. The column set is a human review item on first
  implementation per surface.

---

## 7. The six pending rows — what "done" means per tab

All six are red in `FIND_TABS` today (verified: only `wiki_narration.html` and
`community_explorer.html` define `c2a2Find`). Each flips to passing when it
implements `c2a2ReadDims` / `c2a2WriteDim` *and* its `cut` block in
`manifests.v2.json`, such that T2–T7 pass. One sentence each, with the tab's own
difficulty named.

| tab | family | done means |
|---|---|---|
| **Narrative Connectome** (`prs_3d.html`) | graph | Declares `traditions ∧ disciplines ∧ decades ∧ three bools` as `narrows: true` set dims read through dotted paths (`meshes[].visible`, `prsFilterState`) rather than DOM — and either implements a real `highlight` (today's search "only dims meshes and records nothing") or declares `highlight` absent, since `cuts: false` in its own plot hook currently makes "I searched" unsayable. |
| **Agent Map** (`agents_tab.html`) | chart + table (R7) | Declares the **Explorer sub-view's** real cut — text filter, 6-category facet, 9-column sort — which the manifest today records as `dim_coverage: [{dim:'tab'}]`; the schedule playhead is declared `kind: action, inverse: null, narrows: false`, since nothing would export or subscribe to a position in an animation. |
| **RC Document Explorer** | reader | Declares `view / thinker / toc_filter / query` with `narrows` set correctly, an `address` block admitting `hash_written: false` and `unique: false` (44-char truncation), `narrows_entity` on `toc_filter` (F-1), and `export.source: "upstream"` (F-2) — i.e. done includes *declaring two gaps*, not closing them. |
| **Physics Explorer** | reader | Declares `concept_filter` (over 75 titles) as the one `narrows: true` dim, `mode / sidebar_view / physicist / chat_mode` as `narrows: false`, an `address` block for the stable concept slugs with `hash_written: false`, and brings the undeclared simulation sliders (`shm-amp`, `shm-freq`) in as `continuous` or into `controls_deferred` — today they are invisible to the sweep because the page is never swept. |
| **RC Sandbox** | reader | Declares the seven dims of §2.1 with `narrows` as tabled, points `serialize` at the existing `localStorage.qn` payload, and makes `#hits`/`#scope` a projection of `counts` rather than a parallel read-out — and gets a `voice_guide/knowledge` file, since its `KNOWLEDGE` value is literally `null` and the guide currently cannot speak about it at all. |
| **AI Heartbeat** (`heartbeat/index.html`) | table | Declares the lens as dims whose `read`/`write` are the existing `HB_getPrefs` / `HB_setPrefs` pair, `view` and `snapshot` as `address` dims (`narrows: false`), and `change` pointing at `digest.json.generated_at` with `grain: "signal"`, `key_field: "url"` — making it the first surface where a subscription is evaluable end-to-end. Note the iframe-asset rule: this is the one multi-file tab, so any `app.js` edit must go through `stamp_assets.py`. |

The Sociogram and Community Explorer are not in this table; the Sociogram is §4,
and Community Explorer already has the old contract and migrates by the same
route.

---

## 8. Contradictions found, and other honest gaps

**Recorded rather than designed around, per the brief's constraint.**

1. **The brief's pointer is off by a document.** It says "§6 of
   `voice_guide_redesign.md` already proposed the declared dimension set." §6 of
   that file is *"Perception: `what`, staleness, and mixed authorship"*. The
   phrase "declared dimension set" appears nowhere in it; it appears in
   `explorer_manifest_audit_2026-10-04.md` at lines 70 and 480 (§0.4 and §4.3),
   where the audit *quotes* redesign §6's one clause ("⊕ the manifest dimensions'
   `read()` values") and names the primitive itself. The design model is redesign
   **§3**, "The dimension model". I have treated §3 + audit §4.3–§4.5 as the
   proposal and completed that, which I believe is what was meant — but the
   proposal is spread across two documents and one of them does not contain the
   phrase.

2. **R7 is unresolved and this spec depends on it.** `family` as a list vs
   splitting `agent_map` in two. I have assumed the list. If `agent_map` splits
   instead, its one tab button points at two manifest entries and §7's row for it
   is wrong.

3. **The audit's §4.5 patch and this spec's `narrows` field disagree.** §4.5 says
   readers need `export.records[].grain` with `filter_by_cut: false`. This spec
   says `filter_by_cut` is too coarse — RC Sandbox's 36-way section filter *should*
   filter the export. I think §4.5 is right about the failure and wrong about the
   fix. Flagged explicitly because §4.5 is cited in the brief as settled.

4. **R5/R6 remain open and block T1 becoming a clean gate.** `FIND_TABS` encodes
   *intent* ("the contract is expected here"), which the acceptance test argued is
   neither `caps` (declared) nor `capability` (observed). This spec does not
   resolve where intent lives. Until it does, §5.2's third deprecation condition
   cannot be met.

5. **23% of `manifests.v2.json` leaf values are `"unknown"`, concentrated in
   `cut`.** Nine surfaces have a real cut; fifteen do not. Any claim that this
   contract has 24 consumers is claiming fifteen we cannot describe. The six
   pending rows are the right scope precisely because they are mostly in the nine.

6. **`cut.grain` vs `entities[]` is a near-duplication I did not resolve.** v2
   already has an `entities` block with `id_field` and `fields`. `cut.grain`
   should probably be a *reference* into it (`grain: "cell"` → `entities[name=cell]`)
   rather than a free string. I have written it as a free string to keep the diff
   small; a reviewer may reasonably want the reference.

7. **Not determined:** the Sociogram's `layout` enum (C-5); whether
   `community_explorer.html`'s existing `c2a2*` implementation matches the
   Sociogram's (it defines the functions — 6 hits — but I did not read it);
   how `requires`/`clamps` interact with `narrows` when a clamped dimension is
   also a narrowing one (Metabolism's `metric` under `view`), which needs working
   out before F2 lands.

---

## 9. Decisions reserved to Tom

1. **R7 — `family` as a list, or split the three dual-family surfaces?**
   Everything in §2 and §7 assumes the list.
2. **`narrows` vs §4.5's `filter_by_cut`** (§8.3). Adopting `narrows` means the
   audit's §4.5 paragraph is superseded, and I would want that recorded in
   `architecture/decisions.md`.
3. **Add `orders: true` as a third flag** (F-3), or let export declare its own
   `order_by`?
4. **Delete `getCurrentViewState()` in the first Sociogram regen** (C-1), or keep
   it one cycle for comparison? I recommend delete: keeping it is how the project
   got two readers in the first place.
5. **Where intent lives** (§8.4) — a `plan` block in the manifest, or stay in the
   tests?
6. **Order of work** (§5.3): Sociogram → Heartbeat → RC Sandbox → the rest. The
   non-obvious call is Heartbeat second rather than a second graph, to find out
   early whether the schema is Sociogram-shaped.

---

## 10. Token cost (Rule 6)

Rule 6 sets a per-task budget of 4,000 tokens. **This task breached it by roughly
an order of magnitude and I am surfacing it rather than reporting silently.**

Approximate: ~75k tokens of reading (the 916-line audit, the 469-line acceptance
test, 230 lines of `voice_guide_redesign.md`, four `manifest_audit/` entries,
`manifests.v2.json` parsed, ~250 lines of `generate_visualization.py`, ~120 lines
of `test_voice_shell.cjs`), plus ~12k generating this document. Call it ~90k
total for the session.

The required-reading list in the brief is ~3,500 lines on its own, so the budget
and the brief were not reconcilable. I read selectively — section indexes first,
then named sections — rather than whole files, which is where the saving came
from. If 4,000 is meant to bind on work of this shape, the budget needs raising
for spec tasks or the reading list needs narrowing; it cannot be met by being
more careful.
