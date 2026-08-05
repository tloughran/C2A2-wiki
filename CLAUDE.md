# RC Karpathy Wiki Project — Claude Standing Instructions

## CONSTITUTIONAL RULE: Shell Code Is Pasted Inline, Paste-Safe

**When Claude gives Tom shell commands to run, the default is to paste them inline in chat as copy-paste-ready blocks — NOT to hand him a `.sh` file to invoke.** Tom runs zsh and pastes blocks directly into Terminal.

**Every pasted block must be paste-safe for interactive zsh:**

1. **No `#` anywhere** — interactive zsh does not treat `#` as a comment by default, so a pasted `#` line throws `bad pattern` / `command not found`. Use no comments, or narrate with `echo "..."`.
2. **ASCII only** — no em-dashes, no smart quotes, no apostrophes inside the code.
3. **Stage long quoted paths** into a `cd "..."` on its own line, or a variable; never let a quoted path with spaces wrap across lines.
4. **Single-quote any pathspec/regex containing `!` or `^`** (e.g. `':!hep-det'`, `'^hep-det/'`) so zsh history-expansion and globbing leave them alone.
5. If a `.sh` file is genuinely warranted (long/reusable), tell Tom to run it as `bash "<full path>"` so the shebang handles the `#` lines — he never pastes the file body.

**Durable environment fix (offer once):** `setopt interactivecomments` in `~/.zshrc` makes `#` safe to paste forever; it does not replace rules 2-4.

**Rationale:** 2026-06-28 — Claude reverted to delivering `.sh` files; Tom asked to return to inline paste-ready code. The recurring `#`/quote/em-dash traps hang his zsh at `quote>` or throw `bad pattern`. Inline-and-paste-safe is the contract. (Supersedes the looser "scrub snippets to ASCII" guidance.)

---

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

**Enforcement:** `wiki/heartbeat/backend/stamp_assets.py` rewrites each include's `?v=` to `SHA-1[:10]` of the asset. It takes `--target heartbeat|explorer|all`; **the default stays `heartbeat` on purpose** — `refresh_snapshot.sh` calls it with no arguments inside the heartbeat cron, whose carve-out below permits data-only pushes, so a wider default could make an unattended job commit HTML. `--check` stamps nothing and exits non-zero on a stale include; `scripts/test_voice_shell.cjs` runs `--target all --check` as its last row, so the CCL gate covers it.

**Extended 2026-07-25 to `explorer.html`.** The shell is not an iframe tab, but it is a normal cacheable document loading a separate `lib/c2a2-commandline.js`, which is the same exposure. It had been carrying a hand-typed `?v=` — and that hash was already **wrong** when the stamper first checked it, exactly as rule 2 predicts.

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

## CONSTITUTIONAL RULE: Explain at Grad Level, Afterward, and Stop Asking Permission Mid-Method

Three linked commitments. The register one is load-bearing for the other two: Tom cannot extend trust to a method he cannot follow, and cannot catch an error in prose he cannot parse.

### 1. Default register: first-year graduate

**Write for a capable reader with little background in the field at hand.** Define terms on first use. Expand acronyms. Prefer a concrete example to an abstraction. Never assume familiarity with a method, metric, file, or tool because it appeared earlier in the session.

**The level is one dial, currently set to first-year graduate.** Expect to raise it with experience toward *PhD with very modest coding background* — which is the real shape of the asymmetry: **do not condescend on reasoning, method, statistics, or study design; do unpack code, tooling, shell, and infrastructure.** When in doubt about which side of that line a thing falls on, unpack it.

**Lower the reading level, not the information density.** Every number, caveat, failure mode, disagreement, and limitation stays. This rule shortens sentences and unpacks jargon. It never drops substance, softens a finding, or omits an inconvenience to keep things tidy.

**Exempt:** code, commit messages, PR bodies, and file contents — those match the codebase's own conventions. Also exempt: short status lines during multi-step work.

**Supersedes caveman mode** where the two conflict. (Caveman is a global hook in `~/.claude/settings.json`; it is deliberately not disabled, because it governs other projects too.)

### 2. Explanation is after-the-fact, never a gate

**Do the work, then explain it.** Do not front-load a tutorial before acting, and do not stop mid-task to check that an explanation landed. Explanation is a report on completed work, not a checkpoint in it.

**`explain (X)` — stop and teach.** Drop the current thread, explain X from the ground up at the current level, then resume. No penalty for length. Applies to anything: a term, a number in a table, a design decision, a line of code, a claim just made.

### 3. Trust is granted at the level of method, not the step

**Do not ask Tom to approve individual steps he has no basis to judge.** Approval belongs at the level of *approach* — the method, the plan, the thing that can be agreed or disagreed with. Once the approach is agreed, execute it and report back, including anything that went differently than described.

This does **not** relax the standing gates, which exist for blast radius rather than comprehension: no blind pushes to GitHub, no `git add -A` in this repo, confirmation before anything outward-facing or hard to reverse. Those still stop and wait. What it retires is step-level permission theatre on ordinary read, search, build, and check commands.

**Corollary, mechanical:** permission prompts are enforced by the harness from `.claude/settings.json`, **not** by anything written here. A sentence in CLAUDE.md cannot grant a permission. Reducing prompts means maintaining prefix allow-rules in settings; one-shot entries containing session-specific paths never match again and are noise.

**Rationale:** 2026-07-31 — the OpenStory replication discussion ran three exchanges before the terminology was pitched low enough for Tom to agree or disagree with it. Once it was, he immediately caught two real errors Claude had missed: a corpus misattributed to the wrong arm of the study, and a category label ("AI↔AI") that meant something different from what it counted. The cost of the wrong register is not mild confusion; it is a reviewer who cannot review. His own framing: *we would move faster and wiser if we took down the level of explanation, and made it after-the-fact, with far fewer permissions required at steps I don't always grok, except at the same high level which inspires a generalized trust of your methodologies.*

---

## Wiki Narration Visualization

**Working URL (local):** `file:///Users/tomloughran/Documents/Claude/Projects/RC%20Karpathy%20Wiki%20Project/wiki/wiki_narration.html`

**Vault path:** `/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/`

### Key Files (relative to vault root)
- `wiki_narration.html` — the generated visualization (self-contained, ~38.5MB as of 2026-08-04)
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
- 3864 nodes (wiki files), 98,201 edges (wikilinks + shared references). **Do not hand-copy
  these forward** — the regen writes them to `wiki/c2a2-wiki-narration/scripts/build_meta.json`,
  which is the source of truth. (Read on 2026-08-04.) **`build_meta.json` describes the
  SHIPPED build, not the newest code.** The determinism fix of 2026-08-04 deliberately
  restored it so the guard's baseline still matches origin, and `wiki_narration.html` was
  not regenerated — so a fresh build measures larger (~40.6MB / 3893 nodes / 98,715 links)
  and that is not drift. Both numbers are true about different things; say which you mean.
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

## Talk to the Wiki — Realtime Voice Guide + FAQ Agent

**Voice guide** lives inlined in `wiki/explorer.html` (the shell, not an iframe tab, so it is exempt from the iframe-asset rule but MUST stay inline there). Floating "Talk to the Wiki" pill, bottom-right, draggable by its header. Uses the **OpenAI Realtime API over WebRTC** (voice-to-voice, native barge-in):
- Mint ephemeral token: `POST /v1/realtime/client_secrets` (token at `.value`); SDP: `POST /v1/realtime/calls`. Model `gpt-realtime`, voice `cedar`. (The old `/v1/realtime/sessions` + `/v1/realtime?model=` preview endpoints 404 — do not revert to them.)
- Key: reuses `localStorage['tts_api_key']` (shared with the Sociogram OpenAI TTS). `getKey()` only accepts/stores `sk-` values, so a browser-autofilled junk value can never clobber the shared key.
- Action tool `switch_tab` drives the shell's own tab buttons by voice.
- The **Record** button captures the guide's replies: the assistant's WebRTC stream is mixed directly into the recording graph (`addStreamToRecMix`), independent of Chrome tab-audio sharing.

**FAQ agent** keeps the guide's first-pass answers current AND deepens them over time toward **100 questions** (`TARGET_TOTAL`), then adds ~1/week. Split by Rule 5:
- **Deterministic** (`scripts/voice_faq.py`): `scan` parses every explorer tab + its help text, hashes each feature, diffs against `voice_faq/state.json` → new/changed/unchanged/removed. `status` prints total/target/deficit/phase + per-feature counts (thinnest first). `merge <qa.json>` is **ADDITIVE** — appends authored Q&A per feature, deduped by normalized question (never overwrites); validates (known keys, non-empty q/a, new features need ≥3 seed pairs); writes `wiki/voice_guide_faq.json` + `voice_faq/report.md` + updates state. Phase = `ramp` while total < 100, else `steady`.
- **Generative**: the weekly Claude agent `c2a2-voice-faq-weekly` (Sunday ~06:15) runs `status` + `scan`, then: seeds NEW features, adds corrected pairs for CHANGED ones, and DEEPENS — in `ramp` it authors ~10–15 spread across the thinnest features (high-level → detail); in `steady` it authors exactly **one** genuinely new, more-detailed question. Report-only — **never auto-pushes** (LLM-authored data → human review, per the no-blind-push rule).
- Seeded to **102 Q&A across 14 features** (2026-07-18), so it starts in `steady`.
- The guide `fetch`es `wiki/voice_guide_faq.json` at session start and injects it into the Realtime instructions as its first-pass source; missing file → falls back to built-in knowledge.
- `voice_faq/` (state + report) is gitignored like `janitor/`; `wiki/voice_guide_faq.json` IS tracked/published.

### Manual regen
```bash
python3 scripts/voice_faq.py status
python3 scripts/voice_faq.py scan --pretty
python3 scripts/voice_faq.py merge /path/to/qa.json      # additive; --dry-run to preview
```

---

## Daily-Run Commit Step (the sandbox cannot write .git)

**Script:** `scripts/commit_daily_run.sh` (+ `scripts/test_commit_daily_run.sh`, 41 assertions)
**Runs:** 05:45 daily, first step of the `com.c2a2.scheduled-commit-check` launchd agent
**Commits. Never pushes.**

`c282-wiki-agent-daily-run` completes its whole job and then reports, verbatim:

> `Phase 6 (Commit/push): BLOCKED — sandbox cannot write .git objects. Must run on Mac.`

This is **not** a hang and **not** a permission prompt — the two are separate problems and
were conflated for a while. The scheduled task is structurally unable to write git objects,
so every day's output stayed in the working tree (74 paths by 2026-08-05) and
`check_scheduled_commits.py` failed daily asserting something the sandbox can never do.
This closes it from the Mac, where the credentials and write access are.

It replicates Phase 6 of the run's own SKILL.md — same pathspec, same
`community_explorer.html` guard, same `C2A2 daily run` subject that
`check_scheduled_commits.py` greps for — and adds guards a sandboxed model cannot enforce
on itself.

### Why it does not push
CLAUDE.md's standing rule is that nothing reaches GitHub unreviewed; the lone carve-out is
the heartbeat's data-only refresh behind a CI gate. Daily-run output is wiki **content**,
the exact class that rule protects. Committing turns an unbounded working-tree pile into a
reviewable commit. Pushing stays a human act.

### It refuses (exit 1, tree untouched) when
- the repo is mid-merge/rebase/cherry-pick, or a `.git` lock is present
- HEAD is detached, or the branch is not `main`
- the daily run's `lastRunAt` is older than 25h — **then the dirty tree is someone else's
  work**, and committing it under a "C2A2 daily run" subject would be a lie in the log
- any staged path escapes the allowlist (`wiki/` + six named `prototypes/` files)
- more than 400 paths staged — a ceiling, not a target; a bulk regen or mid-flight vault
  sync should stop it
- `thomas.loughran@gmail.com` appears in the staged diff. It refuses at **commit**, not at
  push: history survives deleting the file
Every refusal path resets the index first — bailing with a half-built index leaves state
nobody created on purpose.

### The authorship check — it holds, it does not refuse
The 25h `lastRunAt` guard answers *when the run happened*. It never answers *which files
the run wrote*, so on a normal morning every dirty `wiki/` path was staged regardless of
author. On **2026-08-05** that would have committed a concurrent session's front-door
redesign: `start_here.html` rewritten to link `what_is_saying.html`, a page that session
had not finished writing — a dead link on the entry page, under a "C2A2 daily run"
subject, with the real author erased.

Any staged path whose mtime is **more than 45 minutes past run-start**, and that is not a
named post-run producer (`wiki/agents/openstory/`, `wiki/agents_tab.html` — the telemetry
refresh, ~06:19), is **unstaged and held**. The run's own output still commits; refusing
the whole run would strand a legitimate day's work every time somebody edits `wiki/` in the
morning. If everything staged is held, that is exit 0 and a no-op.

**Held is not skipped.** The paths are named on stdout (the launchd log) *and* appended to
`scheduler/held_paths.md` — same one-line-per-run shape as `commit_check.md` and
`run_stall.md`, so a held path is still legible after the log scrolls. `morning-system-health`
reads it. A skip nobody can see afterwards is the exact failure this script exists to end.

Clear a held path by committing it yourself, or re-run once its author is done.

mtime is sound here only because these are local writes to a live tree. A branch switch or
fresh clone restamps everything and holds the lot — loud, and correct, on a tree nobody
built on purpose.

```bash
bash scripts/commit_daily_run.sh --dry-run
bash scripts/test_commit_daily_run.sh
```

---

## Scheduler Health (did every job fire, survive, and produce?)

**Script:** `scripts/check_scheduler_health.py` (+ `scripts/test_check_scheduler_health.py`)
**Runs:** 05:45 daily, inside the existing `com.c2a2.scheduled-commit-check` launchd agent
**Writes:** `scheduler/scheduler_health.md` (gitignored, sibling of `commit_check.md` / `run_stall.md`)
**Read by:** the `scheduler-health-check` task at 07:00, which now only *reports* it

### Three questions, in code

| question | asked against |
|---|---|
| did it fire? | launchd `runs`; registry `lastRunAt` vs a cron the script evaluates itself |
| did it survive? | launchd `last exit code` |
| did it produce? | the date the artifact **records about itself** — never an mtime |

Covers **70 registry tasks + 11 launchd agents + the artifact table**. Live 2026-08-05:
**78 OK / 4 WARN / 0 FAIL**. Earlier baseline
2026-08-04: 79 OK / 1 WARN / 2 FAIL.

### Why it replaced a watchdog that already existed

`scheduler-health-check` had run daily for months and caught none of the week's four
silent failures, because it was blind three ways:

1. It enumerated tasks with `mcp__scheduled-tasks__list_scheduled_tasks`, which returns
   only the **calling session's** registry — **1 task of 70**. Its "all N enabled tasks
   healthy" was N=1. Reading the registry JSON directly is the whole fix.
2. It knew nothing about launchd, so `com.c2a2.metabolism-publish` at `runs = 0` was
   never in scope. **A job that never fires writes no log**, so "read the log" finds
   nothing and reads as "not yet".
3. Its output check used **mtimes**. Git does not preserve them, so on a tracked file
   that check is blind by construction.

It cannot live inside the 07:00 task: the registry is under `~/Library/Application
Support/Claude/` and scheduled tasks only mount `~/Documents`. Same constraint that put
`check_scheduled_commits.py` behind a launchd agent. **Only `launchctl kickstart` tests
the real path** — a Terminal shell has its own TCC grant and proves nothing.

### Three deliberate tolerances (do not "fix" these)

- **One missed fire passes; two fail.** One miss is a laptop asleep at 04:30. A report
  that cries wolf is not read.
- **`runs = 0` is only a FAIL once a fire has come round since the job loaded.** A weekly
  agent reloaded on Monday has not failed by Wednesday; it has not been asked yet. The
  reload time is the installed plist's **mtime**, a proxy — launchd does not report when a
  service was bootstrapped, and rewriting the plist is what forces the reload. A
  bootout/bootstrap with no file edit would not move it and would read as FAIL, which is
  the safe direction to be wrong in. Jobs with no readable `StartCalendarInterval` get no
  excuse: `runs = 0` stays FAIL.
- **`VERDICT_EXITS`** — an agent that *is* an assertion exits nonzero to mean "the thing
  I watch is broken". Treating that as an agent fault would leave this permanently red on
  exactly the days the other watchdog is working. Only the listed codes are excused;
  78 (the macl-xattr trap) and 2 still FAIL.

The cron evaluator is strict on purpose: an unparseable expression raises rather than
matching everything, because match-everything turns every stale task into a pass.

### Adding a check
Append to `ARTIFACTS` in the script (owner, path, dotted JSON field holding an ISO date
the producer wrote, max age). If a producer does not date itself, **make it** — do not
fall back to mtime. Then extend the test; every assertion there is driven through its
failure path.

```bash
python3 scripts/test_check_scheduler_health.py
python3 scripts/check_scheduler_health.py --quiet
```

---

## Level-2 Cross-Tradition Signal Stream

**Never hand-build `wiki/level2_signal_stream.html`. Always regenerate it:**
```bash
bash scripts/regen_level2_signals.sh
```

**Wired 2026-08-04** as Phase 5.6 of `c282-wiki-agent-daily-run` (after Phase 0/1, so the day's newly-approved cards are harvested in the same run). `metabolism-regen-daily` at 05:50 reads the result, so a rebuild lands on the metabolism yield axis the same morning.

### Why the wrapper exists
The stream was built ONCE by hand on 2026-06-28 and copied into `wiki/`. Nothing ever rebuilt it, so its newest signal stayed **2026-06-23** while the vault kept producing — 192 signals across 23 days went unpublished. `wiki/metabolism/scripts/build_metabolism_view.py` counts this file for its cross-tradition-signals/day axis, so the metabolism view drew a **flat, honest-looking zero for six weeks** and nothing anywhere threw. A frozen artifact and a genuinely quiet upstream render identically; only a standing rebuild plus a freshness assertion tells them apart.

### The chain (all deterministic — Rule 5, no model passes)
`prototypes/extract_signals.py` (vault `flags/` + `master/` index) → `prototypes/backlog/build_manifest.py` (approved cards not yet covered) → `prototypes/harvest_signals.py` (each card's `## Cross-Tradition Signals` section) → `prototypes/build_prototype.py` (inline the data into one HTML).

### Guards
Built in a temp dir, **promoted only on pass** — a rejected build never overwrites the accepted one. Rejects on: harvest coverage gate not PASS, `SIG` array in the built HTML failing to parse or disagreeing with `signals_grown.json`, or a >10% count drop against `prototypes/level2_build_meta.json` (tracked, written last). Staleness (newest signal older than `LAG_WARN_DAYS`, default 21) is a **loud WARN, not a rejection** — a correct rebuild of a quiet upstream is still correct; the daily run quotes that line into its report.

`build_metabolism_view.py` records `_meta.signal_source` (status / records / latest / `stale_days`) so a zero on that axis carries its own provenance, and `metabolism_monitor.py` forwards the builder's stderr on success too (these WARNs all arrive on exit 0; swallowing them is how the freeze stayed invisible).

`qc_trace.csv` is promoted only when a column other than `date_processed` moved — otherwise a daily run would commit a ~220-row date-only diff every morning.

**Tests:** `bash scripts/test_regen_level2.sh` — 15 assertions driving the failure paths (collapse, empty vault, staleness WARN, and both qc_trace cases), each asserting the accepted HTML survives. Run it by hand when build logic changes.

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
