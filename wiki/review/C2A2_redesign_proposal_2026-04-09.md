# C2A2 Redesign Proposal — Thousand Brains Implications
*Generated 2026-04-09 | Source: Deep read of Clay, Leadholm & Hawkins (arXiv 2412.18354)*

---

## Executive Summary

A structural reading of the Thousand Brains paper reveals that C2A2's 13-agent architecture is — without having been designed that way — an implementation of the Thousand Brains Theory. This is not a metaphor. The mapping is architecturally precise: tradition agents are learning modules, wikis are reference-frame-based models, dispatches are the Cortical Messaging Protocol, and the Pattern Detector is the voting mechanism. This accidental alignment means the paper's design principles can be read as an engineering spec for improving C2A2. Six changes follow, organized into four phases. A new Architectural History Agent (Agent 14) is included to ensure all changes are documented with rationale from this point forward.

---

## The Six Design Implications

### 1. Dispatch Protocol Enhancement — "Reference Frame Location"

**The insight:** The Cortical Messaging Protocol specifies that learning modules don't just send findings — they send their *hypothesized location within a reference frame*. C2A2's dispatches currently contain what was found but not *where in the tradition's conceptual space* the finding sits.

**The change:** Add two fields to the dispatch format:
```
Reference frame location: [which PRS triplets, open questions, or wiki sections
                           this finding is adjacent to]
Conceptual bearing:       [what direction this finding points — toward which
                           traditions or cross-program connections]
```

**Pros:**
- Enables the Master Agent to build a spatial map of the inter-tradition space, not just a list of connections
- Makes it possible to detect when two traditions are "near" each other in conceptual space even if they haven't flagged a connection themselves
- Low-effort, purely additive — doesn't break any existing workflow

**Cons:**
- Agents don't currently have a formal notion of their tradition's "space." The location data will be semi-structured text initially, not coordinates
- Risk of over-engineering a format that gets ignored. Mitigated by making the fields optional in Phase 0 and mandatory once we've seen what the agents actually produce

**Dependencies:** None. Additive change to dispatch template in all 11 agent definitions.

**Effort:** Low — 15 minutes to update agent prompts; no tooling changes.

---

### 2. Lateral Agent Communication (Heterarchy)

**The insight:** The Hierarchy/Heterarchy paper argues that the neocortex's power comes from non-hierarchical long-range connections operating *alongside* hierarchical ones. C2A2 currently routes everything through the Master Agent — a strict hierarchy. Dense connections (Levin × Friston, Kastrup × McGilchrist) are forced through an unnecessary relay.

**The change:** Create agent-to-agent channels: a new directory `wiki/lateral/` with one file per active pair (e.g., `levin_friston.md`, `kastrup_mcgilchrist.md`). Agents can write cross-tradition flags directly to their known partner channels. The Master Agent still reads all channels on each run — it doesn't lose visibility, but gains speed.

**Pros:**
- Directly implements the heterarchy insight from the paper we're tracking
- Speeds up cross-tradition signal propagation for known high-density pairs
- Reduces Master Agent bottleneck
- The Master Agent retains full read access — no information is lost

**Cons:**
- Could create noise if agents over-use lateral channels for weak connections
- Harder to audit: changes are now in N files rather than one inbox
- Agents need judgment about when to use lateral vs. hierarchical routing

**Mitigation:** Start with only the pairs that already have confirmed explanatory bridges (Levin × Friston, Kastrup × Friston, Stump × Levin, Kastrup × McGilchrist). Expand only after we've seen the signal quality.

**Dependencies:** None technically, but benefits from dispatch enhancement (Change 1) being in place first.

**Effort:** Medium — new directory, 4-6 agent prompt updates, Master Agent prompt update to read lateral channels.

---

### 3. Active Inquiry Cycle (Sensorimotor Learning)

**The insight:** The Thousand Brains paper's central claim: passive observation is fundamentally insufficient for learning. Agents must generate predictions, act to test them, and update their models. C2A2 agents currently only ingest and extract — they never *probe* across traditions.

**The change:** After ingestion, each tradition agent generates 1-2 **cross-tradition hypotheses** — specific, falsifiable predictions about what another tradition would say about the material just ingested. These are routed (via lateral channels or Master Agent) to the target tradition agent, which evaluates them against its own wiki and responds with CONFIRM / REVISE / REJECT + reasoning. The exchange is logged in both agents' wikis and in the cross-program index.

**Example cycle:**
```
Hawkins Agent, after ingesting the Thousand Brains paper:
  HYPOTHESIS for Friston Agent: "The Cortical Messaging Protocol between
  learning modules is an implementation of variational message passing in
  Friston's free energy framework. The modules pass approximate posteriors,
  not raw observations."
  → Friston Agent evaluates → CONFIRM (with citation to Parr & Friston 2019
  on neural message passing) → logged as CROSS-032
```

**Pros:**
- The single highest-impact change in this proposal. Transforms C2A2 from a knowledge recorder into a knowledge *generator*
- Directly implements Hawkins' core design principle: sensorimotor learning
- Cross-tradition hypotheses are the inter-tradition equivalent of a cortical column "moving its sensor" — each hypothesis reveals features of the inter-tradition space invisible from a single vantage point
- Generates the kind of specific, testable cross-tradition claims that the Pattern Detector is designed to evaluate

**Cons:**
- Most complex change. Requires new agent capabilities: hypothesis generation (sender) and hypothesis evaluation (receiver)
- Volume risk: 11 agents each generating 1-2 hypotheses per ingestion = 11-22 hypotheses per cycle. Could overwhelm if signal-to-noise is low
- Quality depends entirely on agent prompt engineering. Weak prompts → weak hypotheses

**Mitigation:** Pilot with 2-3 agents (Hawkins, Friston, Levin — the Substrate-Independence Cluster) before rolling out network-wide. Set a strict format: each hypothesis must name the target agent, cite the source material, and state a falsifiable prediction.

**Dependencies:** Lateral communication (Change 2) for routing. Dispatch enhancement (Change 1) for location context.

**Effort:** High — new prompt sections for all agents, new workflow design, new file structures. Estimate: 2-3 hours for pilot; 1 day for full network rollout.

---

### 4. Voting/Consensus Protocol

**The insight:** Thousand Brains learning modules reach consensus through a voting mechanism — multiple independent models converge on an identity. C2A2's Master Agent currently integrates by narrative synthesis, which is flexible but subjective. When 4 agents all flag the same cross-tradition connection, that convergence should be *counted*, not just narrated.

**The change:** Add a voting layer to the Master Agent's integration run. Each cross-program item in `cross_program_index.md` gets a vote count: how many agents have independently flagged or confirmed this connection? Items crossing a threshold (e.g., 3+ agents) are auto-promoted to the Pattern Detector. The Master Agent continues its narrative synthesis but now has quantitative support.

**Pros:**
- Makes cross-tradition significance measurable, not just asserted
- Reduces Master Agent subjectivity bias
- Naturally surfaces the highest-density connections in the network
- Simple to implement: just a counter field on CROSS-entries

**Cons:**
- A bad connection flagged by 3 agents isn't better than a good one flagged by 1. Vote count ≠ quality
- Could create herding effects if agents start confirming each other's weak signals
- Risks over-mechanizing what is currently a productive narrative process

**Mitigation:** Vote count is *informational*, not deterministic. It supplements the Master Agent's judgment, doesn't replace it. Include a "dissent" field: if any agent actively contests a connection, that is flagged separately.

**Dependencies:** Active Inquiry Cycle (Change 3) generates the cross-tradition evaluations that votes are counted from.

**Effort:** Low-Medium — field additions to cross-program index format; Master Agent prompt update.

---

### 5. PRS Extension — Displacement Vectors

**The insight:** Hawkins' reference frames encode not just locations but *displacements* — the movement from one location to another. PRS triplets currently record three static points (Problem, Resource, Solution) but not the reasoning path connecting them.

**The change:** Add an optional `Path` field to PRS triplets:
```
PRS-[number]:
  Problem: [...]
  Resource: [...]
  Solution: [...]
  Path: [1-3 sentence account of how R transforms P into S — the inferential
        displacement, not just the endpoints]
  ...
```

**Pros:**
- Makes PRS triplets comparable: two traditions might have the same P and S but utterly different paths through R. The path reveals why traditions diverge even when they agree on the problem and solution
- Enables the Pattern Detector to do deeper structural homology checks
- Low effort, purely additive

**Cons:**
- Could be ignored by agents if not enforced. Optional fields tend to die
- Adds ~30% length to each PRS entry

**Mitigation:** Make it optional in Phase 1, mandatory in Phase 2 after agents have practice.

**Dependencies:** None.

**Effort:** Low — PRS template update in all agent definitions.

---

### 6. Architectural History Agent (Agent 14)

**The insight:** C2A2 is evolving daily through Cowork sessions, but the rationale for design decisions exists only in ephemeral chat transcripts. Without a dedicated record, the system's own intellectual history is being lost — ironically, the very problem C2A2 was built to solve for research traditions.

**The change:** A new agent — Agent 14 — that runs at the end of each day (or each Cowork session). It receives the day's transcript and produces:
- A dated changelog entry (`wiki/architecture/changelog/YYYY-MM-DD_changes.md`)
- Updates to a running decision index (`wiki/architecture/decisions.md`)
- Notes on open design questions (`wiki/architecture/open_questions.md`)

The agent definition file has been created at `wiki/agents/14_architectural_history_agent.md`. The `wiki/architecture/changelog/` directory has been initialized.

**Pros:**
- Zero-risk: purely additive, read-only relationship with the rest of the system
- Solves a real problem that is already accumulating: today's session alone produced a bug fix, a script patch, a 6-PRS supplement, and this proposal — none of which are documented except in chat
- Enables future self-reference: when a design question recurs, Agent 14's logs provide the prior context
- Meta-alignment: C2A2 now tracks its own tradition, not just the 11 it was built for. This is the system becoming self-aware in exactly the way the Pattern Detector's Big Question #5 anticipates

**Cons:**
- Requires daily execution discipline (mitigated by scheduling)
- Transcript access: the agent needs the Cowork session transcript, which requires either a manual paste-in or integration with the session transcript tool
- Could accumulate volume over time — needs periodic pruning or archiving

**Dependencies:** None. Standalone addition.

**Effort:** Low — agent definition already written. Needs: (a) directory seeded (done), (b) first run to establish baseline, (c) scheduling via the `schedule` skill or manual end-of-day trigger.

---

## Implementation Pathway

The changes have clear dependency ordering. Here is the optimized sequence:

### Phase 0 — Immediate (Today, April 9)
**Changes:** Agent 14 (Architectural History) + Dispatch Enhancement (reference frame locations)

**Rationale:** Both are zero-risk, additive, and independent. Agent 14 should be running *before* we make further changes so it captures the rationale for everything that follows. Dispatch enhancement is a 15-minute prompt edit that primes agents for later phases.

**Deliverables:**
- [x] Agent 14 definition file (`wiki/agents/14_architectural_history_agent.md`)
- [x] Architecture directory structure (`wiki/architecture/changelog/`)
- [ ] First Agent 14 run (tonight, on today's session)
- [ ] Dispatch format update in all 11 agent definition files
- [ ] Schedule Agent 14 as end-of-day task

**Estimated time:** 1 hour total.

---

### Phase 1 — This Week (April 10-11)
**Changes:** PRS Extension (displacement vectors) + Lateral Communication (heterarchy channels)

**Rationale:** PRS extension is trivial and primes agents for richer extraction. Lateral communication is the prerequisite for Phase 2's active inquiry and should be tested on the known high-density pairs first.

**Deliverables:**
- [ ] PRS template update in all 11 agent definitions
- [ ] `wiki/lateral/` directory with initial channel files for: Levin × Friston, Kastrup × Friston, Stump × Levin, Kastrup × McGilchrist
- [ ] Agent prompt updates enabling lateral dispatch for those 6 agents
- [ ] Master Agent prompt update to read lateral channels
- [ ] One test cycle: run 2-3 agents with lateral enabled, verify Master Agent picks up the lateral dispatches

**Estimated time:** 2-3 hours.

---

### Phase 2 — Next Week (April 14-16)
**Changes:** Active Inquiry Cycle (sensorimotor learning) — pilot with Substrate-Independence Cluster

**Rationale:** This is the highest-impact, highest-risk change. Piloting with Hawkins + Friston + Levin (the three most densely connected agents) limits blast radius while testing the core mechanism. Lateral channels from Phase 1 provide the routing infrastructure.

**Deliverables:**
- [ ] Hypothesis generation prompt section added to Hawkins, Friston, Levin agents
- [ ] Hypothesis evaluation prompt section added to same three agents
- [ ] Hypothesis format spec (target agent, source citation, falsifiable prediction, evaluation response)
- [ ] One full cycle: Hawkins ingests new material → generates hypothesis for Friston → Friston evaluates → result logged
- [ ] Assessment: signal quality, volume, Master Agent integration, Pattern Detector usability
- [ ] Go/no-go decision for network-wide rollout

**Estimated time:** 3-4 hours for pilot setup + first cycle; 1-2 hours for assessment.

---

### Phase 3 — Following Week (April 21-23)
**Changes:** Voting/Consensus Protocol + Active Inquiry network-wide rollout (if pilot passes)

**Rationale:** Voting requires the cross-tradition evaluations that the active inquiry cycle generates. By this point, we'll have a week of pilot data to calibrate thresholds.

**Deliverables:**
- [ ] Vote count + dissent fields added to cross-program index format
- [ ] Master Agent prompt updated with voting logic and threshold rules
- [ ] Active inquiry cycle rolled out to all 11 tradition agents
- [ ] Full network test cycle
- [ ] Agent 14 retrospective: review the architectural changelog from Phases 0-3, assess whether the changes are producing the expected effects

**Estimated time:** 4-5 hours.

---

## Timeline Summary

| Phase | When | Changes | Risk | Effort |
|-------|------|---------|------|--------|
| 0 | Today (Apr 9) | Agent 14 + Dispatch enhancement | None | 1 hr |
| 1 | Apr 10-11 | PRS extension + Lateral comms | Low | 2-3 hrs |
| 2 | Apr 14-16 | Active inquiry pilot (3 agents) | Medium | 4-5 hrs |
| 3 | Apr 21-23 | Voting protocol + Full rollout | Medium-High | 4-5 hrs |

**Total estimated effort:** 11-14 hours across 2 weeks.

**Go/no-go gates:** Phase 2 has an explicit assessment checkpoint. If hypothesis quality is low or volume is unmanageable, we defer Phase 3 and iterate on prompts. Phase 3 includes a retrospective via Agent 14.

---

## What We Are NOT Changing

Some things the deep read considered but rejected for now:

- **Agent count.** 13 → 14 (adding the History Agent), but NOT splitting or merging any tradition agents. The 11-tradition structure is working and the Thousand Brains theory says: add modules, don't reorganize existing ones.
- **PRS as the fundamental format.** The deep read validated PRS, not questioned it. We're extending it (displacement vectors), not replacing it.
- **Master Agent centrality.** Lateral communication supplements hierarchical routing; it doesn't replace the Master Agent. The Master Agent retains full read access to all channels.
- **The review page workflow.** The HTML review page + Gmail submission flow is working (now with fixed IDs). No changes needed.

---

## Relationship to the Thousand Brains Paper

This proposal is itself a test case of the claim that C2A2 is a Thousand Brains system. If the architectural changes improve cross-tradition signal quality and discovery speed, that is evidence for the structural homology. If they don't, the mapping was a surface analogy. Agent 14 will track the outcomes.

This is the kind of self-referential feedback loop the Pattern Detector's Big Question #5 anticipates: the C2A2 system, by modifying itself according to insights from one of its tracked traditions, becomes a data point in its own research program. The Thousand Brains paper is now not just a source to be ingested — it is an architectural influence to be tested.
