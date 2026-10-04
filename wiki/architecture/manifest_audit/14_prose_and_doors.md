# Prose pages and door-reached frames

Six surfaces, grouped because five of them have genuinely nothing to describe and
saying so briefly is the honest output. The sixth (Summa Commentary) is a reader
and is the project's reference implementation for a linkable cut.

All the doors are reached by a `data-target` postMessage from Start Here, handled
at `explorer.html:722-775`, which calls `setFrame()` and hides both tab rows while
leaving `chap-intro` lit. **A consequence worth recording: on a door page
`activeSrc()` returns the door's filename while `.chap-btn.active` is still
`chap-intro`, so `activeManifest()` and `showHelp()` can disagree about which
page you are on.** `manifests.json` documents this for `what_is_c2a2` in a
`_reached_note`; it is undocumented for `whos_who`, `summa_commentary` and
`review_log`, which have no entries at all.

---

## Start here
`wiki/start_here.html`, 10,383 B. Chapter button `chap-intro`
(`explorer.html:424`), the shell's default; also the "back" target of
what_is_saying, what_is_c2a2 and whos_who. Hand-authored.

**Purpose**: front door that asks three questions (What's this? / Who's who? /
So what?) and hands each to another page.

**Data**: none. **Entities**: links with `data-target` (`:123, 132, 169, 183,
192`) and one plain link to `whos_who.html` (`:166`). Targets: `saying`,
`fifteen`, `sociogram`, `review-cards`, `summa-commentary`.

**Cut**: nothing beyond `{page, scroll}`. The three manifest-declared "sections"
are walkable items, not state. **The manifest entry is honest** — `knobs: []`, no
filters/views/camera/families, `dim_coverage` one row (`tab`, matching
`a[href], a[data-target], a[onclick]`), `controls_excluded` `a[target=_blank]`,
gestures scroll + link_click (covered by `go`) + hover (excluded, "transient; no
state").

**Change / export**: none; a flat list of section headings plus door links.

**Narration**: shell-side — `speechScript` (`explorer.html:4512`) reads
`section.section` items; `knowledge/start_here.default.md` (3,017 B).

**Capability**: no `c2a2*`, no export, **no shell `descriptions` entry** (so the
"?" button has nothing to say about the front door). Manifest entry yes (T1),
knowledge file yes, `KNOWLEDGE` entry at `:6166`.

**Resisted**: nothing. The one real gap is that **the doors are the entity here** —
what leads where — and nothing declares the door graph, even though the shell
implements it at `:722-775`.

---

## What's it doing? (`what_is_c2a2`)
`wiki/what_is_c2a2.html`, 41,953 B. The "What's this?" right-hand door
(`data-target="fifteen"`, handler `explorer.html:735-740`); also reached from
what_is_saying's navstrip (`:130, 450`). Hand-authored.

**Purpose**: seventeen expandable cards answering "what is C2A2 doing?", one per
structure/function framing, plus an open card and a Tech appendix.

**Data**: inline prose. A markdown slide-in panel fetches raw `.md` vault files
over HTTP (`:710-730`, marked.js from CDN). `openTool()` links click the *parent
shell's* `.tab-btn` (`:683-697`) — a cross-frame navigation the manifest has to
know about.

**Entities**: 17 `section.angle` blocks, each with an accent colour, an index in
the h2, and tool links; one `.angle.open` (`:630`); one appendix (`:654`) linking
`architecture/lowlevel_architecture.html` (`:665`, `target="_blank"`).

**Cut**: nothing beyond `{page, scroll}`; the doc overlay is a transient modal.
Manifest honest — `knobs: []`, `dim_coverage` `tab` only, `controls_excluded` for
`a[target=_blank]` ("raw .md vault files opened in a NEW BROWSER WINDOW") and
`#doc-close`. **One gap: its gestures list only scroll and hover, omitting
`link_click`**, which start_here and what_is_saying both declare, even though this
page has `openTool` links. A coverage sweep that checks gesture declarations would
catch it.

**Change / export**: none. A card count that went 16→17 is visible only by diff
(the manifest's `items._note` says so).

**Narration**: `speechScript` + `knowledge/what_is_c2a2.default.md` (3,686 B).

**Capability**: no `c2a2*`, no export, no `descriptions` entry; manifest entry
and knowledge file yes (`:6166`). Not a tab, not in `TABS`, not in
`destinations.json` — the manifest's `_reached_note` says so.

**Resisted**: nothing.

---

## What's it saying? (`what_is_saying`)
`wiki/what_is_saying.html`, 24,418 B. The left door of Start Here's section 1
(`start_here.html:123`, `data-target="saying"`, handler `explorer.html:741-750`);
also reached from what_is_c2a2's navstrips (`:239, 674`). Hand-authored (a
`what_is_saying_DRAFT.html` and a spec exist upstream at repo root).

**Purpose**: twelve "medium : message" pairs showing what each of the system's
media is saying.

**Data**: none — **no `<script>` at all**, confirmed by grep. **Entities**: 12
`section.pair` blocks (`:136-431`), the last `.pair.open`; two navstrips
(`:129-130, 449-450`).

**Cut**: nothing, not even a toggle. **The manifest entry is the template for
this family**: `controls_excluded: []` is argued as a *positive* claim — "no
`target=_blank` links, no markdown overlay, no buttons" — rather than left as an
empty array that could mean "unfinished". That distinction is what the proposed
`cut.no_cut: true` field generalises (main document §8).

**Change / export**: none; a list of `{n, medium, message}`.

**Narration**: `speechScript` + `knowledge/what_is_saying.default.md` (4,077 B).

**Capability**: manifest entry, knowledge file, `KNOWLEDGE` entry
(`explorer.html:6167`). Nothing else.

**Resisted**: nothing. One cosmetic defect: the title says "Eleven Media" and
there are 12 sections (inferred cosmetic).

---

## Who's Who
`wiki/whos_who.html` (6,095 B) + `wiki/whos_who.json` (6,984 B). Linked from
Start Here (`start_here.html:166`) as a **plain link with no `data-target`**, so
the frame simply navigates and the shell's door machinery is bypassed. The page
has a "Back to Start Here" link. Not a tab, not in `TABS`, not in the manifest,
not in `KNOWLEDGE`, no `descriptions` entry.

**Authored**: HTML hand-authored, renders the JSON at load (**runtime fetch**,
fails gracefully on `file://`). The JSON is hand-edited and billed as "single
source of truth".

**Purpose**: a roster of thinkers, one blurb and one get-to-know-them link each.

**Data**: `whos_who.json` — `_comment`, `sections[2]`, `people[18]`. **Also
consumed by `scripts/build_grounding_index.py:16,70`** (the voice grounding
index) and `scripts/rc_sandbox_figures_check.py:18`;
`wiki/rc_sandbox_figures.json` merges 13 entries from it.

**Entities**: Person — `name, full, section, order, blurb, link, linkLabel`.
Section — `key, title, note`; the two are traditions and companions. (The section
title says "fifteen thinker-traditions" while `people` has 18; the per-section
split was not counted.)

**Cut**: nothing beyond scroll. **But this is the one prose page with a real
record set** — a flat, ordered, sectioned list of 18 × 7 — which makes it the one
prose page where search and CSV export are trivially meaningful.

**Change**: edit the JSON; its mtime. No per-entry date field.
**Export**: the JSON *is* the export; CSV would be 18 rows × 7 columns.

**Narration**: none — no knowledge file, no `KNOWLEDGE` entry. The voice
`grounding.json` is built from the JSON, so the *entity names* are grounded even
though the *page* is not (inferred from the script header).

**Capability**: nothing. No manifest entry, no "?" entry, and because
`chap-intro` stays lit, `activeSrc()` returns `whos_who.html` while
`activeManifest()` returns null — the same class of mismatch the manifest
documents for what_is_c2a2.

**Resisted**: nothing. **Judgement: the cheapest five-layer win in the project.**
18 records, a declared source of truth, an existing consumer, no page state to
model.

---

## Summa Commentary
`wiki/summa_commentary.html`, 3,948,545 B. **Not an explorer tab** (confirmed
absent from the `data-src` rows, `explorer.html:460-477`). Reached by door only:
`data-target="summa-commentary"` (`explorer.html:760-766` →
`setFrame('summa_commentary.html?v=…')`, hides both tab rows, lights the intro
chapter). The door is Start Here's "So what?" card (`start_here.html:192`,
"Open the Summa commentary"). Also listed in `site_guide.html:217, 236`,
`knowledge/start_here.default.md:29`, `voice_guide/destinations.json`, and
referenced by `wiki_narration.html` nodes.

**Authored**: generated by `scripts/rebuild_summa_commentary.py`, whose docstring
says the page "is opened from the Start Here 'So what?' card". **The original
generator was never committed**; the script only appends missing days to the baked
blob (default APPEND-MISSING, `:2-40`), with a faithfulness self-check that
aborts on mismatch. The template shell is hand-authored, and since the script
edits in place with `--html`, **the HTML itself is the source of truth** — there
is no separate template.

**Purpose**: a day-by-day reader of the one-year Summa reading plan's
"Contemporary Parallels" commentary, with a part-grouped table of contents and a
print-to-PDF export of a day or a range.

**Data**: baked. `<script id="data" type="application/json">` at `:213` holds 307
entries `{day, title, part, partName, md}`, days 1-307, from
`wiki/vault/synthesis/Day-NNN - <title> - Contemporary.md` (last present file
Day-307). A minified markdown lib is inlined at `:211`. No fetch.
**Shared corpus with Curriculum Tools and TRV Commentary** — see
`05_curriculum_tools.md` and main document §7.2(b).

**Entities**: day entry as above; `partName` ∈ Introduction, Prima Pars, Prima
Secundae, Secunda Secundae, Tertia Pars, Supplementum (short codes Introduction,
I, I-II, II-II, III, Suppl). `md` sections include "Frame".

**Cut** — **the reference implementation**:

| dim | kind | binding |
|---|---|---|
| day | address, int | `#day-N` hash; `render(day)` (`:321-332`), `currentDay()` parses `/^#day-(\d+)$/` (`:374`), `hashchange` listener (`:389`), and **`history.replaceState` writes it back (`:332`)** |
| filter | value, text | `#filter`, substring over `title + 'day N' + partName` (`:336-338`), 120 ms debounce — narrows the ToC only, not the reader |
| part collapsed | set | `collapsed[partName]`, toggled by `.part-head` (`:350`) |
| print range | value pair, **in the URL** | `?print=1&from=N&to=M[&auto=0]` (`:215-236`) |
| actions | action | `#pdf-btn`, `#pdf-go`, `#pdf-from`, `#pdf-to` (`:187-193, 394-440`); print view `#pv-print` |

**The one page in the project whose cut is a URL, and the one page with a
cut-filtered export.** That is not a coincidence and it is the strongest single
piece of evidence for the restated ReadCut hypothesis (main document §4.1).

**Change signal**: one new day appended — a new `DATA` entry / a new `Day-NNN`
source file. Grain: `day` (int). It is a baked frontier that grows by running the
rebuild script; nothing updates at runtime. Frontier is Day 307 ("You Made It");
whether 307 is the plan's end was not verified beyond the title (inferred).

**Export shape**: CSV `day, part, partName, title, md_length` (+ `md`); JSON the
entry verbatim. **Existing**: the PDF print view, with an edition stamp and a ToC.

**Narration**: the commentary *is* prose, 307 days of it, baked as `md`. No
dedicated knowledge file; Start Here's only points at it
(`start_here.default.md:29`).

**Capability**: no `c2a2*`, no "?" (the `#pdf-pop` popover is a range picker), no
manifest entry. `#filter` covers titles and parts, not the `md` full text — so
307 days of commentary are unsearchable.

**Resisted**: live, not orphaned (three inbound routes). The hand-authored shell
has no separate source. The append-missing faithfulness guard was not exercised
(the script was not run). `agents_tab.html:498` carries a
`summa-commentary-reviewer` task, i.e. an agent reviews this page (inferred link).

---

## Review Log — **audited only to triage; this is a stated gap**
`wiki/review_log.html`, 6,840,888 B — the second-largest live surface in the
project. Door `data-target="review-cards"` from `start_here.html:183`, handled at
`explorer.html:751-756`. Not a tab. Regenerated by
`scripts/refresh_review_log.sh:13` calling `scripts/assemble_review_log.py`; last
commit 2026-10-04, so it is live and current. Daily review pages under
`wiki/review/` are **untracked** (`_superseded/`, `_trash/`,
`_deleted_quarantine/`, plus `2026-10-01..04_review.html`), so only the assembled
log is published.

**No manifest entry, no knowledge file** (confirmed:
`SPEC_voice_faq_key_migration_2026-08-28.md:98` records it as having none), **no
`descriptions` entry, and no audit.** Its entity grain (review cards? days?
findings?) and its cut are unknown to this document.

**This is recorded as a finding, not papered over.** A 6.8 MB surface that is
regenerated daily, reachable in two clicks from the front door, and invisible to
all five layers is exactly the kind of thing a manifest exists to prevent. It
should be the first entry filled after the key namespace is unified.
