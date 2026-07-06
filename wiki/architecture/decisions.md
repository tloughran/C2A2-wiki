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


---

## 2026-05-26 status update (Agent 14a -- mixed-shape day: attended Cowork session + automated pipeline)

(Captured here on 2026-05-27; 2026-05-26's changelog covers the full daily narrative.)

- **DECISION-044** (run the two-summa head-to-head) -- still GATED by REVISE-047/048 (SYSTEMIC-RISK-FLAG H), still AWAITING-REVIEW. The review gate was OPEN for the first time in 6 days following the 10-second re-login (ASSUMPTION-235), but the attended session at 17:42 ET focused on the proposal-approval queue, not on REVISE actioning.
- **DECISION-047** (park the git-history scrub) -- still CHALLENGED by REVISE-049, still AWAITING-REVIEW.
- **SYSTEMIC-RISK-FLAG I** (REVISE-050/051 cluster) -- gate is OPEN; today's attended session demonstrated the loop can in fact close when Tom arrives. REVISE-050/051 still unactioned.
- **Candidate DECISION-048 (NEW 2026-05-26; AWAITING-TOM-NUMBERING):** "The review-page state (verified by direct paste + verbal confirmation) is the authoritative source-of-truth for proposal-approval values when the Gmail decision-email body disagrees; the email-body misfire is a UI/workflow bug to fix on the decision-email-generation side." From ASSUMPTION-230. Scope-extension flagged by PRESUMPTION-254: the rule may need to be "stated intent supersedes BOTH UI and email."

---

## 2026-05-27 status update (Agent 14a -- mixed-shape day: attended Cowork session on Supabase broker v4 + automated pipeline-disposition)

- **DECISION-044** (run the two-summa head-to-head) -- still GATED by REVISE-047/048 (SYSTEMIC-RISK-FLAG H), still AWAITING-REVIEW. **The review gate has been OPEN for 2 consecutive days now; the REVISE backlog has not been actioned in either attended session.** The backlog grew today by 5 new REVISEs (055-059).
- **DECISION-047** (park the git-history scrub) -- still CHALLENGED by REVISE-049, still AWAITING-REVIEW.
- **SYSTEMIC-RISK-FLAG I** (REVISE-050/051/056/058/059 cluster) -- the route-count grew today by REVISE-056 (3rd FLAG-I human-stall route: PRS-extraction backlog); the framing was extended by REVISE-058 (multi-failure-mode framing) and self-referenced by REVISE-059 (atomicity of registry-advance + artifact-write). The gate is OPEN but the backlog continues to grow. **REVISE-response is now a 13-item AWAITING-REVIEW backlog with 4 HIGH-urgency items (047/048/050/056).** REVISE-response is itself the 1st FLAG-I route; STALE-escalations the 2nd; PRS-extraction backlog the 3rd. (PRESUMPTION-265 asks whether route-count should be tracked as a process-fact, rate-of-new-routes-per-cycle, rather than as a bounded state-fact.)
- **Candidate DECISION-048** (review-page-as-authoritative) -- **carried from 2026-05-26; AWAITING-TOM-NUMBERING; scope-extended today** by ASSUMPTION-241 to cover "stated intent supersedes UI state when explicitly stated" (handling the 3-Wright case). Numbering still owed.
- **Candidate DECISION-049 (NEW 2026-05-27; AWAITING-TOM-NUMBERING):** "The Supabase broker v4 web_enrich architecture is a generic broker -- the `tab` field is analytics-only and does NOT gate behavior server-side; per-tab caps/templates/routing live on the client as payload + render adapters; Tavily top-5 results are injected into the system prompt as a `WEB_CONTEXT` block before the OpenRouter call; numeric `[n]` citation markers; separate web-counter columns with hard caps (20/device/day, $3/day global)." From ASSUMPTION-237/238/239. Tom signed off operationally ("broker live, seam shipped, research-tier caps in place, all verified end-to-end") but a numbered DECISION has not been filed.

Decision-candidates surfaced today (agent-recommended; awaiting Tom; not yet numbered):
- (E) The two free wins from 2026-05-26 are still owed: (i) exclude `architecture/lit_search_results/` from the connectivity/orphan metric (sewing agent re-flagged today: orphan count 766 → 1104 → 1409); (ii) one-time mechanical backlink-injection pass from each tradition `wiki.md` to its own `prs_triplets.md` and to bridge notes naming it.
- (F) **Truncation-bug remediation** -- the auto-send `type`-with-newlines path is a known broken path (ASSUMPTION-240/242; PRESUMPTION-262/263). Code-level fix vs documentation-only canonization is itself a decision candidate.
- (G) **Pipeline-integrity fail-loud check** (REVISE-059 recommendation) -- add an explicit check inside the 14a/14b pipeline that errors if a registry advances without a paired dated artifact, or vice versa. PRESUMPTION-264 records the architectural absence of this check before tonight's run.

All REVISE flags (047/048/049/050/051/052/053/054/055/056/057/058/059) are AWAITING-REVIEW. The 2026-05-22→26 6-day signout is over; the review gate has been OPEN for 2 consecutive days. The bottleneck is now confirmed (per ASSUMPTION-235) to be sit-down availability + attention-allocation within an attended session, not gate-availability.


---

## 2026-05-28 status update (Agent 14a -- mixed-shape day: multiple attended Cowork sessions on demo-path infrastructure + automated pipeline-disposition)

- **DECISION-044** (two-summa head-to-head): GATED by REVISE-047/048 (FLAG H); AWAITING-REVIEW. No attended-review-on-REVISE-backlog session today (3rd consecutive day OPEN-gate with no REVISE action).
- **DECISION-047** (park git-history scrub): CHALLENGED by REVISE-049; AWAITING-REVIEW. Standing reminder: scheduled c2a2 git-history scrub prep task fires tomorrow at 10 AM (per morning project status session).
- **Candidate DECISION-048** (review-page-as-authoritative; intent supersedes UI when explicitly stated): **carried from 2026-05-26; AWAITING-TOM-NUMBERING; 3rd cycle unnumbered.** Scope unchanged today (no Gmail-misfire incidents).
- **Candidate DECISION-049** (broker-v4 web_enrich architecture): **carried from 2026-05-27; AWAITING-TOM-NUMBERING; 2nd cycle unnumbered.** Today's AI-search wiring is the first demonstrated instance of the per-tab adapter pattern this candidate names (ASSUMPTION-243).
- **NEW today, un-numbered: AI-search-as-shared-module delegation pattern.** Per ASSUMPTION-243: per-tab consumers via `wiki/lib/c2a2-search.js`; broker action `enrich` routed server-side; `[database]` mode label as proof of routing. Demonstrated working in the Sociogram tab; 5-file changeset staged awaiting Tom's push sign-off (ASSUMPTION-244, ASSUMPTION-245). AWAITING-TOM-NUMBERING; 1st cycle.
- **SYSTEMIC-RISK-FLAG I** (human-stall family): route-count unchanged today (still 3: REVISE-response, STALE-escalations, PRS-extraction backlog), but the **4th-consecutive-cycle FLAG-I recursion** observed today (ASSUMPTION-250) is strong enough empirical evidence to ask the second-order framing question: is "wolfram canary" the right framing, or is demo-path infrastructure in fact the higher-leverage attended-session use given ISME ~5.5 weeks out? PRESUMPTION-267 surfaces a 4th-instance binary-framing pattern that may itself be load-bearing.
- **Three un-numbered DECISION candidates** (DECISION-048 3rd cycle; DECISION-049 2nd cycle; AI-search-delegation 1st cycle) now constitute a tracking blind spot of their own (ASSUMPTION-251; PRESUMPTION-271 surfaces whether DECISION-numbering itself is a hidden FLAG-I gate).
- **Two scheduling decisions** (NEW today, un-numbered): `connector-health-weekly` (Sun 06:19 local; first run 2026-05-31) and `reviewer-review-weekly` (Mon 06:37 local; first run 2026-06-01) registered against the swarm contract (ASSUMPTION-246, ASSUMPTION-247). Baseline-then-delta cadence pattern; real signal Week 2. PRESUMPTION-268 surfaces whether adding agents under FLAG-I conditions is net-positive.

Decision-candidates carried over (agent-recommended; awaiting Tom):
- (A) Connectivity-metric definition: exclude `architecture/lit_search_results/` from the orphan/connectivity metric (3rd cycle renewed; orphan count 766 → 1104 → 1409 today carries forward).
- (B) One-time mechanical backlink-injection pass from each tradition `wiki.md` to its own `prs_triplets.md` and to bridge notes (3rd cycle renewed).
- (C) Unit-promotion of the Wright + Rohr + Stump exile/restoration cluster (ASSUMPTION-222; REVISE-052 caveat per PRESUMPTION-244).
- (D) Three STALE-MONITOR escalations (ASSUMPTION-035/037, PRESUMPTION-037): run-or-retire decision still owed.
- (E) Truncation-bug remediation (ASSUMPTION-240/242; PRESUMPTION-262/263) -- carried; tonight's evening sync is the next test instance per ASSUMPTION-240 framing.
- (F) Pipeline-integrity fail-loud check (REVISE-059 recommendation) -- carried; ASSUMPTION-252 makes tonight's run itself the live atomicity test.
- (G) **NEW today**: Number the three un-numbered DECISION candidates (048/049/AI-search-delegation) in the next attended session; ASSUMPTION-251 names the accumulation as a tracking blind spot.

All REVISE flags (047-064 inclusive after today's 15c dispositions of yesterday's batch) remain AWAITING-REVIEW. The bottleneck remains (per ASSUMPTION-235) sit-down availability + attention-allocation within an attended session; today's multiple attended sessions did not action the REVISE backlog.


---

## 2026-05-29 status update (Agent 14a -- demo-path day: Sociogram navigation increments + Pathway 28 pinned; no attended-review session)

- **DECISION-044** (two-summa head-to-head): GATED by REVISE-047/048; AWAITING-REVIEW. No attended-review-on-REVISE-backlog session today (4th consecutive day OPEN-gate with no REVISE action).
- **DECISION-047** (park git-history scrub): CHALLENGED by REVISE-049; AWAITING-REVIEW. (The scheduled c2a2 git-history scrub prep task ran today; outcome not registry-moving for this pass.)
- **Candidate DECISION-048** (review-page-as-authoritative; intent supersedes UI): **carried; AWAITING-TOM-NUMBERING; 4th cycle unnumbered.** No change today.
- **Candidate DECISION-049** (broker-v4 web_enrich architecture): **carried; AWAITING-TOM-NUMBERING; 3rd cycle unnumbered.** No change today.
- **Candidate AI-search-as-shared-module delegation pattern**: **carried; AWAITING-TOM-NUMBERING; 2nd cycle unnumbered.** No change today.
- **NEW today, un-numbered: Sociogram interaction-model decision** (ASSUMPTION-256). Tom locked it verbatim ("leave the current model"): search/`focus:` is a transient highlight-in-place lens; the filter checkboxes are hard filters; the two do not sync. This is more firmly settled than the other candidates (explicit Tom lock-in), yet still un-numbered. AWAITING-TOM-NUMBERING; 1st cycle. PRESUMPTION-284 surfaces that the alternative (search drives visibility) was dismissed by preference rather than usability evidence.
- **NEW today, un-numbered: Sociogram v1.6 deliberate hold** (ASSUMPTION-255). 1.6 parser coded + logic-validated 16/16 but not pushed / not regenerated into the live file, because 1.6's isolate/link share the opacity mechanism of the now-confirmed focus-fade bug (ASSUMPTION-253/254). A release-gating decision; AWAITING-TOM-NUMBERING is not required (it is a hold, not a commitment), but recorded for traceability.
- **NEW today, un-numbered: MAX_EDGES=30000 retained** (ASSUMPTION-257). The recent crash was diagnosed as pure memory pressure, not an edge-cap issue; the cap stays. Settled by Tom in-session.
- **Pathway 28 -- Single-Source Participant Registration** (ASSUMPTION-259/260): pinned as an architectural *principle* (not a numbered DECISION), the registration-side twin of Pathway 27's retrieval-side entity index. One Rule-12 (fail-loud) gap flagged: `get_group()` silently falls back to `'root'` for a directory present on disk but absent from `COLORS`; recommended fix is to fail loud.
- **Session-handoff rail** (ASSUMPTION-261; NEW): gitignored `handoffs/sociogram-navigation.md` + a "read the handoff doc first on resume" rule in the project `CLAUDE.md`. Framed self-referentially as Pathway 16 (durable memory) in miniature.
- **SYSTEMIC-RISK-FLAG I** (human-stall family): route-count unchanged today (still 3). The FLAG-I recursion reaches its **5th consecutive attended-session cycle** with zero PRS extraction (continuing ASSUMPTION-250's lineage); the second-order framing question is owed a concrete REVISE-056 downgrade-or-commit decision rather than another diagnosis cycle. PRESUMPTION-286 surfaces the closed-loop self-diagnosis bias re-instantiating at the prioritization layer.
- **Un-numbered DECISION accumulation**: now **four** un-numbered candidates (048/049/AI-search-delegation/Sociogram-interaction-model). ASSUMPTION-251's tracking-blind-spot framing strengthens; numbering remains the fastest blind-spot to close in an attended session.

Decision-candidates carried over (agent-recommended; awaiting Tom):
- (A) Connectivity-metric definition: exclude `architecture/lit_search_results/` from the orphan/connectivity metric (renewed; carried).
- (B) One-time mechanical backlink-injection pass (carried).
- (C) Unit-promotion of the Wright + Rohr + Stump exile/restoration cluster (carried).
- (D) Three STALE-MONITOR escalations: run-or-retire decision still owed (carried).
- (E) Truncation-bug remediation (ASSUMPTION-240/242; PRESUMPTION-263 HIGH self-referential via REVISE-063) -- carried; no code-level fix today; tonight's evening sync did not deliver (browser logged out of claude.ai).
- (F) Pipeline-integrity fail-loud check (REVISE-059 recommendation) -- carried; REVISE-059 atomicity streak advanced to N=7/N=6 (both 2026-05-28 artifacts wrote cleanly).
- (G) Rule-12 fail-loud fix for `get_group()` (NEW today; from Pathway 28): make it error on a tradition present on disk but absent from `COLORS`.
- (H) Number the four un-numbered DECISION candidates in the next attended session (ASSUMPTION-251).

All REVISE flags remain AWAITING-REVIEW. The bottleneck remains (per ASSUMPTION-235) sit-down availability + attention-allocation; today's demo-path sessions did not action the REVISE backlog.

---

DECISION-050:
  Date: 2026-06-05 (attended; ratified by Tom)
  Title: Community Explorer relationship architecture — P1 now, P3 as target
  Decision: Adopt Pathway P1 (federated sub-tabs + shared services) as the near-term Community Explorer architecture, and declare Pathway P3 (one app, two projections, unified data model, quality-gate promotion pipeline) the target architecture. The promotion pipeline — Q2 quality crossing as the membrane between the 855-record directory and the curated graph — is named as the actual integration work, to be designed as its own increment.
  Status: P1 in build (search box + shared Ask-AI pipeline shipped to the feature branch, awaiting commit sign-off); P3 deferred / target.
  Rationale: P1 is cheap, ISME-safe, and its pieces (shared `c2a2-search.js` pipeline) are load-bearing in P3 later. P4 (keep only one) rejected — graph and cards are "two verbs over one dataset" (ASSUMPTION-275).
  Correction folded in: the P1 cross-navigation hand-offs ("shared `community_id`") were DEFERRED this session — curated (CC-001…, 156) and directory (C0001…, 855) ids are disjoint (0 id / 3 name / 5 host matches; ASSUMPTION-277). The join is reassigned to the P3 promotion pipeline. P1 therefore shipped as search + shared Ask-AI only.
  Carried locks honored: search = highlight lens never filter (2026-05-29); community graph stays disconnected from the sociogram; subtype filters dropped (140 subtypes / 156 nodes — badge, not checkbox).
  Related: ASSUMPTION-273/274/275/276/277; PRESUMPTION-306..311; OPEN-075
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the 2026-06-05 attended P1 build session and the ratified "DECIDED 2026-06-05 (Tom): P1 now; P3 is the someday target" line in sociogram_feature_review.md.
    Current status: ADOPTED (P1); TARGET (P3)

---

DECISION-051:
  Date: 2026-06-06 (attended; realized by the CE P1 build session, governed by DECISION-050)
  Title: Graph becomes a literal id-subset of Cards; in-product consent/provenance disclosure
  Decision: Merge the 156 curated communities into the Cards directory under their own `CC-xxx` ids (scripts/generate_community_cards_data.py; cards now 1006 after deduping 5 bulk overlaps), making the graph a literal id-subset of the cards — the first concrete realization of the directory⊇graph relationship and the step that makes P1 forward-compatible with the P3 promotion pipeline. Couple this with an explicit consent/provenance disclosure: the "?" popover and a new source-of-truth doc (explorer_tabs_complementarity.md) state that records are seeded from public web pages without express consent and that no community has approved its record.
  Status: REALIZED in code on `feature/sociogram-search-integration` (commits 56da6ab → 64c64bc → 8830d35); push + feature→main merge are attended-only (sandbox cannot push). The graph↔cards cross-navigation hand-off is now mechanically possible on the shared key; its UI is a future increment.
  Rationale: Resolves two falsehoods Tom flagged in the popover — (1) records were implied as approved (now disclosed as unapproved public seeds); (2) the graphed set was not a subset of the carded set (now it is). Directly addresses the 2026-06-05 disjoint-id finding (ASSUMPTION-277) by building the join rather than only deferring it.
  Carried locks honored: search = highlight lens never filter (2026-05-29 LOCK); community graph stays disconnected from the sociogram.
  Related: ASSUMPTION-278/279/280/281/282; ASSUMPTION-277 (superseded cross-nav-deferral by building the join); PRESUMPTION-312/313/314/315/316; OPEN-075 (partial answer), OPEN-076 (new)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the 2026-06-06 attended CE build session, the 2026-06-06 cowork_to_chat summary, the new explorer_tabs_complementarity.md, and the sociogram_feature_review.md 2026-06-06 UPDATE. This is an execution/realization decision under the umbrella of DECISION-050, numbered because it makes a substantive, dated design commitment (subset-merge + consent disclosure). Git state (3 commits on the feature branch) recorded as reported context — the repo is not introspectable from this mount.
    Current status: ADOPTED (realized in code; merge to main pending attended push)

---

DECISION-052:
  Date: 2026-06-07 (attended; realized in the PRS-connectome session)
  Title: PRS-connectome weekly task is git-free; regeneration automated, publishing handed off
  Decision: Redesign the `c2a2-prs-connectome-weekly` scheduled task (Sundays ~07:39) to be git-free: it regenerates `prs_3d.html` from committed/approved PRS data, validates it, writes it in place, and notifies Tom with a one-line "ready to publish — run this" note carrying the current triplet count. All git/worktree/`$HOME`/push logic is removed; publishing stays a manual push Tom runs on his Mac. Established design pattern: automate everything the sandbox can do (regenerate, validate, write, notify) and stop exactly at the capability wall (push, `.git` mutation, credentialed ops).
  Status: REALIZED — script `scripts/regen_prs_connectome.sh` rewritten and tested end-to-end in the sandbox (passes); the scheduled task updated to match. The day's 231 → 269 backlog was published to `origin/main` (commit 2f6356b) via an attended detached-worktree push; live connectome confirmed at 269.
  Rationale: The original auto-push design rested on a falsified premise — that scheduled tasks run on Tom's Mac with credentials and `$HOME` (ASSUMPTION-285 corrects this; PRESUMPTION-317 names the blind spot). The trial run could not push, could not resolve `$HOME`, and left stale `.git` lock cruft. Git-free is the only shape that runs reliably in the task sandbox, and it aligns with the repo's existing reality (nothing in the sandbox can push) and Tom's no-blind-push rule (ASSUMPTION-286: the policy rule coincides with a hard capability wall).
  Carried context (resolved in-session): two paste-run command blocks half-failed (a locked stale worktree holding `main`; an accidental commit on `feature/sociogram-search-integration` that bundled `generate_community_explorer.py`); both were recovered — 269 pushed via a state-independent detached worktree, and Tom ran `git reset --soft HEAD~1` to lift the stray commit ("Reset also done").
  Related: ASSUMPTION-283/284/285/286; PRESUMPTION-317/318/319/320/321; OPEN-077 (audit other scheduled tasks for the same capability mismatch)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the 2026-06-07 attended PRS-connectome session (read via session_info) and corroborated by the on-disk artifacts (`c2a2-prs-3d/prs_3d.PRE-regen-20260607_202243.bak.html`; the updated weekly task). A substantive, dated design commitment (git-free task + the "stop at the capability wall" pattern). The push landing on origin/main (2f6356b, 269) is taken from the session's pasted git output — reported context; the repo is not introspectable from this mount.
    Current status: ADOPTED (realized in code and in the live viz; weekly task updated)

---

DECISION-053:
  Date: 2026-06-08 (attended; realized in code across 4 sessions)
  Title: Agent Explorer re-based on OpenStory telemetry — 3-subtab structure, DB→vault-JSON→injected-HTML pipeline, ship 1+3 now / sociogram next
  Decision: Integrate OpenStory's observed agent telemetry into the C2A2 Agent Explorer (`agents_tab.html`, subtab 3c of the community explorer). Specific commitments locked this day:
    (1) Architecture: extract from the OpenStory SQLite DB (read-only, `mode=ro`) → write a per-agent telemetry JSON into the vault (`agents/openstory/agent_telemetry.json`) → inject it into `agents_tab.html` between `/* TELEMETRY_DATA_START/END */` markers → the HTML reads the embedded JSON. Decoupled from the running `serve`; graceful fallback to authored narration if data is absent. (file:// cannot fetch a sibling JSON — inject per house rule.)
    (2) Identity join: agents are keyed by the scheduled-task `name=` in `sessions.label` == scheduler taskId == roster key in `agent_map.json` (the single source of truth, 34 agents); truncated labels resolved by deterministic unique-prefix match (ASSUMPTION-289, GROUNDED).
    (3) Capture: solve the Cowork-vs-`~/.claude/projects` capture gap with an external symlink bridge (`scripts/openstory-bridge.sh`), NOT an OpenStory fork, so Tom keeps syncing upstream (ASSUMPTION-290). Bounded 72h ingest window keeps restart cost constant; NATS `max_payload` raised 8→64 MB for multi-MB Cowork events.
    (4) UI: evolve `agents_tab.html` into a 3-subtab Agent Explorer — Schedule (telemetry-enriched animation), Sociogram (shared-wiki-node edges), Explorer (sortable/filterable interrogative table). Ship subtabs 1+3 now; build subtab 2 (sociogram) fresh in a future session ("caution over speed"); sociogram pane shipped as an intentional placeholder.
  Status: PARTIALLY REALIZED — subtab switcher + telemetry-enriched Schedule (subtab 1) + interrogative Explorer (subtab 3) landed in `agents_tab.html`; extractor/injector/roster-sync scripts written and run; all static validation green (`node --check` + `validate_html.py`). NOT yet done: subtab 2 (sociogram), Phase-B reseed (#8), scheduled re-extract (#7), and a browser visual-render check (deferred — see PRESUMPTION-324). Committed/pushed on `feature/sociogram-search-integration` (feature files only).
  Rationale: The Agent Explorer was authored-narration; observed telemetry is a truer self-representation of the agent swarm (ASSUMPTION-287). Routing through the OpenStory DB rather than raw transcripts preserves eval/apply + turns (ASSUMPTION-288). Building on the existing 571-session DB rather than reseeding first avoids re-perturbing the running instance (ASSUMPTION-292), after HANDOFF-2's reseed attempt caused a NATS max-payload outage.
  Related: ASSUMPTION-287/288/289/290/291/292; PRESUMPTION-322/323/324/325/326/327; OPEN-078; DECISION-050/051 (community explorer); the `feature/sociogram-search-integration` branch (carries from 06-06/06-07)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the four 2026-06-08 attended OpenStory sessions via their handoff notes (`HANDOFF_openstory_{c2a2,session2,session3,session4}.md`) and the artifacts they describe (`extract_openstory_agent_data.py`, `inject_telemetry.py`, `sync_roster.py`, `agent_telemetry.json`, `agent_map.json`, `agents_tab.html`). A substantive, dated, multi-part design commitment realized in code. Git push state taken from the handoff notes — reported context; the repo is not introspectable from this mount.
    Current status: ADOPTED (subtabs 1+3 realized in code; sociogram + Phase-B + visual verification pending)

## 2026-06-09 status update (Agent 14a — heavily attended day: dyad-MMA charter ratified; ISME 2026 plan shipped; DECISION-053 subtab-2 advanced and browser-verified)

- **NEW: DECISION-054** (below) — the Prototype Measurement Charter v1 (dyad-MMA). NOTE / CORRECTION: today's cowork-to-chat summary recorded "No new DECISION today"; this pass overrides that on quoted evidence — Tom: "Let's articulate the dyad-MMA decision and the individuation principle as version 1, ever revisable as version N+1 will be for all N." A versioned, Tom-ratified measurement-architecture commitment is a decision.
- **DECISION-053** (Agent Explorer on OpenStory telemetry): ADVANCED. Subtab 2 (sociogram) — the deferred half — was built across two attended sessions: de-BOSCO of the email agent in all four locations (roster → 33 agents, telemetry re-injected, "Collaboration History" reframe), `extract_agent_node_refs.py` + `agent_node_edges.json` prepared, generator surgery (agents group, three layer toggles, shown/pass/total indicator restored), `wiki_narration.html` regenerated, and a real browser verify on the served copy (2400 nodes, 62,153 links, 26 agent actors; `#agents` preset: 228 = 183 projected + 45 flow, substrate pruned to 0). The PRESUMPTION-324 visual-render deferral is thereby partially discharged (see PRESUMPTION-328 for the residual file://-equivalence premise). Remaining: iframe + `applyAgentSociogramPreset()` wiring; commit/push attended-only.
- **ISME 2026 talk plan + over-deliver portfolio** (un-numbered): shipped with corrections ledger (April 1 genesis; Day-N = Habash Summa-in-a-year cadence; C2A2 expansion conflict flagged) and week-by-week schedule to July 8; handoff at `handoffs/isme-2026-talk.md`. Tom granted standing license for the portfolio increments "subject to constitutional rules," monitoring in dispatch mode. Carried as a plan, not a numbered DECISION. (ASSUMPTION-298/300; PRESUMPTION-331/332.)
- Sync channel: claude.ai logged out — 7th consecutive day; both directions failed again (morning scrape at /login; evening delivery undelivered, summary .md is the deliverable).

DECISION-054:
  Date: 2026-06-09 (attended)
  Title: Prototype Measurement Charter v1 — the recorded Tom⇄Claude dyad as the pilot MMA unit
  Decision: Adopt, as version 1 (ever revisable, N+1 for all N):
    (1) The pilot MMA unit is the recorded Tom⇄Claude dyad — the smallest cohort with non-trivial formational independence; evidential weight of any MMA scales with the formational independence of its members (Tom–Claude > Claude–Claude′; human pair > Tom–Claude).
    (2) The tradition measured is Tom's integrative perspective ("what it is to think like me, having learned from them"), with Tom as MM-of-1 per the framework's own constitution clause; every instrument's validity is scoped to "second-language competence in Tom's perspective."
    (3) Context is the agent's principle of individuation (materia signata): the individuating context — constitution + seeds + memory state + model — is recorded as the "who" of any agent participation. (Quietly expands OpenStory's "who".)
    (4) The agent must be structurally able to fail/withhold; logged disagreements are first-class evidence, recorded not smoothed.
    (5) Disagreement-closure protocol: table within one manageable session → exhaust all candidates proposed by either member → revisit tabled/marked items → only then close the MMA-capture.
    (6) Caveat carried front-and-center: neither member is ever a *simple* N=1 — that is one projection, never the only one.
    (7) First Level-3 data = whatever the dyad ratifies (or fails to ratify) in the next triplet pass; not gated on Mac backfill or recruited cohort.
  Status: ADOPTED (Charter v1 written; measurement handoff set). Next: task one — Tom's two ladder tools (UG physics; core-doc subset of the fifteen) as scaffolds of candidate PRS-elements; first triplet pass, iterating the pass design. Resume cue: "resume the measurement prototype."
  Rationale: Dissolves the Mac-gating and cohort-gating the master measurement plan assumed; converts the AI-membership question from thesis to empirical question the detector adjudicates; Tom's Rules 1/12 become the methodological safeguard keeping the unit valid.
  Related: ASSUMPTION-293/294/295/296/297; PRESUMPTION-330/333; OPEN-079; DECISION-053 (the "who" expansion); `architecture/master_measurement_plan.md`
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the measurement-framework session transcript and Charter v1; overrode the same-day summary's "no new DECISION" read on quoted evidence.
    Current status: ADOPTED (v1)

## 2026-06-10 status update (Agent 14a — four attended fronts: sociogram counter forensics → budgeted-render ratification; measurement task-one delivered; education-tab fixes verified; Pathway 29 Metabolism shipped live)

- **NEW: DECISION-055** (below) — budgeted-edge DOM rendering, Tom-ratified in-session after he caught the contradictory edge counters.
- **NEW: DECISION-056** (below) — Pathway 29 Agent Metabolism view adopted as a permanent Explorer sub-tab and pushed to the public GitHub Pages site.
- **DECISION-053** (Agent Explorer on OpenStory telemetry): ADVANCED again — all four verification checks passed on the served copy (preset, master-view defaults, group labels, `agents_tab.html` lazy-iframe wiring), closing the "iframe wiring" remainder. Three Tom observations then opened real findings: the time-slider date-cut bug (ASSUMPTION-303), the Summa zero-substrate fact (PRESUMPTION-336), and the H-Admin-centrality-lives-in-hidden-substrate design consequence (→ OPEN-080, parked on an open question to Tom at day end).
- **DECISION-054** (dyad-MMA charter): task one DELIVERED — Tom embedded the two ladder tools as Physics Explorer and RC Document Explorer in the Community Education Tab and re-uploaded the ISME 2026 paper (ASSUMPTION-304); session parked at the review→authoring-pass question.
- **Education-tab fix tally** (un-numbered, carried for the pending two-file commit): caption bleed, return navigation, 28 PhET URL fixes, and the Back-button history cure (ASSUMPTION-305 GROUNDED / ASSUMPTION-306); session parked at the wrap/commit question.
- Sync channel: morning Chat→Cowork scrape failed at /login (8th consecutive day) but the **evening Cowork→Chat delivery SUCCEEDED — first delivery in 8 days** (session restored unexplained; PRESUMPTION-338).

DECISION-055:
  Date: 2026-06-10 (attended)
  Title: Budgeted-edge DOM rendering — retire the legacy MAX_EDGES hidden-DOM layer in `wiki_narration.html`
  Decision: Render only the budgeted edges into the DOM, so the graph never holds the ~30k hidden `<line>` elements the legacy `MAX_EDGES = 30000` cap produced between "total" and "shown." Companion label fixes regardless of refactor: `graph-status` reports nodes only; `edge-status` is the sole edge readout; `pass` becomes the true pre-cap passing count (~60,078 at master defaults, not the post-slice 30000). Folded in: exempt the agent-activity group from the date cut (actors are cumulative telemetry — ASSUMPTION-303).
  Status: ADOPTED; refactor IN PROGRESS — paused mid-design (dependency read of `nodeById` done) to triage Tom's three observations, then parked on the substrate-visibility design call (OPEN-080).
  Rationale: Tom's counter forensics exposed both "30000"s as artifacts of the DOM cap (a labeling bug plus a not-true-pass count), and the synchronous 30k-element build is the diagnosed cause of the heavy-toggle renderer stall (ASSUMPTION-302). Same legacy limiter Tom had already flagged: "let total grow, cap only visually."
  Related: ASSUMPTION-301/302/303; PRESUMPTION-334/335; DECISION-053; OPEN-080
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the sociogram session — Tom picked "the architectural fix" from an explicit in-session question; quoted diagnostic evidence retained.
    Current status: ADOPTED (refactor in progress)

DECISION-056:
  Date: 2026-06-10 (attended)
  Title: Pathway 29 — Agent Metabolism view adopted as permanent Explorer sub-tab and published live
  Decision: Adopt the Agent Metabolism visualization (Pathway 29, `29_agentic_metabolism.md`) as a permanent sub-tab of the Explorer shell and publish it: design doc + standalone prototype generator + three-view visualization (raster, system-pulse waveform, returned-vs-sent) with a live git-derived yield axis; clean 7-file commit (`3080a23`) pushed to `main` and verified on the public GitHub Pages site (`tloughran.github.io/C2A2-wiki`) and locally, zero console errors.
  Status: ADOPTED & SHIPPED. Open handoffs framed to the OpenStory thread: PRS-triplet completion as the next yield dimension; deterministic scheduler before any bandit layer (ASSUMPTION-308); progress/peace KPI distinction (ASSUMPTION-309).
  Rationale: OpenStory's DB was verified in-session to carry full per-session token usage, making the cost side of a metabolism (tokens in / artifacts out) measurable now; git history supplies a live yield proxy today (ASSUMPTION-307) ahead of PRS-completion integration.
  Related: ASSUMPTION-307/308/309; PRESUMPTION-337/339; DECISION-053 (telemetry substrate); `architecture/29_agentic_metabolism.md`; `architecture/pathways.md`
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the metabolism session transcript — an attended, scoped, public-site-verified ship of a numbered pathway. Push state quoted from the session's own verification (commit hash + live-site check); repo not introspectable from this mount.
    Current status: ADOPTED & SHIPPED

## 2026-06-11 status update (Agent 14a — measurement rounds 1–2, sociogram ship, commentary explorer, pipeline backlog drain)

- **No new DECISION-NNN today** (max remains DECISION-056). The day was execution and dispositions. NOTE (Rule-7 flag): the evening cowork-to-chat summary stated "max remains DECISION-054" and "max remains OPEN-079"; the registries are authoritative (DECISION-056, OPEN-081 before today) — the summary's maxes are stale.
- **DECISION-054** (dyad-MMA charter): ADVANCED substantially — **round 1 CLOSED 6/6 agreed, the system's first completed Level-3 MMA capture.** M1–M4 unqualified; M5 agreed scoped (weaker reading: CRm as correctly articulated, not fully resolved) with Tom's narrative-individuation comment recorded verbatim (ASSUMPTION-310); M6 agreed as claim (a), retitled "candidate home," with Tom's methodological-Thomism comment verbatim (ASSUMPTION-312). **Round 2 OPENED:** M7 (narrative individuation) and M8 (methodological Thomism, falsifiers + riders in R) at pending-dyad with the agent member's assents and separately-logged reasons (ASSUMPTION-315 dual-reasons rule, binding from round 2). Physics ladder deferred as next seed. Mid-round correction: Stump false-attribution traced to a name-proximity heuristic — the failure ASSUMPTION-076/PRESUMPTION-089 predicted — fixed at four layers incl. a durable memory; no live attribution survives.
- **DECISION-053/055** (sociogram stack): SHIPPED & PUSHED — commit 2f941aa (six files): budgeted-edge rendering (DECISION-055 refactor completed), substrate context, Summa restored to the narration graph with its silent-drop failure mode closed, agents_tab.html iframe wiring. Tom pushed; live.
- **DECISION-056** (metabolism): round-2 session traced yield categories — GH main carries only the flat git proxy; yield kinds exist as design only; OpenStory telemetry has no yield capture point. ASSUMPTION-314 (falsifier-b = interaction yield) is the proposed bridge.
- **Lit-search pipeline:** backlog drained (39 cycle-0 + 149 re-trigger), DISPOSITION-181..219, PREMISE-055..060 validated, queue EMPTY; AWAITING-REVIEW backlog 57 — review capacity now the binding constraint (PRESUMPTION-337 itself dispositioned REVISE).
- **Un-numbered carries:** commentary (TRV) explorer built out locally (Stump-PRS sweep 63 edits/53 files; 240 scan pages local-only, 82MB sidecar gitignored); Physics Explorer publish gate held (stale index.lock); education-tab handoff PARKED at 3136f41; Summa QC clean behind the parser-regression wall (→ OPEN-082); Ch. IX/X ingest blocked on rejected ANTHROPIC_API_KEY.
- Sync channel: **morning scrape SUCCEEDED** (login restored; summarized the most recent thread since no 06-11 Chat conversation existed yet) and **evening delivery SUCCEEDED** — first same-day round-trip since the 8-day outage (bears on PRESUMPTION-338's watch).

PROVENANCE:
  Origin: 14a
  Chain: [14a]
  Item type: DECISION-STATUS (daily)
  Transform at each step:
    14a: Status updates registered from today's session transcripts (measurement rounds 1–2, sociogram ship, morning scrape) and the evening sync summary + pipeline footer in for_lit_search.md; no new numbered decisions found.
  Current status: COMPLETE

DECISION-057:
  Date: 2026-06-15 (attended)
  Title: Agent Metabolism measurement charter — files-added/day as headline yield + gap-honest rendering of capture cut-offs
  Decision: For the Metabolism view, (1) adopt files-added/day as the headline yield series (replacing the token/commit proxies as the lead axis), and (2) render data cut-offs honestly in the view layer rather than as real zeros — a dashed "interactive capture ends" horizon for the Apr-6 interactive cliff, hollow rings for cadence-only / zero-token lanes, gap-honest day-bars for sparse yield, and a header staleness badge for the stale right edge. The generator gained a `--from-json` render path so the view can be rebuilt without the live DB. Shipped to a previewable build (`metabolism_view_REVIEW.html`) from existing `metabolism_data.json`; the two database-layer causes (interactive cliff, output-token flatline) were diagnosed but NOT fixed from this session (live `open-story.db` unreachable from this mount), and a `probe_openstory.py` was scripted for Tom to run on the Mac.
  Status: ADOPTED (view layer, previewable build); database-layer root-cause + regen PENDING on the Mac; nothing pushed (localhost:8080 review + push stays with Tom per the constitutional rule).
  Rationale: The metabolism metric must not let missing/changed telemetry read as real productive zeros (ASSUMPTION-320); files-added/day is the proxy Tom selected as the most legible headline (ASSUMPTION-318).
  Related: ASSUMPTION-318, ASSUMPTION-320; PRESUMPTION-349, 351, 352; OPEN-083; DECISION-056 (metabolism ship); `architecture/29_agentic_metabolism.md`; `metabolism_view_REVIEW.html`, `CUTOFF_RECOVERY.md`, `probe_openstory.py`
  NOTE (Rule-7 divergence flag): the 2026-06-15 evening cowork→chat summary characterized the day as having "No new decisions." 14a registers DECISION-057/058 anyway: both set load-bearing, durable instrumentation choices for a deployed self-measurement artifact (which yield series is authoritative; which source dates triplets) and meet the decision bar applied to DECISION-056. The summary's "no new decisions" is treated as a reporting-granularity difference, not authoritative; registries are the source of truth.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the WS1 transcript of the 2026-06-15 attended session — an attended, scoped, previewable-build measurement change. Push/DB-regen state quoted from the session's own statements; repo and live DB not introspectable from this mount.
    Current status: ADOPTED (view layer); DB-layer PENDING

DECISION-058:
  Date: 2026-06-15 (attended)
  Title: PRS-triplet yield source — git history of traditions/*/prs_triplets.md
  Decision: The PRS-triplet yield dimension of the Metabolism view will be sourced from the git history of `wiki/traditions/*/prs_triplets.md`, minting a new `PRS-NN` id per commit-day as the "triplet-completed" event. Chosen over the alternative candidate source. The metric is NOT yet built — this decision settles the source ahead of the next build increment.
  Status: ADOPTED (source settled); metric UNBUILT (the clean next increment).
  Rationale: git history supplies a concrete, already-present completion-date signal for triplets (ASSUMPTION-319), extending the metabolism yield axis named as "next" in DECISION-056.
  Related: ASSUMPTION-319; PRESUMPTION-350; OPEN-081 (authoritative PRS counts); DECISION-056, DECISION-057
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the WS2 source-selection step of the 2026-06-15 session (AskUserQuestion resolution). Build state quoted from the session ("not built yet").
    Current status: ADOPTED (source); UNBUILT

DECISION-059:
  Date: 2026-06-16 (attended)
  Title: PRS-triplet yield metric — build charter
  Decision: The WS2 PRS-triplet yield metric (source settled in DECISION-058) is BUILT. Production is operationalized as the first git appearance of each (tradition, PRS-NN) in `wiki/traditions/*/prs_triplets.md`; the series is reported per commit-day; the headline is GROSS cumulative produced (264 across 6 commit-days, 2026-04-07 → 2026-06-16) reported alongside on-disk-unique (262); retired/reused ids are kept in the cumulative and surfaced fail-loud (stump/PRS-01,/PRS-03 retired; arkanihamed/PRS-10 reused). The git-derived series supersedes the static "269 network" count as the authoritative production number. Implementation: `architecture/metrics/prs_yield.py` + outputs (`prs_yield_detail.csv`, `prs_yield_log.csv`, `prs_yield_snapshot_lines.md`, `prs_yield_histogram.py`, `prs_created_vs_delivered.html`).
  Status: BUILT and locally verified (validate_prs_3d.py PASS; node --check PASS; 06-07 commit-message cross-check PASS). PUSH PENDING on the Mac (regen via `regen_prs_connectome.sh`, then commit + push both the connectome and metabolism views). Per the constitutional rule, the localhost review + push stays with Tom.
  Rationale: Realizes the "metric before the view layer that depends on it" sequencing (ASSUMPTION-326) and gives both the metabolism view and the 3D connectome real git-derived numbers; extends the yield axis named "next" in DECISION-056/058.
  Related: ASSUMPTION-322, 323, 324, 325, 326, 327; PRESUMPTION-355, 356, 357, 358, 359, 360; DECISION-058 (source), DECISION-057, DECISION-056; OPEN-081 (authoritative PRS counts), OPEN-084 (three-count divergence); `architecture/metrics/prs_yield.py`
  CHANGE (under this decision, view layer, not pushed): the PRS 3D connectome (`template_prs_3d.html` → `prs_3d_review.html`) layout collision was fixed — position was keyed only on (thinker, year), collapsing 269 triplets onto 47 stacks (222 hidden); a deterministic fan (group by (thinker, year); grid within each thinker's wedge; stable index order) now yields 269 distinct, separable positions. Count indicator reads "Showing 269 / 269." Reproducible across regens (no randomness).
  NOTE (Rule-7 divergence flag): the 2026-06-16 cowork→chat summary reported "No new DECISION-NNN registered in the registry yet today" (citing the overnight EOD-pipeline timing). 14a registers DECISION-059 anyway, on the same standard applied to DECISION-057/058: the build set durable, load-bearing operational choices (what "production" counts; gross-vs-net headline; supersession of 269) for a deployed self-measurement artifact. Registries are the source of truth; the summary's count is a reporting-granularity/timing difference.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the WS2 build transcript of the 2026-06-16 attended session ("PRS triplet yield WS-2") and the `prs_yield_snapshot_lines.md` artifact. Build/verify state quoted from the session and the on-disk outputs; push/repo state quoted from the session (repo + live regen not introspectable from this mount).
    Current status: ADOPTED (metric built; view-layer fan applied); PUSH PENDING

DECISION-060:
  Date: 2026-06-18 (attended)
  Title: Sociogram thinker-summary pop-ups + "living bios" maintenance workflow
  Decision: The Sociogram tab now renders a yellow `?` summary marker on all 15 thinkers, on Summa (Habash folded in), and on the Traditions header (concept text); clicking opens a dark click-to-open / click-away-to-close brief pop-up, and the `?` does NOT toggle the node's filter checkbox. Data path is single-source-of-truth: `extract_vault_data.py` pulls each thinker's `wiki.md` `**Summary**` block, with `traditions/_extra_summaries.json` supplying the non-thinker (Summa / Traditions-concept) briefs; `generate_visualization.py` renders the marker + pop-up. Briefs were seeded once via `apply_summaries.py` (from `approved_summaries.json`); thereafter `wiki.md` is the source of truth and the bios are edited there directly ("living bios"), regenerated via the canonical `regen_sociogram.sh` wrapper, locally verified, and pushed — `apply_summaries.py` is never rerun (it would clobber hand-edits).
  Status: BUILT, locally verified (validate_html.py ALL CHECKS PASSED; 15/15 thinker groups + Summa carry a summary; only Summa among structure groups gets a `?`), and SHIPPED — pushed to `main` as commit `0fdc8ea` on the Mac after local localhost:8080 sign-off (per the constitutional rule, localhost review + push stays with Tom). Surgical staging (no `git add -A`) kept pre-existing untracked clutter out of the public repo.
  Rationale: Surfaces each tradition's brief on demand inside the graph while keeping one canonical copy of the text (ASSUMPTION-328 — no second copy to drift), routed through the guarded regen wrapper (ASSUMPTION-330) and gated by local visual verify (ASSUMPTION-331).
  Related: ASSUMPTION-328, 329, 330, 331, 332; PRESUMPTION-361..368; OPEN-085 (Summa ~256-vs-379 node-count gap parked as a Summa-thread item); `wiki/c2a2-wiki-narration/scripts/extract_vault_data.py`, `…/generate_visualization.py`, `wiki/traditions/_extra_summaries.json`, `wiki/traditions/*/wiki.md`, `wiki/wiki_narration.html`
  NOTE (next round): the recorded resume state is the bio rewrites — edit the `wiki.md` Summary blocks (or `_extra_summaries.json`), regen via `regen_sociogram.sh`, verify, push; do NOT rerun `apply_summaries.py`. The ~256-vs-379 Summa commentary-node question is parked in the handoff (OPEN-085) as a Summa-pipeline item, not a sociogram-feature regression.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the 2026-06-18 attended build transcript ("Thinker summaries for sociogram") and its shipped commit `0fdc8ea`. Build/verify/push state quoted from the session; repo/live state not introspectable from this mount beyond the mounted file changes confirmed in-session.
    Current status: ADOPTED (built, verified, shipped)

DECISION-061:
  Date: 2026-06-23 (attended — tradition-index interactive session, acting on the autonomous bootstrap audit)
  Title: Tradition index node — reconnect the 15 orphaned tradition hub pages
  Decision: Create `traditions/_index.md`, a single index node with one outgoing wikilink to each of the 15 per-tradition `wiki.md` hubs (levin → wright, all present), directly on the bootstrap audit's #1 recommendation. The hub pages were the audit's "one true structural weakness": they link outward to their `prs_triplets` but received zero inbound links. The sociogram (`wiki_narration.html`) was regenerated via the canonical wrapper and verified live in-browser: the index node resolves to all 15 hubs, no console errors, page loads healthy at 2,814 nodes / 71,975 edges with no crash-limit warnings. Reciprocal links + a durability directive were added per the session. The 2,814-vs-2,812 node count is expected (new index node + one other touched file since the 06-22 build).
  Status: ADOPTED — built and locally browser-verified; content commit made locally; **git push PENDING on Tom's Mac** (the sandbox has no git creds — push and localhost review stay with Tom per the constitutional rule). A gitignored handoff was written at `handoffs/tradition-index.md`; resume cue "resume the tradition index work."
  Rationale: Concentrated, cheap, high-leverage fix (ASSUMPTION-340 hub leverage; ASSUMPTION-344 one index converts 15 orphans into hubs at once), chosen over the rejected alternative of mass unattended leaf-seeding (ASSUMPTION-342; OPEN-088 seeding policy left open).
  Related: ASSUMPTION-338, 340, 344, 345; PRESUMPTION-381 (more hub connectivity = good), 382 (autonomous reframing authority); OPEN-087 (production resolver), OPEN-088 (seeding policy); `wiki/traditions/_index.md`, `wiki/wiki_narration.html`, `architecture/sewing_agent_bootstrap_2026-06-23.md`, `handoffs/tradition-index.md`
  NOTE (Rule-7 divergence flag): the 2026-06-23 cowork→chat summary recorded "None formally registered today … the EOD self-awareness pass has not yet fired." 14a registers DECISION-061 anyway, on the same standard applied to DECISION-057/058/059: a durable, load-bearing structural change (a new canonical index node) was built, verified, and committed for a deployed artifact. Registries are the source of truth; the summary's "none yet" is a reporting-timing difference, not a contradiction.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the 2026-06-23 tradition-index session transcript and the bootstrap audit report. Build/verify state quoted from the session and the regenerated artifact; push/repo state quoted from the session (repo not introspectable from this mount).
    Current status: ADOPTED (built, browser-verified); PUSH PENDING

DECISION-062:
  Date: 2026-06-24 (attended — Cortical Column / DEVPATH-031 Cowork thread)
  Title: Elevate the cortical-column (triple-redundant, voting) thinker-assessment proposal to Dev Pathway 31, post-ISME, one-track pilot
  Decision: Replace the single per-thinker assessor with three independently-wired "column" agents plus a fourth adjudicator that surfaces 2-of-3 semantic consensus and reports dissensus as signal (Hawkins' Thousand Brains). Columns must differ by reference frame (corpus slice / analytic axis), at least two axes varying per column — not by random seed alone, "or the vote only measures sampling noise." Status set `outlined, post-ISME`; pathway file `architecture/31_cortical_column_architecture.md` created and indexed in `pathways.md`. Scope discipline adopted in the same decision: pilot on ONE thinker track (Hawkins) under Pathway 29's metabolism controller, with a falsifiable success criterion (ASSUMPTION-350) gating any scale-out.
  Status: ADOPTED (as design pathway) — outlined, not built; implementation gated behind the July 8–10 ISME presentation and a passing single-track pilot. No code; snapshot-clone-then-fork sequence specified.
  Rationale: The accelerator is to be built out of the rationalities it studies (ASSUMPTION-346); robustness requires substantive column independence, not redundancy (ASSUMPTION-347); dissensus is a first-class detector output (ASSUMPTION-348); the 3–4× cost (ASSUMPTION-349) forces a pilot-first, metabolism-governed rollout (ASSUMPTION-350). Rejected alternative: fan out across all 15 traditions immediately (cost collision with Pathway 29; unjustified before the quality gain is demonstrated).
  Related: ASSUMPTION-346, 347, 348, 349, 350, 351; PRESUMPTION-385, 386, 387, 388, 389, 390; OPEN-089 (independence axes), OPEN-090 (operational definition of semantic agreement); Pathway 29 (metabolism), Pathway 14 (honesty layer), Pathway 07 (unsaid edges), Pathway 00 (broker); `architecture/31_cortical_column_architecture.md`, `architecture/pathways.md`.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the 2026-06-24 DEVPATH-031 session as distilled in the committed pathway file and pathways.md index. Design state (outlined/post-ISME/pilot) quoted from the artifact; no build claimed.
    Current status: ADOPTED (design pathway; unbuilt, ISME-gated)

DECISION-063:
  Date: 2026-06-24 (attended — Coil/Triplet Falsifier foundational review Cowork thread)
  Title: Pre-register the coil/triplet usefulness falsifier (v1.1) — register-then-look, convergence battery, asymmetric verdict
  Decision: Adopt a pre-registered, versioned falsifier for the claim that coils are association fibers, not decoration (H1 vs the "just graphics" null). Load-bearing commitments: (a) specification precedes data inspection — "register, then look" (ASSUMPTION-352, discharges REVISE-111); (b) asymmetric verdict — a FAIL is strong/clean, a PASS is only "necessary-condition met, provisional," never "useful, confirmed" (ASSUMPTION-353, discharges REVISE-105); (c) a convergence battery of operationally independent indicators combined by a pre-fixed decision lattice with no post-hoc weighting (ASSUMPTION-355); (d) retrospective-only confirmatory run + architectural firewall separating coil-author / triplet-author / falsifier-runner (ASSUMPTION-354); (e) amendment discipline — free before any run, after a run only on a results-independent, self-classified rationale. Document frozen at v1.1.
  Status: PRE-REGISTERED DRAFT — frozen at v1.1; **registering git commit PENDING on Tom's Mac** (§8 Registration Act; the sandbox has no git creds — commit + push stay with Tom). No confirmatory run has occurred; per §0 attestation no coil-outcome statistic has been inspected.
  Rationale: Closes the reflexive-falsification circularity (a dyad falsifying its own ledger is "passable by construction") via specification-before-inspection; blocks productivity-ism / Goodhart capture via the asymmetry and the jingle guard (§6, falsifier ≠ §6 yield); guards against synthesis-by-novelty false negatives by holding that indicator exploratory until a `derived_from:` schema field exists (ASSUMPTION-357, OPEN-091).
  Related: ASSUMPTION-352, 353, 354, 355, 356, 357; PRESUMPTION-391, 392, 393, 394; OPEN-091 (derived_from lineage field); REVISE-111, REVISE-105, REVISE-115, REVISE-124; `architecture/coil_falsifier_preregistration.md`, `narrative_prs_connectome.md`, `swarm-contract.md`.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the 2026-06-24 falsifier review session as committed in coil_falsifier_preregistration.md v1.1; status (pre-registered draft, commit pending) quoted from §6/§8 of the artifact.
    Current status: PRE-REGISTERED DRAFT (commit pending on Mac)

DECISION-064:
  Date: 2026-06-24 (attended — Wiki-narration Voice & Navigation Cowork thread)
  Title: Ship voice input, a navigation command engine, multi-provider local-first TTS/AI, and fail-soft quota handling in wiki_narration.html
  Decision: Add four interconnected capabilities to the deployed sociogram, all inline in the single `wiki_narration.html` (no new files, no build step): (1) three-provider TTS — Browser / Kokoro neural-local / OpenAI; (2) Web Speech API voice input with a two-tier router (`stripNavPrefix` → `parseBareGuess` resolves known names offline, else `runSearchAI` only if Ask-AI is on); (3) a universal `navigateByCmd` graph-navigation dispatcher driven by both AI responses and voice, mirrored in the search box; (4) an AI-Query provider section (C2A2 broker default + Groq / Ollama / OpenAI-direct), with automatic fall-back to local text search on `free-limit`/`rate-limited`. Keys for OpenAI/Groq stored in `sessionStorage` only.
  Status: ADOPTED — built and described in the session log; per project rule, localhost browser-verification and git push remain on Tom's Mac (push state not asserted here). Open follow-ups logged in the session ("next session"): WebGPU-for-Kokoro via localhost serve, Whisper offline STT, screenshot→vision graph-state queries, ISME demo hardening.
  Rationale: Local-first navigation conserves API quota (ASSUMPTION-358); sessionStorage key handling is the privacy posture (ASSUMPTION-359); local/offline + generous-free providers with graceful degradation reduce single-broker dependence for a public artifact (ASSUMPTION-360). Consistent with the honesty/quota-transparency pattern (the narration bar explains free-limit fallbacks rather than failing cryptically).
  Related: ASSUMPTION-358, 359, 360; PRESUMPTION-395 (sessionStorage threat model), 396 (single-file 40MB maintainability), 397 (closed nav-keyword set); Device-freedom bright pin; Pathway 27 (universal search/ask); `wiki-narration-voice-nav-session-log.md`, `wiki_narration.html`.
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Registered from the 2026-06-24 voice/nav session log (the committed distilled record). Build described per the log; push/verify state held to Tom per the constitutional rule (not asserted).
    Current status: ADOPTED (built per session log; push/verify on Mac)

DECISION-065:
  Date: 2026-06-25
  Title: Heartbeat tool repaired + self-contained refresh scheduled every 6h
  Decision: Repaired the Heartbeat app (tabs/help control functional again; live-refresh button now reacts visibly — "Checking…" → "Updated HH:MM:SS · N new signals" with green flash, or a calm "re-checked"/"no new snapshot," plus a 60s background check that pulses the button when new data has landed). Rebuilt `refresh_snapshot.sh` to be self-contained (starts runtime, polls 5 feeds, exports, broker-summarizes, enriches, archives a timestamped History snapshot only when content changes, shuts down). Registered a recurring Cowork scheduled task `c2a2-heartbeat-refresh` (every 6 hours).
  Status: IMPLEMENTED + SCHEDULED — staged on disk, NOT pushed (public github.io needs a manual post-review push per the no-blind-push rule). Scheduled task is live; runs only while the Cowork app is open. A residual UI-delivery symptom remains (stale cached app.js in explorer iframe), handed off with a cache-bust as the first move next session (ASSUMPTION-366).
  Related assumptions: ASSUMPTION-361..367
  Related questions: OPEN-092 (app-open liveness adequacy); OPEN-086 (pipeline watchdog)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the Heartbeat tool repair session (verified headless: live-refresh 9/9, archive mechanics, manifest).
    Current status: IMPLEMENTED (local), PUSH PENDING

DECISION-066:
  Date: 2026-06-25
  Title: Explorer UI fixes shipped — header unification + tab/title cleanups (commit 1fba4b7)
  Decision: Grid tab bar (tabs resize; Record can't overlap), two-line chapter tabs, removed the Sociogram in-iframe title (in both the generator and the live artifact), and unified all tool headers to brand gold `#C9A84C` (Inter 700, each tool's size preserved). Heartbeat hero kept as a serif hero, recolored to gold but not flattened (ASSUMPTION-369). Restored two earlier over-removed titles ("C2A2 — Agent Ecosystem," "C2A2 — Summa Explorer").
  Status: COMMITTED + PUSHED — commit `1fba4b7` on `main` (`29e6d97..1fba4b7`), 12 files, +108/−32; scoped to exactly this session's files, none of the 39 agent-WIP files swept in. Tom reviewed and signed off before push (no-blind-push rule honored). The only decision today that reached `origin`. Note: push surfaced a pre-existing repo-wide Dependabot alert (4 dependency vulnerabilities), unrelated to this commit.
  Related assumptions: ASSUMPTION-368..370
  Related questions: (two follow-ups left open: Community Interactions data source; shared-search oddity)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the Explorer UI fixes session and the git push confirmation.
    Current status: SHIPPED (pushed to origin main)

DECISION-067:
  Date: 2026-06-25
  Title: OpenStory backend rebuilt, history backfilled, launchd-supervised
  Decision: Diagnosed and rebuilt the OpenStory backend (came back up on `:3002`; UI reconnected to the new build). Backfilled the full historical event backlog with no window filter (218,879 events; sessions 1,099 → 1,332, events 224k → 256,040, deep-history slice 463 → 666), recovering the pre-72h Cowork history. Restored the durable, launchd-supervised state (`com.tomloughran.openstory.backend`), reboot-safe, with a 10-minute bridge keeping `~/openstory-watch` current. Two enhancements explicitly deferred: VPS-hub sync (NATS leaf/token) and a periodic OpenStory health-check watchdog.
  Status: IMPLEMENTED on Tom's Mac — backend supervised and serving; capture→wiki chain sound end to end. Caveat: the history seed ended in `Killed: 9` (SIGKILL) though its cleanup trap fired and reloaded the agent (PRESUMPTION-405 — post-abnormal-termination DB consistency not separately verified).
  Related assumptions: ASSUMPTION-371, ASSUMPTION-372
  Related questions: OPEN-093 (OpenStory watchdog — same as OPEN-086's need?)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the Open Story system diagnosis session (DB-count verification in-session).
    Current status: IMPLEMENTED (local, supervised)

DECISION-068:
  Date: 2026-06-26
  Title: OpenStory extractors rebuilt around a decoupled local-snapshot read + fail-loud surfacing
  Decision: Fixed the 18-day silent stall of the OpenStory agent-telemetry feed. (1) New shared reader `wiki/agents/openstory/openstory_db.py` copies the live ~2 GB WAL DB to local disk, validates the *local* copy, and reads that — decoupling extraction from the live WAL writer over the FUSE mount; it drops the old full-file `quick_check` guard (the scan that aborted every run since June 8) and instead fails loud with retries. Both `extract_openstory_agent_data.py` and `extract_agent_node_refs.py` route through it. (2) The `openstory-agents-telemetry-refresh` task now also runs `extract_agent_node_refs.py` to refresh `agent_node_edges.json` (the Sociogram agent layer that had no refresher) and passes explicit mounted paths instead of broken `~` defaults. (3) The task writes a dated `REFRESH_STATUS.md` (PASS/FAIL) each run, and `morning-system-health` gained a section 7 that surfaces a FAIL so a silent multi-day stall can't recur.
  Status: IMPLEMENTED locally; NOT pushed. Verified: all three scripts compile; clean immutable read under light load (3/3); correct fail-loud refusal under peak write burst (4–5/5). NOT yet verified: a clean full end-to-end run at peak churn — deferred to the 06:15 quiet-window task ("see it operate where it is designed to"). The two scheduled-task SKILL.md files were edited directly (runner copies them at fire time — worth a Mac sanity check). Per-task token budget was exceeded (surfaced per Rule 6).
  Related assumptions: ASSUMPTION-373, ASSUMPTION-374, ASSUMPTION-375, ASSUMPTION-376
  Related presumptions: PRESUMPTION-407 (quiet-window reliability)
  Related questions: OPEN-095; OPEN-086 (liveness keystone); OPEN-093 (OpenStory watchdog)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the "Agent map explorer runs issue" session close-out.
    Current status: IMPLEMENTED (local, awaiting 06:15 end-to-end proof)

DECISION-069:
  Date: 2026-06-26
  Title: Architecture documentation surface shipped (four-lens view + diagrams + What-Is Tech card)
  Decision: Produced a self-describing architecture surface for the wiki: `architecture/lowlevel_architecture.html` (four-lens low-level view), `architecture/ecosystem_diagram.html`/`.mermaid`, `architecture/runtime_topology.mermaid`, and `architecture/daily_run_trace.mermaid`; stamped the architecture HTML header with a gold "System-state snapshot · 2026-06-26" line. Added a final "Tech — Under the Hood" appendix card to `what_is_c2a2.html` (after the conclusion, styled as an appendix rather than a 16th angle to preserve the "Fifteen Angles" framing) linking the four-lens architecture view and the GitHub repo, with its own dated stamp. In-session git checks confirmed `wiki/architecture/` is not gitignored and `what_is_c2a2.html` is tracked, so both ship cleanly.
  Status: REVIEWED by Tom at the Mac ("they're great … sensibly placed to point to, but not highlighted"). Local edits only; NOT pushed (no-blind-push rule). Handoff `handoffs/architecture-diagrams.md` written (local/gitignored) for a careful next-session push; working tree mixes three streams + stray root `c2a2_*.svg` renders needing per-group triage.
  Related assumptions: ASSUMPTION-377, ASSUMPTION-378, ASSUMPTION-379
  Related presumptions: PRESUMPTION-408 (jsdom render-fidelity), PRESUMPTION-412 (push convergence)
  Related questions: OPEN-097
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the "RC Karpathy Wiki architecture diagram" session.
    Current status: IMPLEMENTED (local, reviewed, push pending)

DECISION-070:
  Date: 2026-06-26
  Title: Level-2 cross-tradition signal stream — deterministic harvest + dual date encoding, embedded in the Interactions chapter
  Decision: Built the Level-2 signal-stream dataset and view. A deterministic rule-based harvester (`harvest_signals.py`) read each approved card's Cross-Tradition Signals section, mapped targets to the 15-tradition roster, split multi-tradition lines, and parsed strength — no model passes — harvesting 525 signals from 140 cards (55 clean, 85 flagged for also referencing non-thinker targets, 18 EMPTY early-format cards left for a Phase-2 model pass), passing a hard coverage gate 158/158 and growing the dataset 218 → 743. The timeline dual-encodes formation (proposal date; April 162 / May 319 / June 44) and source vintage (2024–2026 bar panel). `level2_signal_stream.html` was embedded as a lazy iframe in `community_interactions.html` Level Two with a `?v=Date.now()` cache-bust (constitutional iframe-asset rule). A per-card `qc_trace.csv` audit sheet was produced.
  Status: REVIEWED by Tom ("Checked the viz … super"); embed staged and structurally verified via jsdom; NOT pushed (local review gates push; can't push from sandbox). Handoff `handoffs/level2-signal-stream.md` written. Deferred at Tom's direction: (a) reframing the four "levels" (Tom: "they aren't quite coherent or engaging yet"); (b) a status-chip taxonomy (Coming / In-Process / Live) with a dropdown; (c) the daily standing-pass auto-harvest of newly-approved cards; (d) the 18-card model residue; (e) rewording the Level-Two summary, which still reads intra-tradition while the embed is cross-tradition.
  Related assumptions: ASSUMPTION-380, ASSUMPTION-381, ASSUMPTION-382
  Related presumptions: PRESUMPTION-409, PRESUMPTION-410, PRESUMPTION-411, PRESUMPTION-408
  Related questions: OPEN-096
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the "Interactions tab data visualization" session.
    Current status: IMPLEMENTED (local, reviewed, push pending)

DECISION-071:
  Date: 2026-06-28
  Title: Phase-3 agentic-call boilerplate injection deferred (not executed); bounded alternative recommended
  Decision: The autonomous one-time sewing-agent bootstrap audit deliberately did NOT execute Phase 3 (inject agentic calls into all category A/B/C orphan pages). Doing so would have stamped identical boilerplate into ~480 files (456 of them inbox process-artifacts) in one unreviewed automated pass. Four convergent reasons: (1) the task's own "most-relevant-to-multiple-thinkers" heuristic surfaces process logs (PROCESSED_LOG.md, repair manifests, READMEs) at the top because they name every thinker — so injection would add noise, not synthesis hooks; (2) ~482 actionable pages × (read + 14-way relevance judgment + write) is ~two orders of magnitude beyond the per-session token budget (surfaced, not silently overrun — Rule 6/12); (3) 456 of the 482 are inbox residue owned by the inbox pipeline, whose correct disposition is a pipeline decision, not boilerplate stamping (Rule 3); (4) the live weekly `c2a2-sewing-agent-weekly` task already owns orphan/sparse detection, and thinker content is already connected, so there is no synthesis-connectivity emergency. Bounded alternative recommended for a reviewed (non-cron) session: wire the ~9 under-connected tradition hub pages to their neighbors and triage the 456 inbox pages through the inbox pipeline in dated batches. No vault content pages were modified; append-only deliverables (census + CSV row + report); no git push.
  Status: DECIDED & EXECUTED autonomously (Tom not present); surfaced loudly per Rule 12 rather than partially-done-and-called-complete. Awaiting Tom's review of the bounded alternative and of the bootstrap-vs-maintenance reconciliation (OPEN-098). Companion files: architecture/sewing_agent_bootstrap_2026-06-28.md, architecture/metrics/bootstrap_backlink_census_2026-06-28.md, architecture/metrics/connectivity_log.csv (+1 row).
  Related assumptions: ASSUMPTION-383, ASSUMPTION-384, ASSUMPTION-385, ASSUMPTION-386, ASSUMPTION-387
  Related presumptions: PRESUMPTION-414, PRESUMPTION-415, PRESUMPTION-416, PRESUMPTION-417, PRESUMPTION-418
  Related questions: OPEN-098, OPEN-099, OPEN-100
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the autonomous "C2A2 sewing-agent wiki bootstrap audit" run and its report. (Source = autonomous agent run, not an interactive human session — designer-of-record is the agent under standing project rules.)
    Current status: EXECUTED (autonomous; bounded alternative + reconciliation pending Tom)

DECISION-072:
  Date: 2026-06-29
  Title: Adopt `git pull --rebase --autostash` as the standard push pattern (supersedes the manual stash/pop dance)
  Decision: During the Item-2 push, the push workflow was switched from the prior manual "stash → pull --rebase → push → stash-pop" sequence to `git pull --rebase --autostash`, which auto-stashes the ~20 unrelated working-tree files around the rebase and restores them afterward. This was folded into the push-pattern memory as the standard form, with a recorded note that a scoped/partial stash does not work because the other ~20 files still block the rebase. The change was made and approved in an attended session (Tom: "Let push on here").
  Status: DECIDED & ADOPTED (attended). Operational/workflow decision, not an architecture-of-the-network decision; recorded for traceability because it changes a standing procedure. Item 2 itself is code-complete and approved-pending-push at session end (see 2026-06-29 changelog).
  Related assumptions: ASSUMPTION-391
  Related presumptions: PRESUMPTION-424, PRESUMPTION-412 (cross-session push debt)
  Related questions: —
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the interactive "Resume explorer cleanup" session push-pattern change and memory update.
    Current status: ADOPTED

DECISION-073:
  Date: 2026-06-30
  Title: Clear the PRS-triplet backlog via an attended Track-A ingestion pass (guarded tooling; commit-before-regen; No-Blind-Push review)
  Decision: In an attended session (Tom present), the ~68-card PRS backlog was cleared by ingesting 144 QC-vetted triplets across 12 traditions, regenerating the narrative connectome 288→432 (exactly +144), and publishing after a live visual review — acting on OPEN-101 in favor of an attended batch clear rather than a bounded unattended ingest agent. Along the way: (1) a two-way manifest-gate bug was fixed at source in `build_prs_manifest.py` — the un-ingested gate was keying inbox filenames against a proposal-id log, which re-staged ~15 already-ingested cards and hid real pending ones (corrected set 70 units / 152 candidates, not the runbook's 127); (2) a code-driven dedup pass (`qc_prs.py`) dropped 8 of 152 candidates (hawkins SUPP-001 as a full re-derivation of PRS-10–15, a vacuous hawkins citation-upgrade card, and stump PRS-25 duplicating PRS-09), all source-confirmed; (3) the runbook ordering was corrected to commit → yield → connectome because `prs_yield.py` reconstructs the series from git history and fails loud on uncommitted triplets (Rule 12); (4) `apply_prs.py` gained a fail-loud guard after a qc_trace CSV metadata glitch on 3 cross-tradition-shared proposal-ids (05-18-001/002/003; levin/wright/friston) — vault content git-confirmed correct, only the audit CSV suspect; (5) publish used the DECISION-072 `pull --rebase --autostash` pattern after a No-Blind-Push Chrome review. Cross-tradition routing into `master/cross_program_index.md` and the token-axis metabolism view (blocked by the corrupt 4.35 GB OpenStory DB) were deferred to separate attended passes.
  Status: DECIDED & EXECUTED (attended; committed and pushed to origin/main by Tom). Reusable guarded tooling (`build_prs_manifest.py` fix, `apply_prs.py`, `qc_prs.py`) established as the standard PRS-ingestion path. Partially resolves OPEN-101 (this backlog cleared, attended) but leaves the cadence question (OPEN-102) and the freshness-marking question (OPEN-103) open.
  Related assumptions: ASSUMPTION-393, ASSUMPTION-394, ASSUMPTION-395, ASSUMPTION-396, ASSUMPTION-397, ASSUMPTION-398, ASSUMPTION-399, ASSUMPTION-400, ASSUMPTION-401
  Related presumptions: PRESUMPTION-425, PRESUMPTION-426, PRESUMPTION-427, PRESUMPTION-428, PRESUMPTION-429, PRESUMPTION-430, PRESUMPTION-431
  Related questions: OPEN-101 (partially addressed), OPEN-102, OPEN-103, OPEN-104 (new), OPEN-095 (OpenStory proof, still blocked)
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the attended "PRS backlog runbook" session (2026-06-30). Tom ran the Mac-side commit/push; the session drove ingestion, QC, connectome regen, and the No-Blind-Push review.
    Current status: EXECUTED (attended; live on origin/main)

DECISION-074:
  Date: 2026-07-02 (attended — "The convener" / Inter-Tradition Dialogue Study session, Tom present)
  Title: Adopt author-ratification as the Inter-Tradition Dialogue convener's validity standard
  Decision: The study's standard for "understanding was achieved" is set to author-ratification — the person who made a claim is the sole judge of whether it was captured, "never the convener, never a third-party translator" ("Ratified by its author, not mapped between sentences"). This replaced the earlier "inhabitation-checked-by-the-inhabited" phrasing and is now load-bearing across the paper (intro, results, discussion, conclusion). The study operationalizes it through the C0 gate (faithful-vs-strawman verdict discrimination) and the listen/deaf contrast.
  Status: ADOPTED (attended; ratified by Tom in the session). Methodological/meta-architecture commitment for the convener component; the study drafted around it is local (nothing published).
  Rationale: Author-ratification is stated as the only legitimate way understanding can be established in cross-tradition dialogue; it also reinforces the paper's own finding that the C0 gate's word-overlap limb does no real work while its verdict-discrimination limb is decisive.
  Related: ASSUMPTION-403, 404, 405, 406, 408; PRESUMPTION-437, 438, 442; OPEN-108
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the attended convener session's explicit rephrasing and ratification of the validity standard. Draft study `study_interT_dialogue_c2a2.md`; nothing published.
    Current status: ADOPTED (attended; study local)

DECISION-075:
  Date: 2026-07-02 (attended — "InterT study" session, Tom present)
  Title: Ship the Inter-Tradition Study tab + Appendix G live in the Explorer; park the §5.3 strengthening run and publication
  Decision: The Inter-Tradition Study tab (with Appendix G) was merged to `main` and confirmed live in the Explorer's Accelerator Tools row, with the corrected help-popup wording, verified via cache-busted fetch (`explorer.html?cb=verify1` shows the new row; `interT_study.html?cb=verify1` renders). Two moves were explicitly parked per Tom's call: the §5.3 strengthening run (which would earn P3′b a real confidence interval) and the publish/Explorer-render-of-the-paper decision. The next session opens on Appendix G, Stage 1 — a declarative study spec + a one-file runner (generate → analyze → render), with preregister-before-run to become a Stage 2 machine gate.
  Status: REALIZED (tab live on GitHub Pages after the real 07-02 Pages incident cleared; verified). Strengthening + publish DEFERRED. A drift risk is logged: Appendix G lives in both the source `.md` and the embedded HTML copy, so future study edits must be re-pasted; the commit SHA was not captured (read from `git log` on resume).
  Rationale: The tab is ISME-facing and ready; the study's thesis-bearing claim (P3′b) is not yet a banked result (ASSUMPTION-410), so publication waits on the strengthening run rather than shipping an overstated result.
  Related: ASSUMPTION-407, 409, 410; PRESUMPTION-441; OPEN-106, OPEN-107
  Provenance:
    Origin: 14a
    Chain: [14a]
    Item type: DECISION
    Transform at each step:
      14a: Recorded from the attended "InterT study" session close (2026-07-02), including the live-URL verification and the handoff's parked-moves list. Git push/SHA held to Tom's Mac per the standing no-blind-push rule.
    Current status: REALIZED (tab live; strengthening + publish deferred)
