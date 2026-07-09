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

**Re-check due:** 2026-08-02 (Monthly) [re-checked by 15d 2026-07-05; re-confirmed ACTIVE by 15c 2026-07-06, DISPOSITION-408 — new caveats: per-space similarity calibration required; control document length (embedding collapse)]

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

**Re-check due:** 2026-08-02 (Monthly — monitor independence of C2A2 findings) [re-checked by 15d 2026-07-05; re-confirmed ACTIVE by 15c 2026-07-06, DISPOSITION-409 — independence proviso sharpened: correlated LLM errors (Kim et al. ICML 2025) mean same-model-family convergence is NOT independent evidence; count same-mechanism/same-family lines as one; binds REVISE-174]

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


## 2026-05-13 RUN — No new INCORPORATE items

The 2026-05-13 c2a2-lit-search-pipeline run produced **0 INCORPORATE** out of 16 dispositioned items (4 MONITOR + 12 REVISE). No additions to the validated-premises register this cycle.

**Self-referential signal:** PRESUMPTION-148 (this cycle, REVISE) flagged the SELF-MEASUREMENT cluster's third-layer recurrence at the proposal-queue-depth layer; this cycle's 0% INCORPORATE rate re-instates the pattern that ASSUMPTION-112 (MONITOR-114) named as the cluster signature. The 2026-05-11 cycle broke the pattern at 1/21 (4.8%); the 2026-05-13 cycle returns it to 0/16. Across the four-cycle window (2026-05-09, 2026-05-10, 2026-05-11, 2026-05-13), INCORPORATE rate is 1/66 (1.5%) — the cluster pattern's recurrence is now structurally well-observed.

**Cycle-level observation on the register:** the validated-premises register has not received new entries in three of the last four cycles. The structural concern is whether the disposition-criteria are calibrated correctly: if the criteria are correct, the upstream 14a/14b extractions are producing well-formed-but-still-not-validation-ready items; if the criteria are too strict, the register is starving and downstream commitments lack canonical premise grounding. Joint with PRESUMPTION-148 cluster — the proposal-queue and the premise-register are both at-risk of intake-vs-disposition imbalance under different framings.

**Items closest to INCORPORATE this cycle (but not crossed):** ASSUMPTION-118 (15a SUPPORTED Strong; gated on PRESUMPTION-134 substrate-decomposition + PRESUMPTION-145 redesign-vs-discard comparison). If substrate-decomposition is performed and the cost-benefit comparison is documented before the next 15d review (2026-05-20), MONITOR-122 may transition to INCORPORATE on that schedule.

---


## 2026-05-14 RUN — 4 INCORPORATE items (PREMISE-016 through PREMISE-019)

The 2026-05-14 c2a2-lit-search-pipeline run produced **4 INCORPORATE** out of 30 dispositioned items (13.3% — first non-zero INCORPORATE cycle since 2026-05-11; the 2026-05-13 cycle produced 0). The 17-pathway architectural articulation pass surfaced four assumptions with strong canonical literature backing.

---

### PREMISE-016:
**Date validated:** 2026-05-14
**Source item:** ASSUMPTION-120
**Item type:** ASSUMPTION

**Validated statement:**
Cloudflare Workers is an appropriate broker hosting platform for C2A2 streaming-LLM/TTS workloads, conditional on streaming-latency validation. The ~5-30 ms edge overhead reported in Cloudflare's published benchmarks is dwarfed by LLM streaming first-token latency floors (200-800 ms) and TTS first-audio floors (150-400 ms). The platform is the canonical edge-broker for stateless request-response workloads.

**Supporting evidence:**
- Cloudflare Workers documentation and published benchmarks (2024-2025) — sub-50 ms cold-start, ~5-15 ms warm-path edge overhead
- OpenAI / Anthropic streaming API published latency floors (200-800 ms first-token)
- ElevenLabs / Cartesia TTS streaming benchmarks (150-400 ms first-audio)
- Fielding (2000) REST dissertation; Burns et al. (2016) "Designing Distributed Systems" — edge placement canonical for stateless brokers
- C2A2-internal: PREMISE-008 substrate-edge alignment principle

**Challenges noted:**
- p99 tail-latency under load may differ substantially from median (median-case benchmark concern)
- Workers-specific lock-in (Durable Objects, KV, Worker APIs) creates migration cost
- WebSocket time limits and Durable Objects pricing introduce non-trivial constraints
- PRESUMPTION-152 (paired, MONITOR-131) — estimate-without-measurement gate

**Confidence:** Moderate (conditional-on-validation framing is load-bearing)

**Applicable to:**
- Broker hosting decision for ISME demo and beyond
- Streaming-LLM dispatch path
- TTS streaming path
- Any C2A2 stateless request-response component at the edge

**Re-check due:** 2026-08-14 (Quarterly via 15d — platform performance is empirically stable; quarterly review sufficient)

**Status:** ACTIVE (with explicit operational caveat: deployment requires p50/p95/p99 latency validation under realistic voice-dialogue load; portable-broker abstraction recommended to preserve reversibility)

**Rationale:** 15a SUPPORTED Strong; 15b PARTIALLY-CHALLENGED Moderate. Per heuristic: "15a strong support + 15b weak-moderate challenge → lean INCORPORATE with caveats noted" — canonical INCORPORATE case. The conditional clause in ASSUMPTION-120 itself preserves the right epistemic posture. Caveats become the load-bearing implementation discipline (p99 measurement, portable abstraction).

---

### PREMISE-017:
**Date validated:** 2026-05-14
**Source item:** ASSUMPTION-124
**Item type:** ASSUMPTION

**Validated statement:**
The generative-canvas library set (D3 + three.js + Plotly + bare canvas/WebGL) covers the canonical 2026 web-visualization landscape — declarative analytics (Plotly), low-level web grammar (D3), 3D/WebGL (three.js), and bare-metal canvas/WebGL for performance edges. The choice is field-tested and consistent with C2A2-internal production precedent (wiki_narration.html D3 v7).

**Supporting evidence:**
- Bostock (2011-2024) D3.js documentation and case studies — canonical low-level web visualization grammar
- three.js + WebGL community (2010-2025) — dominant high-level WebGL library
- Plotly community benchmarks (2023-2025) — production analytics dashboards
- State of JS / State of Frontend 2024-2025 surveys — chosen libraries are first-tier
- C2A2-internal wiki_narration.html (D3 v7) — production precedent

**Challenges noted:**
- LLM-codegen surface is larger than necessary (Vega-Lite or Observable Plot would reduce error rate for typical plots)
- Library-set sizing concern — four libraries multiply bundle and complexity
- deck.gl may subsume bare-WebGL for geo / large-data
- PRESUMPTION-157 (paired, MONITOR-136) — alternatives comparison gap

**Confidence:** High

**Applicable to:**
- Pathway 05 whiteboard plots
- All generative-visualization codegen paths
- C2A2 dashboard and reporting surfaces

**Re-check due:** 2026-11-14 (Quarterly via 15d — library ecosystem is stable; longer re-check appropriate)

**Status:** ACTIVE (with explicit operational caveat: library-set comparison audit recommended via PRESUMPTION-157 MONITOR-136; additive selection of Vega-Lite / Observable Plot for LLM-codegen-heavy paths may be considered without disturbing core)

**Rationale:** 15a SUPPORTED Strong; 15b PARTIALLY-CHALLENGED Moderate. Library landscape is mature and choice is conservative. Challenges target LLM-codegen optimization rather than catalog validity — addressable as caveats. Heuristic: strong support + moderate challenge → INCORPORATE with caveats.

---

### PREMISE-018:
**Date validated:** 2026-05-14
**Source item:** ASSUMPTION-129
**Item type:** ASSUMPTION

**Validated statement:**
Nightly alignment-agent unidirectional sync from authoritative `architecture/` ground-truth to derivative `wiki/Architecture/` mirror, with diff-detection and flag-on-drift, is the appropriate pattern when the single-writer invariant is enforced. The pattern parallels Summa `sync_vault.sh` + launchd C2A2-internal precedent and is consistent with canonical unidirectional-sync practice (git/rsync/Lamport).

**Supporting evidence:**
- Git / rsync / unison documentation — canonical unidirectional sync with diff + overwrite under single-writer
- Allspaw & Robbins (2010) "Web Operations" — declared ground-truth + scheduled sync is the resilient pattern for derivative invariants
- Lamport (1978) — single-writer invariant is the correctness condition
- Obsidian-syncthing community patterns (2023-2025) — vault-mirror sync with conflict-flag-on-drift
- C2A2-internal: Summa `sync_vault.sh` + launchd precedent

**Challenges noted:**
- Mirror-side edits could occur via direct editing or other agents (PRESUMPTION-162, paired, MONITOR-139)
- Silent overwrite is canonical failure mode if single-writer invariant is not enforced
- "Flag in next session archive" surfaces problem after the fact

**Confidence:** Moderate-High (conditional on single-writer enforcement)

**Applicable to:**
- Alignment-agent sync protocol
- Any architecture/wiki sync pair
- Generalizable to other ground-truth/mirror invariants

**Re-check due:** 2026-08-14 (Quarterly via 15d)

**Status:** ACTIVE (with explicit operational caveat: single-writer invariant must be technically enforced — filesystem read-only on mirror, or pre-overwrite diff with confirmation, or alternative protection. The "flag in next session archive" is not sufficient on its own.)

**Rationale:** 15a SUPPORTED Strong; 15b PARTIALLY-CHALLENGED Moderate. Architecture is canonical under its precondition; precondition is the load-bearing implementation discipline. Heuristic: strong support + moderate challenge → INCORPORATE with caveats.

---

### PREMISE-019:
**Date validated:** 2026-05-14
**Source item:** ASSUMPTION-130
**Item type:** ASSUMPTION

**Validated statement:**
The honesty layer (Pathway 14) is a first-class architectural commitment of C2A2: epistemic-status marks on claims are surfaced as a primary affordance, not buried in footers. The commitment aligns with IPCC scientific-uncertainty conventions, responsible-AI model-card practice, Tufte's data-graphics conventions, and Floridi/Nguyen on epistemic transparency.

**Supporting evidence:**
- IPCC AR5+ uncertainty-marking guidance — confidence/likelihood markers are first-class in canonical scientific reporting
- Anthropic / OpenAI model-card practices (2023-2025) — surfacing uncertainty is dominant pattern in responsible AI output
- Tufte (1990, 2006) — visibility of provenance and uncertainty is a design virtue
- Floridi (2013), Nguyen (2020) — visible epistemic status is load-bearing for epistemic responsibility
- C2A2-internal: PROVENANCE header protocol (already-validated first-class commitment pattern)

**Challenges noted:**
- Universal first-class marking can produce over-saturation invisibility / warning-blindness (alarm-fatigue concern, PRESUMPTION-163, paired, MONITOR-140)
- "First-class" is ambiguous — must distinguish "available and prominent where relevant" from "uniformly emphasized on every claim"
- Graduated marking (high-confidence default-unmarked, deviations emphasized) is the canonical safety-engineering compromise

**Confidence:** High (for commitment-class designation); Moderate (for implementation — graduated marking required)

**Applicable to:**
- Pathway 14 honesty-layer design
- All C2A2 output surfaces (chat, narration, reports, wiki)
- Decision records and operational claims
- Generalizable to other epistemic-transparency commitments

**Re-check due:** 2026-08-14 (Quarterly via 15d)

**Status:** ACTIVE (with explicit operational caveat: implementation must be graduated — high-confidence claims default-unmarked, deviations emphasized — to avoid over-saturation invisibility. Universal-emphasis implementation would not satisfy the commitment, despite appearing to honor it.)

**Rationale:** 15a SUPPORTED Strong; 15b PARTIALLY-CHALLENGED Moderate. The challenge targets implementation uniformity, not commitment-class. Graduated marking captures the intent with better attention economics. Heuristic: strong support + moderate challenge → INCORPORATE with caveats.

---

**Cycle-level observation:** the 2026-05-14 cycle produced 4 INCORPORATEs — the first non-zero cycle since 2026-05-11 — and breaks the SELF-MEASUREMENT Goodhart cluster pattern that recurred across 4 of the last 5 cycles. The 17-pathway architectural articulation pass surfaced four items with strong canonical literature backing (broker hosting, library set, sync protocol, honesty layer). Pre-implementation architectural articulation passes are predicted to be more INCORPORATE-likely than operational-incident passes; this prediction is supported by the cycle data.

---

### PREMISE-020:
**Date validated:** 2026-05-15
**Source item:** ASSUMPTION-132
**Item type:** ASSUMPTION

**Validated statement:**
Toolkit / content separation (Pathway 18) is a first-class architectural commitment for the C2A2 toolkit-extraction work: the framework / content seam must be designed cleanly enough that the parameterizable subset of content can be swapped without code modification. This commitment is load-bearing for the 18 → 25 portability arc; the seam is canonical software engineering practice (Parnas information-hiding; MVC; FLOSS framework precedent).

**Supporting evidence:**
- Parnas (1972) "On the Criteria to Be Used in Decomposing Systems into Modules" — canonical information-hiding formulation
- Reenskaug (1979) MVC and successors — 40+ year canonical pattern for framework/content separation
- Hunt & Thomas (1999) "The Pragmatic Programmer" — DRY and orthogonality
- Fowler (2003) "Patterns of Enterprise Application Architecture" — separation of concerns
- FLOSS precedents: Django, Rails, Hugo, Apache Wicket — successful toolkit-extractions maintained the seam

**Challenges noted:**
- Brooks (1986) "No Silver Bullet" — essential complexity (e.g., tradition-specific reasoning) resists clean extraction into reusable primitives; some content is method, not data
- Brooks (1995) — second-system effect: toolkit-from-demonstration extraction can over-generalize and misidentify what was load-bearing in the original
- C2A2-specific: honesty layer, lattice methodology, and tradition agents contain essential-complexity content that may not parameterize fully (PRESUMPTION challenge, paired audit recommended)

**Confidence:** High (for commitment-class designation); Moderate (for the universal "swap without touching code" framing — requires essential-complexity carve-out)

**Applicable to:**
- Pathway 18 toolkit extraction
- Pathways 19-22 portability arc (federation/institutional/departmental/individual)
- All future framework/content boundaries in C2A2

**Re-check due:** 2026-08-15 (Quarterly via 15d; load-bearing for portability arc and tied to Pathway 18 implementation milestone)

**Status:** ACTIVE (with explicit operational caveat: distinguish "content as data" — parameterizable, swappable — from "content as method" — extension-point-based, requires authorship not configuration. Pathway 18 must document the essential-complexity carve-out explicitly. "Non-optional" applies to the seam; "swap without touching code" applies only to the parameterizable subset.)

**Rationale:** 15a SUPPORTED Strong (50+ years of canonical separation-of-concerns literature; multiple FLOSS framework precedents); 15b PARTIALLY-CHALLENGED Moderate (essential-complexity content resists parameterization; second-system extraction risks). Heuristic: strong support + moderate challenge → INCORPORATE with caveats. The challenge targets the universal "swap without touching code" framing, not the commitment to the seam.

---

### PREMISE-021:
**Date validated:** 2026-05-15
**Source item:** ASSUMPTION-134
**Item type:** ASSUMPTION

**Validated statement:**
C2A2's federation pattern defaults to OFF with selective per-topic per-peer sharing and attribution-by-default. The "structural not aspirational" framing is implemented as default-OFF (enforced in code) plus attribution-by-default with violation-defederation (rather than the over-strong "mandatory attribution" claim). The commitment aligns with W3C ActivityPub / Verifiable Credentials patterns, GDPR data-minimization, FAIR academic-data sharing, and Nudge default-design.

**Supporting evidence:**
- Thaler & Sunstein (2008) "Nudge" — defaults have outsized adoption effect; opt-in defaults preserve agency
- ActivityPub / Mastodon (W3C 2018) — canonical fediverse default-off + per-instance allowlist precedent
- Academic data-sharing (DataONE, ICPSR, FAIR principles) — default-off with explicit opt-in per dataset
- W3C Verifiable Credentials 2.0 (2025) — selective disclosure with attribution
- GDPR Article 5 — opt-in attribution as privacy-preserving default
- Norman (2013) — "structural not aspirational" matches affordance-design literature

**Challenges noted:**
- "Mandatory attribution" cannot be technically enforced beyond originating instance (ActivityPub, Creative Commons, GDPR enforcement records all show attribution-loss is the norm at multi-hop federation)
- Default-off can produce under-federation if not paired with opt-in affordances
- Per-topic per-peer granularity has UI complexity cost
- Selective disclosure preserves the originating signature but cannot prevent downstream re-publication without attribution

**Confidence:** High (for default-off commitment); Moderate (for attribution implementation — must be "attribution-by-default + violation-defederation" rather than "mandatory attribution")

**Applicable to:**
- Pathway 19 federation
- Pathway 20-22 institutional/departmental/individual deployment
- All cross-instance content exchange

**Re-check due:** 2026-08-15 (Quarterly via 15d)

**Status:** ACTIVE (with explicit operational caveat: reframe "mandatory attribution" as "attribution-by-default + violation-defederation"; adopt W3C VC linked-data proofs to preserve attribution across hops; document defederation policy for attribution violations; pair with PRESUMPTION-paired audit items).

**Rationale:** 15a SUPPORTED Strong (multiple converging literatures: behavioral economics, W3C standards, academic data-sharing, GDPR, affordance design); 15b PARTIALLY-CHALLENGED Moderate (attribution enforceability is limited beyond originating instance). Heuristic: strong support + moderate challenge → INCORPORATE with caveats.

---

### PREMISE-022:
**Date validated:** 2026-05-15
**Source item:** ASSUMPTION-135
**Item type:** ASSUMPTION

**Validated statement:**
Meta-crafts (governance, project management, conflict resolution, facilitation, evaluation) are committed as first-class traditions in C2A2's perspective lattice, not as policy layers external to substantive traditions. The commitment aligns with MacIntyre's tradition-as-practice framework, Ostrom's empirical governance studies, Dewey's evaluation-as-inquiry, Habermas's communicative-action, and Schwartzman's facilitation-as-craft.

**Supporting evidence:**
- MacIntyre (1981) "After Virtue" and (1988) "Whose Justice? Which Rationality?" — practices and traditions are first-class; politics-as-tradition argument is canonical
- Ostrom (1990) "Governing the Commons" — empirical demonstration that commons-governance is a tradition with substantive content (8 design principles)
- Dewey (1916, 1929) — evaluation is itself a substantive inquiry tradition, not external scoring
- Habermas (1981) "Theory of Communicative Action" — communicative practices are constitutive
- Schwartzman (1986) "The Meeting" — facilitation as substantive craft
- C2A2-internal: aligns with MacIntyre lineage commitment

**Challenges noted:**
- Substantive/meta-craft boundary is contested (Schatzki, Bourdieu, Stout): practice theory denies the sharp boundary; the distinction is constituted, not given
- Boundary cases (theology, political philosophy) are foundational tensions, not boundary-case-handling (PRESUMPTION-171, paired)
- Adding meta-craft traditions expands lattice coordination cost
- Recursive load (PRESUMPTION-180) — meta-crafts are reflective on substantive crafts, generating recursion that compounds

**Confidence:** High (for first-class commitment); Moderate (for sharp boundary — must accept that the distinction is constituted and requires ongoing arbitration)

**Applicable to:**
- Pathway 24 governance commitments
- Perspective lattice composition
- All meta-craft inclusion decisions

**Re-check due:** 2026-08-15 (Quarterly via 15d)

**Status:** ACTIVE (with explicit operational caveat: the substantive/meta-craft distinction is constituted, not given. Implementation must accommodate boundary cases — theology, political philosophy — as foundational tensions rather than treating them as exceptions. PRESUMPTION-171 paired audit recommended. Recursive load from meta-craft reflection must be bounded; PRESUMPTION-180 cluster carry-forward.)

**Rationale:** 15a SUPPORTED Strong (multiple converging philosophical traditions: MacIntyre, Ostrom, Dewey, Habermas); 15b PARTIALLY-CHALLENGED Moderate (boundary cases contested in practice theory; recursive load real). Heuristic: strong support + moderate challenge → INCORPORATE with caveats. The challenge targets boundary-sharpness, not commitment-class.

---

**Cycle-level observation:** the 2026-05-15 cycle produced 3 INCORPORATEs (ASSUMPTION-132 toolkit/content separation; ASSUMPTION-134 federation default-OFF; ASSUMPTION-135 meta-crafts first-class) — second consecutive non-zero INCORPORATE cycle. Across the six-cycle window (2026-05-09 / 10 / 11 / 13 / 14 / 15), the INCORPORATE rate is now 8/125 (6.4%); the 2026-05-14 and 2026-05-15 cycles together contribute 7 of the 8. Both cycles were driven by architectural-articulation passes (17-pathway pass on 05-13 EOD; breadth-arc 18-25 pass on 05-14 EOD). The pattern that pre-implementation architectural articulation passes are more INCORPORATE-likely than operational-incident passes is now confirmed across two cycles.

---



---

## 2026-05-18 cycle additions (5 INCORPORATE items)

Five new premises validated from the 2026-05-17 cohort, all clustered around the Path-2 worker architecture (vault-safety-boundary cluster) plus the missed-cycle/ownership-boundary documentation pair. This is the largest single-cycle infrastructure-grounding event since 2026-05-15.

---

### PREMISE-023:
**Date validated:** 2026-05-18
**Source item:** ASSUMPTION-158
**Item type:** ASSUMPTION

**Validated statement:**
Folder-as-queue + worker-script is an acceptable integration architecture for adding a non-Claude LLM agent to the C2A2 vault at the current scale (N=1 worker, batch latency tolerance). The pattern is canonical at this scale; operational-maturity gaps will surface at the boundaries (multi-producer, contention) and are tracked under PRESUMPTION-183.

**Supporting evidence:**
- Inbox/Outbox pattern (Wikipedia; Jovanović 2023, milanjovanovic.tech) — file-/table-based queues with at-least-once semantics are a mature integration pattern for decoupling producers and consumers.
- Alaiy (Medium 2024) 'How I Taught My LLM to Queue Up and Chill' — explicit working pattern of LLM-as-row-processor pulling from a queue (SQS analog); validates the LLM-worker-from-queue topology.
- SoftwareMill 'Microservices 101: Transactional Outbox and Inbox' — confirms queue-based decoupling is preferred over in-process tool-call coupling for heterogeneous-runtime workers.

**Challenges noted:** The chosen-architecture claim is supportable at the topology level but vulnerable on operational-maturity grounds. Production queue services exist precisely because rolling-your-own queue surfaces predictable failure modes (lost messages, double-processing, ordering, visibility timeouts) that file-folder coordination cannot natively address. The 'Path 2 chosen' decision optimizes for inspection-and-simplicity over operational robustness — a tradeoff the literature considers defensible at small N but suboptimal at scale.

**Confidence:** Moderate

**Applicable to:** DECISION-036 (candidate); Path-2 worker; non-Claude LLM integrations; any folder-queue-based agent pattern across C2A2

**Re-check due:** 2026-08-18 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a PARTIALLY-SUPPORTED (Moderate); 15b PARTIALLY-CHALLENGED (Moderate). Heuristic application: Topology has Strong literature support; operational caveats are real but addressable within scope (one producer, vault-safety boundary). The decision is well-bounded; INCORPORATE with explicit scope-and-scale conditions noted.

---

### PREMISE-024:
**Date validated:** 2026-05-18
**Source item:** ASSUMPTION-160
**Item type:** ASSUMPTION

**Validated statement:**
Filesystem-scope-locking of worker agents to dedicated inbox/outbox/done/failed folders with Maildir-style naming is a canonical, well-grounded vault-safety boundary. The pattern aligns with mainstream agent-sandboxing literature (Cursor, Bunnyshell, Vercel) and proven file-coordination conventions (Maildir). Full safety requires complementary boundaries (network, resource, process) tracked separately.

**Supporting evidence:**
- Cursor 'Implementing a secure sandbox for local agents' (cursor.com/blog/agent-sandboxing) — filesystem boundary is the first and most cited principle of agent sandboxing.
- Bunnyshell 'Coding Agent Sandbox' guide — isolated filesystem, least-privilege scope, ephemeral lifecycle as canonical components.
- Vercel 'Security boundaries in agentic architectures' — explicit treatment of scope-locking and write-permission narrowing.
- Penligent 'Sandboxes for Coding Agents' — independent confirmation that filesystem-scope is the primary safety boundary.
- Maildir specification (Bernstein, qmail/courier-mta lineage) — well-documented file-naming convention with atomic-delivery properties.

**Challenges noted:** None of substance; see _against.md file.

**Confidence:** High

**Applicable to:** DECISION-036; all worker-agent designs in C2A2; vault-safety boundary cluster; any non-Claude LLM integration

**Re-check due:** 2026-08-18 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b NO-CHALLENGE-FOUND (None). Heuristic application: Strong literature support, no credible challenge to the core commitment. The boundary is well-grounded and aligns with canonical sandboxing practice. Incorporate; track related boundaries (network, resource, credentials) as separate items.

---

### PREMISE-025:
**Date validated:** 2026-05-18
**Source item:** ASSUMPTION-165
**Item type:** ASSUMPTION

**Validated statement:**
c2a2-self-awareness-daily missed 2 consecutive cycles on 2026-05-15 and 2026-05-16; the 3-consecutive on-cadence streak was broken; the 2026-05-17 run was the resumption. The operational fact is documented and load-bearing for OPEN-047; the cause-classification (pipeline-failure vs. rate-mismatch) is a separate question handled under PRESUMPTION-187.

**Supporting evidence:**
- Shaped 'Best Practices in Data Ingestion' — explicit identification that scheduled-task misses are first-line indicators of pipeline-state problems requiring classification.
- Microsoft 'Pipeline failure and error message' (Azure Data Factory) — operational guidance that missed cycles must be classified before resolution, not assumed.
- Beyer et al. (2016) SRE Book — 'visibility-of-stall' is the first SRE objective; documented misses with timestamps is the canonical form.
- C2A2-internal: documented timestamps make the claim falsifiable and audit-friendly.

**Challenges noted:** None of substance; see _against.md file.

**Confidence:** High

**Applicable to:** OPEN-047; pipeline-reliability audit; substrate-decomposition cluster; pipeline-fault-classification protocol

**Re-check due:** 2026-08-02 (Monthly) [re-confirmed ACTIVE by 15c 2026-07-06, DISPOSITION-410 — caveats: time-box classification ahead of reversible fixes; severity-filter miss alerts (2026 alert-fatigue data)]

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b NO-CHALLENGE-FOUND (None). Heuristic application: Documented operational fact; well-grounded in SRE-style reporting. The inferential framing question is handled separately (PRESUMPTION-187). Incorporate the fact; classify the cause separately.

---

### PREMISE-026:
**Date validated:** 2026-05-18
**Source item:** ASSUMPTION-167
**Item type:** ASSUMPTION

**Validated statement:**
Long-unowned RE-TRIGGER cohorts in C2A2 should be classified as ownership-boundary problems (unassigned accountability), not item-ageing problems (items getting stale). This reframe aligns with mainstream data-pipeline-reliability literature on ownership gaps; remediation requires owner assignment, not item-by-item action.

**Supporting evidence:**
- Extract.to 'Why your data pipeline keeps breaking' — explicit identification of unclear ownership as the root cause of pipeline fragility.
- Astronomer 'Data Products: It's not what you call them' — 'every dataset should have an owner. When you depend on someone else's table, you should know who to contact when it changes.' Direct parallel to unowned-cohort situation.
- Closeloop 'Why Data Pipelines Fail and How Enterprise Teams Fix Them' — emphasizes that organizational and ownership gaps, not just technical issues, are the root causes of pipeline fragility.

**Challenges noted:** None of substance; see _against.md file.

**Confidence:** High

**Applicable to:** OPEN-046; cohort-ownership protocol; substrate-decomposition cluster; any long-running unowned queue across C2A2 pipelines

**Re-check due:** 2026-08-18 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b NO-CHALLENGE-FOUND (None). Heuristic application: Reframe is strongly supported by data-pipeline-ownership literature. No credible challenge. Incorporate the reframe; OPEN-046 tracks the follow-through.

---

### PREMISE-027:
**Date validated:** 2026-05-18
**Source item:** ASSUMPTION-170
**Item type:** ASSUMPTION

**Validated statement:**
The five hard prohibitions codified in agents.md (write outside scope; delete without confirmation; edit without read; silent conflict-merge; skip failure-logging) constitute a well-grounded canonical set of vault-safety-boundary primitives, aligned with mainstream agent-sandboxing literature (Cursor, Bunnyshell, Vercel, OpenAI). The set is necessary but not sufficient; additional boundaries (network, resource, credentials) round out a complete safety posture.

**Supporting evidence:**
- Cursor 'Implementing a secure sandbox for local agents' — explicit list of must-have boundaries for coding agents: scope, deletion, read-before-write, conflict, audit.
- Bunnyshell 'Coding Agent Sandbox' — confirms same boundary list as canonical agent-safety practice.
- Vercel 'Security boundaries in agentic architectures' — confirms the five-prohibition pattern as widely adopted; calls these 'first-line agent safety primitives.'
- OpenAI 'Sandbox Agents' (developers.openai.com) — fail-loud-on-violation is the canonical enforcement pattern.
- Reason (1990) 'Human Error' — failure-logging is the load-bearing component for incident analysis; cannot be skipped.

**Challenges noted:** None of substance; see _against.md file.

**Confidence:** High

**Applicable to:** DECISION-036; all worker-agent designs in C2A2; vault-safety-boundary cluster; agents.md SSOT pattern

**Re-check due:** 2026-08-18 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b NO-CHALLENGE-FOUND (None). Heuristic application: Strong literature support across multiple converging sources; no credible challenge to the prohibitions themselves. Incorporate as a canonical vault-safety-boundary statement; track completeness audit separately.

---

**Cycle-level observation:** the 2026-05-18 cycle produced 5 INCORPORATEs (ASSUMPTION-158, ASSUMPTION-160, ASSUMPTION-165, ASSUMPTION-167, ASSUMPTION-170) — third consecutive non-zero INCORPORATE cycle. Across the seven-cycle window (2026-05-09 / 10 / 11 / 13 / 14 / 15 / 18), INCORPORATE rate is now 13/151 (8.6%). Five-item cycles are rare; the pattern is driven by the Path-2 vault-safety-boundary cluster (3 of 5) plus pipeline-state documentation (2 of 5). The pre-implementation-articulation-passes-are-more-INCORPORATE-likely pattern (from prior cycle observation) is reinforced: today's items came from a self-awareness pass over yesterday's substantive infrastructure work, not from operational incidents.

---

### PREMISE-028:
**Date validated:** 2026-05-19
**Source item:** ASSUMPTION-173
**Item type:** ASSUMPTION
**Priority:** LOW

**Validated statement:**
Future-dated lecture announcements warrant follow-up monitoring-task scheduling rather than past-tense treatment, provided the announcement passes a significance-triage filter to avoid muda.

**Supporting evidence:**
- Forward-looking content-curation patterns in academic media monitoring (Becker et al. 2009 on event-detection).
- Calendar-based content workflows in newsroom and research-monitoring tooling.

**Challenges noted:** Risk of muda (Lean waste) if every future-dated announcement triggers monitoring; significance-triage filter required.

**Confidence:** Moderate

**Applicable to:** Monitor-queue agent; content-curation workflow design.

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Moderate); 15b PARTIALLY-CHALLENGED (Weak-Moderate). Sound principle with operational caveat encoded.

---

### PREMISE-029:
**Date validated:** 2026-05-19
**Source item:** ASSUMPTION-174
**Item type:** ASSUMPTION
**Priority:** HIGH

**Validated statement:**
Phase-6 commit blocked by stale .git/index.lock requires recovery before push; the constitutional rule forbidding blind push of 476 uncommitted changes is sound, BUT "visual review of all 476" is ineffective per cognitive-load literature and requires decomposition into per-file or per-phase review.

**Supporting evidence:**
- Pro Git (Chacon & Straub) on index.lock recovery.
- SRE & DevOps literature on checkpoint discipline (Beyer et al. 2016 "Site Reliability Engineering").

**Challenges noted:** Cohen et al. literature on visual-review at N>20 is ineffective; decomposition required.

**Confidence:** High

**Applicable to:** VCS workflow; Phase-N commit protocol; couples to revision in PRESUMPTION-199/REVISE-024.

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Moderate; visual-review-at-scale critique). Core principle correct; review modality needs revision.

---

### PREMISE-030:
**Date validated:** 2026-05-19
**Source item:** ASSUMPTION-176
**Item type:** ASSUMPTION
**Priority:** LOW

**Validated statement:**
Near-duplicate Q&A pairs in tradition-specific pending queues warrant dedup before review; at N=2, "show-both" is cheaper than automated collapse and preserves human judgment.

**Supporting evidence:**
- Near-duplicate detection literature (Manku et al. 2007; Broder 1997 shingling).
- Curation hygiene patterns in scholarly databases.

**Challenges noted:** Auto-collapse risk at low N; show-both preserves reviewer agency.

**Confidence:** High

**Applicable to:** Wolfram pending; per-tradition pending queues; review workflow.

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak-Moderate; auto-collapse cost). Standard hygiene with operational caveat.

---

### PREMISE-031:
**Date validated:** 2026-05-19
**Source item:** ASSUMPTION-178
**Item type:** ASSUMPTION
**Priority:** HIGH

**Validated statement:**
Three-way orchestrator/briefing/specialist contradiction on Monday Levin+Friston output is a real and reproducible inter-agent state-visibility failure; descriptive observation is sound. Remediation lives in the linked PRESUMPTION-196/REVISE-021 path (write-receipt manifest).

**Supporting evidence:**
- Distributed-systems inconsistency literature (Brewer CAP; Helland 2015 "Immutability changes everything").
- Event-sourcing patterns (Fowler).

**Challenges noted:** None of substance for the descriptive claim itself.

**Confidence:** High

**Applicable to:** Inter-agent state-visibility design; couples to REVISE-021 (PRESUMPTION-196) and REVISE-030 (PRESUMPTION-204).

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b NO-CHALLENGE-FOUND. Clean INCORPORATE; descriptive validity not in dispute.

---

### PREMISE-032:
**Date validated:** 2026-05-19
**Source item:** ASSUMPTION-181
**Item type:** ASSUMPTION
**Priority:** MEDIUM

**Validated statement:**
Connectivity-metric scope conflates auto-generated derivative content with human/tradition-authored content; stratification recommended. Soften "entirely" to "predominantly" for the +338 orphan jump attribution and report both layered metrics.

**Supporting evidence:**
- Vault content-type taxonomy patterns in knowledge-graph metrics (Bryl & Bizer).
- Separate-derived-from-authored stratification in scholarly graphs.

**Challenges noted:** Default-include traversal is a benign convention in some tooling; the case here is the conflation, not the inclusion.

**Confidence:** High

**Applicable to:** Connectivity-metric reporting; couples to PRESUMPTION-203/PREMISE-035 (two-metric reporting).

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak-Moderate). Stratification recommendation sound with epistemic-precision caveat.

---

### PREMISE-033:
**Date validated:** 2026-05-19
**Source item:** ASSUMPTION-184
**Item type:** ASSUMPTION
**Priority:** LOW-MEDIUM

**Validated statement:**
Cowork-to-chat delivery via document.execCommand('insertText', ...) on ProseMirror contenteditable succeeds where type-with-newlines path misfires; workaround is technically sound and well-attested in ProseMirror community discussions.

**Supporting evidence:**
- ProseMirror documentation on input handling.
- Browser-automation discussions of contenteditable input dispatch (Puppeteer/Playwright user notes).

**Challenges noted:** execCommand deprecation risk in long-term Chromium roadmap; need documented fallback.

**Confidence:** High

**Applicable to:** SKILL.md update for cowork-to-chat delivery; durable-memory pipeline reliability.

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak-Moderate; deprecation horizon). Document conditions and fallback as caveat.

---

### PREMISE-034:
**Date validated:** 2026-05-19
**Source item:** ASSUMPTION-185
**Item type:** ASSUMPTION
**Priority:** MEDIUM

**Validated statement:**
Pulte Pre-Test Pack four-contamination-mode verification frame (temporal/author/specificity/scoring-grain) plus graded scoring 0/0.5/1 is methodologically sound and C2A2-transferable for bridge-claim and cadence-discipline pre-registration. Transferability of relative weights addressed in PRESUMPTION-205/MONITOR-196.

**Supporting evidence:**
- Pre-registration literature (Nosek et al. 2018 "Preregistration revolution"; Munafò et al. 2017 "Manifesto for reproducible science").
- Contamination-mode taxonomies in research-prediction work.

**Challenges noted:** Four-mode portability across institute-id domains untested (handled separately in PRESUMPTION-205).

**Confidence:** High

**Applicable to:** Cross-project methodology import; bridge-claim and cadence-discipline pre-registration in C2A2.

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak-Moderate). Frame is methodologically sound; weight-calibration is the separate question.

---

### PREMISE-035:
**Date validated:** 2026-05-19
**Source item:** PRESUMPTION-203
**Item type:** PRESUMPTION
**Priority:** MEDIUM

**Validated statement:**
Two-metric stratified reporting (auto-generated derivative vs human/tradition-authored) for vault connectivity is the textbook fix for the layer-conflation in PRESUMPTION-203; low cost, high clarity gain.

**Supporting evidence:**
- Knowledge-graph metrics literature.
- Layered-metric reporting standards (DCAT, schema.org content typing).

**Challenges noted:** Default-include traversal as benign convention; mitigated by reporting both.

**Confidence:** High

**Applicable to:** Connectivity-metric reporting; couples to PREMISE-032 (ASSUMPTION-181).

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak-Moderate). Notable: this is a PRESUMPTION-class INCORPORATE — extra epistemic weight because the system was unaware of the presumption and surfacing it produced a clean fix.

---

### PREMISE-036:
**Date validated:** 2026-05-19
**Source item:** PRESUMPTION-208
**Item type:** PRESUMPTION
**Priority:** MEDIUM

**Validated statement:**
FC26 308-day corpus horizon should add a lightweight re-review trigger (e.g., Day 150 checkpoint) rather than full slack/recovery budget articulation; addresses planning-fallacy risk at low ceremony cost.

**Supporting evidence:**
- Planning-fallacy literature (Kahneman & Tversky 1979; Buehler et al. 1994).
- Long-horizon publication commitments in scholarly project management.

**Challenges noted:** Re-review trigger could become ritualized; mitigated by single checkpoint at Day 150.

**Confidence:** High

**Applicable to:** FC26 abstract closure; long-horizon publication discipline.

**Re-check due:** 2026-08-19 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak). PRESUMPTION-class INCORPORATE; surfacing the no-slack presumption produced an actionable remediation.

---

**2026-05-19 cycle additions to validated_premises:**

Total PREMISEs: 36 (27 prior + 9 new — PREMISE-028 through PREMISE-036).

INCORPORATE rate this cycle (excluding cycle-1 refreshes): 9/28 = 32%.

Cohort breakdown: Cohort B contributed 4 INCORPORATEs (PREMISE-028, -029, -030, -031); Cohort C contributed 5 INCORPORATEs (PREMISE-032 through -036).

PRESUMPTION-class INCORPORATEs (extra epistemic weight): PREMISE-035 (PRESUMPTION-203) and PREMISE-036 (PRESUMPTION-208). Both surfaced presumptions produced clean operational fixes.

Couplings: PREMISE-029 ↔ REVISE-024 (visual-review-of-N decomposition needed); PREMISE-031 ↔ REVISE-021/REVISE-030 (write-receipt manifest is the linked remediation); PREMISE-032 ↔ PREMISE-035 (stratified reporting pair).

---


**2026-05-20 cycle additions to validated_premises (PREMISE-037..041):**

### PREMISE-037:
**Date validated:** 2026-05-20
**Source item:** ASSUMPTION-186
**Item type:** ASSUMPTION
**Priority:** HIGH

**Validated statement:**
Queue-depth alarms and conservation-gate throttles must operate on deduplicated counts; a count corrupted by a known bug is a measurement artifact and must not drive control logic until reconciled.

**Supporting evidence:**
- Redman, T. (2001). "Data Quality: The Field Guide." — Duplicate records are a primary source of inflated counts; deduplication is a precondition for any count-driven decision.
- Batini, C. & Scannapieco, M. (2006). "Data Quality: Concepts, Methodologies and Techniques." — Record-linkage / dedup is the canonical remedy for count corruption from repeated entities.

**Challenges noted:** No credible body of literature defends acting on a raw count known to contain duplicate records. The only weak counter is pragmatic: dedup has cost, and if the alarm threshold has wide margin the artifact may not change the decision. Here it did change the decision (drove a conservation-gate throttl

**Confidence:** High

**Applicable to:** Conservation-gate throttle; pending-queue alarm; couples PRESUMPTION-210 (queue-depth proxy) and PRESUMPTION-212 (documented==true).

**Re-check due:** 2026-08-20 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b NO-CHALLENGE-FOUND (Weak). Strong support, no real challenge, and the artifact already drove a real control action — exactly the case where the generalizable hygiene premise should enter the validated register. Specific counts flagged for re-confirmation post-fix.

---
### PREMISE-038:
**Date validated:** 2026-05-20
**Source item:** ASSUMPTION-188
**Item type:** ASSUMPTION
**Priority:** HIGH

**Validated statement:**
Git commits for the vault are routed through the trusted host shell by policy (least-privilege); the sandbox is not permitted to write .git under current ACL + a removable stale-lock condition. 'Cannot' is a policy/config state, not an impossibility, and remains revisable.

**Supporting evidence:**
- NIST SP 800-190 (2017). "Application Container Security Guide." — Read-only / restricted-write root filesystems for sandboxed execution are a recommended hardening pattern; write restriction on VCS metadata is consistent with least privilege.
- GitOps / CI conventions (Weaveworks, 2017; "Continuous Delivery," Humble & Farley 2010). — Commits originating from a trusted runner/host rather than ephemeral sandboxes is an established, intentional convention.

**Challenges noted:** The challenge targets the framing, not the practice: 'cannot write .git' overstates a situation that is really 'is not currently permitted to, by ACL + a removable stale lock.' Both contributors (ACL and stale lock) are configurable/clearable. Conflating a configuration choice with an impossibility

**Confidence:** Moderate

**Applicable to:** Commit/persistence workflow; couples ASSUMPTION-189 (lock root cause), ASSUMPTION-190 (sync_vault.sh), PRESUMPTION-211 (durability ownership).

**Re-check due:** 2026-08-20 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Moderate). The operational premise (commits routed through the host shell) is well-grounded and already in use; the challenge is to the word 'cannot,' which I incorporate with an explicit reframing rather than rejecting the practice. Moderate (not High) confidence because the mechanism (ACL vs stale lock) overlaps the unresolved REVISE-033 root cause.

---
### PREMISE-039:
**Date validated:** 2026-05-20
**Source item:** ASSUMPTION-191
**Item type:** ASSUMPTION
**Priority:** MEDIUM

**Validated statement:**
Fail-closed build guards (refuse Summa-less sociogram builds; .gitignore *.bak* to exclude backup artifacts) are validated local invariants and should be retained; their consolidation under single build-integrity ownership is tracked separately (PRESUMPTION-216 / MONITOR-206).

**Supporting evidence:**
- Saltzer, J. & Schroeder, M. (1975). "The Protection of Information in Computer Systems." — Fail-safe defaults: deny/refuse on a missing precondition rather than proceed into a degraded state.
- Humble, J. & Farley, D. (2010). "Continuous Delivery." — Build-time invariants / guard checks that fail the build on a violated precondition are a core deployment-safety pattern.

**Challenges noted:** The challenge is not to the guards themselves (which are sound) but to the pattern they exemplify: a growing collection of per-failure point-guards can substitute for systemic integrity ownership and grow the maintenance surface (this is the explicit subject of PRESUMPTION-216). The two guards here

**Confidence:** High

**Applicable to:** regen_sociogram.sh build path; vault commit hygiene; couples PRESUMPTION-216.

**Re-check due:** 2026-08-20 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak-Moderate). The two specific guards are textbook fail-safe defaults with no challenge at the guard level; the only objection (point-guard proliferation) is a distinct presumption dispositioned at MONITOR-206. Incorporate the guards as validated practice with a forward-pointer to the systemic concern.

---
### PREMISE-040:
**Date validated:** 2026-05-20
**Source item:** ASSUMPTION-192
**Item type:** ASSUMPTION
**Priority:** MEDIUM-HIGH

**Validated statement:**
Artifact-derived statistics (node/edge/byte counts) must be auto-generated from the live artifact rather than hand-maintained in documentation; hand-copied stats drift and have already driven a decision (payload-diet deferral) on stale inputs. Re-evaluate that deferral at the corrected ~15.4 MB.

**Supporting evidence:**
- Parnas, D. (1994). "Software Aging" (ICSE). — Documentation drifts out of sync with the system it describes unless actively maintained; stale embedded stats are a canonical instance.
- Lehman, M. (1980). "Programs, Life Cycles, and Laws of Software Evolution." — Continuing change guarantees documentation divergence absent a reconciliation process.

**Challenges noted:** There is no real challenge to the staleness claim. The only weak counter is that some doc figures are deliberately approximate, but here the figures drove a design judgment (the payload-diet deferral), so accuracy matters and 'approximate is fine' does not apply. The 15b routing question — whether t

**Confidence:** High

**Applicable to:** CLAUDE.md / docs maintenance; payload-diet deferral; couples ASSUMPTION-193, PRESUMPTION-212 (REVISE-039).

**Re-check due:** 2026-08-20 (Quarterly)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b NO-CHALLENGE-FOUND (Weak). Strong support, no challenge, and the staleness already affected a design decision — the generalizable premise (artifact stats must be auto-derived, not hand-maintained) belongs in the validated register. The downstream payload-diet re-check is noted as an action.

---
### PREMISE-041:
**Date validated:** 2026-05-20
**Source item:** ASSUMPTION-194
**Item type:** ASSUMPTION
**Priority:** LOW-MEDIUM

**Validated statement:**
The prs_3d generator is non-idempotent and must consume the source template, never a built file; this constraint should be enforced by a fail-closed input guard (refuse built-file inputs) rather than by operator discipline alone. Mirrors the documented wiki_narration non-idempotence constraint.

**Supporting evidence:**
- Reproducible-builds / hermetic-build literature (Bazel docs; Lamb & Zacchiroli 2021, "Reproducible Builds," IEEE Software). — Generators that consume their own output drift; feeding the canonical source/template each time is the standard discipline.
- Infrastructure-as-code idempotence (Ansible/Terraform design docs). — Non-idempotent transforms must be guarded by always operating from the declared source, never from a derived state.

**Challenges noted:** The weak-moderate challenge: non-idempotence is often a fixable property, and encoding 'must be fed template, never a built file' as a permanent operating rule substitutes human discipline for a design fix. A rule that depends on always remembering not to feed a built file will eventually be violate

**Confidence:** High

**Applicable to:** prs_3d generation; mirrors wiki_narration; couples PRESUMPTION-216 (point-guard consolidation).

**Re-check due:** 2026-11-20 (Quarterly; low-medium stakes)

**Status:** ACTIVE

**Rationale:** 15a SUPPORTED (Strong); 15b PARTIALLY-CHALLENGED (Weak-Moderate). The non-idempotence constraint is real, strongly supported, and matches an existing validated internal pattern (wiki_narration). Incorporate it as a known constraint with the 15b mitigation folded in: enforce the rule with a fail-closed input guard rather than relying on operator memory.

---

Total new PREMISEs this run: 5 (PREMISE-037 through PREMISE-041). PRESUMPTION-class INCORPORATEs: 0.

---

### PREMISE-042:
**Date validated:** 2026-05-21
**Source item:** ASSUMPTION-205
**Item type:** ASSUMPTION

**Validated statement:**
Genuine cross-tradition intellectual convergence is predominantly analogical/structural rather than verbatim/lexical; literal shared-resource overlap will therefore be sparse and systematically undercount true convergence (the vocabulary problem). SCOPE: this premise covers the analogical-convergence principle only; the specific '3 literal hubs' count is NOT validated and is quarantined to PRESUMPTION-228 (REVISE-046) pending entity-resolution sensitivity analysis.

**Supporting evidence:**
- Gentner, D. (1983). "Structure-Mapping," Cognitive Science. — Cross-domain convergence is relational/structural, not surface/lexical; foundational support that real convergence is analogical.
- Hofstadter & Sander (2013). "Surfaces and Essences." — Analogy as the core of cross-domain conceptual connection; literal lexical overlap is the exception.

**Challenges noted:** The cited evidence (3 literal hubs) is naming/normalization-dependent and artifact-prone (PRESUMPTION-228); and some convergence is literal (shared formal results), so 'not verbatim' is not exhaustive.

**Confidence:** Moderate

**Applicable to:** DECISION-040 (convergence-is-analogical stance — use the principle, not the raw count); cross-tradition coil/hub detection; ASSUMPTION-206 (lexical detection will undercount by the same vocabulary-problem logic).

**Re-check due:** 2026-08-21 (Quarterly)

**Status:** ACTIVE

**Rationale:** Strong support for the principle with only a weak/measurement-scoped challenge -> INCORPORATE with caveats. Confidence Moderate (not High) because the item as written fuses a strong principle with an artifact-prone count; the count is explicitly excluded and routed to PRESUMPTION-228. Consistency-checked against ASSUMPTION-005/006 (traditions/PRS as imperfect units): no contradiction — this premise asserts the FORM of convergence, not that traditions are crisp.

---
### PREMISE-043:
**Date validated:** 2026-05-21
**Source item:** ASSUMPTION-206
**Item type:** ASSUMPTION

**Validated statement:**
Precision-first lexical/string-matching detection is a sound v1 baseline for generative-coil detection, PROVIDED its output (e.g., the 17 chains) is treated as a high-precision LOWER BOUND, not a complete count; recall is known to be low (vocabulary problem) and must be estimated and then addressed by the planned v2 semantic/embedding stage.

**Supporting evidence:**
- Baseline-first ML practice (Zinkevich, "Rules of Machine Learning"). — A high-precision lexical baseline before semantic models is standard, low-risk staging.
- Manning, Raghavan & Schutze, "Introduction to Information Retrieval." — Exact match gives high precision, low recall; appropriate for a precision-first v1.

**Challenges noted:** Lexical recall is low (Furnas vocabulary problem); the 17-chain count understates true coils until recall is measured or v2 lands.

**Confidence:** High

**Applicable to:** Coil-detection pipeline; OPEN-059; couples PREMISE-042 (the vocabulary problem implies undercount of literal overlap).

**Re-check due:** 2026-11-21 (Quarterly; low-medium stakes)

**Status:** ACTIVE

**Rationale:** Strong support for staged precision-first detection; the only challenge (low recall) is explicitly anticipated by the v2 plan. INCORPORATE at High confidence with the 15b mitigation folded in (treat v1 as a lower bound; measure recall). Consistency-checked: reinforces PREMISE-042 (literal overlap undercounts).

---

Total new PREMISEs this run: 2 (PREMISE-042, PREMISE-043). PRESUMPTION-class INCORPORATEs: 0 (both INCORPOREATEs are ASSUMPTIONs).

---


---

## INCORPORATE — run 2026-05-30

PREMISE-044:
  Date validated: 2026-05-30
  Source item: ASSUMPTION-256
  Statement: Highlight (transient, reversible focus/lens) and filter (persistent, stateful selection) are legitimately distinct, non-syncing interaction idioms; a graph UI may separate a transient search/focus lens from hard checkbox filters without the two synchronizing.
  Item type: ASSUMPTION (stated — Tom locked the model: "leave the current model")
  Supporting evidence: Furnas (1986) Generalized Fisheye Views; Shneiderman (1996) visual information-seeking mantra; Heer & Shneiderman (2012) Interactive Dynamics for Visual Analysis (CACM); Munzner, Visualization Analysis and Design.
  Challenges noted: Two visibility-affecting controls without a shared model can cause mode confusion (Norman 1983); the model was locked by preference, not a usability test (couples PRESUMPTION-284). Caveat recorded, not disqualifying.
  Confidence: Moderate
  Applicable to: Sociogram interaction model; Pathway 27/28 search + filter UI.
  Re-check due: 2026-08-30 (Quarterly, via 15d)
  Status: ACTIVE

---

## INCORPORATE — run 2026-06-02

PREMISE-045:
  Date validated: 2026-06-02
  Source item: ASSUMPTION-264
  Statement: Under a degraded/lagged session, an optimistic intermediate acknowledgement ("message sent," "logged in") is NOT authoritative; the agent must not claim a result it cannot re-verify against committed ground state (fail-loud). [SCOPED TO THE NECESSITY DIRECTION ONLY.]
  Item type: ASSUMPTION (stated)
  Supporting evidence: Read-your-writes / read-after-write consistency (AWS S3 strong read-after-write, 2020; System Design School; GeeksforGeeks); quorum-commit pattern; fail-loud-on-violation as canonical agent-design enforcement (OpenAI 'Sandbox Agents', cited at validated_premises.md ~line 1020).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate). The stronger sub-claim that "clean re-verification IS authoritative" is NOT incorporated — a same-regime re-check can share the fault (Knight & Leveson; common-mode failure), so re-verification is NECESSARY but not automatically SUFFICIENT. The blanket distrust of all intermediate reads is also bounded (optimistic acks are acceptable where channel reliability is independently known). The sufficiency gap is routed to REVISE-084 (PRESUMPTION-293).
  Confidence: Moderate
  Applicable to: Honesty layer; degraded-session handling; any tool-call whose success is asserted from an intermediate ack rather than a ground-state read. Reinforces Tom's Rule 12 (Fail loud). Couples ASSUMPTION-263, MONITOR-290 (PRESUMPTION-292), REVISE-084 (PRESUMPTION-293).
  Re-check due: 2026-09-02 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: The necessity direction (do not claim what you cannot re-verify) is strongly and cross-domain supported and faces no serious challenge; only its over-extension (authoritativeness of an in-band re-check) is contested, and that is explicitly excluded from the premise and handed to REVISE-084. Consistency-checked against PREMISE-001..044: no conflict; the fail-loud framing reinforces the existing fail-loud-on-violation citation. INCORPORATE at Moderate (not High) confidence because the verifier-independence caveat is material.

Total new PREMISEs this run: 1 (PREMISE-045). PRESUMPTION-class INCORPORATEs: 0 (the INCORPORATE is an ASSUMPTION).

---

## INCORPORATE — run 2026-06-02 (batch 2: 2026-06-02 EOD self-awareness batch)

PREMISE-046:
  Date validated: 2026-06-02
  Source item: ASSUMPTION-265
  Statement: The daily-run git/version-control phase must VERIFY that the intended effect occurred (staging/tracking actually happened) each run, rather than infer success from absence-of-error; a stale `.git/index.lock` from a crashed process can silently block all staging while runs report a clean tree. (Verify the side effect; do not equate "no error" with "effect achieved.")
  Item type: ASSUMPTION (stated)
  Supporting evidence: Safety vs liveness properties (Hillel Wayne; Lamport) — "no error" is a weak safety signal, not the liveness property that the change was staged; read-after-write / verify-the-side-effect (read-your-writes consistency, same family as PREMISE-045); fail-loud + pre-flight integrity checks (OpenAI Sandbox Agents, validated_premises ~line 1020). Empirically realized: ~4-day silent staging outage (2026-05-29 → 2026-06-02).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — per-run verification can be over-engineering for a low-frequency pipeline and git exit codes are reliable in the common case; outweighed because the silent failure actually occurred and persisted 4 days. Mitigation folded in: scope the check narrowly (stale-lock detection + read-after-write confirm of the index), not a broad noisy VC audit.
  Confidence: Moderate-High
  Applicable to: C2A2 wiki daily-run git phase; any pipeline step with a consequential, non-self-healing side effect. Reinforces PREMISE-045 and Tom's Rule 12 (Fail loud). Couples PRESUMPTION-294 (REVISE-085, lock-window recovery), OPEN-071.
  Re-check due: 2026-09-02 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption, strong support, only a weak YAGNI challenge that a realized multi-day silent failure on the VC spine outweighs. Same verify-don't-infer / fail-loud family as PREMISE-045 — consistency-checked: reinforces, does not conflict with, PREMISE-001..045. INCORPORATE at Moderate-High (slightly above PREMISE-045 because the failure is empirically realized, not hypothetical; below High because the narrow-vs-broad scoping of the check is an open design choice).

Total new PREMISEs this run (both batches): 2 (PREMISE-045, PREMISE-046). PRESUMPTION-class INCORPORATEs: 0 (both INCORPORATEs are ASSUMPTIONs).

---

## INCORPORATE — run 2026-06-03 (2026-06-02 evening Sociogram batch)

PREMISE-047:
  Date validated: 2026-06-03
  Source item: ASSUMPTION-266
  Statement: In a working tree that chronically carries unrelated modifications (here, Summa-vault-sync files), git staging must use explicit file paths, not `git add -A`/`-u`/`.`, so that a commit contains only intended changes. (Stage by declared intent, not by "everything currently dirty.")
  Item type: ASSUMPTION (stated)
  Supporting evidence: git-scm git-add documentation and GitHub git-guides (granular/explicit staging is the controlled alternative to `-A`); strong practitioner consensus that `git add -A` in a dirty tree risks committing unrelated/sensitive/binary files (HN 12886492; Graphite; codegenes; Medium/Mullatoez); least-privilege / explicit-intent commit principle.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — explicit-path staging treats the symptom while the chronically-dirty tree is the underlying defect (removable via `.gitignore`/separate repos/submodules), and a memory-dependent "never -A" convention is fragile AND can silently OMIT newly-created intended files (an under-commit failure). Not incorporated as "a manual convention is sufficient": the durable form backs it with a forcing function or removes the dirt source.
  Confidence: Moderate
  Applicable to: C2A2 wiki daily-run git phase; any repo with a perpetually-dirty working tree. Complements PREMISE-046 (verify VC health). Reinforces Tom's Rule 3 (surgical changes) and Rule 12 (fail loud). Couples PRESUMPTION-297 (MONITOR-293) and the 2026-06-03 human-memory SYSTEMIC-RISK.
  Re-check due: 2026-09-03 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption with strong, uncontested support for the staging discipline; the moderate challenge targets durability and locus-of-fix, not correctness, so INCORPORATE with caveats. Consistency-checked vs PREMISE-001..046: complements PREMISE-046; no conflict. Moderate (not High) confidence because the control should be a forcing function, not human memory, and explicit paths carry a complementary new-file-omission risk.

PREMISE-048:
  Date validated: 2026-06-03
  Source item: ASSUMPTION-268
  Statement: A pre-push constitutional review must VERIFY the rendered effect in a real served environment (a browser tab over HTTP, not headless/asserted), with explicit observable evidence (e.g., opacity/fade split, cross-link count, clean console) plus a human (Tom's) sign-off — i.e., observe the effect, do not infer it from "the code should do X."
  Item type: ASSUMPTION (stated)
  Supporting evidence: Test-in-the-real-environment guidance (CloudBees "Why and How You Should Test in Production"; Harness "Only a Full Pipeline Run Counts as Real Verification"); smoke / pre-promotion go/no-go gate practice (Harness; GeeksforGeeks); same verify-the-side-effect family as PREMISE-045/046; human sign-off as an out-of-band vantage.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — mandating a MANUAL FOREGROUND pass for the whole check over-claims: objective signals (cross-link count, console-clean, opacity threshold) are more reliable as deterministic automated assertions, and a manual gate is the step an autonomous, human-absent run is most likely to skip. Not incorporated as "must remain manual": the durable form automates the objective checks AND makes the push BLOCK when sign-off is absent.
  Confidence: Moderate-High
  Applicable to: Sociogram/wiki_narration pre-push gate; any release of a self-contained rendered artifact whose correctness is visual. Reinforces PREMISE-045/046 and Tom's Rule 12 (fail loud). Couples PRESUMPTION-298 (MONITOR-294, verification coverage) and the 2026-06-03 human-memory SYSTEMIC-RISK.
  Re-check due: 2026-09-03 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption, strong support for in-situ/observed verification (an instance of the already-incorporated verify-the-effect family); the moderate challenge is about the manual-vs-automated split and skip-risk, not the core, so INCORPORATE with caveats. Consistency-checked vs PREMISE-001..047: reinforces PREMISE-045/046; no conflict. Moderate-High (above PREMISE-047) because the principle is an extension of already-validated premises; below High because the manual gate must be hardened into automated assertions + a blocking sign-off to be robust on autonomous runs.

Total new PREMISEs this run (2026-06-03): 2 (PREMISE-047, PREMISE-048). PRESUMPTION-class INCORPORATEs: 0 (both INCORPORATEs are ASSUMPTIONs). Cumulative through PREMISE-048.

## INCORPORATE — run 2026-06-04 (2026-06-03 EOD self-awareness batch)

PREMISE-049:
  Date validated: 2026-06-04
  Source item: ASSUMPTION-269
  Statement: An unverified cross-tradition lead must never be TREATED AS TRUE — it may not form a trusted edge, enter narration, or ground a downstream artifact — until a targeted confirmation search promotes it. The durable implementation is provisional capture into an explicitly-tagged UNVERIFIED quarantine with a revisit/expiry forcing function, NOT silent refusal-to-capture and NOT silent promotion. ("Flag and confirm before trust," realized so the hold cannot become 'flag and forget.')
  Item type: ASSUMPTION (stated)
  Supporting evidence: LLM-era citation-hallucination integrity risk and verify-before-trust controls (CheckIfExist arXiv 2602.15871; CiteAudit arXiv 2602.23452); write-time gating empirically beating ingest-everything (~100% vs ~13% accuracy) while ARCHIVING rather than deleting (Zahn & Chana 2026, arXiv 2603.15994); KB provenance/metadata-for-reproducibility practice. Same verify-the-effect/provenance family as PREMISE-045/046.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — in a low-volume personal corpus recall is the scarce resource, so a strict do-not-ingest gate optimizes the wrong error, and an un-revisited hold queue reproduces the recall loss invisibly. The challenge targets the control's SHAPE (refuse-to-capture vs capture-and-quarantine-with-revisit), not the principle. Folded into the statement: prefer tagged provisional capture + a revisit/expiry forcing function over refusal-to-capture.
  Confidence: High
  Applicable to: C2A2 intake/ingest of cross-tradition leads; any automated KB-construction step that could create trusted edges from unverified material. Reinforces PREMISE-045/046 (verify-the-effect) and the provenance protocol. Couples ASSUMPTION-264, PRESUMPTION-302 (MONITOR-299, self-referential extraction).
  Re-check due: 2026-09-04 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption with strong, convergent support for verify-before-ingest; the only challenge is operational (corpus-size recall + hold-queue durability), resolved by specifying quarantine-with-revisit rather than refuse-to-capture. Consistency-checked vs PREMISE-001..048: reinforces the verify-the-effect/provenance family; no conflict. High confidence because both the integrity risk and the gating benefit are empirically grounded and the operational caveat is fully absorbed into the premise statement.

Total new PREMISEs this run (2026-06-04): 1 (PREMISE-049). PRESUMPTION-class INCORPORATEs: 0 (the sole INCORPORATE is an ASSUMPTION). Cumulative through PREMISE-049.

## INCORPORATE — run 2026-06-05 (2026-06-04 EOD self-awareness batch)

PREMISE-050:
  Date validated: 2026-06-05
  Source item: ASSUMPTION-272
  Statement: A bounded, quality-sensitive ingest backlog should be drained in small, scoped batches rather than one bulk run, because small batches lower per-transaction risk and variability, speed defect detection, and keep each commit reviewable and revertible. CAVEAT folded in: batch size must be tuned to the per-batch attended-authorization cost (a U-shaped cost curve), not fixed a priori — when the attended gate is expensive and the work is a finite one-time backlog, the cost-optimal batch can be larger than 5-8, and over-fragmentation re-introduces an availability dependency on Tom plus a rubber-stamping hazard. The durable form: small scoped batches with strong automated pre-checks (schema/dedup/scope), committed on a clean dedicated index so unrelated working-tree changes are not swept in.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Lean/agile flow & batch-size theory — small batches reduce variability, accelerate feedback, lower per-transaction risk and simplify review/validation (Reinertsen via SAFe Principle #6, InformIT/Scaled Agile; dev2ops "DevOps Lessons from Lean," 2012; Lean Six Sigma Hub "Batch Size Reduction"). Commit-hygiene practice (small coherent changesets are easier to review/revert) reinforces the scope clause. Same small-increment family as PREMISE-047 (granular staging).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — the support is for small batches, not for the conjunction of small batches WITH a mandatory attended gate each time. Batch-size theory has a transaction-cost lower bound (too-small is costly when the gate is expensive); human-in-the-loop literature documents fixed per-session overhead and a rubber-stamping failure when attended queues back up (Nuvento "Hidden Cost of HITL"; Codebridge/StackAI 2026). For a 36-file one-time backlog this can make a single well-scoped attended ingest dominate many tiny gated runs. The challenge targets sizing/gating, not the small-batch principle — so it is folded into the statement as the tuning caveat rather than blocking INCORPORATE.
  Confidence: Moderate
  Applicable to: C2A2 PROCESSED_LOG ingest-backlog drain; any quality-sensitive batch curation step with a human authorization gate. Reinforces PREMISE-047 (granular staging) and Tom's Rule 2 (simplicity)/Rule 3 (surgical changes). Couples ASSUMPTION-271 (MONITOR-300) and PRESUMPTION-305 (REVISE-088, commit-in-increments) — all three favor bounded small increments.
  Re-check due: 2026-09-05 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption with strong, well-established support for small-batch curation; the only challenge is operational (gate cost / sizing / rubber-stamping), resolved by folding the tune-to-overhead and automated-pre-check caveats into the premise. Consistency-checked vs PREMISE-001..049: complements PREMISE-047 (granular staging) and aligns with PRESUMPTION-305's commit-in-increments remedy; no conflict. Moderate (not High) confidence because the optimal batch size is genuinely cost-dependent and unverified for this backlog — the principle is "small scoped batches, sized to gate cost," not "5-8 is correct."

Total new PREMISEs this run (2026-06-05): 1 (PREMISE-050). PRESUMPTION-class INCORPORATEs: 0 (the sole INCORPORATE is an ASSUMPTION). Cumulative through PREMISE-050.

---

## Run 2026-06-06 (2026-06-05 ATTENDED Community Explorer P1 batch)

PREMISE-051:
  Date validated: 2026-06-06
  Source item: ASSUMPTION-275
  Statement: A relational/structure surface (a node-link graph) and an attribute/lookup surface (a card directory) over one corpus are complementary coordinated views, not duplicates: each affords a primary task the other does not (graph = read relational structure; cards = bulk attribute scan / targeted lookup), so maintaining both is justified by the coordinated-multiple-views Rule of Diversity. CAVEAT folded in (Rule of Parsimony): the justification holds only while non-absorption is demonstrable — i.e., there exists at least one high-value task each surface supports that the other genuinely cannot. If one surface becomes expressible as a saved/filtered state of the other (e.g., Cards = a filtered Graph view-state), the second surface is redundant and its build/test/maintenance + context-switching cost is no longer warranted; re-evaluate and consider deprecating the duplicate.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Baldonado, Woodruff & Kuchinsky 2000 "Guidelines for Using Multiple Views in Information Visualization" (Rule of Diversity); Roberts 2007 "State of the Art: Coordinated & Multiple Views in Exploratory Visualization" (CMV improves task performance, reveals relationships); Scherr / Wang Baldonado, multiple-and-coordinated-views survey.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — Baldonado's own Rule of Parsimony (each added view costs learning/space/maintenance and must be justified vs a single-view alternative) and an empirical finding that more coordinated views do not monotonically help and can impose context-switching cost (arXiv 2204.09524). Resolved by folding the non-absorption / parsimony test into the statement rather than blocking INCORPORATE.
  Confidence: Moderate
  Applicable to: Community Explorer Graph + Cards dual-surface design; any C2A2 tool considering a second coordinated view over one corpus. Reinforces Tom's Rule 2 (simplicity) / Rule 3 (surgical changes) — the parsimony caveat is the guard against speculative second surfaces. SCOPE NOTE: this premise validates the COMPLEMENTARITY of the two views only; the "over ONE dataset" claim depends on the curated↔directory join, which is REVISE-flagged (PRESUMPTION-306 → REVISE-089). If 306 resolves that the two record sets are distinct populations, ASSUMPTION-275's "one dataset" framing weakens even though the views-complementarity premise stands.
  Re-check due: 2026-09-06 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption with strong, well-established CMV support; the only challenge is the parsimony/cost guard, folded in as the non-absorption test. Consistency-checked vs PREMISE-001..050: no conflict — new UI-coordinated-views domain, complements none directly. Moderate (not High) confidence because non-absorption is asserted but not yet demonstrated for CE (no task inventory provided) and because the "one dataset" substrate is contested by PRESUMPTION-306.

**Total new PREMISEs this run (2026-06-06): 1 (PREMISE-051). PRESUMPTION-class INCORPORATEs: 0 (sole INCORPORATE is an ASSUMPTION). Cumulative through PREMISE-051.**

## INCORPORATE — run 2026-06-07 (2026-06-06 EOD attended CE build batch)

PREMISE-052:
  Date validated: 2026-06-07
  Source item: ASSUMPTION-280
  Statement: A tool that lists identifiable communities seeded from public web pages without express consent — none of which has approved its record — must DISCLOSE that provenance in-product (e.g., popover + source-of-truth doc) and must NOT imply endorsement or community approval. Disclosure-of-provenance + non-endorsement is the NECESSARY MINIMUM ethics/transparency bar for such listings. CAVEAT folded in (the boundary of this premise): disclosure is necessary, NOT sufficient — it does not by itself discharge the consent obligation for identifiable groups. The sufficiency overclaim ("disclosure cures the consent gap") is explicitly NOT incorporated and is REVISE-flagged (PRESUMPTION-313 → REVISE-092); this premise is the floor, to be paired with at least an opt-out/takedown path (and opt-in for higher-sensitivity communities).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Brown, Gruen, Maldoff, Messing, Sanderson, Zimmer 2025, "Web scraping for research: Legal, ethical, institutional, and scientific considerations" (Big Data & Society / arXiv 2410.23432); Association of Internet Researchers (AoIR) ethics guidance; data-provenance / metadata-for-reproducibility practice (also the basis of C2A2's own provenance protocol).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — for identifiable groups, transparency is necessary but not sufficient (Brown et al.; AoIR escalates with identifiability); notice-vs-consent critique (Solove, "Privacy Self-Management and the Consent Dilemma," 2013) warns disclosure can become a liability-shield; group-privacy literature (Taylor, Floridi & van der Sloot, "Group Privacy," 2017) notes individual-style notice fits group interests poorly. The challenge targets SUFFICIENCY, not the necessity of disclosure — so it is folded in as the floor-not-ceiling caveat rather than blocking INCORPORATE.
  Confidence: Moderate
  Applicable to: Community Explorer Cards/Graph listing of scraped community records; any C2A2 surface that presents identifiable third parties from non-consented public sources. Reinforces the provenance protocol and Tom's caution-over-speed bias. Couples ASSUMPTION-280's own sufficiency overclaim (PRESUMPTION-313 → REVISE-092) — the two together define floor (this premise) vs ceiling (still open).
  Re-check due: 2026-09-07 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption with strong, convergent support for disclosure-as-minimum; the only challenge is that disclosure is not the whole duty, which is fully separable and routed to REVISE-092, so it is absorbed as the floor-not-ceiling caveat rather than blocking INCORPORATE. Consistency-checked vs PREMISE-001..051: no conflict — new data-ethics/consent-disclosure domain. Moderate (not High) confidence because the surrounding consent question is genuinely unresolved (REVISE-092) and the premise is deliberately scoped to the necessary minimum, not a complete ethical clearance.

**Total new PREMISEs this run (2026-06-07): 1 (PREMISE-052). PRESUMPTION-class INCORPORATEs: 0 (sole INCORPORATE is an ASSUMPTION). ASSUMPTION-279 deliberately NOT re-INCORPORATED — its complementarity core is already PREMISE-051. Cumulative through PREMISE-052.**

## INCORPORATE — run 2026-06-08 (2026-06-07 PRS-connectome EOD batch)

PREMISE-053:
  Date validated: 2026-06-08
  Source item: ASSUMPTION-283
  Statement: When a PUBLISHED derived artifact (e.g., the PRS connectome) lags an append-only source because regeneration is a remembered manual chore, the correct fix is to make regeneration a SCHEDULED, owned pipeline step rather than to rely on ad-hoc manual rebuilds. CAVEAT folded in (the boundary of this premise): scheduling is NECESSARY, not SUFFICIENT. It cures staleness only under two conditions the literature stresses — (a) the scheduled execution context must be VERIFIED CAPABLE of running and publishing the regeneration (dev/prod parity; see PRESUMPTION-317 → REVISE-093, the realized failure of exactly this condition), and (b) the job must FAIL LOUDLY (failure-alerting / dead-man's-switch + a visible "last successfully published" signal), because a silently failing scheduled job reproduces the staleness invisibly and is harder to notice than the manual chore it replaced. Prefer event/threshold-triggered regeneration over fixed cadence for append-driven sources where feasible.
  Item type: ASSUMPTION (stated)
  Supporting evidence: The Twelve-Factor App, Factor XII (Admin processes) + Factor X (Dev/prod parity), 12factor.net; Postgres/Databricks materialized-view scheduled-refresh practice (staleness cured by scheduled or incremental REFRESH); Sculley et al. 2015, "Hidden Technical Debt in Machine Learning Systems" (NeurIPS) — derived data products must be owned, repeatable pipeline steps.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — silent-cron-failure / SRE monitoring (a green-looking schedule can mask a dead pipeline); the 2026-06-07 dev/prod-parity incident (scheduled context could not push, so "schedule it" did not fix publishing); event-driven vs fixed-cadence freshness (fixed cadence is the crudest mechanism). The challenge targets the CONDITIONS of success, not the pattern, so it is folded in as the capability+monitoring caveat rather than blocking INCORPORATE.
  Confidence: Moderate
  Applicable to: PRS-connectome regeneration/publishing; any C2A2 published derived artifact (visualizations, indexes) that must stay in sync with an append-only source. Reinforces Tom's caution-over-speed bias — the caveat is the guard against a "scheduled and therefore fresh" false assurance. SCOPE NOTE: this premise validates SCHEDULING-AS-THE-RIGHT-PATTERN; the capability precondition it names is itself REVISE-flagged (PRESUMPTION-317 → REVISE-093). The premise is the floor; the auto-publish SAFETY split it tends to ride with (ASSUMPTION-284) is only MONITOR (MONITOR-313), and the data-review-exemption (PRESUMPTION-319) is REVISE-094.
  Re-check due: 2026-09-08 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption with strong, convergent SE/data-engineering support for scheduled regeneration of stale derived state; the only challenge is that scheduling is necessary-not-sufficient, fully foldable as the capability+monitoring caveat. Consistency-checked vs PREMISE-001..052: no conflict (new CI/derived-artifact-freshness domain). Moderate (not High) confidence because the enacting environment FAILED the capability precondition (REVISE-093), so the premise is deliberately scoped to the pattern-floor, gated on parity + failure-alerting.

PREMISE-054:
  Date validated: 2026-06-08
  Source item: ASSUMPTION-286
  Statement: Constraints on an agent fall into two distinct layers: (1) CONFIGURABLE POLICY — rules expressed in instructions (e.g., the 12 CLAUDE.md rules) that are waivable with justification; and (2) NON-BYPASSABLE CAPABILITY/MECHANISM — boundaries enforced by what authority the runtime actually holds (e.g., sandbox credentials, missing push token), which cannot be waived because you cannot exercise an authority you were never granted. This is the policy/mechanism separation: policy sits above a non-bypassable enforcement mechanism. CAVEAT folded in (the dangerous case the assumption itself names): a POLICY rule may COINCIDE with a hard capability wall — and that coincidence is where realized cost lands. A policy rule that functionally shadows a capability/safety boundary (e.g., "probe before building," "read before writing") must be treated as EFFECTIVELY NON-WAIVABLE; treating it as ordinary waivable policy invites the confused-deputy / normalization-of-deviance failure of skipping the cheap guard and discovering the wall the expensive way. Every waiver of a policy rule must be EXPLICIT and JUSTIFIED (Tom's Rule 12 — fail loud).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Saltzer & Schroeder 1975, "The Protection of Information in Computer Systems" (least privilege, fail-safe defaults, complete mediation); policy/mechanism separation (Wulf et al., HYDRA; Lampson); capability-based security (unforgeable tokens; authority bounds cannot be talked past).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — the taxonomy is sound but its SAFE USE is risky: confused-deputy authority bugs (Hardy 1988) when policy is treated as freely waivable; mislabeling load-bearing safety rules as mere policy; normalization of deviance (Vaughan, "The Challenger Launch Decision") where routine waiving meets a non-negotiating wall. The challenge sharpens rather than refutes, and concentrates on the stated coincidence case, so it is folded in as the "rules shadowing a capability wall are effectively non-waivable" caveat.
  Confidence: Moderate
  Applicable to: C2A2 agent governance and self-modeling of constraints; deciding which CLAUDE.md rules may be waived and which shadow a hard wall; scheduled-task design (the 2026-06-07 auto-push incident is the coincidence case — a "probe-first" policy rule shadowing the missing-push-credential capability wall). Couples PRESUMPTION-318 (MONITOR-314, build-then-discover) and PRESUMPTION-317 (REVISE-093). Reinforces Rules 1, 8, 12.
  Re-check due: 2026-09-08 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Stated assumption that directly restates one of the most established principles in computer security (policy/mechanism separation + least privilege + capability authority bounds); strong support, and a sharpening-not-refuting challenge folded in as the coincidence-case caveat. Consistency-checked vs PREMISE-001..053: no conflict (new agent-governance/constraint-layering domain). Moderate (not High) confidence because the realized 2026-06-07 cost landed precisely on the coincidence case, so the premise carries an explicit operational warning rather than a clean separation guarantee.

**Total new PREMISEs this run (2026-06-08): 2 (PREMISE-053, PREMISE-054). PRESUMPTION-class INCORPORATEs: 0 (both INCORPOREs are ASSUMPTIONs). Cumulative through PREMISE-054.**


PREMISE-055:
  Date validated: 2026-06-11
  Source item: ASSUMPTION-287
  Statement: Observed telemetry (event streams, process traces) is the higher-fidelity PRIMARY basis for representing what agents in the system actually DO, and should ground the Agent Explorer's activity record in preference to authored narration, which demonstrably drifts from actual behavior. CAVEAT folded in (the boundary): telemetry constitutively cannot carry intent, rationale, or design theory (Naur's theory-building) — the authored narration layer is RETAINED as the intent/rationale record, not discarded. "Replace" is scoped to: replace-as-primary-activity-source, complement-for-intent. This premise covers what agents DO; it deliberately does NOT extend to "the event stream captures what an agent IS" — that substance claim is REVISE-095 (PRESUMPTION-322) and remains unvalidated.
  Item type: ASSUMPTION (stated)
  Supporting evidence: van der Aalst 2016, Process Mining (conformance checking: observed event data vs authored models); model-drift literature; digital-trace methodology (non-intrusive behavioral measurement).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — Naur 1985 "Programming as Theory Building": traces cannot carry intent; an explorer presenting activity as identity misrepresents. Folded as the retain-authored-intent caveat and the explicit substance-claim exclusion.
  Confidence: Moderate
  Applicable to: Agent Explorer data architecture; OpenStory ingest design (ASSUMPTION-288/MONITOR-317); any future agent-representation surface. Couples REVISE-095 (substance conflation), MONITOR-319 (eval/apply), MONITOR-321 (coverage).
  Re-check due: 2026-09-11 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Strong direct support for the activity-record reading; the only challenge targets the replacement-of-intent reading, which is folded out by scoping. Moderate (not High) because the premise sits atop a telemetry stack whose coverage and entity model are themselves REVISE/MONITOR-flagged (REVISE-096, MONITOR-321).

PREMISE-056:
  Date validated: 2026-06-11
  Source item: ASSUMPTION-290
  Statement: When a capture gap requires integrating with an actively-developed upstream (OpenStory), an EXTERNAL adapter/bridge (symlink session-bridge) is preferred over forking, to stay on upstream with zero carried patches. CAVEAT folded in: a bridge coupled to uncontracted internals (file layout, schema) breaks SILENTLY where a fork breaks loudly at merge time — the bridge therefore requires a LIVENESS CANARY (known-session fixture that fails visibly when the bridge stops capturing). Upstreaming the capability remains the unexplored third option and should be considered when the bridge accretes complexity.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Fork-maintenance drift case studies (Meta Engineering 2026 WebRTC shim "Escaping the Fork"); distro packaging policy against forks (Fedora); adapter/anti-corruption-layer pattern.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak) — Hyrum's Law dependence on uncontracted layout; silent-breakage asymmetry; fork-vs-bridge as false binary (upstreaming omitted). Folded as canary + upstreaming-option caveats.
  Confidence: Moderate-High
  Applicable to: OpenStory session-bridge; any future integration with actively-developed upstreams. Member of the silent-failure-seam SYSTEMIC cluster (with MONITOR-317, MONITOR-320) — the canary is the cluster remedy.
  Re-check due: 2026-09-11 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Strong, directly-on-point engineering precedent; weak challenge fully foldable as an operational caveat. Consistency-checked vs PREMISE-001..054: no conflict; reinforces PREMISE-053's fail-loud requirement (the canary).

PREMISE-057:
  Date validated: 2026-06-11
  Source item: ASSUMPTION-292
  Statement: An available pilot dataset (the 571-session OpenStory DB) is sufficient to prove a pipeline MECHANICALLY — exercising schemas, code paths, and end-to-end flow (walking-skeleton/tracer-bullet practice) — without a full reseed. SCOPE BOUNDARY folded in (this is the premise's load-bearing limit): mechanical sufficiency does NOT license trusting the pilot's DISTRIBUTIONAL outputs (rosters, rankings, edge densities, cluster shapes), because the pilot sample is biased exactly along the capture gap it was chosen despite. Any distributional claim requires reseed and/or quantified coverage.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Cockburn 2004 (walking skeleton); Hunt & Thomas 1999 (tracer bullets); standard pipeline-bring-up practice.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — dataset-shift/convenience-sampling literature (Quiñonero-Candela et al. 2009): distributional outputs calibrated on a skewed sample. Folded as the scope boundary, which both search directions independently drew in the same place.
  Confidence: Moderate
  Applicable to: Agent Explorer bring-up; any C2A2 pipeline proven on partial data. Couples REVISE-096 (roster mis-specification) and MONITOR-321 (window bias) — both sit on the distributional side of this premise's boundary.
  Re-check due: 2026-09-11 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Convergent split across both search directions (mechanics yes / distributions no) makes the narrow premise well-grounded. Moderate confidence; the premise is deliberately a boundary-drawing premise — its value is preventing the silent widening of "proves the pipeline" into "proves the picture."

PREMISE-058:
  Date validated: 2026-06-11
  Source item: ASSUMPTION-294
  Statement: The evidential weight of agreement within any Magisterium-Member Assembly (MMA) scales with the formational INDEPENDENCE of its members: independent convergence is strong evidence; same-formation agreement is heavily DISCOUNTED evidence. CORRECTION folded in (15b): same-formation agreement is redundant-but-real signal — a smaller effective N — NOT "near-chance noise"; the original clause overstated the discount to zero. Aggregation gains require bracketing conditions (diversity helps only when errors bracket the truth).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Lorenz et al. 2011 PNAS (social influence undermines wisdom-of-crowds); Becker et al. 2017 PNAS; Herzog & Hertwig (bracketing); Clemen & Winkler 1985 (correlated experts → reduced effective N).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — only the "near-chance noise" clause; the discount-not-zero correction is folded into the premise statement.
  Confidence: High (core); the folded correction is itself well-established.
  Applicable to: dyad-MMA and any future multi-agent assembly design; evidential weighting in PRS ratification. NOTE: this premise governs WEIGHTING; whether the dyad's agent member can achieve ANY effective independence is separately contested (MONITOR-323, ASSUMPTION-295) — this premise does not settle that.
  Re-check due: 2026-09-11 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: One of the best-established results in collective-judgment research; challenge corrects a clause rather than the claim. Consistency-checked vs PREMISE-001..054: no conflict.

PREMISE-059:
  Date validated: 2026-06-11
  Source item: ASSUMPTION-296
  Statement: Curricular ladder tools' implied milestones can legitimately serve as CANDIDATE PRS-elements — a candidate-generation source feeding dyad ratification — per standard learning-progressions practice (construct maps seeded from curriculum, then validated). CAVEATS folded in: (a) curricula encode instructional convention and ladder-linearity artifacts, so candidates carry systematic bias, not just noise; (b) dyad ratification is a far WEAKER validation gate than the empirical-recovery studies the literature expects — ratified elements remain provisional pending empirical validation; (c) coverage is unmeasured — the ladders' omissions become invisible non-candidates (MONITOR-333's audit).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Wilson 2009 (BEAR construct maps); learning-progressions validation-cycle literature; competency-derivation-from-courseware practice.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — convention artifacts; ratification-by-the-ladder's-author as weak filter; backward-design tradition derives milestones from competencies first. Folded as caveats (a)-(c).
  Confidence: Moderate
  Applicable to: first dyad triplet pass (Physics Explorer; RC Document Explorer as candidate sources); PRS-element provenance. Couples MONITOR-333 (coverage audit), REVISE-097 (the certification authority question sits ABOVE this premise and is unresolved).
  Re-check due: 2026-09-11 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: The stated claim is the modest candidate-status claim, which both directions accept; everything stronger is excluded by the caveats. No conflict with PREMISE-001..054.

PREMISE-060:
  Date validated: 2026-06-11
  Source item: ASSUMPTION-308
  Statement: A DETERMINISTIC scheduler should precede any bandit/adaptive layer in agent-activity optimization: at small N, exploration overhead exceeds its value, cold-start bandits underperform, and a deterministic baseline is needed to evaluate any later adaptive policy. CAVEATS folded in: (a) define an explicit GRADUATION CRITERION (what observed condition justifies adding the bandit layer) so "deterministic first" cannot become "deterministic forever by default"; (b) log scheduling decisions WITH occasional randomization (epsilon-style) — purely deterministic logs are confounded and cannot train or validate the later bandit off-policy.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Silva et al. 2022 ACM TORS (cold-start bandits); Lattimore & Szepesvári 2020 (Bandit Algorithms — exploration cost at small N); Li et al. 2011 (off-policy evaluation requires randomized logs — source of caveat b).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — the sequencing creates a data problem for its own successor unless caveat (b) is honored. Folded.
  Confidence: Moderate
  Applicable to: agent-activity scheduler design; the metabolism-instrument consumers (NOTE: any bandit layer would consume the yield metric — MONITOR-335/REVISE-103 must resolve before optimization is wired to it).
  Re-check due: 2026-09-11 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Supported sequencing claim with a constructive, foldable challenge. Consistency-checked vs PREMISE-001..054: no conflict; the applicable-to note guards against composing this premise with an unvalidated metric.

**Total new PREMISEs this run (2026-06-11): 6 (PREMISE-055..060). PRESUMPTION-class INCORPORATEs: 0 (all six are stated ASSUMPTIONs). Cumulative through PREMISE-060.**

PREMISE-061:
  Date validated: 2026-06-12
  Source item: ASSUMPTION-313
  Statement: Taking the weaker reading of each contested rung as the agreement is a rational, non-concessionary convergence strategy (incompletely theorized agreement): the dyad genuinely agrees on the weaker shared content without either member conceding their stronger view. CAVEATS folded in: (a) weaker-reading rungs must remain MARKED as incompletely theorized in the ledger — the deferred stronger-reading disagreement is stored, not resolved, and can collapse at application time (M7–M8); (b) when a marked rung is later USED (built upon, operationalized), the deferred disagreement must be re-surfaced and stress-tested at that point; (c) weaker-reading rungs and fully-theorized rungs should be distinguishable in any PRS count so convergence-by-weakening cannot silently inflate progress.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Sunstein 1995 (incompletely theorized agreements, Harv L Rev 108(7)); Rawls 1993 (overlapping consensus); Gilbert 1989 (joint commitment).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — Bathaee 2007 and negotiation literature: ambiguous agreements succeed at convergence but fail at application; deferred disagreements accumulate as false progress signals. Folded as caveats (a)-(c).
  Confidence: Moderate
  Applicable to: dyad ladder protocol (rung agreement procedure); PRS counting (couples REVISE-105's falsifier/metric separation); M7-M8 progression logic.
  Re-check due: 2026-09-12 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Strong direct support for the strategy as stated; the challenge specifies a maintenance requirement (track and re-surface deferred disagreement) rather than defeating the claim. Consistency-checked vs PREMISE-001..060: no conflict; complements PREMISE-058.

PREMISE-062:
  Date validated: 2026-06-12
  Source item: ASSUMPTION-315
  Statement: Separately-logged reasons preserve evidence distinguishing genuine agreement from convergence-by-adjudication (dual-reasons rule): conclusion-level agreement can mask premise-level disagreement (discursive dilemma), and logging each member's reasons separately makes that premise-level structure observable. CAVEATS folded in: (a) reasons must be logged BEFORE mutual reveal — pre-commitment is what blocks cascade contamination; sequential reason-sharing produces correlated logs; (b) logged reasons are evidence of premise-level structure, NOT guaranteed introspective truth — confabulation (Nisbett & Wilson) caps the evidential ceiling; treat reasons as data about the agreement's structure, not as infallible self-reports; (c) the rule's value degrades if either member can see the other's reasons before logging — enforce the blind window procedurally.
  Item type: ASSUMPTION (stated)
  Supporting evidence: List & Pettit 2002 (discursive dilemma, Econ & Phil 18(1)); Stasser & Titus 1985 (hidden profiles, JPSP); deliberation literature on reason-giving.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — Nisbett & Wilson 1977 (confabulation); informational-cascade literature (reason-sharing can amplify correlation). Folded as caveats (a)-(c).
  Confidence: Moderate
  Applicable to: dyad ladder protocol (dual-reasons rule implementation); agreement-quality evidence; sycophancy countermeasures (couples the dyad reliability protocol, REVISE-106).
  Re-check due: 2026-09-12 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Formal support (discursive dilemma) is direct and strong; challenges define implementation constraints (pre-commitment, epistemic ceiling) rather than refuting the rule. Consistency-checked vs PREMISE-001..060: no conflict; directly reinforces PREMISE-058 (independence-weighting).

**Total new PREMISEs this run (2026-06-12): 2 (PREMISE-061..062). Both stated ASSUMPTIONs; PRESUMPTION-class INCORPORATEs: 0. Cumulative through PREMISE-062.**

PREMISE-063:
  Date validated: 2026-06-16
  Source item: ASSUMPTION-320
  Statement: Gap-honest visualization is preferable to interpolation or silent zero-fill: a time-series/dashboard must not show data that do not exist, must distinguish measured from inferred values, and must encode absence as distinct from a true zero. Any imputation must be shown explicitly as inferred (e.g., a labeled band with uncertainty), never silently. CAVEATS folded in: (a) gap-honesty must be implemented with a LEGIBLE gap encoding (marked break/annotation), not raw blanks, since dense gaps can add more noise than signal; (b) showing the gap is necessary but NOT sufficient for understanding — a visible gap-marker does not by itself communicate the gap's meaning or cause (this is the separate, still-open PRESUMPTION-351 / REVISE-116: visibility != comprehension); (c) where the gap's cause is known (capture artifact vs real inactivity), encode the two distinctly rather than conflating them (couples PRESUMPTION-352).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Tufte 1983/2001 (graphical integrity — do not show data that do not exist); time-series missing-data visualization review (arXiv:2507.14920 — expose missingness + provenance, distinguish measured vs inferred); imputeTS / FlowingData 2018 (explicit missing-data encoding conventions).
  Challenges noted: 15b NO-CHALLENGE-FOUND (Weak; boundary conditions only) — dense gaps can reduce legibility, and marked imputation-with-uncertainty can beat a bare gap for some tasks. Folded as caveats (a)-(c); the "silent zero" alternative the premise rejects has no defenders in the literature.
  Confidence: Moderate-High
  Applicable to: Metabolism view missing-data display; any C2A2 time-series or dashboard visualization (e.g., PRS connectome timelines, agentic-metabolism series).
  Re-check due: 2026-09-16 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Strong, essentially uncontested support for the integrity principle; the only challenges specify HOW to encode gaps legibly, not WHETHER to show them. Consistency-checked vs PREMISE-001..062: no conflict; the comprehension companion (visibility != comprehension) is deliberately NOT incorporated here — it remains REVISE-116, so this premise is scoped to "show the gap honestly," not "the shown gap is understood."

**Total new PREMISEs this run (2026-06-16): 1 (PREMISE-063). Stated ASSUMPTION; PRESUMPTION-class INCORPORATEs: 0. Cumulative through PREMISE-063.**

PREMISE-064:
  Date validated: 2026-06-17
  Source item: ASSUMPTION-326
  Statement: Build (and define) the metric before iterating the view layer that depends on it. The metric is the stable layer; the visualization depends on it, so defining and pressure-testing the metric first avoids the rework guaranteed by designing a view against placeholder or undefined data ("cart-before-horse"). CAVEAT folded in: "metric first" means "define + cheaply pressure-test the metric," NOT "fully finalize the metric in isolation" — a deliberately rough, disposable view is a legitimate validation instrument for the metric definition and should be used to surface definitional edge-cases early (EDA/Tukey; the view validates the measure). CRITICAL SCOPE GUARD: this premise licenses the SEQUENCING only; it does NOT license treating the built metric as trustworthy enough to harden downstream artifacts upon — that over-trust is the separate, REVISE-flagged PRESUMPTION-360 (REVISE-124: provenance != validity).
  Item type: ASSUMPTION (stated)
  Supporting evidence: "Measure first" / data-before-dashboard practice in analytics & BI; dependency-first design (build the stable layer before the volatile one); "garbage in, gospel out" cautions against designing presentation around unsettled data definitions.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — a STRICT "finalize metric before any view" reading is a mini-waterfall that forgoes the diagnostic value of cheap prototype views; folded as the "pressure-test with a disposable view" caveat. The "design a polished view against an undefined metric" alternative the premise rejects has no defenders.
  Confidence: Moderate-High
  Applicable to: PRS-yield metric -> 3D connectome / Metabolism view build order; any C2A2 metric-and-its-visualization sequencing.
  Re-check due: 2026-09-17 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Strong, conventional support for the dependency-ordering; the only challenge specifies HOW to do metric-first (with a diagnostic throwaway view), not WHETHER. Consistency-checked vs PREMISE-001..063 (incl. PREMISE-062, deterministic-scheduler-first — same dependency-ordering family): no conflict. The scope guard deliberately withholds the "built ⇒ trustworthy" step (that remains REVISE-124).

PREMISE-065:
  Date validated: 2026-06-17
  Source item: ASSUMPTION-327
  Statement: For separating co-located nodes in a generated layout, a DETERMINISTIC (reproducible) arrangement is preferable to random jitter. Determinism preserves the viewer's mental map across regenerations (Misue et al.), enables visual diffing / regression testing of the layout, and makes the separation rule inspectable — all of which non-deterministic jitter defeats. CAVEAT folded in (load-bearing): determinism is a reproducibility property, NOT a claim that the resulting positions are meaningful. A stable, ordered arrangement is reliably DECODED AS MEANINGFUL (Cleveland & McGill positional channel), so a deterministic non-semantic fan must be explicitly MARKED INCIDENTAL (uniform/neutral styling; "positions within a node-cluster are non-semantic" note) and must not mimic an ordered scale — otherwise its very consistency manufactures spurious structure. The companion requirement (do not mistake resolvability for fidelity) is the separate REVISE-flagged PRESUMPTION-358 (REVISE-122).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Misue, Eades, Lai, Sugiyama — "Layout Adjustment and the Mental Map" (layout stability across regenerations); reproducibility in scientific visualization (fixed-seed/fixed-rule rendering enables diffs and regression tests); Cleveland & McGill 1984 (position is decoded accurately — basis of the incidental-marking caveat).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — a deterministic ordered fan can be OVER-READ as meaningful more reliably than random jitter (which reads as "noise, ignore"); the real axis is semantic-vs-incidental encoding, not determinism-vs-jitter. Folded as the mandatory incidental-marking caveat; the over-reading remedy itself is carried separately by REVISE-122 (PRESUMPTION-358).
  Confidence: Moderate
  Applicable to: 3D connectome co-located-node separation (the fan-fix); any C2A2 layout requiring reproducibility across regenerations.
  Re-check due: 2026-09-17 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: On the stated determinism-vs-jitter binary, determinism strictly dominates for reproducibility/mental-map/diffing; the challenge does not bear on that binary (it concerns a third option — marking the layout non-semantic) and is folded as a caveat + routed to REVISE-122. Consistency-checked vs PREMISE-001..064 (reinforces PREMISE-062 deterministic-first family): no conflict.

**Total new PREMISEs this run (2026-06-17): 2 (PREMISE-064 metric-before-view sequencing; PREMISE-065 deterministic-over-random layout). Both stated ASSUMPTIONs; PRESUMPTION-class INCORPORATEs: 0. Cumulative through PREMISE-065. Both carry explicit scope guards withholding the over-trust/over-reading steps (routed to REVISE-124 and REVISE-122).**

PREMISE-066:
  Date validated: 2026-06-19
  Source item: ASSUMPTION-328
  Statement: Derive the user-facing thinker pop-up bio from the single canonical wiki.md the agents maintain (single source of truth / DRY) rather than a duplicated copy. Duplicated content is the recognized root cause of drift; one authoritative representation with a read-only derived view removes the entire class of sync bugs ("no second copy to drift"). SCOPE GUARD (load-bearing): SSOT relocates rather than removes the failure mode — the derived view is now COUPLED to the source's parse-contract (which block, which markers). The extraction boundary must therefore be an EXPLICIT, TESTED interface so a refactor of the working doc FAILS LOUDLY rather than silently emitting an empty/wrong pop-up. The premise licenses the one-source ARCHITECTURE only; it does NOT certify that the source text is automatically fit as a user-facing bio (adequacy = MONITOR-357/REVISE-125) nor that the source will be maintained (the upkeep contingency = MONITOR-359).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Hunt & Thomas 1999 (DRY — "single, unambiguous, authoritative representation"); SSOT / master-data-management practice (duplicated state -> drift); Codd normalization (redundant copies -> update anomalies).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — SSOT couples the view to the source format and makes one file serve two masters (agent-workspace + user-presentation); folded as the tested-extraction-boundary scope guard. The rejected alternative (a second hand-curated copy) has no defenders — it is the canonical drift source.
  Confidence: Moderate-High
  Applicable to: Sociogram thinker-summary pop-ups; any C2A2 derived view that reads from an agent-maintained canonical doc.
  Re-check due: 2026-09-19 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Strong, conventional support for the one-source architecture; the only challenge specifies HOW to do SSOT safely (test the extraction boundary), not WHETHER. Consistency-checked vs PREMISE-001..065: no conflict; coheres with the dependency-ordering family. Adequacy and upkeep questions deliberately withheld and routed to REVISE-125 / MONITOR-357 / MONITOR-359.

PREMISE-067:
  Date validated: 2026-06-19
  Source item: ASSUMPTION-330
  Statement: Provide a single canonical build wrapper (regen_sociogram.sh) that hardcodes required flags (--summa) and guards the known-bad configuration (Summa-less builds), and steer all regeneration through it ("paved road" / golden path). Centralizing the correct invocation prevents the "forgot the flag" class of operator misconfiguration and makes the safe path the default. SCOPE GUARD (load-bearing): a golden path enforced only by CONVENTION is bypassable — if generate_visualization.py remains runnable and is "forbidden" only by documentation, the guarantee is one habit-lapse (or one agent invocation) away from a Summa-less build, and the wrapper can drift from the underlying script's interface. The robust form puts the Summa-less guard IN THE ENTRY POINT (refuse/warn) and/or adds a post-build assertion that the artifact contains Summa nodes, so even direct invocation cannot silently ship a bad artifact. The premise licenses HAVING the canonical guarded wrapper; it does not certify that convention-only forbiddance is sufficient enforcement.
  Item type: ASSUMPTION (stated)
  Supporting evidence: "Paved road"/golden-path platform engineering (Netflix/Spotify/Google); build-automation convention (Make targets, wrapper scripts encapsulating required flags); configuration-as-code / sane-defaults.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — unenforced golden paths are bypassable and wrappers drift from the underlying tool; folded as the guard-in-code / post-build-assertion scope guard. Member of the convention-guard cluster (see SYSTEMIC-RISK cluster 4).
  Confidence: Moderate-High
  Applicable to: Sociogram regeneration; any C2A2 build with a required-flag/known-bad-config hazard.
  Re-check due: 2026-09-19 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: Strong support for the canonical wrapper; the challenge specifies HOW to make the "only path" actually safe (enforce in code), not WHETHER to have a wrapper. Consistency-checked vs PREMISE-001..066: no conflict; coheres with PREMISE-062 (deterministic-scheduler-first) and the guard-by-code preference echoed in REVISE-127.

PREMISE-068:
  Date validated: 2026-06-19
  Source item: PRESUMPTION-367
  Statement: Offering thinker summaries as ON-DEMAND pop-ups (details-on-demand / progressive disclosure) improves the sociogram: detail supplied on request keeps the default overview uncluttered while making depth available, which is the canonical improvement to an overview visualization (Shneiderman's "overview first, zoom and filter, details-on-demand"). SCOPE GUARD (load-bearing): the gain comes from the PROGRESSIVE-DISCLOSURE STRUCTURE (opt-in, dismissible, non-occluding), NOT from the presumption's stated rationale "more on-demand information = better." Minimalism/interaction-cost research denies that more information is categorically better and notes even on-demand detail carries discovery/occlusion cost; the "more = better" generalization is explicitly WITHHELD, and future annotation additions must be judged case-by-case (keep the default view clean; pop-ups must not occlude the structure they annotate).
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Shneiderman 1996 "The Eyes Have It" (details-on-demand mantra); Nielsen (progressive disclosure); Pirolli & Card (information scent / cost-of-knowledge).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — Tufte data-ink/minimalism and feature-creep/interaction-cost deny "more = better"; even opt-in detail has residual cost. Folded as the scope guard restricting the premise to the on-demand structure.
  Confidence: Moderate
  Applicable to: Sociogram pop-ups; any C2A2 overview where added detail can be deferred to an on-demand layer.
  Re-check due: 2026-09-19 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: PRESUMPTION with MODERATE-STRONG canonical support and only WEAK-MODERATE challenge -> INCORPORATE-with-guard is warranted (challenge is weak, not strong, so the "PRESUMPTION+strong-challenge->REVISE" heuristic does not trigger). The defensible core (progressive disclosure) is incorporated; the over-general "more = better" rationale is withheld. Consistency-checked vs PREMISE-001..067 and vs REVISE-122 (resolvability != fidelity): no conflict — both withhold "more visible/more info = automatically better."

**Total new PREMISEs this run (2026-06-19): 3 (PREMISE-066 SSOT single-source bios; PREMISE-067 golden-path guarded regen wrapper; PREMISE-068 details-on-demand pop-ups). 2 stated ASSUMPTIONs + 1 PRESUMPTION (367, the first PRESUMPTION-class INCORPORATE in several runs — admitted because its challenge was only weak-moderate and its support canonical). Cumulative through PREMISE-068. All three carry explicit scope guards withholding the over-claim step (tested-extraction-boundary; guard-in-code; withhold 'more=better').**

PREMISE-069:
  Date validated: 2026-06-23
  Source item: ASSUMPTION-335
  Statement: The post-Apr-6 "token cliff" was a schema-migration read-path artifact (token_usage relocated to agent_payload.token_usage, zeroing single-path reads), not an output collapse; a both-paths read recovers a continuous, growing output series. This is an instance of the documented silent-schema-zeroing failure class.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Branch Boston (schema-evolution silent field-relocation zeroing reads); Functionize/Airbyte data-migration silent-corruption testing; C2A2-internal both-paths live-db probe (06-22) recovering a continuous growing series.
  Challenges noted: 15b NO-CHALLENGE-FOUND to the fact (only a weak boundary note that one recovered read path is not a whole-pipeline clean bill — that caution is routed to REVISE-131/134, not against this premise).
  Confidence: High
  Applicable to: token/yield telemetry reads; any derived-metric pipeline crossing the 2026-04-07 schema boundary; historical yield comparisons (read via both paths).
  Re-check due: 2026-09-23 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: SUPPORTED (Moderate-Strong) + empirically GROUNDED + NO-CHALLENGE to the artifact reading -> INCORPORATE. SCOPE GUARD (load-bearing): incorporates ONLY the artifact explanation of the post-Apr-6 cliff; the generalizations "trust all downstream yields" (ASSUMPTION-336 -> REVISE-131) and "the fix is durable / no recurrence guard needed" (PRESUMPTION-373 -> REVISE-134) are explicitly WITHHELD. Consistency-checked vs PREMISE-001..068 and the silent-degradation family (PREMISE-049, REVISE-129): no conflict — same failure class, here correctly diagnosed and bounded.
PREMISE-070:
  Date validated: 2026-06-23
  Source item: ASSUMPTION-337
  Statement: Since 06-16 the binding constraint on the proposal pipeline is human review throughput, not literature discovery (review-bound). By Theory of Constraints, other stages should be subordinated to review — i.e., do not over-feed intake while review is the bottleneck.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Goldratt, Theory of Constraints (ASQ; leanproduction.com) — locate the constraint where WIP accumulates; Little's Law (ASQ; 6sigma.us); kanban/WIP-limit queuing guidance (kanbantool).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — TOC caution that a stage where WIP shows can be downstream of the true constraint (review latency could be readiness- not throughput-driven). Folded as the scope guard: confirm review latency is capacity- not rework-limited.
  Confidence: Moderate
  Applicable to: proposal-review workflow design; intake/WIP policy; 15-pipeline and self-awareness intake cadence.
  Re-check due: 2026-07-23 (Monthly; via 15d)
  Status: ACTIVE
  Rationale: SUPPORTED (Moderate) + only weak-moderate conditional challenge -> INCORPORATE with scope guard. Directly grounds workflow design and entails-against PRESUMPTION-372 (intake-as-progress -> REVISE-133): if review is the binding constraint, added intake is WIP, not progress. Consistency-checked vs PREMISE-001..069: no conflict.

**Total new PREMISEs this run (2026-06-23): 2 (PREMISE-069 token-cliff = schema read-path artifact [grounded, scoped]; PREMISE-070 proposal queue is review-bound [TOC/Little's law]). Both stated ASSUMPTIONs; both carry explicit scope guards withholding the over-claim step (over-trust generalizations -> REVISE-131/134; readiness-vs-throughput confirmation). Cumulative through PREMISE-070.**
PREMISE-071:
  Date validated: 2026-06-24
  Source item: ASSUMPTION-340
  Statement: Reconnecting a small set of high-centrality tradition hub pages restores graph reachability and integration more efficiently than seeding many peripheral leaves (hub leverage) — PROVIDED reconnection targets are chosen by bridging value (betweenness / community-spanning), not by degree alone.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Gomez, Centrality in Networks (finding most important nodes); MDPI Mathematics 9(18):2294 (important-node selection); module-based network analysis arXiv 1502.00353; GraphRAG well-placed-link value arXiv 2507.03226.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate): hubs maximize degree but often have LOW betweenness; the high-leverage integrators are bridge nodes (sometimes 'leaves'). Folded as the scope guard (select by bridging value, not degree).
  Confidence: Moderate
  Applicable to: graph-repair prioritization; sewing-agent reconnection policy; OPEN-088 seeding policy.
  Re-check due: 2026-07-24 (Monthly; via 15d)
  Status: ACTIVE
  Rationale: Moderate support + only weak-moderate conditional challenge -> INCORPORATE with scope guard. Consistency-checked vs PREMISE-001..070: no conflict.

PREMISE-072:
  Date validated: 2026-06-24
  Source item: ASSUMPTION-341
  Statement: Link-graph connectivity must be measured with path-aware (fully-qualified) wikilink resolution; basename-only resolution silently miscounts via cross-folder filename collisions and is an invalid measurement rule. Connectivity figures produced by a basename-only resolver are suspect until recomputed path-aware.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Path-resolution / normalization practice (canonicalization, collision handling); test-to-code traceability requiring fully-qualified keys; C2A2 silent-measurement family (PREMISE-049 verify-before-trust; schema-zeroing 369/373).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak): skew magnitude unknown until recomputed (could be near-null if no collisions); the replacement resolver must itself be verified (routed to REVISE-139).
  Confidence: Moderate
  Applicable to: connectivity_log.csv weekly series; any connectivity/orphan metric; OPEN-087 recompute task.
  Re-check due: 2026-07-24 (Monthly; via 15d)
  Status: ACTIVE
  Rationale: SUPPORTED principle + weak magnitude/boundary challenge -> INCORPORATE the measurement RULE. SCOPE GUARD (load-bearing): incorporates the principle that connectivity must be measured path-aware; does NOT certify the audit's own replacement resolver (uncross-checked self-trust -> PRESUMPTION-379/REVISE-139) and does NOT assert the skew magnitude (pending recompute). Same failure class as PREMISE-049/369/373; no conflict vs PREMISE-001..070.

PREMISE-073:
  Date validated: 2026-06-24
  Source item: ASSUMPTION-342
  Statement: For an unattended/autonomous run, high-impact or irreversible actions (e.g., a ~1,000-page bulk vault mutation) must be emitted as a report plus a ranked action list for human review, not executed. The rule is scoped to high-impact actions by tier (not a blanket ban on autonomous action), and reports must have a path to reviewed execution or they become HITL theater.
  Item type: ASSUMPTION (stated) — GROUNDED (the run enacted it)
  Supporting evidence: HITL agent design (NIST IR 8596; Galileo; Grizzly Peak HITL patterns); batch-review safe-autonomy (getmaxim.ai); C2A2 'caution over speed' rule + deferred-action monitor (Agent 16).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak): over-gating / 'HITL theater' — gating trivial actions causes rubber-stamping; an unread report is not safety. Folded as the scope guard (gate by impact tier; ensure reports convert to reviewed action).
  Confidence: High
  Applicable to: all autonomous agents (sewing agent; 14/15 self-awareness pipelines; deferred-action monitor Agent 16); unattended-run output policy.
  Re-check due: 2026-09-24 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: SUPPORTED (Strong) + GROUNDED + only weak scope-narrowing challenge -> INCORPORATE with scope guard. The inferred over-reach (autonomous INTERPRETIVE authority) is split to PRESUMPTION-382/REVISE-142. Consistent with the project caution rule and Agent 16; no conflict vs PREMISE-001..072.

PREMISE-074:
  Date validated: 2026-06-24
  Source item: ASSUMPTION-344
  Statement: A single index node (traditions/_index.md) linking the 15 tradition hub wikis mechanically de-orphans all 15 in one edit (orphan -> linked); GROUNDED and browser-verified. This is a navigational de-orphaning fact only and does not by itself establish improved analytical graph health.
  Item type: ASSUMPTION (stated) — GROUNDED (built + browser-verified)
  Supporting evidence: Graph degree mechanics; Wikipedia portal/index de-orphaning practice; in-session browser verification (06-23).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate): a universal index node is a maximal-degree hub that can dilute sociogram/community signal ('connects-all = distinguishes-nothing'). WITHHELD and routed to PRESUMPTION-381/REVISE-141.
  Confidence: High
  Applicable to: orphan remediation; vault navigation. NOT for sociogram/community-structure analysis (exclude the index node there).
  Re-check due: 2026-09-24 (Quarterly; via 15d)
  Status: ACTIVE
  Rationale: SUPPORTED (Strong) + GROUNDED for the narrow de-orphaning fact -> INCORPORATE (cf. PREMISE-069: grounded fact in, over-claims out). SCOPE GUARD: navigational de-orphaning fact ONLY; the analytical-health claim is withheld to REVISE-141. No conflict vs PREMISE-001..073.


**Total new PREMISEs this run (2026-06-24): 4 (PREMISE-071 hub-leverage reconnection [betweenness-guarded]; PREMISE-072 path-aware connectivity measurement [principle; replacement resolver NOT certified — see REVISE-139]; PREMISE-073 unattended high-impact actions = report-not-mutate [GROUNDED]; PREMISE-074 index-node de-orphaning [grounded navigational fact only — analytical-health claim withheld to REVISE-141]). 4 stated ASSUMPTIONs (two GROUNDED). All four carry explicit scope guards withholding the over-claim step (betweenness-not-degree; principle-not-resolver; impact-tier-not-blanket; navigational-not-analytical). Cumulative through PREMISE-074.**


## 2026-06-24 cohort INCORPORATE (15c 2026-06-25)

PREMISE-075:
  Date validated: 2026-06-25
  Source item: ASSUMPTION-347
  Statement: Robustness from an agent ensemble comes from error DECORRELATION (member diversity), which reference-frame variation supplies far more than random-seed/temperature resampling; identical agents at temperature chiefly expose stochastic variance. Realized robustness is conditional on MEASURED decorrelation across columns (see MONITOR-375).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Krogh & Vedelsby 1995 (ambiguity decomposition) (15a SUPPORTED/Strong)
  Challenges noted: 15b (Moderate): same-base-model columns can share errors; nominal diversity overstates effective diversity.
  Confidence: Moderate
  Applicable to: Pathway 31 ensemble design; any 'diversity vs redundancy' decision
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-301

PREMISE-076:
  Date validated: 2026-06-25
  Source item: ASSUMPTION-348
  Statement: A per-thinker/per-claim dissensus rate is a meaningful detector output (evidence about contested positions under rich information) ONLY once the measure's reliability is established and instrument noise separated from genuine variation; reported above a measured noise floor.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Plank 2022 (human label variation); Aroyo & Welty 2015 (15a SUPPORTED/Strong)
  Challenges noted: 15b (Moderate): much disagreement is annotation/instrument error; reliability must be demonstrated (VARIERR).
  Confidence: Moderate
  Applicable to: Constitutional detector output; dissensus-rate reporting
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-302

PREMISE-077:
  Date validated: 2026-06-25
  Source item: ASSUMPTION-350
  Statement: A single-thinker pilot can VALIDATE THE MECHANISM only in the necessary-condition / falsification sense: a clean failure refutes it, and a PASS establishes feasibility-in-one-favorable-case, NOT generalization across thinkers (generalization is deferred to multi-thinker replication; see MONITOR-374).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Leon et al. 2011 (pilot purpose); Flyvbjerg 2006 (critical case) (15a PARTIALLY-SUPPORTED/Moderate)
  Challenges noted: 15b (Moderate): pilots mislead about scalability; a PASS on a favorable case is weak evidence for generalization.
  Confidence: Moderate
  Applicable to: Hawkins pilot as falsification test; pathway gating
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-304

PREMISE-078:
  Date validated: 2026-06-25
  Source item: ASSUMPTION-352
  Statement: Self-testing is rendered substantially non-vicious by specifying the falsifier independently of outcomes (register, then look) - NECESSARY but sufficient only when the specification is exhaustive (thresholds, exclusions, analysis path pre-committed); register-then-look does not by itself supply personnel independence (see REVISE-146).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Simmons et al. 2011; Nosek et al. 2018; Mayo 2018 (15a SUPPORTED/Strong)
  Challenges noted: 15b (Moderate): vague preregistrations leak DoF; self-grading is not personnel independence.
  Confidence: Moderate
  Applicable to: The whole falsifier; self-testing protocol; discharges REVISE-111 (partial)
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-305

PREMISE-079:
  Date validated: 2026-06-25
  Source item: ASSUMPTION-353
  Statement: Usefulness must not be equated with productivity (Goodhart/Campbell), and the usefulness test must be ASYMMETRIC: a clean FAIL is decisive, a PASS licenses only 'necessary condition met, provisional'. Asymmetry blunts but does not fully eliminate gaming; necessary conditions must be tight and the test periodically red-teamed.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Goodhart/Strathern 1997; Campbell 1979; Mayo 2018 (15a SUPPORTED/Strong)
  Challenges noted: 15b (Weak): asymmetric/necessary-condition tests are still meta-gameable; not a complete firewall.
  Confidence: High
  Applicable to: Usefulness test design; anti-productivity-ism firewall; discharges REVISE-105
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-306

PREMISE-080:
  Date validated: 2026-06-25
  Source item: ASSUMPTION-355
  Statement: A pre-specified convergence battery of OPERATIONALLY INDEPENDENT indicators (no post-hoc weighting) is more robust and harder to spoof than any single indicator - CONDITIONAL on demonstrated independence (shared method variance yields pseudo-convergence). Extends the existing triangulation/overdetermination premise.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Campbell & Fiske 1959 (MTMM); Wimsatt 1981; Munafo & Davey Smith 2018 (15a SUPPORTED/Strong)
  Challenges noted: 15b (Moderate): indicators sharing method/source give pseudo-robustness; independence must be measured, not assumed.
  Confidence: High
  Applicable to: Convergence-battery design; falsifier indicator selection; extends existing triangulation premise
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-308

PREMISE-081:
  Date validated: 2026-06-25
  Source item: ASSUMPTION-357
  Statement: Because real synthesis often coins NEW vocabulary, a shared-identifier test has a non-trivial false-negative rate; an honest synthesis instrument needs a contemporaneous derived_from lineage field, and the test must be instrumented (false-negative rate measured) before it is trusted.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Fauconnier & Turner 2002 (blending); Small 1973 (co-citation false negatives) (15a SUPPORTED/Moderate)
  Challenges noted: 15b (Weak): not all synthesis coins new terms; lineage fields add maintenance error - measure the false-negative rate before heavy investment.
  Confidence: Moderate
  Applicable to: Synthesis-detection instrument; OPEN-091; miss-direction of shared-id test
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-310

PREMISE-082:
  Date validated: 2026-06-25
  Source item: ASSUMPTION-360
  Statement: For a public artifact, a local/offline path plus an own-key provider plus a local-search fallback is more resilient than single shared-broker dependence (removes a single point of failure) - CONDITIONAL on each fallback path being actually exercised/tested and provider keys not being exposed client-side (see REVISE-144).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Avizienis et al. 2004 (dependability); Kleppmann et al. 2019 (local-first) (15a SUPPORTED/Moderate)
  Challenges noted: 15b (Weak): redundancy adds complexity/inconsistency; client-held keys re-import secret-exposure risk.
  Confidence: Moderate
  Applicable to: Public-artifact provider architecture; resilience/independence design value
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-312

PREMISE-083:
  Date validated: 2026-06-26
  Source item: ASSUMPTION-364
  Statement: Archiving a History snapshot only when content changes (one entry per real update) is the correct anti-duplication rule - CONDITIONAL on comparing a CANONICALIZED form: normalize away non-semantic differences (timestamps, key ordering, whitespace) before change-detection, and ensure the compared content covers the semantic fields of interest, or the same rule yields either churn (false-positive entries) or silent misses (false-negative entries).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Quinlan & Dorward 2002 (Venti content-addressable storage); Git object model; rsync/content-defined chunking (15a SUPPORTED/Moderate)
  Challenges noted: 15b (Weak): change-detection on a non-canonical form churns on non-semantic diffs; a coarse digest misses real changes - define the canonical comparison.
  Confidence: Moderate
  Applicable to: History/snapshot archival; dedup logic; metabolism/heartbeat snapshotting
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-327

PREMISE-084:
  Date validated: 2026-06-26
  Source item: ASSUMPTION-367
  Statement: A change signal should fire only on a real change (new papers) and show a calm 're-checked' on a no-change re-poll - signalling change only when change is real preserves the signal's information value and reflects true system status (honesty refinement). CONDITIONAL on the new/same detector being accuracy-validated (false-positive/negative rates measured) and the calm 're-checked' cue not being over-shown to the point of habituation.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Alarm-fatigue/signal-detection literature; NN/G visibility-of-system-status; Gray et al. 2018 (deceptive design) (15a SUPPORTED/Moderate)
  Challenges noted: 15b (Weak): honesty is only as good as the new/same classifier; a misfiring detector reintroduces false alarms or hides real updates; an over-shown calm cue habituates.
  Confidence: Moderate
  Applicable to: Honesty layer; change/freshness indicators (Heartbeat, paper-poll UIs); aligns with PREMISE-078 (register-then-look honesty)
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-329

PREMISE-085:
  Date validated: 2026-06-26
  Source item: ASSUMPTION-371
  Statement: launchd (or equivalent OS supervisor, e.g. systemd) is the correct posture for SINGLE-NODE process liveness and reboot restart of the backend (restart-on-crash + start-at-boot; aligns with crash-only-software design). SCOPED CAVEAT: 'durable/reboot-safe' here means PROCESS liveness only - it does NOT provide (i) DATA durability (in-flight writes surviving a crash; that requires crash-consistent storage - see PRESUMPTION-405/MONITOR-390), nor (ii) HIGH AVAILABILITY (a single supervised node remains a single point of failure - see PRESUMPTION-404/MONITOR-389).
  Item type: ASSUMPTION (stated)
  Supporting evidence: Apple launchd / launchd.plist (KeepAlive, RunAtLoad); systemd Restart=; Candea & Fox 2003 (Crash-Only Software) (15a SUPPORTED/Moderate)
  Challenges noted: 15b (Moderate): 'durable' conflates process liveness with data durability and availability; supervision does neither - state the posture narrowly to single-node process liveness.
  Confidence: Moderate
  Applicable to: OpenStory backend durability posture; single-node service supervision. Consistency: compatible with PREMISE-082 (multi-provider/local-first no-SPOF resilience is a separate provider-layer value, not contradicted by single-node process supervision).
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-331

PREMISE-086:
  Date validated: 2026-06-27
  Source item: ASSUMPTION-376
  Statement: A silent multi-day pipeline stall is made visible by surfacing the AGE of the last dated PASS/FAIL in a daily health report and ALARMING on staleness (time-since-last-PASS > threshold) - absence/staleness is the signal (dead-man's-switch / heartbeat pattern). CONDITIONAL: the report must alarm on AGE rather than merely display the last-known value (else it becomes the perceived-liveness trap), and the report/monitor must have its own independent liveness check (monitor-of-monitor) so it cannot freeze unnoticed.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Dead-man's-switch / watchdog-timer & heartbeat monitoring; Google SRE Book (freshness / absence-of-signal alerting); Nagios/Prometheus staleness (time-since-last-success) checks (15a SUPPORTED/Strong)
  Challenges noted: 15b (Moderate): a displayed-not-alarmed stale PASS hides the stall; the report generator can itself stall unnoticed; passive surfacing depends on intermittent human reading. All addressed by the conditions in the statement.
  Confidence: High
  Applicable to: OpenStory / health-report monitoring; keystone OPEN-086 liveness; any scheduled pipeline. Complements PREMISE-084 (signal-change-only-on-real-change) and binds REVISE-147 (scheduler dead-man's-switch). Member of the silent-failure / fail-loud cluster.
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-343

PREMISE-087:
  Date validated: 2026-06-27
  Source item: ASSUMPTION-381
  Statement: Representing a signal with two independent timestamps - a formation/event time and a source/vintage time (a bitemporal valid-time vs transaction-time split) - is the honest encoding, because it avoids conflating when-something-happened with when-it-was-recorded. CONDITIONAL: the event each timestamp denotes must be explicitly defined; in particular the choice of WHICH event counts as "formation" (proposal-authoring vs idea-engagement vs approval) is a separate modeling decision tracked under PRESUMPTION-410 / MONITOR-398, not settled by this premise.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Snodgrass, "Developing Time-Oriented Database Applications in SQL" (bitemporal); SQL:2011 temporal features (application-time period + system-versioned tables); data-provenance/lineage practice (15a SUPPORTED/Strong)
  Challenges noted: 15b (Weak-Moderate): the dual structure is sound but the semantics of "formation" are contestable and a strictly honest model may need >2 timestamps; the semantic choice is routed to PRESUMPTION-410. Member of the event-time/temporal-boundary cluster.
  Confidence: High
  Applicable to: cross-tradition signal dating; any dataset distinguishing occurrence time from record/source time.
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-345

PREMISE-088:
  Date validated: 2026-06-29
  Source item: ASSUMPTION-385
  Statement: Bulk automated ("agentic-call") boilerplate injection into many knowledge-base pages should NOT be executed unsupervised. Bulk/templated edits are a recognized quality risk and are conventionally gated behind human review or a small pilot; mass-injecting process-log-style boilerplate tends to add navigational/process noise rather than substantive synthesis hooks. CONDITIONAL: this validates "gate-or-pilot before bulk-acting," NOT an absolute "never" — a small pilot (10-20 pages) and/or a redesign of the injected content toward genuine synthesis prompts may make a targeted version worthwhile. The blanket prediction that injection would necessarily be pure noise is a forward prediction, not established.
  Item type: ASSUMPTION (stated)
  Supporting evidence: MediaWiki bot-edit guidance ("boilerplate changes should always be human checked"); Wikidata automation-quality concerns; knowledge-base template-pollution discussions (15a SUPPORTED/Moderate).
  Challenges noted: 15b (Moderate): bulk templated edits are mainstream and value-adding when well-designed; the real lesson is "human-check / pilot them," not "never"; the noise outcome is untested and may reflect template design. Captured by the CONDITIONAL.
  Confidence: Moderate
  Applicable to: the Phase 3 orphan/connectivity remediation decision; any bulk agentic edit to vault pages. Complements PREMISE-086 (fail-loud / verify-completeness) and the surgical-change discipline.
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-356


PREMISE-089:
  Date validated: 2026-06-30
  Source item: ASSUMPTION-390
  Statement: Freshness/liveness is a per-source property; the liveness of any one feed (e.g., the OpenStory activity feed) must never be taken as evidence for the liveness of another (PRS approval axis, signals axis). Each axis requires its own freshness signal. Refinement: freshness-independence does NOT imply failure-independence — feeds sharing an upstream scheduler can freeze together, so per-source freshness tracking must coexist with shared-failure awareness.
  Item type: ASSUMPTION (stated)
  Supporting evidence: per-source data-freshness doctrine (Elementary Data; Sifflet "stale data looks perfectly normal"; Metaplane; "data downtime") — freshness is measured per source and cross-source liveness inference is a known anti-pattern (15a SUPPORTED/Strong).
  Challenges noted: 15b (Weak/NO-CHALLENGE): no source disputes the claim; only refinement is that shared upstream schedulers create common-mode failure (captured in the Statement).
  Confidence: Moderate
  Applicable to: metabolism/heartbeat display, approval-axis dashboards, any multi-feed visualization. Complements PREMISE-086 (fail-loud / verify-completeness). Binds P-422 (per-axis as-of marking, REVISE-158) and P-421 (freshness watchdog, REVISE-157).
  Re-check due: Monthly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-366


PREMISE-090:
  Date validated: 2026-07-01
  Source item: ASSUMPTION-393
  Statement: For a one-time, quality-sensitive backlog whose extraction errors propagate into a validated-premise register, an attended (human-in-the-loop) ingestion pass is justified over an unbounded unattended agent — because HITL measurably reduces extraction error and catches mid-pass anomalies (QC drops, keying bugs) an unattended agent would commit silently. SCOPE CAVEAT: this justifies attended passes as ONE-TIME remediation only, NOT as the standing ingestion cadence (HITL does not scale; the mature steady-state pattern is human-on-the-loop bounded automation).
  Item type: ASSUMPTION (stated)
  Supporting evidence: HITL extraction literature (IMS Datawise; Forage.ai — 30-40% error reduction; Docsumo; Digital Divide Data HITL-vs-automation framework); C2A2-internal (the attended pass caught the 8-of-152 QC drops and the proposal_id keying bug A-396 mid-pass). 15a SUPPORTED/Moderate-Strong.
  Challenges noted: 15b (Moderate): HITL does not scale; attended-vs-unattended is a false dichotomy (human-on-the-loop); the one-shot pass leaves recurrence unaddressed (P-425 -> REVISE-161). Captured by the SCOPE CAVEAT.
  Confidence: Moderate
  Applicable to: OPEN-101 backlog clears; any one-time quality-sensitive ingestion remediation. Pairs with REVISE-161 (the cadence gap). Complements PREMISE-088 (bulk-edit human-check discipline).
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-374


PREMISE-091:
  Date validated: 2026-07-01
  Source item: ASSUMPTION-398
  Statement: A visual check of the rendered artifact is required before publish even after programmatic green, because visual/rendering defects routinely survive functional CI (defect-escape rises ~25% without a review layer adapted to that gap). For C2A2's current bespoke, low-frequency publishes a human eyeball is the appropriate gate; where publishes become frequent/templated, an automated visual-regression diff should take the primary role, with human review reserved for flagged diffs.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Visual-testing literature (Testmetry; BrowserStack; Percy/Applitools — visual regressions pass unit/e2e); Gartner 2024 defect-escape +25% without adapted review; C2A2-internal (the stale-axis mislead REVISE-158 was a programmatic-green-but-visually-wrong case). 15a SUPPORTED/Moderate-Strong.
  Challenges noted: 15b (Weak-Moderate): "must be a live HUMAN eyeball" over-commits where automated visual regression applies; mandatory manual gates habituate into rubber-stamping. Captured by the automated-where-templated refinement.
  Confidence: Moderate
  Applicable to: No-Blind-Push publish gate; all human-facing visualization publishes. Complements PREMISE-089 (per-axis freshness) and REVISE-158.
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-376


PREMISE-092:
  Date validated: 2026-07-01
  Source item: ASSUMPTION-400
  Statement: Safe recovery of a large corrupt SQLite database follows this sequence: (1) stop all writers; (2) take a raw file-level copy of the corrupt DB first (belt); (3) confirm SQLite >= 3.51.3 (fixes the 2026-03 WAL-reset corruption bug present 3.7.0-3.51.2); (4) checkpoint/backup via the online backup API (which copies consistently); (5) .recover into a FRESH file; (6) PRAGMA integrity_check on the fresh file; (7) swap in and remove stale -wal/-shm files. Corruption risk concentrates at checkpoint and around leftover wal/shm paired with a swapped main file.
  Item type: ASSUMPTION (stated)
  Supporting evidence: sqlite.org (How To Corrupt An SQLite Database File; WAL docs; backup API; 2026-03 WAL-reset bug notice); runebook WAL recovery guide. 15a SUPPORTED/Strong.
  Challenges noted: 15b (Weak): the backup API tolerates a live writer (so "live writer compounds corruption" slightly overstates risk); check SQLite version; raw-copy before any checkpoint. All folded into the Statement as refinements.
  Confidence: High
  Applicable to: OpenStory DB recovery (A-399 dependency); any large-SQLite recovery in C2A2. Complements PREMISE-086 (fail-loud / verify-completeness).
  Re-check due: Quarterly (next 15d review)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-377


PREMISE-093:
  Date validated: 2026-07-02
  Source item: ASSUMPTION-402
  Statement: An unattended C2A2 run must not enter or borrow the user's credentials; a logged-out claude.ai (or any credential-bearing / irreversible action) is a legitimate hard stop for the gated action. However, the hard stop must be paired with a context-bearing escalation to the human, not a silent termination — the safe unattended behavior is "refuse the gated action AND alert," so a human can close the loop promptly.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Ping Identity "Identity for AI: Agentic IAM" (agents must never log in with / borrow a human's credentials; scoped ephemeral-token delegation is canonical); Elementum/Galileo/TeamCopilot HITL best-practice (authentication / irreversible actions are human-gated); reaffirms C2A2 PREMISE-015 (ASSUMPTION-079 / DECISION-022 no-credential-handling). 15a SUPPORTED/Strong.
  Challenges noted: 15b (Moderate, scoped): the "hard stop" clause, taken as a silent terminal stop, is the silent-failure anti-pattern; the endorsed posture is stop + escalate with context (incident.io/OneUptime dead-man's-switch; DigitalApplied HITL escalation). Folded into the Statement as the escalation caveat.
  Confidence: Moderate-High
  Applicable to: all autonomous scheduled runs; any credential-bearing or irreversible action; the human-context loop (claude.ai session). Reinforces PREMISE-015; operationalizes PREMISE-006 (transparent-flagging) and PREMISE-086 (fail-loud) for the auth blocker; pairs with REVISE-169 (logout-SPOF escalation).
  Re-check due: Quarterly (next 15d review; pairs with PREMISE-015 re-check)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-386

PREMISE-094:
  Date validated: 2026-07-03
  Source item: ASSUMPTION-406
  Statement: When observations are nested within conversations, the conversation is the honest unit of replication, and inference must be clustered at the conversation level rather than pseudoreplicated on turns/utterances. This unit choice is uncontested. However, at small cluster counts (e.g. k=5) the correct unit does NOT license standard cluster-robust confidence intervals: cluster-robust CIs are asymptotic in the number of clusters and over-reject badly at k≈5, so small-cluster-valid procedures (wild-cluster bootstrap or randomization/permutation inference) must be used and interval fragility reported. In short: right unit, but not "clustered CIs are automatically correct" at small k.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Hurlbert 1984 (pseudoreplication — the honest replicate is the randomized unit); Cameron & Miller 2015 and Aarts et al. 2014 (nested data must be analyzed at cluster level or with mixed models). 15a SUPPORTED/Strong for the unit.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate-Strong), scoped to the estimator not the unit — MacKinnon & Webb 2018 and Cameron/Gelbach/Miller 2008 (cluster-robust CIs unreliable / anticonservative at few clusters; even wild-cluster bootstrap and RI strain at k≈5). Folded into the Statement as the small-cluster caveat.
  Confidence: Moderate-High
  Applicable to: all C2A2 empirical cells with nested/clustered dialogue data; the Inter-Tradition Dialogue Study inference (constrains A-404's +0.086 effect and A-410; pairs with MONITOR-415 / PRESUMPTION-439's stability question); any conversation-level statistic. Complements the verification-discipline family and PREMISE-086 (fail-loud/monitor).
  Re-check due: Quarterly (next 15d review; stable methodological premise)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-392

---

## 2026-07-06 — Monthly INCORPORATED-premise re-check results (15c; c2a2-lit-search-pipeline)

All three due re-checks RE-CONFIRMED (no premise re-opened): PREMISE-002 (DISPOSITION-408; embedding displacement vectors — new 2025 theory support; caveats: similarity miscalibration, length collapse), PREMISE-004 (DISPOSITION-409; triangulation — Strong new support; independence proviso sharpened: same-model-family convergence is not independent evidence, cross-ref REVISE-174 and SYSTEMIC-RISK #3 of 2026-07-06), PREMISE-025 (DISPOSITION-410; missed-cycle visibility — Strong continued support; caveats: alert-fatigue filtering, time-boxed classification). Full records in lit_search_returns.md; result files use suffix _recheck-2026-07-05 in lit_search_results/{for,against}/. Next re-check due 2026-08-02.
