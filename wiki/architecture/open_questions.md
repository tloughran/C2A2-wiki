# C2A2 Open Architectural Questions
*Maintained by Agent 14 — Architectural History Agent | Initialized: 2026-04-09*

---

OPEN-001:
  Date raised: 2026-04-09
  Question: Should agent-assigned proposal_ids be deprecated entirely, or should we fix them upstream in the hunt agent prompts so they generate unique IDs?
  Context: DECISION-001 (sequential ID fix). The generator now ignores agent-assigned IDs. This means proposal_id in frontmatter is vestigial — used only for agent-internal tracking, with no system-level function.
  Related decisions: DECISION-001
  Status: Open

OPEN-002:
  Date raised: 2026-04-09
  Question: What format should "reference frame location" data take in enhanced dispatches? Free text, wiki-link pointers, or a formal coordinate scheme?
  Context: Redesign proposal Phase 0. The dispatch enhancement proposes adding location data, but the format is unspecified.
  Related decisions: DECISION-003
  Status: Open — depends on Phase 0 implementation

OPEN-003:
  Date raised: 2026-04-09
  Question: How should Agent 14a/14b receive daily session transcripts? Manual paste, scheduled task with transcript tool integration, or some other mechanism?
  Context: DECISION-004 / DECISION-005 (Agent 14 → 14a/14b). The agents need transcript access to function.
  Related decisions: DECISION-004, DECISION-005
  Status: RESOLVED (2026-04-13) — session_info MCP tools (list_sessions, read_transcript) successfully provide transcript access. Used in 14a/14b second run.

OPEN-004:
  Date raised: 2026-04-10
  Question: How should tripled tradition agents be differentiated? By perspective (methodology vs. theory vs. empirical evidence), by temperament (conservative vs. moderate vs. speculative), or by some other scheme?
  Context: DECISION-010 (tripling strategy). If tripled agents are too similar, consensus rate will be 100% and the tripling adds cost without value.
  Related decisions: DECISION-010
  Status: Open — needs resolution before Phase 2a (April 14)

OPEN-005:
  Date raised: 2026-04-10
  Question: What sample size is needed for the health metric r to be statistically meaningful? How many consensus rounds and cross-tradition hypothesis tests are required before r > 1 can be established with confidence?
  Context: DECISION-009 (developmental maturity model). r requires both intra-consensus and cross-survival rates, each needing sufficient N.
  Related decisions: DECISION-009
  Status: Open — needs statistical design before Phase 3 (April 21)

OPEN-006:
  Date raised: 2026-04-10
  Question: Is there a finite typology of cross-paradigm connecting memes (displacement phrasings), or is the space unbounded? What does existing literature say?
  Context: DECISION-011 (PRS displacement vectors). This is a testable hypothesis that should be routed to 15a/15b.
  Related decisions: DECISION-011
  Status: Open — to be tested via 14a → 15a/15b loop

OPEN-007:
  Date raised: 2026-04-10
  Question: What should happen to the original unified Agent 14 definition file? Archive, delete, or annotate as superseded?
  Context: DECISION-005 (14a/14b split). The file wiki/agents/14_architectural_history_agent.md still exists.
  Related decisions: DECISION-005
  Status: Open — low priority

OPEN-008:
  Date raised: 2026-04-10
  Question: What criteria should 15c use to calibrate its disposition heuristics? The current heuristics are starting points. After the first batch of dispositions, should Tom review and adjust the thresholds (e.g., how strong must "strong challenge" be to warrant REVISE)?
  Context: DECISION-012 (Agent 15c). Disposition quality depends on calibrated heuristics.
  Related decisions: DECISION-012
  Status: Open — will become answerable after first 15c cycle

OPEN-009:
  Date raised: 2026-04-10
  Question: What is the right stale-item threshold for 15d? Currently set at 4 weekly cycles before escalation. Should this be adjusted based on the typical pace of literature production in C2A2's fields?
  Context: DECISION-013 (Agent 15d). Too short = premature escalation; too long = items languish.
  Related decisions: DECISION-013
  Status: Open — will become answerable after 15d has run for 4+ weeks

OPEN-010:
  Date raised: 2026-04-10
  Question: Does the review page HTML generator need to be updated to add a CONDITIONAL button (alongside Approve/Deny/Check/Change)? The workflow README now documents CONDITIONAL, but the actual review page may not yet offer it as a UI option.
  Context: DECISION-016 (CONDITIONAL review option). If the review page doesn't have the button, Tom would need to manually write CONDITIONAL in the decision email.
  Related decisions: DECISION-016
  Status: Open — needs check of generate_review_page.py

OPEN-011:
  Date raised: 2026-04-10
  Question: Agent 16 needs web search capability for condition checking (e.g., "has this transcript been published?"). Should 16 use the same search mechanism as 15a/15b, or a lighter-weight check? What are the constraints on web search access from scheduled agent runs?
  Context: DECISION-015 (Agent 16). Condition checking is targeted (specific URL or title), not systematic literature search.
  Related decisions: DECISION-015
  Status: Open — needs resolution before first Agent 16 operational run

OPEN-012:
  Date raised: 2026-04-13
  Question: Should C2A2 implement an alerting mechanism for multi-day pipeline failures? The wiki daily run has failed for 4 consecutive days (auth error) without triggering any alarm. What failure-detection threshold and escalation path would be appropriate?
  Context: Wiki daily run failed 2026-04-10 through 2026-04-13 with 401 authentication error. Morning briefing noted 4-day gap but no escalation mechanism exists. PRS counts frozen; proposals backlogging. See PRESUMPTION-013 and CHANGE-2026-04-13-002.
  Related decisions: DECISION-015 (Agent 16 — could extend to pipeline health monitoring?)
  Status: RESOLVED (2026-04-15) — Alerting implemented via scheduled task monitoring. Wiki auth failure diagnosed and resolved. Agent 16 extended scope to include pipeline health monitoring per DECISION-015.

OPEN-013:
  Date raised: 2026-04-13
  Question: How should the self-awareness pipeline handle self-referential evaluation? When 15a/15b evaluate claims about 15a/15b's own design (ASSUMPTION-003, PRESUMPTION-005), the results may be circular. Should these items be evaluated by an independent mechanism?
  Context: PRESUMPTION-015. The pipeline evaluated claims about itself using itself. This is a known philosophical problem (Gödel, bootstrapping). An independent evaluation mechanism (single neutral agent or human review) could break the circularity.
  Related decisions: DECISION-006
  Status: Open — epistemically significant

OPEN-014:
  Date raised: 2026-04-13
  Question: Should 15c's disposition heuristics be calibrated after the first full cycle? The first run produced 7 REVISE items and 3 INCORPORATE. Are these proportions appropriate or does the threshold need adjustment?
  Context: OPEN-008 (calibration question, raised 2026-04-10) is now answerable with first-cycle data. ASSUMPTION-014 questions whether the framework itself is right.
  Related decisions: DECISION-012
  Status: Open — answerable now (first cycle data available)

OPEN-015:
  Date raised: 2026-04-14
  Question: Should C2A2 build a "paradigm shift detector" tool that tracks interdisciplinary boundary-crossing through bibliometric signals (co-authorships, citation networks, keyword emergence)? If so, should it be assigned to Agent 16, a new specialist agent, or an extension of the pattern detector (Agent 13)?
  Context: Tom proposed this during the morning walk (2026-04-14). He described wanting to see the "bluing" of fields as they merge. PRESUMPTION-019 questions whether bibliometric signals are reliable proxies for genuine intellectual convergence. Design should address the signal-validity question before implementation.
  Related decisions: DECISION-003, DECISION-015
  Status: Open — conceptual (needs design specification before implementation)

OPEN-016:
  Date raised: 2026-04-14
  Question: How should PRESUMPTION-007 (literature absence ≠ novelty) be operationalized as a standing review habit? Tom proposed contextual interpretation of literature absence based on Kuhnian paradigm lifecycle position (ASSUMPTION-019). What would this look like as a protocol change for 15a/15b?
  Context: Morning walk discussion (2026-04-14). Tom connected PRESUMPTION-007 to paradigm shift theory, arguing that absence of literature in a *new* paradigm is expected, not evidence of novelty. This suggests the NOVEL status in the provenance protocol needs contextual qualifiers.
  Related decisions: DECISION-006, DECISION-007
  Status: Open — needs protocol design

OPEN-017:
  Date raised: 2026-04-14
  Question: Can the REVISE review process scale? The REVISE queue grew from 7 to 11 items in one cycle, while Tom reviewed 0 REVISE items. Is there a mechanism to batch, prioritize, or partially automate REVISE triage? See PRESUMPTION-022.
  Context: The self-awareness pipeline generated 4 new REVISE items in the April 13 evening cycle. If this rate continues (2-4 new REVISE items per cycle), and Tom's review capacity is limited, the REVISE queue becomes another bottleneck analogous to the proposal review backlog.
  Related decisions: DECISION-012
  Status: PARTIALLY RESOLVED (2026-04-15) — Tom's batch triage cleared all 16 REVISE items in one session. This addresses the immediate backlog but raises PRESUMPTION-026 (batch triage quality) and ASSUMPTION-027 (adequacy of single-pass review). Whether batch triage is a sustainable solution remains open.

OPEN-018:
  Date raised: 2026-04-15
  Question: Is FINDING-011a (the boundary convergence hypothesis) a genuine structural discovery or a selection artifact of C2A2's own architecture? A system designed to find cross-tradition connections will inevitably find them — how do we distinguish genuine structural unity from designed-in pattern detection?
  Context: PRESUMPTION-024 (CRITICAL risk). Tom articulated the hypothesis that all 11 traditions share the same inside/outside boundary structure. This is the system's most important output. But no adversarial test of the hypothesis was conducted during the session. The emails to Kastrup/Hoffman/Friston and Levin represent the first external test.
  Related decisions: DECISION-017
  Status: Open — CRITICAL (the system's most important epistemic question)

OPEN-019:
  Date raised: 2026-04-15
  Question: How should tripled agents be differentiated in the full rollout? OPEN-004 remains unresolved (differentiation scheme not chosen), but Tom approved full rollout anyway. The Phase 2a design document proposes "configuration 3" (three independent agents per tradition) but does not specify how independence is achieved.
  Context: ASSUMPTION-023 (full rollout approval) proceeded without resolving OPEN-004. The phase2a_multi_agent_plurality.md document describes metrics (intra-thinker consensus >70%) but not differentiation mechanisms (perspective, temperament, focus area).
  Related decisions: DECISION-010, OPEN-004
  Status: Open — blocking (must be resolved before agent definitions are written)

OPEN-020:
  Date raised: 2026-04-16
  Question: What is the operational definition of "benchmarks identified" that gates making the C2A2 wiki repo public? Tom stated publication is "private, for now, with intent to go public after benchmarks are identified" but did not specify what benchmarks, which metrics, or what thresholds.
  Context: ASSUMPTION-030. Without specified benchmarks, the gate is effectively Tom's judgment, which does not transfer to other reviewers and cannot be tracked by the system. The question is whether benchmarks should be: (a) quantitative network metrics (PRS count, connection density), (b) validated findings (some number of INCORPORATE dispositions), (c) external validation (email responses from principals), (d) methodological benchmarks (peer-reviewable protocol documents), or (e) some combination.
  Related decisions: [none yet — would produce a DECISION-019 on publication criteria]
  Status: Open — priority Medium (not blocking day-to-day ops, but blocks any push toward openness)

OPEN-021:
  Date raised: 2026-04-16
  Question: Is the wiki_narration.html refactor to a modular Vite-based architecture (graph.js / tts.js / narration.js / ui.js + data/*.json regenerated from wiki filesystem) the right shape for a visualization layer that must serve both local development and eventual public deployment? ASSUMPTION-029 commits to the refactor but a formal decision entry has not yet been written.
  Context: Debug wiki visualization session 2026-04-16. The assistant proposed a specific directory layout and toolchain (Vite, esbuild as alternative). The shape is reasonable but has not been stress-tested against: (a) Tom's desire to go from single-file-editable-by-LLM to multi-file-harder-for-LLM-to-edit, (b) dependency on `build_data.py` for wiki-scanning, (c) how changes to tradition content propagate to data/*.json, (d) whether Vite's bundling complicates Obsidian co-hosting.
  Related decisions: [proposed DECISION-018]
  Status: Open — design question (needs formalization as DECISION-018 before refactor proceeds)

OPEN-022:
  Date raised: 2026-04-16
  Question: Should there be a cross-task morning-handoff health monitor that aggregates failures across the intent-capture channels (walk-note Gmail, chat scrape, Chrome extension)? PRESUMPTION-032 surfaces that individual-task failure logging exists but there is no escalation when multiple channels fail on the same day.
  Context: On 2026-04-16, both the walk-note capture (Gmail stale since Apr 14) and the chat scrape (Chrome extension not connected) failed. Each task logged its own failure. The morning briefing was still produced from wiki state alone. Over time, a silent drift between Tom's intent and the agents' operating goals becomes possible. Agent 16 or a new Agent 17 could own this.
  Related decisions: DECISION-015
  Status: Open — priority Medium (operational health, not blocking)

OPEN-023:
  Date raised: 2026-04-16
  Question: Is the "daily run" label still accurate for the wiki orchestration task, given that the April 16 run processed an 8-day backlog as a single ingestion event? Should the task be renamed, or should a separate "backlog-catchup" mode be introduced with its own metrics?
  Context: PRESUMPTION-034. The naming convention collapses per-run scope. Metrics snapshots attribute all April 16 deltas to April 16 even though the generative work happened April 8-15. Either the task name should signal the compression, or metrics should be re-allocated to the dates the proposals were generated.
  Related decisions: DECISION-003
  Status: Open — priority Low (cosmetic/interpretability, does not affect correctness)

OPEN-024:
  Date raised: 2026-04-17
  Question: Is the Anthropic billing-propagation delay (blocking narrator regeneration despite $10 visible in the correct credit pool) a one-off incident or a systemic risk for any future LLM-assisted scripts in the C2A2 project? If systemic, what fallback path is appropriate — a secondary credential, a billing-state pre-flight check, or a hard dependency on Anthropic support response times?
  Context: ASSUMPTION-036, PRESUMPTION-038. The C2A2 project has at least three LLM-dependent pipelines (wiki daily run, specialist tradition agents, narrator regeneration). If any of them hit the same vendor-side state issue in the middle of a run, partial-state corruption becomes a risk. Pairs naturally with OPEN-022 (cross-channel drift detection).
  Related decisions: DECISION-015, DECISION-018
  Status: Open — priority Medium (operational resilience; does not block day-to-day if the error resolves on propagation)

OPEN-025:
  Date raised: 2026-04-17
  Question: Does the cowork-resume-session plugin's pattern-based filter (excluding "C2a2", "morning-health", "wiki-agent-daily", "heartbeats", dated prefixes) need an explicit audit before it silently hides an interactive session whose name happens to match the automated pattern? What is the fail-safe if a Tom-named project matches the pattern ("C2a3-something", "Bosco-something", etc.)?
  Context: ASSUMPTION-038, PRESUMPTION-039. The filter was verified structurally but not operationally. The plugin ships with a `limit: 120` escape hatch for named resumes, but there is no monitoring for silent filter-hits on interactive sessions.
  Related decisions: [candidate DECISION-019]
  Status: Open — priority Low-Medium (only relevant if filter ever hits an interactive session; symptomatic, not systemic)

OPEN-026:
  Date raised: 2026-04-17
  Question: Should the cross-session handoff-via-file pattern (~/Documents/Claude/Handoffs/latest.md + SessionStart hook) become a formal architectural primitive for C2A2, with its own reliability contract, versioning, and visibility in the architecture docs? The pattern was introduced ad hoc today; if it becomes a recurring pattern (e.g., any session blocked on an external dependency parks a handoff), formalization avoids the implicit-decision drift surfaced by PRESUMPTION-041.
  Context: ASSUMPTION-035, PRESUMPTION-037. First real stress test is 2026-04-18. Formalization should include: (a) naming convention for handoff files, (b) concurrency behavior when multiple sessions park handoffs simultaneously, (c) retention policy, (d) relationship to DECISION-015 (Agent 16 deferred monitor).
  Related decisions: [candidate DECISION-021]
  Status: Open — priority Medium (depends on how often the pattern recurs)

OPEN-027:
  Date raised: 2026-04-17
  Question: How should the morning autonomous self-awareness run handle days with genuine zero architectural activity vs. days where its extraction pipeline missed real activity? Today's 14a/14b morning run produced zero assumptions/presumptions/decisions/open questions; the afternoon evening sync then generated six assumptions and seven-plus presumption candidates from two interactive sessions the morning run did not yet see. Is a null-coverage audit appropriate, or does this coverage-by-re-run pattern remain adequate?
  Context: PRESUMPTION-042 (today). The morning run is ≤10:14 EDT; afternoon interactive sessions start after that. Either the morning run's architectural extraction is too conservative, or its transcript window is systematically truncated relative to the day's work.
  Related decisions: DECISION-005
  Status: Open — priority Medium (affects reliability of morning-run output as a standalone record)

OPEN-028:
  Date raised: 2026-04-18
  Question: Should parked interactive sessions (blocked on user-preference decisions, as in today's ChatGPT scrape session parked awaiting Tom's route choice) be routed to Agent 16's deferred-watch channel rather than left in implicit indefinite retention? Today's scrape session ended with three route options enumerated and no default-execution or re-prompt contract; the evening summary calls this a "parked" session but there is no mechanism that will re-surface it tomorrow or next week if Tom does not return to it. PRESUMPTION-043 treats indefinite retention as a silent work-loss channel; PRESUMPTION-047 articulates the underlying normative choice (user-directedness over system-initiative).
  Context: PRESUMPTION-043, PRESUMPTION-047, OPEN-024 (Anthropic billing systemic-risk parallel — same shape). The Agent 16 design (DECISION-015) already covers condition-based deferred items; extending it to user-preference-blocked sessions would close the parked-session silent-loss channel without sacrificing user sovereignty (Tom retains the right to direct the session at any time).
  Related decisions: DECISION-015, OPEN-024, OPEN-026
  Status: Open — priority Medium (tractable Agent-16 scope extension; first test case already present in today's scrape session)

OPEN-029:
  Date raised: 2026-04-18
  Question: Is the cross-session handoff-via-file pattern (DECISION-021 candidate) a handoff primitive or a context-loading primitive? Today's Dispatch stress test corroborated the loading half (ASSUMPTION-044) but Tom's pivot to the scrape task discharged the payload without re-queueing it (PRESUMPTION-046). If users habitually pivot on arrival, the execution half may never be observed; the pattern's "reliable handoff" claim becomes operationally unfalsifiable. Either the pattern needs a re-queue-on-pivot contract, or its claim should be weakened to "context-loading on session start."
  Context: DECISION-021 (candidate), ASSUMPTION-035, ASSUMPTION-044, PRESUMPTION-046, OPEN-026 (which this extends). Today's event was the pattern's first real stress test, and it surfaced a contract ambiguity that the original specification ("auto-load if no user direction arrives") did not disambiguate: user-pivot-on-arrival is a legal operation, but the specification does not say what happens to the loaded payload.
  Related decisions: DECISION-021 (candidate), OPEN-026
  Status: Open — priority Medium (resolution needed before DECISION-021 is promoted from candidate)

OPEN-030:
  Date raised: 2026-04-18
  Question: Should the Wolfram (and other tradition) specialist agents perform a transfer-validity check before labeling cross-tradition corridors "new"? Today's PROP-2026-04-18-001 (Wolfram hypergraphing the Sellarsian space of reasons) was framed as opening a "genuinely new Wolfram ↔ analytic-philosophy corridor" without first examining whether Wolfram's hypergraph formalism validly applies to inferential commitment structure (Sellars/Brandom). PRESUMPTION-045 flags this as a HIGH-risk item because it extends the cross-tradition selection-effect cluster (PRESUMPTION-002, 024, 014, 020) to the Wolfram tradition.
  Context: PRESUMPTION-045. Specialist agents are optimized to find connections; the audit question runs counter to their generative momentum. A formal transfer-validity step could be added to the specialist-agent workflow, or it could be delegated to 13 (Pattern Detector) or a new audit agent before a corridor claim is committed to `cross_program_index.md`.
  Related decisions: DECISION-003 (Thousand Brains reference model), DECISION-017 (triangular evidence structure)
  Status: Open — priority Medium-High (directly bears on CRITICAL cluster of selection-effect presumptions)

OPEN-031:
  Date raised: 2026-04-20
  Question: What is the coordination contract between the wiki daily run and specialist scheduled tasks (Levin-Friston-Wolfram tradition agents, narrator, etc.) that share the same wiki working tree? Today exhibited three overlapping risks: (a) a stale `.git/index.lock` from 2026-04-16 blocked the wiki daily run's Phase 6 commit, (b) the `c2a2-agent-levin-friston` task ran 58+ WebSearch turns on the same day without any writes, and (c) the wiki daily run's "11 of 17 findings filtered" step was not audited. No explicit scheduler-level contract specifies ordering, locking, or cost-capping across these tasks.
  Context: PRESUMPTION-049 (scope-partition between tasks), PRESUMPTION-050 (git-lock asymmetric between tasks), PRESUMPTION-051 (pending-count staleness during inter-task gaps), PRESUMPTION-054 (no turn-cap). Candidate primitives: a documented write-lock discipline, a max-turn/wall-clock budget per scheduled task, a pre-flight staleness-probe for `.git/index.lock`, and a filter-audit-log contract.
  Related decisions: DECISION-015, DECISION-003
  Status: Open — priority Medium (operational coordination; becomes High if write collisions produce silent data loss)

OPEN-032:
  Date raised: 2026-04-20
  Question: Should ASSUMPTION-042's transience-threshold structure (git lock age-triggered auto-recovery) be generalized across all OPERATIONAL-DRIFT channels — not just git, but also stale credential states (OPEN-024), stale walk-note Gmail (OPEN-022), stale handoff files (OPEN-028), stale filter rules (OPEN-025)? Each channel currently has its own ad hoc detection pattern; a unified "transience vs. persistence" threshold primitive could subsume them.
  Context: PRESUMPTION-050 (git-lock asymmetry) makes the present-day case salient, but the question generalizes to the whole OPERATIONAL-DRIFT cluster. A generalized pattern would need: (a) a per-channel freshness SLO, (b) a staleness detector, (c) an age-triggered action (recover / escalate / archive), (d) a per-action audit-log contract. This relates to OPEN-012 (alerting) and OPEN-022 (cross-channel handoff monitor).
  Related decisions: DECISION-015, [candidate DECISION-022]
  Status: Open — priority Medium (design-level; needs concrete channels enumerated before specification)

OPEN-033:
  Date raised: 2026-04-20
  Question: Should specialist scheduled tasks (the Levin-Friston-Wolfram tradition agents and similar) have an explicit turn-cap, cost-cap, or wall-clock timeout? Today's `c2a2-agent-levin-friston` task ran 58+ WebSearch turns without writes, consuming compute with no visible progress. No task-definition invariant distinguishes "healthy long run" from "runaway loop" — and no pipeline signal interrupts the latter.
  Context: PRESUMPTION-054 (no turn-cap). A per-task invariant like "≤ N WebSearch turns OR ≤ M write actions OR ≤ T minutes wall clock" would provide a circuit breaker. Candidate mechanisms: scheduler-level timeout (simplest but blunt), in-agent self-budget (more precise but adds complexity), or a watchdog monitor as an extension of Agent 16.
  Related decisions: DECISION-015, OPEN-031
  Status: **PROGRESSING** 2026-04-21 — candidate DECISION-024 drafted (minimal-form: specialist tasks SHOULD declare turn-cap; missing = 20). Chat-side Claude endorsed this form on the 2026-04-21 morning walk (ASSUMPTION-062 "weak circuit breaker beats none"). Two additional supporting data points accumulating at 2026-04-21 EOD: Morning project status and Morning system health both still running with no observable writes, same pattern as Sunday's Levin-Friston case. Priority Medium-High → High if all three overnight terminations match the runaway shape.

OPEN-034:
  Date raised: 2026-04-21
  Question: Should the *absence* of a scheduled self-awareness cycle (14a/14b or 15abc) be a tracked architectural event in its own right, not just narrated in the subsequent day's evening sync? Today, no 14a/14b cycle ran, and the evening-sync's narrative registered the absence but no alert fired. Chat-side Claude's earlier guidance was to ship the narrow "≤ 25h since last self-awareness run" alert as a first cut before the more general OPEN-032 transience-threshold work. Today would have been the first day that narrow alert would have fired. The deeper question: should a missing-run become a first-class event with its own changelog entry / metrics delta / lit-search input, rather than only visible through its cascade effects (no new changelog, no metrics snapshot, etc.)?
  Context: PRESUMPTION-064 (alert absence = visibility — the presumption that narrative-level surfacing is adequate without a firing alert); PRESUMPTION-069 (silence-not-tracked — absence of a cycle is visible through narrative only, not as its own architectural event); ASSUMPTION-058 (evening-sync adequacy claim despite missing cycle); ASSUMPTION-059 (evening-sync scope floor — sync should not manually fire missing cycles). Candidate mechanism: a staleness-clock tied to the self-awareness-pipeline registry that fires when > 25h since last 14a/14b run; the fire action could be (a) a changelog entry auto-written by the staleness monitor, (b) a notification/alert to Tom, (c) an enqueue onto the lit-search queue for the silence-as-signal item.
  Related decisions: candidate DECISION-022 (briefing-layer audit contract — audit of sync-side handling of missing cycles), OPEN-032 (transience-threshold generalization), OPEN-031 (cross-task coordination)
  Status: Open — priority Medium (tractable 20–30 min implementation; first-observable case today; becomes High if second consecutive missed day occurs overnight)

OPEN-035:
  Date raised: 2026-04-21
  Question: Should the wiki daily run's Phase 6 (git commit/push) be restructured to run on the host machine rather than inside the scheduled-task sandbox? Today's Phase 6 attempt revealed a new (compound) failure mode: in addition to the 2026-04-16 `.git/index.lock`, the sandbox mount topology does not include the repo path at all (ASSUMPTION-055). Clearing the lock inside the sandbox is insufficient if the sandbox cannot reach the repo. Candidate restructure: a host-side launchd job on Tom's Mac watches the wiki folder and commits changes when the sandbox's Phase 5 writes land; the sandbox-side task ends at Phase 5 and emits a "ready for commit" marker; the host-side watcher picks up the marker and runs the commit.
  Context: ASSUMPTION-055 (Phase 6 sandbox-unreachable); PRESUMPTION-061 (sandbox mount topology presumed stable); DECISION-018 (rescue commit plan — predicated on the single lock-file failure mode, now outdated by the compound mode); candidate DECISION-023 (caching/execution protocol — its pre-flight gate inherits this compound block; see DECISION-023 2026-04-21 update). The restructuring is architecturally upstream of the lock-fix: the one-time manual lock clear becomes a side operation rather than the centerpiece of a sandbox-side rescue.
  Related decisions: DECISION-018, candidate DECISION-023, OPEN-031 (cross-task coordination — a host-side watcher is a coordination primitive)
  Status: Open — priority High (blocks two parallel tracks: the wiki daily-run's ingestion-of-proposals pipeline and the caching-architecture 2026-04-27 rollout)

OPEN-036:
  Date raised: 2026-04-26
  Question: Should N.T. Wright (scripture-scholarship ground truth) and Richard Rohr (spirituality ground truth) be added to the C2A2 wiki itself as new tradition entries, or should they remain in the derivative-project bridges file (`/Users/tomloughran/Documents/Claude/Projects/Summa 2026 in a Year/vault/refs/Karpathy wiki bridges.md`) where they originated today? Tom's stated intent ("I'll add NT Wright as scripture scholar ground truth, and Richard Rohr (The Universal Christ) as spirituality ground truth") was made in a derivative-project conversation; the addition has not yet propagated to the C2A2 wiki under `Wiki/traditions/`. Candidate paths: (a) formally add Wright and Rohr to the C2A2 wiki, with the same PRS-triplet curation discipline as the existing 11; (b) leave them in the derivative-project bridges file and treat them as downstream-consumer conventions, not C2A2 traditions; (c) admit them as a new "ground-truth tradition" sub-class with a distinct operational primitive.
  Context: ASSUMPTION-064 (Wright + Rohr proposed as new traditions); PRESUMPTION-073 (scaling N=11→13); PRESUMPTION-076 (canonical-works fallback ≠ native wiki entry); PRESUMPTION-080 (cross-discipline operational-primitive presumption); candidate DECISION-025. Resolution depends on a depth-of-curation decision and on whether the C2A2 wiki accepts shadow-architecture changes from derivative projects.
  Related decisions: candidate DECISION-025, ASSUMPTION-005 (traditions as units), ASSUMPTION-064
  Status: Open — priority Medium-High (blocks DECISION-025; affects N≥30 future cross-tradition syntheses if wiki adopts the addition)

OPEN-037:
  Date raised: 2026-04-26
  Question: How should "Stump's metaphysical demotion" (per ASSUMPTION-063, today's user message) be reconciled with (a) her keystone status on virtue, suffering, faith-as-knowledge, and the atonement, and (b) the same-day Stump+Fredrickson specialist reading (ASSUMPTION-067) that explicitly treats Stump as supplying live metaphysics? Today produced two simultaneous and conflicting readings of Stump's metaphysical role within C2A2 — one in a derivative-project design conversation, one in a specialist-agent autonomous-choices note. The C2A2 wiki itself has not yet committed to either reading. Candidate resolution paths: (a) canonize the demotion in the wiki and update the Stump+Fredrickson reading on the next specialist run; (b) reject the demotion and keep Stump's metaphysics live; (c) admit a partial-demotion (metaphysical primaries = Levin/Hoffman/Kastrup; Stump's hylomorphism remains available as secondary metaphysical voice when paired with empirics).
  Context: ASSUMPTION-063, ASSUMPTION-067, PRESUMPTION-070 (decomposability of Stump's frameworks), PRESUMPTION-071 (Levin+Hoffman+Kastrup convergence), PRESUMPTION-078 (Stump+Fredrickson commensurability), candidate DECISION-025. This is the first observed case of same-day intra-system architectural tension on a tradition's role.
  Related decisions: candidate DECISION-025, OPEN-036, ASSUMPTION-005, PREMISE-006 (flag-don't-reconcile — applies recursively here: today's tension should be flagged not silently reconciled)
  Status: Open — priority High (active intra-system tension; affects every downstream synthesis that invokes Stump on metaphysics)

OPEN-038:
  Date raised: 2026-04-26
  Question: Why has the C2A2 master-wiki narrative had no entries for 04-23 through 04-26 (a 4-day gap, surfaced this morning by the Morning walk handoff)? Is this a pipeline-degradation signal that the briefing layer is hiding by design via PREMISE-006 / ASSUMPTION-068 (flag-don't-reconcile / surface-don't-fabricate)? Today's wiki daily run added a 2026-04-27 entry, partially closing the gap, but did not address the prior 4-day silence. The same gap mirrors the 4-day self-awareness gap (2026-04-22 through 2026-04-25) that is the reason this run is closing 04-26 only. Two questions are nested: (a) what concretely caused the 4-day master-narrative gap; (b) at what N-day threshold should a master-narrative gap escalate from "surface-and-proceed" (PREMISE-006) to "investigate-as-incident"?
  Context: ASSUMPTION-068 (master-narrative-gap surfacing > fabrication); PRESUMPTION-077 (4-day gap is operationally absorbable — likely false at high N); PREMISE-006 (silent on staleness-threshold); OPEN-034 (silence-as-signal cluster — adds member); PRESUMPTION-064 (alert absence = visibility); ASSUMPTION-047. The four-day self-awareness gap (concurrent) suggests the cause may be infrastructure-level (e.g., the scheduled-task system not firing) rather than C2A2-internal.
  Related decisions: PREMISE-006 (may need a staleness-floor amendment), OPEN-034, OPEN-035, candidate DECISION-022 (briefing-layer audit contract)
  Status: Open — priority High (4-day gap is the largest yet observed; if cause is infrastructure-level, fixing the cause is upstream of all C2A2 self-awareness)

OPEN-039:
  Date raised: 2026-04-26
  Question: Is the Chrome MCP workaround for the Cowork sandbox-egress allowlist sustainable as a production path, or should the egress allowlist be escalated to the Claude product team as a known-bad pattern? Today's design conversation diagnosed the egress as system-level / hard-coded ("Cowork agent containers ship with a fixed allowlist that survives session restarts"), then routed to Chrome MCP for the production batch path without filing an escalation. The Chrome path has visible fragility (ad-blocker interactions stripping timedtext fetches today). PRESUMPTION-075 captures the workaround-as-permanent stance. The deeper question is whether C2A2's caching-architecture rollout (candidate DECISION-023, scheduled for 2026-04-27) and the wiki daily run's Phase 6 (OPEN-035) — both blocked by sandbox infrastructure constraints — should be combined into a single "sandbox infrastructure escalation" track.
  Context: PRESUMPTION-075, ASSUMPTION-055 (Phase 6 sandbox-unreachable repo), ASSUMPTION-070 (308-episode count, dependent on Chrome path), candidate DECISION-023 (caching/execution protocol), candidate DECISION-025. The pattern is now multi-failure: today is the third confirmed sandbox-infrastructure constraint (egress, mount-topology, .git/index.lock). The case for escalation is accumulating.
  Related decisions: candidate DECISION-023, OPEN-035, ASSUMPTION-055, ASSUMPTION-075 (NEW)
  Status: Open — priority Medium-High (independently low-risk; combined with OPEN-035 escalation may be High)

OPEN-040 (candidate — pathway 00 streaming-latency conditional):
  Date opened: 2026-05-13
  Question: What is the first-token streaming latency through a Cloudflare Workers broker stub for a 1-token Claude streaming call, measured (a) from a coffee-shop wifi connection and (b) from the Notre Dame campus network? Is the latency under ~200 ms across both conditions? If not, what is the latency profile of the AWS Lambda + ALB fallback?
  Why it matters: DECISION-026 (broker hosting on Cloudflare Workers) is conditional on this measurement. PRESUMPTION-152 flags the ~10-30 ms broker-side edge overhead estimate as unverified pre-decision; the validation test is the deciding artifact for whether the broker hosting decision unconditionalizes.
  Related items: DECISION-026 (candidate), ASSUMPTION-120, PRESUMPTION-152, Pathway 00 (Broker)
  Status: Open
  Estimated effort: 30 minutes (test execution) + 10 minutes (write-up)
  Target resolution: Before next significant Pathway 00 build step (broker stub deployment)

OPEN-041 (candidate — recursive self-application termination condition):
  Date opened: 2026-05-13
  Question: The 2026-05-13 dream-conversation framing "the traditions of intellectual inquiry the project exists to accelerate include the tradition of its own becoming" introduces a recursive self-application: C2A2 is a tradition accelerated by C2A2. What is the termination condition or stable fixed point of this recursion? If the system becomes better at accelerating itself than at accelerating its external traditions (Levin, Friston, Hoffman, Kastrup, ...), is that success or pathology?
  Why it matters: PRESUMPTION-165 flags this as joining the SELF-MEASUREMENT Goodhart cluster at the meta-tradition layer. The "tradition of its own becoming" frame is now the operating frame for the next eight weeks (through ISME). If the frame lacks a termination condition, downstream prioritization can drift toward self-acceleration over external acceleration — the worst-case Goodhart outcome at the meta-tradition layer.
  Related items: ASSUMPTION-119, ASSUMPTION-112 (SELF-MEASUREMENT Goodhart confirmation), PRESUMPTION-123, PRESUMPTION-148, PRESUMPTION-165, FINDING-025 (SUTI = C2A2 detection function in microcosm)
  Status: Open
  Estimated effort: 1-2 hours for philosophical-architectural decomposition; 1 week for proxy-metric design
  Target resolution: Before ISME 2026 demo (July 8-10) — at minimum, the operating-frame should have an articulated termination condition or known-pathology mitigation by then

OPEN-042 (candidate — AI-personhood-under-CRM bright-pin engagement plan and operational-gravity audit):
  Date opened: 2026-05-13
  Question: The "AI personhood under conscious-realist-monism" bright pin is held with deliberate brightness pending direct philosophical engagement. PRESUMPTION-164 flags that the held position already shapes Pathway 14 (honesty layer) and Pathway 17 (agent as developed participant) framing — i.e., the pin has operational gravity even though formally undecided. (a) What is the engagement plan for the pin (when will it be directly engaged philosophically, and by whom)? (b) Which downstream architectural choices currently rest on the held-but-undecided commitment, and which of those would need re-architecting if the personhood claim were rejected?
  Why it matters: HIGH-risk new item this run per PRESUMPTION-164. Multiple downstream pathway dependencies on a held but undecided commitment is a brittle foundation; the engagement plan and operational-gravity audit together convert the brittleness into either a stable commitment or a managed dependency.
  Related items: ASSUMPTION-130 (honesty layer), Pathway 14, Pathway 17, PRESUMPTION-164, Two Bright Pins (pathways.md)
  Status: Open
  Estimated effort: 30-60 minutes for operational-gravity audit (which pathway-doc decisions rest on the pin); engagement plan timeline TBD by Tom
  Target resolution: Operational-gravity audit within next 14 days; engagement plan timeline before ISME 2026 demo

OPEN-043 (candidate — pathway-doc Cowork-draft vs walk-content audit):
  Date opened: 2026-05-14
  Question: Of the 8 pathway docs Cowork drafted today (18 Portability through 25 Meta-visualization), each containing ~5-piece function sets, architecture sketches, 5+ "Decisions taken," and 5+ open questions, how much of the content (line-by-line) is grounded in the morning walk transcript vs. extrapolated by Cowork from the project's prior architectural context? The walk transcript contains 2-3 sentence sketches per pathway in Summary 1 plus a 1-2 sentence framing in Summary 2. The pathway docs are ~100 lines each. What is the Cowork-attribution rate per pathway, and how many of the drafted "Decisions" survive Tom's amendment pass unchanged?
  Why it matters: PRESUMPTION-175 flags this gap — substantive Cowork-authored architectural commitments enter the registry at near-canonical weight via pathway-doc-Decisions sections, with only metadata-level acknowledgment of the authorship gap. If Tom's amendment pass diverges substantially, the apparent agreement is artifactual.
  Related items: PRESUMPTION-175, PRESUMPTION-176 (Chat-Claude "review" file labeling), PRESUMPTION-166 (parallel pattern at 17-pathway batch), ASSUMPTION-131..139 (today's pathway-doc-derived assumptions)
  Status: Open
  Estimated effort: 2-3 hours for line-by-line audit per pathway × 8 pathways = ~20 hours total; or sampled audit on 2-3 pathways for proportional estimate ≈ 5-8 hours
  Target resolution: Before any of today's pathway-doc decisions get promoted to canonical DECISION-NNN status

OPEN-044 (candidate — federation wire-format transfer-validity audit for ASSUMPTION-133):
  Date opened: 2026-05-14
  Question: ASSUMPTION-133 commits to file-based handoff (signed JSON over HTTPS) as the primary wire format for inter-instance federation, citing PRESUMPTION-145 as precedent. PRESUMPTION-145 originated from the laptop-to-Chat handoff (intra-user / single-machine-tree) context. PRESUMPTION-170 flags the transfer-validity question: what are the conditions under which file-based-handoff design choices from the intra-user context generalize to inter-organizational federation (different hosts, security domains, key management, update cadences)? Is the file-based commitment robust at federation scale, or does it need to be re-evaluated against persistent-API alternatives in the inter-instance context?
  Why it matters: PRESUMPTION-170 (joins PRESUMPTION-002 CRITICAL transfer-validity cluster). If the file-based commitment has failure modes at federation scale (replay attacks, signature key management, file-staleness, peer-discovery latency) that don't appear in the single-user context, ASSUMPTION-133 is fragile. The audit converts a citation-based architectural commitment into either a validated transfer or a context-dependent commitment.
  Related items: ASSUMPTION-133, PRESUMPTION-170, PRESUMPTION-145, PRESUMPTION-002 (CRITICAL transfer-validity cluster), Pathway 19 (Optional interoperability), Pathway 00 (Broker)
  Status: Open
  Estimated effort: 4-6 hours for federation wire-format threat-model audit; 8-12 hours for prototype testing against a peer instance with different security domain
  Target resolution: Before any Pathway 19 federation prototype work begins; ideally before next DECISION-019 (federation wire-format) canonization

OPEN-045 (candidate — Carpathi-instance-specific human-validator portability):
  Date opened: 2026-05-14
  Question: Across all 8 pathway docs (18-25), the "Cowork-drafted; sequencing subject to Tom's amendment" pattern presumes Tom as the canonical validator. PRESUMPTION-182 flags this as Carpathi-instance-specific — a governance role naturalized by default in the Carpathi instance. As the framework scales toward federation (Pathway 19), institutional deployment (Pathway 20), and individual second brains (Pathway 22), what protocol replaces "Tom's amendment" for non-Carpathi instances? Is the single-human-validator role inherent to the framework, or replaceable with community-vote, BDFL-style governance, or some other ratification protocol?
  Why it matters: Without an explicit protocol, adopter instances either drift toward Carpathi-style single-validator governance (which may not fit their context) or stall on framework-decision questions. This is a Pathway 18/19/24 portability question; Pathway 24's meta-craft-governance content is the natural home for the answer.
  Related items: PRESUMPTION-182, PRESUMPTION-166 (parallel pathway-doc commitment without canonization), Pathway 18 (Toolkit), Pathway 19 (Federation), Pathway 24 (Meta-crafts governance), ASSUMPTION-131..139 (today's pathway-doc decisions)
  Status: Open
  Estimated effort: 2-3 hours to draft a governance-role-portability section for Pathway 24; longer if community-input is sought
  Target resolution: Before toolkit release (Pathway 18 instantiation guide); ideally addressed in Pathway 24's drafting pass before the framework is released for external adoption



OPEN-046 (candidate — does c2a2-15d-monitor exist as a scheduled task at all):
  Date opened: 2026-05-17
  Question: The 57-item RE-TRIGGER cohort from 2026-05-05 (`next_check: 2026-05-12`) is now 4 days overdue, carry-forward through 7+ consecutive daily 15a/15b/15c runs without drain. The cowork summary recommends "verify the 15d cadence" framing — but the lit-search note from the same day says "No `c2a2-15d-monitor` scheduled-task evidence is visible in this session's accessible scope." (a) Does `c2a2-15d-monitor` (or any equivalent task) exist as a scheduled task? (b) If yes, what is its cadence and last-fire timestamp? (c) If no, was 15d-cohort ownership ever explicitly designed, or is the daily/15d split an aspirational architecture that was never built out? (d) If unbuilt, what is the migration path: build 15d, expand daily 15c to own RE-TRIGGER drain, or re-design the cohort-lifecycle protocol?
  Why it matters: PRESUMPTION-188 flags this as 15d-as-fixable-cadence-vs-unbuilt-component — the same pattern as the substrate-decomposition cluster (PRESUMPTION-134/159/177): pre-classifying a failure as the less-expensive cause before the diagnosis is in. If 15d was never built, no "5-minute cadence check" can resolve the cohort; the fix is structural, not operational.
  Related items: ASSUMPTION-167, PRESUMPTION-188, PRESUMPTION-134, PRESUMPTION-159, PRESUMPTION-177, ASSUMPTION-166 (lit-search null-run discipline)
  Status: Open
  Estimated effort: 5 minutes to query the scheduler directly for any 15d-named task; 30-60 minutes to design the migration path if 15d is unbuilt; longer if a build is needed
  Target resolution: Within the next 7 days — the cohort grows older every cycle without ownership clarity

OPEN-047 (candidate — daily 14a/14b cadence vs Chat-side architectural production rate-mismatch):
  Date opened: 2026-05-17
  Question: The c2a2-self-awareness-daily (14a/14b) scheduled task missed 2026-05-15 EOD and 2026-05-16 EOD before resuming on 2026-05-17 (this run). The cowork summary's framing is "verify the scheduler fired and run a heavier-than-usual catch-up." PRESUMPTION-187 raises an alternative reading: the Chat-side architectural production rate (8 new pathway docs on 2026-05-14; today's multi-agent infrastructure) may structurally exceed what a daily Cowork ingestion window can sustain. (a) Was the missed-cycle cause scheduler-state / credential / environment, or was it structural rate-mismatch (e.g., token-budget exhaustion mid-run, scope-too-large for daily cadence)? (b) If structural, what is the ingestion-contract redesign — batch processing? deferred ingest? Cowork-side throttle on Chat-derived work? smaller per-day chunks with multi-day catch-up? (c) What is the relationship to ASSUMPTION-169 (pace-and-shape question on fourth-consecutive evening surfacing) — is the missed-cycle a symptom of the breadth-arc / demo-path tension or a separate event?
  Why it matters: PRESUMPTION-187 maps this to the substrate-decomposition cluster's failure-mode-classification pattern: pre-classifying as the cheaper cause before the diagnosis is in. If Tom diagnoses "scheduler problem" and fixes the schedule, an underlying rate-mismatch (if real) re-surfaces as recurrent missed cycles or shallow ingestions. The honest classification matters for Pathway 14.
  Related items: ASSUMPTION-165, ASSUMPTION-169, PRESUMPTION-187, PRESUMPTION-186 (pace-and-shape zero-sum), Pathway 14 (honesty layer / accurate failure-mode classification)
  Status: Open
  Estimated effort: 30-60 minutes to inspect scheduler logs + tonight's catch-up run output; 1-2 hours to design alternative ingestion contracts if rate-mismatch is supported
  Target resolution: Within the next 7 days — if missed cycles recur, the structural-rate-mismatch reading strengthens regardless

OPEN-048 (candidate — DeepSeek-as-LLM-provider under Pathway 19 federation / peer-trust governance):
  Date opened: 2026-05-17
  Question: The Path-2 sandboxed-worker architecture (DECISION-036 candidate) imports DeepSeek-Flash on cost and capability grounds, without examining the federation / peer-trust / data-flow concerns enumerated for Pathway 19 (PRESUMPTION-189). (a) What vault content (excerpts, prompts, metadata) gets sent to DeepSeek's API in the course of normal worker operation? (b) Does any of that content overlap with content Pathway 19 federation would mark as not-for-default-sharing? (c) Does DeepSeek's model-provenance (jurisdiction, training data, governance) raise concerns under the same framework that motivates Pathway 19's federation-default-off + signed-JSON wire format commitments? (d) If yes, what is the protocol for LLM-provider trust attestations that parallels the inter-instance trust attestation work?
  Why it matters: The toolkit-extraction path (Pathway 18) and the federation path (Pathway 19) both inherit any provider-trust questions unresolved at infrastructure layer. If the data-flow surface to DeepSeek raises governance concerns under Pathway 19's own framings, the architectural infrastructure quietly built today re-opens questions Pathway 19 was set up to close.
  Related items: ASSUMPTION-158, PRESUMPTION-189, Pathway 19 (Optional interoperability), Pathway 18 (Toolkit), PRESUMPTION-170 (federation wire-format transfer-validity), DECISION-033 (federation default-off)
  Status: Open
  Estimated effort: 2-3 hours for a data-flow audit + governance-protocol-parallel analysis; longer if a formal provider-trust attestation protocol needs drafting
  Target resolution: Before any non-Claude LLM provider is used on substantive vault content (i.e., promotion of any worker output to live vault); before Pathway 18 toolkit extraction


OPEN-049 (candidate — orchestrator-vs-specialist state-visibility contradiction):
  Date opened: 2026-05-18
  Question: Today's three-way contradiction across the C2A2 wiki orchestrator (local_2a76d5fd: "Monday Levin+Friston specialist slot did NOT produce proposals today"), the morning walk handoff (local_b1594599: echoes the same framing), and the Levin/Friston specialist itself (local_630c5f21: reports 3 proposals written to `pending/`). (a) At the time the orchestrator's Phase-2 pending/-scan ran, were the specialist's 3 proposals physically present under `pending/`, or were they at a different path (e.g., a tradition-specific subdirectory)? (b) If physically present, why did the orchestrator's scan miss them — tag-filter, path-scope, ordering race? (c) If at a different path, when did the convention of specialist-writes-to-pending/ get re-routed and was that change visible to the orchestrator? (d) What is the correct fix: orchestrator scan re-coverage, specialist write-receipt manifest, run-ordering guarantee, or all three?
  Why it matters: PRESUMPTION-196 flags this as a pending-scan-as-output-ground-truth presumption. If scan-vs-output discrepancy is steady-state, the orchestrator systematically miscategorizes specialist outputs as missing, the morning briefing relays the miscategorization, and Tom's morning intervention space (the "worth checking cron" line) is misdirected from the real problem (state-visibility) to a phantom problem (scheduler). This is a Pathway-14 honesty-layer instance — the briefing is honest about what it sees, but what it sees is wrong.
  Related items: ASSUMPTION-178, PRESUMPTION-196, PRESUMPTION-187 (pipeline-failure-vs-rate-mismatch), Pathway 14 (honesty layer)
  Status: Open
  Estimated effort: 5-15 minutes to physically check `pending/` after a Monday specialist run and compare against the orchestrator's scan output; 30-60 minutes to design a write-receipt manifest protocol if scan-divergence is confirmed
  Target resolution: Before next Monday (2026-05-25) — when the Levin/Friston Monday slot fires again, the same discrepancy is likely to recur and Tom's morning briefing should not relay it a second time

OPEN-050 (candidate — uncommittable-state-extended-interval protocol):
  Date opened: 2026-05-18
  Question: The C2A2 wiki has accumulated 476 uncommitted changes since the .git/index.lock orphaned on 2026-05-17 17:26. CLAUDE.md constitutionally forbids blind push; the lock cannot be cleared from inside the sandbox. (a) What is the protocol for orchestrator and other daily-pipeline writes during an extended uncommittable interval? Continue writing (current behavior, risks accumulation-corruption per PRESUMPTION-199) or pause writes pending Tom's manual lock-clear-plus-review? (b) Is 476 changes a one-off or a steady-state pattern of long lock-clear intervals? (c) Should daily pipelines that produce 0 new content (today's orchestrator wrote 0 new proposals) skip the commit-step entirely, reducing the always-accumulating churn? (d) What does Pathway 14's honesty-layer commit-discipline parameter look like — is it "commit when committable" or "checkpoint-discipline equal to write-discipline"?
  Why it matters: PRESUMPTION-199 flags this as uncommitted-state-is-safe-indefinitely, with a Critical risk rating: 476-day-accumulation is precisely the state in which sandbox-restart or partial-write leaves the vault inconsistent without git as a recovery anchor. The constitutional rule preserves visual-review correctly but is silent on checkpoint discipline during extended pauses.
  Related items: ASSUMPTION-174, PRESUMPTION-199, CLAUDE.md constitutional rule, Pathway 14 (honesty layer)
  Status: Open
  Estimated effort: 15-30 minutes for Tom to manually clear the .git/index.lock and walk through visual review of the 476 changes; 1-2 hours to design a check-pointing protocol that handles extended uncommittable intervals more gracefully
  Target resolution: Within the next 3 days — the lock is preventing the daily commit-discipline that all downstream agents (15a/15b/15c, 15d, 16, sewing-agent) depend on for ground-truth state

OPEN-051 (candidate — cross-specialist confirmation for bridge claims):
  Date opened: 2026-05-18
  Question: PROP-003 (Levin Clofilium + Friston Cambridge) asserts bridges to Hoffman/Hawkins/Wolfram/Kastrup/Carroll as a sole-source claim by the Levin/Friston specialist. The Pattern Detector (Pathway 13) will inherit these bridges as structural-homology signal. (a) Does the system have, or should it have, a cross-specialist confirmation step where the receiving-tradition specialist confirms or denies receptivity to the bridge? (b) What is the false-positive cost of sole-source bridges — do they inflate cross-tradition signal counts and bias the Pattern Detector toward over-bridging? (c) What is the run-cost trade-off — confirmation multiplies runs by N (number of bridged traditions) but improves signal quality. Is the trade-off bounded by selecting only "paradigm-shift candidate" bridges for confirmation, leaving "surface analogies" and "structural homologies" as sole-source? (d) What is the relationship to PROP-003's "explicit cross-tradition signal" tag — is that tag itself the sole-source asserter, or does it incorporate a confirmation step?
  Why it matters: PRESUMPTION-198 flags this as specialist-as-bridge-detector. The current sole-source pattern saves runs but may overcount bridges; downstream pipelines (Pattern Detector, cross-tradition-stage gating) operate on inflated bridge counts. If false-positive rate is high, the Pattern Detector's structural-homology output becomes noise-dominated.
  Related items: ASSUMPTION-172, PRESUMPTION-198, Pathway 13 (Pattern Detector), CROSS-016/021/024 cluster
  Status: Open
  Estimated effort: 2-4 hours to design a cross-specialist confirmation protocol and a paradigm-shift-candidate-only routing rule; longer if a formal bridge-quality metric needs to be defined
  Target resolution: Before the Pattern Detector (Pathway 13) is instantiated for Phase-3 cross-tradition processing — the choice of sole-source vs cross-specialist shapes the Pattern Detector's input distribution


OPEN-052 (candidate — Levin-zero / Friston-one count discrepancy on Monday 2026-05-18):
  Date opened: 2026-05-18
  Question: A second-order count discrepancy compounds OPEN-049. The sewing-agent's EOD pending/-scan (local_57fed042) sees 7 proposals (3 Rohr / 3 Wright / 1 Friston — therefore 0 Levin), while the Levin/Friston specialist's own run report (local_630c5f21) claims "Levin Agent: 2 proposals written / Friston Agent: 1 proposals written / Total: 3." The Friston count agrees across both views (=1); the discrepancy is isolated to the 2 claimed Levin proposals. (a) Where are the 2 Levin proposals — a tradition-subdir (e.g., `inbox/proposals/pending/levin/`), a tag-filter the sewing-agent also misses, or never-actually-written? (b) Is the specialist's "Levin: 2" count a claim that did not result in actual writes (run-report-overcount), or are the writes at a path neither scanning agent currently covers? (c) What is the minimum write-receipt protocol that would let both the orchestrator and the sewing-agent reconcile their counts against a manifest emitted by the specialist itself?
  Why it matters: OPEN-049 partial resolution (ASSUMPTION-179) confirmed proposals exist at `pending/` and shifted the diagnosis from "specialist write-failure" to "orchestrator scan-coverage failure." The new sub-question rebalances that: at least 2 of the specialist's claimed writes are not visible to the sewing-agent's deeper scan either. Without resolving OPEN-052, the OPEN-049 fix (orchestrator scan re-coverage) does not address the residual disagreement, and the inter-agent state-visibility problem remains larger than today's morning diagnosis named.
  Related items: ASSUMPTION-178, ASSUMPTION-179, ASSUMPTION-180, PRESUMPTION-196, PRESUMPTION-204, OPEN-049, Pathway 14 (honesty layer)
  Status: Open
  Estimated effort: 5-15 minutes for direct shell audit (`ls -la inbox/proposals/pending/` filtered by 2026-05-18 mtime + Levin tag, plus a recursive search for Levin-tagged files anywhere under `inbox/proposals/`); 30-60 minutes to design a specialist-emits-write-receipt manifest protocol if the Levin proposals are confirmed missing-from-pending/
  Target resolution: Before next Monday (2026-05-25) — when the Levin/Friston Monday slot fires again, the count discrepancy is likely to recur unless resolved alongside OPEN-049

OPEN-053 (candidate — sewing-agent vs Pattern-Detector bridge-ratification scope):
  Date opened: 2026-05-18
  Question: The sewing-agent (local_57fed042) wrote three substantive cross-tradition bridge notes to `synthesis/` on 2026-05-18 (ASSUMPTION-182) without Pattern-Detector (Pathway 13) confirmation — the same sole-source architectural pattern OPEN-051 raised for the Levin/Friston specialist's PROP-003 bridges, now extended to a second agent class (PRESUMPTION-207). (a) Should bridge ratification be split by agent: sewing-agent ratifies connectivity-bridges (within-vault structural links), Pattern Detector ratifies cross-tradition-bridges (structural-homology + paradigm-shift claims)? (b) Should the Pattern Detector ratify all bridges regardless of source, with the sewing-agent's role downgraded to candidate-bridge-discovery? (c) Should both routes coexist, but with explicit weighting (e.g., sewing-agent bridges enter synthesis/ as "candidate" until Pattern-Detector pass; Pattern-Detector confirms or rejects)? (d) How does the resolution of OPEN-053 interact with OPEN-051 — are they instances of the same architectural question (cross-specialist-confirmation), or do they have different cost-benefit profiles that warrant different routing rules?
  Why it matters: The sewing-agent's three bridges (Friston×Levin precision-weighting "strongest empirical bridge in today's batch", McGilchrist×Rohr hemispheric-operationalization, Wright×Rohr *ruach*×Universal-Christ) are substantive enough that they will be read as cross-tradition signal by every downstream pipeline (Pattern Detector, cross-tradition-stage gating, the master agent's morning briefing). If they enter synthesis/ as de-facto ratified, the Pattern Detector inherits a pre-ratified bridge corpus instead of computing one independently, creating a circular-signal risk (PRESUMPTION-207 Medium-High).
  Related items: ASSUMPTION-172, ASSUMPTION-182, PRESUMPTION-198, PRESUMPTION-207, OPEN-051, Pathway 13 (Pattern Detector)
  Status: Open
  Estimated effort: 2-4 hours to design a bridge-ratification protocol that separates connectivity-discovery from pattern-detection-confirmation (likely combined with OPEN-051 in a single design pass); longer if a formal bridge-quality metric needs to be defined that distinguishes connectivity-bridges from cross-tradition-bridges
  Target resolution: Before the Pattern Detector (Pathway 13) is instantiated for Phase-3 cross-tradition processing — same gate as OPEN-051; the two open questions should be resolved together


OPEN-054 (candidate — demo-path vs pathway-expansion: the "both" default):
  Date opened: 2026-05-19
  Question: For the next two weeks, where does Tom's scarce attention go — the demo path (ISME-critical, ship-by-July-8 surfaces) or pathway-expansion (new architecture docs like Pathway 27)? The morning chat-scrape surfaced this as overdue: "Tom owes the walk a real answer on demo-path vs. pathway-expansion for the next two weeks — 'both' has been the default and isn't working." (a) Are the two genuinely competing for the same resource, or are they sequenceable/composable (e.g., Search + hyperlinking from Pathway 27 are themselves ISME-critical and ship pre-July-8)? (b) What is the minimal demo-path critical path (per evening cowork: per-tradition syntheses 0/12 starting Hawkins×Friston; README ~30 min; FC26 Rev2 submission-ready)? (c) What expansion work is cheap enough to interleave without displacing the demo path?
  Why it matters: A standing "both" allocation with no explicit priority is producing drift on both axes; the chat-scrape names it as the strategic decision blocking focused execution. See PRESUMPTION-220 for the unexamined either/or framing.
  Related items: ASSUMPTION-197 (Pathway 27 ISME staging), ASSUMPTION-183 (FC26 horizon), PRESUMPTION-220, Pathway 27, ISME critical path
  Status: Open
  Estimated effort: 15-30 minutes for Tom to set an explicit two-week priority; this is a judgment call, not an analysis task
  Target resolution: This week — it gates how every subsequent session allocates effort

OPEN-055 (candidate — queue-count reconciliation / write-receipt manifest, generalized):
  Date opened: 2026-05-19
  Question: Today produced four different pictures of the same pending queue: the orchestrator and morning-walk briefing both report 51 pending (and the orchestrator throttled Phase-2 hunts on it); the cleanup scan reports 36 stale duplicates → 15 genuine; the chat-scrape calls it possible "reflection lag." This is the same scan-as-ground-truth pattern OPEN-049/052 raised for proposal counts, now hitting the review-queue count and driving an actual generation-throttling decision. (a) Should the system adopt a single write-receipt / manifest layer that every counting agent reconciles against, rather than each agent trusting its own directory scan? (b) Should the conservation-principle Phase-2 gate validate the pending count against the known duplicate bug before acting on it? (c) How does this unify with OPEN-049/052's proposal-count reconciliation — is it one manifest protocol or two?
  Why it matters: An agent (the orchestrator) made a real operational decision (suspend hunts) on a count corrupted by a known-but-unfixed duplicate bug. Until counts are reconciled against a manifest, every count-driven gate inherits the corruption. This is the structural fix behind lit-pipeline SYSTEMIC-RISK-FLAG A (inter-agent ground-truth oscillation) and B (closed-loop ratification).
  Related items: ASSUMPTION-186, ASSUMPTION-187, PRESUMPTION-209, PRESUMPTION-210, OPEN-049, OPEN-052, lit-pipeline SYSTEMIC-RISK-FLAG A/B
  Status: Open
  Estimated effort: 30-60 minutes to specify a write-receipt manifest protocol shared across orchestrator / sewing-agent / cleanup / chat-scrape; longer to retrofit each agent's count step to reconcile against it
  Target resolution: Before next Monday (2026-05-25) — the count-driven conservation gate fires again on the next orchestrator run (2026-05-20)

OPEN-056 (candidate — commit ownership: who clears the pile and commits architecture/ changes):
  Date opened: 2026-05-19
  Question: OPEN-050 asked for an uncommittable-state protocol; today sharpens it from "lock protocol" to "ownership + collision." The sandbox cannot write `.git` (ASSUMPTION-188); scheduled commit agents appear to collide / silently fail (ASSUMPTION-189); only Tom's host shell commits succeed; and the architecture/ set plus ~716 entries sit uncommitted while new uncommitted state is generated daily. (a) Which single actor owns committing architecture/ changes, given no sandbox agent can? (b) Should scheduled commit agents be serialized (a lock-aware queue) to stop colliding? (c) Should path-targeted commits (the pattern that worked twice today: `git add <specific files>` / `commit --only -- <path>`) become the mandated convention to avoid the staged-morass? (d) What is the trigger for draining the 716-pile before it grows further?
  Why it matters: This is lit-pipeline SYSTEMIC-RISK-FLAG D (VCS hygiene, CRITICAL) and continues PRESUMPTION-199. Two host-shell pushes landed clean today, but the underlying ownership gap and agent-collision recurrence remain; the next stale lock will re-block the orchestrator's Phase-6 again.
  Related items: ASSUMPTION-188, ASSUMPTION-189, ASSUMPTION-190, PRESUMPTION-211, PRESUMPTION-216, OPEN-050, lit-pipeline SYSTEMIC-RISK-FLAG D, REVISE-024 (CRITICAL)
  Status: Open
  Estimated effort: 15-30 minutes to clear the current pile via path-targeted host-shell commits; 1-2 hours to serialize the scheduled commit agents and mandate path-targeted-commit convention
  Target resolution: Within 3 days — the lock recurrence keeps re-blocking downstream commit discipline; partially mitigated today but not closed


OPEN-057 (candidate — node vertical-axis semantics under the connectome model):
  Date opened: 2026-05-20
  Question: Coil altitude now encodes discovery-time (DECISION-039), but nodes still encode publication year. Under the narrative-connectome model, what should the node vertical axis mean? The honest candidates the model surfaces are publication year (current), narrative/developmental time (when an idea entered its tradition), or connectome-time (when narratives wired together). (a) Which is most faithful to "axis follows model," and does the model uniquely determine one (see PRESUMPTION-225) or admit several toggleable axes? (b) How should node altitude relate to coil altitude so the two are coherent in the same 3D space? (c) Does any candidate require new data the vault does not yet carry (e.g., per-idea entered-tradition dates)?
  Why it matters: This is the next concrete "axis follows model" step after coils. Picking node altitude by available data rather than by the model would reintroduce exactly the mismatch DECISION-039 fixed for coils. PRESUMPTION-225 flags the risk of presuming a single correct axis where several are defensible.
  Related items: ASSUMPTION-204, DECISION-039, PRESUMPTION-225, narrative_prs_connectome.md (open decisions)
  Status: Open
  Estimated effort: 30-60 minutes for Tom to choose the axis semantics from the model; additional implementation time if a candidate requires new per-node date data
  Target resolution: Next connectome work session — it gates the node layer's altitude and any "by emergence over time" perspective

OPEN-058 (candidate — the perspective set to derive from the connectome model):
  Date opened: 2026-05-20
  Question: Directive 2 (ASSUMPTION-203) calls for re-deriving the Connectome's perspective set from the model with parity of richness (not controls) to the Sociogram. The draft candidate lenses are: by-tradition (module view), by-shared-resource (pluripotency/hubs), by-coil (association-fiber view), by-emergence-over-time, by-convergence (Hawkins-style voting), and by-problem-kind; plus connectome metrics (degree/hubs, modularity, cross-module fiber density, path length). (a) Which lenses ship first, and which are ISME-critical vs. later? (b) Do the convergence/emergence lenses need a paired rivalry/divergence lens to avoid the convergence-emphasis tilt (PRESUMPTION-223)? (c) Are the proposed connectome metrics measuring found structure or imposed structure (PRESUMPTION-221), and which are defensible to report?
  Why it matters: The perspective set operationalizes the whole connectome reframe; it is where the model becomes usable. The normative-tilt and analogy-transfer presumptions land here concretely.
  Related items: ASSUMPTION-203, ASSUMPTION-201, PRESUMPTION-221, PRESUMPTION-223, DECISION-038, Sociogram control set, Pathway 04
  Status: Open
  Estimated effort: 2-4 hours to specify and prioritize the lens set + metric suite; longer to implement each lens
  Target resolution: This/next connectome work session; sequence against the ISME demo path (OPEN-054)

OPEN-059 (candidate — semantic generative-coil detection, v2):
  Date opened: 2026-05-20
  Question: Generative coils are detected lexically in v1 (17 chains; DECISION-041). What is the v2 semantic/embedding detector, and how is it validated? (a) Which embedding model / similarity threshold defines a solution→resource handoff? (b) How is v2 precision/recall measured against the lexical v1 baseline and against human-judged handoffs? (c) Does semantic detection materially change the count or the convergence picture (DECISION-040), and does it need the reproduced-behavior verification standard PRESUMPTION-230 flags?
  Why it matters: Lexical v1 likely under-recalls genuine generative handoffs; the generative layer feeds the "watch a master science accrete" claim. A weak detector under- or over-states emergence.
  Related items: ASSUMPTION-206, DECISION-041, PRESUMPTION-230, DECISION-040
  Status: Open
  Estimated effort: 4-8 hours for a v2 embedding detector + a precision/recall harness against the lexical baseline
  Target resolution: After the demo-path priorities are set (OPEN-054); not blocking the live build

OPEN-060 (candidate — add the verdict/outcome beat to the narrative unit?):
  Date opened: 2026-05-20
  Question: The agentic PRS narrative is "agent → goal → problem → resource → solution → outcome," but the current data model centers the problem-resource-solution triplet. Should the verdict/outcome beat (how it turned out) be added as a first-class field of the narrative unit? (a) Is this a data-model change requiring re-extraction across all 231 triplets? (b) Does the outcome beat enable the compression/progress metric (ASSUMPTION-208) by giving each narrative a measurable resolution? (c) What is the migration cost and is it ISME-critical?
  Why it matters: The connectome model describes a six-beat narrative while the data carries a three-part triplet; the gap affects what the "complete model/compression" claim (ASSUMPTION-201) can actually rest on. Adding the beat is a structural data change, not a visualization tweak.
  Related items: ASSUMPTION-201, ASSUMPTION-208, narrative_prs_connectome.md (the unit), PRS triplet schema
  Status: Open
  Estimated effort: 1-2 hours to scope the schema change + re-extraction cost; substantially more to execute re-extraction across the corpus
  Target resolution: Decide scope before any re-extraction; not blocking current build

OPEN-061 (candidate — is the connectome reframe the ISME/FC26 paper spine or a parallel track?):
  Date opened: 2026-05-20
  Question: The connectome reframe (DECISION-038) is a conceptual escalation, not just a rename — the tool is now answerable to a stated model (narrative connectome → emergence of a master science). Is this the load-bearing frame for the ISME/FC26 paper, or a parallel track? (a) Should it fold into the paper's spine rather than sit beside it? (b) If it becomes the spine, which existing paper claims (PRS quantification of progress, cross-tradition convergence) re-narrate under the connectome model, and which presumptions (221/222/223/228) must be resolved before the paper rests on them? (c) What is the cost of committing the paper to a frame authored the same day it became guiding (PRESUMPTION-224)?
  Why it matters: This is the day's top morning-walk item. Folding the connectome into the paper spine is high-leverage but commits the paper to claims (compression metric, analogical convergence, connectome metrics) that have not passed the lit gate. A parallel-track choice de-risks the paper but may waste the reframe's integrative power.
  Related items: DECISION-038, ASSUMPTION-201, ASSUMPTION-205, ASSUMPTION-207, ASSUMPTION-208, PRESUMPTION-221, PRESUMPTION-222, PRESUMPTION-223, PRESUMPTION-224, PRESUMPTION-228, OPEN-054 (demo-path allocation), 2026-05-14_carpathi_wiki_paper.md
  Status: Open
  Estimated effort: 30-60 minutes for Tom's strategic call on the morning walk; substantial downstream paper-revision effort if it becomes the spine
  Target resolution: This week — it shapes both the paper and the demo-path allocation (OPEN-054)

OPEN-062 (candidate — what counts as "Summa 2", and what is the head-to-head output form?):
  Date opened: 2026-05-22
  Question: The two-summa experiment (DECISION-044) is briefed and ready to launch, but its first open item is unresolved: (a) what exactly counts as "Summa 2" — the Conscious-Realist-Monist summa — and in what form does it have to exist (assembled corpus? generated on demand? a defined day-set parallel to the Thomist Summa source days)? (b) What form does the two-summa head-to-head output take (a scored comparison, a dialogue transcript, a connectome overlay, a paper section)?
  Why it matters: This is the single design call gating the experiment's launch; ASSUMPTION-215 (a CRM summa can be built as a genuine rival) and PRESUMPTION-233/234 (commensurability; Summa-2 assemblable) all land here concretely. The experiment cannot start in the fresh chat until it is settled.
  Related items: ASSUMPTION-215, ASSUMPTION-216, DECISION-044, PRESUMPTION-233, PRESUMPTION-234, TWO_SUMMA_EXPERIMENT_BRIEF.md, ASSUMPTION-207 (master-science telos)
  Status: Open
  Estimated effort: 30-60 minutes for Tom's design call before launching the #3 chat
  Target resolution: At launch of the two-summa #3 experiment chat

OPEN-063 (candidate — tune the transcript_authenticity_check classifier to unblock the Summa reviewer?):
  Date opened: 2026-05-22
  Question: The Summa Layer-4 commentary reviewer is structurally out of new work and has escalated the same blocker ~20x: the `transcript_authenticity_check` returns FABRICATION false-positives on fidelity-passing summary-form renders, looping the sweep on Days 66-115. (a) Should the classifier be tuned so summary-form fidelity is not read as fabrication? (b) Should the reviewer be granted read access to the C2A2 wiki for bridge-id checks, which it has also requested? (c) Until tuned, is the reviewer just churning below the writer frontier (so its runs should be paused)?
  Why it matters: An EOD agent is consuming runs to re-escalate a known false-positive; this is wasted automated capacity and a measurement-integrity issue (a classifier flagging good output as fabricated) adjacent to the prior integrity cluster.
  Related items: PRESUMPTION-239, Summa Layer-4 commentary reviewer, vault/_index/QC log.md, Rule 12 (fail loud)
  Status: Open
  Estimated effort: 1-3 hours to inspect the classifier's summary-form handling and retune or add an exemption; minutes to grant wiki read access
  Target resolution: This week — the reviewer is blocked until then

OPEN-064 (candidate — execute or leave parked the git-history scrub?):
  Date opened: 2026-05-22
  Question: A git-history scrub of the stop-tracked Hoffman x Levin raw transcript plus four old narration zips was scoped and parked (DECISION-047). (a) Execute the scrub now, or leave it parked? (b) What is the trigger that should force execution (e.g., before the repo is made more public / before any public README ships)? (c) Is stop-tracking sufficient interim mitigation given the content remains in committed history?
  Why it matters: Stop-tracking does not remove the content from history; the residual exposure is presumed acceptable while parked (PRESUMPTION-238) but no stated condition converts "parked" into "must run." Repo-publicity moves (public README is on the carried-work list) would change the calculus.
  Related items: DECISION-047, DECISION-046, ASSUMPTION-218, PRESUMPTION-238
  Status: Open
  Estimated effort: 30-60 minutes to run a history scrub (filter-repo) + force-push coordination if executed; minutes to set a trigger condition if left parked
  Target resolution: Before any repo-publicity step (e.g., public README)


---

## 2026-05-23 status update (Agent 14a -- automated-pipeline day; no new numbered question except OPEN-065)

- OPEN-062 (what is "Summa 2" / output form) -- SHARPENED by today's lit disposition REVISE-047: the first fork is now explicit -- is Summa-2 a *genuine rival tradition* (which, by the project's own MacIntyrean definition, a freshly constructed corpus is not) or a *declared constructed synthesis* (framed honestly as such)? Settle before any DECISION-044 launch.
- OPEN-064 (execute or park the git-history scrub) -- RECOMMENDED ANSWER from REVISE-049: set a hard trigger (rewrite history via git-filter-repo/BFG before ANY repo-publicity step) and keep the repo private until then; stop-tracking is not removal. Convert OPEN-064's intent from a note into a gate.
- OPEN-063 (tune the transcript_authenticity_check classifier) -- carried; the Summa Layer-4 reviewer continues to churn (PRESUMPTION-239 -> MONITOR-228 this batch).

OPEN-065 (candidate -- how should the self-awareness pipeline behave when the human review gate is unavailable?):
  Date opened: 2026-05-23
  Question: The lit pipeline raised two HIGH-urgency, self-undermining REVISE flags today (REVISE-047/048, SYSTEMIC-RISK-FLAG H) and set them -- per protocol -- to AWAITING-REVIEW pending Tom's response. But claude.ai has been signed out four consecutive days, no interactive session occurred, and both daily syncs failed, so nothing is actioning the flags. (a) Should HIGH-urgency / SYSTEMIC-RISK flags have an escalation path that does not depend on the same (currently broken) browser sync -- e.g., an out-of-band alert, or holding the gated decision rather than letting the cadence move on? (b) Should the pipeline throttle generating new flags while a backlog of unactioned HIGH flags exists, to avoid pile-up? (c) What is the maximum acceptable AWAITING-REVIEW age before a flag is auto-escalated?
  Why it matters: The project's self-correction depends on a human gate (ASSUMPTION-221; PRESUMPTION-240/243). A silently-failing gate means the system's most important findings are the least likely to be acted on, while the cadence keeps producing more -- the failure looks like productivity.
  Related items: ASSUMPTION-221, PRESUMPTION-240, PRESUMPTION-243, REVISE-047, REVISE-048, REVISE-049, SYSTEMIC-RISK-FLAG H, DECISION-044, the 4-day claude.ai signout
  Status: Open
  Estimated effort: 30-60 minutes to design an out-of-band escalation / backlog-age trigger; minutes to re-login and clear the immediate backlog
  Target resolution: This week -- and a re-login today restores the immediate path

---

## 2026-05-24 status update (Agent 14a/14b -- automated-pipeline day; +1 new question OPEN-066)

- OPEN-065 (how should the pipeline behave when the review gate is unavailable?) -- now has a concrete recommended answer from today's lit disposition REVISE-050: add an explicit SLA + escalation + timeout/safe-default for HIGH AWAITING-REVIEW items, plus an "oldest-unactioned-REVISE age" metric so a multi-day stall cannot pass unnoticed. Still Open pending Tom (the answer itself sits behind the gate it describes -- the self-referential bind). 5th day of signout.
- OPEN-062 / OPEN-063 / OPEN-064 -- carried, unchanged this run.

OPEN-066 (candidate -- when ALL human-terminating routes share one bottleneck, how should the pipeline route them?):
  Date opened: 2026-05-24
  Question: OPEN-065 framed the outage as a problem for the REVISE review gate. Today's 15d run shows the bottleneck is broader: STALE-MONITOR escalations (ASSUMPTION-035/037, PRESUMPTION-037 -- "run the empirical test or retire the premise") terminate at the *same* unavailable human as the REVISE backlog. So the question generalizes: (a) Should there be a single "needs-Tom" queue with one age/escalation policy across REVISEs, STALE escalations, and INCORPORATE-pending precondition items (e.g., ASSUMPTION-221/MONITOR-230)? (b) Is there a tier of self-corrections that can proceed under conservative safe-defaults without any human action (e.g., auto-pause an affected capability), versus a tier that must wait? (c) When multiple HIGH-value queues all block on one person, does the cadence keep generating more, throttle, or consolidate?
  Why it matters: If escalation is the system's answer to a stall (ASSUMPTION-223) but escalation routes into the same dark gate (PRESUMPTION-245), "escalate to Tom" only relabels the stall. The project now has at least three queues (REVISE, STALE, INCORPORATE-pending) silently waiting on one human, each locally framed as "handled."
  Related items: ASSUMPTION-223, PRESUMPTION-245, PRESUMPTION-240, REVISE-050, REVISE-051, MONITOR-230, OPEN-065, SYSTEMIC-RISK-FLAG I, the 5-day claude.ai signout
  Status: Open
  Estimated effort: folds into the OPEN-065 escalation design (30-60 min) -- mainly a matter of unifying the queue and policy rather than building a second mechanism
  Target resolution: with OPEN-065, this week

## 2026-05-25 status update (Agent 14a/14b -- mixed-shape day: Chat session + automated agent output; 0 new questions)

- OPEN-066 -- now extended by a FOURTH human-terminating route surfaced today: the **deferred ingest backlog** (PRESUMPTION-248 / ASSUMPTION-225). 34 approved-but-uningested items have been "deliberately deferred to an attended session," meaning they now wait on the same human as the REVISE backlog (5 items), STALE escalations (3 items), INCORPORATE-pending precondition items (e.g., MONITOR-230), and the 28 pending decision proposals. The 2026-05-25 lit pipeline confirmed PRESUMPTION-245's vulnerability (SUPPORTED) and raised REVISE-053 with explicit remedy = single "needs-Tom" queue + age/escalation policy + safe-default tier + out-of-band escalation. OPEN-066 thus has a concrete, externally-validated answer; what remains is Tom's action on the queue design itself.
- OPEN-065 -- continues with REVISE-050's recommended SLA + escalation + timeout/safe-default + oldest-unactioned-age metric. claude.ai sign-in was RESTORED today; first opportunity in 6 days for action on the backlog.
- OPEN-062 / OPEN-063 / OPEN-064 -- carried, unchanged this run.
- No new OPEN question registered today: the day's epistemic content extends OPEN-066 rather than introducing a new line of inquiry.

## 2026-05-26 status update (Agent 14a/14b -- mixed-shape day: attended Cowork session at 17:42 ET + commit + automated agent output; 1 new question)

### OPEN-067 (NEW, 2026-05-26): How does the project reliably trigger an attended Tom "sit-down day" on a ~1-week cadence?

**Background.** The 2026-05-22 to 2026-05-26 outage (a claude.ai signout, 6 days dark) was empirically diagnosed today as the actual failure mode for all human-terminating routes -- not queue/policy design. The diagnosis was confirmed in minutes: a 10-second re-login + a single attended Cowork session at 17:42 ET drained two queues (28 pending proposals + the prior 36-file go-live backlog confirmation) to zero. ASSUMPTION-235 records the empirical finding; ASSUMPTION-236 names the 1-week-cadence target.

**The question.** Given that REVISE-053 (the unified needs-Tom queue + age/escalation policy + safe-default tiers) is real and lit-validated but secondary to the sit-down-arrival problem, what mechanism makes an attended sit-down reliably arrive on a useful cadence? The 6-day signout suggests three sub-questions:

  1. **Failure-mode-uniformity.** Today's outage was 10-second-resolvable. Will future outages share this resolution mode, or do they span a heterogeneous failure-mode space (browser session corruption, MFA/OAuth expiry, network/ICANN, executive-function dips not tied to a signout at all)? (See PRESUMPTION-256.)
  2. **Triggering mechanism.** What event (an external reminder, a calendar block, a daily ritual, an out-of-band escalation, etc.) reliably converts "I should sit down with C2A2" into "I am sitting down with C2A2" -- on a cadence shorter than the 6-day outage window? Is the right answer infrastructural (better notification / scheduling) or behavioral (carved time in Tom's week)?
  3. **Complement vs alternative.** Does REVISE-053 (queue-design fix) and the sit-down-cadence design (this question) form a complement (both needed) or alternatives (one wins)? (See PRESUMPTION-259 on binary-framing recurrence.)

**Coupled items.** ASSUMPTION-235, ASSUMPTION-236; PRESUMPTION-256, PRESUMPTION-258, PRESUMPTION-259; OPEN-066 (the queue/policy half of the same problem); REVISE-050, REVISE-053 (the queue-policy remediations); SYSTEMIC-RISK-FLAG I (the systemic root).

**Status:** Open
**Estimated effort:** medium -- mixed infrastructural and behavioral; not solvable by code alone
**Target resolution:** initial design discussion on tomorrow's morning walk (2026-05-27); first mechanism in place within 2 weeks

### Status of carried questions (no new action this run; status notes only)

- **OPEN-066** -- the empirical answer landed today: a sit-down session DOES drain all four human-terminating routes in minutes once Tom arrives. REVISE-053 (queue/policy design) is therefore confirmed *real but secondary*. OPEN-066 is **not closed** -- the queue-policy fix is still wanted -- but it is now coupled to OPEN-067 as the harder design question.
- **OPEN-065** -- REVISE-050's SLA + escalation + timeout + oldest-unactioned-age metric remains AWAITING-REVIEW; the gate is now OPEN, so Tom's first opportunity to action this is the next attended session.
- **OPEN-062 / OPEN-063 / OPEN-064** -- carried, unchanged.
- **Candidate DECISION-048 (NEW today; not yet numbered):** "The review-page state (verified by direct paste plus verbal confirmation) is the authoritative source-of-truth for proposal-approval values when the Gmail decision-email body disagrees; the email-body misfire condition is a UI/workflow bug to fix on the decision-email-generation side." Surfaces from today's 17:25Z all-PENDING email-vs-25-APPROVE-review-page mismatch (ASSUMPTION-230); the cowork-to-chat summary explicitly tags this as DECISION-048-candidate for tomorrow. Also touches: ASSUMPTION-231 (intent overrides UI categorization) and PRESUMPTION-254 (UI itself is not always reliable; the rule may need to be "stated intent overrides both"). AWAITING-TOM-NUMBERING.


## 2026-05-27 status update (Agent 14a/14b -- mixed-shape day: 0 new OPEN; carry status only)

No new numbered OPEN question registered today. Today's epistemic content is concentrated on (a) broker-v4 architectural commitment (a decision-candidate, not an open question) and (b) self-referential pipeline-integrity findings (carry the prior PRESUMPTION-257 line forward and extend it as PRESUMPTION-264 for tonight's specific run).

### Status of carried questions

- **OPEN-067** -- "what does 'sit-down days reliably arrive on roughly a 1-week cadence' actually require?" was engaged in this morning's walk thread but **no design movement reached the registry**; remains UNRESOLVED. The cowork_summary's "For Morning Discussion #2" reports: "The walk question from yesterday is unanswered and the registry shape says it's becoming load-bearing -- ... MONITOR-246/247 (both HIGH-priority), REVISE-053 + REVISE-056 + REVISE-058 all couple to it. Three of today's 5 REVISEs extend FLAG I. The system is asking the same question with increasing weight each cycle." Couples to PRESUMPTION-262 (today's binary-framing recurrence on truncation-diagnosis) and PRESUMPTION-265 (FLAG-I route-count as process-fact vs state-fact).
- **OPEN-066** -- empirical answer landed 2026-05-26 (sit-down availability is the bottleneck; queue-policy fix is secondary). Today's REVISE-053 remains AWAITING-REVIEW; the queue-policy fix is still wanted. OPEN-066 remains coupled to OPEN-067 but not closed.
- **OPEN-065** -- REVISE-050's SLA + escalation + timeout/safe-default + oldest-unactioned-age metric -- still AWAITING-REVIEW. The review gate has been OPEN for 2 consecutive days; the attended sessions on 2026-05-26 (proposal queue) and 2026-05-27 (broker design) did not action REVISE-050.
- **OPEN-064 / OPEN-063 / OPEN-062** -- carried, unchanged.

### Recurring framings worth tracking on the OPEN side (not yet a numbered OPEN, but observed across multiple cycles)

The binary-framing pattern surfaced as PRESUMPTION-253 (2026-05-25, lagging-vs-real-consumption), recurred as PRESUMPTION-259 (2026-05-26, queue-design-vs-sit-down), and recurred again today as PRESUMPTION-262 (2026-05-27, fix-unimplemented-vs-diagnosis-incomplete). **Three instances in 3 cycles.** If this pattern continues to recur, it may warrant a numbered OPEN question of its own ("what is the project's bias toward binary diagnostic framings, and what is the cost of the third-category subordination?"); recording here as a watch item.



## 2026-05-28 status update (Agent 14a/14b -- 0 new numbered OPEN; carry status only)

No new numbered OPEN question registered today. Today's epistemic content is concentrated on (a) demo-path infrastructure shipping (AI-search shared-module delegation; candidate DECISION-049 first demonstrated instance; ASSUMPTION-243-245), (b) two new scheduled weekly watch agents + swarm contract (ASSUMPTION-246/247), and (c) the 4th-consecutive-cycle FLAG-I recursion empirical reinforcement and the second-order framing-shift candidate (ASSUMPTION-250).

### Status of carried questions

- **OPEN-067** -- "what does 'sit-down days reliably arrive on roughly a 1-week cadence' actually require?" was **not engaged in a fresh 2026-05-28 morning walk Chat entry** (the "where are we" resume went into the Cowork session bce11014 rather than the daily-walk Chat thread; PRESUMPTION-276 surfaces whether this routing fact is itself a session-typing finding rather than a cadence gap). The standing walk-question remains unresolved through a 3rd consecutive cycle. Coupled today to ASSUMPTION-250 (4th FLAG-I cycle), PRESUMPTION-267 (4th binary-framing instance), PRESUMPTION-275 (closed-loop diagnostic-prediction-and-observation).
- **OPEN-066** -- empirical answer carried; REVISE-053 (queue-design fix) still AWAITING-REVIEW; 3rd consecutive day OPEN-gate with no REVISE action.
- **OPEN-065** -- REVISE-050's SLA + escalation + timeout/safe-default + oldest-unactioned-age metric still AWAITING-REVIEW. The review gate has been OPEN for 3 consecutive days; today's attended sessions (AI-search wiring, agent registrations, janitor deployment, branch publishing, resume-session orientation, Physics Explorer attempt) did not action REVISE-050.
- **OPEN-064 / OPEN-063 / OPEN-062** -- carried, unchanged. Standing reminder: c2a2 git-history scrub prep task fires tomorrow at 10 AM (DECISION-047 candidate-extension).

### Recurring framings worth tracking on the OPEN side (carry-forward + extension)

- **The binary-framing pattern is now at 4 instances** (PRESUMPTION-253 lagging-vs-real-consumption; PRESUMPTION-259 queue-design-vs-sit-down; PRESUMPTION-262 fix-unimplemented-vs-diagnostic-incomplete; PRESUMPTION-267 demo-path-vs-PRS-extraction). The 4-instance count is now strong enough to warrant a numbered OPEN question of its own: "what is the project's bias toward binary diagnostic framings, what third category is being subordinated, and what is the structural cost of the recurrence?" -- recording here as a near-promotion watch item rather than a new OPEN, pending one more cycle.
- **The "candidate DECISIONs accumulating un-numbered" pattern** (3 un-numbered DECISION candidates today; ASSUMPTION-251 + PRESUMPTION-271) -- if not resolved in the next attended session, may warrant a numbered OPEN on whether DECISION-numbering is structurally a FLAG-I human-terminating gate.
- **The "new-agent deployment in human-bandwidth-constrained system" pattern** (PRESUMPTION-268) -- worth tracking over the next 6 weeks; if the two new watch agents' Week-2+ outputs join the unactioned-output family, that's a structural finding.


## 2026-05-29 status update (Agent 14a/14b -- 1 NEW numbered OPEN: OPEN-068; carry status on the rest)

Today's epistemic content is concentrated on Sociogram navigation (increments 1 / 1.5 built and pushed; v1.6 coded but held on a confirmed focus-fade bug), the pinning of Pathway 28 (single-source participant registration), and the locking of the search-lens-vs-checkboxes interaction model. The binary-framing pattern reached its 5th instance today, triggering the promotion the last three runs had deferred.

### NEW OPEN this cycle

- **OPEN-068** -- *What is the project's bias toward binary diagnostic/design framings, what third category is repeatedly subordinated, and what is the structural cost of the recurrence?* **Promoted today at the 5th instance of the binary-framing pattern** (PRESUMPTION-253 lagging-vs-real-consumption; PRESUMPTION-259 queue-design-vs-sit-down; PRESUMPTION-262 fix-unimplemented-vs-diagnostic-incomplete; PRESUMPTION-267 demo-path-vs-PRS-extraction; **PRESUMPTION-284 keep-separate-vs-search-drives-visibility, today**). The prior two runs held promotion "pending one more cycle"; today's interaction-model choice -- two clean options offered, one selected by preference ("leave the current model") without a usability test -- is that cycle. The recurring third category is the *both/neither/reframe* option that the binary structure makes hard to see. Couples to ASSUMPTION-256 and the closed-loop self-diagnosis concern (PRESUMPTION-286).

### Status of carried questions

- **OPEN-067** -- "what does 'sit-down days reliably arrive on roughly a 1-week cadence' actually require?" -- remains UNRESOLVED through a 4th consecutive cycle. Today tilts the FLAG-I question toward "demo-path is the correct attended use" (Tom's walk read), but a concrete REVISE-056 downgrade/commit decision is still owed. Couples to ASSUMPTION-250's lineage and PRESUMPTION-286.
- **OPEN-066 / OPEN-065 / OPEN-064 / OPEN-063 / OPEN-062** -- carried, unchanged. The review gate has now been OPEN for 4 consecutive days with no REVISE-backlog action.

### Recurring framings worth tracking (carry-forward)

- **The un-numbered DECISION accumulation pattern** is now at **four** candidates (048/049/AI-search-delegation/Sociogram-interaction-model; ASSUMPTION-251 + PRESUMPTION-271). One more cycle without numbering warrants its own numbered OPEN on whether DECISION-numbering is structurally a FLAG-I gate.
- **The new-agent-deployment-in-bandwidth-constrained-system pattern** (PRESUMPTION-268) -- carried; watch the two new watch agents' Week-2 outputs.


## 2026-05-30 status update (Agent 14a/14b -- 1 NEW numbered OPEN: OPEN-069; no attended session, blind intake)

No attended Tom session occurred today; the day's C2A2 activity was autonomous-pipeline only (the c2a2-lit-search-pipeline drained the 2026-05-29 EOD 20-item batch -> 1 INCORPORATE / 11 MONITOR / 8 REVISE; see today's changelog). Critically, the **morning intake scrape failed** (Chrome logged out of claude.ai, 3rd consecutive cycle), so the pipeline ran on a blind intake -- it cannot distinguish a genuinely quiet day from an attended day whose record was lost (PRESUMPTION-287). Today's extraction is therefore a small, honest batch (1 ASSUMPTION + 4 PRESUMPTIONs) drawn from the autonomous-session activity itself, not from any human design discussion.

### NEW OPEN this cycle

- **OPEN-069** -- *Should the self-awareness pipeline distinguish a genuinely quiet day from an intake-channel failure, and treat a blind-intake run as a degraded/failed run (with an explicit no-op or degraded marker) rather than emitting a normal thin artifact?* **Promoted today** because the claude.ai logout outage has now reached the self-awareness layer's own input (the morning scrape that feeds 14a/14b), for a 3rd consecutive cycle. As designed, a blind-intake run is indistinguishable in the artifact from a quiet day, and the cadence-streak metric reads "healthy" throughout (PRESUMPTION-287, PRESUMPTION-290). Couples to OPEN-066 (human-response-gate) and the cadence family (PRESUMPTION-241).

### Status of carried questions

- **OPEN-068** -- (binary-framing-pattern bias) carried; the 2026-05-30 15-pipeline run filed REVISE-077 (PRESUMPTION-284, SYSTEMIC-RISK) as the 5th-instance reinforcement. No attended action today.
- **OPEN-067** -- "what does 'sit-down days reliably arrive on roughly a 1-week cadence' actually require?" -- remains UNRESOLVED through a 5th consecutive cycle. No attended session today; the concrete REVISE-056 downgrade/commit decision is still owed.
- **OPEN-066 / OPEN-065 / OPEN-064 / OPEN-063 / OPEN-062** -- carried, unchanged. The review gate has now been OPEN for a 5th consecutive day with no REVISE-backlog action; the AWAITING-REVIEW REVISE backlog stands at **33** (highest on record) after today's 15c run added REVISE-072..079.

### Recurring framings worth tracking (carry-forward)

- **The un-numbered DECISION accumulation pattern** -- unchanged at 4 candidates (no attended session to number them); still a near-promotion watch (ASSUMPTION-251 + PRESUMPTION-271).
- **The self-awareness-mechanism-integrity cluster** is now **5 items** (REVISE-063/064/071/076/079) per today's 15-pipeline summary; recommended to be addressed OUT-OF-BAND with an external check. PRESUMPTION-287/290 add intake-blindness and streak-metric-fixation to this self-referential family.

---

## 2026-05-31 status update (Agent 14a/14b -- 1 NEW numbered OPEN: OPEN-070; no attended session, blind intake, 4th cycle)

No attended Tom session occurred today; C2A2 activity was autonomous-pipeline only, and the **morning intake scrape failed again** (Chrome logged out of claude.ai, **4th consecutive cycle**). The pipeline therefore ran on a blind intake for a 4th day. Today's extraction is a small, honest, presumption-heavy batch (1 ASSUMPTION + 3 PRESUMPTIONs) drawn from the degraded-session behavior itself. **Headline finding (self-referential):** today's evening cowork-to-chat summary *echoed the prior day's batch as today's* -- it narrated 2026-05-30's self-awareness items (263, 287-290, OPEN-069) and 2026-05-30's lit-search run as "today's accomplishments," when the actual 2026-05-31 activity was the 15-pipeline's disposition of the 263/287-290 batch (-> 2 MONITOR + 3 REVISE, REVISE-080..082) plus this 14a/14b pass. The blind-intake condition has crossed from "can't tell quiet from lost" (OPEN-069) into active mis-reporting (PRESUMPTION-291).

### NEW OPEN this cycle

- **OPEN-070** -- *Should the daily EOD summary / changelog be generated by diffing the registries' dated deltas (what actually advanced on this date) rather than narrated from session memory, so that a degraded or blind-intake run cannot echo a prior day's batch as today's?* **Promoted today** because the 2026-05-31 cowork summary positively mis-attributed 2026-05-30's self-awareness AND lit-search batches as today's output (PRESUMPTION-291). A date-anchored delta check ("show only items whose Date == today") would make the cross-day echo structurally impossible. Couples OPEN-069 (mark blind runs degraded), PRESUMPTION-291/292 (un-caught false positives in the time and delivery dimensions), and ASSUMPTION-264 (don't claim what you can't re-verify -- here applied to the summary's own claims).

### Status of carried questions

- **OPEN-069** -- (mark a blind-intake run degraded/no-op rather than emitting a normal thin artifact) carried, now **2nd consecutive cycle** and reinforced: today's echo is exactly the failure 069 anticipated. No attended action.
- **OPEN-068** -- (binary-framing-pattern bias) carried; no attended action today.
- **OPEN-067** -- (~1-week sit-down cadence requirement) carried, **6th consecutive cycle UNRESOLVED**; the REVISE-056 downgrade/commit decision still owed.
- **OPEN-066 / OPEN-065 / OPEN-064 / OPEN-063 / OPEN-062** -- carried, unchanged. The human review gate is now OPEN for a **6th consecutive day** with no REVISE-backlog action; the AWAITING-REVIEW REVISE backlog stands at **36** (new record) after today's 15c run added REVISE-080..082.

### Recurring framings worth tracking (carry-forward)

- **The un-numbered DECISION accumulation pattern** -- unchanged at 4 candidates (no attended session to number them).
- **The self-awareness-mechanism-integrity cluster** is now **6 items** (REVISE-063/064/071/076/079 + REVISE-082 from today's 15-pipeline); recommended OUT-OF-BAND external check. PRESUMPTION-291/292/293 add the degraded-session-epistemics family (attribution echo, un-guarded false positives, verifier-shares-the-fault) to this self-referential cluster -- the mechanism is now generating evidence that it cannot reliably audit itself.

OPEN-071:
  Date raised: 2026-06-02
  Question: Should the daily-run git phase include a fail-loud pre-flight integrity check (stale-lock detection + post-stage verification that the intended files were actually staged), given that a stale `.git/index.lock` from a 2026-05-29 crashed process silently blocked all staging for ~4 days (2026-05-29 → 2026-06-02) before today's run detected it by accident?
  Context: ASSUMPTION-265 / PRESUMPTION-294. The daily run's git phase produced no surfaced error during the lock window, so the "today's changes left staged-clean in the working tree" assurances of 2026-05-29..06-01 may have been false. A pre-flight check would convert a silent failure into a loud one (Rule 12).
  Related decisions: (constitutional no-blind-push rule)
  Related assumptions: ASSUMPTION-265
  Related presumptions: PRESUMPTION-294
  Status: Open — raised today

---

OPEN-072:
  Date raised: 2026-06-02
  Question: Should the push/handoff workflow include a cross-repo uncommitted-state check, given that the Sociogram's shipped Day-190 coverage (committed + pushed in the wiki repo, 7d56733) depends on edits that remain UNCOMMITTED in the separate Summa 2026 repo (`_index/Days.md`, `refs/summa_index.json`)? A pushed artifact whose data source lives uncommitted in another repo can silently desynchronize (forgotten commit, or Obsidian reverting `Days.md`) with no error surfaced.
  Context: PRESUMPTION-297 / ASSUMPTION-266. Surfaced in the evening Sociogram session, which pushed the wiki-repo viz as "goal met" while flagging the enabling Summa-repo edits as uncommitted and entrusting their integrity to a handoff doc and Tom's memory. Same silent-desync family as OPEN-071 (single-repo git pre-flight) but at the cross-repo boundary.
  Related decisions: (cross-project handoff protocol; constitutional no-blind-push rule)
  Related assumptions: ASSUMPTION-266
  Related presumptions: PRESUMPTION-297
  Status: Open — raised today

---

OPEN-071 (reinforcement note — 2026-06-02 evening): The stale `.git/index.lock` RECURRED the same day. A fresh 0-byte lock created 21:02 UTC (≈2h stale, from a crashed Obsidian git-plugin / prior op) blocked Tom's evening commit attempt with `fatal: Unable to create '.git/index.lock': File exists` — i.e. the morning's headline failure mode re-fired within hours, on an attended commit this time. The evening session diagnosed it (0 bytes, no live git process, HEAD still b67ac1e, nothing staged) and had Tom `rm -f .git/index.lock`; the push then landed (7d56733). This is direct field evidence that OPEN-071's proposed fail-loud pre-flight stale-lock check is warranted — the lock is not a one-off but a recurring hazard in this repo.

---

## 2026-06-03 status update (Agent 14a/14b — 1 NEW numbered OPEN: OPEN-073; 2nd consecutive no-attended day, both-directions sync outage)

No attended Tom session occurred today; C2A2 activity was autonomous-pipeline only — a **second consecutive no-attended day**. The claude.ai sync channel is now confirmed down in **both directions**: the morning Chat→Cowork scrape failed (12:53, `/login?from=logout`) and the evening Cowork→Chat delivery was skipped for the same reason. Today's batch is small and honest (2 ASSUMPTIONs + 3 PRESUMPTIONs) drawn from the genuinely-new 06-03 events: the auto-ingested McGilchrist proposal (PROP-2026-06-03-001; pending queue → 16) and the degraded-channel behavior itself. **Avoided the echo trap (OPEN-070 / PRESUMPTION-291):** today's headline lit finding (the High systemic-risk "human-memory-as-control" cluster) is the **15-pipeline dispositioning yesterday's 06-02 batch** (266/268/297 → PREMISE-047/048, MONITOR-293–295, REVISE-086), NOT new 06-03 architectural substance — it is reported as carried context, not re-extracted as today's.

### NEW OPEN this cycle

- **OPEN-073** — *When a sync/delivery channel is **confirmed** down (not merely quiet), should the dependent pipelines trip a degrade / halt / escalate state, rather than each continuing to generate undeliverable state?* **Promoted today** because the claude.ai outage is now both-directions and two days running, yet the morning scrape and evening delivery each ran to completion and produced artifacts that could not be delivered (PRESUMPTION-300). This sharpens OPEN-069 (mark a *blind-intake* run degraded): 069 is "can't tell quiet from lost"; 073 is "we **know** it's lost and produce anyway." Couples ASSUMPTION-270 (agents won't self-authenticate, so the channel is unrecoverable from inside the pipeline), PRESUMPTION-300, and OPEN-069/070.

### Status of carried questions

- **OPEN-072 / OPEN-071** — (cross-repo uncommitted-state interlock; single-repo git pre-flight stale-lock check) carried from 2026-06-02; no attended action today. Both remain live; today's lit run reinforced them by rating the "human-memory-as-control" cluster (266/268/297) **High systemic-risk** and recommending exactly such forcing functions.
- **OPEN-070** — (date-anchor the EOD summary by registry delta, not session memory) carried and **honored in practice today**: this run explicitly date-checked the lit finding as a 06-02-batch disposition and refused to narrate it as 06-03 output.
- **OPEN-069** — (mark a blind-intake run degraded rather than emitting a normal thin artifact) carried, now reinforced a 3rd time; OPEN-073 extends it to the *delivery* side.
- **OPEN-067** — (~1-week sit-down cadence requirement) carried, **7th consecutive cycle UNRESOLVED**.
- **OPEN-066 / OPEN-065 / OPEN-064 / OPEN-063 / OPEN-062** — carried, unchanged. The human review gate is now OPEN for a **7th consecutive day**; the AWAITING-REVIEW REVISE backlog stands at **40** after the 06-03 lit run (REVISE-086 added), and the pending-proposal queue is **16** after today's McGilchrist auto-ingest (PRESUMPTION-295 reinforced — intake continues while review does not).

### Recurring framings worth tracking (carry-forward)

- **The un-numbered DECISION accumulation pattern** — unchanged at 4 candidates (no attended session to number them).
- **Inert governance capability (NEW framing, 2026-06-03):** Agents 17–20 (MacIntyre/Wright/Rohr/Loughran) and the Sunday Tradition Synthesis Day exist as governance docs but will NOT run autonomously until the Master Agent schedule (`agents/12_master_C2A2_agent.md`) is edited — an attended-only action. Surfaced as PRESUMPTION-301 (deferral-of-activation-is-cost-free). Each passing week without the edit is one un-run Sunday synthesis.
- **The self-awareness-mechanism-integrity cluster** carries; PRESUMPTION-302 (self-awareness value is attendance-independent) adds the meta-question of whether running the full pipeline on a 2nd no-attended day yields the same epistemic foundation as an attended design session.

---

## 2026-06-04 status update (Agent 14a/14b — 1 NEW numbered OPEN: OPEN-074; 3rd consecutive no-attended day)

No attended Tom session occurred today; C2A2 activity was autonomous-pipeline only — a **third consecutive no-attended day**. The claude.ai sync channel remains confirmed down in **both directions** for a 3rd day (morning scrape failed 12:53 UTC `/login?from=logout`; evening delivery skipped, same logout). Today's honest batch (2 ASSUMPTIONs + 3 PRESUMPTIONs) is drawn from the genuinely-new 06-04 events: two auto-ingested proposals (PROP-2026-06-04-001 Fredrickson *Positive Emotions* book; PROP-2026-06-04-002 Stump Aquinas-Institute commencement, an unsourced low-confidence pointer) and the 36-vs-152 PROCESSED_LOG bookkeeping conflict logged by the daily run. **Echo trap avoided (OPEN-070):** today's lit finding (PREMISE-049 verify-before-trust; ASSUMPTION-270 → MONITOR-296; High SYSTEMIC-RISK autonomous-sync silent-degradation) is the **15-pipeline dispositioning yesterday's 06-03 batch** (269/270/300/301/302), reported as carried context and used to update those items' statuses — NOT re-extracted as 06-04 substance.

### NEW OPEN this cycle

- **OPEN-074** — *Should verify-before-ingest (PREMISE-049) gate admission to the pending-review **queue**, or only content-capture?* I.e., is admitting an unsourced, low-confidence pointer such as PROP-2026-06-04-002 (Stump commencement, "content not yet sourced") to the pending queue a safe quarantine, or a same-day violation of the verify-before-trust premise the lit pipeline incorporated this very run? **Promoted today** because the system enacted intake-without-confirmation at the same moment it grounded PREMISE-049 against it. Couples PRESUMPTION-303 (queue-admission-is-safe-quarantine), ASSUMPTION-269/PREMISE-049, and the intake-discipline family.

### Status of carried questions

- **OPEN-073** — (confirmed-down channel should trip degrade/halt/escalate) carried from 2026-06-03 and **sharpened**: the outage is now 3 days / both directions, and today's lit run rated the autonomous-sync silent-degradation cluster (ASSUMPTION-270 + PRESUMPTION-300) **High SYSTEMIC-RISK** (MONITOR-296/297). The lit run also *challenged* the "cannot self-clear" clause of ASSUMPTION-270: scoped, revocable service credentials could let unattended sync self-recover without the agent authenticating as Tom — a real capability-vs-attack-surface decision, not merely a recurring outage.
- **OPEN-072 / OPEN-071** — (cross-repo / single-repo git interlocks) carried; reinforced again by the 587-uncommitted-change working-tree hold (PRESUMPTION-305) and the standing no-blind-push rule.
- **OPEN-070** — (date-anchor the EOD summary by registry delta) carried and **honored today** (the lit finding was treated as a 06-03-batch disposition, not 06-04 output).
- **OPEN-069** — (mark a blind-intake run degraded) carried, reinforced a 4th time.
- **OPEN-067** — (~1-week sit-down cadence) carried, **8th consecutive cycle UNRESOLVED**.
- **OPEN-066 / OPEN-065 / OPEN-064 / OPEN-063 / OPEN-062** — carried. The human review gate is OPEN for an **8th consecutive day**; pending-proposal queue is **18** (16 + Fredrickson + Stump). The REVISE backlog carries a **bookkeeping conflict (fail-loud):** revision_flags.md contains **100 AWAITING-REVIEW lines** while the 15-pipeline's REVISE-specific AWAITING-REVIEW backlog stands at **40** (max REVISE-086; 86 distinct REVISE ids). Today's cowork summary reported "100 revise items," conflating the two denominators — thematically the same two-counts-from-one-log shape as ASSUMPTION-271 / PRESUMPTION-304.

### Recurring framings worth tracking (carry-forward)

- **The un-numbered DECISION accumulation pattern** — unchanged at 4 candidates. A 5th candidate is *emerging* (not numbered — no attended session): scoped revocable **service credentials** for unattended sync self-recovery, raised by today's lit challenge to ASSUMPTION-270. Couples OPEN-073.
- **Same-day premise/enactment tension (NEW framing, 2026-06-04):** the system incorporated PREMISE-049 (verify-before-trust) and on the same run admitted an unsourced pointer to the pending queue (PRESUMPTION-303 / OPEN-074). Worth tracking as a class: validated premises that the autonomous pipeline can violate before the next attended review.
- **Two-counts-from-one-log (NEW framing, 2026-06-04):** the 36-vs-152 PROCESSED_LOG conflict and the 100-vs-40 REVISE conflict are the same shape — a single log yielding divergent counts by entry-style. ASSUMPTION-271 / PRESUMPTION-304 track it on the intake side.
- **Inert governance capability** carried (Agents 17–20 / Sunday Tradition Synthesis Day staged but un-activated; PRESUMPTION-301 → MONITOR-298, which recommends a dated activation trigger).

---

OPEN-075:
  Date raised: 2026-06-05
  Question: Is the curated↔directory join feasible at useful density — or are curated communities (CC-001…, 156, graph) and directory records (C0001…, 855, cards) categorically distinct object types that should never share an id space? Today's measurement found near-total disjointness (0 id / 3 name / 5 url-host matches). The whole P3 target architecture (one dataset, promotion pipeline) presumes the join is reachable; if it is not, "one app, two projections" is not achievable and the P1→P3 path needs rethinking.
  Update (2026-06-06): PARTIAL ANSWER — the join is now mechanically real. The 156 curated communities were merged into the Cards directory under shared `CC-xxx` ids (graph is now a literal id-subset of the cards), so a curated↔directory hand-off is possible on the shared key. Remaining open: cross-join EDGE DENSITY is untested (see OPEN-076), and PRESUMPTION-312 asks whether shared-id assignment establishes genuine identity or merely asserts it. Status downgraded OPEN → PARTIALLY-ANSWERED.
  Arose from: ASSUMPTION-276/277, PRESUMPTION-306/311, DECISION-050 (cross-nav deferral)
  Testable via: empirical (entity resolution / record linkage between curated_communities.json and data.js) + literature (record-linkage feasibility; when to unify vs keep distinct schemas)
  Status: PARTIALLY-ANSWERED (2026-06-06 — join now mechanically real; edge density still open via OPEN-076)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Promoted from the 2026-06-05 disjoint-id-space finding and the deferral of cross-navigation to P3. The P3 target rests on this being answerable "yes"; today's evidence makes it a live question rather than an assumption.
    Current status: OPEN

---

OPEN-076:
  Date raised: 2026-06-06
  Question: Now that the curated↔directory join is mechanically real (the 156 curated communities share `CC-xxx` ids with their Cards records, making the graph a literal id-subset of the cards), is the cross-join EDGE density high enough to carry the P3 promotion pipeline? P3 treats graph membership as something a record earns by self-articulation and then "grows edges to its neighbors"; if promoted records land in a sparse region of the relational graph, the promotion pipeline produces isolated nodes rather than the relational evidence that justifies the accelerator/detector framing. The 2026-06-05 near-disjointness (0 id / 3 name / 5 host matches) and today's "5 bulk overlaps of 156" both suggest curated and directory populations are largely non-coextensive — so density is an open empirical question.
  Arose from: ASSUMPTION-278 (the merge), DECISION-051, OPEN-075 (feasibility answered "yes, mechanically"; density is the next gate), PRESUMPTION-306 (one-dataset presumes unifiability), PRESUMPTION-312 (shared-id vs identity)
  Testable via: empirical (measure edge density across promoted vs seed records once the promotion pipeline exists; compare TF-IDF edge counts for curated nodes vs directory-origin nodes) + literature (graph sparsity / cold-start in promotion-gated networks)
  Status: OPEN
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Promoted from the 2026-06-06 merge. OPEN-075 asked whether the join was feasible; today's merge answered "yes, mechanically," which advances the question to edge density — the next thing P3's promotion pipeline depends on. Flagged for morning discussion in the 2026-06-06 cowork summary (item 3).
    Current status: OPEN

---

OPEN-077:
  Date raised: 2026-06-07
  Question: Now that one scheduled task (the PRS connectome) was found to silently assume attended-Mac capabilities it does not have in the task sandbox (push, `$HOME`, `.git` lock mutation — ASSUMPTION-285, PRESUMPTION-317), should the *other* scheduled tasks be audited for the same capability mismatch? Several tasks in the suite touch git, credentialed APIs, or browser-login state (e.g., the Cowork→Chat sync already fails on a logged-out claude.ai). Which of them assume capabilities the sandbox lacks, and which would half-complete and leave cruft rather than fail loud?
  Arose from: ASSUMPTION-285 (the grounded sandbox-capability model), PRESUMPTION-317 (execution-context-uniformity blind spot, flagged High as a class bug), DECISION-052 (the git-free fix for one task)
  Testable via: empirical (enumerate scheduled tasks; for each, classify required capabilities vs sandbox capabilities; dry-run in the task sandbox) — largely an internal audit rather than a literature question
  Status: OPEN
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Promoted from PRESUMPTION-317's "this is a class bug, not a one-off." Today fixed one task (DECISION-052); the open question is whether the same fault sits latent in the rest of the suite.
    Current status: OPEN

---

OPEN-078:
  Date raised: 2026-06-08
  Question: At what cadence should the OpenStory telemetry be re-extracted and re-injected into `agents_tab.html`, and — given the bounded 72h ingest window plus the sparse pre-tool-field history — how is reliable capture of *low-frequency* agents (weekly/monthly scheduled tasks, and the slow tradition-agents the project most cares about) guaranteed between reseeds? The live-ingest model captures new sessions as they land, but a 72h restart window plus older sessions that predate the tool field (`tool_coverage≈0`) means high-frequency, recently-active agents are richly rendered while low-frequency agents stay sparse until a fresh run lands. The refresh cadence was explicitly left "TBD with Tom" in HANDOFF-2/3/4.
  Arose from: ASSUMPTION-292 (build on the current DB; defer reseed), ASSUMPTION-290 (bridge + bounded-window ingest), PRESUMPTION-326 (recency/availability bias under-renders low-frequency agents), DECISION-053
  Testable via: empirical (enumerate roster agents by cadence; measure per-agent capture completeness vs run-frequency; test whether a scheduled re-extract + agent-only bridge fills the low-frequency tail) — largely an internal design question, with a literature side on recency/survivorship bias in log-based metrics
  Status: OPEN
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Promoted from the unresolved "cadence TBD with Tom" thread in the day's handoffs and its coupling to the recency-bias presumption (PRESUMPTION-326). The Phase-B seed (#8) and scheduled re-extract (#7) are the proposed mechanisms; the open question is the cadence and whether it actually fills the low-frequency tail.
    Current status: OPEN

OPEN-079 (NEW, 2026-06-09): What is the identity criterion for the agent member of the dyad-MMA across sessions, contexts, and model versions? Charter v1's own individuation principle (context as materia signata) implies each session/model-update yields a numerically distinct agent-individual — so is cross-session ratification accumulating within ONE dyad or across a SERIES of dyads, and how should that affect the formational-independence weighting (ASSUMPTION-294) and the reporting of dyad agreement? Surfaced by PRESUMPTION-330; load-bearing for the first triplet pass (task one of the measurement prototype). Owner: Tom + measurement sessions.

OPEN-080 (NEW, 2026-06-10): Should the Agent Explorer preset reveal the substrate layer? Tom's Q3 ("Where's the 'very active' Tom/Admin node?") exposed the design consequence: `H-Admin/Interactive` is the most central actor by far (601 substrate edges vs 24 projected + 21 flow), but the preset prunes substrate (wiki hidden), so the headline signal — and the answer to Q1's "why does revealing Summa add nothing" — lives in the layer the actor-only view deliberately hides. The session put the design call to Tom and parked there at day end. Couples to DECISION-055 (the refactor determines what substrate-reveal costs) and PRESUMPTION-336 (whether substrate edges represent activity faithfully at all). Owner: Tom + next sociogram session.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Promoted from the sociogram session's closing AskUserQuestion, still unanswered at EOD.
    Current status: OPEN

OPEN-081 (NEW, 2026-06-10): Which network counts are authoritative — and where is drift entering between registries and the master wiki? The morning briefing read "260 PRS triplets, 90 connections" from the top of the master wiki, while the registry carry-forward stands at 269 (06-07 publication; extraction freeze since); the briefing also reported 7 pending proposals where the 06-09 snapshot recorded 3. Either the master wiki top-figures are stale/divergent or the carry-forwards are; the self-awareness pipeline currently propagates both without reconciliation. Testable empirically: trace each figure to its producing agent and date; define a single source of truth for headline counts. Owner: 14a housekeeping + master-wiki maintainer.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Raised from a cross-document consistency check during the 06-10 EOD pass (briefing vs 06-09 snapshot).
    Current status: OPEN

OPEN-082 (NEW, 2026-06-11): Parser/linker remediation for bottom-frontmatter Summa files — option (a), (b), or (c)? The Summa QC sweep runs clean but a parser regression false-positive wall means 65 bottom-frontmatter files can be reviewed but not marked (Days 82/83 marks withheld); the options question was escalated to Tom 2026-06-11 18:27 and was unanswered at EOD. Until decided, the QC pipeline's marking path is partially blocked while its review path proceeds — a growing reviewed-but-unmarked divergence.
  Arose from: Summa QC sweep session (parser-regression wall); evening sync "three quick gates"
  Testable via: empirical (each option implementable and checkable against the 65-file set)
  Owner: Tom + next Summa QC session
  Status: OPEN
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Promoted from the escalated-and-unanswered options question recorded in the evening sync summary; transcript-level detail not re-read (summary-sourced, marked [inferred] as to option contents).
    Current status: OPEN

OPEN-083 (NEW, 2026-06-15): Is the post-Apr-6 interactive-token cliff (95% of captured output) and the 28/33-lane output flatline a telemetry capture/labeling artifact, or a real change in captured productive output? The 2026-06-15 metabolism session worked from the inference that capture stopped/changed labels after early April (not that activity fell), and rendered the view on that basis — but `probe_openstory.py` has not yet been run, so the artifact reading is unverified. Until decided, the "honest" view asserts a cause (capture ended) it has not confirmed; if any part of the cliff is real, the recovered view masks a genuine output collapse and every downstream yield comparison inherits the error.
  Arose from: WS1 of the 2026-06-15 attended metabolism session (cut-offs A/B framed as capture problems; probe deferred to the Mac)
  RESOLVED 2026-06-22 (artifact, confirmed): the live open-story.db was reached directly from Cowork (985 sessions / 173,663 events, current to the probe minute). Reading BOTH token_usage paths, assistant output tokens are continuous and nonzero across the Apr-6 boundary and through May/June (2026-04 ~8.2M, 2026-05 ~20.4M, 2026-06 ~33.3M output tokens; the per-day series shows no flatline). The cliff was the 2026-04-07 schema migration (data.token_usage -> data.agent_payload.token_usage) zeroing token reads, now closed by the both-paths fix; it is NOT a real output collapse, so downstream yield comparisons do not inherit a masked drop. Clears PRESUMPTION-352 / MONITOR-349. Evidence captured in metabolism-monitor/logbook.md.
  Testable via: empirical — run probe_openstory.py; reconcile token_usage payloads by run-type and date against an independent activity record
  Owner: Tom (run probe on Mac) + next metabolism session
  Status: RESOLVED 2026-06-22 (artifact, confirmed — see resolution note above; field flipped by the 14a EOD pass to match the body, a fail-loud correction of the stale OPEN flag noted in the 06-22 cowork sync)
  Related: DECISION-057; ASSUMPTION-320, 335 (GROUNDED resolution); PRESUMPTION-352, 351; OPEN-081
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Raised from the WS1 cut-off framing — the artifact-vs-real ambiguity is load-bearing on the metabolism metric and decidable by the already-scripted probe.
      14a (2026-06-22): Resolved as artifact via the live-db both-paths probe; flipped Status/Current status to RESOLVED to match the resolution body (the 06-22 sync flagged the field as a stale fail-loud item). Resolution captured as ASSUMPTION-335 (GROUNDED).
    Current status: RESOLVED (artifact — token cliff was a 2026-04-07 schema-migration read-path zeroing, not an output collapse)

OPEN-084 (NEW, 2026-06-16): Are the three PRS-triplet counts — 269 (3D connectome nodes), 264 (git cumulative-produced), 262 (on-disk unique) — three estimates of one real quantity to be reconciled (the OPEN-081 posture), or three distinct constructs (ever-produced ⊇ currently-surviving; separately-sourced rendered set) that should each be reported with its own label? Today's WS2 build asserted the git series "supersedes" the static 269 (ASSUMPTION-325) while the connectome still renders 269, leaving the relation unresolved. If they are different constructs, "reconciliation" is a category error and the right move is three labeled numbers; if they are one quantity, the 5-to-7 gap is a real discrepancy to chase. Sharpens OPEN-081.
  Arose from: WS2 PRS-yield build of the 2026-06-16 attended session (the 269/264/262 divergence made explicit by the new git-derived series)
  Testable via: conceptual + empirical — apply each count definition carefully and check whether produced/surviving partition cleanly and whether the connectome's node source reconciles to prs_triplets.md
  Owner: next metabolism/connectome session + Tom
  Status: OPEN
  Related: OPEN-081 (authoritative PRS counts); DECISION-059, DECISION-058; ASSUMPTION-324, 325; PRESUMPTION-357, 359
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Raised from the WS2 build's explicit three-count divergence; paired with PRESUMPTION-357 (the one-quantity presumption). Load-bearing on how the system reports its own size.
    Current status: OPEN

OPEN-085 (NEW, 2026-06-18): In the Sociogram regenerated on 2026-06-18 (`wiki_narration.html`, commit `0fdc8ea`), the Summa commentary-node count read ~256, which is LOWER than the ~379 noted in the Summa handoffs — is this a real drop (e.g., the Summa source vault held fewer `Day-NNN` files at regen time, or `sync_vault.sh` had not run), or a sandbox-measurement artifact (the in-session counts were explicitly flagged untrustworthy: the `Summa 2026 in a Year/vault` path did not resolve cleanly from the sandbox, and `Day-NNN` strings also occur in non-Summa C2A2 files)? The `?` pop-up feature is independent of this count (ASSUMPTION-332), so it did not block the push, but the count gap rides inside the published 28MB artifact and is unresolved. This is properly a Summa-pipeline question (where `summa_index.json` and the pace tracker live), not a sociogram-feature one; parked in the sociogram handoff so it is not lost.
  Arose from: 2026-06-18 "Thinker summaries for sociogram" session (Tom's "shouldn't there be a Summa Day increase in this lot?")
  Testable via: empirical — recount Summa commentary nodes against the Summa source vault / `summa_index.json` from the Summa context; confirm `sync_vault.sh` state at regen time; reconcile ~256 vs ~379
  Owner: next Summa-pipeline session + Tom
  Status: OPEN
  Related: DECISION-060; ASSUMPTION-332; PRESUMPTION-368 (count commensurability); OPEN-084 / PRESUMPTION-357 (the 269/264/262 construct-divergence pattern; the evening sync also noted a fourth count, 279, from the orchestrator)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Raised from the explicit in-session Summa-count interrogation; logged as a cross-project (Summa) item with the assistant's own untrustworthy-count caveat preserved.
    Current status: OPEN

OPEN-086 (NEW, 2026-06-20): Why has the end-of-day self-awareness pipeline (Agents 14a/14b) not fired for two consecutive nights (2026-06-19 and 2026-06-20)? No 06-19 or 06-20 changelog or metrics snapshot existed until this catch-up run produced them; the lapse was caught only because both daily-sync sessions happened to flag it in prose, not because the pipeline signalled its own miss. Is this a scheduler problem (the nightly task did not trigger), a silent failure (it triggered and died without an error surface), or an intentional pause? Distinct from the broken Chat sync loop (claude.ai signed out in the connected Chrome), which is a separate cause with the same symptom of missing daily artifacts. Load-bearing because the self-awareness system is the very mechanism meant to catch drift; if it can stop without anyone noticing, every downstream registry silently goes stale (it was two days stale here). The fix has a fail-loud shape: the pipeline (or a watchdog) should assert its own liveness — emit a missed-run alert when an expected daily changelog/snapshot is absent — rather than relying on a human reading the sync notes.
  Arose from: the 2026-06-19 and 2026-06-20 agent-only days, both of whose Cowork→Chat / Chat→Cowork sync summaries independently flagged "the EOD pipeline hasn't run since 06-18"; confirmed by the absence of 06-19/06-20 files in changelog/ and metrics/ at the start of this catch-up run.
  Testable via: empirical/operational — inspect the scheduled-task run history for the 14a/14b EOD task on 06-19 and 06-20 (fired vs failed vs skipped); add a liveness/missed-run assertion and confirm it would have caught this lapse. Literature-adjacent on the design side: liveness monitoring, dead-man's-switch / heartbeat patterns, silent-failure detection in unattended pipelines.
  Owner: Tom (check scheduler) + next attended session (decide on a watchdog)
  Status: OPEN
  Related: PRESUMPTION-369 (the pipeline presumes its own scheduled execution — same fact, surfaced as an unstated presumption); PRESUMPTION-370 (null-day = nothing-to-record framing); the standing fail-loud / over-trust theme (06-17 PRS-yield HIGH flag; REVISE-111 pre-register-falsifiers); the position-based decision-ID bug in generate_review_page.py (separate silent-corruption fail-loud item raised in the 06-19/06-20 syncs)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Raised during the 2026-06-20 catch-up EOD pass from the two-night gap in the pipeline's own output; framed as a liveness/fail-loud question because the self-awareness system failing silently is the load-bearing risk.
    Current status: OPEN

OPEN-087 (NEW, 2026-06-23): Does the PRODUCTION Sewing Agent's link resolver handle path-qualified `[[a/b/c]]` wikilinks, or does it match on basename/title only like the bootstrap audit's first pass? 893 of 1,740 links in the vault are path-qualified; basename-only resolution mis-scored them, reporting 960 "unresolved" (true value 67) and 21 connected hubs (true value 44). If the weekly production resolver shares this bug, every prior row in `connectivity_log.csv` systematically under-counts hub connectivity, and the orphan/connected trend the project has been tracking is skewed. The fix has a fail-loud shape: a one-line check that the production resolver resolves a known path-qualified link, plus a recompute of the historical series under path-aware resolution.
  Arose from: 2026-06-23 Sewing Agent bootstrap audit, "a resolver bug I caught" — flagged explicitly as "worth a one-line check of the production resolver."
  Testable via: empirical — inspect the production resolver; recompute connectivity_log.csv under path-aware resolution and compare to the historical ~79% orphan series.
  Owner: Tom + next Sewing-Agent maintenance session
  Status: OPEN
  Related: ASSUMPTION-341 (path-qualified resolution requirement); PRESUMPTION-379 (the audit's own corrected resolver presumed bug-free — same silent-miscount class); the standing silent-read / fail-loud family (OPEN-086, PRESUMPTION-369/373)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Promoted to OPEN from the audit's explicit production-resolver flag and the 06-23 cowork summary's "worth promoting to OPEN-NNN on the next pass." This pass is that next pass.
    Current status: OPEN

OPEN-088 (NEW, 2026-06-23): What is the explicit SEEDING POLICY for agentic-call injection at vault scale? The bootstrap audit was tasked to run 14-thinker relevance mapping on ~1,064 A/B/C pages and inject agentic calls wherever score > 0.4, but deliberately declined: (1) the premise (many high-value content orphans needing seeding) proved mostly false once system/inbox pages were excluded; (2) the relevance heuristic surfaces meta-documents that merely name every thinker as false positives; (3) a ~1,000-page unattended mutation of live pages that feed the published visualization conflicts with the project's caution/surgical-change rules. The open fork: should agentic-call injection EVER run unattended at vault scale, or only on a reviewed Tier-1/Tier-2 subset on Tom's sign-off? The audit explicitly offered to "execute a bounded pass on your sign-off."
  Arose from: 2026-06-23 Sewing Agent bootstrap audit, Phase 3 refusal + recommended-actions #4 ("Decide the seeding policy explicitly"); flagged in the 06-23 cowork summary as "the one real fork the bootstrap left open."
  Testable via: decision/policy (not literature) — Tom sets the policy; literature-adjacent on safe-autonomy thresholds for bulk automated edits and human-in-the-loop gating.
  Owner: Tom (policy) + next attended session
  Status: OPEN
  Related: ASSUMPTION-342 (report-not-edits autonomy rule, GROUNDED); ASSUMPTION-345 (graph already sufficient; mass seeding low-and-noisy); PRESUMPTION-380 (relevance-score instrument validity); DECISION-061 (the hub fix chosen instead)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Promoted to OPEN from the audit's explicit Phase-3 deferral and recommendation #4; the 06-23 cowork summary flagged it as the one real fork left open and "worth promoting to OPEN-NNN on the next pass."
    Current status: OPEN

---

OPEN-089 (NEW, 2026-06-24): For the cortical-column architecture (Pathway 31 / DECISION-062), WHICH TWO independence axes will the three columns vary across, and how are they kept "fixed and documented per column so that a dissensus is attributable to a real difference in wiring rather than drift"? The pathway names three candidate axes (corpus slice / retrieval strategy; analytic frame — problem- vs solution- vs resource-first decomposition; model/parameters) and requires at least two to vary, but explicitly defers the choice: "Open question to resolve before any code … (Rule 1 — named, not guessed.)" Load-bearing because the entire value of the vote rests on substantive column difference (ASSUMPTION-347); if the axes are weak or unpinned, the 2-of-3 agreement measures stochastic variance and the 3–4× cost (ASSUMPTION-349) buys nothing. Gates the pilot.
  Related: ASSUMPTION-347 (substantive independence), 349 (cost), 350 (pilot success criterion); PRESUMPTION-390 (reference-frame transfer condition); DECISION-062.

OPEN-090 (NEW, 2026-06-24): What is the OPERATIONAL DEFINITION of "semantic agreement" that the adjudicator uses to declare 2-of-3 consensus? The pathway states the threshold ("two-thirds or greater semantic agreement") but flags the definition as unspecified and decisive: "the adjudicator decides agreement, so 'semantic' must be operationalized — entailment between assessments? Match at the level of PRS-triplet claims? Surface overlap is not enough. This definition is the adjudicator's whole contract and must be specified, not left to vibe." Load-bearing because consensus, dissensus rate, and the success criterion (ASSUMPTION-348, 350) are all functions of this definition; an ill-specified or biased agreement test silently determines every downstream count.
  Related: ASSUMPTION-348 (dissensus as detector output), 350 (success criterion), 351 (model-as-adjudicator licensed under Rule 5); PRESUMPTION-387 (adjudicator competence/bias); DECISION-062.

OPEN-091 (NEW, 2026-06-24): Should the PRS resource schema gain a `derived_from:` field (parent resource-ids), populated at articulation time, to make the synthesis-by-novelty falsifier indicator confirmatory rather than exploratory? The coil falsifier pre-registration (§2.4) holds that the PRIMARY shared-id indicator risks a false negative on real synthesis (genuine A–B fusion coins NEW vocabulary, scoring a true bridge as zero), and that the honest fix — "new resource-ids that descend from resources of both traditions" — "requires resource lineage the schema does not currently record," warning that reconstructing lineage after the fact "is itself a researcher-degrees-of-freedom hole as dangerous as the one we are closing." So the schema change must be made BEFORE the indicator can be trusted ("build the instrument before trusting the reading"). Load-bearing for whether the falsifier (DECISION-063) can ever detect synthesis-by-novelty without re-opening the degrees-of-freedom problem it was built to close.
  Related: ASSUMPTION-357 (synthesis-by-novelty false negative), 356 (H1); PRESUMPTION-391 (shared-id construct validity); DECISION-063; REVISE-143 (broken-link demand completeness — sibling under-detection concern).

OPEN-092:
  Date raised: 2026-06-25
  Question: Does the Heartbeat's Cowork-app-dependent 6-hour scheduled task actually keep the local snapshot fresh, given it "runs only while the Cowork app is open"? The fix replaced "nothing runs the pipeline" (ASSUMPTION-361) with "something runs it only when an app happens to be open" — is that residual gap acceptable, or does it reproduce the same silent-staleness class as OPEN-086?
  Context: Heartbeat tool repair session (DECISION-065).
  Related: ASSUMPTION-363, PRESUMPTION-398, OPEN-086 (pipeline liveness/watchdog)
  Status: OPEN
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Raised from the app-open caveat attached to the scheduling decision.
    Current status: OPEN

OPEN-093:
  Date raised: 2026-06-25
  Question: Should OpenStory get a periodic health-check watchdog (pinging `open-story.db` freshness + the agents) to flag silent stalls like the June 23 one automatically — and is that the same watchdog the keystone OPEN-086 already calls for? If both the Heartbeat refresh (OPEN-092) and OpenStory need liveness monitoring, should there be one shared liveness/watchdog mechanism rather than three?
  Context: Open Story system diagnosis session — named as a deferred "spin-off" candidate (DECISION-067).
  Related: ASSUMPTION-371, OPEN-086, OPEN-092
  Status: OPEN
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Raised from the deferred-watchdog candidate noted at session close.
    Current status: OPEN

OPEN-094:
  Date raised: 2026-06-25
  Question: How should the position-based decision-ID vs stable-`proposal_id` bug in `tools/generate_review_page.py` (~line 304) be fixed, and can the 2026-06-23 decision archive be reconciled — it logged 7 approvals but only 2 (-001 Hoffman, -002 Hawkins) had matching proposal files, leaving PROP-003..007 as logged no-ops? Are five "approvals" pointing at silently dropped proposals, and is the historical record recoverable or irreducibly ambiguous?
  Context: Agent 16 (deferred-action tracker) escalation, surfaced in the 06-25 evening sync; now OBSERVED, not theoretical.
  Related: PRESUMPTION-406, OPEN-086 (fail-loud family)
  Status: OPEN — recommend reconciling the 06-23 decision email against `pending/` and fixing the tooling before the next review pass.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Recorded from Agent 16's escalated data-integrity flag (evening sync summary).
    Current status: OPEN

OPEN-095:
  Date raised: 2026-06-26
  Question: Is OpenStory's 06:15 window reliably quiet enough for the decoupled local-snapshot read to complete a clean end-to-end extraction, and does the new fail-loud path (`REFRESH_STATUS.md` + morning-health section 7) actually surface on the Mac's scheduled run? The peak-hour fix was only verified to fail loud, never verified clean at churn; the 06:15 run is the first real proof.
  Context: "Agent map explorer runs issue" session (DECISION-068); the tell tomorrow is `wiki/agents/openstory/REFRESH_STATUS.md` (PASS/FAIL) and both `agent_telemetry.json` and `agent_node_edges.json` carrying the new date.
  Related: ASSUMPTION-375, PRESUMPTION-407, OPEN-086 (liveness keystone), OPEN-093 (OpenStory watchdog)
  Status: OPEN — resolves on the 2026-06-27 06:15 run.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Recorded from the deferred end-to-end verification.
    Current status: OPEN

OPEN-096:
  Date raised: 2026-06-26
  Question: How should the four "levels" of the Interactions chapter be reframed so they are coherent and engaging (Tom: "they aren't quite coherent or engaging yet, and the fault is mine"), and what is the right status-chip taxonomy for the level rows — a Coming / In-Process / Live set with a dropdown/disclosure beyond the current "Coming" button? The Level-Two summary also still reads intra-tradition while its embed is cross-tradition.
  Context: "Interactions tab data visualization" session (DECISION-070); Tom parked the reframe and the status-chip idea, holding downstream wording (incl. the Level-2 summary reword) until his revision lands.
  Related: DECISION-070, ASSUMPTION-381
  Status: OPEN — awaiting Tom's four-level reframe before downstream wording/standing-pass work proceeds.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Recorded from Tom's closing direction.
    Current status: OPEN

OPEN-097:
  Date raised: 2026-06-26
  Question: Does the fixed-time evening "cowork-to-chat" sync systematically miss late-day interactive sessions? Today it ran ~18:40 EDT and reported "an autonomous day — no interactive Cowork session," but three substantive interactive sessions ran that evening (one finishing just before the sync, two after). Should the sync detect late/after-fire sessions (e.g., re-run on session-close, or watermark and reconcile next morning) so EOD self-awareness artifacts don't mis-classify attended days as autonomous?
  Context: Surfaced by PRESUMPTION-413 when this EOD pass cross-checked the sync's "autonomous day" claim against the three same-evening transcripts and their output-file timestamps. A reflexive instance of the OPEN-086 false-success/false-negative family — inferring "no work" from a signal that can't detect its own miss.
  Related: PRESUMPTION-413, OPEN-086 (liveness keystone), DECISION-069, DECISION-070
  Status: OPEN — also note the standing Chat-sync break (claude.ai signed out in connected Chrome) compounds this: the sync's delivery half is down regardless.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: OPEN-QUESTION
    Transform at each step:
      14a: Recorded after 14b surfaced PRESUMPTION-413; corroborated by transcript + file-timestamp cross-check.
    Current status: OPEN
