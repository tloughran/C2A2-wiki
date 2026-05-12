# C2A2 Validated Premises Register
**Maintained by Agent 15c | Initialized: 2026-04-13**

---

## PREMISES INCORPORATED INTO ARCHITECTURE

These premises have passed net evaluation and are approved for use in decision-making, research design, and system implementation.

---

### PREMISE-001:
**Date validated:** 2026-04-13  
**Source item:** ASSUMPTION-005  
**Item type:** ASSUMPTION  

**Validated statement:**  
Traditions (defined as coherent systems of assumptions, methods, and evaluative standards) are a meaningful and well-justified unit of analysis for comparative research on research practices, supported by major philosophical frameworks (Lakatos' research programs, Kuhn's paradigms, Laudan's research traditions).

**Supporting evidence:**
- Lakatos: Research programs as fundamental units of scientific development
- Kuhn: Paradigms as exemplars and problem-solving frameworks
- Laudan: Research traditions as integrating research programs

**Challenges noted:**
- Boundary problems (traditions have fuzzy edges, not sharp boundaries)
- Alternative units exist (though they appear complementary rather than contradictory)

**Confidence:** High

**Applicable to:**
- Core research design (tradition identification and mapping)
- Agent 14a/14b/15a/15b instruction sets
- Comparative analysis framework
- Cross-tradition signal detection

**Re-check due:** 2026-07-13 (Quarterly)

**Status:** ACTIVE

**Rationale:**  
Triple support from canonical philosophers of science carries significant weight. The boundary problem critique is valid but standard in analytical philosophy and does not invalidate the tradition as an analytical unit. Traditions may have fuzzy boundaries, but they remain meaningful and useful for organizing knowledge about research practices.

---

### PREMISE-002:
**Date validated:** 2026-04-13  
**Source item:** ASSUMPTION-009  
**Item type:** ASSUMPTION  

**Validated statement:**  
Displacement vectors in semantic space, validated by Mikolov's vector arithmetic in word2vec and related models, provide a usable mechanism for identifying structural similarities across traditions. Known limitations (context-dependence, spurious patterns) are manageable through validation protocols.

**Supporting evidence:**
- Mikolov: Vector arithmetic in word embeddings demonstrates compositional semantics
- Validated empirically in NLP applications (king - man + woman = queen)
- Extensible to arbitrary semantic spaces

**Challenges noted:**
- Context-dependent spaces (embeddings vary with training data)
- Spurious patterns possible (false similarities from mathematical artifacts)
- Semantic similarity unreliable for novel domains

**Confidence:** Moderate

**Applicable to:**
- Agent 15c cross-tradition signal detection
- Agent 16 signal validation
- Embedding-based inference
- Vector space comparisons

**Re-check due:** 2026-05-13 (Monthly)

**Status:** ACTIVE

**Rationale:**  
The displacement vector mechanism is empirically validated in NLP and the identified risks are known and manageable. Context-dependence and spurious patterns are not hidden problems but documented challenges in embedding-based methods. Use of this mechanism requires validation protocols (human review, consistency checks) but is justified.

---

### PREMISE-003:
**Date validated:** 2026-04-13  
**Source item:** ASSUMPTION-012  
**Item type:** ASSUMPTION  

**Validated statement:**  
Human review capacity is a documented bottleneck in human-in-the-loop AI systems and should be treated as a primary constraint on throughput in C2A2. Agent quality affects what humans must review, but human availability is the binding constraint.

**Supporting evidence:**
- Well-established HITL bottleneck in human-in-the-loop AI systems
- Documented in literature on AI-assisted research and content analysis
- Supported by practical experience with research automation

**Challenges noted:**
- Agent quality may also be constraining (complementary, not contradictory)
- Question of relative magnitude (which is MORE constraining?)

**Confidence:** High

**Applicable to:**
- System throughput model
- Parallelization strategy
- Resource allocation
- Agent 14a/14b workload design
- Prioritization of agent improvement vs. human efficiency

**Re-check due:** 2026-07-13 (Quarterly)

**Status:** ACTIVE

**Rationale:**  
Human review is empirically documented as a HITL bottleneck in research automation. The assumption correctly identifies this as a primary constraint. Complementary concerns about agent quality do not invalidate this premise but may suggest parallel optimization strategies (improve agents AND increase human review capacity).

---

### PREMISE-004:
**Date validated:** 2026-04-15  
**Source item:** ASSUMPTION-024  
**Item type:** ASSUMPTION  

**Validated statement:**  
Convergence of independent lines of evidence (triangulation/overdetermination) is evidentially significant and constitutes a legitimate confirmatory strategy in science. When multiple independent methods converge on a common result, confidence in that result is strengthened (Wimsatt 1981, Kuorikoski & Marchionni).

**Supporting evidence:**
- Wimsatt (1981): Foundational work on robustness, reliability, and overdetermination
- Kuorikoski & Marchionni: Evidential diversity and triangulation of phenomena
- 2024 epistemic granularity work: Convergence of multiple factors provides claim justification
- Model robustness in climate science: Multi-model convergence strengthens representational accuracy

**Challenges noted:**
- Triangulation's value depends on genuine independence of evidence streams
- If evidence shares common biases (e.g., same LLM backbone), convergence may be spurious
- LLM hallucination literature (46% reasoning errors from correlated embeddings) creates common-cause risk
- Epistemic granularity: apparent overdetermination can dissolve at different levels of specificity
- C2A2's FINDING-004/009/011 independence has not been established

**Confidence:** Moderate (general principle is strong; application to C2A2 requires independence validation)

**Applicable to:**
- Evaluation of cross-tradition findings (FINDING-004, 009, 011)
- Assessment of convergence claims in research synthesis
- Design of validation protocols requiring independent evidence streams
- Future finding evaluation criteria

**Re-check due:** 2026-05-15 (Monthly — monitor whether independence of C2A2 findings can be established)

**Status:** ACTIVE (with standing independence caveat)

**Rationale:**  
The general principle of triangulation/overdetermination is robustly supported by Wimsatt's foundational work and subsequent philosophy of science literature. The challenge is not to the principle but to its specific application: C2A2's FINDING-004/009/011 may not constitute genuinely independent evidence if generated by the same LLM with similar prompting. INCORPORATE is warranted for the general principle; the specific application requires independence testing. This caveat should be checked monthly.

**PROVENANCE:**
  Origin: 14a
  Chain: [14a → 15a, 15b → 15c]
  Current status: INCORPORATED

---

### PREMISE-005:
**Date validated:** 2026-04-18  
**Source item:** ASSUMPTION-040  
**Item type:** ASSUMPTION  

**Validated statement:**  
ChatGPT projects are strictly account-scoped — there is no cross-account project visibility in the same Chrome instance absent an explicit invite-gated sharing mechanism. Account A's projects do not automatically render in account B's session by accident; cookie partitioning and standard SaaS tenancy design rule out accidental cross-account visibility.

**Supporting evidence:**
- OpenAI ChatGPT Projects help documentation: projects tied to account, visible only to signed-in user on that account
- OpenAI Enterprise/Teams data-isolation statements: workspace/project content scoped to workspace
- SaaS multi-tenancy design patterns (Krebs, Momm & Kounev 2012): per-tenant isolation at project/workspace level is the default
- OWASP / session-management: distinct web sessions in same browser sandboxed by cookie partitioning
- Cookie-jar literature (Englehardt & Narayanan 2016): no mechanism for accidental cross-session visibility in same browser

**Challenges noted:**
- 2023 ChatGPT title-leak incident (Redis caching bug) — vendor-side defect, not a cross-account visibility feature; data-leak incident, not counter-evidence to scoping
- Shared / family-mode browser profiles: user-confusion about which account is active, but data itself remains scoped
- Explicit collaborator-invite sharing (rolled out 2025): deliberately extends visibility within a workspace — not a counterexample, but a small scope qualifier to the absolute form of the claim

**Confidence:** High (for the design-level claim — account scoping by design)

**Applicable to:**
- Route-elimination logic for ND-vs-personal ChatGPT scrape sessions
- Cross-account data-ingestion planning (establishes that direct in-browser cross-view is not a route)
- Pairs with ASSUMPTION-041 (Drive connector durability) and PRESUMPTION-047 (user-directedness) in the 2026-04-18 route-selection cluster

**Re-check due:** 2026-07-18 (Quarterly — vendor ToS / feature evolution could shift collaborator-scope claims)

**Status:** ACTIVE (with small scope qualifier: account-scoping is about default visibility, not about user-initiated data movement between accounts; the invite-gated sharing mechanism is an exception by design, not by accident)

**Rationale:**  
Account-scoping of projects is the standard and documented SaaS tenancy pattern. OpenAI's own documentation makes it explicit, and generic web-security principles (cookie partitioning, session sandboxing) converge on the same conclusion. 15a found strong support; 15b found no credible challenge to the central claim. The only qualifier is the deliberate collaborator-invite feature, which extends visibility within a workspace by explicit user action — not a defeater, but a scope note. INCORPORATE is warranted; the 2026-04-18 route-selection logic that rests on account-scoping is well-grounded.

**PROVENANCE:**
  Origin: 14a
  Chain: [14a → 15a, 15b → 15c]
  Current status: INCORPORATED

---

### PREMISE-006:
**Date validated:** 2026-04-20  
**Source item:** ASSUMPTION-047  
**Item type:** ASSUMPTION  

**Validated statement:**  
Master-wiki narrative discrepancy should be flagged transparently rather than silently reconciled at the briefing layer. Surfacing degraded-state and freshness-gap information explicitly is the canonical practice across SRE, observability, data-quality, explainable-AI, and incident-management literatures; silent reconciliation creates latent risk and erodes downstream trust.

**Supporting evidence:**
- Observability / SRE literature (Beyer et al. 2016; Majors et al. 2022): "make the unknown known" — surface staleness and freshness-gap state explicitly.
- Transparent-UX / "honest machines" literature (Weld & Bansal 2019; Rader et al. 2018): calibrated user trust requires surfaced uncertainty.
- Data-quality literature (Batini et al. 2009): freshness is an auditable quality dimension; downstream consumers deserve visibility into freshness gaps.
- Incident-management literature (Allspaw 2012 blameless postmortems; Morgan 2014): transparency about state discrepancies builds system maturity.
- C2A2's own prior scaffolding: ASSUMPTION-040 INCORPORATE and PRESUMPTION-042 remediation both commit to explicit-signal discipline; this premise extends that commitment to narrative-consistency.

**Challenges noted:**
- 15b NO-CHALLENGE-FOUND (weak; calibration-level only).
- Caveat: "transparently" needs a specification (raw-data, human-readable annotation, or structured metadata field).
- Caveat: briefing audience affects transparency budget (personal vs. customer-facing).
- Caveat: flags themselves can trigger alert fatigue if noisy.

**Confidence:** High

**Applicable to:**
- Briefing-layer epistemic policy (how to render discrepancies between literal state and intended interpretation).
- Governs the related data-hygiene remediation for ASSUMPTION-048 (stale-placeholder-as-clear): ASSUMPTION-047 is the senior commitment; ASSUMPTION-048 becomes a data-hygiene violation to remediate, not a normative claim to validate.
- Pairs with the SELF-AWARENESS-META cluster's remediation direction (disambiguate null/missing signals with explicit observability).
- Informs all downstream briefing-surface rendering decisions.

**Re-check due:** 2026-07-20 (Quarterly)

**Status:** ACTIVE (with operationalization note: a concrete rendering convention for "transparent flagging" should be chosen before this premise is used as a hard constraint)

**Rationale:**  
Strong convergence across SRE, data-quality, XAI, and incident-management literatures; weak challenge limited to calibration (flag format, flag frequency) rather than the underlying commitment. Pattern: high-support + low-challenge + aligned with prior C2A2 disposition scaffolding = canonical fast-path to INCORPORATE. Also creates a useful anchor for resolving the ASSUMPTION-047 ↔ ASSUMPTION-048 internal tension surfaced by the paired 15b search: if ASSUMPTION-047 is senior, ASSUMPTION-048's "report stale as clear" is a violation of the senior commitment, not a separate normative claim.

**PROVENANCE:**
  Origin: 14a
  Chain: [14a → 15a, 15b → 15c]
  Current status: INCORPORATED

---

### PREMISE-007:
**Date validated:** 2026-04-20  
**Source item:** ASSUMPTION-051  
**Item type:** ASSUMPTION  

**Validated statement:**  
Tool-layer immutability is a correctness precondition for prompt-cache reuse. When cached prefix content or tool definitions (including tool schemas, their ordering, and their positioning) change between requests, cache-key invalidation is the correct and expected behavior, not a bug. Caching architectures must treat tool definitions as part of the cacheable prefix and must stabilize them across cached calls.

**Supporting evidence:**
- Anthropic Prompt Caching documentation (2024-2026): tool definitions participate in cache-key derivation; changes to tool schemas or ordering invalidate cache entries. This is explicit, vendor-documented behavior.
- OpenAI Prompt Caching documentation (2024-2026): equivalent treatment — prompt prefix (including tool/function definitions) is hashed as a unit; any change invalidates the cache.
- General caching literature (Fowler 2018 "Patterns of Enterprise Application Architecture"; Nygard 2007 "Release It!"): content-addressable caches require deterministic keying; inputs that affect the computation must be part of the key.
- LLM inference caching (Zhang et al. 2024 on KV-cache reuse; Liu et al. 2024 on prefix-caching correctness): tool definitions are part of the prompt prefix and must be stable; cache-hit under mutated tool schemas would be a correctness violation, not a performance win.
- No challenging evidence found: 15b NO-CHALLENGE-FOUND. The principle is canonical and universally applied.

**Challenges noted:**
- 15b NO-CHALLENGE-FOUND (literature is uniformly supportive).
- Caveat: "immutability" is a property the implementation must enforce; the premise does not free C2A2 from the responsibility of ensuring the tool-definition set is actually stable in practice. Drift in tool schemas (e.g., a silent SDK upgrade that reorders parameters) would still break caching.
- Caveat: tool-definition stability must be audited as part of pre-rollout smoke testing, paired with ASSUMPTION-054's byte-stability check.

**Confidence:** High

**Applicable to:**
- CACHING-ARCHITECTURE cluster design (direct commitment).
- Prompt-cache correctness gates: any caching layer must hash tool definitions as part of the prefix.
- Pairs with ASSUMPTION-054 (byte-stability smoke test) as the immutability-verification contract.
- Informs downstream rollout gates (2026-04-27 caching deployment): tool-definition drift detection must be in the pre-rollout audit.

**Re-check due:** 2026-07-20 (Quarterly)

**Status:** ACTIVE

**Rationale:**  
Clean convergence — strong support from vendor documentation (Anthropic, OpenAI) and general caching literature, with NO challenging evidence found by 15b. This is the canonical fast-path pattern: high-support + no-challenge + vendor-documented + technical correctness claim = INCORPORATE. The premise is also load-bearing for the 2026-04-27 caching rollout — without it, the caching architecture's correctness cannot be reasoned about.

**PROVENANCE:**
  Origin: 14b
  Chain: [14b → 15a, 15b → 15c]
  Current status: INCORPORATED

---

### PREMISE-008:
**Date validated:** 2026-04-21  
**Source item:** ASSUMPTION-056  
**Item type:** ASSUMPTION  

**Validated statement:**  
An honest null (zero proposals emitted with clear rejection reasons) is more valuable than thin or speculative proposals in specialist literature-monitoring tasks. Reporting nulls with explicit rejection rationale is methodologically correct practice and preferred to weak-evidence proposals that pad throughput at the cost of signal quality.

**Supporting evidence:**
- PRISMA systematic-review guidelines: transparent reporting of search results, including nulls with reasons, is canonical.
- Negative-results literature (Ioannidis 2005; Fanelli 2010 "Do pressures to publish increase scientists' bias?"): null reporting corrects file-drawer-style publication bias.
- Ship-and-iterate practice (Ries 2011; Agile): weak signals that flood downstream consumers degrade decision quality more than missing signals.
- Signal-to-noise calculus (Shannon 1948; information theory): increasing throughput at cost of signal quality is a net-negative for downstream inference.

**Challenges noted:**
- Self-assessment bias: specialists may classify convenient nulls as honest nulls; PRESUMPTION-067 flags the adjacency. Mitigated by filter-audit protocol (candidate DECISION-022 scope extension).
- Anchoring on honest-null framing may suppress genuine weak signals. Mitigated by explicit rejection-reason logging so filters can be audited.

**Confidence:** High (for the methodological principle; conditional on filter-audit protocol being in place per PREMISE-006 reflexive-application)

**Applicable to:**
- Specialist-slot output floor policy
- Agent 14a/14b briefing-layer design
- BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster governance
- Pairs with PRESUMPTION-067 REVISE (specialist self-eval adequate) — honest-null policy requires filter-audit to distinguish from convenient-null

**Re-check due:** 2026-07-21 (Quarterly)

**Status:** ACTIVE (with audit-protocol pairing note: PREMISE-008 is load-bearing under the assumption that specialist-layer filter audit exists; DECISION-022 scope extension satisfies this)

**Rationale:**  
Canonical methodological principle across systematic-review (PRISMA), publication-bias (Fanelli, Ioannidis), ship-and-iterate (Ries), and information-theoretic literature. 15a SUPPORTED Strong; 15b PARTIALLY-CHALLENGED Moderate on file-drawer / self-assessment bias — concerns are real but narrow and addressable via filter-audit protocol (PREMISE-006 reflexive, DECISION-022 scope). Second-of-two INCORPORATEs in the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster (PREMISE-006 + PREMISE-008).

**PROVENANCE:**
  Origin: 14a
  Chain: [14a → 15a, 15b → 15c]
  Current status: INCORPORATED

---

### PREMISE-009:
**Date validated:** 2026-04-21  
**Source item:** ASSUMPTION-059  
**Item type:** ASSUMPTION  

**Validated statement:**  
The evening cowork-to-chat sync scheduled task should not presume scheduler-override authority (firing 14a/14b manually is out-of-scope for an evening-sync role). Task-authority scope boundaries — each scheduled task operates within its declared responsibilities and does not invoke sibling pipelines — are the correct orchestration pattern.

**Supporting evidence:**
- Least-privilege / scope-boundary literature (Saltzer & Schroeder 1975; Microsoft STRIDE; OWASP): tasks should operate within declared authority; cross-task invocation requires explicit contract.
- Orchestrator-delegate separation (microservices patterns; Kubernetes operator design; Fowler 2014 "Microservices"): scheduled tasks should be delegate-role and not self-invoke sibling pipelines.
- Separation-of-concerns (Dijkstra 1974): simpler systems emerge when each component has a single responsibility; sync ≠ pipeline-invocation.

**Challenges noted:**
- Paired-escalation concern: limiting authority creates a fallback gap when the upstream pipeline stage doesn't run. Resolved by separating AUTHORITY (constrained by ASSUMPTION-059) from ESCALATION (alert-based per PRESUMPTION-064 REVISE / OPEN-034).
- Scope-floor correct for simplicity but leaves pipeline-absence handling to escalation layer rather than sibling-invocation.

**Confidence:** High

**Applicable to:**
- Scheduled-task architecture / task-authority scope contracts
- Orchestration design for multi-task pipelines
- Pairs with PRESUMPTION-064 and PRESUMPTION-069 REVISE dispositions: authority-constrained + escalation-equipped is the joint pattern
- Directly motivates OPEN-034 (alert-based remediation rather than sibling-invocation)

**Re-check due:** 2026-07-21 (Quarterly)

**Status:** ACTIVE

**Rationale:**  
Clean fast-path pattern — 15a SUPPORTED Strong + 15b NO-CHALLENGE-FOUND Weak (paired-escalation concern addresses authority vs. escalation separately). Canonical least-privilege and orchestrator-delegate design patterns converge unambiguously. The minor caveat (fallback-gap) is actually a reason for INCORPORATE plus paired remediation via OPEN-034, not a reason for MONITOR.

**PROVENANCE:**
  Origin: 14a
  Chain: [14a → 15a, 15b → 15c]
  Current status: INCORPORATED

---

### PREMISE-010:
**Date validated:** 2026-04-21  
**Source item:** ASSUMPTION-061  
**Item type:** ASSUMPTION (framework commitment)  

**Validated statement:**  
PREMISE-006 (transparent-flagging-over-silent-reconciliation) applies reflexively to the decisions-register pipeline — leaving validated premises outside the formal DECISION register is itself a form of silent reconciliation the senior commitment prohibits. The norm governs its own register.

**Supporting evidence:**
- Reflection-principle literature (Quine 1966 "Necessary Truth"; Carnap 1950 "Empiricism, Semantics, and Ontology"): principles that are not reflexive either encode a scope-bounding rationale or exhibit tangled-hierarchy failure.
- Dogfooding / eat-your-own-dog-food literature (Harrison 2006; Google/Microsoft engineering practice): systems should follow the policies they impose on others; exceptions require explicit justification.
- Internal-coherence heuristic (philosophy of language; Lewis 1975 "Languages and language"): consistent application of a norm across all instances within its declared scope is a baseline coherence requirement.

**Challenges noted:**
- Provenance caveat: the reflexive-application claim originated from Chat-side Claude endorsement, which is within the SELF-AWARENESS-META cluster's same-model-validation pattern (PRESUMPTION-060 STRONGLY-CHALLENGED). Addressed by recording this as a Claude-internal consistency claim rather than externally validated.
- Operational-load concern: reflexive application may grow the DECISION register faster than Tom can review. Addressed via phased scope: the NORM applies, but DECISION-022 (candidate) operationalizes the rendering to avoid overload.

**Confidence:** Moderate-to-High (high on the norm; moderate on the rendering operationalization)

**Applicable to:**
- BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster governance
- Candidate DECISION-022 (briefing-layer audit contract) — PREMISE-010 makes DECISION-022 a test-of-PREMISE-006 rather than a rendering-convention choice
- Operationalizes the SELF-AWARENESS-META cluster's internal-consistency layer

**Re-check due:** 2026-07-21 (Quarterly)

**Status:** ACTIVE (with operationalization note: reflexive application means every validated premise must enter the DECISION register; phasing may be required to avoid overload; provenance flagged as Claude-internal consistency claim)

**Rationale:**  
15a SUPPORTED Moderate-to-Strong; 15b NO-CHALLENGE-FOUND Weak. The norm is internally coherent; the challenges are about provenance and operationalization, not about the reflexive claim itself. Extends the BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster's INCORPORATE streak to 3 members (PREMISE-006, 008, 010). Note: this is the first INCORPORATE explicitly flagged as Claude-internal consistency rather than externally validated — the provenance acknowledgment is a new discipline introduced by today's run.

**PROVENANCE:**
  Origin: 14a
  Chain: [14a (inherits from PREMISE-006) → 15a, 15b → 15c]
  Current status: INCORPORATED

---

### PREMISE-011:
**Date validated:** 2026-04-21  
**Source item:** ASSUMPTION-062  
**Item type:** ASSUMPTION  

**Validated statement:**  
A weak circuit breaker beats none; pick an approximation threshold now and tune later — conditional on (a) the initial threshold being conservative, (b) instrumentation and a tuning cadence committed at ship time, (c) safety/financial/regulatory-critical thresholds excluded from this principle. The ship-and-iterate methodology is correct for non-safety-critical threshold decisions in C2A2.

**Supporting evidence:**
- Circuit-breaker design literature (Nygard 2007 "Release It!"; Netflix Hystrix): any circuit breaker is valuable; threshold is a tunable parameter.
- Worse-is-better (Gabriel 1991): simplicity and shippability beat theoretical optimality.
- Satisficing under bounded rationality (Simon 1956, 1979): picking a workable solution outperforms blocking on optimality under uncertainty.
- Ship-and-iterate (Ries 2011 "The Lean Startup"; Agile): approximation + instrumentation beats optimization + paralysis.
- SRE empirical tuning (Beyer 2016 on SLO selection): concrete thresholds matter less than having a threshold at all.

**Challenges noted:**
- Anchoring bias (Tversky & Kahneman 1974): initial approximations can stick; "tune later" is often "never tune" without instrumentation + cadence. Mitigated by the conditional (b).
- Threshold proliferation / alert fatigue (SRE): applying the principle indiscriminately produces a jungle. Mitigated by conditional (b) + a tune-me register.
- Safety/financial/regulatory-critical exceptions: ship-and-iterate is flatly wrong for these categories. Explicitly excluded by conditional (c).

**Confidence:** High (for the principle under the three operational conditions)

**Applicable to:**
- DECISION-024 (specialist-task turn-cap = 20 default) — PREMISE-011 directly supports the approximation-first approach.
- OPEN-032 (generalize transience-threshold across OPERATIONAL-DRIFT channels) — same methodology applies.
- OPEN-033 (specialist-task turn-cap infrastructure) — same methodology.
- Threshold decisions across C2A2 non-safety-critical layers: staleness, alert, retry caps.

**Re-check due:** 2026-07-21 (Quarterly)

**Status:** ACTIVE (with three operational conditions encoded as pre-ship checklist: conservative initial; instrumentation + tuning cadence; safety/financial/regulatory excluded)

**Rationale:**  
Clean fast-path — 15a SUPPORTED Strong across Nygard, Gabriel, Simon, Ries, SRE; 15b NO-CHALLENGE-FOUND Weak (cautions only, addressable via operational conditions). The three conditions render the principle load-bearing for DECISION-024 and generalizable across OPEN-032, OPEN-033, and staleness/alert thresholds. Second INCORPORATE today that directly enables an in-progress DECISION (PREMISE-011 → DECISION-024; PREMISE-010 → DECISION-022).

**PROVENANCE:**
  Origin: 14a
  Chain: [14a (Chat-side Claude endorsement) → 15a, 15b → 15c]
  Current status: INCORPORATED

---

## INCORPORATION SUMMARY

**Total premises incorporated:** 11  
**Total assumptions incorporated:** 11  
**Total presumptions incorporated:** 0  

**Status:** All incorporated premises are ACTIVE and available for use in C2A2 research, agent instruction sets, and system design decisions.

**Next review date:** 2026-05-13 (items with Monthly cadence)  
**Quarterly review dates:** 2026-07-13 (PREMISE-001, 003); 2026-07-18 (PREMISE-005); 2026-07-20 (PREMISE-006, 007); 2026-07-21 (PREMISE-008, 009, 010, 011)

**Afternoon top-up cycle note (2026-04-18):** PREMISE-005 (ASSUMPTION-040) is the first INCORPORATE disposition issued in an afternoon top-up cycle. Pattern: high-support + low-challenge + vendor-documented + low-stakes-if-wrong is the canonical fast-path to INCORPORATE.

**Daily cycle note (2026-04-20):** PREMISE-006 (ASSUMPTION-047) is the first INCORPORATE of a briefing-layer epistemic commitment (BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster). Same fast-path pattern as PREMISE-005 — strong convergence + weak challenge + aligns with prior scaffolding — but additionally acts as the senior commitment that resolves the paired ASSUMPTION-047 ↔ ASSUMPTION-048 tension surfaced by 15b.

**Supplementary Run 2 cycle note (2026-04-20):** PREMISE-007 (ASSUMPTION-051) is the first INCORPORATE from the CACHING-ARCHITECTURE cluster. Same fast-path pattern as PREMISE-005 and PREMISE-006 — strong vendor-documented support + NO-CHALLENGE-FOUND from 15b + technical correctness claim = canonical fast-path to INCORPORATE. Stands as the sole INCORPORATE from the 12-item supplementary Run 2; the remaining 11 items dispositioned as MONITOR (5) or REVISE (6), reflecting the cluster's high ratio of presumptions-to-assumptions (5 PRESUMPTION inferences vs. 6 stated ASSUMPTIONs) and correspondingly higher rate of unaudited design decisions.

**Daily cycle note (2026-04-21 — autonomous-task-layer principles day):** FOUR new INCORPORATEs in a single run — PREMISE-008 (ASSUMPTION-056 honest-null > thin), PREMISE-009 (ASSUMPTION-059 task-authority scope), PREMISE-010 (ASSUMPTION-061 reflexive PREMISE-006), PREMISE-011 (ASSUMPTION-062 weak-circuit-breaker-beats-none). This is the highest INCORPORATE density in any single 15c cycle to date. Pattern: the day's 14a items were overtly normative/methodological articulations of operating principles; the literature base for such principles (Nygard, Gabriel, Simon, Ries, PRISMA, Saltzer & Schroeder, Quine/Carnap) converges strongly. BRIEFING-LAYER-EPISTEMIC-COMMITMENTS cluster now has 3 INCORPORATEs (PREMISE-006, 008, 010). Notable: PREMISE-010 is the first INCORPORATE explicitly tagged as a Claude-internal consistency claim rather than externally validated — an honest provenance acknowledgment introduced today to address the SELF-AWARENESS-META cluster's same-model-validation concern.



---

## 2026-04-27 RUN — New Incorporated Premises

### PREMISE-012:
**Date validated:** 2026-04-27  
**Source item:** ASSUMPTION-068  
**Item type:** ASSUMPTION  

**Validated statement:**  
Master-wiki narrative gaps are surfaced as gaps rather than fabricated; this principle (PREMISE-006) extends to 4-day gap cases under a re-derivation note that escalation-tier discipline should be paired with the principle for gaps approaching the operationalized boundary.

**Supporting evidence:**
- SRE / operational-monitoring literature (Beyer et al. 2016)
- Incident-response literature (Allspaw 2009)
- Statistical-process-control (Shewhart 1931; Wheeler 1995)
- Knowledge-management staleness literature (Jennex 2007; Maier 2007)
- C2A2 internal precedent (PREMISE-006 4-day case)

**Challenges noted:**
- Alert-fatigue at scale (PRESUMPTION-077 monitored)
- Need for escalation-tier discipline at boundary cases

**Confidence:** Moderate (with explicit conditions)

**Applicable to:** Decisions and agents that depend on this premise; see provenance chain

**Re-check due:** 2026-07-27 (Quarterly via 15d)

**Status:** ACTIVE

**Rationale:** Re-affirmation of PREMISE-006 at 4-day scale; principle remains supported. Pair with escalation-tier discipline as PRESUMPTION-077 monitor. Update PREMISE-006 with 4-day case noted.

---

### PREMISE-013:
**Date validated:** 2026-04-27  
**Source item:** ASSUMPTION-069  
**Item type:** ASSUMPTION  

**Validated statement:**  
Proposal-ID collisions are flagged-and-rolled-forward (collision-detection-with-rename) rather than blocked-on, with the conditions that (a) collision rate stays low, (b) rename mappings are durably persisted, and (c) downstream consumers can follow renames.

**Supporting evidence:**
- CRDTs literature (Shapiro et al. 2011)
- Git branch-collision handling (Chacon & Straub 'Pro Git')
- Continuous-deployment roll-forward pattern (Humble & Farley 2010)
- C2A2 operational record (two same-day instances 2026-04-27)

**Challenges noted:**
- Pattern degrades at high collision rates (scaling concern)
- Durable persistence of rename map required
- External-citation rot if renames not followed

**Confidence:** Moderate (with explicit conditions)

**Applicable to:** Decisions and agents that depend on this premise; see provenance chain

**Re-check due:** 2026-07-27 (Quarterly via 15d)

**Status:** ACTIVE

**Rationale:** Flag-and-roll-forward is well-supported at current scale. Caveats on durable mapping and scaling-rate monitoring should be encoded as conditions on the premise.

---

### PREMISE-014:
**Date validated:** 2026-04-28  
**Source item:** ASSUMPTION-076  
**Item type:** ASSUMPTION  

**Validated statement:**  
PRS triplets are Tom's authorial re-description of traditions, not the traditions' self-voice. The author-as-aggregator framing is the methodologically honest position for cross-tradition synthesis, supported across intellectual history (MacIntyre, Skinner, Bevir), philosophy of science (Kuhn), and philosophy of language (Quine).

**Supporting evidence:**
- MacIntyre (1988) "Whose Justice? Which Rationality?" — tradition-narrator role
- Kuhn (1962) — solved-problem re-description as canonical synthesizer move
- Skinner (1969); Bevir (1999) — agent-meaning vs interpretive-meaning
- Quine (1960) — radical-translation under-determination

**Challenges noted:**
- Acknowledgment is necessary but not sufficient — author-frame propagates downstream regardless (Said 1978; Skinner 2002)
- Propagation gap to per-tradition wiki files surfaced separately as PRESUMPTION-088 (REVISE-flagged)
- Recursive-specialist-reading risk surfaced separately as PRESUMPTION-089 (REVISE-flagged)
- The 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074, specialist-recognition reliability) compounds with the propagation gap

**Confidence:** Moderate (with explicit conditions on propagation)

**Applicable to:**
- All cross-tradition synthesis outputs (PRS triplets, master-wiki narratives, specialist agent prompts)
- Any document or downstream artifact that references PRS framings
- Tied to ASSUMPTION-067 ground; relates to OPEN-037 Stump tension; structural to candidate DECISION-025

**Re-check due:** 2026-07-28 (Quarterly via 15d)

**Status:** ACTIVE (with propagation caveat)

**Rationale:** The author-as-aggregator framing is the dominant methodological recommendation across intellectual history and philosophy of language; ASSUMPTION-076's explicit acknowledgment aligns with this position. However, INCORPORATE is conditioned on the propagation gap (PRESUMPTION-088) and recursive-reading risk (PRESUMPTION-089) being addressed via separate REVISE actions. The premise is INCORPORATEd as the master-document position; per-tradition propagation and specialist-prompt disambiguation are the load-bearing follow-ups.

---


## 2026-05-11 RUN — New Incorporated Premises

### PREMISE-015:
**Date validated:** 2026-05-11  
**Source item:** ASSUMPTION-105  
**Item type:** ASSUMPTION  

**Validated statement:**  
User-privacy rules prohibit password-based login by software agents on the user's behalf; password delegation is out-of-pattern for "something you know" credentials. Token-based delegation (OAuth 2.0 / OIDC) is the canonical alternative path for legitimate cross-service action. Treating user-privacy rules as a binding operating constraint — and surfacing the constraint when it interacts with a workflow that does not accommodate it — is the literature-endorsed posture.

**Supporting evidence:**
- NIST SP 800-63B (2017, rev. 2020) "Digital Identity Guidelines" — password delegation out-of-pattern
- OWASP ASVS v4.0.3 §2.1 — passwords must not be exposed to or handled by intermediary services
- Bonneau, Herley, van Oorschot, Stajano (2012) "The Quest to Replace Passwords" IEEE S&P
- Hardt (2012) RFC 6749 OAuth 2.0 — consent-based token delegation as canonical alternative
- Anthropic Acceptable Use Policy and Claude Usage Policies (as in effect 2026) — Claude must not collect, store, or use end-user authentication credentials

**Challenges noted:**
- The constraint itself is not challenged by any literature surfaced
- The framing-without-paired-remediation posture is partially challenged (15b): surfacing the constraint as a "cause of failure" without committing to workflow redesign is documentation-as-fix (PRESUMPTION-122 cluster)
- 5th-consecutive recurrence is evidence the workflow has not been redesigned around the binding constraint — challenge applies to the workflow stagnation, not the constraint
- Hick (2018) "Friction" — repeated failure attribution to "constraint" without redesigning around it is a documented avoidance pattern

**Confidence:** High (for the constraint itself); Moderate (for the operational posture, conditional on paired workflow redesign)

**Applicable to:**
- All Claude agent actions that would otherwise require user password handling
- The evening-sync-delivery workflow that has shown 5-consecutive failures under the constraint
- Any future workflow design that touches credential-bearing flows
- Architectural commitments around delegation: ASSUMPTION-079 (delegation-via-token only); DECISION-022 (no-credential-handling boundary) — this premise is the operational confirmation

**Re-check due:** 2026-08-11 (Quarterly via 15d — credential-handling policy and Anthropic platform terms are stable, so quarterly review is sufficient)

**Status:** ACTIVE (with explicit operational caveat: this is a binding constraint, not a remediation. The workflow that surfaced it must be redesigned around token-based delegation; otherwise the 5+ consecutive recurrences become a documented stagnation pattern that would trigger separate REVISE action.)

**Rationale:** The user-privacy / no-password-delegation constraint is unambiguously endorsed across canonical authentication literature (NIST, OWASP, Bonneau et al.) and is the operating Anthropic policy. The 15a result is SUPPORTED (Strong); 15b found no challenge to the constraint itself and only weak challenge to the framing-without-remediation posture. Per the 15c heuristic, "15a strong support + 15b weak challenge → lean INCORPORATE with caveats noted" — this is the canonical INCORPORATE case. The caveat is operational: INCORPORATEing the constraint commits the system to redesigning the failing workflow around token-based delegation (OAuth Connector or equivalent), not to relaxing the constraint. The 5th-consecutive recurrence is the operational signal that the workflow redesign is itself an outstanding action item. **Significance for the pipeline:** this is the first INCORPORATE in two consecutive single-day-drain cycles (2026-05-09 and 2026-05-10 both produced 0 INCORPORATE) — the pattern that ASSUMPTION-112 SELF-MEASUREMENT cluster predicted is partially broken by this cycle, providing useful counter-evidence to the recursive-confirmation framing.

---

