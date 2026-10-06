# Community Interactions

**family** prose (a frame around three instruments) · **manifest entry** NONE · **redesign candidate**

*This is the page the audit flags as genuinely amorphous — not because it is
vague in the small, but because it does not know what it is. Main document §3.1
and §7.2(a).*

## identity
`wiki/community_interactions.html`, 31,757 B, 711 lines. Chapter button
`chap-interaction` (`explorer.html:428`), also standalone. **Hand-authored** — no
generator in `scripts/` references it; git history shows hand edits
("Community Interactions: start closed, lock Level 1…", `77ff…`; "Level 4: embed
DET structure matrix", `5450285a`).

## purpose
A scaffold page that names C2A2's four levels of dialogue (intrapersonal to
meta-traditional), embeds a live instrument for each of levels 2 to 4, and lists
the project's development pathways under "The Road Ahead".

## data sources
- Three iframes, each cache-busted with `?v=Date.now()`:
  `level2_signal_stream.html` (`:354`), `intertradition-readout.html` (`:372`),
  `intertradition-matrix.html` (`:391`). Each is its own document with its own
  controls. See `21_nested_subsurfaces.md`.
- **The Road Ahead is fetched live**: `fetch('architecture/pathways.md?v=…')`
  (`:703`), parsing the `## Pathway inventory` section up to `## Bright pins`
  (~`:475-485`). Pathway links come from the markdown; bare legacy items 01-17 are
  backfilled from a hard-coded `LEGACY` map to `architecture/NN_*.md`
  (~`:433-460`). The reader pop-up fetches each pathway `.md` (`:649`).

The Road Ahead is the best thing on the page and the only part of it that is
genuinely live: it is a rendering of `architecture/pathways.md`, and its own text
says "New pathways appear here automatically".

## entities and fields
- **Level**: number, title, an `lv-where` aim line, three rows (What it means /
  Why it matters / In practice). **Level 1 is a locked "Under construction" stub**
  with no body (`onclick="event.preventDefault()"`).
- **Pathway** (parsed from `pathways.md`): `group, id` (two digits), `title,
  href, status` (drafted | outlined | pinned | deferred, plus an ISME star flag),
  `desc`.
- **Signal** (inside the Level 2 frame, not this page): `a, b, date, strength,
  weight, nature, …`.

So the page has **two entity types of its own** (level, pathway) and borrows
three more from its frames. No single record type spans it.

## cut
The page's own state is trivial and describable:

| dim | kind | binding |
|---|---|---|
| level_open | set over L2, L3, L4 | `details.level[open]`; L1 is locked |
| road_ahead_open | value, bool | `details.devpath[open]` |
| pathway | value | `.pw-link[data-idx]` |
| reader | read/action | `#reader` open state, `#reader-title`, `#reader-prev` / `#reader-next` / `#reader-close`, walking the ordered `ORDER` list |

The per-level frames are **separate documents with their own state** — the signal
matrix's cell click, the readout's two acts and 18-step playhead with an
auto-play timer, the matrix's 4 bands and 45 step cells. Those are sub-views
needing their own rosters, and the existing machinery can express them (the
Community Explorer's `frames` block is the precedent). What it cannot express is
what the *page* is: asking "what is the current view state of Community
Interactions" has no answer, because the page is a table of contents that renders
its contents inline.

## change signal
Two real ones, both inherited:
1. **A new or changed pathway in `architecture/pathways.md`** — a new id, or a
   status change in the lifecycle enum or the ISME star. That is the single source
   of truth and this page is a live view of it. Grain: one pathway.
2. **A new signal in the Level 2 `SIG` array.** Grain: one signal, or one
   pair-day.

Nothing is emitted. `architecture/pathways.md`'s mtime is the available stamp.

## export shape
None exists. Pathways CSV: `group, id, title, status, isme, href, desc` — i.e.
the parsed output of `parse()` (~`:475-490`), which is already a structured
record set nobody can get out. Signals belong to the frame, not here.

## narration
The page is mostly prose: lede, per-level text, "In practice" rows, and the
"A note on construction" box (~`:326-410`). Shell `descriptions` entry
(`explorer.html:1034-1036`, "A scaffold for the four levels of dialogue C2A2
cares about, and a live rendering of where the project is heading…"), voice words
at `:1929`, and `voice_guide/knowledge/community_interactions.default.md`.
**Level 1 has no prose beyond one aim line** — a declared gap on the page itself.

## current capability
Contract: none. No `c2a2Ask`, no export, no in-page "?" (the embedded readout has
per-outcome "?" buttons, which the page's own prose advertises at ~`:362`).
Shell `descriptions` entry present. **No manifest entry** — `community_interactions`
is absent from the 9, so `activeManifest()` returns null and the shell falls back
to generic caps, on a chapter button that sits in the top row.

## what resisted description
1. **The page contradicts its own embed by a factor of two.** Its prose says
   "743 such signals to date" (~`:346`); the frame it embeds says "1611 signals
   across 87 tradition pairs" (`level2_signal_stream.html:58-59`). A page that
   cannot keep its own count straight is the audit's working definition of a page
   that does not know what it is for.
2. The ISME note says "presentation July 8-10, 2026" — a past date as of
   2026-10-04.
3. The real controls inside the three iframes were covered separately, not here
   (undocumented, not amorphous).
4. The pathway status taxonomy beyond `drafted/outlined/pinned/deferred`, and
   whether `parse()`'s regexes still match current `pathways.md` content, were
   not checked against live data.

**Judgement.** The three embeds each deserve their own manifest entry; the
Level-2 Signal Stream deserves promotion to a tool tab (it is the project's best
layer-2 candidate, `21_nested_subsurfaces.md`); and the remainder of this page is
the project roadmap, which is a legitimate and useful thing for it to be. Saying
so would let Level 1's emptiness stop being a defect and become an honest "not
built yet" on a roadmap page.
