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

DECISION-026 (candidate — broker hosting platform):
  Date: 2026-05-13 (surfaced by 2026-05-13 dream-conversation session; recorded in Pathway 00 — Broker)
  Title: Broker hosting on Cloudflare Workers (conditional on streaming-latency validation)
  Summary: The C2A2 broker (Pathway 00) — single integration point for API-key holding, vault-scope enforcement, escalation gating, sensing aggregation, episode-publishing gate, and outreach gating — is hosted on Cloudflare Workers. The $5/mo paid plan gives 30 s CPU + unlimited requests; edge-distributed deployment puts brokerage close to users with ~10-30 ms broker-side overhead presumed dwarfed by LLM + TTS provider latency floors. Decision is conditional on a 30-minute streaming-latency validation test: round-trip a single 1-token Claude streaming call through a Worker stub from coffee-shop wifi and from the Notre Dame campus network; measure first-token latency. If under ~200 ms, decision is unconditional; if not, fall back to the AWS Lambda + ALB alternative noted in Pathway 00.
  Category: Architecture / Operational platform / Pathway 00
  Status: Candidate — formalization blocked on (a) streaming-latency validation test execution; (b) acknowledgment that PRESUMPTION-152 (10-30 ms edge overhead unverified pre-decision) is in force until measurement; (c) Tom's endorsement after the latency test. Promote to DECISION if the latency test shows first-token under ~200 ms across both network conditions. Related assumptions: ASSUMPTION-119 (17-pathway inventory), ASSUMPTION-120 (Cloudflare Workers hosting), ASSUMPTION-121 (Twilio SMS one-tap webhook co-location). Related presumptions: PRESUMPTION-152, PRESUMPTION-167 (broker-as-substrate hypothesis). Note: prior DECISION-026 candidate (Wright/Rohr addition per ASSUMPTION-111) has been renamed DECISION-026-WR (Wright/Rohr) pending reconciliation; OR the Wright/Rohr candidate may be re-issued at next available ID after DECISION-031.

DECISION-027 (candidate — phone confirmation mechanism):
  Date: 2026-05-13 (surfaced by 2026-05-13 dream-conversation session; recorded in Pathway 00 — Broker)
  Title: Twilio SMS one-tap signed link for external-escalation phone-confirmation gating
  Summary: External-escalation gating (the broker's gatekeeper role for outbound action — outreach, episode publishing, escalated sensing actions) uses a Twilio SMS one-tap signed link for phone-confirmation, NOT reply-keyword. Rationale: "no typing at the moment of approval." Webhook co-located on the same Cloudflare Worker as the broker (DECISION-026 candidate). Security depth (signed-link integrity, replay resistance, signing-key rotation) is implementation-detail to be specified; threat model is queued (PRESUMPTION-153). Alternative modalities (push-notification, email magic link, in-cowork-session confirmation, pre-authorized scope tokens) not considered (PRESUMPTION-154).
  Category: Architecture / UX / Operational platform / Pathway 00
  Status: Candidate — formalization blocked on (a) threat-model document for the one-tap surface (PRESUMPTION-153); (b) acknowledgment of unconsidered alternative modalities (PRESUMPTION-154); (c) Tom's endorsement. Note: this is a new DECISION-027; the prior DECISION-027 candidate (specialist self-attribution adjudication per ASSUMPTION-099) has been renamed DECISION-027-SA (Specialist Adjudication) pending reconciliation. Related assumptions: ASSUMPTION-121, ASSUMPTION-119, ASSUMPTION-120. Related presumptions: PRESUMPTION-153, PRESUMPTION-154.

DECISION-028 (candidate — Perspectives in vault as first-class wiki citizens):
  Date: 2026-05-13 (surfaced by 2026-05-13 dream-conversation session; recorded in Pathway 04 — Perspective Lattice)
  Title: Eager-tier perspective-lattice content lives in vault at `wiki/Perspectives/` with structure-group tag
  Summary: Eager-tier perspective-lattice content (Pathway 04) is stored in the C2A2 vault at `wiki/Perspectives/` with a Perspectives structure-group tag (Sociogram color TBD pending alignment with the existing structure-group palette). This makes perspectives first-class wiki citizens: Sociogram-retrievable, structure-group-filterable, and addressable by the voice agent during dialogue. Lazy-tier and fresh-tier content remain ephemeral / on-demand. Pre-implementation flag: the first-class-citizen machinery is presumed to generalize from thinker/PRS schema to perspectives without audit (PRESUMPTION-155).
  Category: Architecture / Content / Pathway 04
  Status: Candidate — formalization blocked on (a) Sociogram structure-group palette assignment for Perspectives; (b) machinery audit per PRESUMPTION-155 (which Sociogram features assume thinker/PRS schema vs. which are content-agnostic); (c) Tom's endorsement. Related assumptions: ASSUMPTION-122, ASSUMPTION-119. Related presumptions: PRESUMPTION-155.

DECISION-029 (candidate — whiteboard ephemerality + Pin-this + per-plot export):
  Date: 2026-05-13 (surfaced by 2026-05-13 dream-conversation session; recorded in Pathway 05 — Whiteboard)
  Title: Whiteboard plots ephemeral by default + Pin-this promotion to vault + per-plot export (PNG/SVG/HTML/CSV/PDF)
  Summary: Pathway 05 (quantification-on-demand whiteboard) treats plots as ephemeral by default: plots disappear after the session unless the user invokes "Pin this" to promote the plot to the vault. Each plot exposes export buttons for PNG / SVG / HTML / CSV / PDF. The opposite default ("persistent by default, swipe to discard") was not considered; the implicit user model is "user evaluates each plot in real time and acts on it" (PRESUMPTION-156).
  Category: Architecture / UX / Pathway 05
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-156 (real-time-recognition assumption may fail for derivative-realization use cases); (b) Tom's endorsement. Related assumptions: ASSUMPTION-123, ASSUMPTION-119. Related presumptions: PRESUMPTION-156.

DECISION-030 (candidate — generative-canvas library set):
  Date: 2026-05-13 (surfaced by 2026-05-13 dream-conversation session; recorded in Pathway 06 — Generative Canvas)
  Title: Generative-canvas library set = D3 + three.js + Plotly + bare canvas/WebGL
  Summary: Pathway 06 (generative-canvas visualization, code-writing agent producing custom visualization on request) uses a four-library catalog: D3 + three.js + Plotly + bare canvas/WebGL. The code-writing agent generates against this set; continuity-of-visualization-under-edits is a primary requirement. Alternatives — Observable Plot, deck.gl, regl, vega-lite, P5.js, Mapbox GL JS, ECharts — not considered (PRESUMPTION-157).
  Category: Architecture / Tooling / Pathway 06
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-157 (closed-enumeration without justification against omitted alternatives); (b) Tom's endorsement. Set is additive — additional libraries can be incorporated later as gaps emerge. Related assumptions: ASSUMPTION-124, ASSUMPTION-119. Related presumptions: PRESUMPTION-157.

DECISION-031 (candidate — unsaid-edges two-filter scoring with Low × High emphasis):
  Date: 2026-05-13 (surfaced by 2026-05-13 dream-conversation session; recorded in Pathway 07 — Unsaid Edges)
  Title: Unsaid-edges scoring uses how-often × how-important two-filter quadrant with Low × High visually emphasized as strongest research-program candidate
  Summary: Pathway 07 (unsaid-edges map, foregrounding empty edges in the perspective lattice as research-program-generating facts) scores each unsaid edge along two filters: how-often (frequency of mention across the corpus) and how-important (weight of mention when it occurs). Visualization emphasizes the Low × High quadrant (rarely mentioned but important when mentioned) as the strongest research-program candidate. This is a normative scoring commitment baked into the visualization (PRESUMPTION-158); the UI emphasis trains user attention toward this quadrant.
  Category: Architecture / Methodology / Pathway 07
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-158 (normative claim operationalized as UI emphasis without auditing alternative quadrant readings); (b) Tom's endorsement; (c) pilot of Low × High emphasis on N≥4 known research-program-seed edges from the existing CROSS register. Related assumptions: ASSUMPTION-125, ASSUMPTION-119. Related presumptions: PRESUMPTION-158.


DECISION-032 (candidate — toolkit / content separation as portability foundation):
  Date: 2026-05-14 (surfaced by 2026-05-14 morning walk + Cowork pathway-doc drafting; recorded in Pathway 18 — Portability and Toolkit Design)
  Title: Framework / content separation is non-optional; framework and content live in separate repos with config-driven instantiation
  Summary: Pathway 18 (portability toolkit) commits to a clean framework/content seam. The framework (broker, retrieval, agent ecosystem, visualization engine, governance protocols) lives in a separate `c2a2-framework` repo; the Carpathi vault becomes the reference instance. A `instance.yaml` configuration file drives substantive choices (thinkers, PRS axes, broker provider, ISME-equivalent target). No hardcoded references to Aquinas, Levin, MacIntyre, or any specific thinker in the framework layer. New adopters clone the framework + template-vault, configure their instance, and instantiate without touching framework code. Documentation carries the rationality standards (MacIntyrean tradition-constituted inquiry as system's normative shape) — adopting the framework without engaging the standards produces a different (and weaker) instance.
  Category: Architecture / Operational platform / Pathway 18
  Status: Candidate — formalization blocked on (a) line-by-line audit of current repo to identify the framework/content seam (called for in Pathway 18 Open Questions); (b) acknowledgment of PRESUMPTION-179 (dual-maintenance burden unaudited); (c) Tom's endorsement; (d) underlying ASSUMPTION-132 + ASSUMPTION-139 carrying Cowork-derived-subject-to-amendment status (PRESUMPTION-175). Related assumptions: ASSUMPTION-131, ASSUMPTION-132, ASSUMPTION-139. Related presumptions: PRESUMPTION-175, PRESUMPTION-179, PRESUMPTION-182.

DECISION-033 (candidate — federation default-off + file-based wire format + mandatory attribution):
  Date: 2026-05-14 (surfaced by 2026-05-14 morning walk + Cowork pathway-doc drafting; recorded in Pathway 19 — Optional Interoperability)
  Title: Federation defaults to off; primary wire format is signed JSON file-based handoff over HTTPS; cross-instance attribution is mandatory
  Summary: Pathway 19 (optional interoperability) commits to three load-bearing architectural decisions: (1) federation defaults to off — an instance that runs and never federates is fully legitimate; (2) the primary wire format is signed JSON file-based handoff over HTTPS (per PRESUMPTION-145 / ASSUMPTION-133), demoting persistent OAuth-token-mediated APIs; (3) cross-instance attribution is mandatory — peer material in local results always carries the peer's identity, honesty-layer markings, and source link. Selective sharing is per-topic, per-peer (not binary public/private). No canonical instance — Carpathi is not a master vault even after federation. The architectural commitment from Pathway 00 (broker as scope enforcer) extends to inter-instance queries: each request is a discrete, signed, scope-checked event.
  Category: Architecture / Operational platform / Pathway 19
  Status: Candidate — formalization blocked on (a) federation wire-format transfer-validity audit (OPEN-044); (b) acknowledgment of PRESUMPTION-170 (file-based handoff transfer from intra-user to inter-instance unaudited); (c) Tom's endorsement; (d) underlying ASSUMPTION-133 + ASSUMPTION-134 carrying Cowork-derived-subject-to-amendment status (PRESUMPTION-175). Related assumptions: ASSUMPTION-133, ASSUMPTION-134. Related presumptions: PRESUMPTION-170, PRESUMPTION-175.

DECISION-034 (candidate — meta-crafts as first-class traditions in perspective lattice):
  Date: 2026-05-14 (surfaced by 2026-05-14 morning walk + Cowork pathway-doc drafting; recorded in Pathway 24 — Meta-Crafts and Governance)
  Title: Meta-crafts (governance, project management, conflict resolution, facilitation, evaluation) are first-class traditions in the perspective lattice, not policy layers
  Summary: Pathway 24 commits meta-crafts to first-class tradition status: each meta-craft (governance, project management, conflict resolution, facilitation, evaluation, and others to be identified) is registered as a tradition in the perspective lattice (Pathway 04) with eager-tier overview, key thinkers, internal-debate map, apprenticeship trajectory, and PRS framing. Connective rendering in the Sociogram: visually distinct overlay with edges to every substantive tradition. Operational integration is non-optional — the system's own governance (DECISION canonization, PRESUMPTION escalation, federation peer admission, agent accountability) is itself a case of governance-as-meta-craft, held to the same standards. The boundary between meta-craft and substantive tradition is acknowledged as a boundary-case question (Open Questions section of Pathway 24); the architectural commitment is asserted prior to boundary resolution (PRESUMPTION-171).
  Category: Architecture / Methodology / Pathway 24
  Status: Candidate — formalization blocked on (a) boundary-case resolution for theology / political philosophy (PRESUMPTION-171); (b) Sociogram connective-overlay design prototype; (c) PRS framework specification for at least one meta-craft (governance); (d) Tom's endorsement; (e) underlying ASSUMPTION-135 carrying Cowork-derived-subject-to-amendment status (PRESUMPTION-175). Related assumptions: ASSUMPTION-135. Related presumptions: PRESUMPTION-171, PRESUMPTION-175, PRESUMPTION-181 (personhood-pin operational gravity extending into Pathway 24).

DECISION-035 (candidate — meta-visualization with agent as co-explorer, not oracle):
  Date: 2026-05-14 (surfaced by 2026-05-14 morning walk + Cowork pathway-doc drafting; recorded in Pathway 25 — Meta-Visualization of Pathways)
  Title: Pathway 25 meta-visualization commits the agent to co-explorer role (not oracle); annotation is co-authored; counterfactual integration is structural, not optional
  Summary: Pathway 25 (meta-visualization of pathways) commits to three architectural decisions: (1) the agent is a co-explorer, not an oracle — "query-response is the wrong mode"; the agent dwells, revises, surfaces considerations, draws on prior conversations via durable memory (Pathway 16) and continuity-of-character (Pathway 17); (2) annotation is co-authored — both user and agent annotate, with agent annotations carrying honesty-layer markings (Pathway 14) and user annotations carrying attribution; (3) counterfactual integration (Pathway 23) is structural, not optional — the user can mark counterfactual branch points in the pathway space and explore them. Pathway 25 is architecturally distinct from Pathway 13 (Under-Development Visualizer) — different audiences (intellectual co-explorers vs GitHub contributors), different data substrates (pathway dependency / annotation / counterfactual vs commits / PRs / contributors).
  Category: Architecture / UX / Methodology / Pathway 25
  Status: Candidate — formalization blocked on (a) user-modeling work to validate the agent-as-co-explorer-only commitment vs mode-toggling for oracle-mode users (PRESUMPTION-172); (b) recursive-self-application termination-condition audit for self-visualization (PRESUMPTION-174, OPEN-041 cluster); (c) Tom's endorsement; (d) underlying ASSUMPTION-136 + ASSUMPTION-137 carrying Cowork-derived-subject-to-amendment status (PRESUMPTION-175); (e) SELF-MEASUREMENT cluster compounding load across Pathways 23 + 24 + 25 (PRESUMPTION-180). Related assumptions: ASSUMPTION-136, ASSUMPTION-137. Related presumptions: PRESUMPTION-172, PRESUMPTION-174, PRESUMPTION-175, PRESUMPTION-180, PRESUMPTION-181.



DECISION-036 (candidate — sandboxed non-Claude LLM worker on shared C2A2 vault, Path 2 architecture):
  Date: 2026-05-17 (surfaced by 2026-05-16 Multi-agent Obsidian/DeepSeek Chat thread, recorded into the architecture register on 2026-05-17 by the resumed c2a2-self-awareness-daily run)
  Title: Multi-agent vault coordination uses Path 2 — DeepSeek-Flash via API + folder-scoped one-shot worker, scope-locked to `_agents/<provider>/`, with `agents.md` as the single-source-of-truth operating contract
  Summary: For adding any non-Claude LLM agent to the same Obsidian vault Claude agents operate on, the architecture is **Path 2** (chosen over Path 1 — in-Obsidian plugin + local Ollama, "not really agentic" — and Path 3 — MCP-capable third-party harness, "elegant but requires harness debugging while DeepSeek tool-call reliability lags reasoning"). Path 3 is worth doing after Path 2 is paying off, not before. Operating contract: `agents.md` imports Tom's 12 rules verbatim with a one-line analogy note ("code"→"notes", "codebase"→"vault", "tests"→"verification") plus vault-specific corollaries on Rules 5, 8, 9. Both Claude agents and the non-Claude worker read the same `agents.md` (MindStudio editable-control-plane analogy: single source of truth). Worker is scope-locked to `_agents/<provider>/` (inbox / outbox / done / failed); never writes to live vault content; promotion is a human-or-Claude review step. Output filenames Maildir-style: `{YYYYMMDD-HHMMSS}_{task}_{job-stem}.md`. Worker is one-shot, no daemon, no retry logic, fail-loud (~60 lines, C1–C5 PASS at 2026-05-16T20:49:13 UTC). Coordination primitives: MCP shared protocol, Git as universal undo / conflict layer, folder-scoped agent assignments (no scheduler / no lock manager — last-write-wins). Five hard prohibitions in `agents.md` (write outside scope; delete without confirmation; edit without read; silent conflict-merge; skip failure-logging) candidate for the C2A2 vault-safety-boundary cluster. Explicitly reinforces PREMISE-016 (toolkit/content separation). Classification: C2A2 infrastructure (reusable post-ISME), not pathway content.
  Category: Architecture / Infrastructure / Multi-agent coordination
  Status: Candidate — formalization blocked on (a) Tom's shake-out of `agents.md` + `worker.py` on the Mini against the real vault; (b) Tom's choice at the chat-thread terminus branch-point (draft promote-to-vault helper next vs pause-and-test); (c) reconciliation with any existing Mini-side `CLAUDE.md` (Tom to confirm naming convention `agents.md` vs `CLAUDE.md`); (d) acknowledgment of PRESUMPTION-183 (Maildir scaling beyond N=1 producer), PRESUMPTION-184 (12-rules transfer-validity for the 9 un-corollary'd rules), PRESUMPTION-185 (Claude-as-reviewer bottleneck), PRESUMPTION-189 (DeepSeek provider-trust under Pathway 19 governance); (e) Tom's endorsement. Related assumptions: ASSUMPTION-158, ASSUMPTION-159, ASSUMPTION-160, ASSUMPTION-161, ASSUMPTION-162, ASSUMPTION-163, ASSUMPTION-170. Related presumptions: PRESUMPTION-183, PRESUMPTION-184, PRESUMPTION-185, PRESUMPTION-189. Related: PREMISE-016 (reinforced), DECISION-032 (candidate, leans on same spirit).


DECISION-037 (candidate — Pathway 27 Universal Search & Ask, one-index-two-surfaces):
  Date: 2026-05-19 (surfaced by the debug-wiki-push session local_9dec9408; recorded in new architecture doc 27_universal_search_and_ask.md, status: drafted)
  Title: Adopt Pathway 27 (Universal Search & Ask) on a one-index-two-surfaces architecture; ship Search + canonical auto-hyperlinking before July 8, stage Ask after the broker + honesty layer
  Summary: Pathway 27 commits to a single `entity_index.json` driving three surfaces: (1) a client-side, deterministic Search box (cold-start entry); (2) render-time canonical auto-hyperlinking (lateral jumps), built from the same index; and (3) a broker-backed, honesty-layer-disciplined Ask box. The load-bearing claim is "search ≠ hyperlinks — both needed, different moments (cold-start vs. lateral jump), but driven by one index." ISME staging: Search + hyperlinking are broker-independent table-stakes and ship before July 8; Ask stages after Pathway 00 (broker) and Pathway 14 (honesty layer) land. Doc front-matter: status: drafted; depends_on [broker, perspective_lattice, honesty_layer]; enables [recursive_episode, apprentice_mode]; isme_critical: yes. Four open questions flagged in the draft: index freshness (with the explicit lesson from tonight's index_summary staleness + --summa recurrence), two-boxes-vs-toggle on mobile, hyperlink density rule, entity disambiguation. Pathway 27 is a new file, not yet listed in pathways.md (the draft deliberately left the index untouched pending Tom's one-line add).
  Category: Architecture / Retrieval / UX / Pathway 27
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-217 (one index serving cold-start search + lateral linking + broker-backed Ask without freshness/determinism/disambiguation conflict); (b) Tom's endorsement and the one-line pathways.md add; (c) resolution of OPEN-054 (demo-path vs pathway-expansion) — Search + hyperlinking are themselves ISME-critical so partly resolve into the demo path. Related assumptions: ASSUMPTION-197. Related presumptions: PRESUMPTION-217. Related: Pathway 00 (broker), Pathway 14 (honesty layer), Pathway 11 (recursive episode), Pathway 15 (apprentice mode).


DECISION-038 (candidate — adopt the Narrative (PRS) Connectome model as guiding frame):
  Date: 2026-05-20 (surfaced by the Review-PRS-triplet-visualization session local_a20a370b; recorded in new guiding document `architecture/narrative_prs_connectome.md`, status: architecturally guiding)
  Title: The "3D PRS" view is reframed as the Narrative (PRS) Connectome Explorer; the tool is answerable to a stated model (narrative connectome → emergence of a master science), with perspectives re-derived from the model and an author-contribution self-documentation convention
  Summary: Tom authored `narrative_prs_connectome.md` as an architecturally-guiding document: the connected unit is the agentic PRS narrative read as a complete model/compression; three connectomes share one architecture (neural, Hawkins/Thousand-Brains, narrative); synergistic coils are association fibers (ASSUMPTION-202); the telos is the emergence of a master science as architectonic/sapientia/tradition-craft, with rival master sciences meeting through coils as rivals-and-complements, never one convergent whole (ASSUMPTION-207). Three directives: (1) rename "3D PRS" → "Narrative (PRS) Connectome Explorer"; (2) re-derive the perspective set from the model, parity of richness with the Sociogram not parity of controls (ASSUMPTION-203, OPEN-058); (3) author-contribution convention — Tom's guiding docs live in both `architecture/` and `traditions/loughran/`, wikilinked into the connectome, so the system documents itself inside itself (ASSUMPTION-211). The view was renamed and the rebuild promoted to live the same day.
  Category: Architecture / Methodology / Conceptual frame / PRS visualization
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-221 (connectome-analogy transfer conditions), PRESUMPTION-223 (convergence-emphasis normative tilt), and PRESUMPTION-224 (guiding-doc acquires governing status outside the lit gate); (b) routing the document's own empirical claims (coils-as-fibers, compression, 3-hub convergence) through 15a/15b before the doc governs changes; (c) Tom's endorsement (Tom is the author, so endorsement is implicit for the frame, pending the presumption acknowledgments); (d) OPEN-061 (is this the ISME/FC26 paper spine or a parallel track?). Related assumptions: ASSUMPTION-201, ASSUMPTION-202, ASSUMPTION-203, ASSUMPTION-207, ASSUMPTION-208, ASSUMPTION-211. Related presumptions: PRESUMPTION-221, PRESUMPTION-222, PRESUMPTION-223, PRESUMPTION-224, PRESUMPTION-229. Related: Pathway 04 (perspective lattice), traditions/hawkins, traditions/macintyre, traditions/loughran.

DECISION-039 (candidate — coil altitude = discovery-time, "axis follows model"):
  Date: 2026-05-20 (surfaced by Review-PRS-triplet-visualization local_a20a370b; implemented as Phase 1 of the connectome rebuild)
  Title: A coil's vertical altitude encodes the discovery-time of its bridging insight (~2026 for nearly all current coils), not the age of the ideas it joins — the first concrete instance of "axis follows model"
  Summary: Phase 1 of the connectome rebuild moved coil altitude from each tradition's founding era to the ~2026 discovery-year band, on the model's principle that a coil sits where its bridging insight was formed (ASSUMPTION-204). This fixes the "no post-2020 coils / coils sink to founding era" surprise and is the first concrete test of the broader "axis follows model" discipline. The parallel node-axis decision is deliberately deferred (OPEN-057).
  Category: Architecture / Visualization semantics / PRS connectome
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-225 ("axis follows model" presumes a unique axis semantic where several may be defensible); (b) resolution of OPEN-057 (node vertical-axis semantics) so node and coil altitudes are coherent; (c) Tom's endorsement. Related assumptions: ASSUMPTION-204. Related presumptions: PRESUMPTION-225. Related: DECISION-038, OPEN-057.

DECISION-040 (candidate — convergence is analogical; coils, not shared resources, are the convergence instrument):
  Date: 2026-05-20 (surfaced by Review-PRS-triplet-visualization local_a20a370b; Phase-2 convergence-hub finding)
  Title: Cross-tradition convergence is treated as analogical, not verbatim — only 3 literal shared-resource hubs exist (max 2 traditions per resource), so the coil layer (association fibers) is the project's primary convergence instrument, and "convergence" is to be described accordingly in the ISME/FC26 framing
  Summary: Phase 2 made resources shared across ≥2 traditions glow gold and surfaced the empirical finding that only 3 literal cross-tradition hubs exist, none shared by more than 2 traditions (ASSUMPTION-205). The design stance adopted: traditions converge analogically rather than verbatim, so the coil layer — not literal shared resources — carries the real convergence signal, and the paper's account of convergence should reflect this.
  Category: Methodology / Empirical finding adopted as design stance / PRS connectome
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-228 (the 3-hub count may be a resource-naming/normalization artifact rather than the territory); (b) a normalization/fuzzy-match re-run of hub detection to confirm the count is stable; (c) Tom's endorsement; (d) reconciliation with how "convergence" is described in the FC26/ISME materials. Related assumptions: ASSUMPTION-205, ASSUMPTION-202. Related presumptions: PRESUMPTION-228, PRESUMPTION-223. Related: DECISION-038, lit-pipeline SYSTEMIC-RISK-FLAG A (ground-truth oscillation).

DECISION-041 (candidate — generative-coil detection lexical-first, semantic v2):
  Date: 2026-05-20 (surfaced by Review-PRS-triplet-visualization local_a20a370b; Phase-3 generative layer)
  Title: Generative coils (directed solution→resource handoffs) are detected lexical-first in v1 — 17 chains found — with semantic/embedding detection deferred to v2
  Summary: Phase 3 added 17 directed generative coils via lexical matching (ASSUMPTION-206), rendered live and verified to react to the year slider (15 of 17 chains have a 2026 endpoint). Semantic/embedding detection is explicitly a v2 follow-on (OPEN-059). Lexical-first is chosen for shippability now, accepting lower recall than an embedding approach.
  Category: Tooling / Methodology / PRS connectome generative layer
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-230 (the slider-reaction verification leaned on data-reasoning rather than reproduced on-screen observation); (b) a precision/recall comparison of lexical-v1 against the planned semantic v2 (OPEN-059); (c) Tom's endorsement. Related assumptions: ASSUMPTION-206. Related presumptions: PRESUMPTION-230. Related: DECISION-038, OPEN-059.

DECISION-042 (candidate — common interaction-behavior cluster across tabs + review-before-promote):
  Date: 2026-05-20 (surfaced by Review-PRS-triplet-visualization local_a20a370b; Sociogram interaction model ported to the Connectome)
  Title: Explorer tabs share a common interaction-behavior cluster (node→right panel; edge→collapse filters + two connected files; click-toggle + dismiss-on-new-click; "?" toggles), with uniform two-endpoint rendering for all edge types; UI bundles promote to live only after Tom's visual review of the review file, and the git push is reserved to Tom's host shell
  Summary: The Sociogram's two-panel + dismiss-on-new-click model was ported faithfully to the Connectome so the tabs feel identical (ASSUMPTION-209), with edges rendering the two endpoint narratives uniformly for all edge types under an edge-nature/year header — accepting representative-narrative imprecision for tradition-bridging coils/cross-links (ASSUMPTION-210). Process commitment reaffirmed this session: the biggest UI/layout changes are staged in `prs_3d_review.html`, promoted to live (`prs_3d.html`) only after Tom's visual review, and the git push remains a Tom-side host-shell step.
  Category: UX / Process / PRS connectome
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-226 (representative-narrative substitution may be over-read as idea-precise) and PRESUMPTION-227 (cross-tab uniformity may override 3D-native affordances — cf. the zoom/blank-space dismissal bug); (b) Tom's endorsement; (c) reconciliation with the standing commit-ownership question (OPEN-056) for the host-shell-push reservation. Related assumptions: ASSUMPTION-209, ASSUMPTION-210. Related presumptions: PRESUMPTION-226, PRESUMPTION-227. Related: DECISION-038, OPEN-056, Sociogram interaction model.

DECISION-043 (candidate — ship the connectome 2-panel bundle + execute the deferred push):
  Date: 2026-05-22 (surfaced by the Review-PRS-triplet-visualization session local_a20a370b)
  Title: Ship the Narrative (PRS) Connectome 2-panel interaction bundle to live and execute the push that was deferred from 2026-05-20 (catch-up commit `fc79739`)
  Summary: The connectome interaction bundle (two-panel edge-cluster view, "?" pop-ups, node click-to-toggle, edge-picking via Three.js raycast, brightness + "Year >=" sliders; ASSUMPTION-213) was validated against the release gate (graph data byte-identical to the approved file, `node --check` clean; ASSUMPTION-212), promoted to live (`prs_3d.html`), reviewed by Tom in the explorer, and pushed in commit `fc79739` — which finally carried the Narrative Connectome work deferred from 2026-05-20 to origin. With the bundle shipped, the connectome thread is treated as complete and handed off to the two-summa experiment (ASSUMPTION-219).
  Category: UX / Process / PRS connectome
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-231 (data+syntax+eyeball promotion may not equal reproduced interaction-behavior verification — re-instantiates PRESUMPTION-230/218); (b) Tom's endorsement (review already given). Related assumptions: ASSUMPTION-212, ASSUMPTION-213, ASSUMPTION-219. Related presumptions: PRESUMPTION-231. Related: DECISION-042, DECISION-038, OPEN-056 (commit-ownership; the 05-20 deferred push is now resolved).

DECISION-044 (candidate — run the two-summa head-to-head as Option #3 in a fresh chat):
  Date: 2026-05-22 (surfaced by Review-PRS-triplet-visualization local_a20a370b; handoff written to TWO_SUMMA_EXPERIMENT_BRIEF.md)
  Title: Run the two-summa experiment as Option #3 in a cold-start chat, handed off via a self-contained brief — Thomist summa vs. Conscious-Realist-Monist summa across the Aquinas<->Levin teleology seam
  Summary: With the connectome shipped, Tom chose Option #3 for the two-summa head-to-head and asked to run it in a fresh chat. A self-contained handoff (`TWO_SUMMA_EXPERIMENT_BRIEF.md`, project root) was written carrying project context, all paths, the PRS+tradition schema, the #3 design, the Aquinas<->Levin teleology seam with specific Summa source days, success criteria, and guardrails (Obsidian-clobber, no-blind-push, publish decisions). Premise: a Conscious-Realist-Monist summa can be built as a genuine rival and compared head-to-head (ASSUMPTION-215, 216); the experiment is portable via a single brief (ASSUMPTION-214).
  Category: Methodology / Experiment design / Traditions
  Status: Candidate — formalization blocked on (a) OPEN-062 (what exactly counts as "Summa 2" and what form the head-to-head output takes — the brief's first open item); (b) acknowledgment of PRESUMPTION-233 (commensurability of rival summae), PRESUMPTION-234 (Summa-2 exists/assemblable), PRESUMPTION-232 (cold-start handoff loses no load-bearing tacit context), PRESUMPTION-235 (focal-seam chosen without weighing alternatives); (c) Tom launching the chat. Related assumptions: ASSUMPTION-214, ASSUMPTION-215, ASSUMPTION-216. Related presumptions: PRESUMPTION-232, PRESUMPTION-233, PRESUMPTION-234, PRESUMPTION-235. Related: ASSUMPTION-207 (master-science telos), DECISION-038.

DECISION-045 (candidate — embed faculty research summaries in sociogram node data):
  Date: 2026-05-22 (surfaced by the Assess-wiki-visualization-build-requirements session local_26b6c078; separate KSGA-sociogram repo)
  Title: Embed the 307 "Principal research areas" faculty summaries directly in the KSGA sociogram's node data so node side-panels are self-contained
  Summary: The KSGA sociogram was regenerated against the current vault (500 nodes / 911 links; 475 wikilink + 436 affiliation; 93 gold-ring central+institute faculty), and the 307 faculty research summaries were embedded directly in the graph data and now render in the node side-panel (ASSUMPTION-217). `index.html` grew 1.3 -> 1.9 MB; `node --check` SYNTAX OK; only `index.html` changed (the explorer iframes it). This is a separate repo from the C2A2 wiki.
  Category: Architecture / Data model / Sociogram (separate repo)
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-236 (inline-embed self-containment benefit outweighs page-weight/scaling cost as the vault grows); (b) Tom-side close-out: the sandbox `git status` left a stale `.git/index.lock` — commit/push needs `rm -f .git/index.lock` first (push not yet at origin). Related assumptions: ASSUMPTION-217. Related presumptions: PRESUMPTION-236, PRESUMPTION-229 (scaling). Related: KSGA-sociogram repo, explorer iframe.

DECISION-046 (candidate — per-artifact repo publish/untrack calls + root .gitignore):
  Date: 2026-05-22 (surfaced by Review-PRS-triplet-visualization local_a20a370b; repo-hygiene pass)
  Title: Make explicit per-artifact publish/untrack calls and add a root `.gitignore` — eulogy IN, Archbishop report OUT, Habash transcripts IN, Hoffman x Levin raw transcript stop-tracked
  Summary: A repo-hygiene pass in the connectome session added a root `.gitignore` and made deliberate publish decisions per artifact (eulogy in, Archbishop report out, Habash transcripts in, Hoffman x Levin raw transcript stop-tracked); ASSUMPTION-218. The decisions are individually explicit; the governing criterion of "publishable vs. private" is tacit (PRESUMPTION-237).
  Category: Process / Repo governance
  Status: Candidate — formalization blocked on (a) acknowledgment of PRESUMPTION-237 (an unstated, stable publishability criterion is being applied); (b) Tom's endorsement. Related assumptions: ASSUMPTION-218. Related presumptions: PRESUMPTION-237. Related: DECISION-047 (parked history scrub of the stop-tracked transcript).

DECISION-047 (candidate — park, do not execute, the git-history scrub):
  Date: 2026-05-22 (surfaced by Review-PRS-triplet-visualization local_a20a370b)
  Title: Park (do not run inline) the git-history scrub of the Hoffman x Levin raw transcript plus four old narration zips — scope it, do not execute it this session
  Summary: A git-history scrub of the now-stop-tracked Hoffman x Levin transcript and four old narration zips was scoped and parked rather than executed. Stop-tracking removes the file going forward; the content remains in committed history until a scrub runs (PRESUMPTION-238 — the parked residual exposure is presumed acceptable in the interim, with no stated trigger for when "parked" becomes unacceptable).
  Category: Process / Repo governance / Risk
  Status: Candidate — formalization blocked on (a) OPEN-064 (execute or leave parked the history scrub); (b) acknowledgment of PRESUMPTION-238 (acceptable residual exposure while parked; success-criteria gap). Related assumptions: ASSUMPTION-218. Related presumptions: PRESUMPTION-238. Related: DECISION-046.


---

## 2026-05-23 status update (Agent 14a -- automated-pipeline day; no new numbered DECISIONs)

No interactive Tom session occurred 2026-05-23; no new DECISION candidates were generated. Today's lit-pipeline dispositions bear on two existing candidates:

- DECISION-044 (run the two-summa head-to-head) -- now GATED by today's HIGH-urgency lit flags REVISE-047 (ASSUMPTION-215) and REVISE-048 (PRESUMPTION-233), co-anchoring SYSTEMIC-RISK-FLAG H, both AWAITING-REVIEW. Do not launch until the comparability/refereeing objections are resolved: have an independent agent build/steelman Summa-2; pre-register losable criteria; use MacIntyre's tradition-internal epistemological-crisis test rather than a neutral scorecard. Also coupled to MONITOR-221/224/225.
- DECISION-047 (park the git-history scrub) -- now CHALLENGED by REVISE-049 (PRESUMPTION-238, MED, AWAITING-REVIEW): stop-tracking does not remove already-committed content. Recommended conversion to a hard pre-publicity trigger (filter-repo/BFG before any public step; repo stays private until then). See OPEN-064.

All three REVISEs are AWAITING-REVIEW; per PRESUMPTION-240 / OPEN-065 the review gate has been unavailable four days, so they are currently unactioned.

---

## 2026-05-24 status update (Agent 14a -- automated-pipeline day; no new numbered DECISIONs)

No interactive Tom session occurred 2026-05-24 (claude.ai signed out a 5th consecutive day; both daily syncs failed). No new numbered DECISION was generated. Today's automated activity (lit pipeline 15a/15b/15c; periodic monitor 15d; weekly sewing agent; 5 new proposals) moves existing candidates and surfaces decision-candidates that are not yet numbered:

- DECISION-044 (run the two-summa head-to-head) -- remains GATED by REVISE-047/048 (SYSTEMIC-RISK-FLAG H), still AWAITING-REVIEW. Unchanged this run.
- DECISION-047 (park the git-history scrub) -- remains CHALLENGED by REVISE-049, still AWAITING-REVIEW. Unchanged this run.
- NEW gating cluster: SYSTEMIC-RISK-FLAG I (REVISE-050 HIGH on PRESUMPTION-240; REVISE-051 MED-HIGH on PRESUMPTION-243) now gates the self-correction loop itself and the autonomous-agent accountability story. ASSUMPTION-221 (MONITOR-230) is INCORPORATE-pending-precondition: strong, live-verified literature support for locating accountability in the oversight/deployment layer, blocked from promotion to validated_premises.md until REVISE-050/051 resolve. REVISE-050 is partly self-fulfilling: deciding it *is* building the escalation that prevents the next silent stall. This flag answers OPEN-065.

Decision-candidates surfaced today (agent-recommended; awaiting Tom; not yet numbered):
- (A) Connectivity-metric definition: exclude `architecture/lit_search_results/` from the orphan/connectivity metric (ASSUMPTION-224; renewed sewing recommendation from 2026-05-18). Cheap, scriptable; see also PRESUMPTION-246 on the deeper metric-validity question.
- (B) One-time mechanical backlink-injection pass: from each tradition `wiki.md` to its own `prs_triplets.md` and to the bridge notes naming it (renewed from 2026-05-10/05-18). Scriptable, no model needed; would move connectivity more than several sewing runs.
- (C) Unit-promotion of the Wright + Rohr exile/restoration + Stump corporate-substance cluster as one paradigm-bridge (ASSUMPTION-222; sewing recommendation). Caveat per PRESUMPTION-244: confirm the convergence is tradition-level, not a pipeline/batch artifact, before hardening it as the "central theme."
- (D) Three STALE-MONITOR escalations (ASSUMPTION-035/037, PRESUMPTION-037): run the un-run empirical/paired test, or retire the premise -- a Tom decision, not a literature question (ASSUMPTION-223). Caveat per PRESUMPTION-245: these escalations terminate at the same human gate currently blocking the REVISE backlog.

All REVISE flags (047/048/049/050/051) are AWAITING-REVIEW; per PRESUMPTION-240/243 (now CHALLENGED/SUPPORTED) and OPEN-065/066 the review gate has been unavailable five days, so all are currently unactioned. A ~10-second re-login clears the immediate backlog.
