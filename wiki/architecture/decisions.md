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
  Status: Partial (commit script written; refactor scaffolding pending; Tom to run script locally)
