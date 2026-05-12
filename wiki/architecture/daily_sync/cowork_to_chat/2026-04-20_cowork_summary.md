# Cowork Progress Summary — 2026-04-20 (Evening)
*Generated at 18:51 EDT (Monday evening scheduled run) for tomorrow morning's walk Chat context*
*Supersedes the earlier 11:43 EDT "morning-mislabeled-as-evening" summary, which has been preserved at `2026-04-20_cowork_summary_am.md`. The AM summary was already delivered to Chat; this PM update adds ~7 hours of afternoon activity.*

## What Was Accomplished Today

Monday 2026-04-20 started quiet-but-signal-rich (per the 11:43 EDT AM summary) and became **substantially richer in the afternoon**. Five scheduled tasks ran today, three of them after the AM summary was generated:

1. **Wiki daily run (morning)** — produced 2 candidate Levin proposals; Phase 6 commit still blocked by stale `.git/index.lock` from 2026-04-16 (five calendar days old). Unchanged from AM summary.

2. **Morning walk cowork handoff (morning)** — sixth+ consecutive null-walk-notes day; Gmail channel still degraded. Surfaced ASSUMPTION-046/047/048 + PRESUMPTION-053. Unchanged.

3. **Self-awareness daily (morning 14a/14b)** — produced the changelog, metrics snapshot, +4 assumptions, +6 presumptions, +3 open questions; logged 2026-04-19 GAP-NOTE. Unchanged.

4. **Lit-search pipeline (afternoon, ran ~11:50–11:57 EDT)** — **NEW since AM summary.** Processed all 13 QUEUED items from today's 14a/14b cycle in a single afternoon pass, closing the pipeline lag from 2 days back to 0. Six premises now incorporated (up from 5), including the first-ever INCORPORATE of a briefing-layer epistemic commitment (PREMISE-006 on transparent flagging of master-wiki narrative discrepancies). Surfaced three new clusters, raised two SYSTEMIC-RISK flags, and — notably — exposed an **INTERNAL-CONSISTENCY tension** inside today's own 14a cycle (ASSUMPTION-047 INCORPORATE vs ASSUMPTION-048 REVISE — same cycle produced a policy and a violation of that policy).

5. **Caching-architecture-monday one-time task (afternoon)** — **NEW since AM summary.** Produced three substantive deliverables in the local session outputs folder: (a) C2A2 Execution Protocol v1.0 (one-session-per-agent-run; 49 RC Wiki files as static cache prefix; dynamic suffix for pending/changelog; hard per-session caps; pipeline agents migrate from 5-session to 1-appended-turn pattern), (b) Levin Agent Template (splits joint Levin-Friston entry point into two; names 2026-04-27 as first v1.0 run; ~50% per-run cost reduction on Levin alone, 70–80% projected aggregate across pipeline agents), (c) RC Wiki MCP Install Plan (pre-flight: clear the 04-16 git lock first; then `bash setup.sh`, wire `claude_desktop_config.json`, three smoke tests including byte-stability for cache determinism).

6. **Weekly agent ecosystem report (evening, ran earlier)** — **NEW since AM summary.** Audited all 29 scheduled agents (21 active scheduled, 4 manual, 4 disabled). Flagged ~6 stranded agents for cleanup: `rc-wiki-morning-backup` (disabled, dark since 04-06), `dispatch-daily-summary` (manual-only but description reads as a nightly job; last fired 04-10), `openstory-install` + `openstory-monitor` (never ran; probably orphaned), `gdrive-book-pdf-lookout` (disabled expired one-timer), `macintyre-commentary-monday-reminder` + `caveman-install-monday` (completed one-timers). Overall health assessed as good; recurring schedule humming reliably; the one-timers are cluttering the registry.

7. **Self-awareness daily (evening, currently RUNNING at this write-time)** — started but not yet complete; uncertain whether it is running a legitimate second cycle for the day or is a scheduler artifact (the AM run already produced today's 14a/14b deliverables). A deliverable conflict is possible; flag for morning review.

Also of note: the **Levin-Friston specialist task** that was still running with 58+ WebSearch turns and no writes at AM summary time is now **idle** in the session list — meaning it has terminated one way or the other. No proposal-draft artifact has been observed in the wiki state, so the most likely outcome is natural termination (hit a turn/cost ceiling, or simply stopped) without any written output. This is a live test of PRESUMPTION-054 — an unbounded specialist task ran to ~wall-clock-end and produced zero artifacts.

## Key Decisions Made

*(No new formal DECISION-NNN entries written to `decisions.md` today.)*

Candidate decisions status (updated from AM):
- **DECISION-019 (candidate)** — `cowork-resume-session` phrase-triggered plugin. Unchanged.
- **DECISION-020 (candidate)** — regenerator default model bump to `claude-opus-4-7`. Unchanged.
- **DECISION-021 (candidate)** — handoff-via-file pattern. Unchanged; OPEN-029 still unresolved.
- **DECISION-022 (candidate)** — briefing-layer audit contract. **Status shifted this afternoon.** The lit-search pipeline's INCORPORATE on ASSUMPTION-047 (→ PREMISE-006) effectively ratifies the senior commitment behind DECISION-022 (transparent flagging over silent reconciliation); what remains is the concrete rendering convention — raw-data vs. annotation vs. structured metadata field. This is closer to ripe than it was this morning.
- **DECISION-023 (candidate, newly surfaced this afternoon)** — adopt the caching-architecture protocol (one-session-per-agent-run; RC Wiki 49-file static prefix; dynamic suffix; hard per-session caps). The caching deliverable names 2026-04-27 for first v1.0 run of the Levin agent, which is effectively a decision-forcing date.
- **DECISION-024 (candidate, newly surfaced this afternoon)** — specialist-task invariants (turn-cap / cost-cap / wall-clock timeout). OPEN-033 plus today's natural experiment (Levin-Friston ran unboundedly and produced zero artifacts) argue this should become formal rather than continuing as a candidate.

## New Open Questions

No new OPEN-NNN entries since the AM summary's OPEN-031/032/033. The afternoon's work reshaped those three rather than adding new ones:

- **OPEN-031 (cross-task coordination contract)** — reinforced by SYSTEMIC-RISK flag raised on CROSS-TASK-COORDINATION cluster. Moves up in priority.
- **OPEN-032 (generalized transience-threshold primitive)** — reinforced by the 15c SYSTEMIC-RISK flag on SELF-AWARENESS-META's recurrence pattern (PRESUMPTION-052 is the 7th member of that cluster). The "build a cheap freshness-SLO primitive" argument grew teeth this afternoon.
- **OPEN-033 (specialist task invariants)** — natural experiment completed today. Levin-Friston ran to termination, produced nothing. Empirical evidence for the turn-cap argument; candidate DECISION-024 is the disposition.

One new tension worth naming explicitly (though not yet filed as an OPEN): **INTERNAL-CONSISTENCY between ASSUMPTION-047 and ASSUMPTION-048** — same 14a cycle produced a normative policy (transparent flagging) and a practical violation of that policy (treating a stale placeholder as clear). 15c flagged this as a self-consistency event inside the pipeline's own output. Worth deciding whether this needs a formal OPEN-034 or can be absorbed as operationalization of PREMISE-006.

## Files Created or Modified

Afternoon additions (post-AM summary):
- `wiki/architecture/validated_premises.md` — PREMISE-006 added (5 → 6 incorporated); footer note on BRIEFING-LAYER-EPISTEMIC-COMMITMENTS fast-path pattern.
- `wiki/architecture/for_lit_search.md` — 13 items DISPOSITIONED (from QUEUED); pipeline lag flipped from 2 days to 0.
- `wiki/architecture/monitor_queue.md` — +5 MONITOR entries (ASSUMPTION-035, 037, 045; PRESUMPTION-037, 051); 3 cycle-1 refreshes; total now 49.
- `wiki/architecture/revision_flags.md` — +7 REVISE entries (ASSUMPTION-046, 048; PRESUMPTION-049, 050, 052, 053, 054); total now 45.
- `wiki/architecture/lit_search_returns.md` — daily cycle summary appended; PREMISE-006 rationale recorded.

Caching-architecture deliverables (session-local, not yet in wiki):
- `outputs/C2A2_EXECUTION_PROTOCOL.md` — the protocol v1.0 doc
- `outputs/LEVIN_AGENT_PROTOCOL_TEMPLATE.md` — concrete Levin application
- `outputs/RC_WIKI_MCP_INSTALL_PLAN.md` — install plan with git-lock pre-flight
- `outputs/C2A2_MONDAY_REPORT.md` — aggregator summary

Morning-summary contents (unchanged, preserved at `2026-04-20_cowork_summary_am.md`):
- `wiki/architecture/changelog/2026-04-20_changes.md`, `metrics/2026-04-20_snapshot.md`, +4 ASSUMPTIONs, +6 PRESUMPTIONs, +3 OPEN questions, GAP-NOTE for 2026-04-19, 10 QUEUED items (now all dispositioned), morning briefing, Agent 16 clean run.

Evening self-awareness daily (currently running): outputs pending.

## Pipeline Status

**Self-awareness registry:**
- Assumptions: **48 total** (+4 today; unchanged since AM)
- Presumptions: **54 total** (+6 today; unchanged since AM)
- Open questions: **33 total** (+3 today; unchanged since AM)
- Decisions formal: **18** (unchanged; 4 candidates this morning, now 6 candidates after afternoon developments: 019, 020, 021, 022 [closer to ripe], 023 [new], 024 [new])

**Lit-search pipeline — big afternoon movement:**
- Queue total: **100 items** (+10 today)
- Dispositioned cumulative: **91** (was 78 this morning; **+13 today**)
- Validated premises (INCORPORATE): **6** (+1 today → PREMISE-006 on BRIEFING-LAYER transparent flagging)
- MONITOR: **49** (+5 today; was 42 this morning)
- REVISE: **45** (+7 today; was 32 this morning)
- Pipeline lag: **0 days** (was 2 days this morning — caught up by today's 15c run)
- CRITICAL in MONITOR: 2 (unchanged)
- 3 new clusters surfaced: CROSS-TASK-COORDINATION (3 members), BRIEFING-LAYER-EPISTEMIC-COMMITMENTS (4 members), Unaudited-filter (3 members)
- SYSTEMIC-RISK flags newly raised: CROSS-TASK-COORDINATION, SELF-AWARENESS-META (7 members — first recurrence)

**PRS corpus — unchanged:**
- PRS triplets: **151** (Phase 6 still blocked)
- Cross-connections: **54**
- Proposals pending: **10 visible / 12 actual** (2 Levin proposals behind git lock)
- Pattern-detector findings: **17**

**Deferred action layer:**
- Agent 16 cycle clean; 0 items in any intake channel (unchanged all day)

**Self-awareness cycles skipped (cumulative): 1** (2026-04-19 GAP-NOTE; unchanged)

**Infrastructure health:**
- Git: **DEGRADED-COMPOUNDED** (lock at 5 calendar days; DECISION-018 rescue still unexecuted)
- Gmail (walk notes): **DEGRADED** (sixth+ consecutive null day; PRESUMPTION-052 strengthening)
- Chrome MCP extension: **OPERATIONAL** (AM sync delivered successfully to the daily walk conversation)
- Specialist agents (Levin-Friston): **TERMINATED** (ran ~unboundedly earlier, now idle; produced no detectable artifacts — natural experiment for OPEN-033/DECISION-024)
- Self-awareness evening cycle: **RUNNING** at write-time (possible scheduler duplication with morning cycle; flag for morning review)
- Review-folder ACLs: **DEGRADED** (no movement)
- Anthropic billing propagation: **DEGRADED** (no movement)
- Agent ecosystem registry: **CLUTTERED but HEALTHY** (~6 stranded one-timers/manual-only items flagged by weekly ecosystem report; no impact on active pipeline)

## What's Next

Near-term (Tuesday 2026-04-21):

- **Highest-priority unblock (unchanged, now six calendar days by Tuesday morning):** manual `rm .git/index.lock` + execute DECISION-018 rescue script. Without this, Phase 6 stays frozen, today's 2 Levin proposals remain invisible, and the caching-architecture deliverable's "pre-flight: clear git lock" gate blocks the MCP install plan too.
- **Formalize DECISION-024 (specialist task invariants):** the Levin-Friston natural experiment today is empirical enough that a minimal formalization is cheap. Recommended draft: "specialist scheduled tasks SHOULD declare an upper-bound turn count in their task definition; missing = 20-turn default; override requires explicit justification in the SKILL.md."
- **Audit the INTERNAL-CONSISTENCY tension (ASSUMPTION-047 vs ASSUMPTION-048):** decide whether to absorb ASSUMPTION-048 as an operationalization violation of PREMISE-006 (cleaner) or file it as OPEN-034 (more conservative).
- **Verify the evening self-awareness cycle's output:** check whether today's currently-running `c2a2-self-awareness-daily` wrote a second changelog/metrics snapshot that conflicts with the AM run. If yes, reconcile by taking the later one authoritative or merging.
- **Caching-architecture adoption decision:** the 04-27 first-v1.0-Levin-run date is one week out. Tom's call on whether to adopt the protocol (candidate DECISION-023) wants to happen by end of this week to leave implementation buffer.
- **Agent-ecosystem housekeeping:** ~10 minutes to delete the 6 stranded one-timers flagged by the weekly report.
- **Lit-search 15a/15b/15c pipeline:** caught up to 0-day lag, so no backlog for Tuesday.

Medium-term carried forward (unchanged from AM):

- CRITICAL null-baseline re-extraction test (PRESUMPTION-029 + ASSUMPTION-031) still pending from 2026-04-16 (day 4).
- Narrator richer-inputs Python work still not executed.
- OPEN-020 (benchmarks-milestone criterion for private→public publication) still blocks external-release conversation.

## For Morning Discussion

Five items worth chewing on during the walk (two carried from the AM summary that Chat already engaged with; three new from the afternoon):

1. **The git-lock is now a hard blocker on three parallel workstreams, not one.** Phase 6 wiki commits remain frozen (two Levin proposals trapped, pending-count a fiction), AND the caching-architecture MCP install plan has "clear the git lock" as its own pre-flight, AND the "generalized transience-threshold primitive" (OPEN-032) keeps pointing at this same lock as its canonical motivating example. Six calendar days by Tuesday morning. The cheap fix remains the cheap fix: a pre-flight probe + `rm`. This has moved from "should have done it last week" to "blocks three things simultaneously."

2. **PREMISE-006 is the day's concrete architectural gain.** First briefing-layer epistemic commitment to pass the disposition gate; validates the "transparent flagging over silent reconciliation" stance drawn from SRE/observability/XAI literature; supersedes and absorbs ASSUMPTION-048's "stale-as-clear" disposition (which is now a data-hygiene violation to remediate rather than a normative claim to validate). This effectively makes candidate DECISION-022 (briefing-layer audit contract) ripe enough to draft — the senior commitment is in; what's left is the rendering convention. Walk-worthy: **is this the week DECISION-022 gets formalized?**

3. **The Levin-Friston natural experiment happened without us designing it.** At AM summary time the task was still running at 58+ WebSearch turns with no writes; at evening sync time it's idle with zero observable artifacts. That's a no-cap specialist task that ran ~half a day, consumed an unknown amount of cost, and delivered nothing. PRESUMPTION-054's risk characterization just moved from "hypothetical" to "observed event." Walk-worthy: **does DECISION-024 (20-turn default cap) get formalized Tuesday, or wait for a full OPEN-033 literature pass?** The minimum-viable version is trivially cheap — even a default in the SKILL.md template buys most of the protection.

4. **The caching-architecture deliverable arrived as a substantial one-shot.** Three documents, concrete cost projections (50% Levin-alone, 70–80% aggregate), a named first-run date (04-27), and a pre-flight dependency on clearing the git lock. This is a decision-forcing function. Walk-worthy: **does Tom review the protocol this week, or defer it?** If defer, acknowledge that the 04-27 first-run date slips; if review, a 30-minute reading pass plus go/no-go is the critical path.

5. **An INTERNAL-CONSISTENCY flag inside the pipeline's own output is a new pattern.** 15c observed that today's 14a produced both a normative commitment (ASSUMPTION-047 → PREMISE-006) and a concrete violation of that commitment (ASSUMPTION-048, dispositioned REVISE). This is the first case where the self-awareness layer caught itself in a self-consistency violation within a single day. Useful evidence that the multi-agent structure actually works — the left hand noticed the right hand. Walk-worthy: **is this pattern worth naming and watching for across future cycles** (as its own cluster / flag type), or is today's instance a one-off?

Separately, one flag for the morning: the evening `c2a2-self-awareness-daily` task was still running at 18:51 EDT, and today's AM 14a/14b already produced the day's canonical changelog + metrics snapshot. If the evening run produces a second set, the two will conflict and want reconciliation. Worth a glance at 14a/14b artifacts first thing tomorrow.

---

## Delivery Status

**SUCCESS** — Evening addendum posted into the same daily walk conversation ("Morning planning walks and name confusion," chat ID `93f1a91d-e6e6-419b-8144-c2f838096f05`) at ~18:55 EDT, supplementing the 11:37 AM delivery. The payload was split into two messages (a header-separator newline triggered a send-on-enter for the first line; the body text went as the second message), both received intact. Chat-side Claude has read and engaged with the addendum. Notable confirmed-read responses: (a) endorsed absorbing ASSUMPTION-048 as a PREMISE-006 operationalization violation rather than filing OPEN-034 ("absorption is the move that takes PREMISE-006 seriously; filing a new open question would dilute that signal"); (b) endorsed minimal DECISION-024 in the form "specialist tasks SHOULD declare turn-cap; missing = 20" with explicit note to "not overthink the number — today the value is the existence of the cap, not its calibration"; (c) endorsed the caching-architecture 30-minute read tomorrow with 04-27 decision-forcing acknowledged; (d) raised a practical recommendation: pre-commit the evening-vs-morning self-awareness-cycle reconciliation rule TONIGHT rather than adjudicating it on the walk groggy. That last item is worth executing before end of this task if the evening self-awareness daily has finished — otherwise note it for morning.

*Autonomous choices noted for this run:*
- *Preserved the AM summary at `2026-04-20_cowork_summary_am.md` rather than overwriting it, to retain provenance of what was delivered to Chat earlier.*
- *Wrote this evening summary as the authoritative `2026-04-20_cowork_summary.md` file (the task spec's expected filename).*
- *Did not interrupt the currently-running evening `c2a2-self-awareness-daily` cycle; flagged the potential scheduler duplication for morning review instead.*
- *Did not attempt to ingest the caching-architecture deliverables into the wiki tree this run (they sit in the local session outputs folder); that's a separate chat_to_cowork / human-review decision.*
- *Payload split across two messages because a blank line between the header and body triggered an enter-as-send; total content delivered intact; noted here in case the pattern recurs and needs a fix in future evening runs.*
