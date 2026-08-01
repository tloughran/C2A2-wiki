# tools/guide — the screenshot guide, recovered

Transferred from another box, 27 July 2026. Source material was built there on 26 July 2026
and its build scripts were left in a session scratchpad that is expected to be deleted.

## What is here

| Path | What it is | Committed? |
|---|---|---|
| `web/1x`, `web/2x` | 220 WebP derivatives — what the guide actually serves | **yes** — 15.1 MB |
| `manifest.json` | slug, section, title, caption, viewport, sha256, derivative paths | yes |
| `recover_from_pdf.py` | rebuilds `shots/` + `manifest.json` from the PDF | yes |
| `build_derivatives.py` | rebuilds `web/` from `shots/` | yes |
| `HANDOFF.md`, `IN_APP_GUIDE_PLAN.md` | notes transferred from the originating box | yes |
| `shots/` | 110 PNG plates at native capture resolution | **no** — gitignored, 22.1 MB |

Neither the PNGs nor `C2A2_Explorer_Complete_User_Guide.pdf` (27.6 MB) is committed. Both
are inputs. The chain `PDF → recover_from_pdf.py → shots/ → build_derivatives.py → web/`
reproduces everything committed, so the PDF is the archival source of truth and the repo
carries 15.1 MB instead of 49.7 MB.

WebP quality is 86, chosen for legibility rather than size: these are dark-UI screenshots
with small anti-aliased label text, and below ~80 the sub-tab row and the Sociogram's foot
counters smear. At 86 a native-size crop is indistinguishable from the PNG.

### Why the PDF was a sufficient backup

The build embedded each plate losslessly at its capture size and printed the plate's own
filename in the page footer. So the PDF carries the images *and* their identifiers:

```bash
python3 tools/guide/recover_from_pdf.py tools/guide && python3 tools/guide/build_derivatives.py
```

reproduces `shots/`, `manifest.json` and `web/` from the PDF alone. Recovery verified:

- 110 images, one per plate page — matches the cover's stated count
- **0 duplicate hashes** — the plan's own duplicate-detection guardrail passes on the recovered set
- viewports 73 x (1440x900), 34 x (1440x1600), 3 x (390x844) — matches the plan's table exactly

## What is still missing, and cannot be recovered from the PDF

- **The capture harness.** `cap_lib.py`, `stage_a.py` … `stage_l.py`, `manifest2.py`,
  `build4.py`, `verify_pdf.py`, `verify_links.py`, `audit.py`. The PDF preserves the
  *output* of those scripts, not the scripts.
- **The `reach` steps** — how each state was navigated to. `manifest.json` therefore records
  what each plate *shows* but not how to get back to it. That is the single largest gap, and
  it is what `IN_APP_GUIDE_PLAN.md` Part 5 proposes to make declarative.
- **`_rejected/`** — the 11 GitHub-Pages 404 captures and the superseded shots. Only the
  known-bad 404 hash matters (it is a denylist entry), and it is not preserved here.

## `reach` — how far it goes, and where it stops

`schema: c2a2-guide-manifest/1`. Every plate now carries a `reach`: the steps that drive the
app to it, meant to be replayed by both the capture harness and the guide's "open this view
in the app" link, so the two cannot drift.

```bash
python3 tools/guide/build_reach.py
```

**What is authored: the page-level route, and only because it is checkable.** Chapter and
sub-tab come from each plate's section and are asserted against the real DOM in
`wiki/explorer.html`, the real `a.launch` links in `wiki/start_here.html`, and the real files
on disk. 18 assertions. A renamed `data-src`, a renamed `postMessage` case, or a moved Start
Here link **fails the run, names the selector, and leaves the manifest unwritten** — verified
against a mutated copy of the site, not assumed.

**What is not authored: the within-page steps.** Opening a modal, expanding a level,
selecting a node. Those lived in `stage_a.py … stage_l.py` and did not survive the transfer.
Guessing them would produce recipes that look authoritative and silently reach the wrong
state — the precise failure mode the plan was written about. So:

| | count |
|---|---|
| `reach_exact: true` — the route lands on exactly what the plate shows | 18 |
| `reach_exact: false` — the route reaches the plate's page, not its state | 92 |
| `volatile: true` — content changes every run; diff structure only | 15 |
| `cost: "model"` — spends credits to recapture (the four Physics AI actions) | 4 |

Closing the remaining 90 is the next increment, and it needs the live site, not the PDF.

### Replay — the static gate is not enough

```bash
node tools/guide/replay_reach.cjs [--port 8080] [--cdp 9222] [--only <slug-prefix>]
```

`check_coverage.py` asserts routes *statically*. Necessary, not sufficient: eleven plates
once carried `a.launch[data-target='review-cards']` — two true substrings, matching no
element — behind a green gate. Only a browser can say a recipe arrives. **19 routes, 110
plates, 0 failures.**

It is not a new harness. `scripts/test_voice_shell.cjs` already serves the wiki and drives a
real Chrome over raw CDP with **zero dependencies**, and already exports its plumbing behind
a `require.main === module` guard, so this borrows it and adds nothing to it. No Playwright,
no `node_modules`, no browser download.

That also lets a reach step be a **CCL command** rather than a selector:

```json
{ "cmd": "open the first node" }
```

A command is the app's own declared vocabulary, policed by the §9 audit, so one that stops
working fails loudly — where a dead selector fails silently. It also hands the plan's Part 5
over for free: "the app replays the same reach to drive a live session" needs no new runtime,
because the app already interprets exactly this vocabulary.

Within-page commands live in `WITHIN_PAGE` in `build_reach.py`. They reproduce the **state
class** a plate shows, not its pixels — the captions record that a search was run, never
which term — and nothing enters that dict until `replay_reach.cjs` has executed it.

Three bugs this found in its own first runs, all silent-by-default and all mine: reading
`frame.src` (the shell navigates by `contentWindow.location.replace`, so the element's
attribute never changes — `window.CCLFrameSrc` is the app's single reader and is now used
here); clicking into a chapter's document before it finished loading, which presents as a
dead selector; and re-checking CCL readiness per command, when `#ccl-result` is also where
every reply lands, so the banner never returns.

### NOTE — two asymmetries the assertions surfaced

**Two link classes, not one.** Start Here reaches its four otherwise-unreachable pages via
`a.launch` (What Is C2A2, Who's Who) *and* `a.door` (Review Log, Summa Commentary). An
earlier version of `build_reach.py` claimed `a.launch` for all four and its assertion still
passed, because it checked whether `data-target="review-cards"` appeared **anywhere in the
file** rather than on the anchor. `anchor_exists()` now requires the class and the attribute
on the same tag. A selector that matches nothing fails here instead of in the browser.

**Who's Who is wired differently from its three siblings.** The other three carry a
`data-target` and post `{source:'c2a2-start-here', action:'navigate', target}` to the shell,
which swaps the frame *and* hides the sub-tab rows. Who's Who is a plain
`href="whos_who.html"` that navigates the iframe directly, so the shell's row state is never
updated, and `explorer.html`'s message switch has no `whos_who` case to add one. Recorded,
not fixed: a live-site behaviour change needs its own review.

## The gate — one contract, both directions

```bash
python3 tools/guide/check_coverage.py
```

The guide and the voice guide both describe how to reach a view, and must not drift. They do
**not** share a file to achieve that: this manifest is generated and rebuilt on every
recapture, while `wiki/voice_guide/manifests.json` is hand-authored and changes only when a
tab gains a control. Merging them would make every regeneration collide with a human edit,
and within months no one could answer who owns a given line. They share an assertion instead.

- **Direction A** — no plate may claim a route the app does not have. Catches a guide gone
  stale against a renamed tab.
- **Direction B** — no destination the app declares may go undocumented. Catches the more
  valuable failure: a page nobody wrote up. This is the direction that finds pages like the
  four only Start Here reaches — the gap two hand-run capture passes both missed.

Destinations come from `wiki/explorer.html` and `wiki/start_here.html` directly, never from
`voice_guide/destinations.json`, which is generated from `explorer.html` — reading the
generated copy would let both sides agree while both were wrong.

Currently **20 destinations, 20 documented, 0 gaps**. A destination may be undocumented, but
only via the `UNDOCUMENTED` allowlist with a written reason; an empty allowlist is the
healthy state and a growing one is the signal the guide has fallen behind.

Verified by mutation, not by assertion: a renamed documented tab goes red in both
directions; a new tab and a new Start Here door each go red under Direction B; allowlisting
is the only thing that silences either; and re-introducing the `a.launch`/`a.door` mix-up
above fails `build_reach.py` by name.

Slug prefixes (`a01`, `b05`, `d06`) are **capture-stage identifiers, not section numbers** —
`d10-mobile-shell-default` sits in section 1.5. Order comes from the manifest, never from the
prefix, and never from a page number (page counts already moved 86 → 112 → 117).

## Known drift to reconcile before this guide is republished

Recorded here rather than fixed, because each is a claim about the live site that someone
has to adjudicate:

- **Sociogram counts.** Plates show 4,385 nodes / 114,182 edges (26 July). `CLAUDE.md`
  states 2,638 nodes / 70,407 edges (measured 5 June). `voice_guide/destinations.json`
  states 4,211 nodes (23 July). Three numbers, three dates, one graph.
- **PRS triple count.** The guide's glossary states 511 triples across 15 traditions and the
  per-tradition breakdown sums to 511. `CLAUDE.md` states 282 for the Review Log's PRS
  Triples tab. These may be counting different things; nothing here establishes which.
- **The product expands its own acronym two ways.** The masthead reads *Community Dialogue
  Accelerator/Detector System*; the Sociogram's narration reads *Community Context for AI
  Alignment*. Both are live. The guide documents this rather than resolving it.
