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
