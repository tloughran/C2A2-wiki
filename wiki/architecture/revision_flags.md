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

