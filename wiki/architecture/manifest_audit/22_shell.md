# The shell — `wiki/explorer.html`

Not a content page, but it has real state, and **four of the five layers would
actually live here**. This entry is the inventory of what already exists to be
reused, because the single most expensive mistake available is rebuilding any of
it.

## identity
`wiki/explorer.html`, 377,365 B, 6,394 lines. The entry page. **Hand-authored**,
with library code split out into `lib/c2a2-commandline.js` (94,679 B),
`lib/c2a2-plots.js` and `lib/c2a2-search.js` (`:2887`, `:6147`).
`scripts/generate_community_explorer.py` generates a different page, not this one.

## purpose
The tabbed frame that hosts every content page as an iframe, and carries the
shared search, back/forward, voice guide, help and record controls.

## data sources
- `voice_guide/verbs.json`, `destinations.json`, `manifests.json` (`:2952-2954`,
  all `?v=Date.now()`).
- `voice_guide/knowledge/*.md` (`:6159-6219`), `voice_guide/grounding.json`
  (`:6231`), `voice_guide_faq.json` (`:2000`).
- A broker via `lib/c2a2-search.js` (`C2A2Search.callBroker`, used `:6246-6256`)
  for planning, plan memory and realtime sessions (`:1985`).
- `localStorage` for a device id (`:1966`).

## entities and fields
Chapters `chap-intro | chap-community | chap-education | chap-tools |
chap-interaction` (`:424-428`); sub-tab rows `#row2` (`:450`) and `#row2-edu`
(`:465`) of `.tab-btn[data-src]`; iframe `#content-frame` (`:477`); the voice
table `TABS` (`:1925-1940`); the `KNOWLEDGE` map (`:6159`); the `descriptions`
map for "?" (`:1026-1130`).

## cut
The shell has real dimensions, but its honest cut is "which page, and that page's
cut".

| dim | kind | binding |
|---|---|---|
| chapter | value, 5 | `.chap-btn.active`; `setActiveChapter` (`:565`) |
| tab | value | the visible row's `.tab-btn.active`; `visibleRowButtons` (`:5953`), `activeTabBtn` (`:5919`) |
| **frame** | value | the iframe's pathname — `frameSrc` (`:527`), `activeSrc` (`:3208`). **This, not the buttons, is the truth.** The comment at `:510-530` calls the button-reading bug "the sixth instance" of itself. |
| history | read/action | `navStack` / `navIdx`; `navRecord` (`:689`), `navGo` (`:700`) |
| search text | value | `#ask-input` |
| cut | value | `cutIds` / `cutQuery`; `readCut` (`:3501`), `writeCut` (`:3564`), `applyCut` (`:3440`) — shell-enforced on a tab's graph |
| cursor | value | `execCursor` (`:4284`), journal (`:2943`) |
| transient | — | voice session (mic, speaking), reader state (`CCLReaderState` `:4573`), ask-drawer open/closed, help modal, record modal |

Nothing persists except the device id. **The frame-vs-button distinction is the
single most repeated bug class in the project's own commentary** (six recorded
instances, §L2 and §M of `voice_guide_redesign.md`), and it is a direct
consequence of having the page identity in two places. A manifest with one
`identity.key` resolved from `frameSrc` removes the whole family.

## change signal
None. The shell does not poll or subscribe. The frame `load` listeners
(`:669, 712, 2909, 6014`) only re-sync chrome. The only `subscribe` in the file is
`C2A2Plot.subscribe` for hand-changes to a plot (`:5388-5426`).

## export shape
Not defined for content. The only downloads are the test-grid markdown
(`downloadResults` `:1812`, `copyResults`) and the voice recording (`:994-1003`).

## narration
`Speaker` (`:4519-4542`, Web Speech API) driven by `speechScript` (`:4512`); the
realtime voice is `VoiceGuide` (`:1221`, OpenAI realtime over WebRTC through the
broker).

## current capability
The hidden CCL engine is the important part: `#ccl-bar` / `#ccl-input` /
`#ccl-result` are retained but **retired as a visible surface** (`:484-491`,
comment "RETIRED as a visible surface"), with `CCLRun` at `:5961` exported at
`:6006`. Voice still drives it. So the command layer exists, is tested
(`scripts/test_voice_shell.cjs`, 364 rows), and is invisible to users.

---

## What each layer can reuse — functions and lines

### 1. Search
- Search UI `#ask-input` (`:435`), `#ask-go`, `#ask-clear` (`:434-438`), wired at
  `:6382-6390`, exposed as `window.C2A2AskBox` (`:6390`).
- Router `CommandLine.routeRequest` (`:6340`) — query → direct or plan.
- Command runner `run` / `CCLRun` (`:5961` / `:6006`).
- Page-local item search: `searchSpec` (`:3994`), `searchHits` (`:3996`),
  `execSearch` (`:4024`).
- **The tab contract**: `tabFindApi` (`:3496`) calls `c2a2Find`/`Clear`/`ReadCut`;
  a page defining the trio gets `evalCutExpr` (`:3515`), `applyCut`, `readCut`,
  `writeCut`. Only `wiki_narration.html` answers.
- Page-agnostic helpers: `itemSpec` (`:3611`), `domItems` (`:3728`),
  `pageLinks` / `followableLinks` / `matchLinks` (`:3670` / `:3699` / ~`:3705`).
- Cross-page: `findDestination` (`:2145`) over `destinations.json` (`:2136`);
  grounding (`:6234`) over `grounding.json`.

**Assessment: layer 1 is ~80% built and blocked on 7 pages not answering the
contract, not on shell work.** The one shell-side change worth making is
decoupling "a page has a readable cut" from "a page has `c2a2Find`", since five
pages have working search and no contract.

### 2. Subscriptions — **nothing exists; only building blocks**
- Frame `load` hooks (`:712, 2909, 6014`).
- `manifests.json` fetch with `?v=` cache-bust (`:2954`).
- `localStorage` device id (`:1966`).
- The journal `CL.createJournal` (`:2943`).
- `C2A2Plot.subscribe` (plot hand-changes only).

There is **no change feed and no "last seen" marker on any page**. The two
working implementations are both inside content pages (Metabolism's staleness
banner, the Heartbeat's 60 s poll), so the shell work is to generalise *them*,
not to design from scratch.

### 3. Explainer "?" popups
- `showHelp` (`:1011`), the `descriptions` map (`:1026-1130`) keyed by page src,
  `help-modal` / `closeHelp`; buttons `#btn-help` (`:459`), `.btn-help-row`
  (`:472`); reader-help modal `showReaderHelp` / `#ccl-readhelp` (`:441`).
- Alternative text source: the knowledge `.md` files via `pageKnowledge`
  (`:6215`).

Two defects to fix with the manifest rather than by hand: (a) the map has **no
entry** for start_here, what_is_c2a2, what_is_saying, whos_who, interT_study or
study_shell; (b) **`showHelp` picks its src from the active chapter or tab, not
from the frame** (`:1013-1025`), so it is stale after any in-page navigation —
the frame-vs-button bug again, this time in the "?" layer. The
`community/index.html` entry (`:1040`) appears unreachable for the same reason
(inferred).

### 4. Export — **nothing for content**
Reusable pieces: `domItems` / `CCLItems` (`:3728` / `:6040`) to enumerate a
page's items; `speechScript` (`:4512`) for page text; `readCut` (`:3501`) for the
cut; `activeManifest` for field and dimension names; and the Blob + anchor-click
download pattern at `:1816-1819` to copy. Also worth copying from a content page:
Community Cards' filtered CSV/JSON writer (`community/app.js:1326-1332`).

### 5. Voice guide — the layer that carries the architecture
- `VoiceGuide` (`:1221`); TTS reader `Speaker` (`:4519`).
- `TABS` (`:1925`), `whereAmI` (`:2366`), `describeView` (`:2391`) which posts
  `c2a2-voice` `describe_view` into the page (`:2415`).
- Verb dispatcher `execute` (`:5025`) with `execKnob`, `execRead`, `execCursor`,
  `execCamera`, `execFilters`, `execShell`.
- **Knob machinery** — the manifest consumer: `activeManifest` (`:3216`),
  `knobBind` (`:3233`), `readKnob` (`:3248`), `writeKnob` (`:3261`), `execKnob`
  (`:5490`), `tabViews` (`:4066`), `itemSpec` (`:3611`).
- `navGo` (`:700`) / `CCLNavGo` (`:719`); `frameSrc` / `CCLFrameSrc`
  (`:527` / `:536`); `activeSrc` (`:3208`).
- `KNOWLEDGE` (`:6159`) and `pageKnowledge` (`:6215`).
- `enterView` / `announceView` (`:4144` / `:4166`).
- The planner `C2A2Plan` (`:6259`) and `C2A2PlanMemory` (`:6258`).

**The decisive reuse argument**: `activeManifest` → `knobBind` → `readKnob` /
`writeKnob` → `execKnob` is already a generic "read and write any declared
dimension of any page" engine, with write-returns-the-read enforced
(`:5486-5490`). Export, subscription and explainer text are all *reads* of the
same declarations. Layers 2, 3 and 4 are, architecturally, three new consumers of
one existing engine.

## what resisted description
The shell's state is not serialisable as a single cut: it is chrome plus history
plus a voice session. That is the right answer, not a gap — the proposed schema
should not give the shell a `cut` block at all, only `identity` and
`capability`.
