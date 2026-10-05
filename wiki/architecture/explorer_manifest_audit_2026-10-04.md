# Explorer manifest audit — first pass

*Written 2026-10-04. Read-only audit of every published Explorer surface, as the
evidence base for the five-layer plan (search, subscriptions, explainers, export,
voice guide) and for a possible site redesign. No page, generator or test was
modified. Per-surface entries are in `manifest_audit/`.*

*Commissioned by Tom with the standing instruction that this is judgement work,
not extraction. Where this document states an opinion it says so and gives the
evidence; where it is inferring rather than reading it says "(inferred)".*

---

## 0. Headline findings, in order of how much they should change the plan

1. **The manifest already exists, under another name, and is 9 of 24 surfaces
   complete.** `wiki/voice_guide/manifests.json` (89.8 KB, `version: 1`) is a
   per-page manifest with `tier / caps / knobs / items / views / frames /
   filters / families / camera / gestures / dim_coverage / controls_deferred /
   controls_excluded`. It is consumed by two independent readers already — the
   shell builds the active tab's command context from it
   (`explorer.html:3216` `activeManifest`), and the coverage audit fails the
   pre-push gate when a live control is neither a bound knob nor an explicit
   exclusion (`manifests.json:_about`). The five-layer plan should **extend this
   file**, not start a new one. Starting a new one would make seven page tables
   instead of six (see finding 2).

2. **There are already SIX hand-maintained page tables, in three key
   namespaces, and no two of them agree.** This is the strongest argument for
   the single manifest, and it holds independently of whether any of the five
   layers ever gets built.

   | table | where | n | keyed by |
   |---|---|---|---|
   | `TABS` | `explorer.html:1926` | 14 | voice key |
   | `manifests.json.tabs` | `voice_guide/manifests.json` | 9 | voice key *or* filename, mixed |
   | `descriptions` ("?" text) | `explorer.html:1026-1130` | 13 | path-with-dirs |
   | `KNOWLEDGE` | `explorer.html:6159` | 16 | basename |
   | `destinations.json.tabs` | `voice_guide/destinations.json` | 13 | voice key |
   | `FIND_TABS` | `scripts/test_voice_shell.cjs:2487` | 8 | path-with-dirs |

   Concretely: `curriculum_tools` is `summa_explorer.html` in `TABS`, `summa_explorer.html`
   in `descriptions` and `KNOWLEDGE`, `curriculum_tools` in `manifests.json` and
   `destinations.json`, and absent from `FIND_TABS`. `rc_sandbox` is in five tables
   and its `KNOWLEDGE` value is literally `null`. `community/index.html` has a "?"
   entry that `showHelp` can never reach, because `showHelp` resolves the community
   chapter to `community_explorer.html` before looking the key up
   (`explorer.html:1013-1025, 1040`) (inferred). The manifest's own comment at
   `explorer.html:3201-3202` admits the dual road: "The TABS `key` IS the manifest
   key, so match the active data-src's filename (or the key)".

3. **The surface count is roughly double the working assumption.** The brief said
   "~11 tabs/pages". There are **14 tab/chapter surfaces, 5 door-reached frames
   that are not tabs, 5 nested sub-surfaces inside other pages, 2 build-input
   templates, 9 orphaned/stale/dead files, and the shell** — 34 tracked HTML
   files under `wiki/`, of which **24 are live surfaces a user can reach**. Four
   of the five "capability layers" would therefore have 24 consumers, not 11.
   Enumeration method and completeness claim: §1.

4. **`c2a2ReadCut` is not the pivot primitive, and on the one page that
   implements it, it does not describe the current view state.** The hypothesis is
   half right and the half that is wrong matters. §4 has the evidence; the short
   version is that `c2a2ReadCut()` returns `{query, ids}` — the *highlight* — and
   nothing about the filters (`generate_visualization.py:3669`, written only by
   `noteCut()`/`clearCut()` off `SEARCH_CUT`, `:1024`). The filters live in
   `groupVisibility`, and the thing that actually returns the view state is
   `buildDescriptor()` → `describe_view` (`:4151`). The spec already knows this:
   §6 of `voice_guide_redesign.md` defines `what` as `describe_view` **⊕ the
   manifest dimensions' `read()` values**. So the real pivot is the **declared
   dimension set**, and `c2a2ReadCut` is one dimension's reader that has been
   mistaken for the whole. The hypothesis survives with that substitution and
   two additions (§4.3, §4.4).

5. **The pages are not homogeneous, but they need one schema with a `family`
   discriminator, not five schemas.** Five families, §5. The two that break the
   current model are the **readers** (cut is an *address*, not a filter) and the
   **charts** (dimensions are not independent — Metabolism's `metric` select is
   clamped by `view`).

6. **Layer 2 (subscriptions) has almost nothing to stand on, and exactly three
   pilot candidates.** Nothing in the project subscribes to anything today. Only
   three surfaces carry a change stamp at all: AI Heartbeat (a 60-second client
   poll that already renders "New data available (N new)",
   `heartbeat/app.js:742-760`), Metabolism (an in-page staleness banner driven by
   `_meta.t_max_event`, the only page that warns about its own freshness), and the
   Level-2 Signal Stream (`prototypes/level2_build_meta.json` plus
   `LAG_WARN_DAYS=21`). Everything else is a frozen corpus whose only honest
   change signal is "a regen happened". §6.

7. **Layer 4 (export) has exactly one working implementation, and it is nested
   two frames deep and unreachable from the shell.** The Community Cards app has
   `#download-csv`, `#download-json` and `#copy-share-link`
   (`community/app.js:1326-1332`), filtered by its live cut. The manifest
   *excludes* those controls from voice. Two pages have a print-to-PDF view
   (Summa Commentary's `?print=1&from=N&to=M`, the only linkable cut-as-URL in
   the project; the Heartbeat's lens-filtered `window.print()`). Nothing else
   exports anything. The shell's only download is a test-grid markdown blob
   (`explorer.html:1812`).

---

## 1. Enumeration — method, and the completeness claim

Four independent enumerations were crossed:

1. `git ls-files 'wiki/*.html' 'wiki/*/*.html' 'wiki/*/*/*.html'` → **34 tracked
   HTML files**. Because the repo publishes to GitHub Pages from the tracked tree,
   "tracked" is the publishable set. 100+ untracked HTML files exist under
   `wiki/review/` (daily review pages in `_superseded/`, `_trash/`,
   `_deleted_quarantine/`) and are *not* published.
2. The shell's own buttons: `.chap-btn[data-src]` and `.tab-btn[data-src]`
   (`explorer.html:424-428, 452-457, 467-471`) → 5 chapters, 11 tool/education tabs.
3. The shell's voice table `TABS` (`explorer.html:1926-1940`) → 14 entries, which
   is the union of the chapter and tab rows minus the two chapter buttons that are
   pure row-switchers (`chap-education`, `chap-tools`).
4. Every `<iframe>` and `data-src` *inside* content pages, plus every
   `data-target` door handled by the shell (`explorer.html:722-775`) → the nested
   sub-surfaces and the non-tab doors.

Each of the 34 tracked files was then grepped for inbound references across
`wiki/**/*.html` and `scripts/` to classify it.

**Completeness claim.** The set of *published* surfaces is complete with respect
to the tracked tree, which is what GitHub Pages serves. Two caveats:
`wiki/architecture/` contains 746 entries including `.fuse_hidden*` artefacts and
~500 `.bak` files, and three HTML files live there (`ecosystem_diagram.html`,
`lowlevel_architecture.html`, `metrics/prs_created_vs_delivered.html`) which are
published but reachable only by typed URL or `target="_blank"`. And
`wiki/review_log.html` (6.84 MB) is a live door-reached surface that this audit
only triaged — it did not get a full manifest attempt. That is a stated gap, not
a tidy table.

### The roster

**A. Tab and chapter surfaces (14)** — the `TABS` array.

| key | label | file | authored |
|---|---|---|---|
| `start_here` | Start here | `start_here.html` | hand |
| `community_explorer` | Community Explorer | `community_explorer.html` | generated (`scripts/generate_community_explorer.py`) |
| `community_interactions` | Community Interactions | `community_interactions.html` | hand |
| `sociogram` | Sociogram | `wiki_narration.html` (63 MB) | generated (`c2a2-wiki-narration/scripts/generate_visualization.py`) |
| `narrative_connectome` | Narrative Connectome | `prs_3d.html` (1.2 MB) | generated (`c2a2-prs-3d/.../generate_prs_3d.py` from `template_prs_3d.html`) |
| `agent_map` | Agent Map | `agents_tab.html` | hybrid (hand shell + injected `TELEMETRY` block) |
| `metabolism` | Metabolism | `metabolism/metabolism_view.html` (1.2 MB) | generated (`metabolism/scripts/build_metabolism_view.py`) |
| `curriculum_tools` | Curriculum Tools | `summa_explorer.html` | hand |
| `inter_tradition_study` | Inter-Tradition Study | `interT_study.html` | generated (`scripts/build_study.py` from `study_shell.html`) |
| `rc_document_explorer` | RC Document Explorer | `rc_document_explorer.html` (1.76 MB) | **generator lost**; baked artifact, script-patched |
| `rc_sandbox` | RC Sandbox | `rc_sandbox_notebook.html` (1.78 MB) | **generator lost**; baked, patch-maintained |
| `physics_explorer` | Physics Explorer | `physics_explorer.html` | hand |
| `trv_commentary` | TRV Commentary | `commentary-explorer/commentary_explorer.html` (11 MB) | generated (`commentary-explorer/scripts/generate_html.py`) |
| `ai_heartbeat` | AI Heartbeat | `heartbeat/index.html` | hand page + generated data |

**B. Door-reached frames, not tabs (5).** Reached by a `data-target` postMessage
from Start Here, handled at `explorer.html:722-775`, which calls `setFrame()` and
hides the tab rows while leaving `chap-intro` lit.

`what_is_c2a2.html` · `what_is_saying.html` · `whos_who.html` ·
`summa_commentary.html` (3.95 MB) · `review_log.html` (6.84 MB)

**C. Nested sub-surfaces inside other pages (5).** Each is a separate document
with its own controls and no manifest entry of its own.

`community/index.html` (the Cards directory, iframed by Community Explorer) ·
`level2_signal_stream.html` (913 KB, iframed by Community Interactions Level 2) ·
`intertradition-readout.html` (Level 3) · `intertradition-matrix.html` (Level 4) ·
`wiki_narration.html#agents` (the Sociogram re-iframed inside both Agent Map and
Curriculum Tools, ~25-29 MB each time)

**D. Build inputs, never served (2).** `study_shell.html` (the template
`build_study.py` substitutes into) · `c2a2-prs-3d/template_prs_3d.html` (the
template the PRS generator must be run against; `assumptions.md:3409` and
`SPEC_prs_time_axis_2026-08-27.md:104` both warn the generator is not idempotent
and must never be run against the built page).

**E. Orphaned, stale or dead (9).** Detail in `manifest_audit/23_non_surfaces.md`.
`site_guide.html` · `master/C2A2_master_wiki.html` · `prs_3d_debug.html` ·
`test_load.html` · `architecture/ecosystem_diagram.html` ·
`architecture/metrics/prs_created_vs_delivered.html` ·
`inbox/Resurrecting Civility — Document Explorer.html` ·
`inbox/rc_sandbox/quodlibet_notebook.html` · (plus `architecture/lowlevel_architecture.html`,
which is live but reachable only via `target="_blank"` and so structurally
invisible to the guide).

**F. The shell (1).** `explorer.html` (377 KB) — not a content page, but it has
real state and it is where four of the five layers would actually live. Entry:
`manifest_audit/22_shell.md`.

---

## 2. Coverage matrix — 24 live surfaces × 5 layers

`●` implemented · `◐` partial, or present but not wired to the shared layer ·
`○` absent · `–` not applicable

Column definitions, so the marks are checkable:

- **Search** = defines `window.c2a2Find` + `c2a2Clear` + `c2a2ReadCut`, the
  contract the shell's `tabFindApi` looks for (`explorer.html:3496`).
  `◐` = the page has its own working search but does not expose the contract.
- **Subscribe** = anything a watcher could poll for "this changed", at any
  grain. `◐` = a freshness stamp exists; `●` = the page itself detects and
  announces change.
- **Explain** = a "?" entry in the shell's `descriptions` map, or an in-page
  explainer popover. `●` = both or a shell entry; `◐` = in-page only.
- **Export** = a control that writes a file the user keeps.
- **Voice** = a `manifests.json` entry (`●` complete-ish, `◐` present but thin,
  or knowledge file only with no manifest entry).

| surface | search | subscribe | explain | export | voice |
|---|:--:|:--:|:--:|:--:|:--:|
| Sociogram | ● | ◐ | ● | ○ | ● |
| Narrative Connectome | ○ | ○ | ● | ○ | ● |
| Agent Map | ○ | ◐ | ● | ○ | ◐ |
| Metabolism | ○ | ◐ | ● | ○ | ◐ |
| Curriculum Tools | ○ | ○ | ●* | ○ | ◐ |
| Inter-Tradition Study | ○ | ◐ | ○ | ○ | ◐ |
| RC Document Explorer | ◐ | ○ | ● | ○ | ◐ |
| RC Sandbox | ◐ | ○ | ● | ○ | ○ |
| Physics Explorer | ◐ | ○ | ● | ○ | ◐ |
| TRV Commentary | ○ | ○ | ● | ○ | ◐ |
| AI Heartbeat | ◐ | ● | ● | ◐ | ◐ |
| Community Explorer (graph) | ◐ | ○ | ● | ○ | ● |
| Community Interactions | ○ | ○ | ● | ○ | ◐ |
| Start here | – | ○ | ○ | ○ | ● |
| What's it doing? | – | ○ | ○ | ○ | ● |
| What's it saying? | – | ○ | ○ | ○ | ● |
| Who's Who | – | ○ | ○ | ○ | ○ |
| Summa Commentary | ◐ | ○ | ○ | ◐ | ○ |
| Review Log | ? | ◐ | ○ | ○ | ○ |
| Community Cards (nested) | ◐ | ○ | ●† | **●** | ◐ |
| Level-2 Signal Stream (nested) | ○ | ◐ | ○ | ○ | ○ |
| IT Readout (nested) | ○ | ○ | ◐ | ○ | ○ |
| IT Matrix (nested) | ○ | ○ | ○ | ○ | ○ |
| Shell (`explorer.html`) | ◐ | ○ | ◐ | ○ | ● |

`*` Curriculum Tools has a "?" entry, but its text describes a different page:
`explorer.html:1049-1050` talks about a 471-page tome and a daily-synthesis
progress tracker, which is RC Document Explorer. A wrong explainer is worse than
a missing one, and the single manifest is what would have made that impossible.

`†` Community Cards has a `descriptions` entry keyed `community/index.html` that
`showHelp` cannot reach (finding 2).

`?` Review Log was triaged, not manifested. Stated gap.

### Totals

- **Search**: 1 of 24 on the contract. Five more have a working page-local search
  that the shell cannot read. `FIND_TABS` expects the contract on 8 surfaces, so
  7 rows are red by design, and that red is the only honest instrument in the
  project for this layer (commit `13eb8468`: "364 rows, 357 pass, 7 red = the
  seven pending contract tabs").
- **Subscribe**: 1 of 24 announces change; 5 carry a stamp; 18 have nothing.
- **Explain**: 13 shell entries, 4 in-page explainers, 1 of which
  (Community Explorer's Graph-vs-Cards popover) is the only explainer in the
  project generated from a declared source-of-truth doc
  (`architecture/explorer_tabs_complementarity.md`, mirrored by
  `generate_community_explorer.py:204`). That one is the pattern to copy; note it
  can still drift, and has: the popover says "156 communities", the graph file's
  `meta.node_count` says 155.
- **Export**: 1 real (nested, unsurfaced), 2 print-to-PDF, 0 at tab level.
- **Voice**: 9 manifest entries for 24 surfaces; 17 knowledge files; 2 state
  buses (the Sociogram's `describe_view`/`view_changed`, and the plot bus). Every
  other knowledge file says, in its own frontmatter, `volatile: none -- NO state
  bus on this tab`.

**The honest reading of this matrix**: four of the five layers are at or near
zero on 20+ surfaces, one layer (voice) is at roughly 40% and carries all the
architectural thinking, and the per-page work already done for voice is the only
reason a manifest plan is credible at all. Build the manifest by **finishing the
voice manifest and widening its schema**, and the other four layers become
readers of it. Build it as a new artefact and the project acquires a seventh
disagreeing table.

---

## 3. What resisted description

This is the section Tom asked to be the most valuable, so it is deliberately not
tidied. Three of these are genuinely amorphous — there is no fact of the matter
about what a "cut" is on them. The rest are undocumented, which is a different
and cheaper problem.

### 3.1 Genuinely amorphous — no cut exists to describe

**Community Interactions.** The page itself is four `<details>` and a
markdown-fed list, which is describable. What resists is the page's *identity*:
it is a frame around three unrelated instruments (a signal matrix, an 18-step
animation, a 40-step matrix), each a separate document, none manifested, none
sharing an entity type. Asking "what is the current view state of Community
Interactions" has no answer, because the page is a table of contents that renders
its contents inline. Its own prose contradicts its own embed — the page says
"743 such signals to date" while the frame it embeds says "1611 signals across
87 tradition pairs". A page that cannot keep its own count straight is a page
that does not know what it is for. **Verdict: amorphous because mis-scoped, and a
redesign candidate (§7.2), not a manifest-entry problem.**

**Metabolism's time axis.** Not that the page is vague — its four controls are
the cleanest declared surface in the project, swept 4/4. What resists is that the
*obvious* dimension is absent and cannot be added by declaration. The x-axis is
hard-wired to the full history (`t0 = floor(meta.t_min)`,
`t1 = ceil(meta.t_max_event || meta.t_max)`); there is no brush, no date select,
no zoom. So "the current view state" of a time-series page excludes time. Worse,
the four controls that do exist are **not independent**: `setControls(view)`
disables all five `yield_*` metrics unless `view === 'wave'` and silently resets a
selected one to `events`; `color` only exists in raster; `logy` is hidden in
raster and inert for wave+yield. The §3 dimension model is a set of *independent*
assignments, and this page is a small dependency graph. **Verdict: the model needs
`requires` / `clamps`. Evidence this matters: `execKnob` already re-reads after
writing (`explorer.html:5486-5490`) precisely so the guide never reports the value
it asked for when the tab clamped it — the runtime already copes with the problem
the schema does not name.**

**The Agent Map schedule view.** A canvas playhead over a 7-day cycle
(`TOTAL_MIN = 7*24*60`). The playhead is a position in an animation, not a filter
and not an address: pausing at minute 4,312 is not a state anyone would subscribe
to, export, or narrate. The Explorer sub-view on the same page is a perfectly
ordinary filtered, sorted table. **Verdict: one page, two surfaces, and the
schedule half has no cut worth declaring. Declare the table; mark the animation
`kind: action` with `inverse: null`, which §3 already provides for.**

### 3.2 Undocumented, not amorphous — describable once someone looks

**The Sociogram's cut is split across two stores and no call returns both.**
Filters are only reachable through `groupVisibility` / `activeFilters()`; the
highlight only through `c2a2ReadCut()`. There is no "read the whole cut" call on
the one page that is supposed to be the reference implementation. See §4.

**RC Document Explorer has the data for a cut and does not expose it.** The
extraction ran (`wiki/inbox/rc_tome/tome_extract_log.md`, V1-V8 PASS, SHA-256
`9ecb26fa…`) and produced `tome_units.csv` with `unit_id = tome:pPPPhHHsSS` per
paragraph. Only ~15 `u-tome-…` ids made it into the DOM. Heading anchors
(`#pNNN-slug`) exist and are stable but are truncated to ~44 chars and **are not
unique**, and the ToC click handler `preventDefault`s, so `location.hash` is never
written. So the page's address is real, computable, and unreachable. Also: the
spec `SPEC_tome_extraction.md` still says "NOT YET EXECUTED" while the log says it
passed. **Undocumented, and the cheapest high-value fix in the audit.**

**RC Sandbox is the opposite case — it has the richest cut in the project and
nobody knows.** It already serialises its entire view state to `localStorage` as
`qn = {s, q, r, v, x:[unchecked leaf ids]}`, already computes a prose read-out of
the current cut into `#hits` ("N of 2,191") and `#scope`, and already writes
addresses back with `history.replaceState`. That is `c2a2ReadCut`,
`describe_view` and a URL-serialisable cut, all present and none exposed. What
genuinely resists: **its generator is lost** (`handoffs/explorer-roadmap.md`:
`~/gen_html.py` "GONE"), so the 1.78 MB of baked DOM is now maintained by
idempotent patch scripts. You cannot regenerate the page you most want to change.

**TRV Commentary's filters are in-memory only and its address is not serialised.**
`satKindShown` / `chapShown` / `thinkerShown` / `summaShown` / `onlyConnected`
compose cleanly in `satVisible`, and nav frames `{nodeId, crumbLabel}` exist in
`navStack`. Nothing is written to a hash or storage. Describable; just never
described.

**Who's Who is the only prose page with a real record set, and it is invisible to
every layer.** `whos_who.json` is 18 people × 7 fields, declared "single source of
truth", already consumed by `scripts/build_grounding_index.py:16,70`. The page has
no manifest entry, no `KNOWLEDGE` entry, no "?" entry, and no export — yet it is
the one prose surface where CSV export and search are trivially meaningful.

### 3.3 Where description failed because I could not open the thing

- **`review_log.html`** (6.84 MB, live, door-reached from `start_here.html:183`,
  regenerated by `scripts/refresh_review_log.sh`). Triaged only. Its entity grain
  (review cards? days?) and its cut are unknown to this audit. **This is a
  finding, not a gap to guess around: the second-largest live surface in the
  project has no manifest entry, no knowledge file (confirmed:
  `SPEC_voice_faq_key_migration_2026-08-28.md:98`), no "?" entry, and no audit.**
- **Count disagreements I could not reconcile.** The Narrative Connectome's live
  file parses to 962 triplets; `manifests.json` says 507; `voice_guide_redesign.md`
  §T says 453; `SPEC_prs_time_axis_2026-08-27.md` says 642. These are four
  different dates and no page states its own build date in a place a reader can
  see. **A manifest with a `count_source` field would have made all four
  self-checking.**
- **Whether the two inbox duplicates differ from their live descendants** — not
  diffed (`inbox/Resurrecting Civility — Document Explorer.html` vs
  `rc_document_explorer.html`; `inbox/rc_sandbox/quodlibet_notebook.html` vs
  `rc_sandbox_notebook.html`).
- **Which scheduled job refreshes the Heartbeat.** The launchd plist is a
  template with the `StartInterval` vs `StartCalendarInterval` choice left to the
  installer, so the actual cadence is unverified even though the data is clearly
  current (2026-10-03).

### 3.4 Two things that are broken rather than undescribed

Both were found while attempting manifest entries, which is itself an argument
for the exercise.

1. **Level-2 Signal Stream's strength filter cannot select 58% of its records.**
   `#fStrength` offers Moderate / Strong / Speculative / High. 938 of 1,611
   signals carry strength `Unlabeled`, which has no option. They appear under
   "all" and are unselectable alone. The cut literally cannot express the majority
   of the data.
2. **Curriculum Tools' "?" text describes RC Document Explorer**
   (`explorer.html:1049-1050`), and the Agent Map's telemetry is currently stale
   with a recorded FAIL (`agents/openstory/REFRESH_STATUS.md`: sandbox
   `useradd: No space left on device`, Mac-shell fallback auto-declined, last PASS
   2026-10-04T10:15Z). The page shows baked numbers with no on-page indication
   that the feed did not refresh — unlike Metabolism, which does warn. Same
   failure class, opposite handling, on two adjacent tabs.

---

## 4. The ReadCut hypothesis — tested, and the verdict

> **Hypothesis as posed:** `c2a2ReadCut` is the pivot primitive. A page that can
> describe its current view state as named dimensions can be exported (the
> description *is* the export query), narrated, and subscribed to.

### 4.1 The second clause holds, and it holds strongly

A page that can name its view state as dimensions can be exported, narrated and
subscribed to. The evidence is positive and comes from the project's own best and
worst cases sitting side by side:

- **Community Cards** declares nothing to the manifest but *does* hold its cut in
  one place, and it is the only surface in the project with a working CSV and
  JSON export — and the export is cut-filtered
  (`c2a2_community_explorer_filtered.csv`, `app.js:1326-1332`). The description
  *was* the export query, built by someone who was not thinking about manifests
  at all. That is the hypothesis holding by accident.
- **RC Sandbox** holds its whole cut in `localStorage.qn` and already renders a
  prose read-out of it into `#hits`/`#scope`. Export and narration are both one
  function away.
- **Summa Commentary** writes its address to `location.hash` and accepts
  `?print=1&from=N&to=M`. The one page whose cut is a URL is the one page with a
  cut-filtered PDF.
- Against: **Narrative Connectome**'s search "only dims meshes" and keeps no
  query and no hit list. No readable cut → no export, no narration of the search,
  and the manifest has to declare `find` undeclared (§T, "Deliberately NOT
  declared"). Its own plot hook says so in data: `cuts: false`
  (`template_prs_3d.html:1618`).

So the *architectural* claim is confirmed three times over and falsified nowhere.
Proceed on it.

### 4.2 The first clause is wrong as stated, and the error is load-bearing

`c2a2ReadCut` is **not** the primitive. On `wiki_narration.html`, the only page
that implements it:

```
window.c2a2ReadCut = function() { ... }   // generate_visualization.py:3669
// returns SEARCH_CUT -> { query, ids } | null       (:1024)
// "null = nothing cut. Written only by noteCut()/clearCut()"
```

It returns the **highlight** and nothing else. The filters — which group
checkboxes are on, which is the dimension that actually determines what is on
screen — live in `groupVisibility` and are read by `activeFilters()`. The thing
that returns the view state is a different function on a different road:
`buildDescriptor()` (`:4151`), answered over `postMessage describe_view`,
returning `{selected, filters, counts:{passingNodes, inViewNodes, totalNodes, …},
legend, dominant}`.

So: **`clear` followed by `c2a2ReadCut()` returns `null` on a page showing 412 of
4,211 nodes behind 27 switched-off filters.** "Nothing cut" and "a heavy cut" are
indistinguishable through this primitive. An export built on it would export
everything. A subscription built on it would never fire.

Two further pieces of evidence that the primitive is the wrong unit:

- `getCurrentViewState()` (`:3678`) exists *alongside* it as a lossy scrape of
  node opacities, i.e. the project already needed a second reader and built a
  worse one.
- The harness found exactly this class of lie: `test_voice_shell.cjs:2555` records
  that on the scrape road a search matching **nothing** read back as "5102 nodes
  shown", because `deriveLitIds` reads "nothing dimmed" as "everything lit". The
  bar then reported the opposite of what happened. The contract road was built to
  fix *that*, and it fixed the highlight only.

### 4.3 What the pivot primitive actually is — and the spec already says so

`voice_guide_redesign.md` §6 defines perception as:

> `what` = merged `where_am_i` + bus `describe_view` … **⊕ the manifest
> dimensions' `read()` values**

That is the real primitive: **the declared dimension set, each with a `read` and a
`write`, whose union is the cut.** `c2a2ReadCut` is one dimension's reader
(`highlight`). `describe_view` is an optional, per-page, 700 ms-timeout
convenience. The manifest is the only thing that knows the *whole* list.

**Restated hypothesis, which this audit endorses:**

> A page that **declares** its view state as named dimensions with readers and
> writers can be exported (the dimension reads *are* the export query), narrated
> (the dimension names and labels *are* the sentence), and subscribed to (a
> semantic-fingerprint subset of the dimension reads *is* the change key).

This is a stronger claim than the original and it is cheaper, because the
declaration already exists for 9 surfaces and the machinery to consume it already
exists in the shell (`activeManifest`, `knobBind`, `readKnob`, `writeKnob`,
`execKnob`, `tabViews`, `itemSpec`, `domItems`).

### 4.4 Two extensions the evidence forces

**(a) `address` is a kind, alongside `value | set | action | read`.** Seven of the
24 surfaces are readers whose current view state is a *position*, not a filter:
RC Document Explorer, RC Sandbox, Summa Explorer, Summa Commentary,
Inter-Tradition Study, Physics Explorer, TRV Commentary's page view. For these,
"the cut" is `{document, section, scroll}`, and the useful questions are *is the
address stable* and *is it linkable*. Today:

| surface | anchor | stable | unique | hash written |
|---|---|:--:|:--:|:--:|
| Summa Commentary | `#day-N` | yes | yes | **yes** (`replaceState`) |
| RC Sandbox | `#rNcM`, `#row-N` | yes | yes | **yes** (`replaceState`) |
| RC Document Explorer | `#pNNN-slug`, `#page-N` | yes | **no** (truncated) | no |
| Physics Explorer | concept id | yes | yes | no |
| Curriculum Tools | `I.Q1.A1` in data only | yes | yes | no |
| Inter-Tradition Study | `#doc=<key>` + slug | yes | ~ | yes |
| TRV Commentary | node id + page | yes | yes | no |

Summa Commentary and RC Sandbox are the reference implementations and nobody has
noticed. An `address` block with `{anchor_pattern, linkable, hash_written}` makes
the four "no" rows a one-line gate failure instead of an undiscovered gap.

**(b) `requires` / `clamps` between dimensions.** The §3 model treats dimensions
as independent assignments. Metabolism's four knobs are not (§3.1). Curriculum
Tools already needed a workaround for the same thing — its manifest carries
`requires_knob: {id: 'articles', v: 'on', why: "with it off, a question click
jumps to an article instead of expanding, so `open` would have two meanings"}`.
So the relation is already in the data, invented once, locally, under a different
name. Promote it to a first-class field and Metabolism's interlock becomes
declarable instead of a comment.

### 4.5 One thing the hypothesis does not buy

The description is the export query **only for data pages**. On a reader, the
address describes *where you are*, not *what you'd want out*. Exporting
"paragraph 412 of the Tome" is not useful; exporting "all units under heading
p221-slug" is. So readers need the export grain declared **separately** from the
cut: `export.records[].grain` with `filter_by_cut: false`. The identity
"description = export query" is a property of F1/F2/F5 (graphs, charts, tables),
not of F3 (readers). Shipping one export mechanism on the assumption it is
universal would produce useless exports on seven surfaces.

---

## 5. Are the pages homogeneous enough for one schema?

**No, and yes.** They fall into five families with genuinely different cuts, but
the differences are expressible as *required blocks per family* within one
schema, discriminated by a `family` field. One schema, five profiles. Not five
schemas, which would reintroduce the six-tables problem at the schema level.

### F1 — Graph instruments (5)
Sociogram · Narrative Connectome · Community Explorer (graph) · TRV Commentary ·
Level-2 Signal Stream

Cut = **filter sets ∧ selection ∧ camera ∧ highlight**. Items are addressable
(nodes, triplets, cells). The existing schema fits with no changes; this is the
family it was designed for. Required blocks: `filters`, `items`, `camera`,
`families`.

The one internal split: **DOM-backed vs data-backed rosters**. The Sociogram
leaves SVG circles behind that `revealedNodes` can read; the Narrative Connectome
is one `<canvas>` with WebGL meshes and no per-node DOM (§T: "THE FIRST TAB WITH
NO ELEMENTS TO WALK"). That is already handled by declaring dotted paths
(`meshes`, `userData.triplet.id`, `visible`) instead of selectors, so it is a
`source: dom | data` field, not a family.

### F2 — Chart / series views (2, plus one orphan)
Metabolism · Agent Map (schedule half) · `metrics/prs_created_vs_delivered.html`

Cut = **interdependent knobs**, no addressable items, `items.kind: none`.
Required: `requires` / `clamps`. **Missing and should be added: a `window`
dimension.** A time-series page whose cut excludes time is the clearest
"page that doesn't know what it's for" in the audit, and it is the page with the
*cleanest* declared surface — which is the lesson: a complete sweep of the
controls that exist is not a complete description of the state that matters.

### F3 — Readers over a corpus (7)
RC Document Explorer · RC Sandbox · Curriculum Tools · Summa Commentary ·
Inter-Tradition Study · Physics Explorer · (TRV Commentary's page view)

Cut = **address** ± a ToC-scoped text filter. Required: `address`, and
`export.records` declared independently of the cut (§4.5). This is the largest
family, the one the current schema serves worst, and the one where a single
shared component would pay most: all seven have a left-hand roster, a
right-hand body, a filter over the roster, and a scroll-spy or equivalent. Four
of the seven have a *lost or absent* generator.

### F4 — Prose / door pages (6)
Start here · What's it doing? · What's it saying? · Who's Who ·
Community Interactions · (Site Guide, orphaned)

Cut = **nothing beyond `{page, scroll}`**. The three that already have manifest
entries are honest about this and say so in their own `_caps_note`s — "A content
tab: no graph, so no filters/cut/camera". `what_is_saying`'s
`controls_excluded: []` is argued as a *positive* claim ("no `target=_blank`
links, no markdown overlay, no buttons"), which is exactly right and is the
template for this family. Required blocks: almost none — `items` (the walkable
sections), `narration`, and a `no_cut: true` assertion so that silence is never
mistaken for an unfinished entry. **These pages should get a deliberately minimal
profile, not a padded full one.** Note one real hole: the *doors* are the entity
here (what leads where), and nothing declares the door graph even though the shell
implements it at `explorer.html:722-775`.

### F5 — Record tables (4)
Community Cards · Agent Map (Explorer half) · Who's Who · AI Heartbeat (Pulse)

Cut = **text filter ∧ facet sets ∧ sort ∧ page size**. Required: `sort`,
`pagination`. This family is where export is trivial and already half-built
(Cards does it), where search is trivial (all four have a working local box),
and where subscription is most natural (all four are keyed record sets). **It is
also the family the voice manifest serves worst** — Agent Map's entry has
`dim_coverage: [{dim: 'tab'}]` and five `controls_deferred`, i.e. the sortable,
filterable table is declared as "a tab you can go to". If one family gets the
first full pass, it should be this one: four surfaces, five layers, and the
lowest cost per layer in the audit.

### A cross-cutting structure the families miss

Three surfaces are the *same page* re-iframed: `wiki_narration.html` is the
Sociogram tab, the Agent Map's sociogram sub-view (`#agents`, ~25 MB) and
Curriculum Tools' sociogram sub-view (~29 MB). Same document, three presets,
three loads. The schema needs `route.preset` and `route.parent`, or the manifest
will say three contradictory things about one file — which is precisely how the
six-table problem started.

---

## 6. Layer 2 (subscriptions) — what the ground actually supports

Nothing subscribes to anything today. The shell has no change feed, no "last
seen" marker on any page, and no poll; its only `subscribe` is
`C2A2Plot.subscribe` for hand-changes to a plot (`explorer.html:5388-5426`).
What exists is five freshness stamps, of three different kinds, on five surfaces.

| surface | stamp | kind | cadence | already warns? |
|---|---|---|---|---|
| AI Heartbeat | `digest.json.generated_at`; `snapshots/index.json.sort_key` | content signature + 60 s client poll | ~daily (launchd template) | **yes** — "New data available (N new)" |
| Metabolism | `_meta.t_max_event`, `_meta.t_max`, `db_mtime` | derived data edge | regen daily 05:00, publish Sun 06:30 (launchd) | **yes** — "no OpenStory events for Nd — ingest is down, not the artifact" |
| Level-2 Signal Stream | `prototypes/level2_build_meta.json` (1,611 signals, latest 2026-09-23) | record count + latest date | manual regen, `LAG_WARN_DAYS=21` | script-side only |
| Agent Map | `TELEMETRY._meta.generated`, `REFRESH_STATUS.md` | build stamp + PASS/FAIL | daily refresh, **manual publish** | **no** (currently FAIL, page silent) |
| Sociogram | `build_meta.json` (node/link counts, `nodes_by_group`) | per-regen aggregate | per regen, delta-guarded | regen script only |

Three observations that should shape the layer:

1. **Two pages already solved this, differently, and neither knows about the
   other.** Metabolism distinguishes "the pipeline is dead" from "the artifact is
   old" and says so on the page; the Heartbeat detects new data client-side and
   offers a refresh. Those are the two halves of a subscription layer, built
   independently, on adjacent surfaces. The manifest's `change` block should be
   the *generalisation of those two*, not a new design.

2. **Change grain is per-surface and mostly coarse.** Only four surfaces have a
   keyed, dated, growing record set where a per-record subscription is meaningful:
   Level-2 Signal Stream (per signal, `a/b/date`), AI Heartbeat (per signal,
   keyed by `url`, with `first_seen_at`), Summa Commentary (per day, 1-307), and
   Agent Map (per agent `last_seen`). Everything else is a frozen corpus — the
   Tome is a historical document, TRV is a scanned book, the DET matrix is a
   published algorithm — and for those the only honest signal is "a regen
   happened", which is a `grain: regen` declaration, not a failure.

3. **The pilot set is Level-2 Signal Stream + AI Heartbeat + Metabolism.** They
   are the only three with a dated, moving record set *and* an existing stamp.
   The Level-2 stream is the most interesting of the three and the least
   surfaced: 1,611 dated cross-tradition signals across 87 pairs, growing, and it
   is nested inside a `<details>` on a page with no manifest entry whose prose
   claims 743 of them. **Opinion: if layer 2 ships on one surface first, ship it
   there, and promote the page to a tab while doing it.**

---

## 7. Redesign candidates, with the evidence

Flagged in descending order of how much the audit's evidence supports the call.

### 7.1 Cut (9 files, ~4 MB of published dead weight)

| file | why |
|---|---|
| `site_guide.html` | Orphaned — nothing links it. `explorer.html:561` comment: "site_guide.html documents a phantom one". `fact_inventory.md:109,113`: "largely counterfactual". It is a 27 KB published document describing a chapter tab that does not exist. |
| `prs_3d_debug.html` | 194 KB, orphaned, superseded by `prs_3d.html`; `SESSION_SUMMARY_2026-08-27.md:124` already says "untrack". |
| `test_load.html` | A node-array loading fixture, published, zero inbound references. |
| `master/C2A2_master_wiki.html` | April 2026, light theme, never regenerated; the `.md` twin is what everything references. `STATE_OF_PROJECT_2026-05-08.md:61,77` already asks to pick one format. |
| `inbox/Resurrecting Civility — Document Explorer.html` (1.88 MB) | Initial-commit original of the live RC Document Explorer, untouched since 2026-04-07. |
| `inbox/rc_sandbox/quodlibet_notebook.html` (1.67 MB) | Superseded predecessor of `rc_sandbox_notebook.html`. |
| `architecture/metrics/prs_created_vs_delivered.html` | June snapshot with no scheduled regenerator found. |
| `physics_explorer_candidate_2026-04-02.html`, `_2026-05-01.html` (repo root, untracked) | Superseded candidates; untracked so not published, but they confuse the roster. |

This is bookkeeping, not architecture — but it is bookkeeping that makes the
manifest's `status` field meaningful on day one instead of a field nobody fills.

### 7.2 Merge / rescope (3 calls)

**(a) Community Interactions should either become a real tab with declared
frames, or dissolve.** It is reached as a chapter button, has no manifest entry,
and its content is three independent instruments nested in `<details>` plus a
live markdown-fed pathway list. The pathway list is genuinely good and genuinely
live (it fetches `architecture/pathways.md` and backfills legacy ids). The three
embeds each deserve their own entry. **Opinion: promote Level-2 Signal Stream to a
tool tab, keep the Readout and Matrix as declared frames, and let the remainder
become what it actually is — the project roadmap page.** Supporting evidence: the
page's own prose disagrees with its own embed by a factor of two (§3.1).

**(b) Three readers over one Summa corpus.** `vault/synthesis/Day-NNN -
… - Contemporary.md` is read by Curriculum Tools (as a per-article pane), by
Summa Commentary (307 days, door-reached, not a tab), and by TRV Commentary (267
`summa-day-NNN` satellites baked into an 11 MB bundle). Three UIs, one corpus,
three different addresses for the same text, and only one of them (Summa
Commentary) writes a linkable hash. **Opinion: this is one surface with three
views, not three surfaces. Merging is a bigger job than this audit can price, but
the manifest should at minimum declare the shared corpus so the duplication is
visible in data rather than discoverable only by reading three generators.**

**(c) The Sociogram is loaded three times at 25-63 MB.** As the Sociogram tab
(63 MB), as Agent Map's sociogram sub-view (~25 MB), and as Curriculum Tools'
(~29 MB). Declaring `route.preset` would at least make the reuse legible; sharing
one load would be a performance project.

### 7.3 Rebuild (2 calls, both because the generator is gone)

**RC Sandbox** — highest value, and the recommendation this audit is most
confident about. The page already has the best cut in the project (serialised to
`localStorage.qn`), a prose read-out of that cut, and stable anchors it writes
back. It is 1.78 MB of baked DOM whose generator is **GONE**
(`handoffs/explorer-roadmap.md`), maintained by two idempotent patch scripts. The
upstream data survives (`inbox/rc_sandbox/assignments.csv`,
`tl_sandbox_cells.json`, `cell_dates.json`, `TL_sandbox_reordered.md`), and
`gen_notebook.py` is already *planned*. Rebuilding it from data would make it the
cheapest surface in the project to give all five layers at once, and would
convert the project's best-designed cut from an accident into a reference
implementation.

**RC Document Explorer** — rebuild the *addressing*, not the page. The extraction
already ran and produced per-paragraph `unit_id`s; ~15 of them reached the DOM.
Stamping the remaining 1,091 and writing `location.hash` on ToC clicks would turn
a 1.76 MB opaque reader into an addressable, exportable, narratable corpus. Also
fix the heading-id truncation collision, and update `SPEC_tome_extraction.md`,
which still says "NOT YET EXECUTED" about work that passed V1-V8.

### 7.4 Fix, not redesign (4 one-liners found while auditing)

1. Curriculum Tools' "?" text describes RC Document Explorer
   (`explorer.html:1049-1050`).
2. Level-2's strength filter has no `Unlabeled` option while 58% of records are
   Unlabeled.
3. Agent Map shows baked telemetry with no staleness notice while
   `REFRESH_STATUS.md` records a FAIL — Metabolism, next door, handles the same
   case correctly.
4. Community Explorer's Graph/Cards popover says 156 communities; the graph file
   says 155. The popover is a mirror of
   `architecture/explorer_tabs_complementarity.md` and has drifted from the data,
   which is the exact failure a `count_source` field prevents.

---

## 8. Proposed manifest schema

This is `manifests.json` v2: every v1 field is kept (so the shell and the
coverage gate keep working), the key namespace is unified, and five blocks are
added — one per layer, plus `identity`. Blocks marked **[new]** do not exist
today; everything else is present in v1 and listed so the proposal is a diff, not
a replacement.

```jsonc
{
  "schema": "c2a2-page-manifest/2",
  "version": 2,
  "pages": {
    "<page_key>": {                  // [new] ONE namespace. The six tables
                                     // collapse into this key. Every other
                                     // table becomes a derived view.

      // ---- identity ------------------------------------------------ [new]
      "identity": {
        "key":        "rc_sandbox",
        "title":      "RC Sandbox",            // as printed in the UI
        "aka":        ["quodlibet notebook", "tl sandbox"],   // v1 `aka`
        "path":       "wiki/rc_sandbox_notebook.html",
        "route": { "kind": "tab|chapter|door|nested|standalone|build_input",
                   "parent": "<page_key>|null",   // nested surfaces
                   "selector": ".tab-btn[data-src=...]",
                   "data_src": "rc_sandbox_notebook.html",
                   "preset": null },              // the Sociogram-thrice case
        "authored":   "hand|generated|hybrid|lost",
        "generator":  { "script": "...", "inputs": [], "regen": "...",
                        "idempotent": true },
        "status":     "live|stale|dead|build_input|test_fixture",
        "family":     "graph|chart|reader|prose|table",  // the §5 discriminator
        "tier":       "T1"                               // v1
      },

      // ---- purpose -------------------------------------------------- [new]
      "purpose": "One sentence, human-authored, what this page is FOR.",

      // ---- data ----------------------------------------------------- [new]
      "data": {
        "sources": [ { "path": "...", "mode": "baked|fetched|broker",
                       "note": "" } ],
        "counts":  [ { "name": "cells", "value": 2191,
                       "source": "#hits" } ]     // kills the 4-way count drift
      },

      // ---- entities ------------------------------------------------- [new]
      "entities": [ { "name": "cell", "id_field": "cell_id",
                      "fields": ["row","seq","node","voice","date_lo","text"] } ],

      // ---- cut -------------------------------- (v1 core, extended) --
      "cut": {
        "dims": [ { "name": "sections", "kind": "set",       // + "address" [new]
                    "read": "<path or fn>", "write": "<path or fn>",
                    "label": "", "aka": [], "values": [],
                    "fingerprint": "semantic|continuous",
                    "requires": [], "clamps": [] } ],        // [new] §4.4b
        "address": { "anchor_pattern": "#r{row}c{col}",       // [new] §4.4a
                     "stable": true, "unique": true,
                     "hash_written": true, "scroll_tracked": false },
        "serialize": { "read_fn": "window.c2a2ReadState",     // [new]
                       "write_fn": "window.c2a2WriteState",
                       "storage_key": "qn", "url_param": null },
        "no_cut": false,                                      // [new] F4
        "items": {}, "views": [], "frames": [],               // v1, unchanged
        "filters": [], "families": [], "camera": {}           // v1, unchanged
      },

      // ---- change ---------------------------------------------- [new] L2
      "change": {
        "grain": "record|section|node|regen|none",
        "key_field": "cell_id",
        "stamp": { "path": "...", "field": "_meta.generated" },
        "detect": "poll|content_signature|count_delta|file_mtime|none",
        "cadence": "daily 05:00 launchd",
        "staleness_warn_days": 21,
        "announces_on_page": false,       // Metabolism/Heartbeat = true
        "subscribable": true
      },

      // ---- export ---------------------------------------------- [new] L4
      "export": {
        "records": [ { "name": "cells", "grain": "cell",
                       "columns": [], "filter_by_cut": true } ],
        "existing": [ { "control": "#download-csv", "format": "csv" } ]
      },

      // ---- explain --------------------------------------------- [new] L3
      "explain": {
        "shell_entry": true,                      // the `descriptions` map
        "source_of_truth": "architecture/explorer_tabs_complementarity.md",
        "mirrored_in": "scripts/generate_community_explorer.py:204",
        "in_page": [ { "anchor": "#tabs-help", "topic": "graph vs cards" } ]
      },

      // ---- narration ------------------------------------------- [new] L5
      "narration": {
        "knowledge_file": "voice_guide/knowledge/rc_sandbox.default.md",
        "page_prose": [ { "selector": "#about", "role": "lede" } ],
        "needs_writing": true
      },

      // ---- capability: OBSERVED, not aspirational -------------- [new]
      "capability": {
        "find_contract": "none|partial|full",
        "ask": false, "state_bus": false, "describe_view": false
      },

      // ---- coverage (v1, unchanged) ---------------------------------
      "caps": [], "knobs": [],
      "dim_coverage": [], "controls_deferred": [], "controls_excluded": [],
      "gestures": {},
      "swept": { "at": "2026-10-04", "total": 84, "uncovered": 0 }
    }
  }
}
```

### Why these fields and not others

- **`identity.key` is the whole point.** Six tables exist because six places each
  invented a key. Every one of them can be *generated* from this block:
  `TABS` from `route`, `destinations.json` from `identity` + `items`,
  `descriptions` from `explain`, `KNOWLEDGE` from `narration.knowledge_file`,
  `FIND_TABS` from `capability.find_contract`. That is the acceptance test for
  v2: **no hand-maintained page table survives it.**
- **`capability` is observed, `caps` is declared.** Keeping them separate is what
  lets the gate say "this manifest claims `find`, the page does not define
  `c2a2Find`" — which is the check `FIND_TABS` performs by hand today for eight
  rows.
- **`data.counts[].source`** exists because four documents give four different
  triplet counts for one page (§3.3). A count with no stated source is a rumour.
- **`change.announces_on_page`** records which pages already solved §6, so the
  layer generalises two working implementations instead of inventing a third.
- **`cut.no_cut: true`** is a positive assertion for F4. `what_is_saying`'s
  entry already argues this way in prose; the schema should let it be data, so
  that silence remains a gate failure and honesty is cheap.
- **Nothing here replaces `voice_guide/knowledge/*.md`.** Those are prose for a
  model to read; the manifest points at them. Keeping prose out of JSON is why
  the voice layer's text has stayed good.

### Suggested order of work

1. **Unify the key namespace and generate the five derived tables.** No new
   capability, and it removes the failure mode that produced a "?" popup
   describing the wrong page. This is also the only step that pays off even if
   the five layers are never built.
2. **Fill `identity` + `purpose` + `capability` for all 24 surfaces.** Most of it
   is in `manifest_audit/` already.
3. **F5 first for the layers** (Community Cards, Agent Map table, Who's Who,
   Heartbeat Pulse): four surfaces, trivial export, trivial search, natural
   change grain, and one working export already to copy.
4. **Layer 2 pilot on Level-2 Signal Stream**, generalising Metabolism's and the
   Heartbeat's two existing mechanisms.
5. **`address` + F3**, starting with RC Document Explorer's unit ids.
6. **`requires`/`clamps` + a `window` dimension for Metabolism.**

---

## 9. Per-surface entries

In `manifest_audit/`. Each attempts the ten fields of the brief against the real
files, and each ends with what resisted.
