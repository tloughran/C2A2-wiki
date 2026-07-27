# C2A2 Explorer screenshot-guide — COMPLETE

Status: finished 26 July 2026. Supersedes the v3 draft.

## Deliverable

`C2A2_Explorer_Complete_User_Guide.pdf` — 117 pages, 110 captured views across 18 sections,
ordered as the site's own chapters, plus a "Before you begin" orientation preface, a glossary
and live-vs-planned note, a first-visitor FAQ, and a closing scope note.

Source captures: `shots/` (110 PNGs, all 1440 px wide, no duplicates).

Navigation: the contents page is fully hyperlinked with real page numbers, there are 22 PDF
outline bookmarks, and every plate's section kicker links back to the contents.

Page orientation follows the capture: 73 landscape plates (1440x900) on landscape pages,
37 portrait plates (1440x1600 and the 390x844 phone shots) on portrait pages, so tall
captures are not shrunk to fit a horizontal page.

### Third pass additions

- **PRS Triples reader.** The PRS Triples stream lists one card per thinker with its own
  count. Clicking any triple opens `#tmodal` — a pop-up showing Label / Problem / Resource /
  Solution, date, source and confidence, plus the originating file. Its header reads
  `1 / 511`: Prev and Next page through the entire set across all fifteen traditions, not
  just the thinker clicked. Trigger is `.trow`; the traditions are `<details>` and at least
  one is open by default.
- **The three level interactives.** Each of Levels Two, Three and Four embeds its own
  iframe, and they only exist once the level is expanded:
  `#l2-signal-embed` -> `level2_signal_stream.html`,
  `#l3-readout-embed` -> `intertradition-readout.html` (Act 1 / Act 2, its own Play / Prev /
  Next / Restart transport over 18 steps),
  `#l4-matrix-embed` -> `intertradition-matrix.html` (the DET 40-step matrix).
  The earlier single "lower page" plate showed only one of the three.

## Second pass — first-visitor crawl (26 July 2026)

The first pass walked the tab bar and so missed everything the tab bar cannot reach:

- **The Explorer does not open on Start here.** It loads Accelerator Tools > Sociogram.
  Start here is the intended front door and is a 30-minute, three-stop route.
- **Four substantial pages are reachable only from Start here's links**, which post a
  message to the shell to swap the frame: `what_is_c2a2.html` (fifteen framings, led by
  the MacIntyre angle), `whos_who.html`, `review_log.html` (292 cards, 78 review dates,
  511 PRS triples, 54 bridges, 54 findings, five streams) and `summa_commentary.html`.
  No sub-tab leads to any of them.
- **Community Interactions pathway cards were missed.** 'The Road Ahead' holds 32
  numbered pathways in four groups, each with a DRAFTED/OUTLINED badge and a star for the
  ISME critical path (8-10 July 2026 presentation). `a.pw-link` opens a reader that
  fetches the pathway's source file, with Prev / Next Step paging. Expanding the levels
  also reveals 11 level cards, two marked 'coming'.
- **Mobile** is a distinct state: the Sociogram prints 'Mobile preview - pan and tap nodes
  - filters require a larger screen' and the filter rail is unavailable.

## Site

https://tinyurl.com/C2A2explorer resolves to:

    https://tloughran.github.io/C2A2-wiki/wiki/explorer

The shell loads every tool into `iframe#content-frame` from `/C2A2-wiki/wiki/`.
The earlier 404 captures came from requesting page names such as `explorer.html`
at the domain root, where they do not exist.

## Navigation map

Five chapters (`.chap-btn`), each loading a sub-page:

- Start here — `start_here.html`
- Community Explorer — `community_explorer.html` (nests `community/index.html` for Cards)
- Community Education — sub-tab row `#row2-edu`
- Community Accelerator Tools — sub-tab row `#row2`
- Community Interactions — `community_interactions.html`

Accelerator Tools: Sociogram (`wiki_narration.html`), Narrative Connectome (`prs_3d.html`),
Agent Map (`agents_tab.html`), Metabolism (`metabolism/metabolism_view.html`),
Curriculum Tools (`summa_explorer.html`), Inter-Tradition Study (`interT_study.html`).

Education Tools: RC Document Explorer (`rc_document_explorer.html`),
Physics Explorer (`physics_explorer.html`),
TRV Commentary (`commentary-explorer/commentary_explorer.html`),
AI Heartbeat (`heartbeat/index.html`).

## Capture notes worth keeping

- Most sub-pages are locked to `100vh` and never scroll. At a 1440x900 window the
  iframe is only ~804 px tall, which hides real controls with no way to scroll to them:
  the Cards / Map / PRS / Overview sub-tabs and the whole community directory, and the
  AI Heartbeat Pulse / History / My Lens / Roadmap tab row (at y≈917). Those views were
  captured at 1440x1600 instead. Anything captured short will silently look complete.
- The Cards sub-views live in a **nested** iframe (`community/index.html`), not in
  `community_explorer.html`. Selectors must be resolved against the deeper frame.
- Sociogram node detail is reachable through the page's own `openNodeByLabel(label)`
  against the global `NODES` array; canvas clicks do not land reliably.
- Curriculum Tools hides its Transcript / Contemporary Synthesis mode row until an
  article is open. Use `.landing-art-link` on the landing page.
- Physics Explorer's summary modal must be dismissed before the AI answer bar is
  visible — otherwise the AI captures are just the modal.
- Inter-Tradition help overlay toggles class `on`, not `show`.

## Deliberately not captured

- A genuine Record run: `toggleRecord()` calls `getDisplayMedia`, so entering the state
  for real starts an actual screen recording. The two Record plates are staged from the
  page's own markup and are labelled STAGED in both the filename and the caption.
- External `PhET Simulation` links on the Physics concept cards (they leave for
  phet.colorado.edu). The in-app Simulate action is captured.
- Ask AI / Ask Claude answers in the Sociogram and RC Document Explorer, which draw on
  the account's limited free semantic queries. The three Physics AI actions were each
  run once to show a representative result.
- Community Interactions Level One does not expand — its header suppresses the click
  while the level is marked UNDER CONSTRUCTION. Captured as-is.

## Rejected material

`_rejected/` holds the 11 identical GitHub-Pages 404 captures and one mislabelled
duplicate from the earlier pass; `_rejected/superseded/` holds shots that turned out to
duplicate another state (default modes re-selected, and lens states already fully
visible in the My Lens plate).

## Rebuilding

Scripts used are not kept in this directory. To rebuild the PDF from `shots/`, any
image-to-PDF pass works; the guide places one capture per landscape-letter page with a
section kicker, title, and caption, ordered as in the Contents page.
