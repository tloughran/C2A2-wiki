---
title: Voice Guide Redesign — CCL, the One-Command Control Surface
pathway_id: voice_guide_redesign
status: proposed (awaiting Tom review)
created: 2026-07-23
depends_on: [voice_guide_state_bus, voice_guide_dev_pathway, fact_inventory, broker]
supersedes: the tool-per-affordance design punted 2026-07-23 (WIP checkpoint f108855 on voice-guide-v2)
---

# Voice Guide Redesign — CCL: One Command Surface

> **North star (Tom, 2026-07-23):** anything a user would ordinarily do for himself or
> herself in the explorer can be articulated in English and responded to automatically
> by the system through voice.

**Provenance of this design.** Produced by a 21-agent design workflow: 4 recon readers over
the abandoned implementation + contracts, 4 independent architectures (declarative state
document / command box / capability manifest / first principles), 3 adversarial critiques per
design (symmetry-completeness, implementation reality, maintenance-drift), one cross-design
judge. All four designs scored "fixable"; the judge picked the command-box spine and grafted
the strongest elements of the other three. Every fatal and serious critique finding has an
explicit resolution in this document (§12 maps them).

---

## 1. Why the old design died (diagnosis, carried forward)

The abandoned build gave gpt-realtime **seven narrow tools** (`switch_tab`, `where_am_i`,
`describe_view`, `find_destination`, `navigate`, `filter_sociogram`, `search_sociogram`) and
a ~1,700-token prompt of routing discipline telling it when to call each. Three structural
failures, all confirmed by recon:

1. **Intent→tool routing is the model's job, and it is brittle.** "Two tools, pick by
   intent" is a coin-flip dressed as a rule. The model often misunderstood what the user
   wanted because understanding meant *choosing a tool*, not just hearing English.
2. **Asymmetry by construction.** Each verb was hand-built, so every capability existed
   only where someone had written it. "It can add but not remove" was not a bug; it was
   the architecture expressing itself. Fixing one asymmetry surfaces ten more.
3. **Every new intent = another tool + more prompt.** The surface grows linearly with
   affordances and the routing prompt grows with it — the exact opposite of scaling to
   12 tabs.

The one piece users and tests loved: the Sociogram's own search box. One expressive surface,
already understood, no routing. That observation is the seed of this design.

## 2. The decision

**One realtime tool, forever: `run_command(text)`.** Its argument is a string in a small,
documented, symmetric command grammar (CCL — the C2A2 Command Line). The same string drives
a visible shell command box, so voice and typing are one code path and one test surface.
The model's only job collapses to the one thing a language model is actually good at:
*English → a terse command string*. Everything else — parsing, fuzzy name resolution,
execution, undo, state reporting — is deterministic, shell-side, and testable without a
billed session.

```
user voice ──► gpt-realtime (WebRTC, broker mint — plumbing unchanged)
                  │ run_command("only levin friston")
                  ▼
explorer.html shell: window.CommandLine  (wiki/lib/c2a2-commandline.js, content-hash stamped)
  ├─ Parser      string ─► canonical op {dim, op, args}     (grammar-as-data: verbs.json)
  ├─ Resolver    fuzzy names ─► group keys / node ids       (LIVE DOM roster; generated node index)
  ├─ Journal     absolute {dim, before, after} vectors      (undo/redo/restore)
  └─ Dispatcher  op ─► executor for the active tab
                     │
     ┌───────────────┼──────────────────────────┐
     ▼               ▼                          ▼
 shell dims      Sociogram executors        per-tab manifests + adapters
 (tab, back)     (verified iframe globals   (declarative bindings where the
 click real       now; inline bus adapter    DOM allows; small adapter modules
 buttons          at next justified regen)   where closures force it)
                     │
              result {ok, did, state, ...} ─► function_call_output ─► model speaks "did"
```

Tool count stays **1** at 12 tabs or 50. Adding a capability is a manifest line or an
executor, never a new tool, never a prompt change, never a session-schema change.

**Explicitly rejected alternatives** (see §14 for the full kill list): per-tab tool
injection via mid-session `session.update` (unexercised mechanic, races the response
latch); model-authored structural JSON patches (higher error surface than a terse string
for a model with a documented intent-mapping failure history); moving name resolution
inside the 47MB regen artifact.

## 3. The dimension model (how symmetry stops being hope)

Commands are **assignments over declared state dimensions**, not hand-built actions.
Every affordance a user can operate is modeled as a dimension of the active tab's state:

```jsonc
{
  "name": "filters",            // one per affordance, per tab
  "kind": "set",                // value | set | action | read
  "type": "group-key[]",
  "read": "<binding or adapter fn>",
  "write": "<binding or adapter fn>",
  "fingerprint": "semantic",    // semantic | continuous (see §8)
  "gated": false,               // true => shell-enforced confirm (see §10)
  "spend": false                // true => costs broker quota (ask)
}
```

Rules that make the punt's failure class *unrepresentable*:

- `show / hide / only / all / none` are all set-operations (∪, ∖, :=, :=ALL, :=∅) on the
  ONE `filters` dimension. Add-without-remove cannot be shipped because add and remove are
  the same code applied to the same dimension.
- `open / close` write `selection`. `find / focus / clear` write `highlight`. `go / back`
  write `tab`. `set <knob> <value>` covers every enum/scalar knob as one manifest line.
- **Every verb must compile to a dimension write or read.** `fit`, `zoom in/out` write a
  declared `camera` dimension; `read/stop` write a `playback` dimension. A verb with no
  dimension is a lint error, not a shipping feature. (This closes the critique's
  "journal does not cover the grammar" fatal.)
- **`kind: action`** exists for genuinely one-way operations (they declare
  `inverse: null` and are excluded from the symmetry sweep *visibly, in data* — never
  silently skipped).
- **Defaults are captured, not authored.** On first load of a tab, the shell snapshots
  every dimension's `read()` — that snapshot IS the default set for `reset`. Nobody
  hand-writes defaults, so nobody can "correct" the Sociogram's intentional
  `EXCLUDED_FROM_ALL` variance into a bug (hazard H1 closed by construction).

**The write returns the read** (grafted from the declarative-state design): every executor
re-reads actual state after applying. If the graph clamps at MAX_NODES or a group refuses
to toggle, the spoken answer reflects reality, not intention.

## 4. The grammar (CCL v1)

Small, closed, symmetric. One command per call.

| Verb | Compiles to | Inverse |
|---|---|---|
| `go <tab>` / `back` | tab := x | journal (tab + snapshot, §7) |
| `show <groups…>` / `hide <groups…>` | filters ∪ / ∖ | each other |
| `only <groups…>` / `all` / `none` | filters := | journal |
| `open <node>` / `close` | selection := / null | each other |
| `find <text>` / `clear` | highlight := {find,q} / null | each other |
| `focus <a> ~ <b> [~ <c>…]` | highlight := {focus,[…]} (n-ary, via linkGroups) | `clear` |
| `set <knob> <value>` | knob dimension := v | journal |
| `fit` / `zoom in` / `zoom out` | camera := v | journal |
| `read` / `stop` | playback := v (gated on Tom's §16 call) | each other |
| `undo` / `redo` / `reset` / `restore` | journal ops | — |
| `what` / `where` / `help` | reads (no journal entry) | — |
| `ask <question>` | broker route; `spend:true`, never replayed | none (by design) |

Notes:
- `focus` is **n-ary** because `linkGroups(n)` already generalizes; the old bipartite-only
  `runFocus` limit does not constrain CCL ("compare Levin, Friston and Hoffman" works).
- Names are fuzzy-resolved **at execution time** against live sources: the checkbox roster
  read from the iframe DOM (the old `filterRoster` trick, kept — nothing to keep in sync),
  and the generated node index for `open`. **No enum is ever baked into connect-time
  instructions.** (Kill-list item: hand-authored catalogs of volatile values.)
- The Sociogram's native search box **keeps its legacy semantics untouched**. CCL lives in
  the new shell command box (`/` to focus) and in voice. One documented asymmetry, chosen
  over breaking existing typed workflows or shipping a third in-page grammar.

### The prompt shrinks to behavior only

Routing rules die. What remains: "You act and see ONLY via run_command. One command per
call. Speak the `did` back in one short sentence. Answer live-state questions only from the
latest result; if you have none, run `what` first. On `ambiguous`, read candidates and ask.
On `unsupported_here`, say so and offer what the tab is for." Plus the retained rules:
anti-fabrication, color-is-not-an-identifier, brevity cap, English default.

## 5. Result contract

```jsonc
// success — every mutating command returns fresh state (write returns the read)
{ "ok": true, "did": "only traditions/levin traditions/friston",
  "echo": "only levin friston",
  "state": { "page_state": "sociogram.graph.default",     // knowledge-grain key, always present
             "tab": "sociogram",
             "counts": {"visibleNodes": 412, "totalNodes": 4211},
             "filters": {"on": ["Levin","Friston"], "offCount": 27},
             "selected": null, "highlight": null,
             "knobs": {"layout": "discipline", "brightness": 0.5} },  // §12/F6: knobs are readable
  "undoable": true }

// ambiguity — candidates ride in the result, disambiguation needs no model memory
{ "ok": false, "error": "ambiguous", "term": "levin",
  "candidates": ["Michael Levin (tradition)", "levin-bioelectric-fields-02 (article)"] }

// capability gap — the supported list comes FROM the manifest, so it is never stale prose
{ "ok": false, "error": "unsupported_here", "tab": "metabolism",
  "supported": ["go <tab>", "what", "help", "set view raster|waveform|returned", "set logy on|off"] }

// scope disclosure — find never lies about what it searched (§12/F9)
{ "ok": true, "did": "find bioelectric", "matches": 3,
  "scope": {"searched": 412, "of": 4211, "note": "hidden groups not searched"} }
```

`page_state` keys (`sociogram.graph.node_selected` etc.) ride in every result, keeping the
knowledge-file grain (one file per affordance-profile) wired into perception.

## 6. Perception: `what`, staleness, and mixed authorship

- `what` = merged `where_am_i` + bus `describe_view` (700ms timeout, `stale:true` cached
  fallback, `supported:false` degradation — all kept verbatim) **⊕ the manifest dimensions'
  `read()` values**. On a manifest-but-no-bus tab, `what` returns the dimension reads with
  `supported:"partial"` — the guide never mutates a lens and then claims blindness to it.
  On a nothing tab: "I can take you there and tell you what it's for, but I can't operate
  it yet."
- **Both stale-note injectors survive, reworded** to say `run_command('what')` (the old
  text names `describe_view`, a tool that no longer exists — confirmed live-fire bug if
  kept verbatim).
- **The `_viewFetched` arming gate arms on every command result too**, not only on bus
  descriptor replies. Otherwise the common pattern voice-command → mouse-toggle → "how many
  now?" fires no stale note and the prompt's answer-only-from-results rule *instructs*
  fabrication. (Critique finding, accepted and fixed.)
- **The bus fingerprint gains a semantic knob tier**: dimensions marked
  `fingerprint:"semantic"` (filters, selection, highlight, layout, view mode) participate
  in `view_changed`; `continuous` ones (zoom, brightness) are excluded or quantized so
  wheel-zoom cannot flood the session with stale notes or evict undo snapshots.

**Mixed voice+mouse authorship — the single-writer delusion, killed:** the journal never
assumes it is the only writer. Three mechanisms:
1. **Read-at-command-time**: every write records `{dim, before: read(), after}` — `before`
   is reality, not the journal's memory of its own last write.
2. **Journal rebasing**: on every `view_changed` push, the shell refreshes its full-dimension
   snapshot; a manual mouse change lands as a rebase entry, so "undo that" right after a
   hand-click undoes the hand-click, not the last voice command.
3. **Highlight replay reads the iframe first**: before replaying a stored highlight after a
   rebuild, the dispatcher checks the live `#search-input` value; a user-typed query wins
   over the shell's stored one (never clobber the user's own search).

## 7. Undo / restore

- Journal entries are **absolute vectors** `{dim, before, after}` (grafted from D4);
  `show`/`hide` compile to absolute sets before journaling, so replay is deterministic.
- `undo`/`redo` = per-tab stack, max 20. `reset` = write every dimension to its
  **boot-captured** default snapshot.
- **Cross-tab restore is real, not punted** (the critiques were right that "impossible" was
  false): before `go`, the shell snapshots ALL dimensions of the outgoing tab; when the user
  returns (iframe reloads cache-busted, factory-default), the dispatcher **replays the
  snapshot through the same executors**. "Put it back how it was" works across the most
  common flow — glance at another tab and come back. `restore` is the explicit verb.
- **`ask` is fire-once, never replayed** — replaying it would re-bill nondeterministic
  broker calls and the Ask-AI mode auto-flips under quota. It is journaled only as its
  *resulting* highlight state, or not at all.
- Batch writes: multi-group filter changes mutate `groupVisibility` once + ONE
  `rebuildGraph()` + checkbox sync (both are window-reachable today — verified), never N
  sequential `toggleGroup` rebuilds. Without this, undo of `only levin friston` is ~27
  rebuilds of a 4,200-node graph mid-conversation — a multi-second frozen tab.

## 8. Execution tiers and the 12-tab scaling story

One grammar, one dispatcher, **honestly tiered executors** (the critique that "manifests
are code wearing a data costume" is accepted — about half the tabs need real adapter code):

- **T0 — shell dimensions** (free, all tabs): `tab`, `back`, `where`, `help`. Clicks the
  shell's real buttons (salvaged `switchTab`).
- **T1 — declarative bindings** (cheap): tabs whose controls are addressable DOM
  (selects, checkboxes, inputs with ids). The manifest binding IS data
  (`{dim: "view", bind: {select: "#view-mode"}}`).
- **T2 — adapter modules** (small code): closure-bound tabs (agents_tab canvas
  hit-testing, heartbeat chip clicks). A per-tab adapter implements `read/write` for its
  dimensions. Adapters live **shell-side in one owned file per tab**
  (`wiki/voice_guide/adapters/<tab>.js`, content-hash stamped), against a shared contract,
  covered by the same conformance battery. This is N small executors under ONE symmetric
  contract — not N bespoke tools, because the grammar, journal, result shapes, and tests
  are shared and the asymmetry class is checked mechanically.
- **T3 — inline bus adapter** (regen-priced): a generated tab (Sociogram) implements the
  contract's already-specified `command`/`command_result` bus messages natively. v1 ships
  **regen-free** on the verified iframe globals; the T3 adapter rides the next *justified*
  regen, batched (§13).

**Honest onboarding cost for tab #N:** manifest + (T1 bindings or T2 adapter) + knowledge
default file + battery rows. What it never costs: a new tool, a prompt change, a routing
rule, a session-schema change — which were the actual killers.

**Registry honesty:** this design adds manifests to the tabs-registry family. Mitigations:
defaults are captured not authored; the destinations index stays generated (with freshness
wired, §12/F12); the manifest is coverage-gated against the *runtime DOM* (§9) so it cannot
silently rot the way `descriptions`/`capabilities` arrays did. Collapsing TABS/HTML-rows
into a generated pair is a worthwhile *separate* increment, not load-bearing here.

## 9. Enforcement (H4: gates that run, not conventions)

The fatal critique — "the enforcement story cannot run as specified" — is answered by
moving the engine out of inline script:

- **`CommandLine` lives in `wiki/lib/c2a2-commandline.js`**, loaded by the shell with a
  content-hash `?v=` include (`stamp_assets.py`, the heartbeat pattern; explorer.html is
  the top-level document, not an iframe-loaded tab, so the constitutional inline rule does
  not bind it — and the repo's Class-A exemplar, `community/index.html` + `c2a2-search.js`,
  already blesses exactly this shape).
- **Grammar-as-data**: `verbs.json` is consumed by BOTH the parser and the janitor. "Every
  verb maps to a declared dimension", "every dimension is reachable by ≥1 verb", and
  "help == manifest" become real Python checks over real data files.
- **Tier-0 tests run headless**: parser, resolver, journal, and compilation are pure
  functions in the lib file — `node`/jsdom testable in `scripts/test_voice_ccl.py`-style CI,
  janitor-runnable weekly. (Precedent: the heartbeat jsdom roster test.)
- **Runtime coverage audit** (the answer to "the manifest is a hand-list with a lint that
  cannot see the gap"): a debug-panel sweep enumerates the tab's LIVE interactive elements
  (the Sociogram's 29 checkboxes exist only as `buildFilters` innerHTML output — static
  HTML parsing is provably blind) and diffs them against manifest dimensions + an explicit
  exclusion list. Unbound control ⇒ loud failure. Runs as a **pre-push step in the
  No-Blind-Push ritual** (loud, human-visible), plus janitor for the parseable subset.
- **Symmetry sweep** (unbilled, from the debug panel + pre-push): for every mutating
  dimension: read v0 → write non-default → assert read-back → `undo` → assert v0.
  `kind:action` exclusions are visible in data, so the sweep proves exactly what §3 claims.

## 10. Safety and spend

- Dimensions carry `gated` and `spend` flags. `ask` (`spend:true`) gets a **shell-enforced
  confirm handshake** — the executor refuses without a confirmed flag that only a fresh
  user yes sets; a prompt rule alone is not a gate. Broker caps (50/device/day, $5/day
  global) and BYO fallback unchanged.
- Anything auth/export/record/settings-shaped appears in manifests as `gated:true`
  (visible-but-refused), converting today's accidental safety into recorded decisions.
- `read` (long-form TTS) ships **only with the audio-collision engineering**: mic track
  `enabled=false` for the duration, `runSearchAI`'s auto-TTS suppressed while a live
  session exists, `stop` as the inverse — or the verb is deferred (Tom's call, §16).
  Long reads go to the page's own TTS, never through the realtime audio channel (most
  expensive tokens per word, fights the brevity rule, and the broker's server-minted scope).

## 11. Canonical utterances → execution (v1)

1. "Show me only Levin and Friston" → `only levin friston` → live-roster resolve →
   batch filters write → "Showing only Levin and Friston — 412 nodes."
2. "Undo that" / "Put it back how it was" → `undo` / `restore` — absolute-vector journal,
   rebased against mouse changes; works across tab round-trips via snapshot-replay.
3. "Open the McGilchrist node" → `open mcgilchrist` → node index → `openNodeByLabel`.
4. "Hide all the architecture stuff" → `hide architecture` → fuzzy expands to the matching
   structure groups; `did` names exactly what was hidden.
5. "Go to the heartbeat tab" → `go heartbeat` → salvaged `switchTab`.
6. "Zoom out so I can see everything" → `fit` → `fitAll()`.
7. "What am I looking at?" → `what` → bus descriptor ⊕ dimension reads, `page_state` key.
8. "Read me this article" → `read` → page TTS with mic muted (or deferred; §16).
9. "No, not that one — the other Levin" → previous result carried `candidates`; model
   re-runs `open` with the exact label. Disambiguation lives in results, not model memory.
10. "Turn everything off except the philosophy traditions" → needs the discipline→tradition
    facet mapping, which is MEANING → a small Tom-owned facets file in `knowledge/`
    (§16). Until it exists the guide asks which traditions the user means — never invents.

## 12. Critique findings → resolutions (the sound-by-inspection map)

| # | Finding (fatal/serious) | Resolution |
|---|---|---|
| F1 | Manifest completeness is a hand-list; lint can't see gaps | Runtime DOM coverage audit + exclusion list, pre-push loud (§9) |
| F2 | Journal doesn't cover grammar (fit/zoom/read/ask outside) | Every verb MUST compile to a dimension; camera/playback declared; lint enforces (§3) |
| F3 | Single-writer delusion (mouse invisible to journal) | before=read(), rebase on view_changed, iframe-first highlight replay (§6) |
| F4 | Enforcement can't run (inline JS, manual sweep) | lib file + verbs.json + jsdom Tier-0 + pre-push audit (§9) |
| F5 | Edge selection unreachable (remove-without-add mirrored) | Honest v1 gap: `selection` write for edges lands with the T3 regen batch (id-addressable edge-open API); until then `unsupported` spoken plainly, never faked (§13) |
| F6 | Write-only knobs (set then can't answer "what layout?") | Knobs ride every result state block + `what` (§5, §6) |
| F7 | Cross-tab undo destroys state; "impossible" was false | Snapshot-before-go + replay-after-return; `restore` verb (§7) |
| F8 | `read` TTS into a hot mic (echo → VAD chaos, billed) | Mic-mute engineering or defer verb — Tom gates (§10, §16) |
| F9 | `find` silently scoped to visible groups → spoken false negatives | Scope disclosure in result; model offers `all` first (§5) |
| F10 | Undo = ~27 sequential rebuilds at voice latency | Batch write path: groupVisibility once + one rebuildGraph (§7) |
| F11 | Stale notes name a dead tool; arming gate never arms | Reworded to run_command('what'); gate arms on command results (§6) |
| F12 | Node index goes stale after regen (build step not wired) | build_destinations.py wired into regen_sociogram.sh + janitor mtime check |
| F13 | Perception incoherent off-Sociogram (mutate then claim blind) | Manifests double as partial descriptors; supported:"partial" (§6) |
| F14 | Utterance 10 rests on nonexistent knowledge | Tom-owned facets file, or ask-until-it-exists (§11, §16) |
| F15 | Defaults hand-authored → H1 trap (EXCLUDED_FROM_ALL) | Defaults captured from boot state, never authored (§3) |
| F16 | Ask-AI/undo interaction (metered, nondeterministic) | ask fire-once, journaled as resulting highlight only (§7) |
| F17 | "Same string same path" shipped a third grammar | Native box untouched; CCL = shell box + voice only, documented (§4) |
| F18 | Manifests-as-JSON can't bind closure-bound tabs | Honest T1/T2 tiering; shared contract + battery (§8) |

## 13. Build plan (increments, each with an exit gate)

**Base:** `voice-guide-v2` in the C2A2-dev worktree (judge-verified it carries the
chapGuide fix; primary tree stays on `main`). Cherry-pick the two entangled bug fixes
(visible-row `activeTabSrc`, LANGUAGE pin) out of WIP `f108855` first; then the WIP is
reference-only.

0. **Kill-switch spike (~$1, needs Tom's authorization):** 2–4 broker mints, typed-injection
   harness against a STUB `run_command` that only logs the emitted string. Measure
   utterance→command accuracy on the 10 canonical utterances BEFORE building the engine.
   This is the falsification point every prior phase lacked. Exit: ≥8/10 clean or
   fixable-by-grammar-tweak; else stop and rethink.
1. **Engine:** `c2a2-commandline.js` (parser/resolver/journal/dispatcher) + `verbs.json` +
   shell command box + Tier-0 jsdom tests. No realtime changes yet. Exit: battery green
   headless; typed CCL drives the Sociogram via existing globals.
2. **Voice cutover:** replace the 7 tools with `run_command`; shrink the prompt; rewire
   stale injectors + arming gate. Exit: 25-cell grid re-run — cells now diff the emitted
   command string; 0 fabrications, 0 hangs.
3. **Undo/restore:** journal + rebase + cross-tab snapshot-replay + batch filter path.
   Exit: symmetry sweep green; scripted mixed voice+mouse scenario passes.
4. **Manifest fan-out, one tab per increment** (T1 tabs first: metabolism, review_log,
   summa; T2 adapters after: heartbeat, agents_tab). Exit per tab: coverage audit green,
   battery rows green, knowledge default file present, No-Blind-Push review.
5. **The one batched Sociogram regen** (when next justified): inline T3 bus-command
   adapter, id-addressable edge-open API (closes F5), NODES accessor or exported roster,
   semantic-fingerprint knob tier, batched group setter. Single constitutional review cycle.
6. **Facets file + FAQ re-key + provenance** (existing step-6 work, unchanged scope).

**Salvaged unchanged:** mint/WebRTC/data-channel plumbing, the response-collision latch
(single-active-response discipline — hard-won, keep verbatim), record-mix bridge, state bus
+ Sociogram responder, both stale injectors (reworded), debug harness chassis (text
injection, grid autorun, stale proof), `build_destinations.py` parser (now feeding the
resolver index, no longer a model-facing tool), knowledge/ + derive_tab_help + janitor
checks, voice pill UI.

**Deleted:** all 7 tools as tools; every routing rule in the prompt; `filter_sociogram`'s
checkbox-only semantics; `destinations.json` as a model-visible artifact.

## 14. Explicitly rejected (kill list — do not resurrect)

1. **Mid-session `session.update` tool/enum swapping.** Unexercised here, contradicts
   observed bind-at-start behavior, races the latch. The tool surface is fixed forever.
2. **Name resolution inside the regen artifact.** The hottest iteration path stays
   shell-side over the generated index.
3. **Per-tab registry/adapter boilerplate pasted inline into 12 tabs.** Shell-side except
   where a tab is regenerating anyway.
4. **Fingerprints/undo hashing continuous fields.** Semantic tier only; zoom/brightness
   excluded or quantized.
5. **Hand-authored catalogs baking volatile enums into connect-time instructions.** The
   "over sixteen hundred nodes" bug reborn inside the control channel. Names/types/verbs
   only; values resolve live.
6. **Replaying `ask` through undo/restore/sweeps.** Metered, nondeterministic, auto-flips.
7. **Reading articles through the realtime audio channel.** Page TTS with mic engineering.
8. **Static-HTML completeness gates.** The controls that matter don't exist in static
   HTML; only runtime DOM enumeration counts (else the gate is green forever — worse than
   no gate, per H4).
9. **Exact-key structural JSON as the model boundary.** Terse fuzzy strings; the
   deterministic shell absorbs the fuzziness.
10. **Retrofitting CCL into the Sociogram's native search box.** Legacy box untouched.

## 15. Why this meets the north star

"Anything a user would ordinarily do for himself" = the runtime DOM's interactive surface —
and that exact surface is what the coverage audit enumerates and diffs against the manifest
(§9). So the north star stops being an aspiration and becomes a **checkable invariant**:
any control a user can click that voice cannot reach is a loud pre-push failure, not a
discovery a user makes mid-conversation. English→command is the model's whole job;
command→action is deterministic and tested; action→spoken-truth is the write-returns-the-
read contract. Symmetry is not promised; it is swept mechanically per build.

## 16. Decisions reserved to Tom

1. **Base tree confirm:** pin redesign work to C2A2-dev `voice-guide-v2`.
2. **Authorize the ~$1 kill-switch spike** (increment 0) before any engine code.
3. **Orphan destinations** (review_log, summa_commentary, what_is_c2a2): promote into the
   tab roster so voice can reach them, or declare them outside the voice surface for v1.
4. **Undo under mixed voice+mouse:** is rebase-on-view_changed (manual changes become
   journal entries) the v1 bar, or is "undo reverses the last VOICE command and says so"
   acceptable to ship first?
5. **`read` verb:** ship v1 with mic-mute engineering, or defer until the audio collision
   is demonstrably solved? Is read/stop enough, or is paragraph addressing required?
6. **The facets vocabulary** ("philosophy traditions", "the science ones"): Tom authors the
   discipline facet file (same reservation as the palette — no agent mints tradition
   semantics), or the guide always asks.
7. **Scope of the batched Sociogram regen** (§13 item 5): which candidates earn the slot,
   and what event justifies spending the constitutional review cycle.
8. **Privacy:** may the shell log emitted command strings (and optionally raw transcripts)
   to tune the grammar and feed the usage-grounded FAQ? Voice traffic is currently captured
   nowhere; this is the standing 4b privacy gate.

---

# ADDENDUM — 2026-07-25 build day (reconciling the spec with what shipped)

> Everything above is the design as judged on 2026-07-23. In one build day the
> implementation moved past it in ways the spec does not describe, and
> spec/build drift is a named hazard in this project's constitution. This
> addendum is the reconciliation. Where it contradicts the text above, **this
> section wins**; §§1–12 remain accurate as the *rationale*.
>
> Branch `voice-guide-v2` in C2A2-dev. Verify with:
> `node scripts/test_voice_ccl.cjs && node scripts/test_voice_shell.cjs`

## A. The criterion is now stated (Tom, 2026-07-25)

**"Voice-only exploration — the full and clear design criterion for this tool."**

This sharpens the north star from "anything a user would ordinarily do" into
something with teeth, and it reclassifies existing work:

- The audit's `controls_deferred` list is **holes in the product**, not backlog.
  A mouse user routes around a missing verb; a voice-only user hits a wall.
- `what` must be able to **enumerate**, not only summarise.
- Any command that selects something must **announce what it landed on** —
  with no screen, the announcement *is* the result.
- **Asking must be rare** — well under one reply in ten. See §D.

## B. New dimensions (the model of §3 is unchanged; the roster grew)

| dimension | value | written by | notes |
|---|---|---|---|
| `cut` | absolute node-id set, nullable | `find`, `focus`, `clear` (marquee next) | Replaces the former `highlight` dimension; the search query travels *inside* the value so undo restores query + node set together. |
| `edges` / `layers` / `tags` / `bridges` | per-family boolean maps | `show/hide/only/all/none` **+ family qualifier** | Second filter families. `filters` is defined as `groupVisibility`, a *node-group* map, so nothing in the grammar could ever name an edge. Addressed by qualifier so the verb set does not grow. |
| `cursor` | position in the revealed set | `pick random\|first\|last`, `next`, `previous` | Writes through to `selection`, so undo restores the node, not an index. |
| `playback` | reading / stopped | `read`, `stop` | Drives the artifact's **own TTS**, never the realtime channel (§14.7 upheld). |
| `camera` | zoom + translate | `fit`, `zoom in\|out`, `pan left\|right\|up\|down` | Reachable but **not journaled** — §14.4 bars *hashing* continuous fields, not reaching them. |

`all` and `none` take an **optional** family qualifier, which required a new
0-or-1 argument kind in the parser.

## C. Auto-framing is an invariant, not a verb

Every reveal ends centred, with a **minimum-scale legibility floor**: below it,
centre rather than shrink, and say so. `fit` is the deliberate escape hatch and
is never floored. Rationale: a filter moved the graph's contents and left the
camera alone, so a correct reveal could put every matching node off-screen —
"revealed" did not mean "visible". Making it a verb would have made the user
responsible for remembering it, which is how the old tool bag grew.

Three implementation facts worth keeping: a rebuilt circle has no `cx`/`cy`
(the sim writes them on tick, so positions come from the bound datum); the sim
keeps moving for ~1s, so framing happens twice; and the settle re-frame is
cancelled by any user gesture, registered in the **capture phase** because
d3-zoom calls `stopImmediatePropagation`.

## D. Ambiguity policy REVERSED (supersedes §5's ask-on-ambiguous)

The spec above returns `ambiguous` and asks. In a voice-only tool the user
cannot *see* the candidate list being asked about, so a returned question costs
more than a stated assumption. **A ranked winner is now acted on**, marked
low-confidence, with the alternatives carried so the shell can say
*"taking 'su' as summa (could be summa-extra)"*. Only a genuine tie asks.

**The line that makes this safe: hedge the INTERPRETATION, never the outcome.**
What was assumed is soft; what is on screen is reported exactly. A wrong guess
is therefore visible rather than hidden, and `undo` is one word away.

Consequence for §16.6: the facets file is **no longer a gate**. Derive an index
from the corpus, speak it hedged, let Tom override. The original reservation
applied to *publishing* a claim in a static file, not to a hedged spoken guess.

## E. Enforcement gained a second half: gestures (§9 extended)

The coverage audit enumerates *elements*, so it certified "0 uncovered" while
zoom, pan and edge-click were unreachable — an entire modality invisible to the
gate. Gestures cannot be discovered, only **declared**, so the gate checks the
declaration's honesty: a status from `covered|deferred|excluded`, `covered`
naming verbs the tab **actually has in caps**, `deferred` naming its increment,
`excluded` giving a reason, and a tab declaring nothing **fails**.

`controls_deferred` is a **third category, deliberately not a synonym for
excluded**: in scope, not yet reachable, asserted as an exact count. Folding it
into `excluded` is how this gate would rot to permanent green.

## F. Verification: what the harness can and cannot see

`scripts/test_voice_shell.cjs` — headless Chrome over CDP, no npm deps, drives
`window.CCLRun` (the same entry point `run_command` uses), never touches the
voice pill, so it mints **no realtime session**. It is the pre-push gate and
runs the asset-stamp check as its last row.

**Three failures it could not have caught, all found by a human at the screen:**

1. **Bound ≠ sayable.** metabolism's metric select is labelled *Amplitude*; the
   knob id is `metric`. The audit checks controls are bound, never that they
   are speakable.
2. **Ran ≠ produced.** Filters reported the variable they had just written, so
   an empty graph read as success. *Every* filter row asserted the same state
   variable the code wrote — the tests agreed with the bug for three commits.
   **A test that reads back what the code just wrote proves nothing.**
3. **Prompt behaviour has no DOM.** Banning the model's honest disclaimer
   ("I don't have direct visual input") without supplying a truthful
   replacement produced outright fabrication — it described the user's desk,
   a plant, papers, from an audio-only session. **Never ban a truthful
   statement without supplying the truthful replacement.**

Outstanding: a **live canary row** for (3) — ask "what do you see", require the
live counts, fail on any mention of the user or the room. Costs one billed
session per run; converts this class from anecdote to measurement.

## G. Policy for mouse-only affordances

A mouse-only affordance is acceptable **only when its outcome is reachable by
name**. The marquee passes (`only` / `find` / `focus` / cursor reach the same
set) and is declared `excluded` with that reason. Each such exclusion is
individually defensible; the risk is the *third* one, after which the product
is mouse-first with a voice veneer. This policy is the check on that drift.

## H. Increment 5 (the regen) — now a measured list, not a guess

1. **Per-node cut predicate** consulted by `rebuildGraph` — top item. Makes the
   graph's own counters truthful, removes ~60 lines of shell-side enforcement,
   and lets the cut be fingerprinted, not merely journaled.
2. Addressable edge ids (closes F5, and the last deferred gesture).
3. `all` does not restore `architecture/changelog` — `toggleAll` leaves that
   subgroup off, so `all` is not quite "everything".
4. The artifact's own status line and narration still speak native semantics
   after a CCL cut ("the rest faded").
5. The 6 remaining deferred controls.

## J. Items grew three declarations (Community Explorer, 2026-07-25)

Phase 1 gave a tab ONE item spec: a selector, a label, a noun. Community
Explorer needed three things that spec could not express, and each is now a
declared property rather than a branch — which is the whole bet of the item
model, so it is worth naming what they cost.

**1. `items` may be a LIST, and a spec may carry `when`.** What is walkable
depends on which sub-view is showing: Community Explorer is a graph under one
sub-tab and a card grid under the other, and they are not the same roster. The
first spec whose `when` holds wins; one with no `when` is the fallback. The only
predicate implemented is `{"active": "<sel>"}` — the element carries `.active` —
because that is the only one a real tab has needed. Six of the thirteen tabs
have sub-views, so the alternative was six branches.

**2. `frame`.** Items are not always in the tab's own document. The cards are a
separate application one iframe deeper — same-origin, so reachable, but
`ifDoc()` is the wrong document. `specDoc(sp)` resolves it. This immediately
exposed a **fourth** instance of the "which document / which view is active"
family that already bit `activeTabSrc`, `activeTabBtn` and `activeSrc`: the
reader asked `ifDoc().contains(el)` and got false for every card, so `read`
called the card "this article". Anything asking which document must ask the
element (`ownerDocument`), not the shell. **Assume a fifth exists.**

**3. `total` — and it is a HONESTY declaration, not a convenience.** The grid
renders `CARD_LIMIT` = 60 of 1006 matching communities. A count taken from the
DOM is wrong by a factor of seventeen, and this is the same failure the graph's
counter had under a cut ("4184 of 4184 shown" over two visible nodes). `total`
names a selector and a regex over the page's OWN status line, so the number
spoken is the page's own claim: *"60 of 1006 communities here"*, and the cursor
carries it as an aside — *"1 of 60 communities (1006 in all)"* — because "1 of
60 of 1006" is unspeakable.

`plural` joined them for a duller reason: `noun + 's'` said "60 communitys".
English plurals are not a rule the shell should be inferring.

### Sub-views ride on `go`, and are resolved on UNRESOLVED
A tab's sub-views are declared as `views: [{name, aka, enter, active}]`. No new
verb — the same call §D made for tab order. Two placement notes that were not
obvious:

- Resolution happens where the engine reports **`unresolved`**, not in
  `switchTab`. `destinations.json` is a build artifact listing TABS; a sub-view
  is per-tab and live, so the engine will always hand its name back unresolved.
  That also settles precedence for free — a sub-view can never shadow a tab.
- It also runs on **`ambiguous`**: `go graph` came back ambiguous between two
  tabs *while the user was standing on the one they meant*. Being there is the
  disambiguation, so a sub-view of the active tab wins. `go` only — ambiguity in
  any other verb is a real question.

Entering a sub-view **clears the cursor**, and announces the roster when it
arrives rather than when it is asked for: the cards are a whole app that loads
on first entry, so a confident "0 communities" would be a lie with a timer on it.

### §9 enforcement now reaches into declared frames
A tab whose content is a nested app hides most of its operable surface one
document down: **21 controls in Community Explorer, 2294 in the cards frame.**
Sweeping only the tab document would have reported a clean tab while the thing
the user is looking at was entirely undeclared. `frames: [{sel, covered_by_items,
controls_excluded, controls_deferred}]` extends the sweep.

The assertion there is **"nothing UNDECLARED", not an exact count** — a
deliberate departure from §9's exact-deferred rule. The nested overview view is
a 158x11 heatmap of buttons, so an exact count would go red on every data
refresh, and a gate that cries wolf on data churn is a gate people learn to
widen. Counts are reported; undeclared controls fail. Current state: 60 covered
by items, 8 excluded, 2226 deferred, **0 uncovered**.

Two spend surfaces were **excluded rather than deferred**, which is the stronger
word: the nested app's Ask-AI pipeline (`#run-ai-query`, `#allow-external-search`
and friends) and the tab's own `#search-ai-mode`. Both bill the broker. Voice
reaches paid retrieval only through the deliberate `ask` verb, never as a side
effect of walking cards — the same rule `pinPlainSearch` enforces.

### What the harness gained
`F6b` asserts the picked card is **actually on screen in the nested frame**, not
merely tagged — it failed on first run (card at 879px in a 784px viewport,
frame scrolled 0) because `scrollIntoView` is smooth and had not landed. It
settles first, like `settledInView` does for the graph's framing. Marking an
element the user cannot see is exactly the "spoken claim with no render behind
it" this suite exists to catch.

**Not done here, deferred by name in the manifest:** the tab's own graph filters,
search and camera (increment 2); the cards app's filters, sort and its own
search (increment 2); its map / PRS / overview views (increment 3).

## K. The soft layer, made hard (Tom's live review, 2026-07-26)

Tom's first end-to-end run found four symptoms that reduce to **two root causes
and two honesty gaps**. All four were in the SHELL; none were in the item model.

### K1. `go <tool tab>` produced a state no human click can produce

The `.tab-btn` click handler set the frame and moved `.active` inside its own
row — and nothing else. A human can never reach that path, because a human
cannot click a button in a hidden row. **Voice can.** So `go sociogram` from a
chapter page loaded the Sociogram into the iframe while `#row2` stayed hidden
and `.chap-btn.active` stayed on the chapter. Everything downstream —
`activeTabBtn` → `activeSrc` → `activeManifest` — then resolved to the CHAPTER:
every graph verb answered "not available on this view" while the user was
looking straight at the graph.

The severe form is not the refusal but the **fabrication**: `what` read the
Sociogram's real filters and node counts out of the iframe and narrated them
under the title "Start here". No prompt rule can defend against that, because
the instrument itself was lying. This is the **fifth** instance of the
which-document family and the first that is a bad **write** rather than a bad
read — so the fix is `revealOwningRow()`, at the single place the state
changes, shared with `syncShellToFrame` so the two cannot drift apart again.
The drift between those two was the bug.

**Assume a sixth.** The family has now bitten `activeTabSrc`, `activeTabBtn`,
`activeSrc`, the reader's title, and the row/chapter state.

### K2. Synonyms belong in the grammar, not in the model's good intentions

`pick first` had always worked. Every way Tom actually SAID it did not:
`pick first card`, `pick first section`, `what is this` → `too_many_args`;
`open the first card` → a ten-verb word list. A guide that accepts exactly one
blessed word per intent is a command line with a microphone attached.

Leaving the paraphrase to the model was the standing design, and it is what
failed: the common phrasings then depend on the model's worst day. So the
mapping is now **data in `verbs.json`, deterministic and under test** — the
model's latitude sits ON TOP of that for genuinely novel phrasing, not
underneath it as the only line of defence (§5, "if code can answer, code
answers").

- **`filler`** — words the grammar does not need (`the`, `this`, `is`,
  `section`, `card`, `node`…). Stripped ONLY on the arity-error branch of
  `none` / `opt` / `one`, and NEVER for `text` / `many` verbs, so a search
  string, tab name or group list cannot lose a token.
- **`aliases`** — `select` / `choose` → `pick`, `search` / `highlight` →
  `find`, `quiet` → `stop`. **Context-sensitive where the word is genuinely
  ambiguous**: `open levin` still opens a node's article, `open first` moves
  the cursor, disambiguated by ARGUMENT SHAPE via `when_arg_in` — never by
  guessing.
- **`near`** — the graceful fallback when a verb has no meaning here at all:
  offered only where the near verb is really in this tab's caps.

Two invariants are enforced at grammar-compile time, so a bad declaration dies
at load with a named reason: **a filler word may not also be an enum value**
(put `out` in the list and `zoom out` becomes `missing_arg`), and **an alias
may not silently shadow a real verb** without `when_arg_in` (aliasing `back`
would have quietly broken `go back` — caught by this rule while writing it).

### K3. The reader promised an interrupt nobody had built

The bar said `say "stop" to interrupt` for a month. **Nothing routed a spoken
"stop" to `run_command`** — the prompt asked the model to "act on a clear
instruction" without ever saying that acting meant calling the tool, and a
voice model hearing "stop" reads it as barge-in on its own speech. Typed `stop`
worked, which is why it survived review. Two contradictory comments sat in the
same function, one claiming the mic stays live and the next claiming it is off.

**Tom's call: mute during reading.** The mic is muted at read start and handed
back on stop, on end, and on speech error. Consequences, stated plainly rather
than discovered later: the guide is **deaf for the whole article**, so the
on-screen **Stop reading** button is the only interrupt, and the message names
it. In exchange the guide stops listening to wiki prose read AT it — a token
cost and a live injection surface, since any sentence in an article can read as
an instruction.

A `?` beside the command bar opens reader instructions in the shell's existing
help modal. **Every sentence in that help text describes behaviour held by a
row in `test_voice_shell.cjs`** — help drifting ahead of the build is exactly
how "say stop" came to be advertised for a month.

### K4. What the harness gained, and the row that would have caught it

`D8-D10` arrive at a tool tab **by voice, from a chapter page** — which nothing
had ever done; every earlier row reached the Sociogram by clicking a button
already on screen. They assert the **resolved manifest**, not the spoken line,
because the old bug said "go Sociogram" perfectly while leaving the shell
pointing at Start Here.

`E7-E11` hold Tom's verbatim phrasings, the mic contract (spied at the
`CCLSetMic` seam, which is engine-independent), and the `?`.

Two rows were **reversed, not deleted**: `A24b` used to demand the words
`say "stop" to interrupt`, and `A24c` asserted a visible Stop button during
playback — which passed only because nothing tore the reader down when speech
FAILED, so headless it sat offering to stop a read that was never happening.

**Still not addressable, and named rather than absorbed:** `open card 1` —
numeric ordinals are not in `pick`'s vocabulary at all (`random|first|last`),
so "the third one" cannot be said; and `what is this` after a pick describes
the TAB, never the picked ITEM.

## L. The frame is the truth (second live review, 2026-07-26)

### L1. `inView` — the guide had no idea where the middle of the screen was

It reported `shown`, a FILTER result that is true no matter where the camera is
pointing, and called that visible — while the tab's own status line read **0 in
view** and Tom was looking at empty space. The count already existed; the shell
simply never passed it on.

`inView` is now **added to** `shown`, never substituted for it. The older
comment arguing for `shown` is still right — in-view alone would report a
correct filter as a small number merely because the viewport is tight — so the
two now answer their two different questions: `shown` says what the COMMAND
did, `inView` is the only thing any claim about VISIBILITY may rest on. At zero
the bar says so outright and offers `fit`. The prompt states the split, in
those terms.

### L2. The SIXTH which-document instance, and the end of that family

Start Here's "See all 15 framings" postMessages the shell to swap the frame
while the Start Here chapter button stays lit. Every reader of view identity
asked a BUTTON for its `data-src`, and a button only changes when a button is
clicked — so in-page navigation was **invisible to the shell**. The guide could
not see the new page, would not believe the user who said they had opened it,
and `read` read the OLD document's cursor.

`frameSrc()` derives identity from the iframe's actual `location.pathname`,
with the button as fallback for the moment before the frame's first load. Both
`activeSrc()` (the CCL/manifest path) and `activeTabSrc()` (where_am_i,
describe_view, the four `!== wiki_narration.html` gates) share the ONE
implementation — a second copy is precisely how these readers drifted apart
five times before. **This is the last form the family can take**: derived from
the frame, identity is right by construction no matter who navigated or how.

The last button-derived answers were in `what` itself, which named the view
"Start here (1 of 3)" while walking the framings page's sixteen sections —
correct counts under the wrong name, the same species of lie. When frame and lit
button disagree the frame wins: the page is named from its own `<title>` and a
row position belonging to another document is dropped.

`what_is_c2a2` is now a declared tab (`section.angle`, sixteen of them: fifteen
numbered framings plus a Tech appendix that shares the class). The noun is
`section`, not `framing`, so counting sixteen never contradicts the link's
promise of fifteen.

### L3. Frame history, because `location.replace` left one-way doors

`setFrame` uses `location.replace` deliberately — browser Back would otherwise
rewind the iframe while the tab bar kept its own state. The cost was that a page
reached by an in-page link had **no way back at all**, since no tab button
corresponds to it.

So the shell keeps its own stack over FRAME DOCUMENTS — the thing a user
experiences as "where I was" — with ← → in the command strip. They sit there
rather than floating over the iframe because an overlay would cover whatever the
tab puts in that corner (the Sociogram's filter panel). Moving through the stack
re-syncs the chrome, so the bar cannot disagree with the frame. **The `back`
verb rides the same stack**, or `back` would mean two different things depending
on whether it was said or clicked.

Also fixed en route: `syncShellToFrame` was bound `{once: true}`, so it ran for
the FIRST frame load only — which is why a mid-session in-page navigation left
the tab bar stale.

### L4. Harness

**Phase G** navigates by an in-page LINK, which no phase had ever done — every
earlier phase clicked a tab button, which is exactly why nothing caught this.
It asserts the resolved manifest, the spoken name, that `read` reads THIS
document, and that button and verb share one history. **A2b** holds the empty
screen: with the camera stranded, `shown` must stay unmoved while the
visibility claim flips — asserted as a relationship, not two literals, so it
keeps meaning something when an earlier row's filter state changes.

## M. L2 was only half a fix — and the harness said otherwise (Tom's recording, 2026-07-26)

Tom recorded a live session and asked whether it was a failed test of §L2. **It
was.** Standing on the fifteen-framings page, the guide said *"You're now on the
'Start here' page, under the 'intro' tab"* and then argued with him when he said
he was not. Phase G was green the whole time.

### M1. The frame truth was reached, then thrown away one function later

`activeTabSrc()` correctly returned `what_is_c2a2.html`. `tabForSrc()` searches
`TABS`, which has no entry for a page reached by an in-page link, so it returned
null — and `whereAmI()` dropped straight through to `.chap-btn.active`. The word
`intro` in the guide's answer was literally `chap.id` minus its prefix.

A page with no TABS entry and no button is **still where the user is**, so it is
now named from its own document (`<title>`, first clause). The chapter is the
answer only when there is no frame document at all. `describeView()`'s base
follows the same rule.

### M2. The real defect: ONE verb, TWO implementations

`run_command` intercepted `what` and `where` **before** `window.CCLRun` and sent
them to the bus instead. So every fix made to the CCL answer — naming the page
from the frame, dropping a row position belonging to another document, the whole
item model, `inView` — was reachable from the **typed bar** and invisible to the
**voice guide**, which is the surface that actually gets used. §2 of this
document says one code path; the perception verbs had quietly forked from it.

`what` now calls the engine FIRST and always, and **merges** the bus descriptor
when the tab supplies one. Merge, not replace: the bus is genuinely richer where
it exists (live counts, dominant cluster). The payoff is that every future
manifest declaration becomes visible to the voice guide for free, which was the
premise of the whole fan-out and had silently not been true.

### M3. The testing lesson, which is the durable one

**I asserted the path I had fixed rather than the path the user talks to.**
Phase G drives `window.CCLRun`; the guide's `what`/`where` bypassed it. Nothing
headless could reach the perception verbs at all, so the suite could not have
caught this no matter how many rows it had.

`window.VGWhere` / `window.VGDescribe` now expose them read-only (no session, no
broker, no mic — `describeView` is the same postMessage with the same 700ms
timeout the live path uses), and `G5b-G5d` + `G7a` hold them. G5c is written as
the negative the recording produced: **never** a chapter id or "Start here"
while a frame document exists.

This is the same shape as the two gaps before it — nothing had ever arrived at a
tool tab by voice; nothing had ever navigated by an in-page link. The rule that
keeps falling out: **when a fix is verified, check that the assertion runs
through the surface the user actually uses**, not merely through the function
that was edited.

## N. Links are doors, and they belong to every page (Tom, 2026-07-26)

Both content manifests EXCLUDED the page's links, with the reason *"voice
reaches those by name via `go`"*. That reason is false for every link that is
not a tab — which is most of them. "See all 15 framings" is a page, not a tab,
so `go` never could reach it, and Tom found the hole the only way left: with the
mouse.

Under the north star (*anything a user would ordinarily do can be said*),
clicking a link is not an optional per-tab extra. It is one of the two or three
most ordinary things a reader does.

### N1. Shell-side and generic, deliberately

Link-following is implemented once in the shell and works on **any** page with
no declaration and no per-tab work. Declaring it per manifest would have parked
a universal capability behind twelve fan-out increments — the same mistake as
the reader living inside one tab (§the phase-1 note).

It rides on **`go`**, resolved at the engine's `unresolved` branch **after**
tabs and sub-views — the third thing to use that seam, for the third time for
the same reason: links are live and per-page, so the engine can only hand their
names back. Resolving them last means a link can never shadow a real
destination, and precedence is settled without a rule.

### N2. Two strings per link, on purpose

Start Here's "door" links wrap a whole paragraph, and the phrase a person would
actually say ("open the review cards") sits at the END of it. So matching runs
against the anchor's FULL text, while the SPOKEN label strips trailing arrow
glyphs — "go see all 15 framings right-arrow" is what the raw text reads aloud
as — and clips at 60 characters so a paragraph does not become a sentence of
confirmation.

### N3. What is named but never followed

- **`target="_blank"`** — opens a new browser window the guide cannot see into
  or navigate; following one strands the session behind a page it cannot
  perceive.
- **Off-origin** — voice must not be a way to send someone to an external site,
  and page content is not a trustworthy instruction.

Both are still **reported by name, with the reason**, and the user is told to
open them by hand. Silently omitting them would be the old lie in a new place:
the user would hear that a link plainly on their screen is not there.

`what` now lists the followable links, because to someone who cannot see the
page an unmentioned link does not exist. In the manifests they moved from
`controls_excluded` to `dim_coverage` (dim `tab`) — covered, not excluded —
with only the genuinely unreachable ones left excluded.

## I. Still open, reserved to Tom

- **Voice**: one voice throughout; wants Anthropic *Airy* or nearest. Not
  available through this page's TTS providers (browser / Kokoro / OpenAI) —
  pick the nearest and audition.
- **§16.4 mixed-authorship undo**: the marquee makes this concrete rather than
  theoretical, since it is a large deliberate mouse edit of a voice-written
  dimension.
- **Retrieval arc**: "what does the Summa say about angels" → quick reply;
  "dig deeper" → longer, **hard 5-second turnaround enforced in code**, not
  requested of the model. **Carry the risk**: summarisation is where
  fabrication re-enters, and a summary has no DOM to check it against. Require
  quote-anchored spans; "found nothing" must be sayable.
