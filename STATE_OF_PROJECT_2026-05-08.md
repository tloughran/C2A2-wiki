# State of the Project — Wiki + C2A2 Explorer

*Compiled 2026-05-08 (Friday) from a deep walk of `wiki/`, the `architecture/` self-awareness pipeline, the agent network's run logs, the four Explorer sub-tabs (Sociogram, 3D PRS, Agent Map, Curriculum Tools), recent commits, and the most recent session archive.*

---

## Executive Overview

You have, in functional terms, two distinct artifacts that share a single backing store:

1. **The Wiki** — an active, agent-driven, MacIntyre-style tradition-accelerator with eleven research-program corpora, two integration layers (Master + Pattern Detector), a five-agent self-awareness pipeline (14a/14b → 15a/15b/15c/15d), and a sixteenth deferred-action monitor. It runs on a daily 8am orchestrator with six weekday specialist agents at 7am, plus a Sunday 20:00 weekly review and a 21:00 nightly Summa vault sync.

2. **The C2A2 Explorer** — `wiki/explorer.html`, a four-tab shell (three stubbed under construction, one live) that exposes the Wiki to the world through four working sub-tools: Sociogram, 3D PRS, Agent Map, Curriculum Tools.

Both are **working** in the strong sense — the daily run is producing real cross-tradition findings, the public GitHub repo is live, the Explorer has demoable polish — and **partially broken** in the same sense — review throughput is the bottleneck on the agent side, and the Sociogram's narration engine and several UX rough edges are visible in the public demo. The point of this report is to make those simultaneous truths concrete enough to drive the next dev sessions.

---

# PART ONE — THE WIKI

## 1.1 Goals

The Wiki has three governing goals, each visible in its file structure and run logs:

- **Tradition acceleration.** Hold each research program (Levin, Friston, Hoffman, Hawkins, McGilchrist, Fredrickson, Stump, Carroll, Arkani-Hamed, Wolfram, Kastrup) at second-first-language depth — enough that an AI agent can carry on a mature internal conversation in that idiom. The eleven `traditions/<name>/wiki.md` + `prs_triplets.md` pairs are the artifact of that goal.
- **Cross-tradition detection.** Surface where two or more programs converge, conflict, or formally bridge. The instruments are `master/cross_program_index.md` (CROSS-001 through CROSS-058), `flags/pattern_detector_findings.md` (FINDING-001 through FINDING-018a), and the explicit Pattern Detector evaluation protocol.
- **MacIntyre-grade methodological self-awareness.** Catch the Wiki's own assumptions and presumptions before they ossify. The `architecture/` folder runs this layer: `assumptions.md` (87 entries), `presumptions.md` (103 entries), `decisions.md` (25 candidates, several promoted), `open_questions.md`, plus the 14a→14b→15a→15b→15c→15d cycle with documented disposition rules.

These three goals are wired together: program agents feed the Master, the Master feeds the Pattern Detector, and the self-awareness pipeline audits all of it. That tight loop is what makes the Wiki different from a static knowledge base.

## 1.2 What's Working

**Agent network — fully operational.** 13 named agents in `wiki/agents/` (`01_levin_agent.md` through `13_pattern_detector_agent.md`) plus the self-awareness layer (`14a` assumption extractor, `14b` presumption detector, `15a` lit-search-for, `15b` lit-search-against, `15c` net evaluator, `15d` periodic monitor) and `16_deferred_action_monitor_agent.md`. The daily orchestrator `c282-wiki-agent-daily-run` runs at 8am; six weekday specialist tasks at 7am cover Mon (Levin+Friston) through Sat (Wolfram). The most recent metrics snapshot (`architecture/metrics/2026-05-05_snapshot.md`) reads as a live system: 169 PRS triplets, 58 CROSS items, 19 findings.

**Decision throughput is moving — barely.** The newest entry in `wiki/review/archive/` is `2026-05-08_decisions.md`, recording today's email approval of the seven 2026-04-28 proposals (Levin Pai, McGilchrist Great Simplification, Stump What-are-we, three Wolfram, one Hoffman). That ten-day lag from approval-batch to ingestion is the largest visible operational drag.

**Self-awareness pipeline producing output.** `architecture/decisions.md` has DECISION-021 through DECISION-025 in candidate state with explicit promotion criteria. `15d_run4_2026-05-05_report.md` shows the periodic monitor re-queued 57 items on 2026-05-05; the lit-search queue stands at 188 items / 119 dispositioned. The pipeline is not just instrumentation — it's actively driving REVISE-flagging and MONITOR backlog.

**Cross-tradition signals at a productive density.** FINDING-011 (the SUPER-BRIDGE: Hoffman trace logic → Friston Markov blanket → Kastrup dissociative boundary) sits as the network's most significant open signal, reinforced by the 2026-04-28 batch of 26 approved proposals. CROSS-051 through CROSS-058 capture the highest three-way ontological adjacency in network history (Levin Platonic Space ↔ Hoffman conscious-agent space ↔ Wolfram Ruliad). FINDING-018a (Hawkins × Friston operational prediction) is the first concrete falsifiable cross-tradition synthesis the network has generated — directly relevant to the ISMcI summer paper.

**Infrastructure scaffolding.** Nightly Summa vault sync at 21:00 (`sync_vault.sh` + launchd plist; last successful run 2026-05-07 21:00 with `0 entries updated, 457 total available`). Weekly review pipeline at Sunday 20:00 (`weekly_review.plist` + `scripts/generate_weekly_review.py`); 2026-W19 review HTML is in `wiki/review/`. The Summa-2026-wiki companion repo is public and serving the Curriculum Tools tab via GitHub Pages.

**Public artifact landed.** `github.com/tloughran/C2A2-wiki` has been public since 2026-05-04; pre-public history scrub (RSA private key, ISME draft) is complete. `main` branch is now the explorer-shell-v2 merge. The "shipped within 24 hours of Karpathy's tweet" claim is documented in commits and live for the ISMcI paper.

**Total file count.** 822 markdown files in `wiki/` (excluding `.git/`), 596 modified in the last seven days. Most-modified subfolders this week: `architecture/` (358 files touched), `vault/` (100), `inbox/` (90).

## 1.3 What's Not Working

**Review-decision lag is the system bottleneck.** The 2026-04-28 batch of seven proposals was approved today, 10 days after generation. ASSUMPTION-012 in `architecture/assumptions.md` already names review throughput as the gating factor; the 2026-04-28 metrics snapshot says the pattern is now empirically confirmed. Twenty-one proposals sit in `inbox/proposals/pending/` (most from 2026-05-04 and 2026-05-05) waiting on the next decision email. Until that lag closes, Pattern Detector findings, CROSS additions, and PRS-count growth are all delayed by a week or more.

**Sandbox cannot push to GitHub.** Documented in the public-repo memory and in the 2026-05-05 session archive. Any commit Claude prepares has to be force-pushed from your Mac. This is fine when you're at the keyboard, but it removes the option of fully unattended git work and makes the daily orchestrator's Phase 6 a hand-off step rather than a closed loop.

**Sandbox mount blocks deletes and chmod** even on files the agent itself created. `tar-pipe with --no-same-permissions --no-same-owner` is the documented workaround. Same class of issue: old `review/*.html` files cannot be cleaned up by the orchestrator's Phase 5 (extended ACLs); they persist in the repo as visual clutter.

**DECISION-025 (Wright + Rohr addition; Stump metaphysical demotion) is blocked.** The two-line change to `traditions/` registry is gated on resolving OPEN-036 (does the addition propagate to C2A2 or stay in Summa-2026-derivative scope?) and OPEN-037 (Stump-demoted vs. Stump-as-live-metaphysics tension produced same-day by the 2026-04-26 specialist run). Eight underlying presumptions (PRESUMPTION-070 through 080) need to be surfaced and dispositioned. This is not a code problem; it's a paradigm-registry problem the human has to decide.

**The thirteen named tradition wikis are thin.** Each `traditions/<name>/wiki.md` is a single overview document with seven-to-ten Active Research Questions and a Solved/Advanced table. The depth lives in `prs_triplets.md` (per-tradition triplet logs) and in `inbox/` content. There is no visible per-tradition longform synthesis — no chapter-style "Levin: a state of the program 2026-Q2" document. For ISMcI-grade public defensibility, that thinness will eventually become visible.

**Inbox vs. proposal pipeline naming is split.** Top-level `inbox/` contains daily named files (98 entries, mostly 2026-04-07 to 2026-04-28). `inbox/proposals/` contains the proposal-pipeline structure (`pending/`, `approved/` 86 files, `needs_review/` 1 file). Those two stores duplicate concepts (some inbox entries are dated proposals). The proposal pipeline is the live one; the top-level `inbox/` is a partly-superseded daily-drop store.

**Two-format sources in some places.** `master/C2A2_master_wiki.md` exists alongside `master/C2A2_master_wiki.html` — the Master Agent writes both. Drift between them is currently minor but is a real source of truth ambiguity if either ever gets edited by hand.

**Self-awareness pipeline metrics are getting heavy.** 87 assumptions + 103 presumptions = 190 self-awareness items, with 64 REVISE-flagged and 65 in MONITOR queue as of 2026-05-05. The 15d periodic monitor re-queued 57 items in run 4. There is no explicit pruning protocol for items that have stayed UNTESTED across many cycles. This will grow.

## 1.4 Areas for Improvement

**Close the review-decision loop.** The single highest-leverage Wiki change. Options I see in the data: (a) reduce batch size — review every 2-3 days rather than every 7-10; (b) add a one-line decision shortcut so a proposal can be approved by reply-Y rather than a structured email; (c) auto-approve specialist proposals from a vetted thinker after N days unless explicitly rejected (high-risk); (d) move the review HTML into the Explorer itself with a click-to-approve UI.

**Resolve OPEN-036 / OPEN-037 to unblock DECISION-025.** Wright and Rohr are sitting in `traditions/` already (their folders exist with `wiki.md` placeholders) but are not yet exercised by the agent network. A single conversation with you about whether they're C2A2 traditions or Summa-derivative-only would unblock the canonization.

**Per-tradition longform synthesis docs.** Add `traditions/<name>/state_2026_q2.md` for each tradition — a 1500-2000 word essay-grade summary the Master can keep current. This is the thing that actually shows up in your ISMcI paper bibliography.

**Prune or escalate the self-awareness backlog.** Define a cutoff: any UNTESTED assumption/presumption past N=8 cycles gets either escalated to Tom for a flag-vs-park decision or auto-MONITORED. The current pipeline accumulates without a draining mechanism.

**Reconcile `inbox/` vs `inbox/proposals/`.** Either lift the daily-drop store into `inbox/proposals/incoming/` so there's one canonical pipeline, or document explicitly which is which in `inbox/README.md`.

**Single source of truth for the Master Wiki.** Pick one of `C2A2_master_wiki.md` or `C2A2_master_wiki.html` as canonical and generate the other.

---

# PART TWO — THE C2A2 EXPLORER

## 2.1 Goals

The Explorer's goals are explicit in `wiki/EXPLORER_VISION.md` (2026-05-05) and `wiki/EXPLORER_V2.md`:

- **Be the public face of the Wiki.** A visitor lands on `explorer.html` and sees a serious system, not a folder of markdown.
- **Lay out the full architecture as four chapters.** Tab 1 Community Explorer (PRS-structured community profiles), Tab 2 Community AI Education (the AI Heartbeat tool, currently external), Tab 3 Community Accelerator Tools (the four working visualizations), Tab 4 Community Interaction (the future dialogue layer). The three stubbed tabs are deliberately visible — they preview the whole system, with "🚧 Under construction" mouseover signage.
- **Let the user climb into a perspective.** EXPLORER_VISION calls the Sociogram a "tool for entering another perspective. You have to put a team on the field." The 3D PRS view, Agent Map, and Curriculum Tools each express that idea at different magnifications.
- **Eventually be mirrorable / scrapable.** Section 7 of EXPLORER_VISION envisions a configurable instance — drop in your own thinkers, your own agents, design your own Sociogram.

## 2.2 What's Working

**Shell renders correctly.** `explorer.html` (446 lines, 15kB) is a clean two-row tab bar. Row 1: brand + four chapter tabs + Record button. Row 2: four sub-tool tabs scoped to the active chapter (Sociogram / 3D PRS / Agent Map / Curriculum Tools). Stubbed chapter tabs are dimmed and unresponsive with construction tooltips, exactly as documented in EXPLORER_V2.md. The active sub-tool loads in an iframe.

**Sociogram (`wiki_narration.html`, 6.5MB) is at "Pass G" maturity.** Reading the May 5–7 commits in order:

- *Pass A* — adaptive edge density;
- *Pass B* — multi-vault Summa integration;
- *Pass C* — Summa-specific edges;
- *Pass D/E* — first-impression polish (two-stage Fit All, brighter link baseline, brightness slider headroom 0.1–2, invisible hover hit-test halo);
- 3D PRS becomes a true data explorer (commit `138b35d`);
- *Pass F* — Summa headlines, pop-out window button, LINKS interning;
- *Pass G* — dynamic banner counts, Content-tags cuts, date slider.

The Sociogram now exposes: traditions filter (15 thinkers), structure filter (10 categories), content-tags filter, date threshold slider, brightness slider (max 2), Hold Forces / Show Hover Names / Fit All controls, six narration tracks (Intro/History/Recent/Latest × Brief/Deep), TTS via browser and OpenAI backends, edge-click panel toggle, edges-help popover, pop-out window for both panels. 1647 nodes, ~3000 edges, crash-proof at 2000/3000 caps.

**3D PRS (`prs_3d.html`, 209kB) is now a real data explorer.** Per the 2026-05-05 session archive and the memory entry, three independent cut axes are wired: Traditions × Disciplines × Years, with edges derived from currently-visible nodes (orphan edges never drawn), a "Reset" button that clears all cuts, and per-cut "?" help popovers. Confirmed working 2026-05-05.

**Agent Map (`agents_tab.html`, 67kB).** Inside-view of the agent ecosystem. Per the EXPLORER_VISION text, this is infrastructure visibility, not user-facing — the audience is you and people who want to see how the network is built.

**Curriculum Tools (`summa_explorer.html`, 44kB) is live.** Fetches `vault/refs/summa_index.json` from the local `vault/` (or from the Summa-2026-wiki GitHub Pages site in PROD), exposes Days 1-50 of the Summa-in-1-year transcript track plus Contemporary-Synthesis toggle, has Contents and Sociogram sub-tabs in its left panel. `wiki/vault/transcripts/` contains 50 day files and `wiki/vault/synthesis/` mirrors them. The 2026-05-07 commits confirm the GitHub Pages fetch path is fixed and reindexing is hardened.

**Public-repo CONSTITUTIONAL RULE in CLAUDE.md.** "No blind pushes to GitHub" is now documented at the top of the project's CLAUDE.md as a result of the `adbd456` incident — local HTTP server + browser-eyes-on inspection before any push.

**Session archive workflow.** `c2a2-wiki-narration/scripts/archive_session.py` plus the four-stage Regen → Inspect → Push → Archive workflow lets sessions survive as wiki-readable markdown in `wiki/session-archive/`.

## 2.3 What's Not Working

**The 2026-05-05 video-review punch list is mostly still open.** The session archive captured 20 observations. Status as of today:

- **Items closed:** #1 Macintyre/McGilchrist/Arkani-Hamed label typos (commit `138b35d`); #5 brightness slider max raised; #4 hover-hit-test halo; #3 first-impression auto-Fit-All. The 2026-05-07 c282 voice-typo scrub also landed.
- **Items still open:** #2 1659 vs 1647 file-count display reconciliation; #6 narration-panel right-margin truncation (likely a `clamp()` / resize-listener fix); #7 track-button state doesn't reflect playback (yellow stays on the clicked button); #8 Intro/History/Recent/Latest + Brief/Deep are ungrouped and unlabeled; #9 the big red "Stop" button at top-right looks like a system kill-switch but is actually screen-recording stop; #11 3D PRS year/discipline label collisions; #12 C2A2 Master appears as STRUCTURE in Sociogram and as a Tradition-equivalent in 3D PRS — same group, two mental models; #13 STRUCTURE > Master unchecked by default; #14 Intro narration ~2 minutes over a static graph (no progressive reveal); #15 Agent Map circle-vs-filled-dot legend missing; #16 Agent Map activity-log truncation; #17 Curriculum Tools has its own "Sociogram" sub-tab — same word, two different graphs, naming collision; #18 Curriculum Tools header progress bar not wired to actual coverage; #19 Day badges not in the Contents tree; #20 no intro/closing card on the recording.

**Narration engine temporal/semantic mode state leakage (Priority 1 in EXPLORER_V2.md).** Three attempted fixes shipped (full stop before mode switch, 50ms gap after `cancel()`, double-cancel with silent flush utterance) — none resolved the symptom. The likely remaining culprits are documented: speech-synthesis queue depth deeper than 50ms can drain, `advancePlay()` re-entry without an `isSwitching` flag, and stale `currentTrack` reference across mode switches. The recommended next move is `console.log` instrumentation across `toggleNarrationMode`, `scheduleNextSegment`, `advancePlay`, and `TTS.speakBrowser` to trace actual execution order.

**Lower-left narration-epochs slider is in limbo.** Memory entry from 2026-05-06 flags it as "next session priority" — needs (a) functionality verification (no dead positions), (b) redundancy check against the Pass-G date slider and the 6-track narration matrix, (c) a "?" popover matching the banner / edges / content-tags help-popover pattern.

**Three chapter tabs are deliberately stubbed.** Community Explorer (Tab 1) was already built before Karpathy and needs integration. AI Heartbeat (Tab 2) was built in February pre-Cowork and needs a UI rebuild. Community Interaction (Tab 4) is genuinely future. The "Under construction" tooltips honor the public-draft framing, but every visitor sees three-quarters-empty chapter row.

**Twelve changelog files silently excluded from Sociogram counts.** `architecture/changelog/` holds 12 .md files that are intentionally excluded by the graph builder (so 1659 wiki files → 1647 graphed nodes). The header still reads "1659 files" in some places and "1647 nodes" in others. Either show "1647 nodes / 12 excluded" with a tooltip or split into two pills.

**Public-repo footprint is thin.** The repo is public, but a visitor landing on `github.com/tloughran/C2A2-wiki` from the Karpathy claim sees mostly a wiki vault and a single `explorer.html`. There is no README that frames "open `wiki/explorer.html`" as the entry point, no demo video link, no architectural overview at the top level. The substance is real; the wayfinding is sparse.

**Workflow polish gaps in Curriculum Tools.** Per session-archive observations #18 and #19: the "375 of 2648 articles available" header is not wired to actual per-question coverage; Day badges live only in the right-hand article index, not the left-hand contents tree, even though Days are the temporal spine of the Summa-in-1-year pedagogy.

## 2.4 Areas for Improvement

**Close the May-5 punch list as an explicit work block.** Twelve to fourteen of the twenty observations are 30-minute fixes; doing them as a single session ("punch-list pass H") visibly lifts the public demo. Sequence by visibility-per-minute: typos and counter reconciliation (#2) first; control labeling and grouping (#7, #8) second; legend/UI polish (#15, #16, #17, #19) third.

**Resolve the narration engine mode leakage.** Add the recommended `console.log` instrumentation, capture an actual mode-switch trace, and write the fix from the trace rather than from speculation. EXPLORER_V2.md flags this as Priority 1.

**Audit the lower-left narration-epochs slider.** This is the queued task from memory. Either (a) merge it into the date threshold slider if it's truly redundant, or (b) keep it and add the "?" popover. Either way, write down what each slider position means.

**Wire the Curriculum Tools header to real coverage.** A reader needs to see at a glance which Summa questions are stubbed vs. complete. The data is there in `vault/refs/summa_index.json`.

**Add a README at the C2A2-wiki repo root.** "Open `wiki/explorer.html` to start. The Sociogram (graph), 3D PRS (axes-cut explorer), Agent Map (infrastructure view), and Curriculum Tools (Summa-in-1-year) are the four working tabs." Plus a 60-second demo video link. This is the single highest-leverage change for the Karpathy-credibility audience.

**Recording chrome cleanup.** The big red "Stop" button is a known confusion point. Either hide it outside recording mode, recolor it from system-kill-red to neutral grey, or move it inside the recording-active overlay only.

**Resolve the "C2A2 Master" two-mental-models issue (#12).** Either expose Master as a tradition in both Sociogram and 3D PRS, or as a structure group in both. Pick one mental model.

**Resolve the Curriculum-Tools "Sociogram" naming collision (#17).** Rename the inner one to "Article Sociogram" or "Question Map" so visitors don't conflate the two graphs.

---

# Recommended Next Steps (Prioritized)

This is what I would do, in order, if I were sitting at the keyboard with you for the next several Cowork sessions:

**1. Wiki — close the review-decision loop.** Answer: do you want the agents' proposals reviewed every 2-3 days, or do you want a one-line approve/reject path that can be done in 5 minutes? A 10-day lag is the largest visible drag on the network's live signal generation. Concrete: spec out a "review widget" that lives inside `explorer.html` and auto-posts approve/reject to `inbox/proposals/approved/` or `inbox/proposals/rejected/` with one click, replacing the email round-trip.

**2. Explorer — punch-list pass H (the May-5 closure).** Single session. Order: Sociogram counter reconciliation, narration-panel truncation, control labeling, recording-button cleanup, Curriculum Tools coverage wiring, naming-collision rename, Day badges in Contents, intro/closing video card. Ten to fourteen line items, all in `wiki_narration.html`, `summa_explorer.html`, and `agents_tab.html`. Local HTTP server inspection per the constitutional rule before any push.

**3. Explorer — narration engine instrumentation + fix.** Priority 1 from EXPLORER_V2.md. `console.log` trace first, fix second. Dedicated session.

**4. Explorer — narration-epochs slider audit.** Smaller than #3. Either merge into date slider or add the "?" popover. Probably 30 minutes once you've decided which.

**5. Wiki — resolve OPEN-036 / OPEN-037 to unblock DECISION-025.** Conversation, not code. Once decided, propagate Wright + Rohr into the agent network and update the Stump-metaphysics role explicitly in `traditions/stump/wiki.md`.

**6. Wiki — per-tradition longform synthesis docs.** `traditions/<name>/state_2026_q2.md`, ~1500-2000 words each, generated by the program agents themselves and reviewed by you. Twelve documents (current 11 + the Summa-bridge Aquinas slot if we go that direction). This is the artifact your ISMcI paper will cite.

**7. Public-repo README.** 30 minutes. High visibility-per-minute.

**8. Self-awareness backlog pruning protocol.** Define the cutoff for UNTESTED-without-progress items. Codify in `architecture/decisions.md`.

**9. Inbox / proposals reconciliation.** Lift `inbox/` daily-drop into `inbox/proposals/incoming/` or document the split explicitly.

---

## Quick Reference

- **Wiki vault root:** `/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/`
- **Explorer entry point:** `wiki/explorer.html` (open via local HTTP server before any push)
- **Public repo:** `github.com/tloughran/C2A2-wiki`
- **Summa companion:** `github.com/tloughran/Summa-2026-wiki`
- **Daily orchestrator:** `c282-wiki-agent-daily-run` at 8am
- **Specialists:** Mon Levin+Friston, Tue Hawkins+Hoffman, Wed McGilchrist+Kastrup, Thu Stump+Fredrickson, Fri Carroll+Arkani-Hamed, Sat Wolfram (all 7am)
- **Nightly sync:** Summa vault sync 21:00 (`sync_vault.sh`)
- **Weekly:** Sunday 20:00 weekly review
- **Network state (2026-05-05):** 169 PRS triplets · 58 CROSS items · 19 Pattern Detector findings · 87 assumptions · 103 presumptions · 25 decision candidates
- **Most significant open signal:** FINDING-011 SUPER-BRIDGE (Hoffman trace logic ↔ Friston Markov blanket ↔ Kastrup dissociative boundary)
