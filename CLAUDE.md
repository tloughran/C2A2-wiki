# RC Karpathy Wiki Project — Claude Standing Instructions

## CONSTITUTIONAL RULE: No Blind Pushes to GitHub

**Before any `git push` to any GitHub repository, Claude must:**

1. Serve the affected HTML locally over HTTP (`python3 -m http.server 8080` from the `wiki/` folder, or equivalent)
2. Use the browser (via Claude-in-Chrome or computer-use screenshot) to visually verify the changed page loads and renders correctly
3. Report specific observations to the user ("ToC loads with N entries, article click works, no console errors")
4. Wait for explicit user sign-off before pushing

**Default localhost target for "pop the local" / visual review is `http://localhost:8080/explorer.html`** — the full system shell with the chapter + accelerator-tool tab bar. `wiki_narration.html` alone is just the Sociogram iframe content and has no tab bar by design; loading it directly looks like the bar is broken when it isn't.

**This rule applies to:** C2A2-wiki, any Summa repository, and any other GitHub repo touched in this Claude account.

**Rationale:** We pushed `adbd456` without local HTTP review (2025-05-07) and the user reported unexpected behavior. A 30-second local check would have caught it.

**EXCEPTION — automated data-only heartbeat refresh (added 2026-06-26).** The `heartbeat-refresh` GitHub Actions cron MAY commit and push without human sign-off, but ONLY when both hold: (a) it changes **data files exclusively** — `wiki/heartbeat/data/digest.json`, `wiki/heartbeat/data/snapshots/**`, `wiki/heartbeat/data/sources_roster.json` — never code, HTML, or CSS; and (b) the **CI gate passes** (the jsdom roster test `wiki/heartbeat/test/roster.test.js` + `node --check` on the JS + the pipeline's seed/size/`signals>0` guards). A failing gate fails the job, so nothing is pushed. This carve-out honors the rule's intent: the rule exists because an unreviewed **code/HTML** push broke rendering; auto-publishing only **validated data** behind a green gate is low blast-radius. Any change to the heartbeat's code/HTML/CSS still requires the full human local review above.

---

## CONSTITUTIONAL RULE: Iframe-Loaded Tabs Must Not Ship Bare Asset Includes

**`explorer.html` force-freshes each tab's iframe document (`data-src + '?v=' + Date.now()`) but cannot reach the assets INSIDE that document.** A sub-page that loads its own separate `.js`/`.css` with a bare `src="app.js"` therefore gets fresh HTML + browser-cached assets on every load — a guaranteed stale-asset mismatch the instant the asset is edited.

**Therefore, any tab loaded into the explorer iframe must either:**

1. **Inline its JS/CSS** (as every single-file tab does — they are immune because the whole file is the iframe document), OR
2. **Content-hash its `?v=` includes** via a deterministic stamp step. Never ship a bare local `src=`/`href=` include on an iframe-loaded page, and never rely on a manual `?v=N` bump (forgetting it IS the repeatable error).

**Enforcement (heartbeat):** `wiki/heartbeat/backend/stamp_assets.py` rewrites each include's `?v=` to `SHA-1[:10]` of the asset; it is step 6 of `refresh_snapshot.sh` and is runnable standalone after any asset edit. Run it (or inline) before any push that touches a multi-file tab's assets.

**Rationale:** 2026-06-26 — the heartbeat "What is a lens?" link was dead in-browser while jsdom tests passed, because the browser ran a cached `app.js` against fresh `index.html`. A code review confirmed heartbeat was the only multi-file tab; all others inline. Content-hash stamping makes the version a function of file content, so it is always correct with no human in the loop (Rule 5: if code can answer, code answers).

---

## CONSTITUTIONAL RULE: Mismatched-Context Push-Back

**If a question seems to presume knowledge on Claude's part that isn't available in the current project context, Claude should consider pushing back rather than scramble too long to assemble context. The push-back response is:**

> "Should this be a Project Inquiry? If so, find the right one."

**How to apply:** When a user opens a Cowork session in one project and asks a question whose answer probably lives in a different project, conversation history, or external system Claude can't see, Claude should NOT silently spelunk Gmail, neighbor repos, or memory to backfill. State what's missing, offer the push-back phrase, and let the user redirect (either by re-opening in the right project or by explicitly importing the missing context).

**Rationale:** 2026-05-26 — Tom opened a session in RC Karpathy Wiki Project and asked a scheduling check across "Summa by ISME" and "dev path pre-ISME." Both threads' load-bearing context (the ISME submitted abstract, the Summa pace tracker, paper status) lives elsewhere; Claude scrambled across Gmail, the docx in inbox, and memory rather than naming the mismatch. Tom caught it after several exchanges. Asking up front is cheaper and more honest.

---

## CONSTITUTIONAL RULE: Session Handoff Continuity

**On resume, Claude reads `handoffs/<thread>.md` FIRST** and treats it as the authoritative pickup source — before any session-title search or `read_transcript`. Fall back to title-search / transcript only if no handoff doc exists for the thread.

**At the close of any working session on a named thread, Claude rewrites that thread's `handoffs/<thread>.md`** with: branch, what shipped + commit, the exact resume cue, the next-increment scope, parked items, and the originating session_id. The doc is gitignored (local-only, never published) and should be rich enough that a transcript read is unnecessary.

**Rationale:** 2026-05-29 — resuming the sociogram work, the prior session was auto-titled "Summa Explorer integration status" (no "sociogram" in the title), so the resume skill's title-keyword match failed and Claude burned tokens probing transcripts. A deterministic per-thread handoff doc makes a bad auto-title irrelevant, and is cheaper and more accurate than a transcript read. (It is also a tiny instance of Pathway 16, durable conversational memory.)

---

## Wiki Narration Visualization

**Working URL (local):** `file:///Users/tomloughran/Documents/Claude/Projects/RC%20Karpathy%20Wiki%20Project/wiki/wiki_narration.html`

**Vault path:** `/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/`

### Key Files (relative to vault root)
- `wiki_narration.html` — the generated visualization (self-contained, ~28.7MB as of 2026-06-02)
- Source scripts are in the Cowork session at:
  - `wiki-narration/scripts/generate_visualization.py` — HTML generator
  - `wiki-narration/scripts/extract_vault_data.py` — vault data extractor
  - `validate-html/scripts/validate_html.py` — HTML validation (JS syntax, brace balance, data integrity)
  - `wiki-narration/SKILL.md` — skill definition
  - `validate-html/SKILL.md` — validation skill definition

### Regeneration Workflow

**ALWAYS regenerate via the wrapper — never call the scripts directly:**
```bash
bash wiki/c2a2-wiki-narration/regen_sociogram.sh
```
The wrapper hardcodes BOTH the `--summa <source vault>` extract flag and the
`agents/openstory/agent_node_edges.json` third arg, and guards against shipping a
Summa-less or agent-less build. Calling `generate_visualization.py` directly with
just `<vault_data.json> <out.html>` silently drops the agent-activity layer AND
the Summa nodes — this happened on 2026-06-23 (the Tradition Index regen), which
left the Agent Map Sociogram subtab opening empty. The raw three-step sequence
(extract `--summa` → generate with agent arg → validate) is the wrapper's body;
read it there, don't paste a bare two-arg call.

### Architecture
- D3.js v7 force-directed graph, dark theme (#0a0a0f)
- 2638 nodes (wiki files), 70,407 edges (wikilinks + shared references) — counts measured 2026-06-05 from the 2026-06-02 regen
- Left panel: checkbox filters by tradition (14 thinkers) and structure group (10 categories)
- Upper-right: Hold Forces, Show Hover Names, Fit All
- Node click → right panel with rendered markdown; edge click → both panels
- 6 narration tracks assembled at load: History/Recent/Latest x Brief/Deep
- TTS: browser (Web Speech API) and OpenAI API backends
- Crash-proofing: node limit 20000, edge limit 30000, warnings at 80%

### Color Palette (muted)
- Levin #C45B5B, Friston #5A8EAF, Hoffman #C08B3E, Kastrup #8B5DAB
- McGilchrist #3D9E89, Hawkins #B87D3E, Wolfram #4A5E6D, Carroll #4E8A5E
- Arkani-Hamed #A85D3A, Fredrickson #C47A9A, Stump #A8923A
- Rohr #9A7A5A, Wright #5A72A8, Loughran #4A8A7A
- Master #C9A84C, Architecture #5B7FA5, Agents #8B6DAE

### Template Rules (critical for contributors)
- Python generator uses regular strings (NOT f-strings) for HTML template
- Data injection: `""" + json_var + """` concatenation only
- CSS/JS must use single braces `{` `}` — never `{{` `}}`
- Always validate with `node --check` on extracted JS before delivering

---

## Summa Explorer

- `summa_explorer.html` fetches `./vault/refs/summa_index.json` (relative, same repo)
- Vault data lives at `wiki/vault/` in C2A2-wiki repo
- `sync_vault.sh` + launchd agent at 21:00 daily keeps vault in sync from Summa 2026 project
- **Before pushing updates to summa_explorer.html or vault data:** verify locally via HTTP server

---

## Wiki Janitor (weekly polish-and-surface pass)

**Script:** `scripts/janitor.py`
**Schedule:** Sunday 05:45 local (`c2a2-wiki-janitor-weekly` scheduled task)
**Outputs:** `janitor/findings.md` and `janitor/state.json` (outside `wiki/` so Obsidian doesn't see them)

### What it does
Auto-fixes a small safelist of categories (currently: trailing whitespace in vault `.md` files, stray `.DS_Store`). Runs report-only checks for everything else: broken wikilinks, Summa SRC↔PUB drift (refs/), reindexer freshness, undated refs nodes, stale uncommitted WIP (>14 days), duplicate H1 titles. Skips orphan/sparse detection — the sewing agent (`c2a2-sewing-agent-weekly`) owns that and writes `wiki/architecture/metrics/connectivity_log.csv`. Do not duplicate.

### Baseline-then-deltas
First run snapshots all open findings as accepted noise. Subsequent runs flag only deltas in the "New since last week" section (which morning-system-health reads). Baseline is preserved across runs; cleaned-up findings auto-fall-out.

### Promotion rule
Categories start report-only. After a clean run, promote one to auto-fix with:
```bash
python3 scripts/janitor.py --promote <check_name>
```
Destructive categories (`empty_section`, `dead_end_wikilink`) are permanently notify-only.

### morning-system-health integration (WIRED 2026-06-19)
The `morning-system-health` scheduled task (daily 6 AM) now reads `janitor/findings.md` directly and surfaces its `## New since last week` section as report section 5, flagging `reindexer_freshness` and `src_pub_refs_drift` staleness/drift signals especially. No separate brief file is emitted — `findings.md` is the single source. (The janitor runs weekly Sunday; the daily report restates the same "new" items until the next janitor run, which is intended.) Known gap, deferred: chronic findings buried in the accepted-noise baseline don't resurface — see `handoffs/reliability-backlog.md` (escalate-chronic-findings).

### Manual operations
```bash
python3 scripts/janitor.py                 # normal run (auto-fix + report)
python3 scripts/janitor.py --dry-run       # report only; no writes
python3 scripts/janitor.py --baseline      # reset baseline to current findings
python3 scripts/janitor.py --promote <c>   # add check to auto-fix safelist
```

---

## Review Log (historical preservation archive)

**Output:** `wiki/review_log.html` (self-contained, ~2MB) — **PUBLISHED** (2026-06-22). `assemble_review_log.py` auto-scrubs every email address from the HTML on each build (final `re.subn` pass), so the public copy is address-clean. The `provenance/` sidecar stays **gitignored/local** — it holds `decision_emails.json` with the raw addresses.

### What it is
A chronological, zero-drop archive built from DURABLE sources, because the daily review HTML pages are ephemeral (Phase 0 deletes them). Five tabs: **Cards** (every `inbox/proposals/**` file, full text, grouped by proposal date), **Your Responses** (verbatim decision emails + `review/archive/*_decisions.md`), **PRS Triples** (per-tradition, 282), **Bridges** (per tradition-pair from `master/cross_program_index.md` + embedded `synthesis/*_bridge.md` essays), **Findings** (`flags/pattern_detector_findings.md`, all, filterable by recommended-action).

### Scripts (in `scripts/`)
- `build_provenance.py` — joins each visualized triplet back to its proposal (sidecar in `provenance/`); reconciliation + proposed→ingested lag. Non-destructive.
- `assemble_review_log.py` — builds `review_log.html` from vault + `provenance/`.
- `append_decision_email.py` — idempotent append of one decision email to `provenance/decision_emails.json`.
- `refresh_review_log.sh` — deterministic regen wrapper (build_provenance + assemble + size guard).

### Manual regen
```bash
bash scripts/refresh_review_log.sh
```

### Auto-update (wired 2026-06-22)
The `c282-wiki-agent-daily-run` task does it: Phase 0 appends each processed decision email to `provenance/decision_emails.json` (via `append_decision_email.py`, idempotent) BEFORE deleting the review page; new Phase 5.5 runs `refresh_review_log.sh` and grep-asserts the scrub held. `review_log.html` (address-scrubbed) is pushed by Phase 6; `provenance/` stays gitignored/local. Validation: cards rendered == proposal files with an id (content-fingerprint check, README/manifest excluded); triples/findings/bridges counts == source counts; `node --check` the embedded JS.

### Known caveat
Only 1 page-snapshot (2026-06-16) was lost before archiving; its 13 cards survive as proposal files. Provenance: 282 triples = A179 backref + B17 fuzzy + C74 seed + D12 (early seeds of later-added traditions; not failures). Reverse gap 168 approved candidates not visualized (101 are secondary -02/-03 candidates).
