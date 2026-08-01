# C2A2 Revision Flags
**Items requiring human (Tom's) review | Initialized: 2026-04-13**

*These items have been flagged for REVISE based on net evaluation. They require human decision-making about whether to abandon, modify, or replace the premises. Items are ordered by urgency.*

---

## CRITICAL & HIGH URGENCY ITEMS

---

### REVISE-001:
**Date flagged:** 2026-04-13
**Source item:** PRESUMPTION-013
**Item type:** PRESUMPTION
**Urgency:** HIGH (Evidence of existing failure)

**Statement:**
"Infrastructure failures caught before compounding"

**What is at risk:**
- System reliability
- Data quality during failure periods
- Research continuity
- Trust in automation system

**Evidence summary:**
This presumption has already been violated. A 4-day infrastructure failure occurred without detection or containment. The system failed to meet its own reliability presumption. 15a acknowledges silent failures are a known risk; 15b documents the failure happened.

**Recommended action:**
1. **Immediate (this week):** Implement explicit monitoring and alerting for infrastructure health
2. **This month:** Reduce failure detection latency from 4 days to <1 hour maximum
3. **This month:** Implement automated failover for critical components (prevent single points of failure)
4. **This month:** Add redundancy for critical infrastructure (e.g., backup message queues, failover databases)
5. **Ongoing:** Monitor infrastructure health metrics weekly

**Implementation notes:**
- Use standard infrastructure monitoring tools (e.g., Prometheus, Grafana for visibility)
- Set up alerts for system degradation (don't wait for complete failure)
- Document RTO/RPO targets for critical components
- Test failover procedures monthly

**Status:** ADDRESSED (2026-04-15) — Wiki auth fixed, git locks cleared, OPEN-012 resolved. Monitoring recommendation accepted as operational improvement; not architectural blocker.

**Priority:** Highest (System is currently at risk)

---

### REVISE-002:
**Date flagged:** 2026-04-13
**Source item:** PRESUMPTION-011
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:**
"Agent quality filters sufficient without calibration"

**What is at risk:**
- Agent quality assurance
- Output reliability
- Any decision depending on quality filters
- System integrity

**Evidence summary:**
15a finds no support for claims that uncalibrated filters are sufficient (NO-SUPPORT-FOUND, contradicting). 15b confirms that uncalibrated filters are ineffective. This is a design error: filters without calibration cannot reliably distinguish good from poor outputs.

**Recommended action:**
1. **This week:** Audit all quality filters currently in use (identify which are uncalibrated)
2. **This month:** Implement calibration protocols for all filters:
   - Define ground truth or acceptable baseline
   - Measure filter sensitivity/specificity against ground truth
   - Adjust thresholds based on calibration results
   - Document threshold justifications
3. **Ongoing:** Re-calibrate quarterly as output distributions change

**Implementation notes:**
- Calibration requires labeled data (correct vs. incorrect outputs)
- Consider ROC curve analysis to choose optimal thresholds
- Document false positive vs. false negative tradeoffs
- Consider separate thresholds for different decision types

**Status:** DEFERRED TO PHASE 2A (2026-04-15) — Tripling provides natural calibration: compare 3 agents' filter decisions on same sources. Revisit with Phase 2a data.

**Priority:** High (Quality control is foundational)

---

### REVISE-003:
**Date flagged:** 2026-04-13
**Source item:** ASSUMPTION-011
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:**
"Specialist-first/orchestrator-fallback is right division of labor"

**What is at risk:**
- Division of labor between specialists and orchestrator
- Sequential task handling (critical for research pipelines)
- System robustness
- Agent 16's reliability on dependent tasks

**Evidence summary:**
FOR shows modest improvement on parallel tasks (20% makespan gain). AGAINST shows critical degradation on sequential tasks (39-70% performance drop). The brittleness on sequential dependencies is unacceptable for research automation reliability.

**Recommended action:**
1. **This week:** Identify all sequential task dependencies in Agent 16 pipeline
2. **This week:** Test specialist outputs on sequential chains (measure actual degradation)
3. **This month:** Revise division of labor:
   - Use specialists for truly independent parallel subtasks
   - Add orchestrator verification for sequential task outputs
   - Implement fallback/repair mechanisms for degraded sequential performance
4. **This month:** Design sequential robustness testing:
   - Create test chains with 3-5 dependent steps
   - Benchmark current vs. revised architecture
   - Target <10% degradation on sequential chains

**Implementation notes:**
- Specialists may be efficient for isolated tasks but need validation when outputs feed into other tasks
- Consider orchestrator pre-checking specialist outputs before passing to next task
- May need to revert to unified agents for critical sequential chains

**Status:** DISMISSED (2026-04-15) — Literature finding (39-70% degradation) pertains to task-decomposition specialists, not C2A2's tradition agents. Framing does not apply to this architecture.

**Priority:** High (Architecture affects all Agent 16 operations)

---

### REVISE-004:
**Date flagged:** 2026-04-13
**Source item:** ASSUMPTION-004
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:**
"Self-awareness scales with decision complexity not agent count"

**What is at risk:**
- Current 3-agent team design (15a, 15b, 15c)
- Multi-agent scaling assumptions
- Oversight and coordination effectiveness
- Future team expansion plans

**Evidence summary:**
15a concedes agent count has independent effects. 15b provides specific empirical threshold: coordination overhead saturates at N≈4. The assumption is false — both complexity AND agent count matter independently.

**Recommended action:**
1. **This month:** Measure coordination costs in current 3-agent team (15a, 15b, 15c)
   - Time spent on cross-agent communication
   - Overhead of consensus-building
   - Opportunity costs vs. independent work
2. **This month:** Revise assumption to: "Self-awareness scales with decision complexity AND coordination overhead (which scales with N, with saturation observed at N≈4)"
3. **This month:** Design safeguards for N>4:
   - Hierarchical coordination for larger teams
   - Explicit subteams to break coordination bottlenecks
   - Monitoring for saturation effects
4. **Quarterly:** Re-evaluate if team expands beyond N=4

**Implementation notes:**
- N=3 is below saturation point but not immune to coordination costs
- Document actual coordination overhead to validate empirical threshold
- Consider whether current 3-agent structure is optimal or could be improved

**Status:** ACCEPTED (2026-04-15) — Assumption revised to: "Self-awareness scales with both decision complexity AND coordination overhead (saturation at N≈4)." Current N=3 is safe; revisit if team expands.

**Priority:** High (Fundamental architectural assumption)

---

## MEDIUM URGENCY ITEMS

---

### REVISE-005:
**Date flagged:** 2026-04-13
**Source item:** PRESUMPTION-007
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:**
"Literature absence = NOVEL"

**What is at risk:**
- Classification of novel research conditions
- Agent 16 detection of novel situations
- PRESUMPTION-010 validity (Agent 16 detection depends on this)
- Entire "novelty detection" strategy

**Evidence summary:**
15a explicitly contradicts (publication bias makes literature absence unreliable indicator). 15b confirms: file drawer problem and systematic publication gaps mean absence indicates nothing about novelty. This is a fundamental logical error.

**Recommended action:**
1. **Immediately:** Revise premise to: "Literature absence MAY indicate novelty but could also reflect publication bias, file drawer problem, or systematic coverage gaps. Absence alone is insufficient."
2. **This week:** Revise Agent 16 novelty detection:
   - Require ADDITIONAL evidence beyond literature absence (theoretical novelty, methodological novelty, empirical novelty)
   - Implement multi-factor novelty assessment
   - Don't use literature gaps as primary signal
3. **This month:** Define what counts as "novel" with explicit criteria:
   - Contradicts prior research findings
   - Uses novel methods not seen in literature
   - Applies to new domain/context
   - Proposes new theory/mechanism
4. **Quarterly:** Validate novelty classifications against expert judgment

**Implementation notes:**
- Publication bias is well-documented in social science — assume it exists
- File drawer problem means negative findings are systematically underrepresented
- Literature absence is weak evidence; use it only as secondary signal
- Novel research often gets published first (paradox), so presence/absence is unreliable

**Status:** SUPERSEDED (2026-04-15) — Addressed by kuhnian_evidence_framework.md. Literature absence now interpreted contextually: Pattern 3 (Mixed FOR + Faint AGAINST) = paradigm-shift signal, not weakness. NOVEL status replaced by contextual interpretation.

**Priority:** High (Foundational error in novelty detection logic)

---

### REVISE-006:
**Date flagged:** 2026-04-13
**Source item:** ASSUMPTION-010
**Item type:** ASSUMPTION
**Urgency:** MEDIUM

**Statement:**
"Finite typology of connecting memes exists"

**What is at risk:**
- Classification scheme for connecting memes
- Expectation of typology completion or closure
- Categorization of novel analogies
- Cross-tradition analogy detection

**Evidence summary:**
FOR shows patterns exist but typology is unvalidated. AGAINST notes that analogy-making is unbounded and new types emerge continuously. The set of connecting memes is generative/open-ended, not finite/closed.

**Recommended action:**
1. **This month:** Revise assumption to: "Recognizable families of connecting memes exist and can be identified, but the typology is open-ended. New types emerge through novel analogy-making."
2. **This month:** Implement classification system as taxonomy that grows with use:
   - Document observed meme families
   - Establish criteria for new types
   - Allow taxonomy to expand
   - Track emergence of new types
3. **Quarterly:** Review typology evolution and emerging patterns

**Implementation notes:**
- Don't expect to find all possible meme types upfront
- Use open-ended categorization (machine learning cluster, not closed taxonomy)
- Be prepared for novel analogies that don't fit existing categories
- Track which novel meme types emerge and how often

**Status:** ACCEPTED (2026-04-15) — Assumption revised to open-ended taxonomy: "Recognizable families of connecting memes exist and can be identified, but the typology is open-ended. New types emerge through novel analogy-making."

**Priority:** Medium (Affects classification but not fundamental)

---

### REVISE-007:
**Date flagged:** 2026-04-13
**Source item:** PRESUMPTION-006
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:**
"Developmental stages monotonic"

**What is at risk:**
- Models assuming linear developmental progression
- Agent 16 scheduling assumptions if they assume monotonic progress
- Research progress models
- Expectations about system maturation

**Evidence summary:**
15a explicitly contradicts (NO-SUPPORT-FOUND, contradicting). 15b concurs: non-linear development is the norm. Development includes cycles, reversals, plateaus — not monotonic improvement.

**Recommended action:**
1. **This month:** Remove the presumption entirely (it's contradicted by evidence)
2. **This month:** If development models are needed, incorporate non-linearity:
   - Allow for cycles and reversals
   - Accept plateaus and regressions
   - Recognize phase transitions
   - Model feedback loops
3. **Quarterly:** Monitor actual development patterns to validate model

**Implementation notes:**
- Examples of non-monotonic development: skill learning (plateaus), system performance (regressions during refactoring), research progress (paradigm shifts reverse prior work)
- Don't assume systems always get better with time
- Plan for maintenance, adaptation, and occasional backtracking

**Status:** ACCEPTED (2026-04-15) — Non-linearity acknowledged. Maturity model stages can be revisited. Already demonstrated empirically when Phase 2a was paused and then unpaused.

**Priority:** Medium (Affects expectations but correctable)

---

## SUMMARY TABLE

| Item | Premise | Type | Urgency | Key Risk | Recommended First Action |
|------|---------|------|---------|----------|------------------------|
| REVISE-001 | Infrastructure failures caught | PRESUMPTION | HIGH | System unreliability | Implement monitoring/alerting |
| REVISE-002 | Quality filters sufficient | PRESUMPTION | HIGH | Quality control failure | Audit and calibrate filters |
| REVISE-003 | Specialist/orchestrator division | ASSUMPTION | HIGH | Sequential task brittleness | Test degradation on chains |
| REVISE-004 | Self-awareness scales with complexity | ASSUMPTION | HIGH | Team coordination | Measure N=3 overhead |
| REVISE-005 | Literature absence = NOVEL | PRESUMPTION | HIGH | Novelty detection error | Revise to multi-factor assessment |
| REVISE-006 | Finite meme typology | ASSUMPTION | MEDIUM | Classification completeness | Revise to open-ended taxonomy |
| REVISE-007 | Developmental stages monotonic | PRESUMPTION | MEDIUM | Expectation management | Remove or replace with non-linear model |

---

## NEXT STEPS

**Agent 15c recommends:**

1. **Week of 2026-04-13 (THIS WEEK):**
   - Review all HIGH urgency items (REVISE-001 through REVISE-005)
   - Prioritize REVISE-001 (infrastructure failures) — system is currently at risk
   - Make decision: revise, abandon, or mitigate each premise

2. **Week of 2026-04-20:**
   - Implement immediate fixes for accepted revisions
   - Report back with revised premises
   - Schedule architecture review meeting

3. **Ongoing:**
   - Update ASSUMPTIONS and PRESUMPTIONS documents with revisions
   - Brief Agent 14a/14b on changes
   - Update agent instruction sets accordingly
   - Incorporate revised premises into system design

---

**Status:** All 7 items AWAITING-REVIEW
**Total ASSUMPTIONS flagged for revision:** 3
**Total PRESUMPTIONS flagged for revision:** 4
**Total with HIGH urgency:** 5
**Total with MEDIUM urgency:** 2

**Document prepared by Agent 15c**
**Ready for human review and decision-making**

---
---

## ITEMS ADDED — Second Cycle (2026-04-13 evening)

*4 new REVISE items from 15c dispositions (DISPOSITION-029, 030, 031, 032)*

---

### REVISE-008:
**Date flagged:** 2026-04-13
**Source item:** PRESUMPTION-015
**Item type:** PRESUMPTION
**Urgency:** HIGH (Fundamental logical limitation)

**Statement:**
"Self-awareness pipeline can evaluate claims about itself without circularity"

**What is at risk:**
- Epistemic integrity of all dispositions concerning the pipeline's own design
- Specifically: dispositions for ASSUMPTION-003, PRESUMPTION-005, and ASSUMPTION-015 are self-referential
- False confidence in pipeline validity based on circular self-assessment

**Evidence summary:**
Both 15a (no support found — contradicted by Gödel, bootstrapping problem) and 15b (challenged — Gödel's Second Incompleteness Theorem, LLM self-consistency research) converge. No supporting literature exists. Mathematical logic establishes this as a formal impossibility: no consistent system can prove its own consistency.

**Recommended action:**
1. **Immediate:** Mark all self-referential dispositions (ASSUMPTION-003, PRESUMPTION-005, ASSUMPTION-015) as PRELIMINARY — subject to external validation
2. **This week:** Have Tom independently assess the self-referential items using his own judgment (not the pipeline's results)
3. **This month:** Design external validation mechanism — either a neutral single-agent evaluator or human review panel for self-referential items
4. **Ongoing:** Any item where the pipeline evaluates a claim about itself should be automatically flagged for external review

**Status:** ACCEPTED IN PRINCIPLE (2026-04-15) — Self-referential dispositions (ASSUMPTION-003, PRESUMPTION-005, ASSUMPTION-015) marked PRELIMINARY. Human triage session (this session) serves as external validation mechanism. Automatic flagging of self-referential items accepted.

**PROVENANCE:**
  Origin: 14b
  Chain: [14b → 15a, 15b → 15c]
  Current status: REVISION-FLAGGED

---

### REVISE-009:
**Date flagged:** 2026-04-13
**Source item:** PRESUMPTION-016
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (Methodological limitation affecting all dispositions)

**Statement:**
"Single-day literature search is sufficient for reliable dispositioning"

**What is at risk:**
- Stability of all 32 dispositions (25 prior + 7 current)
- INCORPORATE items may flip on second pass
- REVISE items may be false positives from narrow search

**Evidence summary:**
15a found no support (contradicted by systematic review methodology standards requiring multi-pass, multi-database search). 15b confirmed with moderate-strong evidence (PRISMA-S standards, rapid review limitations). Single-day search is a known methodological weakness with documented risks of incomplete evidence synthesis.

**Recommended action:**
1. **Immediate:** Label all dispositions as "rapid review — preliminary" in relevant files
2. **This month:** Plan second-pass searches on INCORPORATE and REVISE items using alternative search strategies and different search terms
3. **Ongoing:** Track disposition stability across cycles — if dispositions change significantly on second pass, single-day search is confirmed insufficient
4. **Note:** This finding is self-referential (this very search was single-day) — treat with appropriate epistemic caution per REVISE-008

**Status:** ACCEPTED AS STANDING CAVEAT (2026-04-15) — All dispositions labeled "rapid review — preliminary." 15d re-evaluation cycle provides iterative improvement. No blocking action needed.

**PROVENANCE:**
  Origin: 14b
  Chain: [14b → 15a, 15b → 15c]
  Current status: REVISION-FLAGGED

---

### REVISE-010:
**Date flagged:** 2026-04-13
**Source item:** PRESUMPTION-017
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (Data integrity issue — partially addressed by 15d)

**Statement:**
"Data consistency discrepancies in pipeline are cosmetic, not structural"

**What is at risk:**
- Data integrity of monitor_queue.md and downstream monitoring
- Items may be silently dropped from surveillance
- Compounding errors in future pipeline runs

**Evidence summary:**
15a provided only weak support (and that support was for investigating, not dismissing). 15b provided strong evidence that small count discrepancies are sentinel events in data engineering — ArXiv SDC research, enterprise pipeline failure documentation. Both directions agree the discrepancy warrants investigation. Note: Agent 15d partially addressed this by adding 4 missing items (correcting 13 → 17), but root cause was not identified.

**Recommended action:**
1. **Immediate:** Audit the full data flow from 15c dispositions through to monitor_queue.md and revision_flags.md
2. **This week:** Identify root cause of the original 2-item discrepancy (was it a write error, filter error, or categorization error?)
3. **This month:** Implement count assertions at each pipeline stage — halt downstream on any discrepancy
4. **Ongoing:** Monitor for recurrence in future pipeline cycles

**Status:** ACCEPTED (2026-04-15) — Root cause investigation warranted but low urgency (15d already corrected count). Count assertions at each pipeline stage accepted as engineering improvement.

**PROVENANCE:**
  Origin: 14b
  Chain: [14b → 15a, 15b → 15c]
  Current status: REVISION-FLAGGED

---

### REVISE-011:
**Date flagged:** 2026-04-13
**Source item:** PRESUMPTION-018
**Item type:** PRESUMPTION
**Urgency:** HIGH (Operational reliability risk)

**Statement:**
"Chat conversation serves as reliable inter-session memory channel"

**What is at risk:**
- Fidelity of evening-to-morning handoff
- 4 primed discussion topics from evening sync may not all surface in morning walk
- Critical items may be lost across session boundaries
- Trust in operational workflow

**Evidence summary:**
Both 15a (no support — LLMs are stateless, no native inter-session memory) and 15b (challenged — context rot degrades accuracy 30%+, no cross-session persistence) converge. This is directly contradicted by LLM architecture. The evening sync to Claude Chat treats Chat as a database; in reality, Chat is an LLM with context window constraints and no guaranteed inter-session retrieval.

**Recommended action:**
1. **Immediate:** Write evening sync summaries to a persistent wiki file (e.g., wiki/architecture/session_handoffs/YYYY-MM-DD_handoff.md)
2. **This week:** Morning walk sessions should explicitly load the handoff file rather than relying on Chat memory
3. **This month:** Track handoff fidelity — compare morning walk discussion topics against evening sync delivery
4. **Ongoing:** Use wiki as canonical inter-session memory; Chat as supplement only

**Status:** ACCEPTED (2026-04-15) — Wiki is canonical inter-session memory; Chat is supplemental. Already partially implemented via daily_sync/chat_to_cowork files. Formalized as standing practice.

**PROVENANCE:**
  Origin: 14b
  Chain: [14b → 15a, 15b → 15c]
  Current status: REVISION-FLAGGED

---

---

## ITEMS ADDED — Third Cycle (2026-04-14)

*5 new REVISE items from 15c dispositions (DISPOSITION-038–042)*

---

### REVISE-012:
**Date flagged:** 2026-04-14
**Source item:** PRESUMPTION-019
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "Bibliometric signals are reliable proxies for genuine intellectual convergence"

**What is at risk:**
- Paradigm shift detector (proposed tool) would be built on these signals
- Cross-tradition convergence measurement
- Validation of FINDING-011 through bibliometric evidence

**Evidence summary:** Bibliometric signals are corrupted proxies due to citation gaming, strategic co-authorship, and Goodhart's Law. Cross-field convergence signals particularly vulnerable. 15a found moderate support within disciplines; 15b found strong challenge due to gaming and Goodhart effects.

**Recommended action:**
1. Do NOT build paradigm shift detector on raw bibliometric signals alone
2. Shift from metric-level to citation-level analysis (check substantive engagement in individual citations)
3. Require semantic validation alongside any bibliometric evidence
4. Manually sample Hoffman-Friston-Levin cross-citations for substantive vs. perfunctory engagement

**Status:** SUPERSEDED (2026-04-15) — Addressed by kuhnian_evidence_framework.md. Framework already requires semantic validation alongside bibliometric evidence. Raw bibliometric signals alone insufficient; citation-level substantive engagement analysis required.

---

### REVISE-013:
**Date flagged:** 2026-04-14
**Source item:** PRESUMPTION-020
**Item type:** PRESUMPTION
**Urgency:** HIGH (threatens C2A2's value proposition)

**Statement:** "AI synthesis is qualitatively complementary to human synthesis"

**What is at risk:**
- C2A2's entire value proposition as AI-driven interdisciplinary science
- ASSUMPTION-017 (AI synthesis + human validation model)
- Quality of all cross-tradition findings including FINDING-011

**Evidence summary:** No support for qualitative complementarity. Strong evidence that LLM synthesis is "biased acceleration" — same pattern-matching process as humans but faster and with overconfidence. LLMs systematically overgeneralize, creating false analogies. Especially dangerous for theoretical synthesis like FINDING-011.

**Recommended action:**
1. Reframe AI synthesis explicitly as "hypothesis generation" not "discovery"
2. Implement mandatory falsification testing before any finding is elevated
3. Compare AI-generated connections against expert-generated ones to measure false-positive rate
4. Add explicit AI bias disclaimer to all C2A2 findings

**Status:** ACCEPTED (2026-04-15) — AI synthesis relabeled as "hypothesis generation" not "discovery." Consistent with ASSUMPTION-017 (human as validator). Add disclaimer language to findings metadata. Does not undermine C2A2's value proposition; reframes it more precisely.

---

### REVISE-014:
**Date flagged:** 2026-04-14
**Source item:** PRESUMPTION-021
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "Internal depth assessment of findings is reliable without external calibration"

**What is at risk:**
- FINDING-011 triple-flag credibility
- All internal quality assessments
- System's ability to prioritize findings

**Evidence summary:** Internal assessment is systematically unreliable without external calibration (Dunning-Kruger analog). Triple-flag may indicate internal consistency (fits C2A2's framework) rather than actual depth. Models cannot reliably self-correct intrinsically.

**Recommended action:**
1. Submit FINDING-011 to external domain experts in Hoffman, Friston, and Levin traditions
2. Make internal assessment criteria explicit, objective, and pre-specified
3. Do not publish or heavily prioritize findings based solely on internal assessment
4. Establish external calibration benchmark (compare internal ratings with expert ratings)

**Status:** IN PROGRESS (2026-04-15) — External calibration email sent to Kastrup, Hoffman, Friston (cc Levin) today. Awaiting responses. Internal assessment stands as preliminary pending external validation.

---

### REVISE-015:
**Date flagged:** 2026-04-14
**Source item:** PRESUMPTION-022
**Item type:** PRESUMPTION
**Urgency:** HIGH (mirrors proposal review bottleneck at meta-level)

**Statement:** "REVISE backlog is bounded and manageable"

**What is at risk:**
- Self-awareness pipeline actionability
- REVISE items accumulating without review
- Pipeline generating problems it cannot close

**Evidence summary:** Technical debt and queue theory predict unbounded growth when generation > review rate. Industry baseline: ~5% review rate. REVISE grew from 7→11→16 across three cycles with zero items reviewed. The pattern mirrors the proposal review bottleneck (ASSUMPTION-012) at meta-level.

**Recommended action:**
1. Set hard cap on REVISE backlog (e.g., max 25 items)
2. Implement automatic pipeline slowdown if backlog exceeds cap
3. Dedicate at least 15% of session time to REVISE triage
4. Consider batch review: group related REVISE items (e.g., all FINDING-011-related items together)
5. Track queue growth rate vs. review rate explicitly

**Status:** ADDRESSED (2026-04-15) — Batch triage model proven effective this session (16 items in ~10 min). Formalize batch triage as standing practice: 15% of session time. REVISE backlog is bounded when review process matches generation cadence.

---

### REVISE-016:
**Date flagged:** 2026-04-14
**Source item:** PRESUMPTION-023
**Item type:** PRESUMPTION
**Urgency:** HIGH (active infrastructure vulnerability)

**Statement:** "Three concurrent infrastructure failures are independent incidents"

**What is at risk:**
- System reliability and uptime
- Research workflow continuity
- If correlated, individual fixes won't prevent recurrence

**Evidence summary:** Both 15a and 15b found evidence that concurrent infrastructure failures are typically correlated, not independent. Common-cause mechanisms: shared infrastructure, credential lifecycle, cascading overload. The presumption of independence requires positive evidence, not absence of evidence.

**Recommended action:**
1. Conduct full incident analysis for each failure: root cause, shared dependencies, ripple effects
2. Map shared infrastructure: do git, Gmail, and wiki share authentication, network, or credential infrastructure?
3. Test cascading: deliberately trigger one failure; measure effects on others
4. Implement circuit breakers and monitoring for shared dependencies
5. Set SLOs for critical infrastructure uptime

**Status:** CLOSED (2026-04-15) — P-023 downgraded to LOW risk. Two of three failures were routine operational friction (git locks, Gmail session). Wiki auth was the substantive issue. No evidence of correlation. Individual fixes appropriate.

---

**Updated summary (2026-04-14):**
**Total REVISE items:** 16 (11 prior + 5 new from 2026-04-14 cycle)
**New ASSUMPTIONS flagged:** 0
**New PRESUMPTIONS flagged:** 5 (PRESUMPTION-019, 020, 021, 022, 023)
**New with HIGH urgency:** 5

---

## TRIAGE SESSION — 2026-04-15

**All 16 items triaged by Tom in batch review.**

| Item | Decision | Notes |
|------|----------|-------|
| REVISE-001 | ADDRESSED | Infrastructure fixed today |
| REVISE-002 | DEFERRED | To Phase 2a (calibration via tripling) |
| REVISE-003 | DISMISSED | Literature doesn't apply to C2A2's architecture |
| REVISE-004 | ACCEPTED | Assumption reworded (complexity + coordination overhead) |
| REVISE-005 | SUPERSEDED | By Kuhnian evidence framework |
| REVISE-006 | ACCEPTED | Open-ended taxonomy |
| REVISE-007 | ACCEPTED | Non-linearity acknowledged |
| REVISE-008 | ACCEPTED IN PRINCIPLE | Self-referential items flagged PRELIMINARY |
| REVISE-009 | ACCEPTED AS CAVEAT | All dispositions "rapid review — preliminary" |
| REVISE-010 | ACCEPTED | Count assertions as engineering improvement |
| REVISE-011 | ACCEPTED | Wiki = canonical memory, Chat = supplement |
| REVISE-012 | SUPERSEDED | By Kuhnian evidence framework |
| REVISE-013 | ACCEPTED | AI synthesis = "hypothesis generation" not "discovery" |
| REVISE-014 | IN PROGRESS | External calibration email sent; awaiting responses |
| REVISE-015 | ADDRESSED | Batch triage proven effective; formalized as practice |
| REVISE-016 | CLOSED | P-023 downgraded; no correlation evidence |

**AWAITING-REVIEW count: 0 (all 16 triaged)**
**Reviewed by: Tom (2026-04-15 afternoon session)**

**Document updated: 2026-04-15**

---
---

## ITEMS ADDED — Fifth Cycle (2026-04-15)

*4 new REVISE items from 15c dispositions*

---

### REVISE-017:
**Date flagged:** 2026-04-15
**Source item:** ASSUMPTION-027
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:** "Batch REVISE triage (16 items in one pass) produces adequate review quality"

**What is at risk:**
- Quality of all 16 triage decisions from 2026-04-15 session
- HIGH urgency items may have received heuristic rather than deliberate treatment
- Downstream decisions dependent on triage outcomes

**Evidence summary:** Both 15a (NO-SUPPORT-FOUND — contradicted by 82-study systematic review on decision fatigue) and 15b (CHALLENGED — Strong, same literature) converge. Decision fatigue research consistently finds quality degradation in serial processing. System 2→System 1 switching documented. Items late in batch receive less deliberate attention.

**Recommended action:**
1. Re-review HIGH urgency items individually (REVISE-008, -011, -013, -014, -015, -016)
2. Check for pattern-based dismissals (same resolution framework applied to multiple items)
3. Limit future batch sizes to 5-7 items
4. Review items in random order to prevent systematic late-batch degradation

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-018:
**Date flagged:** 2026-04-15
**Source item:** PRESUMPTION-024
**Item type:** PRESUMPTION
**Urgency:** HIGH (CRITICAL risk)

**Statement:** "The boundary convergence hypothesis reflects genuine structure, not a selection effect of C2A2's own architecture"

**What is at risk:**
- FINDING-011a credibility — potentially the system's largest false positive
- C2A2's value proposition as a genuine discovery engine
- All cross-tradition findings dependent on LLM pattern genuineness

**Evidence summary:** 15a found only weak support (conditional on independence). 15b found strong challenge from apophenia literature, LLM hallucination research (46% reasoning errors), and construct validity concerns. SYSTEMIC-RISK-FLAG raised: shares vulnerability with ASSUMPTION-022, 024, 026, PRESUMPTION-020 — all depend on genuineness of LLM-generated patterns.

**Recommended action:**
1. **Immediate:** Design null hypothesis test — ask agents to find convergence on a concept known to be absent; if they find it, finding is systematic bias
2. **This month:** Test whether alternative LLMs produce the same boundary convergence
3. **This month:** Submit boundary convergence claim to external domain experts for independent assessment
4. **Ongoing:** Do not elevate FINDING-011a to confirmed status until null hypothesis test passes

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-019:
**Date flagged:** 2026-04-15
**Source item:** PRESUMPTION-026
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "Batch triage quality is comparable to deliberate individual review for HIGH urgency items"

**What is at risk:**
- Same as REVISE-017 — this is the presumption-side counterpart
- 7+ HIGH urgency items in the batch triage may have been inadequately reviewed
- Framework-based dismissals may have substituted for item-specific analysis

**Evidence summary:** Same as ASSUMPTION-027 (REVISE-017). 82-study systematic review, surrogate decision-maker fatigue, System 2→1 switching. All converge on quality degradation.

**Recommended action:**
- Same as REVISE-017; items are paired (assumption + presumption covering same phenomenon)
- Consolidated review recommended

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### Note: ASSUMPTION-026 (C2A2 as new empirical methodology) was dispositioned MONITOR rather than REVISE despite strong challenge, because the NOVELTY flag from 15a indicates this is genuinely novel territory where absence of supporting literature is expected. Strong challenge from hallucination literature is serious but addresses the methodology's implementation (LLM limitations) rather than the concept (agents as instruments). MONITOR with HIGH priority and weekly cadence.

---

**Updated summary (2026-04-15, post-fifth-cycle):**
**Total REVISE items:** 19 (16 prior + 3 new)
**New ASSUMPTIONS flagged:** 1 (ASSUMPTION-027)
**New PRESUMPTIONS flagged:** 2 (PRESUMPTION-024, PRESUMPTION-026)
**New with HIGH urgency:** 3 (all)
**AWAITING-REVIEW:** 3 (new items)
**Prior items status:** All 16 triaged by Tom (see TRIAGE SESSION above)

**SYSTEMIC-RISK-FLAG (2026-04-15):**
Items PRESUMPTION-024, ASSUMPTION-022, ASSUMPTION-024, ASSUMPTION-026, PRESUMPTION-020 share common vulnerability: all depend on genuineness of LLM-generated cross-tradition patterns. If LLM outputs reflect training data biases rather than genuine structural properties, all five items are compromised simultaneously. Recommend: null hypothesis testing + external validation before treating any as confirmed.


---

## 2026-04-16 CYCLE — NEW REVISE ITEMS (5)

---

### REVISE-[new]: ASSUMPTION-028
**Date flagged:** 2026-04-16
**Source item:** ASSUMPTION-028
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:** "Batch 45-file ingestion is equivalent in quality to incremental 5-file daily ingestion"

**What is at risk:**
- Quality of April 16 PRS extractions across the 45 ingested files
- FINDING-013–017 (pattern-detector findings derived from these extractions) — possibly inherit degradation
- Trajectory metrics that compare April 16 to prior single-ingestion days

**Evidence summary:**
15a found only weak-moderate partial support; no direct literature supports equivalence. 15b found strong challenge — the decision-fatigue 82-study systematic review and LLM session-drift literature both predict degradation over sustained batches, and this is the same cluster that already flagged ASSUMPTION-027 and PRESUMPTION-026 as REVISE.

**Recommended action:**
1. A/B sample of files from the 45-file batch: re-extract incrementally, compare PRS-field agreement.
2. Tag FINDING-013–017 with batch-ingestion provenance marker to make inherited risk visible downstream.
3. Set an operational threshold on future backlog sizes (e.g., maximum 15 files/session) pending evidence of equivalence.

**Status:** OPEN — awaits Tom review
**Priority:** HIGH

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: ASSUMPTION-031
**Date flagged:** 2026-04-16
**Source item:** ASSUMPTION-031
**Item type:** ASSUMPTION
**Urgency:** HIGH (CRITICAL — SYSTEMIC-RISK cluster)

**Statement:** "Parallel subagent processing preserves per-tradition PRS-extraction quality"

**What is at risk:**
- Validity of per-tradition extractions from parallel subagent runs
- FINDING-013–017 (derived from parallel subagent output)
- Any Phase 2a architectural commitments predicated on subagent parallelism preserving quality

**Evidence summary:**
15a moderate partial support (multi-agent literature endorses parallel specialists when tasks cleanly decomposable). 15b strong challenge — parallel LLM calls with shared backbone and similar prompts produce correlated outputs, not independent. This is the specific mechanism underlying the SYSTEMIC-RISK-FLAG cluster on LLM pattern genuineness.

**Recommended action:**
1. Pair this REVISE with PRESUMPTION-029 review (shared test).
2. Design and run re-extraction experiment with prompt-diversified parallel subagents; compare finding rates.
3. Add a null-baseline: scrambled/adversarial prompts — finding rate under null sets the floor.
4. Hold Phase 2a commitments premised on FINDING-013–017 pending this test.

**Status:** OPEN — awaits Tom review
**Priority:** HIGHEST (CRITICAL)

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-029
**Date flagged:** 2026-04-16
**Source item:** PRESUMPTION-029
**Item type:** PRESUMPTION
**Urgency:** HIGH (CRITICAL — SYSTEMIC-RISK cluster)

**Statement:** "April 16 pattern-detector findings (13–17) are genuine signals, not artifacts of correlated subagent prompting"

**What is at risk:**
- FINDING-013, 014, 015, 016, 017 directly
- Any downstream paper drafts, architectural decisions, or Phase 2a commitments premised on these findings
- Extended SYSTEMIC-RISK-FLAG cluster credibility (PRESUMPTION-020, 024; ASSUMPTION-022, 024, 026, 031)

**Evidence summary:**
15a NO-SUPPORT-FOUND — the specific positive test (null-baseline, diverse-prompt genuineness comparison) has not been performed, and no literature provides equivalent. NOVELTY flagged. 15b STRONGLY CHALLENGED — apophenia, LLM hallucination, and correlated-prompt contamination literature all converge on the conclusion that shared-backbone parallel subagents produce correlated outputs by construction.

**Recommended action:**
1. **Required before Phase 2a premised on these findings:** Run null-baseline + diverse-prompt re-extraction test.
2. Mark FINDING-013–017 as PROVISIONAL until the test completes.
3. Treat the re-extraction protocol as the beginning of a general C2A2 null-baseline methodology.
4. Document the test design as a candidate original contribution (NOVELTY flag — no prior literature).

**Status:** OPEN — awaits Tom review
**Priority:** HIGHEST (CRITICAL)

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-030
**Date flagged:** 2026-04-16
**Source item:** PRESUMPTION-030
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "The 8-day version-control gap (April 8–16, 189 uncommitted files) was cosmetic rather than structurally significant"

**What is at risk:**
- Provenance-protocol integrity for the gap window
- Reliability of April 15 "fully operational" operational-health claim (measured against unversioned baseline)
- Audit trail and reproducibility guarantees for architectural artifacts modified during the gap

**Evidence summary:**
15a NO-SUPPORT-FOUND — SE literature is essentially unanimous that VCS discipline is structural. 15b STRONGLY CHALLENGED with the same consensus. The presumption directly conflicts with C2A2's own PROVENANCE protocol, which requires chain-of-custody for all artifacts.

**Recommended action:**
1. Immediate commit + tag of current state.
2. Document known in-gap state transitions (which files changed when; who/what touched them).
3. Establish a commit cadence enforcement mechanism (pre-session check; scheduled reminder; automated nightly commit for in-progress work).
4. Re-qualify any April 8–16 operational-health metrics as measured against an unversioned baseline.

**Status:** OPEN — awaits Tom review
**Priority:** HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-032
**Date flagged:** 2026-04-16
**Source item:** PRESUMPTION-032
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (mirrors PRESUMPTION-023 pattern)

**Statement:** "Morning-handoff channel failures (Gmail stale, Chrome extension down) are isolated events rather than a systemic degradation of Tom's intent-signal"

**What is at risk:**
- Fidelity of Tom's intent signal reaching the agents
- Agent prioritization aligning with Tom's actual priorities
- Silent drift if common-cause dependency exists between the channels

**Evidence summary:**
15a NO-SUPPORT-FOUND (weak) — reliability literature permits independence but requires common-cause analysis. 15b CHALLENGED (strong) — same-day concurrent failures with plausibly shared auth/identity/network dependencies have a higher prior for common cause. This mirrors PRESUMPTION-023 (already REVISE).

**Recommended action:**
1. Common-cause analysis: timestamps, error codes, dependency graph.
2. Add aggregated cross-channel health telemetry.
3. Explicit "intent-signal integrity" step in morning handoff (verify with Tom that agents have latest intent).
4. Escalation mechanism when ≥2 channels degrade in the same session.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

**Updated summary (2026-04-16):**
Total REVISE items: 25 (20 prior + 5 new from 2026-04-16 cycle)
HIGH priority (new): ASSUMPTION-028, ASSUMPTION-031 (CRITICAL), PRESUMPTION-029 (CRITICAL), PRESUMPTION-030
MEDIUM priority (new): PRESUMPTION-032

SYSTEMIC-RISK-FLAG cluster (extended): ASSUMPTION-022, 024, 026, 031; PRESUMPTION-020, 024, 029
→ Re-extraction experiment with null-baseline is elevated from PROPOSED to REQUIRED for any Phase 2a decision premised on April 16 findings.


---

## 2026-04-17 CYCLE — 7 new REVISE items

### REVISE-[new]: ASSUMPTION-034
**Date flagged:** 2026-04-17
**Source item:** ASSUMPTION-034
**Item type:** ASSUMPTION
**Urgency:** MEDIUM

**Statement:** "The default regenerator model should be upgraded from claude-opus-4-6 to claude-opus-4-7"

**What is at risk:**
- Narrator-style consistency for wiki_narration outputs
- Silent regression on style-sensitive generation
- Existing prompts tuned to 4-6 quirks

**Evidence summary:**
15a NO-SUPPORT-FOUND (weak "newer is better" prior only; no project-specific support). 15b CHALLENGED (moderate) — foundation-model transitions are empirically non-monotonic on task-level performance; upgrade without regression testing is a documented technical-debt anti-pattern.

**Recommended action:**
1. Document the rationale for the upgrade (what problem is it solving?).
2. Hold the default at 4-6 until a regression test against the 2026-04-15 narration corpus passes.
3. Run A/B comparison on a held-out subset before changing default.
4. If the upgrade is accepted, deploy with a rollback switch.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-035
**Date flagged:** 2026-04-17
**Source item:** PRESUMPTION-035
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "Four Chrome-extension failures in one day meet the OPERATIONAL-DRIFT threshold defined by PRESUMPTION-032 — although PRESUMPTION-032 never specified a threshold"

**What is at risk:**
- Consistency of the OPERATIONAL-DRIFT flag as a useful signal
- False positives (over-alerting) and false negatives (silent drift) compound
- Downstream decisions premised on the flag become unstable

**Evidence summary:**
15a NO-SUPPORT-FOUND — SRE literature is unanimous that thresholds must be pre-defined; retrospective invocation has no support. 15b STRONGLY CHALLENGED — threshold-free alerting is an explicit anti-pattern in Google SRE Workbook and alert-fatigue literature.

**Recommended action:**
1. Define a quantitative OPERATIONAL-DRIFT threshold (e.g., "≥N failures across ≥M channels within T hours").
2. Document the threshold in an SRE-style runbook or directly in monitor_queue.
3. Evaluate future invocations against the documented threshold, not retrospectively.
4. Audit prior OPERATIONAL-DRIFT invocations against the new threshold for consistency.

**Status:** OPEN — awaits Tom review
**Priority:** HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-036
**Date flagged:** 2026-04-17
**Source item:** PRESUMPTION-036
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** "Aggregating Chrome + git + ACL + Anthropic failures as one 'OPERATIONAL-DRIFT' cluster is legible despite four disjoint root causes"

**What is at risk:**
- Chronic under-fixing: most-visible channel gets attention, quieter three persist
- Remediation dilution across disjoint root causes
- Inability to reason about per-channel reliability over time

**Evidence summary:**
15a PARTIALLY-SUPPORTED (weak — situational-awareness use case only). 15b CHALLENGED (strong) — RCA and incident-management literature consistently treat single-label aggregation of disjoint root causes as a remediation anti-pattern.

**Recommended action:**
1. Separate "composite-for-visibility" from "atomic-for-remediation": dashboard aggregates, but incident records are per-channel.
2. Track each channel's fix independently; cluster flag closes only when all component incidents close.
3. Tag each failure with its root-cause category; report per-cause and aggregate counts.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-038
**Date flagged:** 2026-04-17
**Source item:** PRESUMPTION-038
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "The Anthropic billing-propagation bug will clear by Saturday morning without action beyond waiting"

**What is at risk:**
- Dispatch's regeneration smoke test remains blocked if propagation doesn't clear
- Weekend work stalls with no active recovery path
- Prioritization signal to vendor absent (no ticket filed)

**Evidence summary:**
15a NO-SUPPORT-FOUND — no literature predicts a specific clearance window. 15b CHALLENGED (moderate) — recovery-by-waiting without active escalation is an ITIL anti-pattern; recovery-time predictions are systematically optimistic.

**Recommended action:**
1. File a timestamped support ticket with Anthropic immediately (belt-and-suspenders, not replacement for waiting).
2. Define a recovery-window threshold (e.g., "if not cleared by Saturday 10:00, escalate").
3. Consider pre-funding or alternate API key as a fallback path to unblock Saturday work independently.
4. Track retry-timestamp pattern to distinguish vendor-side (staircase recovery) from client-side (flat-line) causes.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-040
**Date flagged:** 2026-04-17
**Source item:** PRESUMPTION-040
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "Structural verification of a .plugin archive is an adequate proxy for end-to-end operational readiness"

**What is at risk:**
- Plugin passes structural check, installs, and silently fails to fire
- "Installed but never fires" is exactly the dominant plugin-failure class
- Silent miss invisible until the next actual resume attempt

**Evidence summary:**
15a NO-SUPPORT-FOUND — testing literature is unanimous that structural ≠ operational readiness. 15b STRONGLY CHALLENGED (strong) — "installed but never fires" is a named, documented failure class across plugin ecosystems.

**Recommended action:**
1. Add an end-to-end smoke test to the plugin-release definition-of-done: install in a fresh environment → send trigger phrase → observe activation.
2. Add observable per-activation log so non-activation is visible, not silent.
3. Make this smoke-test gate mandatory before claiming "operationally ready."

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-041
**Date flagged:** 2026-04-17
**Source item:** PRESUMPTION-041
**Item type:** PRESUMPTION
**Urgency:** HIGH (direct internal inconsistency with PROVENANCE protocol)

**Statement:** "Afternoon-session architectural commitments do not require same-day DECISION-NNN entries (the 'implicit decision' workflow pattern is adequate)"

**What is at risk:**
- Architectural rationale decays rapidly after commitment
- Future reversal cost rises; intent becomes unrecoverable
- Direct internal inconsistency with C2A2's own PROVENANCE protocol (which requires chain-of-custody for all architectural claims)
- 15d monitor and 16 deferred-action agent cannot reason about decisions that weren't recorded

**Evidence summary:**
15a NO-SUPPORT-FOUND — ADR literature unanimous that synchronous capture is required. 15b STRONGLY CHALLENGED (strong) — implicit-decision is the named anti-pattern ADR practice was invented to counter; also directly contradicts C2A2's own PROVENANCE protocol.

**Recommended action:**
1. Adopt standing rule: any afternoon-session architectural commitment creates a same-day DECISION-NNN entry before session close.
2. Create a lightweight short-form ADR template to reduce capture friction.
3. Audit today's afternoon-session commitments: record them as DECISION-NNN entries retrospectively.
4. Reconcile this presumption against the PROVENANCE protocol formally — the two cannot coexist; one must be revised.

**Status:** OPEN — awaits Tom review
**Priority:** HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-[new]: PRESUMPTION-042
**Date flagged:** 2026-04-17
**Source item:** PRESUMPTION-042
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** "The morning autonomous 14a/14b run's zero-output is a correct reflection of zero architectural activity, rather than a pipeline-coverage miss"

**What is at risk:**
- Silent blind-spot accumulation in the self-awareness pipeline itself
- False confidence in coverage; zero-output days taken as signals of nothing-to-extract
- Extends the self-referential validity cluster (PRESUMPTION-015) — the system cannot validate its own coverage

**Evidence summary:**
15a NO-SUPPORT-FOUND — IE-evaluation literature requires external gold-standard for null-output validation. 15b CHALLENGED (moderate-strong) — self-referential coverage validation is a known blind spot; 14b's own operating instructions explicitly acknowledge false-negative invisibility.

**Recommended action:**
1. Establish periodic external coverage audit: Tom or another agent reviews the source transcript of a random zero-output day and independently identifies extractable items.
2. Consider a "coverage canary" — a planted test item that should always be extractable; a missed canary would reveal a pipeline failure.
3. Replace silent zero-output with explicit "no extractable items from [source]; audit trail recorded."
4. Reconcile with PRESUMPTION-015 and the existing self-referential cluster — move to an auditable coverage discipline.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

**Updated summary (2026-04-17):**
Total REVISE items: 32 (25 prior + 7 new from 2026-04-17 cycle)
HIGH priority (new): ASSUMPTION-034 (MEDIUM), PRESUMPTION-035 (HIGH), PRESUMPTION-041 (HIGH — PROVENANCE internal inconsistency)
MEDIUM-HIGH priority (new): PRESUMPTION-036, PRESUMPTION-042
MEDIUM priority (new): PRESUMPTION-038, PRESUMPTION-040

OPERATIONAL-DRIFT meta-cluster (2026-04-17): PRESUMPTION-035 (threshold), 036 (aggregation), 038 (escalation), 042 (coverage audit) — remediate together, not one-by-one; the operational-drift response mechanism itself has unaddressed meta-issues.

SELF-AWARENESS-META cluster (extended from 2026-04-13): PRESUMPTION-015, 024, 041, 042 all share the self-referential validity vulnerability. PRESUMPTION-041 is especially notable for creating a direct internal inconsistency with the PROVENANCE protocol.

---

### REVISE-[new]: ASSUMPTION-043
**Date flagged:** 2026-04-18
**Source item:** ASSUMPTION-043
**Item type:** ASSUMPTION
**Urgency:** HIGH (extends existing CRITICAL cross-tradition-transfer-validity cluster to the specialist-proposal layer)

**Statement:** "PROP-2026-04-18-001 opens a genuinely new Wolfram ↔ analytic-philosophy corridor absent from cross_program_index.md"

**What is at risk:**
- cross_program_index.md accumulates a corridor that looks new but is a selection-effect artifact
- Later corridors compound on it; the overall index loses credibility as a structural map of genuine bridges
- The prior CRITICAL cluster (PRESUMPTION-002, 014, 020, 024) extends to a new layer — content generation rather than extraction
- Downstream agents use the unchecked corridor as grounds for further inference

**Evidence summary:**
15a PARTIALLY-SUPPORTED (novelty-as-absence is verifiable by grep and broadly true; novelty-as-genuineness is NOT established and is specifically flagged by PRESUMPTION-045 as a transfer-validity concern). 15b PARTIALLY-CHALLENGED (moderate-strong) — the registry's own prior CRITICAL cluster directly predicts this failure mode; novelty-as-absence is systematically being treated as evidence for novelty-as-genuineness; Cartwright 1999 and Hofstadter & Sander 2013 converge on the same diagnosis.

**Recommended action:**
1. Tag PROP-2026-04-18-001 as PROVISIONAL in cross_program_index.md.
2. Gate INCORPORATE on a transfer-validity statement from a tradition-specialist agent (Stump agent, Wolfram agent, or Brandom-aware sub-agent); PRESUMPTION-045 remediation must precede the novelty claim's INCORPORATE.
3. Adopt the general remediation from the existing CRITICAL cluster: novelty-claim-only-after-transfer-validity-statement.
4. Standing rule: no cross-tradition corridor is INCORPORATED without a paired transfer-validity statement from a target-domain specialist.

**Status:** OPEN — awaits Tom review
**Priority:** HIGH

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** SYSTEMIC-RISK-FLAG extends existing CRITICAL cluster (PRESUMPTION-002, 014, 020, 024) to the specialist-proposal layer; paired with PRESUMPTION-045.

---

### REVISE-[new]: PRESUMPTION-043
**Date flagged:** 2026-04-18
**Source item:** PRESUMPTION-043
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "Parked interactive sessions are implicitly indefinitely retained (no timeout, no default-execution, no Agent-16 routing)"

**What is at risk:**
- Cumulative hidden backlog of parked sessions
- Architectural intent decays because it is never revisited
- Systemic blindness about what has been parked vs. what is active
- Extends the self-awareness-meta cluster; joins PRESUMPTION-015, 024, 041, 042, 046 as a self-referential blind spot
- Direct contradiction with C2A2's own Agent 16 (deferred-action monitor) architecture — parked sessions bypass an agent specifically designed for this routing

**Evidence summary:**
15a NO-SUPPORT-FOUND — no literature supports indefinite retention of parked interactive sessions as designed behavior; SaaS/agent-platform norm is explicit retention policy, and Agent 16 already exists in C2A2's own architecture. 15b CHALLENGED (moderate-strong) — GTD, email-overload, queue-backlog literatures converge: parked items without review cadence accumulate until they lose signal value; this is a routing gap, not a feature.

**Recommended action:**
1. Route parked sessions to Agent 16 explicitly.
2. Add a parked-session retention policy (e.g., review after 14 days; escalate after 28 days).
3. Maintain a parked-sessions index so the backlog is observable.
4. Audit current parked sessions: count how many have been parked for > 14 days without review; if > 0, the presumption is factually in effect and is a routing gap to fix.
5. Treat as one of three BLOCKED-ROUTE-LIFECYCLE cluster members (with PRESUMPTION-046, 047); define the parked-session lifecycle end-to-end rather than piecewise.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** New BLOCKED-ROUTE-LIFECYCLE cluster (PRESUMPTION-043, 046, 047) — remediate together.

---

### REVISE-[new]: PRESUMPTION-044
**Date flagged:** 2026-04-18
**Source item:** PRESUMPTION-044
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (direct internal inconsistency with ASSUMPTION-042)

**Statement:** "Retry-as-default is the correct first remediation for Chrome-MCP-not-reachable errors even after 5-consecutive-day failure"

**What is at risk:**
- Delayed human response to persistent channel failure
- Routine logs that obscure a real, actionable problem; alert-fatigue compound effect
- Direct internal inconsistency with ASSUMPTION-042 (which says 5-of-3 = "not transient"); PRESUMPTION-044 implies retry continues past that threshold
- Joins the OPERATIONAL-DRIFT cluster as a 5th member (with PRESUMPTION-035, 036, 038, 042)

**Evidence summary:**
15a PARTIALLY-SUPPORTED — retry-first is canonical for transient failures (Nygard 2007; SRE book; AWS Well-Architected); the "even after 5-day failure" extension is NOT supported. 15b CHALLENGED (moderate-strong) — circuit-breaker pattern literature, SLO/alert-fatigue literature, and C2A2's own ASSUMPTION-042 all converge: once the persistence threshold is crossed, the correct remediation shifts from retry to manual intervention. PRESUMPTION-044 describes a retry posture that has outlived its validity window.

**Recommended action:**
1. Pair retry with a staleness counter; escalate when the counter crosses ASSUMPTION-042's threshold.
2. Maintain a last-success-timestamp per scheduled task; surface staleness as an observable.
3. Implement circuit-breaker: after N consecutive retries, suspend retry and surface a manual-intervention alert.
4. Reconcile with ASSUMPTION-042 — the two should govern different phases of the same failure trajectory (retry governs [0, threshold); manual-intervention governs [threshold, ∞)).
5. Check current Chrome-MCP scheduled task: does its retry logic include a staleness ceiling? If not, the presumption is factually in effect as a gap.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** Extends OPERATIONAL-DRIFT meta-cluster; INTERNAL-CONSISTENCY flag with ASSUMPTION-042.

---

### REVISE-[new]: PRESUMPTION-045
**Date flagged:** 2026-04-18
**Source item:** PRESUMPTION-045
**Item type:** PRESUMPTION
**Urgency:** CRITICAL (extends existing CRITICAL cross-tradition-transfer-validity cluster)

**Statement:** "Wolfram's hypergraph formalism applies to the Sellarsian space of reasons without transfer-validity check"

**What is at risk:**
- Cross_program_index.md accumulates a corridor that is a selection-effect artifact
- The CRITICAL cluster expands to the specialist-proposal layer (content generation, not just extraction)
- Downstream agents use the unchecked corridor as grounds for further inference, compounding the error
- Structural incompatibility: hypergraph rewriting is causally-invariant in Wolfram's target domain; the space of reasons is notoriously NOT causally-invariant — norms depend on social-practice context

**Evidence summary:**
15a NO-SUPPORT-FOUND — the philosophy-of-science literature on formalism transfer is unanimously opposed to the pattern described; no literature supports unchecked transfer of Wolfram's hypergraph formalism to the Sellarsian space of reasons. 15b STRONGLY-CHALLENGED (strong) — C2A2's own CRITICAL cluster (PRESUMPTION-002, 014, 020, 024) directly predicts this failure mode; Cartwright 1999, Batterman 2002, Hofstadter & Sander 2013 converge; specific structural obstacles (causal invariance vs. normative context-sensitivity) make the transfer not merely unjustified but potentially inconsistent.

**Recommended action:**
1. Gate PROP-2026-04-18-001 on a transfer-validity statement from a tradition agent in the target domain (Stump agent, or a Brandom-aware sub-agent).
2. Adopt the general remediation from the CRITICAL cluster: novelty-claim-only-after-transfer-validity-statement.
3. Tag any Wolfram↔analytic-philosophy edges as PROVISIONAL in cross_program_index.md until the validity statement exists.
4. Commission Stump agent + Wolfram agent joint review of PROP-2026-04-18-001; validity statement issued iff both concur on transfer conditions.
5. Adopt standing rule: no cross-tradition corridor is INCORPORATED without a transfer-validity statement from a tradition-specialist agent.

**Status:** OPEN — awaits Tom review
**Priority:** CRITICAL

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** SYSTEMIC-RISK-FLAG CRITICAL — extends existing CRITICAL cluster (PRESUMPTION-002, 014, 020, 024) to the content-generation layer; paired with ASSUMPTION-043.

---

### REVISE-[new]: PRESUMPTION-046
**Date flagged:** 2026-04-18
**Source item:** PRESUMPTION-046
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (renders ASSUMPTION-044's reliability claim unfalsifiable)

**Statement:** "User pivot on arrival discharges a loaded handoff payload rather than re-queues it (payload-discharge-on-pivot)"

**What is at risk:**
- DECISION-021's reliability claim (ASSUMPTION-044) accumulates confidence without evidence
- Payload intent silently discharges; architectural direction drifts
- The handoff-vs-context-loader taxonomy ambiguity is never resolved
- Joins the self-awareness-meta cluster as a 5th/6th member — self-referential blind spot

**Evidence summary:**
15a PARTIALLY-SUPPORTED — descriptive claim (users do discharge loaded payloads on pivot) is supported by HCI literature and the 2026-04-18 Dispatch session. 15b CHALLENGED (moderate-strong) — two-pronged challenge: (a) normative — discharge-on-pivot is a failure mode for a handoff pattern; (b) epistemic — discharge-on-pivot makes the handoff pattern's reliability unfalsifiable (execution half only runs when discharge doesn't occur). The cluster with ASSUMPTION-044 (N=1 reliability) and PRESUMPTION-041 (implicit decisions) is a classic invisible-design-debt pattern.

**Recommended action:**
1. Decide explicitly whether DECISION-021 is a handoff or a context-loader; rename accordingly.
2. If handoff: implement re-queue-on-pivot so the payload is not silently discharged.
3. If context-loader: drop the "reliably orients" framing (ASSUMPTION-044) and treat it as a load-only primitive.
4. Instrument: track (loaded-count, acted-on-count, discharged-count) as three distinct observables.
5. On next Dispatch session: if Tom pivots, does the loaded payload persist to the next session? If no, the presumption is factually in effect and the mechanism is a context-loader by behavior.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** BLOCKED-ROUTE-LIFECYCLE cluster (PRESUMPTION-043, 046, 047); SELF-AWARENESS-META cluster extension; pair with MONITOR-049 (ASSUMPTION-044).

---

### REVISE-[new]: PRESUMPTION-048
**Date flagged:** 2026-04-18
**Source item:** PRESUMPTION-048
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (extends self-awareness-meta cluster to 6 members)

**Statement:** "Null walk notes at briefing time indicate missed-capture rather than zero-walk-content (no disambiguation)"

**What is at risk:**
- Tom's walk-direction intent drifts silently from the briefing's operating goals on days when walks happen but notes don't get captured
- Extends the self-awareness-meta cluster to a 6th member, deepening the system-wide blind-spot pattern
- The briefing's perceived quality is uncalibrated to the input-quality it is actually receiving

**Evidence summary:**
15a PARTIALLY-SUPPORTED — the *interpretation half* ("null should be treated as missed-capture rather than definitive zero") is supported by missing-data, IE-evaluation, and knowledge-work literatures (Little & Rubin 2019; Chinchor 1995; Kandel et al. 2012). What is NOT supported is the absence of a disambiguation mechanism. 15b CHALLENGED (moderate) — null-without-disambiguation is a blind spot regardless of which default interpretation is chosen; the literature consistently calls for disambiguation, which PRESUMPTION-048 explicitly lacks. PRESUMPTION-048 is half-right (treating null as missed is better than treating it as zero) and half-wrong (the absence of disambiguation means neither interpretation is defensible).

**Recommended action:**
1. Require an explicit walk-status ping: walked/didn't-walk, captured-notes/no-notes.
2. Surface degraded-connector state in the briefing preamble.
3. Reconcile with PRESUMPTION-042 and PRESUMPTION-015 — the entire self-awareness-meta cluster shares one remediation: disambiguate null signals.
4. Add a "coverage canary" pattern to walk-capture: a daily minimum-signal ping that the capture pipeline is online.
5. Test: On any given null-walk-notes day, ask Tom directly: "walked today? captured notes?" Count days where the disambiguation differs from the presumption's missed-capture default.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** SELF-AWARENESS-META cluster extension — now 6 members (PRESUMPTION-015, 024, 041, 042, 046, 048); treat as one remediation package.

---

**Updated summary (2026-04-18 afternoon top-up cycle):**
Total REVISE items: 38 (32 prior + 6 new from 2026-04-18 cycle — ASSUMPTION-043; PRESUMPTION-043, 044, 045, 046, 048)
CRITICAL priority (new): PRESUMPTION-045 (extends existing CRITICAL cross-tradition-transfer-validity cluster)
HIGH priority (new): ASSUMPTION-043 (extends CRITICAL cluster to specialist-proposal layer)
MEDIUM-HIGH priority (new): PRESUMPTION-044 (internal inconsistency with ASSUMPTION-042), PRESUMPTION-046 (renders ASSUMPTION-044 unfalsifiable)
MEDIUM priority (new): PRESUMPTION-043, PRESUMPTION-048

**Cross-cluster coordination (2026-04-18):**

CRITICAL CROSS-TRADITION-TRANSFER-VALIDITY cluster (extended): PRESUMPTION-002, 014, 020, 024, 045 + ASSUMPTION-043 — the previously-extraction-layer cluster now includes content-generation and specialist-proposal instances. Single remediation: standing rule that no cross-tradition corridor is INCORPORATED without a transfer-validity statement from a target-domain specialist agent.

SELF-AWARENESS-META cluster (extended to 6 members): PRESUMPTION-015, 024, 041, 042, 046, 048 — all share the self-referential validity vulnerability and the same remediation pattern (disambiguate null/missing signals with explicit observability). Treat as one remediation package.

OPERATIONAL-DRIFT cluster (extended to 5 members): PRESUMPTION-035, 036, 038, 042, 044 — threshold/aggregation/escalation/coverage-audit/retry-ceiling all related; PRESUMPTION-044 introduces the INTERNAL-CONSISTENCY flag with ASSUMPTION-042.

BLOCKED-ROUTE-LIFECYCLE cluster (NEW, 2026-04-18): PRESUMPTION-043 (parked-session retention), 046 (payload-discharge-on-pivot), 047 (user-directedness — MONITOR) — together define an unspecified end-to-end lifecycle for blocked routes. Remediation: define parked-session lifecycle end-to-end rather than piecewise.

INTERNAL-CONSISTENCY flag (2026-04-18): ASSUMPTION-042 ↔ PRESUMPTION-044 — the two items say different things about the same failure trajectory; reconcile by assigning them to different phases.

---

### REVISE-[new]: ASSUMPTION-046
**Date flagged:** 2026-04-20
**Source item:** ASSUMPTION-046
**Item type:** ASSUMPTION
**Urgency:** MEDIUM (briefing-layer unaudited filter; part of the unaudited-filter cluster with PRESUMPTION-029 CRITICAL + PRESUMPTION-053)

**Statement:** "Filtering active Pattern-Detector findings from 17 to 'most significant 11' preserves actionable signal"

**What is at risk:**
- Quiet attenuation of high-actionability findings that score low on the unaudited ranker (symmetric to PRESUMPTION-029's quiet amplification)
- Systematic under-representation of finding-types the ranker scores low (e.g., anomaly-class vs. pattern-class)
- Extends the unaudited-filter cluster across Pattern-Detector and briefing layers — two filters in one pipeline, neither audited

**Evidence summary:**
15a PARTIALLY-SUPPORTED moderate — the *cognitive-budget rationale* is strong (Miller 1956; Cowan 2001; Few 2013; Ancker 2017); the *preservation-of-actionable-signal* clause is conditional on a well-calibrated ranking function, which is the exact calibration gap PRESUMPTION-053 names. 15b CHALLENGED moderate — selection on unstated criteria is a named selection-bias mechanism (Heckman 1979; Hernán & Robins 2020); LLM rankers have documented calibration failures (Zheng et al. 2023); ranked truncation drops tail-risk actionable items by construction (Taleb 2007); symmetric to PRESUMPTION-029's CRITICAL disposition. The assumption's stated half (cognitive budget) is supportable; the stated preservation claim is unfalsifiable at current operationalization.

**Recommended action:**
1. Specify the selection criterion explicitly (even "top 11 by recency-weighted novelty" is better than unstated).
2. Log the 6 dropped findings with their scores for audit.
3. Periodically sample dropped items for ground-truth actionability check (ask Tom to rate dropped-vs-retained).
4. Pair remediation with PRESUMPTION-053 (same filter, different framing — stated commitment + unstated basis) and with PRESUMPTION-029 (symmetric partner at the extraction layer).
5. Test: Take today's 6 dropped findings and ask Tom to rate actionability against the 11 retained; measure whether top-6-of-dropped beats bottom-6-of-retained. Repeat weekly.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM (part of unaudited-filter cluster; pair with PRESUMPTION-053 remediation)

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** Unaudited-filter cluster (PRESUMPTION-029 CRITICAL prior, ASSUMPTION-046, PRESUMPTION-053) — all three at different layers of the Pattern-Detector → briefing pipeline; one remediation package. Also BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster (ASSUMPTION-046, 047, 048, PRESUMPTION-053).

---

### REVISE-[new]: ASSUMPTION-048
**Date flagged:** 2026-04-20
**Source item:** ASSUMPTION-048
**Item type:** ASSUMPTION
**Urgency:** MEDIUM (cheap remediation available; INTERNAL-CONSISTENCY flag with ASSUMPTION-047)

**Statement:** "Execution queue with only a stale placeholder (2026-03-31) can be reported as 'clear' per briefing intent"

**What is at risk:**
- Downstream consumers (Tom; downstream digests and agents) act on "clear" when the actual state is "stale placeholder present"
- Extends the SELF-AWARENESS-META cluster to a 7th member — null/stale interpretation blind spots now visible at the execution-queue layer
- Internal tension with ASSUMPTION-047 (transparent flagging) — the same day-cycle 14a extraction surfaces a commitment (047) and a counter-example (048) to it

**Evidence summary:**
15a NO-SUPPORT-FOUND — every relevant body (database semantics, dashboard convention, queue-management, C2A2's prior null-disambiguation dispositions) distinguishes empty from stale-placeholder. 15b CHALLENGED moderate-strong — queue semantics do not license collapsing stale-placeholder to empty; pattern matches the null-as-success pattern the SELF-AWARENESS-META cluster has already flagged; framing has downstream consequences; cheap remediation (clear the placeholder) is strictly preferable. INTERNAL-CONSISTENCY-FLAG raised: ASSUMPTION-047 (senior commitment) contradicts ASSUMPTION-048 on the same normative axis — the latter should be resolved as a data-hygiene violation, not as a separate normative claim.

**Recommended action:**
1. Preferred: clear the stale placeholder from queue.md (made possible once DECISION-018 git-lock rescue executes).
2. Report the execution-queue state literally: "0 current items; 1 stale placeholder from 2026-03-31."
3. Distinguish literal state from briefing-intent in the rendering layer.
4. Add a stale-item sweep to the briefing preprocessor.
5. Adopt ASSUMPTION-047 (PREMISE-006) as the senior commitment; treat ASSUMPTION-048 as derivative and resolve at data-hygiene layer.
6. Test: After DECISION-018 git-lock rescue, verify that the execution queue updates and that the "clear" / "stale" distinction resolves at the data layer rather than the briefing layer.

**Status:** OPEN — awaits Tom review (with preferred remediation: clear the stale placeholder)
**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** SELF-AWARENESS-META cluster extension (now 7 members); BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster (ASSUMPTION-046, 047, 048, PRESUMPTION-053). INTERNAL-CONSISTENCY flag with ASSUMPTION-047 (PREMISE-006).

---

### REVISE-[new]: PRESUMPTION-049
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-049
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (CROSS-TASK-COORDINATION cluster; duplicate-Levin evidence already observed)

**Statement:** "Wiki daily run and Levin+Friston specialist run are scope-partitioned without coordination contract"

**What is at risk:**
- Duplicate-production noise in the review queue (already observed empirically — duplicate-Levin artifact)
- Silent Friston coverage gap if specialist scope fails to match daily-wiki scope
- Schedule overlap if specialist convergence is unbounded (compounds with PRESUMPTION-054)
- Invisible-to-the-pipeline state: neither task knows the other ran

**Evidence summary:**
15a PARTIALLY-SUPPORTED weak — scope-partition-by-convention is a valid pattern *only when* the partition is disjoint, stable, and writes are idempotent; the literature supports the *pattern* but not *unchecked use* of it. The specific instance shows observed partition drift. 15b CHALLENGED moderate — distributed-systems literature (Lamport 1978; Gray & Reuter 1992; Kleppmann 2017) explicitly names scope-partition-by-convention as a failure mode when writes are not write-exclusive or idempotent; the duplicate-Levin artifact is direct empirical evidence the partition has already failed. The "without coordination contract" clause converts from permissible to implicated once the drift is observable.

**Recommended action:**
1. Add an explicit coordination-contract document: who is responsible for which thinker-slots, at what cadence, with what handoff.
2. Write-exclusion via per-thinker lock-file or per-day lease; idempotent merge for dedup.
3. Cross-task state ping: each task emits a "ran at T with scope X" marker that the other reads before starting.
4. Enforce per-thinker uniqueness in the review queue.
5. Remediate as one package with PRESUMPTION-051 (MONITOR — as-of labeling) and PRESUMPTION-054 (REVISE — turn/cost/time-caps) — all three are CROSS-TASK-COORDINATION cluster members.
6. Test: Audit the review queue for duplicate items over the next 4 weeks; measure per-thinker duplicate rate; observe whether daily-wiki runs complete before specialist runs start.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** CROSS-TASK-COORDINATION cluster (new 2026-04-20, 3 members): PRESUMPTION-049 (this), PRESUMPTION-051 (MONITOR-052), PRESUMPTION-054 (REVISE).

---

### REVISE-[new]: PRESUMPTION-050
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-050
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (INTERNAL-CONSISTENCY cluster now 2 pairs; ASSUMPTION-042 template is not uniformly applied; normalization-of-deviance risk)

**Statement:** "4-day stale .git/index.lock classified as single incident, not escalation (asymmetric with ASSUMPTION-042 Chrome threshold)"

**What is at risk:**
- INTERNAL-CONSISTENCY cluster expands to 2 pairs (ASSUMPTION-042 ↔ PRESUMPTION-044 + ASSUMPTION-042 ↔ PRESUMPTION-050) — ASSUMPTION-042 becomes the shared failure-mode center
- Master-wiki updates blocked for 4+ days without escalation (visible via PRESUMPTION-047 narrative discrepancy commitment in PREMISE-006)
- Downstream consumers of the wiki (Dispatch, briefings) operate on stale data without awareness
- Normalization-of-deviance risk: future 5-day / 6-day / 10-day blockers become harder to escalate once the 4-day precedent is normalized

**Evidence summary:**
15a NO-SUPPORT-FOUND — every relevant body (ITIL Incident vs. Problem classification; Google SRE ch. 14; Nygard 2007 circuit-breakers; DECISION-018 in-wiki history) supports classifying a 4-day standing blocker as a problem with escalation, not as a single transient incident. 15b STRONGLY-CHALLENGED — convergent literature plus C2A2's own prior scaffolding; INTERNAL-CONSISTENCY-FLAG raised showing ASSUMPTION-042's escalation structure is a *template* not being applied uniformly. The 4-day git-lock is the visible tip; the same gap applies to other OPERATIONAL-DRIFT channels.

**Recommended action:**
1. Define a git-lock-specific threshold analogous to ASSUMPTION-042 (e.g., 24h → attempt auto-clear; 48h → alert; 72h → block master-wiki writes and escalate).
2. Generalize ASSUMPTION-042 from a Chrome-specific threshold to a channel-agnostic template; instantiate per-channel thresholds across all OPERATIONAL-DRIFT channels.
3. Uniformly report channel state in every briefing preamble.
4. Execute DECISION-018 remediation to remove the blocker at source.
5. Test: Audit every OPERATIONAL-DRIFT channel for (a) defined threshold, (b) automated escalation, (c) surfacing in briefing. Count the channels without all three.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** INTERNAL-CONSISTENCY cluster (2 pairs): ASSUMPTION-042 ↔ PRESUMPTION-044 + ASSUMPTION-042 ↔ PRESUMPTION-050. OPERATIONAL-DRIFT cluster (extended to 6 members with PRESUMPTION-050). Treat ASSUMPTION-042 as a *template* and audit all drift channels for compliance.

---

### REVISE-[new]: PRESUMPTION-052
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-052
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (extends PRESUMPTION-048 with recurrence signal; SELF-AWARENESS-META cluster now 7 members; MTTD failure)

**Statement:** "Second-consecutive null-walk-notes handled by same fallback without escalation (Gmail degraded 7+ calendar days)"

**What is at risk:**
- Normalization-of-deviance at the intent-capture layer — the system learns to operate with Tom's most intentional input channel silent
- SELF-AWARENESS-META cluster now growing along a new dimension (time/recurrence), not just membership — from 6 to 7 members
- MTTD failure — the system does not detect its own degraded state; 7+ days of degraded Gmail without detection/escalation is an MTTD failure by any standard
- Compounds with ASSUMPTION-042 (only one channel has a documented threshold) and PRESUMPTION-050 (git-lock asymmetric classification)

**Evidence summary:**
15a NO-SUPPORT-FOUND — SRE circuit-breakers, alert-fatigue, normalization-of-deviance, and C2A2's own prior PRESUMPTION-048 REVISE disposition all predict escalation on consecutive failures, not steady-state repeated fallback. 15b STRONGLY-CHALLENGED with SYSTEMIC-RISK-FLAG — convergent literature (Nygard 2007; Vaughan 1996; Dekker 2011; Allspaw 2012; Ancker 2017) all point to escalation as the canonical response; SELF-AWARENESS-META cluster extends to 7 members and grows along the time dimension. The system's own self-awareness pipeline has flagged the same structural gap (PRESUMPTION-048), dispositioned it for revision, and then immediately produced a recurrence — the remediation loop is slower than the rate of new evidence (a meta-MTTD failure in the self-awareness pipeline itself).

**Recommended action:**
1. Recurrence-aware escalation: count consecutive degraded-channel days and escalate after N=3 or N=5.
2. Channel-health SLI: define a reliability SLO per channel (e.g., "intent-capture channel: no more than 2 consecutive null days").
3. Surface channel state in briefing preamble (degraded-Gmail 7d; Chrome extension down 5th consecutive run; git-lock 4d).
4. Cluster-wide remediation: treat SELF-AWARENESS-META cluster as one package — audit every signal in the self-awareness pipeline for (a) null-disambiguation, (b) recurrence counter, (c) escalation primitive.
5. Test: Starting today, count consecutive null-channel days for every input channel; escalate any channel at N=3; observe whether Tom receives an escalation signal before the 7-day mark on any future instance.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM-HIGH (strengthens PRESUMPTION-048 prior REVISE disposition; one of the most time-sensitive items in this cycle)

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** SELF-AWARENESS-META cluster (now 7 members): PRESUMPTION-015, 024, 041, 042, 046, 048, 052. OPERATIONAL-DRIFT intersection. Cluster-wide remediation = one package.

---

### REVISE-[new]: PRESUMPTION-053
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-053
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (symmetric to PRESUMPTION-029 CRITICAL; unaudited-filter cluster at briefing layer)

**Statement:** "17→11 findings filter selection criterion unstated and unaudited (symmetric partner to PRESUMPTION-029)"

**What is at risk:**
- Quiet attenuation of high-actionability findings that score low on the unaudited ranker (symmetric to PRESUMPTION-029's quiet amplification)
- Extends the unaudited-filter cluster to a second layer of the Pattern-Detector → briefing pipeline — filters now compound
- If PRESUMPTION-029 stays unresolved, PRESUMPTION-053 has no remediation template to inherit; symmetric neglect of the symmetric problem is itself an internal-consistency violation

**Evidence summary:**
15a NO-SUPPORT-FOUND — every relevant body (auditability, selection-bias, symmetric pairing with PRESUMPTION-029 CRITICAL) predicts this is an anti-pattern. 15b CHALLENGED moderate-strong with SYSTEMIC-RISK-FLAG — unaudited filters produce silent systematic bias (Heckman 1979; Hernán & Robins 2020); LLM rankers require calibration (Zheng 2023); symmetric partner PRESUMPTION-029 has been CRITICAL for 4 days unresolved; pair with ASSUMPTION-046 (the stated commitment whose implicit basis this presumption surfaces). Treating this as a lower-priority item than PRESUMPTION-029 would itself be an internal-consistency violation.

**Recommended action:**
1. State the selection criterion explicitly (even "top 11 by recency-weighted novelty" is better than unstated).
2. Log the 6 dropped findings with their scores for audit.
3. Periodically sample dropped items for ground-truth actionability check.
4. Remediate PRESUMPTION-029 and PRESUMPTION-053 together — they are symmetric problems with symmetric remediations; pair with ASSUMPTION-046 (same filter, stated commitment framing).
5. Test: In the next briefing cycle, compare the 11 retained findings against the 6 dropped; measure retention rate weighted by downstream-action rate; escalate if drop-set actionability is non-trivial.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM-HIGH (inherits PRESUMPTION-029's CRITICAL on symmetric-partner logic, moderated to briefing-only scope)

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** Unaudited-filter cluster (3 members): PRESUMPTION-029 (CRITICAL prior), ASSUMPTION-046 (REVISE), PRESUMPTION-053 (this) — one remediation package. Also BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster.

---

### REVISE-[new]: PRESUMPTION-054
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-054
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (runaway-cost risk; CROSS-TASK-COORDINATION cluster; compounds with PRESUMPTION-049 and PRESUMPTION-051)

**Statement:** "Specialist scheduled tasks converge on terminal output without turn-cap / cost-cap / time-cap"

**What is at risk:**
- Runaway-cost risk (direct operational cost; specialist cost is unbounded by construction)
- Read-after-write race with next daily cycle (compounds with PRESUMPTION-051 in-flight read)
- Coordination-contract gap across the scheduled-task layer (compounds with PRESUMPTION-049)
- SELF-AWARENESS-META cluster intersection — specialist tasks are part of the self-awareness pipeline, so their unboundedness is a self-awareness-of-self-awareness gap

**Evidence summary:**
15a NO-SUPPORT-FOUND — every relevant body (AI-safety, LLM-agent-framework practice, bounded-exploration theory, CRON-task best practices) prescribes explicit caps; removing caps is documented as a known bug class. 15b STRONGLY-CHALLENGED with SYSTEMIC-RISK-FLAG — convergent wall of literature (Zilberstein 1996; Amodei 2016; LangChain/OpenAI Assistants docs; Google SRE book; FinOps 2023; systemd-timer/K8s CronJob defaults). PRESUMPTION-054 compounds with PRESUMPTION-049 (no coordination contract) and PRESUMPTION-051 (in-flight read) to form a 3-member CROSS-TASK-COORDINATION cluster.

**Recommended action:**
1. Add explicit caps to every scheduled task: turn-cap (e.g., 30 turns), cost-cap (e.g., $1.50/run), time-cap (e.g., 20 minutes).
2. Best-so-far emission: on cap, emit the partial output with a "capped" marker.
3. Coordination contract: specialist task emits a "started at T, expected completion T+N" marker that the briefing layer can check.
4. Cluster-wide remediation: treat PRESUMPTION-049, 051, 054 as one CROSS-TASK-COORDINATION package deployed together across all scheduled tasks.
5. Test: Run one specialist task with caps at 30 turns / 20 min / $1.50 and observe convergence; compare to uncapped run to measure actual utilization and pick tighter caps.

**Status:** OPEN — awaits Tom review
**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** CROSS-TASK-COORDINATION cluster (3 members): PRESUMPTION-049 (REVISE), PRESUMPTION-051 (MONITOR-052), PRESUMPTION-054 (this). SELF-AWARENESS-META cluster intersection (specialist-pipeline unboundedness ↔ self-awareness-pipeline blindspot for in-flight state).

---

**Updated summary (2026-04-20 daily cycle):**
Total REVISE items: 45 (38 prior + 7 new from 2026-04-20 cycle — ASSUMPTION-046, 048; PRESUMPTION-049, 050, 052, 053, 054)
MEDIUM-HIGH priority (new): PRESUMPTION-050 (INTERNAL-CONSISTENCY cluster expansion), PRESUMPTION-052 (SELF-AWARENESS-META recurrence), PRESUMPTION-053 (symmetric to PRESUMPTION-029 CRITICAL), PRESUMPTION-054 (runaway-cost; CROSS-TASK-COORDINATION)
MEDIUM priority (new): ASSUMPTION-046, ASSUMPTION-048, PRESUMPTION-049

**Cross-cluster coordination (2026-04-20):**

CROSS-TASK-COORDINATION cluster (NEW, 3 members): PRESUMPTION-049 (REVISE), 051 (MONITOR-052), 054 (REVISE) — scheduled-task layer lacks coordination contract, timing caps, and as-of labeling. Shared remediation package: caps + contract + labeling, deployed together across all scheduled tasks.

SELF-AWARENESS-META cluster (extended to 7 members): PRESUMPTION-015, 024, 041, 042, 046, 048, 052 — now growing along time dimension (recurrence) as well as membership dimension. Cluster-wide remediation: audit every signal in the self-awareness pipeline for (a) null-disambiguation, (b) recurrence counter, (c) escalation primitive.

INTERNAL-CONSISTENCY cluster (extended to 2 pairs): ASSUMPTION-042 ↔ PRESUMPTION-044 (prior) + ASSUMPTION-042 ↔ PRESUMPTION-050 (new) — ASSUMPTION-042's escalation structure is a *template* not being applied uniformly across OPERATIONAL-DRIFT channels.

BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster (NEW, 4 members): ASSUMPTION-046 (REVISE), 047 (PREMISE-006 INCORPORATED), 048 (REVISE), PRESUMPTION-053 (REVISE) — first cluster where 14a extracts the briefing agent's own methodological commitments explicitly. ASSUMPTION-047 (transparent flagging, PREMISE-006) is the senior commitment that resolves the internal tension with ASSUMPTION-048 (stale-as-clear).

Unaudited-filter cluster (NEW, 3 members): PRESUMPTION-029 (CRITICAL prior), ASSUMPTION-046 (REVISE), PRESUMPTION-053 (REVISE) — same filter concern at three surfaces of the Pattern-Detector → briefing pipeline. One remediation package.

Note on symmetric dispositions: PRESUMPTION-029 (CRITICAL, 2026-04-16) and PRESUMPTION-053 (REVISE MEDIUM-HIGH, 2026-04-20) are structurally symmetric (quiet amplification vs. quiet attenuation on the same pipeline). PRESUMPTION-029 remains unresolved at 4 days; PRESUMPTION-053 should be remediated jointly with it. Keeping them at different priority tiers would itself be an internal-consistency violation.

---

### REVISE-[new]: ASSUMPTION-053
**Date flagged:** 2026-04-20
**Source item:** ASSUMPTION-053
**Item type:** ASSUMPTION
**Urgency:** HIGH (CONFLICTS with ASSUMPTION-003's 15a/15b independence requirement; SYSTEMIC-RISK-FLAG; blocks 2026-04-27 rollout until resolved)

**Statement:** "The 14a/14b/15a/15b/15c pipeline can be implemented as appended-turn topology over a shared context (the caching-friendly shape)"

**What is at risk:**
- **Same-model-independence conflict:** ASSUMPTION-003 commits to 15a/15b being independent literature searches (FOR and AGAINST, not cross-contaminated). Appended-turn topology on a shared context means 15b sees 15a's findings before searching — 15b's search becomes "find counterexamples to what 15a found" rather than "independently search for challenging evidence." This is a known anti-pattern (Zheng 2023 self-preference; Panickssery 2024 on anchoring in LLM-judge pipelines).
- **Cross-contamination in the self-awareness pipeline** — the pipeline's value depends on independence between FOR and AGAINST; appended-turn topology structurally defeats that.
- **Rollout-blocker:** the 2026-04-27 caching rollout depends on this topology; either the topology needs modification, or ASSUMPTION-003 needs amendment to acknowledge cross-contamination.
- **SYSTEMIC-RISK-FLAG:** this is the first CACHING-ARCHITECTURE-cluster item that conflicts with a prior validated architectural commitment (ASSUMPTION-003 → PREMISE-003 equivalent); the conflict surfaces only because 14b surfaced the topology as an unstated assumption.

**Evidence summary:**
15a SUPPORTED (Strong) — appended-turn topology IS the canonical caching-friendly shape; vendor-documented (Anthropic, OpenAI) and technically correct for cache reuse. 15b STRONGLY-CHALLENGED (Strong) with SYSTEMIC-RISK-FLAG — literature on LLM-judge independence (Zheng 2023; Panickssery 2024), multi-agent pipeline anchoring (Du et al. 2023 "Improving Factuality and Reasoning"; Liang et al. 2023 on multi-agent debate), and cross-contamination in sequential generation (Bender & Koller 2020 on context-carrying effects) converge on the claim that appended-turn topology over shared context is INCOMPATIBLE with the independence requirement 15a/15b was designed to satisfy. The presumption is technically correct about caching and architecturally wrong about independence; the two cannot both be true with the current topology.

**Recommended action:**
1. **Decide which commitment is senior:** if 15a/15b independence is preserved, the caching topology must be modified (e.g., fresh-context-per-agent with tool/system-prompt caching only; OR separate cache namespaces per agent). If caching-topology is preserved, ASSUMPTION-003 must be amended to acknowledge that 15a/15b are not independent and the self-awareness-pipeline's value claim must be reassessed.
2. **Preferred path:** preserve 15a/15b independence; implement caching as per-agent fresh context with shared static prefix (tools + system-prompt), accepting that agent-to-agent continuity is not cached. This preserves both PREMISE-007 (tool-layer immutability) and 15a/15b independence.
3. **Block the 2026-04-27 rollout until resolved** — this is not a rollout-friendly disagreement; it is a foundational architecture decision.
4. **Test:** implement one test run under fresh-context-per-agent topology; measure cache-hit rate vs. the appended-turn projection; if the drop is >30%, reconsider; if <30%, adopt the independence-preserving topology.

**Status:** OPEN — BLOCKS 2026-04-27 rollout; awaits Tom review and architecture decision

**Priority:** HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** CACHING-ARCHITECTURE cluster (rollout-blocker); INTERNAL-CONSISTENCY cluster intersection (conflicts with ASSUMPTION-003 committed isolation); SELF-AWARENESS-META cluster adjacency (self-awareness-pipeline's value claim depends on this being resolved correctly).

---

### REVISE-[new]: ASSUMPTION-054
**Date flagged:** 2026-04-20
**Source item:** ASSUMPTION-054
**Item type:** ASSUMPTION
**Urgency:** MEDIUM (byte-stability is necessary but not sufficient; pair with cache-hit telemetry before rollout)

**Statement:** "Byte-stability smoke test is the sufficient verification that caching is working correctly"

**What is at risk:**
- False-sense-of-security: byte-stability confirms the input didn't drift, but does not confirm the cache actually hit. A cache-miss on stable input produces the same byte output at higher cost — byte-stability cannot detect this.
- Quality-regression blindness: byte-stability verifies output, not quality; pairs with PRESUMPTION-056 (cost-only gate) as the quality-verification gap.
- Precondition-gap: ASSUMPTION-050's 4 unaudited preconditions (ordering, encoding, path-resolution, churn) are not directly tested by byte-stability; the test needs extension.

**Evidence summary:**
15a PARTIALLY-SUPPORTED (Moderate) — byte-stability is a canonical correctness property for deterministic caching systems (Fowler 2018; content-addressable storage literature); necessary for correctness verification. 15b PARTIALLY-CHALLENGED (Moderate) — sufficiency claim is literature-challenged: observability / SRE literature (Beyer et al. 2016) prescribes multi-signal verification (correctness + economics + quality); cache-specific monitoring (CDN best practices 2020-2024) pairs byte-stability with cache-hit telemetry (not either alone). Byte-stability is necessary but strictly insufficient.

**Recommended action:**
1. **Extend the smoke test** to include cache-hit telemetry (verify actual cache hits, not just output byte-equality).
2. **Pair with quality-regression gate** (PRESUMPTION-056 remediation) — byte-stability is orthogonal to quality; both are needed.
3. **Extend to cover ASSUMPTION-050's 4 preconditions** (ordering, encoding, path-resolution, churn).
4. **Test:** run the byte-stability test alongside a deliberately-cache-missing reference run; verify the test can distinguish them.

**Status:** OPEN — awaits Tom review and test extension

**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** CACHING-ARCHITECTURE cluster; pairs with PRESUMPTION-056 (cost-only gate) as the gate-completeness package.

---

### REVISE-[new]: PRESUMPTION-056
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-056
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (cost-only gate is a documented anti-pattern; SYSTEMIC-RISK-FLAG; cheap fix available before 2026-04-27 rollout)

**Statement:** "Cost is the sole optimization target (no quality-regression smoke test in the rollout gate)"

**What is at risk:**
- Goodhart's Law pressure toward cost at quality's expense — single-metric optimization is a well-documented failure mode.
- LLM-specific quality regression (cache-breakpoint truncation, cache-miss fallback paths, attention-pattern interactions) is invisible to cost-only gates.
- Interaction with ASSUMPTION-053 REVISE: if 15a/15b independence is degraded by the appended-turn topology, that is a quality regression invisible to cost-only and byte-stability gates.
- Cumulative drift undetected until manifested in a downstream failure (e.g., degraded cross-tradition signal detection).

**Evidence summary:**
15a NO-SUPPORT-FOUND — no literature supports cost-only gates as sufficient for production rollout. 15b STRONGLY-CHALLENGED (Strong) with SYSTEMIC-RISK-FLAG — continuous-delivery literature (Humble & Farley 2010; Forsgren et al. 2018 "Accelerate"), ML Test Score (Chen et al. 2020; Google "Rules of Machine Learning"), Goodhart's Law (Manheim & Garrabrant 2019) all converge on requiring quality gates alongside cost gates. LLM-specific concerns (prompt-caching edge cases) compound the gap. The fix (add a judge-agent comparison of N pre/post samples) is cheap and standard.

**Recommended action:**
1. **Add a quality-regression smoke test to the rollout gate:** sample N=10 proposals pre-cache and post-cache; LLM-judge compare blind; any material delta blocks rollout.
2. **Define quality-floor thresholds** (e.g., no more than 10% of proposals judged worse).
3. **Instrument quality-adjacent signals continuously post-rollout** (proposal length, reasoning depth, citation count, cross-tradition-signal generation rate).
4. **Require quality-gate PASS + cost-gate PASS for rollout approval** — either gate failing blocks.
5. **Test:** dry-run the quality-regression test on current architecture output; calibrate the judge-agent threshold before the real gate.

**Status:** OPEN — BLOCKS 2026-04-27 rollout until quality gate added

**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** CACHING-ARCHITECTURE cluster (rollout-gate package); pairs with ASSUMPTION-054 (byte-stability gate extension) and ASSUMPTION-053 (appended-turn quality risk).

---

### REVISE-[new]: PRESUMPTION-057
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-057
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH ("measure, don't assume" violation; gates ASSUMPTION-052 cost projection; cheap audit)

**Statement:** "The 49 RC Wiki files are stable enough (no churn-rate audit performed)"

**What is at risk:**
- Cache-hit rate sensitivity to invalidation rate is nonlinear — modest churn increases can cut hit-rate by >50% (Fowler 2018 cache economics).
- Burst-edit patterns (Halfaker et al. 2013 on wiki-activity) cluster during active research phases — average churn under-represents peak invalidation.
- Mid-day edits create read-after-write races between editing and running sessions.
- Dependency chain: ASSUMPTION-052 cost projection depends on cache-hit rate depends on file stability depends on this presumption holding — three-link causal chain with silent-failure potential at each link.

**Evidence summary:**
15a NO-SUPPORT-FOUND — "slow-changing" is used descriptively without measurement; no literature argues for declaring stability in lieu of measuring it. 15b STRONGLY-CHALLENGED (Strong) — "measure, don't assume" is canonical (Google SRE book 2016; Nygard 2007; Fowler 2018); wiki-activity-burst literature shows averages under-represent peaks; cache-economics nonlinearity makes "probably slow enough" untested at the point of highest downside. C2A2's own OPERATIONAL-DRIFT cluster provides independent evidence that stability assumptions break down in practice. Test is cheap: git log over 4-8 weeks on the 49 files.

**Recommended action:**
1. **Run git log audit** on the 49 static-prefix files over the past 4-8 weeks: compute daily-edit-frequency histogram.
2. **Compare against cache-invalidation-rate threshold** derived from ASSUMPTION-052's cost projection; verify consistency.
3. **Set a cache-invalidation-rate alarm** that triggers if weekly rate exceeds threshold post-rollout.
4. **Consider an edit-lock / mid-day-edit-avoidance policy** during active caching periods.
5. **Document actual churn rate** as part of the rollout gate.
6. **Test:** `git log --follow --format=%ad -- <file>` on each of the 49 files over a 56-day window; aggregate; compare against the invalidation-rate threshold.

**Status:** OPEN — BLOCKS 2026-04-27 rollout until churn audit completed

**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** CACHING-ARCHITECTURE cluster (pre-rollout audit package); gates ASSUMPTION-052 cost projection and MONITOR-054 (ASSUMPTION-050 preconditions).

---

### REVISE-[new]: PRESUMPTION-059
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-059
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (silent-failure anti-pattern + 5 days in-house empirical failure evidence; OPERATIONAL-DRIFT cluster extension)

**Statement:** "Chrome profile auth for claude.ai is user-maintained out-of-band (no alternative ingestion channel defined)"

**What is at risk:**
- Silent-failure anti-pattern (Amblard & Bouchon 2013; monitoring literature): logging a failure and continuing is worse than crashing loudly.
- 5+ consecutive days of Chrome-related failures (2026-04-16 through 2026-04-20) — the out-of-band maintenance assumption is empirically failing.
- Repeated silent ingestion failure degrades cross-session context; self-awareness pipeline loses input signal without alarm; downstream C2A2 decisions made on incomplete signal.
- OPERATIONAL-DRIFT cluster extension — the cluster is growing as this channel's failures accumulate without escalation.

**Evidence summary:**
15a NO-SUPPORT-FOUND — no literature supports single-channel design with no escalation on 5+ days of consecutive failure. 15b STRONGLY-CHALLENGED (Strong) with SYSTEMIC-RISK-FLAG — graceful-degradation literature (Nygard 2007; Google SRE 2016), silent-failure anti-pattern literature (Amblard 2013), precondition-failure design-by-contract (Meyer 1992; Fowler 2018), cross-channel fallback (Woods 2015 resilience engineering) uniformly prescribe at minimum an ESCALATION trigger. C2A2's own OPERATIONAL-DRIFT cluster provides 5+ days of in-house empirical evidence that the single-channel design is failing. Cheap standard remediation: escalation trigger after 1 day of failure.

**Recommended action:**
1. **Add an escalation trigger:** Tom notified when Chrome auth fails for >1 consecutive day.
2. **Audit for alternative ingestion paths:** manual export; conversation-share links; API-level retrieval if available.
3. **Fallback primitive:** prompt Tom directly for walk-conversation content when automated ingestion fails.
4. **Add to the OPERATIONAL-DRIFT cluster's remediation package** — treat as one cluster-wide fix across PRESUMPTION-030, 031, 032, 044, 050, 059.
5. **Test:** simulate Chrome auth failure on a test day; verify escalation triggers; verify downstream awareness of degraded state.

**Status:** OPEN — awaits Tom review

**Priority:** MEDIUM (cheap remediation; 5-day failure record is concerning; part of cluster-wide remediation)

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** OPERATIONAL-DRIFT cluster (extended; now 7+ members including ASSUMPTION-042, PRESUMPTION-030, 031, 032, 044, 050, 059) — shared silent-failure anti-pattern across all channels. Also CACHING-ARCHITECTURE cluster adjacency (ingestion channel feeds into the walk-conversation context used by the pipeline).

---

### REVISE-[new]: PRESUMPTION-060
**Date flagged:** 2026-04-20
**Source item:** PRESUMPTION-060
**Item type:** PRESUMPTION
**Urgency:** HIGH (CRITICAL SELF-AWARENESS-META cluster 8th member; SYSTEMIC-RISK-FLAG; cluster-wide remediation warranted)

**Statement:** "Chat-side Claude endorsement functions as architectural validation (Claude-to-Claude agreement treated as cross-check)"

**What is at risk:**
- Same-model validation is a named anti-pattern: Zheng 2023 self-preference bias; Panickssery 2024 "LLM Evaluators Recognize and Favor Their Own Generations"; Page 2007 / Hong & Page 2004 on correlated-error ensembles.
- Architectural direction drifts under false validation signal.
- Self-awareness pipeline (which is supposed to catch bias) is undermined by its outer-loop dependence on same-model endorsement.
- Handoff primitives (DECISION-021, ASSUMPTION-044) that depend on Cowork↔Chat agreement inherit this risk.
- **CRITICAL SELF-AWARENESS-META cluster expansion to 8 members** — the cluster has been accumulating evidence for weeks that same-model self-reference is unreliable; PRESUMPTION-060 joins PRESUMPTION-015, 024, 041, 042, 046, 048, 052 as the 8th member. Cluster is now large enough to warrant standing cluster-wide remediation.

**Evidence summary:**
15a NO-SUPPORT-FOUND — no literature supports treating same-model agreement as independent cross-check. 15b STRONGLY-CHALLENGED (Strong) with SYSTEMIC-RISK-FLAG — same-model validation bias (Zheng 2023; Panickssery 2024), peer-review independence requirements (Cochrane methodology), echo-chamber / correlated-error literature (Page 2007; Hong & Page 2004), self-consistency-vs-cross-validation distinction (Wang et al. 2023), and C2A2's own accumulated 7-member SELF-AWARENESS-META cluster all converge. False-endorsement rate in LLM evaluators is materially higher than human baselines (Zheng 2023).

**Recommended action:**
1. **Language downgrade (minimum viable fix):** in all pipeline and briefing surfaces, "endorsed by Chat-side Claude" → "not disputed by Chat-side Claude"; explicit acknowledgment that endorsement is not validation.
2. **Introduce at least one non-Claude cross-check** for critical architectural reads (human review; or a different model family).
3. **Require disagreement-triggered review** rather than agreement-confirmation — flip the polarity so same-model disagreement is the signal.
4. **Cluster-wide SELF-AWARENESS-META remediation:** audit every signal where same-model agreement is treated as validation (all 8 cluster members); either downgrade the language or introduce non-Claude cross-checks across the pipeline.
5. **Test:** present a deliberately-wrong architectural read to Chat-side Claude; measure false-endorsement rate. If endorsement rate on wrong reads is high, the presumption is empirically broken.

**Status:** OPEN — awaits Tom review; CRITICAL cluster warrants cluster-wide remediation plan

**Priority:** HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** CRITICAL SELF-AWARENESS-META cluster (8 members): PRESUMPTION-015, 024, 041, 042, 046, 048, 052, 060. Cluster-wide remediation package recommended: audit every same-model agreement signal across the C2A2 pipeline; downgrade "endorsed" → "not disputed"; require human or cross-family cross-check for architectural-grade signals.

---

**Updated summary (2026-04-20 supplementary Run 2):**
Total REVISE items: 51 (45 prior + 6 new from 2026-04-20 supplementary Run 2 — ASSUMPTION-053, 054; PRESUMPTION-056, 057, 059, 060)
HIGH priority (new): ASSUMPTION-053 (conflicts with ASSUMPTION-003 isolation; rollout-blocker), PRESUMPTION-060 (CRITICAL SELF-AWARENESS-META 8th member)
MEDIUM-HIGH priority (new): PRESUMPTION-056 (cost-only gate; rollout-blocker), PRESUMPTION-057 (churn audit; rollout-blocker)
MEDIUM priority (new): ASSUMPTION-054 (byte-stability gate extension), PRESUMPTION-059 (escalation trigger; OPERATIONAL-DRIFT cluster extension)

**Cross-cluster coordination (2026-04-20 supplementary Run 2):**

CACHING-ARCHITECTURE cluster (NEW, 12 members spanning all 3 disposition buckets): PREMISE-007 INCORPORATED (ASSUMPTION-051); MONITOR-053 through 057 (ASSUMPTION-049, 050, 052; PRESUMPTION-055, 058); REVISE ASSUMPTION-053, 054 + PRESUMPTION-056, 057, 059, 060. Rollout gate 2026-04-27 requires: (a) ASSUMPTION-053 topology decision, (b) PRESUMPTION-056 quality gate added, (c) PRESUMPTION-057 churn audit completed. Without these three, 2026-04-27 rollout should be held.

SELF-AWARENESS-META cluster (extended to 8 members; CRITICAL by membership): PRESUMPTION-015, 024, 041, 042, 046, 048, 052, 060 — cluster-wide remediation warranted. Language downgrade ("endorsed" → "not disputed") is the cheapest cluster-wide fix; non-Claude cross-check is the stronger fix.

OPERATIONAL-DRIFT cluster (extended to 7+ members): ASSUMPTION-042, PRESUMPTION-030, 031, 032, 044, 050, 059 — shared silent-failure anti-pattern. Cluster-wide remediation: escalation trigger on precondition failure across all channels.

INTERNAL-CONSISTENCY cluster (new pair): ASSUMPTION-003 (15a/15b isolation) ↔ ASSUMPTION-053 (appended-turn topology) — first cluster entry where a CACHING-ARCHITECTURE item conflicts with a prior validated architectural commitment. Resolution requires an architecture-level decision on which commitment is senior.

Note on rollout blockers: Three of the 6 new REVISE items (ASSUMPTION-053, PRESUMPTION-056, PRESUMPTION-057) are hard blockers on the 2026-04-27 caching rollout. The cluster's high ratio of rollout-blocking issues (3/12 = 25%) reflects the supplementary Run 2's role as a pre-rollout architecture-review pass — the pipeline is surfacing exactly the gaps it was designed to surface, before the rollout commits C2A2 to them.

---

### REVISE-[new]: ASSUMPTION-058
**Date flagged:** 2026-04-21
**Source item:** ASSUMPTION-058
**Item type:** ASSUMPTION
**Urgency:** MEDIUM (substitutability unbenchmarked; inherits PRESUMPTION-062 transcript-ground-truth risk)

**Statement:** "Five-session coverage (wiki daily run, Hawkins/Hoffman specialist, Agent 16, chat scrape, morning walk handoff) is sufficient for a legitimate end-of-day brief despite no 14a/14b cycle having run"

**What is at risk:**
- Substitutability claim ("5 sessions substitute for the missed 14a/14b cycle") is unbenchmarked — no prior comparison of 5-session-without-14 vs. 14a/14b-cycle as information sources.
- Downstream consumers of the evening-sync brief may treat substitution as equivalent when it is in fact a graceful-degradation output.
- Compounds with PRESUMPTION-062 (transcript-as-ground-truth) — both ASSUMPTION-058 and PRESUMPTION-062 inherit the same "reading-about-own-state-counts-as-coverage" failure mode.
- First-observable instance of a "no-14-cycle" day — if the bar is set here without explicit framing, it becomes the precedent.

**Evidence summary:**
15a PARTIALLY-SUPPORTED (Weak-to-Moderate) — coverage-across-signals is a standard design pattern; but the specific claim of 5-session-sufficiency is not literature-backed at that size. 15b CHALLENGED (Moderate-to-Strong) — substitutability claims require empirical calibration; no benchmark exists for this specific substitution; compounds with PRESUMPTION-062 transcript-reliance risk.

**Recommended action:**
1. Reframe the claim from "sufficient" to "degraded-fallback coverage with known gaps" in the evening-sync brief and any downstream surfaces.
2. Explicitly list what the 14a/14b cycle would have produced but the 5-session coverage does not (e.g., formal presumption-surfacing).
3. Pair remediation with PRESUMPTION-062 reconciliation protocol.
4. Set a retrospective comparison — after the next 14a/14b cycle runs, compare what it surfaces against what was captured by the 5-session evening-sync; calibrate the substitutability claim.

**Status:** OPEN — awaits Tom review

**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** SELF-AWARENESS-META cluster adjacent (not a direct member; compounds via PRESUMPTION-062 pairing); narrative-channel-reliability sub-cluster.

---

### REVISE-[new]: ASSUMPTION-060
**Date flagged:** 2026-04-21
**Source item:** ASSUMPTION-060
**Item type:** ASSUMPTION
**Urgency:** MEDIUM (N-of-1 precedent; runaway-process concern; direct tension with DECISION-024)

**Statement:** "Read-only observation of still-running specialist sessions is the correct default (natural-termination precedent from 2026-04-19 Levin-Friston)"

**What is at risk:**
- Single-precedent default establishment is a known weak basis for design (Levin-Friston on 2026-04-19 is N=1).
- Direct tension with DECISION-024 (formal interrupt policy at turn cap): if natural-termination is the default, DECISION-024 is the exception; if DECISION-024 is the default, natural-termination is the exception. The two are currently undecided about their relative standing.
- Runaway-process concern: a read-only default means a stuck session continues to consume resources without triggering intervention until external observation catches it.
- Compounds with ASSUMPTION-059 (task-authority scope / no scheduler-override) — if the evening-sync task cannot fire 14a/14b manually AND the default response to a long-running session is read-only observation, the system has no active runaway-detection at the scheduled-task layer.

**Evidence summary:**
15a PARTIALLY-SUPPORTED (Weak-to-Moderate) — natural-termination is a valid pattern in some autonomous-agent frameworks; but not universally the default. 15b CHALLENGED (Strong) — N-of-1 precedent literature (Bayesian priors, selection effects); runaway-process patterns (Nygard "Release It!"; SRE circuit-breaker); DECISION-024 tension.

**Recommended action:**
1. Resolve the natural-termination vs. DECISION-024 tension explicitly: formalize DECISION-024 as the default, with natural-termination as the observed-outcome path within DECISION-024's turn-cap window.
2. Add a runaway-detection precondition to scheduled-task layer (even if it only surfaces the condition, not remediates — this addresses the read-only-default concern).
3. Require N>=3 precedent before establishing a default policy from empirical instances.
4. Pair with PRESUMPTION-063 (natural-termination-as-default) which challenges the same presumption at the presumption layer.

**Status:** OPEN — awaits Tom review

**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** Paired with PRESUMPTION-063 (same failure-mode at presumption layer); intersects DECISION-024 governance.

---

### REVISE-[new]: PRESUMPTION-061
**Date flagged:** 2026-04-21
**Source item:** PRESUMPTION-061
**Item type:** PRESUMPTION
**Urgency:** HIGH (STRONGLY-CHALLENGED; SYSTEMIC-RISK-FLAG; pre-flight mount-topology probe; pair with ASSUMPTION-055)

**Statement:** "Sandbox filesystem mount topology is presumed stable across scheduled-task runs"

**What is at risk:**
- Mount topology stability is explicitly counterindicated by container-runtime semantics (Docker/OCI mount propagation modes; 12-Factor App V — config stored in environment varies per run) and is not guaranteed by the platform.
- Empirical evidence: Phase 6 failure is itself the counterexample to the stability presumption — if topology were stable, the failure mode would not have appeared today.
- ASSUMPTION-055 (Phase 6 diagnosis) depends on topology stability to be a meaningful diagnosis; without stability, the diagnosis is day-local.
- Silent failure class: mount-topology changes do not fire their own event; they are detected only when a downstream operation fails on them.
- SYSTEMIC-RISK-FLAG: every scheduled task that reaches host artifacts depends on this presumption.

**Evidence summary:**
15a NO-SUPPORT-FOUND — no literature supports treating mount topology as stable-by-default across container runtime invocations. 15b STRONGLY-CHALLENGED (Strong) with SYSTEMIC-RISK-FLAG — container mount semantics (Docker propagation modes, OCI spec), 12-Factor App V (config per-run), empirical evidence from today's failure, SRE silent-failure class.

**Recommended action:**
1. Implement a pre-flight mount-topology probe in every scheduled-task entry point (list mounts; verify required paths are present; fail loudly on missing mounts rather than silently on downstream operations).
2. Log mount topology to a dedicated stream per run for longitudinal comparison.
3. Pair remediation with ASSUMPTION-055 MONITOR — the probe is the instrument that would allow MONITOR-058 to promote to INCORPORATE (stable topology observed over >=10 consecutive runs).
4. Pre-flight probe must be in place before the 2026-04-27 caching rollout — Phase 6 commit path cannot be relied upon without it.

**Status:** OPEN — awaits Tom review; pre-rollout gate recommended

**Priority:** HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** OPERATIONAL-DRIFT cluster at infrastructure layer; paired with ASSUMPTION-055 MONITOR-058.

---

### REVISE-[new]: PRESUMPTION-062
**Date flagged:** 2026-04-21
**Source item:** PRESUMPTION-062
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (SELF-AWARENESS-META cluster 10th member; SYSTEMIC-RISK-FLAG; reconciliation protocol required)

**Statement:** "The evening-sync task treats its own reading of session transcripts (via session_info MCP) as ground truth — no cross-validation against a second source"

**What is at risk:**
- Single-source ground-truth is a known anti-pattern in observability (triangulation methodology; Denzin; Creswell).
- MCP read failures are silent: a failed transcript read returns empty-or-partial data that looks indistinguishable from "nothing happened."
- SELF-AWARENESS-META cluster 10th member — the cluster has now crossed critical-mass threshold. This presumption is the 10th instance of "self-referential measurement treated as adequate without cross-check" in the C2A2 architecture.
- PRESUMPTION-015 precedent: STRONGLY-CHALLENGED on exactly this pattern at the same-model-validation layer; the same critique applies at the data-source layer.
- Downstream consumers (evening-sync brief, MONITOR items, REVISE items) inherit the risk — a missed transcript becomes an invisible gap in all derived artifacts.

**Evidence summary:**
15a NO-SUPPORT-FOUND — no literature supports treating a single opaque data source as ground truth without cross-validation. 15b CHALLENGED (Strong) with SYSTEMIC-RISK-FLAG — triangulation methodology, observability best practices, PRESUMPTION-015 precedent, SELF-AWARENESS-META cluster critical-mass evidence.

**Recommended action:**
1. Implement a reconciliation protocol: for every session transcript read, cross-check against at least one of (a) filesystem artifacts produced by that session, (b) scheduled-task log records, or (c) external observation signals (chat logs, user-visible outputs).
2. Epistemic-status labeling: any observation derived from single-source MCP read must be labeled "derived-from-MCP-read" so downstream reasoning can weight it appropriately.
3. Pair with PRESUMPTION-069 (absence-of-cycle not first-class) — same cluster, joint fix opportunity.
4. Consider promoting this to a cluster-wide SELF-AWARENESS-META architectural remediation (paired with PRESUMPTION-015, 024, 041, 042, 046, 048, 052, 060, 069).

**Status:** OPEN — awaits Tom review

**Priority:** MEDIUM-HIGH

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** SELF-AWARENESS-META cluster (10 members, critical mass). Cluster-level architectural fix recommended over per-member patches. Joint-remediation candidates: PRESUMPTION-015, 024, 041, 042, 046, 048, 052, 060, 069.

---

### REVISE-[new]: PRESUMPTION-063
**Date flagged:** 2026-04-21
**Source item:** PRESUMPTION-063
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (direct tension with DECISION-024; N-of-1 precedent; formalize DECISION-024 as resolution)

**Statement:** "'Natural termination' is an acceptable default resolution for scheduled tasks that appear to be running indefinitely"

**What is at risk:**
- Direct tension with DECISION-024 (formal turn-cap interrupt policy). The two cannot both be default.
- N-of-1 precedent: "natural termination works" is a single-case observation from 2026-04-19 Levin-Friston; not a pattern.
- Runaway-process concern: accepting natural-termination as default means a stuck task consumes resources without intervention until external observation catches it. In the worst case, scheduled tasks accumulate over days before manual review.
- Pattern partnership with ASSUMPTION-060 (read-only-only default) — both items propose non-intervention defaults for long-running sessions; together they leave the C2A2 system without an active runaway-detection mechanism at the scheduled-task layer.

**Evidence summary:**
15a NO-SUPPORT-FOUND — no literature supports natural-termination as the default resolution policy for indefinite-running autonomous tasks. 15b CHALLENGED (Moderate-to-Strong) — circuit-breaker / runaway-process literature (Nygard), default-resolution-policy literature (Beyer SRE), DECISION-024 tension.

**Recommended action:**
1. Formalize DECISION-024 as the canonical default (turn-cap interrupt); record natural-termination as an observable outcome that can occur within DECISION-024's policy window but is not itself the policy.
2. Instrument an active runaway-detection precondition at the scheduled-task layer (even if it only surfaces, not remediates).
3. Pair remediation with ASSUMPTION-060 (N-of-1 precedent default) — same failure-mode at the assumption layer.
4. Require N>=3 evidence before establishing any new default resolution from empirical instances.

**Status:** OPEN — awaits Tom review

**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** Paired with ASSUMPTION-060 (same failure at assumption layer); intersects DECISION-024 governance; runaway-process cluster candidate.

---

### REVISE-[new]: PRESUMPTION-064
**Date flagged:** 2026-04-21
**Source item:** PRESUMPTION-064
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (CHALLENGED Strong; implement Monday-recommended alert; pair with PRESUMPTION-069)

**Statement:** "Narrative-level surfacing of a missing scheduled-task run is adequate without an alert firing"

**What is at risk:**
- Monitoring-as-code literature (Prometheus, Datadog, Google SRE Ch. 6) uniformly treats narrative-only surfacing as inadequate for liveness/absence signals. Absence-of-expected-event is a primary silent-failure signature.
- Detection latency: narrative surfacing runs on human read-cycle time (O(day)); alert firing runs on O(minute). The difference is the detection-latency delta and is material.
- Channel-reliability dependency: narrative channels are predicted to drop reliability during the external-visit-week (PRESUMPTION-066 compounding). Exactly the window in which narrative-only adequacy fails.
- Ready-made mitigation: Chat-side Claude articulated on Monday the specific alert spec — "≤25h since last self-awareness run." Today is the first observable case; the recommendation has not been implemented.
- Paired with PRESUMPTION-069 — both rely on narrative channel for absence-of-cycle conditions.

**Evidence summary:**
15a NO-SUPPORT-FOUND — event-sourcing literature requires deliberate absence-representation (timeout events, heartbeat events) that C2A2 does not have. 15b CHALLENGED (Strong) — monitoring-as-code, detection-latency, channel-reliability.

**Recommended action:**
1. Implement Monday-recommended "≤25h since last self-awareness run" alert. Specification exists; cost is low.
2. Pair with PRESUMPTION-069 as the anchor for SELF-AWARENESS-META cluster remediation.
3. Elevate absence-of-expected-event to a first-class architectural event class in the scheduled-task layer (draft DECISION-NNN).
4. Instrument detection-latency measurement: record time from absence-event to human-observation across the 30-day window following alert implementation.

**Status:** OPEN — awaits Tom review

**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** Narrative-channel-reliability sub-cluster (PRESUMPTION-064, PRESUMPTION-066 MONITOR-061, PRESUMPTION-069). Implementation of Monday-recommended alert is the cluster-anchor remediation.

---

### REVISE-[new]: PRESUMPTION-067
**Date flagged:** 2026-04-21
**Source item:** PRESUMPTION-067
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (extend DECISION-022 scope to specialist self-eval; pair with PRESUMPTION-053 unaudited-filter remediation)

**Statement:** "Specialist self-evaluation of 'honest null' is adequate without downstream filter-audit check"

**What is at risk:**
- Self-evaluation-without-audit is the documented failure pattern of the unaudited-filter cluster (PRESUMPTION-053).
- File-drawer and convenient-null literature (Rosenthal 1979; Fanelli 2012; Ioannidis 2005) show that null-judgment by the producer of the null is systematically lenient (producer has incentive to declare null).
- PREMISE-008 (ASSUMPTION-056 honest-null-over-thin-proposals) depends on the honest-null being honest — if the null-judgment is unaudited, the premise is load-bearing on an unvalidated signal.
- DECISION-022 established audit requirements for downstream filters; specialist self-eval is a parallel surface that has not been brought into DECISION-022's scope.

**Evidence summary:**
15a WEAK-SUPPORT (Weak-to-Moderate) — self-evaluation is a valid first-pass; but no literature supports skipping a downstream audit when the null carries downstream load. 15b CHALLENGED (Moderate-to-Strong) — PRESUMPTION-015 precedent (same failure at agent-self-audit layer), PRESUMPTION-053 unaudited-filter cluster, file-drawer literature, convenient-null pattern.

**Recommended action:**
1. Extend DECISION-022 scope to explicitly cover specialist self-evaluation of null-output judgments.
2. Implement a sampling-audit: 10-20% of specialist null-declarations reviewed by a second pass (non-specialist or human) for 30 days; measure false-null rate.
3. Pair remediation with PRESUMPTION-053 (unaudited-filter cluster anchor) and ASSUMPTION-057 MONITOR-059 (17→11 filter rule application) — same cluster, joint audit protocol.
4. If false-null rate > 10%, revise PREMISE-008 qualification to require audit-confirmed null rather than self-declared null.

**Status:** OPEN — awaits Tom review

**Priority:** MEDIUM

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** Unaudited-filter cluster (PRESUMPTION-053 REVISE, ASSUMPTION-057 MONITOR-059, this item REVISE). Cluster-level fix: DECISION-022 scope extension to all upstream filter/judgment surfaces.

---

### REVISE-[new]: PRESUMPTION-069
**Date flagged:** 2026-04-21
**Source item:** PRESUMPTION-069
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH (STRONGLY-CHALLENGED; SYSTEMIC-RISK-FLAG; anchor for SELF-AWARENESS-META cluster cluster-level remediation; implement Monday alert)

**Statement:** "The absence of a 14a/14b cycle during business hours on 2026-04-21 is tracked in narrative but not as its own first-class architectural event"

**What is at risk:**
- Heartbeat-pattern literature (Lamport 1978; Kafka/Kreps 2013) and silent-failure SRE literature (Google SRE book Ch. 6; Nygard 2007) both treat absence-of-expected-event as canonical alert-firing.
- SELF-AWARENESS-META cluster 10th member (critical mass). Per-member deferral is itself the failure mode the cluster keeps instantiating.
- Chat-side Claude articulated the mitigation on Monday ("≤25h since last self-awareness run" alert). Today is the first observable case; the recommendation remains unimplemented at the exact moment it was needed.
- Pipeline-integrity dependency: tomorrow's 14a/14b cycle depends on today's completion for chain continuity; detection-latency > 24h makes cycle-based reasoning unreliable.
- external-visit-week attention scarcity (PRESUMPTION-066 compounding): narrative-channel reliability is predicted to drop through 2026-04-26 — the adequacy argument is explicitly undermined by a concurrent presumption.
- SYSTEMIC-RISK-FLAG: anchor for SELF-AWARENESS-META cluster cluster-level remediation.

**Evidence summary:**
15a NO-SUPPORT-FOUND — absence-as-architectural-event requires deliberate instrumentation that C2A2 lacks. 15b STRONGLY-CHALLENGED (Strong) — heartbeat/silent-failure/cluster critical mass / Monday-recommendation-readiness all contradict narrative-only adequacy.

**Recommended action:**
1. Implement Monday's "≤25h since last self-awareness run" alert. Specification exists; low cost; anchor mitigation.
2. Draft a DECISION-NNN formalizing absence-of-expected-event as first-class in the scheduled-task layer.
3. Pair with PRESUMPTION-062 (transcript ground truth) and PRESUMPTION-064 (narrative-adequate) as joint cluster-level fix.
4. Treat this item as the anchor for SELF-AWARENESS-META cluster remediation — the cluster has crossed critical mass and warrants a cluster-wide architectural fix rather than per-member patches.
5. Test: instrument "absent(self_awareness_cycle_last_run) > 25h" as alert for 30 days; measure detection-latency delta vs. narrative-only; correlate alerts with downstream pipeline-integrity issues.

**Status:** OPEN — awaits Tom review; CRITICAL cluster-anchor warrants cluster-wide remediation plan

**Priority:** MEDIUM-HIGH (cluster-anchor role elevates from MEDIUM)

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

**Cluster note:** SELF-AWARENESS-META cluster (10 members, anchor). Narrative-channel-reliability sub-cluster (PRESUMPTION-064, PRESUMPTION-066 MONITOR-061, PRESUMPTION-069). Recommendation: treat as anchor for cluster-level architectural fix.

---

**Updated summary (2026-04-21):**
Total REVISE items: 59 (51 prior + 8 new from 2026-04-21 — ASSUMPTION-058, 060; PRESUMPTION-061, 062, 063, 064, 067, 069)
HIGH priority (new): PRESUMPTION-061 (sandbox mount topology; SYSTEMIC-RISK-FLAG; pre-rollout gate recommended)
MEDIUM-HIGH priority (new): PRESUMPTION-062 (transcript ground truth; SELF-AWARENESS-META 10th member; SYSTEMIC-RISK-FLAG), PRESUMPTION-069 (absence-of-cycle; SYSTEMIC-RISK-FLAG; cluster anchor)
MEDIUM priority (new): ASSUMPTION-058 (five-session coverage substitutability), ASSUMPTION-060 (N-of-1 read-only default), PRESUMPTION-063 (natural-termination default), PRESUMPTION-064 (narrative-surfacing adequacy), PRESUMPTION-067 (specialist self-eval adequacy)

**Cross-cluster coordination (2026-04-21):**

SELF-AWARENESS-META cluster (extended to 10 members; CRITICAL MASS): PRESUMPTION-015, 024, 041, 042, 046, 048, 052, 060, 062, 069 — 10-member threshold crossed; per-member deferral is itself the failure mode. Cluster-level architectural fix recommended. PRESUMPTION-069 is the natural cluster-anchor; ready-made mitigation (Monday "≤25h" alert) is implementation-ready.

Narrative-channel-reliability sub-cluster (NEW, surfaced 2026-04-21): PRESUMPTION-064 REVISE + PRESUMPTION-066 MONITOR-061 + PRESUMPTION-069 REVISE + PRESUMPTION-051 staleness. Compounding pattern: narrative-channel reliability drops during external-visit-week AND narrative-adequate presumptions load-bear on it. Anchor remediation: implement Monday-recommended alert.

OPERATIONAL-DRIFT cluster (extended at infrastructure layer): PRESUMPTION-061 sandbox mount topology + ASSUMPTION-055 Phase 6 diagnosis. Joint remediation: pre-flight mount-topology probe in scheduled-task entry points.

Unaudited-filter cluster (extended to 3 members): PRESUMPTION-053 REVISE + ASSUMPTION-057 MONITOR-059 + PRESUMPTION-067 REVISE. Cluster-level fix: DECISION-022 scope extension to specialist self-eval and filter application audits.

INTERNAL-CONSISTENCY cluster (extended): ASSUMPTION-060 ↔ DECISION-024 (natural-termination vs. turn-cap interrupt); ASSUMPTION-058 ↔ PRESUMPTION-062 (coverage-substitutability relies on transcript-as-ground-truth).

Note on cluster critical-mass signal: The SELF-AWARENESS-META cluster at 10 members is the first critical-mass signal the pipeline has produced. The recommendation to treat the cluster as a single architectural concern (rather than continuing per-member patches) is itself an output of the self-awareness pipeline examining its own outputs — a meta-level surfacing that the pipeline is working as designed even while its individual members surface the same failure mode repeatedly.


---

## 2026-04-27 RUN — New Revision Flags

### REVISE-[new]: ASSUMPTION-063
- **Date flagged:** 2026-04-27
- **Item type:** ASSUMPTION
- **Urgency:** HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** Demote-and-elevate move challenged by Stump scholarship and convergence skepticism. PRESUMPTION-070 and PRESUMPTION-071 (structural dependencies) also challenged. Tom should review the demotion stance before downstream synthesis use.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-070
- **Date flagged:** 2026-04-27
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Stump scholarship treats metaphysics as load-bearing for ethics; decomposability is contested. Tension with ASSUMPTION-067 is structural. Tom should resolve.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-071
- **Date flagged:** 2026-04-27
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Levin/Hoffman/Kastrup are anti-physicalist allies, not a coherent monist convergence. Treating them as convergent imports a fictitious unanimity into ASSUMPTION-063.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-074
- **Date flagged:** 2026-04-27
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Specialist-recognition reliability is contested by LLM-evaluation literature. SYSTEMIC-RISK: three same-week ASSUMPTIONs (063, 065, 066) plus ASSUMPTION-067 depend on this. Tom should consider an independent-verification tier.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-075
- **Date flagged:** 2026-04-27
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + moderate-to-strong challenge → REVISE. Browser-extension workarounds are a fragility surface; 'permanent' is too strong. Treat as conditional with success-threshold monitoring. Ties to OPEN-039.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-076
- **Date flagged:** 2026-04-27
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Moderate)
- **What is at risk / Recommended action:** PRESUMPTION + moderate challenge → REVISE. Native curation outperforms canonical-works fallback for structured downstream tasks; 'methodologically equivalent' is too strong. Block on native curation for Wright/Rohr before downstream use.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-078
- **Date flagged:** 2026-04-27
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None (Novel at specific level))
- **15b (AGAINST):** CHALLENGED (strength: Moderate)
- **What is at risk / Recommended action:** Novel pairing without literature attestation; level-of-analysis error suspected. Direct tension with ASSUMPTION-063 unresolved. Tom should review the bridge construction or downgrade to 'suggestive analogy'.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-079
- **Date flagged:** 2026-04-27
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + moderate-to-strong challenge → REVISE. Technical literature treats Carroll and Arkani-Hamed as parallel-but-distinct programs; same-shift framing is rhetorical. ASSUMPTION-065 should be reframed as 'parallel programs.'
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-080
- **Date flagged:** 2026-04-27
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + moderate-to-strong challenge → REVISE. Science-tradition and theology-tradition primitives differ; PRS-triplet transfer is contested. Either confirm transfer empirically or introduce a separate primitive for theology-traditions.
- **Awaiting Tom review.**


## 2026-04-28 RUN — New Revision Flags

### REVISE-[new]: ASSUMPTION-078
- **Date flagged:** 2026-04-28
- **Item type:** ASSUMPTION
- **Urgency:** HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** Two parallel sandbox-infrastructure failure modes (auth gap, mount topology) treated as user-fixable contradicts both literature (Reason; SRE toil; Norman) and C2A2's own prior dispositions (PRESUMPTION-061 REVISE 2026-04-21; PRESUMPTION-068 MONITOR 2026-04-21). The OPEN-039 cluster has been growing for weeks. Reclassify both failure modes as escalation-required; add pre-flight checks or circuit-breakers; track user-fix occurrence as a metric. Joint remediation with REVISE-[new]: PRESUMPTION-083 and REVISE-[new]: PRESUMPTION-084.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-081
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. The "without quality degradation" claim is empirically unsupportable from operational record alone and is contradicted by batch-evaluation literature (Hertwig & Pleskac; Danziger et al.; Kahneman). Reframe as "single-cycle drains are feasible at throughput; quality variance across batch position is acknowledged and mitigated." Add depth-per-item documentation; randomize batch order; sample-cross-check.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-082
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Refresh-cycle null reports without depth documentation are unreliable per Cochrane LSR explicit precondition. C2A2 currently produces 39+ same-day carry-forwards without depth pairing — silent staleness is operationally consistent with the data. Document refresh-cycle search depth; periodic depth-matched audits; flag carry-forward beyond N cycles for explicit re-evaluation.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-083
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Indefinite user-fixability is the canonical "blame the user" anti-pattern. The OPEN-039 cluster (PRESUMPTION-061, PRESUMPTION-068, this) has been growing for weeks. Add an escalation tier with explicit triggers; track user-fix occurrence rate as a metric. Joint remediation with REVISE-[new]: ASSUMPTION-078 and REVISE-[new]: PRESUMPTION-084.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-084
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Pattern-blind scheduling (recurring pre-flight stalls without architectural response) is the documented anti-pattern (Nygard "Release It!"; Beyer SRE). Open DECISION-026 candidate for pre-flight grant pattern; add circuit-breaker on N consecutive pre-flight stalls; join PRESUMPTION-069 cluster remediation track.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-085
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. PREMISE-012 was ratified at 4-day staleness with no upper bound; literal scope-extension failure mode (Reason; Shewhart; Wheeler). Specify an explicit upper bound on PREMISE-012 (e.g., 7-day reapply-with-caveat, 14-day re-derive). Tie to PRESUMPTION-077 / MONITOR-069 monitor cadence.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-087
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE (highest urgency tier). Self-correction without external check is not a calibration mechanism. Compounds 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074, specialist-recognition reliability). Add an audit pattern: require override to cite specific evidence; sample-based justification review; track override rate as metric. Joint remediation with REVISE-[new]: PRESUMPTION-074 from 2026-04-27 cycle.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-088
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + moderate-strong challenge → REVISE. Acknowledging "this is my re-description" only in the master document does not propagate the caveat. Per-tradition wiki files become tacit voice-of-tradition documents. Propagate the author-frame caveat to every per-tradition file; add disambiguation cues to specialist agent prompts; include the caveat in synthesis outputs. Pairs with PREMISE-014 INCORPORATE.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-089
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Recursive-specialist-reading is the operational form of the 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074). Specialists prompted with Tom's PRS framings will report on those framings as if they were tradition-internal, producing artifactual convergence. ASSUMPTION-065/066/067 specialist outputs from yesterday inherit this risk directly. Add disambiguation cues to specialist prompts; add an independent-verification tier; joint remediation with PRESUMPTION-074 SYSTEMIC-RISK and PRESUMPTION-088.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-091
- **Date flagged:** 2026-04-28
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Unbounded queues are documented anti-pattern (Kingman; Goldratt; Reinertsen). 33 items deep is past saturation point for high-quality review by literature benchmarks. Define a queue-depth ceiling; trigger explicit prioritization when ceiling approached; link to PRESUMPTION-077 monitor cadence.
- **Awaiting Tom review.**

---

## 2026-05-05 cycle REVISE additions (11 new items)

### REVISE-[new]: ASSUMPTION-086
- **Date flagged:** 2026-05-05
- **Item type:** ASSUMPTION
- **Urgency:** HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** Treating specialist self-attributed superlatives as primary cross-tradition signal contradicts expert-judgment, Delphi, wisdom-of-crowds, and self-assessment-validity literatures. PREMISE-013 (specialist N-collisions) is C2A2's own validated requirement and is silently bypassed. Compounds 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074) without remediation; recurrence-without-remediation pattern. Open DECISION-027 candidate (specialist-self-attribution adjudication tier); enforce PREMISE-013 N-collisions as gate before primary-signal status; add deflation pass on superlative inflation; joint remediation with 2026-04-27 SYSTEMIC-RISK and 2026-04-28 PRESUMPTION-088/089.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-093
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Structural equivalence broken by temporal-clustering effects, shared-context bias, and within-cluster correlation; PRESUMPTION-status removes the prompt to test preconditions. Surface as stated assumption (then inherits ASSUMPTION-079 MONITOR cadence); test stationarity preconditions; randomize per-specialist prompt context within catch-up window.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-094
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. fireAt workaround was deployed without blast-radius analysis vs. C2A2 self-awareness pipeline; cross-task interaction effects (ordering, idempotency, resource contention) plausible given catch-up fires in same window as self-awareness pipeline. Surface explicit blast-radius analysis; document expected interactions; stagger catch-up runs against self-awareness pipeline; joint remediation with scheduler-workaround cluster (ASSUMPTION-080/081, PRESUMPTION-102).
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-095
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Single-strategy null is consistent with both exhaustion and method failure; literature unanimous on requiring multi-strategy variation. Bibliometric literature reports ±50% variance from query-form alone. Add fallback query-form variation before declaring exhaustion; document Phase-2 search depth; joint remediation with ASSUMPTION-084 MONITOR-084 and Phase-2 search-method gap SYSTEMIC-RISK.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-096
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Recurrence of 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074) without remediation is the strongest signal of structural failure on self-tagging-as-primary-signal pattern. Confirmation bias in own-output evaluation is well-documented. Joint remediation with ASSUMPTION-086 REVISE under DECISION-027 candidate; enforce PREMISE-013 N-collisions; add independent-adjudication tier.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-097
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Multiple parallel "strongest" claims are logically inconsistent without rescaling; same-day batch concentrates superlative inflation. Compounds ASSUMPTION-086 / PRESUMPTION-096 cluster. Explicitly rescale "strongest" to "among-strongest" with N specified; require ranking when superlatives compose across specialists; deflation pass per cycle; joint remediation under DECISION-027 candidate.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-098
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Informal-as-canonical is documented anti-pattern (Bass/Clements/Kazman; Nygard; Maier; Power). PRESUMPTION-041 cluster recurrence indicates structural absence of canonization step. Lift the six 2026-05-05 walk-thread decisions to DECISION-NNN entries; add canonization step to walk-thread extraction routine; joint remediation with PRESUMPTION-041 cluster.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-099
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Layer coherence and non-overlap are not defaults; require explicit isolation patterns (Garlan/Allen/Ockerbloom; Buschmann). Joint treatment with ASSUMPTION-082 (HIGH-priority MONITOR-082). Add layer-isolation tests with cross-layer-item examples; articulate feedback-loop design between layers.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-100
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Cybernetics-101 failure mode: self-aware system with feedback-gap on a foundational assumption. ASSUMPTION-007 PARTIALLY-CHALLENGED status now an explicit dependent of this gap — without feedback the status cannot improve. Add feedback channel from specialist outputs to foundational-assumption status; cross-link in 14a/14b protocol; periodic re-evaluation of stale-status assumptions.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-101
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** LOW-MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Doc-implementation equivalence-by-default is documented anti-pattern; popover/tooltip text is highest-drift documentation surface. Remediation is low-cost: add snapshot test on popover content to existing validate_html.py pipeline; add integration test on filter semantics. Small ticket; remediates concretely.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-102
- **Date flagged:** 2026-05-05
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Cross-path determinism is not a default in distributed schedulers; literature unanimous on requiring cross-path testing. Load-bearing for ASSUMPTION-081 workaround scope. Cross-path test (3+ creation paths with single-link tasks); document workaround scope per path; joint remediation with ASSUMPTION-080 disambiguation under scheduler-workaround SYSTEMIC-RISK cluster.
- **Awaiting Tom review.**

---

**2026-05-05 REVISE summary:**
- 11 new REVISE entries: ASSUMPTION-086 (HIGH); PRESUMPTION-096 (HIGH); PRESUMPTION-094, 097, 100 (MEDIUM-HIGH); PRESUMPTION-093, 095, 098, 099, 102 (MEDIUM); PRESUMPTION-101 (LOW-MEDIUM)
- Cluster signals: 5 of 11 REVISEs anchor cluster-level architectural responses (DECISION-027 candidate; scheduler-workaround migration plan; RC Explorer L1/L2/L3 isolation specification; foundational-assumption feedback channel; walk-thread canonization).
- Specialist-self-attribution cluster (ASSUMPTION-086 + PRESUMPTION-096 + PRESUMPTION-097) is the principal architectural action surfaced this run; recurrence of 2026-04-27 SYSTEMIC-RISK without remediation.

---

## 2026-05-09 cycle REVISE additions (9 new items)

### REVISE-[new]: PRESUMPTION-105
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Implicit cross-session persistence without registry entry is documented anti-pattern across distributed-systems, workflow-management, and agent-systems literatures; empirical drop rates 5–30% under load. Third recurrence of cross-session persistence cluster (PRESUMPTION-046 / PRESUMPTION-043 / PRESUMPTION-105) confirms structural absence of registration step. Add registry entry for items queued at end-of-session; instrument drop rate; explicit handoff at session end. Joint remediation with prior PRESUMPTION-046 / PRESUMPTION-043 cluster.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-106
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Self-evident classification is empirically refuted by inter-rater-reliability literature; ADR practice exists precisely because architectural-decision boundaries are not self-evident. Third recurrence of implicit-decision-drift cluster (PRESUMPTION-098 / PRESUMPTION-041 / PRESUMPTION-106). Write canonization criterion (small artifact); run inter-rater test on existing categorization; explicit promotion review on a fixed cadence. Joint remediation with PRESUMPTION-098 walk-thread canonization track.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-107
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Service-side-default attribution at N=2 is documented availability bias; SRE / quota / postmortem / causal-inference literatures uniformly require balanced two-side enumeration. Compounds with PRESUMPTION-104 (naming misclassification) — both presumptions short-circuit investigation. Instrument usage-pattern signals (call rate, concurrency, session duration); capture wire-level response signature for each interrupt; run two-side enumeration before service-side framing. Joint remediation with PRESUMPTION-104 wire-level inspection track.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-108
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Human-noticing as primary alert is empirically refuted; SRE / ops research literature uniformly recommends automated stall-pattern alerts. Third recurrence of monitoring-meta cluster (PRESUMPTION-035 / PRESUMPTION-052 / PRESUMPTION-108) plus the explicit prediction by SELF-AWARENESS-META cluster anchor (PRESUMPTION-069). The empirical pattern (5-day silence in 2026-04-26 run; 2-day silence triggering this 2026-05-08 run) confirms the literature's prediction. Implement automated ≤25h stall alert per PRESUMPTION-069 recommendation; configure cross-task watchdog; cluster-level remediation. HIGH urgency given recurrence-without-remediation pattern at the SELF-AWARENESS-META layer.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-109
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Compositional equivalence between LLM reviews without weighting protocol aggregates shared blind spots rather than averaging them; cross-LLM training-data overlap is documented and material. Three-item cluster (ASSUMPTION-089 / PRESUMPTION-109 / PRESUMPTION-115) signals structural absence of weighting/adjudication protocol. Adopt epistemic-weight protocol; use third LLM with different training corpus or human reviewer; document divergence cases. Joint remediation under review-aggregation cluster.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-110
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Same-architectural-layer is canonical bundling criterion only when verified; presumed-same-layer without verification is documented as dilution-prone. ITIL severity discipline requires explicit layer assignment before bundling. Load-bearing for ASSUMPTION-094 (N≥5 bundling). Add explicit layer tagging per item before bundling; layer-shared verification step; atomic-report items that fail layer verification. Joint remediation with ASSUMPTION-094 MONITOR-094 under cross-project-escalation track.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-111
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Three-strikes is the canonical fallback-design threshold; SRE / fault-tolerance / authentication-design literatures uniformly require fallback at this point. The presumption inverts the canonical disposition. Third recurrence of cowork-to-chat sync cluster (ASSUMPTION-071 / PRESUMPTION-038 / PRESUMPTION-111). Design fallback channel (manual export, email, alternate API); document three-strikes threshold and adhere to it; cluster-level remediation across recurrences. Joint remediation with ASSUMPTION-071 / PRESUMPTION-038 cluster.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-114
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Recency-priority cause attribution is documented availability bias; causal-inference, debugging, SRE-postmortem literatures uniformly require alternative-cause enumeration. Pairs with ASSUMPTION-092 MONITOR-092 (regression hypothesis) — the presumption short-circuits exactly the enumeration step that ASSUMPTION-092's PARTIALLY-SUPPORTED disposition flagged. Run alternative-cause enumeration (≥3 alternatives) before attribution commitment; diagnostic probe to distinguish causes; reframe as "working hypothesis" rather than "most-likely cause". Joint remediation with ASSUMPTION-092 MONITOR-092.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-115
- **Date flagged:** 2026-05-09
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Near-verbatim adoption of external-LLM prioritization without project-context adjudication is recurrence of 2026-04-27 PRESUMPTION-074 SYSTEMIC-RISK at a new operational layer (external-tool-review). Third instance of the "one source treated as primary signal without adjudication" pattern across (a) specialist self-attribution (PRESUMPTION-074), (b) author-frame propagation (PRESUMPTION-088/089), and now (c) external-LLM prioritization (PRESUMPTION-115). HIGH urgency given recurrence-without-remediation pattern. Add local-adjudication step before adoption; explicit weight protocol; document divergence cases. Joint remediation under DECISION-027 candidate (specialist-self-attribution adjudication tier) extended to cover external-tool-review layer.
- **Awaiting Tom review.**

---

**2026-05-09 REVISE summary:**
- 9 new REVISE entries: PRESUMPTION-108 (HIGH); PRESUMPTION-115 (HIGH); PRESUMPTION-105, 107, 109, 111 (MEDIUM-HIGH); PRESUMPTION-106, 110, 114 (MEDIUM)
- Cluster signals: 6 of 9 REVISEs anchor or extend cluster-level architectural patterns:
  1. **SELF-AWARENESS-META cluster recurrence** (PRESUMPTION-108): fourth recurrence at the monitoring layer; the predicted alert (≤25h stall watchdog) remains unimplemented.
  2. **Cross-session persistence cluster** (PRESUMPTION-105): third recurrence of registry-entry gap.
  3. **Implicit-decision-drift cluster** (PRESUMPTION-106): third recurrence of canonization-criterion gap.
  4. **Specialist/external-source primary-signal cluster** (PRESUMPTION-115): recurrence of 2026-04-27 SYSTEMIC-RISK at external-tool-review layer; DECISION-027 candidate scope extension.
  5. **Review-aggregation cluster** (PRESUMPTION-109 + ASSUMPTION-089 MONITOR-089 + PRESUMPTION-115 REVISE): three-item cluster surfacing structural absence of epistemic-weight protocol.
  6. **Cross-project escalation cluster** (PRESUMPTION-110 + ASSUMPTION-094 MONITOR-094): bundling without layer verification.
- Cowork-to-chat sync (PRESUMPTION-111) is third recurrence; warrants cluster-level fallback design beyond per-incident manual workaround.

---

## 2026-05-10 cycle REVISE additions (11 new items)

### REVISE-[new]: PRESUMPTION-116
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Cycle-density without normalization is documented across metric-design, bibliometric, SPC, and Goodhart literatures as artifact rather than signal. Per-item normalization (rather than per-cycle) + batch-size and topic-mix disclosure + historical baseline distribution are the canonical remediations. Joint with ASSUMPTION-096 MONITOR-099 — when ASSUMPTION-096 emits density claims, PRESUMPTION-116 remediation requires the disclosure to accompany the claim. Low-cost remediation: add normalization fields to run-summary template.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-117
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge → REVISE. Substrate-coupling at meta-level is weaker bundling justification than literature requires (DORA / Accelerate / AntiPatterns). Implementation-substrate verification (do registration / canonization / fallback share code paths or remediation surface?) is the precondition for sprint commitment. Otherwise small-batch atomic delivery with explicit cross-track coordination is the literature-endorsed alternative. Joint with ASSUMPTION-097 MONITOR-100 — sprint endorsement is contingent on this verification step.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-118
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Treating reversibility as default-low-cost is canonical anti-pattern (Bezos two-way-doors / Nygard / AntiPatterns / Bass-Clements-Kazman). Asymmetric-reversibility analysis is required before canonization; downstream coupling accumulates immediately at canonization. Load-bearing for ASSUMPTION-099 (DECISION-027 scope decision) — without this analysis, scope decision is uninformed. Default heuristic: split is the cheap initial state; merging later is cheaper than splitting later. Run reversibility analysis explicitly before DECISION-027 canonization this week.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-119
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Single-axis collapsing of multi-axis construct ("leverage") without operational definition is canonical Goodhart precondition (Hempel operational definitions; Keeney-Raiffa multi-attribute decision; Goodhart's Law). Operational definition with disclosed attributes + multi-axis ranking + divergence flag are canonical remediations. Joint with ASSUMPTION-100 MONITOR-103 — when superlative leverage rankings are emitted, the operational definition must accompany.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-120
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Policy-free out-of-band scheduling is canonical anti-pattern (selection-effect / OS-scheduling / distributed-systems literatures; CFS / Linux scheduler design). Recurrence of PRESUMPTION-029 multi-subagent batch inflation pattern at adjacent layer (Pattern-Detector deep-pass scheduling). Explicit out-of-band-insertion policy + per-cycle out-of-band budget + outcome-based ranking are canonical remediations. Joint with ASSUMPTION-100 MONITOR-103.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-121
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. **Third instance** in <30 days of "external source treated as primary signal without adjudication" failure mode (PRESUMPTION-074 specialist self-attribution 2026-04-27; PRESUMPTION-115 external-LLM prioritization 2026-05-09; PRESUMPTION-121 external-LLM diagnostic for Chrome MCP 2026-05-10). **Second-layer recurrence in <24h** after PRESUMPTION-115. Recurrence-without-remediation pattern at SYSTEMIC-RISK level. Per ASSUMPTION-098's three-recurrence governance trigger, this cluster meets the canonization threshold this week. DECISION-027 scope extension is now URGENT — cover external-LLM prioritization adoption AND external-LLM diagnostic root-cause attribution as a unified or split decision (per ASSUMPTION-099 / PRESUMPTION-118 reversibility analysis). Cross-LLM divergence test for high-stakes external-LLM uptake. Independent project-context adjudication step inserted before adoption.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-122
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Documentation-as-fix is canonical SRE / human-factors (Reason 1990) / organizational-formalization (Adler-Borys 1996) anti-pattern. Empirical recurrence pattern within C2A2 (cowork-to-chat sync at 4 instances, chat-scrape, Chrome MCP environment) confirms the predicted failure mode. Programmatic enforcement (toil reduction; automated guard) is canonical remediation. Reframe documentation as "interim measure" rather than "fix". Joint with PRESUMPTION-125 (recurrence-counter / severity-ladder absent) and PRESUMPTION-126 (audit-trigger absent) — three items in this batch instantiate the same documentation-as-fix pattern.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-123
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Throughput-as-sole-success-metric is canonical Goodhart instance. Empirical pattern (0% INCORPORATE / 11 MONITOR / 9 REVISE on 2026-05-09; 0% INCORPORATE / 9 MONITOR / 11 REVISE on 2026-05-10 — same pattern across two consecutive cycles) confirms the predicted Goodhart failure mode. Multi-metric design (throughput + INCORPORATE-rate + REVISE-backlog + quality-drift) is canonical remediation. Self-referential signal: this very PRESUMPTION REVISE'd within a cycle that celebrated throughput while INCORPORATE rate stayed at 0%. Joint with ASSUMPTION-102 MONITOR-105.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-124
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Global-from-partial inference for selectively-affected systems is canonical selection bias (Heckman 1979; FMEA; distributed-systems). The wiki-orchestrator-not-in-evidence-frame gap is the structural failure mode. Per-task disaggregation (specifically check wiki-orchestrator status today) + explicit per-task framing + avoid cross-task inference from per-task positive evidence. Joint with ASSUMPTION-103 MONITOR-106 and ASSUMPTION-092 MONITOR-092 master-narrative-gap diagnostic — the per-task evidence about wiki-orchestrator is the missing data point in the regression hypothesis evidence frame.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-125
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. **Fourth recurrence** of cowork-to-chat sync cluster (ASSUMPTION-071 → PRESUMPTION-038 → PRESUMPTION-111 REVISE 2026-05-09 → PRESUMPTION-125 REVISE 2026-05-10). Flat-severity for recurring same-mode failures is canonical ITIL / SRE / ISO 9001 / incident-management anti-pattern. Recurrence-counter + severity-ladder + programmatic escalation are canonical remediations. HIGH urgency: 4-recurrence-without-remediation pattern at the cluster level confirms predicted failure mode of relying on flat disposition. The cowork-to-chat sync cluster is a standalone DECISION candidate — fallback channel design + recurrence-counter implementation. Per ASSUMPTION-098 governance trigger, this cluster meets the three-recurrence threshold (now at 4) for promotion to DECISION-NNN this week.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-126
- **Date flagged:** 2026-05-10
- **Item type:** PRESUMPTION
- **Urgency:** LOW-MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. One-time backfill without audit-trigger is canonical data-quality / database / audit anti-pattern (Wang-Strong 1996; Redman 2008; Date 2003). Empirical evidence (the 6-entry backfill itself was needed) is the predicted failure mode of relying on backfill without ongoing audit. Periodic audit-trigger schedule (weekly?) + completeness check at backfill time + drift-detection alert are canonical remediations. Lower urgency than other 2026-05-10 REVISEs because PROCESSED_LOG is not user-facing and drift is recoverable; still warrants audit-trigger to escape recurring-backfill cycle.
- **Awaiting Tom review.**

---

**2026-05-10 REVISE summary:**
- 11 new REVISE entries: PRESUMPTION-121 (HIGH); PRESUMPTION-125 (HIGH); PRESUMPTION-118, 122, 123 (MEDIUM-HIGH); PRESUMPTION-116, 117, 119, 120, 124 (MEDIUM); PRESUMPTION-126 (LOW-MEDIUM)
- Cluster signals: 8 of 11 REVISEs anchor or extend cluster-level architectural patterns:
  1. **Specialist/external-source primary-signal cluster — second-layer recurrence in <24h** (PRESUMPTION-121): cumulative N=5 across 30 days; SYSTEMIC-RISK HIGH. DECISION-027 scope extension URGENT this week per ASSUMPTION-098 governance trigger.
  2. **Cowork-to-chat sync cluster — fourth recurrence** (PRESUMPTION-125): flat-severity confirmed empirical anti-pattern; recurrence-counter + severity-ladder canonical remediation; standalone DECISION candidate.
  3. **SELF-MEASUREMENT (Goodhart) cluster** (PRESUMPTION-123 + ASSUMPTION-102 MONITOR-105 + ASSUMPTION-096 MONITOR-099): system celebrating throughput while INCORPORATE rate stays at 0% across two consecutive cycles.
  4. **Documentation-as-fix cluster** (PRESUMPTION-122 + PRESUMPTION-125 + PRESUMPTION-126): three items in this batch instantiate the same anti-pattern (documentation without programmatic enforcement / recurrence-counter / audit-trigger).
  5. **Asymmetric-reversibility cluster** (PRESUMPTION-118 + ASSUMPTION-099 MONITOR-102): DECISION-027 scope decision uninformed by reversibility analysis; load-bearing for the URGENT canonization decision this week.
  6. **Operational-definition cluster** (PRESUMPTION-119 + ASSUMPTION-100 MONITOR-103 + PRESUMPTION-116): superlative rankings emitted without operational definition at three layers (leverage; cycle-density; convergence highest-leverage).
  7. **Selection-bias / per-task-vs-cross-task cluster** (PRESUMPTION-124 + ASSUMPTION-103 MONITOR-106 + PRESUMPTION-120): per-task evidence treated as global; out-of-band scheduling without policy.
  8. **Decision-governance circularity** (ASSUMPTION-098 MONITOR-101 + PRESUMPTION-106 REVISE 2026-05-09 unresolved): canonizing-this-week presupposes the canonization criterion that PRESUMPTION-106 was REVISE'd for.
- ASSUMPTION REVISE rate is 0/8 (0%) for the second consecutive cycle — same pattern as 2026-05-09. PRESUMPTION REVISE rate is 11/12 (92%) — at the historical high range, driven by NO-SUPPORT findings on 10 of 12 PRESUMPTIONs.
- INCORPORATE rate remains at 0% for the second consecutive cycle; total REVISE backlog growing (cumulative +11 today after +9 yesterday). The throughput-vs-architectural-progress gap is now the dominant pipeline signal.


## 2026-05-11 CYCLE — 8 new REVISE items

### REVISE-[new]: ASSUMPTION-107
- **Date flagged:** 2026-05-11
- **Item type:** ASSUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Weak-Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** ASSUMPTION + weak support + strong challenge → REVISE. Unnormalized-superlative anti-pattern reaches **THIRD-LAYER recurrence** within 48h (PRESUMPTION-116 REVISE 2026-05-10 → PRESUMPTION-129 REVISE 2026-05-11 → ASSUMPTION-107 REVISE 2026-05-11). The three-layer recurrence within 48 hours satisfies the ASSUMPTION-098 three-recurrence governance threshold for canonization of the anti-pattern as a documented and load-bearing concern. **Significance:** this is the FIRST ASSUMPTION REVISE across two consecutive cycles (2026-05-09 and 2026-05-10 produced 0 ASSUMPTION REVISEs), self-referentially falsifying the "ASSUMPTION REVISE rate 0/8 for SECOND consecutive cycle" claim made by ASSUMPTION-106 (MONITOR-109 this cycle). Per-item normalization + batch-composition disclosure + baseline reference distribution + demote "record" framings are canonical remediations.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-129
- **Date flagged:** 2026-05-11
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. SECOND-LAYER recurrence within 24h of PRESUMPTION-116. The unnormalized-superlative anti-pattern is documented across SPC (Wheeler), bibliometric (Bornmann-Mutz), and Goodhart (Strathern) literatures with converging conclusions; recurrence within 24h across stated/unstated layers indicates the anti-pattern is structural in the C2A2 reporting cadence rather than incidental. With ASSUMPTION-107 (also REVISE this cycle), the cluster reaches three-layer recurrence within 48h, satisfying the ASSUMPTION-098 three-recurrence governance threshold. Canonical remediations: reporting template guards, normalization disclosure, anti-pattern canonization as DECISION, Goodhart-mitigation paired-metric.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-130
- **Date flagged:** 2026-05-11
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + moderate-strong challenge + NO-SUPPORT → REVISE. Agent-defined thresholds adopted as canonical baseline without external validation contradicts converging metric-validity literature (Fenton-Bieman, Boehm, Newman, ISO/IEC 25010). Joint with PRESUMPTION-131 (MONITOR-116 — agent-judgment-without-policy gap) and PRESUMPTION-139 (REVISE — sensitivity-threshold not specified). Document thresholds in policy file + verify alignment with standard graph-theory conventions + external review checkpoint before "canonical" designation + version threshold definitions are canonical remediations. Fix is cheap; absence is the structural concern. Load-bearing for ASSUMPTION-110 (MONITOR-112) sewing-agent baseline canonicalness.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-132
- **Date flagged:** 2026-05-11
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Moderate-Strong)
- **What is at risk / Recommended action:** PRESUMPTION + moderate-strong challenge + NO-SUPPORT → REVISE. Agent-generated cross-tradition synthesis without explicit human review contradicts AI-content-review practice (Bender et al. "Stochastic Parrots"; Buolamwini-Gebru) and intellectual-history methodological commitment (MacIntyre, Bevir). **Directly contradicts PREMISE-014** (INCORPORATEd 2026-04-28: PRS triplets as Tom's authorial re-description); bridge notes generated by sewing agent in synthesis/ folder bypass the author-mediation commitment. Extends PRESUMPTION-024 selection-effect cluster to new agent-generated-bridges layer. Canonical remediations: frame bridge notes as "CANDIDATE" not "valid synthesis", explicit review-trigger before promotion to synthesis/, "DRAFT" or "UNREVIEWED" tag, author-mediation checkpoint per PREMISE-014. **Premise-violation flag.**
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-134
- **Date flagged:** 2026-05-11
- **Item type:** PRESUMPTION
- **Urgency:** HIGH (substrate-decomposition gate for ASSUMPTION-108 + ASSUMPTION-109 URGENT canonization triggers)
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Treating two failure clusters with observable shared substrate (Chrome MCP + claude.ai login state) as having independent failure surfaces is unambiguously contradicted by reliability engineering (Vesely fault-tree), complex-systems analysis (Allspaw-Cook), and root-cause analysis (Toyota Five Whys). The alternation between PRESUMPTION-121 and PRESUMPTION-125 clusters in successive cycles is the textbook signature of common-cause failure being mis-classified as two independent surfaces. **Load-bearing for ASSUMPTION-108 + ASSUMPTION-109 (MONITOR-110 + MONITOR-111)** URGENT canonization triggers — without substrate-decomposition, the recurrence-counter that authorizes those canonizations is itself unreliable. If substrate is shared, the two HIGH-urgency canonizations reduce to one combined DECISION, also easing PRESUMPTION-136 week-carrying-capacity concern. Substrate-decomposition must precede DECISION canonization this week.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-136
- **Date flagged:** 2026-05-11
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Moderate)
- **What is at risk / Recommended action:** PRESUMPTION + moderate challenge + NO-SUPPORT → REVISE. Week-carrying-capacity presumption without consultation contradicts Bryar-Carr (Amazon ADR), Kotter (change management), Goldratt (theory-of-constraints), and PMBOK (resource leveling). Two HIGH-urgency canonizations same day is the canonical overload-anti-pattern signature. The PRESUMPTION-134 substrate-decomposition concern (REVISE same cycle) offers a mitigating path: if substrate is shared, the two canonizations reduce to one combined DECISION, easing the carrying-capacity demand. Canonical remediations: Tom consultation on week-carrying-capacity; substrate-decomposition first; sequential rather than parallel canonization.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-138
- **Date flagged:** 2026-05-11
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Historic-completion-rate extrapolation as substitute for per-task verification of in-flight tasks contradicts SRE (Beyer), monitoring (Allspaw), Bayesian-reasoning (Jaynes), and safety-science (Hollnagel) literatures. **Drift into failure** is the textbook description of historic-extrapolation pattern (Hollnagel). Extends PRESUMPTION-124 (REVISE 2026-05-10 per-task-vs-cross-task evidence-frame cluster) to a new layer (in-flight-tasks). Canonical remediations: per-task verification step; timeout-based alerts; explicit per-task framing in scheduled-task health metric. Three in-flight tasks at evening-sync time presumed to complete overnight without verification means three potential silent failures — the predicted-empirical-failure-mode of historic-extrapolation.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-139
- **Date flagged:** 2026-05-11
- **Item type:** PRESUMPTION
- **Urgency:** LOW-MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Moderate)
- **What is at risk / Recommended action:** PRESUMPTION + moderate challenge + NO-SUPPORT → REVISE. Intervention without sensitivity-threshold specification contradicts metric-design (Fenton-Bieman), statistical-power (Cohen), network-analysis (Newman), and requirements-engineering (Boehm) literatures. "Make sensitive" without minimum-detectable-effect specification is operationally meaningless. Joint with PRESUMPTION-130 (REVISE same cycle) — same agent-judgment-without-validation gap at the threshold-definition layer. Canonical remediations: specify minimum-detectable-effect for "sensitive"; pre/post measurement design with explicit success criterion; document threshold change rationale; paired-validation with PRESUMPTION-130 threshold-definition fix.
- **Awaiting Tom review.**

---

**2026-05-11 REVISE summary:**
- 8 new REVISE entries: PRESUMPTION-134 (HIGH); PRESUMPTION-129, PRESUMPTION-132, PRESUMPTION-138 (MEDIUM-HIGH); ASSUMPTION-107, PRESUMPTION-130, PRESUMPTION-136 (MEDIUM); PRESUMPTION-139 (LOW-MEDIUM)
- **First ASSUMPTION REVISE in three consecutive cycles** (ASSUMPTION-107) — breaks the 0/8 + 0/8 ASSUMPTION REVISE streak that ASSUMPTION-106 (MONITOR-109 this cycle) asserted as a confirmed pattern. Self-referential falsification mid-cycle.
- Cluster signals:
  1. **Unnormalized-superlative anti-pattern reaches three-layer recurrence in 48h** (PRESUMPTION-116 → PRESUMPTION-129 → ASSUMPTION-107): satisfies ASSUMPTION-098 three-recurrence governance threshold for canonization of the anti-pattern as DECISION-NNN candidate. Note: the cluster includes the stated-claim form (ASSUMPTION-107), not just the unstated form — the anti-pattern is now visible to designers as well as inferable.
  2. **Substrate-decomposition gate** (PRESUMPTION-134) — load-bearing for ASSUMPTION-108 (MONITOR-110) and ASSUMPTION-109 (MONITOR-111) URGENT canonization triggers. If substrate is shared, two HIGH-urgency canonizations reduce to one combined DECISION, also resolving PRESUMPTION-136 week-carrying-capacity concern.
  3. **Sewing-agent first-run validation gap cluster** (PRESUMPTION-130 + PRESUMPTION-139 + MONITOR-112 ASSUMPTION-110 + MONITOR-116 PRESUMPTION-131): four-item cluster around threshold definitions, sensitivity-threshold, baseline canonicalness, and agent-judgment-call autonomy. Joint remediation set.
  4. **Premise-violation flag** (PRESUMPTION-132): contradicts PREMISE-014 INCORPORATEd 2026-04-28. First explicit premise-violation in the registry — author-mediation commitment bypassed by sewing-agent bridge generation.
  5. **Per-task-vs-cross-task evidence-frame cluster extends to in-flight-tasks layer** (PRESUMPTION-138 + PRESUMPTION-124 prior REVISE + ASSUMPTION-103 MONITOR-106 prior): three-layer cluster.
- ASSUMPTION REVISE rate is 1/9 (11%) — first non-zero ASSUMPTION REVISE in three consecutive cycles. PRESUMPTION REVISE rate is 7/12 (58%) — markedly lower than 2026-05-10's 92% due to five heuristic-exception MONITORs this cycle. Watch heuristic-exception rate for sustainability.
- **INCORPORATE rate is 1/21 (4.8%) — first non-zero INCORPORATE rate in three consecutive cycles** (2026-05-09 and 2026-05-10 both produced 0 INCORPORATE). ASSUMPTION-105 → PREMISE-015 (user-privacy no-password-delegation constraint). Partial falsification of ASSUMPTION-112 (MONITOR-114) SELF-MEASUREMENT cluster's "0% INCORPORATE confirmation" framing.


## 2026-05-13 CYCLE — 12 new REVISE items

### REVISE-[new]: ASSUMPTION-115
- **Date flagged:** 2026-05-13
- **Item type:** ASSUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** ASSUMPTION + moderate support + strong challenge → REVISE. "Cleanest single-page" is a superlative without comparison set, measurement, or denominator — structurally identical to PRESUMPTION-116 / PRESUMPTION-129 / ASSUMPTION-107 prior REVISEs. The unnormalized-superlative anti-pattern has now produced four REVISEs across stated/unstated forms at rate-comparison and source-comparison layers within 4 days — satisfies ASSUMPTION-098 three-recurrence governance threshold at the cluster level. Canonical remediations: specify comparison set explicitly; operationalize "cleanest" with measurement; specify audience; demote framing to "best identified general-audience compact framing among [list]." Joint with PRESUMPTION-141 (same cycle).
- **Awaiting Tom review.**

---

### REVISE-[new]: ASSUMPTION-116
- **Date flagged:** 2026-05-13
- **Item type:** ASSUMPTION
- **Urgency:** HIGH (joint with PRESUMPTION-142; joins PRESUMPTION-002 CRITICAL + PRESUMPTION-074 SYSTEMIC-RISK clusters)
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** ASSUMPTION + moderate support + strong challenge → REVISE. Reframing Arkani-Hamed/Wolfram/Carroll as pre-foundational without inverse-acceptance check joins the cross-tradition transfer-validity CRITICAL cluster (PRESUMPTION-002) and specialist-recognition SYSTEMIC-RISK cluster (PRESUMPTION-074). Substantive evidence each named program would reject pre-foundational placement on its own foundational commitments (Carroll's poetic-naturalism; Wolfram's framework-completeness; Arkani-Hamed's geometric/structural-realism). Authorizing a Pattern Detector deep-pass on contested philosophical premise inflates the cluster's downstream weight. Canonical remediations: run inverse-acceptance check before deep-pass; solicit specialist (Arkani-Hamed/Wolfram/Carroll) agent reactions; demote "structurally significant" to "structurally proposed pending engagement"; joint cluster remediation with PRESUMPTION-002 + PRESUMPTION-074.
- **Awaiting Tom review.**

---

### REVISE-[new]: ASSUMPTION-117
- **Date flagged:** 2026-05-13
- **Item type:** ASSUMPTION
- **Urgency:** MEDIUM-HIGH (compounds ASSUMPTION-108 first-activation gates at second activation)
- **15a (FOR):** PARTIALLY-SUPPORTED (strength: Moderate)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** ASSUMPTION + moderate support + strong challenge → REVISE. Second activation of ASSUMPTION-098 governance threshold compounds the circular-dependency that gated the first activation (ASSUMPTION-108 MONITOR-110: governance rule itself MONITORed not INCORPORATEd). Substrate-decomposition gate (PRESUMPTION-134 REVISE 2026-05-11, HIGH urgency, unresolved) applies: 5 consecutive skips may be a single common-cause failure misclassified as five. Skip-vs-failure ambiguity unaddressed — PRESUMPTION-138 (REVISE 2026-05-11) flagged the historic-extrapolation anti-pattern for the same registry. Canonical remediations: block second activation until ASSUMPTION-098 is INCORPORATE; substrate-decomposition first; explicit skip-vs-failure rule clarification; reframe "second activation" as "second pending-activation pending governance-rule validation."
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-140
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Empty active watch list framed as positive signal without intake-coverage audit contradicts SRE (Beyer absence-of-alerts), surveillance epidemiology (Mason zero-count disambiguation), and Hollnagel Safety-I/Safety-II distinction. Joins PRESUMPTION-069 silence-not-tracked cluster at the empty-watch-list layer. Canonical remediations: intake-coverage audit on chat-log sample; explicit "empty list = positive OR broken intake" framing; periodic coverage-test schedule; demote framing to "no items surfaced; coverage pending audit."
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-141
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM (third-layer recurrence; cluster-level governance trigger)
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Third-layer recurrence of unnormalized-superlative anti-pattern at source-comparison layer (after rate-comparison recurrences in PRESUMPTION-116, PRESUMPTION-129, ASSUMPTION-107). With ASSUMPTION-115 (same cycle), cluster reaches four-layer breadth in 4 days — extends and confirms the SYSTEMIC-RISK-FLAG raised 2026-05-11. The cluster has now satisfied ASSUMPTION-098 three-recurrence governance threshold at the cluster level twice over. Canonical remediations: reporting-template guards for superlative claims; normalization-disclosure requirement; anti-pattern canonization as DECISION-NNN candidate; Goodhart-mitigation paired-metric.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-142
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** HIGH (today's highest-risk new item; joint with ASSUMPTION-116; joins two prior CRITICAL/SYSTEMIC-RISK clusters)
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. One-way reframing of three first-tier physics TOE programs as pre-foundational to Hoffman without inverse-acceptance check is the exact pattern PRESUMPTION-002 (CRITICAL) was REVISE'd for. Substantive examination of each named program's actual articulations (Carroll Mindscape Ep #91/#135; Wolfram Physics Project framework-completeness; Arkani-Hamed Amplituhedron-derives-spacetime) gives overwhelming prima facie evidence the inverse-acceptance test would fail for all three. MacIntyre cross-tradition methodology requires substantive engagement. Canonical remediations: inverse-acceptance check (assemble strongest case for each program's rejection); specialist-agent (Arkani-Hamed/Wolfram/Carroll) responses solicited before Pattern Detector deep-pass; PRS-CANDIDATE-01 demoted to contested-proposal status; joint cluster remediation with PRESUMPTION-002 + PRESUMPTION-074.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-143
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM (joint with ASSUMPTION-113 + ASSUMPTION-114 single-data-point conjunction)
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Single-data-point maturity claim ("first end-to-end resolution cycle" framing) contradicts SRE production-readiness review (Beyer Ch. 27), SPC pattern-confirmation discipline (Wheeler), Hollnagel drift-into-failure mechanism, and PMBOK operational-readiness criteria. C2A2-internal track record shows first-cycle-success-then-degradation pattern (cowork-to-chat-sync had successful first cycle then degraded into the 6-consecutive-day failure underlying ASSUMPTION-118). Joins PRESUMPTION-040 operational-readiness cluster. Joint with ASSUMPTION-113 (MONITOR-120) and ASSUMPTION-114 (MONITOR-121) single-data-point conjunction — three items together inflate the maturity claim. Canonical remediations: demote framing to "first successful instance pending broader validation"; multi-cycle acceptance criteria; drift-into-failure guards; joint remediation with ASSUMPTION-113 + ASSUMPTION-114.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-144
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM (pre-implementation flag for Vault Linker Agent; empirically falsifiable)
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Closed seven-category taxonomy presumed complete contradicts Hjørland classification theory, Foskett facet-analysis, Hodge KOS digital-library literature, Bowker-Star Sorting Things Out. Brief empirical examination of actual C2A2 vault content reveals at least 5-6 reference types not in the seven-category list (section-anchors, concept-tags, transcript-timestamps, image-embeds, podcast-episode-IDs, footnotes). The presumption is empirically falsifiable on inspection — straightforward test would falsify. Canonical remediations: empirical audit on representative vault sample before implementation; facet/extensible-list design replacing closed enumeration; explicit "other / TBD" residual category; audit cadence post-implementation; align categories with actual vault reference patterns. Pre-implementation flag: fix before Vault Linker Agent is built rather than after.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-145
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH (structural counterpart to ASSUMPTION-118 MONITOR-122; substrate-decomposition gate cluster)
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. First-option bias: chat-scrape sign-in barrier framed as token-delegation problem without explicit redesign-vs-discard-vs-file-handoff comparison contradicts Goldratt theory-of-constraints, Christensen sunk-cost analysis, Bryar-Carr Amazon ADR practice. PREMISE-015 itself preserved alternative paths ("token-based delegation OR equivalent"); narrower-than-premise reading is the structural concern. PRESUMPTION-134 (REVISE 2026-05-11, HIGH, unresolved) substrate-decomposition gate applies — if substrate is shared, local redesign is not root-cause fix. Canonical remediations: explicit redesign-vs-discard-vs-file-handoff comparison with cost estimates; substrate-decomposition first; PREMISE-015 read at full breadth; joint remediation with ASSUMPTION-118 (MONITOR-122) and PRESUMPTION-134 cluster.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-146
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM (third recurrence of on-disk-as-load-bearing-without-trigger pattern)
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Moderate)
- **What is at risk / Recommended action:** PRESUMPTION + moderate challenge + NO-SUPPORT → REVISE. Loughran papers on-disk-without-processing-trigger contradicts Reinertsen flow principles, Poppendieck Lean WIP-without-trigger anti-pattern, and PMBOK completed-vs-in-progress distinction. Third recurrence of on-disk-as-load-bearing-without-trigger pattern (after PRESUMPTION-128 and ASSUMPTION-111). Per-thinker asymmetry is unique structural concern: Wright/Rohr pending proposals are explicitly "blocking" (ASSUMPTION-111 MONITOR-113) while Loughran papers are "not-yet-ingested without urgency" — same on-disk status, different operational treatment. Canonical remediations: explicit ingest trigger for Loughran papers (date, event, or workflow signal); per-thinker policy parity across Wright/Rohr/Loughran; WIP visualization; joint remediation with PRESUMPTION-128 workflow-accommodation cluster.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-147
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** LOW-MEDIUM
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Moderate)
- **What is at risk / Recommended action:** PRESUMPTION + moderate challenge + NO-SUPPORT → REVISE. Three-event narrative segmentation without explicit tier-criteria contradicts Allspaw post-mortem methodology, Boltanski-Thévenot worth-ordering critique, Pentland-Feldman routine-narrative simplification gap, and cognitive-psychology rule-of-three bias (McKee, Aristotle Poetics). Joins PRESUMPTION-036 single-cluster-framing cluster. Without explicit criteria, segmentation is non-reproducible. Canonical remediations: explicit tier-criteria (severity, scope, novelty); full-event-log alongside narrative-summary; reproducibility test; joint remediation with PRESUMPTION-036 cluster.
- **Awaiting Tom review.**

---

### REVISE-[new]: PRESUMPTION-148
- **Date flagged:** 2026-05-13
- **Item type:** PRESUMPTION
- **Urgency:** MEDIUM-HIGH (third-layer SELF-MEASUREMENT Goodhart cluster recurrence; most actionable architectural item this cycle)
- **15a (FOR):** NO-SUPPORT-FOUND (strength: None)
- **15b (AGAINST):** CHALLENGED (strength: Strong)
- **What is at risk / Recommended action:** PRESUMPTION + strong challenge + NO-SUPPORT → REVISE. Proposal-queue +2-today framing as positive throughput contradicts Little's Law (queue arrival must balance with service rate), Reinertsen flow principles (WIP-growth as anti-signal), and Goodhart/Strathern (intake-count as target diverts effort from disposition). Third-layer recurrence of SELF-MEASUREMENT cluster at proposal-pending-count queue (after ASSUMPTION-112 MONITOR-114 cluster anchor, PRESUMPTION-123 REVISE 2026-05-10, PRESUMPTION-129 REVISE 2026-05-11, ASSUMPTION-107 REVISE 2026-05-11). Cluster now reaches multi-layer recurrence across REVISE-rate-as-target, REVISE-rate-as-confirmed, and proposal-queue-depth-as-positive — three distinct queue-and-rate layers within one anti-pattern signature. Canonical remediations: disposition-rate paired metric (proposal-throughput = dispositions/day, not intake/day); ratio-metric (intake:disposition ratio with explicit target); qualitative-veto on intake-celebration without disposition-match; joint cluster remediation with ASSUMPTION-112 + PRESUMPTION-123 + PRESUMPTION-129; multi-metric SLI/SLO design per Beyer SRE.
- **Awaiting Tom review.**

---

**2026-05-13 REVISE summary:**
- 12 new REVISE entries: ASSUMPTION-116 + PRESUMPTION-142 (HIGH — cross-tradition reframing cluster); PRESUMPTION-145 + PRESUMPTION-148 + ASSUMPTION-117 (MEDIUM-HIGH); ASSUMPTION-115 + PRESUMPTION-140 + PRESUMPTION-141 + PRESUMPTION-143 + PRESUMPTION-144 + PRESUMPTION-146 (MEDIUM); PRESUMPTION-147 (LOW-MEDIUM)
- **Three ASSUMPTION REVISEs this cycle** (ASSUMPTION-115, ASSUMPTION-116, ASSUMPTION-117) — second consecutive cycle with non-zero ASSUMPTION REVISE rate (3/6 = 50%), markedly elevated relative to prior 0/8 + 0/8 + 1/9 sequence. PRESUMPTION REVISE rate is 9/10 (90%) — back to the 2026-05-10 high range; heuristic-exception rate fell from 5/12 (42%) to 1/10 (10%) at the PRESUMPTION layer.
- Cluster signals:
  1. **Unnormalized-superlative anti-pattern reaches four-layer breadth across stated/unstated forms within 4 days** (PRESUMPTION-116 → PRESUMPTION-129 → ASSUMPTION-107 → PRESUMPTION-141 + ASSUMPTION-115): extends and confirms the SYSTEMIC-RISK-FLAG raised 2026-05-11. The cluster has now satisfied ASSUMPTION-098 three-recurrence governance threshold at the cluster level twice over (across rate-comparison AND source-comparison layers). DECISION-NNN canonization candidacy strengthens.
  2. **Cross-tradition transfer-validity cluster reaches new TOE-hierarchy layer** (PRESUMPTION-142 + ASSUMPTION-116): joins PRESUMPTION-002 CRITICAL + PRESUMPTION-074 SYSTEMIC-RISK; today's highest-risk new items. Pattern Detector deep-pass routing on contested philosophical premise compounds the cluster's downstream weight.
  3. **SELF-MEASUREMENT Goodhart cluster reaches proposal-queue-depth layer** (PRESUMPTION-148): third-layer recurrence after rate-comparison layers; most actionable architectural item per 14b extraction. Cluster now spans REVISE-rate-as-target + REVISE-rate-as-confirmed + proposal-queue-depth-as-positive.
  4. **Single-data-point conjunction at Agent 16 protocol layer** (ASSUMPTION-113 MONITOR-120 + ASSUMPTION-114 MONITOR-121 + PRESUMPTION-143 REVISE): three-item conjunction inflating the protocol-maturity claim. Method, cadence, and protocol-maturity are independent claims that the conjunction risks conflating.
  5. **Substrate-decomposition gate carries forward unresolved** (PRESUMPTION-134 REVISE 2026-05-11 + new ASSUMPTION-117 REVISE + new ASSUMPTION-118 MONITOR-122 + new PRESUMPTION-145 REVISE): four-item cluster across two cycles. Substrate-decomposition is the load-bearing prerequisite for at least three this-cycle dispositions.
  6. **Closed-taxonomy pre-implementation flag** (PRESUMPTION-144): empirically falsifiable on inspection; pre-implementation rather than post-implementation REVISE — a useful precedent for catching design errors before they ship.
- **INCORPORATE rate is 0/16 (0%) — back to 0% after the 2026-05-11 cycle broke the streak.** ASSUMPTION-112 (MONITOR-114) SELF-MEASUREMENT cluster prediction temporarily restored: this cycle would re-instate the "0% INCORPORATE" pattern that PRESUMPTION-148 (also this cycle, REVISE) flags as the cluster signature. Self-referential signal — the cluster predicts the cycle that produces the prediction's confirmation.

---

## 2026-05-14 REVISE entries (4 items: 2 ASSUMPTION + 2 paired PRESUMPTION)

### REVISE-[new]: ASSUMPTION-126
- **Date flagged:** 2026-05-14
- **Item type:** ASSUMPTION
- **Urgency:** HIGH (joint with PRESUMPTION-159; joins substrate-decomposition cluster carry-forward; ASSUMPTION-118 MONITOR-122 path remains the architectural-layer fix)
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** CHALLENGED (Strong)
- **What is at risk:** Treating credential-layer sign-in restoration as "drought broken" risks foreclosing the architectural-layer fix (ASSUMPTION-118 token-delegation redesign) and treating recurrence as a fresh failure rather than as the expected pattern. Working-channel framing then becomes the operational baseline, and the 7-day drought is effectively rationalized as "fixed." Substrate-decomposition gate (PRESUMPTION-134 REVISE 2026-05-11, unresolved) compounds the risk: if the failure shares substrate with other failure clusters, sign-in restoration is symptomatic, not curative.
- **Recommended action:**
  1. **Demote framing immediately:** "drought broken" → "momentarily restored; durability under observation."
  2. **Multi-day durability test:** track success rate over 14+ days; correlate with sign-in-state events.
  3. **Continue ASSUMPTION-118 path in parallel:** the architectural-layer fix is not preempted by the credential-layer restoration; token-delegation redesign proceeds.
  4. **Prosecute PRESUMPTION-134 substrate-decomposition** (already on REVISE backlog from 2026-05-11): if substrate is shared, credential-layer fix is the wrong layer.
  5. **Root-cause analysis** on the 7-day drought before treating it as resolved: what allowed sign-in state to lapse for 7 consecutive days? What changed at the moment of restoration?
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-159 (paired with ASSUMPTION-126)
- **Date flagged:** 2026-05-14
- **Item type:** PRESUMPTION
- **Urgency:** HIGH (paired with ASSUMPTION-126; same cluster)
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **What is at risk:** Credential-layer-as-architectural-layer-fix confusion is canonical post-incident-analysis anti-pattern (Reason 1990 Swiss-cheese; Allspaw 2010; SRE postmortem culture). If the sign-in fix is framed as durable root-cause, the system loses the operational signal that PRESUMPTION-134 substrate-decomposition is unresolved.
- **Recommended action:** Joint remediation with ASSUMPTION-126: demote framing; multi-day durability test; continue architectural-layer fix path; substrate-decomposition audit.
- **Awaiting Tom review.**

### REVISE-[new]: ASSUMPTION-128
- **Date flagged:** 2026-05-14
- **Item type:** ASSUMPTION
- **Urgency:** HIGH (joins PRESUMPTION-002 + PRESUMPTION-080 + PRESUMPTION-161 transfer-validity cluster — multi-cycle carry-forward)
- **15a (FOR):** PARTIALLY-SUPPORTED (Moderate)
- **15b (AGAINST):** STRONGLY-CHALLENGED (Strong)
- **What is at risk:** "FINDING-030 is first quantitative C2A2 detector" status is over-claimed. Three unaudited transfers underlie the claim: (1) active-inference ↔ OODA is informal analogy in literature (Parr/Pezzulo/Friston 2022 treat it as analogy, not formal homology); (2) traditions-as-probability-distributions is itself a load-bearing assumption that has not been validated; (3) comparable-claim-spaces is the precondition for KL-divergence to be meaningful as a cross-tradition metric, and this precondition has not been established. Without these preconditions, KL-divergence produces numbers but not signal. Treating it as a deployed detector imports unaudited transfers into the system's operational layer.
- **Recommended action:**
  1. **Demote claim:** "first quantitative C2A2 detector" → "candidate quantitative formalization pending transfer-validity audit."
  2. **Prosecute PRESUMPTION-002 / PRESUMPTION-080 / PRESUMPTION-161 transfer-validity cluster:** these have been on the MONITOR/REVISE backlog and are now load-bearing.
  3. **Pilot validation:** Run KL-divergence on known-similar and known-different tradition pairs (e.g., Kuhn vs. Lakatos as known-similar; Aquinas vs. logical positivism as known-different); check whether the metric tracks expert judgment.
  4. **Operationalization audit:** before any further use, document how a "tradition" becomes a probability distribution; over what claim-space; how comparability across claim-spaces is established.
- **Awaiting Tom review.**

### REVISE-[new]: PRESUMPTION-161 (paired with ASSUMPTION-128)
- **Date flagged:** 2026-05-14
- **Item type:** PRESUMPTION
- **Urgency:** HIGH (paired with ASSUMPTION-128; same transfer-validity cluster)
- **15a (FOR):** SUPPORTED (Strong)
- **15b (AGAINST):** NO-CHALLENGE-FOUND (Weak)
- **What is at risk:** Cross-discipline metric transfer without explicit homology audit is canonical scientific-method concern (Cartwright 1999 "The Dappled World"). The PRESUMPTION-002 / PRESUMPTION-080 / PRESUMPTION-161 cluster represents three unresolved transfer-validity audits accumulating in the system. SYSTEMIC-RISK: cross-discipline transfers continue to enter faster than audits close them.
- **Recommended action:** Joint remediation with ASSUMPTION-128. Audit the transfer-validity cluster as a single operational item; PRESUMPTION-002 (Thousand Brains → multi-agent AI) is the load-bearing top of the cluster.
- **Awaiting Tom review.**

---

**2026-05-14 REVISE summary:**
- 4 new REVISE entries: ASSUMPTION-126 + paired PRESUMPTION-159 (HIGH; credential-vs-architectural-layer); ASSUMPTION-128 + paired PRESUMPTION-161 (HIGH; transfer-validity cluster).
- **ASSUMPTION REVISE rate this cycle:** 2/12 (16.7%) — markedly lower than the 2026-05-13 rate (3/6 = 50%). The 17-pathway articulation pass produced fewer REVISEs and more INCORPORATEs than recent operational-incident cycles.
- **PRESUMPTION REVISE rate this cycle:** 2/18 (11.1%) — substantially lower than the 2026-05-13 rate (9/10 = 90%). Most PRESUMPTIONs received MONITOR rather than REVISE because their inferences are supported but the underlying design choices have caveats addressable as monitoring rather than revision.
- **Cluster signals:**
  1. **Substrate-decomposition gate carries forward unresolved into its third cycle** (PRESUMPTION-134 REVISE 2026-05-11; new ASSUMPTION-126 REVISE + PRESUMPTION-159 REVISE + PRESUMPTION-167 MONITOR-144 this cycle). The cluster is now ~5 items across three cycles. Substrate-decomposition is the load-bearing prerequisite for an increasing share of dispositions.
  2. **Transfer-validity cluster extends to KL-divergence layer** (new ASSUMPTION-128 REVISE + PRESUMPTION-161 REVISE; joins PRESUMPTION-002 CRITICAL + PRESUMPTION-080). Cross-discipline transfers continue to accumulate faster than the audit closes them.
- **INCORPORATE rate is 4/30 (13.3%) — first non-zero INCORPORATE cycle since 2026-05-11.** Cycle's INCORPORATE-richness is concentrated in pre-implementation architectural articulation items (broker hosting, library set, sync protocol, honesty layer) — articulation passes produce more INCORPORATE-likely items than operational-incident passes.

---

## 2026-05-15 REVISE additions (Agent 15c)

### REVISE-[new]: PRESUMPTION-177
**Date flagged:** 2026-05-15
**Source item:** PRESUMPTION-177
**Item type:** PRESUMPTION (unstated — surfaced by inference)
**Origin:** 14b (2026-05-14 EOD)
**Provenance chain:** [14b → 15a, 15b → 15c]
**Current status:** REVISION-FLAGGED

**Statement:** Chrome-MCP-offline failure today recurs after only one successful day; degraded-mode protocol treats the recurrence as a credential issue rather than as a recurring architectural failure mode.

**Disposition:** REVISE — joint with PRESUMPTION-159 REVISE (2026-05-14, unresolved) and substrate-decomposition cluster (PRESUMPTION-134 REVISE 2026-05-11, unresolved)

**15a result:** SUPPORTED (Strong) — credential-vs-architectural distinction is canonical post-incident-analysis (Reason 1990 "Human Error"; Allspaw 2009; Beyer et al. 2016 SRE; Hollnagel 2014 Safety-II); PRESUMPTION-159 carry-forward is the same pattern.

**15b result:** NO-CHALLENGE-FOUND (Weak) — counter-patterns exist (some recurrence is genuinely credential-layer; N=2 is below canonical "recurring pattern" threshold) but do not refute the inference, especially given the PRESUMPTION-159 cluster carry-forward making this a second data point.

**Reasoning for REVISE:** PRESUMPTION with strong inference paired with an unresolved REVISE cluster (PRESUMPTION-159, PRESUMPTION-134 substrate-decomposition gate) inherits REVISE per disposition heuristic. The recurrence of Chrome-MCP failure after only one good day is direct evidence of the recurring architectural failure mode that PRESUMPTION-159 named. Framing the recurrence as "Chrome MCP offline" (credential-layer) rather than as "Chrome-MCP-dependency architectural fragility" perpetuates the documented anti-pattern.

**What is at risk:**
- Continued operational drift on Chrome-MCP-dependent pathways (cowork-to-chat delivery; browser-mediated outputs)
- Substrate-decomposition cluster (PRESUMPTION-134 REVISE 2026-05-11, PRESUMPTION-159 REVISE 2026-05-14, PRESUMPTION-167 MONITOR-146, ASSUMPTION-126 REVISE 2026-05-14) — now extending into fourth cycle without closure
- Pathway 14 honesty-layer commitment (PREMISE-019) requires that recurring failures be classified accurately
- Demo-readiness (ISME July 8-10, 2026) — Chrome-MCP-dependent demo paths carry recurrence risk

**Recommended action for Tom's review:**
1. **Resolve substrate-decomposition gate** — the cluster is now in its fourth cycle without closure. The PRESUMPTION-134 audit is the load-bearing item. Sub-steps:
   - Enumerate Chrome-MCP dependency surface (which pathways/agents depend on Chrome-MCP being online)
   - Classify each Chrome-MCP failure in the past 14 days as credential-vs-architectural
   - Identify fall-back paths that don't depend on Chrome-MCP
2. **Reframe operational reporting** — replace "Chrome MCP offline (likely credential)" with "Chrome-MCP-dependent path failed; failure mode pending classification" in degraded-mode protocol output
3. **Bound the credential-vs-architectural distinction** — explicit criteria for when a recurrence becomes architectural (e.g., 2nd recurrence within N days)
4. **Address Pathway 14 implication** — the honesty-layer commitment requires accurate failure classification; recurrence-as-credential framing without evidence violates the commitment

**Urgency:** HIGH (joint with PRESUMPTION-159; substrate-decomposition cluster fourth-cycle carry-forward; ISME demo-readiness load-bearing)

**Awaiting Tom review.**

---

**2026-05-15 REVISE summary:**
- 1 new REVISE entry: PRESUMPTION-177 (HIGH; recurring-failure-as-credential; joint with PRESUMPTION-159 REVISE 2026-05-14 carry-forward and PRESUMPTION-134 substrate-decomposition REVISE 2026-05-11 carry-forward).
- **ASSUMPTION REVISE rate this cycle:** 0/14 (0%) — no new ASSUMPTION REVISEs. ASSUMPTION-140 (sign-in fix holding) was a candidate but the framing concern lives in PRESUMPTION-177 paired; ASSUMPTION-140 received MONITOR with cluster-membership noted.
- **PRESUMPTION REVISE rate this cycle:** 1/15 (6.7%) — substantially lower than the 2026-05-14 rate (2/18 = 11.1%) and the 2026-05-13 rate (9/10 = 90%). The breadth-arc 18-25 pass surfaced more presumptions about commitments-in-design than about operational failures, producing more MONITORs than REVISEs.
- **Cluster signals:**
  1. **Substrate-decomposition gate enters its fourth consecutive cycle without closure** (PRESUMPTION-134 REVISE 2026-05-11; PRESUMPTION-159 REVISE 2026-05-14; new PRESUMPTION-177 REVISE this cycle). The cluster now spans four cycles with at least one new entry per cycle. This is the strongest unresolved-cluster signal in the system.
  2. **CRITICAL transfer-validity cluster extends to federation wire-format** (new ASSUMPTION-133 MONITOR-148 + new PRESUMPTION-170 MONITOR-160; joins PRESUMPTION-002 + PRESUMPTION-080 + PRESUMPTION-161 + ASSUMPTION-128 prior). Cluster has been open since 2026-04-13 without closure.
  3. **Writing-pass-as-claim-making cluster grew this cycle** — four new MONITOR items (155, 165, 166, 171) form a new cluster joint with PRESUMPTION-166 carry-forward.
  4. **Recursive-self-application cluster** — PRESUMPTION-180 multi-pathway recursive load (MONITOR-169 HIGH) extends a prior cluster (PRESUMPTION-165, PRESUMPTION-148) — recursive load growing.
- **INCORPORATE rate is 3/29 (10.3%) — second consecutive non-zero INCORPORATE cycle.** Combined 2026-05-14 + 2026-05-15 INCORPORATE rate is 7/59 (11.9%), strongly above the prior baseline. Both cycles were driven by architectural-articulation passes; the pattern is now confirmed across two cycles.



---

## 2026-05-18 cycle additions (2 REVISE items)

Both REVISE items in this cycle (PRESUMPTION-187, PRESUMPTION-188) extend the CRITICAL substrate-decomposition cluster (now N=5+ unresolved instances). Both flag the pre-classification anti-pattern recurring at new layers (pipeline-failure-vs-rate-mismatch; cadence-fix-vs-unbuilt-component). Cluster-level remediation is overdue.

---

### REVISE-[new]: PRESUMPTION-187
**Date flagged:** 2026-05-18
**Source item:** PRESUMPTION-187
**Item type:** PRESUMPTION (unstated — surfaced by inference)
**Origin:** 14b (2026-05-17 EOD)
**Provenance chain:** [14b → 15a, 15b → 15c]
**Current status:** REVISION-FLAGGED

**Statement:** '14a/14b ingestion pipeline visibly stalled' framing presumes pipeline-failure (scheduler/credential/environment) rather than rate-mismatch (Chat-side production exceeds daily ingestion capacity); pipeline-failure framing operationally simpler, chosen by default.

**Disposition:** REVISE — joins CRITICAL substrate-decomposition cluster (PRESUMPTION-134 REVISE 2026-05-11 unresolved; PRESUMPTION-159 REVISE 2026-05-14 unresolved; PRESUMPTION-177 REVISE 2026-05-15 unresolved)

**15a result:** NO-SUPPORT-FOUND (None)

**15b result:** STRONGLY-CHALLENGED (Strong) — Defaulting to pipeline-failure framing without classification is the exact pattern the substrate-decomposition cluster catches. The literature on incident analysis (Reason; Hollnagel) treats pre-classification as a known mode of failure-attribution error. The presumption joins a cluster now at N=4+ instances; pattern strength is strong.

**Reasoning for REVISE:** PRESUMPTION + Strong challenge + cluster-membership in CRITICAL substrate-decomposition cluster (now N=4+). Per 15c heuristic: PRESUMPTION with strong challenge → lean REVISE with HIGH urgency. The cluster pattern is itself the systemic risk; this instance is one more data point that the pre-classification anti-pattern is recurring.

**What is at risk:** (a) OPEN-047 (pipeline reliability audit) may fix the wrong layer; (b) the substrate-decomposition cluster pattern continues; (c) Pathway-14 honesty-layer commitment (PREMISE-019) requires accurate cause classification.

**Recommended action for Tom's review:** 1. Diagnose the missed cycles before fixing: confirm scheduler fired vs. didn't; confirm 14a/14b ran vs. didn't; confirm input rate. 2. Cluster-level: establish pre-classification protocol that treats rate-mismatch as a peer candidate to pipeline-failure for all missed-cycle reports. 3. Tom's review of substrate-decomposition cluster as a whole (now N=4+ instances; not closing).

**Urgency:** HIGH

---

### REVISE-[new]: PRESUMPTION-188
**Date flagged:** 2026-05-18
**Source item:** PRESUMPTION-188
**Item type:** PRESUMPTION (unstated — surfaced by inference)
**Origin:** 14b (2026-05-17 EOD)
**Provenance chain:** [14b → 15a, 15b → 15c]
**Current status:** REVISION-FLAGGED

**Statement:** 'Verify 15d cadence' framing presumes c2a2-15d-monitor exists; lit-search note same day says 'no scheduled-task evidence visible'; cadence-fix-vs-unbuilt-component is the same pre-classification pattern.

**Disposition:** REVISE — joins CRITICAL substrate-decomposition cluster (PRESUMPTION-134 REVISE 2026-05-11 unresolved; PRESUMPTION-159 REVISE 2026-05-14 unresolved; PRESUMPTION-177 REVISE 2026-05-15 unresolved)

**15a result:** NO-SUPPORT-FOUND (None)

**15b result:** STRONGLY-CHALLENGED (Strong) — Verifying cadence on an unbuilt component is the exact substrate-decomposition anti-pattern. The same-day evidence already shows the component is not visible; the framing persists despite contradicting evidence. Cluster N=4+ now joined by N=5.

**Reasoning for REVISE:** PRESUMPTION + Strong challenge + cluster-membership + same-day contradicting evidence already on disk. Per 15c heuristic: PRESUMPTION with strong challenge → REVISE with HIGH urgency. This is the most clearly-falsifiable instance of the cluster pattern.

**What is at risk:** (a) OPEN-046 + OPEN-047 may both be working on framing-questions about a component that doesn't exist; (b) cluster-level pattern recurrence.

**Recommended action for Tom's review:** 1. Verify c2a2-15d-monitor scheduled task existence (5-minute audit). 2. If not built: build it (or document the decision not to build it as an architectural commitment). 3. Cluster-level: existence-before-property protocol for all subsequent component-audit invocations.

**Urgency:** HIGH

---

**2026-05-18 cycle additions to revision_flags:**

2 new REVISE items (PRESUMPTION-187, PRESUMPTION-188), both joining the CRITICAL substrate-decomposition cluster. The cluster is now at N=5+ unresolved instances; cluster-level remediation (pre-classification-protocol commitment) is overdue and should be elevated.

---

### REVISE-020:
**Date flagged:** 2026-05-19
**Source item:** ASSUMPTION-172
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:** "Clofilium-CRC + Friston-precision-psychiatry as cross-tradition paradigm-shift-candidate cluster (precision-failure framing converges across bioelectric and neuromodulatory scales)."

**What is at risk:**
- DECISION-013 (cross-tradition bridge promotion)
- Pattern Detector input quality
- Over-claiming paradigm-shift status on vocabulary-convergence basis only

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Moderate-strong; precision-weighting framings are real in both literatures); 15b found CHALLENGED (Strong; vocabulary-convergence ≠ structural-homology per Galison's "trading zone" critique; the two scales involve substantively different physical substrates).

**Recommended action:** Downgrade "paradigm-shift cluster" framing to "framing-convergence-monitor"; require receiving-specialist (FEP, bioelectric) confirmation before promoting beyond hypothesis. Couples to PRESUMPTION-198/REVISE-023.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-021:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-196
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "pending/-scan as output-ground-truth presumption; orchestrator treats absence-in-scan as evidence-of-absence-in-output without bounding scan-coverage or run-ordering."

**What is at risk:**
- All multi-agent state-visibility decisions in C2A2
- OPEN-049 cascade
- Downstream Pattern Detector input integrity

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Weak; scan-as-truth acceptable as fallback only); 15b found CHALLENGED (Strong; textbook anti-pattern per distributed-systems literature — Helland, Kleppmann; event-sourcing and write-ahead-log patterns established as standard).

**Recommended action:** Introduce write-receipt/manifest protocol as primary ground-truth layer; deprecate scan-as-truth pattern across all orchestrator/specialist/sewing-agent interactions. Couples to PRESUMPTION-204/REVISE-030 (symmetric error) and PREMISE-031 (ASSUMPTION-178 descriptive validation).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-022:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-197
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "agent-significance-judgment-as-bounded presumption; out-of-window exception filter grants unbounded inclusion discretion when agent can articulate cross-tradition signals."

**What is at risk:**
- Curation drift
- Out-of-window inclusion rate unbounded
- Carpathi-instance-validator cluster

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Weak; articulation as a sanity-check is supported); 15b found CHALLENGED (Strong; articulation ≠ calibration per agent-evaluation literature; need ground-truth comparator).

**Recommended action:** Add Tom-acceptance gate for out-of-window inclusions; cap exception rate at empirically-derived threshold; couple to PRESUMPTION-182 (Carpathi cluster).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-023:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-198
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "specialist-as-bridge-detector presumption; PROP-003 cross-tradition bridge claims to 5+ traditions are sole-source from Levin/Friston specialist without confirmation from receiving-tradition specialists."

**What is at risk:**
- Pattern Detector input integrity
- Over-claimed cross-tradition bridges that propagate into downstream paradigm-shift candidates

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Weak; specialist as detection layer is fine); 15b found CHALLENGED (Strong; sole-source bridge claims are hypotheses, not findings, per STS replication literature — Collins; Latour on closure).

**Recommended action:** Mandatory cross-specialist confirmation step before bridge claim is published; mark sole-source bridges as "proposed pending cross-specialist confirmation" at agent write-time. Couples to PRESUMPTION-207/REVISE-032 (sewing-agent variant).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-024:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-199
**Item type:** PRESUMPTION
**Urgency:** CRITICAL

**Statement:** "uncommitted-state-is-safe-indefinitely presumption; 476-uncommittable-change accumulation tolerated without explicit checkpoint discipline."

**What is at risk:**
- Catastrophic data loss from one disk corruption or accidental rm event
- Loss of 476 uncommitted edits including Phase-6 work

**Evidence summary:** 15a found NO-SUPPORT-FOUND (no literature defends extended-uncommitted state as safe); 15b found CHALLENGED (Strong; SRE/DevOps literature — Beyer et al., Forsgren et al. "Accelerate" — well-attested loss modes from extended uncommitted state).

**Recommended action:** URGENT — adopt structured intermediate-commit protocol to bound uncommitted state at e.g. N<50; constitutional "no blind push" rule needs amendment to permit checkpoint commits that are not pushes; visual-review-of-N decomposition per Cohen (couples to PREMISE-029).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-025:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-200
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "cycle-count-as-staleness-proxy presumption; 15d's cycle-3-stale-watch / cycle-4-escalation thresholds presume regular weekly cadence, decoupled from wall-clock-time staleness during irregular firing."

**What is at risk:**
- Escalation discipline silently under-reports during cadence gaps
- Normalized deviance from stale-watch protocol

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Weak; cycle-count proxy valid when cadence holds); 15b found CHALLENGED (Strong; documented failure mode when cadence is irregular — SRE escalation-threshold design literature).

**Recommended action:** Add wall-clock-days as secondary staleness measure; escalate on whichever crosses threshold first. Couples to PRESUMPTION-188.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-026:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-201
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** "morning-briefing-write-as-success vs Tom-action-as-success presumption; briefing-write counter is measured, action-rate is not, gap is invisible."

**What is at risk:**
- Goodhart SELF-MEASUREMENT cluster compounds
- System appears productive while drifting from purpose
- Briefing optimization without outcome accountability

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Weak; briefing-write as interim metric defensible only as bootstrap); 15b found CHALLENGED (Strong; textbook Goodhart — Strathern, Muller "Tyranny of Metrics"; agent-self-measurement antipatterns).

**Recommended action:** Add Tom-action-rate as outcome metric; pair every briefing-write count with downstream action-completion count; remove briefing-write as standalone success signal. Couples to PRESUMPTION-148/165/180/193 (SELF-MEASUREMENT cluster).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-027:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-202
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "queue-depth-as-review-urgency presumption; 42-pending framing recommends Tom-reviews-more (throughput-side intervention) without decomposing into generation-rate vs throughput-capacity."

**What is at risk:**
- Reviewer surge prescription treats Tom as elastic
- Underlying mismatch (generation > service rate) goes unaddressed

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Weak; depth as signal valid); 15b found CHALLENGED (Strong; queue theory — Kingman's formula, Little's law; depth signals investigation of arrival vs service rate, not throughput-side intervention).

**Recommended action:** Decompose queue depth into arrival rate and service rate; if arrival > service, the fix is upstream (slower generation or higher reviewer capacity), not "more Tom-reviewing." Couples to ASSUMPTION-175/MONITOR-192, PRESUMPTION-186.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-028:
**Date flagged:** 2026-05-19
**Source item:** ASSUMPTION-182
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:** "Three new substantive cross-tradition bridge notes written to synthesis/ by sewing-agent — Friston×Levin (precision-weighting substrate-agnostic FEP), McGilchrist×Rohr (hemispheric-operationalization), Wright×Rohr (ruach×Universal-Christ + cruciform-suffering)."

**What is at risk:**
- Pattern Detector input quality
- Bridges promoted to synthesis/ without ratification
- Wright×Rohr conflates pneumatology with cosmic Christology per theological literature

**Evidence summary:** 15a found SUPPORTED (Strong/Moderate/Moderate per bridge); 15b found PARTIALLY-CHALLENGED (Moderate; substrate-agnostic FEP has documented limits; alternate hemispheric models exist; pneumatology-vs-Christology mapping disputes are real).

**Recommended action:** Mark all three bridges as "proposed pending cross-specialist confirmation"; require receiving-tradition specialist sign-off before synthesis/ promotion. Wright×Rohr specifically needs theological-specialist disambiguation. Couples to PRESUMPTION-207/REVISE-032.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-029:
**Date flagged:** 2026-05-19
**Source item:** ASSUMPTION-183
**Item type:** ASSUMPTION
**Urgency:** MEDIUM

**Statement:** "FC26 abstract Revision-2 closed as submission-ready; corpus horizon stated as 'Day 100 of 308, full commentary by July 2026.'"

**What is at risk:**
- Planning-fallacy exposure on 308-day single-author commitment
- Today's 2-cycle cadence gap silently strains the commitment without surfacing the strain

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Moderate; submission-ready closure protocols sound); 15b found PARTIALLY-CHALLENGED (Moderate; long-horizon single-author commitments without slack budget systematically miss per planning-fallacy literature).

**Recommended action:** Add slack/re-review trigger (couples to PRESUMPTION-208/PREMISE-036's Day-150 checkpoint); rephrase commitment with conditional ("contingent on cadence X holding"). The submission-ready closure itself is sound; the corpus-horizon framing needs softening.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-030:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-204
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "Sewing-agent's pending/-scan-as-ground-truth — inverts morning's PRESUMPTION-196 (orchestrator-as-ground-truth) without auditing whether the two scans use identical path/filter/timing coverage."

**What is at risk:**
- Symmetric error to PRESUMPTION-196
- Ground-truth role oscillates agent-to-agent within a single day
- Every downstream agent inherits the latest oscillation

**Evidence summary:** 15a found SUPPORTED (Strong; this is a real inversion that the system has documented); 15b found NO-CHALLENGE-FOUND (no literature defends scan-as-truth replacement by another scan-as-truth).

**Recommended action:** Same as REVISE-021 — introduce write-receipt manifest layer; deprecate ANY scan-as-truth pattern regardless of which agent does the scanning. Core systemic fix.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-031:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-206
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "Inter-model disagreement (Opus + Claude) as useful signal — presumes independent observations rather than correlated noise from shared training/RLHF lineage."

**What is at risk:**
- Over-weighting concurrence as confirmation when intra-family models share training data and RLHF preferences
- Correlated-noise problem in ensembling literature

**Evidence summary:** 15a found SUPPORTED (Strong; inter-model agreement IS a signal); 15b found PARTIALLY-CHALLENGED (Moderate; Dietterich on ensemble independence; Lakshminarayanan on deep ensembles; recent LLM-ensembling literature documenting correlated errors within model family).

**Recommended action:** Discount intra-family agreement weight; when invoking inter-model concurrence as signal, name the independence level explicitly (e.g., "Opus + Sonnet concurrence at intra-family level only"); reserve high-weight concurrence claims for cross-family pairs.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

### REVISE-032:
**Date flagged:** 2026-05-19
**Source item:** PRESUMPTION-207
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "Sewing-agent-as-bridge-ratification-authority — extends PRESUMPTION-198's sole-source-bridge-detector pattern to a second agent class without re-asking the cross-specialist confirmation question; creates circular-signal risk into Pattern Detector."

**What is at risk:**
- Closed-loop ratification spreads from specialist agents to sewing-agent class
- Pattern Detector input integrity doubles in risk surface
- Any new agent class would inherit the pattern by default

**Evidence summary:** 15a found SUPPORTED (Strong; this is the documented extension); 15b found NO-CHALLENGE-FOUND (no literature defends agent-class-extension of detection-equals-ratification pathology).

**Recommended action:** Mandatory "proposed pending cross-specialist confirmation" provenance label at agent write-time for ALL bridge claims regardless of source agent class; explicit ratification-vs-detection boundary in architecture-decision-record form. Couples to PRESUMPTION-198/REVISE-023, ASSUMPTION-182/REVISE-028.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

**2026-05-19 cycle additions to revision_flags:**

Total REVISEs: 32 (19 prior + 13 new — REVISE-020 through REVISE-032).

REVISE rate this cycle (excluding cycle-1 refreshes): 13/28 = 46% (notably high; dominated by PRESUMPTION-side clusters surfaced today).

HIGH/CRITICAL urgency: REVISE-024 (CRITICAL — PRESUMPTION-199 VCS hygiene); REVISE-020 (HIGH — ASSUMPTION-172 paradigm-shift overclaim); REVISE-021 (HIGH — PRESUMPTION-196 scan-as-truth); REVISE-023 (HIGH — PRESUMPTION-198 sole-source bridges); REVISE-028 (HIGH — ASSUMPTION-182 unratified bridges); REVISE-030 (HIGH — PRESUMPTION-204 scan-as-truth inversion); REVISE-032 (HIGH — PRESUMPTION-207 closed-loop ratification spread). REVISE-026 MEDIUM-HIGH (PRESUMPTION-201 Goodhart).

Cluster identification:
- Ground-truth oscillation cluster: REVISE-021 + REVISE-030 (both polarities of scan-as-truth)
- Closed-loop ratification cluster: REVISE-023 + REVISE-028 + REVISE-032 (spreading across agent classes)
- Goodhart SELF-MEASUREMENT cluster: REVISE-026 + REVISE-027 (joins prior PRESUMPTION-148/165/180/193 cluster)
- VCS hygiene cluster: REVISE-024 (couples to PREMISE-029 visual-review-decomposition)

All REVISEs status AWAITING-REVIEW per protocol — require Tom's response before status changes.

---


**2026-05-20 cycle additions to revision_flags (REVISE-033..041):**

### REVISE-033:
**Date flagged:** 2026-05-20
**Source item:** ASSUMPTION-189
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:** "Recurring index.lock + 716/356 morass caused by colliding/silently-failing scheduled commit agents."

**What is at risk:** The 21:00 sync run, all scheduled commit agents, vault durability; recurrence corrupts staging state (716/356 morass).

**Evidence summary:** 15a found SUPPORTED (Strong); 15b found PARTIALLY-CHALLENGED (Moderate). 15a SUPPORTED (Strong; collision is a real, common mechanism); 15b PARTIALLY-CHALLENGED (Moderate; credible alternative causes share the symptom and it is under-instrumented). Both directions converge on the same remediation: serialize + instrument.

**Recommended action:** Serialize every scheduled git operation behind a single exclusive lock (flock); add per-agent commit + lock-acquire/release logging; add a guarded stale-lock clear on startup; re-evaluate after one week of logged runs. Couples ASSUMPTION-188, ASSUMPTION-190, PRESUMPTION-211 (REVISE-038), PRESUMPTION-216.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---
### REVISE-034:
**Date flagged:** 2026-05-20
**Source item:** ASSUMPTION-198
**Item type:** ASSUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** "32 fabricated transcripts to re-fetch before July 8 (transcript-only; commentaries sound)."

**What is at risk:** Pathway-14 honesty layer; the July-8 publicize gate; corpus integrity if contaminated commentaries pass as sound.

**Evidence summary:** 15a found SUPPORTED (Strong); 15b found PARTIALLY-CHALLENGED (Moderate-Strong). 15a SUPPORTED (Strong; re-fetch is the right repair); 15b PARTIALLY-CHALLENGED (Moderate-Strong; the 'commentaries sound' scope is unverified and contamination propagates to derived artifacts). The action item (re-fetch) is sound but the contamination-scope assumption needs revision before the gate.

**Recommended action:** Before July 8: (1) proceed with the 32-transcript re-fetch; (2) for each fabricated transcript, enumerate commentaries derived from it and re-verify them against the re-fetched source; (3) replace the blanket 'commentaries sound' assumption with a per-commentary provenance check. Couples Pathway-14, ASSUMPTION-199 (citation provenance).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---
### REVISE-035:
**Date flagged:** 2026-05-20
**Source item:** ASSUMPTION-199
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:** "Lit-pipeline cycle-1 carry-forward (no net-new search, low yield) + training-corpus citation convention."

**What is at risk:** All 15a/15b grounding quality; the validated_premises register; couples PRESUMPTION-214 (MONITOR-205) and PRESUMPTION-215 (REVISE-040); symmetric to ASSUMPTION-198 fabrication concern.

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Moderate); 15b found CHALLENGED (Strong). 15a PARTIALLY-SUPPORTED (Moderate; defensible for low-velocity/well-attested topics); 15b CHALLENGED (Strong; fails for fast-moving/long-tail, raises fabricated-citation risk, self-referential to the pipeline's own method). The asymmetry favors revision.

**Recommended action:** Stratify refresh by field velocity (live search for fast-moving/recency-dependent items; carry-forward only for low-velocity well-attested ones); label every citation as training-corpus or live-verified; schedule a periodic live-literature audit of a carry-forward sample to empirically test the low-yield assumption. SYSTEMIC-RISK-FLAG E (epistemic-grounding method).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---
### REVISE-036:
**Date flagged:** 2026-05-20
**Source item:** PRESUMPTION-209
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** "A single agent's directory scan is authoritative — no reconciliation layer across counting agents."

**What is at risk:** Conservation-gate decisions, Pattern Detector input integrity, OPEN-055; all count-driven control logic.

**Evidence summary:** 15a found NO-SUPPORT-FOUND (Weak); 15b found CHALLENGED (Strong). 15a NO-SUPPORT-FOUND (Weak; single-source-of-truth actually argues for reconciliation); 15b CHALLENGED (Strong; CAP/consensus/read-repair + observed split-brain discrepancies). Clear asymmetry against the presumption.

**Recommended action:** Introduce a reconciliation layer as source of truth: write-receipt manifest, inter-agent count agreement, and alarms on disagreement; treat any single scan as a proposal pending reconciliation. Couples PRESUMPTION-196/REVISE-021, PRESUMPTION-204/REVISE-030, ASSUMPTION-186, OPEN-055. SYSTEMIC-RISK-FLAG A.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---
### REVISE-037:
**Date flagged:** 2026-05-20
**Source item:** PRESUMPTION-210
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** "Raw queue depth is a valid proxy for 'generate more?' — no decomposition before throttling."

**What is at risk:** Generation throttling logic; conservation gate; OPEN-055; compounds ASSUMPTION-186 and PRESUMPTION-202.

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Weak); 15b found CHALLENGED (Strong). 15a PARTIALLY-SUPPORTED (Weak; signaling half only); 15b CHALLENGED (Strong; decomposition required by all flow/TOC literature). Strong asymmetry; mirrors the already-REVISEd PRESUMPTION-202.

**Recommended action:** Decompose queue depth into generation-rate and throughput-rate components per cycle; key the generate-more decision off the rate gap, not raw depth; report all three. Couples PRESUMPTION-202, ASSUMPTION-186, OPEN-055.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---
### REVISE-038:
**Date flagged:** 2026-05-20
**Source item:** PRESUMPTION-211
**Item type:** PRESUMPTION
**Urgency:** CRITICAL

**Statement:** "File-on-disk == durably persisted — commit responsibility is unowned."

**What is at risk:** All generated vault/PRS/artifact content; OPEN-056; the entire commit/persistence pipeline; couples ASSUMPTION-188/189/190, REVISE-033.

**Evidence summary:** 15a found NO-SUPPORT-FOUND (Weak); 15b found CHALLENGED (Strong). 15a NO-SUPPORT-FOUND (Weak); 15b CHALLENGED (Strong, CRITICAL; ACID-D, git semantics, fsync research, ownership). Maximal asymmetry against the presumption.

**Recommended action:** Assign explicit, single, serialized commit ownership; redefine durability as committed+pushed (not on-disk); emit write-receipts only post-commit; alarm on uncommitted-content age; treat the working tree as staged-not-durable everywhere. Couples REVISE-033 (serialization), PRESUMPTION-199/REVISE-024, OPEN-056. SYSTEMIC-RISK-FLAG D (CRITICAL).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---
### REVISE-039:
**Date flagged:** 2026-05-20
**Source item:** PRESUMPTION-212
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "The documented number == the true number — registers presumed consistent and current."

**What is at risk:** All register-driven decisions; Pattern Detector input quality; couples ASSUMPTION-192/193, PREMISE-040, OPEN-055.

**Evidence summary:** 15a found NO-SUPPORT-FOUND (Weak); 15b found CHALLENGED (Strong). 15a NO-SUPPORT-FOUND (Weak; ideal supports enforcement not assumption); 15b CHALLENGED (Strong; software-aging + two same-cycle realized instances). Asymmetry against the presumption, with in-system proof.

**Recommended action:** Auto-derive documented figures from their artifacts; add register-vs-artifact reconciliation/divergence checks (CI or scheduled); treat documented numbers as claims requiring validation; alarm on divergence. Couples PREMISE-040 (auto-derive stats), ASSUMPTION-193 (MONITOR-199), PRESUMPTION-209. SYSTEMIC-RISK-FLAG A.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---
### REVISE-040:
**Date flagged:** 2026-05-20
**Source item:** PRESUMPTION-215
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** "Training-corpus is an adequate stand-in for live literature when grounding premises."

**What is at risk:** The entire 15a/15b grounding layer and validated_premises register; epistemic credibility of the self-awareness pipeline; couples ASSUMPTION-198 (fabrication), ASSUMPTION-199, PRESUMPTION-214.

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Moderate); 15b found CHALLENGED (Strong). 15a PARTIALLY-SUPPORTED (Moderate; adequate for well-attested facts); 15b CHALLENGED (Strong; long-tail/recency failure + fabrication risk; self-applying to this run). Asymmetry favors revision with a scoping carve-out.

**Recommended action:** Label every citation's provenance (training-corpus vs live-verified); require live literature search for recency-dependent or long-tail premises; live-verify a sample of high-stakes citations; reserve training-corpus grounding for well-attested foundations. SYSTEMIC-RISK-FLAG E (epistemic-grounding method). Note: applies to this run's own citations.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---
### REVISE-041:
**Date flagged:** 2026-05-20
**Source item:** PRESUMPTION-220
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** "On-cadence firing == healthy pipeline — no input/output-validity check paired to cadence."

**What is at risk:** Pipeline-health reporting; the self-measurement layer; ASSUMPTION-117/200 (cadence claims); couples PRESUMPTION-201, FLAG C.

**Evidence summary:** 15a found PARTIALLY-SUPPORTED (Weak); 15b found CHALLENGED (Strong). 15a PARTIALLY-SUPPORTED (Weak; liveness only); 15b CHALLENGED (Strong; Goodhart, liveness-vs-safety, with same-cycle proof that cadence-green coincided with validity-red). Strong asymmetry, in-system demonstrated.

**Recommended action:** Pair cadence-liveness with input/output-validity checks (schema/sanity/coverage on 14a/14b/15x outputs); report error/quality signals alongside liveness; treat on-cadence firing as necessary-but-not-sufficient for health. Couples PRESUMPTION-201/REVISE-026 (Goodhart cluster), ASSUMPTION-117/200. SYSTEMIC-RISK-FLAG C.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b → 15a, 15b → 15c]; Current status: REVISION-FLAGGED

---

Total new REVISEs this run: 9 (REVISE-033 through REVISE-041). CRITICAL: REVISE-038 (PRESUMPTION-211). HIGH: REVISE-033, REVISE-035, REVISE-036. All status AWAITING-REVIEW per protocol (require Tom's response before status changes).

Clusters: FLAG A ground-truth oscillation (REVISE-036, REVISE-039); FLAG D VCS/persistence (REVISE-033, REVISE-038 CRITICAL); FLAG E epistemic-grounding NEW (REVISE-035, REVISE-040); FLAG C Goodhart (REVISE-041); queue-decomposition (REVISE-037 + prior PRESUMPTION-202); corpus-integrity (REVISE-034).

---

### REVISE-042:
**Date flagged:** 2026-05-21
**Source item:** ASSUMPTION-208
**Item type:** ASSUMPTION
**Urgency:** MEDIUM

**Statement:** Progress = better compression; a forming master science shows as total description length falling while coverage rises.

**What is at risk:** The entire progress-measurement layer and any decision tying 'compression' to 'progress'; the proposed headline metric. Gated by PRESUMPTION-222 (REVISE-044).

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Moderate; real compression-as-progress lineage). 15b CHALLENGED (Strong; ill-defined/uncomputable total description length, paradigm-incommensurability, gameability, plus counterexamples where progress adds machinery). Asymmetry against, on a high-stakes headline metric resting on an unvalidated presumption.

**Recommended action:** Do NOT adopt description-length as THE progress metric. Demote to a single explicitly-labeled, computable proxy (LM cross-entropy codelength or MDL graph summarization) used as one indicator, paired with a coverage/fidelity guard; validate the proxy against independently-judged progress before any headline use. Resolve PRESUMPTION-222 first.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-043:
**Date flagged:** 2026-05-21
**Source item:** PRESUMPTION-221
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** The connectome is the right master-metaphor — neural/Hawkins structure presumed to transfer to narratives without a transfer-condition check.

**What is at risk:** The whole connectome metric suite: ASSUMPTION-201 (connectome framing), ASSUMPTION-202 (association-fiber/integration), PRESUMPTION-229 (metrics at scale). The analogy is load-bearing and unchecked.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Moderate; generic network metaphor only). 15b CHALLENGED (Strong; brain-specific measures presuppose physical constraints narratives lack, connectome metrics are null-model-fragile, and no transfer check exists). Designer-unaware presumption load-bearing for the whole metric suite.

**Recommended action:** Before any connectome metric informs a decision, run a one-time transfer-condition audit: for each metric, state the brain-specific assumption it relies on (wiring economy, developmental constraint) and accept only those whose assumptions hold for a curated narrative graph; default to generic graph measures with explicit degree-preserving null models. Re-label 'connectome' as heuristic where assumptions fail.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-044:
**Date flagged:** 2026-05-21
**Source item:** PRESUMPTION-222
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** Narrative compression == information-theoretic compression — description length presumed definable/computable over PRS triplets.

**What is at risk:** ASSUMPTION-208's headline progress metric and any 'compression' claim about the corpus; the connectome compression sub-claim in ASSUMPTION-201.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Moderate; computable proxies — LM codelength, MDL graph summarization — exist). 15b CHALLENGED (Strong; no canonical/computable description length, scheme-dependence, syntax != meaning). Designer-unaware presumption gating a headline metric.

**Recommended action:** Drop the identity. Commit to a single explicitly-labeled, computable proxy (LM cross-entropy codelength OR MDL graph summarization), fix and publish its coding scheme, and validate it against independently-judged progress. Treat it as a scheme-relative indicator, never as 'the' narrative compression. Resolve before ASSUMPTION-208's metric is used.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-045:
**Date flagged:** 2026-05-21
**Source item:** PRESUMPTION-223
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** Making integration visible/attractive is value-neutral — convergence-emphasis views presumed not to bias toward convergence over preserved rivalry.

**What is at risk:** The pluralism commitment in ASSUMPTION-207; the credibility of any 'convergence is increasing' reading drawn from the viz; self-confirming unification.

**Evidence summary:** 15a NO-SUPPORT-FOUND (Weak; neutrality is only an aspiration). 15b CHALLENGED (Strong; framing effects, viz-ethics, attention/salience all show emphasis shapes inference). Clear asymmetry: no support for neutrality, strong evidence against it.

**Recommended action:** Stop treating the convergence-emphasis design as value-neutral. Give preserved rivalry/incommensurability visual parity with convergence (color/size/position), audit the view for convergence tilt, and A/B test whether viewers over-estimate convergence vs a balanced control. The text-level pluralism guard is insufficient against pre-attentive salience.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-046:
**Date flagged:** 2026-05-21
**Source item:** PRESUMPTION-228
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** The "3 literal hubs" finding reflects the territory, not the resource-naming/normalization method (measurement-artifact risk).

**What is at risk:** DECISION-040 (convergence-is-analogical) if it relies on the '3 hubs' count; the evidence basis cited for ASSUMPTION-205 (the principle is INCORPORATED as PREMISE-042, but the count is quarantined here).

**Evidence summary:** 15a NO-SUPPORT-FOUND (Weak; only conditional support under controlled vocabulary, which is not documented). 15b CHALLENGED (Strong; vocabulary problem, entity resolution, in-system FLAG A measurement-integrity history). Strong asymmetry against trusting the raw count.

**Recommended action:** Before DECISION-040 firms, run entity resolution / normalization on shared-resource names and a sensitivity analysis re-counting literal hubs under >=3 reasonable normalization schemes; report stability. Use the analogical-convergence PRINCIPLE (PREMISE-042), not the raw literal count, as the decision basis.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

Total new REVISEs this run: 5 (REVISE-042 through REVISE-046). HIGH urgency: REVISE-043, REVISE-044. All status AWAITING-REVIEW per protocol (require Tom's response before status changes).
Clusters: FLAG F connectome-analogy transfer (REVISE-043 HIGH); FLAG G compression-metric definability (REVISE-042, REVISE-044 HIGH); FLAG A measurement-integrity continuation (REVISE-046); convergence-emphasis neutrality (REVISE-045).

---

---
## 2026-05-23 batch — REVISE-047..049 (two-summa experiment cluster + git-history exposure)

---
### REVISE-047:
**Date flagged:** 2026-05-23
**Source item:** ASSUMPTION-215
**Item type:** ASSUMPTION
**Urgency:** HIGH

**Statement:** A "Conscious-Realist-Monist summa" can be constructed as a genuine rival to the Thomist summa and run head-to-head to produce evidence.

**What is at risk:** DECISION-044 (launch of the two-summa experiment) and OPEN-062; the evidential value of the experiment's headline result; the project's MacIntyrean credibility.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Moderate; rival comprehensive frameworks can be constructed and compared — MacIntyre's own three-rival-versions, adversarial collaboration, comparative theology). 15b CHALLENGED (Strong; by the project's OWN MacIntyrean definition a tradition is historically extended and socially embodied, so a constructed corpus is not a genuine tradition; and Conscious-Realist-Monism is the designer's own position, so the contest has a refereeing/home-team bias). Moderate-vs-strong asymmetry on a high-stakes, self-undermining item.

**Recommended action:** Before launch, decide whether Summa-2 must be a genuine tradition or a DECLARED constructed synthesis (and frame the claim accordingly, acknowledging the asymmetry with the canon). Remove the refereeing conflict: have an independent constructor/agent build and steelman Summa-2, and pre-register the comparison criteria and the conditions under which Thomism would win. A contest that cannot be lost is not evidential. Co-anchors SYSTEMIC-RISK-FLAG H.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-048:
**Date flagged:** 2026-05-23
**Source item:** PRESUMPTION-233
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** The head-to-head presumes the two summae are commensurable enough to be compared on shared criteria — against the project's own MacIntyrean incommensurability commitment.

**What is at risk:** Whether the two-summa experiment can yield UNBIASED evidence at all; the pluralism commitment in ASSUMPTION-207; coherence of the project's MacIntyrean foundations; DECISION-044.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Moderate; rational comparison without a neutral standard IS possible — MacIntyre's epistemological-crisis mechanism, Kuhn's "incommensurable != incomparable," Davidson). 15b CHALLENGED (Strong; MacIntyre denies any tradition-neutral standard, so "shared criteria" scoring smuggles in one tradition's success-conditions — directly contradicting ASSUMPTION-207). Crucially the supportive route is a DIFFERENT method (tradition-internal) than the shared-criteria scoring the presumption describes.

**Recommended action:** Do not score the head-to-head on imposed neutral/shared criteria. Either (a) use MacIntyre's tradition-internal test — judge each tradition by whether it can resolve the rival's epistemological crises in its own terms — or (b) run the comparison under each tradition's own criteria separately and report both, declaring criteria provenance. Resolve before DECISION-044. Co-anchors SYSTEMIC-RISK-FLAG H with REVISE-047.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-049:
**Date flagged:** 2026-05-23
**Source item:** PRESUMPTION-238
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** Parking the git-history scrub presumes acceptable residual exposure while parked; stop-tracking presumed sufficient interim mitigation; no trigger set (success-criteria gap).

**What is at risk:** Confidentiality/consent of sensitive content already in git history (the Hoffman x Levin transcript, narration zips); DECISION-047; OPEN-064; the project's exposure the instant the repo is shared or made public.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak-Moderate; time-boxed risk acceptance + private-repo compensating control + stop-tracking-as-first-step are legitimate IF exposure is bounded and a trigger exists). 15b CHALLENGED (Strong; git history is immutable — stop-tracking does NOT remove already-committed content; standard secret/PII remediation requires history rewrite; "no trigger set" is unbounded risk acceptance). Conditions for the supportive case are exactly what is missing.

**Recommended action:** Set an explicit, hard trigger — execute the history scrub before ANY repo-publicity/sharing step (formalize OPEN-064's intent into a gate, not a note). Make the risk acceptance explicit and time-boxed; decide now whether to rewrite history (git-filter-repo/BFG) and, for any secrets, rotate; confirm the repo stays private until the scrub runs. Treat parked-and-committed sensitive content as recoverable by anyone with repo access.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

Total new REVISEs this run (2026-05-23): 3 (REVISE-047 through REVISE-049). HIGH urgency: REVISE-047, REVISE-048. All status AWAITING-REVIEW per protocol (require Tom's response before status changes).
Clusters: SYSTEMIC-RISK-FLAG H two-summa comparability (REVISE-047, REVISE-048 HIGH; MONITOR-221/224/225 ride the flag); git-history exposure (REVISE-049).

---

## Batch 2026-05-24 (Agent 15c -- c2a2-lit-search-pipeline scheduled run)

### REVISE-050:
**Date flagged:** 2026-05-24
**Source item:** PRESUMPTION-240
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** The AWAITING-REVIEW gating of REVISE flags presumes the human review gate is reliably available -- but it has been absent four consecutive days; HIGH-urgency self-corrections sit unactioned.

**What is at risk:** The project's entire self-correction mechanism. Standing HIGH-urgency REVISE flags (REVISE-047/048 from 2026-05-23, plus REVISE-051 from this run) sit unactioned; the "AWAITING-REVIEW" state reads as orderly while it is actually a silent stall (Rule 12 fail-loud violation).

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; human-gated review is reliable only WHEN resourced with on-call/escalation/SLA -- Beyer et al. 2016 SRE -- which is exactly what is absent). 15b CHALLENGED (Strong; unattended queues grow without bound (queueing theory / Little's Law), alarm fatigue (Cvach 2012) and automation complacency (Parasuraman & Manzey 2010) erode response, and oversight steps frequently go unperformed (Green 2022)). The observed 4-day absence is direct disconfirming data. Reinforced by existing validated premise that human-review capacity is the binding HITL bottleneck.

**Recommended action:** Add an explicit SLA + escalation for AWAITING-REVIEW items and a timeout policy: for HIGH-urgency items unreviewed within N days, escalate loudly (notification) and/or apply a conservative safe-default (e.g., auto-pause the affected capability) rather than waiting silently. Surface an "oldest-unactioned-item age" metric so a multi-day stall cannot pass unnoticed. Resolve jointly with REVISE-051 and the standing REVISE-047/048 backlog. Anchors SYSTEMIC-RISK-FLAG I.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-051:
**Date flagged:** 2026-05-24
**Source item:** PRESUMPTION-243
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** Locating accountability in "Tom's review gate" (ASSUMPTION-221) presumes the gate is exercised; with the 4-day signout it is currently a no-op, so the accountability story is presently unwarranted.

**What is at risk:** The coherence of the project's accountability claim for its autonomous ("ownerless") agents (ASSUMPTION-221, parked at MONITOR-230). For the duration of the signout, autonomous-agent outputs accrue under an assurance of accountability that is not currently operative.

**Evidence summary:** 15a SUPPORTED (Strong; accountability requires an EXERCISED control -- COSO/SOC design-vs-operating-effectiveness; Santoni de Sio & van den Hoven 2018 tracking condition; Green 2022 oversight-that-isn't-performed; Elish 2019 moral crumple zone). 15b NO-CHALLENGE-FOUND (Weak; the "standing authority / periodic review suffices" counter covers brief bounded gaps, not an open-ended multi-day no-op with HIGH-urgency items queued). The surfaced vulnerability is real and currently active.

**Recommended action:** Either (a) restore/guarantee gate exercise (the SLA + escalation of REVISE-050), or (b) explicitly downgrade the accountability claim to "latent/periodic" with a bounded parking window AND a hard rule that no irreversible/external action fires while the gate is parked, plus tracing every autonomous output to a responsible human regardless of gate timing. Note: this REVISE is the precondition whose resolution would let ASSUMPTION-221 (MONITOR-230) be INCORPORATED. Couples PRESUMPTION-240 (REVISE-050). Co-anchors SYSTEMIC-RISK-FLAG I.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

Total new REVISEs this run (2026-05-24): 2 (REVISE-050, REVISE-051). HIGH urgency: REVISE-050. All status AWAITING-REVIEW per protocol (require Tom's response before status changes).
Cluster: SYSTEMIC-RISK-FLAG I -- unexercised human review gate (REVISE-050 HIGH, REVISE-051 MED-HIGH; MONITOR-230 rides the flag as INCORPORATE-pending). NOTE: this same gate failure is why the 2026-05-23 REVISE-047/048 (HIGH) remain unactioned -- the backlog is itself evidence for REVISE-050.

---

## Batch 2026-05-25 (Agent 15c -- c2a2-lit-search-pipeline scheduled run)

### REVISE-052:
**Date flagged:** 2026-05-25
**Source item:** ASSUMPTION-222
**Item type:** ASSUMPTION
**Urgency:** LOW-MEDIUM

**Statement:** Thematically convergent same-week intake proposals (Wright exile + Rohr exile + Stump corporate-substance) should be promoted into the network as a single unit, because together they articulate one paradigm-bridge (Summa 2026 "loving unity as telos").

**What is at risk:** Network credibility. Promoting a same-week / same-pipeline cluster 'as a single unit because together they articulate one paradigm-bridge' bakes a possible method artifact into the network as if it were validated cross-tradition structure (same family as the SUPER-BRIDGE over-claim risk, ASSUMPTION-020). Downstream agents will read the unit as established homology.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Moderate; convergence CAN be a validity signal — Campbell & Fiske 1959 — and chunking aids reuse, but only under method independence). 15b CHALLENGED (Strong; common-method variance — Campbell & Fiske 1959; Podsakoff et al. 2003; Podsakoff & Organ 1986 — holds that same-method/same-occasion convergence is artifact-suspect, which is exactly this case).

**Recommended action:** Require a cross-method / cross-occasion discriminant check BEFORE unit-promotion: re-elicit each source independently (different agent/occasion/prompt) and confirm the 'loving unity as telos' bridge still co-emerges; OR promote the three proposals individually and let any convergence emerge from independent routing rather than asserting it at intake. Couples PRESUMPTION-244 (MONITOR-235).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-053:
**Date flagged:** 2026-05-25
**Source item:** PRESUMPTION-245
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** The 15d stale-escalation rule (ASSUMPTION-223) presumes an available human endpoint, but the same review-gate outage stalling the REVISE backlog (PRESUMPTION-240/REVISE-050) also terminates these escalations -- converting a literature-stall into a human-stall.

**What is at risk:** The self-correction loop's exit path. ALL human-terminating routes — the REVISE backlog (REVISE-047..052), the STALE escalations (MONITOR-040/042/044), and INCORPORATE-pending preconditions (MONITOR-230, MONITOR-233) — converge on one unavailable reviewer (review gate dark 5+ days). The STALE-escalation rule (ASSUMPTION-223) therefore only RELABELS a literature-stall as a human-stall; 'escalated to Tom' reads as orderly while nothing moves (Rule 12 fail-loud violation).

**Evidence summary:** 15a SUPPORTED (Strong; single-point-of-failure alerting — escalation resolves a stall only if the next tier is reachable (SRE/incident practice, OnPage 2024, incident.io 2025); unbounded-queue/no-server result from queueing theory; Parasuraman & Manzey 2010 on unexercised human legs). 15b NO-CHALLENGE-FOUND (Weak; no literature supports that escalation to an absent endpoint clears a backlog).

**Recommended action:** Implement OPEN-066's direction: a SINGLE 'needs-Tom' queue with one age/escalation policy and an 'oldest-unactioned age' metric; a safe-default tier that may proceed without the human for reversible, low-stakes items, vs a tier that must wait; out-of-band escalation that does not itself depend on the gate. Couples REVISE-050 (the SLA/escalation mechanism) and ASSUMPTION-223 (MONITOR-233). Extends SYSTEMIC-RISK-FLAG I; answers OPEN-066.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-054:
**Date flagged:** 2026-05-25
**Source item:** PRESUMPTION-247
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** Extracting "stated assumptions" from agent output on a no-human day presumes an agent's stated rationale == a designer-aware commitment -- blurring the ASSUMPTION (designer-aware) vs PRESUMPTION (surfaced-after-the-fact) distinction the provenance protocol exists to protect.

**What is at risk:** Provenance-protocol integrity. Default-tagging agent-surfaced rationale as ASSUMPTION (designer-aware) collapses the ASSUMPTION/PRESUMPTION distinction the protocol exists to protect, silently corrupting both the counts and the downstream epistemic weighting. Self-referential: this very run extracts agent-surfaced items on a no-human day.

**Evidence summary:** 15a SUPPORTED (Strong; introspection illusion — Nisbett & Wilson 1977 — shows even human stated reasons are confabulated reconstructions; CoT-faithfulness — Turpin et al. 2023 — shows LLM-stated reasoning is frequently unfaithful to the actual cause). 15b NO-CHALLENGE-FOUND (Weak; no basis for equal epistemic weight; the pragmatic counter only supports keeping the items under a CORRECT, non-equivalent tag).

**Recommended action:** Add a provenance sub-type for agent-stated rationale that is NOT designer-confirmed (e.g., 'agent-surfaced rationale — designer-unconfirmed'), and require explicit human confirmation before any agent-surfaced item is promoted to ASSUMPTION (designer-aware) status. Until then, count agent-surfaced 'assumptions' separately. Couples PRESUMPTION-241.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

Total new REVISEs this run (2026-05-25): 3 (REVISE-052, 053, 054). Urgency: REVISE-053 MED-HIGH; REVISE-052 LOW-MED; REVISE-054 MED. All status AWAITING-REVIEW per protocol (require Tom's response before status changes).
**Fail-loud / SYSTEMIC-RISK-FLAG I continuation:** All 3 REVISEs enter the AWAITING-REVIEW queue behind the same human review gate that has now been dark 6 consecutive days. REVISE-053 is *about* that bottleneck and must be escalated OUT-OF-BAND, not via the gate it describes. The standing backlog (REVISE-047/048/049/050/051) remains unactioned. This run can DETECT but not REMEDIATE — the closed-loop-no-exit pattern of FLAG I persists and now spans 3 more flags. OPEN-066 (single needs-Tom queue + escalation policy) is the project's #1 item.

---

## 2026-05-27 RUN — c2a2-lit-search-pipeline batch (5 new REVISEs 055-059)

This batch dispositions 24 cycle-0 items: 11 from the 2026-05-25 14a/14b batch and 13 from the 2026-05-26 14a/14b batch. Five items received REVISE disposition. See lit_search_returns.md 2026-05-27 entry for full DISPOSITION records.

### REVISE-055:
**Date flagged:** 2026-05-27
**Source item:** ASSUMPTION-229
**Item type:** ASSUMPTION
**Urgency:** MEDIUM

**Statement:** Leading theories of consciousness are substrate-permissive in principle — their brain-focus is a convention of imagination — so the substrate-independence thesis is portable from cognition to consciousness for the PRS-31 AI-membership question.

**What is at risk:** The PRS-31 AI-membership criterion — a load-bearing item in the C2A2 master architecture for AI-as-tradition-member determination. The current assumption rests on substrate-permissive consciousness theories (IIT, GWT, HOT, AST) as if their substrate-permissiveness is uncontested. It is not: Searle's Chinese Room, Chalmers' hard problem, Block's access-vs-phenomenal distinction, the embodiment tradition (Merleau-Ponty / Varela), and recent cellular-mechanism work (Aru, Suzuki & Larkum 2020) all challenge the in-principle portability of consciousness. Within C2A2's own roster, phenomenologically-rooted traditions (MacIntyre, Aquinas via Stump, Rohr) may dispute the framing.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Moderate; the formal portability across IIT/GWT/HOT/AST is documented by Rouleau & Levin 2026 and the multiple-realizability tradition Putnam 1967 / Fodor 1974). 15b PARTIALLY-CHALLENGED (Moderate-Strong; Searle 1980 Chinese Room, Chalmers 1995 hard problem, Block 1995, Aru-Suzuki-Larkum 2020, embodiment tradition all deny in-principle portability).

**Recommended action:** Frame PRS-31 CONDITIONALLY on a theory choice — "IF substrate-permissive consciousness theories are correct, then AI-membership operationalizes as X; IF embodiment/hard-problem framings are correct, then AI-membership operationalizes as Y." Document the theory-dependence explicitly so downstream agents know PRS-31 is method-dependent. Hold the unconditional "substrate-permissive in principle" claim open. Pair with a sensitivity analysis: for each candidate consciousness theory, compute the implied AI-membership criterion. Architectural import for the Loughran-master integration project.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-056:
**Date flagged:** 2026-05-27
**Source item:** PRESUMPTION-248
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** Deferring the 34-item ingest backlog to a "focused, ideally attended" session presumes an attended session will occur on a useful timescale, but the same human gate that has been dark 5-6 days is the bottleneck — the deferral may be a third instance of OPEN-066 / SYSTEMIC-RISK-FLAG I.

**What is at risk:** Extends SYSTEMIC-RISK-FLAG I to a third route. The PRS extraction backlog (the next major work-cycle's content) now sits behind the same gate that has been dark 5-6 days. The 2026-05-26 attended session demonstrated the recursion exactly as the presumption predicts: approval queue cleared in minutes, PRS work deferred to ANOTHER "ideally attended" session. Each deferral relabels a literature-stall as a human-stall (per REVISE-053 pattern). The C2A2 self-correction pipeline can DETECT this but cannot REMEDIATE without out-of-band action.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; defer-to-attended is a valid pattern ONLY under engineered availability — Beyer 2016; ITIL emergency-change; Hollnagel 2014). 15b CHALLENGED (Moderate-Strong; Goldratt Theory of Constraints + queueing theory + SRE single-point-of-failure analysis all converge: multi-queue convergence on one unreliable reviewer is queueing-theory canonical failure mode).

**Recommended action:** (1) Extend OPEN-066 single-needs-Tom queue to include the PRS-extraction backlog explicitly — it should not have a separate, parallel deferral path. (2) Engineer the ingest-pipeline preconditions (idempotency + rollback + observability — addresses ASSUMPTION-225 / MONITOR-237's INCORPORATE-pending block) so attended-only is not the safety mechanism. (3) Add an SLA + age-threshold so a backlog past N days surfaces an out-of-band alert. Couples REVISE-050 (the SLA/escalation mechanism), REVISE-053 (single needs-Tom queue), ASSUMPTION-225 (MONITOR-237). Co-anchors SYSTEMIC-RISK-FLAG I.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-057:
**Date flagged:** 2026-05-27
**Source item:** PRESUMPTION-252
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** The "approved" status counter for proposals is silently misaligned with the underlying tradition-wiki state — 34 of 131 approved (26%) are not yet in the tradition wikis; "approved" reads as "ingested" but means "approved and possibly-ingested-or-not."

**What is at risk:** Measurement-validity. A 26% silent gap between intake-stage state ("approved") and downstream state ("ingested in tradition wiki") is a textbook ETL state-decoupling + Goodhart surrogation pattern. The headline metric is "approved," which reads as completed network contribution; the actual network contribution lags. Downstream agents and metrics consumers (changelog, snapshot, dashboard) treat the "approved" count as the success criterion, masking the next bottleneck (PRS-extraction → REVISE-056). Couples PRESUMPTION-258 (MONITOR-254 — the headline-framing extension) and the broader Goodhart family (PRESUMPTION-201, PRESUMPTION-246 / MONITOR-236).

**Evidence summary:** 15a SUPPORTED (Strong; Kimball & Ross 2013 ETL state separation; Fowler PEAA state-machine modeling; Goodhart 1975 / Strathern 1997 surrogation; established anti-pattern). 15b NO-CHALLENGE-FOUND (Weak; stage metrics are legitimate IF both stages are reported — but the presumption is about silent decoupling, which the support direction documents directly).

**Recommended action:** (1) Distinct terminal states for "approved" and "ingested-in-wiki"; (2) dual-display in any headline framing (both counts, plus lag); (3) commit-cadence target so the lag stays bounded; (4) pair with the dual-display headline + next-bottleneck call-out in MONITOR-254. Update DECISION-048 candidate to require both metrics.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-058:
**Date flagged:** 2026-05-27
**Source item:** PRESUMPTION-256
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** The 1-week-cadence sit-down target and the sit-down-availability bottleneck diagnosis presume future signout/attention-outage events share the 10-second-resolvable failure mode of the 2026-05-22 to 2026-05-26 outage; alternate failure modes (browser/MFA/OAuth/ICANN/non-signout exec-function dips) may not be 10-second-resolvable.

**What is at risk:** The architectural design that flows from ASSUMPTION-235/236 (MONITOR-246/247 — sit-down-availability is THE bottleneck; weekly cadence is sufficient). If the next outage event is NOT 10-sec-resolvable — and the literature predicts heterogeneous failure modes (Kahneman & Tversky availability heuristic; SRE post-incident analysis; OAuth/MFA failure-mode taxonomy) — the design is mis-targeted. The "binary framing third category" pattern (PRESUMPTION-253/259) recurs here: the failure-mode space is being subordinated to a single recent observation.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; availability-heuristic + stationary-distribution gives some defense but the support is essentially "what else can you do with N=1"). 15b CHALLENGED (Moderate-Strong; failure-mode heterogeneity is canonical, single-event-attribution is a documented bias, OAuth/MFA failure modes have known non-10-sec resolution times).

**Recommended action:** (1) Instrument failure-mode tracking — log the resolution mode for every outage event; (2) design escalation/SLA/safe-defaults that work across modes, not optimized for 10-sec resolution alone; (3) revisit ASSUMPTION-235/236 (MONITOR-246/247) framing to be "complement, not alternative" to queue/policy design; (4) tiered cadence (daily for HIGH, weekly for MED) rather than flat weekly. Couples ASSUMPTION-235/236 (MONITOR-246/247); PRESUMPTION-259 (MONITOR-255 — the recurrence). Extends FLAG I to multi-failure-mode framing.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---
### REVISE-059:
**Date flagged:** 2026-05-27
**Source item:** PRESUMPTION-257
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** The 2026-05-25 Rule-12 gap (registries advanced ASSUMPTIONs 225-229 / PRESUMPTIONs 248-253 but no 2026-05-25_changes.md or 2026-05-25_snapshot.md was written) is direct evidence the 14a/14b artifact-write step can fail silently while the registries-advance step succeeds — a Rule-12 fail-loud violation embedded in the pipeline that exists to detect Rule-12 violations.

**What is at risk:** Pipeline-integrity. Self-referential failure: the C2A2 self-awareness pipeline writes paired outputs (registry-advance + artifact-write) that should be atomic. If one succeeds while the other fails silently, the pipeline that exists to detect Rule-12 violations IS a Rule-12 violator. The 2026-05-25 incident is direct empirical evidence: registry entries 225-229/248-253 exist; the paired changelog/snapshot artifacts do not. This is structurally identical to the silent-partial-failure pathology documented in Gray & Reuter 1992 and Nygard 2007.

**Evidence summary:** 15a SUPPORTED (Strong; transaction-processing literature on atomicity, distributed-systems silent-partial-failure anti-pattern, ISO 27001 audit-trail atomicity requirements). 15b NO-CHALLENGE-FOUND (Weak; the specific-incident diagnosis MAY be benign — the artifacts may be by-design attended-only — but the presumption-level vulnerability stands).

**Recommended action:** (1) Diagnose the specific 2026-05-25 incident — was the missing artifact intended-asymmetric (attended-only) or a silent partial failure? (2) Document the contract: which artifacts are always-written vs which are sit-down-attended; (3) automate post-write invariant check on always-written artifacts; (4) update the 14a/14b pipeline definition to make atomicity guarantees explicit. Self-referential elevation: this concerns the integrity of the pipeline producing today's outputs. Couples PRESUMPTION-241 (introspection-pipeline integrity), PRESUMPTION-247 (REVISE-054 — provenance-protocol integrity).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

Total new REVISEs this run (2026-05-27): 5 (REVISE-055..059). Urgency: REVISE-056 HIGH; REVISE-057/058/059 MEDIUM-HIGH; REVISE-055 MEDIUM. All status AWAITING-REVIEW per protocol.

**Fail-loud / SYSTEMIC-RISK-FLAG I continuation:** All 5 REVISEs enter the AWAITING-REVIEW queue behind the same human review gate. The 2026-05-26 attended session cleared the APPROVAL queue but the REVISE-response gate remains effectively dark for response purposes (no records of REVISE-047..054 being actioned). REVISE-056 extends FLAG I explicitly to the PRS-extraction backlog (3rd documented FLAG I route). REVISE-058 extends FLAG I to the failure-mode-heterogeneity dimension. REVISE-059 is self-referential — concerns the integrity of the very pipeline producing today's output and must be diagnosed out-of-band. The standing backlog (REVISE-047..054) remains unactioned + 5 new REVISEs this run. OPEN-066 (single needs-Tom queue + escalation policy) is the project's #1 item.

---

## 2026-05-28 RUN — REVISE additions (REVISE-060..064)

### REVISE-060:
**Date flagged:** 2026-05-28
**Source item:** ASSUMPTION-242
**Item type:** ASSUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** Canonizing the truncation recurrence in the `.md` header as a Pathway-14 honesty-layer event is the substantive response taken today; no code-level fix attempted; "the auto-send `type`-with-newlines path is a known broken path that wasn't fixed after 05-18."

**What is at risk:** The honesty-layer mechanism itself. Documentation-as-mitigation is supported as a FIRST step in incident-response literature (Allspaw; Cook & Woods; Beyer SRE) but NOT as a complete response. The 2026-05-18 → 2026-05-27 9-day gap with recurrence is direct empirical evidence that canonization in this case did not produce remediation. The pattern risks becoming the highest-level instance of PRESUMPTION-248 (defer-as-bottleneck-relabel) — a pathology already validated within C2A2. If the honesty-layer's response to "known broken path" becomes "canonize and continue," the very mechanism designed for self-awareness becomes a vehicle for self-deferral.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Moderate; canonization is legitimate first step per Cook & Woods, Polanyi, Schön; honesty-layer architecture is internally consistent). 15b CHALLENGED (Moderate-Strong; SRE/incident-response/complex-systems-failure literatures require remediation commitment paired with documentation; the 05-18 → 05-27 gap is direct empirical instance of the "we noticed" trap; PRESUMPTION-248 already validates the pattern in C2A2).

**Recommended action:** (1) Every honesty-layer event must include action item + owner + deadline (not just description); (2) recurrence triggers required-fix, not additional canonization; (3) audit canonization-to-remediation ratio (target ≥ 0.5 within 30 days); (4) alert when canonization-without-remediation exceeds N days. Couples PRESUMPTION-263 / REVISE-063.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-061:
**Date flagged:** 2026-05-28
**Source item:** PRESUMPTION-260
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** [inferred] The web_enrich design presumes Tavily top-5 snippets are sufficient for cross-tradition / paradigm-bridge queries; no calibration check on whether top-5 + WEB_CONTEXT-injection is adequate for C2A2's tradition-aware query shape.

**What is at risk:** Broker-v4 web_enrich quality for the highest-value C2A2 use case — cross-tradition / paradigm-bridge queries. Scholarly cross-domain retrieval is a documented distinct retrieval shape (BEIR; SPECTER; Adlakha et al.). Generic web search underperforms tradition-aware retrieval for this shape; top-5 is documented as inadequate (10-20 snippets needed). Without calibration, the inadequacy is invisible until users encounter shallow answers; the failure mode does not trigger an alert. C2A2's tradition-bridge use case is exactly the case where the literature predicts inadequacy.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; top-5 is defensible baseline for general RAG (Karpukhin 2020) but does not validate the specific cross-tradition use case). 15b CHALLENGED (Moderate; BEIR / SPECTER / Adlakha et al. directly support the inadequacy concern for scholarly cross-domain retrieval).

**Recommended action:** (1) Pre-ship or 30-day post-ship calibration sprint: 20 known-answer cross-tradition queries, measure adequacy at K=5 vs K=10 vs K=20; (2) consider Semantic Scholar or domain-tuned retrieval for tradition-bridge mode; (3) flag tradition-bridge as distinct query class with separate retrieval policy; (4) instrument retrieval quality metrics (recall@K against known-answer benchmark).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-062:
**Date flagged:** 2026-05-28
**Source item:** PRESUMPTION-262
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** [inferred] The 2026-05-18 truncation diagnosis was complete; today's recurrence = "fix-unimplemented" rather than "diagnostic-incomplete"; alternative reading (multi-causal-path bug; one patched, another active) not separately considered.

**What is at risk:** Operational reliability of an auto-send user-facing path. Reason / Cook & Woods / Allspaw all explicitly recommend re-investigation on recurrence, not re-execution of prior diagnosis. Multi-causal-path bug patterns are documented as the norm in complex systems; single-cause attribution is systematic underestimate. ProseMirror has multiple input paths (keypress, paste, insertText, transaction.replace); a fix to one path doesn't preclude another path from producing the same symptom. The "fix did not land" framing is the comfortable hypothesis; "fix landed but missed a path" is the rigorous one. Without re-investigation, the actually-active path remains unaddressed and a third recurrence becomes more likely.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; single-cause-as-first-pass is defensible (Cockburn; Allspaw) when diagnosis is documented and unimplemented). 15b CHALLENGED (Moderate-Strong; Reason / Cook & Woods / Allspaw all recommend re-investigation on recurrence; ProseMirror multi-input-path architecture and Tiptap bug history support multi-causal-path hypothesis).

**Recommended action:** (1) Re-investigate the 2026-05-27 instance before re-executing the 05-18 fix; (2) trace the input path through editor's transaction log; (3) compare 05-18 and 05-27 traces; (4) test patch against all 4+ ProseMirror input paths before declaring fixed; (5) treat recurrence as new diagnostic data, not confirmation of old. Couples ASSUMPTION-240 / MONITOR-259 (truncation-recurrence operational monitoring).

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-063:
**Date flagged:** 2026-05-28
**Source item:** PRESUMPTION-263
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** [inferred] Naming-a-recurrence-in-a-document (the Pathway-14 honesty-layer event tag) is a substantive response to a known broken path; this may be the same defer-as-bottleneck-relabel pattern (PRESUMPTION-248) recurring at the honesty-layer itself.

**What is at risk:** The integrity of C2A2's primary self-awareness mechanism. PRESUMPTION-248 (already validated within C2A2 as a pathology) is the exact pattern recurring at the honesty-layer's own mechanism — the very tool that exists to surface such patterns. The 05-18 to 05-27 9-day gap with recurrence-without-intervening-fix is direct empirical evidence. Literature on naming-as-deferral (Bainbridge "Ironies of Automation"; Goffman on ritual; Allspaw on postmortem-action-items) is robust. If canonization substitutes for action at the honesty-layer level, every downstream self-awareness mechanism in C2A2 inherits the same vulnerability. Self-referential elevation: this is the mechanism that REVISE-060 also bears on, viewed through the unstated/presumption lens.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak-Moderate; canonization as legitimate first-step (Polanyi; Schön; Cook & Woods)). 15b CHALLENGED (Moderate-Strong; PRESUMPTION-248 internal-evidence + Bainbridge/Goffman/Allspaw literature; the 9-day gap is direct empirical instance).

**Recommended action:** (1) Pair every honesty-layer event with action item + owner + deadline (mandatory); (2) recurrence triggers required-fix, not additional canonization; (3) audit canonization-to-remediation ratio (target ≥ 0.5 within 30 days); (4) alert when canonization-without-remediation exceeds 14 days; (5) treat REVISE-063 + REVISE-060 as a coupled architectural decision — the honesty-layer protocol needs revision. Self-referential elevation: HIGH urgency because the mechanism producing today's output is itself implicated.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-064:
**Date flagged:** 2026-05-28
**Source item:** PRESUMPTION-264
**Item type:** PRESUMPTION
**Urgency:** MEDIUM-HIGH

**Statement:** [inferred] This evening's c2a2-self-awareness-daily run presumes its own artifact-write step will succeed atomically with registry-advance; REVISE-059's concern about silent artifact-write failure is acknowledged but not architecturally addressed before tonight's run.

**What is at risk:** Pipeline-integrity, self-referentially. REVISE-059 (PRESUMPTION-257) established that the 14a/14b artifact-write step can fail silently while the registries-advance step succeeds — a Rule-12 fail-loud violation embedded in the pipeline that exists to detect Rule-12 violations. PRESUMPTION-264 names the gap between flagging that vulnerability and architecturally addressing it. Gray & Reuter / Nygard / Anderson all support: self-monitoring systems require atomicity guarantees + external verification; internal self-checks alone are documented as producing silent gaps. Running tonight's pipeline (or the lit-search pipeline now executing) without architectural remediation means the failure mode remains exposed for another cycle. The presumption (architectural concern can be deferred behind operational continuity) is exactly the pattern that produced the original silent failure.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; atomicity-and-verify-after-write pattern is well-grounded (Gray & Reuter; Kleppmann)). 15b CHALLENGED (Moderate; Gray & Reuter / Nygard / Anderson explicitly warn against deferred architectural remediation of self-monitoring failures; REVISE-059 is direct C2A2 instance).

**Recommended action:** (1) Add external verification step after each daily run — independent script checks registry-advance + artifact-write + return-write succeeded together (or all rolled back); (2) document explicit atomicity contract for the 14a/14b pipeline; (3) treat REVISE-059 + REVISE-064 as coupled architectural blocker — neither resolves until both are addressed; (4) fail-loud check before next-cycle start. Self-referential: this pipeline's own integrity is at stake.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

Total new REVISEs this run (2026-05-28): 5 (REVISE-060..064). Urgency: REVISE-063 HIGH; REVISE-060/062/064 MEDIUM-HIGH; REVISE-061 MEDIUM. All status AWAITING-REVIEW per protocol.

**Fail-loud / SYSTEMIC-RISK-FLAG I continuation:** Four of five new REVISEs join or extend FLAG I:
- REVISE-060 + REVISE-063: honesty-layer canonization-as-substantive contested; recurrence of PRESUMPTION-248 defer-as-bottleneck-relabel at the self-awareness mechanism (HIGH self-referential elevation)
- REVISE-062: multi-causal-path bug pattern; recurrence of PRESUMPTION-259 binary-framing at the bug-diagnostic level
- REVISE-064: self-referential atomicity vulnerability; couples REVISE-059 (PRESUMPTION-257)
- REVISE-061: independent (broker-v4 calibration gap)

The standing AWAITING-REVIEW backlog (REVISE-047..059 = 13) + 5 new REVISEs this run = **18 total AWAITING-REVIEW**. The response-gate remains dark per FLAG I: closed-loop-no-exit. REVISE-063 and REVISE-064 in particular concern the integrity of the self-awareness mechanism itself and must be escalated OUT-OF-BAND. OPEN-066 (single needs-Tom queue + escalation policy) remains the project's #1 item.

---

## 2026-05-29 RUN — REVISE additions (REVISE-065..071)

### REVISE-065:
**Date flagged:** 2026-05-29
**Source item:** PRESUMPTION-267
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** [inferred] The "demo-path vs PRS-extraction" binary in today's For Morning Discussion #1 is the 4th instance of the binary-framing pattern (PRESUMPTION-253/259/262); the binary structure itself, not the particular pair, may be the load-bearing presumption; a third category is again subordinated.

**What is at risk:** The framing process itself. 4-instance recurrence is the canonical signature of organizational defensive-routine (Argyris) or framing-bias (Heath & Heath, Kahneman, Tversky). Continuing binary framings without structural restructuring will continue to subordinate third-and-fourth options. The 4-cycle pattern is internally validated; the same shape will recur unless the framing process is restructured.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; binary framings have conditional legitimate use under recognition-primed decision-making). 15b CHALLENGED (Moderate-Strong; Heath & Heath / Tversky & Kahneman / Argyris / Kahneman directly support the structural-bias reading; 4-instance internal recurrence is the direct evidence).

**Recommended action:** (1) Require ≥3 options for any prioritization framing; (2) explicit "what's the third option?" check at framing-time; (3) treat 4-instance recurrence as automatic trigger for framing-process review; (4) Argyris-style double-loop review of the framing process itself, not just individual decisions. Self-referential elevation: this concerns the framing mechanism that produces today's morning-discussion outputs.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-066:
**Date flagged:** 2026-05-29
**Source item:** PRESUMPTION-269
**Item type:** PRESUMPTION
**Urgency:** HIGH

**Statement:** [inferred] The "no-blind-push" constitutional rule (ASSUMPTION-245) presumes Tom's push sign-off availability scales through the 5.5-week pre-ISME period without becoming the bottleneck; the push gate is structurally identical to other FLAG-I human-stall routes.

**What is at risk:** Extends SYSTEMIC-RISK-FLAG I cluster to a potential 5th route. Bainbridge's "Ironies of Automation" directly predicts that the gate the constitutional rule creates becomes the bottleneck under load. C2A2's own FLAG-I cluster (REVISE-053/056/058) shows the pattern is structurally embedded. The 5.5-week ISME window is the load period. Constitutional rule erosion under deadline pressure (Reason normalization-of-deviation) compounds the risk. "Rule held today" (ASSUMPTION-245) is one positive observation that does not address aggregate stall-rate.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; rule design supported but scaling claim not). 15b CHALLENGED (Moderate-Strong; Bainbridge / Christiano / Reason / Allspaw all document HITL bandwidth-bottleneck pattern; FLAG-I internal cluster is direct evidence).

**Recommended action:** (1) Instrument push-gate from-stage-to-sign-off latency; (2) define SLA + escalation path for staged changesets exceeding N hours; (3) make rule-bounds explicit (changeset-size threshold, deadline-window adjustment); (4) couple with FLAG-I cluster remediation (REVISE-053 single-needs-Tom queue + escalation policy). Couples ASSUMPTION-245 (MONITOR-266). FLAG-I cluster extension.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-067:
**Date flagged:** 2026-05-29
**Source item:** PRESUMPTION-272
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** [inferred] The single Friston query in ASSUMPTION-244's verification protocol is representative of the Sociogram-tab query distribution for ship-readiness; query-class coverage is not separately defended.

**What is at risk:** Sociogram-tab ship-readiness verification adequacy. Beizer / Myers equivalence-class partitioning literature requires coverage spanning partitions; BEIR / SPECTER / Adlakha retrieval-evaluation literature requires multi-query benchmarks across task classes; scholarly cross-domain (tradition-bridge) queries are a documented distinct retrieval shape that single-query verification does not cover. Couples REVISE-061 (PRESUMPTION-260 broker-v4 calibration gap) — both concern under-defined query-class coverage at the integration verification level.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; single-path is defensible first gate per Beyer SRE / Forsgren but does not validate representativeness). 15b CHALLENGED (Moderate; Beizer / Myers / BEIR / SPECTER reject single-query-as-representative).

**Recommended action:** (1) Expand verification to 3-5 query classes (named-thinker, keyword, paradigm-bridge, multi-hop); (2) define query-class coverage rubric per integration; (3) couple with REVISE-061 calibration sprint (broker-v4 cross-tradition retrieval); (4) include class-coverage check in ship-readiness rubric. Couples ASSUMPTION-244 (MONITOR-265); REVISE-061.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-068:
**Date flagged:** 2026-05-29
**Source item:** PRESUMPTION-270
**Item type:** PRESUMPTION
**Urgency:** MEDIUM (Low-cost remediation; can be discharged quickly)

**Statement:** [inferred] The swarm-contract mirror pattern (root architecture/ + wiki/architecture/) is a stable ground-truth pattern; drift risk is not separately defended.

**What is at risk:** Ground-truth integrity of the swarm-contract document. Kleppmann / Nygard / Conway / Bass all document that copy-mirror conventions drift without active drift-detection. The assumption does not name a drift-detection mechanism. Downstream agents read either location; silent divergence produces inconsistent state. Symlink is the canonical literature-preferred remediation when both locations must always agree. The cost of remediation is near-zero (single symlink replacement or single file-hash check added to Janitor).

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; mirror conventions usable WITH drift-detection per Nygard / Kleppmann). 15b CHALLENGED (Moderate; same literature documents drift as default without detection; symlink canonical remediation).

**Recommended action:** (1) Replace copy-mirror with symlink (root architecture/ → wiki/architecture/, or vice versa) — near-zero-cost, instant remediation; OR (2) add file-hash equality check between the two locations to Janitor; (3) on drift detection, fail-loud per Rule-12. Lowest-cost REVISE in this run; could be discharged today.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-069:
**Date flagged:** 2026-05-29
**Source item:** PRESUMPTION-274
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** [inferred] "Architectural-reviewer pinned for post-ISME" presumes named-trigger deferral is operationally distinct from open-ended deferral; the named "post-ISME" trigger may join the deferred-with-named-trigger family under FLAG-I conditions.

**What is at risk:** Architectural-reviewer engagement. "Post-ISME" is the named-but-elastic trigger; named-but-elastic triggers are documented as functionally equivalent to open-ended deferrals when the named event itself slides (Allen, Bainbridge, Reason, Cook & Woods). C2A2's own validated PRESUMPTION-248 (defer-as-bottleneck-relabel) is direct internal evidence. ISME-end is itself elastic (post-event windows have no defined edge). Without trigger-discipline, the reviewer never engages.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak; named-trigger is better than open-ended per Allen / GTD / PMI, but not immune to FLAG-I when trigger itself slides). 15b CHALLENGED (Moderate; PRESUMPTION-248 internal-evidence + Allen / Bainbridge / Reason / Cook & Woods literature on elastic-trigger degradation).

**Recommended action:** (1) Tie the trigger to a date, not an event (e.g., "review by 2026-07-15"); (2) explicit re-surface SLA; (3) quarterly audit of all named-trigger deferrals; (4) treat "post-X" triggers as elastic by default unless calendar-anchored. Couples ASSUMPTION-246 (MONITOR-267); PRESUMPTION-248 family.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-070:
**Date flagged:** 2026-05-29
**Source item:** PRESUMPTION-273
**Item type:** PRESUMPTION
**Urgency:** MEDIUM

**Statement:** [inferred] ASSUMPTION-249's ISME ~5.5-week deadline is treated as a fixed external constraint; the alternative (renegotiating scope or timeline) is not separately considered.

**What is at risk:** Implicit scope-renegotiation. Iron-triangle literature (Atkinson, PMI PMBOK) requires that when time is fixed, scope and quality trade-offs be made explicit. Demo-path tiebreaking (ASSUMPTION-249) IS scope-shaping, but it's invisible-as-scope-decision. Brooks / Standish CHAOS document that fixed-deadline projects systematically ship reduced scope; without explicit acknowledgment, this scope-reduction is unaccounted. Post-ISME compounded-debt is the documented downstream effect when implicit trade-offs accumulate.

**Evidence summary:** 15a PARTIALLY-SUPPORTED (Weak-Moderate; fixed-deadline framing defensible for external conferences per Brooks / Reinertsen). 15b PARTIALLY-CHALLENGED (Weak-Moderate; Atkinson / PMI / Brooks / Standish all require explicit scope-vs-time trade-off acknowledgment).

**Recommended action:** (1) Make scope-vs-time-vs-quality trade-offs explicit per prioritization cycle; (2) document pre-ISME scope-commitment; (3) label demo-path tiebreaking as scope-decision, not just prioritization-heuristic; (4) track scope deferred to post-ISME for compounded-debt visibility. Couples ASSUMPTION-249 (MONITOR-270); FLAG-I cluster.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

### REVISE-071:
**Date flagged:** 2026-05-29
**Source item:** PRESUMPTION-275
**Item type:** PRESUMPTION
**Urgency:** HIGH (self-referential elevation)

**Statement:** [inferred] ASSUMPTION-250's reading of today's events as empirical evidence for REVISE-056 presumes the system's diagnostic predictions are independent of the behavior they predict; the prediction-and-observation loop runs entirely inside the same registry-and-summary apparatus.

**What is at risk:** The integrity of C2A2's self-awareness mechanism itself. The prediction-observation loop running entirely inside the same registry-and-summary apparatus is precisely the warning condition that Argyris (double-loop learning), Cook & Woods (second story), Goodhart's Law, and the philosophy-of-self-measurement literature (Lawvere / Hofstadter) all name as systematically bias-prone. ASSUMPTION-250's framing-shift question (MONITOR-271) is the live instance: the system is reading its own outputs as empirical evidence for a framing-shift, with no external check. This is the same self-referential vulnerability family as REVISE-063 (honesty-layer canonization) and REVISE-064 (atomicity verification) — three concurrent instances at three different levels of the self-awareness mechanism.

**Evidence summary:** 15a NO-SUPPORT-FOUND (Weak; reflection-in-action literature supports bounded reflection but does not validate independence claim). 15b CHALLENGED (Moderate-Strong; Argyris / Cook & Woods / Goodhart / Hawthorne / philosophy-of-measurement literature directly support the structural-bias reading; coupled with REVISE-063 / REVISE-064 makes the cluster significant).

**Recommended action:** (1) Require external check (Tom or Adaptive Sarah-mode) for any framing-shift commitment derived from internal recurrence-counts; (2) treat internal recurrence-counts as data, not conclusions; (3) treat REVISE-063 + REVISE-064 + REVISE-071 as a coupled self-referential-vulnerability cluster — they should be addressed together as architectural decision about the integrity of the self-awareness mechanism; (4) external-validation step before any structural framing-shift. Self-referential elevation: HIGH urgency because the mechanism producing today's output (and this very disposition) is itself implicated.

**Status:** AWAITING-REVIEW

**PROVENANCE:**
  Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

---

Total new REVISEs this run (2026-05-29): 7 (REVISE-065..071). Urgency: REVISE-065/066/071 HIGH; REVISE-067/068/069/070 MEDIUM. All status AWAITING-REVIEW per protocol.

**Fail-loud / SYSTEMIC-RISK-FLAG I continuation:** Six of seven new REVISEs join or extend existing systemic risk clusters:
- REVISE-065 (PRESUMPTION-267): 4-instance binary-framing pattern; structural-bias signal; couples to PRESUMPTION-253/259/262 family
- REVISE-066 (PRESUMPTION-269): push-gate as potential 5th FLAG-I route; constitutional rule scaling concern; couples REVISE-053
- REVISE-067 (PRESUMPTION-272): query-class coverage gap at ship-readiness; couples REVISE-061
- REVISE-068 (PRESUMPTION-270): swarm-contract mirror drift; lowest-cost remediation (symlink or hash-check)
- REVISE-069 (PRESUMPTION-274): named-trigger elastic deferral; couples PRESUMPTION-248 family
- REVISE-070 (PRESUMPTION-273): implicit scope-renegotiation; couples FLAG-I demo-path bias cluster
- REVISE-071 (PRESUMPTION-275): self-referential observation independence; HIGH self-referential elevation; clusters with REVISE-063 (honesty-layer) + REVISE-064 (atomicity) into a coherent self-awareness-mechanism-integrity architectural decision

The standing AWAITING-REVIEW backlog (REVISE-047..064 = 18) + 7 new REVISEs this run = **25 total AWAITING-REVIEW**. The response-gate remains dark per FLAG I: closed-loop-no-exit. REVISE-071 in particular completes a 3-item self-referential-vulnerability cluster (REVISE-063 + 064 + 071) at three different levels of the self-awareness mechanism; these should be addressed as a coupled architectural decision OUT-OF-BAND. OPEN-066 (single needs-Tom queue + escalation policy) remains the project's #1 item. The 5-route FLAG-I cluster (REVISE-053/056/058 + new -066/-070) now spans deployment, ingest, route-rate, push-gate, and scope-renegotiation — full closure of the closed-loop-no-exit pathology.


---

## New REVISEs — run 2026-05-30 (REVISE-072..079)

### REVISE-072 — PRESUMPTION-277
**Statement:** [inferred] The fade bug 'real' verdict generalizes from one foreground query/user/browser to the whole fade mechanism; symptom presumed code-path-bound, not render-context-bound.
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Weak) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** Unstated single-observation generalization underlies the fade verdict; render behavior is context-dependent, so the presumption is challenged with only weak support. PRESUMPTION + strong challenge -> REVISE.
**Reasoning:** Designers did not articulate that the verdict rests on N=1; the dependent decisions (254, 255) inherit the risk. Cheap, decisive remedy (multi-context reproduction) before committing.
**Recommended action:** Urgency Medium-High (gates 1.6 push). Recommended: require multi-context reproduction before treating the fade as a general code defect. Couples ASSUMPTION-253/254/255, PRESUMPTION-278.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-073 — PRESUMPTION-278
**Statement:** [inferred] The hidden-tab rAF confound is presumed isolated to that one diagnosis; remote-Chrome probes are still trusted for other visual-rendering diagnoses without re-examination.
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Weak) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** The throttling confound is a general background-tab artifact class, so presuming it isolated leaves a whole class of remote-Chrome visual diagnoses untrustworthy. PRESUMPTION + strong challenge + class-level scope -> REVISE.
**Reasoning:** A methodological tool-trust error affecting all background visual probes, not one diagnosis. SYSTEMIC-RISK candidate; needs an audit, not just monitoring.
**Recommended action:** Urgency Medium-High. Recommended: audit + re-validate remote-Chrome visual diagnoses with visibility forced / throttling disabled. Couples PRESUMPTION-277; flagged SYSTEMIC-RISK (remote-visual-probe trust).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-074 — PRESUMPTION-280
**Statement:** [inferred] Pathway 28's 'cannot drift' presumes COLORS is the only coupling surface; dir name + frontmatter are also surfaces, and the get_group -> 'root' silent fallback is an existing leak.
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Weak) | **15b:** CHALLENGED (Strong)
**Net assessment:** The single-source 'cannot drift' claim is refuted by additional coupling surfaces (dir, frontmatter) and a concrete existing silent-default leak (get_group->'root'). PRESUMPTION + strong challenge + present defect -> REVISE.
**Reasoning:** Not a future risk but a current fail-loud violation; the over-claim plus the live leak warrant design review and a cheap fix.
**Recommended action:** Urgency Medium-High. Recommended: (1) replace get_group->'root' silent fallback with a loud error; (2) derive or eliminate the dir/frontmatter surfaces. Lowest-cost remediation of the batch. Couples ASSUMPTION-259/260.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-075 — PRESUMPTION-282
**Statement:** [inferred] The handoff rail presumes the next session honors the 'read handoff first' rule and keeps the doc current; no failure mode or check is defined (success-criteria gap).
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Weak) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** The handoff rail has no defined failure mode or adherence/freshness check; literature says both rule-skip and staleness are likely. PRESUMPTION + strong challenge + success-criteria gap -> REVISE.
**Reasoning:** A self-awareness/continuity mechanism with no way to detect its own failure is exactly the kind of gap the pipeline exists to surface. Cheap to add a check.
**Recommended action:** Urgency Medium. Recommended: add freshness timestamp + staleness check + explicit resume-acknowledgement + fail-loud on skip. Couples ASSUMPTION-261; relates to self-awareness-mechanism-integrity cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-076 — PRESUMPTION-283
**Statement:** [inferred] Framing the handoff rail as 'the system practicing its own thesis' (Pathway 16 in miniature) presumes self-application is evidence for the pathway's validity -- self-referential confirmation risk.
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Moderate) | **15b:** CHALLENGED (Moderate)
**Net assessment:** Dogfooding is valid feedback but not validity evidence; framing self-application as evidence for Pathway 16 is self-referential confirmation. PRESUMPTION + self-referential elevation -> REVISE.
**Reasoning:** Joins the standing self-referential-vulnerability cluster (REVISE-063/064/071); conflating motivation with evidence is precisely the integrity risk that cluster concerns.
**Recommended action:** Urgency Medium. Recommended: label self-application as motivation, require external validation for pathway-validity claims. Joins self-awareness-mechanism-integrity cluster (REVISE-063/064/071/079).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-077 — PRESUMPTION-284
**Statement:** [inferred] [5th binary-framing instance] The interaction-model choice was offered as two clean options and resolved by preference without a usability test, subordinating the reframe/unify third category. Triggered OPEN-068.
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** The 5th instance of binary-framing elevates this from a satisficing choice to a structural decision-making bias that subordinates third options; false-dichotomy/framing literature supports the challenge. PRESUMPTION + pattern-level + strong challenge -> REVISE.
**Reasoning:** Pattern-level structural bias (couples PRESUMPTION-267 binary-framing family, triggered OPEN-068). A per-decision fix is insufficient; a standing process change is indicated.
**Recommended action:** Urgency Medium-High. Recommended: add a standing 'name and weigh a third option' step; usability-test before locking. Flagged SYSTEMIC-RISK (binary-framing pattern, 5 instances). Couples OPEN-068, PRESUMPTION-267 family.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-078 — PRESUMPTION-285
**Statement:** [inferred] '16/16 logic validation' presumes the 16 cases cover the parser's input space; coverage adequacy undefended, and the fade bug shows logic-pass != visually working.
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Weak) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** Coverage adequacy is asserted by pass count, not demonstrated; mutation-testing practice and the fade bug both challenge the presumption. PRESUMPTION + strong challenge -> REVISE.
**Reasoning:** Unstated coverage-adequacy presumption underpins the 1.6 readiness claim (ASSUMPTION-262); cheap to address with a mutation/partition check.
**Recommended action:** Urgency Medium. Recommended: run mutation testing / input-space characterization before treating 1.6 as parser-correct. Couples ASSUMPTION-262.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-079 — PRESUMPTION-286
**Statement:** [inferred] Today's demo-path day is read as 'correct prioritization, not recursion' within the same registry-and-summary apparatus that flags the 5-cycle zero-PRS streak -- closed-loop self-diagnosis bias at the prioritization layer.
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** The 'correct prioritization, not recursion' reading is produced inside the same apparatus that flags the streak; closed-loop self-diagnosis with no external check. PRESUMPTION + self-referential + strong challenge -> REVISE.
**Reasoning:** Self-referential prioritization-layer bias; joins the self-awareness-mechanism-integrity cluster (REVISE-063/064/071/076). Needs a pre-registered external criterion, not internal monitoring.
**Recommended action:** Urgency Medium-High. Recommended: pre-registered external criterion for prioritization-vs-recursion, applied outside the self-summary loop (Tom/Adaptive). Couples OPEN-067, PRESUMPTION-275 (REVISE-071); joins self-referential cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-05-30):** 8 (REVISE-072..079). All status AWAITING-REVIEW.

**SYSTEMIC-RISK flags this run:**
- REVISE-073 (PRESUMPTION-278): remote-Chrome visual-probe trust — rAF/background-tab throttling is a *general* artifact class, so a whole class of remote-Chrome visual diagnoses is suspect, not one. Recommend audit + re-validation with visibility forced / throttling disabled.
- REVISE-077 (PRESUMPTION-284): binary-framing pattern — 5th instance; structural decision-making bias subordinating third options. Couples PRESUMPTION-267 family; triggered OPEN-068. Recommend a standing "name a third option" deliberation step.

**Self-awareness-mechanism-integrity cluster extension:** REVISE-076 (PRESUMPTION-283, self-application-as-evidence) and REVISE-079 (PRESUMPTION-286, closed-loop prioritization self-diagnosis) join the standing self-referential cluster (REVISE-063 honesty-layer + REVISE-064 atomicity + REVISE-071 observation-independence). All five concern self-referential confirmation at different layers and should be addressed together as a coupled architectural decision OUT-OF-BAND with an external check (Tom/Adaptive).

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 25 (REVISE-047..071); +8 this run = **33 total AWAITING-REVIEW**. The human response-gate remains the project's #1 item (OPEN-066). Lowest-cost remediation this run: REVISE-074 (PRESUMPTION-280) — replace get_group->'root' silent fallback with a loud error.

---

## REVISE — run 2026-05-31

### REVISE-080 — PRESUMPTION-287
**Item type:** PRESUMPTION (unstated)
**15a:** NO-SUPPORT-FOUND (None) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** No literature endorses "absence of record == no event"; observability practice treats it as a defect to design out. PRESUMPTION + only-evidence-against + self-referential blind spot in the self-awareness layer's own intake.
**Reasoning:** Designers unknowingly coupled extraction completeness to intake-channel health; unsupported and actively challenged, most dangerous in the present known-down state. Cheap, fail-loud remedy.
**Recommended action:** Urgency Medium-High. Record intake-health explicitly — emit DEGRADED/UNKNOWN-completeness rather than defaulting to no-event when the scrape fails. Couples OPEN-069, PRESUMPTION-290; 2026-05-31 single-transport systemic-risk cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-081 — PRESUMPTION-289
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** Alert-fatigue research supports notification restraint, but escalation design exists precisely so a repeating unacknowledged failure changes salience — and 3 identical cycles with no resolution partly falsify "passive note is adequate."
**Reasoning:** The passive-notification presumption belongs with the standing human-response-gate flag (OPEN-066); empirically it has not closed the loop in 3 cycles. Route to Tom; design the fix to fire ONCE on repetition, not every cycle, to respect the alert-fatigue caveat.
**Recommended action:** Urgency Medium. A single repetition-triggered escalation step (raise salience / change channel once on cycle N>=2 of the same blocker), bounded to avoid fatigue. Couples OPEN-066, PRESUMPTION-240; 2026-05-31 systemic-risk cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-082 — PRESUMPTION-290
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** Streaks are legitimate only when the counted thing IS the goal; the advance-streak counts a diligence proxy, and its missing "correct not-to-advance" null is the diagnostic signature of surrogation (Goodhart). PRESUMPTION + self-referential + strong challenge.
**Reasoning:** Joins the self-referential / metric-fixation cluster with REVISE-079 (PRESUMPTION-286). On degraded-intake days the streak pressures manufacturing output over honest reporting — defeating the self-awareness goal. Cheap remedy: redefine what the streak counts.
**Recommended action:** Urgency Medium. Make an explicit "honest no-op / degraded" run a first-class state that PRESERVES the streak; count "honest accounting performed," not "items emitted." Couples PRESUMPTION-287, PRESUMPTION-286 (REVISE-079); 2026-05-31 systemic-risk cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-05-31):** 3 (REVISE-080..082). All status AWAITING-REVIEW.

**SYSTEMIC-RISK flag this run:**
- Single-transport common-mode cluster (ASSUMPTION-263 + PRESUMPTION-287/288/289, downstream 290): the whole daily-sync loop — intake, delivery, and the self-awareness layer's own intake — rides ONE claude.ai session in ONE Chrome profile. One logout disables all directions including the outage-reporting channel. Single coupled remedy: a diverse, non-Chrome degraded-mode path that records intake-health (DEGRADED/UNKNOWN, not no-event) AND carries an escalation signal surviving a claude.ai logout. Couples OPEN-066 (project #1), OPEN-069.

**Self-referential / metric-fixation cluster extension:** REVISE-082 (PRESUMPTION-290, surrogated advance-streak) joins REVISE-079 (PRESUMPTION-286, closed-loop prioritization self-diagnosis) and the standing self-referential cluster (REVISE-063/064/071/076). All concern the self-awareness apparatus self-justifying; address OUT-OF-BAND with an external check.

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 33 (REVISE-047..079); +3 this run = **36 total AWAITING-REVIEW**. The human response-gate remains the project's #1 item (OPEN-066), and REVISE-081 is now coupled directly to it. Lowest-cost remediation this run: REVISE-082 (PRESUMPTION-290) — redefine the streak to count honest accounting, preserving cadence without the surrogation pull.

---

## REVISE — run 2026-06-02

### REVISE-083 — PRESUMPTION-291
**Item type:** PRESUMPTION (unstated)
**15a:** SUPPORTED (Moderate) | **15b:** PARTIALLY-CHALLENGED (Weak-Moderate)
**Net assessment:** Textbook event-time vs processing-time confusion: narrating the latest on-disk batch as "today's" conflates when an artifact was produced with when it was read. The echo was empirically realized (2026-05-30's self-awareness + lit-search batches narrated as 2026-05-31's). The YAGNI/low-stakes defense is real but bounded, and weakens sharply here because the mislabelled artifact IS the self-awareness layer's own honesty/accounting output.
**Reasoning:** PRESUMPTION + self-referential + active mis-reporting (not hypothetical) + the layer mis-dating its own record defeats its purpose and masks the underlying intake outage. The honest-reporting stakes outweigh the over-engineering objection; the remedy is cheap (no full stream-processing machinery needed).
**Recommended action:** Urgency Medium-High. Stamp each batch with its event-date and have the EOD summary emit a dated DELTA — e.g., "no new items produced today; latest on disk is 2026-05-30" — rather than echoing latest-on-disk as today's. Idempotent dated-delta reporting. Couples PRESUMPTION-287 (REVISE-080, intake-health DEGRADED/UNKNOWN), PRESUMPTION-290 (REVISE-082, honest no-op state); 2026-06-02 degraded-session / no-independent-vantage cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-084 — PRESUMPTION-293
**Item type:** PRESUMPTION (unstated)
**15a:** SUPPORTED (Strong) | **15b:** PARTIALLY-CHALLENGED (Weak-Moderate)
**Net assessment:** The Knight-Leveson result and common-mode-failure literature strongly ground the concern: independence of a checker from the checked system cannot be assumed and is frequently violated. A "clean reload" performed inside the same Chrome/claude.ai regime whose lag/batching/throttling it adjudicates is a same-regime (common-mode) verifier. 15b's only valid pushback is against the absolutist reading — independence is CONSTRUCTIBLE (out-of-band), not impossible — which sharpens rather than refutes the remedy.
**Reasoning:** PRESUMPTION + strong support + directly undercuts the SUFFICIENCY of ASSUMPTION-264's in-band re-verification (the part deliberately excluded from PREMISE-045). Designers were unaware they were assuming a fault-free vantage point. The correct conclusion is "make the verifier out-of-band," not "abandon verification."
**Recommended action:** Urgency Medium. Require the re-verification path to be OUT-OF-BAND relative to the degraded mechanism (a different transport/process, or a provably-foregrounded/fresh process that exits rAF/background-tab throttling); treat in-band-only re-checks as "unknown," never "verified." Characterize the degraded regime's mechanism to confirm independence. Couples ASSUMPTION-264 (PREMISE-045 sufficiency gap), REVISE-073 / PRESUMPTION-278 (rAF throttling), PRESUMPTION-288 (single-transport SPOF, MONITOR-289).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-02):** 2 (REVISE-083..084). All status AWAITING-REVIEW.

**SYSTEMIC-RISK flag this run:**
- No-independent-vantage / degraded-session common-mode cluster (ASSUMPTION-264 + PRESUMPTION-291/292/293): verification, dated self-reporting, and the honesty layer's enforcement all execute INSIDE the same degraded regime they are meant to police. 264's re-verification can share the fault (293); the EOD summary mis-dates from stale latest-on-disk (291); fail-loud is a behavioral norm with no engineered interlock (292). This is the same common-mode root as the 2026-05-31 single-transport cluster (PRESUMPTION-288/MONITOR-289), now reaching the verification/honesty layer itself. Single coupled remedy: establish an OUT-OF-BAND vantage point — a path (transport/process) that does not share the degraded regime's failure mode — used for re-verification, intake-health, and dated-delta reporting. Couples REVISE-080, OPEN-066 (project #1), OPEN-069.

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 36 (REVISE-047..082); +2 this run = **38 total AWAITING-REVIEW**. Lowest-cost remediation this run: REVISE-083 (PRESUMPTION-291) — stamp batches with event-date and emit a dated delta; small change, removes active self-referential mis-reporting.

---

## REVISE — run 2026-06-02 (batch 2: 2026-06-02 EOD self-awareness batch)

### REVISE-085 — PRESUMPTION-294
**Item type:** PRESUMPTION (unstated)
**15a:** SUPPORTED (Strong, silent-failure core; rider NO-SUPPORT) | **15b:** PARTIALLY-CHALLENGED (Weak-Moderate core; rider STRONGLY challenged)
**Net assessment:** Two-part item. (a) "git no-error == changes staged" is a textbook safety-vs-liveness / unverified-side-effect failure, empirically realized over ~4 days — well-grounded as a real defect (its verify-don't-infer remedy is now PREMISE-046). (b) The RIDER — "clearing the lock today restores correctness for the lock-window days" — finds NO support and is challenged STRONGLY: lock removal is forward-only and not idempotent over the missed window, so the ~4 days of silently-skipped staging are NOT retroactively committed.
**Reasoning:** The core is incorporated as the stated twin (PREMISE-046); what REQUIRES design action is the false recovery rider — it would leave the system believing the 4-day window is healed when those changes remain untracked, layering a second silent integrity gap on the first. PRESUMPTION + self-referential + actively-wrong rider -> REVISE.
**Recommended action:** Urgency Medium-High. After clearing the stale lock, do NOT assume history healed: explicitly diff the working tree against the last confirmed-staged commit for the lock window (2026-05-29 → 2026-06-02), re-stage/commit the skipped changes, and verify via read-after-write. Add a stale-lock pre-flight check (couples PREMISE-046/ASSUMPTION-265). Couples OPEN-071; 2026-06-02 absence!=success cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-02, both batches):** 3 (REVISE-083, REVISE-084, REVISE-085). All status AWAITING-REVIEW.

**SYSTEMIC-RISK flag (batch 2, extends the 2026-06-02 cluster):**
- Absence != success/event common-mode (ASSUMPTION-265 + PRESUMPTION-294/296, and prior 264/291/292/293): the system repeatedly infers a positive state from a NULL signal it never verified out-of-band — "no git error" == staged (294/265), "no decision email" == no decision (296), "no readable transcript" == no session (287), an in-band reload == verified (264/293). All are the same root: no fault-independent confirmation that the intended effect/event actually occurred. Single coupled remedy as flagged in batch 1: an OUT-OF-BAND vantage point plus explicit verify-the-effect checks (PREMISE-045/046) so a null is recorded as UNKNOWN, never as a confirmed positive. Couples REVISE-080, OPEN-066 (project #1), OPEN-069, OPEN-071.

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 36 (REVISE-047..082); +3 this run (REVISE-083..085) = **39 total AWAITING-REVIEW**. Lowest-cost remediation this run: REVISE-083 (event-date stamp + dated delta) and the lock-window reconciliation half of REVISE-085 (one-time recovery diff).

---

## REVISE — run 2026-06-03 (2026-06-02 evening Sociogram batch)

### REVISE-086 — ASSUMPTION-267
**Item type:** ASSUMPTION (stated)
**15a:** PARTIALLY-SUPPORTED (Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**Net assessment:** Two-part claim (Rule 7 — surfaced, not blended). (a) "Raise the cap above the 2529-node graph with headroom" is CORRECT and kept — the old 2000 cap truncated real data, a genuine defect now fixed. (b) "20000 is a SAFE ceiling" is challenged moderate-strong with only weak support: browser D3/SVG force-directed layouts degrade non-linearly well below 20000 (cliffs near ~1000+ nodes), so the cap likely sits ABOVE real render capacity and can silently re-admit the crash it exists to prevent. The safe limit was never measured — set to a round 10x, validated only at 2529.
**Reasoning:** Weak support + moderate-strong challenge on the load-bearing sub-claim -> REVISE. The truncation fix stands; the untested ceiling needs Tom's review. A cheap, concrete measurement resolves it.
**Recommended action:** Urgency MEDIUM. Measure the render cliff for this build (sweep ~3k/5k/8k/12k/16k/20k nodes; record frame time, interaction latency, memory) and set MAX_NODES below the first cliff; OR move the renderer to canvas/WebGL for a genuinely high safe ceiling. Until measured, label 20000 a provisional, explicitly-untested guard and re-anchor the 80%-of-cap warning to the measured cliff. Couples PRESUMPTION-299 (MONITOR-295, same measurement), ASSUMPTION-267 truncation-fix (kept).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-03):** 1 (REVISE-086). Status AWAITING-REVIEW.

**SYSTEMIC-RISK flag (2026-06-03 — human-memory-as-control, High):**
- Human-memory-as-control cluster (ASSUMPTION-266/268, PRESUMPTION-297): each relies on a manual, memory-dependent convention as the control of record — "use explicit git paths" (266), "do a live foreground review" (268), "remember the cross-repo handoff" (297) — rather than an enforced forcing function. On an autonomous, human-absent run these are exactly the controls most likely to be silently skipped, re-admitting the failure they prevent. This is the human-vantage twin of the 2026-06-02 "absence != success/event" cluster. Single coupled remedy: convert each to a cheap pre-push forcing function (generated/checked explicit-path set + new-file-omission check; automated served-browser assertions with a BLOCKING human sign-off; a pre-push dependent-repo-clean check). Couples PREMISE-045/046/047/048, MONITOR-293, OPEN-071/072.
- Secondary cluster (untested ceiling from current load): ASSUMPTION-267 (this REVISE) + PRESUMPTION-299 (MONITOR-295), cousin PRESUMPTION-298 (MONITOR-294) — a limit/verification asserted "safe/correct" from a single current-load data point. Remedy: measure before asserting (render-cliff sweep; read the fade code path).

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 39 (REVISE-047..085); +1 this run (REVISE-086) = **40 total AWAITING-REVIEW**. Lowest-cost remediation this run: the REVISE-086 render-cliff sweep (one-time measurement that also discharges MONITOR-295).

---

## REVISE flags — run 2026-06-04 (2026-06-03 EOD self-awareness batch)

**Total new REVISEs this run (2026-06-04): 0.** All 5 items dispositioned INCORPORATE (1: PREMISE-049) or MONITOR (4: MONITOR-296..299); none reached the REVISE bar. The closest call was ASSUMPTION-270 (MONITOR-296): its load-bearing "attended-only / cannot self-clear" clause is challenged Moderate-Strong, but the proposed fix (a standing delegated credential) carries a real attack-surface downside flagged by 15a's own least-privilege literature, so it is genuinely contested -> MONITOR, not REVISE. It will escalate to REVISE if lapsed-session blocks recur (trip-wire recorded in MONITOR-296).

**SYSTEMIC-RISK flag (2026-06-04 — autonomous-sync silent-degradation, High):**
- Cluster: ASSUMPTION-270 (MONITOR-296) + PRESUMPTION-300 (MONITOR-297). Common vulnerability: the unattended sync path degrades SILENTLY at both ends of the same failure — it neither self-clears a lapsed claude.ai session (treats it as a hard external blocker) nor fails loud on a confirmed-down channel (runs the full workflow and accumulates undeliverable state). On a human-absent run these are exactly the controls that should fail loud or self-recover, and instead do neither. This is the availability twin of the 2026-06-03 "human-memory-as-control" cluster (ASSUMPTION-266/268, PRESUMPTION-297) and the 2026-06-02 "absence != success/event" cluster — the same family expressed in the autonomous sync/auth path.
- Literature basis: circuit-breaker / fail-fast / dead-letter (Nygard; Azure Architecture Center; SQS DLQ); OAuth client-credentials / refresh / workload-identity federation for unattended self-recovery (Scalekit, Auth0, Microsoft Entra); graceful degradation with durable store-and-forward (Azure/SRE graceful-degradation guides).
- Risk level: High (it has already produced realized harm — the 06-03 hard block + accumulated undeliverable state).
- Single coupled remedy: make the sync path BOTH self-clearable AND fail-loud — (a) provision a sync-scoped, least-privilege, revocable delegated credential (a service identity, never Tom's) so a lapsed session self-recovers unattended; (b) route undeliverable items to a durable, replayable dead-letter with a visible escalation on confirmed-down and auto-drain on recovery. Couples PREMISE-049, MONITOR-296/297, OPEN-069/073, SYSTEMIC-RISK 2026-06-02/2026-06-03.

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 40 (REVISE-047..086); +0 this run = **40 total AWAITING-REVIEW** (unchanged). Lowest-cost standing remediation remains the REVISE-086 render-cliff sweep (one-time measurement that also discharges MONITOR-295). No new human-review debt added this run.

---

## REVISE flags — run 2026-06-05 (2026-06-04 EOD self-awareness batch)

### REVISE-087 — PRESUMPTION-304
**Statement:** [inferred] The 36-vs-152 PROCESSED_LOG conflict is presumed a cosmetic format artifact resolvable by a later tidy — presuming 36 is correct and 152 carries no lost data, i.e., a narrative log can double as a machine-diffable system-of-record once cleaned.
**Item type:** PRESUMPTION (unstated)
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**Net:** As the inferred twin of ASSUMPTION-271, this adds two unexamined bets on top of 271's mechanism: (1) a DIRECTIONAL bet that 36 is correct and 152 carries nothing real, and (2) a DEFERRAL bet that the reconciling "tidy" is cheap and will happen. 15a supports only feasibility (a heterogeneous log CAN become machine-diffable; a divergence CAN be a projection artifact) — not the optimistic direction. 15b names bet (1) as the canonical silent-data-loss antipattern ("assume the smaller count is canonical") and bet (2) as systematically cost-understating (deferred reconciliation reliably costs more or never happens).
**Reasoning:** Weak feasibility-only support + moderate-strong challenge on the two load-bearing bets, and it is a PRESUMPTION (designers were unaware they made the directional+deferral commitments, so they had no deliberate scrutiny) -> REVISE. The honest status is unknown-until-reconciled; "cosmetic, fix later" pre-decides the audit.
**Recommended action:** Urgency MEDIUM-HIGH. Demote the presumption from "cosmetic" to "unverified" and run the reconciliation NOW rather than deferring it: partition the 152, classify every non-36 entry, and require the audit to either confirm residual = 36 or enumerate the lost/un-ingested items. Treat "narrative log as machine-diffable system-of-record" as a goal requiring an explicit structuring pass, not a property the log already has. This single one-time audit also discharges MONITOR-300 (ASSUMPTION-271). Couples ASSUMPTION-271 (MONITOR-300), ASSUMPTION-272 (PREMISE-050), and the defer-and-tidy-later SYSTEMIC-RISK.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-088 — PRESUMPTION-305
**Statement:** [inferred] Accumulating uncommitted working-tree state is cost-free — 587 changes (up from 476) on feature/sociogram-search-integration, each unattended run adding to the pile under the no-blind-push rule, presuming a future attended session cleanly separates and commits them.
**Item type:** PRESUMPTION (unstated)
**15a:** NO-SUPPORT-FOUND (Weak) | **15b:** CHALLENGED (Strong)
**Net:** 15a found essentially no FOR case — the only honest supportive fragment (deferring the PUSH under no-blind-push) defends a DIFFERENT action than the one presumed (letting the uncommitted working tree grow). 15b is strong and convergent: version-control and lean literature treat unmerged/uncommitted divergence as holding cost that grows with size and time (harder merges, conflict risk, technical debt, decayed rationale), and the "future session cleanly separates 587 changes" bet is exactly the merge-hell failure — separability degrades as the pile grows.
**Reasoning:** No support + strong challenge on a PRESUMPTION (unexamined "cost-free" default), with realized, monotonically-growing exposure (587 and rising) -> REVISE, the clearest REVISE of this run. The no-blind-push rule (sound) is being mis-applied to justify not COMMITTING rather than merely not PUSHING.
**Recommended action:** Urgency HIGH. Decouple the two conflated actions: KEEP the no-blind-PUSH safety rule, but COMMIT frequently in small, scoped, local commits each run (committing is not pushing). This bounds working-tree growth, preserves per-change rationale, and turns the eventual attended push into a review of coherent commits instead of a 587-change untangling. Add the working-tree change count as a tracked, surfaced metric so the silent accrual is visible each run. Couples ASSUMPTION-272 (PREMISE-050, commit-in-increments), PRESUMPTION-295/301, and the defer-and-tidy-later SYSTEMIC-RISK.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-05):** 2 (REVISE-087, REVISE-088). Status AWAITING-REVIEW.

**SYSTEMIC-RISK flag (2026-06-05 — defer-and-tidy-later, High):**
- Cluster: PRESUMPTION-303 (MONITOR-301) + PRESUMPTION-304 (REVISE-087) + PRESUMPTION-305 (REVISE-088), coupled with ASSUMPTION-271 (MONITOR-300). Common vulnerability: a shared optimism that a future attended session will cleanly resolve accumulated, unverified, or intermingled state at no extra cost — admit-now/review-later (303), reconcile-later (304), commit-later (305). Each presumes deferral is free; the literature independently shows deferral cost grows with accumulation and the cleanup sometimes never happens. This is the deferral-family expressed across the intake queue, the ingest log, and the git working tree — a cousin of the 2026-06-04 "autonomous-sync silent-degradation" and 2026-06-03 "human-memory-as-control" clusters (all are silent accrual on human-absent runs).
- Literature basis: staging-queue rot / backlog inflation / inertia-promotion (Agile Alliance backlog refinement; IBM & Metaplane data-quality; maintenance-backlog cost-inflation 15-30%); ETL reconciliation / silent-data-loss (dbseer; Monte Carlo; Integrate.io); trunk-based-development merge-hell & lean WIP-as-inventory (Atlassian; StxNext; trunkbaseddevelopment.com; SAFe Principle #6).
- Risk level: High (PRESUMPTION-305 already shows realized, growing exposure — 587 uncommitted changes and rising every run).
- Single coupled remedy: treat "later attended cleanup" as a cost-bearing liability that accrues every unattended run, not a free option, and adopt bounded-accumulation defaults system-wide — enforced provisional-item adjudication deadlines with purge-not-promote default (303), reconcile counts at detection rather than deferral (304/271), commit-in-increments while deferring only the push (305) — and surface backlog/queue/working-tree size as tracked metrics so the silent accrual becomes visible. Couples PREMISE-049/050, MONITOR-300/301, REVISE-087/088.

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 40 (REVISE-047..086); +2 this run (REVISE-087, REVISE-088) = **42 total AWAITING-REVIEW**. Lowest-cost remediation this run: the REVISE-087 PROCESSED_LOG reconciliation (one-time audit that also discharges MONITOR-300) and the REVISE-088 commit-in-increments change (bounds a growing liability at near-zero cost).

## REVISE — run 2026-06-06 (2026-06-05 ATTENDED Community Explorer P1 batch)

### REVISE-089 — PRESUMPTION-306
**Statement:** [inferred] "Two verbs over one dataset" presumes the curated graph (156, CC-001…) and the cards directory (855, C0001…) are unifiable, despite measured near-total disjointness (0 id / 3 name / 5 host matches). P3 rests on a join that may be very sparse.
**Item type:** PRESUMPTION (unstated) | Risk if wrong: HIGH
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Strong)
**Net:** Entity-resolution establishes only that a join is not impossible; the measured 0/3/5 overlap across 156×855 is near the recoverable-signal floor, where linkage theory (Fellegi-Sunter; Christen) says forcing a join manufactures false matches and the parsimonious reading is that the two sets describe largely DISTINCT populations. P3's entire "two projections / one dataset" architecture rests on this join.
**Reasoning:** Weak feasibility-only support + strong challenge on a HIGH-risk PRESUMPTION whose failure invalidates P3 -> REVISE (clearest of the run). Designers were unaware they were betting on unifiability. "Unifiable" pre-decides the linkage experiment; the honest status is unknown-until-measured.
**Recommended action:** Urgency HIGH. BEFORE building any more of P3: run the actual record-linkage pass (e.g., Splink / Fellegi-Sunter over name+host+fuzzy fields), report estimated true matches with precision/recall against a shuffled-null baseline, and pre-register the minimum join density P3 requires. If density is below threshold, treat the two as DISTINCT populations that ASSOCIATE via a link table rather than unify (resolves with PRESUMPTION-311 / MONITOR-307), and revisit ASSUMPTION-275's "one dataset" framing (PREMISE-051 scope note). Couples PRESUMPTION-309 (REVISE-090), 311 (MONITOR-307), ASSUMPTION-275/276.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-090 — PRESUMPTION-309
**Statement:** [inferred] P1 pieces (shared pipeline, id-keyed hand-offs) are presumed "load-bearing in P3 later" — forward-compatibility presumed for an architecture whose central join is unbuilt and newly doubted; one named load-bearing piece (id-keyed hand-off) was already deferred this session. No P3 failure criterion stated.
**Item type:** PRESUMPTION (unstated) | Risk if wrong: MEDIUM-HIGH
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Strong)
**Net:** Evolutionary-architecture (Ford et al.; Martin) endorses building seams that pay forward ONLY when the later need is reasonably known — a condition unmet here: P3's central join is unbuilt AND doubted (306), no P3 failure criterion exists, and a named load-bearing piece was already deferred this session (the forward-compat bet already slipping). Strong YAGNI / speculative-generality challenge (Fowler).
**Reasoning:** Weak conditional support + strong challenge on a Medium-High-risk PRESUMPTION with realized slippage -> REVISE. The right time to build the P3 seam is when P3 is committed and its join validated, not before.
**Recommended action:** Urgency MEDIUM-HIGH. Apply YAGNI's own test ("we know we need this" vs "we might"): defer P3-shaped seams until the 306 linkage result commits P3; state an explicit P3 validate/kill criterion tied to that result; track deferred "load-bearing" pieces as a visible liability (the already-deferred id-keyed hand-off is item #1). Couples PRESUMPTION-306 (REVISE-089), ASSUMPTION-276 (MONITOR-303).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-06):** 2 (REVISE-089, REVISE-090). Status AWAITING-REVIEW.

**SYSTEMIC-RISK flag (2026-06-06 — unvalidated-P3-join-as-foundation, High):**
- Cluster: PRESUMPTION-306 (feasibility, REVISE-089) + PRESUMPTION-309 (forward-compat seams, REVISE-090) + PRESUMPTION-311 (conceptual appropriateness, MONITOR-307), coupling ASSUMPTION-275 (PREMISE-051) and ASSUMPTION-276 (MONITOR-303). Common vulnerability: the entire P3 "one app, two projections over one dataset" architecture rests on a curated↔directory join that is simultaneously (a) empirically near-absent — 0 id / 3 name / 5 host across 156×855, and (b) conceptually unexamined — whether the two record sets are the same kind of object (identity) or merely related (association) was never raised. The system is building toward, and reasoning as if, a join exists that has neither been measured nor conceptually justified.
- Literature basis: record-linkage signal floor & false-match inflation at low overlap (Fellegi-Sunter; Christen "Data Matching"; Data Ladder); YAGNI / speculative generality (Fowler; Refactoring); identity-vs-association modeling error & over-merge caution (Chen ER model; Bowker & Star "Sorting Things Out"; MDM golden-record practice).
- Risk level: High (the join is load-bearing for the whole CE target architecture, yet unmeasured and unjustified; continued P1 build accrues speculative structure under it — a structural cousin of the prior "defer-and-tidy-later" deferral-family clusters).
- Single coupled remedy: run the record-linkage experiment FIRST (REVISE-089), gate all further P3 build on its result, and make the identity-vs-association decision explicitly before committing an id space (MONITOR-307). One experiment + one modeling decision discharges most of the cluster.

**Secondary note (2026-06-06 — validity-smuggled-into-a-technical-gate, Medium):** PRESUMPTION-308 (normative: articulation-gated visibility, MONITOR-305 HIGH) + PRESUMPTION-310 (construct: TF-IDF lexical similarity as relatedness, MONITOR-306). Common pattern: a value choice (who deserves visibility) or a measurement assumption (lexical overlap = relatedness) is embedded in a step presented as technically neutral. Remedy: surface each assumption explicitly — route the visibility-policy value choice to Tom (308); re-test edges with semantic embeddings before reading near-zero cross-links as relational signal (310).

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 42 (REVISE-047..088); +2 this run (REVISE-089, REVISE-090) = **44 total AWAITING-REVIEW**. Lowest-cost, highest-leverage remediation this run: the REVISE-089 record-linkage experiment — a single measurement that also gates REVISE-090 (defer seams) and MONITOR-303/307 (P3 target + entity model), discharging most of the new SYSTEMIC-RISK cluster at once.

## REVISE — run 2026-06-07 (2026-06-06 EOD attended CE build batch)

### REVISE-091 — PRESUMPTION-312
**Statement:** [inferred] Assigning shared CC-xxx ids presumes that sharing an id key constitutes genuine entity identity rather than asserting a link by fiat; the merge may have manufactured the identity that 2026-06-05 found missing (disjoint id spaces: 0 id / 3 name / 5 host) rather than discovering it.
**Item type:** PRESUMPTION (unstated) | Risk if wrong: HIGH
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Strong)
**Net:** Across entity-resolution (Fellegi-Sunter), relational modeling (Chen ER), and MDM golden-record practice, identity is INFERRED from evidence and EXPRESSED by a key — never CREATED by one. Minting shared ids in the near-zero-overlap regime is the canonical false-match / over-merge error; the merge answers "same entity?" with "they are now."
**Reasoning:** Weak conditional support + strong challenge on a HIGH-risk PRESUMPTION that is ALREADY ENACTED (ids minted) → REVISE, the clearest of the run. PRESUMPTION weight applies (designers were unaware they were betting identity on a key).
**Recommended action:** Urgency HIGH. Run the record-linkage experiment FIRST on attributes OTHER than the freshly-minted id (this is the same measurement as prior REVISE-089); gate any P3 build / cross-navigation / "one dataset" reasoning on its result. If overlap stays near the signal floor: downgrade CC-xxx to an ASSERTED (not evidenced) link, model curated↔directory as association via a link table, and unwind/avoid committing the shared id space. Make the identity-vs-association decision explicit before further dependence (couples MONITOR-308, prior MONITOR-307).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-092 — PRESUMPTION-313
**Statement:** [inferred] Disclosing the no-consent / public-seed status presumes in-product disclosure discharges the ethical obligation of listing communities without consent (transparency cures the consent gap); the don't-list / opt-in alternatives were never raised.
**Item type:** PRESUMPTION (unstated) | Risk if wrong: MEDIUM-HIGH (ethics / reputational / group-harm)
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Strong)
**Net:** Notice can be proportionate for low-sensitivity public data, but consent theory (Solove, "Privacy Self-Management and the Consent Dilemma," 2013) and group-privacy work (Taylor/Floridi/van der Sloot 2017) hold that disclosure does NOT discharge consent for IDENTIFIABLE groups — which these communities are. The structural flaw is a collapsed option space: opt-in / don't-list were never on the table.
**Reasoning:** Weak support + strong challenge on a HIGH-risk ethics PRESUMPTION that is already enacted (communities listed without consent) → REVISE. Pairs with ASSUMPTION-280 / PREMISE-052: disclosure is the necessary FLOOR (INCORPORATED), disclosure-is-sufficient is the overclaim (this REVISE).
**Recommended action:** Urgency HIGH. Reopen the option space explicitly (don't-list / opt-in / opt-out / disclose-only) and decide per sensitivity tier with Tom; add at minimum an opt-out/takedown path (opt-in for higher-sensitivity communities); document a don't-list criterion; treat group privacy at the community level, not via individual-style notice. Keep PREMISE-052 (disclose + non-endorsement) as the floor.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-07):** 2 (REVISE-091, REVISE-092). Status AWAITING-REVIEW.

**SYSTEMIC-RISK flag (2026-06-07 — manufactured-identity-as-foundation, HIGH):**
- Cluster: ASSUMPTION-278 (merge-by-shared-id, MONITOR-308) + PRESUMPTION-312 (id-as-identity-by-fiat, REVISE-091), escalating the prior "unvalidated-P3-join-as-foundation" cluster (PRESUMPTION-306 → REVISE-089; PRESUMPTION-311 → MONITOR-307; ASSUMPTION-275/276). Common vulnerability: the 2026-06-05 measurement found the curated↔directory join empirically near-absent (0 id / 3 name / 5 host across 156×855) and conceptually unexamined (identity vs association never raised). The 2026-06-06 build "resolved" this not by MEASURING the join but by ASSIGNING shared CC-xxx ids — manufacturing the identity by fiat. The risk has therefore escalated from "join unbuilt and doubted" to "join asserted and now load-bearing," which is harder to reverse.
- Literature basis: entity-resolution / false-match at low overlap (Fellegi-Sunter; Christen "Data Matching"); identity-vs-association modeling error & over-merge caution (Chen ER model; Bowker & Star "Sorting Things Out"; MDM golden-record practice).
- Risk level: HIGH (a manufactured identity underlies cross-navigation, "one dataset / two projections," and any P3 promotion; committed id spaces are expensive to split, and derived artifacts inherit the error).
- Single coupled remedy: run the record-linkage experiment FIRST on non-minted attributes (discharges REVISE-089 and REVISE-091 at once); gate all further dependence on its result; if overlap stays near zero, downgrade CC-xxx to asserted links and model as association (MONITOR-308 / MONITOR-307). One measurement + one explicit modeling decision discharges most of the cluster.

**SYSTEMIC-RISK flag (2026-06-07 — consent-gap-papered-by-disclosure, MEDIUM-HIGH, ethics):**
- Cluster: ASSUMPTION-280 (in-product disclosure, INCORPORATE → PREMISE-052, the defensible floor) vs PRESUMPTION-313 (disclosure-discharges-consent, REVISE-092, the overclaim); reinforced by PRESUMPTION-314 (curator-produced "quality bar," MONITOR-310) and PRESUMPTION-316 (visibility-as-earned-status stigma, MONITOR-312). Common vulnerability: identifiable communities are listed (and implicitly ranked by graph-visibility) from scraped public pages without consent, with transparency treated as ethical closure and the stronger alternatives (opt-in / don't-list) never raised.
- Literature basis: notice-vs-consent critique (Solove 2013); web-scraping ethics for identifiable groups (Brown et al. 2025; AoIR); group privacy (Taylor/Floridi/van der Sloot 2017); construct validity / criterion contamination (Messick); status-tier stigma & participation inequality (Nielsen 90-9-1; visibility-as-power, Bowker & Star).
- Risk level: MEDIUM-HIGH (group-level harm + reputational/ethical liability for the project and for Tom/Notre Dame; biases the very evidence-about-traditions the system aims to produce toward visibility over merit).
- Single coupled remedy: route the listing-ethics + visibility-value decisions to Tom as one bundle — reopen the consent option space (REVISE-092), relabel the "quality bar" honestly (MONITOR-310), and present graph membership as a data-coverage state rather than a merit badge (MONITOR-312). PREMISE-052 (disclose + non-endorsement) stands as the floor underneath whatever Tom decides.

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 44 (REVISE-047..090); +2 this run (REVISE-091, REVISE-092) = **46 total AWAITING-REVIEW**. Lowest-cost, highest-leverage remediation this run: the REVISE-091 record-linkage experiment — the SAME single measurement as the still-open REVISE-089, which now also gates MONITOR-308 and the whole manufactured-identity cluster. One measurement discharges two REVISEs and two MONITORs.

---

## REVISE — run 2026-06-08 (2026-06-07 PRS-connectome EOD batch)

### REVISE-093 — PRESUMPTION-317
**Statement:** [inferred] The prior task design presumed execution-context uniformity — that scheduled tasks inherit the attended Cowork environment's capabilities (push, $HOME, writable .git).
**Item type:** PRESUMPTION (unstated) | Risk if wrong: HIGH (unattended automation fails, possibly silently; the auto-publish design rests on a capability the runtime may lack)
**15a:** NO-SUPPORT-FOUND (Weak/conditional only) | **15b:** CHALLENGED (Strong)
**Net:** Execution-context uniformity is contradicted by one of the most established lessons in operations: interactive and scheduled/non-interactive contexts differ in environment and credentials as a rule ("works on my machine"; "works interactively, fails in cron"), and least-privilege design (Saltzer & Schroeder) deliberately scopes automated identities DOWN. The presumption is the textbook environment-mismatch anti-pattern and it is already ENACTED — the 2026-06-07 scheduled task could not push.
**Reasoning:** No support + strong challenge on a HIGH-risk PRESUMPTION already enacted and failed unattended → REVISE, the clearest of the run. PRESUMPTION weight applies (designers were unaware they were betting on inherited capabilities). Core of the environment-capability-mismatch SYSTEMIC-RISK.
**Recommended action:** Urgency HIGH. CAPABILITY-DISCOVERY-FIRST: before any scheduled task depends on push/$HOME/writable-.git, run a capability-probe task in the SCHEDULED context and diff its environment/credentials against the attended session; design tasks for the LEAST-capable context or engineer explicit parity (same image/credentials); make missing-capability failures loud and early. Couples PRESUMPTION-318 (MONITOR-314, the build-then-discover cause) and PRESUMPTION-320 (MONITOR-315).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-094 — PRESUMPTION-319
**Statement:** [inferred] The data/code guard presumes PRS-data regeneration is deterministic/safe enough to publish unreviewed (data treated as review-exempt).
**Item type:** PRESUMPTION (unstated) | Risk if wrong: MEDIUM-HIGH (a wrong-but-well-formed datum auto-publishes as fact and propagates to every derived artifact, undetected)
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate; only with automated gates) | **15b:** CHALLENGED (Strong)
**Net:** Both halves are challenged: determinism is asserted, not verified (real pipelines drift via ordering/dedup/input change), and an unreviewed data path is the quietest, most-propagating failure surface (Sculley et al. 2015 — data deps cost more than code; data-downtime literature). Support exists only if automated data-quality gates REPLACE the human, which the design did not provide. The manufactured-identity case (REVISE-091) is a concrete wrong-but-well-formed datum such a path would publish.
**Reasoning:** Weak conditional support + strong challenge on a PRESUMPTION already enacted in the auto-publish split (ASSUMPTION-284) → REVISE. PRESUMPTION weight applies (the review-exemption was never deliberately decided). Honest status: unverified-determinism + unguarded-data-path. Pairs ASSUMPTION-284 (floor, MONITOR-313) with this overclaim.
**Recommended action:** Urgency MEDIUM-HIGH. Before any unreviewed data publish: (1) VERIFY generator determinism empirically (re-run on identical inputs, diff); (2) add AUTOMATED data-quality/anomaly gates (schema + invariants + referential checks + diff-magnitude thresholds) to stand in for the absent human; (3) bound auto-publish to small diffs and escalate large/anomalous diffs to human review; (4) record per-run data diffs so regressions are observable. Secondary "derived-data-review-exempt" SYSTEMIC cluster with MONITOR-313.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-08):** 2 (REVISE-093, REVISE-094). Status AWAITING-REVIEW.

**SYSTEMIC-RISK flag (2026-06-08 — environment-capability-mismatch / build-before-probe, HIGH):**
- Cluster: PRESUMPTION-317 (execution-context-uniformity bet, REVISE-093) + PRESUMPTION-318 (build-then-discover ordering, MONITOR-314) + PRESUMPTION-320 (blind state-mutating shell blocks on a mismodeled repo state, MONITOR-315). Common vulnerability: the agent scripted state-mutating automation (auto-push; blind compound shell blocks) against a PRESUMED-uniform execution context and a PRESUMED-known repo state, without probing actual capabilities/state first. The 2026-06-07 incident (scheduled task could not push) is the realized instance; 318 is its procedural cause; 320 is the same mismodeling applied to repo state instead of environment.
- Literature basis: dev/prod parity & "works on my machine" / cron-env differences (12factor Factor X); least-privilege batch identities (Saltzer & Schroeder 1975); walking-skeleton/spike & fail-fast/shift-left & pre-mortem (Cockburn; Freeman & Pryce; Klein 2007); idempotency / make-retries-safe (AWS Builders' Library); declarative convergence (Ansible/Terraform). Also the project's own Rules 1 and 8.
- Risk level: HIGH (unattended automation that fails — possibly silently — at the worst time; a mid-sequence shell failure can strand the user's repo in an unknown partial state; the whole auto-publish design rests on a capability the runtime may lack).
- Single coupled remedy: CAPABILITY-AND-STATE-PROBE FIRST — dry-run / capability probe in the target (scheduled) context before building or handing off any automation, and inspect repo state before mutating it; make each step safe-to-fail (idempotent, reversible, halt-on-surprise). One probe-first discipline discharges most of the cluster (REVISE-093 + MONITOR-314 + MONITOR-315). This also operationalizes PREMISE-054's coincidence-case warning (a probe-first "policy" rule that shadows the hard push-credential wall is effectively non-waivable).

**SYSTEMIC-RISK flag (2026-06-08 — derived-data-treated-as-review-exempt, MEDIUM-HIGH):**
- Cluster: ASSUMPTION-284 (auto-publish-data / gate-code split, MONITOR-313, the asymmetry floor) vs PRESUMPTION-319 (data-review-exempt overclaim, REVISE-094, the ceiling). Common vulnerability: the auto-publish design treats regenerated data as the safe class on unverified determinism and with NO check (human or automated) on the data path — the quietest, most-propagating failure surface — for a system whose OUTPUT is evidence-about-traditions. Couples the manufactured-identity risk (REVISE-091): a concrete wrong-but-well-formed datum the path would publish as fact.
- Literature basis: Sculley et al. 2015 (data dependencies / CACE / pipeline jungles); data-downtime / data-observability; reproducible/deterministic pipelines; automated data-validation gates (schema/invariant assertions).
- Risk level: MEDIUM-HIGH (silent data-quality regression published as fact into the connectome and every derived artifact, biasing the system's own evidence).
- Single coupled remedy: keep code-gating (the asymmetry floor stands), but convert the data path from UNREVIEWED to AUTO-CHECKED — verify generator determinism empirically, add automated data-quality/anomaly gates, bound auto-publish to small diffs, escalate anomalies (discharges REVISE-094 and resolves MONITOR-313 toward INCORPORATE).

**Backlog note (fail-loud):** standing AWAITING-REVIEW backlog was 46 (REVISE-047..092); +2 this run (REVISE-093, REVISE-094) = **48 total AWAITING-REVIEW**. Lowest-cost, highest-leverage remediation this run: the capability-and-state-probe-first discipline — a single standing pre-step that discharges REVISE-093 and downgrades MONITOR-314 and MONITOR-315 (the entire environment-capability-mismatch cluster) at once. Note: REVISE-093 (env-capability) is independent of the still-open record-linkage measurement (REVISE-089/091); the two highest-leverage open actions remain the record-linkage experiment and the capability-probe discipline.


## 2026-06-11 — REVISE intake (9 items, REVISE-095..103; from cycle-0 backlog drain 06-08/09/10). All AWAITING-REVIEW (Tom).

### REVISE-095 — PRESUMPTION-322 (trace=substance root)
**Statement:** [inferred] The event stream is a faithful proxy for what an agent IS and does (telemetry captures agent substance).
**15a:** PARTIALLY-SUPPORTED (Moderate; traces measure what an entity DOES) | **15b:** CHALLENGED (Strong; Sen 1973 revealed-preference critique; streetlight effect — wisely-idle and dead agents emit the same stream)
**What is at risk:** The Agent Explorer's foundational semantics; every downstream layer (eval/apply display, sociogram, metabolism) inherits the activity→substance conflation as ground truth. Root of the trace=substance SYSTEMIC-RISK (HIGH).
**Recommended action:** Urgency MEDIUM-HIGH. Decide the explorer's claim explicitly: it represents agent ACTIVITY (defensible, PREMISE-055), not agent identity/substance. Rename/relabel accordingly; add an explicit "what this does not show" note to the explorer; keep substance claims out of derived metrics until a validation path exists.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-096 — PRESUMPTION-325 (roster mis-specification)
**Statement:** [inferred] The agent population is a clean one-cron-task-per-agent roster (already contradicted by multi-fire agents + unmapped interactive sessions).
**15a:** NO-SUPPORT-FOUND (None; entity resolution exists because populations violate this) | **15b:** CHALLENGED (Strong; Binette & Steorts 2022; falsified by own data)
**What is at risk:** Every per-agent metric divides by a mis-specified denominator; contaminates ASSUMPTION-287/291/292 outputs (the whole explorer measurement layer).
**Recommended action:** Urgency HIGH. Replace the 1:1 presumption with an explicit entity model (agent ↔ sessions mapping with multi-fire and interactive cases), or at minimum quantify the mismatch rate before further explorer metrics ship. Cheapest version: count known violations in the current 571-session DB.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-097 — ASSUMPTION-293 (MM-of-1 self-certification) [NOVELTY]
**Statement:** An MM-of-1 can authoritatively certify the milestones of his own integrative tradition; at N=1, face validity must carry what inter-rater agreement otherwise would.
**15a:** PARTIALLY-SUPPORTED (Weak) + NOVELTY-FLAG (N=1 self-certification uncovered in psychometrics) | **15b:** CHALLENGED (Strong; Standards — face validity cannot carry an instrument; self-certification maximizes self-confirmation)
**What is at risk:** The evidential status of every dyad-ratified PRS milestone; downstream ISME claims that rest on "certified" milestones.
**Recommended action:** Urgency MEDIUM-HIGH. Re-scope: certifications are PROVISIONAL/candidate-generating, not authoritative; adopt the dyad reliability protocol (date/version-stamped assents, anchor-item blind re-presentation, planted-error catch trials — one protocol advances MONITOR-323/324/329 and REVISE-100 simultaneously). NOVELTY: the N=1 integrative-tradition case is genuinely uncovered — worth writing up as methodology.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-098 — ASSUMPTION-298 (deliberate over-promising)
**Statement:** Deliberate over-promising under accelerating capability ("over-promise with firm expectation of over-delivery") is a sound planning method.
**15a:** PARTIALLY-SUPPORTED (Weak; stretch goals require slack + recent-success conditions) | **15b:** CHALLENGED (Strong; planning fallacy; escalation of commitment on public promises)
**What is at risk:** The ISME schedule and any external commitments priced on expected over-delivery.
**Recommended action:** Urgency MEDIUM. Replace "firm expectation" with reference-class forecast from the project's OWN actuals (including the 7-day outage); pre-commit a minimum-viable deliverable. Joint review with REVISE-101/102.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-099 — ASSUMPTION-299 (scrub discharges exposure concern)
**Statement:** Removing all "bosco"/"email" strings from the current public HTML discharges the public-exposure concern (validated by string count + static checks).
**15a:** PARTIALLY-SUPPORTED (Weak; valid for the working tree only) | **15b:** CHALLENGED (Strong; git history, archives/mirrors, encoding variants survive)
**What is at risk:** A privacy/exposure concern recorded as CLOSED that is only partially closed; involves identifiable-person data (BOSCO Uganda context).
**Recommended action:** Urgency MEDIUM. One-time surface audit: git log -S on the removed strings; check published copies (GitHub Pages history, Wayback CDX); grep encoding variants. Closing the audit also closes MONITOR-327. Until then, record the concern as MITIGATED-NOT-DISCHARGED.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-100 — PRESUMPTION-330 (dyad persistence) [NOVELTY]
**Statement:** [inferred] "The recorded Tom⇄Claude dyad" is a persisting unit across sessions/contexts/model versions, despite the charter's own individuation principle implying otherwise.
**15a:** PARTIALLY-SUPPORTED (Weak; persistence is certifiable via invariance checks, not default) + NOVELTY-FLAG | **15b:** CHALLENGED (Strong; LLM drift = different instruments without measured linkage; charter self-contradiction)
**What is at risk:** All dyad ratifications form an unanchored mixture across instrument versions; the charter contradicts itself on individuation.
**Recommended action:** Urgency MEDIUM-HIGH. Design decision needed (not monitorable): define dyad individuation criteria + an invariance protocol (version-stamped assents; anchor-item re-presentation across model versions; explicit re-certification on model change). Resolve the charter contradiction explicitly. NOVELTY: composite human-AI measurement unit is an original-methodology candidate.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-101 — PRESUMPTION-332 (capacity persistence through ISME)
**Statement:** [inferred] Current build capacity (attended cadence + agentic throughput + infrastructure) persists through the ~4-week ISME schedule, despite same-day record of a 7-day sync outage and a growing single-human review gate.
**15a:** NO-SUPPORT-FOUND (None) | **15b:** CHALLENGED (Strong; the contrary evidence is the project's own same-day record)
**What is at risk:** The ISME plan's feasibility; cascades into REVISE-098's commitments.
**Recommended action:** Urgency MEDIUM-HIGH. Price the outage base rate into the schedule (buffer from own actuals); define the minimum-viable ISME deliverable; acknowledge the single-gate throughput cap (REVISE-102) as the binding constraint, not agentic capacity.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-102 — PRESUMPTION-337 (single-gate scaling)
**Statement:** [inferred] The single-human attended commit gate scales with parallel-session output (local-only queues can accumulate indefinitely without integration risk).
**15a:** NO-SUPPORT-FOUND (None; CI literature contradicts both clauses) | **15b:** CHALLENGED (Strong; fixed-capacity gate + elastic arrivals = unbounded queue; review degrades to rubber-stamping under load)
**What is at risk:** Review quality exactly when it matters; merge-conflict debt on shared hub files (queue files, generated HTML, indexes); ISME throughput (couples REVISE-101).
**Recommended action:** Urgency MEDIUM-HIGH. Set a WIP limit on unintegrated parallel sessions; scheduled integration cadence; conflict pre-check on shared hub files; consider tiered review (auto-checks for low-risk classes) to keep the human gate for what needs judgment.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-103 — PRESUMPTION-339 (exhaust tracks the aim)
**Statement:** [inferred] Measurable exhaust tracks the constitutional aim — interim commit-yield metabolism display presumes artifact throughput is the right thing to maximize, before PRS/peace dimensions exist in the metric.
**15a:** PARTIALLY-SUPPORTED (Weak; interim proxies have precedent; gap nonzero by construction) | **15b:** CHALLENGED (Strong; surrogation — display salience alone causes metric-substitution; single-operator-as-optimizer is the highest-exposure configuration)
**What is at risk:** The system's optimization direction: throughput-first instrumentation selects against low-exhaust peace/deliberation work — the constitutional aim — and entrenches before the mission dimensions arrive.
**Recommended action:** Urgency MEDIUM-HIGH. Caveat-label the metabolism display; strip ranking salience; time-box the interim explicitly; add PRS/peace placeholder dimensions (visible "not yet measured" slots) so the proxy cannot silently become the aim. Floor (hedged yield axis) stands as MONITOR-335.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-11):** 9 (REVISE-095..103). **AWAITING-REVIEW backlog: was 48 → now 57.** Fail-loud: this is the largest single-run REVISE intake to date; cause is the 3-day backlog drain (39 items) plus unusually measurement-heavy source sessions, not a 15c calibration change.

**SYSTEMIC-RISK flags (2026-06-11, 7):**
1. **trace=substance Agent-Explorer stack — HIGH.** ASSUMPTION-287 (PREMISE-055, scoped floor) + PRESUMPTION-322 (REVISE-095, root) + PRESUMPTION-323 (MONITOR-319) + PRESUMPTION-327 (MONITOR-322). Single inferential ladder: telemetry faithful → ratio directional → display neutral → narration replaceable; if 322 falls, the stack falls, and 327 closes the loop by letting the flawed representation steer agent evolution. Remedy: the explorer claims ACTIVITY, not substance (REVISE-095's relabel) + no rankings until validated.
2. **Dyad-measurement-validity — HIGH.** ASSUMPTION-293 (REVISE-097) + 294 (PREMISE-058) + 295 (MONITOR-323) + 297 (MONITOR-324) + PRESUMPTION-330 (REVISE-100) + 333 (MONITOR-329). No reliability infrastructure of any kind around the single-rater + sycophancy-prone-agent apparatus. ONE shared remedy: the dyad reliability protocol (date/version-stamped assents + anchor-item blind re-presentation + planted-error catch trials) substantially advances all six.
3. **Proxy-metric surrogation — HIGH.** ASSUMPTION-307 (MONITOR-335, floor) + PRESUMPTION-339 (REVISE-103, overclaim); ASSUMPTION-309 (MONITOR-336) adjacent. The metabolism instrument's only live axis is a gameable throughput proxy instrumented before the constitutional dimensions exist; PREMISE-060's scheduler would CONSUME this metric if wired up — do not compose until resolved.
4. **Biased-denominator cascade — MEDIUM-HIGH.** ASSUMPTION-292 (PREMISE-057 boundary) + PRESUMPTION-325 (REVISE-096) + 326 (MONITOR-321), contaminating 291 (MONITOR-318). Three correlated undercounts of the same population (capture gap, window, 1:1 roster) skew the explorer's population baseline in the same direction.
5. **Verification-by-inference — MEDIUM-HIGH.** ASSUMPTION-301 (MONITOR-330) + PRESUMPTION-334 (MONITOR-337) + 335 (MONITOR-338) + 324 (MONITOR-320). Correctness claims without behavioral observation compound: a structurally-argued change passes a syntax-only validator and a change-blind human gate. Remedy: render smoke-test + display invariants + "structural = interim" standing rule.
6. **Optimism-under-single-gate — MEDIUM-HIGH (ISME-specific).** ASSUMPTION-298 (REVISE-098) + PRESUMPTION-332 (REVISE-101) + 337 (REVISE-102). Over-promise layered on presumed capacity persistence with a saturating single-human gate as binding constraint. Remedy: reference-class buffer + MVD + WIP limit (one joint review).
7. **Remediation-completeness — MEDIUM.** ASSUMPTION-299 (REVISE-099) + PRESUMPTION-329 (MONITOR-327). Validation measured the action (tree scrub), not the concern (exposure surfaces). Remedy: the one-time surface audit.

**Highest-leverage open actions after this run:** (a) dyad reliability protocol (discharges most of cluster 2); (b) render smoke-test + display invariants (cluster 5, two MONITORs); (c) ISME joint review of REVISE-098/101/102 (cluster 6); (d) explorer relabel to ACTIVITY semantics (cluster 1). Carried from prior runs: record-linkage experiment (REVISE-089/091), capability-probe discipline (REVISE-093).

### REVISE-104 — ASSUMPTION-310 (narrative individuation exclusivity)
**Statement:** Narrative-embedded perspective is the principle of individuation within CRm ("different narratives, different perspectives, are the principle of individuation: there is nothing else").
**15a:** PARTIALLY-SUPPORTED (Moderate; Ricoeur/Schechtman/Dennett support narrative as AN individuating principle — none assert exclusivity) | **15b:** CHALLENGED (Strong; Strawson episodic self; cosmopsychist decombination problem; animalism/haecceity alternatives)
**What is at risk:** M7 agent-identity claims; CRm's individuation story. The challenged element — the "nothing else" clause — is exactly the load-bearing part.
**Recommended action:** Urgency MEDIUM. Two clean options, Tom's call: (1) weaken to "narrative-embedded perspective is the (or a) primary principle of individuation" — fully literature-supported; or (2) keep exclusivity and write the explicit defense against the episodic-self and decombination objections (would itself be a contribution; couples the planned individuation_vs_reunion.md, see REVISE-110).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-105 — ASSUMPTION-314 (falsifier = yield metric)
**Statement:** Falsifier (b) as positive prediction and master-plan §6 interaction yield are the same measurement (agreed rungs = first countable PRS-milestone yield).
**15a:** PARTIALLY-SUPPORTED (Moderate; convergent-validity structure sound; construct identity unverifiable externally) + NOVELTY flag | **15b:** CHALLENGED (Strong; jingle fallacy — Cronbach & Meehl; one observable as both falsifier and progress metric is a non-falsifiable inner loop, Lakatos-degenerative)
**What is at risk:** Falsifiability of the dyad-ladder programme; M-milestone evidence integrity. Anchor of the self-referential-measurement Critical cluster (with MONITOR-341/342, REVISE-111).
**Recommended action:** Urgency HIGH. Pre-register falsifier-(b) thresholds and operational definitions independently of §6 yield counting (timestamped, before ledger inspection). Treat construct identity as a hypothesis to demonstrate empirically (correlate the two counts across sessions), not an identity to assume. NOVELTY: if demonstrated rather than stipulated, this is a potential original contribution.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-106 — PRESUMPTION-340 (ledger as Level-3 without external rater)
**Statement:** [inferred] A dyad's own agreement ledger is valid Level-3 evidence without an external rater.
**15a:** PARTIALLY-SUPPORTED (Moderate; diary/EMA precedent for participant-generated records) | **15b:** CHALLENGED (Strong; Bazerman et al. auditor-independence impossibility; psychometric inter-rater requirements; self-serving coding bias is unconscious)
**What is at risk:** Level-3 evidential status of the agreement ledger and everything the maturity model builds on it. Anchor of the dyad-measurement-validity cluster — ESCALATED HIGH -> CRITICAL this run (capture 341, coding 340, falsification 346 all lack independence; no stage of the evidence chain is independent of the dyad).
**Recommended action:** Urgency HIGH. Records-vs-coding distinction: the ledger is valid DATA (diary precedent); the dyad's own quality-coding of it is not yet valid EVIDENCE. Define Level-3 to require periodic independent rating of a random rung sample (external human or structurally independent agent); implement the dyad reliability protocol (date/version-stamped assents + anchor re-presentation + catch trials) already recommended by the prior cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-107 — PRESUMPTION-341 (neutral sole scribe)
**Statement:** [inferred] The agent member as sole scribe does not shape the shared record.
**15a:** PARTIALLY-SUPPORTED (Moderate; structured templates reduce recorder variation — weaker claim only) | **15b:** CHALLENGED (Strong; LLM summarization framing bias ~22% of instances, Yang et al. 2025; note-taker selective recording; cooperative training predisposes curation over transcription)
**What is at risk:** Fidelity of the shared record the ledger is built from; disagreement systematically softened/omitted. Dyad-measurement Critical cluster (scribing facet).
**Recommended action:** Urgency MEDIUM. Retain raw session transcripts as record of reference (curated notes as index, not substitute); periodic human spot-audit of curated-vs-verbatim divergence, specifically checking for softened disagreement; add a mandatory dissent field to record templates so absence of recorded dissent is conspicuous rather than default.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-108 — PRESUMPTION-343 (batch-size invariant quality)
**Statement:** [inferred] Disposition quality is batch-size invariant (188-item drain ≈ daily cadence quality).
**15a:** PARTIALLY-SUPPORTED (Weak; protocols are the main quality determinant at volume — but best practice distributes large batches) | **15b:** CHALLENGED (Strong; decision fatigue, vigilance decrement within 20-30 min, code-review batch-size effects)
**What is at risk:** Disposition quality on large drains; late-batch high-stakes items rubber-stamped. SELF-APPLICABLE: the 2026-06-11 drain processed 188 items in one run — its late-position dispositions are flagged as positionally suspect by this evidence.
**Recommended action:** Urgency MEDIUM. Cap autonomous-run batch size (~30 dispositions/run; drain backlogs across multiple runs); order processing by stakes so HIGH-priority items are not late; spot re-review of late-position dispositions from the 2026-06-11 drain. Pipeline-health cluster (with REVISE-109/110).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-109 — PRESUMPTION-344 (queue emptiness = health)
**Statement:** [inferred] Queue emptiness is pipeline health (the indicator did not migrate with the constraint to the 57-item review stage).
**15a:** PARTIALLY-SUPPORTED (Moderate; queue length is a legitimate flow indicator — TOC itself predicts the observed failure) | **15b:** CHALLENGED (Strong; Goldratt — measuring a non-constraint stage produces local optima masking global state; this is a direct instance)
**What is at risk:** Capacity/prioritisation decisions on a false health signal; invisible accumulation at the human-review constraint (AWAITING-REVIEW now 65).
**Recommended action:** Urgency MEDIUM. Both search directions converge on the same fix: every run summary reports end-to-end flow — per-stage WIP (QUEUED / SEARCHED / DISPOSITIONED / AWAITING-REVIEW), oldest-item age, net flow at the constraint — not just disposition-queue emptiness. (This run's PROCESSED block starts the practice.) Pipeline-health cluster.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-110 — PRESUMPTION-345 (plan-inventory durability)
**Statement:** [inferred] Proposed artifacts get created or their absence gets noticed (individuation_vs_reunion.md gap went 18 days unnoticed).
**15a:** PARTIALLY-SUPPORTED (Moderate; Gollwitzer implementation intentions specify the conditions under which plan durability IS achievable) + NOVELTY flag (vault-as-tracker hybrid unstudied) | **15b:** CHALLENGED (Strong; already falsified by its own citing instance; prospective-memory mechanism — deferred intentions without external cues fail across session boundaries)
**What is at risk:** Vault coverage silently diverging from vault intention; planning activity miscounted as production. Pipeline-health cluster.
**Recommended action:** Urgency MEDIUM. Weekly plan-artifact reconciliation sweep: extract proposed-artifact mentions from session notes/plans, diff against vault contents, surface orphans with age. Give every proposed artifact implementation-intention structure at proposal time (owner, trigger cue, due date). And create individuation_vs_reunion.md or explicitly cancel it (couples REVISE-104 option 2).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-111 — PRESUMPTION-346 (reflexive falsification non-circular)
**Statement:** [inferred] Reflexive falsification is non-circular (the dyad applying its own falsifier to its own ledger constitutes a genuine test).
**15a:** PARTIALLY-SUPPORTED (Moderate; Chang — self-testing is non-vicious IF the falsifier is specified independently of tested outcomes) | **15b:** CHALLENGED (Strong; Simmons et al. researcher degrees of freedom; auditor self-review impairment; falsification requires independent disconfirmatory capacity)
**What is at risk:** Epistemic value of the reflexive falsification programme — its tests may be passable by construction. Falsification facet of the dyad-measurement Critical cluster; couples REVISE-105.
**Recommended action:** Urgency HIGH. Pre-register falsifier definitions, thresholds, and analysis procedure (timestamped commit BEFORE ledger inspection); verification of falsifier application by a party outside the dyad (15-series agent or human third party); log analytic choices to constrain degrees of freedom. Note: 15a and 15b converge — Chang's independence condition is exactly what 15b finds absent; the remedy (pre-registration) is common ground.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-12):** 8 (REVISE-104..111). **AWAITING-REVIEW backlog: was 57 → now 65.** Fail-loud: second-largest single-run REVISE intake (after 06-11's 9), at normal cohort size (14 items) — the driver is cohort content, not volume: 14b's 06-11 EOD pass surfaced the measurement/validity substrate of the dyad-ladder programme, and the literature robustly challenges self-measurement without independence. Two Critical systemic clusters this run: (1) dyad-measurement circularity ESCALATED HIGH->CRITICAL (340/341/346 + prior 293/294/295/297/330/333) — capture, coding, and falsification all lack structural independence; single highest-leverage remedy remains the dyad reliability protocol + pre-registration + periodic independent rating; (2) self-referential measurement (311/312/314/315, with 314/346 flagged REVISE) — pre-registration of falsifiers is the shared first step for both clusters.

## REVISE intake — run 2026-06-16 (15c; autonomous)

### REVISE-112 — ASSUMPTION-317 (marking resets staleness clock; leave transcript-pass unmarked)
**Statement:** Marking a QC item resets its staleness clock, so a transcript-only pass is left unmarked to avoid masking the synthesis half's later Layer-4 review.
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate; TTL semantics + POC accounting support the concern) + NOVELTY (specific sub-component-staleness pattern unstudied) | **15b:** PARTIALLY-CHALLENGED (Moderate; "leave unmarked" trades a visible failure for an invisible one — unrecorded work; the binary mark/no-mark scheme is the defect)
**What is at risk:** Coverage accounting silently undercounts completed-but-unmarked work; a transcript pass can be lost if the synthesis review is delayed/dropped (the project's recurring absence-as-evidence hazard).
**Recommended action:** Urgency LOW. Scope the freshness clock per sub-component (separate transcript-pass and synthesis-review timestamps) so marking one does not reset the other; until then keep a "done-but-unmarked" ledger so the work is not invisible. Resolves OPEN-082.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-113 — PRESUMPTION-347 (pinned model ID stays valid indefinitely)
**Statement:** [inferred] A model identifier pinned in a scheduled-task config stays valid indefinitely (06-14 morning scrape died on unavailable "claude-fable-5").
**15a:** PARTIALLY-SUPPORTED (Weak; pinning is sound practice, but supports "pin + fallback," not "pin is permanent") | **15b:** CHALLENGED (Strong; hosted aliases deprecate on vendor time; pins to vendor namespaces rot; already falsified by the trigger)
**What is at risk:** Every task pinned to a single hosted model is a deprecation time-bomb; failure is total and (with 348) invisible for days; likely shared across multiple tasks.
**Recommended action:** Urgency MEDIUM-HIGH. Add a preflight model-availability check; add an ordered fallback-model chain (preferred -> alternates -> minimal); centralize the model ID in one config consumed by all tasks; log substitutions (fail-loud). Implement jointly with REVISE-114 under SYSTEMIC-RISK cluster (1).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-114 — PRESUMPTION-348 (a failing scheduled task announces its own failure)
**Statement:** [inferred] A failing scheduled task announces its own failure (no liveness monitor; channel degraded ~3 days, 06-13 summaries simply missing).
**15a:** NO-SUPPORT-FOUND (None; cron/observability literature describes the opposite) | **15b:** CHALLENGED (Strong; cron monitoring is built on "guilty until proven innocent"; failures are silent; falsified by the 3-day outage)
**What is at risk:** Any scheduled-task failure is invisible until a human notices missing output (here ~3 days; unbounded in principle); downstream pipelines silently run on absent inputs.
**Recommended action:** Urgency MEDIUM. Add a dead-man's-switch (task pings an external monitor on clean exit; alert on absence within the expected window) + output assertions (alert if produced < N expected artifacts); distinguish "ran" from "succeeded" in a status log. Implement with REVISE-113 under SYSTEMIC-RISK cluster (1).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-115 — PRESUMPTION-349 (one added file = one unit of yield)
**Statement:** [inferred] One added file = one unit of yield (file-count commensurability beneath the files-added metric).
**15a:** NO-SUPPORT-FOUND (None; equal-weighting is a tractability default, not validated commensurability) | **15b:** CHALLENGED (Strong; files are heterogeneous in size/effort/value; equal-weighting is the canonical LOC-style gaming mechanism)
**What is at risk:** All downstream uses inherit false commensurability; foregrounding (ASSUMPTION-318) or optimizing rewards artifact-splitting and thin files.
**Recommended action:** Urgency MEDIUM-HIGH. Replace/augment raw count with a distribution-aware view (median/quartile file size; net content after deletions; optional word-count weighting); always show the size distribution alongside the count; never use the raw count as a target or optimizer input; label "artifacts emitted," not "yield." NOTE (Rule-7 surface-don't-average): the SERIES choice (318) is held at MONITOR-345 while this hidden UNIT assumption is REVISEd — keep the headline IF the commensurability beneath it is corrected. Member of Metabolism-proxy SYSTEMIC-RISK cluster (2); couples MONITOR-335/REVISE-103.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-116 — PRESUMPTION-351 (a visible gap-marker is an understood gap)
**Statement:** [inferred] A visible gap-marker is an understood gap (visibility = comprehension).
**15a:** PARTIALLY-SUPPORTED (Weak; understood only when the marker uses a learned convention) | **15b:** CHALLENGED (Moderate-Strong; comprehension tracks learned encodings, not visibility; a custom gap convention has none; trace-vs-substance error)
**What is at risk:** Honest gaps (correctly preferred per PREMISE-063) are misread — a capture-artifact gap read as "did nothing," real inactivity read as a glitch — so integrity gained at display is lost at comprehension; especially acute given 352's open artifact-vs-real ambiguity.
**Recommended action:** Urgency LOW. Annotate gaps with their reason (inline label/tooltip: "instrumentation gap" vs "no activity"); add a legend defining the gap convention; encode artifact-vs-real gaps differently (couples PRESUMPTION-352 / MONITOR-349); comprehension-test the convention (even on the sole expert viewer after a delay). This is the necessary companion to PREMISE-063.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-16):** 5 (REVISE-112..116). **AWAITING-REVIEW backlog: was 65 -> now 70.** Two SYSTEMIC-RISK clusters drive the operational subset: cluster (1) "absence != success/event" (113/114 + 112's invisibility facet) — single coupled remedy: preflight checks + heartbeat/dead-man's-switch + fail-loud logging on every scheduled task; cluster (2) Metabolism-view proxy stack (115 + MONITOR-345/346/348/350) — treat all Metabolism metrics as descriptive-only/provisional until each proxy is validated against an independent signal. Highest-leverage single fixes: (a) one heartbeat+preflight wrapper closes 113/114; (b) the post-Apr-6 probe (MONITOR-349) and one git-history audit unblock most of cluster (2).

### REVISE-117 — ASSUMPTION-323 (a commit-message self-report verifies the yield series)
**Statement:** A commit-message self-report ("+38 PRS triplets") is an adequate cross-check that verifies the derived yield series.
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate; a matching contemporaneous self-report is real POINT-LOCAL corroboration via triangulation) | **15b:** CHALLENGED (Moderate-Strong; commit messages are unreliable narrators, may be non-independent of the pipeline (circular), and one match verifies one window — not the series)
**What is at risk:** A single self-report taken as series validation lets systematic pipeline errors on uncorroborated days survive into the headline yield (feeds the PRESUMPTION-360 over-trust).
**Recommended action:** Urgency LOW-MEDIUM. Verify against the DIFFS (count added triplet-ids), not the commit prose; sample multiple windows; confirm the cross-check is independent of the pipeline's derivation; report "N of 6 windows corroborated," not "series verified." Same instrument as the cluster-3 git-history audit. Couples REVISE-120 (PRESUMPTION-356).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-118 — ASSUMPTION-325 (the git series supersedes "269" as THE authoritative PRS number)
**Statement:** The git-derived production series supersedes the static "269 network" count as the authoritative PRS number.
**15a:** PARTIALLY-SUPPORTED (Moderate, conditional; an auditable/recent measure supersedes an undocumented one WHEN both target the same quantity) | **15b:** CHALLENGED (Moderate-Strong; if 269=network footprint and 264/262=production/census are distinct constructs, "supersedes as THE number" is a category error — discriminant validity)
**What is at risk:** Retiring "269" as superseded silently drops the network-footprint construct; readers inherit a false "one true PRS count"; OPEN-081/084 mis-scoped as reconciliation.
**Recommended action:** Urgency MEDIUM. Reword to "the git series is the authoritative PRODUCTION measure"; keep 269 as the authoritative NETWORK measure with its construct labeled; reframe OPEN-084 as construct-disambiguation. Resolve jointly with REVISE-121 (PRESUMPTION-357) — both turn on the same construct-distinctness question. Member of SYSTEMIC-RISK cluster (3).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-119 — PRESUMPTION-355 (yield = birth-rate; lifecycle irrelevant)
**Statement:** [inferred] The meaningful event is a triplet's creation (first appearance), not its revision/validation/use/retirement — yield = birth-rate.
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate; creation-count is a legitimate first-order leading indicator) | **15b:** CHALLENGED (Moderate-Strong; birth-rate is a gameable output proxy diverging from value — Goodhart; churn/survival carry the real signal — Lehman; scientometrics impact-weights)
**What is at risk:** A birth-rate "yield" rewards many short-lived triplets; the system reads volume as productivity while survival/quality silently degrade.
**Recommended action:** Urgency MEDIUM. Report birth-rate as ONE leading indicator beside survival (fraction of created triplets persisting/used/validated) and a churn/retirement rate; never optimize birth-rate; survival-weight (or at least caveat) the headline. Member of Metabolism-proxy cluster (2) and SYSTEMIC-RISK cluster (3); couples ASSUMPTION-322/324, PRESUMPTION-359.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-120 — PRESUMPTION-356 (one corroborating point verifies the whole 6-day series)
**Statement:** [inferred] One corroborating data point (06-07 commit message) verifies the whole 6-day series.
**15a:** NO-SUPPORT-FOUND (None; triangulation supports only point-local corroboration) | **15b:** CHALLENGED (Strong; confirmation bias / problem of induction; sampling-coverage; the lone match manufactures false confidence that suppresses further checking)
**What is at risk:** A pipeline bug on the five unchecked days is masked by the single match; the headline yield is trusted on 1/6 coverage; over-trust propagates to PRESUMPTION-360.
**Recommended action:** Urgency LOW-MEDIUM. Sample/check multiple windows (every day with any independent signal); compute and report corroboration COVERAGE; treat the 06-07 match as 1-of-6 corroborated, not "series verified." Implement with REVISE-117 (stated twin, ASSUMPTION-323) under SYSTEMIC-RISK cluster (3).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-121 — PRESUMPTION-357 (269/264/262 estimate one quantity to reconcile)
**Statement:** [inferred] The three counts (269 / 264 / 262) estimate one real quantity to be reconciled, not three distinct constructs.
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate, conditional; IF one construct, reconcile-them is correct — convergent validity) | **15b:** CHALLENGED (Strong; discriminant validity + stock-vs-flow say footprint / cumulative-production / surviving-census are distinct constructs that SHOULD differ — "reconcile to one" is a category error)
**What is at risk:** Effort spent forcing distinct constructs to one number; informative gaps (retired set, network footprint) discarded; a false "single true PRS count" hardens into the system's self-description (OPEN-081/084).
**Recommended action:** Urgency MEDIUM-HIGH. Replace "reconcile to one quantity" with "define three constructs and report each with its question"; show gaps as meaningful (264-262 = retired/reused; 269 vs 264 = footprint vs production); reframe OPEN-084 as disambiguation. Resolve jointly with REVISE-118 (stated twin, ASSUMPTION-325). Member of SYSTEMIC-RISK cluster (3).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-122 — PRESUMPTION-358 (visual resolvability = informational fidelity)
**Statement:** [inferred] Making all 269 nodes individually resolvable increases fidelity (visual resolvability = informational fidelity).
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate; de-occluding co-located nodes is a real legibility gain for identity/count — anti-overplotting; Tufte "show the data") | **15b:** CHALLENGED (Moderate-Strong; resolving by an arbitrary fan injects positions read as structure — Cleveland & McGill — and "show every item" can bury aggregate structure; trace-vs-substance error)
**What is at risk:** Viewers (incl. the sole expert) infer rings/clusters/orderings from the resolving fan; clutter from 269 resolved nodes hides real aggregate pattern; "everything visible" mistaken for "picture faithful."
**Recommended action:** Urgency LOW. Decouple goals: identity-resolution on demand (hover/zoom/detail) while the default view shows faithful aggregate structure; mark the fan's positions non-semantic (uniform styling + "positions within a node-cluster are incidental" note); evaluate fidelity by what viewers correctly infer, not by whether every node is drawn. This is the perception companion to PREMISE-065 (ASSUMPTION-327); couples that incidental-marking caveat.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-123 — PRESUMPTION-359 (git history is a complete census of production)
**Statement:** [inferred] Git history is a complete census of PRS-triplet production ("264 produced", not "264 git can see").
**15a:** PARTIALLY-SUPPORTED (Weak, conditional; born-in-repo artifacts make git a census of the TRACKED STORE by construction) | **15b:** CHALLENGED (Strong; git records what was COMMITTED not what was PRODUCED — Kalliamvakou 2014; rebase/squash, pre-VCS and out-of-band authoring break the census; map-vs-territory)
**What is at risk:** Production systematically undercounted (invisible pre-VCS/out-of-band work) or miscounted (rewritten history) while reported as true production; couples ASSUMPTION-322 and PRESUMPTION-355.
**Recommended action:** Urgency LOW-MEDIUM. Phrase the figure as "264 in the tracked history," not "264 produced"; run the git-history audit (rebase/squash + pre-VCS/out-of-band inventory); state the coverage boundary; if a true census is needed, reconcile git against an independent inventory. Surfaced-not-averaged with stated twin ASSUMPTION-322 (MONITOR-352): 322 (creation-DATING proxy) monitored, 359 (the stronger CENSUS claim) revised — mirrors the 318/349 split. Audit shared with REVISE-117. Member of SYSTEMIC-RISK cluster (3).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-124 — PRESUMPTION-360 (building the metric dissolved the cart-before-horse concern)
**Statement:** [inferred] Building the metric dissolved the cart-before-horse concern (data-backed ⇒ trustworthy-enough-to-build-on).
**15a:** NO-SUPPORT-FOUND (None; provenance/derivation is not validity) | **15b:** CHALLENGED (Strong; "garbage in, gospel out"; validity is a property of the inference to the construct — Cronbach & Meehl; mechanically-produced figures attract unearned authority — Porter "Trust in Numbers")
**What is at risk:** The view layer and downstream readings hardened on a series with five open challenges (322/323/355/356/359); the "data-derived" halo suppresses the very validation those items require.
**Recommended action:** Urgency MEDIUM. Treat "built" as the START of validation, not its end; require the series to clear its open challenges (coverage, creation-dating, multi-window verification, construct disambiguation) before the view hardens on it; label the series PROVISIONAL / descriptive-only until then; separate provenance (how derived) from validity (does it measure the construct) in reporting. KEYSTONE of SYSTEMIC-RISK cluster (3) — the inference that lets the system skip validation of the other seven items. Scope guard companion to PREMISE-064 (ASSUMPTION-326).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-17):** 8 (REVISE-117..124). **AWAITING-REVIEW backlog: was 70 -> now 78.** All eight are facets of SYSTEMIC-RISK cluster (3): the PRS-yield series is treated as more complete (123/117/120), more validated (124 keystone), and more singular (118/121) than warranted, with birth-rate-as-yield (119) atop and the resolvability/fidelity conflation (122) in the view. Two cheap instruments close most of it: (a) ONE git-history audit of prs_triplets.md (rebase/squash + pre-VCS/out-of-band + multi-window diff recount) closes 117/120/123 and unblocks MONITOR-352; (b) a one-paragraph construct-definition note for 269/264/262 closes 118/121 and reframes OPEN-084. The keystone fix (124) is a policy: PRS-yield = descriptive-only/provisional until validated; do NOT harden the view layer on it yet.

### REVISE-125 — PRESUMPTION-363 (model-drafted, human-approved bio adequately represents a living tradition)
**Statement:** [inferred] A model-drafted, human-approved mini-bio adequately/fairly represents a living tradition (approval = adequacy).
**15a:** PARTIALLY-SUPPORTED (Weak; editorial sign-off / human post-editing raises accuracy above raw generation) | **15b:** CHALLENGED (Moderate-Strong; model drafts carry distributional bias and flatten internal diversity; one sign-off certifies acceptability-to-one-reviewer not representational fairness; automation bias under-scrutinizes fluent AI text; "whose voice represents a living tradition?")
**What is at risk:** Bios that are fluent and approved but subtly misrepresent/flatten traditions; sole-expert approval creates false confidence; adherents would not recognize the portrayal as fair. The presumption's weak link is the EQUATION approval=adequacy, not the value of approval.
**Recommended action:** Urgency MEDIUM. Claim the bios only as orienting, editorially-vetted summaries — NOT authoritative representations: label them "model-drafted, editorially approved — not authoritative," disclose provenance, and provide a correction path; where feasible seek tradition-holder review or cite source texts. Separate "accurate enough to display" from "fairly represents," and assert only the former. Couples MONITOR-357 (PRESUMPTION-361, granularity) — together the representation cluster for the bios.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-126 — PRESUMPTION-364 (rendering-correctness implies content-correctness)
**Statement:** [inferred] Local visual verify certifies correctness — rendering-correctness implies content-correctness (right brief, accurate text).
**15a:** NO-SUPPORT-FOUND (None; no literature supports render ⇒ content — the testing field separates the two assertions) | **15b:** CHALLENGED (Strong; a page can render flawlessly with wrong brief/text/counts; smoke tests don't cover content; inattentional blindness/automation bias miss non-salient errors — a recognized verification fallacy)
**What is at risk:** Wrong/inaccurate bio text or wrong node counts ship because the page rendered; the "verify" gives false certification. Made concrete by the unexplained ~256-vs-379 Summa gap a glance would not surface.
**Recommended action:** Urgency MEDIUM. Add explicit content/fidelity assertions to the gate (expected text present, expected counts, each `**Summary**` non-empty and matching source) and treat render-verify and content-verify as SEPARATE required checks; never let "it renders" stand in for "it's correct." Strong (inferred) twin of ASSUMPTION-331 (MONITOR-355): 331 (stated, over-claims sufficiency of the visual check) monitored; 364 (the stronger render⇒content inference) revised — the surfaced-not-averaged split. The content-assertion add-on shared with REVISE-128 (surfaces the count definitions). Member of convention-guard / glance-verification cluster (SYSTEMIC-RISK cluster 4).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-127 — PRESUMPTION-366 (documentation-only caveat is a sufficient guard for an armed destructive script)
**Statement:** [inferred] A documentation-only caveat is a sufficient guard for an armed destructive script (never-rerun by memory, not by code).
**15a:** NO-SUPPORT-FOUND (None; no literature endorses documentation as a SUFFICIENT safeguard for a destructive operation) | **15b:** CHALLENGED (Strong; fail-safe design and the safety hierarchy-of-controls rank documentation the WEAKEST control — reliable only if every human/agent remembers perfectly forever; latent-error probability rises with contributors/time/automation while the doc guard stays flat — Nygard)
**What is at risk:** Eventually someone/something reruns apply_summaries.py and irreversibly clobbers the hand-approved bios; the only safeguard was a sentence in the docs. Priority MEDIUM-HIGH.
**Recommended action:** Urgency MEDIUM. Replace/supplement the caveat with an ENGINEERING control: make the seed idempotent (merge not overwrite), add a guard clause (refuse if hand-edits present / require --force + explicit confirmation), or DISARM by removing the script post-seed (history retains it). If docs are kept, treat them as a complement to — never a substitute for — the code guard. Strong (inferred) twin of ASSUMPTION-329 (MONITOR-354): 329 states the correct never-rerun constraint; 366 makes explicit the insufficient doc-only guard relied on to enforce it. KEYSTONE of new SYSTEMIC-RISK cluster (4): guard/verify-by-convention rather than by code/assertion.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-128 — PRESUMPTION-368 (the two Summa counts are commensurable)
**Statement:** [inferred] The two Summa counts (~256 vs ~379) are commensurable, so the difference reads as a "drop" not a definitional mismatch.
**15a:** NO-SUPPORT-FOUND (None-Weak; nothing supports default commensurability of differently-defined counts — measurement theory makes it a thing to be demonstrated) | **15b:** CHALLENGED (Strong; construct validity / multiple operationalism — two measures are comparable only after establishing same construct & scale; a gap between differently-defined counts is often a definitional artifact, not a real drop — Cronbach & Meehl, Campbell & Fiske)
**What is at risk:** The system narrates a definitional mismatch as a real loss (or vice versa), misdiagnosing its own state; ASSUMPTION-332's "doesn't block push" (MONITOR-356) inherits the misframing. Recurrence of the 269/264/262 category error (PRESUMPTION-357 family).
**Recommended action:** Urgency MEDIUM. Write down the inclusion rule behind 256 and behind 379 (source, what qualifies as a "Summa node") BEFORE comparing; if the definitions differ, label the gap a DEFINITIONAL MISMATCH, not a drop; if a single quantity is genuinely intended, reconcile the operationalizations or pick one canonical definition — mirror the 357 construct-disambiguation fix. Couples MONITOR-356 (332). Member of the construct-validity / commensurability family (with PRESUMPTION-357 / REVISE-121).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-19):** 4 (REVISE-125..128). **AWAITING-REVIEW backlog: was 78 -> now 82.** Three are the stronger inferred twins of stated assumptions monitored this run (126↔ASSUMPTION-331/MONITOR-355; 127↔ASSUMPTION-329/MONITOR-354; 128↔ASSUMPTION-332/MONITOR-356) — the surfaced-not-averaged pattern. NEW SYSTEMIC-RISK cluster (4) flagged this run: guard-and-verify-by-CONVENTION rather than by code/assertion — REVISE-127 (doc-only guard, keystone), REVISE-126 (render-glance as content verify), and the scope guards on PREMISE-067 (convention-only "forbidden" path) and MONITOR-354/355 all share the vulnerability that safety/correctness rests on humans (or agents) behaving perfectly rather than on enforced controls. Two cheap engineering instruments close most of the cluster: (a) one code-guard/disarm pass on apply_summaries.py + an entry-point Summa-less guard (closes REVISE-127, hardens PREMISE-067, unblocks MONITOR-354); (b) a content-assertion add-on to regen — expected counts + each `**Summary**` present/non-empty (closes REVISE-126, unblocks MONITOR-355, and surfaces the 256-vs-379 definitions for REVISE-128/MONITOR-356). REVISE-125 (bio adequacy/voice) is independent and policy-level (label bios non-authoritative).

### REVISE-129 — PRESUMPTION-369 (drift detector presumes its own reliable scheduled execution)
**Statement:** [inferred] The EOD self-awareness pipeline presumes its own reliable scheduled execution — no internal liveness check on the mechanism whose job is to detect drift.
**15a:** NO-SUPPORT-FOUND (None-Weak; only YAGNI/proportionality offers adjacent shelter, and it collapses for a job that IS the drift detector) | **15b:** CHALLENGED (Strong; dead man's switch / heartbeat monitoring — assume failure unless the job actively pings success; a non-running job emits no error; quis-custodiet regress — the auditor cannot guarantee its own liveness from inside. healthchecks.io / Dead Man's Snitch / OneUptime)
**What is at risk:** Unbounded blindness to the system's own degradation: every downstream registry (assumptions/presumptions/lit-search/dispositions) silently goes stale while appearing current. Priority HIGH. Already FALSIFIED IN PRODUCTION — the pipeline stalled silently for two nights (06-19→06-20, OPEN-086); the drift detector failed to detect its own drift.
**Recommended action:** Urgency HIGH. Add an EXTERNAL liveness control: a dead-man's-switch / heartbeat that alerts on a MISSED expected run (not only on error); write a last-run/freshness timestamp downstream consumers and a separate watcher check; emit a "ran-but-produced-nothing" assertion so a no-op is distinguishable from a no-run; consider a second, independently-scheduled watcher (monitor-the-monitor). Keystone of SYSTEMIC-RISK cluster (5): over-trust of unattended automation / failure to fail loud (with MONITOR-296 autonomous-sync silent-degradation; PREMISE-049 verify-before-trust). COUPLED to REVISE-130 — one daily system-day liveness record discharges both.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-130 — PRESUMPTION-370 (agent-only "null day" presumed to carry no extraction-worthy content)
**Statement:** [inferred] An agent-only day with no attended session is presumed to carry no extraction-worthy epistemic content ("null day" = nothing to record).
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate; selective logging / alert fatigue / signal-to-noise genuinely caution against recording everything — but support only the WEAK form, not "no attended session => no content") | **15b:** CHALLENGED (Moderate-Strong; survivorship/selection bias — Abraham Wald — conditioning the record on attendance filters out exactly the unattended cases where unsupervised drift accrues; self-demonstrated: the 06-19→06-20 null days held the window's decisive fact, the silent stall)
**What is at risk:** The system's self-model biases toward attended periods; unattended drift and silent failures are under-represented precisely where they matter; absence-of-record gets misread as absence-of-event, compounding REVISE-129. Priority LOW (14b flagged speculative-confidence).
**Recommended action:** Urgency LOW. Record a minimal heartbeat/system-day STATUS entry every day, attended or not, that distinguishes "no-op / nothing changed" from "did-not-run" — treat "nothing notable happened" as a positive recorded fact, not an inference from silence. Use null-day records as the baseline against which drift is measured. NOT "record everything" (the valid 15a counter stands). COUPLED to REVISE-129: the same daily liveness record closes both the mechanism gap (369) and the epistemic gap (370). Member of SYSTEMIC-RISK cluster (5).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-21):** 2 (REVISE-129..130). **AWAITING-REVIEW backlog: was 82 -> now 84.** NEW SYSTEMIC-RISK cluster (5) flagged this run: over-trust of unattended automation / failure to fail loud — REVISE-129 (no liveness check on the auditor, keystone, FALSIFIED IN PRODUCTION via OPEN-086) and REVISE-130 (unattended periods presumed contentless) form a closed blind spot, coupled to the prior silent-degradation family (MONITOR-296, PREMISE-049). One cheap instrument closes most of the cluster: a mandatory daily system-day liveness record (no-op vs did-not-run) plus an external dead-man's-switch alert on missed runs.

### REVISE-131 — ASSUMPTION-336 (one corrected read path licenses trust in ALL downstream yields)
**Statement:** Correcting the token-read artifact licenses trust in all downstream yield comparisons ("do not inherit a masked drop")
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**What is at risk:** Historical and ongoing yield comparisons that silently assume whole-pipeline integrity after a single-path fix.
**Recommended action:** Urgency Medium. Restate as a scoped, per-path rule: "trust only reconciled read paths." Add a both-paths/canary reconciliation per yield-relevant field crossing the 04-07 migration. Tom to confirm no other yield field was affected.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14a; Chain: [14a -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-132 — PRESUMPTION-371 (shared vocabulary warrants a formal bridge — commensurability smuggle)
**Statement:** [inferred] That "same problem in two vocabularies" warrants a formal bridge — cross-vocabulary commensurability of the cognitive-glue and group-Markov-blanket accounts
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**What is at risk:** ASSUMPTION-333 and the Levin<->Friston bridge in PRS/connectome structure, if built on unverified commensurability.
**Recommended action:** Urgency Medium. Before formalizing the bridge, produce the structure-mapping table (corresponding higher-order relations, not shared vocabulary). Treat the bridge as "candidate homology" until it passes. Apply the 357/368 construct-validity guard.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-133 — PRESUMPTION-372 (intake-as-progress into a review-bound queue)
**Statement:** [inferred] That adding two well-chosen proposals is progress, even into a queue the same session calls review-bound and five deep with nothing decided since 06-16 (intake-as-progress)
**15a:** NO-SUPPORT-FOUND (None-Weak) | **15b:** CHALLENGED (Strong)
**What is at risk:** Intake cadence / sense of progress in the proposal and self-awareness pipelines while review is the constraint.
**Recommended action:** Urgency Low-Medium. Set an explicit WIP limit on the proposal-review queue; subordinate intake to review throughput; track progress as decisions decided, not proposals added. Exempt only rare perishable insights, with a decay check.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-134 — PRESUMPTION-373 (both-paths fix is durable — no recurrence guard)
**Statement:** [inferred] That the both-paths fix fully and durably resolves the token-read problem — exactly two payload schemas, no future migration silently re-zeroing reads, no recurrence guard installed
**15a:** NO-SUPPORT-FOUND (None-Weak) | **15b:** CHALLENGED (Strong)
**What is at risk:** Token/yield telemetry integrity across any future schema migration; the 335 correction's longevity.
**Recommended action:** Urgency Medium. Install a canary/contract assertion on token reads (fail loud on zeroed/missing path) and a derived-metric regression test across migrations. Do not presume the schema is frozen. One assertion can cover the 369/373 silent-read class.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-135 — PRESUMPTION-375 (monotone token growth = healthier (metric-direction smuggle))
**Statement:** [inferred] That month-over-month token growth (8.2M->20.4M->33.3M) is itself reassuring — more output tokens = healthier (metric-direction normative smuggling)
**15a:** NO-SUPPORT-FOUND (None-Weak) | **15b:** CHALLENGED (Strong)
**What is at risk:** Interpretation of token/yield dashboards; justification of token spend; the 336 "trust downstream yields" generalization.
**Recommended action:** Urgency Low. Replace/augment raw token-growth reassurance with a value- or efficiency-normalized metric (e.g., validated-premises or decisions per token). Treat raw growth as cost requiring justification. Couple with REVISE-131 (336) and the 367 metric-direction line.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-136 — PRESUMPTION-376 (papers' formal results transfer intact to epistemic/AI tradition-agents — keystone)
**Statement:** [inferred] That the papers' formal results (group-level Markov blanket as super-agent criterion; cognitive glue as binding mechanism) transfer intact to a community of inquirers / AI tradition-agents — transfer conditions named as "C2A2's extension" but never checked
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Strong)
**What is at risk:** The entire "individual<->collective" detector framing and any PRS/connectome structure that assumes group-level active inference governs tradition-agents.
**Recommended action:** Urgency High. Before relying on the transfer, enumerate and test the scope conditions for a group-level Markov blanket over a community of inquirers (shared generative model; Markovian separation of internal/external states). Treat as hypothesis; pilot on a bounded epistemic collective. Tom to review as the cohort's priority item.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-23):** 6 (REVISE-131..136). **AWAITING-REVIEW backlog: was 84 -> now 90.** Two SYSTEMIC-RISK clusters drive these. NEW cluster 6 (cross-vocabulary over-claim / unchecked transfer): REVISE-132 (commensurability from shared vocabulary) and REVISE-136 (intact transfer to epistemic collectives, KEYSTONE, HIGH) — paired with the MONITORed stated twins (MONITOR-360/361). EXTENDED cluster 5 (token-telemetry over-trust / fail-loud): REVISE-131 (trust-all-downstream), REVISE-134 (durability without recurrence guard, same silent-read class as REVISE-129), REVISE-135 (growth-as-health) — coupled, closed mostly by one canary/contract assertion + a value-normalized metric. REVISE-133 (intake-as-progress) is the direct corollary-error of the INCORPORATEd review-bound premise (PREMISE-070), closed by a WIP limit. Priority order for Tom: REVISE-136 (HIGH, load-bearing transfer) > REVISE-132/134 (bridge + telemetry durability) > REVISE-131/133/135 (scope-narrowing / cheap-fix).

### REVISE-137 — PRESUMPTION-377 (inbound-backlink count = graph health (vanity-metric smuggle))
**Statement:** [inferred] That inbound-backlink count is the right proxy for graph health at all (connectivity measured, synthesis quality never)
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Strong)
**What is at risk:** The audit's whole notion of 'graph health' may track a vanity metric; connectivity is optimized while synthesis quality is never measured and may decline.
**Recommended action:** Urgency Low-Medium. Pair connectivity with at least one synthesis-quality metric (validated cross-tradition syntheses per unit graph change); never make backlink count an optimization target; ensure the index-node move (344/381) cannot game it. Twin of ASSUMPTION-338 (MONITOR-363); metric-direction family (367/375).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-138 — PRESUMPTION-378 (orphan exclusion is principled (motivated-reclassification risk))
**Statement:** [inferred] That excluding 2,112 orphans as 'should not carry backlinks' is principled, not a motivated reclassification that erases the alarm
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Strong)
**What is at risk:** A standing, human-tracked orphan alarm is retired on an unregistered, possibly outcome-driven denominator change; a real connectivity problem could become invisible.
**Recommended action:** Urgency Medium. Pre-register the page-class exclusion criterion (independent of the count); report orphan rate WITH and WITHOUT exclusions; route the reclassification through human review before it changes the alarm's tracked status. Tension-twin of ASSUMPTION-339 (MONITOR-364).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-139 — PRESUMPTION-379 (own corrected resolver trusted with no cross-check (asymmetric self-trust))
**Statement:** [inferred] That the audit's own corrected (path-aware) resolver is now bug-free — production resolver flagged, own resolver trusted with no cross-check
**15a:** NO-SUPPORT-FOUND (Weak) | **15b:** CHALLENGED (Strong)
**What is at risk:** The 'corrected' (path-aware) connectivity series could be wrong in a new way; the audit would have swapped a flagged silent miscount for an unflagged, trusted one.
**Recommended action:** Urgency Medium. Cross-validate the new resolver against a labelled link-form test set and a second independent implementation; require agreement before adopting its recount; add a fail-loud check for ambiguous/unresolved links. Couples PREMISE-072. Member of the EXTENDED silent-measurement / fail-loud cluster (369/373/MONITOR-296/PREMISE-049).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-140 — PRESUMPTION-380 (keyword/page-unit is the right instrument for cross-tradition relevance)
**Statement:** [inferred] That a 14-thinker keyword/relevance score (>0.4) is the right instrument for cross-tradition relevance, merely mis-tuned (page-as-unit / keyword-match unexamined)
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**What is at risk:** Cross-tradition seeding driven by a keyword score surfaces lexical coincidences and misses genuine conceptual bridges — low precision AND recall on exactly the links that matter.
**Recommended action:** Urgency Medium. Use embedding/semantic relevance (or a hybrid keyword+embedding) at passage/claim granularity, not keyword-over-pages; validate precision/recall against a labelled cross-tradition set before seeding. Gates OPEN-088 with ASSUMPTION-345 (MONITOR-366); instrument/demand-completeness theme (with 384).
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-141 — PRESUMPTION-381 (more inbound hub connectivity is simply good (universal-hub dilution))
**Statement:** [inferred] That more inbound hub connectivity is simply good — an all-to-one index node may dilute the sociogram's signal (connects-all = distinguishes-nothing)
**15a:** NO-SUPPORT-FOUND (Weak) | **15b:** CHALLENGED (Moderate-Strong)
**What is at risk:** Adding a universal index node (344) inflates connectivity counts while degrading the sociogram and community detection — improving the watched number and worsening the interpreted structure.
**Recommended action:** Urgency Low-Medium. Exclude or down-weight universal/index hubs in sociogram and community-detection pipelines; evaluate connectivity changes by their effect on community legibility (modularity), not raw inbound count. The withheld over-claim of ASSUMPTION-344 (PREMISE-074) and value-side of ASSUMPTION-340; member of the connectivity-metric-validity cluster; twin of 340/344.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-142 — PRESUMPTION-382 (autonomous run may authoritatively reframe a human-tracked alarm (interpretive-caution gap))
**Statement:** [inferred] That a one-night autonomous census can authoritatively reframe a standing human-tracked alarm — write-caution applied, interpretive-caution not
**15a:** PARTIALLY-SUPPORTED (Weak-Moderate) | **15b:** CHALLENGED (Moderate-Strong)
**What is at risk:** A human-tracked alarm is effectively closed by an unattended run's interpretation; the human loses a tracked signal without reviewing the reframe, and downstream readers treat it as settled (automation bias).
**Recommended action:** Urgency Medium. Allow autonomous runs to PROPOSE reframes flagged provisional pending Tom's review; do not autonomously change a human-tracked alarm's status; log interpretive moves distinctly from measurements. Extends PREMISE-073 (342): write-caution incorporated, interpretive-caution added here.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

### REVISE-143 — PRESUMPTION-384 (absence of broken links = no bridges needed (self-justifying demand signal — KEYSTONE))
**Statement:** [inferred] That absence of broken bridge links = no synthesis bridges needed (the graph can only request bridges someone already stubbed — self-justifying)
**15a:** NO-SUPPORT-FOUND (Weak) | **15b:** CHALLENGED (Strong)
**What is at risk:** The system could conclude its cross-tradition synthesis coverage is complete when it is not, leaving the most valuable non-obvious bridges permanently unbuilt because nothing flags them.
**Recommended action:** Urgency High. Enumerate warranted cross-tradition bridges independently of broken links (embedding link-prediction over the PRS connectome; structured cross-tradition pairing); treat broken-link demand as a LOWER BOUND on need, never as completeness. Tension-twin of ASSUMPTION-343 (MONITOR-365); KEYSTONE of the cohort's instrument/demand-completeness concern. Tom to review as the cohort's priority item.
**Status:** AWAITING-REVIEW
**PROVENANCE:** Origin: 14b; Chain: [14b -> 15a, 15b -> 15c]; Current status: REVISION-FLAGGED

**Total new REVISEs this run (2026-06-24):** 7 (REVISE-137..143). **AWAITING-REVIEW backlog: was 90 -> now 97.** Driven by two SYSTEMIC-RISK clusters. NEW cluster 7 (connectivity-metric validity / vanity-metric — a structural connectivity COUNT treated as graph HEALTH, gameable by index nodes and scope changes): REVISE-137 (backlink-as-health), REVISE-138 (motivated reclassification), REVISE-141 (universal-hub dilution) — with ASSUMPTION-344 (PREMISE-074) scope-guarded against it; Risk High. EXTENDED cluster 5 (silent-measurement / fail-loud): REVISE-139 (uncross-checked replacement resolver), joining PREMISE-072 (basename miscount) and prior 369/373/MONITOR-296/PREMISE-049 — closed by one cross-check + fail-loud assertion. Instrument/demand-completeness sub-theme: REVISE-140 (keyword instrument) + REVISE-143 (broken-link demand, KEYSTONE) + MONITOR-365 — the audit's instruments under-detect what to connect. Governance: REVISE-142 (interpretive-caution gap) complements the INCORPORATEd write-caution (PREMISE-073). Priority order for Tom: REVISE-143 (HIGH, synthesis-coverage completeness) > REVISE-138/139/140/142 (MED) > REVISE-137/141 (LOW-MED).


## 2026-06-24 cohort REVISE (15c 2026-06-25; for Tom's review)

REVISE-144:
  Date: 2026-06-25
  Source item: ASSUMPTION-359 (ASSUMPTION (stated))
  Disposition: REVISE (DISPOSITION-311)
  Net assessment: 15a weak, 15b strong, and the assumption contains a factual error ('never written to disk'). Clear net-negative.
  What is at risk: Client-side API-key confidentiality for the public artifact; user trust in a posture OWASP rates a critical risk.
  Recommended action: Correct the 'never on disk' claim; hold keys in-memory/Web Worker only or proxy via a backend-for-frontend; if web storage is unavoidable, document the XSS residual risk explicitly and minimize lifetime.
  Urgency: Medium
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED

REVISE-145:
  Date: 2026-06-25
  Source item: PRESUMPTION-386 (PRESUMPTION (unstated))
  Disposition: REVISE (DISPOSITION-314)
  Net assessment: 15a none, 15b strong, AND the presumption contradicts an existing validated premise (MMA-independence: same-formation agreement is discounted).
  What is at risk: Pathway 31's entire consensus/confidence semantics; the constitutional detector's reliability claims.
  Recommended action: Replace vote-count confidence with a function of MEASURED effective independence (pairwise error correlation / effective N); diversify base models or strongly diversify prompting; reconcile with the existing MMA-independence premise. Keystone of consensus-validity cluster.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED

REVISE-146:
  Date: 2026-06-25
  Source item: PRESUMPTION-394 (PRESUMPTION (unstated))
  Disposition: REVISE (DISPOSITION-322)
  Net assessment: 15a weak, 15b strong; a presumption mislabeling a mitigated self-audit as 'genuine independence'. Partial closure of REVISE-111 is undermined by the independence gap.
  What is at risk: The falsifier's claim to independent oversight; the epistemic status recorded in provenance; partial closure of REVISE-111.
  Recommended action: Recruit an external or blinded second party for the audit; if infeasible, relabel as 'owner self-audit (not independent)' and lean on pre-registration + the adversarial 15b search; do not record it as 'genuine independence'.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED

REVISE-147:
  Date: 2026-06-26
  Source item: PRESUMPTION-398 (PRESUMPTION (unstated))
  Disposition: REVISE (DISPOSITION-332)
  Net assessment: 15a none, 15b strong; a PRESUMPTION on a demo-critical liveness claim that recapitulates the unfixed keystone OPEN-086 (app-gated execution with no non-execution detection).
  What is at risk: Heartbeat freshness guarantees; demo credibility; propagation of the keystone OPEN-086 silent-stall gap to a new surface.
  Recommended action: Add an external heartbeat/dead-man's-switch that alerts on missed runs ('absence is the signal'); move scheduling off app-gating to OS supervision (launchd/cron); surface true last-run age and an explicit 'stale' state. Member of the silent-failure systemic cluster; bind to OPEN-086.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED

REVISE-148:
  Date: 2026-06-26
  Source item: PRESUMPTION-402 (PRESUMPTION (unstated))
  Disposition: REVISE (DISPOSITION-336)
  Net assessment: 15a none, 15b strong; a PRESUMPTION that human vigilance reliably partitions a dirty tree with no structural guard - contradicted by human-error and hierarchy-of-controls evidence.
  What is at risk: Accidental commit of 39 agent-WIP files (continuous, not per-event exposure); polluted/leaky git history.
  Recommended action: Replace correct-by-attention with correct-by-construction: dedicated worktree/branch so WIP is absent from the commit surface, or sparse-checkout + a pre-commit hook asserting the allowed fileset. Member of the correct-by-construction systemic cluster.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED

REVISE-149:
  Date: 2026-06-26
  Source item: PRESUMPTION-406 (PRESUMPTION (unstated))
  Disposition: REVISE (DISPOSITION-340)
  Net assessment: 15a weak, 15b strong; a PRESUMPTION that the 06-23 approval/proposal mismatch is a reconcilable tooling defect with a recoverable ground truth, despite position-based decision IDs (a known anti-pattern with no recovery anchor once order drifts).
  What is at risk: Five governance approvals possibly un/mis-attributable; auditability and trust in the governance/decision record.
  Recommended action: Replace positional decision IDs with stable immutable IDs + an append-only audit log + idempotency keys (correct-by-construction). For the EXISTING mismatch, attempt recovery ONLY via an independent stable-keyed record; if none exists, record the five approvals as unverifiable rather than guessing a reconciliation. Member of the correct-by-construction systemic cluster.
  Urgency: Medium-High
  PROVENANCE: Origin 14b; Chain [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED

REVISE-150:
  Date: 2026-06-27
  Source item: PRESUMPTION-412 (PRESUMPTION (unstated))
  Disposition: REVISE (DISPOSITION-352)
  Net assessment: 15a none, 15b moderate-strong; a PRESUMPTION that deferred pushes converge - contradicted by the CI/DORA evidence base, which says deferred integration accumulates debt. Three sessions staged-not-pushed over an already-mixed tree is the long-lived-divergence anti-pattern. Cross-session form of PRESUMPTION-402 (REVISE-148).
  What is at risk: Merge conflicts/regressions and entangled or lost WIP across three accumulated sessions; an already-mixed tree pushed with unintended files; growing unreviewed divergence.
  Recommended action: Enforce a push cadence / WIP limit (integrate per session); use worktree/branch isolation so each session is independently pushable (extends REVISE-148 from commit-surface to push-cadence); fail loud when unpushed sessions exceed a threshold. Member of the correct-by-construction systemic cluster.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED

REVISE-151:
  Date: 2026-06-27
  Source item: PRESUMPTION-413 (PRESUMPTION (unstated))
  Disposition: REVISE (DISPOSITION-353)
  Net assessment: 15a none, 15b strong; a PRESUMPTION that a fixed-time evening sync captures "the day". Streaming theory (watermarking / late-arriving data) says a wall-clock cutoff cannot capture after-cutoff events, and the system PROVED it - it labeled an attended day "autonomous" and missed three same-evening interactive sessions. This is a reflexive false-negative on the pipeline's OWN OPEN-086 liveness reporting (the worst failure class, already realized).
  What is at risk: Days mislabeled (attended vs autonomous); same-evening events lost from the record; the self-awareness pipeline misreporting its own liveness. Binds OPEN-097.
  Recommended action: Replace the fixed evening cutoff with event-driven/append capture or watermark-aware windowing with allowed-lateness; re-scan the prior window on the next run to absorb late events; never finalize a day-label from a single pre-evening snapshot; fail loud if post-sync activity is detected. Member of the silent-failure / fail-loud systemic cluster.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a, 15b -> 15c]; Transform: net evaluation and disposition; Current status: REVISION-FLAGGED

## 2026-06-29 intake (15c; from 2026-06-28 EOD cohort) — REVISE-152..154 (for Tom's review)

REVISE-152:
  Date: 2026-06-29 | Source: DISPOSITION-358 | Item: ASSUMPTION-387 (stated) | Urgency: MEDIUM
  Claim flagged: "Deterministic path/size heuristics correctly classify 2,984 orphan+sparse pages into A-E."
  15a/15b: PARTIALLY-SUPPORTED(Weak-Mod) / CHALLENGED(Moderate-Strong)
  What is at risk: downstream triage actions keyed to the A-E buckets; misclassified high-value short pages treated as disposable.
  Why flagged: metadata-only classification is documented everywhere as an approximation needing a content backstop; file size is an especially weak proxy for content type/value; "correctly classify" is an unaudited accuracy claim over ~3,000 pages.
  Recommended action: run a sampled CONTENT audit (50-100 random pages, hand-classify, compare to heuristic) to estimate error rate before trusting A-E; add a content-based confidence fallback for ambiguous pages; treat A-E labels as PROVISIONAL meanwhile.
  Binds: REVISE-153 (its unstated twin); member of the STRUCTURAL-PROXY-AS-GROUND-TRUTH systemic-risk cluster.

REVISE-153:
  Date: 2026-06-29 | Source: DISPOSITION-360 | Item: PRESUMPTION-415 (unstated) | Urgency: HIGH
  Claim flagged: "[inferred] directory path + file size reliably indicate content type and synthesis value (folder taxonomy as ground truth; no misfiled/mis-sized content)."
  15a/15b: PARTIALLY-SUPPORTED(Weak) / CHALLENGED(Moderate-Strong)
  What is at risk: any pipeline step that trusts folder/size as content truth without a content check.
  Why flagged: unstated twin of ASSUMPTION-387 in stronger form (asserts RELIABILITY as ground truth). Folder taxonomies decay in growing repos; metadata mislabels when incomplete; size barely encodes content. Elevated urgency because it is a PRESUMPTION (designers were unaware they were treating taxonomy as ground truth) + strong challenge.
  Recommended action: treat path/size as PRIORS, not ground truth; the REVISE-152 content audit doubles as the test for this presumption; flag and content-check any page whose size/location conflicts with its apparent role.
  Binds: REVISE-152 (surfaced-not-averaged: stated assumption + unstated twin flagged together, not blended).

REVISE-154:
  Date: 2026-06-29 | Source: DISPOSITION-363 | Item: PRESUMPTION-418 (unstated) | Urgency: HIGH
  Claim flagged: "[inferred] orphan-detection should have a single canonical owner; bootstrap-beside-weekly is wasteful 'double-counting' rather than a useful redundant cross-check."
  15a/15b: PARTIALLY-SUPPORTED(Mod) / CHALLENGED(STRONG)
  What is at risk: liveness/dead-man's-switch coverage for orphan detection; the project's standing defense-in-depth posture.
  Why flagged: INTERNALLY INCONSISTENT with validated PREMISE-086 (monitor-of-monitor / dead-man's-switch / "absence is the signal"). Defense-in-depth literature treats independent overlapping detectors as a FEATURE; the deduplication/single-ownership case applies to FINDINGS, not DETECTORS. Collapsing to one detector reintroduces a single point of failure for liveness — exactly what PREMISE-086 exists to prevent. Per 15c consistency rule, a new claim contradicting an existing PREMISE is flagged for human review; PREMISE-086 is NOT overwritten.
  Recommended action: keep bootstrap + weekly orphan-detection as INDEPENDENT detectors; deduplicate the FINDINGS (one ticket per orphan) while preserving two detectors; ALARM ON DISAGREEMENT between them. If consolidation is still desired for cost, require an explicit liveness check on the sole remaining detector.


## 2026-06-30 — REVISE intake (from 2026-06-29 cohort dispositions)

REVISE-155:
  Date: 2026-06-30 | Source: DISPOSITION-368 | Item: PRESUMPTION-419 (presumption) | Urgency: HIGH
  Claim flagged: "That the count rate of cross-tradition signals (signals/day) is a valid proxy for synthesis yield — more signals = more genuine production, never asking whether volume tracks insight or noise."
  15a/15b: PARTIALLY-SUPPORTED(Weak-Moderate) / CHALLENGED(Strong)
  Net: Weak conditional support only as a paired/non-targeted indicator (15a) against a STRONG Goodhart challenge to the unexamined volume=yield equivalence (15b). The presumption is unstated and the designers were unaware they had adopted it.
  What is at risk: The metabolism 'amplitude' display and any curation/agent behavior that optimizes toward signal count; the project's credibility if 'productivity' is noise.
  Recommended action: Do not display signals/day as productivity until it is paired with a homology/quality counterweight and a spot-audit confirms count tracks genuine-homology yield. (Same verify-before-trust family as PREMISE-086 / the 2026-06-29 content-audit remedy.)
  Urgency: High
  Why flagged: PRESUMPTION + strong challenge + membership in the active 'structural-proxy-as-ground-truth' SYSTEMIC-RISK cluster -> REVISE (HIGH). Mirrors the prior-cycle handling of P-414 (connectivity-as-proxy -> MONITOR-403 HIGH) but here the proxy is displayed as a headline 'productivity' axis, raising urgency.

REVISE-156:
  Date: 2026-06-30 | Source: DISPOSITION-369 | Item: PRESUMPTION-420 (presumption) | Urgency: MED-HIGH
  Claim flagged: "That attended-gating of PRS extraction buys enough quality to justify its cost — the quality benefit is unmeasured while the gate freezes axes 12 days and queues ~68 cards."
  15a/15b: PARTIALLY-SUPPORTED(Weak-Moderate) / CHALLENGED(Moderate-Strong)
  Net: Conditional support for the trade IF the benefit were bounded (15a), but a moderate-strong challenge because the benefit is unmeasured while the cost (12-day freeze, ~68 cards) is concrete and observed (15b). Unstated presumption.
  What is at risk: Liveness of the PRS/signals approval axes and backlog growth; the legitimacy of the gating policy (DECISION) itself.
  Recommended action: Time-box the gate and instrument it — sample-measure the quality delta attended-vs-unattended on a handful of triplets; if the delta is small, move to confidence-routed selective gating so low-risk extraction does not freeze the axes.
  Urgency: Medium-High
  Why flagged: PRESUMPTION + moderate-strong challenge + a faith-based cost-benefit claim with a measured downside -> REVISE (Medium-High). The remedy is cheap relative to the stakes: measure the quality benefit or time-box/selectively-route the gate. Binds A-389 (the stated form, MONITOR-407).

REVISE-157:
  Date: 2026-06-30 | Source: DISPOSITION-370 | Item: PRESUMPTION-421 (presumption) | Urgency: HIGH
  Claim flagged: "That a human will notice metric staleness and trigger regen by hand — "someone will look" as the liveness mechanism, no watchdog; freeze ran 06-17→06-29 undetected until a chance question."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: No support and a strong challenge backed by a 12-day undetected freeze and by the system's own PREMISE-086 (monitor-of-monitor). 'Someone will notice' is the anti-pattern automated freshness monitoring exists to replace.
  What is at risk: Liveness of every approval/metric axis; the credibility of the heartbeat/metabolism display; consistency with PREMISE-086.
  Recommended action: Add an automated freshness watchdog — per-axis next-expected-update SLA that alarms (fail-loud) when an axis exceeds its freshness budget. This is the dead-man's-switch of PREMISE-086 / REVISE-147 applied to the dashboard feeds.
  Urgency: High
  Why flagged: PRESUMPTION + strong challenge + direct contradiction of validated PREMISE-086 + live operational failure -> REVISE (HIGH). Per the 15c consistency rule, a claim contradicting an existing premise is flagged for human review rather than allowed to stand. The remedy is the same dead-man's-switch pattern already validated.

REVISE-158:
  Date: 2026-06-30 | Source: DISPOSITION-371 | Item: PRESUMPTION-422 (presumption) | Urgency: HIGH
  Claim flagged: "That a stale axis displayed beside a fresh one (no per-axis as-of marking) is acceptable — viewer presumed to attribute each axis its own freshness; the most expert viewer was in fact misled."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: No support and a strong, operationally-confirmed challenge: per-axis 'data last updated' marking is documented best practice and its absence misled the most expert viewer. Directly downstream of A-390 (feeds are independent).
  What is at risk: Trustworthiness of the metabolism/heartbeat display; any decision read off a mixed-freshness board.
  Recommended action: Add per-axis as-of timestamps (and/or color-coded staleness) to each approval/metric axis so freshness is read at the point of use. This operationalizes PREMISE-089 and is a small UI change.
  Urgency: High (low effort)
  Why flagged: PRESUMPTION + strong challenge + live mislead of the actual expert user + it is the positive obligation implied by the just-INCORPORATED PREMISE-089 -> REVISE (HIGH but low-cost fix). Binds PREMISE-089 and P-421 (the watchdog).

REVISE-159:
  Date: 2026-06-30 | Source: DISPOSITION-373 | Item: PRESUMPTION-424 (presumption) | Urgency: MED
  Claim flagged: "That auto-stashing ~20 unrelated working-tree files every push is safe and a clean win — normalizes a chronically dirty working tree instead of resolving the persistent uncommitted files (push-debt)."
  15a/15b: PARTIALLY-SUPPORTED(Weak) / CHALLENGED(Moderate-Strong)
  Net: Weak support for the mechanism's convenience (15a) against a moderate-strong challenge to the HABIT: normalizing a chronically dirty ~20-file tree is push-debt entrenchment, the working-tree form of REVISE-150's deferred-push accumulation (15b). Unstated presumption.
  What is at risk: Working-tree integrity and push reliability; compounding push-debt across sessions (with REVISE-150).
  Recommended action: Resolve the ~20 persistent uncommitted files at the source — commit the intentional ones, .gitignore the local-only artifacts, remove the strays — so the tree is clean and autostash becomes an occasional convenience, not a per-push crutch.
  Urgency: Medium
  Why flagged: PRESUMPTION + moderate-strong challenge + membership in the push-debt cluster (PRESUMPTION-412/REVISE-150) -> REVISE (Medium). The remedy is concrete and cheap (resolve the ~20 files: commit, .gitignore, or remove), which retires the debt rather than automating around it. Binds A-391 (the stated mechanism, MONITOR-409).


REVISE-160:
  Date: 2026-07-01 | Source: DISPOSITION-375 | Item: ASSUMPTION-394 (assumption) | Urgency: MED
  Claim flagged: "A clean connectome regen (288->432, +144, node --check + count-match + content-population green) is sufficient verification of ingestion correctness."
  15a/15b: PARTIALLY-SUPPORTED(Moderate) / CHALLENGED(Strong)
  Net: Structural checks are necessary and standard but NOT sufficient — blind to semantic errors and to compensating errors that net to an exact count (P-426). Classic false-green.
  What is at risk: Ingestion correctness of claim cards feeding the connectome and premise register.
  Recommended action: Add an identity + semantic layer to the gate — verify expected proposal_id SET (not count), duplicate/near-duplicate scan, sampled content-fidelity check vs source cards. Bind REVISE-162.
  Urgency: Medium
  Why flagged: stated ASSUMPTION whose operative word "sufficient" is strongly contradicted; fix is additive/cheap.

REVISE-161:
  Date: 2026-07-01 | Source: DISPOSITION-379 | Item: PRESUMPTION-425 (presumption) | Urgency: HIGH
  Claim flagged: "That a one-shot attended backlog clear keeps the PRS axis live — no cadence change, so re-accumulation is unaddressed (OPEN-102 remains)."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: Lean backlog literature — a one-shot clear without cadence change re-accumulates, often bigger (symptom not cause). OPEN-102 remaining open is the tell. Unstated presumption.
  What is at risk: The PRS approval axis silently re-freezes post-clear, reviving the 12-day-freeze failure mode (REVISE-156/157) under a false "handled" sense.
  Recommended action: Pair the one-shot clear with a durable mechanism — standing bounded ingestion cadence (human-on-the-loop) and/or a PRS-axis freshness watchdog (bind REVISE-157). Resolve OPEN-102.
  Urgency: High
  Why flagged: PRESUMPTION + strong challenge + no support + revives a known keystone failure mode. Pairs with PREMISE-090's scope caveat.

REVISE-162:
  Date: 2026-07-01 | Source: DISPOSITION-380 | Item: PRESUMPTION-426 (presumption) | Urgency: MED-HIGH
  Claim flagged: "That an exact count-match (+144) proves content correctness — presumes no compensating (drop-plus-wrong-add) errors."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: Compensating/offsetting errors are a named failure class; equal counts routinely hide two errors that cancel. Downstream of A-394's "sufficient."
  What is at risk: Wrong/misattributed cards enter the connectome undetected because the headline +144 matched.
  Recommended action: Replace count-match with identity-set verification (expected_ids symmetric-difference present_ids == empty) + content spot-check. Bind REVISE-160.
  Urgency: Medium-High
  Why flagged: PRESUMPTION + strong challenge; decisive cheap fix.

REVISE-163:
  Date: 2026-07-01 | Source: DISPOSITION-381 | Item: PRESUMPTION-427 (presumption) | Urgency: HIGH
  Claim flagged: "That fixing one identity-keying bug makes the toolchain trustworthy — a second audit-identity divergence (qc_trace) appeared same session."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: Defect clustering/pesticide paradox predicts more keying bugs where one was found; the same-session qc_trace divergence empirically confirms the class was not eliminated.
  What is at risk: Silent identity/keying mismatches elsewhere corrupt audit trails and ingestion identity while the toolchain is presumed trustworthy.
  Recommended action: Systematic keying-identity audit across ALL joins (proposal_id, qc_trace, filename surfaces); assert one stable key, no surface-key joins remain. Bind REVISE-164.
  Urgency: High
  Why flagged: PRESUMPTION + strong challenge + live empirical confirmation same session.

REVISE-164:
  Date: 2026-07-01 | Source: DISPOSITION-382 | Item: PRESUMPTION-428 (presumption) | Urgency: MED-HIGH
  Claim flagged: "That a wrong audit CSV is acceptable if vault content is correct + a guard is added — treats provenance correctness as secondary to the artifact."
  15a/15b: PARTIALLY-SUPPORTED(Weak) / CHALLENGED(Strong)
  Net: For an audit/provenance artifact the correctness of the trail IS the product; a known-wrong CSV voids the guarantee it exists to provide — self-referentially central to C2A2 (provenance_protocol.md). A forward guard does not repair the known-wrong record.
  What is at risk: The audit CSV is later trusted as authoritative provenance; C2A2's chain-of-custody guarantee is silently false; future audits build on a corrupt baseline.
  Recommended action: Regenerate the audit CSV from source-of-truth to match the vault, THEN keep the guard. Treat provenance correctness as first-class. Bind REVISE-163.
  Urgency: Medium-High
  Why flagged: PRESUMPTION + strong challenge + self-referential provenance stakes.

REVISE-165:
  Date: 2026-07-01 | Source: DISPOSITION-384 | Item: PRESUMPTION-430 (presumption) | Urgency: MED
  Claim flagged: "That 'fast turn + measurably-larger connectome' is a success signal — smuggles a velocity/growth norm into a quality-gated pipeline."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Moderate-Strong)
  Net: Goodhart — a growth/speed proxy treated as the success signal in a quality-gated pipeline invites optimizing size/speed at the expense of quality. Member of the standing structural-proxy / measurement-validity cluster (P-414, A-388/P-419).
  What is at risk: The pipeline is optimized for turn-speed and node-count, eroding the quality gate; growth masks quality regressions.
  Recommended action: Report speed/connectome-size as neutral operational stats, never as success; define run success solely by quality-gate outcomes (identity/semantic correctness, provenance integrity).
  Urgency: Medium
  Why flagged: PRESUMPTION + moderate-strong challenge + membership in the measurement-validity SYSTEMIC-RISK cluster.

REVISE-166:
  Date: 2026-07-01 | Source: DISPOSITION-385 | Item: PRESUMPTION-431 (presumption) | Urgency: MED
  Claim flagged: "That the recurring stale git index.lock is benign routine noise rather than a concurrency symptom (heartbeat cron vs attended commits)."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: Recurring stale index.lock is a documented concurrency symptom (heartbeat cron racing attended commits = the write-vs-write race the lock guards), with a recognized escalation path to index/ref corruption and a concrete fix.
  What is at risk: Concurrent git writers interleave into index/ref corruption; attended commits fail or are silently blocked; the repo state the whole C2A2 pipeline reads from is corrupted.
  Recommended action: Serialize git access (repo-level lock/queue around commits); set GIT_OPTIONAL_LOCKS=0 / --no-optional-locks for the heartbeat cron's read-only git; run git fsck for existing damage. Relates to REVISE-147 (scheduler dead-man's-switch).
  Urgency: Medium
  Why flagged: PRESUMPTION + strong documented challenge (incl. Claude Code issue tracker); plausibly the root of the recurring-lock family.

REVISE-167:
  Date: 2026-07-02 | Source: DISPOSITION-387 | Item: PRESUMPTION-432 (presumption) | Urgency: MED-HIGH
  Claim flagged: "That the compute sandbox's ephemeral disk is unbounded/self-managing — no monitoring or scratch GC, so a full container disk silently halts any agent needing local writes."
  15a/15b: NO-SUPPORT-FOUND(Weak) / CHALLENGED(Strong)
  Net: Ephemeral disk is a bounded, exhaustible, poorly-visible resource (K8s disk-pressure eviction; poor default visibility) that must be explicitly monitored, quota'd, and GC'd. "Unbounded/self-managing" is exactly the belief that produced the silent halt.
  What is at risk: Agents needing local writes halt/evict silently on scratch exhaustion; node-level exhaustion can affect co-located work; the halt is misattributed to downstream symptoms (P-433 / REVISE-168).
  Recommended action: Add ephemeral-disk monitoring with a threshold alert; set scratch quotas; implement scratch GC/cleanup (within and between runs); fail loud with an explicit "disk full" error instead of halting silently. Bind the liveness/observability cluster (REVISE-147/157/158).
  Urgency: Medium-High
  Why flagged: PRESUMPTION + strong challenge + medium-high stakes; root cause of the 2026-07-01 incident; core member of the ABSENCE-AS-EVIDENCE / silent-infrastructure SYSTEMIC-RISK cluster.

REVISE-168:
  Date: 2026-07-02 | Source: DISPOSITION-388 | Item: PRESUMPTION-433 (presumption) | Urgency: MED
  Claim flagged: "That the disk-full failure is isolated to the OpenStory feed, when one full compute disk produced two symptoms attributed to two separate problems."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Moderate-Strong)
  Net: One exhausted resource characteristically produces multiple seemingly-independent symptoms (AWS correlated-failure library; microservice root-cause literature). Per-symptom attribution is a documented misdiagnosis pattern; the isolation reading is itself an absence-as-evidence move ("no traced common cause" => "isolated").
  What is at risk: Fixing only the OpenStory symptom leaves the shared cause (full disk) live; the second symptom recurs and is re-triaged as another "separate" problem; root cause never retired.
  Recommended action: On any multi-symptom day, check shared resources (disk/memory/session) FIRST; add a root-cause-aggregation step correlating co-occurring anomalies to common substrates before filing them independently. Binds REVISE-167 (the shared cause here was disk).
  Urgency: Medium
  Why flagged: PRESUMPTION + strong challenge; cheap diagnostic-discipline fix; member of the silent-infrastructure cluster.

REVISE-169:
  Date: 2026-07-02 | Source: DISPOSITION-389 | Item: PRESUMPTION-434 (presumption) | Urgency: MED-HIGH
  Claim flagged: "That a 2nd-day logged-out claude.ai is transient/self-healing, not a single point of failure in the human-context loop with no fallback or escalation."
  15a/15b: NO-SUPPORT-FOUND(Weak) / CHALLENGED(Strong)
  Net: A recurring (2nd-day) logged-out state with no fallback or escalation is a textbook single point of failure, not self-healing (SPOF definition; heartbeat/dead-man's-switch; HITL escalation). "A human can fix it" != "it self-heals" — with no escalation the human is never prompted.
  What is at risk: The human-context loop silently stays degraded across runs; autonomous work proceeds on stale context or stalls with no alert; one expired session halts the whole loop.
  Recommended action: Add escalation/alerting on logout (surface to Tom); provide a fallback/degraded-mode path so a single expired session does not halt everything; track logout recurrence as a reliability metric. Pairs directly with PREMISE-093 (hard-stop-must-escalate) and REVISE-147 (dead-man's-switch).
  Urgency: Medium-High
  Why flagged: PRESUMPTION + strong challenge + recurrence evidence + human-context-loop stakes.

REVISE-170:
  Date: 2026-07-02 | Source: DISPOSITION-390 | Item: PRESUMPTION-435 (presumption) | Urgency: MED
  Claim flagged: "That 'no changelog logged' means 'quiet day, nothing to track,' when automated state changes occurred and the summary's counts diverged from the registry."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: The canonical absence-as-evidence fallacy (abyrint/arXiv silent-failure; watchflow cron; Databricks/DQLabs data-observability). A divergence between summary counts and the source-of-truth registry is affirmative evidence of unlogged automated activity; missing logs are a heartbeat/reconciliation prompt, not an all-clear.
  What is at risk: Automated state changes go untracked; the changelog silently under-reports; summary/registry drift accumulates and erodes trust; post-hoc reconstruction becomes impossible once the window passes.
  Recommended action: Reconcile the daily summary against the source-of-truth registry (counts must match or the diff is surfaced / fails loud); emit a positive heartbeat for autonomous activity so a genuinely quiet day is confirmed rather than inferred from silence. Binds PREMISE-006 (transparent-flagging) and REVISE-167 family.
  Urgency: Medium
  Why flagged: PRESUMPTION + strong challenge + already-observed drift (divergent counts) + trivial fix; core member of the ABSENCE-AS-EVIDENCE SYSTEMIC-RISK cluster.

## 2026-07-03 intake (15c; from 2026-07-02 EOD Inter-Tradition Dialogue Study cohort) — REVISE-171..174 (for Tom's review)
## SYSTEMIC-RISK (new, High): AI-IN-THE-LOOP EVIDENTIAL VALIDITY cluster — the study's human/philosophical conclusions chain through four unvalidated links below (agent fidelity, metric construct validity, generate/analyze independence, direction-neutral framing) feeding ASSUMPTION-408 (now MONITOR-414). Validate each link before banking any human-tradition or anti-pessimism claim.

REVISE-171:
  Date: 2026-07-03 | Source: DISPOSITION-395 | Item: PRESUMPTION-436 (presumption) | Urgency: HIGH
  Claim flagged: "That AI tradition-agents instantiate the human traditions faithfully enough that agent-dialogue is evidence about human-tradition interaction (transfer unchecked)."
  15a/15b: PARTIALLY-SUPPORTED(Weak, aggregate-only) / CHALLENGED(Strong)
  Net: Silicon-persona work shows heterogeneity collapse, stereotype amplification, and fidelity that DEGRADES with persona richness (arXiv 2604.23575; 2507.02919); support is confined to aggregate distributions. C2A2's own ASSUMPTION-007 was already strong-challenged/REVISE (2026-04-13). This is the external-validity crux of the whole study.
  What is at risk: Every "human-tradition interaction" conclusion; agent artifacts (stereotype-amplified concord/conflict) mistaken for tradition dynamics; feeds ASSUMPTION-408's bearing claim.
  Recommended action: Add an agent-to-human fidelity validation on a subset (run the same protocol with human tradition-holders; check effect sign + rough magnitude replicate); until then scope all findings to "agent interaction, provisionally suggestive about humans." Binds ASSUMPTION-007 and the AI-in-the-loop SYSTEMIC-RISK.
  Urgency: High
  Why flagged: PRESUMPTION + strong challenge + whole-study external validity at stake + concrete unperformed check; primary node of the AI-in-the-loop cluster.

REVISE-172:
  Date: 2026-07-03 | Source: DISPOSITION-396 | Item: PRESUMPTION-437 (presumption) | Urgency: MED-HIGH
  Claim flagged: "That 'understanding' is a single quantity a numeric score validly tracks — construct validity of the understanding metric is unexamined."
  15a/15b: NO-SUPPORT-FOUND(Weak, procedural) / CHALLENGED(Strong)
  Net: Mainstream measurement theory treats understanding/comprehension as multidimensional; single-score validity requires construct work (Cronbach-Meehl 1955; Messick 1995) the item concedes is undone. A score change could reflect one sub-dimension (e.g. lexical overlap), not "understanding."
  What is at risk: The headline effect (A-404's +0.086), the robust/directional/null sort (P-439), and the MacIntyre bearing claim (A-408) all inherit a metric of unknown construct validity.
  Recommended action: Construct-validate the metric — factor structure; convergent validity vs author-ratification and blind human raters; discriminant validity vs pure lexical overlap (the study's own C0 finding that the lexical limb "does no real work" is a start); report sub-scores where they diverge. Binds A-408, A-404, REVISE-171.
  Urgency: Medium-High
  Why flagged: PRESUMPTION + strong challenge + foundational (underlies every downstream effect); remediable but currently unvalidated.

REVISE-173:
  Date: 2026-07-03 | Source: DISPOSITION-398 | Item: PRESUMPTION-440 (presumption) | Urgency: MED-HIGH
  Claim flagged: "That evidence FOR MacIntyre's project is the desirable outcome — an 'against pessimism' framing smuggles the sought direction into the tool."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: Preferred-direction framing with subjective measures and no blinding is a documented effect-inflating channel — allegiance effect (Dragioti 2015), observer-expectancy (Rosenthal), blind-recording need (Holman 2015), confirmation bias (Nickerson). The framing is a bias channel, not a mere hope. (C2A2's adversarial 14/15 pipeline is a partial structural control, tempering urgency below High.)
  What is at risk: The allegiance-favored headline ("against pessimism") is discounted absent controls; compounds P-437 (unvalidated metric) and P-442 (non-independence).
  Recommended action: Restate hypotheses direction-agnostically; preregister the desired-outcome-neutral analysis (ties A-407 / MONITOR-413); blind raters/agents to framing and condition; declare the allegiance risk as a limitation. Binds A-408, P-442.
  Urgency: Medium-High
  Why flagged: PRESUMPTION + strong challenge + subjective measure + un-blinded direction-committed framing.

REVISE-174:
  Date: 2026-07-03 | Source: DISPOSITION-399 | Item: PRESUMPTION-442 (presumption) | Urgency: MED-HIGH
  Claim flagged: "That co-authorship where the same model family generates the dialogue data AND analyzes/writes it up does not compromise evidential independence."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: Non-independence failure — LLM self-recognition/self-preference (Panickssery et al. NeurIPS 2024; arXiv 2410.21819) and psychometric/common-method-bias theory (Podsakoff 2003) require generation and scoring to be independent operations. Where model JUDGMENT enters scoring/interpretation, the study may partly measure the model's internal consistency, not the phenomenon.
  What is at risk: Model-graded steps (understanding scores, C0 verdicts, interpretive write-up) may reflect self-preference; compounds agent-fidelity (P-436) and allegiance (P-440) into stacked non-independence.
  Recommended action: Use a different model family (or blind human raters) for scoring/analysis than for generation; report inter-model agreement as an independence check; separate deterministic steps from model-judgment steps in reporting; treat same-family results as a lower bound pending cross-model replication. Binds P-436, P-440.
  Urgency: Medium-High
  Why flagged: PRESUMPTION + strong challenge + stacks with P-436/P-440; the steelman (deterministic computations less exposed than model-graded judgments) scopes the fix, not dissolves it.

## 2026-07-06 RUN — 15c flags (c2a2-lit-search-pipeline; DISPOSITION-401..407)

REVISE-175:
  Date: 2026-07-06 | Source: DISPOSITION-401 | Item: PRESUMPTION-444 (presumption) | Urgency: High
  Claim flagged: "That deadline-driven gating ('ready for ISME') is the right release principle for public artifacts of an evidence-bearing system."
  15a/15b: PARTIALLY-SUPPORTED(Moderate) / CHALLENGED(Strong)
  Net: Release trains legitimize date-fixed delivery with SCOPE as the flexed variable; nothing endorses the calendar as the quality gate for evidence-bearing public artifacts. Kuutila et al. 2020 (102-study SLR: time pressure reduces quality) + Rogers Commission burden-of-proof inversion.
  What is at risk: credibility of every public C2A2 artifact; the release rule itself.
  Recommended action: rewrite the release rule as deadline-invariant criteria; scope reduction is the one sanctioned pressure valve; anything else requires a logged waiver. Retrospect the ISME release against the rule as written. Binds A-414 (MONITOR-416), P-450 (REVISE-181); SYSTEMIC-RISK #2.

REVISE-176:
  Date: 2026-07-06 | Source: DISPOSITION-402 | Item: PRESUMPTION-445 (presumption) | Urgency: Medium-High
  Claim flagged: "That a human-mediated compile loop (agent pastes commands, human runs regen/reload) is a reliable substrate for iterative debugging."
  15a/15b: PARTIALLY-SUPPORTED(Weak) / CHALLENGED(Strong)
  Net: THERP/HEART per-step human error rates compound across loop iterations and multiply under pressure; silent state-drift (stale build/cache — the A-412/OPEN-109 situation) corrupts the debugging evidence itself.
  What is at risk: validity of conclusions reached through the loop; attended-session time.
  Recommended action: one idempotent scripted regen/reload command with an embedded build stamp the agent verifies each cycle; unverified stamp = no-data.

REVISE-177:
  Date: 2026-07-06 | Source: DISPOSITION-403 | Item: PRESUMPTION-446 (presumption; queue CRITICAL) | Urgency: High
  Claim flagged: "That scheduled agents and attended sessions can share one git repository with no coordination protocol."
  15a/15b: PARTIALLY-SUPPORTED(Weak) / CHALLENGED(Strong)
  Net: Only support is git's fail-safe abort locking + low-contention OCC — and the 2026-07-05 index.lock/HEAD.lock collisions are the signature that low contention no longer holds. In-domain challenge: claude-code Issues #11005/#28823; 2026 worktree-isolation consensus; distributed mutual exclusion (Lamport 1978).
  What is at risk: integrity of the git history — C2A2's evidentiary substrate; OPEN-110/OPEN-113.
  Recommended action: worktree or per-writer-branch isolation for scheduled agents with defined merge path; single serialized pusher; written stale-lock procedure (owner/PID/age; never delete under uncertainty); verify/disable iCloud Documents sync on the vault path. Anchor of SYSTEMIC-RISK #1 (Critical) with REVISE-179/180.

REVISE-178:
  Date: 2026-07-06 | Source: DISPOSITION-404 | Item: PRESUMPTION-447 (presumption) | Urgency: Medium
  Claim flagged: "That snippet-level screening establishes source novelty when the primary source is unfetchable."
  15a/15b: PARTIALLY-SUPPORTED(Weak) / CHALLENGED(Strong)
  Net: Title/abstract triage licenses cheap EXCLUSION, never a load-bearing novelty claim: 13–51% single-screener miss rates; median 39% abstract/full-text inconsistency; novelty is the most spun abstract element.
  What is at risk: unverified novelty claims entering the wiki as validated (gates PROP-2026-07-05-001 / A-416, the June 12 Wolfram observer-boundary segment).
  Recommended action: full-text confirmation required before any novelty claim is load-bearing; snippet-only findings enter as PROVISIONAL with an explicit fetch-debt tag. SYSTEMIC-RISK #3.

REVISE-179:
  Date: 2026-07-06 | Source: DISPOSITION-405 | Item: PRESUMPTION-448 (presumption) | Urgency: High
  Claim flagged: "Racing concurrent writers is an acceptable coordination mechanism for repo operations."
  15a/15b: PARTIALLY-SUPPORTED(Moderate) / CHALLENGED(Strong)
  Net: OCC (Kung & Robinson 1981) requires conflict DETECTION + programmatic RETRY; bare racing plus lock-deletion-under-uncertainty is the documented corruption path (CWE-367 TOCTOU). Support endorses a different mechanism than the one presumed.
  What is at risk: repo corruption; silent lost updates in the evidentiary record.
  Recommended action: standard write path = fetch->rebase->push with bounded retry/backoff; forbid lock deletion without owner/PID/age evidence; log every lock event. SYSTEMIC-RISK #1.

REVISE-180:
  Date: 2026-07-06 | Source: DISPOSITION-406 | Item: PRESUMPTION-449 (presumption) | Urgency: High
  Claim flagged: "The set of possible repo writers is fully enumerable from the local process table."
  15a/15b: PARTIALLY-SUPPORTED(Weak) / CHALLENGED(Strong)
  Net: Process tables show CURRENT local writers only; scheduled/future writers, remote pushers, and sync daemons are invisible. Directly applicable: claude-code Issue #47241 — iCloud fileproviderd corrupts repos under ~/Documents, which is where this vault lives. Unexplained push 511b3b2 is the predicted hidden-writer signature.
  What is at risk: diagnosis quality for every concurrency incident; repo integrity via fileproviderd.
  Recommended action: IMMEDIATE — check iCloud Desktop & Documents sync for the vault path (disable or relocate the repo). Build a writer inventory (scheduled tasks + cadences, remote credentials, sync daemons); identify who pushed 511b3b2. SYSTEMIC-RISK #1.

REVISE-181:
  Date: 2026-07-06 | Source: DISPOSITION-407 | Item: PRESUMPTION-450 (presumption) | Urgency: Medium
  Claim flagged: "Marker-grep verification of an agent-rebuilt artifact can substitute for the visual sign-off the release rule requires."
  15a/15b: PARTIALLY-SUPPORTED(Weak) / CHALLENGED(Strong)
  Net: Content markers are necessary-not-sufficient; visual regression testing exists because content-present/render-broken failures are common. Substitution = Goodhart/surrogation + automation bias.
  What is at risk: public artifact shipping visually broken while all markers pass.
  Recommended action: retain marker-grep as a floor; require visual sign-off (human or headless screenshot-diff) before public release; add a render-level automated check. Binds REVISE-175; SYSTEMIC-RISK #2.

## 2026-07-07 RUN — 15c flags (c2a2-lit-search-pipeline; DISPOSITION-413..416)

REVISE-182:
  Date: 2026-07-07 | Source: DISPOSITION-413 | Item: PRESUMPTION-451 (presumption) | Urgency: Medium-High
  Claim flagged: "Scheduler task-lifecycle defects (ONE-TIME task firing 3x) are for agents to absorb, not for the scheduling layer to enforce."
  15a/15b: PARTIALLY-SUPPORTED(Moderate) / CHALLENGED(Strong)
  Net: Consumer idempotency is mainstream but as a designed contract ALONGSIDE delivery-layer guards (microservices.io idempotent-consumer); absorbing a known uncorrected defect as convention-only is single-layer defense + normalization of deviance (Vaughan 1996; Reason).
  What is at risk: the first scheduled agent written without dedup logic silently triples any non-idempotent action when the 3x-fire defect recurs.
  Recommended action: explicit idempotency contract for every scheduled agent (run-ID dedup at start); scheduling-layer guard (run registry detecting duplicate fires); report the defect upstream. Part of SYSTEMIC-RISK single-layer self-verification (2026-07-07).

REVISE-183:
  Date: 2026-07-07 | Source: DISPOSITION-414 | Item: PRESUMPTION-452 (presumption) | Urgency: Medium
  Claim flagged: "Subset (9-page) + aggregate (<2%) resolver agreement establishes census-wide delta validity."
  15a/15b: PARTIALLY-SUPPORTED(Weak-Moderate) / CHALLENGED(Strong)
  Net: 9 concordant pages bound per-page agreement no better than ~70% (95% CI); aggregate concordance is the summary-statistic validation Bland & Altman (1986) rejected; Simpson's-paradox aggregation can hide stratum-level category shifts inside a stable total.
  What is at risk: instrument-change artifacts read as connectivity findings; the OPEN-114 bootstrap-retirement decision resting on unvalidated equivalence (gates A-424).
  Recommended action: stratified agreement sample (n>=60 pages across orphan/sparse/connected + edge-case link syntaxes) with per-stratum concordance before treating resolver deltas as real; tag all deltas by resolver meanwhile.

REVISE-184:
  Date: 2026-07-07 | Source: DISPOSITION-415 | Item: PRESUMPTION-453 (presumption) | Urgency: High
  Claim flagged: "The orphan/sparse/connected census still measures synthesis health when 100% of growth is orphans-by-design (metric dilution unexamined)."
  15a/15b: NO-SUPPORT-FOUND(None; PARTIALLY-NOVEL) / CHALLENGED(Strong)
  Net: Maximal asymmetry — zero support, convergent challenge (composition effects/Bickel 1975; case-mix adjustment; Goodhart/surrogation, Choi-Hecht-Tayler 2012). With all growth entering the orphan stratum by construction, the unstratified orphan rate measures the growth policy, not synthesis health.
  What is at risk: the system's synthesis-health instrument reporting an artifact; masked real decay among legacy pages; Goodhart-style "fixes" corrupting the orphans-by-design intent. Feeds A-423 and OPEN-114; kin to OPEN-112.
  Recommended action: stratify the census by design-status (orphan-by-design vs organic) before the next weekly sewing run; report per-stratum rates alongside the headline; recompute the historical trend stratified. Short wiki note on the PARTIALLY-NOVEL dilution-by-design configuration worth writing.

REVISE-185:
  Date: 2026-07-07 | Source: DISPOSITION-416 | Item: PRESUMPTION-454 (presumption) | Urgency: High (outage live)
  Claim flagged: "Single-credential, self-masking alerting (failure notes delivered through the failed channel) is adequate for the daily Chat<->Cowork sync."
  15a/15b: NO-SUPPORT-FOUND(None) / CHALLENGED(Strong)
  Net: Textbook common-mode-failure anti-pattern (SRE: alerting must be independent of and more reliable than the monitored path) with an OBSERVED instance — sync down since >=2026-07-03, failure notices swallowed by the failed channel; detection latency unbounded.
  What is at risk: silent Chat/Cowork divergence compounding daily; every "no news is good news" inference about the sync unfounded. ABSENCE-AS-EVIDENCE cluster.
  Recommended action: IMMEDIATE — restore the sync; add a dead-man's switch (heartbeat on success, independent agent or Tom's daily review alarms on staleness); alert path must share no credential/codepath with the sync. Reinforces PREMISE-025 (channel-independence corollary).

---

## 2026-07-08 REVISE escalations (MONITOR -> REVISE; autonomous refresh run; Tom not present)

REVISE-186:
  Date: 2026-07-08 | Source item: PRESUMPTION-352 (PRESUMPTION, unstated) | from DISPOSITION-417 (was MONITOR-349, cycle 2)
  Statement: The post-Apr-6 token cliff / output flatline is a capture/instrumentation artifact, not a real activity change.
  Why escalated: 15b CHALLENGED/Strong stable across 2+ cycles; 15a support flat at PARTIALLY-SUPPORTED/Moderate and generic. MNAR theory: mechanism is unidentifiable from the observed pattern; a real drop fits the same curve. The deciding probe has been outstanding 3+ cycles.
  What is at risk: any downstream inference treating the cliff as "artifact" (activity-continuity / telemetry-maturity claims).
  Recommended action for Tom: run probe_openstory.py (or otherwise reconstruct post-Apr-6 activity from a channel independent of the capture pipeline). Until run, label the cliff UNKNOWN-cause, never "artifact." NOTE: the A-363 heartbeat run-log (REVISE-147) would supply exactly this out-of-band check — one fix serves both.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c -> 15d -> 15c]; Current status: REVISION-FLAGGED

REVISE-187:
  Date: 2026-07-08 | Source item: PRESUMPTION-387 (PRESUMPTION, unstated) | from DISPOSITION-419 (was MONITOR-372, cycle 1)
  Statement: The adjudicator agent is itself competent and unbiased at judging semantic agreement/entailment.
  Why escalated: 15b CHALLENGED/Strong with new 2026 evidence (arXiv 2602.02219) that rubric-based LLM judges show measurable position bias and ~10-25% self-preference (worst within a shared model family); 15a support is explicitly CONDITIONAL on calibration, which the presumption asserts unconditionally.
  What is at risk: every downstream agreement/dissensus call (incl. P-388) inherits the adjudicator's unmeasured error rate and any same-family self-preference. Upstream of the whole agreement pipeline; gated by OPEN-090.
  Recommended action for Tom: make adjudicator calibration a measured gate — human-labeled agreement sample (Cohen's kappa), position-swap to cancel order bias, prefer a judge model family different from the columns; treat adjudicator error as a de-biased measured input.
  Urgency: Medium (highest-leverage of this run — upstream dependency)
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c -> 15d -> 15c]; Current status: REVISION-FLAGGED

REVISE-188:
  Date: 2026-07-08 | Source item: PRESUMPTION-389 (PRESUMPTION, unstated) | from DISPOSITION-421 (was MONITOR-374, cycle 1)
  Statement: A pilot validated on the Hawkins track generalizes to other thinker tracks.
  Why escalated: 15b CHALLENGED/Strong now formally grounded (PMC7014944 Risk of Generalizability Bias; friendliest-case pilots overstate effects that fail at scale). Hawkins is the most self-confirming subject (his theory frames the columns), so a pass there is weak transfer evidence. 15a supports pilot legitimacy but NOT transfer.
  What is at risk: the "generalize across thinker tracks" decision and anything gated on the pilot, if the mechanism is selection-bound to Hawkins.
  Recommended action for Tom: pre-register >=1 theory-misaligned / least-favorable thinker before claiming transfer. Pass there = generalization support; pass only on Hawkins = confirmed selection-bound (REVISE the transfer claim).
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c -> 15d -> 15c]; Current status: REVISION-FLAGGED

---

## 2026-07-09 REVISE intake (15c; fresh cohorts 07-07 + 07-08; DISPOSITION-424..438 run)

REVISE-189:
  Date: 2026-07-09 | Source item: ASSUMPTION-427 (ASSUMPTION, stated; QUEUED-EMPIRICAL) | from DISPOSITION-425
  Statement: A byte-copy of a write-quiescent DB over the sandbox mount is faithful, so quick_check failure on the copy establishes source-file corruption.
  Why flagged: 15b CHALLENGED/Strong with 15a concurring on the weak link — WAL-mode byte-copies without -wal/-shm sidecars fail integrity checks on HEALTHY sources (sqlite.org howtocorrupt); mount-layer torn/short reads are an independent live hypothesis. quick_check failure on the copy establishes only that (copy OR copy-process OR source) is faulty. Inference direction unsound.
  What is at risk: the openstory recovery path — a healthy source could be declared corrupt, triggering unnecessary restore with data loss to the backup point. Interacts badly with REVISE-192 (opposite-direction alarm dismissal).
  Recommended action for Tom: run sqlite3 quick_check NATIVELY on the Mac source (pending empirical test; the sandbox cannot run it — fail-loud). Before any future copy-based diagnosis: checkpoint (PRAGMA wal_checkpoint(TRUNCATE)) or copy sidecars, prefer .backup/VACUUM INTO, and require two independent copy paths to agree before a corruption verdict.
  Urgency: High
  PROVENANCE: Origin 14a; Chain [14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-190:
  Date: 2026-07-09 | Source item: PRESUMPTION-456 (PRESUMPTION, unstated) | from DISPOSITION-428
  Statement: Human review capacity is elastic — proposal intake needs no backpressure, queue cap, or aging policy.
  Why flagged: 15a NO-SUPPORT-FOUND (domain literature uniformly prescribes the opposite); 15b CHALLENGED/Strong (Little's Law; Sadowski et al. 2018 — overloaded reviewers review WORSE, not just later). The lambda>mu signature is observed: pending 4->13 in two days, last review a week old. An unbounded queue before the approval gate silently converts "human-reviewed" into "human-backlogged."
  What is at risk: the meaningfulness of C2A2's core human-in-the-loop control; all proposal-driven changes inherit review-under-overload quality.
  Recommended action for Tom: WIP cap on pending proposals (cap N), aging policy (auto-expire or batch-summarize items older than X days), and agent-side backpressure (throttle emission when cap hit). Decide N and X; the mechanism is cheap.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-191:
  Date: 2026-07-09 | Source item: PRESUMPTION-457 (PRESUMPTION, unstated) | from DISPOSITION-429
  Statement: Model training priors are a valid oracle over live search results when they conflict about post-cutoff events.
  Why flagged: 15b CHALLENGED/Strong (Longpre et al. 2021 — priors systematically biased against ALL post-cutoff events; policy inverts RAG's design rationale and freezes recall at cutoff). 15a's partial support covers calibrated skepticism with verification — a different policy than prior-wins-by-default.
  What is at risk: systematic novelty-blindness — genuinely new talks/papers/appearances rejected because the model hadn't heard of them, in exactly the monitoring tasks the tradition agents exist for.
  Recommended action for Tom: replace prior-wins with a verification rule — on prior/retrieval conflict about a post-cutoff event, neither side is oracle; require a second independent (or primary) source before accept OR reject; log conflicts. Pairs with MONITOR-419 (A-426 catalog-check error rate).
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-192:
  Date: 2026-07-09 | Source item: ASSUMPTION-431 (ASSUMPTION, stated; QUEUED-EMPIRICAL) | from DISPOSITION-433
  Statement: A failing QC signal (qc_sweep "fidelity fail") can be reclassified as environmental (absent sandbox cache) without independent re-verification of content.
  Why flagged: 15b CHALLENGED/Strong (Leveson & Turner 1993, Therac-25 — dismissing alarms as known-spurious without verification is the canonical accident precursor); 15a concurs that rationalization is sanctioned only as a documented evidence-based determination. Environmental plausibility is not evidence about content. Unvalidated-instrument cluster member.
  What is at risk: the qc_sweep instrument's trustworthiness — one plausibility-only waiver gives every future fail a known-benign escape hatch; real corruption rides through.
  Recommended action for Tom (cheap, decisive): regenerate /tmp/dayNNN_segments.json in-sandbox and re-run the fidelity check. Pass -> document environmental cause with evidence; fail -> real content issue. Policy: never close a QC fail on plausibility alone.
  Urgency: Medium
  PROVENANCE: Origin 14a; Chain [14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-193:
  Date: 2026-07-09 | Source item: PRESUMPTION-460 (PRESUMPTION, unstated) | from DISPOSITION-436
  Statement: Capture is binary and final — a source already in prs_triplets.md needs no re-examination after a lens change (e.g., paradigm-boundary lens).
  Why flagged: 15a NO-SUPPORT-FOUND; 15b CHALLENGED/Strong (living systematic reviews, qualitative re-coding, re-indexing on ontology change all obligate re-examination when the coding frame shifts — extraction is source x lens). Prospective-only application is legitimate only as an explicit documented decision, never made here.
  What is at risk: paradigm-boundary signal sitting unrecognized in the captured back-catalog; the scarcest signal class under-counted (compounds REVISE-194).
  Recommended action for Tom: choose deliberately — (a) one-time re-scan of existing prs_triplets.md sources under the paradigm-boundary lens, or (b) an explicit recorded prospective-only decision with rationale. Do not default.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-194:
  Date: 2026-07-09 | Source item: PRESUMPTION-461 (PRESUMPTION, unstated) | from DISPOSITION-437
  Statement: A single specialist agent can reliably assign the "paradigm-shift candidate" label at intake, one pass, no adjudication.
  Why flagged: 15b CHALLENGED/Strong (Gartlehner et al. 2020: single screener misses 13% vs 3% dual; Waffenschmidt et al. 2019); 15a's best case (~3%, experienced screeners) does not extend to rare, fuzzy, high-stakes categories — the worst case on every axis. Compounding: the adjudicator layer is itself under REVISE-187 and upstream review is a week behind (REVISE-190).
  What is at risk: the scarcest, most-watched signal class contaminated at intake in both directions, with no second pass to catch either.
  Recommended action for Tom: two-reader design for this label only — a second independent agent pass (different model family per REVISE-187) with adjudicated disagreements, or a periodic retrospective second pass over single-labeled items.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-195:
  Date: 2026-07-09 | Source item: PRESUMPTION-462 (PRESUMPTION, unstated) | from DISPOSITION-438
  Statement: Fixed re-check cadences (7-day reviewer staleness; weekly 15d re-trigger) are right-sized — set once, never load- or change-rate-adapted.
  Why flagged: 15b CHALLENGED/Moderate (adaptive-polling literature; own queue growth is the failure signature) and — decisive — CONSISTENCY: PREMISE-095, incorporated this run, validates that the weekly 15d cadence structurally overruns throughput. An incorporated premise contradicts this presumption; surfaced, not averaged. Both failure directions observed same-day.
  What is at risk: the 15d refresh loop's usefulness (backlog swamps signal); staleness rules firing wrongly in both directions.
  Recommended action for Tom: make cadence a controlled variable — key 15d re-trigger interval (or per-run re-trigger cap) to queue depth; revisit the 7-day reviewer-staleness rule against observed latency. Same decision as OPEN-115/116 — resolve together.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-196:
  Date: 2026-07-10 | Source item: ASSUMPTION-435 (ASSUMPTION, stated; QUEUED-EMPIRICAL) | from DISPOSITION-441
  Statement: DB write-staleness beyond threshold reliably indicates the OpenStory runtime is down, and freezing (refusing to refresh) beats serving stale feeds.
  Why flagged: 15b CHALLENGED/Strong on both clauses — failure-detector theory (Chandra & Toueg 1996) shows staleness cannot distinguish down/slow/idle, so "reliably indicates" is unsound by construction; and graceful-degradation standards (RFC 5861 stale-if-error; AWS Well-Architected) prescribe serving LABELED stale data over refusing service for read-mostly, non-safety content. 15a's own support (heartbeat doctrine, Aguilera et al. 1997) concedes timeout detectors false-positive.
  What is at risk: an idle-but-healthy runtime or a broken heartbeat path triggers a false freeze — the freeze becomes the availability incident; staleness verdicts also feed the openstory recovery work already under REVISE-186/189.
  Recommended action for Tom: replace freeze with serve-stale-clearly-labeled (age banner) + an out-of-band liveness probe of the runtime itself (process/health check, not DB mtime). Converges with the REVISE-186/189 probe — one instrument now serves four flags. The queued post-.recover empirical check (did staleness actually track runtime state?) remains decisive and should run.
  Urgency: Medium
  PROVENANCE: Origin 14a; Chain [14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-197:
  Date: 2026-07-10 | Source item: PRESUMPTION-463 (PRESUMPTION, unstated) | from DISPOSITION-443
  Statement: Platform pause policy is stable and a synthetic query is a trustworthy activity proxy — the keep-warm loop needs no outcome verification.
  Why flagged: 15b CHALLENGED/Strong — all three legs fail independently: free-tier policies change without notice; whether the ping path is COUNTED as activity is undocumented (Supabase clarification threads exist); and trusting action-success (cron ran) over outcome (project unpaused) is the textbook open-loop control failure. 15a found no literature endorsing unverified keep-alive — support for that clause was inferential only (15a NOVELTY-weak: the practice-vs-literature gap is itself the finding).
  What is at risk: keep-warm reports green while the project pauses anyway — discovered only when the demo broker is dead in use.
  Recommended action for Tom: close the loop — probe actual project status (management API or read-back check) on a schedule and alert on pause; verify once that the SELECT 1 path counts as activity. One probe also settles MONITOR-427 (A-434).
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-198:
  Date: 2026-07-10 | Source item: PRESUMPTION-464 (PRESUMPTION, unstated) | from DISPOSITION-444
  Statement: The daily-walk Chat is the sole canonical human-context channel and browser delivery its only transport; on failure, waiting is the only remedy.
  Why flagged: 15b CHALLENGED/Strong — single-channel single-transport human comms is a named ops anti-pattern with a standard remedy (pre-provisioned out-of-band secondary; TrustedSec; post-CrowdStrike-2024 analyses); absence of messages is indistinguishable from absence of instruction. 15a supports one CANONICAL channel (SSOT/ChatOps consolidation) but found nothing supporting waiting-as-remedy and flagged that clause NOVELTY — unaddressed in literature because no one designs it deliberately.
  What is at risk: the human-context loop — already severed 7 days by the Chrome login failure while a working Gmail fallback existed in-fleet. This is the live instance, not a hypothetical.
  Recommended action for Tom: keep Chat canonical; add the Gmail transport as explicit fallback delivery for daily-walk content when browser delivery fails (the one-line task change named at intake). Canonicality and transport redundancy are compatible — SSOT says where truth lives, not how many roads reach it.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-199:
  Date: 2026-07-10 | Source item: PRESUMPTION-465 (PRESUMPTION, unstated) | from DISPOSITION-445
  Statement: Appending a FAIL line to a file constitutes surfacing — fail-loud presumes a reliable listener, never verified.
  Why flagged: 15b CHALLENGED/Strong — security (OWASP Top 10:2025 A09), IT-ops (Target 2013 unheeded alerts), and clinical alarm literature (Joint Commission SEA 50) all distinguish recording from surfacing: an alert's value is the verified probability a listener acts on it; a file-appended FAIL has no notification, no assigned responder, no acknowledgment, no escalation. The system's own record confirms: openstory down 4d, Chrome login 7d, review backlog 9d — alarms written, remediation absent. 15a's conditional support (a contractual scheduled reader makes the write BE the surfacing) names exactly the unverified condition.
  What is at risk: the system believes it fails loud while failing silent; every fail-loud commitment in the fleet inherits the flaw.
  Recommended action for Tom: add an acknowledgment layer — FAIL lines carry an ack field; unacked FAILs older than a threshold escalate to a verified channel. Converges with REVISE-198's fallback transport and MONITOR-420's auto-escalate — this is the missing actuator for both.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-200:
  Date: 2026-07-10 | Source item: PRESUMPTION-466 (PRESUMPTION, unstated; QUEUED-EMPIRICAL) | from DISPOSITION-446
  Statement: Count discrepancy means prior figures were estimates, not that items were lost — the loss hypothesis went unvoiced.
  Why flagged: 15b CHALLENGED/Strong — premature closure + anchoring + normalcy bias are among the best-documented causes of diagnostic error (Al Essa et al. 2026, Medical Education; AHRQ PSNet); the prescribed countermeasure is voicing and preferentially testing the harmful hypothesis BEFORE closing. 15a's base-rate support (most registry drift is benign — DeHoratius & Raman 2008; SRE triage doctrine) justifies the benign hypothesis as LEADING — not as unvoiced-and-untested. The practice error stands regardless of what the reconciliation finds.
  What is at risk: benign-first closure becomes a triage habit; real losses absorbed into "estimation noise" narratives with no recorded trace that the alternative was considered.
  Recommended action for Tom: (a) run the provenance-ID reconciliation now (the same test gates MONITOR-426/A-433 — one test settles both items); (b) adopt the triage rule: when counts disagree, record both hypotheses and the discriminating test before adopting either.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-201:
  Date: 2026-07-11 | Source item: ASSUMPTION-437 (ASSUMPTION, stated; QUEUED-EMPIRICAL) | from DISPOSITION-447
  Statement: The pipeline's tag-based queue enumeration is complete — 8 fresh + 13 held QUEUED-EMPIRICAL exhausts the July items; "nothing was missed."
  Why flagged: 15a NO-SUPPORT-FOUND/None + 15b CHALLENGED/Strong — the cleanest verdict split available. Capture-recapture / dual-system estimation doctrine (Bird & King 2018; census DSE) holds that a single enumeration cannot measure its own undercount; audit completeness testing requires tracing from an independent source population. "Nothing was missed," asserted by the same tag query being audited, is structurally unverifiable — the P-466 error repeated at the enumeration layer.
  What is at risk: silent orphaning of queued items (mis-tagged, untagged, or malformed entries invisible to the tag query); the integrity cluster's reconciliation inherits the blind spot.
  Recommended action for Tom: adopt a dual-channel enumeration check — tag query vs independent ID-gap/regex sweep over for_lit_search.md and the registries — run it now as part of the MONITOR-426/REVISE-200 reconciliation (one pass settles the integrity cluster) and keep it as the standing completeness check.
  Urgency: Medium
  PROVENANCE: Origin 14a; Chain [14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-202:
  Date: 2026-07-11 | Source item: PRESUMPTION-467 (PRESUMPTION, unstated) | from DISPOSITION-451
  Statement: Firing-health aggregates to system health — a scheduler watchdog may say "all clear / action needed: none" while multi-day outcome-level outages stand.
  Why flagged: Both search directions converge against the embedded belief. 15a SUPPORTED/Strong for the surfaced hazard (watermelon-SLA ITSM literature; Google SRE Ch. 4/6 — measure user-visible outcomes, not component liveness); 15b CHALLENGED/Strong (firing-health does not compose into outcome health). The system's own July record is the live instance: three multi-day outcome outages (openstory, Chrome login, review backlog) persisted through green watchdog mornings.
  What is at risk: the morning watchdog is a systemwide sedative — its "all clear" suppresses the human check that would otherwise catch standing outages; outage duration is bounded only by happenstance.
  Recommended action for Tom: add outcome-level SLIs to the watchdog and make "all clear" conditional on them: openstory runtime actually serving; today's expected artifacts exist and parse (per REVISE-203's manifest); human-channel transport verified (per REVISE-198). Dashboard face of the open-loop family — same fix as the 2026-07-11 SYSTEMIC-RISK recommendation.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-203:
  Date: 2026-07-11 | Source item: PRESUMPTION-468 (PRESUMPTION, unstated; QUEUED-EMPIRICAL) | from DISPOSITION-452
  Statement: Fresh files in a shared output tree attribute to the task under verification — the daily run's output check is satisfied by any of a dozen writers.
  Why flagged: 15b CHALLENGED/Strong — a check any of a dozen writers can satisfy is a verifier that cannot fail (vacuous by test-effectiveness doctrine: Inozemtseva & Holmes ICSE 2014; assertion-specificity: Zhang & Mesbah FSE 2015); 15a's Moderate support confirms the hazard from the data-observability side (lineage/attribution is a named pillar precisely because freshness-of-shared-target checks mis-attribute).
  What is at risk: the daily run can be dead indefinitely while its output check stays green off other writers' files — the P-468 check is today unfalsifiable.
  Recommended action for Tom: manifest convention — each scheduled task declares its expected task-specific outputs (name pattern + location); output checks match the manifest, not tree freshness. Verify attribution once via manifest diff or a deliberate no-op day. Cheap fix; feeds REVISE-202's artifact SLI.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-204:
  Date: 2026-07-11 | Source item: PRESUMPTION-469 (PRESUMPTION, unstated; QUEUED-EMPIRICAL) | from DISPOSITION-453
  Statement: Task-file drift is benign because each run's agent will re-derive the repair — noted fixes in run outputs reach no future run and no file owner.
  Why flagged: 15b CHALLENGED/Strong — configuration-drift and snowflake literature (Fowler/Morris) plus SRE toil doctrine treat repeated unpersisted remediation as a compounding anti-pattern, and postmortem-completion data (<40% of even tracked action items done in 90 days) refutes "someone will fix it later" as a mechanism. 15a's PARTIALLY-SUPPORTED/Moderate is strictly conditional and the condition fails: per-run re-derivation is healthy only when repairs converge to a persisted source of truth (GitOps desired-state); ephemeral run outputs persist nothing.
  What is at risk: task files accumulate literally-unresolvable instructions; every run pays a re-derivation toll; nondeterministic agents apply divergent repairs so task semantics vary run to run.
  Recommended action for Tom: give task files an owner and a repair path — runs append noted defects to a task-file-fixes queue that a named owner (or the weekly sewing agent) applies to the files themselves; run the cheap one-time audit for currently-unresolvable instructions.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-205:
  Date: 2026-07-11 | Source item: PRESUMPTION-470 (PRESUMPTION, unstated; QUEUED-EMPIRICAL) | from DISPOSITION-454
  Statement: Registry counts are interchangeable across agents and clocks — no census protocol (timestamp + rule) governs shared figures.
  Why flagged: Convergent from two independent literatures. 15a SUPPORTED/Strong for the hazard (Chandy & Lamport 1985: uncoordinated snapshots compose into global states that never existed; accounting cut-off doctrine: counts compare only relative to declared timestamp + rule); 15b CHALLENGED/Strong (without a census protocol, phantom discrepancies and masked real losses are indistinguishable — registry disagreements unclosable in principle). Generalizes the A-433/P-466 count cluster and P-458/OPEN-112.
  What is at risk: every cross-agent shared figure (queue sizes, backlog tallies, registry counts) may describe a state that never existed; the MONITOR-426 reconciliation inherits the ambiguity unless the census rule comes first.
  Recommended action for Tom: adopt a census protocol — every shared figure carries a timestamped cut-off + counting rule (which tags/statuses count, as of when). Have the A-433/P-466 reconciliation adopt its census rule from this item's one-day counting test — one convention settles three flags (MONITOR-426, REVISE-200, REVISE-205).
  Urgency: Medium-High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-206:
  Date: 2026-07-12 | Source item: ASSUMPTION-442 (ASSUMPTION, stated; QUEUED-EMPIRICAL) | from DISPOSITION-456
  Statement: Form-check-only PRS-id QC (wiki unmounted) is an acceptable degraded mode provided a deferred spot-check compensates.
  Why flagged: 15b CHALLENGED/Strong — graceful degradation is acceptable only with its constitutive safeguards, and this instance lacks them: degraded passes are indistinguishable from full passes (P-471's uniform last_qc_at), and the compensating spot-check is deferred with no owner or trigger in a system whose measured action-item completion is <40% (normalization-of-deviance entry pattern: Vaughan; JSR 2022 systematic review). Real id-drift was confirmed the same morning — the reduced checks have live misses. 15a's Moderate support is conditional on exactly the missing safeguards.
  What is at risk: form-check-only passes accumulate under fresh full-strength QC stamps; id-drift spreads silently; on discovery the entire QC history becomes suspect.
  Recommended action for Tom: keep the degraded mode but add its safeguards — qc_mode field on the stamp (REVISE-207's fix), the Days-239/240 spot-check scheduled with a date and owner, and a bounded lifetime (max N form-only runs before a forced full pass).
  Urgency: Medium-High
  PROVENANCE: Origin 14a; Chain [14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-207:
  Date: 2026-07-12 | Source item: PRESUMPTION-471 (PRESUMPTION, unstated) | from DISPOSITION-460
  Statement: A QC freshness stamp certifies uniform verification depth — degraded-mode pairs get the same last_qc_at as fully verified pairs, hiding skipped checks from all future scans.
  Why flagged: Convergent from three literatures. 15a SUPPORTED/Strong for the hazard (SLSA v1.1: verification claims without depth metadata are untrustworthy by design — hence graded attestation; arXiv:2605.28546: "SKIP is not evidence"); 15b CHALLENGED/Strong against the embedded belief (gray failure, Huang et al. 2017: uniform-green-over-heterogeneous-state is the dominant dangerous signal class; a stamp both modes set identically is a verifier that cannot fail, per the Inozemtseva & Holmes standard). The staleness system inverts the stamp into active protection of the defect: freshest-looking pairs include the least-verified.
  What is at risk: id-drift (confirmed 07-11) rides in pairs marked fully fresh; the degraded cohort becomes unreconstructible as run logs age out — the fix window is closing.
  Recommended action for Tom: add qc_mode (full | form-only) beside last_qc_at; backfill the known degraded cohort from run records NOW; make staleness scans treat form-only as due-for-full. Enables REVISE-206's safeguards; sibling of REVISE-203's manifest fix.
  Urgency: High (backfill depends on run logs that decay)
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-208:
  Date: 2026-07-12 | Source item: PRESUMPTION-472 (PRESUMPTION, unstated; QUEUED-EMPIRICAL) | from DISPOSITION-461
  Statement: Systematic citation mislabels are textually regular enough for batch grep — the error class is presumed string-shaped, though one observed instance is a gloss.
  Why flagged: 15b CHALLENGED/Strong — citation-integrity literature classifies mislabels as predominantly semantic (claim-vs-source inconsistency requiring full-text comparison: arXiv:2606.08589; Sarol et al. 2024, 20–26% inaccuracy rates dominated by semantic classes), and the presumption's only inspected instance is itself a gloss — the error class was defined by the available tool, not the observed errors. 15a support is Weak and conditional on the presumed property.
  What is at risk: OPEN-118 closes on grep exhaustion while the semantic remainder persists under a "resolved" flag; the fix cannot see its own exemplar.
  Recommended action for Tom: define "cluster closed" as grep yield PLUS a sampled semantic read showing negligible residue; run both passes on the same day-range before closing OPEN-118. Governs MONITOR-433's closure criterion.
  Urgency: Medium
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-209:
  Date: 2026-07-12 | Source item: PRESUMPTION-473 (PRESUMPTION, unstated) | from DISPOSITION-462
  Statement: System-produced completion/freshness denominators are trusted as the universe; nothing audits the denominator (30,529/30,529; 307/307 — the latter known-wrong).
  Why flagged: Convergent. 15a SUPPORTED/Strong for the hazard (capture-recapture doctrine: a registry cannot measure its own completeness from within — IJE 1995; modern registry methods, arXiv:2211.13842); 15b CHALLENGED/Strong against the embedded belief (even multi-source corrections carry unknown dependence bias, PMC11022997; the in-house 307/307 known-wrong figure is a live counterexample of exactly the claimed shape). Terminal "complete" states make the error permanent — no remaining detection path.
  What is at risk: every terminal completeness state may conceal silent gaps forever; cross-agent figures inherit unaudited denominators, compounding the A-433/P-466 count cluster.
  Recommended action for Tom: convention — terminal completeness claims require one independent corroboration (provider-side count for BOSCO per MONITOR-435; dual-channel census for registries per REVISE-200/205), and denominators carry provenance (source, method, timestamp). Extends the REVISE-205 census protocol from counts to denominators; one protocol settles this flag, MONITOR-435, and strengthens three prior flags.
  Urgency: Medium-High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-210:
  Date: 2026-07-12 | Source item: PRESUMPTION-474 (PRESUMPTION, unstated) | from DISPOSITION-463
  Statement: Full-cadence autonomous production remains valuable while human consumption is severed — no quiescence or backpressure rule exists for prolonged operator absence.
  Why flagged: 15b CHALLENGED/Strong — the same decoupling literature that licenses continued artifact production REQUIRES backpressure (unbounded production into a consumer-less system is the named anti-pattern); for signal-type outputs the verdict is unambiguous: overproduction is the cardinal lean waste, alert-fatigue doctrine says unconsumed escalations degrade the channel itself, and dead-man's-switch doctrine says operator absence should trigger a designed SAFE reduced state, not default continuation. The system is living the counterexample: A-428 escalates nightly into an unread channel; 25+ REVISE flags now await an absent reviewer (this run adds 5). 15a's Moderate support covers only the durable-artifact class and is conditional on backpressure existing somewhere.
  What is at risk: unratified authority accumulates — every REVISE flag is a decision awaiting a decision-maker; the pipeline's human-in-the-loop legitimacy at the REVISE boundary silently expires while throughput continues; return-triage cost grows superlinearly.
  Recommended action for Tom: adopt a quiescence rule distinguishing artifact from signal production — after 7 consecutive days without operator consumption: reduce cadence, suppress per-item escalations in favor of one daily digest, and accumulate REVISE flags into a triage-ordered return-brief. (Self-referential: this run operates under the condition it flags.)
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-211:
  Date: 2026-07-13 | Source item: ASSUMPTION-448 (ASSUMPTION, stated) | from DISPOSITION-466
  Statement: The knowledge graph is sufficient for thinker-agent synthesis — hub backlink concentration plus an accounted-for orphan population means "the bottleneck is not connectivity."
  Why flagged: The claim's OWN supporting literature undermines it. Adamic et al. 2001 (sublinear search in power-law graphs) REQUIRES hubs connected to the periphery; GraphRAG's Leiden partition (Edge et al. 2024) is collectively exhaustive — every node lands in a community. A ~75%-orphan vault violates the precondition of both. Meanwhile 15b: two independent 2025 benchmarks find GraphRAG "frequently underperforms vanilla RAG" and that any benefit is contingent on graph construction quality (Xiang et al., arXiv:2506.05690; Han et al., arXiv:2502.11371); KG sparsity is the named mechanism that breaks multi-hop traversal (Saxena et al., EmbedKGQA, ACL 2020); the long tail is where retrieval already fails (Mallen et al., ACL 2023). Sufficiency was DERIVED FROM GRAPH STATISTICS WITHOUT ASKING WHAT CONSUMES THE GRAPH — an invalid derivation whether or not its conclusion holds.
  What is at risk: "The bottleneck is not connectivity" is the load-bearing conclusion of the 2026-07-12 census and will steer effort AWAY from the graph. If wrong, C2A2 spends its effort elsewhere while three quarters of its corpus stays invisible to its own synthesis agents — and the failure is SILENT: agents produce confident syntheses over the reachable quarter and never report what they could not see.
  Recommended action for Tom: WITHDRAW the sufficiency verdict until the retrieval mode is determined — a one-hour code read that also decides ASSUMPTION-447/MONITOR-437 (see SYSTEMIC-RISK #2). Then measure: 30 held-out synthesis questions whose gold answers require content from >=2 orphan notes; compare orphan-note recall against hub-note recall. Do not let the verdict steer prioritisation before one of these is in hand.
  Urgency: Medium
  PROVENANCE: Origin 14a; Chain [14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-212:
  Date: 2026-07-13 | Source item: ASSUMPTION-450 (ASSUMPTION, stated) | from DISPOSITION-468
  Statement: Active inference has no fatigue term and cannot obviously derive why a well-fitted model degrades once its goal is met; if that absence holds, aging is evidence about FEP rather than an application of it.
  Why flagged: THE FIRST CLAUSE IS FALSE AS WRITTEN. Stephan, Manjaly, Mathys et al. (2016), "Allostatic self-efficacy: a metacognitive theory of dyshomeostasis-induced fatigue and depression," Front. Hum. Neurosci. 10:550, constructs a fatigue term INSIDE active inference — a metacognitive belief about one's own regulatory competence that degrades endogenously. Cieri et al. (2021), Front. Hum. Neurosci. 15:647513, treat AGING ITSELF as an FEP application via brain entropy, precisely inverting the claim's conclusion. Precision is already a free FEP parameter and its decay in aging is documented (Chao et al. 2021, Cerebral Cortex 31(4)). 15a's support is real but narrower than the claim: FEP's CORE answers "why persist?", not "why stop?".
  What survives (and is worth keeping): a precise, still-open, possibly publishable question — does any FEP formalism predict decay in a system with INTACT RESOURCES, NO EXOGENOUS DAMAGE, and a SATISFIED generative model? Stephan's fatigue arises from sustained FAILURE (dyshomeostasis), not from success, so it does not strictly cover the "well-fitted model that has met its goal" case.
  What is at risk: This gates the friston_levin standalone-synthesis promotion and has been flagged two consecutive weeks. Promoting a synthesis headlined "active inference has no fatigue term" would put C2A2's name behind a claim refuted by a well-known paper in the field's flagship venue.
  Recommended action for Tom: RESTATE the assumption in its narrow form and re-test THAT. Required reading before the friston_levin promotion: Stephan et al. 2016 IN FULL — and ask it one question: is the downward revision of allostatic self-efficacy DERIVED from free-energy minimisation in a resource-intact, model-satisfied system, or TRIGGERED by exogenous persistent prediction error? If the latter, the narrow claim stands and should be restated in those terms. Also read Cieri et al. 2021 and Kuchling, Friston, Georgiev & Levin 2020 (Physics of Life Reviews 33:88-108) — the last being the Friston-Levin collaboration this very bridge concerns.
  Urgency: Medium-High (gates a promotion; second consecutive flag)
  PROVENANCE: Origin 14a; Chain [14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-213:
  Date: 2026-07-13 | Source item: PRESUMPTION-476 (PRESUMPTION, unstated) | from DISPOSITION-471
  Statement: An in-run self-caught, self-fixed tool defect needs no independent confirmation — the erring run certifies its own fix and the exoneration of all prior output.
  Why flagged: Four independent evidentiary traditions converge WITHOUT EXCEPTION — code inspection (Fagan 1976, IBM Sys J 15(3); Basili & Selby 1987, IEEE TSE SE-13(12): an INDEPENDENT reader outperforms the author's own testing), supply-chain attestation (SLSA v1.0: L1 self-attested provenance is "trivial to forge"; only L2+ requires a build platform the tenant cannot modify), metrology (ISO/IEC 17025 cl. 6.5: traceability to an INDEPENDENT reference — an instrument certifying itself has none), and regression testing (Rothermel & Harrold 1997: safety requires re-running modification-traversing tests). The presumption conflates "the fix is correct" with "prior output was unaffected"; no doctrine found licenses that inference. FIFTH member of the self-certifying family, and it sits at the TOOLING layer BENEATH the other four — it can silently invalidate the evidence they are argued from.
  What is at risk: If the resolver defect predates the 2026-07-12 run, the entire connectivity CSV series is silently biased; three items in this cohort (A-447, A-448, P-475) inherit the bias; and the run that would have detected this instead closed the question. Terminal exoneration removes the last detection path — the REVISE-209 hazard, one layer down.
  Recommended action for Tom: Convention — NO SELF-PRODUCED ARTIFACT MAY CERTIFY ITSELF, at the tooling layer: a self-caught, self-fixed defect is confirmed by REPLAY (re-run the corrected tool over every prior input; diff against emitted output). Empty diff -> exonerated BY RE-EXECUTION. Non-empty -> back-correct. Replay infeasible -> prior output is marked PROVISIONAL in every downstream artifact that consumes it, not clean. NEARLY-FREE FIRST STEP: read the resolver's git history and DATE the defect. Subsumes MONITOR-436; unifies with REVISE-209 (denominators) and REVISE-214 (captures) under ONE rule — see SYSTEMIC-RISK #1.
  Urgency: Medium-High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-214:
  Date: 2026-07-13 | Source item: PRESUMPTION-477 (PRESUMPTION, unstated) | from DISPOSITION-472
  Statement: Agent-mediated captures are sufficient evidence to overturn a months-standing bridge classification and seed the paradigm-shift channel — no primary-text verification pass before master-agent routing.
  Why flagged: Decisive at the THRESHOLD level. Human secondary capture already misquotes ~1 time in 4 (Jergas & Baethge 2015, PeerJ 3:e1364 — 25.4%; corroborated in history by Lehmann et al. 2023, Scientometrics — 24.27%); LLM attribution specifically is worse (Walters & Wilder 2023, Sci Rep 13 — 18-55% fabricated citations, 24-43% of the real ones carrying substantive errors); and INTRINSIC hallucination — using the source's own vocabulary while misrepresenting its claim — is invisible to any check short of reading the source (Maynez et al. 2020, ACL). Greenberg 2009 (BMJ 339:b2680) names the systemic mechanism: an unverified secondary claim, routed onward, acquires authority through REPETITION rather than evidence. 15a's support was collected on structured extractive content (RCT reports, news), which is not this task.
  ** THE FAILURE ALREADY OCCURRED, IN THIS RUN, ON THE FLAGSHIP ITEM. ** 15b's independent primary-source pass on ASSUMPTION-449 found Kastrup explicitly affirming a "dissociative hierarchy" with sub-alters and layered internal dissociation — directly contradicting the capture-derived "incompatible mereologies" framing. Kastrup himself notes this material is "not to be found in anything I have written" (it appears in an interview, not the written corpus), which is precisely why the capture missed it. One primary-source pass caught it, on the channel's first real use. This flag is now backed by EVIDENCE, not merely doctrine.
  What is at risk: The paradigm-shift channel is C2A2's highest-signal pathway. Feeding it unverified secondary material converts it into its highest-VARIANCE one. A capture-artifact false positive corrupts C2A2's central evidence stream, and every downstream artifact inherits it unmarked.
  Recommended action for Tom: GATE the paradigm-shift channel behind a primary-text verification pass. (1) Every capture triggering a reclassification must carry VERBATIM quotations with locators (page/section/timestamp). (2) Label captures LEAD, not FINDING, until they pass the gate — captures remain excellent LEAD GENERATION and that use should continue unchanged. (3) Run a FActScore-style atomic decomposition (Min et al. 2023, EMNLP) against the primary text. (4) Sample-audit 10 existing captures underwriting standing bridge classifications and measure the misattribution rate; given that the FIRST such check returned a miss, set the prior high. Same rule as REVISE-213 and REVISE-209, applied at the INPUT layer — see SYSTEMIC-RISK #1.
  Urgency: HIGH (gates the first use of the paradigm-shift channel; ASSUMPTION-449/MONITOR-438 is blocked on it)
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED


## 2026-07-16 — REVISE flags from 15a/15b/15c pipeline run (autonomous; 07-13/07-14-backfill/07-15 batches)

SYSTEMIC-RISK #4:
  Date: 2026-07-16
  Affected items: ASSUMPTION-454, ASSUMPTION-456, PRESUMPTION-478 (invisibility), PRESUMPTION-481, PRESUMPTION-482, PRESUMPTION-483
  Common vulnerability: LIVENESS-AS-SUCCESS. The fleet's only failure detector (the scheduler watchdog) reads firing / a current lastRunAt as success. Consequently silent crashes that write nothing (A-456; 07-14 x4), verification checks pointed at unreachable paths (A-454), quota exhaustion on delivery paths (P-478), crashed-but-unretried runs with no started-but-unfinished signal (P-481), un-measured audit coverage (P-482), and redundant monitors that share the one lastRunAt signal (P-483) are ALL invisible to it. The redundancy is illusory: multiple green checks reduce to one correlated signal (Knight & Leveson).
  Literature basis: liveness-vs-correctness monitoring (heartbeat != health); gray/silent-failure; survivorship bias in audit coverage; N-version / common-cause failure (Knight & Leveson 1986); crash-only design (Candea & Fox 2003).
  Risk level: Critical
  Recommendation: treat "the watchdog is green" as evidence of liveness only. Add an artifact-content check per output-bearing task (REVISE-215), durable start/finish markers + a started-but-unfinished alarm (REVISE-216), a quota-exhaustion alarm (REVISE-219), a coverage ratio (MONITOR-443), and a monitor->signal independence audit (MONITOR-444). NOTE: SYSTEMIC-RISK #1 (self-certification) is addressed this run by PREMISE-096 (A-452) — its proposed terminator.

REVISE-215:
  Date: 2026-07-16 | Source item: ASSUMPTION-454 + ASSUMPTION-456 (ASSUMPTION, stated; QUEUED-EMPIRICAL) | from DISPOSITION-475, DISPOSITION-480
  Statement: FIRING-HEALTH / UNFALSIFIABLE-GREEN-CHECK. Two of the watchdog's three output checks point at unmounted paths and can never fail (A-454); and a current lastRunAt is read as a valid non-empty output, so the watchdog called 07-14 healthy while four tasks crashed and wrote nothing (A-456).
  Why flagged: 15a Strong on both — the liveness-vs-correctness distinction is foundational, and a check wired to an unreachable target is a canonical unfalsifiable green check that inflates apparent coverage. 15b found NO defense of either practice. This is the generative defect behind SYSTEMIC-RISK #4, demonstrated in-run on 07-14.
  What is at risk: the fleet's sole failure detector certifies crashed, empty-output runs as healthy; true coverage is ~1/3, not 3/3.
  Recommended action for Tom: (1) verify the watchdog's sandbox mounts against its three verification paths; mount the folders in the watchdog's environment or DROP the two inert rows and report coverage honestly. (2) Add an artifact-content check (non-empty, well-formed, recent mtime) for every output-bearing task; for one day compare the lastRunAt-set against the valid-artifact-set (07-14's four crashes are a ready sample).
  Urgency: High
  PROVENANCE: Origin 14a; Chain [14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-216:
  Date: 2026-07-16 | Source item: ASSUMPTION-458 + PRESUMPTION-481 (mixed; QUEUED-EMPIRICAL / unstated) | from DISPOSITION-482, DISPOSITION-483
  Statement: CHECKPOINT-BEFORE-WORK / DURABILITY. "The .md persists even if delivery fails" assumes the failure lands at the delivery step, but a crash before Step 2 writes no file (A-458); and a crashed mid-run task is presumed a harmless idempotent no-op covered by tomorrow, though the four 07-14 crashes retried nothing, left no partial artifact, and raised no alarm (P-481).
  Why flagged: 15b Strong on both, grounded in write-ahead logging / ARIES (durable write must precede the risky operation) and crash-only design / at-least-once semantics (idempotent-and-skippable requires checkpointing + retry + a started-but-unfinished marker). A-458 was FALSIFIED in-run on 07-14.
  What is at risk: any crash before the write step loses the whole deliverable; a whole day's throughput can vanish with no record it was attempted.
  Recommended action for Tom: write a checkpoint/skeleton .md BEFORE the long read or any crash-prone step (treat the deliverable as write-ahead, not a late artifact); add durable start + completion markers, retry-on-crash, and a "started-but-unfinished" alarm the watchdog reads.
  Urgency: High
  PROVENANCE: Origin 14a/14b; Chain [14a/14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-217:
  Date: 2026-07-16 | Source item: ASSUMPTION-455 + ASSUMPTION-460 + PRESUMPTION-484 (mixed; QUEUED-EMPIRICAL / unstated) | from DISPOSITION-476, DISPOSITION-486, DISPOSITION-488
  Statement: STALE SELF-DESCRIPTION / STALE-WATCH — EVIDENCE-FRESHNESS GATE. The master wiki has not been written since 07-09 while daily runs report success and its network-state block diverges from pattern_detector_findings.md (A-455); its un-ingested 07-10->07-14 deposits feed the FINDING-048 / FLAG-016 paradigm-shift watch, turning ingestion lag into a stalled evidence path into a live flag (A-460); and flags are presumed to self-refresh, so FINDING-048 is carried as a live watch with no staleness marker while its evidence is frozen (P-484).
  Why flagged: 15b grounded in data-freshness SLA + stale-while-revalidate / cache-coherence doctrine — derived/authoritative state served without a freshness marker while its source is frozen is a coherence violation; consumers cannot tell live from stale. On the paradigm-shift channel (C2A2's central evidence stream) this is high-severity.
  What is at risk: every agent reading the master wiki as current is misinformed; FINDING-048 could be confirmed or killed on evidence that stopped arriving 07-10; a stalled watch is indistinguishable from a live one downstream.
  Recommended action for Tom: add an explicit as-of timestamp + evidence-freshness gate to the master wiki AND to every flag/watch; block confirm/kill transitions under stale ingestion; trace FINDING-048's confirm/kill condition to the un-ingested deposits and repair the ingestion; fix the daily refresh that fires but writes nothing (ties to REVISE-215). Kin to OPEN-112.
  Urgency: High
  PROVENANCE: Origin 14a/14b; Chain [14a/14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-218:
  Date: 2026-07-16 | Source item: PRESUMPTION-479 + ASSUMPTION-461 + PRESUMPTION-485 (mixed; QUEUED-EMPIRICAL / unstated) | from DISPOSITION-478, DISPOSITION-487, DISPOSITION-489
  Statement: OPEN-WORLD / MULTIPLE-CAUSE FAILURE. The sync-outage diagnosis presumed failure modes are mutually exclusive — that finding a cause is finding the cause (P-479); today's connection errors are filed as a clean "third distinct cause" after login and quota (A-461); and the cause set is presumed closed and enumerable, so each new signature is absorbed as the final one and every point-fix (REVISE-198/199) is defeated by the next unmodeled cause (P-485).
  Why flagged: 15b Strong, grounded in resilience engineering (R.I. Cook, "How Complex Systems Fail": each contributor necessary, only jointly sufficient; "the root cause" is a blame construct) and fault-masking (a known cause hides a co-occurring one). Three new signatures in ~two weeks (login -> quota -> connection) empirically refute closure; enumerate-and-patch cannot converge.
  What is at risk: remedy budget spent chasing a receding tail; every prior sync-outage diagnosis accepted on single-cause reasoning; the fleet stays brittle to the next unmodeled cause while each fix "works" against the cause it targeted.
  Recommended action for Tom: shift from enumerate-and-patch to GRACEFUL DEGRADATION / defense-in-depth; make delivery paths fail soft; adopt contributing-factors analysis and score each failure DIRECTION independently (re-score MONITOR-434 per-direction); classify crash tails by error string AND surviving artifact AND co-occurring conditions; count distinct signatures since 07-01 and, for each, how many prior remedies it defeated.
  Urgency: Medium-High
  PROVENANCE: Origin 14b/14a; Chain [14b/14a -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

REVISE-219:
  Date: 2026-07-16 | Source item: PRESUMPTION-478 (PRESUMPTION, unstated) | from DISPOSITION-477
  Statement: MODEL-QUOTA ADMISSION CONTROL. Model quota is presumed an unmetered substrate — ~37 daily tasks with no budget, no back-pressure, no exhaustion alarm, no precedence; the evening delivery died on "out of usage credits" while the day's producers ran to completion and the watchdog reported all clear.
  Why flagged: 15a found NO support for treating a finite resource as unmetered; 15b Strong — admission-control / load-shedding literature (RED, Floyd & Jacobson 1993; CoDel, Nichols & Jacobson 2012; SRE load-shedding practice) uniformly requires metering, back-pressure, and priority under exhaustion. Because producers are scheduled before delivery, the quota is systematically consumed by lower-value work — a designed-in precedence inversion, invisible to the liveness-only watchdog. PRESUMPTION + strong challenge -> REVISE, HIGH.
  What is at risk: delivery/reconciliation (the human-facing output); every queued remedy that assumes a working channel (REVISE-198/199).
  Recommended action for Tom: introduce a token/quota budget with back-pressure; a precedence order that protects delivery over producers (shed low-value producer work first under exhaustion); and an exhaustion alarm the watchdog can read. Plot the cost-tracker's daily series against the account ceiling to confirm and to set the budget.
  Urgency: High
  PROVENANCE: Origin 14b; Chain [14b -> 15a,15b -> 15c]; Current status: REVISION-FLAGGED

---

## 2026-07-17 — new REVISE flags from 15c (DISPOSITION-491/493/494/496)

REVISE-220:
  Date: 2026-07-17 | Source item: ASSUMPTION-463 (stated) | Disposition: DISPOSITION-491 | Urgency: HIGH
  Problem: Git-persistence cannot self-complete from the autonomous sandbox (mount denies .git object writes; no push creds); outputs left "staged for the Mac" and unpersisted across an 11-day autonomous stretch.
  At risk: All autonomous run outputs incl. ~470-file Summa diff; durable store unreachable without a human.
  Recommended action (Tom): Add a credentialed, review-gated staging-ref persistence path + age-based escalation; preserves No-Blind-Push while ending indefinite non-persistence.
  15a: SUPPORTED (Moderate-Strong) | 15b: PARTIALLY-CHALLENGED (Moderate)
  PROVENANCE: Origin=14a; Chain=[14a -> 15a,15b -> 15c]; Item type=ASSUMPTION

REVISE-221:
  Date: 2026-07-17 | Source item: PRESUMPTION-486 (unstated) | Disposition: DISPOSITION-493 | Urgency: HIGH
  Problem: Re-syncing the narrative status line is presumed to discharge staleness; indicator reads current while FINDING-048's feeding deposits stay un-ingested (Goodhart substitution).
  At risk: FINDING-048 (FLAG-016) paradigm-shift watch indistinguishable from live while its evidence is frozen.
  Recommended action (Tom): Require a freshness gate binding narrative-date to evidence-age; render a staleness badge. Consolidate with REVISE-217.
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Weak-Moderate)
  PROVENANCE: Origin=14b; Chain=[14b -> 15a,15b -> 15c]; Item type=PRESUMPTION

REVISE-222:
  Date: 2026-07-17 | Source item: PRESUMPTION-487 (unstated) | Disposition: DISPOSITION-494 | Urgency: HIGH
  Problem: No-Blind-Push + "staged for the Mac" presume a human appears regularly; on an 11-day autonomous stretch the safety rule became a durability failure ("staged == never persisted").
  At risk: Every run's durable output hinges on an absent human step.
  Recommended action (Tom): KEEP No-Blind-Push (do not fail-open); add durable staging + age-based human-on-the-loop escalation. 15b warns fail-open would trade a durability problem for an integrity problem.
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate)
  PROVENANCE: Origin=14b; Chain=[14b -> 15a,15b -> 15c]; Item type=PRESUMPTION

REVISE-223:
  Date: 2026-07-17 | Source item: PRESUMPTION-489 (unstated) | Disposition: DISPOSITION-496 | Urgency: MEDIUM-HIGH
  Problem: Agent outputs presumed cleanly separable from a shared base; a shared working tree lets one agent's incidental churn (470-file last_qc_at bumps) stall another agent's commit — no per-agent isolation.
  At risk: Commit stalls and entangled reviews; compounds PRESUMPTION-446 (SYSTEMIC-RISK #1 Critical, shared repo / no coordination protocol).
  Recommended action (Tom): Give each scheduled agent its own git worktree/clone (private index/HEAD); add commit retry-with-backoff.
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate)
  PROVENANCE: Origin=14b; Chain=[14b -> 15a,15b -> 15c]; Item type=PRESUMPTION

REVISE-224:
  Date: 2026-07-18 | Source item: ASSUMPTION-465 (stated) | Disposition: DISPOSITION-497 | Urgency: HIGH
  Problem: Today's git-persistence blocker is framed as a stale unremovable `.git/index.lock` from a concurrent 04:40 process — a "different proximate cause" than A-463. But "Operation not permitted" on lock REMOVAL points to the mount/permission root, i.e. the SAME family as A-463.
  At risk: Git persistence. A lock-hygiene fix could leave the mount write-permission blocker intact; compounds durability (REVISE-220/222).
  Recommended action (Tom): Run the discriminator as the scheduled user on the mount — `touch .git/index.lock && rm .git/index.lock`. Removal denied -> mount/permission root (fix once at credential/mount layer, resolves A-463+A-465); removal succeeds -> distinct lock-hygiene (per-agent worktree/lock cleanup, see REVISE-223).
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate)
  PROVENANCE: Origin=14a; Chain=[14a -> 15a,15b -> 15c]; Item type=ASSUMPTION

REVISE-225:
  Date: 2026-07-18 | Source item: ASSUMPTION-466 (stated) | Disposition: DISPOSITION-498 | Urgency: MEDIUM-HIGH
  Problem: Metabolism regen script relies on `~/`/implicit HOME, which resolves to the sandbox home under the scheduler (exit 1). But the operative staleness is the OpenStory writer freeze (db unwritten since 07-05); a path-only fix yields a false "fixed."
  At risk: The metabolism view (recurs consecutive days).
  Recommended action (Tom): (1) explicit mount-aware absolute paths (not `~/`); (2) verify the mount exposes the live db path; (3) unfreeze the OpenStory writer; (4) bind "refreshed" to db mtime (see MONITOR-448 / P-491). Do not close on exit-0 alone.
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Weak-Moderate)
  PROVENANCE: Origin=14a; Chain=[14a -> 15a,15b -> 15c]; Item type=ASSUMPTION

REVISE-226:
  Date: 2026-07-18 | Source item: ASSUMPTION-467 (stated) | Disposition: DISPOSITION-499 | Urgency: MEDIUM
  Problem: A maintained 300-PRS narrative figure is treated as canonical over the computed per-file sum (447); two same-day agents advanced different counts. Dual-bookkeeping guarantees drift, but neither figure is canonical without a PRS DEFINITION — auto-adopting the computed sum risks over-counting (Goodhart-by-mechanization).
  At risk: Metric integrity; narrative-vs-evidence family; OPEN-112.
  Recommended action (Tom): Write an explicit PRS counting rule; compute both figures under it; reconcile once; designate a single AUTOMATED canonical counter so agents cannot diverge. Treat the 300/447 gap as a definitional signal, not a defect to eliminate toward one side.
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate)
  PROVENANCE: Origin=14a; Chain=[14a -> 15a,15b -> 15c]; Item type=ASSUMPTION

REVISE-227:
  Date: 2026-07-18 | Source item: PRESUMPTION-492 (unstated) | Disposition: DISPOSITION-502 | Urgency: MEDIUM-HIGH
  Problem: The lit pipeline presumes 15d RE-TRIGGER generation stays within daily drain capacity; a 129-item undrained backlog (07-05, 07-12) persists. Queueing theory confirms lambda>mu -> unbounded growth, but a two-cohort snapshot cannot distinguish rate-instability from a COVERAGE bug (the daily loop structurally skips RE-TRIGGER cohorts) — and the pipeline's own logs favor the omission hypothesis.
  At risk: The searched corpus silently diverges from the enqueued corpus (integrity of the 15-pipeline). This is the live backlog repeatedly not drained (see BACKLOG NOTE in lit_search_returns.md).
  Recommended action (Tom/orchestrator): MEASURE FIRST — log 15d enqueue/day vs 15abc drain/day for 1-2 weeks. enqueue<=drain but backlog persists -> omission: schedule RE-TRIGGER (and the 18 orphaned 06-29..07-06 EMPIRICAL) cohorts into the drain loop. enqueue>drain sustained -> add bounded work-queue + fan-out cap + STALE/TTL aging. Different mechanisms, different fixes.
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate)
  PROVENANCE: Origin=14b; Chain=[14b -> 15a,15b -> 15c]; Item type=PRESUMPTION

REVISE-228:
  Date: 2026-07-18 | Source item: PRESUMPTION-493 (unstated) | Disposition: DISPOSITION-503 | Urgency: HIGH
  Problem: Fail-loud presumes an attending listener within bounded time; on day 12 of no attended session, loud surfacings accumulate unactioned (17-day review gap, 27 proposals, staged-not-pushed writes). Generalizes P-487 beyond No-Blind-Push. 15b narrows the true harm to PERISHABLE-referent surfacings (durable idempotent ones are deferred, not lost) and warns drastic auto-action would reintroduce blind-push risk.
  At risk: Perishable-referent surfacings that decay while unattended — unpushed git writes (may never persist), frozen dbs, expiring credentials.
  Recommended action (Tom): (1) ensure all surfacings are durable; (2) classify surfacings by referent durability; (3) wire ONLY perishable-referent items to a time-bounded fallback (alternate channel or a bounded, review-gated autonomous persistence step) so a lone absent listener is not a single point of failure — without opening a blind-push hole for durable items. Consolidate with REVISE-220/222.
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Weak-Moderate)
  PROVENANCE: Origin=14b; Chain=[14b -> 15a,15b -> 15c]; Item type=PRESUMPTION

---

# ===== 2026-07-19 Agent 15c dispositions — 2026-07-18 EOD batch (12 items) =====

REVISE-229:
  Date flagged: 2026-07-19
  Source item: ASSUMPTION-468
  Item type: ASSUMPTION (stated)
  Net assessment: 15a and 15b agree the diagnosis is sound (a sandbox-context failure is architectural, not flaky). They diverge entirely on the proposed remedy: 15b retrieved three independently documented mechanisms by which loopback is blocked in sandboxed agent runtimes (socket-layer EPERM, browser SSRF policy, Chrome Local Network Access) plus a direct counterexample (openai/codex #24559) where the service was reachable and navigation still failed.
  Reasoning: The item bundles a well-supported observation with an unvalidated remedy. Standing up a local HTTP server is a multi-step build whose success hypothesis has a documented failure mode and a one-line discriminating test that has not been run. Disposition targets the remedy, not the diagnosis.
  What is at risk: The delivery leg of the review workflow; the 29-proposal backlog depends on reviewer notification actually arriving.
  Recommended action: Before building anything, run a one-line loopback socket test from the scheduled sandbox context (bind + connect on 127.0.0.1). If it returns EPERM, the localhost fix is dead on arrival and an out-of-band delivery route (file path in the report body, or email) is the correct design. Split the item: the diagnosis half is INCORPORATE-ready once the remedy is settled.
  Urgency: High
  Status: OPEN — awaiting Tom's review
  Full results: lit_search_results/for/ASSUMPTION-468_for.md ; lit_search_results/against/ASSUMPTION-468_against.md

REVISE-230:
  Date flagged: 2026-07-19
  Source item: ASSUMPTION-470
  Item type: ASSUMPTION (stated)
  Net assessment: Both directions converge on the same finer distinction and it cuts against the item. The systematic-review literature (Mateen et al. 2013, PMID 23526335) validates title/abstract screening as a filter with mandatory downstream full-text re-adjudication, not as a terminal evidential basis carrying a confidence label. 15a's own supporting search returned this caveat unprompted; 15b found the same boundary independently.
  Reasoning: Two independent searches landing on the same boundary condition is the strongest signal available here. This also resolves an existing internal contradiction in C2A2's favour: REVISE-214 already treats this evidential gap as blocking rather than downgrade-able, and the literature sides with REVISE-214. Confidence-downgrading is the wrong instrument for a kind-difference in evidence.
  What is at risk: PRS corpus quality — every Medium-confidence candidate admitted on publisher metadata alone; and the coherence of the confidence scale itself, which currently spans both degree- and kind-differences in evidence.
  Recommended action: Adopt REVISE-214's treatment as canonical: no confidence label is well-founded when primary text is unavailable. Introduce an explicit 'unfounded — pending retrieval' state rather than a downgrade, and re-adjudicate the affected June 3 candidates once the transcript is retrieved by a permitted route. Separately, the 30-day primary-material window relaxation returned zero supporting evidence in either direction and should be treated as an unexamined change.
  Urgency: High
  Status: OPEN — awaiting Tom's review
  Full results: lit_search_results/for/ASSUMPTION-470_for.md ; lit_search_results/against/ASSUMPTION-470_against.md

REVISE-231:
  Date flagged: 2026-07-19
  Source: Agent 15b SYSTEMIC-RISK-FLAG (High), 2026-07-19 — not tied to a single queue item
  Affected items: ASSUMPTION-468, ASSUMPTION-469, ASSUMPTION-472, PRESUMPTION-494, PRESUMPTION-495, PRESUMPTION-498, PRESUMPTION-499 (7 of 12)
  Pattern: remedy-jumping under single-explanation bias. In each item the observation is well evidenced but the pipeline proposes a remedy that the literature names as an anti-pattern, or that is unvalidated against the actual mechanism, while a cheap discriminating test exists and was not run.
  Second thread: three of the proposed remedies (A-472 enable dormant checks; P-495 TTL / auto-escalation; A-469 blocking emission gate) all increase signal volume into a channel with demonstrated zero throughput. The alert-fatigue evidence predicts suppression that degrades the signals already working.
  Recommended action: introduce a discriminating-test step between surfacing and remedy across the 14/15 pipeline — no remedy proposed without naming the cheapest test that would falsify the diagnosed mechanism. Separately, cap net new alert volume until the review channel has demonstrated non-zero throughput.
  Urgency: High
  Status: OPEN — awaiting Tom's review

REVISE-232:
  Date flagged: 2026-07-19
  Source: narrow sub-claim of PRESUMPTION-496 (item dispositioned MONITOR — see MONITOR-450)
  Note: 15a and 15b disagree strongly on P-496's general claim but agree on this narrow one, so it is broken out for independent action.
  Finding: the No-Blind-Push rule is scoped to writes, but a read-only diagnostic (the .git/index.lock discriminator) was deferred under it. Restraint was applied beyond the rule's actual scope.
  Recommended action: clarify No-Blind-Push to state explicitly that read-only diagnostics are always in scope for autonomous execution. Cheap, reversible, and independent of the contested general claim.
  Urgency: Medium
  Status: OPEN — awaiting Tom's review


---

# ===== 2026-07-20 Agent 15c dispositions — 2026-07-19 EOD batch (4 REVISE items) =====

REVISE-233:
  Date flagged: 2026-07-20
  Source item: ASSUMPTION-477
  Item type: ASSUMPTION (stated)
  15a: SUPPORTED (Strong) | 15b: CHALLENGED (Strong)
  **ADJUDICATED DIRECT CONFLICT — the two agents returned opposite verdicts at equal strength on this item. Averaging was refused; the conflict is resolved below on the evidence.**

  Net assessment: The two verdicts are not verdicts on the same proposition, and separating the propositions dissolves most of the conflict and settles the remainder against the item.
    (i) THE DATED FACT — "independence became structural on 2026-07-19; every prior disposition was produced under asserted independence." 15a explicitly declines to assess it (outside search scope, an internal-record claim). 15b explicitly states it is "not challenged." The fact is therefore UNCONTESTED by both agents and is not what either verdict is about.
    (ii) THE NORMATIVE CORE — "asserted independence is materially weaker than enforced independence." This is what 15a graded Strong, citing arXiv:2606.29270 (LLMs share pretraining corpora and architectures, so their errors correlate and violate the Condorcet independence assumption; the correlated majority suppresses correct minority findings) and arXiv:2606.10296 (an LLM judge over correlated LLM inputs can make the aggregate WORSE than either input — a claim that bears directly on this agent). Uncontested by 15b.
    (iii) THE IMPLIED CONSEQUENCE — that the pre-07-19 record is therefore materially contaminated and the 905 existing pairs should be discounted or re-run. This is what 15b graded Strong AGAINST, citing van Rooyen et al., JAMA 1998 (PMID 9676666): 527 consecutive BMJ manuscripts randomized, blinding "made no editorially significant difference to review quality, reviewers' recommendations, or time taken" — masked 2.82 vs unmasked 2.96. The one trial usually cited for blinding's value, McNutt 1990, is a quarter the size and reports 3.5 vs 3.1.

  Adjudication and reason for deciding rather than averaging: van Rooyen is the largest randomized trial of THE SPECIFIC INTERVENTION at issue — blinding one evaluator to another's assessment — and it is null. 15a knew of it: van Rooyen appears as source 5 in 15a's own file, reported under the no-cherry-picking rule, and 15a still graded Strong. That is not a disagreement about the source; it is 15a grading proposition (ii) while 15b graded proposition (iii). Decisively, 15a's OWN strongest sources undercut the item's implied relief. 15a's caveat (c) reads: "structural file-access blocking does not address shared-pretraining correlation, which is the dominant channel in the retrieved literature. The 905-pair record may be contaminated by a mechanism the 07-19 fix does not touch. This is support for the item's concern but not for its proposed resolution." 15b's symmetric risk reads: "declaring independence 'now structural' invites the belief that the remaining sources of correlation are handled. They are not." **The two agents converge on the operative finding: the read channel is not the dominant correlation source, and 2026-07-19 removed the weakest of at least four.** The item as written claims more than either agent supports, in the direction that produces both a costly action and a false sense of security. That is a design representation to revise, not a premise to incorporate or a contest to monitor.

  Reasoning: This is dispositioned REVISE rather than MONITOR because the design change has already been made and is already being represented — "independence became structural" appears in this batch's own 15a return header. An inaccurate label on a live architectural property, propagating into every disposition produced under it, is not something to watch for a week. The revision is cheap, is textual, and both agents recommend the same wording.

  What is at risk: (1) The scarcest resource in the system. PREMISE-106 establishes the drain rate as the binding constraint; re-deriving 905 pairs to correct an effect whose closest empirical analogue sizes near zero would consume it entirely. (2) Every disposition produced from 2026-07-19 onward, including this one, which inherits a correlation channel it is describing. (3) The false-security failure this vault has already named in PRESUMPTION-505 / PREMISE-110 — a green signal ("independence achieved") over an unfixed condition, which is the REMEDY-INHERITS-DEFECT pattern in REVISE-236 applied to the pipeline's own architecture.

  Recommended action (Tom / orchestrator):
    1. RELABEL, do not re-run. Report the 2026-07-19 change as "READ-CHANNEL INDEPENDENCE ENFORCED," never as "independence achieved." Both agents recommend this wording independently. It is accurate and it is free.
    2. DO NOT discount or re-derive the 905-pair record on the strength of an unmeasured contamination assumption.
    3. If a contamination estimate is wanted, use the design that isolates the variable: take ~20 pre-07-19 items and, IN ONE SESSION with one model version, one prompt and one corpus snapshot, run each twice — once with 15a's file readable, once blocked. The paired difference in 15b challenge strength is the blinding effect, cleanly isolated. Record it with its interval and stop. The item's own proposed test (re-run pre-07-19 dispositions under blocking) varies blinding TOGETHER WITH model version, prompt revision, retrievable literature and a year of vault content, so its delta is uninterpretable as a contamination estimate — the item's test does not measure what the item claims.
    4. ADDRESS THE DOMINANT CHANNEL. Run 15a and 15b on the same item under full blocking and measure how often they cite the SAME SOURCES. High overlap under enforced blocking means the shared corpus and shared pretraining are the real channel and the 07-19 change addressed the wrong one. This is the measurement that matters and it has never been taken.
  Urgency: Medium (the relabel is immediate and costless; the measurement is not urgent, but the record must stop claiming what it has not established)
  Status: OPEN — awaiting Tom's review
  Full results: lit_search_results/for/ASSUMPTION-477_for.md ; lit_search_results/against/ASSUMPTION-477_against.md
  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-477
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline transcript
      15a: Searched for supporting literature; SUPPORTED (Strong) — graded on the normative core
      15b: Searched for challenging literature; CHALLENGED (Strong) — graded on the implied consequence
      15c: Net evaluation and disposition; conflict adjudicated by separating the three propositions and deciding on source directness; REVISE
    Current status: REVISION-FLAGGED (CONTESTED, adjudicated)
    Disposition record: DISPOSITION-ASSUMPTION-477 (lit_search_returns.md, 2026-07-20)

REVISE-234:
  Date flagged: 2026-07-20
  Source item: ASSUMPTION-481
  Item type: ASSUMPTION (stated)
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Moderate)
  Net assessment: The DIAGNOSIS is uncontested and well evidenced on both sides — connector enumeration has failed four consecutive weeks, all classification is fallback, a genuinely uninstalled connector is undetectable, and the retraction of the prior week's "too charitable" explanation is behaviour both agents endorse. It is already covered in general form by PREMISE-110 (detectors invert; a fallback that manufactures plausible-shaped output is, in the retrieved phrasing, "a hallucination implemented in shell"). What is flagged here is the RESPONSE, where the two agents cite opposed literatures and 15b's is the stronger evidence. 15a cited epistemic-humility framings (arXiv:2605.23614, 2512.19466) that ASSERT abstention is correct; these are preprints and assert rather than measure, and 15a's own caveat (b) concedes "no effect sizes were found" and notes a countervailing literature it did not search. 15b cited van der Bles et al., PNAS 2020 (PMID 32205438) and Royal Society Open Science 2023 (doi 10.1098/rsos.230604), which MEASURE the effect and find it sharply format-dependent: NUMERIC uncertainty expressed as a range or interval costs little credibility and can increase it, while UNQUANTIFIED VERBAL uncertainty consistently lowers trust in the information AND in the source. Declining to state any figure is the unquantified form taken to its limit — the version the evidence disfavours.
  Reasoning: The mechanism matters more than the effect size and it applies directly here. Uncertainty communication permits belief-consistent processing: an abstention does not deliver "we don't know," it leaves the reader holding their prior — which for a weekly connector report is the last number they saw. That number is the fallback-derived count the agent has just repudiated. **The abstention therefore republishes the disputed figure with the caveat quietly removed, while appearing to withhold it.** This is the REMEDY-INHERITS-DEFECT pattern (REVISE-236) in its cheapest form: answering "our number may be wrong" with silence leaves the consumer holding the same wrong number, uncaveated. A better-evidenced report was available and was not made.
  What is at risk: The connector-health weekly's usefulness as a signal, and the integrity of its own series. Four weeks of fallback classification are now unlabelled and a fifth week is absent — a discontinuity in the agent's own reporting series, which is PREMISE-105's break-in-series problem appearing in a different register and with the same fix. Downstream: any artifact that cites a connector count.
  Recommended action (Tom / orchestrator):
    1. REPORT A DIRECTIONAL BOUND, DO NOT ABSTAIN. The correct report was available: "at least N installed; uninstalled connectors are undetectable under fallback, so the true count is N or higher." State uncertainty numerically; avoid unquantified verbal hedging.
    2. WHERE ABSTENTION IS GENUINELY CORRECT, state explicitly what the consumer should NOT infer — that the previous number still holds — because the belief-consistency evidence says they will otherwise infer it.
    3. RETAIN AND LABEL the four weeks of fallback classification as a known-biased series with the bias direction named. Reconciliation practice treats a known-biased source as usable once the direction is stated. Discarding it forfeits the only evidence available for sizing the error — which is exactly what the item's own in-house test proposes to recover later.
    4. APPLY THE PREMISE-105 TREATMENT to the four-week record: it has a break and needs a marker or a re-derivation, and the same decision applies.
    5. REPAIR ENUMERATION, then compare four weeks of fallback classification against ground truth to measure the fallback error rate. This is the item's own well-formed discriminating test and it also settles whether the floor claim the agent declined to make would have been correct.
    6. VERIFY THE PREDICTION CHEAPLY: inspect the next artifact that cites a connector count. If the pre-abstention fallback figure reappears uncaveated, the abstention failed in exactly the predicted way and step 1 becomes mandatory rather than advisory.
  Urgency: Medium
  Status: OPEN — awaiting Tom's review
  Note: the diagnosis half of this item is INCORPORATE-ready once the reporting convention is settled (precedent: REVISE-229, 2026-07-19). It is not incorporated now because the item as stated bundles the diagnosis with the endorsed abstention, and incorporating the bundle would validate the disfavoured response.
  Full results: lit_search_results/for/ASSUMPTION-481_for.md ; lit_search_results/against/ASSUMPTION-481_against.md
  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-481
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 connector health weekly transcript
      15a: Searched for supporting literature; SUPPORTED (Strong)
      15b: Searched for challenging literature; PARTIALLY-CHALLENGED (Moderate — against the response, not the diagnosis)
      15c: Net evaluation and disposition; REVISE targeting the reporting convention; diagnosis held for incorporation once settled
    Current status: REVISION-FLAGGED
    Disposition record: DISPOSITION-ASSUMPTION-481 (lit_search_returns.md, 2026-07-20)

REVISE-235:
  Date flagged: 2026-07-20
  Source item: PRESUMPTION-500
  Item type: PRESUMPTION (unstated — surfaced by inference)
  15a: SUPPORTED (Strong) | 15b: PARTIALLY-CHALLENGED (Strong, against the evaluation; the surfacing itself is NOT challenged)
  **Highest-stakes item in the batch. 14b's own risk note: "Critical — this is the target function of the accelerator."**
  Net assessment: Both agents agree on the surfacing and both agree the item's implied next move is unsafe, which is an unusual and informative convergence. THE SURFACING IS UNCONTESTED: convergence is nowhere stated as a hypothesis, is built into the Rung-2 detector and every cross-connection counter, and 14b checked decisions.md and assumptions.md and found no prior statement. THE PRESUMED CRITERION IS STRONGLY CHALLENGED BY 15a's OWN SUPPORTING SEARCH — and this is the key structural point: because the item is a critique, 15a's strong support for the item IS strong evidence against the presumption. Lorenz et al. (PNAS 2011) show mild influence toward convergence lowers accuracy WHILE RAISING CONFIDENCE, which makes a convergence-scored detector not merely a poor instrument but an INVERTING one — it would report improving success exactly as collective accuracy degrades, placing this in the same class as PREMISE-110. The diversity prediction theorem makes diversity a subtracted term in collective error. Three 2025-2026 results establish that LLM populations homogenise and that long-form debate specifically flattens, so convergence is the DEFAULT DRIFT of the substrate C2A2 runs on: an unstated presumption that convergence indicates success would systematically mistake substrate homogenisation for research progress. THE IMPLIED REPLACEMENT IS STRONGLY CHALLENGED BY 15b: MacIntyre, recruited by the item against convergence scoring, in fact argues rival traditions ARE rationally adjudicable with one defeated on the other's own terms — a convergence-shaped outcome; the ensemble literature reports an interior optimum rather than a monotone preference for preserved difference; and the leading instrument for the alternative signature, the Ideological Turing Test, operationalises passing as OPPONENTS AGREEING at or above the in-group rate, with the paper's own limitations section conceding it conflates persuasiveness with understanding.
  Reasoning: The item is dispositioned REVISE, not MONITOR, because the two halves have opposite time constants and opposite costs. The SUBSTANTIVE question — which signature is right — is genuinely contested and is monitored under MONITOR-453 (ASSUMPTION-475, the stated twin) pending a rank-correlation test. The DESIGN DEFECT — that the accelerator's target function has never been written down as a hypothesis anywhere in the record — is not contested by anyone, is the item's real contribution, is free to fix, and requires an authority this pipeline does not have. Leaving it in MONITOR would leave the target function undeclared for another week for no reason. This flag targets the declaration, and explicitly forbids the replacement.
  What is at risk: The Rung-2 detector, every cross-connection counter, and the accelerator's target function — i.e. what the whole system is optimising for. Secondarily: the interpretation of every cross-tradition result produced to date, all of which were scored against an undeclared criterion.
  Recommended action (Tom / orchestrator):
    1. STATE THE PRESUMPTION AS A HYPOTHESIS, in decisions.md, in the form "we are treating convergence as the success signature of inter-tradition dialogue; the alternative signature is mutual registration with preserved local optimization; this has not been tested." Both agents recommend it, it costs nothing, and it is the item's entire uncontested content.
    2. DO NOT REPLACE THE CRITERION. Removing convergence from Rung-2 scoring before a separable alternative exists leaves the rung unscored and, worse, UNFALSIFIABLE — two traditions talking past each other indefinitely satisfies "preserved local optimization." 15b's formulation is exact: replacing a possibly-wrong objective with an unmeasurable one converts it into no objective.
    3. INSTRUMENT BOTH AND REPORT THE PAIR. This is the ensemble literature's own recommendation and is ASSUMPTION-475's stated in-house test.
    4. RUN THE DISCRIMINATING TEST BEFORE CHANGING ANY DETECTOR: score existing dialogues under (a) convergence, (b) mutual registration, (c) an ITT-style measure, and compute pairwise rank correlations. Strong (b)-(a) correlation -> the dichotomy is false and the presumption is harmless. Weak correlation -> the disagreement set is the item's entire empirical content; inspect it by hand.
    5. IF AN ITT-STYLE INSTRUMENT IS ADOPTED, PUBLISH THE AGREEMENT-RATE CORRELATION ALONGSIDE THE SCORE. Otherwise the system will believe it has switched criteria while measuring the old one — 15b names this the worst of the three available states because it is invisible.
    6. MANDATORY PRE-DIALOGUE BASELINE (see CROSS-ITEM adjudication in REVISE-236 and in REVISE-233): C2A2's traditions are instantiated by agents drawn from a COMMON PRETRAINED MODEL, so an agent may produce a rival tradition's arguments fluently from shared pretraining rather than from registration acquired in dialogue. The ITT would then read high at baseline and be insensitive to the very thing it is meant to measure. No post-dialogue ITT score is interpretable without a pre-dialogue baseline.
    7. CONSIDER MACINTYRE'S OWN CRITERION as an independent third measure, which both agents proposed unprompted: can tradition A restate tradition B's position in B's vocabulary AND identify B's unresolved epistemic crisis? It is testable, it is not agreement, and it is not convergence.
  Urgency: HIGH (per the 15c spec: a PRESUMPTION whose presumed criterion is strongly challenged, at the target function of the system, where the designers did not know they were assuming it)
  Status: OPEN — awaiting Tom's review
  Full results: lit_search_results/for/PRESUMPTION-500_for.md ; lit_search_results/against/PRESUMPTION-500_against.md
  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: PRESUMPTION-500
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-07-19 sewing weekly transcript; checked against decisions.md and assumptions.md for any prior statement (none found)
      15a: Searched for supporting literature; SUPPORTED (Strong)
      15b: Searched for challenging literature; PARTIALLY-CHALLENGED (Strong, against the evaluation only)
      15c: Net evaluation and disposition; REVISE on the declaration, replacement explicitly forbidden pending MONITOR-453's test
    Current status: REVISION-FLAGGED
    Disposition record: DISPOSITION-PRESUMPTION-500 (lit_search_returns.md, 2026-07-20)

REVISE-236:
  Date flagged: 2026-07-20
  Source: Agent 15b SYSTEMIC-RISK-FLAG (High), 2026-07-20 — "REMEDY-INHERITS-DEFECT". Not tied to a single queue item. Evaluated, not passed through.
  Affected items as filed by 15b: ASSUMPTION-474, ASSUMPTION-476, ASSUMPTION-481, PRESUMPTION-500, PRESUMPTION-502, PRESUMPTION-503, PRESUMPTION-505 (7 of 14).
  Pattern: in seven of fourteen items the observation is sound and the proposed remedy reproduces, one level up, the exact property the observation was about — so running the remedy would produce a green signal over the unfixed condition, converting a VISIBLE defect into an INVISIBLE one. This is distinct from the 2026-07-19 flag (REVISE-231, remedy-jumping before a discriminating test): here the test is not merely skipped, the instrument is structurally isomorphic to the disease.

  15c EVALUATION OF THE FLAG (this is the part 15b could not do): the flag is UPHELD, and it was applied item-by-item rather than recorded. In every one of the seven cases the disposition above separates the observation from the instrument. Specifically:
    - A-474 (proxy replaced by a proxy subject to the identical Goodhart argument, and one agents can write to directly): PREMISE-105 incorporates the DIAGNOSIS and explicitly excludes connectivity as the replacement metric.
    - A-476 (a detector whose reference is generated by the monitored process, answered with a reference that is non-monotonic and drifts, fired into a channel with no consumer): MONITOR-454 holds the remedy pending a one-line clock check and a bulk-transition count; the diagnosis is absorbed into PREMISE-110.
    - A-481 ("our number may be wrong," answered with silence, which leaves the consumer holding the same wrong number uncaveated): REVISE-234 replaces abstention with a numeric floor and a stated error direction.
    - P-500 / A-475 ("we are measuring agreement instead of understanding," answered with an instrument whose passing criterion is opponents' agreement): REVISE-235 forbids replacement and mandates publishing the agreement-rate correlation; MONITOR-453 holds the substantive question.
    - P-502 ("flagging is presumed to be delivery," answered with acknowledgement receipts, under which "acknowledged" is presumed to be "acted on"): PREMISE-108 makes the instrument CONTENT-APPEARING-IN-RECIPIENT-OUTPUT load-bearing and forbids acknowledgement as a health metric.
    - P-503 ("claims exceed evidence," answered with a coverage percentage that rises on marginal reads and reads green during the target failure): PREMISE-109 makes CLAIMS-WITHOUT-EVIDENCE load-bearing and excludes coverage.
    - P-505 ("detectors invert," answered with a discrepancy check provably blind to common-mode inversion, in a fleet whose monitors share runtime, scheduler and permissions with their subjects): PREMISE-110 folds the common-mode scope guard into the premise and replaces the reachability audit with a live proof-test.
  **Net effect: no defective instrument entered the validated-premises register this run.** That was the flag's purpose and it is discharged at the item level. What remains and requires Tom is the standing process change.

  Residual finding 15c adds: the flag applies to THIS PIPELINE'S OWN ARCHITECTURE and 15b did not extend it there. ASSUMPTION-477 announces that 15a/15b independence "became structural," when the enforced channel is the weakest of at least four correlation sources and the dominant one (shared pretraining and shared corpus) is untouched. That is a green signal over an unfixed condition, produced by the same pipeline that raised the flag, on the same day. It is dispositioned separately as REVISE-233.

  Recommended action (Tom / orchestrator):
    1. ADOPT THE ISOMORPHISM TEST as a standing step between surfacing and remedy, alongside REVISE-231's discriminating-test step: state the property the observation identified as defective, then ask whether the proposed instrument HAS THAT SAME PROPERTY. If it does, the remedy is worse than no remedy, because the current defect is at least visible.
    2. Note that in all seven cases the isomorphism-free alternative is CHEAPER than the remedy it replaces (a one-line clock comparison; counting claims without evidence; searching recipients' outputs; a sandbox proof-test; reporting a floor). This flag does not trade rigour against cost.
    3. SECONDARY PATTERN, recorded by 15b and endorsed here: SAME-DAY GENERALIZATION. Four items (A-479's 7-of-12, A-480, P-504's three breaches, P-505's four detectors) generalize from cases observed and counted on a single day by the pipeline that also produced them, with no external coding rule and no base rate. This is the posture challenged in PRESUMPTION-499 on 2026-07-19 and it has not narrowed. In every instance the base rate is obtainable cheaply from the existing record; none was obtained. 15c acted on this by excluding all four counts from what was incorporated (see PREMISE-107's "Not incorporated" clause and PREMISE-110's "Scope limit" clause) — but exclusion is not a fix, and the standing recommendation is that a count produced by the pipeline that authored the items be re-coded by a different agent against a written rule before it is quoted.
  Urgency: High
  Status: OPEN — awaiting Tom's review
  PROVENANCE:
    Origin: 15b (systemic; not a 14a/14b queue item)
    Chain: [15b -> 15c]
    Original item: n/a — cross-item systemic flag over the 2026-07-19 EOD batch
    Item type: SYSTEMIC-RISK-FLAG (High)
    Transform at each step:
      15b: Raised REMEDY-INHERITS-DEFECT across 7 of 14 items with literature basis
      15c: Evaluated and upheld; applied item-by-item to exclude every named instrument from incorporation; extended the flag to the pipeline's own independence claim (REVISE-233); residual process change routed to Tom
    Current status: REVISION-FLAGGED
    Disposition record: CROSS-ITEM FLAG EVALUATIONS (lit_search_returns.md, 2026-07-20)

REVISE-237:
  Date flagged: 2026-07-21
  Source item: ASSUMPTION-486
  Item type: ASSUMPTION (stated)
  15a: SUPPORTED (Strong) | 15b: **CHALLENGED (Moderate)**
  **This flag also places PREMISE-108 UNDER-REVIEW. It is a consistency conflict against the validated register, not only a disposition.**
  Net assessment: The sharpest cross-agent conflict in the batch, and it resolves by separating two propositions rather than averaging them. PROPOSITION 1 — a receipt is not acceptance — is strongly supported and uncontested. Clinical informatics encodes it as a measurement convention: an alert counts as overridden if the acknowledgement reason indicates no change, including "aware," and accepted only on a concrete order change; override rates run 49-96%, acknowledgement comprises 28% of responses, and acceptance falls to 1.4% where acknowledgement is not compelled (JMIR Medical Informatics 10(10):e40511, PMC9579928; Barenfanger et al. 2004, Joint Commission Journal on Quality and Safety 30(7)). Receipt-based counting would report near-total success against that. PROPOSITION 2 — therefore NEVER an acknowledgement receipt — is directly contradicted by the highest-stakes domain available. Read-back is the foundational mechanism of closed-loop communication (Joint Commission Journal on Quality and Safety, S1549-3741(04)30053-5), directed closed-loop communication is associated with increased task COMPLETION rather than merely receipt (PMC12597367), and I-PASS raised handoff adherence 41.6%->70.5% at MD Anderson (2019-2022) by making acknowledgement substantive rather than by abolishing it. 15b's operational objection is decisive and 15a did not have it: **output-scanning alone cannot distinguish "flag not received" from "flag received, weighed, and correctly declined," so the item's metric penalises judgement** and removes the fastest available failure detector — under it, a lost flag stays invisible until the recipient's next output cycle. 15a reached the adjacent defect from the supportive side, noting the item's own metric is closer to paraphrase than to acceptance and "inherits a weaker form of the defect it names."
  Reasoning for REVISE rather than MONITOR: this item is not a free-standing claim. Its provenance records it as the extraction of PREMISE-108's instrumentation constraint, incorporated one day earlier on 2026-07-20. A disconfirmatory search run against that clause in isolation returns CHALLENGED on evidence better matched to it than the evidence it was validated on. Per the 15c spec, a result contradicting an existing PREMISE is flagged for human review rather than silently resolved — and 15c will not amend its own premise one day after writing it on its own authority.
  What is at risk: PREMISE-108's instrumentation constraint ONLY. The premise's first half — transmission is not delivery; a flag "for" a named agent does not transfer responsibility; an unacknowledged flag leaves responsibility unheld while the record shows it discharged — is not challenged in either direction and is NOT under review. Also at risk: the instrumentation design for the cross-agent flag channel; MONITOR-455; any measure that would count a declined flag as a delivery failure.
  Recommended action (Tom):
    1. DECIDE whether PREMISE-108's instrumentation constraint is amended to the two-measure form or retained as written. 15c recommends amendment.
    2. THE TWO-MEASURE FORM, which both searchers independently arrive at: content read-back (not a bare receipt) as the DELIVERY check; flagged content appearing in the recipient's output as the EFFECTIVENESS check. These measure different things and neither substitutes for the other.
    3. ADD A THIRD STATE. The current scheme can represent "delivered" and "not delivered" and cannot represent "received, weighed, and declined with reason." That third state is not a failure and is currently indistinguishable from one.
    4. CHEAP CHECK AVAILABLE MEANWHILE, and it decides the question: enumerate 30 days of cross-agent flags and classify each into the three bins. The size of the third bin settles whether the exclusivity clause is costing anything. Under an hour.
    5. DO NOT abolish acknowledgement pending the decision. Per SYSTEMIC-RISK-FLAG-B (REVISE-241), the item's binary remedy has a documented failure mode worse than the problem it addresses.
  Urgency: Medium (the underlying premise's first half is intact; the contested clause governs instrumentation not yet built)
  Status: OPEN — awaiting Tom's review. PREMISE-108 marked UNDER-REVIEW pending it.
  **Standing note per the fail-loud convention:** a premise validated on Monday and challenged on Tuesday is evidence about this pipeline's validation threshold, not only about this premise. This is the second consecutive run in which a better-matched disconfirmatory search arrived one cycle after incorporation. Whether that is acceptable latency or a threshold set too low is a question for REVISE-239's effectiveness-check regime, not for this flag.
  Full results: lit_search_results/for/ASSUMPTION-486_for.md ; lit_search_results/against/ASSUMPTION-486_against.md
  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-486
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the PREMISE-108 instrumentation constraint
      15a: Searched for supporting literature; SUPPORTED (Strong) with a self-noted caveat that the item's metric inherits a weaker form of the defect it names
      15b: Searched for challenging literature; CHALLENGED (Moderate)
      15c: Net evaluation; cross-agent conflict resolved by separating two propositions, not averaged; consistency conflict with PREMISE-108 surfaced and routed to human review
    Current status: REVISION-FLAGGED
    Disposition record: DISPOSITION-ASSUMPTION-486 (lit_search_returns.md, 2026-07-21)

REVISE-238:
  Date flagged: 2026-07-21
  Source item: ASSUMPTION-487
  Item type: ASSUMPTION (stated)
  15a: PARTIALLY-SUPPORTED (Moderate on fault class and stopped writer; **Weak** on the point-in-time-backup argument) | 15b: **CHALLENGED (Strong)**
  **The only item in this batch whose recommended action has an irreversible failure mode. Urgency HIGH is on the REMEDY, not the diagnosis.**
  Net assessment: Weak support plus strong challenge on the item's load-bearing inference, reached independently from both search directions. The item argues that errors observed IN a point-in-time backup rule OUT a mid-write artifact. SQLite's own corruption documentation ("How To Corrupt An SQLite Database File," sqlite.org/howtocorrupt.html) lists copying or backing up a database WHILE IT IS BEING WRITTEN as a canonical cause of "database disk image is malformed" — which makes the observation evidence FOR the artifact hypothesis, not against it. 15a reached the same conclusion from the supportive side: the exclusion holds only if the copy went through the backup API or VACUUM INTO with proper locking, and an ordinary filesystem copy of a live database is a known source of spurious malformed-image errors. 15b adds that the two halves of the claim are mutually dependent — a stopped writer would not produce mid-write artifacts — so the item cannot be half-right in the way it is written. What IS supported: reading SQLITE_CORRUPT as B-tree corruption is the documented interpretation, and 14.6 days stale with 13 consecutive failures is the canonical freshness signature of a halted producer. The diagnosis is plausible; the argument offered FOR it is inverted.
  What is at risk: open-story.db integrity and every count derived from it. Specifically: (i) running VACUUM or VACUUM INTO on an already-corrupt file will either fail with another SQLITE_CORRUPT **or silently drop the unreadable data** — both searchers retrieved this independently — converting detected corruption into undetected data LOSS; (ii) `.recover` can resurrect previously deleted rows as live data with no marker, converting it into undetected data ADDITION; (iii) in a vault already carrying six unresolved counting disputes, either outcome would be indistinguishable from the disputes already open. Secondarily: if the "writer has stopped" half is wrong (writer running and failing at commit), the real fault survives a completed repair.
  Recommended action (Tom):
    1. **RUN `PRAGMA integrity_check` ON THE LIVE DATABASE, Mac-side, BEFORE ANY RECOVERY ACTION.** Minutes of work. It discriminates cleanly between a corrupt live file and a bad backup copy, and nothing downstream should proceed without it.
    2. ESTABLISH HOW THE POINT-IN-TIME BACKUP WAS TAKEN — backup API, VACUUM INTO, or filesystem copy — before treating the backup's errors as evidence about the live file. If it was a filesystem copy of a live database, the errors are expected and say nothing about the live file's state.
    3. **DO NOT RUN VACUUM OR VACUUM INTO on the corrupt copy.** This is the specific action the item proposes and the specific action both searchers warn against.
    4. IF RECOVERY IS GENUINELY NEEDED, use `.recover` (SQLite CLI 3.29.0+) with row-count reconciliation against a known-good prior snapshot, and MARK any resurrected rows so they cannot silently enter the counting disputes.
    5. SEPARATELY CONFIRM whether the writer process is stopped or running-and-failing. The freshness signature is consistent with both and the fixes differ.
  Urgency: **HIGH**
  Status: OPEN — awaiting Tom's review
  Note on 15c's own limits: this is a measurement 15c could have taken and did not, because its spec does not authorise it to execute against the vault's databases. Recorded rather than excused; it is the substance of REVISE-239.
  Full results: lit_search_results/for/ASSUMPTION-487_for.md ; lit_search_results/against/ASSUMPTION-487_against.md
  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-487
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 metabolism regen daily transcript
      15a: Searched for supporting literature; PARTIALLY-SUPPORTED, with an unprompted warning on the proposed remedy
      15b: Searched for challenging literature; CHALLENGED (Strong) — the load-bearing inference runs backwards
      15c: Net evaluation and disposition; remedy hazard escalated above the diagnosis; resolved in 15b's favour on source directness (SQLite's own documentation is primary and reverses the item's inference)
    Current status: REVISION-FLAGGED
    Disposition record: DISPOSITION-ASSUMPTION-487 (lit_search_returns.md, 2026-07-21)

REVISE-239:
  Date flagged: 2026-07-21
  Source: SYSTEMIC-RISK-FLAG-C (Agent 15b, 2026-07-21) — evaluated by 15c, UPHELD and extended
  Item type: CROSS-ITEM SYSTEMIC
  Affected items as filed by 15b: ASSUMPTION-482, ASSUMPTION-490, PRESUMPTION-506, PRESUMPTION-512, PRESUMPTION-513
  **15c extends the affected set to every disposition this agent has ever issued, including all 18 in this run.**
  Common vulnerability: Findings are generated and closed without an effectiveness check, and success bars are implicit rather than pre-registered. 482 and 513 dispute which constraint binds with no pre-registered threshold, so the fifteen-day record can be read either way after the fact. 490 asks which reading is authoritative with no written definition. 506 infers total propagation failure with no prior for what success looks like. 512 asks for an hours total with no target. The CAPA literature identifies exactly this pattern — investigation completed, effectiveness criterion never defined, failure recurs, record documents the cycle — as the most common way correction programmes fail, and it is visible in ASSUMPTION-488's same-day recurrence.
  15c's extension, recorded per the fail-loud convention: **no disposition record in lit_search_returns.md, in any run, carries a field stating what evidence would show the item changed behaviour, by when, or who checks.** MONITOR entries carry "what would change the disposition," which is a re-evaluation trigger, not an effectiveness check — it asks what would change 15c's mind, not what would show the system changed. REVISE entries carry recommended actions with no verification step. PREMISE entries carry a re-check date with no criterion. The gap is architectural and it is this agent's, not only the items'.
  Literature basis: CAPA practice literature (Deltek, "The CAPA Process"; The FDA Group, "Definitive Guide to CAPA"; SimplerQMS) — effectiveness criteria must be defined at the start and met before closure, and most CAPA failures occur at follow-up rather than investigation. Ivers et al., Cochrane CD000259.pub3 (PMID 22696318) and CD000259.pub4 — the realistic effect size of feedback is 4-6% absolute, which is the prior any propagation mechanism should be judged against. ISO/IEC 17025 clauses 7.10/8.7 — verify the fix worked.
  Risk level: **Critical**
  What is at risk: 110 prior premises (121 after this run), 236 revision flags (241 after this run) and 457 monitors (462 after this run), none of which carries a criterion by which its effect could be established or denied. If PREMISE-116 is right, this is the mechanism. It is also the reason the 482/513 dispute cannot be settled by argument.
  Recommended action (Tom):
    1. **ADD A MANDATORY FIELD** to every validated premise, disposition and revision flag: *what evidence would show this changed behaviour, by when, and who checks.* No item closes until that evidence exists. 15b names this the highest-leverage recommendation in the batch and 15c concurs.
    2. **PRE-REGISTER SUCCESS THRESHOLDS BEFORE running any of the measurements this batch proposes**, so results are interpretable rather than arguable after the fact. Three of the five new MONITOR items (458, 461, 462) are blocked on this and will produce unusable results without it.
    3. Note the single change addresses three separate findings at once: the mechanism behind ASSUMPTION-488's recurrence, PREMISE-116's propagation gap, and the 482/513 dispute.
    4. **This change requires an authority 15c does not have.** 15c is not authorised to add a mandatory field to the registries and has not done so. It is routed, not implemented — which is itself an instance of what PREMISE-116 describes.
  Urgency: High
  Status: OPEN — awaiting Tom's review
  PROVENANCE:
    Origin: 15b (SYSTEMIC-RISK-FLAG-C)
    Chain: [14a, 14b -> 15b -> 15c]
    Transform at each step:
      15b: Cross-item pattern identified across five items in the 2026-07-20 batch; Critical
      15c: Evaluated and upheld; extended from five items to the full disposition record of this agent, with the specific structural gap named; routed to Tom, not implemented
    Current status: REVISION-FLAGGED
    Disposition record: CROSS-ITEM FLAG EVALUATIONS (lit_search_returns.md, 2026-07-21)

REVISE-240:
  Date flagged: 2026-07-21
  Source: SYSTEMIC-RISK-FLAG-A (Agent 15b, 2026-07-21) — evaluated by 15c, UPHELD, with a new in-run measurement added
  Item type: CROSS-ITEM SYSTEMIC
  Affected items: ASSUMPTION-483, ASSUMPTION-491, PRESUMPTION-508, PRESUMPTION-511 (and, per 15c's extension, every disposition citing cross-agent convergence)
  Common vulnerability: Independence is asserted from the EXISTENCE of two artifacts rather than engineered and measured. Four items in one batch turn on whether a second check is genuinely independent of the first — 483 on 15a/15b, 491 on "independently confirmed," 508 on judging with a self-flagged correlated judge, 511 on reproduction as confirmation — and no house measurement of correlation exists. 15b notes the batch is internally inconsistent: ASSUMPTION-491 asserts independent confirmation on the same day PRESUMPTION-511 argues the concept does not apply to same-code re-runs.
  **15c's addition — the first in-run measurement of the defect, which 15b could not see because it was blinded:** 15a and 15b were run as separate agents under full blocking, neither able to read the other's output, and they nonetheless retrieved THE SAME KEY SOURCES on at least five items — arXiv:2605.29800 and van Rooyen PMID 9676666 (A-483), the metrology/no-gold-standard literature (A-490 and P-507), Cochrane CD000259 (P-506), NASEM 2019 doi:10.17226/25303 (P-511), and the Danziger/ego-depletion caution (P-512). Two agents assigned OPPOSITE search directions converging on the same citations is a direct observation of the correlation channel ASSUMPTION-483 is about, and it means the apparent agreement between the two directions on those five items is worth materially less than two independent confirmations. Every disposition in this run that leans on "both agents converged" should be read with that discount. **This datum was produced as a by-product; it does not substitute for the measurement recommended below.**
  Literature basis: NASEM (2019), "Reproducibility and Replicability in Science," doi:10.17226/25303. "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels," arXiv:2605.29800 — ~75% of nominal independence lost, 8-22pp accuracy shortfall. "How Independent are Large Language Models?", arXiv:2604.07650. "A Systematic Methodology for Evaluating Failure Independence in LLM-Generated Code," arXiv:2607.02808 — structural variation does not buy failure independence. ISO/IEC 17025 7.10/8.7 (via PREMISE-118).
  Risk level: High
  What is at risk: Every disposition produced by 15a/15b/15c, including the 14 from 2026-07-20 and the 18 from this run, and the 121 standing premises. Per PREMISE-118, incorporated in this run, naming this defect obliges a RETROSPECTIVE IMPACT ASSESSMENT over results already produced. **That assessment has not been performed. The defect was named on 2026-07-20 in REVISE-233; 18 further dispositions were produced on 2026-07-21 without it. The premise validated in this run is violated by this run, and it is recorded here rather than elided.**
  Recommended action (Tom):
    1. **ESTABLISH ONE HOUSE NUMBER.** Measure 15a/15b source-citation overlap under full blocking. The five-item overlap above is the starting datum; a proper measurement over a run gives the discount to apply.
    2. **RECORD THE FOUR SHARED COMPONENTS** for every claimed second check: code path, corpus, model, execution context. Treat checks sharing all four as a single channel regardless of label.
    3. **ADOPT NASEM VOCABULARY VAULT-WIDE** and forbid "independently confirmed" unless the second check obtained its own data by a different path. This is now PREMISE-120 and is stated; what is routed here is enforcement.
    4. **PERFORM THE RETROSPECTIVE IMPACT ASSESSMENT** that PREMISE-118 requires over the 2026-07-20 and 2026-07-21 disposition sets. Per PREMISE-118 the correct response is to PRICE the defect (the measured 8-22pp shortfall gives a bound), not to disown the output and not to proceed silently.
    5. DECIDE whether 15c should continue dispositioning while the assessment is outstanding. 15c has no authority to suspend itself and did not.
  Urgency: High
  Status: OPEN — awaiting Tom's review. Second consecutive run in which this condition is documented and unremedied (see REVISE-233, 2026-07-20).
  PROVENANCE:
    Origin: 15b (SYSTEMIC-RISK-FLAG-A)
    Chain: [14a, 14b -> 15b -> 15c]
    Transform at each step:
      15b: Cross-item pattern identified across four items; High
      15c: Evaluated and upheld; a fifth instance added from within this run (cross-direction source overlap under full blocking); PREMISE-118's retrospective-assessment obligation applied to this agent and recorded as unmet
    Current status: REVISION-FLAGGED
    Disposition record: CROSS-ITEM FLAG EVALUATIONS (lit_search_returns.md, 2026-07-21)

REVISE-241:
  Date flagged: 2026-07-21
  Source: SYSTEMIC-RISK-FLAG-B (Agent 15b, 2026-07-21) — evaluated by 15c, UPHELD and applied item-by-item within this run
  Item type: CROSS-ITEM SYSTEMIC
  Affected items: ASSUMPTION-486, ASSUMPTION-489, PRESUMPTION-507, PRESUMPTION-510
  Common vulnerability: Sound observation, over-corrective remedy. Each of the four pairs a defensible finding with a proposed control whose own documented failure mode is worse than the problem — abolishing acknowledgement (removes the fastest failure detector and cannot distinguish non-receipt from informed rejection), tightening a detector with no oracle (converts false positives into silent false negatives), quarantining disputed figures (stops work in a channel that cannot clear the stop), a flat admission cap (binds immediately against 67 carried items, gets raised, leaves arrival-minus-service untouched). In every case the literature's actual remedy is graded rather than binary.
  Action already taken by 15c within this run — recorded so the flag is not double-counted as outstanding work: the graded substitution was applied to all four items at disposition. ASSUMPTION-486 -> REVISE-237, recommending content read-back as delivery check plus output appearance as effectiveness check plus a third "received and declined" state, with the abolition explicitly not recommended. ASSUMPTION-489 -> PREMISE-113, which makes a labelled corpus with precision AND recall load-bearing and excludes the local verdict. PRESUMPTION-507 -> PREMISE-117, whose statement is "the defect is silence, not continuation," with quarantine excluded and mark-and-revise substituted. PRESUMPTION-510 -> PREMISE-119, which excludes the flat cap and substitutes the requirement to establish service rate > 0 before designing any admission policy.
  Literature basis: Joint Commission Journal on Quality and Safety S1549-3741(04)30053-5 and PMC12597367 (read-back increases task completion). Snyk, "Minimizing False Positives," and OX Security (threshold loosening suppresses detection). UK ONS Revisions and Correction of Errors Policy (mark and revise, not withdraw). arXiv:2603.13870 and arXiv:2601.22295 (value-based screening and dynamic shadow price over fixed caps); practitioner evidence that fixed WIP limits are raised on first bind.
  Risk level: High
  What remains outstanding and requires Tom: the STANDING RULE, which 15c cannot install. 15b proposes: before adopting any proposed control, search for its documented failure mode and state it; prefer graded controls (discount, flag, value-based triage, read-back with content) to binary ones (abolish, quarantine, cap); require every proposed detector or process change to come with a positive control demonstrating it still fires when it should.
  15c's note on placement: this rule is the same shape as PREMISE-107's discriminating-test requirement applied to REMEDIES rather than to DIAGNOSES. PREMISE-107 already holds that a remedy attached to an observation without being validated against the actual mechanism costs effort AND leaves the fault in place. **Recommend merging this rule into PREMISE-107 as a second clause rather than filing it as a separate premise** — a separate premise would be a duplicate of an existing one, which is the volume-over-value pattern MONITOR-461 exists to watch. 15c does not amend PREMISE-107 on its own authority.
  Urgency: High
  Status: OPEN — awaiting Tom's review (standing rule and PREMISE-107 merge only; item-level application already complete)
  PROVENANCE:
    Origin: 15b (SYSTEMIC-RISK-FLAG-B)
    Chain: [14a, 14b -> 15b -> 15c]
    Transform at each step:
      15b: Cross-item pattern identified across four items; High
      15c: Evaluated and upheld; applied item-by-item at disposition with each binary control excluded and its failure mode stated; residual standing rule routed to Tom with a recommended merge into PREMISE-107 rather than a new premise
    Current status: REVISION-FLAGGED (residual process change only)
    Disposition record: CROSS-ITEM FLAG EVALUATIONS (lit_search_returns.md, 2026-07-21)

**Intake summary (2026-07-21):** 5 flags added (REVISE-237..241) from the 2026-07-20 EOD batch of 18 — two item-level (237, 238) and three cross-item systemic (239 Critical, 240 High, 241 High), all three of 15b's SYSTEMIC-RISK flags having been evaluated and upheld rather than passed through. REVISE-238 is the only item in the batch whose recommended action carries an irreversible failure mode and is the one to read first: run `PRAGMA integrity_check` on the live open-story.db before any recovery action. REVISE-237 places PREMISE-108 UNDER-REVIEW, the first consistency conflict against the validated register since PREMISE-101/PRESUMPTION-501 on 2026-07-20. **Standing caution per PREMISE-121, validated in this run:** these five enter a channel with demonstrated near-zero throughput, and each additional correctly-argued item can lower the probability that any item is acted on. If only one is read, read REVISE-238. If a second, REVISE-239 — it is the change that would make the other four checkable.

REVISE-242:
  Date flagged: 2026-07-21
  Source: Agent 15c register-integrity check, performed as part of the 2026-07-21 verification pass
  Item type: REGISTER INTEGRITY — not a literature disposition
  **Finding: 40 validated premises are referenced across the vault but are ABSENT from validated_premises.md.**
  Detail: validated_premises.md currently contains 78 entries running PREMISE-044 to PREMISE-121, plus a single stray PREMISE-006. PREMISE-001 through PREMISE-043 are not in the register. They ARE referenced — 40 distinct IDs in that range appear across lit_search_returns.md, monitor_queue.md, revision_flags.md and for_lit_search.md. The earliest surviving backup (validated_premises.md.bak.20260525-pre-15pipeline) contains ONE entry, so the loss predates 2026-05-25 and is not attributable to this run or to any recent one.
  Why this matters beyond bookkeeping:
    1. **15d is scheduled to re-check premises that do not exist.** The 2026-07-05 15d section of for_lit_search.md records a monthly INCORPORATED re-check covering PREMISE-002, PREMISE-004 (due 2026-07-05) and PREMISE-025 (overdue from 2026-06-18). None of the three is in the register. Either those re-checks were performed against something other than the register, or they were recorded as performed and were not.
    2. **Consistency checking before INCORPORATE has been running against a partial register** — including in this run. 15c is required to check each new premise against existing validated premises for contradictions. It has been checking against 78 of 118, and could not have detected a conflict with any of the 40.
    3. This is an instance of PREMISE-109 (a view over a read set is not a view over the system) holding for the register itself, and of PREMISE-120 (reproduction is not confirmation) — every consistency check since the loss reproduced the same blind spot exactly.
  What is at risk: the completeness of every consistency check performed since before 2026-05-25; 15d's monthly INCORPORATED re-check cycle; any claim about the total number of validated premises, including the counts this pipeline reports about itself.
  Recommended action (Tom):
    1. Determine whether PREMISE-001..043 were lost, archived elsewhere, or never written to this file. The disposition records in lit_search_returns.md should permit reconstruction of their statements, since each INCORPORATE disposition contains the premise text.
    2. Until resolved, treat "78 validated premises" and "121 premises" as different numbers meaning different things, and do not report either as a count of the system's validated self-knowledge.
    3. Re-run 15c's consistency check for the 11 premises incorporated on 2026-07-21 once the register is complete.
  Urgency: Medium (no active decision is known to depend on the missing entries; but the defect is silent, long-standing, and invalidates a check the pipeline reports as performed)
  Status: OPEN — awaiting Tom's review
  15c note on its own conduct: this was found by a verification step, not by the disposition process, and it had been undetected across every prior run of this agent. Recorded per the fail-loud convention rather than corrected silently — 15c did not reconstruct the missing entries, which would have meant inventing register content from disposition text without review.
  PROVENANCE:
    Origin: 15c (register integrity check)
    Chain: [15c]
    Transform at each step:
      15c: Cross-referenced PREMISE IDs cited across four registry files against the entries present in validated_premises.md; 40 orphan references found; backups checked to date the loss
    Current status: REVISION-FLAGGED
    Disposition record: RUN SUMMARY — Agent 15c, 2026-07-21 (lit_search_returns.md)

---
## Intake 2026-07-22 (Agent 15c — c2a2-lit-search-pipeline; from 2026-07-21 EOD batch)

REVISE-243:
  Date: 2026-07-22
  Source item: ASSUMPTION-495 (FLAG-018: over-alignment is a pathology; a Rung-2 metric scoring convergence-as-progress is miscalibrated)
  Item type: ASSUMPTION (stated)
  15a: SUPPORTED (Strong for the failure mode) — "Diversity Collapse in Multi-Agent LLM Systems" (arXiv:2604.18005): diversity collapse is driven by alignment priors alone, on C2A2's own substrate; over-optimization collapses collective fitness (Levin; Hong-Page).
  15b: PARTIALLY-CHALLENGED (Moderate) — convergence per se is not pathological; the failure mode is *imposed/premature* convergence. There is an optimum, not a monotone. A metric rewarding pure divergence would be as miscalibrated as one rewarding pure convergence.
  What is at risk: The Rung-2 progress metric. If it scores convergence/agreement as progress, it rewards a documented pathology; if over-corrected to reward divergence-as-such, it rewards incoherence.
  Recommended action (for Tom): Re-specify the Rung-2 metric to score the *process* — independent evidence exchange and coupling (mutual responsiveness) — rather than either endpoint. Concretely: re-analyze the +0.031 "listening lift" to separate coupling from convergence (in-house test), and define Rung-2 to track earned convergence (post-information-exchange) while penalizing diversity collapse.
  Urgency: Medium (design-shaping, not a live data-integrity failure).
  DEPENDENCY: PRESUMPTION-516 (same 07-21 batch, DEFERRED unsearched) asserts there is currently NO mechanism propagating a FLAG or premise into the metric it governs. If PRESUMPTION-516 is correct, this REVISE cannot be actioned until that propagation path exists. REVISE-243 should be read together with PRESUMPTION-516 when it is searched.
  PROVENANCE: Origin=14a; Chain=[14a->15a,15b->15c]; Item type=ASSUMPTION (stated); Current status=REVISION-FLAGGED
  Disposition record: DISPOSITION-504 (lit_search_returns.md, 2026-07-22)

REVISE-244:
  Date: 2026-07-22
  Source item: PRESUMPTION-522 (documentation-as-compliance: PREMISE-118 named but its owed retrospective assessment left unperformed, second day running)
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight)
  15a: SUPPORTED (Strong) — disclosure and remediation are distinct obligations across ICFR (Deloitte 2024) and patient-safety (APSF; AHRQ/NCBI) literatures; a mature program tracks corrective actions to verified closure. Documenting a defect does not discharge the duty to fix it.
  15b: NO-CHALLENGE-FOUND (Weak boundary note) — disclosure-FIRST is correct (protects reporting) and low-risk deferral is legitimate; so the finding is "every named defect owes a tracked, risk-prioritized disposition to closure," NOT "remediate everything instantly." The PREMISE-118 case is not exculpated: the owed retrospective assessment IS the tracked disposition, and it is absent.
  What is at risk: The integrity of the whole self-awareness pipeline. If naming a defect is treated as discharging the obligation, the falsifiability contract is decorative and the defect backlog grows silently. This is a PRESUMPTION with strong support and a live, repeat violation -> HIGH urgency per the 15c spec heuristic.
  Recommended action (for Tom): Institute a defect-closure ledger. Every named defect (FLAG / REVISE / self-caught error) gets an owner, a risk rank, and a closure state; disclosure stays immediate, remediation is tracked to done. First test: check whether ANY named defect has ever received its owed retrospective assessment (a zero rate confirms the presumption).
  Urgency: HIGH.
  PROVENANCE: Origin=14b; Chain=[14b->15a,15b->15c]; Item type=PRESUMPTION (unstated); Current status=REVISION-FLAGGED
  Disposition record: DISPOSITION-508 (lit_search_returns.md, 2026-07-22)

---
## Intake 2026-07-24 (Agent 15c — c2a2-lit-search-pipeline; from 2026-07-23 day-#18 batch)

REVISE-245:
  Date: 2026-07-24
  Source item: PRESUMPTION-534 (documenting the missing propagation edge into the same non-propagating self-knowledge layer is presumed to be progress on closing it)
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight)
  15a: SUPPORTED (Strong) — "Measurement without management" (Brehaut et al., BMC HSR 2019): audit/feedback that stops at measurement, with no response/action stage, produces an incomplete feedback loop and no improvement; Ivers 2012 (Cochrane) — A&F moves practice only when coupled to explicit action/targets. Filing a finding into the (per PREMISE-123) non-propagating layer is a textbook instance, and self-instancing (the filing IS the anti-pattern).
  15b: PARTIALLY-CHALLENGED (Moderate) — documentation is a valid, often necessary step-1 with deferred value; it becomes the named anti-pattern only if actuation never follows. STEELMAN: an only-ever-documenting layer is a placebo that discharges the felt obligation to act — worse than not knowing.
  What is at risk: The actuation of the entire self-awareness pipeline. Today's run alone added 6 MONITOR entries and 2 REVISE flags into a layer that (per PREMISE-123) has no wired path to the agents they bear on. Without a propagation edge, all of it is inert.
  Recommended action (for Tom): Wire ONE propagation mechanism — a concrete edge from a validated finding/REVISE to an agent-spec edit, with an owner and an SLA (extends the REVISE-244 defect-closure ledger to cover findings, not just defects). This single change relieves the 2026-07-24 SYSTEMIC-RISK flag (513/534/538/539) simultaneously. Adding more findings does not.
  Urgency: HIGH.
  SYSTEMIC-RISK: This is the general remedy the 2026-07-24 15b SYSTEMIC-RISK-FLAG recommends (common vulnerability = STALLED ACTUATION across ASSUMPTION-513, PRESUMPTION-534/538/539).
  PROVENANCE: Origin=14b; Chain=[14b->15a,15b->15c]; Item type=PRESUMPTION (unstated); Current status=REVISION-FLAGGED
  Disposition record: DISPOSITION-520 (lit_search_returns.md, 2026-07-24)

REVISE-246:
  Date: 2026-07-24
  Source item: PRESUMPTION-536 (PREMISE-124 — "require an external referent" — was validated from inside the pipeline with no external referent; presumed exempt from its own standard)
  Item type: PRESUMPTION (unstated — surfaced by inference; reflexive on a validated premise)
  15a: SUPPORTED (Strong) — Tarski (undefinability), Goedel (2nd incompleteness), quis-custodiet self-regulation literature, and multi-agent self-correction findings all converge: a self-audit inherits the blind spot it is meant to catch unless an independent check terminates the regress. A referent-requiring rule minted without a referent is self-exempting.
  15b: PARTIALLY-CHALLENGED (Moderate) — PREMISE-124 may be a coherence-warranted NORM rather than an empirical claim, so Tarski/Goedel are not strictly on point and a norm need not cite an external referent. BUT its "High" confidence label is an empirical-sounding calibration assigned with no referent, which does violate PREMISE-124 on its own terms.
  What is at risk: The soundness/credibility of PREMISE-124 (and, by precedent, any self-validated premise). If the rule is exempt from itself, its authority to demand calibration of everything else is undermined.
  Recommended action (for Tom): Apply PREMISE-124 to itself. Either (a) name the external referent-of-record that calibrated it, or (b) reclassify it explicitly as a methodological NORM and STRIP/qualify its "High" confidence label to UNCALIBRATED. Do NOT silently edit PREMISE-124 — human sign-off required (15c rule: REVISE items touching validated premises require Tom's response before status changes).
  Urgency: HIGH (reflexive integrity; cheap to fix).
  PROVENANCE: Origin=14b; Chain=[14b->15a,15b->15c]; Item type=PRESUMPTION (unstated); Current status=REVISION-FLAGGED
  Disposition record: DISPOSITION-522 (lit_search_returns.md, 2026-07-24)

REVISE-247:
  Date: 2026-07-28
  Source item: PRESUMPTION-560 (adjunct — the presumption itself was INCORPORATED as PREMISE-133; this flag is the concrete unmet need PREMISE-133 exposes)
  Item type: PRESUMPTION (unstated — surfaced by inference; reflexive on 15c's own disposition practice)
  15a: SUPPORTED (Strong) — abstention is an action inside the decision problem with its own cost (Chow 1970; reject-option / risk-coverage literature), suspension of judgement is committal rather than null (Friedman 2017, Nous 51(2)), and where the only available adjudicator is disqualified the prescribed response is recusal-WITH-TRANSFER or escalation to a named external arbiter (nemo iudex in causa sua; Raji et al. 2022) — never recusal into silence.
  15b: PARTIALLY-CHALLENGED (Moderate) — abstention IS asymmetric and is not merely disguised assertion (El-Yaniv & Wiener 2010), and unadoptability may follow from self-reference itself rather than from 15c's choice. BUT 15b reaches the SAME operational conclusion: "suspension is only defensible if it keeps the question OPEN with a specified escalation route, and if no such route exists the abstention silently becomes a permanent verdict of non-adoption."
  What is at risk: MONITOR-486 / PRESUMPTION-556 — the single HIGH-risk item concerning the pipeline's own reliability — has no written rule whose satisfaction would move it out of MONITOR, no named adjudicator, and no deadline. By construction it is therefore permanently non-adopted while appearing to be under active monitoring. The same structure applies to the fired-trigger cohort (MONITOR-420/423, unactioned since 2026-07-19) and to the ~174-item 15d re-trigger backlog with zero consumption since 2026-07-08: in each case suspension has become non-adoption by default. 15c cannot fix this from inside — naming an adjudicator is a human act.
  Recommended action (for Tom): Write the discharge rule for MONITOR-486 explicitly, as three fields: (a) ADJUDICATOR — yourself, or a differently-trained model with no access to this corpus; (b) TRIGGER — what specific check, performed by that adjudicator, discharges it (a spot-check of N INCORPORATED premises against their cited external referents is the obvious candidate, and PREMISE-132 now supplies the standard it must meet); (c) DEADLINE — a date after which continued suspension is reported in the daily run as an unresolved HIGH-risk exposure rather than as a monitored item. Adopt the same three fields as a standing requirement for any MONITOR issued on self-referential grounds. Consider also reporting an ABSTENTION COVERAGE figure — what fraction of HIGH-risk items the pipeline declined to dispose — so that abstention carries a visible cost.
  Urgency: HIGH (this run INCORPORATED PREMISE-133, which binds 15c to exactly this requirement; the pipeline is now formally out of compliance with its own newest premise until the rule is written. Fail-loud: stated rather than deferred.)
  PROVENANCE: Origin=14b; Chain=[14b->15a,15b->15c]; Item type=PRESUMPTION (unstated); Current status=REVISION-FLAGGED
  Disposition record: DISPOSITION-543 (lit_search_returns.md, 2026-07-28)

REVISE-248:
  Date: 2026-07-28
  Source item: PRESUMPTION-561 — ROUTED BACK TO 14b as a correction (the presumption's own technical premise is false)
  Item type: PRESUMPTION (unstated — surfaced by inference); this flag reports that the presumption's own technical premise is FALSE
  15a: PARTIALLY-SUPPORTED (Moderate-Strong) — supported only in CONDITIONAL form (the register's semantics is a separately-specifiable design fact; ISO 31000:2018 risk registers are a named external instance where items legitimately remain open). 15a's own caveat (b) cuts against the presumption: ISO 31000 practice treats an item with no recent REVIEW date as a red flag, so the log/watch-list reading substitutes a review-cadence obligation for a drain obligation — it does not license zero drain. Caveat (c) concedes Little's Law is robust and needs only a steady state.
  15b: CHALLENGED (Strong) — Little & Graves (2008), "Little's Law," in Chhajed & Lowe (eds.), Building Intuition (Springer), state that a service process is NOWHERE required by the law; it needs only a system boundary, arrivals and departures. With arrivals positive and departures zero the system is non-stable and residence time diverges, so calling the register unstable is a CORRECT application, not a category error. The log/watch-list reclassification also fails to deliver the exemption: alarm-management standards (EEMUA 191, IEC 62682) impose explicit per-operator throughput limits on monitoring registers precisely because reader attention is the service capacity, and append-only logs require retention or compaction because unbounded growth is a defect there too.
  What is at risk: If this presumption were adopted, C2A2 would retire a valid stability metric on a false technical premise and swap a drain obligation for a retention policy — letting the register grow while formally compliant. It would also implicitly undermine DISPOSITION-536 / PRESUMPTION-553, whose queueing-theory finding is CORRECT and STANDS. Note the direction of the correction: this does not relieve the backlog concern, it CONFIRMS it. The ~174-item register with zero consumption since 2026-07-08 is already inside the EEMUA-style overload regime for a single reader.
  Recommended action (for Tom): (1) Route the correction back to 14b — the inference rested on a false belief about what Little's Law requires, which is a checkable factual error worth recording so the pattern is not repeated. (2) Adopt the presumption's SURVIVING constructive half, which both directions endorse and which is not either/or: specify BOTH a named consumer and a terminal state for monitor-register items, AND a size/rate limit plus review cadence scored against reader capacity rather than against zero. Report L (register size) and W (median item age since last review) explicitly — both are computable today and their divergence is the alarm. (3) If genuinely no consumer is intended, apply log semantics honestly: add retention/compaction AND stop routing action-bearing items there.
  Urgency: Medium (no design change was made on this presumption, so nothing is currently broken by it; but it bears directly on the standing backlog decision already awaiting you)
  PROVENANCE: Origin=14b; Chain=[14b->15a,15b->15c]; Item type=PRESUMPTION (unstated); Current status=REVISION-FLAGGED (presumption refuted; constructive half retained)
  Disposition record: DISPOSITION-544 (lit_search_returns.md, 2026-07-28)

REVISE-249:
  Date: 2026-07-28
  Source item: 15b SYSTEMIC-RISK-FLAG 2026-07-28 (affected items PRESUMPTION-557, 558, 559, 560, 562, 563, 565 — the whole cohort bar 561)
  Item type: SYSTEMIC RISK (cross-item structural vulnerability), risk level High
  15b finding: Every presumption in this cohort is built the same way — each identifies a place where the pipeline accepted a graded, internal or self-reported standard, and demands an EXTERNALIST GOLD STANDARD in its place (formal proof of a defect class; an engineering interlock; a decorrelated external checker; an external arbiter for self-reference; demonstrated structural homology; a pre-specified construct; a full independent reconciliation). Every one of those demanded standards routes to the SAME scarce resource: an external decorrelated verifier — in practice a human, reachable only over the sync channel that has now failed five consecutive times (ASSUMPTION-559 / OPEN-135). The cohort therefore shares a single point of dependence, and it is currently unavailable. Today's literature shows the demanded standard is in several cases STRICTER THAN ACCEPTED PRACTICE: internal consistency checks do detect hallucinated references without external resources (Agrawal et al. 2024, Findings of EACL); internal assurance is graded rather than void (IIA Three Lines Model 2020); constructs are legitimately refined THROUGH measurement (Chang 2004, Inventing Temperature; Cronbach & Meehl 1955); and Little's Law does not require a service process (Little & Graves 2008). Applied uniformly and literally, the cohort converts seven tractable verification tasks into seven permanently blocked ones — reproducing the exact arrivals>0 / service=0 pathology that PRESUMPTION-553 and DISPOSITION-536 formalise.
  What is at risk: The pipeline's ability to discharge ANY of its own verification obligations while the human channel is dark. More specifically, this flag is in direct TENSION WITH TWO VALIDATED PREMISES, and 15c is required to surface rather than silently reconcile that: (a) PREMISE-124 requires an external baseline or an UNCALIBRATED tag — a BINARY standard; (b) PREMISE-114 holds that authority is a property of a documented chain to an external reference. If the assurance-grade reading is correct, both are stricter than the evidence supports and should become GRADED rather than binary. Both premises are hereby flagged alongside this item for human review; neither has been edited.
  Recommended action (for Tom): Adopt an explicit ASSURANCE-GRADE vocabulary with three levels — (1) SELF-REPORTED, (2) INTERNALLY CROSS-CHECKED BY A DECORRELATED AGENT, (3) EXTERNALLY VERIFIED — and require every remedy in the register to name the LOWEST grade that materially reduces its risk, rather than defaulting to grade 3. On today's evidence most of this cohort is satisfiable at grade 2 IN-HOUSE TODAY (PREMISE-132 already encodes this for citation checking). Reserve the grade-3 external-arbiter route for the genuinely self-referential item (MONITOR-486, via REVISE-247), and attach an aging clock to it so a blocked external dependency is reported as an EXPOSURE rather than absorbed silently as a queue. Then reconcile PREMISE-124 and PREMISE-114 to the graded vocabulary explicitly, with sign-off — do not let the graded reading take effect by drift.
  Urgency: HIGH (it unblocks seven items in this cohort AND supplies the constructive route for standing REVISE-246, which has been open since 2026-07-24 asking exactly "name the referent")
  PROVENANCE: Origin=15b (systemic-risk flag over a 14b-origin cohort); Chain=[14b->15b->15c]; Item type=SYSTEMIC RISK; Current status=REVISION-FLAGGED
  Disposition record: DISPOSITION-548 (lit_search_returns.md, 2026-07-28)

---
## Intake 2026-07-29 (Agent 15c — c2a2-lit-search-pipeline; from 2026-07-29 batch, PRESUMPTION-566..570, 572, 573, 575)

REVISE-250:
  Date: 2026-07-29
  Source item: PRESUMPTION-569 — ROUTED BACK TO 14b as a correction (the framing the presumption SHARES with the text it targets is a statistical error), constructive half retained
  Item type: PRESUMPTION (unstated — surfaced by inference); this flag reports that the presumption and its target made the SAME error in opposite directions
  15a: SUPPORTED (Moderate to Strong) — signal detection theory gives the presumption its sharpest form: a rise in the "yes" rate is jointly consistent with improved sensitivity and with a relaxed criterion, and the two are separated ONLY by the false-alarm rate, so an adoption count alone cannot show a bar works (Macmillan & Creelman 2005). Campbell's Law (Campbell 1979, Evaluation and Program Planning 2(1)) and Strathern's Goodhart formulation (1997, European Review 5(3)) establish that once a criterion's satisfaction is reported back as evidence of its own success the observed rate is contaminated by design rather than by misconduct. Moore, Tetlock, Tanlu & Bazerman 2006 (AMR 31(1)) supply the sharpest point: unawareness is the EXPECTED condition of a party assessing a matter in which its own standing is at stake, so the pipeline's sincerity about its explanation is not evidence about the explanation. King & Bearman 2009 (Int J Epidemiol 38(5)) show the pattern empirically AND show the decomposition can be done. BUT 15a's caveat (c), volunteered against its own direction, is the load-bearing line: "n = 1 vs n = 5 is a very small sample; a fivefold ratio on these counts is not distinguishable from noise on any conventional test, which independently — and perhaps more simply than any mechanism in this file — undercuts reading it as evidence of anything. This arithmetic point should be checked in-house before the reactivity literature is invoked."
  15b: PARTIALLY-CHALLENGED (Moderate) — reaches the same conclusion independently and from the other side. Spiegelhalter 2005 (Statistics in Medicine 24(8)): apparent large ratios between small counts fall inside control limits and carry no signal, which is why funnel plots exist and why "spurious ranking into league tables" is to be avoided — a 1-to-5 movement sits well within Poisson variation, so "fivefold rise" is not a fact about the pipeline but an artefact of dividing small numbers. Lopez Bernal, Cummins & Gasparrini 2017 (Int J Epidemiol 46(1)): attributing a level change to an intervention requires adequate pre- and post-intervention observations with the secular trend modelled; a single post-change run cannot separate a level change from trend or noise. Separately, the presumption's own alternative explanation is the WEAKER hypothesis: Levitt & List 2011 (AEJ: Applied 3(1)) recovered the original Hawthorne illumination data and found the canonical result to be a day-of-week artefact — all lighting changes fell on Sundays, the only off day — and McCambridge et al. 2014 find reactivity effects small, wildly inconsistent, and the label too imprecise to be useful. Meanwhile the note's own explanation is a documented mechanism with 75 studies behind it: explicit, analytic, topic-specific criteria measurably tighten judgement, immediately (Jonsson & Svingby 2007, Educational Research Review 2(2)) — though the same review's second finding constrains it, since a criterion that raises inter-rater consistency has NOT thereby been shown to raise validity.
  What is at risk: A run-to-run count movement statistically indistinguishable from noise being filed as evidence that a self-imposed bar functions — on the very run where the pipeline's competence to adopt premises about its own reliability was the item under judgement — and that unearned validation then licensing further self-referential adoptions. Symmetrically at risk on the other side, and this is the half the presumption gets wrong: a reflex of discounting any favourable post-change movement as reactivity or self-serving application would make the system unable to register that any of its own corrections ever worked, which is a failure mode symmetrical with the one being guarded against, and would suppress a mechanism with 75 studies behind it. NOTE THE DIRECTION OF THE CORRECTION, so it cannot be misread: this does NOT vindicate the 2026-07-28 note. It finds that the note and the presumption made the same error with the sign flipped, and that PREMISE-124's FORBIDDEN MOVE ("reading a single favorable self-observation as evidence a safeguard 'works'") already forbade the note's move without needing any of this run's literature — which is why nothing new was minted here.
  Recommended action (for Tom): (1) Route the small-n correction back to 14b — the inference rested on treating a count difference as a finding, which is a checkable statistical error and a repeatable pattern, and it belongs alongside the Little's Law correction already routed as REVISE-248. (2) STOP CALLING IT A FIVEFOLD RISE. Plot the INCORPORATE count against its denominator for each of the last N runs with Spiegelhalter control limits and record whether the current point is inside them. If it is, the anomaly does not exist and neither explanation is needed. (3) Run the discriminating test, which is cheap and blind to the current run's incentives: apply the external-referent bar RETROSPECTIVELY to the last 20 MONITOR dispositions and count how many now clear it. Roughly a quarter clearing -> the bar has a stable threshold and the current run's count is consistent with threshold placement rather than favourable application. Far fewer clearing -> the bar was applied more permissively on the run where permissiveness was self-serving, which is the presumption's prediction. (4) Per Jonsson & Svingby, check the ADMITTED items for actual external-referent quality on independent inspection, not merely for having been admitted under a criterion that names external referents — consistency and validity are different properties. (5) Where practicable, have the bar's effect assessed on a run where the pipeline's own reliability is NOT the item under judgement.
  APPLIED REFLEXIVELY THIS RUN RATHER THAN RECOMMENDED FOR LATER: the 2026-07-29 batch produced 1 INCORPORATE against the previous run's 5. That movement is reported in lit_search_returns.md and in PREMISE-135 as a count with its denominator (1 of 8 items dispositioned) and is explicitly NOT narrated as evidence about the bar, about this run's discipline, or about anything else. On the same Poisson reasoning that refutes 1-to-5, a 5-to-1 movement is equally uninformative, and claiming the drop as evidence of rigour would be the identical error with the sign flipped. Recorded here so the claim can be checked rather than taken on trust.
  Urgency: Medium (no design change was made on this presumption, so nothing is currently broken by it; but it bears directly on how every future batch reports itself, including this one, and step (3) is a single cheap retrospective pass)
  PROVENANCE: Origin=14b; Chain=[14b->15a,15b->15c]; Item type=PRESUMPTION (unstated); Current status=REVISION-FLAGGED (shared framing refuted by both directions; constructive half retained)
  Disposition record: DISPOSITION-552 (lit_search_returns.md, 2026-07-29)

REVISE-251:
  Date: 2026-07-29
  Source item: 15b SYSTEMIC-RISK-FLAGS (i), (ii) and (iii) of 2026-07-29 — CONSOLIDATED (affected items PRESUMPTION-566, 567, 568, 569, 570, 572; cf. 565)
  Item type: SYSTEMIC RISK (cross-item structural vulnerability), risk level High on each sub-flag
  CONSOLIDATION NOTE, stated first because it is a decision Tom should be able to review: three separate HIGH systemic flags were raised this run and are filed as ONE revision flag with three sub-flags, not three. They name one locus — 14b's presumption-construction — and one remedy shape — state the quantity that would settle the item BEFORE filing it. Per PREMISE-121, each additional separately-tracked item lowers the probability that ANY item is acted on, and the obligation is to raise the information value of what is routed to a human rather than merely to route less. Each sub-flag retains its own DISPOSITION-NNN (557, 558, 559) so nothing is lost to consolidation.
  SUB-FLAG (i) "categorical-parity / binary-not-graded" — PRESUMPTION-566 + 567. 15b finding: both items run the inference "the instrument or procedure that produced X belongs to the same kind as one already known to be fallible, therefore X inherits that fallibility undiminished," treating a GRADED epistemic property as binary — warrant-from-iterated-generalisation in 566, independence-in-verification in 567. The governing literatures hold that categorical similarity is not decisive and that the correct move is to SIZE the residual: state the population and the termination criterion (Mitchell 1982, Artificial Intelligence 18(2); Mayo 2018, CUP), or estimate the dependence parameter (NUREG/CR-5485 beta factors of 0.03-0.22; Littlewood & Miller 1989, IEEE TSE 15(12); GAO threats-and-safeguards). Consequence if unchecked, and it is not rhetorical: a rule under which NO CORRECTION CAN BE BANKED AND NO CHECKER CAN BE TRUSTED is functionally the arrivals>0 / service=0 pathology PRESUMPTION-553 and DISPOSITION-536 already formalise. ACTED ON IN-RUN: the binary parity reading was explicitly NOT incorporated on 566 and the graded form was incorporated in its place as PREMISE-135 with the genetic inference excluded as a scope guard; on 567 the binary reading was likewise declined and the item held to the sized-residual reading with a three-arm dependence measurement as its discharge condition (MONITOR-490 instance A).
  SUB-FLAG (ii) "favourable-direction without a null model" — PRESUMPTION-568 + 569, structurally INVERTED in PRESUMPTION-565. 15b finding: both items infer a motivated-reasoning explanation from a direction-of-favourability pattern without establishing a null model or base rate for how often that pattern arises from a legitimate single mechanism or from ordinary variation. PRESUMPTION-565 failed on the same structure in the OPPOSITE direction, arguing from NON-uniform direction — which is checkable against MONITOR-489 and is verified there. A heuristic that fires on uniform AND non-uniform patterns alike is not discriminating. The pattern IS codified as a bias indicator (ISA 450), but as a PROMPT TO INVESTIGATE, not a finding, and it needs a denominator first. ACTED ON IN-RUN: DISPOSITION-552 / REVISE-250 routes the correction to 14b and applies it reflexively to this batch's own INCORPORATE count; PRESUMPTION-568 is held at MONITOR-491 pending the ISA 450 aggregate-direction tabulation, which is exactly the "file as a prompt to investigate, with a denominator" the flag asks for.
  SUB-FLAG (iii) "gate-vs-grade" — PRESUMPTION-570 + 572. Raised independently in BOTH against/ files as a cross-item candidate. 15b finding: both items convert a graded, revisable practice into a BINARY PRECONDITION that must be satisfied before an inference is permitted — provisional causal attribution corrected by re-triage (570), graded analogical alignment revised by negative-analogy bookkeeping (572) — and NEITHER BUDGETS THE COST OF THE CHECK IT DEMANDS. The costs are measured, not speculative: alert fatigue is an empirically quantified degradation of the very detection capability 570's remedy is meant to protect (Tariq et al. 2025, ACM Computing Surveys 57(9) Art.224; Ancker et al. 2017, BMC Med Inform Decis Mak 17:36), and a domain-similarity gate would have blocked the Ising -> Hopfield transfer (Knuuttila & Loettgers 2014, The Monist 97(3)) while applying to the majority of the reasoning the system actually does (Dunbar 1995). ACTED ON IN-RUN: on 570 the causal-establishment gate was refuted and dropped, the queue/priority claim was dropped (conceded weak by 15a itself), and 15b's zero-volume reconciliation was adopted instead — a provisional marker plus a stated falsifier, and ONE watchdog over the whole scheduled-output set. On 572 the check is held as graded bookkeeping subordinate to PREMISE-134's existing boundary clause, not as a precondition on the comparison.
  What is at risk: 14b's presumption-construction produces items at a rate the pipeline cannot absorb, and three of its recurring inference forms are now documented as unsound in the same run. The compounding risk is that each unsound form generates items that LOOK actionable — they name a real hazard and cite a real pattern — and so consume literature searches, dispositions and register entries before being refuted. That is not a neutral cost: this run also found (MONITOR-490) that four of eight items were governed by premises already ACTIVE, so between the two findings a majority of the batch was avoidable at intake. TENSION SURFACED RATHER THAN RECONCILED, per 15c's standing obligation: a general preference for grades over gates sits uneasily with PREMISE-124 (external baseline or UNCALIBRATED — a BINARY standard) and PREMISE-114 (authority as a documented chain to an external reference). Both were already flagged for review under REVISE-249 on 2026-07-28 and NEITHER HAS BEEN EDITED. This run relied on PREMISE-124 in its binary form four times (DISPOSITIONS 552, 555, 556, and as the INCORPORATE bar on 549), so the tension is live rather than theoretical.
  Recommended action (for Tom): (1) Adopt ONE intake rule at 14b covering all three sub-flags: before a presumption is filed, it must name the QUANTITY that would settle it — a stopping criterion, a dependence estimate, a miss rate, a null model with a denominator, or the cost of the check it demands. Absent that quantity, the observation is filed as a PROMPT TO INVESTIGATE and does not consume a literature search. This is a single change and it addresses all three patterns, because all three are the same omission wearing three faces. (2) Add the register pre-check that MONITOR-490 makes urgent: before an item is routed to 15a/15b, grep the validated-premise register for a governing premise. Four of eight items this run had one. (3) Read this alongside REVISE-249 (2026-07-28), whose recommended three-level assurance-grade vocabulary is the same gate-to-grade move in the verification register — these are one decision, not two, and taking them separately risks adopting graded assurance while leaving PREMISE-124 binary. (4) Then reconcile PREMISE-124 and PREMISE-114 to the graded vocabulary explicitly, with sign-off. Do not let the graded reading take effect by drift; this run's four uses of the binary form are the evidence that drift is the live risk.
  Urgency: HIGH (it bears on intake for every future batch, and combined with MONITOR-490 it names the two mechanisms that made a majority of this batch avoidable at source)
  PROVENANCE: Origin=15b (three systemic-risk flags over a 14b-origin cohort); Chain=[14b->15b->15c]; Item type=SYSTEM RISK; Current status=REVISION-FLAGGED; sub-flags partly discharged in-run via PREMISE-135, MONITOR-490 (instances A and B), MONITOR-491, MONITOR-492 and REVISE-250
  Disposition record: DISPOSITION-557, DISPOSITION-558, DISPOSITION-559 (lit_search_returns.md, 2026-07-29)

REVISE-252:
  Date: 2026-07-30
  Source item: PRESUMPTION-576
  Item type: PRESUMPTION (unstated — surfaced by inference); protocol status CONTESTED (Low confidence) — 15a SUPPORTED (Strong) against 15b CHALLENGED (Strong)
  FILED SEPARATELY FROM REVISE-253, DELIBERATELY: this run raises two revision flags rather than consolidating them, because PRESUMPTION-577 (MONITOR-493, same batch) is an item about whether consolidating adverse findings preserves their salience, and consolidating on the run that searched it would have pre-empted its own finding. The two flags name different loci — REVISE-252 amends a rule's TEXT, REVISE-253 adds a missing INTAKE CONVENTION — so they are not one finding in two readings. Combined severity of the two: HIGH. Independent findings routed to Tom this run: 2 flags, 5 disposition ids (560-564).
  What the item claims: REVISE-251's proposed intake rule requires a presumption to name the quantity that would settle it BEFORE it may consume a literature search; but on the 2026-07-29 record the settling quantities came OUT OF the searches (the NUREG dependence betas, the ISA 450 denominators, the alert-fatigue costings). The gate therefore demands information the gated step supplies.
  Net evidence: BOTH DIRECTIONS AGREE THE STRUCTURE IS REAL AND BOTH REFUSE THE ITEM'S CONCLUSION FROM IT, and — this is the finding — both arrive independently at the SAME amendment. 15b's decisive distinction is that the item equivocates on "quantity": a gate demanding a VALUE obtainable only from the search is circular, but a gate demanding a SPECIFICATION of the quantity whose value the search will supply is the ordinary discipline of every field that took pre-registration seriously (ICH E9(R1) 2019 estimand addendum; PICO, Richardson et al. 1995, ACP Journal Club 123(3):A12-A13; value-of-information ranking of unrun searches, Claxton & Sculpher 2006, PharmacoEconomics 24(11):1055-1068). Where the design parameter genuinely is a product of the data, the standard remedy is a PROVISIONAL commitment with a licensed revision and a preserved error rate (Wittes & Brittain 1990, Statistics in Medicine 9(1-2):65-71, internal pilots) — not abolition of the gate. 15a, searching independently and in the opposite direction, reached the same remedy from different sources: the screening literature names the condition (cold start) and its answer is cheap seeding with revision, never exclusion (Ferdinands et al. 2023, Systematic Reviews); and auditing practice sets materiality provisionally, records it, and revises it (ISA 320 / ISA 450 / PCAOB AS 2810). 15a's caveat (a) converges on the PROVISIONAL-COMMITMENT half of the remedy, though NOT on 15b's specification/value distinction, which it does not address — it affirms the item's negative claim and then says: "every source above is compatible with — and Ferdinands et al. positively recommends — requiring a provisional or candidate settling quantity at intake, which would satisfy most of REVISE-251's stated purpose at near-zero false-negative cost."
  What is at risk on each side, both priced: OVER-READING the item removes the pipeline's only pre-commitment device, and the failure mode is documented rather than hypothetical — without a pre-specified target, the quantity that settles an item becomes whatever the search returned, no item can ever be recorded as having FAILED to settle, and the disposition record silently converts into a record of what the literature happened to contain (Chan, Hrobjartsson, Haahr, Gotzsche & Altman 2004, JAMA 291(20):2457-2465, outcome reporting bias). UNDER-READING it — adopting REVISE-251 as a hard gate with no provisional path and no revision clause — turns away exactly the items a search would most improve, because the items whose settling quantity is a nuisance parameter are the high-expected-value-of-information ones (Boudreau, Guinan, Lakhani & Riedl 2016, Management Science 62(10):2765-2783, randomised evidence that evaluation filters penalise novelty).
  Recommended action (for Tom): AMEND REVISE-251 action (1) rather than adopt or reject it. Four changes, each traceable to a source above: (i) require a nameable quantity TYPE — population, outcome variable, summary measure, in the estimand sense — not a value; (ii) permit a PROVISIONAL value with its basis recorded, and permit exactly one recorded post-search revision; (iii) make the sanction for an unspecified item DEPRIORITISATION, not exclusion, so the false-negative cost is bounded; (iv) retain a bounded scoping pass whose only output is a sharpened specification, logged as such. TENSION SURFACED RATHER THAN RECONCILED, per 15c's standing obligation: change (iii) is in direct tension with PREMISE-106, which holds that this queue is in the unstable regime and that arrival already exceeds service. A gate that only deprioritises does nothing for the queue — so REVISE-251 cannot serve BOTH as a pre-commitment device and as admission control, and the pipeline needs admission control from somewhere else. Deciding which job the rule is for is prior to deciding its text.
  WHY NO PREMISE WAS MINTED FROM THIS CONVERGENCE, stated because a two-direction convergence on a specific rule is normally the strongest INCORPORATE signal available: (a) PREMISE-111's standing discount applies — 15a and 15b share model family, corpus and execution context, and PREMISE-120's shared-components line for this batch is at the end of DISPOSITION-564; (b) PREMISE-117 already carries the provisional-entry-plus-documented-revision discipline in the OUTPUT register (publish-then-revise in official statistics), so an intake version of it is a scope extension of an ACTIVE premise rather than a new premise, and under PREMISE-105 that is the register-inflation case; (c) most decisively, the rule this convergence supports is an amendment to a flag that is ITSELF UNADOPTED and pending Tom's review, and minting a premise that gives a pending rule its content would be adoption by use — which is PRESUMPTION-586's objection in this same batch (MONITOR-494). The convergent content is therefore recorded here, in the flag, where it awaits sign-off, rather than in the register where it would take effect.
  Urgency: HIGH (REVISE-251 has been before Tom since 2026-07-29 and the 2026-07-29 EOD intake already applied its rule to its own output voluntarily "though neither is adopted" — so the unamended rule is shaping intake now)
  PROVENANCE: Origin=14b; Chain=[14b->15a,15b->15c]; Original item=PRESUMPTION-576; Item type=PRESUMPTION (unstated); Transform at this step=Net evaluation and disposition; Current status=REVISION-FLAGGED
  Disposition record: DISPOSITION-560 (lit_search_returns.md, 2026-07-30)

REVISE-253:
  Date: 2026-07-30
  Source item: PRESUMPTION-588 (item-level) CONSOLIDATED WITH the 15b SYSTEMIC-RISK-FLAG of 2026-07-30 (cross-item; affected items PRESUMPTION-576, 577, 588 primary and PRESUMPTION-586 secondary)
  Item type: PRESUMPTION (unstated) + SYSTEMIC RISK (cross-item structural vulnerability), risk level High
  CONSOLIDATION NOTE — WRITTEN TO THE STANDARD PRESUMPTION-577 SAYS WAS MISSING, which is the point of writing it: one item-level REVISE and one cross-item systemic flag are filed as ONE entry because the systemic flag's subject matter (unmeasured treated as unbounded) IS the item's subject matter (a missing input's cost recorded as unmeasurable) — they are one finding, not two readings of one finding. (i) COMBINED SEVERITY: HIGH, higher than either part alone, because the item shows the defect operating and the flag shows it operating in four places. (ii) INDEPENDENT-FINDING COUNT: 2 findings (1 item, 1 systemic flag over 4 items), retaining 2 disposition ids (DISPOSITION-563, DISPOSITION-564), and 4 affected items each retaining its own disposition id. (iii) SYMMETRY CHECK, recorded because its absence was the substance of PRESUMPTION-577: this run consolidated ONE pair of ADVERSE findings and split ONE pair that could have been consolidated (REVISE-252 kept separate from REVISE-253) — so the run's own consolidation rate is 1 of 2 on adverse findings, and it produced no favourable findings this run to compare against. That denominator is too small to establish symmetry either way and is recorded as UNCALIBRATED per PREMISE-124, not as compliance. The historical symmetry audit is MONITOR-493's discharge condition.
  ITEM-LEVEL FINDING (PRESUMPTION-588, narrowed): the 7th consecutive dark sync was mitigated on the outbound side and the stated inbound loss — "today's agents had no Chat context" — was given no consequence, so its cost entered the record as zero because nothing measured it. Both directions agree the record contains no bound and that "the file is the deliverable" does not address the inbound direction. BOTH DIRECTIONS ALSO REFUTE THE ITEM'S OWN REMEDY, which is why this is REVISE and not MONITOR: the matched with/without comparison the item names as its settling quantity would not identify the effect. 15b: the missingness mechanism is unidentifiable from observed data, so the contrast still rests on an unverifiable exchangeability assumption and a sensitivity range is the terminal deliverable either way (Molenberghs, Beunckens, Sotto & Kenward 2008, JRSS-B 70(2):371-388). 15a, independently and against its own direction, reached the same objection from the applied side: at n=1 per arm the two arms cannot run simultaneously, so day-to-day workload variation is fully confounded with the treatment, which is why the ghost-ads design exists (Johnson, Lewis & Nubbemeyer 2017, Journal of Marketing Research 54(6):867-884). Two further sources discipline the item's premises rather than its remedy: the amount of missing input predicts the size of distortion badly, so seven dark days licenses no magnitude claim (Groves & Peytcheva 2008, Public Opinion Quarterly 72(2):167-189; Groves 2006, POQ 70(5):646-675), and added long-context input is not monotonically beneficial, so the SIGN of the missing term is not given either (Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni & Liang 2024, TACL 12:157-173).
  CROSS-ITEM SYSTEMIC FINDING (15b, accepted): all four items in this batch reason from the ABSENCE OF A MEASUREMENT OR RECORD to the ABSENCE OF A BOUNDED QUANTITY. 576 infers circularity from the settling VALUE being unavailable at intake when only the value, not the specification, was unavailable. 588 infers that UNCALIBRATED is the honest entry when worst-case bounds, threshold statements and sensitivity analysis are all computable without the matched comparison it asks for (Manski 1990, American Economic Review 80(2):319-323; VanderWeele & Ding 2017, Annals of Internal Medicine 167(4):268-274). 577 asserts a salience effect while supplying no measurement of it, and the effect is not even signed (Sloman et al. 2004, JEP:LMC 30(3):573-582). 586 shares the structure in the normative register: a missing sign-off record is read as an absence of legitimate authority rather than as an unmeasured question. The unifying defect converts UNMEASURED to UNBOUNDED, which in an auditing layer is not conservatism — it systematically inflates the apparent severity of anything not yet instrumented, and it does so in the direction that generates more items.
  RELATION TO EXISTING PREMISES — this flag is the SYMMETRIC COMPLETION of two ACTIVE premises and it is the reason a new premise is not minted for it: PREMISE-112 forbids the OPPOSITE error (declaring the unmeasured unimportant, then absent — the McNamara fallacy, unmeasured -> zero), and PREMISE-124 supplies UNCALIBRATED as the honest null entry. The flag's contribution is that BOTH defaults are wrong where a bound is computable, and that neither existing premise says so. That is a SCOPE AMENDMENT TO PREMISE-124, not a new premise, and 15c does not amend a validated premise — hence its appearance here as a recommendation.
  What is at risk: PREMISE-124 in its current form licenses UNCALIBRATED as a terminal entry. On this batch's evidence that is too permissive in one specific case — where a worst-case bound is cheaply computable, recording UNCALIBRATED is a refusal to compute rather than epistemic humility. Since PREMISE-124 was relied on four times in the 2026-07-29 run and is relied on three times in this one (MONITOR-493's magnitude entry, this flag's own symmetry-check line, and DISPOSITION-561), the scope question is live rather than theoretical. Note also that PREMISE-124 and PREMISE-114 were BOTH already flagged for amendment under REVISE-249 (2026-07-28) and REVISE-251 action (4) and NEITHER HAS BEEN EDITED — this is the sixth consecutive day, and the present flag is the third separate finding to land on PREMISE-124's text.
  Recommended action (for Tom): (1) ADOPT A THREE-STATE INTAKE CONVENTION at 14a/14b/15*, replacing the single undifferentiated "unmeasured": UNSPECIFIED (the quantity type is not yet named), UNMEASURED-BUT-BOUNDED (type named, value unknown, worst-case or logical bounds stated), UNIDENTIFIABLE (no observation could settle it, so a sensitivity analysis over stated assumptions is the terminal deliverable). Require any item asserting a cost, loss or effect to state a bound or name the method by which one would be obtained; forbid "no consequence recorded" for an unbounded quantity, AND forbid its converse, treating an unbounded quantity as high-risk by default. (2) AMEND PREMISE-124 to add the fourth option ahead of UNCALIBRATED: a computable worst-case bound, where one exists, displaces UNCALIBRATED. Do this with recorded sign-off, per MONITOR-494 — not by use. (3) RE-FILE the four items under the three states and check the resulting distribution; if a large share of open presumptions turn out UNMEASURED-BUT-BOUNDED, the pipeline's severity ratings need recalibrating, and that recalibration is itself measurable. (4) READ WITH REVISE-252: both flags are about intake and both are amendments to REVISE-251's action (1). Taking them separately risks adopting a specification rule without a bounding rule, which would leave three of this batch's four items unaffected.
  RUN THIS FIRST, IT IS FREE AND IT MAY SETTLE 588 OUTRIGHT: retrospectively grep the seven dark days' outputs for items whose content plausibly required prior-day conversational context, and count them. Zero would substantially challenge the item; a nonzero count converts an unmeasured cost into a lower bound, which is the entry the item should have had. Then compute the threshold statement from output already in hand: what fraction of attended items would have had to differ for any recorded disposition to flip. Only if both leave the question open is a comparison worth running, and then as a THREE-arm contrast — with, without, and with deliberately inflated inbound context — because Liu et al. predict a non-monotonic response a two-arm design cannot detect.
  Urgency: HIGH on the systemic half (it bears on every future item's severity rating and on PREMISE-124's text); MEDIUM-HIGH on the item half (the free test may close it)
  PROVENANCE: Origin=14b (item) and 15b (systemic flag over a 14b-origin cohort); Chain=[14b->15a,15b->15c]; Original items=PRESUMPTION-588 (item), PRESUMPTION-576/577/588/586 (flag cohort); Item type=PRESUMPTION (unstated) + SYSTEM RISK; Transform at this step=Net evaluation and disposition; Current status=REVISION-FLAGGED
  Disposition record: DISPOSITION-563 (item) and DISPOSITION-564 (systemic flag), lit_search_returns.md, 2026-07-30

# ================================================================================
# ---- 2026-07-31 c2a2-lit-search-pipeline (15c) — REVISE-254..257 ----
# 4 REVISE entries from a 3-item batch plus one systemic flag. REVISE-254 and REVISE-257
# are AMENDMENTS to pending items (REVISE-253 and REVISE-252 respectively) and narrow them;
# REVISE-255 and REVISE-256 are new. Net addition to Tom's queue: 2.
# ================================================================================

REVISE-254:
  Date: 2026-07-31
  Source item: PRESUMPTION-591
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Status: AMENDMENT TO REVISE-253 (does not stand alone; adopt or reject with it)
  What the item claims: REVISE-253's proposed three-state intake convention may resolve the cases PREMISE-124's UNCALIBRATED was minted for, or may merely rename them. The amendment's warrant is cost BOUNDABILITY; its stated validating test (grep the seven dark days) measures item FREQUENCY, which cannot confirm or refute the warrant.
  What is at risk: PREMISE-124's UNCALIBRATED discipline — the register's only standing block on favourable self-produced numbers, and by its own Applicable-to line binding on 15a/15b/15c/15d self-reporting. Adopting the third state on unmeasured ground relaxes that block in exchange for an unknown quantity.
  Net evidence: 15a SUPPORTED (Moderate-Strong) — partial identification (Manski 1990, 2003; Tamer 2010) supplies a COMPUTED entry criterion for an intermediate state, which is exactly the settling quantity 14b names, and Der Kiureghian & Ditlevsen 2009 supply the action-relevance test. 15b CHALLENGED (Strong) — Dubois & Prade hold that ignorance is a meta-evaluation and NOT a truth value homogeneous with true and false, so the three-valued form is a category error rather than a refinement; Preston & Colman 2000 and Lozano et al. 2008 measure two- and three-point scales as WORST on reliability, validity and discriminating power, with improvement monotone to about seven; Krosnick 1991 names the mechanism (the middle category becomes a refuge for judgments the rater declined to make, INCREASING measurement error). 15a's own caveat (a) concedes the decisive empirical point before 15b was read: Cochran abandoned worst-case bounding because the bounds were too conservative to act on, and modern partial identification repeats that no-assumptions bounds frequently cover zero.
  Recommended action — FOUR CLAUSES, all gating adoption rather than replacing the amendment:
    (1) MEASURE THE PARTITION FRACTION FIRST, over the existing UNCALIBRATED population. For each item attempt to state (a) an outcome scale and (b) a worst-case bound on it. Record one of three outcomes: bound computed AND strictly narrower than the logical range / bound computed but trivial / no scale statable. The fraction in the first bin is the whole question. In-house; no search; decisive.
    (2) FIX THE ADOPTION THRESHOLD BEFORE RUNNING (1). Below it the amendment is WITHDRAWN, not weakened. Pre-registration is the point — the measurement is being run by the party that proposed the amendment.
    (3) IF ADOPTED, entry to the new state must carry the COMPUTED BOUND inside the entry, so an empty bound field is a schema violation rather than a judgment. This is the clause that answers Krosnick: a state you cannot enter without producing a number cannot be satisficed into.
    (4) IF ADOPTED, items in the new state must receive a DIFFERENT SUBSEQUENT ACTION from UNCALIBRATED items, or the state is descriptive and not action-bearing.
    CONSIDER INSTEAD, per the logic literature's own recommendation: a possibility/necessity or interval PAIR attached to the existing two states, which adds expressiveness without adding a category for a rater to retreat into. Dubois & Prade's objection is specifically to truth-functional three-valued calculi, not to graded representation as such.
  Urgency: Medium-High — the gate must be in place before adoption; not urgent otherwise.
  CORRELATION DISCLOSURE (PREMISE-120): both search directions cite Manski, Ciucci/Dubois/Lawry 2014 and Graydon & Holloway 2017. Those are ONE reading each. The load-bearing UNSHARED material is 15b's rating-scale and satisficing literature, which 15a did not reach and which 15a's caveat (d) named as its own gap.
  Disposition record: DISPOSITION-565 (lit_search_returns.md, 2026-07-31)
  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: PRESUMPTION-591
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from a mismatch between an amendment's stated warrant (boundability) and its stated validating test (frequency)
      15a: Searched for supporting literature (2026-07-31); SUPPORTED (Moderate-Strong), Cochran conceded against its own direction in caveat (a)
      15b: Searched for challenging literature (2026-07-31); CHALLENGED (Strong)
      15c: Net evaluation and disposition; routed as a pre-adoption gate on REVISE-253 rather than as a new recommendation
    Current status: REVISION-FLAGGED

REVISE-255:
  Date: 2026-07-31
  Source item: PRESUMPTION-592
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Status: AMENDMENT TO AN ACTIVE PREMISE — PREMISE-110 (High confidence, ACTIVE, Applicable-to names "the scheduler watchdog")
  What the item claims: The scheduler watchdog issued a PASS over `c282-wiki-agent-daily-run` on a file-count-and-recency test while the task was DIRECTLY OBSERVED to be still executing (status: running, 26 turns). The watchdog has a symbol for "cannot check" and none for "still running."
  What is at risk: PREMISE-110 as written, and every green signal its Applicable-to line covers. The watchdog is the only layer asserting fleet health, and its PASS is currently readable as a termination claim it cannot support.
  WHY THIS IS AN AMENDMENT AND NOT A NEW PREMISE — the load-bearing finding of this entry: PREMISE-110 already governs the scheduler watchdog by name, and prescribes the safe form as "affirmative and perishable — the monitor must be actively fed on an independent timebase, so that cessation of activity is itself the alarm." THE WATCHDOG SATISFIES THAT PRESCRIPTION. Artifact recency is affirmative, perishable and actively fed. It went false-green anyway. So this is not an instance of PREMISE-110 being violated; it is PREMISE-110 being under-specified — the clause says the signal must be fed, and does not say WHICH signal. Minting a new premise would leave the defective one standing and give a reader two overlapping records to adjudicate.
  Net evidence: 15a SUPPORTED (Strong) — Lamport 1977 and Alpern & Schneider 1985: termination is a LIVENESS property and no finite prefix of an execution confirms one; artifact inspection is by construction a finite observation, so the check certifies a safety-class fact and reports it as a liveness-class fact. Chandra & Toueg 1996: unreliable detectors are acceptable and unavoidable but must DECLARE their accuracy class. Isermann 2006 supplies the stuck-at analogy. 15b PARTIALLY-CHALLENGED (Moderate) — and it does NOT contest the category claim; its steelman concedes "the defect, if any, is in the verdict's label" and its first mitigation is exactly the relabel below. What 15b defeats is the REMEDY: SRE ch. 6 holds black-box symptom monitoring is what should page a human; the Two Generals result makes exactly-once completion signalling impossible, so exit status is a proxy too; and an unthresholded "still running" branch is unactionable, which the alerting literature names as a principal driver of alert fatigue. 15b also correctly notes the stuck-at analogy is imperfect in the direction that matters — a fresh artifact is NEW evidence, not a frozen reading.
  Recommended action — ONE AMENDMENT AND THREE OPERATIONAL CLAUSES:
    (1) AMEND PREMISE-110: the affirmative perishable signal must be the subject's TERMINAL STATE, not any of its outputs. An output is produced mid-execution and cannot distinguish "finished" from "still going", because termination is a liveness property and no finite observation settles one.
    (2) RELABEL, and this is near-zero cost and discharges the whole documentation defect: change the watchdog's PASS to name its evidence — "artifacts present and fresh" — so that the termination inference is not silently available to readers.
    (3) DO NOT replace the artifact criterion with exit status. ADD terminal state as an additional field. Per SRE ch. 6 the symptom check should remain the paging signal, and a run that exits cleanly having produced nothing must still fail — the remedy the item implies would pass it.
    (4) Introduce a "still running" state only WITH a duration threshold. Without one the third branch has no defined action.
  Urgency: Medium — the amendment and the relabel are warranted on theory alone and cost almost nothing; the magnitude is unknown (see below) and nothing here is time-critical.
  VALIDATING TEST (in-house, cheap, and it decides the magnitude this flag deliberately leaves open): (a) for the last N scheduled runs, compare artifact write time against the scheduler's own terminal time — the distribution of that gap is how often, and by how much, PASS precedes termination; (b) separately, for runs that TERMINATED IN ERROR, check whether their artifacts were nonetheless fresh at check time. (b) is the damaging case and is the false-green rate as 14b defined it.
  UNCALIBRATED (PREMISE-124): the false-green RATE is unmeasured. The observed instance is n=1. This entry must not be read as evidence that the rate is material — only that the verdict cannot mean what its label implies.
  CONSOLIDATION NOTE (PRESUMPTION-577 / MONITOR-493): the magnitude question could have been split to a separate MONITOR entry and was not, because the measurement is already named here as this flag's validating test and a separate entry would add a record without adding an action. This run's consolidation rate on adverse findings is 1 of 4. Too small a denominator to establish symmetry; recorded as UNCALIBRATED, not as compliance.
  CORRELATION DISCLOSURE (PREMISE-120): both directions cite Chandra & Toueg 1996 and the data-observability freshness material, in OPPOSITE services. One source doing work on two sides is not two sources agreeing; no convergence is claimed from it.
  Disposition record: DISPOSITION-566 (lit_search_returns.md, 2026-07-31)
  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: PRESUMPTION-592
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from a watchdog verdict whose evidence class could not express the state directly observed (task still running)
      15a: Searched for supporting literature (2026-07-31); SUPPORTED (Strong), refusing any claim about the rate in caveat (a)
      15b: Searched for challenging literature (2026-07-31); PARTIALLY-CHALLENGED (Moderate) — remedy defeated, category claim conceded
      15c: Net evaluation and disposition; pre-check found PREMISE-110 governs AND is under-specified, converting the batch's strongest INCORPORATE candidate into an amendment of the governing premise
    Current status: REVISION-FLAGGED

REVISE-256:
  Date: 2026-07-31
  Source item: PRESUMPTION-600
  Item type: PRESUMPTION (unstated — surfaced by inference)
  What the item claims: The 07-29 register pre-check removed 9 of 13 items; the 07-30 0-of-4 yield was then explained entirely downstream (PREMISE-114 unratified). An intake filter that removes already-governed items may be depressing the residual cohort's yield, and the explanation offered does not account for it.
  What is at risk: In one direction, the register pre-check (MONITOR-490's convention), applied voluntarily since 2026-07-29 without adoption and without its error rate reported. In the other direction — and this is the risk the item does not see — the queue's arrival rate, if the pre-check is weakened on an underpowered comparison.
  Net evidence: 15a SUPPORTED (Moderate-Strong) — Berkson 1946, Heckman 1979, Altman & Bland 1994 and the sequential-filtering recall results agree that a non-random admission filter changes the residual population's composition, so an explanation citing only downstream causes is incomplete by construction. 15b CHALLENGED (Strong) — and the decisive challenge is arithmetic, not bibliographic: 1/8 versus 0/4 has no discriminating power at any conventional standard and one conversion either way reverses it, so the item's OWN settling quantity cannot settle it. 15b adds two things 15a reached for and did not find: PRISMA-S (Rethlefsen et al. 2021) makes redundancy filtering at intake MANDATED and separately reportable, with the literature's sole concern being false exclusion whose remedy is measurement rather than removal; and Little 1961, under which admission control is the textbook prescription for exactly C2A2's disclosed pathology (MONITOR-484: ~174-item backlog, observed drain rate zero). 15a's caveat (b) independently volunteers the disanalogy that carries 15b's case.
  Recommended action — THREE CLAUSES; clause (1) REPLACES the item's own test:
    (1) DO NOT run the cohort comparison the item specifies. Run the DIRECT test instead: take the 9 GOVERNED-CANDIDATE items the 07-29 pre-check removed and push them through 15a/15b/15c BLIND to the pre-check's verdict. Their conversion rate IS the false-exclusion cost, measured directly at n=9, requiring no matched cohort and no cross-day comparability assumption.
    (2) ADOPT PRISMA-S-STYLE REPORTING of the pre-check as a standing convention: count in, count removed, criterion applied, measured false-exclusion rate — every cycle. This is what the nearest applied practice mandates and it costs four numbers.
    (3) DO NOT weaken or remove the pre-check on the current evidence, and STATE THE FIGURE OF MERIT before measuring anything. Per-item yield and dispositions-per-unit-reviewer-capacity recommend OPPOSITE actions, and the item silently assumes the first.
  Urgency: Medium-High — clause (3) is protective and should hold immediately; clause (1) is cheap and unblocks the question.
  NOTE ON INCENTIVE, recorded because the run has one: 15b's challenge here partly defends a convention this pipeline adopted for itself, and 15c's disposition partly declines to weaken it. The direct test in clause (1) is the check on that, and it is specified to run blind for that reason.
  CORRELATION DISCLOSURE (PREMISE-120): both directions cite the sequential-filtering recall result and Wang et al. 2020, read in opposite services. No convergence claimed from shared sources.
  Disposition record: DISPOSITION-567 (lit_search_returns.md, 2026-07-31)
  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: PRESUMPTION-600
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from a downstream-only explanation offered for a yield figure whose cohort had been non-randomly filtered upstream
      15a: Searched for supporting literature (2026-07-31); SUPPORTED (Moderate-Strong), caveats (a) and (b) volunteered against its own direction
      15b: Searched for challenging literature (2026-07-31); CHALLENGED (Strong) — settling quantity shown unpowered, remedy replaced
      15c: Net evaluation and disposition; constructive half retained and strengthened, destructive half refused
    Current status: REVISION-FLAGGED

REVISE-257:
  Date: 2026-07-31
  Source item: SYSTEMIC-RISK-FLAG (15b, 2026-07-31) over PRESUMPTION-591, PRESUMPTION-592, PRESUMPTION-600
  Item type: PRESUMPTION (unstated) + SYSTEMIC RISK
  Status: AMENDMENT TO REVISE-252 (does not stand alone; adopt or reject with it)
  What the flag claims: UNDERPOWERED SELF-MEASUREMENT. All three items in this batch name a settling quantity by TYPE, which is REVISE-252's amendment working as intended — partition fraction, false-green rate, yield comparison. In all three the available denominator is single-digit: n=1 observed still-running task; cohorts of 8 and 4; a per-item bound judgment over an UNCALIBRATED population of unstated size. A proportion estimated on a single-digit denominator cannot discriminate the hypotheses posed.
  What is at risk: REVISE-252's settling-quantity convention itself. It is a genuine improvement over naming a quantity by value, and it would be discredited by a run of inconclusive tests it licensed. The specific hazard is that in the register a null returned FOR WANT OF POWER is indistinguishable from a null returned ON EVIDENCE.
  Net evidence: 15b CHALLENGED (batch-level, Strong). No FOR search is run against a systemic flag. The claim is arithmetic rather than bibliographic and is therefore NOT discounted for model-level correlation in the way a shared-citation convergence would be. Independent corroboration from a different agent in the same run: for all three items, 15c's recommended action REPLACED the item's stated test with a better-powered one drawn from the existing population — which is a second party finding the specified quantities infeasible as named, arrived at while writing the dispositions rather than while reading the flag.
  Recommended action: Extend REVISE-252 with a FEASIBILITY CLAUSE. A settling quantity must be accompanied by (a) the denominator currently available, and (b) where that denominator is single-digit, either a named route to a larger one or an explicit statement that the item is NOT CURRENTLY DECIDABLE on the quantity as named. In practice the larger-n route is usually available and cheaper — for all three items in this batch a direct per-item test over the existing population (attempt the bound on each UNCALIBRATED item; compare write-time to terminate-time over the last N runs; run the 9 removed items) has a larger effective n than the cohort comparison the item specified.
  Urgency: Medium
  PATTERN COUNT, recorded so the unit of analysis can change if it recurs: this is the SECOND consecutive batch in which measurement DESIGN, not evidence, was the binding constraint (cf. REVISE-253, 2026-07-30, where both directions refuted the item's own remedy). Two instances in two batches is not yet a defect class under PREMISE-130. A third, in a third signature, would make the right unit "a convention that does not require feasible tests" rather than "three items with weak tests."
  Disposition record: DISPOSITION-568 (lit_search_returns.md, 2026-07-31)
  PROVENANCE:
    Origin: 14b (items) / 15b (flag)
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: batch-level over PRESUMPTION-591, PRESUMPTION-592, PRESUMPTION-600
    Item type: PRESUMPTION (unstated) + SYSTEMIC RISK
    Transform at each step:
      14b: Surfaced three items, each naming a settling quantity by type per REVISE-252
      15a: n/a — no FOR direction is run against a 15b systemic flag
      15b: Raised SYSTEMIC-RISK-FLAG on the common single-digit-denominator problem across all three (2026-07-31)
      15c: Net evaluation and disposition; accepted, routed as an amendment to REVISE-252
    Current status: REVISION-FLAGGED

REVISE-258:
  Date flagged: 2026-08-01
  Source item: PRESUMPTION-601 · Disposition record: DISPOSITION-569
  Item type: PRESUMPTION (unstated)
  Finding: The item's CONSTRUCTIVE half is supported from both directions — a HOLD is a decision, and the question "where does it live?" is answered by naming an authority for the fact class. Its DESTRUCTIVE half is REFUTED by 15b: SSOT prohibits multiple AUTHORITIES, not multiple stores, and CQRS read models and bounded-context duplication make a reader-shaped second store a named correct pattern. "The remedy adds a third state store" is therefore not, by itself, a fault.
  ITEM'S OWN REMEDY DIRECTION DEFEATED: routing HOLD facts to decisions.md would move them into a register with a 26-day observed write failure — converting a propagation failure into total silent loss. The ADR literature also scopes decision registers to architectural decisions and counsels against inflating them with per-item operational state.
  Already governed, amended rather than duplicated: PREMISE-066 states the SSOT architecture with a load-bearing scope guard requiring an explicit, TESTED extraction interface that FAILS LOUDLY. That guard is written for a user-facing derived view. The finding is that it is UNDER-SPECIFIED for operational state. No new premise minted (07-31 precedent, REVISE-255).
  Recommended action for Tom:
    (1) Amend PREMISE-066's scope guard to cover OPERATIONAL state, and to state the criterion explicitly as ONE AUTHORITY PER FACT CLASS WITH WRITTEN DERIVATION RULES — not the count of files.
    (2) Name the authority for HOLD facts. If the answer is decisions.md, HOLD_LIST.md becomes a legitimate derived projection with a stated refresh rule, and the 07-31 remedy is fine as built.
    (3) Do NOT route anything to decisions.md until its write path is repaired and demonstrated.
    (4) Run 15b's discriminating test: enumerate every fact class in the wiki and count independently-WRITABLE stores per class. Fact-class denominator, not per-run — satisfies PREMISE-136.
  Urgency: Medium-High
  PROVENANCE: Origin 14b · Chain [14b → 15a, 15b → 15c] · Current status: REVISION-FLAGGED

REVISE-259:
  Date flagged: 2026-08-01
  Source: SYSTEMIC-RISK-FLAG 2026-08-01 (Agent 15b) · Disposition record: DISPOSITION-575
  Affected: PRESUMPTION-601, -602, -611, -615 primary; -604, -609 by mechanism. Structurally: every item this pipeline has processed.
  Finding: ALL SIX ITEMS IN THIS BATCH NAME A REMEDY THE PIPELINE CANNOT EXECUTE. 601 needs an authority named for HOLD facts; 602 needs a downstream-consumer index; 604 needs a scope field on settling quantities; 609 needs an invariant added to the verifier suite; 611 needs an interval representation and a two-classifier sample; 615 needs a confidence field on the PRS record. The pipeline's only outputs are PREMISE, MONITOR and REVISE entries. Every finding, however well evidenced, terminates in a flag.
  This is not a literature gap. It is a closed-loop failure: the diagnostic organ has no effector. Corroborating register history — 0 INCORPORATE on three consecutive runs before today; 24 days of zero drain on the ~189-item 15d backlog; the 26-item legacy-cohort retag pending authorisation for SEVEN consecutive runs; and now THREE consecutive runs (07-30 unratified PREMISE-114; 07-31 under-specified PREMISE-110; 08-01 PRESUMPTION-611 against REVISE-254) in which the register's own state rather than the evidence determined an outcome.
  Governing premise, already on the books: PREMISE-131 — a warning is not a control, and an UNDELIVERED warning is zero mitigation, not reduced mitigation. A REVISE flag awaiting authorisation across seven runs is an undelivered warning by that premise's own definition. The pipeline has been applying to its subject matter a standard it fails on its own output.
  Recommended action for Tom — ONE question, and everything else is downstream of it:
    What, if anything, is this pipeline authorised to write outside its own four registers
    (validated_premises.md, monitor_queue.md, revision_flags.md, lit_search_returns.md)?
    Two decisions are already blocked on the answer and are named so the cost is visible:
      (a) the 26-item legacy-cohort retag to [MISROUTED-INTERNAL-EMPIRICAL] — 7th run pending;
      (b) the PRESUMPTION-611 sample — cheap, population in hand, no authorised runner.
  Urgency: High
  NOT A CLAIM THAT THE FINDINGS ARE WRONG. Every item this run was searched in both directions and the evidence stands on its own. The claim is that the disposition step has no move available that changes the system, and that this has been true long enough to be a structural property rather than a run of bad luck.
  PROVENANCE: Origin 15b · Chain [15b → 15c] · Current status: REVISION-FLAGGED
