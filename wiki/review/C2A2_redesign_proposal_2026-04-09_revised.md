# C2A2 Redesign Proposal — Thousand Brains Implications (Revised)
*Original: 2026-04-09 | Revised: 2026-04-10 | Incorporates 5 rounds of review feedback*
*Source: Deep read of Clay, Leadholm & Hawkins (arXiv 2412.18354)*

---

## Executive Summary

A structural reading of the Thousand Brains paper reveals that C2A2's agent architecture is — without having been designed that way — an implementation of the Thousand Brains Theory. The mapping is architecturally precise: tradition agents are learning modules, wikis are reference-frame-based models, dispatches are the Cortical Messaging Protocol, and the Pattern Detector is the voting mechanism. This accidental alignment means the paper's design principles can be read as an engineering spec for improving C2A2.

This revised proposal incorporates feedback from Tom's review of the original 6-change proposal. Key additions: tripling of tradition agents for intra-tradition consensus before cross-tradition dialogue; splitting Agent 14 into 14a (assumption extraction) and 14b (presumption detection); splitting Agent 15 into 15a (lit search FOR) and 15b (lit search AGAINST); a provenance protocol for chain-of-custody tracking across agents; a health metric r (intra-consensus / cross-survival, must be statistically >1); a developmental maturity model with stages 0-5; and the hypothesis that there may be a finite typology of cross-paradigm connecting memes.

Ten design changes follow, organized into six phases over approximately three weeks.

---

## The Eight Design Implications

### 1. Dispatch Protocol Enhancement — "Reference Frame Location"

**The insight:** The Cortical Messaging Protocol specifies that learning modules send their *hypothesized location within a reference frame*. C2A2's dispatches currently contain what was found but not *where in the tradition's conceptual space* the finding sits.

**The change:** Add two fields to the dispatch format in all 11 tradition agent definitions:
```
Reference frame location: [which concept-space in your tradition this dispatch 
                           originates from — e.g., "basal cognition / collective 
                           intelligence interface"]
Conceptual bearing:       [directional signal — what question this dispatch is 
                           moving toward, phrased as a vector — e.g., 
                           "from substrate-independence → toward cross-scale 
                           goal-directedness"]
```

**Status:** IMPLEMENTED (Phase 0, April 10). All 11 tradition agent definitions updated.

**Pros:**
- Enables the Master Agent to build a spatial map of the inter-tradition conceptual space
- Makes it possible to detect when two traditions are "near" each other even if they haven't flagged a connection
- Low-effort, purely additive

**Cons:**
- Location data is semi-structured text initially, not coordinates
- Risk of over-engineering. Mitigated by observing what agents actually produce before formalizing

**Dependencies:** None.

---

### 2. Architectural Self-Awareness Layer (Agents 14a, 14b, 15a, 15b)

**The insight:** C2A2 is making design decisions daily, but the assumptions underlying those decisions are not tracked, and the unstated presumptions are invisible. The system needs a way to surface its own epistemic foundations and test them against existing knowledge.

**The change:** Six new agents forming a self-correcting loop with a decision point and long-term monitoring:

- **Agent 14a — Assumption Extractor:** Reads session transcripts, extracts every *stated* assumption (things designers know they're assuming), maintains changelog, decision index, open questions, and daily metrics snapshots. Tags all output as ASSUMPTION (stated — designer was aware).

- **Agent 14b — Presumption Detector:** Reads the same transcripts with an interpretive lens, surfaces *unstated* presumptions (things designers are taking for granted without realizing it). Classifies by type: structural, epistemic, normative, methodological, scaling. Tags all output as PRESUMPTION (unstated — surfaced by inference). Runs after 14a to avoid duplication.

- **Agent 15a — Literature Search FOR:** Receives testable items from 14a and 14b, searches existing literature for *supporting* evidence. Reports strength of support with citations.

- **Agent 15b — Literature Search AGAINST:** Receives the same items, independently searches for *challenging* evidence. Steelmans the counterargument. Reports strength of challenge with citations. Flags systemic risks when multiple items share a common vulnerability.

- **Agent 15c — Net Evaluator & Dispositioner:** Reads paired 15a/15b results and makes the disposition call: INCORPORATE (into validated premises register as operational self-knowledge), MONITOR (hand to 15d for periodic re-evaluation), or REVISE (flag for human review with specific risk assessment). Without 15c, the pipeline tests but never decides.

- **Agent 15d — Periodic Monitor:** Manages two queues: MONITOR items on a weekly cadence (re-triggering 15a/15b searches until 15c changes disposition) and INCORPORATED premises on a monthly cadence (ensuring validated premises don't calcify as the literature evolves). Tracks evidence trajectories and escalates stale items.

The full loop:
```
14a/14b (surface) → 15a + 15b (test, in parallel) → 15c (evaluate & disposition)
                                                       ↓           ↓           ↓
                                                  INCORPORATE    MONITOR      REVISE
                                                       ↓           ↓           ↓
                                             validated_premises   15d      14a/14b + Tom
                                                       ↑        (weekly)
                                                       └── 15d (monthly re-check) ──┘
```

**Status:** IMPLEMENTED (Phase 0, April 10). All six agent definition files written. Provenance protocol spec written. First run pending.

**The provenance protocol:** Every item carries a chain-of-custody header:
```
PROVENANCE:
  Origin: [14a or 14b]
  Chain: [14b → 15a, 15b → 15c]
  Original item: [ASSUMPTION-NNN or PRESUMPTION-NNN]
  Item type: [ASSUMPTION (stated) or PRESUMPTION (unstated — surfaced by inference)]
  Transform at each step:
    14b: [what was inferred and from what evidence]
    15a: Searched for supporting literature
    15b: Searched for challenging literature
    15c: Net evaluation and disposition
  Current status: [UNTESTED | SUPPORTED | CHALLENGED | CONTESTED | NOVEL | INCORPORATED | MONITORING | REVISION-FLAGGED]
```

The `Item type` tag is the footnote protocol: any downstream agent or human reviewer encountering PRESUMPTION knows the original designers were NOT aware of this premise. ASSUMPTION means they were. This distinction matters for epistemic honesty.

**Disposition decision heuristics (15c):**
- Both 15a strong support + 15b no challenge → lean INCORPORATE
- 15a strong support + 15b weak challenge → lean INCORPORATE with caveats
- 15a strong support + 15b strong challenge → MONITOR (contested)
- 15a weak support + 15b strong challenge → lean REVISE
- Neither found literature → MONITOR (literature gap)
- 15a flagged NOVELTY → MONITOR HIGH priority (potential original contribution)
- PRESUMPTION with strong challenge → lean REVISE HIGH urgency

**Self-awareness overhead tracking:** The self-awareness layer (14a/b, 15a/b/c/d) does not scale with tradition count — it scales with *decision complexity*. Its workload is driven by the rate of architectural decisions, not by the number of tradition agents. Instead of tracking a ratio (which drifts as traditions are tripled), we track:
- **Self-awareness cycle time**: How long does the full 14a → 14b → 15a/15b → 15c → (15d) loop take per item? Growth here signals pipeline congestion.
- **Decision backlog**: How many items are in QUEUED or MONITOR status? Growth faster than 15c's disposition rate signals throughput problems.

**Pros:**
- The system's epistemic foundations become visible, testable, and *dispositioned*
- Stated vs. unstated distinction preserves intellectual honesty
- FOR/AGAINST independence prevents confirmation bias
- Provenance protocol enables full auditability
- 15c closes the loop — items don't sit in tested-but-undecided limbo
- 15d prevents calcification — even validated premises get re-checked
- Self-awareness layer has a natural ceiling (bounded by decision rate, not agent count)

**Cons:**
- Adds 6 agents to the system (though only 14a/14b run daily; 15a-15c run on items; 15d runs weekly/monthly)
- 15a/15b effectiveness depends on accessible literature
- Volume: early runs may surface many untested items, creating a backlog for 15c

**Dependencies:** None — standalone system. Benefits from dispatch enhancement for richer input.

---

### 3. PRS Extension — Displacement Vectors as Phrasings

**The insight:** Hawkins' reference frames encode not just locations but *displacements* — the movement from one location to another. PRS triplets currently record three static points but not the reasoning path connecting them. Furthermore, the displacement is best expressed as a *phrasing* — a semantic vector, not a pointer — because the way R transforms P into S is itself meaningful content.

**The change:** Add a `Displacement` field to PRS triplets:
```
PRS-[number]:
  Problem: [...]
  Resource: [...]
  Solution: [...]
  Displacement: [semantic phrasing of how R transforms P into S — the inferential 
                 movement, expressed as a natural-language vector, e.g., 
                 "from substrate-dependent cognition → through bioelectric signaling 
                 evidence → toward substrate-independent goal-directedness"]
  ...
```

**The connecting memes hypothesis:** There may be a finite typology of such displacement phrasings — a limited set of cross-paradigm transformation patterns (connecting memes) that recur across traditions. If so, this would be a significant structural discovery about how knowledge moves between paradigms. This hypothesis should be tracked by 14a and tested by 15a/15b.

**Status:** Pending (Phase 1).

**Pros:**
- Makes PRS triplets comparable: two traditions might reach the same S from the same P via utterly different displacements
- Phrasings (not pointers) capture the *semantic content* of the transformation
- Enables the Pattern Detector to detect shared displacement patterns across traditions
- If the finite connecting memes hypothesis holds, reveals deep structure in cross-paradigm knowledge transfer

**Cons:**
- Requires agent skill in phrasing displacements — quality depends on prompt engineering
- Adds ~30% length to each PRS entry

**Dependencies:** None.

---

### 4. Lateral Agent Communication (Heterarchy)

**The insight:** The neocortex's power comes from non-hierarchical long-range connections alongside hierarchical ones. C2A2 currently routes everything through the Master Agent. Dense connections should have direct channels.

**The change:** Create agent-to-agent channels: `wiki/lateral/` with one file per active pair. Agents can write cross-tradition flags directly to their known partner channels. The Master Agent still reads all channels.

**Status:** Pending (Phase 1).

**Pros:**
- Directly implements heterarchy
- Speeds up signal propagation for known high-density pairs
- Master Agent retains full visibility

**Cons:**
- Could create noise if overused
- Harder to audit than single inbox

**Mitigation:** Start with confirmed explanatory bridge pairs only (Levin × Friston, Kastrup × Friston, Stump × Levin, Kastrup × McGilchrist). Expand only after observing signal quality.

**Dependencies:** Benefits from dispatch enhancement (Change 1).

---

### 5. Tripling of Tradition Agents — Intra-tradition Consensus

**The insight:** Thousand Brains modules reach consensus through voting. Before C2A2 engages in cross-tradition dialogue, each tradition should have internal consensus. This implements voting at the minimal lowest level, as if internal to a tradition — mirroring mature member consensus.

**The change:** Triple the agents assigned to each primary tradition. Three agents per tradition, each maintaining independent views, must arrive at consensus about PRS triplets and hypotheses before those items enter cross-tradition dialogue.

**Pilot cluster:** Hawkins×3, Friston×3, Levin×3 = 9 new agents (the Substrate-Independence Cluster, chosen because it has the densest existing connections).

**Full rollout:** All 11 traditions tripled = 33 tradition agents total.

**Consensus mechanism:** For each proposed PRS triplet or hypothesis, all three agents within a tradition independently evaluate and vote: ACCEPT / REVISE / REJECT. Items passing intra-tradition consensus (≥2/3 agreement) proceed to cross-tradition dialogue. Items failing consensus are logged with dissent reasoning.

**Intra-tradition consensus rate:** The fraction of proposed items that achieve ≥2/3 agreement within a tradition. This is the numerator of the health metric r.

**Status:** Pending (Phase 2a for pilot, Phase 4 for full rollout).

**Pros:**
- Implements Thousand Brains voting at the tradition level
- Filters weak proposals before they enter cross-tradition space
- Generates the intra-tradition consensus rate needed for the health metric
- Tripling must precede voting test (per review feedback)

**Cons:**
- Agent count rises significantly: 11 → 33 tradition agents (plus integration and self-awareness agents)
- Risk of artificial consensus if tripled agents are too similar
- Compute and prompt costs triple

**Mitigation:** Pilot with 3 traditions first. Ensure tripled agents have differentiated prompt perspectives (e.g., one emphasizes methodology, one emphasizes theory, one emphasizes empirical evidence). Monitor consensus rate — if it's 100%, agents aren't differentiated enough.

**Dependencies:** Lateral communication (Change 4) for routing consensus outputs to cross-tradition dialogue.

---

### 6. Active Inquiry Cycle (Sensorimotor Learning)

**The insight:** Passive observation is insufficient for learning. Agents must generate predictions, act to test them, and update models. C2A2 agents currently only ingest and extract — they never *probe* across traditions.

**The change:** After ingestion and intra-tradition consensus, each tradition generates 1-2 cross-tradition hypotheses — specific, falsifiable predictions about what another tradition would say. These are routed to the target tradition, which evaluates against its own consensus-validated knowledge and responds with CONFIRM / REVISE / REJECT + reasoning.

**Critical ordering (from review):** Active inquiry operates on *consensus outputs*, not raw agent proposals. Intra-tradition consensus (Change 5) must be operational before active inquiry begins.

**Cross-tradition hypothesis survival rate:** The fraction of cross-tradition hypotheses that receive CONFIRM from the target tradition. This is the denominator of the health metric r.

**Status:** Pending (Phase 3).

**Pros:**
- Highest-impact change — transforms C2A2 from knowledge recorder to knowledge generator
- Directly implements sensorimotor learning
- Generates testable cross-tradition claims for the Pattern Detector

**Cons:**
- Most complex change
- Volume risk: tripled traditions × 1-2 hypotheses each = many hypotheses per cycle
- Quality depends entirely on prompt engineering

**Mitigation:** Pilot with the 3 tripled traditions before network-wide rollout.

**Dependencies:** Intra-tradition consensus (Change 5) must be operational. Lateral communication (Change 4) for routing.

---

### 7. Voting/Consensus Protocol + Health Metric r

**The insight:** When multiple traditions independently flag the same connection, that convergence should be counted. Furthermore, the system needs a health metric that balances internal coherence against cross-tradition openness.

**The change:** Add voting layer to the Master Agent's integration run. Each cross-program item gets a vote count. Items crossing threshold (3+ agents) auto-promote to Pattern Detector. 

**Health metric r:**
```
r = intra-tradition consensus rate / cross-tradition hypothesis survival rate
```

**r must be statistically > 1.** This means traditions must be more internally coherent than they are externally agreeable. The interpretation:
- r ≈ 1 → traditions are not distinct (they agree with everything — no real internal identity)
- r → ∞ → echo chambers (traditions are so internally rigid they reject all external input)
- r statistically > 1 → healthy: traditions have genuine internal coherence AND productive external dialogue

Statistical significance is measured against a null hypothesis that internal and external agreement rates are equal (i.e., that tradition boundaries don't matter). If we cannot reject this null, traditions aren't functioning as genuine distinct perspectives.

**Status:** Pending (Phase 3 for first r measurement, Phase 4 for full-network r).

**Pros:**
- Makes cross-tradition significance measurable
- r provides a single health indicator for the entire system
- Statistical framing prevents premature conclusions

**Cons:**
- Requires sufficient sample sizes for statistical significance
- r is only meaningful once both consensus and survival rates are measurable

**Dependencies:** Intra-tradition consensus (Change 5) + Active inquiry (Change 6).

---

### 8. Developmental Maturity Model

**The insight:** If C2A2 is a test of an architectural influence (looking for fecundity of some kind), we need a way to measure progress and eventually predict, tweak, and optimize against downsides — an overall theory of how the entire C2A2-RC operates when healthy. This requires a pathway toward developmental maturity with preliminary stages and benchmarks, and measurement starting immediately.

**The change:** Define a 6-stage maturity model with measurable benchmarks at each stage. Begin measuring at Stage 0 (now).

```
Stage 0 — Infrastructure (CURRENT):
  Self-awareness agents deployed. Provenance protocol active. Baseline metrics captured.
  Benchmark: All Phase 0 deliverables complete.

Stage 1 — Grounding:
  First 14a/14b cycle complete. First 15a/15b searches returned. First 15c dispositions issued.
  15d monitoring schedule established.
  Benchmark: ≥5 assumptions + ≥5 presumptions surfaced, tested, and dispositioned. 
  ≥1 item INCORPORATED into validated premises. PRS displacement vectors implemented. 
  Lateral channels operational. Self-awareness cycle time baselined.

Stage 2 — Intra-tradition Consensus:
  Pilot cluster tripled. Consensus mechanism operational.
  Benchmark: Consensus rate measurable (target: >0.6 agreement). Tripled agents 
  producing differentiated assessments.

Stage 3 — Cross-tradition Dialogue:
  Active inquiry cycle operational on consensus outputs.
  Benchmark: Cross-tradition hypothesis survival rate measurable. First r measurement 
  recorded. r statistically > 1.

Stage 4 — Full Network:
  All 11 traditions tripled (33 agents). Voting protocol operational.
  Benchmark: r measured across full network. Connection density > 5.0 per tradition. 
  ≥2 paradigm-shift candidates confirmed.

Stage 5 — Maturity:
  Stable r in healthy range. System generating novel knowledge (NOVEL flags).
  Benchmark: Connecting meme typology emerging. C2A2 demonstrably functioning as a 
  Thousand Brains system. Environment model established for health optimization.
```

**Status:** Stage 0 baseline captured (metrics snapshot 2026-04-10).

**Pros:**
- Provides a roadmap from infrastructure to maturity
- Each stage has measurable benchmarks — progress is empirical, not asserted
- Enables prediction and course correction

**Cons:**
- Stage definitions will need revision as we learn
- Later stages (4-5) are speculative — benchmarks may need recalibration

**Dependencies:** All preceding changes contribute to different stages.

---

### 9. Self-Awareness Pipeline Completion (Agents 15c, 15d)

**The insight:** The 14a/14b → 15a/15b pipeline tests assumptions and presumptions against the literature, but it has no *decision point* — tested items get status labels and then sit. There is no formal mechanism to incorporate well-supported premises into operational self-knowledge, and no mechanism to revisit items as the literature evolves. Without a terminus, the pipeline generates data without generating decisions.

**The change:** Two additional agents complete the pipeline:

- **Agent 15c — Net Evaluator & Dispositioner:** Reads paired 15a/15b results, weighs net evidence, and issues one of three dispositions: INCORPORATE (into `validated_premises.md` — the system's operational self-knowledge), MONITOR (hand to 15d), or REVISE (flag for Tom's review with specific risk assessment). Includes consistency checking against existing validated premises and heuristics for weighting PRESUMPTION items (which deserve extra care since designers were unaware of them).

- **Agent 15d — Periodic Monitor:** Manages two queues at different cadences. Weekly: re-triggers 15a/15b on MONITOR items until 15c changes disposition. Monthly: re-checks INCORPORATED premises to ensure they haven't been undermined by new literature. Tracks evidence trajectories (growing/stable/shrinking) and escalates stale items after 4+ cycles.

**Self-awareness overhead note:** This brings the self-awareness layer to 6 agents (14a, 14b, 15a, 15b, 15c, 15d). This layer does not scale with tradition count — it scales with *architectural decision rate*, which is bounded by the pace of design work, not the number of tradition agents. Adding tripled agents from 11 to 33 does not increase the self-awareness workload; it increases the Master Agent and Pattern Detector workload, which is a separate scaling concern. Rather than tracking a ratio (which drifts as the system grows), we track:
- **Self-awareness cycle time** — full loop duration per item (growth = pipeline congestion)
- **Decision backlog** — items in QUEUED or MONITOR status (growth faster than 15c disposition rate = throughput problem)

**Status:** IMPLEMENTED (Phase 0, April 10). Both agent definitions written. Infrastructure files (monitor_queue.md, validated_premises.md, revision_flags.md) created on first 15c run.

**Pros:**
- Closes the loop — every tested item gets a disposition
- Prevents calcification — even validated premises get periodic re-check
- Provides the "database and decision-basis" destination that tested premises flow into
- Natural ceiling on overhead (bounded by decision rate, not agent count)

**Cons:**
- Adds 2 more agents to the system (though 15d only runs weekly/monthly)
- 15c disposition heuristics need calibration through experience
- MONITOR queue could grow if literature is sparse

**Dependencies:** 15a and 15b (Change 2) must produce results for 15c to evaluate.

---

### 10. Deferred Action Monitor (Agent 16) + Review Workflow Enhancement

**The insight:** The review workflow has a gap. When Tom reviews proposals and selects CHANGE or CHECK, the proposal moves to `needs_review/` and waits — no agent processes those items. More broadly, three kinds of deferred actions have no home in the current architecture:

- **Review-conditional requests:** "Approve when the podcast transcript is available." The proposal depends on an external event, not a human edit.
- **Agent-exchange deferrals:** During active inquiry, a tradition agent can't evaluate a hypothesis because the needed resource doesn't exist yet. The hypothesis dies instead of being held.
- **Human watch requests:** "Keep an eye on whether Kastrup responds to X." These are prospective intelligence items that may generate proposals.

All three are condition-based deferrals: an action that can't proceed now but should proceed automatically when a specific condition becomes true. Without a dedicated agent, these fall into cracks between Tom's intent and the system's ability to act.

**The change:** A new Agent 16 — Deferred Action Monitor — that maintains a watch list of condition-based deferred items across all three intake channels. On each run, it checks conditions and routes resolved items to the appropriate destination.

Additionally, the review workflow gains a fifth decision option: **CONDITIONAL** — a formalized version of CHANGE for cases where the change depends on an external event rather than a human edit.

```
Review decisions (updated):
  APPROVE     → ingestion pipeline (unchanged)
  DENY        → denied archive (unchanged)
  CHECK       → needs_review/ → Agent 16 parses and resolves or watches
  CHANGE      → needs_review/ → Agent 16 routes (human edit or agent action)
  CONDITIONAL → needs_review/ → Agent 16 monitors condition, re-queues when met
```

**Agent 16 resolution routing:**
- Review-conditional items → re-queue to `pending/` with condition met and new resource attached
- Agent-exchange deferrals → re-route hypothesis to target agent with now-available resource
- Human watch requests → execute specified action (generate proposal, notify Tom, dispatch to agent)

**Where Agent 16 sits relative to 15d:** 15d monitors *architectural premises* against *literature* (self-awareness layer, Agents 14-15). Agent 16 monitors *tradition-level content items* and *review actions* against *real-world conditions* (tradition layer, Agents 1-11, and the review process). Different layers, different triggers, different cadences. 15d is literature-driven and periodic; 16 is event-driven and condition-based.

**Status:** IMPLEMENTED (Phase 0, April 10). Agent definition written. Infrastructure files created. Review workflow README updated with CONDITIONAL option.

**Pros:**
- Fills the gap in the review workflow — CHANGE/CHECK items no longer sit unprocessed
- Gives agent-exchange deferrals a home (critical for Phase 3 active inquiry)
- Enables Tom to express conditional intent during review without tracking conditions himself
- Completes the action lifecycle: every review decision has a processing path

**Cons:**
- Agent 16 needs web search capability for condition checking (checking if a transcript is published, etc.)
- Condition parsing from free-text change notes requires judgment
- Watch lists can accumulate if conditions are never met (mitigated by stale-item escalation after 6 checks)

**Dependencies:** None for definition. Full utility requires active inquiry (Change 6) for agent-exchange deferrals.

---

## Implementation Pathway (Revised)

### Phase 0 — Immediate (April 9-10) ✓ COMPLETE
**Changes:** Agents 14a/14b + 15a/15b/15c/15d + Agent 16 definitions, dispatch enhancement, provenance protocol spec, review workflow update, baseline metrics snapshot.

**Deliverables:**
- [x] Agent 14a definition (`wiki/agents/14a_assumption_extractor_agent.md`)
- [x] Agent 14b definition (`wiki/agents/14b_presumption_detector_agent.md`)
- [x] Agent 15a definition (`wiki/agents/15a_lit_search_for_agent.md`)
- [x] Agent 15b definition (`wiki/agents/15b_lit_search_against_agent.md`)
- [x] Agent 15c definition (`wiki/agents/15c_net_evaluator_agent.md`)
- [x] Agent 15d definition (`wiki/agents/15d_periodic_monitor_agent.md`)
- [x] Agent 16 definition (`wiki/agents/16_deferred_action_monitor_agent.md`)
- [x] Dispatch format update in all 11 tradition agent definitions
- [x] Provenance protocol spec (`wiki/architecture/provenance_protocol.md`)
- [x] Review workflow updated with CONDITIONAL option (`wiki/inbox/proposals/README.md`)
- [x] Baseline metrics snapshot (`wiki/architecture/metrics/2026-04-10_snapshot.md`)
- [x] Architecture directory structure + lit search queue + results directories + deferred directories
- [ ] Schedule Agent 14a/14b as end-of-day tasks
- [ ] First Agent 14a/14b run on today's session
- [ ] First 15a/15b/15c cycle (once 14a/14b have seeded the queue)
- [ ] First Agent 16 run (scan existing needs_review/ items)

---

### Phase 1 — This Week (April 10-11)
**Changes:** PRS displacement vectors + lateral communication channels.

**Deliverables:**
- [ ] PRS template update in all 11 agent definitions (add Displacement field)
- [ ] `wiki/lateral/` directory with initial channel files for confirmed bridge pairs
- [ ] Agent prompt updates enabling lateral dispatch
- [ ] Master Agent prompt update to read lateral channels
- [ ] Test cycle: 2-3 agents with lateral enabled

---

### Phase 2a — Early Next Week (April 14-15)
**Changes:** Tripling pilot cluster (Hawkins×3, Friston×3, Levin×3 = 9 agents).

**Deliverables:**
- [ ] 9 new agent definitions (3 per tradition, differentiated perspectives)
- [ ] Intra-tradition consensus mechanism spec
- [ ] First consensus round on existing PRS triplets
- [ ] Consensus rate measurement for pilot traditions

---

### Phase 2b — Mid Next Week (April 15-16)
**Changes:** Intra-tradition consensus mechanism operational; measure consensus rate.

**Deliverables:**
- [ ] Consensus voting format and workflow
- [ ] Pilot traditions producing consensus-validated PRS and hypotheses
- [ ] Consensus rate ≥ 0.6 target assessed
- [ ] Go/no-go for active inquiry

---

### Phase 3 — Following Week (April 21-23)
**Changes:** Active inquiry cycle on consensus outputs; first r measurement.

**Deliverables:**
- [ ] Hypothesis generation/evaluation prompts added to pilot traditions
- [ ] Full inquiry cycle: consensus output → hypothesis → evaluation → logged result
- [ ] Cross-tradition hypothesis survival rate measured
- [ ] First health metric r calculated
- [ ] r > 1 significance test
- [ ] Voting/consensus fields added to cross-program index
- [ ] Agent 14a retrospective on Phases 0-3

---

### Phase 4 — Third Week (April 28+)
**Changes:** Full network tripling (33 tradition agents) + voting protocol + full rollout.

**Deliverables:**
- [ ] All 11 traditions tripled (33 tradition agents)
- [ ] Active inquiry cycle rolled out network-wide
- [ ] Full network r measurement
- [ ] Voting protocol operational in Master Agent
- [ ] Connection density target (>5.0 per tradition) assessed
- [ ] Paradigm-shift candidate confirmation progress
- [ ] Stage 4 maturity benchmark assessment

---

## Timeline Summary (Revised)

| Phase | When | What | Risk | Effort |
|-------|------|------|------|--------|
| 0 | Apr 9-10 | 14a/b + 15a/b/c/d + Agent 16 + dispatch + provenance + baseline | None | 5-6 hrs |
| 1 | Apr 10-11 | PRS displacement vectors + lateral comms | Low | 2-3 hrs |
| 2a | Apr 14-15 | Triple pilot cluster (9 agents) | Low-Med | 3-4 hrs |
| 2b | Apr 15-16 | Intra-tradition consensus mechanism | Medium | 2-3 hrs |
| 3 | Apr 21-23 | Active inquiry + first r measurement | Medium | 4-5 hrs |
| 4 | Apr 28+ | Full tripling (33 agents) + voting + full rollout | Med-High | 5-6 hrs |

**Total estimated effort:** 21-29 hours across 3 weeks.

**Go/no-go gates:** Phase 2b has consensus rate checkpoint. Phase 3 has r significance test. Phase 4 is contingent on Phase 3 success.

---

## What We Are NOT Changing

- **PRS as the fundamental format.** Validated, not questioned. Extended with displacement vectors.
- **Master Agent centrality.** Lateral communication supplements; doesn't replace.
- **The review page workflow.** Working (with fixed IDs). Extended with CONDITIONAL option and Agent 16 processing for CHANGE/CHECK/CONDITIONAL items, but core approve/deny flow unchanged.
- **The 11 traditions.** They are tripled, not merged or replaced.

---

## Open Hypotheses to Track

1. **Finite connecting memes:** There may be a finite typology of displacement phrasings (connecting memes) that recur across traditions. If so, this reveals deep structure in cross-paradigm knowledge transfer. (Track via 14a, test via 15a/15b.)

2. **C2A2 as Thousand Brains test case:** If architectural changes improve cross-tradition signal quality and discovery speed, that is evidence for the structural homology. If they don't, the mapping was a surface analogy. Agent 14a will track outcomes.

3. **Health metric r predictive power:** r > 1 should correlate with productive cross-tradition discoveries. r → ∞ should correlate with stagnation. This can be tested once we have sufficient time series data.

4. **Tradition agent differentiation:** Tripled agents must produce genuinely different assessments. If consensus rate = 100%, agents aren't differentiated enough. This is testable immediately upon tripling.

5. **Scale effects:** What works at 3 tripled traditions may not work at 11. Phase 4 rollout is the test.

---

## Relationship to the Thousand Brains Paper

This proposal is itself a test case of the claim that C2A2 is a Thousand Brains system. The developmental maturity model provides the measurement framework: if the system progresses from Stage 0 through Stage 5 — with measurable improvements in consensus quality, cross-tradition signal fidelity, and the health metric r — that is evidence for the structural homology's fecundity. If progress stalls, the mapping was a surface analogy.

The health metric r gives us a way to measure not just that the system works, but *how* it works: whether traditions maintain genuine internal identity (r > 1) while still engaging productively across boundaries (r < ∞). This is the beginning of an operational theory of how C2A2 functions when healthy — a theory that can eventually be optimized, predicted, and controlled.

Agent 14a/14b will track the outcomes. Agent 15a/15b will test the underlying assumptions. Agent 15c will make disposition decisions. Agent 16 will ensure nothing falls through the cracks. The system is now watching itself — and closing its own loops.
