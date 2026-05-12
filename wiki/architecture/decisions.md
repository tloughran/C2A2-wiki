# C2A2 Architectural Decision Index
*Maintained by Agent 14 — Architectural History Agent | Initialized: 2026-04-09*

---

DECISION-001:
  Date: 2026-04-09
  Title: Sequential proposal IDs in review page generator
  Summary: Changed generate_review_page.py to always assign sequential IDs (001-N) regardless of agent-assigned proposal_id in frontmatter, fixing duplicate ID bug that broke sidebar navigation after item 4.
  Changelog entry: wiki/architecture/changelog/2026-04-09_changes.md (CHANGE-2026-04-09-001)
  Category: Tooling
  Status: Active

DECISION-002:
  Date: 2026-04-09
  Title: Supplementary proposal mechanism for deep-read analysis
  Summary: Established convention for supplementary proposal files (PROP-YYYY-MM-DD-SUPP-NNN) that extend existing proposals with additional PRS triplets from deeper analysis, inserted into the same review pipeline.
  Changelog entry: wiki/architecture/changelog/2026-04-09_changes.md (CHANGE-2026-04-09-002)
  Category: Workflow
  Status: Active

DECISION-003:
  Date: 2026-04-09
  Title: Adopt Thousand Brains Theory as C2A2 architectural reference model
  Summary: Recognized structural homology between C2A2's 13-agent system and Hawkins' Thousand Brains architecture. Six design changes proposed in phased timeline. See redesign proposal.
  Changelog entry: wiki/architecture/changelog/2026-04-09_changes.md (CHANGE-2026-04-09-003)
  Category: Meta-architecture
  Status: Under review (proposal pending approval)

DECISION-004:
  Date: 2026-04-09
  Title: Create Architectural History Agent (Agent 14)
  Summary: New agent to inspect daily Cowork sessions and produce structured changelogs, decision index entries, and open question tracking. Agent definition written; infrastructure seeded.
  Changelog entry: wiki/architecture/changelog/2026-04-09_changes.md (CHANGE-2026-04-09-004)
  Category: Agent design
  Status: Superseded by DECISION-005 (14a/14b split)

DECISION-005:
  Date: 2026-04-10
  Title: Split Agent 14 into 14a (Assumption Extractor) and 14b (Presumption Detector)
  Summary: The unified Agent 14 was split to separate stated assumptions (things designers know they're assuming) from unstated presumptions (things taken for granted without awareness). 14a extracts stated assumptions; 14b surfaces unstated presumptions. The distinction matters for epistemic honesty — downstream consumers need to know whether original designers were aware of a premise.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md
  Category: Agent design
  Status: Active (definitions written; first run pending)

DECISION-006:
  Date: 2026-04-10
  Title: Create Agents 15a (Lit Search FOR) and 15b (Lit Search AGAINST)
  Summary: Two literature search agents that independently test assumptions and presumptions surfaced by 14a/14b. 15a searches for supporting evidence; 15b searches for challenging evidence. Independence prevents confirmation bias. Combined results determine item status via reconciliation rules.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md
  Category: Agent design
  Status: Active (definitions written; first run pending)

DECISION-007:
  Date: 2026-04-10
  Title: Adopt provenance protocol for inter-agent chain-of-custody tracking
  Summary: Every item passing between self-awareness agents carries a PROVENANCE header with origin, chain, item type (ASSUMPTION vs PRESUMPTION), transforms at each step, and current status. The item type tag serves as a footnote protocol — PRESUMPTION means original designers were NOT aware of the premise.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md
  Category: Protocol
  Status: Active (spec written at wiki/architecture/provenance_protocol.md)

DECISION-008:
  Date: 2026-04-10
  Title: Enhance dispatch format with reference_frame_location and conceptual_bearing
  Summary: All 11 tradition agent dispatch formats updated with two new fields: reference_frame_location (which concept-space the dispatch originates from) and conceptual_bearing (directional signal toward which question the dispatch moves). Implements Thousand Brains reference frame principle.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md
  Category: Protocol
  Status: Active (all 11 agent definitions updated)

DECISION-009:
  Date: 2026-04-10
  Title: Adopt developmental maturity model (Stages 0-5)
  Summary: Defined 6-stage maturity pathway from infrastructure (Stage 0) through maturity (Stage 5). Each stage has measurable benchmarks. Health metric r (intra-consensus / cross-survival rate, must be statistically >1) is the core health indicator. Baseline metrics snapshot captured as Stage 0.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md
  Category: Meta-architecture
  Status: Active (Stage 0 baseline captured)

DECISION-010:
  Date: 2026-04-10
  Title: Adopt tripling strategy for tradition agents (intra-tradition consensus before cross-tradition dialogue)
  Summary: Each tradition will have 3 agents with differentiated perspectives that must reach consensus (≥2/3 agreement) on PRS triplets and hypotheses before those items enter cross-tradition dialogue. Pilot cluster: Hawkins×3, Friston×3, Levin×3. Full rollout: 33 tradition agents.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md
  Category: Meta-architecture
  Status: Approved in principle (implementation Phase 2a, April 14-15)

DECISION-011:
  Date: 2026-04-10
  Title: Adopt PRS displacement vectors as semantic phrasings
  Summary: PRS triplets will be extended with a Displacement field expressing how R transforms P into S as a natural-language semantic vector (a phrasing, not a pointer). Enables comparison of transformation patterns across traditions. Tied to the hypothesis of finite connecting memes.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md
  Category: Data model
  Status: Approved in principle (implementation Phase 1, April 10-11)

DECISION-012:
  Date: 2026-04-10
  Title: Create Agent 15c (Net Evaluator & Dispositioner) to close the self-awareness loop
  Summary: The 14a/14b → 15a/15b pipeline tested items but had no decision point. 15c reads paired for/against results and dispositions each item: INCORPORATE (into validated premises register), MONITOR (hand to 15d for weekly re-evaluation), or REVISE (flag for human review). Creates a "validated premises" database as operational self-knowledge.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md (CHANGE-2026-04-10-008)
  Category: Agent design
  Status: Active (definition written; first run pending after first 15a/15b cycle)

DECISION-013:
  Date: 2026-04-10
  Title: Create Agent 15d (Periodic Monitor) for long-term evidence tracking
  Summary: Manages MONITOR items on weekly cadence (re-triggering 15a/15b until 15c changes disposition) and INCORPORATED premises on monthly cadence (ensuring validated premises don't calcify). Tracks evidence trajectories and escalates stale items.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md (CHANGE-2026-04-10-009)
  Category: Agent design
  Status: Active (definition written; first run after first 15c cycle populates monitor queue)

DECISION-014:
  Date: 2026-04-10
  Title: Track self-awareness overhead via cycle time and decision backlog, not agent ratio
  Summary: The self-awareness layer scales with architectural decision complexity, not tradition agent count. A fixed ratio would drift as traditions are tripled. Instead, track: (a) self-awareness cycle time per item (full loop duration), and (b) decision backlog (items in QUEUED or MONITOR status). Growth in either signals pipeline problems.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md (CHANGE-2026-04-10-010)
  Category: Meta-architecture / Metrics
  Status: Active (fields added to metrics framework)

DECISION-015:
  Date: 2026-04-10
  Title: Create Agent 16 (Deferred Action Monitor) for condition-based deferred items
  Summary: A new agent that tracks deferred actions across three intake channels: review-conditional requests (CHANGE/CHECK/CONDITIONAL from Tom's review), agent-exchange deferrals (hypotheses that can't be evaluated yet), and human-originated watch requests (prospective intelligence items). Monitors conditions, routes resolved items. Fills the gap where CHANGE/CHECK items in `needs_review/` had no processing agent.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md (CHANGE-2026-04-10-011)
  Category: Agent design + Workflow
  Status: Active (definition written; first run pending)

DECISION-016:
  Date: 2026-04-10
  Title: Add CONDITIONAL as fifth review decision option
  Summary: When a proposal depends on an external event (transcript published, paper updated) rather than a human edit, Tom can now use CONDITIONAL with a structured condition and cadence. Agent 16 monitors the condition and re-queues the proposal to `pending/` when met. Formalizes what CHANGE was being informally used for in event-dependent cases.
  Changelog entry: wiki/architecture/changelog/2026-04-10_changes.md (CHANGE-2026-04-10-012)
  Category: Workflow
  Status: Active (README updated; review page generator may need update to add CONDITIONAL button)

DECISION-017:
  Date: 2026-04-15
  Title: Recognize triangular evidence structure as meta-finding for Consciousness Cluster unification
  Summary: The three core Consciousness Cluster findings — FINDING-004 (Hoffman ↔ Kastrup direct ontological convergence), FINDING-009 (Friston ↔ Kastrup boundary equivalence), and FINDING-011 (Hoffman → Friston trace logic subsumption) — form a closed triangle with three independent evidence paths arriving at the same conclusion through different methods (philosophical, structural, and mathematical respectively). This triangular overdetermination is itself evidentially significant: it means the unification claim does not depend on any single link. If any one finding fails, the other two still provide an independent path between the same programs. The network should track and evaluate the triangle as a unit, not just the individual findings. The associative property applies: Hoffman↔Kastrup directly (FINDING-004) AND Hoffman→Friston→Kastrup via formal subsumption (FINDING-011 + FINDING-009) constitute two independent derivations of the same equivalence. Action: Email sent to Kastrup, Hoffman, and Friston (cc Levin) posing the boundary-equivalence question directly to the principals. Their responses will determine whether the triangle holds, collapses, or reveals structure not yet visible from within the network.
  Changelog entry: wiki/architecture/changelog/2026-04-15_changes.md
  Category: Meta-architecture / Epistemology
  Status: Active (email sent; awaiting responses)

DECISION-018:
  Date: 2026-04-16
  Title: Rescue commit of wiki repo (v4-narration-checkpoint) and refactor wiki_narration.html to a modular Vite-based architecture
  Summary: After discovering 189 uncommitted files dating back to April 8 in the C2A2 wiki git repository, the decision was taken (a) to rescue-commit the current state on main, tag it v4-narration-checkpoint, and branch to narration-modular for ongoing work, and (b) to refactor the 1341-line single-file wiki_narration.html into a modular structure (graph.js / tts.js / narration.js / ui.js + data/*.json regenerated by a build_data.py scanner, with Vite as the build tool). Tom explicitly approved the refactor ("let's get right to the hard work of doing it right"). The single-HTML-file architecture was described as the limiting factor ("we are now fighting the format, not the problem"). Script checkpoint-commit.sh was written for Tom to run locally (sandbox cannot perform git commits). Publication remains private for now per ASSUMPTION-030.
  Changelog entry: wiki/architecture/changelog/2026-04-16_changes.md
  Category: Tooling / Architecture
  Status: Partial (commit script written; refactor scaffolding pending; Tom to run script locally). **Update 2026-04-17:** .git/index.lock blocked the rescue commit path during the morning autonomous run; checkpoint-commit.sh has not yet been executed; DECISION-018 remains Partial.

---

## Candidate Decisions Identified 2026-04-17 (Not Yet Formalized)

The following afternoon-session implicit decisions have not yet been written as formal DECISION-NNN entries. They are recorded here as candidates pending Tom's endorsement at the next morning walk or review session. See PRESUMPTION-041 (14b) which flags the pattern of implicit-decision drift.

DECISION-019 (candidate — plugin architecture):
  Date: 2026-04-17
  Title: Cowork-resume-session plugin published as phrase-triggered single skill (not SessionStart hook)
  Summary: The cowork-resume-session plugin was packaged as a single skill that activates on trigger phrases ("resume" / "continue" / "pick up" variants) rather than as a SessionStart hook that would silently auto-load context on every new Cowork session. Pattern-based filter excludes automated/scheduled sessions (C2a2, morning-health, wiki-agent-daily, heartbeats, dated prefixes) with a `limit: 120` escape hatch for named resumes.
  Category: Tooling
  Status: Candidate — INFORMAL CORROBORATION 2026-04-18. Today's Dispatch session "Wiki visualization architecture in dispatch mode" opened with "Let's resume my most recent discussion" — a natural trigger phrase that matched the skill; the resume flow produced a coherent orientation brief, correctly filtered automated sessions, and found the intended "Debug wiki visualization: graph, voice, layout" session. Pattern-filter did not silently hide any interactive session in that invocation. Promote to DECISION if 2-3 more such invocations succeed over the next week without false negatives. Related assumptions: ASSUMPTION-033, ASSUMPTION-038.

DECISION-020 (candidate — regenerator model default):
  Date: 2026-04-17
  Title: Default regenerator model upgraded from claude-opus-4-6 to claude-opus-4-7
  Summary: Code edit in narration/tools/regenerate_narrations.py changed the default model constant. Rationale was not stated in the session. Regeneration did not run due to the Anthropic billing block, so the upgrade's effect on narrator output quality has not yet been observed.
  Category: Tooling
  Status: Candidate — promote to DECISION if post-regeneration narrator output quality confirms the upgrade was warranted.

DECISION-021 (candidate — cross-session handoff pattern):
  Date: 2026-04-17
  Title: Cross-session handoff via ~/Documents/Claude/Handoffs/latest.md + SessionStart hook
  Summary: When an interactive session is blocked on a vendor-side issue (e.g., Anthropic billing propagation) but has well-defined next steps, the session is parked with a handoff written to ~/Documents/Claude/Handoffs/latest.md for the next scheduled agent (Saturday Dispatch) to auto-load via a resume-handoff SessionStart hook. First real stress test is 2026-04-18 Dispatch run.
  Category: Workflow / Architecture
  Status: Candidate — PARTIAL CORROBORATION 2026-04-18. The Dispatch session "Wiki visualization architecture in dispatch mode" auto-loaded Friday's narrator-debugging context via the resume-handoff SessionStart hook; the orientation brief was coherent and did not require re-prompting. Loading half confirmed (see ASSUMPTION-044). Payload-execution half remains UNTESTED because Tom pivoted the session to the ChatGPT scrape task, which discharged the Python helper work without re-queueing it. PRESUMPTION-046 surfaces the structural ambiguity this creates: if users habitually pivot on arrival, the execution half may never be observed in practice. Promote to DECISION only after a future Dispatch session where no user pivot occurs and the payload is actually executed. Related assumptions: ASSUMPTION-035, ASSUMPTION-044. Related presumption: PRESUMPTION-046.

DECISION-022 (candidate — briefing-layer audit contract):
  Date: 2026-04-20 (conceptual; surfaced by Run 1 self-awareness cycle)
  Title: Briefing-layer audit contract (flag-vs-reconcile + selection-criterion logging)
  Summary: The morning briefing accumulated three stated methodological commitments today (ASSUMPTION-046 17→11 findings filter; ASSUMPTION-047 flag-vs-reconcile disposition on master-wiki staleness; ASSUMPTION-048 "clear" semantics for stale-placeholder queues). Together they sketch a candidate audit contract that any briefing-layer transform must log its selection criterion and flag-vs-reconcile disposition alongside the transformed output. ASSUMPTION-047 has been INCORPORATED as PREMISE-006 (2026-04-20 15c cycle); the full contract is not yet drafted.
  Category: Protocol / Briefing layer
  Status: Candidate — formalization blocked on (a) writing a briefing-layer style guide and (b) retrofitting ASSUMPTION-048 to match ASSUMPTION-047's flag-over-reconcile policy (today's 15c cycle flagged INTERNAL-CONSISTENCY between them). Related assumptions: ASSUMPTION-046, 047, 048. Related presumption: PRESUMPTION-053.

DECISION-023 (candidate — caching / execution protocol v1.0):
  Date: 2026-04-20 (surfaced by supplementary Run 2 self-awareness cycle from the C2a2 caching architecture monday session)
  Title: Layer 2 Execution/Trigger Protocol v1.0 with prompt-caching architecture
  Summary: A coherent Execution Protocol v1.0 was drafted today covering session lifetime, static/dynamic prefix partitioning, tool-definition immutability, pipeline topology, and smoke-test rollout gates. Core commitments: (1) one session = one full tradition agent run (ASSUMPTION-049); (2) static prefix = 49 slow-changing RC Wiki files, dynamic suffix = vault daily activity, date-stamped filenames excluded from cached region (ASSUMPTION-050); (3) all tool definitions load upfront and never mutate mid-session (ASSUMPTION-051); (4) self-awareness pipeline (14a→14b→15a→15b→15c) runs as appended turns in one session rather than five (ASSUMPTION-053); (5) three smoke tests including byte-stability for cache determinism (ASSUMPTION-054); (6) projected 70–80% aggregate cost reduction, ~50% Levin per-run (ASSUMPTION-052). First rollout target: Levin v1.0 on 2026-04-27. Pre-flight gate: clear the 2026-04-16 .git/index.lock on physmini02 before `bash setup.sh` and wiring claude_desktop_config.json. **Update 2026-04-21:** the pre-flight gate is now compound — in addition to the stale lock, the wiki daily run's Phase 6 attempt today revealed that the sandbox mount topology does not include the repo path (ASSUMPTION-055). Clearing the lock in the sandbox is insufficient if the sandbox cannot reach the repo. The pre-flight sequence may need restructuring around a host-machine git-writer rather than a sandbox-internal commit step; see OPEN-035.
  Category: Meta-architecture / Execution protocol
  Status: Candidate — formalization deferred pending (a) Tom's endorsement; (b) pre-flight .git/index.lock clear + sandbox-mount-topology resolution (ASSUMPTION-055 / OPEN-035); (c) addressing the presumptions surfaced alongside the assumptions (PRESUMPTION-055 binary partition as sole primitive; PRESUMPTION-056 quality-regression smoke test absent; PRESUMPTION-057 RC Wiki churn-rate unaudited; PRESUMPTION-058 Levin+Friston joint-entry rationale not reviewed before split). Promote to DECISION after Levin v1.0 first run on 2026-04-27 if byte-stability passes, cost-delta within 10% of projection, and no quality regression observed. Related assumptions: ASSUMPTION-049, 050, 051, 052, 053, 054, 055. Related presumptions: PRESUMPTION-055, 056, 057, 058, 061. Implementation note: ASSUMPTION-053 will require updating the 14a and 14b agent-definition files to reflect the appended-turn topology.

DECISION-024 (candidate — specialist-task invariants / turn-cap default):
  Date: 2026-04-21 (conceptualized 2026-04-20 via OPEN-033; explicitly endorsed by Chat-side Claude on the 2026-04-21 morning walk)
  Title: Specialist scheduled tasks SHOULD declare a turn-cap; missing default = 20
  Summary: Minimal-form specialist-task invariant proposed to close OPEN-033. Specialist scheduled tasks (Levin-Friston, Hawkins-Hoffman, narrator, and other tradition-agent slots) SHOULD declare an explicit turn-cap (or wall-clock or cost-cap) in their task definition; if missing, a default cap of 20 turns applies. Rationale from Chat-side Claude: "A weak circuit breaker beats none, and you can tune the number later" (ASSUMPTION-062). Scope is deliberately narrow — no cost-cap or wall-clock-cap enforcement in this first cut; just a turn-count circuit breaker that interrupts unbounded loops. Live data points accumulating for this candidate as of 2026-04-21 EOD: (1) Sunday 2026-04-19 Levin-Friston runaway (58+ WebSearch turns, no writes); (2) Tuesday 2026-04-21 Morning project status (still running at EOD); (3) Tuesday 2026-04-21 Morning system health (still running at EOD). If (2) and (3) terminate without writes overnight, the empirical case moves from one supporting event to three in four days.
  Category: Agent design / Scheduling / Invariants
  Status: Candidate — formalization blocked on (a) Tom's endorsement (Chat-side Claude endorsed this morning); (b) scheduler implementation of the turn-cap primitive; (c) resolution of the tension with ASSUMPTION-060 (read-only-only natural-termination precedent — turn-cap interruption replaces natural-termination). Promote to DECISION after the first interruption of a specialist task via the turn-cap mechanism produces a measurable cost saving and no false-positive interrupts across N=5 subsequent specialist runs. Related assumptions: ASSUMPTION-060, 062. Related presumptions: PRESUMPTION-054 (no turn-cap — this candidate directly addresses it), PRESUMPTION-063 (natural-termination-wins as default — this candidate would supersede it). Related open questions: OPEN-033 (parent question), OPEN-031 (cross-task coordination, which turn-cap partially mitigates).

DECISION-025 (candidate — Wright/Rohr addition + Stump metaphysical demotion):
  Date: 2026-04-26 (surfaced by today's design-project conversation in local_4e0f61e4 "Design project architecture and timeline")
  Title: Add Wright + Rohr as new C2A2 traditions and demote Stump on metaphysics in favor of Levin + Hoffman + Kastrup
  Summary: Two co-extensive structural changes to the C2A2 wiki proposed today by Tom in a derivative-project ("Summa 2026 in a Year") design session: (1) **Wright + Rohr addition** — N.T. Wright as scripture-scholarship ground truth (primary on Christology, divine law, Pauline faith, biblical justice, and last things); Richard Rohr as spirituality ground truth (primary on contemplative life and cosmic-Christ reframes of Tertia Pars). N=11 → N=13 if adopted. (2) **Stump metaphysical demotion** — for metaphysical loci, the synthesizer follows Levin + Hoffman + Kastrup (a "mind-everywhere monist convergence") rather than Stump. Stump remains the keystone for virtue, suffering, faith-as-knowledge, and the atonement. The two changes were made in a single user message (ASSUMPTION-063 + ASSUMPTION-064) and committed to a derivative-project bridges file (`/Users/tomloughran/Documents/Claude/Projects/Summa 2026 in a Year/vault/refs/Karpathy wiki bridges.md`); the C2A2 wiki itself under `Wiki/traditions/` was NOT modified today. Same-day specialist (Stump+Fredrickson, ASSUMPTION-067) produced a directly conflicting reading of Stump as supplying live metaphysics — surfaced in OPEN-037.
  Category: Architecture / Traditions registry
  Status: Candidate — formalization blocked on (a) resolving OPEN-036 (should the addition propagate to the C2A2 wiki itself, or remain a derivative-project convention?); (b) resolving OPEN-037 (how to reconcile the Stump-demoted vs. Stump-as-live-metaphysics tension produced same-day); (c) surfacing the eight presumptions beneath the proposed change (PRESUMPTION-070 decomposability, 071 Levin-Hoffman-Kastrup convergence-coherence, 072 Catholic synthesis frame appropriateness, 073 N→13 scaling, 074 specialist-recognized-convergence reliability, 076 canonical-works-fallback equivalence, 078 Stump+Fredrickson commensurability, 080 cross-discipline operational-primitive transfer); (d) Tom's explicit canonization decision after OPEN-036/037 are addressed. Promote to DECISION only after wiki-side traditions/wright/wiki.md and traditions/rohr/wiki.md exist (or are explicitly declined) AND Stump's metaphysical role is unambiguously stated in the wiki. Related assumptions: ASSUMPTION-063, 064, 067 (tension), 070, 005. Related presumptions: PRESUMPTION-070, 071, 072, 073, 074, 076, 078, 080. Related open questions: OPEN-036, OPEN-037.
