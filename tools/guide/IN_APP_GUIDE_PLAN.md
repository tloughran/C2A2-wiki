# From PDF tour to living in-app user guide

Companion to `C2A2_Explorer_Complete_User_Guide.pdf` and `shots/`.
Written 26 July 2026. Capture-harness detail lives in `HANDOFF.md`; this file covers
what exists, and what remains to build.

Agreed direction:

1. HTML guide is the primary in-app artifact; the PDF becomes a download/print export.
2. Two entry points — a sixth chapter button **and** a link inside every existing `?` overlay.
3. Build the shared state-recipe layer, so the guide can drive the app to the state it depicts.
4. Weekly refresh for structure; monthly for the plates that spend model credits.

---

## Part 0 — Do this first, or the rest is not reproducible

**The build scripts are currently in a session scratchpad and will be deleted.**

`cap_lib.py`, `stage_a.py` … `stage_l.py`, `manifest2.py`, `build4.py`, `verify_pdf.py`,
`verify_links.py`, `audit.py` presently live under
`/private/tmp/claude-503/.../scratchpad/`. Nothing in the repo can rebuild the guide today.

Move them into the wiki repo — suggested `tools/guide/` — together with:

- a `requirements.txt` pinning `playwright`, `reportlab`, `pypdf`, `pypdfium2`
- a note that Playwright runs against the **system Chrome** via `channel="chrome"`, so no
  browser download is needed
- `shots/` and the PDF as build outputs

Until this is done, the guide is a one-off artifact, not a pipeline.

---

## Part 1 — What has been done

### The artifact

`C2A2_Explorer_Complete_User_Guide.pdf` — 117 pages, **110 captured views** across 18
sections, in the site's own chapter order, with:

- a **"Before you begin"** preface (the Explorer does not open where you should start)
- a **glossary and live-vs-planned note** (PRS, G·P·R·S, pathway, the four graphs, the
  "inferred seed" provenance caveat, what is LIVE / PLANNED / UNDER CONSTRUCTION)
- a **first-visitor FAQ** (cost, what leaves your machine, Record, node caps, mobile)
- a closing scope note on what is deliberately absent
- a hyperlinked contents page with real page numbers, 22 PDF outline bookmarks, and a
  back-link from every plate to the contents
- page orientation matched to each capture: 73 landscape, 37 portrait

### The captures

`shots/` — 110 PNGs, no duplicates (verified by hash):

| Size | Count | Why |
|---|---|---|
| 1440×900 | 73 | standard desktop viewport |
| 1440×1600 | 34 | pages whose controls sit below the fold in a short window |
| 390×844 | 3 | mobile states |

`_rejected/` holds the earlier pass's 11 identical GitHub-Pages 404s and one mislabelled
duplicate; `_rejected/superseded/` holds captures that turned out to duplicate another
state. Nothing was hard-deleted.

### What three passes established

- **Pass 1** walked the tab bar and captured tool chrome.
- **Pass 2** crawled as a first-time visitor and found that four substantial pages are
  reachable *only* from Start Here, plus the whole orientation problem.
- **Pass 3** added the PRS triple reader and the three level interactives.

The recurring lesson, and the reason Part 2 of the refresh job matters more than the
screenshots: **every miss was silent.** The 404s reported success. The duplicate Agent Map
shot reported success. The Physics AI plates captured a modal covering the answer. Nothing
failed loudly.

---

## Part 2 — Architecture facts that constrain the build

All verified against the live site, 26 July 2026.

**Hosting.** Static GitHub Pages from `github.com/tloughran/C2A2-wiki`, served at
`https://tloughran.github.io/C2A2-wiki/wiki/`. No server-side anything: all automation must
be GitHub Actions plus committed artifacts.

**Shell.** `explorer.html` holds two nav rows and loads every tool into a single
`iframe#content-frame` via `setFrame(src + '?v=' + Date.now())`.

- Chapters: `#chap-intro`, `#chap-community`, `#chap-education`, `#chap-tools`,
  `#chap-interaction`
- Sub-tab rows: `#row2` (Accelerator Tools) and `#row2-edu` (Education), each holding
  `.tab-btn[data-src]`
- Help: `showHelp()` / `closeHelp()`, triggered by `#btn-help` and `.btn-help-row`

**There is already a postMessage channel.** `explorer.html` listens for
`{source:'c2a2-start-here', action:'navigate', target:…}` with cases `fifteen`,
`review-cards`, `summa-commentary`, `sociogram`. **Extending this switch is the
in-idiom way to add guide deep links** — no new architecture required.

**The iframe sandbox already permits a second window:**
`allow-scripts allow-same-origin allow-forms allow-modals allow-popups
allow-popups-to-escape-sandbox allow-downloads`.

**Constraints that will bite:**

- Most sub-pages are locked to `100vh` and never scroll. At 1440×900 the iframe is ~804 px
  and real controls are unreachable — the Cards/Map/PRS/Overview sub-tabs and the Heartbeat
  tab row (at y≈917) among them. The guide must keep documenting this, and the harness must
  keep using a taller viewport for those plates.
- The Community Explorer Cards sub-views live in a **nested** iframe
  (`community/index.html`, tabs `.cc-tab`). Selectors must resolve against the deeper frame.
- The three Community Interactions embeds (`#l2-signal-embed`, `#l3-readout-embed`,
  `#l4-matrix-embed`) **do not exist in the DOM until their level is expanded**.
- Several states are not URL-addressable at all. This is the core problem Part 5 solves.

---

## Part 3 — Goal A: the in-app guide

### Slugs, not page numbers

Page numbers have already moved 86 → 112 → 117 across three builds. **No link may ever
target a page number.** The plate filenames are already stable, unique and readable —
`a01-shell-default`, `d06-reviewlog-prs-triple-popup`, `b05-sociogram-settings`. Promote
them to canonical slugs. Section numbers (`5.6`) are display-only and also unstable.

### One manifest, two outputs

```
manifest.(py|json)
   ├── build_html.py  →  wiki/guide/index.html  + per-slug anchors   (primary, in-app)
   └── build_pdf.py   →  C2A2_Explorer_Complete_User_Guide.pdf       (download / print)
```

`build4.py` already does the PDF half. The HTML build is new work.

### Delivery

- `guide.html` loads into `iframe#content-frame` exactly like every other tool, so it
  inherits the persistent tab bar and needs no new layout.
- Serve **WebP derivatives** at 1× and 2×, not the 1440-px PNGs. The PNG set is ~30 MB and
  the PDF is 28 MB; unoptimised, the guide would outweigh the app it documents.
- Lazy-load plates; the guide is long.
- Deep-link on load: `guide.html?at=<slug>` scrolls to and highlights that entry.

### Both entry points

- **Sixth chapter button** in row 1 — discoverable, the front door for "where is the manual".
  Loads `guide.html` and hides both sub-tab rows, mirroring how `#chap-interaction` behaves.
- **Inside every `?` overlay** — keep the existing short contextual help, and append
  *"Full guide for this view →"* resolving to the slug for the current view. This is the
  contextual path, and costs one line per overlay if the overlays are generated (see Part 6).

### Acceptance criteria

- Every one of the 110 slugs resolves to a rendered entry with its caption.
- The tab bar stays visible and functional while the guide is open.
- Guide page weight under ~2 MB on first paint.
- The PDF still builds from the same manifest, unchanged in content.

---

## Part 4 — Goal B: keeping it refreshed

Recapturing on a schedule is the easy half and the less important half. **The job's primary
duty is to detect that the site changed, and to fail loudly when the harness breaks.**

### Two cadences

| Cadence | Scope | Rationale |
|---|---|---|
| **Weekly** | Structural contract test + recapture of all non-AI plates | Cheap, catches UI drift |
| **Monthly** (or manual) | The four Physics AI plates — `c16` Explain, `c17` Problem, `c18` Analogy, `c18b` Simulate | Each is a live model call against the shared C2A2 pipeline |

### The structural contract test

The manifest's selectors are a *specification of the site*. Assert them before capturing:

- the five `.chap-btn` ids
- every `.tab-btn[data-src]` in `#row2` and `#row2-edu`, matched against the expected list
- `#tab-cards` and the nested `.cc-tab` set (Cards / Map / PRS / Overview)
- `.trow` → `#tmodal`, and that its header still matches `\d+ / \d+`
- `#l2-signal-embed`, `#l3-readout-embed`, `#l4-matrix-embed` after expanding the levels
- `a.pw-link` and the pathway reader's Prev / Next
- globals the harness depends on: `openNodeByLabel`, `NODES`, `showHelp`
- the four Start Here link targets (`what_is_c2a2`, `whos_who`, `review_log`,
  `summa_commentary`) — the most easily orphaned pages on the site

Any miss → fail the run and open a GitHub issue naming the selector. A missing selector
means the guide is stale *and* the harness is silently broken.

### Guardrails learned the hard way

- **Duplicate detection.** Hash every capture; any two identical files means an interaction
  did not fire. This caught four real failures during the build.
- **Known-bad hashes.** Keep the GitHub-Pages 404 hash on a denylist so a routing change can
  never re-enter the set as 11 "successful" captures.
- **Volatility flags.** Mark `c30`–`c37` (Heartbeat), `b30`–`b33` (Metabolism) and
  `b20`–`b24` (Agent Map) volatile — their content legitimately changes every run. Diff
  structure only, or the weekly alert becomes noise and stops being read.
- **Coverage report.** Diff the live DOM's interactive elements against the manifest and
  list anything undocumented. This is precisely what would have caught the four missing
  Start Here destinations automatically.

### Provenance

Stamp every guide page and the PDF cover with the site commit SHA and capture date —
*"captured against `abc1234`, 6 days ago"* — so staleness is visible rather than assumed.

### Acceptance criteria

- A deliberately renamed selector fails the run and opens an issue.
- A week with no site change produces no diff on non-volatile plates.
- The monthly job is the only thing that spends model credits.

---

## Part 5 — Goal C: bidirectional deep links, via shared state recipes

### The problem

`?goto=sociogram` can restore a chapter and tab. It cannot restore "settings dialog open",
"node selected", "Level Three expanded with its embed loaded", or "PRS triple reader at
1 / 511". Most of what the guide documents is exactly that kind of state, so a tab-level
round-trip is a weak promise.

### The solution

**The capture scripts are already state recipes.** `stage_l.py` encodes that reaching the
PRS reader means: Start Here → review cards link → PRS Triples tab → open a `<details>` →
click `.trow`. Lift those steps out of the Python into declarative data, and one artifact
serves both the harness and the app.

```json
{
  "slug": "d06-reviewlog-prs-triple-popup",
  "title": "PRS Triples — a single triple, opened",
  "section": "Start here > Review Log — the evidence",
  "viewport": [1440, 1600],
  "volatile": false,
  "cost": "free",
  "reach": [
    { "chapter": "chap-intro" },
    { "frameClick": "a[href*='review_log']" },
    { "frameClick": "div:text-is('PRS Triples')" },
    { "frameEval": "document.querySelector('details').open = true" },
    { "frameClick": ".trow" }
  ],
  "assert": ["#tmodal:visible", "text:/\\d+ \\/ 511/"]
}
```

- The **harness** replays `reach` to capture the plate and checks `assert`.
- The **app** replays the same `reach` to drive a live session to that state.
- They cannot drift, because they are the same file.
- `assert` doubles as the Part 4 contract test — the specification comes for free.

### Wiring

**App → guide.** Each view's `?` posts
`{source:'c2a2-guide', action:'open-guide', target:'<slug>'}`. The shell resolves the
current chapter + tab + any open modal to a slug and loads `guide.html?at=<slug>`.

**Guide → app.** Each entry carries *"Open this view in the app →"*, with two modes:

- **Same window** — post `{source:'c2a2-guide', action:'goto', target:'<slug>'}`; extend the
  existing `message` switch to look the slug up and replay its `reach`.
- **Second window** — `window.open('explorer?goto=<slug>')`, permitted by the existing
  sandbox flags. Closing the window returns the reader to the guide untouched. **Prefer this
  as the default**, because replaying a recipe in the reader's current session mutates their
  state (expands levels, opens modals, changes filters) with no undo.

If same-window replay is offered at all, confirm first: *"This will change what you're
looking at."*

### Acceptance criteria

- Every slug's `reach` replays successfully in both harness and app.
- A recipe that no longer reaches its state fails the weekly run rather than producing a
  wrong screenshot.
- Second-window round-trip leaves the reader's original session untouched.

---

## Part 6 — Further development worth considering

- **Generate the `?` overlays from manifest captions.** The overlays and the guide currently
  explain the same views in two places and can already diverge. One source, two renderings.
- **Search across captions.** They are written as prose and would index well with no extra
  authoring.
- **A "what changed" page** built from weekly diffs — in keeping with the project's own
  Review Log ethos of preserving its history rather than overwriting it.
- **Captions as alt text.** The graph-heavy tools have essentially no accessible description
  today; the guide has already written 110 of them.
- **First-run tour.** Reuse the existing Start Here three-stop structure, shown once, since
  the app opens on the Sociogram rather than the front door.
- **Guide-driven onboarding for the directory problem.** The "inferred seed" caveat matters
  most to a community finding its own wrong entry; that FAQ answer could link straight to a
  claim/correct flow if one is ever built.
- **Per-section PDF exports** for circulation (e.g. Review Log evidence alone) rather than
  the full 28 MB.

---

## Part 7 — Sequencing, risks, open questions

**Suggested order.** Part 0 (rescue the scripts) → recipe schema + manifest migration to
JSON → HTML build → CI contract test → deep links → the extras. The recipe layer lands
early because both the guide and the refresh job depend on it.

**Risks**

- *Silent capture failure* is the dominant failure mode and the reason for the assert layer.
- *Diff fatigue* — without volatility flags the weekly report is noise within a month.
- *Weight* — unoptimised images make the guide heavier than the app.
- *Recipe rot in the app* — a `reach` that half-executes could leave a user's session in a
  confusing state. Second-window default mitigates this.
- *Documenting a moving target* — the site is under active development, with 32 pathways
  DRAFTED or OUTLINED and none complete. Expect the guide to churn, and treat the coverage
  report as the signal for when it has fallen behind.

**Open questions**

1. Should the guide be versioned per site release, or always reflect `main`?
2. Should volatile plates be captured at all, or replaced by a live embed of the real view?
3. Is the sixth chapter button permanent, or a temporary aid while the site is young?
4. Who receives the weekly failure issue?
