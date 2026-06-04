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
- `wiki_narration.html` — the generated visualization (self-contained, ~15.4MB as of 2026-05-19)
- Source scripts are in the Cowork session at:
  - `wiki-narration/scripts/generate_visualization.py` — HTML generator
  - `wiki-narration/scripts/extract_vault_data.py` — vault data extractor
  - `validate-html/scripts/validate_html.py` — HTML validation (JS syntax, brace balance, data integrity)
  - `wiki-narration/SKILL.md` — skill definition
  - `validate-html/SKILL.md` — validation skill definition

### Regeneration Workflow
```bash
python3 extract_vault_data.py /path/to/vault > /tmp/vault_data.json
python3 generate_visualization.py /tmp/vault_data.json /path/to/wiki/wiki_narration.html
python3 validate_html.py /path/to/wiki/wiki_narration.html --source-data /tmp/vault_data.json
```

### Architecture
- D3.js v7 force-directed graph, dark theme (#0a0a0f)
- 1533 nodes (wiki files), 36,608 edges (wikilinks + shared references) — counts as of 2026-05-19 regen
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

### morning-system-health integration (TODO, not yet wired)
The Sunday janitor writes a brief to `~/Documents/Claude/Reports/janitor-YYYY-MM-DD.md`. Morning-system-health should be edited to surface the most recent janitor brief in its Monday report. Until that edit lands, Tom reads the brief directly or opens `janitor/findings.md`.

### Manual operations
```bash
python3 scripts/janitor.py                 # normal run (auto-fix + report)
python3 scripts/janitor.py --dry-run       # report only; no writes
python3 scripts/janitor.py --baseline      # reset baseline to current findings
python3 scripts/janitor.py --promote <c>   # add check to auto-fix safelist
```
