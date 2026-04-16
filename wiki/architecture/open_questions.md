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
