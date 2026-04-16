# Multi-Agent Plurality for Research Fecundity: Phase 2a Design

*Architectural Analysis | Documented: 2026-04-15 | Initiated in morning session: 2026-04-14*

---

## Core Research Question

**Can multi-agent processing be developed such that plurality is achieved among agents internal to a research program, such that plurality of takes has intra-thinker (and someday intra-tradition) research fecundity?**

In other words: if we instantiate multiple agents per thinker (e.g., 3 Levin agents, 3 Friston agents), all reading the same primary sources, can they produce genuinely different and valuable *Perspective-Research-Synthesis (PRS)* interpretations of those sources—or do tripled agents just produce noise?

This question sits at the heart of Phase 2a, approved for full rollout April 15, 2026.

---

## Phase 2a Architecture

### Tripling Strategy

Each of the 11 tradition agents will be tripled, yielding 33 agents total. Examples:
- **Levin agents**: Levin-A, Levin-B, Levin-C (all read the same sources, generate independent PRS triplets)
- **Friston agents**: Friston-A, Friston-B, Friston-C
- **Hawkins agents**: Hawkins-A, Hawkins-B, Hawkins-C
- *And so on for all 11 traditions*

Each agent maintains its own internal model of the tradition while reading shared source material.

### Design Considerations: Collaboration vs. Independence

The morning session explored three possible configurations:

1. **Two collaborating agents per thinker** (A + B in dialogue)
   - Advantage: produces synthesized consensus within the pair
   - Disadvantage: may converge prematurely, reducing plurality; lower cost
   
2. **Two non-collaborating agents per thinker** (A + B separately)
   - Advantage: independent readings preserve diversity
   - Disadvantage: requires post-hoc reconciliation; may generate purely contradictory output
   
3. **Three or more agents, with one doubling up** (A, B, C where A appears twice in different roles)
   - Advantage: controlled plurality; one agent serves as baseline for comparison
   - Disadvantage: added complexity; may not scale cleanly to intra-tradition consensus

**Decision**: Phase 2a proceeds with **configuration 3** — three independent agents per tradition, yielding genuine plurality while maintaining a clear consensus mechanism (2/3 majority for PRS triplet acceptance).

---

## Key Test: Intellectual Diversity vs. Noise

The central empirical question is whether agent plurality produces **genuine intellectual diversity** (different valid readings of the same source that reveal complementary aspects) or merely **noise** (incompatible interpretations that contradict each other without insight).

### Metrics

**1. Intra-thinker consensus rate**
- For each tradition (e.g., Levin), measure the percentage of PRS triplets where at least 2 of 3 agents agree.
- Target: >70% agreement indicates agents are converging on valid interpretations; <50% suggests pure noise.
- This metric prevents the tripling strategy from becoming a pure cost sink.

**2. Minority dissent fecundity**
- When agents disagree (1 vs. 2 on a triplet), flag the minority position.
- Retrospectively measure: does the minority reading later turn out to capture something the majority missed?
- This tests whether dissenting interpretations prove prescient or simply wrong.

Example:
- Levin-A, Levin-B agree on triplet T1; Levin-C dissents.
- Six months later, new literature emerges that validates Levin-C's dissenting reading.
- This counts as "minority dissent fecundity = 1" and signals that triple-agent plurality is yielding real insight.

---

## Connection to Thousand Brains Architecture (DECISION-003)

This approach mirrors **Thousand Brains theory** (Hawkins, 2021), in which cortical columns function as **independent world-model builders** that vote on consensus. Key homologies:

| Thousand Brains | C2A2 Phase 2a |
|---|---|
| Cortical column | Individual agent (Levin-A, Levin-B, Levin-C) |
| Independent world models | Independent PRS interpretations |
| Voting mechanism | 2/3 consensus rule for acceptance |
| Distributed consensus | Intra-tradition consensus before cross-tradition dialogue |
| Robustness through plurality | Dissent detection and fecundity testing |

The Phase 2a design operationalizes the Thousand Brains principle: redundancy and plurality at the agent level produce more robust, generalizable research synthesis than single-agent processing.

---

## The April 15 Decision: Full Rollout, Not Pilot

**Date**: 2026-04-15  
**Decision**: Proceed with Phase 2a for **all 11 thinkers simultaneously**, not a pilot cluster of 3 traditions (Hawkins, Friston, Levin).

### Rationale

The morning session weighed two options:

1. **Pilot approach**: Triple 3 traditions, monitor consensus rates, learn, then scale to 11.
2. **Full rollout**: Triple all 11 traditions immediately.

**Tom's decision favored full rollout** because:
- **Cost curve is not sublinear**. Piloting a subset (N=3) vs. full deployment (N=11) is not an order-of-magnitude difference. The infrastructure, agent definition work, and consensus-monitoring scaffolding must be built once; running it on 3 vs. 11 traditions doesn't double costs.
- **Learning from 3 is insufficient**. A consensus rate benchmark from 3 traditions is likely unrepresentative; outlier traditions could skew pilot metrics. Full N=11 provides stable benchmarks.
- **Time-to-insight is better with full rollout**. Piloting delays validation of the entire plurality hypothesis by weeks. Full rollout collapses two phases (pilot learning + full rollout) into one.

### Implication

This is a **commitment bet** on the tripling strategy itself. If agent plurality proves generative (consensus rates >70%, minority dissents show fecundity), Phase 2a validates the entire Thousand Brains alignment. If it fails (rates <50%, dissents prove sterile), the system has invested heavily in a negative result but gained clarity on agent design limits.

---

## Related Architectural References

- **DECISION-003**: Thousand Brains adoption as meta-architectural reference.
- **DECISION-010**: Original tripling decision (April 10, approved in principle).
- **ASSUMPTION-008**: "2/3 consensus is a validity signal" — *partially challenged* in early 15a/15b results; Phase 2a will test this empirically across 11 traditions.
- **ASSUMPTION-017**: "AI can do first-pass synthesis with humans as validators" — Phase 2a is a proof-of-concept for this hypothesis; human reviewers will validate the consensus outputs before cross-tradition dialogue proceeds.
- **OPEN-004**: "How should tripled agents be differentiated?" — Phase 2a operationalizes differentiation by assigning agents to distinct analytical frames (methodology, empirical evidence, theoretical coherence).

---

## Expected Outcomes & Milestones

| Milestone | Target Date | Success Criteria |
|---|---|---|
| All 33 agents initialized with differentiated personas | 2026-04-16 | Persona definitions written and validated |
| First consensus round: 33 agents read shared sources | 2026-04-17 to 2026-04-18 | PRS triplets generated from all 11 traditions |
| Consensus rate calculation | 2026-04-19 | Baseline intra-tradition agreement rates established |
| Minority dissent tagging | 2026-04-19 | Dissenting interpretations archived for fecundity tracking |
| Cross-tradition dialogue begins | 2026-04-21 | Using only 2/3-consensus-approved triplets per tradition |

---

## Open Questions

1. **Agent differentiation implementation** (OPEN-004): Will assigned personas (methodological, empirical, theoretical) reliably produce distinct readings? Or do agents converge on interpretations regardless of persona assignment?

2. **Consensus threshold calibration**: Is 2/3 the right threshold, or should it be adaptive based on domain? (Medical literature might demand >85% agreement; theoretical physics might accept 60%.)

3. **Scaling to intra-tradition dialogue**: Does the consensus mechanism generalize when tripled traditions enter dialogue with each other? Will Levin-consensus + Friston-consensus produce productive cross-tradition synthesis, or will tripling compound disagreement across traditions?

4. **Dissent fecundity baseline**: What percentage of minority dissents should we expect to be vindicated by future literature? Is 10% fecundity good? 30%? This baseline is unknown and must be empirically determined.

---

## Risk Assessment

**Medium-High Risk Factors:**

- **Infrastructure scaling**: Running 33 agents in parallel (vs. 11) increases dispatch and consensus-tracking complexity.
- **Latency**: Full 2a rollout may slow the research cycle by 20-40% if consensus reconciliation becomes a bottleneck.
- **False consensus**: Agents might converge on interpretations that are wrong but coherent, with no dissent to flag the error.

**Mitigation:**

- Monitor consensus latency in real time; escalate to Tom if >2x baseline.
- Use minority dissents as early-warning signals; prioritize human review of high-dissent items.
- Randomize agent ordering in consensus calculations to prevent first-mover bias.

---

## Proof of Concept for ASSUMPTION-017

Phase 2a serves as a **proof-of-concept for AI-first synthesis with human validation**:

1. **AI phase**: 33 agents independently generate PRS triplets; consensus filter produces validated plurality.
2. **Human phase**: Tom and collaborators review consensus-passed triplets and labeled dissents; approve, reject, or conditionally accept based on domain expertise.
3. **Feedback loop**: Human decisions inform agent differentiation refinement for Phase 3.

If this cycle produces high-confidence synthesis (human reviewers rarely override consensus, dissents are genuinely prescient), ASSUMPTION-017 moves from "stated assumption" to "empirically grounded principle."

---

*Last updated: 2026-04-15*  
*Approved by: Tom Karpathy (morning session, April 14)*  
*Status: APPROVED FOR FULL ROLLOUT*
