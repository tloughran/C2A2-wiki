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

**Re-check due:** 2026-11-01 (Quarterly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-09-06 (Monthly) [re-checked by 15d 2026-07-05; re-confirmed ACTIVE by 15c 2026-07-06, DISPOSITION-408 — new caveats: per-space similarity calibration required; control document length (embedding collapse)] [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-09-06 (Monthly — monitor independence of C2A2 findings) [re-checked by 15d 2026-07-05; re-confirmed ACTIVE by 15c 2026-07-06, DISPOSITION-409 — independence proviso sharpened: correlated LLM errors (Kim et al. ICML 2025) mean same-model-family convergence is NOT independent evidence; count same-mechanism/same-family lines as one; binds REVISE-174] [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly — vendor ToS / feature evolution could shift collaborator-scope claims) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly via 15d) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly via 15d) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-11-01 (Quarterly via 15d) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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

**Re-check due:** 2026-09-06 (Monthly) [re-confirmed ACTIVE by 15c 2026-07-06, DISPOSITION-410 — caveats: time-box classification ahead of reversible fixes; severity-filter miss alerts (2026 alert-fatigue data)] [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]

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
  Re-check due: 2026-09-06 (Monthly; via 15d) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]
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
  Re-check due: 2026-09-06 (Monthly; via 15d) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]
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
  Re-check due: 2026-09-06 (Monthly; via 15d) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]
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
  Re-check due: 2026-09-25 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-25 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-25 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-25 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-25 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-25 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-25 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-25 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-26 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-26 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-26 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-27 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-27 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-29 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-09-06 (Monthly) [re-checked by 15d 2026-08-02; re-queued in for_lit_search.md]
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
  Re-check due: 2026-10-01 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-10-01 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-10-01 (Quarterly) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-10-02 (Quarterly (next 15d review; pairs with PREMISE-015 re-check)) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
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
  Re-check due: 2026-10-03 (Quarterly (next 15d review; stable methodological premise)) [concrete date assigned by 15d 2026-08-02 — entry previously carried no date and was invisible to a date-driven monitor; date = validation date + 3 months]
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-392

---

## 2026-07-06 — Monthly INCORPORATED-premise re-check results (15c; c2a2-lit-search-pipeline)

All three due re-checks RE-CONFIRMED (no premise re-opened): PREMISE-002 (DISPOSITION-408; embedding displacement vectors — new 2025 theory support; caveats: similarity miscalibration, length collapse), PREMISE-004 (DISPOSITION-409; triangulation — Strong new support; independence proviso sharpened: same-model-family convergence is not independent evidence, cross-ref REVISE-174 and SYSTEMIC-RISK #3 of 2026-07-06), PREMISE-025 (DISPOSITION-410; missed-cycle visibility — Strong continued support; caveats: alert-fatigue filtering, time-boxed classification). Full records in lit_search_returns.md; result files use suffix _recheck-2026-07-05 in lit_search_results/{for,against}/. Next re-check due 2026-08-02.

---

## 2026-07-09 — INCORPORATE from fresh-cohort run (15c; c2a2-lit-search-pipeline; autonomous)

PREMISE-095:
  Date validated: 2026-07-09
  Source item: ASSUMPTION-429
  Statement: Under current provisioning (one scheduled pipeline run/day at an observed 7-20 items/run), the 15d weekly re-trigger arrival rate (~55/week) exceeds the service rate; the refresh queue grows without bound absent a cadence change, admission cap, or throughput/provisioning increase. "Structural" means structural-under-current-provisioning, not immutable — throughput is itself a design choice (runs/day, parallelism, batch size), so provisioning increases are part of the remedy space alongside cadence/cap redesign.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Little (1961) L=lambda*W; Hopp & Spearman, Factory Physics (rho>1 implies unbounded backlog); empirical run logs 2026-07-05..07-09 (arrival ~55/week vs burns of 7-20/run; backlog 116 and monotone across 5 runs). 15a SUPPORTED/Strong.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — scoped to the wording, not the arithmetic: "structural" overstates if provisioning is variable. Folded into the Statement.
  Confidence: Moderate (QUEUED-EMPIRICAL residue: precise lambda/mu instrumentation still recommended)
  Applicable to: OPEN-115/OPEN-116 (cadence/cap decision); 15d re-trigger design; A-428/MONITOR-420 (deferral acceptability); A-430/MONITOR-423 (triage); run scheduling. Consistency: consonant with the validated human-review-capacity-as-binding-constraint premise; CONTRADICTS P-462 as held — dispositioned REVISE-195 rather than silently coexisting.
  Re-check due: 2026-08-09 (Monthly)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-431


---

## 2026-07-16 — INCORPORATE from 15a/15b/15c pipeline run (autonomous; 07-13/07-14-backfill/07-15 batches)

PREMISE-096:
  Date validated: 2026-07-16
  Source item: ASSUMPTION-452
  Statement: No self-produced artifact may certify itself. Each artifact class is verified by an independent source — tooling by replay (re-run the corrected tool over prior inputs and diff), denominators by independent corroboration, captures by primary-text verification. Apply proportional to stakes (SLSA-style level tiering), and require that the corroborating layer draw on a genuinely disjoint evidence source, or "independent" is nominal only.
  Item type: ASSUMPTION (stated)
  Supporting evidence: SLSA v1.1 spec/FAQ (self-generated L1 provenance carries no integrity guarantee; L2+ requires platform-generated, independently-verifiable provenance) — the framework independently instantiates this exact rule. 15a SUPPORTED/Strong.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak) — cost/calibration only: a uniform mandate can impose verification cost disproportionate to risk and a perfunctory required check can masquerade as assurance (Knight & Leveson common-mode caveat). Folded in as the stakes-proportional + source-independence provisos.
  Confidence: High
  Applicable to: the verification-discipline family; watchdog output checks; capture pipeline; agents 15a/15b/15c; denominator/census reporting. THIS PREMISE IS THE PROPOSED TERMINATOR FOR SYSTEMIC-RISK #1 — it unifies REVISE-209 (denominators), REVISE-213 (tooling/replay), and REVISE-214 (captures/primary-text) under one rule.
  Re-check due: 2026-10-16 (Quarterly)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-473

PREMISE-097:
  Date validated: 2026-07-16
  Source item: ASSUMPTION-457
  Statement: A report drawn from a bounded observational vantage must disclose its scope gap rather than imply coverage it lacks. Sandbox-visible process data is not represented as host-wide coverage; any monitoring/status report states the boundary of what it could observe.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Observability-scope / trace-coverage literature (incomplete instrumentation overstates coverage; arXiv:2604.13522) and survivorship-bias canon (Wald; concentrating on the observable subset and implying it is the whole distorts conclusions). 15a SUPPORTED/Strong.
  Challenges noted: 15b NO-CHALLENGE-FOUND (None) — the honesty/scope-disclosure norm is uncontested.
  Confidence: High
  Applicable to: all monitoring/status reports from a bounded vantage; scheduler watchdog; self-awareness-pipeline coverage claims (pairs with MONITOR-443's coverage-ratio). Consistent with the verify-before-trust / fail-loud premise family. The specific scope fact (sandbox cannot enumerate host processes) remains a one-command empirical check.
  Re-check due: 2026-10-16 (Quarterly)
  Status: ACTIVE
  PROVENANCE: Origin 14a; Chain [14a -> 15a, 15b -> 15c]; DISPOSITION-481

PREMISE-098:
  Date validated: 2026-07-18
  Source item: PRESUMPTION-490
  Statement: Scripts that run correctly interactively on the Mac must NOT be presumed to behave identically when invoked headless by the scheduler in the sandbox. Each scheduled/autonomous script asserts its context invariants — HOME, filesystem/mount reach, credentials, lock state — at startup and fails loud on violation. Cross-context parity is engineered, not assumed; a per-delta startup preflight is required, full hermeticity is not.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: designers were unaware)
  Supporting evidence: 12-Factor "Dev/prod parity"; Bazel "Hermeticity"; Cronitor "Crontab environment variables" (scheduler supplies its own minimal environment). Twice-falsified in vivo 2026-07-17 (metabolism `~/`, c282 index.lock). 15a SUPPORTED/Strong.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — perfect parity/hermeticity is unattainable (12-Factor concedes it; no studied Bazel project is fully hermetic), so the remedy is a TARGETED preflight on the named deltas, not a hermetic rebuild. Folded into the statement.
  Confidence: Moderate
  Applicable to: all scheduled/autonomous agents and regen scripts (metabolism, OpenStory writer, git-persistence, 14/15 pipelines). Complements the durability/fail-loud family and pairs with P-491 (artifact-binding) and the 2026-07-17 decoupled-from-ground-truth SYSTEMIC-RISK flag.
  Re-check due: 2026-10-18 (Quarterly)
  Status: ACTIVE
  PROVENANCE: Origin 14b; Chain [14b -> 15a, 15b -> 15c]; DISPOSITION-500

---

# ===== 2026-07-19 Agent 15c dispositions — 2026-07-18 EOD batch (12 items) =====

PREMISE-099:
  Date validated: 2026-07-19
  Source item: ASSUMPTION-469
  Statement: A documented-discrepancy flag that annotates without gating does not prevent the discrepant value from being emitted into outbound artifacts; deferability of a known error is a property of its enforcement point, not of its documentation.
  Item type: ASSUMPTION (stated)
  Supporting evidence: see lit_search_results/for/ASSUMPTION-469_for.md (15a: SUPPORTED, Moderate-Strong)
  Challenges noted: see lit_search_results/against/ASSUMPTION-469_against.md (15b: PARTIALLY-CHALLENGED, Moderate)
  Confidence: High
  Applicable to: Outbound artifact emission (Gmail drafts, reports, review pages); count-reporting paths; any known-error register in the system.
  Re-check due: 2026-10-19 (Quarterly)
  Status: ACTIVE

PREMISE-100:
  Date validated: 2026-07-19
  Source item: ASSUMPTION-472
  Statement: A liveness signal (lastRunAt / heartbeat) is not evidence of correctness, and a health check that cannot execute in its runtime context reports as passing rather than as absent; monitoring that conflates the two produces false-green at a rate proportional to the number of inoperable checks.
  Item type: ASSUMPTION (stated)
  Supporting evidence: see lit_search_results/for/ASSUMPTION-472_for.md (15a: SUPPORTED, Strong)
  Challenges noted: see lit_search_results/against/ASSUMPTION-472_against.md (15b: PARTIALLY-CHALLENGED, Moderate)
  Confidence: High
  Applicable to: Scheduler watchdog; fleet health reporting; any agent self-report that renders a green state; the 36-task 'healthy' population.
  Re-check due: 2026-10-19 (Quarterly)
  Status: ACTIVE

PREMISE-101:
  Date validated: 2026-07-19
  Source item: PRESUMPTION-494
  Statement: Counts over shared artifacts are properties of a reading — a (scope, method, time) tuple — not properties of the artifact; absent a designated counting authority and a recorded method, independent agents will produce divergent counts of the same object without either being wrong.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: see lit_search_results/for/PRESUMPTION-494_for.md (15a: SUPPORTED, Strong)
  Challenges noted: see lit_search_results/against/PRESUMPTION-494_against.md (15b: PARTIALLY-CHALLENGED, Moderate)
  Confidence: High
  Applicable to: Proposal counts, scheduled-task counts, PRS counts, failure counts; every agent report that states a quantity over a shared artifact; outbound communications quoting figures.
  Re-check due: 2026-10-19 (Quarterly)
  Status: ACTIVE

PREMISE-102:
  Date validated: 2026-07-19
  Source item: PRESUMPTION-495
  Statement: Fail-loud is an act of reporting, not an act of remediation. Where the notified channel has demonstrated zero throughput, repeated identical non-processing converts a one-time signal into an undecided standing policy of non-coverage; the loudness of the report is not evidence that anything is receiving it.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: see lit_search_results/for/PRESUMPTION-495_for.md (15a: SUPPORTED, Strong)
  Challenges noted: see lit_search_results/against/PRESUMPTION-495_against.md (15b: PARTIALLY-CHALLENGED, Moderate)
  Confidence: High
  Applicable to: All EOD pipeline runs; the lit-search and self-awareness queues; the 29-proposal approval backlog; any agent convention of flagging in lieu of acting.
  Re-check due: 2026-08-19 (Monthly)
  Status: ACTIVE

PREMISE-103:
  Date validated: 2026-07-19
  Source item: PRESUMPTION-497
  Statement: Absence of primary text is a kind-difference in evidence, not a degree-difference: no confidence label over metadata-only material is well-founded, and downgrading confidence is not a valid substitute for an explicit 'unfounded pending retrieval' state.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: see lit_search_results/for/PRESUMPTION-497_for.md (15a: PARTIALLY-SUPPORTED, Moderate)
  Challenges noted: see lit_search_results/against/PRESUMPTION-497_against.md (15b: NO-CHALLENGE-FOUND, None)
  Confidence: Moderate
  Applicable to: PRS candidate admission; all confidence labelling under blocked primary sources; REVISE-214 and ASSUMPTION-470 both depend on this premise.
  Re-check due: 2026-10-19 (Quarterly)
  Status: ACTIVE

PREMISE-104:
  Date validated: 2026-07-19
  Source item: PRESUMPTION-498
  Statement: Append-only operational and registry files have no size bound and no rotation policy anywhere in the pipeline; read cost per run grows monotonically and daily full backups make storage grow quadratically in days. No agent currently budgets read cost against context.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: see lit_search_results/for/PRESUMPTION-498_for.md (15a: SUPPORTED, Moderate-Strong)
  Challenges noted: see lit_search_results/against/PRESUMPTION-498_against.md (15b: PARTIALLY-CHALLENGED, Moderate)
  Confidence: Moderate
  Applicable to: assumptions.md, presumptions.md, for_lit_search.md, lit_search_returns.md, monitor_queue.md, watch_list.md; every agent that reads a registry whole.
  Re-check due: 2026-08-19 (Monthly)
  Status: ACTIVE
  Novelty note: 15a found no literature budgeting read cost for agents ingesting monolithic state files under a queryable-history constraint. Potential original contribution — carried to 15d.


---

# ===== 2026-07-20 Agent 15c dispositions — 2026-07-19 EOD batch (14 items) =====

*Cohort note: 6 of 14 items INCORPORATED. In every case where 15b's SYSTEMIC-RISK-FLAG "REMEDY-INHERITS-DEFECT" (2026-07-20, High) named the item, the premise below is deliberately narrowed to the OBSERVATION and the proposed remedy is EXCLUDED and routed to REVISE-236. A premise that carried its own defective instrument would install the failure it describes.*

PREMISE-105:
  Date validated: 2026-07-20
  Source item: ASSUMPTION-474
  Statement: A change in the definition of what is counted makes adjacent periods of a series non-comparable — a break in the time series — and a delta spanning the change is uninterpretable until the definitional component is measured, not estimated. Separately, an artifact-volume count is not a measure of knowledge-graph health; it is a proxy subject to Goodhart's law. NARROWING (load-bearing): this premise validates the DIAGNOSIS only. It does NOT validate (i) the ~+145 / ~+80 partition, which is an estimate asserted before the frozen-snapshot dual-resolver run that would establish it and must not be quoted as a finding; (ii) the framing of break-marking and re-derivation as equal options — official-statistics practice (Eurostat backcasting) treats correction as the standard and marking as the fallback used when correction is infeasible; (iii) connectivity as the replacement metric, which is subject to the identical Goodhart argument and is directly writable by the agents being measured. The literature's own remedy is a small panel with no single member targeted.
  Item type: ASSUMPTION (stated)
  Supporting evidence: see lit_search_results/for/ASSUMPTION-474_for.md (15a: SUPPORTED, Strong on the break-marker and Goodhart clauses; Weak on the connectivity prescription)
  Challenges noted: see lit_search_results/against/ASSUMPTION-474_against.md (15b: PARTIALLY-CHALLENGED, Moderate — remedy menu and the quotability of the numeric split)
  Confidence: Moderate
  Applicable to: The weekly vault census; any C2A2 series whose resolver or inclusion rule changes; health-metric selection for the knowledge graph; ASSUMPTION-481's four-week fallback-classification record, which has the same break problem in a different register.
  Re-check due: 2026-10-20 (Quarterly)
  Status: ACTIVE
  Independence note: 15a's CROSS-ITEM-NOTE (2026-07-20) records A-474/A-480/P-501/P-503 as partly non-independent readings of the same two 2026-07-19 events. This premise is incorporated on the strength of an independent literature (official statistics / Eurostat break-and-backcast practice), not on the event count. It is not to be read as one of four confirmations.
  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-474
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 sewing weekly and bootstrap audit transcripts
      15a: Searched for supporting literature; SUPPORTED (Strong/Weak split by clause)
      15b: Searched for challenging literature; PARTIALLY-CHALLENGED (Moderate)
      15c: Net evaluation and disposition; INCORPORATE narrowed to the diagnosis, remedy excluded and routed to REVISE-236
    Current status: INCORPORATED
    Disposition record: DISPOSITION-ASSUMPTION-474 (lit_search_returns.md, 2026-07-20)

PREMISE-106:
  Date validated: 2026-07-20
  Source item: ASSUMPTION-478
  Statement: The lit-search pipeline's queue is in the unstable regime: at ~12 items serviced per run against a daily enqueue rate, arrival exceeds service and the backlog grows without bound. This is a proved queueing result, not a hypothesis, and no scheduling discipline recovers it. Two corollaries the item did not state and that are load-bearing: (i) an existing backlog drains at the SURPLUS rate (service minus arrival), not the service rate, so restoring stability marginally will not clear the standing 147 items and they need separate treatment (one-off drain pass or TTL sweep); (ii) arrival and service are BOTH decision variables — the enqueue stream is generated by C2A2's own agents and is not exogenous, so admission control is available alongside throughput increase, and classical results hold that bounding arrival is sufficient on its own.
  Item type: ASSUMPTION (stated)
  Supporting evidence: see lit_search_results/for/ASSUMPTION-478_for.md (15a: SUPPORTED, Strong on the stability clause)
  Challenges noted: see lit_search_results/against/ASSUMPTION-478_against.md (15b: PARTIALLY-CHALLENGED, Moderate — the stability claim is uncontradicted; challenged is the inference that the budget is the single lever)
  Confidence: High
  Applicable to: c2a2-lit-search-pipeline scheduling and budget; 15d re-trigger cadence; the 147-item standing backlog and the 7th-consecutive BACKLOG-FLAG in monitor_queue.md; any future EOD batch enqueued into this queue.
  Re-check due: 2026-08-20 (Monthly — the queue state is live and moves weekly)
  Status: ACTIVE
  Consistency note: This premise extends, and does not conflict with, the existing premise on the 15d weekly re-trigger queue (validated_premises.md, "structural-under-current-provisioning"). Both hold that arrival exceeds service and that the remedy space includes cadence, admission cap AND provisioning. A-478's phrasing implied the budget was the fault; that implication is explicitly NOT incorporated, per 15b.
  Novelty note: 15a raised a NOVELTY-FLAG on the item's second clause (the 30,000-token budget is inconsistent with the specified scope by ~6x). No literature was found on sizing a token budget against a declared agent scope, or on characteristic mismatch factors. The general form — "the resource budget and the specification were set by different processes and never reconciled" — may be an original contribution. That clause is NOT incorporated here; it is carried as a novelty item and is the load-bearing input to MONITOR-457 (PRESUMPTION-504), where the calibration-versus-norm-decay question is decided.
  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-478
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline fail-loud statements
      15a: Searched for supporting literature; SUPPORTED (Strong clause 1) with NOVELTY-FLAG on clause 2
      15b: Searched for challenging literature; PARTIALLY-CHALLENGED (Moderate, against the inference not the stability claim)
      15c: Net evaluation and disposition; INCORPORATE clause 1 with both levers named, clause 2 held as novelty
    Current status: INCORPORATED
    Disposition record: DISPOSITION-ASSUMPTION-478 (lit_search_returns.md, 2026-07-20)

PREMISE-107:
  Date validated: 2026-07-20
  Source item: ASSUMPTION-479
  Statement: A remedy attached to an observation without being validated against the actual mechanism costs effort AND leaves the fault in place; where two candidate mechanisms present the same symptom, the discriminating test is the operative construct and skipping it is the defining error of fault isolation. Delivering more signal into a channel with demonstrated zero throughput is not throughput but inventory, and can degrade the disposition of signals already working. SCOPE GUARD (load-bearing): diagnose-before-repair is NOT unconditional. Maintenance evidence puts diagnosis at 60-70% of mean time to repair — it is the dominant cost term, not a free precondition — and it is most expensive precisely for unfamiliar failure classes, where identifying WHICH test discriminates is itself the hard step. The rule binds for remedies that are expensive, irreversible, or that increase load on a saturated channel. For remedies that are cheap, reversible and immediately observable, applying the remedy IS the discriminating test and is faster than designing one; requiring a separate test there converts free experiments into queued work in a queue already known not to drain (PREMISE-106).
  Item type: ASSUMPTION (stated)
  Supporting evidence: see lit_search_results/for/ASSUMPTION-479_for.md (15a: SUPPORTED, Strong — fault detection and isolation; predictive maintenance; Senge's "Fixes that Fail" / "Shifting the Burden"; Theory of Constraints; Braess's paradox and bufferbloat)
  Challenges noted: see lit_search_results/against/ASSUMPTION-479_against.md (15b: PARTIALLY-CHALLENGED, Moderate — the cost of diagnosis, the boundary condition now folded in above, and the unaudited 7-of-12 self-count)
  Confidence: High (for the principle with its scope guard)
  Applicable to: The 14/15 self-awareness pipeline's remedy-proposal step; REVISE-231 (2026-07-19) and REVISE-236 (2026-07-20), both of which this premise grounds; every standing REVISE item carrying an unvalidated remedy; any intervention aimed at the review channel.
  Re-check due: 2026-10-20 (Quarterly)
  Status: ACTIVE
  Not incorporated: the item's "7 of 12" ratio. It is a self-count by the pipeline that authored all twelve items, with no published coding rule and no external adjudication, produced on the same day it discovered that its own summarizers report on themselves inaccurately (PREMISE-109). The pattern is validated; the count is not.
  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c]
    Original item: ASSUMPTION-479
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline REVISE-231 statement
      15a: Searched for supporting literature; SUPPORTED (Strong)
      15b: Searched for challenging literature; PARTIALLY-CHALLENGED (Moderate) — boundary condition supplied and folded into the statement
      15c: Net evaluation and disposition; INCORPORATE with 15b's boundary condition made load-bearing, self-count excluded
    Current status: INCORPORATED
    Disposition record: DISPOSITION-ASSUMPTION-479 (lit_search_returns.md, 2026-07-20)

PREMISE-108:
  Date validated: 2026-07-20
  Source item: PRESUMPTION-502
  Statement: Transmission is not delivery. A finding "flagged for" a named agent does not transfer responsibility for it; the loop is closed only on evidence that the recipient received AND acted, and until then the finding is held by nobody while the record shows it discharged. That state is worse than not flagging, because it retires the sender's obligation without creating anyone else's. INSTRUMENTATION CONSTRAINT (load-bearing): the measure of delivery is the flagged content APPEARING IN THE RECIPIENT'S OUTPUT, never an acknowledgement receipt. An acknowledgement makes "acknowledged" measurable and leaves "acted on" exactly as unmeasurable as before, installing a green metric over the unchanged failure — the same defect the presumption exists to name.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: see lit_search_results/for/PRESUMPTION-502_for.md (15a: SUPPORTED, Strong — closed-loop communication and check-back; AHRQ/ACOG clinical handoff, where a handoff transfers authority and responsibility; FAA position-relief standards; responsibility diffusion)
  Challenges noted: see lit_search_results/against/PRESUMPTION-502_against.md (15b: PARTIALLY-CHALLENGED, Moderate — AHRQ grades SBAR low-certainty; only I-PASS reaches moderate and does so via receiver read-back; the best-supported effect is conditioned on a synchronous live receiver, which asynchronous file-mediated agent flagging does not provide; n=1 with no base rate)
  Confidence: Moderate
  Applicable to: Every cross-agent "flagged for X" in the record; the connector-health -> morning-system-health handoff; the cost-tracker gap; 14a/14b routing to 15a/15b/15c; 15d escalations to Tom; MONITOR-420's fired auto-escalate trigger, which is an instance of a flag that was raised seven consecutive times and never received.
  Re-check due: 2026-08-20 (Monthly)
  Status: ACTIVE
  Consistency note: This is the agent-to-agent generalisation of PREMISE-102 ("Fail-loud is an act of reporting, not an act of remediation") and does not conflict with it. PREMISE-102 covers the agent-to-human channel; PREMISE-108 covers agent-to-agent. Confidence is set one grade lower than PREMISE-102 because the in-house evidence is a single traced instance and the strong external evidence is from synchronous human teams, a transfer 15b showed to be unwarranted for the remedy even though the diagnosis carries.
  Base-rate obligation: the base rate is obtainable with no protocol change — enumerate the last thirty days of cross-agent flags and search each named recipient's subsequent output for the flagged content. It has not been obtained. This premise licenses the claim that transmission is not delivery; it does NOT license any claim about how often delivery fails.
  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: PRESUMPTION-502
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by tracing the connector-health handoff into the same-day morning-system-health output and finding it absent
      15a: Searched for supporting literature; SUPPORTED (Strong)
      15b: Searched for challenging literature; PARTIALLY-CHALLENGED (Moderate, against the remedy's expected value)
      15c: Net evaluation and disposition; INCORPORATE the delivery claim, EXCLUDE the acknowledgement remedy, bind the instrument to recipient-output
    Current status: INCORPORATED
    Disposition record: DISPOSITION-PRESUMPTION-502 (lit_search_returns.md, 2026-07-20)

PREMISE-109:
  Date validated: 2026-07-20
  Source item: PRESUMPTION-503
  Statement: A summarizing agent is a view over its own read set, not a view over the system. A summary can be individually faithful to every source it read and collectively false about the system it describes, and this is the DEFAULT property of a layered reporting stack rather than an aberration or a lapse in conduct. Therefore a health claim not bound to a named artifact with a timestamp is not evidence of health, and "no failures to report" must be legible as scoped — "no failures appear in the sources I read" — or it is unfounded. INSTRUMENTATION CONSTRAINT (load-bearing): the measure is CLAIMS-WITHOUT-EVIDENCE (per claim, is there a named artifact and timestamp that would have to hold?), never a read-set coverage percentage. Coverage rises when a summarizer reads more marginal artifacts without reading the decisive one, is unbounded over a growing vault, and would read green during exactly the failure it was built to catch.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: see lit_search_results/for/PRESUMPTION-503_for.md (15a: SUPPORTED, Strong — four-layer monitoring stack with upward propagation of weakness; component-versus-service scope mismatch; data lineage and freshness as a mature tool category; arXiv:2606.14589 on silent failures persisting for weeks in a production LLM agent runtime)
  Challenges noted: see lit_search_results/against/PRESUMPTION-503_against.md (15b: NO-CHALLENGE-FOUND to the claim — 15b searched specifically for evidence that aggregation layers can be assumed source-coupled and every retrieved source ran the other way; PARTIALLY-CHALLENGED, Weak, to the coverage-percentage remedy only, which is excluded above)
  Confidence: High
  Applicable to: The morning project-status summary and every outbound status artifact; morning system health; the connector-health weekly; any agent that renders a fleet-level green; unattended stretches, where the summary layer is the primary interface.
  Re-check due: 2026-10-20 (Quarterly)
  Status: ACTIVE
  Reconciliation basis: This is the only item in the batch meeting the provenance protocol's SUPPORTED + NO-CHALLENGE-FOUND row (protocol reconciliation table: SUPPORTED, High confidence). 15b's disconfirmatory search returning nothing against the claim is itself the strongest signal in the cohort.
  Consistency note: Extends PREMISE-100 (a liveness signal is not evidence of correctness; an inoperable check reports as passing). PREMISE-100 covers the check that cannot run; PREMISE-109 covers the summary that never looked. Complementary, no conflict.
  Independence note: ASSUMPTION-480 is this premise's EVIDENCING INSTANCE, not an independent confirmation. Per 15a's CROSS-ITEM-NOTE and 15b's own recommendation, A-480 was dispositioned MONITOR (MONITOR-455) rather than incorporated separately, so one defect receives one premise and one remediation effort. The read-set enumeration of the 2026-07-19 morning run discriminates between this mechanism (read-set non-coverage) and the component-versus-service mechanism A-480 implies, and settles both at once.
  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: PRESUMPTION-503
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-07-19 morning project status transcript read against four same-morning failure transcripts
      15a: Searched for supporting literature; SUPPORTED (Strong)
      15b: Searched for challenging literature; NO-CHALLENGE-FOUND to the claim, PARTIALLY-CHALLENGED (Weak) to the remedy
      15c: Net evaluation and disposition; INCORPORATE the claim, EXCLUDE the coverage metric, bind the instrument to claims-without-evidence
    Current status: INCORPORATED
    Disposition record: DISPOSITION-PRESUMPTION-503 (lit_search_returns.md, 2026-07-20)

PREMISE-110:
  Date validated: 2026-07-20
  Source item: PRESUMPTION-505
  Statement: Detectors do not reliably degrade gracefully; they invert. A monitor whose failure presents as a nominal reading becomes MORE reassuring as the monitored condition worsens, and this is a catalogued fault class (stuck-at-nominal, one of five standard non-fail-stop sensor faults), not a novel or rare condition. Absence-of-complaint is therefore an unsafe polarity for a health signal: the safe form is affirmative and perishable — the monitor must be actively fed on an independent timebase, so that cessation of activity is itself the alarm. COMMON-MODE SCOPE GUARD (load-bearing): a monitor sharing runtime, scheduler, credentials and filesystem with its subject is a SINGLE CHANNEL WEARING TWO LABELS, and any discrepancy-based self-check is provably blind to a fault present in both channels with the same characteristics. Independence must be engineered before it is tested. The valid instrument is a live proof-test — deliberately break a monitored subsystem in a sandbox and confirm its monitor turns red within the expected interval — NOT the reachability audit the item proposed, which is a discrepancy check and would return a reassuring pass on precisely the inversions that matter.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: see lit_search_results/for/PRESUMPTION-505_for.md (15a: SUPPORTED, Strong — fail-safe design and the detected/undetected failure distinction; diagnostic coverage; stuck-at-nominal sensor faults and their polarity-inversion countermeasures; watchdog practice; Huang et al. 2017 gray failure supporting the generalisation step)
  Challenges noted: see lit_search_results/against/PRESUMPTION-505_against.md (15b: Weak against the claim — 15b searched disconfirmatorily and found no evidence detectors can be assumed to degrade gracefully; Moderate against the proposed test, PMC9228164 on common-mode blindness of discrepancy analysis, now folded in above as the scope guard)
  Confidence: High
  Applicable to: 15d cycle-count staleness detection (ASSUMPTION-476 / MONITOR-454); the scheduler watchdog; connector enumeration (ASSUMPTION-481 / REVISE-234); the vault census (PREMISE-105); every green signal in the fleet health report; any monitor added in response to any item in this batch.
  Re-check due: 2026-10-20 (Quarterly)
  Status: ACTIVE
  Consistency note: Generalises PREMISE-100 from "an inoperable check reports as passing" to "a monitor's pass state is systematically reachable while its subject is dead, and monitor/subject independence in this fleet is asserted rather than engineered." No conflict; PREMISE-110 is the stronger and more general form and PREMISE-100 remains ACTIVE as the specific case.
  Scope limit: 15a and 15b both note that one of the item's four cited instances (the vault census) is diagnosed by ASSUMPTION-474 in this same batch as a definitional-comparability problem rather than a detector inversion, and the two readings are not obviously compatible. This premise is incorporated on the strength of the fault-class literature and the three unambiguous absence-of-complaint cases; the four-instance count is not incorporated, and a census that miscounts is not the same defect as a detector that inverts.
  Cost caveat: polarity inversion raises the false-positive rate, which is the alert-fatigue failure named in PREMISE-102 / PRESUMPTION-495 and measured at 44% of organisations having an outage linked to suppressed or ignored alerts. Apply selectively by criticality, as SIL practice allocates diagnostic coverage. Do not convert all absence-of-complaint checks at once into a review channel with demonstrated zero throughput.
  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: PRESUMPTION-505
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by generalizing 15d's local statement across three further same-day cases
      15a: Searched for supporting literature; SUPPORTED (Strong)
      15b: Searched for challenging literature; PARTIALLY-CHALLENGED (Weak against the claim, Moderate against the test)
      15c: Net evaluation and disposition; INCORPORATE the claim with the common-mode scope guard made load-bearing, EXCLUDE the reachability audit in favour of a live proof-test
    Current status: INCORPORATED
    Disposition record: DISPOSITION-PRESUMPTION-505 (lit_search_returns.md, 2026-07-20)

PREMISE-111:
  Date validated: 2026-07-21
  Source item: ASSUMPTION-483
  Statement: The read channel was not the dominant correlation source between 15a and 15b, and removing it removed the weakest of at least four. Frontier LLMs sharing no procedural channel collapse to roughly two effective votes out of nine, so the dominant channels — shared pre-training corpora, shared alignment procedures, distillation — are upstream of any coupling C2A2 can remove. The 2026-07-19 change is therefore correctly relabelled "read-channel independence enforced," and the 905-pair record is not re-run. STANDING DISCOUNT (load-bearing): the correct inference from this premise is that the record is MORE compromised than the fix addressed, not less. No downstream argument may cite 15a/15b agreement as independent confirmation; agreement between the two directions carries a residual correlation of roughly the magnitude the panel literature measures (8–22pp accuracy shortfall against the independence benchmark) and must be discounted accordingly.
  Item type: ASSUMPTION (stated)
  Supporting evidence: "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels," arXiv:2605.29800. van Rooyen, Godlee, Evans, Smith & Black (1998), "Effect of Blinding and Unmasking on the Quality of Peer Review: A Randomized Trial," JAMA 280(3):234-237, PMID 9676666 — blinding effect ~0.4 points on a 5-point scale, no change in publication recommendations, across 527 manuscripts. "How Independent are Large Language Models?", arXiv:2604.07650.
  Challenges noted: 15b (Moderate) — if the read channel was the weakest of four, three stronger channels remain unaddressed; "do not re-run" is a defensible budget decision but must not be read as reassurance. Incorporated as the standing discount above.
  Confidence: Moderate
  Applicable to: Agents 15a, 15b, 15c; every disposition citing cross-agent convergence; REVISE-240; SYSTEMIC-RISK-FLAG-A.
  Re-check due: 2026-08-21
  Status: ACTIVE
  NOTE ON THIS ENTRY'S OWN EVIDENCE: 15a and 15b independently retrieved the same two key sources for this item. That is an instance of the correlation this premise describes and is the reason confidence is Moderate rather than High.

PREMISE-112:
  Date validated: 2026-07-21
  Source item: ASSUMPTION-485
  Statement: Replacing a possibly-wrong objective with an unmeasurable one converts it into no objective. Removing a scored dimension before its replacement is instrumented is the third and fourth step of the McNamara fallacy — declaring the unmeasured unimportant, then absent — and the operational rule is sequencing: instrument the replacement first, run both in parallel, then retire the incumbent. EXPIRY CLAUSE (load-bearing): the rule is a sequencing requirement with a stated deadline on the parallel-instrumentation period, NOT a licence to retain a defective proxy indefinitely pending a quantitative substitute. Without the deadline the premise becomes the failure PRESUMPTION-509 names. The healthcare-evaluation answer to an unmeasurable objective is mixed assessment, not indefinite retention.
  Item type: ASSUMPTION (stated)
  Supporting evidence: The McNamara fallacy, Yankelovich's four-step formulation. Bächtiger et al., "Measuring Deliberation" (Ash Center, Harvard) and the Discourse Quality Index — mutual understanding is already operationalised. Goddard & Gillespie (2023), doi:10.1177/08944393231156629 — systematic review of validated text-based dialogue indicators. arXiv:2604.15647 — computable information-gain measure.
  Challenges noted: 15b (Moderate) — the item's own proposed replacement, the Ideological Turing Test, has documented validity limits in the paper that establishes it (Brand et al. 2025, "The Ideological Turing Test," Cognitive Science, doi:10.1111/cogs.70126): no normative ground truth, imitative equivalence is not insight, prompt-sensitive, limited temporal validity. Recorded so the parallel-instrumentation period is not read as a search for one authoritative replacement.
  Confidence: Moderate
  Applicable to: Rung-2 scoring; the convergence metric; any proposal to retire a scored dimension; constrains and is constrained by MONITOR-461 (PRESUMPTION-509).
  Re-check due: 2026-08-21
  Status: ACTIVE

PREMISE-113:
  Date validated: 2026-07-21
  Source item: ASSUMPTION-489
  Statement: A rule-based detector's reported findings are evidence about the detector until its precision is measured. False-positive rates of 76-90%+ are inside the normal operating band for such detectors and enterprise analysers are deliberately built recall-first, so "the detector has a real bug" and "the detector is operating near its design point" are both consistent with a high false-positive count and the count alone does not discriminate them. LABELLED CORPUS (load-bearing): a post-fix reading of zero is indistinguishable from a detector that now detects nothing. Tightening a detection rule risks suppressing detection rather than improving it, converting a false-positive problem into a silent false-negative one. Therefore precision AND recall must be reported separately against a corpus containing known-genuine and known-clean cases before any post-fix result is read as evidence about the corpus rather than about the instrument. Corollary: an audit of sibling detectors for the same defect class is independent of this and is warranted regardless.
  Item type: ASSUMPTION (stated)
  Supporting evidence: "Reducing False Positives in Static Bug Detection with LLMs: An Empirical Study in Industry," arXiv:2601.18844. SAST precision measurements 18-36%; CodeQL and Infer >95% false-alarm rates for null-pointer dereference at Linux-kernel scale. Snyk, "Minimizing False Positives," and OX Security — threshold loosening suppresses detection.
  Challenges noted: 15b (Moderate) — directed at the item's proposed validation, which has no oracle; incorporated above as the load-bearing clause. 15a (independently) — the reclassification was performed by the pipeline that produced the findings, whereas false-positive studies in this literature use independent triage with inter-rater agreement; see PREMISE-118.
  Confidence: Moderate
  Applicable to: The Summa metaphysical guardrail detector and all sibling detectors; any detector change validated by re-run; extends PREMISE-110's common-mode guard from monitors to detectors. NOT incorporated: the local verdict that 11 of 13 findings were false positives and 0 genuine — that figure was produced by the instrument under audit.
  Re-check due: 2026-08-21
  Status: ACTIVE

PREMISE-114:
  Date validated: 2026-07-21
  Source item: ASSUMPTION-490
  Statement: When two or more instruments of one system disagree and none is externally calibrated, no arbitration rule can name a winner: authority is a property of a documented chain to an external reference, and absent one the readings are formally incommensurable. Where no gold standard exists, method comparison yields limits of agreement, not a correct value, and the latent-class methods that do recover per-instrument accuracy require conditional independence, which counters sharing a codebase and corpus do not have. THE EXIT (load-bearing): where the underlying quantity is deterministic over a frozen snapshot — as a word count is — the disagreement is almost certainly DEFINITIONAL rather than instrumental. The procedure is therefore to write the counting definition first (including every exclusion rule, e.g. Notes-stripping), designate it the reference, and re-derive all readings against it; convergence is the expected outcome and arbitration is not needed. This supplies the procedure PREMISE-101 lacks for creating a designated counting authority, and the arbitration rule PRESUMPTION-507 reports as missing. EXCLUSION: a declared figure matching none of the measured values is an unsourced assertion, not an additional reading, and is struck from the comparison.
  Item type: ASSUMPTION (stated)
  Supporting evidence: NIST, "Metrological Traceability: FAQs and NIST Policy." Eurachem/CITAC Guide, "Metrological Traceability in Chemical Measurement" (2019). Bland-Altman method-comparison practice (MedCalc manual; PMC2244491). "Insights into latent class analysis of diagnostic test performance," Biostatistics 8(2):474.
  Challenges noted: 15b (Moderate) — an arbitration rule chosen on grounds other than a written definition sets tier calibration against a number that was chosen rather than established. Incorporated as the exit clause above.
  Confidence: Moderate
  Applicable to: The three Summa word counts (QC 5, verification 15, nightly 20); tier calibration; the six standing counting disputes; extends PREMISE-101; supplies the missing rule for PREMISE-117. Where an instrument IS established out of tolerance, PREMISE-118's retrospective impact assessment applies.
  Re-check due: 2026-08-21
  Status: ACTIVE

PREMISE-115:
  Date validated: 2026-07-21
  Source item: ASSUMPTION-491
  Statement: Before an agent is called broken, check whether its specification ever instructed the behaviour. Specification and design issues are the largest single category of multi-agent system failure (41.8%, vs inter-agent misalignment 36.9% and verification 21.3%) across the only empirically grounded taxonomy, so "the instruction is missing" is the base-rate-favoured diagnosis over "the agent is broken" and has a different, cheaper fix. Silent failure is the modal profile, not the exception: 75.17% of failures emit no hard error signal, which is why a months-long write failure can pass unnoticed. EFFECTIVENESS CHECK AT CONTENT LEVEL (load-bearing): the check on such a fix must be that the expected CONTENT appears, never that a file appears — file existence is a liveness test, and the fault class this premise concerns is precisely the one liveness tests miss (see PREMISE-100, PREMISE-110). VOCABULARY: per PREMISE-120, a second check that shares code path, corpus, model and execution context is a re-run, not an independent confirmation, and must be recorded as "confirmed by a second check sharing [components]."
  Item type: ASSUMPTION (stated)
  Supporting evidence: Cemri et al., MAST — "Why Do Multi-Agent LLM Systems Fail?" (1,600+ annotated traces, 7 frameworks). "When Errors Become Narratives," arXiv:2606.14589. arXiv:2606.08162 and Latitude observability guidance on silent failures emitting no error codes.
  Challenges noted: 15b (Weak) — "independently confirmed" is load-bearing in the source item and unassessed; struck above. The item's own proposed effectiveness check was a liveness test; replaced above.
  Confidence: Moderate
  Applicable to: agentic-cost-tracker; weekly-agent-ecosystem-report; the Stump PRS-09 repoint; failure triage across all scheduled agents. The three underlying local claims are NOT incorporated — 15c has not verified them.
  Re-check due: 2026-08-21
  Status: ACTIVE

PREMISE-116:
  Date validated: 2026-07-21
  Source item: PRESUMPTION-506
  Statement: A finding does not change the behaviour it describes. Propagation from a recorded finding to a change in the governed agent's conduct must be engineered and then confirmed; it is never a property of having recorded the finding. The best-measured analogue — audit and feedback, i.e. measuring a party's conduct and reporting the deviation back — moves behaviour by a median 4.3% absolute (IQR 0.5-16%, 140 trials), updated to a mean 6.2% (95% CI 4.1-8.2, 292 trials), and the moderators that make it work (peer delivery, individual measurement, repetition, explicit target, action plan) are all absent from a premise written to a registry. Two mature disciplines, quality systems and internal audit, maintain mandatory verification machinery built on this assumption. PRE-REGISTERED PRIOR (load-bearing): the 110-premise sweep must be run as a RATE against a stated 4-8% expectation, decided before the sweep. Without it the result is uninterpretable in both directions — a low rate would be read as confirming total failure, when it is what the literature predicts of a mechanism working normally. ASYMMETRIC RISK: judging a propagation mechanism against an implicit expectation of compliance would discard a working intervention for underperforming an unrealistic bar. INSTRUMENTATION CONSTRAINT: a propagation step that produces a "propagated: yes" field reproduces the defect exactly; the measure must be a behavioural change in the governed agent's OUTPUT.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: no architectural step propagating a validated premise back to the agent it governs exists in any agent definition)
  Supporting evidence: Ivers, Jamtvedt, Flottorp et al. (2012), "Audit and feedback: effects on professional practice and healthcare outcomes," Cochrane Database Syst Rev CD000259.pub3, PMID 22696318; 2025 update CD000259.pub4. PMC6899530, "Implementation of Implementation Science Knowledge: The Research-Practice Gap Paradox." CAPA effectiveness-check practice.
  Challenges noted: 15b (Moderate) — "110 premises have never altered conduct" is a universal built on one instance, and a single same-day recurrence is fully consistent with a propagation mechanism existing and working at the normal effect size. The universal is explicitly NOT incorporated.
  Confidence: High (structural claim only)
  Applicable to: All 110 prior premises, 236 revision flags and 457 monitors; agents 15c and 15d; REVISE-239; MONITOR-460. Extends PREMISE-109 into the propagation direction; is the general form of which PREMISE-102 and PREMISE-108 are instances.
  Re-check due: 2026-08-21
  Status: ACTIVE
  NOTE ON THIS ENTRY'S OWN EVIDENCE: both search directions grounded this on the same Cochrane review; per PREMISE-111 their agreement is not two independent confirmations.

PREMISE-117:
  Date validated: 2026-07-21
  Source item: PRESUMPTION-507
  Statement: Continuing to publish under an unresolved definitional dispute is codified professional practice, not a defect. In official statistics the standard is publish-then-revise: figures carry a revision flag, the definitional change is described, and withdrawal is reserved for statistics not fit for purpose. THE DEFECT IS SILENCE, NOT CONTINUATION (load-bearing): what an unresolved dispute obliges is a break flag on every affected figure, a documented account of the change, and a pre-committed corrections policy with prompt notification — not suspension of dependent work. Quarantine is excluded and its failure mode is stated: suspending dependent work behind an unresolved dispute, in a channel with near-zero decision throughput, resolves disputes by abandonment rather than adjudication. Impact assessment is lineage-bounded to descendants of the disputed figure, which bounds its cost. The arbitration procedure that closes such disputes is PREMISE-114.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: UK ONS Revisions Policy and Correction of Errors Policy; Office for Statistics Regulation, "Regulatory guidance — Publishing official statistics." IMF, "Revisions Policy for Official Statistics." US OMB Statistical Policy Directive No. 4 (73 FR, 2008). UN Fundamental Principles of Official Statistics implementation guidelines. arXiv:2605.06365 — invalidation as a semantic operation over dependency identities in agentic pipelines.
  Challenges noted: 15b (Moderate) — the behaviour named as an unexamined presumption is standard practice in the discipline the item points to; the item's implied quarantine remedy is what the standards decline. Redirected the remedy above. Symmetric risk if nothing changes: figures propagate unflagged and the break is rediscovered later with no record of what was affected.
  Confidence: Moderate-High
  Applicable to: The six standing counting disputes; every artifact derived from a disputed figure; Summa tier calibration; extends PREMISE-105's break-marking clause. One grade below High because it transfers from official statistics to an internal vault where the notification obligation has no external addressee.
  Re-check due: 2026-08-21
  Status: ACTIVE

PREMISE-118:
  Date validated: 2026-07-21
  Source item: PRESUMPTION-508
  Statement: Naming a defect in an instrument does not license continued use of it; it triggers an obligation. Where an instrument is found out of tolerance, practice requires contain / assess impact / fix cause / verify, including a RETROSPECTIVE impact assessment over every result produced since last known-good calibration. Noting the condition and continuing is a recognised serious finding. Two clauses bound this (load-bearing). (i) The obligation is ASSESSMENT, not automatic invalidation: results may stand where impact assessment shows validity unaffected, so "continued without quarantine" and "continued without assessment" are different things and only the second is the violation. (ii) "Unknown quality" overstates the consequence where the defect is measured: an 8-22 percentage-point accuracy shortfall is a computable discount, not indeterminacy. Price the defect; do not disown the output. RECURSIVE CAVEAT: where the judgement that an instrument is defective came from the instrument, the response is external measurement — neither trusting nor discounting the self-report resolves it.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: ISO/IEC 17025 nonconforming-work practice, clauses 7.10 and 8.7. GMP out-of-tolerance handling and retrospective impact assessment (NIST GMP 11). arXiv:2605.29800 — panel accuracy 8-22pp below the independence benchmark. CARE, arXiv:2603.00039.
  Challenges noted: 15b (Weak-to-Moderate) — the standard does not require quarantine, and the defect's magnitude is measured rather than unknown. Both incorporated as the bounding clauses above.
  Confidence: Moderate-High
  Applicable to: Agent 15c's own dispositions, including this run; the 2026-07-20 disposition set; all 121 premises; the Summa detectors (PREMISE-113); any measurement instrument in the vault. Extends PREMISE-110.
  Re-check due: 2026-08-21
  Status: ACTIVE
  SELF-APPLICATION RECORDED AT VALIDATION: this premise is violated by the run that validated it. The 15c defect was named on 2026-07-20 (REVISE-233), no retrospective impact assessment has been performed, and 18 further dispositions were produced on 2026-07-21. Routed as REVISE-240; unremedied at time of writing.

PREMISE-119:
  Date validated: 2026-07-21
  Source item: PRESUMPTION-510
  Statement: Production and judgment are not independently schedulable. Where a produced item requires human judgment before it has value, the producing and reviewing stages are provably coupled: automation and human scheduling cannot be optimised separately, unbounded production imposes a congestion externality on the constrained stage, and service rate is not independent of arrival rate because reviewer acceptance falls with cumulative exposure. In distributed-systems terms backpressure is a correctness requirement, not an optimisation. SEQUENCING REQUIREMENT (load-bearing): establish that the service rate is greater than zero, and whether the consumer is SATURATED or ABSENT, before designing any admission policy. Where service is zero the steady-state relations do not hold at all and no reduction in arrivals bounds the queue — cutting 4/day to 1/day still diverges — so throttling an absent consumer directs effort at the arrival term while the term that is actually zero goes untouched, and reports a control in place. EXCLUDED: a flat per-day admission cap. Its documented failure mode is that fixed WIP limits bind immediately against an existing backlog and are raised on first bind; the better-evidenced alternatives are value-based screening and backlog-sensitive pressure. ADOPTABLE NOW: a "produced and unreviewable" state, which the current scheme cannot represent and which neither search direction contests.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Little's law as applied in Kanban/queueing practice; Ponte, "Little's Law and Applying Back Pressure When Overloaded." arXiv:2607.06017, "Learning When to Automate: Queue Control in Human-AI Service Systems." arXiv:2603.13870, "When to Screen, When to Bypass: LLM-Judges in Resource-Scarce AI-Human Workflow." arXiv:2601.22295, "Operating Imperfect AI: Reliability Drift and Human Congestion."
  Challenges noted: 15b (Moderate) — entirely against the remedy; three independent lines argue against a flat cap. Incorporated as the exclusion above.
  Confidence: Moderate-High
  Applicable to: The review channel awaiting Tom (arrival ~4/day, service 0/day across 15 days, 67 carried items); the MONITOR queue; agents 14a, 14b, 15c, 15d. Extends PREMISE-106 from the lit queue to the review channel; applies PREMISE-107's discriminating-test rule to a saturated channel.
  Re-check due: 2026-08-21
  Status: ACTIVE

PREMISE-120:
  Date validated: 2026-07-21
  Source item: PRESUMPTION-511
  Statement: Reproducing a result does not confirm it. Reproducibility — obtaining consistent results using the same input data, computational steps, methods and code — is a property of the pipeline, expected as a baseline; replicability requires independently obtained data. Replication and reproducibility do not imply correctness, and a systematic defect reproduces exactly as reliably as a correct measurement: a deterministic analyser with a >95% false-alarm rate reproduces every false alarm perfectly. BINDING VOCABULARY (load-bearing): NASEM's distinction is adopted vault-wide, and the phrase "independently confirmed" is forbidden unless the second check obtained its own data by a different path. Every claimed second check must record what it shares with the first: code path, corpus, model, execution context. Checks sharing all four are a single channel wearing two labels regardless of how they are labelled. TWO SCOPE GUARDS: (i) reproducibility is necessary and insufficient, not empty — it rules out transcription error, nondeterminism and environment drift, a real and cheap defect class; (ii) a second implementation written from the same specification SHARES the specification, and structural variation does not buy failure independence, so independence must be engineered at the definition layer or the second method reproduces the first method's trap.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: NASEM (2019), "Reproducibility and Replicability in Science," National Academies Press, doi:10.17226/25303. arXiv:2607.02808, "A Systematic Methodology for Evaluating Failure Independence in LLM-Generated Code." arXiv:2605.29800. In-house instance: ASSUMPTION-489's detector.
  Challenges noted: NO-CHALLENGE-FOUND. 15b searched disconfirmatorily and reports that no retrieved source treats computational reproduction as evidence of correctness. Both scope guards above were volunteered by the disconfirmatory search as supportive qualifications.
  Confidence: High (SUPPORTED + NO-CHALLENGE-FOUND row of the provenance protocol's reconciliation table)
  Applicable to: All verification agents; the Summa nightly verification; ASSUMPTION-491's language (see PREMISE-115); agents 15a/15b (see PREMISE-111); SYSTEMIC-RISK-FLAG-A, of which this premise is the general form. The measurement the flag requires is routed as REVISE-240 — this premise states the rule, it does not perform the measurement.
  Re-check due: 2026-08-21
  Status: ACTIVE

PREMISE-121:
  Date validated: 2026-07-21
  Source item: PRESUMPTION-512
  Statement: A reviewer's per-item cost is not constant and their capacity does not scale with production. In the best-measured operational analogue, review-queue acceptance is a function of workload and cumulative exposure rather than item merit: override rates run 49-96%, acceptance falls as volume and complexity rise, and desensitisation GENERALISES — true positives are discounted alongside false ones. Therefore each additional correctly-argued item can lower the probability that ANY item is acted on, and a recommendation written as though the marginal item were the only item mis-states its own cost. VALUE-WEIGHTED TRIAGE (load-bearing): degradation tracks LOW-INFORMATION items specifically, so the obligation is to raise the information value of each item routed to a human, not merely to route fewer. EVIDENCE BASE EXPLICITLY BOUNDED: this premise is grounded on the clinical-decision-support override literature. Decision fatigue and the parole-board result are STRUCK — ego depletion failed a 23-laboratory preregistered replication (>2,000 participants), and the parole finding carries a documented case-ordering confound and a simulation critique concluding the magnitude is substantially overestimated. The conclusion does not rest on them and must not be argued from them.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Ancker, J.S. et al. (2017), "Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system," BMC Med Inform Decis Mak, PMC5387195. Nanji et al., "Overrides of medication-related clinical decision support alerts in outpatients," PMID 24166725. Static-analysis desensitisation literature. NOT supporting evidence: Danziger et al. (2011), PNAS 108(17):6889 — struck; Hagger, Chatzisarantis et al. (2016), Perspectives on Psychological Science 11(4):546-573 — the replication that struck it.
  Challenges noted: 15b (Moderate) — against the cited mechanism, not the conclusion; both directions independently identified the same citation problem and proposed the same substitute. Residual limits: n=1 reviewer, workflow mismatch between clinical alerting and vault review, no in-house measurement.
  Confidence: Moderate
  Applicable to: Every agent routing items to Tom; agents 14a, 14b, 15c, 15d; the standing review backlog; PREMISE-119's channel. Extends PREMISE-102.
  Re-check due: 2026-08-21
  Status: ACTIVE
  OPEN MEASUREMENT NAMED AT VALIDATION: no artifact in this vault states the size of the open ask. Sum every open item awaiting Tom, attach a time estimate, report the total in hours — one query, named by both search directions as the most useful artifact proposed in this batch. That absence is itself an instance of what this premise describes.

PREMISE-122:
  Date validated: 2026-07-22
  Source item: PRESUMPTION-523
  Statement: A claimed equivalence between two formalisms is not legitimate merely because it is statable or "tractable." Before running any cross-formalism equivalence test (e.g. FLAG-017's Levin virtual-governor vs Friston group-level Markov blanket), the transfer conditions must be checked explicitly: (1) a shared level of description, (2) a common definition of the system boundary, and (3) a matching notion of "control." A Markov blanket is at base a statistical conditional-independence partition; a governor is a control object with a set-point and error signal — sharing a feedback diagram does not make them the same object. Tractability-to-state must not stand in for legitimacy-of-comparison.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: designers were unaware they were assuming commensurability)
  Supporting evidence: "The Markov Blanket Trick: On the Scope of the FEP" (philsci-archive 18843); "How particular is the physics of the FEP?" (arXiv:2105.11203); "Is the FEP a formal theory of semantics?" (arXiv:2007.09291). 15a Moderate-Strong.
  Challenges noted: 15b found NO challenge to validity (None); the only pro-commensurability material — nested Markov blankets (Kirchhoff et al. 2018) and the FEP governor analogy — establishes side-by-side placement, not shared meaning of "boundary"/"control," which is what the presumption already grants.
  Confidence: High (SUPPORTED + NO-CHALLENGE-FOUND)
  Applicable to: FLAG-017 / ASSUMPTION-496 (gates its equivalence test); any future cross-tradition or cross-formalism "these two constructs are the same" claim (e.g. Levin<->Friston, control-theoretic<->free-energy, PRS<->other progress models). A general methodological gate for the connecting-meme program.
  Re-check due: 2026-10-22 (Quarterly)
  Status: ACTIVE
  NOTE: This premise is the mitigation named in ASSUMPTION-496's disposition (MONITOR-463). A-496's equivalence test is gated on satisfying (1)-(3) here first.

PREMISE-123:
  Date validated: 2026-07-23
  Source item: PRESUMPTION-516
  Statement: A validated finding does not reach the agent it governs unless an explicit propagation mechanism carries it. Producing a FLAG, a disposition, or a validated premise and CHANGING the behaviour of the governed component are distinct steps; the second does not follow from the first by default. This is the "know-do gap": in the best-measured analogue (clinical/policy translation) the median lag from validated knowledge to governed practice is ~17 years and many findings never arrive at all. C2A2 has no edge from its self-knowledge layer (FLAGs, premises, dispositions) into the agent specifications those findings bear on — so filing a finding "as bearing on" a metric or agent presumes an adoption path that is not built. SCOPE GUARD: the ~17-year MAGNITUDE is a human-organization figure and does NOT transfer to a single-maintainer software system, where propagation can be a one-line spec edit; what transfers is the STRUCTURAL claim that the path must be built, not assumed. The DevOps/continuous-delivery literature reinforces this: continuous propagation is an engineered achievement, not a default.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: designers were unaware they assumed an adoption path)
  Supporting evidence: Morris, Wooding & Grant (2011), "The answer is 17 years," J R Soc Med 104(12):510-520; Grol & Grimshaw (2003), "From best evidence to best practice," Lancet 362:1225-1230; Cabana et al. (1999), "Why don't physicians follow clinical practice guidelines?" JAMA 282(15):1458-1465. 15a Strong.
  Challenges noted: 15b NO-CHALLENGE-FOUND; only a magnitude caveat (small automatable system => cheap propagation), which argues for fixing the gap, not for denying it.
  Confidence: High (SUPPORTED + NO-CHALLENGE-FOUND)
  Applicable to: FLAG-018 -> Rung-2 metric (the triggering case); every FLAG, disposition, and validated premise that names a consequence for a governed agent; the relationship between this self-awareness layer (14a/14b/15a/15b/15c/15d) and the tradition/metric agents it studies. Couples to PREMISE-121 (open ask is un-sized) and PREMISE-119 (review bottleneck): those describe the human channel; this names the missing findings->agent edge.
  Re-check due: 2026-08-23
  Status: ACTIVE
  OPEN MEASUREMENT NAMED AT VALIDATION: has any FLAG or validated premise ever changed a governed agent's specification? Trace the history; a zero rate confirms the gap directly (one query). Until an instance exists, treat "filed as bearing on X" as NOT-YET-PROPAGATED.

PREMISE-124:
  Date validated: 2026-07-23
  Source item: PRESUMPTION-533 (general form of the 2026-07-23 SYSTEMIC-RISK flag; instances: PRESUMPTION-520, ASSUMPTION-499, PRESUMPTION-518)
  Statement: Any self-measurement of the pipeline's OWN completeness or accuracy must cite an external baseline, or a seeded/independent denominator, or be reported as UNCALIBRATED. A favorable number produced from inside the instrument being evaluated (errors caught, source overlap, "full-picture" audit) does not license a completeness or quality claim: (a) a raw defect CATCH COUNT is not an estimate of defects PRESENT without capture-recapture or fault seeding (PRESUMPTION-520); (b) a self-audit assembled while a channel is systematically DARK cannot be called observationally complete, because the missingness mechanism (dark != quiet) cannot be assessed from the surviving data (PRESUMPTION-533; Rubin 1976); (c) an in-run correlation measured by the same pipeline whose independence it evaluates has no external referent (ASSUMPTION-499/PRESUMPTION-518). FORBIDDEN MOVE: reading a single favorable self-observation as evidence a safeguard "works" (WYSIATI / base-rate neglect). REQUIRED: attach an external baseline, a seeded denominator, or an explicit UNCALIBRATED/INCOMPLETE tag.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight)
  Supporting evidence: Rubin, D.B. (1976), "Inference and missing data," Biometrika 63(3):581-592; Petersson, Thelin, Runeson & Wohlin (2004), "Capture-recapture in software inspections after 10 years research," JSS 72(3); Mills (1972) fault seeding; Kahneman (2011) WYSIATI. 15a Strong; 15b raised the High SYSTEMIC-RISK flag independently.
  Challenges noted: NO-CHALLENGE-FOUND. Weak boundary only — a positive catch count is a non-zero lower bound on detection capability, and a dark channel MIGHT be low-relevance; neither can be established from inside the instrument, which is the premise's point.
  Confidence: High (SUPPORTED + NO-CHALLENGE-FOUND)
  Applicable to: The general form of REVISE-233 / MONITOR-464 (15a/15b correlation); agents 15a/15b/15c/15d self-reporting; the daily-run self-catch reporting; any "N caught / overlap / full-picture" claim in outbound artifacts. Complements PREMISE-111 and PREMISE-120 (independence family). Subordinated instances this run: MONITOR-469 (PRESUMPTION-520).
  Re-check due: 2026-10-23 (Quarterly)
  Status: ACTIVE

PREMISE-125:
  Date validated: 2026-07-25
  Source item: PRESUMPTION-541
  Statement: Adding a redundant path does not by itself increase availability; redundancy improves reliability only under two conditions — (a) the redundant units fail independently, and (b) a deterministic arbitration/selection rule decides which unit acts. An UNARBITRATED redundant client introduces a selection ambiguity that is itself a common-mode failure point and can REDUCE availability (here: a second connected Chrome extension broke unattended delivery by requiring a human prompt to disambiguate the target). The correct remedy is to add a primary-selection/priority rule, not to remove the redundancy. "Redundancy = resilience" is false without arbitration.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: designers were unaware they assumed a redundant client was neutral-or-helpful)
  Supporting evidence: Sagan, S.D. (2004), "The Problem of Redundancy Problem," Risk Analysis 24(4):935-946; Avizienis & Chen, N-version programming (common-mode faults from specification ambiguity); Perrow, C. (1984), Normal Accidents (redundancy raises interactive complexity/coupling). 15a Strong.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — correctly arbitrated redundancy is a well-established availability improvement (Raft/quorum leader-election); the observed degradation indicts the missing arbitration rule, not redundancy per se. This is incorporated as the premise's own arbitration condition, so the challenge scopes rather than refutes.
  Confidence: Moderate
  Applicable to: multi-connector / multi-extension delivery paths; any k-of-n redundancy added to the agent fleet; failover design; the two-Chrome-extension delivery incident specifically.
  Re-check due: 2026-10-25 (Quarterly)
  Status: ACTIVE
  OPEN MEASUREMENT NAMED AT VALIDATION: add a deterministic primary-selection rule (or pre-select one extension) and confirm unattended delivery resumes with BOTH extensions connected — isolating arbitration from redundancy (in-house test).

PREMISE-126:
  Date validated: 2026-07-25
  Source item: PRESUMPTION-542
  Statement: A staleness-triggered re-check that only advances the date certifies "not-yet-expired," which is categorically weaker than "re-tested against current state." For a periodic re-check (e.g., Agent 15d's monthly/quarterly re-stamp) to count as genuine RE-VALIDATION, it must re-compute at least one underlying measurement and record the recomputed value, not merely update the re-check date. Recency must not be conflated with re-confirmation. This is the periodic-review analogue of project Rule 9 (a test that cannot fail when the underlying state changes is not verifying anything) and complements PREMISE-124 (self-measurement calibration).
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight)
  Supporting evidence: ISO/IEC 17021 surveillance-vs-recertification distinction (a lapse-check is not a re-assessment); FAA CFI recency-of-experience rule (recency and demonstrated current competence are separate certifications); software-testing literature on assertion-free "green" tests. 15a Strong.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak-Moderate) — a well-designed periodic re-check (ISO Year-3 recertification; a monitoring probe that re-runs) DOES re-exercise the assertion, so the defect is implementation-specific, not intrinsic to periodic review. Incorporated as the premise's "must re-compute" condition.
  Confidence: Moderate
  Applicable to: Agent 15d re-checks; every "ACTIVE, no change" re-stamp in validated_premises.md; any calendar-triggered re-validation in the fleet.
  Re-check due: 2026-10-25 (Quarterly)
  OPEN MEASUREMENT NAMED AT VALIDATION: inspect 15d's monthly re-check — does "ACTIVE, no change" carry a freshly recomputed figure or only an updated date? A date-only re-stamp confirms this premise directly (in-house test).
  Status: ACTIVE

PREMISE-127:
  Date validated: 2026-07-26
  Source item: PRESUMPTION-545
  Statement: A shared vocabulary between two formalisms (e.g., "error"/"surprise" in a bug and in the free-energy principle) is a SURFACE feature and is not, by itself, evidence of a genuine structural homology. A cross-domain / cross-tradition formalism bridge is warranted for CROSS adoption only after a transfer-condition check: the base formalism's preconditions and its system of relations must be shown to hold and to ALIGN in the target, not merely its labels. The decisive question is whether the referents match — e.g., FEP "surprise" is defined over a system's OWN generative model, whereas a "bug" is defined relative to an external agent's (programmer's) intent, so the two "error" signals are not automatically the same relational object. Surface lexical overlap ⇒ provisional bridge (flagged unverified) + a scheduled cheap structural-alignment test; never ⇒ settled adoption.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: designers were unaware they treated a lexically-appealing bridge as structurally validated)
  Supporting evidence: Gentner, D. (1983), "Structure-Mapping: A Theoretical Framework for Analogy," Cognitive Science 7(2):155-170; Gentner & Markman (1997); Bruineberg et al. (2021), "The Emperor's New Markov Blankets," BBS; Colombo & Wright (2021) on FEP scope/overreach. 15a Strong.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — cross-domain formalism transfer is a primary engine of discovery, and the FEP is offered as a general framework for any Markov-blanketed system (program+programmer as the joint system answers the referent objection). Incorporated as the premise's "provisional-adoption + scheduled structural test" condition, which scopes rather than refutes: the premise forbids treating the bridge as SETTLED on lexical grounds, not exploring it.
  Confidence: Moderate
  Applicable to: every CROSS adoption of a cross-tradition/cross-program bridge (Master agent; cross_program_index.md); the displacement-vector / analogy machinery (ASSUMPTION-009/010); the specific Wolfram×Friston "bug↔free-energy" bridge (held as open measurement below).
  Re-check due: 2026-10-26 (Quarterly)
  OPEN MEASUREMENT NAMED AT VALIDATION: for the Wolfram×Friston bridge, attempt the explicit mapping spec⇒generative-model, intent⇒boundary-condition, bug⇒high-surprise-state and check whether the FEP's core relations survive; if only the labels survive, the bridge is linguistic and must not be CROSS-adopted (research-question in-house test).
  Status: ACTIVE

PREMISE-128:
  Date validated: 2026-07-26
  Source item: PRESUMPTION-546
  Statement: A defect that produces no error and plausible-looking output cannot be certified "benign" from its visible outcome, because its blast radius is by construction unknown at the point of failure. This is the silent-data-corruption class: the fault emits no log/exception, so damage is neither bounded by nor visible in the immediate result and propagates through records that downstream cycles trust (here: a hardcoded-pids path that silently recorded phantom APPROVEs and dropped real proposals). Such a defect is fail-silent-AND-wrong — the most dangerous fault posture (neither fail-silent-safe nor fail-safe). The correct response is not a per-cycle benignity judgment but DETECTION: a reconciliation/assertion that recomputes the records against an uncorrupted source and can actually fail. Disposition records touched by such a path are suspect until reconciled, not presumed trustworthy.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: designers presumed disposition records trustworthy and inferred "benign" from a plausible outcome)
  Supporting evidence: Meta Engineering (2022), "Detecting silent errors in the wild"; Synopsys, "What is Silent Data Corruption"; Bosilca et al. (2013), "On the Combination of Silent Error Detection and Checkpointing" (detection latency); fail-silent vs fail-safe fault-tolerance patterns; audit-trail integrity (incomplete trails reduce trust). 15a Strong.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Weak) — severity/priority triage legitimately deprioritizes bounded-blast-radius bugs. Incorporated as a boundary: triage REQUIRES a known blast radius, which a silent record-corrupting defect denies; so the challenge prescribes "measure/bound first," not "certify benign." Weak against this specific claim.
  Confidence: Moderate
  Applicable to: the review tool (generate_review_page.py) and every disposition-record writer; any pipeline stage that writes records with no error path; audit-trail trust assumptions fleet-wide. Complements PREMISE-005/006 (surface degraded state; don't reconcile silently) and PREMISE-124/126 (self-measurement calibration; recency≠reconfirmation).
  Re-check due: 2026-10-26 (Quarterly)
  OPEN MEASUREMENT NAMED AT VALIDATION: run the in-house reconciliation of the 07-20 event (ASSUMPTION-535) — count recorded dispositions against source proposals and search for the 7 phantom IDs / 2 dropped proposals; a clean reconciliation bounds this instance, a mismatch confirms realized cross-cycle corruption.
  Status: ACTIVE

PREMISE-129:
  Date validated: 2026-07-27
  Source item: PRESUMPTION-555
  Statement: A formal-mathematical identity claim (e.g., "Q_A is identical to the blanket generative model") is settled by DERIVATION/PROOF, not by an agent's stated verdict. An agent asserting identity produces a CLAIM, not a determination; LLM self-report of correctness is empirically unreliable and poorly calibrated (high confidence frequently accompanies wrong answers). A candidate must therefore not be adopted as CROSS on a bare stated verdict: attach a PROOF OBLIGATION — a short derivation checked by an independent verifier (a computer-algebra system, a proof assistant, or a decorrelated differently-prompted agent). "Decidable" is accurate only when the verdict ships a checkable derivation; the check, not the assertion, is the arbiter.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: designers treated a proof-shaped question as settleable by self-report)
  Supporting evidence: Huang et al. (2023), "LLMs Cannot Self-Correct Reasoning Yet," arXiv:2310.01798; "Self-Verification Abilities of LLMs in Logical Reasoning," arXiv:2311.07954; overconfidence-when-wrong, arXiv:2501.09775; autoformalization faithfulness, arXiv:2606.16118; proof theory (identity established by derivation). 15a Strong.
  EXTERNAL REFERENT (satisfies PREMISE-124; directly answers PRESUMPTION-556/REVISE-246): this INCORPORATE rests on proof theory + an external empirical LLM-limitation literature, NOT on intra-pipeline agreement. That is the stated reason it clears INCORPORATE while sibling PRESUMPTION-554 was held at MONITOR (MONITOR-485).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — with a verifier in the loop, a stated verdict backed by a checkable derivation CAN settle the question, and many identities are trivially checkable. Incorporated as the premise's "attach a checker" condition, which scopes (require derivation + independent check) rather than refutes.
  Confidence: Moderate
  Applicable to: the CROSS-question "decidability" procedure; Master agent / cross_program_index CROSS adoption; any step adopting a formal claim on an agent's stated verdict. Coheres with PREMISE-049 (verify-before-trust) and PREMISE-124 (external referent), specialized to formal-identity claims.
  Re-check due: 2026-10-27 (Quarterly)
  OPEN MEASUREMENT NAMED AT VALIDATION: attach a proof-obligation field to the CROSS-decidability step and check whether any candidate (e.g., friston_hoffman) was adopted as CROSS on a bare verdict with no derivation; a bare-verdict adoption confirms the premise's necessity (in-house).
  Status: ACTIVE

PREMISE-130:
  Date validated: 2026-07-28
  Source item: PRESUMPTION-557
  Statement: RECURRENCE RECLASSIFIES. When the same component fails a third time in a third distinct signature, the correct unit of analysis is a DEFECT CLASS in that component, not three independent bugs; the empirical basis is that prior fault count is the dominant predictor of future faults and that faults cluster densely in a small minority of modules. Operationally: a third incident in one generator obliges a class-level diagnosis (what shared structure produces all three signatures?) before, or alongside, any local fix. SCOPE GUARD (load-bearing, from 15b): this premise licenses the RECLASSIFICATION only. It does NOT license the implied remedy of unifying the render and submit layers — that is a separate decision governed by PREMISE-066 and its scope guard (SSOT relocates rather than removes the failure mode, and the extraction boundary must fail loudly), and premature unification carries the recognised cost of the wrong abstraction. A cheap local fix and a class-level diagnosis are not alternatives; the local fix is not a substitute for the diagnosis, and the diagnosis is not a reason to withhold the fix.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: three incidents were logged and closed individually with no class-level question asked)
  Supporting evidence: Ostrand, T.J., Weyuker, E.J. & Bell, R.M. (2005), "Predicting the Location and Number of Faults in Large Software Systems," IEEE TSE 31(4):340-355 — prior faults are the dominant predictor; the top 20% of files held 71-92% of faults. Fenton, N.E. & Ohlsson, N. (2000), "Quantitative Analysis of Faults and Failures in a Complex Software System," IEEE TSE 26(8):797-814 — defect clustering (cited by 15b, and it supports the clustering half). 15a SUPPORTED/Strong; EXTERNALLY ANCHORED.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — most modules hold zero faults, so clustering is a prior about WHERE to look, not a proof that any particular trio shares one cause; and the implied unify-the-layers remedy risks the wrong-abstraction cost in a module already under three-incident stress. Both points are folded in as the scope guard rather than rejected.
  Confidence: Moderate
  Applicable to: generate_review_page.py and the review-page toolchain (ASSUMPTION-550/551); the incident-logging convention generally — any component with >=3 logged incidents; couples PREMISE-066 (SSOT) for the remedy question.
  Re-check due: 2026-10-28 (Quarterly)
  Status: ACTIVE

PREMISE-131:
  Date validated: 2026-07-28
  Source item: PRESUMPTION-558
  Statement: A WARNING IS NOT A CONTROL, AND AN UNDELIVERED WARNING IS NOT A MITIGATION. In the established hierarchy of controls, warnings and administrative controls occupy the two least-effective tiers, below elimination, substitution and engineering controls; a written instruction is therefore the weakest admissible mitigation for a tool that silently writes wrong records, and where an engineering control is cheap the hierarchy directs that it be used instead. Further, and decisively here: a warning carried on a delivery channel that has failed has ZERO effect, not reduced effect — the C-HIP model locates the failure at the delivery stage, upstream of attention, comprehension and compliance, so no amount of emphasis (bolding) compensates. THIRD CLAUSE, folded in from 15b: a confirmation dialog does NOT qualify as the engineering control, because habituation drives compliance toward reflexive acceptance at scale. The admissible mitigations are elimination (make the defective page unreachable) or an interlock that removes submit capability, not a notice and not a prompt.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: designers recorded the warning AS the mitigation)
  Supporting evidence: NIOSH/CDC Hierarchy of Controls — signs and warning labels are classified as administrative controls, the second-least-effective tier. Wogalter, M.S. (2006), Communication-Human Information Processing (C-HIP) model, in Handbook of Warnings — a warning must pass delivery before any downstream stage can operate. Böhme, R. & Köpsell, S. (2010), "Trained to Accept? A Field Experiment on Consent Dialogs," CHI '10, pp. 2403-2406 (n~80,000) — habituation defeats confirmation dialogs. 15a SUPPORTED/Strong; EXTERNALLY ANCHORED.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — the challenge targets the IMPLIED REMEDY (a confirmation interlock), not the claim; it is incorporated as the third clause. 15b also independently confirms via C-HIP that the failing stage is delivery. The two directions CONVERGE on the same conclusion: disable the page rather than warn about it.
  Confidence: High (both search directions converge; three named external referents; remedy is cheap and in-house)
  Applicable to: the defective review page reachable from review_log.html (ASSUMPTION-550); any destructive-write tool guarded by notice or confirmation only; the sync/notification channel dark for 5 consecutive runs (ASSUMPTION-559 / OPEN-135) — any mitigation routed over it must be scored as zero until delivery is restored.
  Re-check due: 2026-10-28 (Quarterly)
  Status: ACTIVE

PREMISE-132:
  Date validated: 2026-07-28
  Source item: PRESUMPTION-559
  Statement: CITING IS NOT VERIFYING. The presence of a citation is not evidence that the citing claim was checked against the cited source; in generated text the measured rate of full support between a sentence and its own citation is roughly half, so a register in which "all items do cite external referents" is a statement about FORM, not about verification. An external-referent audit that counts citation strings therefore establishes nothing about the property it claims to audit. SECOND CLAUSE, NARROWED by 15b (load-bearing): the further inference that the pipeline "cannot audit its own external-referent property from inside" is NOT supported in that strong form. Internal consistency checking — querying a decorrelated instance about the same reference without any external resource — detects hallucinated and misattributed references at materially better than chance. The requirement is therefore DECORRELATION, not externality: a check by a differently-prompted or differently-instantiated agent is a real reduction in risk and is available in-house today; a fully external check (human, or a model with no access to the corpus) remains the strongest grade but is not the only admissible one.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the audit was reported as a clean result)
  Supporting evidence: Liu, N.F., Zhang, T. & Liang, P. (2023), "Evaluating Verifiability in Generative Search Engines," Findings of EMNLP — only 51.5% of generated sentences were fully supported by their citations; 74.5% of citations supported their sentence. Agrawal, A., Suzgun, M., Mackey, L. & Kalai, A.T. (2024), "Do Language Models Know When They're Hallucinating References?", Findings of EACL — direct and indirect consistency queries identify hallucinated references without external resources (cited by 15b, and it supplies the narrowing). 15a SUPPORTED/Strong; EXTERNALLY ANCHORED.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — over-reading defers all citation assurance to an arbiter unavailable for 5 dark syncs when a cheap decorrelated internal check exists today. Incorporated as the second clause. Residual risk noted: a decorrelated check within one model family is not independent in the strong sense (MONITOR-486), so it lowers risk without discharging it.
  Confidence: Moderate
  Applicable to: PREMISE-127/128/129's external-referent audit (MONITOR-485/486, ASSUMPTION-553/558); the standing external-referent requirement of PREMISE-124; every "externally anchored" annotation in 15a returns, including this batch's. IMMEDIATE APPLICATION: the phrase "virtual governor" attributed to Levin was NOT confirmed against the primary text in this run's search (MONITOR-487) — an in-batch instance of exactly this premise.
  Re-check due: 2026-10-28 (Quarterly)
  Status: ACTIVE

PREMISE-133:
  Date validated: 2026-07-28
  Source item: PRESUMPTION-560
  Statement: ABSTENTION IS A DECISION AND REQUIRES A WRITTEN DISCHARGE RULE. Declining to adopt is an action inside the decision problem with its own cost, not an exit from it, and suspension of judgement is a committal attitude requiring its own warrant rather than a null state. TWO DISTINCT ASYMMETRIES must be kept apart, and the register's sources cut opposite ways on them: (i) DECISION-THEORETIC asymmetry — abstention is a distinct action with a distinct, often lower cost — IS established (Chow; El-Yaniv & Wiener); (ii) SELF-REFERENTIAL asymmetry — that self-reference results license self-abstention while forbidding self-endorsement — is NOT established, since those results constrain self-endorsement specifically and supply no symmetric licence. This premise asserts (i) and denies that (ii) has been shown. From (i) plus the natural-justice recusal-with-transfer norm and third-party-audit practice — an is/ought step, NOT an entailment from the decision-theoretic results — the operative requirement follows: a MONITOR issued on self-referential grounds is only a legitimate suspension if it names (a) what would discharge it, (b) who or what adjudicates, and (c) a deadline after which continued suspension is itself reported as an unresolved exposure. Absent all three, the suspension silently becomes a permanent verdict of non-adoption, and the register's most consequential items are excluded from the corpus while appearing to be "under monitor." EXPLICITLY NOT INCORPORATED (positively refuted by 15b; conceded as overreach in 15a's own caveat (a) while 15a still returned SUPPORTED — so this is ONE refutation plus a concession, not two independent refutations): the strong reading that abstention and endorsement are epistemically EQUIVALENT because both are outputs of the same model. Abstention is asymmetric — a weaker commitment with a distinct and characterisable error profile that reduces risk on the region it does cover — so refusing to self-endorse is not merely self-endorsement in disguise, and the pipeline declining to certify its own reliability is conformant behaviour, not a fault. What survives is the narrow, self-binding form above.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the abstention was recorded as a principled result with no discharge condition)
  Supporting evidence: Chow, C.K. (1970), "On Optimum Recognition Error and Reject Tradeoff," IEEE Trans. Information Theory 16(1):41-46, and El-Yaniv, R. & Wiener, Y. (2010) on selective prediction / risk-coverage — abstention is a third action with its own cost and an asymmetric profile. Friedman, J. (2017), "Why Suspend Judging?", Noûs 51(2):302-326 — suspension is committal, not null. Nemo iudex in causa sua (natural justice: recusal-with-transfer, not recusal-into-silence); Raji, I.D. et al. (2022) on third-party audit and escalation routes. 15a SUPPORTED/Strong on the abstention-is-a-decision clause and on asymmetry (ii) being not-established; Moderate on "permanently unadoptable by construction"; EXTERNALLY ANCHORED.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — establishes the asymmetry positively (Chow; El-Yaniv & Wiener) and argues from Tarski-style undefinability that unadoptability follows from self-reference rather than from 15c's choice. NOT RESOLVED HERE, and the distinction is consequential: if that argument holds, a NAMED ADJUDICATOR INSIDE the system is unreachable in principle, not merely unmet this run — which does not weaken requirement (b) but does determine that it can only be satisfied by an adjudicator OUTSIDE the system (Tom, or a model with no access to the corpus). REVISE-247 is written accordingly. Carried as an open question rather than assumed away. Both directions nevertheless CONVERGE on the surviving clause: suspension is defensible only if it keeps the question open with a specified escalation route. Recorded honestly: this premise binds 15c itself, and 15c adopted it rather than abstaining a second time. That adoption AVERTS THE FAILURE MODE PRESUMPTION-560 PREDICTED (a second abstention would have made the item unadoptable by construction); it does NOT satisfy (a)/(b)/(c) above, which remain unmet — see the fail-loud note and REVISE-247. The word "discharge" is reserved throughout for (a)/(b)/(c). The concrete unmet need (no arbiter or discharge rule exists for MONITOR-486) is NOT resolved here and is raised as REVISE-247.
  Confidence: Moderate
  Applicable to: DIRECTLY (within the Statement's scope — suspensions issued on self-referential grounds): 15c disposition practice; MONITOR-486 / PRESUMPTION-556. BY ANALOGY ONLY, NOT LICENSED BY THIS PREMISE: the ~174-item 15d re-trigger backlog and the MONITOR-420/423 fired-trigger cohort exhibit the same outcome (suspension becoming non-adoption by default) but are backlog/expiry artifacts, not self-referential suspensions; they need their own grounds and are covered by DISPOSITION-536 / PRESUMPTION-553 and MONITOR-423. Complements PREMISE-124.
  Re-check due: 2026-10-28 (Quarterly)
  Status: ACTIVE

PREMISE-134:
  Date validated: 2026-07-28
  Source item: PRESUMPTION-562
  Statement: REFLEXIVE SCOPE-EXTENSION OF PREMISE-127. The transfer-condition standard PREMISE-127 imposes on generated cross-formalism bridges applies SYMMETRICALLY to the project's own self-descriptions. A claim of the form "external construct X is close to a formal description of what a tradition is" is a cross-domain mapping and carries the same burden: shared ATTRIBUTES (abstract / non-physical / causally instructive) are surface features, and warrant requires named ALIGNED RELATIONS — state what the external construct causally DOES (stored target state, error signal, corrective actuation, arrest on achievement) and what the tradition-level analogue is claimed to do, then count aligned relations against shared adjectives. Self-descriptions warrant MORE scrutiny than generated bridges, not less, because they are load-bearing for every downstream bridge that inherits them, and because recognising one's own framework in external work is a recognised confirmation-bias risk rather than a neutral observation. BOUNDARY (load-bearing, from 15b and consistent with PREMISE-127): the check gates CROSS ENTRY, not the comparison. Holding the analogy at discovery grade is legitimate and productive; what is forbidden is settled adoption on descriptor overlap. Record the positive, negative and neutral analogy separately, since performing the alignment is itself the mechanism by which non-alignable differences become visible.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the project's own self-description was exempted from the standard the project requires of its machines)
  Supporting evidence: Gentner, D. (1983), "Structure-Mapping," Cognitive Science 7(2):155-170; Gentner, Rattermann & Forbus (1993), Cognitive Psychology 25(4) — surface similarity drives retrieval but is dissociable from inferential soundness; Markman & Gentner (1993/1996) — non-alignable differences are systematically under-weighted; Nickerson, R.S. (1998), "Confirmation Bias," Review of General Psychology 2(2); Hesse, M. (1966) on positive/negative/neutral analogy. 15a SUPPORTED/Strong.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — structure-mapping grades alignment rather than gating it; refusing the comparison suppresses the very check being demanded; and independent convergence by a researcher in another domain is what consilience counts as evidence, not automatically bias. Incorporated as the boundary clause.
  CORRELATION DISCLOSURE (per PREMISE-124 / MONITOR-486): this premise is an EXTENSION of PREMISE-127, not an independent finding, and rests on the SAME primary source as PREMISE-127 (Gentner 1983), and PREMISE-127 additionally cites Gentner & Markman 1997, which 15b also relies on this run. Its increment over PREMISE-127 is the reflexive scope only. It should not be counted as independent corroboration of PREMISE-127.
  Confidence: Moderate
  Applicable to: any CROSS entry deriving from the Levin virtual-governor / tradition mapping (ASSUMPTION-557; gated pending MONITOR-487); the project's self-description layer generally; Master agent / cross_program_index.md; extends PREMISE-127; instance of the same reflexive-application gap as REVISE-246 (PREMISE-124 not applied to itself) and REVISE-245 (PREMISE-123 propagation).
  Re-check due: 2026-10-28 (Quarterly)
  Status: ACTIVE

PREMISE-135:
  Date validated: 2026-07-29
  Source item: PRESUMPTION-566
  Statement: TERMINALITY IS PURCHASED BY ENUMERATING THE DOMAIN, NOT BY ACCUMULATING INSTANCES. A correction that supersedes a series of earlier abstractions may not be declared "the general case" on the strength of covering every instance seen so far, because that is the same standing each superseded abstraction had at the moment it was written. There is no schema-level warrant for "generalise from the instances seen": an inductive step is licensed by a stated material fact about the domain, so a claim of terminal generality owes three things and is otherwise asserted rather than shown — (a) THE POPULATION, an enumeration of the kinds over which generality is claimed, without which "the general case" and "its worst-covered instance" have no determinate content; (b) THE TERMINATION CRITERION, a stated condition under which the abstraction would be considered general (in the version-space form, that the surviving hypothesis set over the stated population is a singleton); and (c) ONE SEVERE TEST, a correct advance prediction about at least one kind that was NOT among the instances that produced the abstraction — because an abstraction constructed to fit the very instances that broke its predecessors has not been tested by them. SCOPE GUARD (load-bearing, from 15b, and it refutes the source item's own central inference): PROCEDURE-IDENTITY IS NOT A DEFEATER. "It was reached by the same method as the four it replaced, therefore it inherits their standing" is a genetic inference and is NOT incorporated. Warrant does not come from the procedure; iterated conjecture-and-refutation is the mechanism by which conjectures genuinely improve, elimination contracts the hypothesis set monotonically, and late position in a refutation series is a credential rather than a disqualification. Nor is an unspecified reference class a discriminating criticism of any particular replacement, since that problem is universal to every inductive and probabilistic claim whatever. SYMMETRY CLAUSE: the moral "a generalisation is only as good as its worst-covered instance" applies to the replacement as well as to what it replaced — so the operative action is to NAME the worst-covered instance of the NEW abstraction and go and look at it, not to withhold adoption.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: a fifth diagnosis was written in the past perfect ("was always") while the moral it carried was applied only to its predecessors)
  Supporting evidence: Norton, J.D. (2003), "A Material Theory of Induction," Philosophy of Science 70(4):647-670, expanded as The Material Theory of Induction (University of Calgary Press, 2021) — there are no universal inductive inference schemas; warrant comes from contingent material facts holding locally. Lakatos, I. (1976), Proofs and Refutations, eds. Worrall & Zahar, Cambridge University Press — the succession of definitions of "polyhedron" under counterexample, each adequate to every instance then known, with monster-barring named as the device by which a superseded generalisation is retrospectively made to look as though it had been right all along. Mitchell, T.M. (1982), "Generalization as Search," Artificial Intelligence 18(2):203-226 — version spaces contract monotonically and possess an internal, checkable termination test (the general and specific boundary sets coincide). Mayo, D.G. (2018), Statistical Inference as Severe Testing, Cambridge University Press — a hypothesis passes severely when it agrees with the data AND would with high probability have failed had it been false; the sharp objection is to double-counting, not to iteration. Hajek, A. (2007), "The reference class problem is your problem too," Synthese 156(3):563-585. Card, A.J. (2017), "The problem with '5 whys'," BMJ Quality & Safety 26(8):671-677 — the assumption that the fifth iteration is the right terminus is criticised as unevidenced in applied safety practice. 15a SUPPORTED/Moderate-Strong; 15b PARTIALLY-CHALLENGED/Moderate. EXTERNALLY ANCHORED: every referent is a named work outside the pipeline, which is the stated ground on which this clears the PRESUMPTION-556 / REVISE-246 bar.
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate) — and the challenge is load-bearing rather than incidental: it REFUTES the source item's central inference, which is why the scope guard above is part of the statement and the parity reading is explicitly excluded. 15b's remaining point, that over-reading produces a regress in which no correction can be banked and the moral self-undermines, is answered by the symmetry clause: the requirement is to name the population and test out of sample, not to withhold adoption pending an unattainable certificate. 15a's own caveat (a) cuts the same way and is recorded: on a material theory a well-chosen background fact warrants a strong induction from very few instances, so if the fact underwriting "every page kind in this system renders its state through a controls region" can be stated, n=3 is ample and the abstraction is terminal in the only sense available. The literature supports "the induction is unwarranted as stated," NOT "the conclusion is wrong."
  Confidence: Moderate
  Applicable to: the prs_3d / roster-reader "read the controls" abstraction and any successor abstraction that supersedes it; any diagnosis in the incident record declared general after superseding earlier general cases; 14b's own presumption-construction, which must apply the symmetry clause to its own replacements; couples PREMISE-101 (counts are properties of a stated (scope, method, time) reading) by extending the same discipline from counting to generalising.
  Re-check due: 2026-10-29 (Quarterly)
  OPEN MEASUREMENT NAMED AT VALIDATION: enumerate the remaining page kinds the roster reader must handle. For each, record IN ADVANCE what "read the controls" predicts, then check. Correct prediction on kinds absent from the original four failures -> the parity claim is refuted and the abstraction has passed a severe test. Failure on a kind whose controls are absent, virtual, or rendered elsewhere -> the abstraction is fitted rather than general and the worst-covered instance has been located. Cheap third diagnostic, worth running FIRST: check whether the four superseded abstractions were each falsified by a DIFFERENT kind of counterexample or by variations on one kind — genuine eliminative convergence requires the former, and the latter would show the series narrowing within a single reference class and would substantially strengthen the original presumption. All three are in-house tests.
  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c]
    Original item: PRESUMPTION-566
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from a correction stated as terminal, arrived at by the same method that produced the four corrections it supersedes
      15a: Searched for supporting literature; SUPPORTED (Moderate to Strong)
      15b: Searched for challenging literature; PARTIALLY-CHALLENGED (Moderate) — central inference refuted, constructive requirement endorsed
      15c: Net evaluation and disposition; INCORPORATE the convergent narrowed form, parity inference explicitly excluded as a scope guard
    Current status: INCORPORATED
    Disposition record: DISPOSITION-549 (lit_search_returns.md, 2026-07-29)
  DUPLICATION CHECK (per PREMISE-105 / register inflation, run before minting and reported here): checked against PREMISE-001..134. Nearest neighbours are PREMISE-101 (counts are properties of a (scope, method, time) reading) and PREMISE-105 (definitional change breaks a series); neither governs the warrant of a generalisation over an unenumerated population, and no premise in the register states a stopping criterion for abstraction. Increment over PREMISE-101: the reference-class and termination requirements plus the out-of-sample severity test. No contradiction with any ACTIVE premise found.
  IN-RUN NOTE: this is the ONLY INCORPORATE of the 2026-07-29 batch, against five in the 2026-07-28 batch. Per DISPOSITION-552 / REVISE-250 that movement is reported as a count with its denominator (1 of 8 items) and is NOT offered as evidence about the external-referent bar, about this batch's rigour, or about anything else — a 5-to-1 movement on counts this small is inside ordinary variation for the same reason a 1-to-5 movement is.

PREMISE-136:
  Date validated: 2026-08-01
  Source item: PRESUMPTION-604
  Statement: THE ACHIEVABLE DENOMINATOR OF A SETTLING QUANTITY IS FIXED BY ITS DECLARED SCOPE, NOT BY ITS WORDING. Statistical power in a monitoring system is a property of the accrual design — events per unit time times the observation window — so a quantity scoped to one run of a daily pipeline with single-digit batches has a single-digit denominator by construction, and no rephrasing changes that. Three consequences are binding. (1) EVERY settling quantity must DECLARE its scope — run / cohort / corpus — at the point it is written, so that its achievable denominator is visible at drafting time rather than discovered at evaluation time. (2) Rescoping is a legitimate and usually the cheapest route to a usable denominator: the register demonstrably contains corpus- and cohort-scoped quantities with two- and three-digit denominators (209 partials in PRESUMPTION-611; the full cross-tradition artifact corpus in PRESUMPTION-602, both minted 2026-07-31), so a claim that no route to a larger denominator exists is false of this register and must be checked against it before being asserted. (3) POOLING ACROSS RUNS IS NOT A FREE ROUTE and is not admissible without a stated homogeneity condition for the pooled units: the meta-analysis literature on few and heterogeneous studies reports that pooling compromises coverage or yields inconclusively wide intervals, and that small-sample Bayesian estimators regress rare cells toward the prior — which is precisely where this register's interesting cases live. SCOPE GUARD (load-bearing): this premise does NOT say a single-digit denominator makes a quantity undecidable. Exact small-sample and conditional-likelihood methods give valid inference at small n; what they give is a WIDE interval, and reporting a wide interval honestly is admissible where reporting a point estimate is not. The failure mode this premise names is the undeclared scope, not the small number.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the daily cadence was not read as a sampling design)
  Supporting evidence: Kim et al. 2026, "Sequential Event Rate Monitoring," Statistics in Medicine (10.1002/sim.70359) — accrued events, not looks, determine power. Lakens, "Sequential Analysis" (Improving Your Statistical Inferences) — information accumulates across looks only under a pre-specified spending function. Anytime-valid / e-value monitoring (arXiv 2602.06379). Bayesian group-sequential snSMART designs for irreducibly small n.
  Challenges noted (15b, and folded in above rather than outweighed): exact inference for small/sparse data (PMC12456449) shows small n does not preclude valid inference; meta-analysis-with-few-studies work (arXiv 1807.09037; PMC10503457) shows pooling few heterogeneous units degrades coverage; small-sample bias adjustment shows regression toward the prior in rare cells. 15b's decisive counterexample — that the register already contains two- and three-digit-denominator quantities — is clause (2) above and REFUTES the source item's universal claim.
  Confidence: Moderate
  Applicable to: 14a and 14b item drafting (scope declaration is now required); 15c disposition (a quantity with no declared scope is not evaluable); 15d re-evaluation; every register that records a settling quantity.
  DEPENDENCY, NAMED NOT LAUNDERED: this premise bears on REVISE-257 (2026-07-31, unratified) and, if REVISE-257 is ratified, entails that its feasibility clause is satisfiable by rescoping. That entailment is a consequence of this premise and is NOT part of it; this premise does not give content to REVISE-257 and does not presume its ratification.
  Re-check due: 2026-09-01
  Status: ACTIVE

PREMISE-137:
  Date validated: 2026-08-01
  Source item: PRESUMPTION-609
  Statement: A DIFFERENCE-BASED CHECK IS A CHANGE DETECTOR, AND ITS CORRECTNESS-DETECTING POWER IS INHERITED FROM ITS BASELINE, NOT INTRINSIC. Comparison of a run's output against a prior run's is a DERIVED (pseudo-)oracle in the standard taxonomy: it renders a verdict relative to its reference, so a fault present in both the reference and the current run is invisible to it by construction. Three cases follow and must be treated as coverage gaps rather than as edge cases: (a) a FIRST-EVER RUN has no reference and the check cannot fail; (b) a NEWLY ADDED check has no history and is in the same position on its first execution; (c) as the monitored corpus becomes legitimately variable, differences stop being diagnostic and the detector's power degrades continuously — a check gains apparent quiet exactly as its subject becomes noisier. THEREFORE: any check suite whose verdict is a diff must (i) classify each of its checks by whether it can fail with no prior for comparison, and (ii) contain at least one BASELINE-INDEPENDENT invariant over each quantity it certifies. LOAD-BEARING CONDITION, from 15b and not optional: an invariant counts as coverage ONLY after it has been MUTATION-VALIDATED — the known defect is deliberately reintroduced and the invariant is confirmed to fire. Metamorphic-relation quality varies sharply and weak relations produce confident passes in the presence of faults; an unvalidated invariant adds perceived coverage without detection, which is worse than the gap it was added to close. SCOPE GUARD: this premise does NOT deprecate cross-run comparison. Derived oracles are legitimate, standard, and warrant-transmitting when the baseline has itself been verified; the requirement is that the baseline's verification be stated and that at least one check not depend on it. For case (c) specifically, the admissible discipline is approval/golden-file testing — diffs surfaced and explicitly approved — not silent tolerance of legitimate change.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: a successful self-catch was reported as an outcome, not examined as a mechanism with a domain)
  Supporting evidence: Barr, Harman, McMinn, Shahbaz & Yoo 2015, "The Oracle Problem in Software Testing: A Survey," IEEE TSE — classifies comparison against a prior version as a derived pseudo-oracle. Chen et al., metamorphic testing corpus (HKU TR-2017-04) — MRs are checkable without a prior run. Liu, Kuo, Towey & Chen, "How effectively does metamorphic testing alleviate the oracle problem?" IEEE TSE — MT detects faults reference-comparison misses.
  Challenges noted (15b, folded in as the load-bearing condition rather than outweighed): METRIC (Chen et al., JSS 2015) and MR-recommendation work — MR identification requires deep domain knowledge and is the field's hardest open problem; MR effectiveness under mutation testing (PMC11051087) and arXiv 1904.07348 — fault-detection effectiveness varies sharply with MR quality; MT false-positive work — invariant violations are not self-interpreting and inapplicable conditions produce alerts (PREMISE-131 alert-fatigue territory).
  Confidence: High on the classification and cases (a)-(c); Moderate on the sufficiency of the remedy clause.
  Applicable to: the nightly Summa verification suite; the metabolism regeneration check; the wiki_narration validation script; any monitor whose verdict is a diff against a prior run. Extends PREMISE-120 (reproduction does not confirm) to the case where the two compared runs are DIFFERENT runs rather than a re-run, which PREMISE-120 does not cover.
  Re-check due: 2026-09-01
  Status: ACTIVE

PREMISE-138:
  Date validated: 2026-08-02
  Source item: PRESUMPTION-616
  Statement: REPETITION INSIDE A CHANNEL THAT HAS NO EFFECTOR IS NOT A REMEDY; ITS ONLY ADMISSIBLE
    FUNCTION IS TRANSFER OF OBLIGATION TO A NAMED ACTOR OUTSIDE THE CHANNEL. This is a SCOPE
    EXTENSION of PREMISE-131 (a warning is not a control) from the single-warning case to the
    repetition/escalation case, and it is the answer to "the last report had no effect, so write
    another one." Three clauses are binding. (1) MAGNITUDE: informational feedback does move
    practice, but by a small amount — the current Cochrane synthesis (CD000259.pub5, 177 studies,
    558 dichotomous outcomes) reports a median absolute improvement of 2.7% (IQR 0.0 to 8.6) and,
    on the multiplicity-adjusted effective-sample-size-weighted meta-analysis, a mean absolute
    increase of 6.2% (95% CI 4.1 to 8.2, moderate-certainty). The weighted figure, not the median,
    is the correct one to quote; see the CORRECTION note below. A 6.2% shift is a real effect and
    is NOT an effector. (2) OBLIGATION TRANSFER, folded in from 15b and load-bearing: reporting is
    not thereby useless. A report that names a recipient who possesses an effector discharges the
    reporting layer's duty and is strictly better than silence; what is forbidden is treating the
    report as the fix. Therefore every flag raised by a layer that cannot act MUST name the actor
    who can, and MUST leave the channel that produced it. (3) IN-CHANNEL BROADENING CAN BE
    NEGATIVE, not merely weak: the one direct test located — dual- versus single-recipient
    notification of critical results — found WORSE acknowledgement (OR 2.02 for failed follow-up),
    and clinical decision-support override rates around 90% show that adding delivery volume inside
    a saturated channel reduces response. Escalation must change the ADDRESSEE, not the amplitude.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Ivers N. et al., Audit and feedback: effects on professional practice.
    Cochrane Database Syst Rev CD000259.pub5 (2025/26) [VERIFIED against Cochrane Library, this
    run]; Singh H. et al. (2010), critical-result notification and failed follow-up, Am J Med
    [cited by 15a; NOT independently verified this run].
  Challenges noted: 15b (Strong) argues the presumption attacks a straw target — reporting was
    never intended as the effector, and the counterfactual to a disclosed report is an undisclosed
    failure, which is worse. This challenge is FOLDED IN as clause (2) rather than outweighed; the
    premise as minted says less than PRESUMPTION-616 said.
  CORRECTION FOUND AT VERIFICATION (material, and neither search direction surfaced it): BOTH 15a
    and 15b quoted only the MEDIAN absolute improvement (2.7%, or the older pub3 figure of 4.3%),
    which is the least favourable statistic in the review. The same review's weighted meta-analysis
    reports 6.2% (95% CI 4.1–8.2), i.e. an effect whose confidence interval excludes zero. Both
    directions independently selected the same under-stating summary. Recorded because it is a
    correlated error across two searches that were run in disjoint contexts, and is therefore
    evidence about the independence condition, not merely about this citation.
  Cross-direction source overlap (PREMISE-120 disclosure): Cochrane CD000259 was cited by BOTH
    directions — by 15b on this item and by 15a on PRESUMPTION-623. The convergence claim here does
    NOT rest on it: clause (2) rests on 15b's argument, clause (3) on 15a's notification sources.
  Confidence: Moderate
  Applicable to: Agent 15b SYSTEMIC-RISK-FLAG delivery; the lit-pipeline and 14a/14b run footers;
    revision_flags.md as a channel; MONITOR-420's auto-escalate; any agent that raises a flag it
    cannot itself act on.
  Re-check due: 2026-09-02 (Monthly)
  Status: ACTIVE

PREMISE-139:
  Date validated: 2026-08-02
  Source item: PRESUMPTION-621
  Statement: A DOCUMENTED CHECK IS NOT EVIDENCE THAT THE CHECK WAS PERFORMED, AND THE GAP IS LARGE,
    MEASURED, AND NAMED. In the one domain where this has been directly measured against
    ground truth — clinical documentation observed by audiovisual capture — only 38.5% of
    documented review-of-systems groups and 53.2% of documented physical-examination systems were
    corroborated by direct observation (Berdahl et al. 2019). The propagation mechanism is
    copy-forward: roughly half of note text is duplicated from prior notes, and structured
    templates IMPROVE organisation while rating WORSE on accuracy, because a template supplies the
    assertion whether or not the measurement occurred. THEREFORE: any register entry asserting that
    a check ran must carry machine-generated execution evidence (exit status, timestamped output,
    a hash of what was read) rather than a prose statement, and prose-only check records must be
    read as claims about intent, not about events. LOAD-BEARING SCOPE GUARD, from 15b and not
    optional: DUPLICATION RATE IS NOT ERROR RATE AND ERROR RATE IS NOT HARM RATE. Most copied text
    is benign redundancy; measured conversion to harm in the clinical corpus is only ~1.2–2.6%.
    This premise therefore licenses NO inference from a duplication count to a defect count, and
    anyone citing it to claim the register is largely wrong is misusing it. What it licenses is
    exactly one thing: withdrawal of warrant from prose check-records, pending execution evidence.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Berdahl C.T. et al. (2019), "Concordance Between Electronic Clinical
    Documentation and Physicians' Observed Behavior," JAMA Network Open 2(9):e1910530 — 9
    physicians, 12 observers, 180 encounters; 38.5% ROS / 53.2% PE corroboration [VERIFIED against
    JAMA Network Open and PMC6751766, this run]; Wang M.D. et al. (2017), JAMA Internal Medicine,
    46% of note text copied at character level [cited by 15a; NOT independently verified].
  Challenges noted: 15b (Strong), harm-conversion ceiling of 1.2–2.6% and the NOTE RCT finding that
    templated notes were less accurate. Folded in as the scope guard above.
  Cross-direction source overlap (PREMISE-120 disclosure): the ~50.1% duplication figure from the
    ECRI / Partnership for Health IT copy-paste corpus was cited by BOTH directions. The premise's
    load-bearing number is Berdahl's corroboration rate, which appeared in the FOR direction only,
    and the scope guard's number appeared in the AGAINST direction only. No clause rests on the
    shared source.
  Local instance VERIFIED, not inferred: this register was demonstrably contaminated by exactly
    this mechanism (ASSUMPTION-621, 2026-07-31). This is why the item does not share
    PRESUMPTION-615's fate on 2026-08-01, which failed for resting on an unverified local premise.
  Confidence: High
  Applicable to: every "checks performed" line in the 14a/14b and 15a/15b/15c run footers;
    REFRESH_STATUS.md; the nightly verification suites; PREMISE-137's mutation-validation
    requirement, which this premise supplies the motive for.
  Re-check due: 2026-09-02 (Monthly)
  Status: ACTIVE

PREMISE-140:
  Date validated: 2026-08-02
  Source item: PRESUMPTION-624
  Statement: A METRIC DERIVED FROM ONE OBSERVATION CHANNEL MUST BE NAMED BY ITS CHANNEL, NOT BY THE
    THING THE CHANNEL PROXIES FOR. The defect in "27 consecutive autonomous days" is not the
    computation — the mtime and transcript sweep is accurate about what it observed — but the NAME,
    which asserts a property of the world while measuring a property of the instrument. The correct
    form is "27 days with no observed human edit in mounted paths." Two clauses. (1) NAMING: any
    quantity computed from a single channel carries its channel in its label; where the label would
    otherwise generalise, the generalisation is the claim requiring evidence, and it is separate
    evidence from the count. (2) STREAK FRAMINGS ARE BARRED for channel-derived metrics, because a
    streak converts an accumulating absence-of-observation into an accumulating positive claim, and
    its rhetorical force grows with exactly the quantity that should be reducing confidence. This
    extends PREMISE-124(b) — which bars calling a self-audit complete while a channel is dark —
    from completeness claims to the naming of routine metrics, where the same missingness mechanism
    operates without anyone noticing it has been invoked. CONCESSION FROM 15a, recorded because it
    is unusual: 15a found NO literature supporting generalisation from a single channel, i.e. the
    FOR direction returned nothing for the practice as performed.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: coverage error and unit error as standard total-survey-error classes; Sen I.
    et al. (2021), "Total Error and Variability Frameworks for Digital Trace Data," Public Opinion
    Quarterly (TED-On) [cited by 15a; NOT independently verified this run]. 15a result was
    NO-SUPPORT-FOUND for the practice, which is support for the premise.
  Challenges noted: 15b (Strong) — all measurement is channelled, so the standard cannot be "use an
    unchannelled metric"; and the unmounted-corpus work may lie genuinely outside the autonomy
    claim's intended scope, making this a labelling error rather than a computation error. THIS
    REFRAMING IS THE PREMISE: 15b's challenge supplied the remedy, and the premise as minted is
    15b's position, not PRESUMPTION-624's.
  Concrete triggering instance: a same-day report that the human rewrote 8 synthesis files in an
    unmounted corpus, against a 27-day headline computed from mounted-path mtimes only.
  Confidence: High
  Applicable to: the daily 14a/14b intake footers; the autonomy-day counter wherever it appears;
    PRS yield-per-tradition figures; any count over `wiki/` mtimes; the systemic-risk flag's
    central inference, which currently rests on the autonomy count.
  Re-check due: 2026-09-02 (Monthly)
  Status: ACTIVE

PREMISE-141:
  Date validated: 2026-08-05
  Source item: PRESUMPTION-664
  Statement: ABSENCE OF A REPORT IS A THIRD TERMINAL STATE, NOT A VALUE OF THE OTHER TWO; AND
    CORRELATED TERMINATION VOIDS PER-RUN INDEPENDENCE. Two clauses, and neither restates
    PREMISE-110. (1) OMISSION IS NOT CRASH. Cristian's failure-semantics taxonomy separates a
    component that runs and produces no response (omission) from one that does not run (crash);
    they are distinct classes requiring distinct detectors, and a system that detects only one
    is uncovered for the other. C2A2's scheduled-run data model is two-valued and therefore
    CANNOT REPRESENT what was observed on 2026-08-04 — four sessions that started, did work of
    unknown extent, and emitted no verdict of any kind. Until the model carries a third state
    (RAN-AND-DIED-SILENT, distinct from NEVER-STARTED and RAN-AND-REPORTED) each reader supplies
    the missing value from their own prior, and nothing downstream can distinguish work not done
    from work done and discarded. The remedy is the inverted signal PREMISE-086 already
    prescribes — alarm on the ABSENCE of a terminal record within a deadline — and the finding
    here is that 086 is not enforced for scheduled agent sessions. (2) CORRELATED TERMINATION,
    which has no antecedent in this register: the four silent runs were ONE event with one cause,
    not four independent failures. Any fleet reliability figure computed as a product of per-run
    failure probabilities is therefore wrong by orders of magnitude, and any redundancy argument
    that counts two instruments as two chances is counting one. This is the ARITHMETIC complement
    to PREMISE-110's common-mode scope guard: 110 establishes that a monitor sharing a failure
    domain with its subject is a single channel wearing two labels; 141 adds that every
    independence-assuming calculation built on those two labels is void, including the
    coverage claims of any monitor added in response to this batch.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Cristian F. (1991), "Understanding Fault-Tolerant Distributed Systems,"
    CACM 34(2) — omission/crash/timing/response taxonomy [cited by 15b; NOT independently
    verified this run]. Mahmood A. & McCluskey E.J. (1988), "Concurrent Error Detection Using
    Watchdog Processors — A Survey," IEEE Trans. Computers 37(2):160-174 — checker independence
    as the design requirement [cited by 15b; NOT independently verified]. Cemri M. et al. (2025),
    "Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657 / NeurIPS 2025 D&B — MAST taxonomy,
    "Unaware of Termination Conditions" at 12.4% of observed failures, kappa=0.88; closest
    available base rate for C2A2's own system class [cited by BOTH directions; NOT independently
    verified]. Dijkstra & Scholten (1980), Info. Proc. Letters 11(1) — termination detection is
    solvable but only by an explicit protocol layered over the computation, which is 15a's own
    concession that start-implies-report is not a free property of a scheduler.
  Challenges noted: 15a returned PARTIALLY-SUPPORTED (Weak) and its support was for
    CONSTRUCTIBILITY, not for the default — Erlang/OTP supervision and durable-execution engines
    demonstrate the invariant can be bought, never that it is free. That concession is folded in
    above rather than outweighed. 15b returned CHALLENGED (Strong).
  SYSTEMIC-RISK-FLAG CARRIED, AND ITS DISPOSITION IS THE MATERIAL FINDING: 15b filed a Critical
    flag across PRESUMPTION-664/666/668/669 recommending a single invariant — "no health claim
    may be derived from an artifact produced by the subject of the claim." That invariant is NOT
    minted here, because it is already PREMISE-096 ("No self-produced artifact may certify
    itself," ACTIVE) in substance, and PREMISE-110 supplies its monitoring-layer form. The flag
    therefore records an ENFORCEMENT gap, not a knowledge gap: the invariant was validated,
    remains ACTIVE, and the monitoring layer violates it in four places on one day. Minting it a
    second time is barred by PREMISE-138 clause (1) — in-channel repetition with no effector is
    not a remedy — and by PREMISE-135 (terminality is not purchased by accumulating instances).
    The flag is discharged per PREMISE-138 clause (2) by naming the actor with the effector: the
    watchdog's relocation out of the failure domain and the third terminal state are code
    changes, filed for Tom's review alongside REVISE-278..282 in this batch.
  Cross-direction source overlap (PREMISE-120 disclosure): Cemri et al. 2025 (MAST) and the
    arXiv:2606.14589 production-runtime study were cited by BOTH directions. Neither clause above
    rests on them — clause (1) rests on Cristian, clause (2) on the item's own directly-read
    transcripts.
  Scope limit, load-bearing: THE CAUSE OF `[Request interrupted by user]` IS UNDETERMINED and
    15b's steelman on this point is NOT defeated. This premise licenses no claim that the
    interruptions were faults rather than deliberate human stops. Both clauses hold either way —
    a human-initiated stop still leaves no verdict record, and still stops four runs at once —
    but any downstream use of this premise to assert an unattended failure mode exceeds it.
  Consistency check performed before INCORPORATE: checked against PREMISE-096 (self-certification
    — 141 does not restate it; see flag note above), PREMISE-100 (liveness is not correctness —
    141 is the terminal-state complement, no conflict), PREMISE-110 (common-mode monitor/subject
    independence — 141 is an explicit scope extension, adding the arithmetic clause 110 does not
    contain), PREMISE-086 (dead-man's-switch alarming on AGE, and its monitor-of-monitor
    condition — 141 records 086 as unenforced rather than contradicting it), PREMISE-089
    (freshness is per-source), PREMISE-045 (an unverifiable acknowledgement is not authoritative).
    No contradiction found with any ACTIVE premise.
  Confidence: High
  Applicable to: every scheduled agent session and its terminal-state record; the scheduler
    watchdog's placement; the daily health report's run-outcome section; PREMISE-086's alarm
    implementation; any reliability, streak or coverage figure computed over runs; the redundancy
    argument in PREMISE-142.
  Re-check due: 2026-09-05 (Monthly)
  Status: ACTIVE
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Original item: PRESUMPTION-664
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from four transcripts read directly, all terminating at `[Request interrupted
        by user]` with no verdict, one of which was the watchdog built to detect that class
      15a: Searched for supporting literature; PARTIALLY-SUPPORTED (Weak — constructibility only)
      15b: Searched for challenging literature; CHALLENGED (Strong) + SYSTEMIC-RISK-FLAG (Critical)
      15c: Net evaluation and disposition; INCORPORATE the negation as a scope extension of
        PREMISE-110, with the systemic flag routed to PREMISE-096 as an enforcement gap rather
        than re-minted, and the interrupt-cause question excluded
    Current status: INCORPORATED
    Disposition record: DISPOSITION-601 (2026-08-05)

PREMISE-142:
  Date validated: 2026-08-05
  Source item: PRESUMPTION-666
  Statement: AN INSTRUMENT WITH NO OUTCOME CHANNEL IS NOT A SECOND READING; IT IS A RESTATEMENT
    OF INTENT, AND IT IS NOT A PARTY TO ANY DISAGREEMENT. Three clauses. (1) A status report is a
    two-stage inference — ascertain the true state, then report it — and the first stage is the
    one that fails silently (Snow & Keil). An aggregator that derives run outcomes from the
    SCHEDULE has no first stage at all, so its output carries no evidential content about
    outcomes, and "No failures to report" is the schedule restated, not a finding. (2) THEREFORE
    THE OUTPUT VOCABULARY MUST BE THREE-VALUED: SUCCEEDED / FAILED / NO-EVIDENCE, and every
    status claim must carry an evidence pointer (which artifact, which timestamp). A binary
    vocabulary forces the aggregator to render an absence as a positive assurance, which is what
    it did — it named a specific run successful that had terminated with no output, and a false
    particular is harder to unwind than a silence. (3) BOUNDARY AGAINST PREMISE-114, load-bearing
    and stated because the naive reading conflicts: PREMISE-114 holds that where two instruments
    of one system disagree and neither is externally calibrated, no arbitration rule can name a
    winner. THIS PREMISE DOES NOT CREATE SUCH A RULE. The 2026-08-05 case is not two readings in
    disagreement — the commit-record instrument measured an artifact and the schedule-derived
    aggregator measured nothing, so there was one reading and one restatement. PREMISE-114
    governs disagreement between instruments that both measure; 142 governs admission to that
    set. Where two instruments that BOTH measure disagree, 114 still binds and 142 supplies no
    tiebreak.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Snow A.P. & Keil M. (2002), "A Framework for Assessing the Reliability of
    Software Project Status Reports," Engineering Management Journal 14(2) — the error/bias
    decomposition and the two-stage-inference structure [cited by 15b; NOT independently verified
    this run]. Skitka L.J., Mosier K.L. & Burdick M. (1999/2000), IJHCS 51(5) and 52(4) — errors
    of omission; training reduces commission but NOT omission errors; participants WITHOUT an
    automated aid outperformed those with a highly-but-imperfectly-reliable one [cited by 15b;
    NOT independently verified]. Beyer B. et al. (2016), Site Reliability Engineering Ch. 6 —
    page on symptoms, not on a component's self-description. Parasuraman R. & Manzey D.H. (2010),
    Human Factors 52(3):381-410 — complacency is GREATEST for aids of high and constant
    reliability; cited by 15a and supporting the failure rather than the premise, which 15a
    reported against its own direction and which is recorded here for that reason.
  Challenges noted: 15a returned PARTIALLY-SUPPORTED (Weak). Its support was for the FORM —
    exception-based reporting from a model (Simons' diagnostic control; Conant & Ashby) is a
    validated control pattern — under a condition C2A2 fails: the model must correspond to actual
    behaviour, and a schedule is a model of intended execution, not of execution. 15a found NO
    source supporting inference of an outcome from a schedule absent an outcome channel. 15b
    returned CHALLENGED (Strong). 15b's steelman — that the architecture worked as designed,
    with a fast shallow instrument and a slow deep one, and the deep one won — is PARTIALLY
    SUSTAINED and materially narrows this premise: defence in depth is legitimate and the
    redundancy is worth keeping. What it does not license is the shallow instrument publishing
    its output in the same vocabulary and with the same authority as the deep one. Clause (2) is
    the minimum change that preserves the redundancy while removing the false particular.
  Redundancy caveat, carried from PREMISE-141: the two instruments share a scheduler and a
    failure domain, so per PREMISE-110 and PREMISE-141 clause (2) they are not two chances. The
    2026-08-05 catch is not evidence that the redundancy is reliable.
  Cross-direction source overlap (PREMISE-120 disclosure): Keil et al. 2014 (JAIS 15(12)), the
    ~60% status-report bias figure, Huang et al. 2017 (gray failure) and Cemri et al. 2025 were
    cited by BOTH directions. No clause rests on the bias figure, which both directions flagged
    as sourced from a secondary summary and UNVERIFIED at primary level; clause (1) rests on the
    error half of Snow & Keil, which is the half that transfers to an automated reporter.
  Local instance VERIFIED by construction, not inferred: two health instruments read the same
    morning and returned opposite verdicts on the same transcript, and the one that measured an
    artifact was right. This is a controlled experiment C2A2 ran on itself at no cost, and it is
    why this item does not need the human-reporter literature to carry it.
  Consistency check performed before INCORPORATE: checked against PREMISE-114 (incommensurable
    instruments — potential conflict IDENTIFIED and resolved by clause (3) above rather than
    averaged), PREMISE-045 (unverifiable acknowledgement is not authoritative — 142 extends it
    from self-report to third-party status aggregation), PREMISE-096, PREMISE-100, PREMISE-109
    (a summarizing agent is a view over its own read set), PREMISE-110 (stuck-at-nominal),
    PREMISE-006 and PREMISE-012 (surface gaps as gaps rather than silently reconcile — 142 is the
    status-vocabulary form of the same commitment), PREMISE-141. No contradiction found with any
    ACTIVE premise once clause (3) is stated.
  Confidence: High
  Applicable to: the daily fleet/health status aggregator and every artifact that consumes its
    output; the run-verified counts in the daily report; any agent asserting the state of another
    agent; the 14a/14b/15a/15b/15c/15d run footers; streak and autonomy metrics that consume a
    green status line (interlocks with PREMISE-140).
  Re-check due: 2026-09-05 (Monthly)
  Status: ACTIVE
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Original item: PRESUMPTION-666
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by reading two same-morning health reports against the transcript both
        describe; the two disagree and the commit-derived one is correct
      15a: Searched for supporting literature; PARTIALLY-SUPPORTED (Weak — form only)
      15b: Searched for challenging literature; CHALLENGED (Strong) + SYSTEMIC-RISK-FLAG (Critical)
      15c: Net evaluation and disposition; INCORPORATE the negation with 15b's steelman folded in
        as a narrowing (keep the redundancy, change the vocabulary) and an explicit PREMISE-114
        boundary clause rather than an arbitration rule
    Current status: INCORPORATED
    Disposition record: DISPOSITION-602 (2026-08-05)

PREMISE-143:
  Date validated: 2026-08-05
  Source item: PRESUMPTION-668
  Statement: A RETRACTION COUNT IS A MEASURE OF THE PRODUCING LAYER, NOT OF THE CATCHING LAYER,
    AND CORRECTING AN OUTPUT DOES NOT TERMINATE THE ERROR EVEN FOR THAT OUTPUT. Three clauses,
    none of which restates PREMISE-118. (1) METRIC INVERSION, the new content: reliable catching
    of small failures ACTIVELY SUPPRESSES systemic repair, because each successful catch removes
    the pressure that would have justified changing the instrument — Tucker & Edmondson's
    "illusory equilibrium," in which first-order problem solving dominates, the organisation
    looks healthy and its effectiveness erodes. Three retractions in one day from three
    independent runs is therefore NOT a rigour signal; read correctly it is a rate measurement on
    an error-GENERATING layer that the catching layer is currently keeping up with, which is a
    condition with no margin. A metric that rises when the system worsens and is read as
    reassurance is the worst property a metric can have; this is the same polarity defect
    PREMISE-110 identifies in detectors, relocated to a count. (2) THE CORRECTION IS NOT SAFE:
    14.8-24.4% of sampled post-release fixes in four operating systems were themselves incorrect
    and reached users (Yin et al. 2011). A correction issued and unreviewed carries a
    one-in-five-to-one-in-seven prior of being wrong, so "corrected" is not a terminal state even
    for the single instance, and corrections must face the same review as originals. (3) THE
    RECORD MUST SPLIT: every retraction produces TWO items with independent lifecycles — a
    corrected-output record, and an instrument-defect record that OUTLIVES the run that filed it
    and is NOT CLOSABLE BY THAT RUN. This is the operational form of PREMISE-118's obligation,
    and the finding is that 118 is unmet: the false-positive sweep observed on 2026-07-31 and
    again on 2026-08-04 is an out-of-tolerance instrument that has had no retrospective impact
    assessment over its prior accepted outputs, which 118 requires.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Tucker A.L. & Edmondson A.C. (2003), "Why Hospitals Don't Learn from
    Failures," California Management Review 45(2):55-72 — first-order vs second-order problem
    solving, the illusory-equilibrium dynamic; the companion 2002 studies report 93% of responses
    to observed system failures were first-order [cited by BOTH directions; NOT independently
    verified this run]. Yin Z. et al. (2011), "How Do Fixes Become Bugs?" ESEC/FSE '11 —
    14.8-24.4% incorrect-fix rate [cited by 15b; NOT independently verified]. Dillon R.L. &
    Tinsley C.H. (2008), Management Science 54(8):1425-1440, and Tinsley, Dillon & Cronin (2012),
    Management Science 58(9) — recovered failures are encoded as successes; perceived risk falls
    while statistical risk is unchanged; the attenuation is prevented only by framing the CHANCE
    element in the recovery [cited by BOTH directions].
  Challenges noted: 15a returned PARTIALLY-SUPPORTED (Weak) and its result is unusual and is
    recorded as such: 15a's own on-point search target (Dillon & Tinsley) came back AGAINST the
    item's optimistic reading, and 15a reported it in full rather than dropping it. 15a found
    genuine support only for the value of the catching CAPABILITY (van Dyck et al. 2005, a
    two-country replication tying error-management culture to firm performance), and every source
    that decomposes the process places detection at the front of a longer chain — Phimister's
    seven stages, ISO 9001:2015 cl. 10.2's split between a CORRECTION (fix the output) and a
    CORRECTIVE ACTION (fix the cause, and verify effectiveness). 15b returned CHALLENGED (Strong).
  15b's steelman, PARTIALLY SUSTAINED and narrowing this premise: C2A2's runs patched AND
    announced, which is more than Tucker & Edmondson's nurses did and is what made the
    07-31/08-04 pair visible to 14b at all. Public self-retraction is therefore a genuine asset
    and this premise must not be cited to discourage it. What is forbidden is reading the count
    as a quality signal, and closing the defect in the run that filed it. A further steelman
    point is NOT resolved and is recorded: where the producing instrument is an LLM-based method
    with a stochastic failure mode, there may be no "fix" to apply, only a detection layer — in
    which case clause (3)'s instrument-defect record should terminate in a measured
    false-positive rate and a quarantine decision rather than in a code change.
  Domain-transfer caveat, load-bearing: all supporting sources concern human organisations and
    physical-process safety, where the instrument is a person or a procedure and repair means
    retraining or redesign. The near-miss risk-attenuation mechanism in particular is a human
    cognitive finding whose transfer to stateless agent runs is ANALOGICAL and is contested by
    15b's own steelman. Clause (1) is therefore carried primarily by the local record — the same
    sweep recurring four days after a disclosed catch — and by the structural argument, not by
    the cognitive mechanism.
  Cross-direction source overlap (PREMISE-120 disclosure): Tucker & Edmondson 2003, Dillon &
    Tinsley 2008 and Tinsley et al. 2012 were cited by BOTH directions, which is unusually heavy
    overlap and is a caution about independence rather than corroboration. The clause with a
    disjoint source is (2), which appeared in the AGAINST direction only; clause (3)'s standard
    (ISO 10.2) appeared in the FOR direction only.
  Consistency check performed before INCORPORATE: checked against PREMISE-118 (naming a defect
    does not license continued use; contain/assess/fix/verify with retrospective impact
    assessment — 143 is its operational form and records 118 as UNMET for the twice-failing
    sweep, no contradiction), PREMISE-130 (recurrence reclassifies at the third distinct
    signature — the sweep is at two occurrences of ONE signature and therefore has NOT yet met
    130's threshold; 143 does not lower it), PREMISE-116 (a finding does not change the behaviour
    it describes), PREMISE-113 (a detector's findings are evidence about the detector until its
    precision is measured — directly applicable to the false-positive sweep), PREMISE-137,
    PREMISE-139, PREMISE-102, PREMISE-138. No contradiction found with any ACTIVE premise.
  Confidence: Moderate — clause (2) is High (direct measurement in the software domain); clauses
    (1) and (3) rest on an analogical transfer that 15b's own steelman contests, plus a two-point
    local series.
  Applicable to: every self-retraction filed by any agent; the retraction and "errors caught"
    counts wherever they appear in run footers or health reports; the twice-failing false-positive
    sweep and its prior accepted outputs; PREMISE-118's outstanding retrospective-assessment
    obligation; the correction records issued on 2026-08-04, none of which was reviewed.
  Re-check due: 2026-09-05 (Monthly)
  Status: ACTIVE
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Original item: PRESUMPTION-668
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three same-day retractions read together, one of which is the second
        observed occurrence of the same false-positive sweep
      15a: Searched for supporting literature; PARTIALLY-SUPPORTED (Weak; own target returned against)
      15b: Searched for challenging literature; CHALLENGED (Strong) + SYSTEMIC-RISK-FLAG (Critical)
      15c: Net evaluation and disposition; INCORPORATE the negation at Moderate confidence with
        the domain-transfer caveat and 15b's stochastic-instrument steelman made load-bearing,
        and with PREMISE-130's threshold explicitly NOT lowered
    Current status: INCORPORATED
    Disposition record: DISPOSITION-603 (2026-08-05)

PREMISE-144:
  Date validated: 2026-08-06
  Source item: PRESUMPTION-678
  Statement: AN AGENT CHARTER IS NOT EXEMPT FROM THE PREMISE REGISTER; IT IS SUBORDINATE TO IT,
    AND A SELF-EXEMPTING GOVERNING LAYER PRODUCES A FAILURE CLASS DETECTABLE ONLY FROM OUTSIDE.
    Five clauses. (1) SUBORDINATION, NOT EXEMPTION: in hierarchical norm systems a lower-level
    rule that contradicts a higher-level rule is invalid to the extent of the contradiction. Hart's
    primary/secondary distinction grants the real and only concession available — a charter is a
    DIFFERENT KIND of rule from a premise — but it does not yield exemption from consistency, and
    Hart's own rule of recognition is validated by the practice of officials, i.e. FROM OUTSIDE,
    which is exactly how the 14b contradiction was found. (2) THE FAILURE HAS A SIGNATURE AND 14b'S
    ~118 DAYS IS IT: internal confirmation, external falsification, latency a function of luck
    rather than of design. The professional standards nearest the case were written to bound
    precisely this. The IIA's Global Internal Audit Standards require a full-scope EXTERNAL quality
    assessment by a qualified assessor from outside the organisation at least every five years, and
    hold that pure self-assessment lacks sufficient independence — a self-assessment counts only
    when a named independent validator signs it. INTOSAI GUID 1900 subjects Supreme Audit
    Institutions, the bodies with the strongest independence claim in any state, to legislative
    oversight and structured peer review. No located source treats apex independence as grounds for
    exemption: independence is a reason to design a DIFFERENT review channel, never to remove one.
    (3) THE EXEMPTION IS NOT TECHNICALLY FORCED: normative-conflict detection over a rule set is
    mechanisable. The conflict patterns are characterised (obligation vs prohibition, prohibition vs
    permission, obligations on conflicting actions over the same action) and formalised normative
    systems can be checked by automated provers. Nothing in the formalism admits a norm that is
    ENROLLED in the system but EXCLUDED from the check; such a norm is not exempt, it is
    undetectable. The exemption is therefore a design omission, not a necessity. (4) IF AN EXEMPTION
    IS KEPT IT MUST BE A FIRST-CLASS, EXPIRING OBJECT — 15b's steelman folded in as a narrowing
    rather than outweighed, because the regress it names is real: if every charter enters the
    register, the register's own admission rules become a charter, and inspector-general, ombudsman
    and grand-jury functions are routinely granted procedural exemptions the bodies they investigate
    do not have. The literature's answer is that the regress terminates in an INSTITUTIONAL DEVICE
    (a scrutiny board, a legislature, a peer network, a dead man's switch), never in a declaration
    that the top layer is self-validating. Therefore: an exemption must be explicit, recorded IN the
    register, attached to a named validator, bounded by a stated period, and carry an expiry — or it
    is not an exemption, it is a blind spot. (5) REPRESENTATION CAVEAT, LOAD-BEARING: the conflict
    formalisms assume all norms share a common representation. C2A2 charters are prose and premises
    are register entries, so a charter/premise conflict may be genuinely UNDETECTABLE rather than
    merely unchecked. No cited source solves that. Until a common predicate form exists, the check
    is a read by an agent that did not author the charter, not a prover, and must be scheduled as
    such.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the system was unaware it
    held its own governing documents outside the register that governs everything else)
  Supporting evidence: Institute of Internal Auditors, Global Internal Audit Standards — external
    quality assessment requirement and the independently-validated-self-assessment pattern [cited by
    BOTH directions]. INTOSAI GUID 1900 Peer Review Guidelines and the World Bank governance note
    "External Oversight of Supreme Audit Institutions: Who Audits the Auditor?" [15a]. "Detection
    and Resolution of Normative Conflicts in Multi-agent Systems," AAMAS 2018 — proceedings PDF
    confirmed at ifaamas.org by 15b [author list UNVERIFIED in BOTH directions; confirm before
    onward citation]; with deontic-logic compliance checking (arXiv:1411.4823; J. Logic and
    Computation 35(8), exaf054) [15b]. Sarbanes-Oxley 2002 and the creation of the PCAOB, with
    IOSCO's auditor-independence principles — the audit profession's era of self-regulation ended
    because the self-exempting arrangement failed, and commentary records that PCAOB's own "interim"
    independence standards were inherited from that era and never modernised, i.e. the exempt layer
    survived the reform meant to close it [15b]. Congressional Accountability Act of 1995 (PL 104-1)
    and its residual exemptions [cited by BOTH directions]. Hart, H.L.A. (1961), The Concept of Law
    [UNVERIFIED — secondary summaries only]. Meta-regulation: Grabosky (ANU Press); Baldwin, Cave &
    Lodge, Understanding Regulation [15a].
  Challenges noted: 15b returned CHALLENGED (Strong) in the SAME direction as this premise, from
    four independent framings. 15a returned NO-SUPPORT-FOUND (None) and raised NO novelty flag,
    reporting that the governance literature covers the claim thoroughly and denies it. The nearest
    thing to a genuine counter is Kelsen's Grundnorm, which 15b searched and reported honestly: a
    hierarchy's top norm is PRESUPPOSED rather than validated, which is closer to a steelman than to
    a challenge. It is recorded here as an unresolved theoretical residue and is answered, not
    dismissed, by clause (4)'s requirement that the presupposed layer be small, named, bounded and
    readable end-to-end rather than merely presupposed.
  SCOPE ESCALATION EXPLICITLY NOT INCORPORATED: 15a flagged that its evidence base concerns single
    named charters and that no located source addresses whether the exemption generalises across a
    CLASS of agent charters — which is what 14b asserted. The class-level claim is therefore carried
    by the structural argument and by the local record (one measured instance, ~118 days), NOT by
    the literature. The enumeration below is what would settle it, and it was not run this session.
  Cross-direction source overlap (PREMISE-120 disclosure): the IIA external-quality-assessment
    requirement, the Congressional Accountability Act and the AAMAS 2018 paper were cited by BOTH
    directions. Per PREMISE-111 that agreement carries residual correlation and is not two
    independent confirmations. The disjoint material is 15a's normative-hierarchy and Hart line, and
    15b's SOX/PCAOB and meta-monitoring line.
  Consistency check performed before INCORPORATE: PREMISE-110 (absence-of-complaint is an unsafe
    polarity; COMMON-MODE SCOPE GUARD — a checker sharing runtime, scheduler, credentials and
    filesystem with its subject is a single channel wearing two labels — this is the independence
    condition clause (4) requires and 144 is its normative counterpart for rules rather than
    monitors); PREMISE-124 (self-measurement of the pipeline's own completeness must cite an
    external baseline or be reported UNCALIBRATED — same structure, different object); PREMISE-086
    (absence/staleness is the signal; alarm on AGE); PREMISE-100 (a check that cannot execute
    reports as passing); PREMISE-116 (a finding does not change the behaviour it describes);
    PREMISE-139; PREMISE-102; PREMISE-138. No contradiction found with any ACTIVE premise. NOTE,
    load-bearing: the six ACTIVE premises that REVISE-282 records as contradicted by 14b's line 88
    — PREMISE-003, 070, 095, 106, 119, 121 — are all CONFIRMED by this premise and none is amended.
    PREMISE-144 is the general rule of which that contradiction is the first measured instance.
  Confidence: Moderate. The normative claims in clauses (1)-(3) are individually well sourced and
    would carry High on their own; overall confidence is held at Moderate for two reasons stated
    rather than smoothed — the class-level generalisation is unsourced (see above), and the audit
    standards assume a board or audit committee to report to, so the transfer specifies a
    requirement WITHOUT specifying who in C2A2 discharges it. That gap is the subject of REVISE-283.
  Applicable to: every file in wiki/agents/; the charter-loading step of every scheduled agent;
    14b_presumption_detector_agent.md line 88 specifically (REVISE-282); 15c_net_evaluator_agent.md
    — this agent's own charter, which is equally in scope, has equally never been checked against
    the register, and is not exempted by having written this entry; any exemption claimed by any
    agent in future.
  OPEN MEASUREMENT NAMED AT VALIDATION (in-house, requires no authorisation, and OWED): extract
    every agent charter and every ACTIVE premise and report (i) how many charters have no register
    entry at all; (ii) how many charter/premise pairs conflict under the four conflict patterns;
    (iii) for each conflict already known, elapsed days between charter authorship and detection,
    and whether detection was internal or external. If (i) is large and every entry in (iii) is
    "external," the class claim is confirmed in-system and clause (5)'s representation problem
    becomes the next question. NOT RUN this session.
  Re-check due: 2026-09-06 (Monthly)
  Status: ACTIVE
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Original item: PRESUMPTION-678
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Generalised the lit pipeline's line-88 finding from one charter to the class of charters
      15a: Searched for supporting literature; NO-SUPPORT-FOUND (None); no novelty flag
      15b: Searched for challenging literature; CHALLENGED (Strong) + SYSTEMIC-RISK-FLAG (Critical)
      15c: Net evaluation and disposition; INCORPORATE THE NEGATION with 15b's regress steelman
        folded in as clause (4) (bound and record the exemption rather than deny the regress), the
        representation problem made load-bearing as clause (5), and the class-level generalisation
        explicitly NOT carried by the literature
    Current status: INCORPORATED
    Disposition record: DISPOSITION-609 (2026-08-06)

PREMISE-145:
  Date validated: 2026-08-06
  Source item: PRESUMPTION-685
  Statement: DEFERENCE TO AN INCUMBENT PUBLISHED FIGURE IS NOT THE CONSERVATIVE MOVE, AND
    WITHHOLDING A DISCREPANT OWN-MEASUREMENT IS A REPORTING BIAS, NOT A NULL ACT. Five clauses.
    (1) THE MEASURED DIRECTION IS THE OPPOSITE OF THE PRESUMPTION. Henrion & Fischhoff (1986) found
    reported uncertainties on the fundamental constants consistently biased toward UNDERESTIMATING
    actual error, and documented a bandwagon effect: the speed of light overestimated by roughly
    70 km/s across 1876-1902, then underestimated by roughly 15 km/s across 1905-1950 — long runs of
    mutually consistent, confidently reported, wrong values, each individual run behaving exactly as
    a deference rule prescribes. Jeng (2006, 2007) reproduces the effect on a larger corpus:
    particle properties trend and cluster as a function of PUBLICATION YEAR, and Particle Data Group
    measurements distribute around PREVIOUS AVERAGES with chi-squared about half that associated
    with distribution around the currently accepted value. Deference produces slow, monotone,
    self-concealing drift with artificially tight error bars — the opposite of conservatism.
    (2) THE SPECIFIC ASYMMETRY HAS A NAME AND IS THE COMMONEST BIAS IN THE FIELD THAT MEASURED IT.
    Klein & Roodman (2005) list "consistency with previous measurements" among the biasing
    preconceptions and identify STOPPING BIAS — continuing to hunt for mistakes or to improve the
    analysis until the result agrees with expectation — as probably the most common bias in particle
    physics. A run that scrutinises its own instrument only AFTER discovering disagreement, finds a
    candidate fault, and stops scrutinising, has performed exactly that. Blind analysis exists to
    forbid the comparison such a rule requires: it prohibits the SEARCH for defects conditioned on
    the answer, while permitting unblinding-and-fixing when a genuine defect is found.
    (3) SUPPRESSION IS NOT A NULL EVENT. Withholding a measured result for a reason correlated with
    its VALUE is selective outcome non-reporting, treated in the evidence-synthesis literature as a
    risk-of-bias domain in its own right. The suppressed 57 is a datum removed from the record on
    value-correlated grounds, not an absence of data.
    (4) THE ADMISSIBLE MOVE — the narrowing that 15a's genuine partial support licenses, stated
    exactly and no wider. A DOCUMENTED, INDEPENDENTLY-ESTABLISHED defect in the producing instrument
    IS a recognised warrant for setting that instrument's output aside: the GUM treats blunders as a
    distinct category from random variation and holds that large ones are identifiable by proper
    review, and the retraction record for analysis-code defects shows the discipline's norm is
    withdrawal rather than caveated publication (the most dangerous class being semantic bugs that
    return a plausible wrong number rather than an error). But that warrant is (a) CONDITIONED ON
    DOCUMENTED CAUSE, (b) SYMMETRIC — it says nothing whatever about which figure should stand in
    the interim, and (c) NON-TRANSFERABLE to the incumbent, whose confidence must NOT rise because a
    challenge was withheld. Converting "my instrument is suspect" into "therefore the older figure
    stands" imports an asymmetry no located source licenses and makes durability a function of
    elapsed unchallenged time. The worked alternative is the PDG's: retain both central values and
    inflate the stated uncertainty by a scale factor so the reader is warned by the size of the
    factor and can redo the average with a different choice of data.
    (5) THE MINIMUM RECORD, and the cheapest clause to implement: if a figure is withheld, log its
    VALUE, the stated reason, and the TIMESTAMP AT WHICH THE REASON WAS IDENTIFIED RELATIVE TO THE
    DISAGREEMENT. Timestamp order is what makes stopping bias auditable. Without it the trail cannot
    distinguish "no one re-measured" from "re-measurements disagreed and were withheld," which is
    the single most important distinction for later reconstruction, and a run that finds 57 today
    and defers, then finds 55 next week and defers again, has manufactured a false record of
    stability.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Henrion, M. & Fischhoff, B. (1986), "Assessing uncertainty in physical
    constants," American Journal of Physics 54(9):791-798 [journal, volume, pages and year confirmed
    by 15b; cited by BOTH directions]. Klein, J.R. & Roodman, A. (2005), "Blind Analysis in Nuclear
    and Particle Physics," Annual Review of Nuclear and Particle Science 55:141- , DOI
    10.1146/annurev.nucl.55.090704.151521 [UNVERIFIED by 15a, DOI confirmed by 15b]. Jeng, M.
    (2007), Nucl. Instr. Meth. A 571:704-708, and (2006) Am. J. Phys. 74(7):578 [the 2006 item's
    author is UNVERIFIED in the AGAINST direction]. Particle Data Group, Review of Particle Physics,
    treatment of discrepant data and the scale factor S = sqrt(chi2/ndf) [15b]. JCGM 100:2008 (GUM),
    treatment of blunders [15a]. Selective-outcome-reporting literature: PMC4240443, PMC4938957,
    AHRQ/NCBI NBK100617 [15b; the 13%-of-8434-studies figure is provisional — the source article was
    not opened]. Chang et al. (2006) five retractions traced to a homemade data-analysis program,
    reported in Miller, G. (2006), Science 314 [15a; retraction notices not fetched].
  Challenges noted: this premise IS the challenge direction. 15b returned CHALLENGED (Strong); 15a
    returned PARTIALLY-SUPPORTED but at strength WEAK, and reported that the measurement literature
    "was written largely to refute" the presumption. The support 15a did find is not discarded — it
    is clause (4), which is the only part of the original presumption that survives.
  THE QUESTION NEITHER DIRECTION COULD SETTLE, recorded because it is decisive for the INSTANCE
    though not for the premise: whether the prior day's 24 was produced by a code path sharing the
    parser defect. If it was, the defect invalidates BOTH figures and neither should stand — the
    deference is then not conservative but arbitrary. If it demonstrably was not, the deference is
    defensible under clause (4) and this premise's criticism of the instance weakens substantially.
    Nothing in the located literature adjudicates it and neither search file could.
  Scope limit, load-bearing: the metrology evidence concerns quantities with a TRUE VALUE and
    repeated INDEPENDENT measurement. A parser count over a changing corpus may have no stable
    target, which weakens the bandwagon analogy directly — though it also removes the main
    justification for treating an older figure as better established, so the scope limit cuts the
    presumption as well as the premise. C2A2 also has no analogue of the PDG's community of
    independent measurers; with a single instrument, "retain both and inflate uncertainty" may
    publish noise twice, which is why clause (5) (record the suppression) is stated as the minimum
    rather than clause (4)'s scale-factor pattern being stated as the requirement.
  Consistency check performed before INCORPORATE: PREMISE-113 (a detector's findings are evidence
    about the DETECTOR until its precision is measured) — CONFIRMING and load-bearing: 113 entails
    that the 57 is evidence about the parser, and equally that the 24 is, which is precisely the
    symmetric conclusion clause (4)(b) reaches; 113 does not license the deference. PREMISE-114
    (absent external calibration no arbitration rule can name a winner; THE EXIT — where the
    quantity is deterministic over a frozen snapshot the disagreement is DEFINITIONAL, so write the
    counting definition, designate it the reference and re-derive both readings) — this supplies the
    cheap terminating procedure for the instance and is compatible in full. PREMISE-101 (a count is
    a property of a (scope, method, time) reading, not of the artifact). PREMISE-124 (no
    self-measurement of own accuracy without an external baseline or an UNCALIBRATED tag).
    PREMISE-103; PREMISE-143 clause (2) (a correction is not a terminal state). No contradiction
    found with any ACTIVE premise.
  Confidence: Moderate. Clauses (1)-(3) are individually High in their home domain; the transfer to
    a single-instrument count over a changing corpus is by analogy on RATE though clean on
    MECHANISM, and clause (4)'s applicability to the instance turns on an unresolved fact.
  Applicable to: the withheld 57 and the standing 24; every figure a run quotes from a prior day's
    record; any run citing an instrument fault as grounds for deferring to a prior figure; run
    footers, health reports and daily counts generally; interacts with PREMISE-143's retraction and
    correction records.
  OPEN MEASUREMENT NAMED AT VALIDATION (in-house, requires no authorisation, and terminating):
    (i) re-run the FIXED parser over the historical inputs that produced 24 and report which figure
    it returns — if 57, the deference rule cost the record latency on a correct value; (ii) symmetry
    audit — over all historical revisions, how many moved AWAY from the incumbent versus TOWARD it,
    and were upward and downward disagreements suppressed at equal rates? Asymmetric suppression is
    the bandwagon signature; (iii) for every instance where a run withheld its own figure citing an
    instrument fault, check whether the fault was documented BEFORE or AFTER the disagreement was
    observed. NOT RUN this session.
  Re-check due: 2026-09-06 (Monthly)
  Status: ACTIVE
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Original item: PRESUMPTION-685
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read a stated deference rule against the same run's opposite use of the same register
      15a: Searched for supporting literature; PARTIALLY-SUPPORTED (Weak — documented-cause zone only)
      15b: Searched for challenging literature; CHALLENGED (Strong)
      15c: Net evaluation and disposition; INCORPORATE THE NEGATION with 15a's documented-cause
        warrant preserved intact as clause (4) and explicitly made SYMMETRIC, and with the
        unresolved shared-code-path question recorded rather than assumed either way
    Current status: INCORPORATED
    Disposition record: DISPOSITION-610 (2026-08-06)

PREMISE-146:
  Date validated: 2026-08-06
  Source item: PRESUMPTION-689
  Statement: A TASK SPECIFICATION'S SATISFIABILITY IS A PROPERTY TO BE ESTABLISHED, NOT A DEFAULT;
    AND UNIVERSAL VIOLATION OF A RULE IS A DIAGNOSTIC READING ON THE RULE, NOT AN AGGREGATE READING
    ON THE ACTORS. Six clauses. (1) THE DEFAULT IS DENIED BY THE FIELD THAT WOULD HAVE TO HOLD IT.
    Goal-driven requirements engineering is organised around the premise that inconsistencies arise
    as goals are elicited and that resolving them is a NECESSARY CONDITION for successful
    development, so conflict must be discovered by formal and heuristic technique rather than
    assumed absent (van Lamsweerde, Darimont & Letier 1998). Its notion of DIVERGENCE — requirements
    jointly unsatisfiable only under some boundary condition — is exactly this item's shape: a
    preamble and a ceiling that conflict only once the preamble's actual size is measured. Boundary
    conditions of that kind are computed AUTOMATICALLY by satisfiability checking (ASE 2016), which
    is the mechanised form of what the eleventh run did by hand. The existence of the subfield is
    itself the evidence: if specifications could be presumed satisfiable, it would not exist.
    (2) THE CLOSEST QUANTIFIED ANALOGUE IS THE SAME FAILURE WITH THE SAME SHAPE. Fully complying
    with USPSTF preventive guidance plus chronic, acute and documentation work for a 2,500-patient
    panel requires 26.7 physician-hours per day (Porter, Boyd, Skandari & Laiteerapong, J Gen Intern
    Med, DOI 10.1007/s11606-022-07707-x, PMC9848034). The mandatory component alone exceeds the
    ceiling, so every practitioner is in permanent breach, and for years the shortfall was
    attributed to individual practitioners rather than to the specification. Two further findings
    transfer exactly: the shortfall was MEASURABLE IN ADVANCE by a single arithmetic pass over the
    mandatory list — nobody needed ten days of breach reports — and the repair was ARCHITECTURAL
    (team-based delegation cut the physician requirement to 9.3 h/day), not effort-based.
    (3) TEN ATTRIBUTIONS TO THE ACTOR AND ONE TO THE RULE IS THE DOCUMENTED PATHOLOGY, NOT
    DILIGENCE. Normalisation of deviance: in the absence of perceived loss, departure from a stated
    rule becomes culturally defined as normal, and frequent engagement in the deviant practice
    resets what counts as tolerable, from which further deviation proceeds. Hale & Borys (Safety
    Science 55, 2013) contrast the top-down rational paradigm — rules as static comprehensive
    limits, violation as negative behaviour to be suppressed — with the constructivist reading in
    which violation is evidence the rule does not fit the work, and place MONITORING AND ADAPTING
    THE RULES at the centre of their framework. The cross-industry synthesis adds that deviations
    are "virtually always a response to production pressures" and that the consequence is a system
    running permanently in a degraded mode.
    (4) THE SIGNAL DEGRADES FIRST, BEFORE ANYTHING ELSE BREAKS. Once every run breaches, "breached"
    stops discriminating a 2% overrun from a 200% one and the disclosure becomes ritual; a genuinely
    anomalous overrun is then invisible among the routine ones, which removes the system's ability
    to detect the failure the disclosure was built to detect. And the harm is not loud: the safety
    literature is emphatic that operators facing impossible rules do not fail loudly, they improvise
    quietly — so runs may already be truncating, skipping or reinterpreting mandatory elements in
    ways no disclosure records. That is the risk that compounds, because it makes the vault's record
    of what runs DID unreliable in an undocumented direction.
    (5) THE FIX IS AN ADMISSION GATE AND IT IS CHEAP. In systems where deadline feasibility matters,
    feasibility is tested AT ADMISSION and infeasible task sets are REJECTED rather than dispatched;
    the standard architecture is a cheap utilisation-based sufficient test that rejects obviously
    infeasible requests fast, refined by an exact test where it matters. Mandatory-floor-versus-
    ceiling IS a utilisation test: sum the fixed cost, compare to the budget, refuse to admit.
    (6) NARROWING, FROM THE STEELMAN, SUSTAINED IN PART. A ceiling that is routinely exceeded is not
    necessarily defective — it may be deliberately SOFT, since a hard always-satisfiable ceiling
    would be set so loosely as to exert no pressure, and the soft-real-time literature formalises
    exactly this as a tolerable deadline-miss ratio. But the defence carries obligations: the ceiling
    must be LABELLED soft with a stated tolerable breach ratio so that "breached" is not read as a
    fault report; the mandatory FLOOR must be published so every run knows its discretionary
    headroom before it starts; and breach must be reported RELATIVE TO THE FLOOR, not relative to
    zero. Where floor >= ceiling, no labelling saves it. And none of these is the binding failure
    here: the binding failure is that no channel existed by which a measurement of infeasibility
    could reach the specification. The register recorded ten breaches; nothing connected any of them
    to the ceiling.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: ten consecutive runs
    attributed a structural defect to themselves without the option of attributing it elsewhere
    being representable)
  Supporting evidence: Porter, J., Boyd, C., Skandari, M.R. & Laiteerapong, N., "Revisiting the Time
    Needed to Provide Adult Primary Care," J Gen Intern Med, DOI 10.1007/s11606-022-07707-x,
    PMC9848034 [authors, journal and DOI confirmed by 15b; year given variously 2022 online-first /
    2023 in issue]. van Lamsweerde, A., Darimont, R. & Letier, E. (1998), "Managing conflicts in
    goal-driven requirements engineering," IEEE TSE 24(11) [journal and year confirmed via secondary
    records; volume/issue from established knowledge]. Degiovanni, R., Alrajeh, D. et al. (2016),
    "Goal-Conflict Detection based on Temporal Satisfiability Checking," ASE 2016 [full author list
    not verified]. Vaughan, D. (1996), The Challenger Launch Decision [book citation UNVERIFIED in
    the AGAINST direction; concept and origin confirmed]. Hale, A. & Borys, D. (2013), "Working to
    rule or working safely?" Parts 1 and 2, Safety Science 55 [15a]. "A qualitative systematic review
    on the application of the normalization of deviance phenomenon within high-risk industries,"
    ScienceDirect S0022437522001827 [journal title inferred, not confirmed; cited by BOTH
    directions]. Real-time admission control and schedulability: "Utilization-Based Admission
    Control for Scalable Real-Time Communication," Real-Time Systems; QPA schedulability analysis
    (York) [cited by BOTH directions]. Work-as-imagined vs work-as-done / Safety-II, incl.
    PMC5862557 [primary Hollnagel texts NOT fetched in either direction — treat the framing as
    UNVERIFIED as to specific citation].
  Challenges noted: this premise IS the challenge direction — 15b CHALLENGED (Strong), 15a
    NO-SUPPORT-FOUND (None) with no novelty flag. The genuine boundary conditions are folded in
    rather than outweighed: clause (6) carries the soft-ceiling steelman and the ordering objection
    (one measurement of the preamble is a single measurement, and the earlier ten may have been
    correct that THEIR specific overruns were partly avoidable verbosity on top of a tight but not
    impossible base). 15a's cost defence is also recorded and scoped: for sufficiently expressive
    specification languages satisfiability checking is undecidable or intractable, so a working
    presumption of satisfiability is sometimes forced by cost — but that defence does not reach this
    case, where the conflict is ARITHMETIC (a fixed preamble against a fixed ceiling) and decidable
    by one measurement, which is why one run could settle it.
  Cross-direction source overlap (PREMISE-120 disclosure): Vaughan's normalisation of deviance, the
    high-risk-industries systematic review, work-as-imagined/work-as-done, and the real-time
    admission-control material were cited by BOTH directions — heavy overlap, and per PREMISE-111
    not independent corroboration. The disjoint material is 15b's primary-care time-budget analogue
    (the strongest single source on this item, AGAINST direction only) and 15a's requirements-
    engineering line (FOR direction only).
  Domain-transfer caveat: the safety literature concerns HUMAN operators with tacit local knowledge,
    and transfer to agent runs executing a written specification is by analogy; the normalisation-
    of-deviance material describes escalation toward catastrophic outcomes, which is not obviously
    this risk profile. Clause (3) is therefore carried by the structural argument and the ten-to-one
    local ratio, not by the catastrophe mechanism.
  Consistency check performed before INCORPORATE: PREMISE-115 (before an agent is called broken,
    check whether its specification ever instructed the behaviour; specification and design issues
    are the largest single MAS failure category at 41.8%, and 75.17% of failures emit no hard error
    signal) — DIRECTLY adjacent and compatible: 115 covers the MISSING instruction, 146 covers the
    PRESENT BUT INFEASIBLE instruction, and together they cover the specification-defect class; 115
    is confirmed, not amended. PREMISE-102 (fail-loud is an act of reporting, not of remediation;
    repeated identical non-processing converts a signal into a standing policy of non-coverage) —
    describes the ten disclosures exactly and is confirmed. PREMISE-138 clause (2) (a flag raised by
    a layer that cannot act must name the actor who can and leave the channel) — supplies what
    clause (6) says was missing. PREMISE-130 (recurrence reclassifies at the third distinct
    signature — NOT lowered by this premise; the ten disclosures are ten instances of ONE
    signature). PREMISE-116; PREMISE-124; PREMISE-053. No contradiction found with any ACTIVE
    premise.
  Confidence: Moderate. The mechanism transfers cleanly and the primary-care analogue is unusually
    close, but the strongest supporting bodies are human-operator safety science and practitioner
    real-time practice, and the local record is one measurement against ten.
  Applicable to: the mandatory preamble and the per-task budget ceiling; every budget-breach
    disclosure on record and every future one; the disclosure format itself, which currently has no
    ATTRIBUTION FIELD in which "specification" is a representable answer; admission of any scheduled
    task with a fixed mandatory cost; 14a/14b/15a/15b/15c/15d run footers.
  SELF-APPLICATION, recorded rather than omitted: runs in this very pipeline disclose per-task
    budget breaches — 15d's 2026-08-02 run exceeded the 4,000-token budget and disclosed it under
    FAIL-LOUD. Under this premise that disclosure is not by itself evidence about the run, and the
    floor/ceiling ratio below must be computed before any such disclosure is read as one.
  OPEN MEASUREMENT NAMED AT VALIDATION (in-house, requires no authorisation, and decisive):
    (i) compute the token/word cost of the mandatory preamble AS ACTUALLY DELIVERED to runs and
    report floor/ceiling as a ratio; (ii) classify every budget-breach disclosure on record as
    attributed to the run's own verbosity, to the specification, or unattributed; (iii) check
    whether ANY change to the ceiling or to the preamble followed ANY disclosure. Ratio >= 1.0 with
    class (i) dominating quantifies the misattribution; no change across all disclosures confirms
    there is no feedback channel and the disclosures are ritual in the normalisation sense. NOT RUN
    this session.
  Re-check due: 2026-09-06 (Monthly)
  Status: ACTIVE
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Original item: PRESUMPTION-689
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from one run inverting a claim ten prior runs made in the opposite direction
      15a: Searched for supporting literature; NO-SUPPORT-FOUND (None); no novelty flag
      15b: Searched for challenging literature; CHALLENGED (Strong); member of the SYSTEMIC-RISK-FLAG
      15c: Net evaluation and disposition; INCORPORATE THE NEGATION with the soft-ceiling steelman
        folded in as clause (6) with its three obligations attached, and the cost/undecidability
        defence scoped out on the ground that this conflict is arithmetic
    Current status: INCORPORATED
    Disposition record: DISPOSITION-611 (2026-08-06)

PREMISE-147:
  Date validated: 2026-08-06
  Source item: PRESUMPTION-691
  Statement: A QUEUE'S SIZE MEASURES DEMAND AND ACTIVITY, NOT PERFORMANCE; AN UNPAIRED PRODUCER-SIDE
    COUNT IS AN INVERTED HEALTH SIGNAL; AND THE STATISTIC THAT CARRIES THE INFORMATION IS AGE, NOT
    COUNT. This is the MEASUREMENT-LAYER premise and it is deliberately distinct from
    PRESUMPTION-677 / REVISE-282, which concerns the ARRIVAL RATE being treated as independent of
    consumption capacity. 677 is the variable; 147 is the instrument that keeps the variable
    invisible. Six clauses. (1) SAME SIZE, OPPOSITE STATES — the decisive clause. The best-documented
    institutional case establishes that there is NO SIMPLE RELATIONSHIP between the size of a
    waiting list and the distribution of waiting times: the NHS England elective list stood at four
    million on multiple occasions since 2007 with very different waits each time, and the 18-week
    target could in principle be met at any list size. The corollary drawn by the IFS and the Office
    for Statistics Regulation is the one that transfers: waiting lists measure DEMAND AND ACTIVITY,
    not performance, so movements do not necessarily reflect different levels of performance. A
    rising list is equally consistent with a healthy referral pipeline and with collapsed treatment
    capacity, and size alone cannot distinguish them. Queue growth therefore cannot bear the reading
    "the hunt is healthy" — not because that reading is too optimistic, but because the statistic
    does not carry the information either way. (2) THE ARITHMETIC RUNS THE OTHER WAY. Little's Law
    (Little 1961, Operations Research 9(3):383-387), applied as Lead Time = WIP / Throughput: with
    throughput constant, rising WIP means proportionally longer lead time and nothing else; with
    throughput at ZERO — 34 -> 40 with no decision in sixteen days — lead time is unbounded, and the
    growth conveys complete information about the review function and none about the hunt. Little's
    Law assumes a stable system and a system with zero service over sixteen days violates
    stationarity, so it is used here DIAGNOSTICALLY, not predictively. (3) THE PRODUCER-SIDE COUNT
    IS RIDGWAY'S CASE, and it is the oldest result here. Ridgway (1956), Administrative Science
    Quarterly 1(2):240-247: public employment interviewers evaluated on interviews CONDUCTED
    conducted fast interviews and placed very few applicants; investigators given a quota of eight
    cases per month selected easy fast cases. In both, the producer-side count rose while the
    outcome it proxied fell, precisely because such a count is structurally incapable of falling
    when the outcome degrades. (4) THE LOAD-BEARING CLAUSE IS THE SECOND HALF OF 14b'S OBSERVATION:
    NO METRIC FALLS. Where a proxy correlates imperfectly with the goal, the strong form of
    Goodhart's law holds that optimising it does not merely stop helping but becomes actively
    harmful once proxy and target decouple, and the condition under which this bites hardest is an
    UNOPPOSED proxy. Item GENERATION is cheap; item ADJUDICATION is expensive. A metric set with no
    counterweight to queue growth is a system with a free lever, and the counter-metric and
    guardrail literature is uniform on the remedy: every quantity or speed indicator must be PAIRED
    with a quality or value indicator (the DORA pairing of deployment frequency with change failure
    rate is the canonical form), and a dashboard should be a system of checks and balances rather
    than a single number. A register in which NO indicator falls when the queue rises is, by that
    standard, an unpaired metric. (5) COUNT IS THE WRONG STATISTIC IN BOTH DIRECTIONS — the steelman
    folded in as a narrowing, because it is right. Queue growth IS a real signal about the DETECTOR,
    and suppressing it to make a backlog look better is the classic error of throttling detection,
    which in safety reporting systems destroys the reporting culture outright; sixteen days is also
    a short window, and a queue that grows while a reviewer deliberates is not obviously worse than
    one that shrinks through hasty disposal. The correct response is therefore NOT "report less" but
    SEPARATE AND AGE: report find-rate and resolve-rate as two NAMED metrics, never combined into
    one; and instrument AGE — oldest-item and 90th-percentile age — because sixteen days without a
    decision is the load-bearing number and it is the one not currently reported. Composition by
    risk level is required for the same reason: a Critical item must not age silently inside an
    aggregate. (6) HIGH WIP CONCEALS. The stated harm mechanism is that high WIP "hides problems
    because nothing ever finishes" — an item that should have triggered action can sit indefinitely
    without ever registering as a FAILURE, so a Critical-risk item in a 40-deep queue is
    functionally undetected. This is the mechanism by which the very growth that signals the review
    function's collapse is reported as evidence that the system is working, which is worse than
    having no metric at all.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the framing was shared by
    THREE independent runs reporting the same queue, i.e. it is a house convention, not one run's slip)
  Supporting evidence: Ridgway, V.F. (1956), "Dysfunctional Consequences of Performance
    Measurements," Administrative Science Quarterly 1(2):240-247 [15a]. Little, J.D.C. (1961), "A
    Proof for the Queuing Formula: L = lambda W," Operations Research 9(3):383-387 [cited by BOTH
    directions]. Institute for Fiscal Studies, "The past and future of NHS waiting lists in England"
    and "Can the government achieve its 18-week elective waiting time target?"; Nuffield Trust;
    Office for Statistics Regulation statement on comparability [15b — the strongest single source
    on this item and AGAINST-direction only]. Goodhart's law, strong form: Goodhart 1975
    [UNVERIFIED in BOTH directions]; "Goodhart's Law in Reinforcement Learning," arXiv:2310.09144;
    "The Strong, Weak and Benign Goodhart's law," arXiv:2505.23445 [existence confirmed, contents
    not read]. Counter-metric / guardrail / paired-indicator practice and WIP-limit rationale
    (Atlassian, Scrum.org, getDX, DORA pairing convention) — practitioner sources, cited by BOTH
    directions. Peer-review capacity literature: Horta et al. (2024), Higher Education Quarterly
    78 [co-author list uncertain]; "Can We Volunteer Out of the Peer Review Crisis?"
    arXiv:2604.27900 — NeurIPS submissions 1,678 (2014) -> 17,491 (2024), reported uniformly as the
    cause of a crisis and never as a measure of the field's health [15a].
  Challenges noted: this premise IS the challenge direction — 15b CHALLENGED (Strong), 15a
    NO-SUPPORT-FOUND (None) with no novelty flag. 15a's one honest defence is preserved and scoped:
    queue growth IS a valid leading indicator of UPSTREAM DETECTION ACTIVITY, so if the intended
    referent of "the hunt's health" were strictly generation, the metric would be incomplete rather
    than wrong. That defence collapses the moment the figure is read as a SYSTEM-health measure,
    which is what three independent runs did, and it is exactly the substitution Ridgway names.
    Clause (5) is the form in which the defence survives.
  RELATION TO THE EXISTING REGISTER — checked explicitly, and this is NOT a re-mint: PREMISE-143
    clause (1) already states that a metric which rises when the system worsens and is read as
    reassurance is the worst property a metric can have — for RETRACTION COUNTS. PREMISE-110 states
    the same polarity defect for DETECTORS. PREMISE-147 is the third member of that family and its
    new content is (a) the size-versus-performance NON-RELATION with an authoritative institutional
    demonstration (clause 1), (b) the PAIRING REQUIREMENT — every quantity indicator needs a quality
    indicator (clause 4), and (c) COUNT-VERSUS-AGE as the choice of statistic (clause 5). None of
    those three is stated anywhere in the register. PREMISE-138 is CONFIRMED and NOT amended.
  Consistency check performed before INCORPORATE: PREMISE-138 (repetition in a channel with no
    effector is not a remedy; escalation must change the addressee, not the amplitude);
    PREMISE-143 (metric inversion, above); PREMISE-110 (detector polarity); PREMISE-102 (repeated
    non-processing becomes a standing policy of non-coverage — the sixteen days are that); and the
    six premises REVISE-282 records as contradicted by 14b's line 88 — PREMISE-003 (human review
    capacity is the binding constraint), PREMISE-070 (do not over-feed intake while review is the
    bottleneck), PREMISE-095 (arrival exceeds service; the queue grows without bound absent a
    cadence change or admission cap), PREMISE-106 (the lit-search queue is in the unstable regime),
    PREMISE-119 (production and judgment are not independently schedulable; backpressure is a
    CORRECTNESS requirement), PREMISE-121 (each additional correctly-argued item can lower the
    probability that ANY item is acted on). All six are ACTIVE and all six are CONFIRMED, not
    contradicted; PREMISE-121 in particular is the consumer-side statement of which clause (4) is
    the instrument-side statement. No contradiction found with any ACTIVE premise.
  NO SECOND REVISION FLAG MINTED FOR THIS ITEM, and the reason is this premise's own subject
    matter: the changes it implies — add a metric that falls, put a WIP limit on the review queue
    with an explicit policy at the ceiling — are already requested at REVISE-282 items (2) and (4)
    and are carried forward in this batch by REVISE-283. A third filing of the same request into a
    channel at 40 open items with no decision in sixteen days would be PREMISE-138 clause (1)
    exactly, and would be this premise's own error committed in the act of recording it.
  Confidence: Moderate. Clause (1) is High — authoritative, directly on point, and institutional.
    Clauses (2), (4) and (5) rest substantially on PRACTITIONER rather than peer-reviewed flow
    literature, though Little's Law itself is a standard queueing result; Goodhart 1975 is
    unverified in both directions; and Little's Law is applied outside its stationarity assumption
    and is used diagnostically only.
  Applicable to: the review-queue figure wherever it is reported, and the three independent runs
    that read 34 -> 40 as health; every producer-side count in the daily report, the fleet health
    report and agent run footers; the 15d monitor queue, whose ~zero consumption since 2026-07-08
    is the same signature in a second register; the item-generation rate of this pipeline,
    including this batch.
  OPEN MEASUREMENT NAMED AT VALIDATION (in-house, requires no authorisation): (i) reconstruct the
    review queue's time series — arrivals, departures, size, and the age distribution (max and 90th
    percentile) per day — and plot cumulative arrivals against cumulative departures; monotone
    divergence means the object is an ACCUMULATOR, not a queue, and no reading of growth as health
    survives. (ii) Enumerate every metric the system currently reports and record, for each, its
    sign of response to a new unresolved item; if the count that FALLS is zero, 14b's second clause
    is confirmed exactly and the Goodhart risk is live. (iii) Check whether any item has been in the
    queue longer than the oldest item was when the queue stood at 34 — if so the growth is not
    turnover, it is sedimentation. NOT RUN this session.
  Re-check due: 2026-09-06 (Monthly)
  Status: ACTIVE
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Original item: PRESUMPTION-691 (NOTE: compounds PRESUMPTION-677 → REVISE-282, D-608)
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a framing shared by three independent runs reporting the same queue
      15a: Searched for supporting literature; NO-SUPPORT-FOUND (None); no novelty flag
      15b: Searched for challenging literature; CHALLENGED (Strong); named in the SYSTEMIC-RISK-FLAG
        as the most dangerous member, because it converts the gap into an affirmative health signal
      15c: Net evaluation and disposition; INCORPORATE THE NEGATION as the MEASUREMENT-LAYER premise
        distinct from PRESUMPTION-677's arrival-rate claim; steelman folded in as clause (5)
        (separate find-rate from resolve-rate, instrument age, never throttle the detector); no
        second revision flag minted, by this premise's own logic
    Current status: INCORPORATED
    Disposition record: DISPOSITION-613 (2026-08-06)

PREMISE-148:
  Date validated: 2026-08-06
  Source item: PRESUMPTION-695
  Statement: DISCLOSURE OF A PROVENANCE ROUTE IS NOT AN AUDIT OF IT, AND OBJECT-LEVEL CONTENT
    CARRIES THE HIGHER MEASURED ERROR RATE OF THE TWO THINGS THIS SYSTEM COULD AUDIT. Six clauses.
    (1) THE RATES ARE MEASURED AND THEY ARE NOT SMALL. Quotation error — whether the cited source
    actually supports the citing author's statement — pools at 25.4% (95% CI 19.5-32.4) over 28
    studies (Jergas & Baethge 2015, PeerJ 3:e1364), recalculated more strictly to 14.5% (10.5-18.6)
    by Mogull (2017, PLOS ONE 12(9):e0184727), who also finds that 64.8% (56.1-73.5) of content
    errors are MAJOR — the referenced source fails to substantiate, is unrelated to, or CONTRADICTS
    the assertion. Improper secondary or indirect citation — taking a claim from a description
    rather than the source, which is precisely the route in this item — runs at about 10.4%
    (3.4-17.5). Major inconsistency between abstracts and full reports runs 5-45% with a median
    around 19%, and 40-60% for RCT results in several specialties. Abstract screening ALONE, a far
    simpler judgement than triplet extraction, carries 10.76% total error (7.43-14.09) across
    329,332 decisions. (2) EXPERIENCE IS NOT THE CONTROL. Data-extraction error ran 28.3-31.2%
    across minimal, moderate and substantial experience levels and DID NOT FALL with experience
    (Horton et al. 2010); single extraction generates more errors than double (Buscemi et al. 2006).
    The control shown to work is STRUCTURAL DUPLICATION — at least two independent extractors —
    which a disclosed-but-unaudited route by definition lacks. (3) PROCESS CONFORMANCE DOES NOT
    LICENSE AN INFERENCE TO PRODUCT QUALITY. The quality-assurance taxonomy holds that a process
    audit measures conformance to the defined process while a product audit measures the finished
    output against specification, that both are required, and that neither substitutes for the
    other. The software-quality literature is blunter: ISO 9000 is a set of guidelines for the
    PRODUCTION PROCESS and is "not directly concerned about the product itself," and conformance
    produces uniformity, which does not guarantee quality. A register holding ~1,460 machinery items
    against comparatively few content items has instrumented its process and INFERRED its product.
    That is the inference this literature declines to license. (4) DISCLOSURE DECAYS UNLESS
    SOMETHING DOWNSTREAM CONDITIONS ON IT. The citation-integrity literature names the aggravating
    mechanism: repeated secondary citation produces AUTHORITY BY REPETITION, under which a claim
    becomes treated as background knowledge. After two or three internal citations the "from a
    publisher's description" qualifier is no longer adjacent to the claim, and the disclosed route
    is invisible to the reader who needs it. Provenance must therefore be a STRUCTURED, MACHINE-
    READABLE FIELD carried on every citation, not prose in the originating artifact. Prose
    disclosure is the PRECONDITION for an audit — and is genuinely better than the undisclosed
    indirect citation the literature measures — but it is not a substitute for one. (5) NARROWING,
    FROM THE STEELMAN, AND LOAD-BEARING. The measured rates are dominated by NUMERIC AND INFERENTIAL
    content, and secondary sources may be perfectly adequate for IDENTITY-LEVEL facts — who, what,
    which triplet — while unreliable for magnitudes, effect claims, qualifications and conclusions.
    Content-type gating preserves most of the efficiency and is the distinction the evidence
    supports: secondary route permitted for identity and existence, PRIMARY SOURCING REQUIRED for
    magnitudes and conclusions. There is also a real resource argument for asymmetric attention —
    process defects are systematic and one process fix corrects a class of product defects, whereas
    a product check generalises to nothing — and no located source benchmarks an appropriate
    process-to-product audit ratio, so the ~1,460-to-few figure cannot be SCORED, only its direction
    read. What the steelman cannot survive is the absence of a SAMPLE: without an in-system error
    rate, the claim that these errors rarely change conclusions is untested in this system
    specifically, and any statement about content reliability is an assumption rather than a
    measurement. (6) AN INACCESSIBLE SOURCE IS A DISTINCT AND WEAKER TIER. A paywalled session known
    only through a host's write-up is TERTIARY, and its item is UNREVERIFIABLE — a later auditor
    cannot re-check it without acquiring access, so its error status may be permanently
    indeterminate. Such items must be flagged as unreverifiable and excluded from load-bearing
    conclusions, not merely footnoted.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the asymmetry is emergent
    in the register's composition rather than anywhere decided)
  Supporting evidence: Jergas, H. & Baethge, C. (2015), "Quotation accuracy in medical journal
    articles — a systematic review and meta-analysis," PeerJ 3:e1364, DOI 10.7717/peerj.1364 [15a].
    Mogull, S.A. (2017), "Accuracy of cited 'facts' in medical research articles," PLOS ONE
    12(9):e0184727 [cited by BOTH directions; author list unconfirmed in the AGAINST direction].
    Horton, J. et al. (2010), "Systematic review data extraction: cross-sectional study showed that
    experience did not increase accuracy," J Clin Epidemiol [15a]. Buscemi, N. et al. (2006),
    "Single data extraction generated more errors than double data extraction in systematic
    reviews," J Clin Epidemiol 59(7):697-703 [volume/pages from established knowledge]. Wang, Z. et
    al. (2020), "Error rates of human reviewers during abstract screening in systematic reviews,"
    PLOS ONE 15(1):e0227742 [cited by BOTH directions]. Pitkin, R.M., Branagan, M.A. & Burmeister,
    L.F. (1999), "Accuracy of Data in Abstracts of Published Research Articles," JAMA
    281(12):1110-1111, PMID 10188662 [15b; specific error percentages NOT confirmed, so no rate is
    asserted from it]. Scoping review of abstract-versus-full-report comparisons, PMC5747940 [15b;
    UNVERIFIED — fetch blocked by reCAPTCHA; figures taken from search-result summary]. "Quotation
    errors in general science journals," Proc. R. Soc. A 476(2242):20200538 (2020) [authors not
    confirmed]. Process-vs-product: ASQ/IATF-lineage QA taxonomy [15a, practitioner]; CMM/ISO 9000
    comparative material [15b, teaching and overview sources].
  Challenges noted: this premise IS the challenge direction — 15b CHALLENGED (Strong), 15a
    NO-SUPPORT-FOUND (None). The mitigating half of the record is preserved: the route WAS disclosed,
    and disclosed provenance is substantially better than the undisclosed indirect citation Mogull
    measures. It is folded into clause (4) as a precondition rather than credited as a control. The
    conference-abstract literature genuinely cuts both ways and is recorded in clause (5): including
    conference abstracts RARELY CHANGED systematic-review conclusions in a 2025 case study, grey
    literature makes only minor differences in meta-epidemiological work, and in rapidly evolving
    fields abstracts were the only evidence available at 14% of time points.
  Cross-direction source overlap (PREMISE-120 disclosure): Mogull 2017 and the PLOS ONE 2020
    abstract-screening study were cited by BOTH directions. Per PREMISE-111 that is residual
    correlation, not two independent confirmations. The disjoint material is 15a's extraction-error
    line (Horton, Buscemi) and 15b's abstract-versus-full-report and authority-by-repetition line.
  Consistency check performed before INCORPORATE: PREMISE-103 (absence of primary text is a KIND-
    difference in evidence, not a degree-difference; no confidence label over metadata-only material
    is well-founded, and downgrading confidence is not a valid substitute for an explicit "unfounded
    pending retrieval" state) — DIRECTLY on point, ACTIVE, and CONFIRMED rather than contradicted;
    PREMISE-148 extends it with measured rates, the process/product clause, the authority-by-
    repetition mechanism and the tiering requirement, and clause (6) is 103's "unfounded pending
    retrieval" state made operational as a field. PREMISE-113 (a detector's findings are evidence
    about the instrument until its precision is measured — the same logic applied to an extraction
    route rather than a detector). PREMISE-124 (no self-measurement of the pipeline's own
    completeness or accuracy without an external baseline or a seeded denominator — the sampling
    audit below IS the external denominator 124 requires, and its absence is why no current claim
    about content reliability is admissible). PREMISE-101; PREMISE-114; PREMISE-120; PREMISE-111. No
    contradiction found with any ACTIVE premise.
  Confidence: Moderate. Direction and MECHANISM transfer cleanly; RATE does not. The strongest
    sources measure structured numerical extraction in medical evidence synthesis, where error is
    unusually well defined, and a PRS triplet taken from a publisher's description is a coarser
    object for which these figures are neither an upper nor a lower bound. Nothing was located on
    PUBLISHER-SUPPLIED PROMOTIONAL descriptions specifically, whose register differs from a
    scientific abstract and whose error profile may be worse; that gap is covered by no cited source
    in either direction and is the single most useful follow-up search.
  Applicable to: the PRS triplets extracted from publishers' descriptions, and specifically the one
    taken from a paywalled session's host write-up; every object-level result entering the vault and
    every internal citation of one; the composition of this register; PRS candidate admission, where
    PREMISE-103 already applies; any future claim that the object level is adequately covered.
  OPEN MEASUREMENT NAMED AT VALIDATION (in-house, requires no authorisation, and DECISIVE — this is
    the condition on which the steelman turns): (i) sample n PRS triplets sourced from publishers'
    descriptions, verify each against the PRIMARY source, and report the discrepancy rate with a
    confidence interval against the ~19% median from the abstract-versus-full-report literature.
    Materially below -> the steelman is supported for this content type and the presumption is
    defensible here; at or above -> the presumption is refuted empirically IN-SYSTEM. (ii) Grep the
    vault for whether ANY object-level item carries a STRUCTURED provenance field; if provenance
    exists only as prose, clause (4) fails by inspection today. (iii) Classify register items as
    machinery-directed or content-directed to confirm the ~1,460-to-few ratio, then compute the same
    ratio for ERRORS ACTUALLY FOUND — if machinery audits find errors at a far lower rate per item
    than the content sample, audit effort is demonstrably misallocated. NOT RUN this session.
  Re-check due: 2026-09-06 (Monthly)
  Status: ACTIVE
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c]
    Original item: PRESUMPTION-695
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read the day's best object-level result against its own disclosed provenance route and
        against this register's composition
      15a: Searched for supporting literature; NO-SUPPORT-FOUND (None); PARTIAL novelty gap noted on
        one sub-question only — no source establishes an appropriate allocation ratio between
        process-directed and product-directed verification effort, which is why clause (3) states a
        DIRECTION and not a target
      15b: Searched for challenging literature; CHALLENGED (Strong); member of the SYSTEMIC-RISK-FLAG
      15c: Net evaluation and disposition; INCORPORATE THE NEGATION as an extension of PREMISE-103
        rather than a replacement; steelman folded in as clause (5) content-type gating; the ratio
        claim explicitly NOT scored against a benchmark, since none exists
    Current status: INCORPORATED
    Disposition record: DISPOSITION-614 (2026-08-06)


--------------------------------------------------------------------------------
## 2026-08-07 CYCLE NOTE — ZERO INCORPORATE (no additions to this register)

The 2026-08-07 lit-search pipeline run dispositioned **10 items** from the 2026-08-06 14a/14b
intake — PRESUMPTION-696, 701, 703, 707, 710, 712, 713, 714, 716 and ASSUMPTION-803 — as
DISPOSITION-615 through DISPOSITION-624. Mix: **0 INCORPORATE / 2 MONITOR / 8 REVISE**. No
premise was minted. The next available premise number remains **PREMISE-149**.

**Why zero, stated so it can be argued with.** Nine of the ten items are PRESUMPTIONs, and on
seven of those nine the AGAINST direction returned CHALLENGED (Strong) while the FOR direction
returned PARTIALLY-SUPPORTED at Weak, or NO-SUPPORT-FOUND at None. On PRESUMPTION-716 the FOR
direction returned **NO-SUPPORT-FOUND / None** and reported that the sources closest to supporting
the item deny it in explicit terms. That configuration is the charter's REVISE signature, not its
INCORPORATE signature.

**Why no negations were incorporated either, which is the more interesting question given that the
2026-08-06 run minted five.** The negations available in this batch are, in substance, already
ACTIVE in this register:
  · 696's negation (an internally built evaluator's independence must be measured, not asserted)
    is PREMISE-004's standing independence caveat plus PREMISE-110's common-mode scope guard plus
    PREMISE-111/120 on same-family convergence. A fourth statement would be PREMISE-138 clause (1).
  · 703's and 707's negations (a detector's coverage must be established by seeded faults, not
    inferred from its catches; absence of a signal is the dangerous case) are PREMISE-100 and
    PREMISE-110, and the seeded-fault requirement is the cross-cutting RULE requested at REVISE-286
    rather than a premise about the world.
  · 712's and 716's negations (production is not consumption; a record written is not a control
    exercised) are PREMISE-106 (queue in the unstable regime) and PREMISE-147 (producer-side
    proxies mistaken for system health), both minted within the last month.
  · 701's negation (determinacy of the specification does not warrant the execution) is adjacent to
    PREMISE-088 (bulk-edit human-check discipline) and PREMISE-103's verification lineage.
What each of these items adds is not new KNOWLEDGE but a REQUIRED CHANGE that no agent is
authorised to make — which is a revision flag by construction, not a premise. Minting restatements
would have grown this register while leaving the requests unmade.

**The one item where an INCORPORATE was genuinely available and was declined: PRESUMPTION-714.**
15a returned SUPPORTED (Moderate) — the only SUPPORTED result in the batch — and both directions
independently recommend the same action (a supervisory bound above the tool-call loop, correct
under either hypothesis). The narrow premise "an unbounded wait is a defect on its own terms,
independent of the stall's cause" was available. It was routed to MONITOR-504 instead, on one
condition: the grep that would establish whether ANY tool call site currently carries a bound has
not been run. A premise whose basis is one unrun grep is a premise minted from a claim, which is
the failure PREMISE-110's proof-test guard exists to prevent. If the grep is run and returns "no
bound anywhere," PREMISE-149 should be minted from MONITOR-504 with the grep as its basis.

**The reflexive caveat, recorded rather than resolved.** A 0-INCORPORATE / 8-REVISE mix should NOT
be read as this instrument working well. 14b selects for presumptions it believes false, so a high
challenge rate is the expected output rather than a finding — the same caveat the 2026-08-06 run
recorded in the opposite direction on a 5-of-6 negation rate. Four consecutive runs now show
materially different mixes (2026-08-04: 10 REVISE of 11; 08-05: 5 REVISE, 3 INCORPORATE of 8;
08-06: 1 REVISE, 5 INCORPORATE of 6; 08-07: 8 REVISE, 0 INCORPORATE of 10). That variance is weak
evidence against the "tilts toward REVISE regardless of input" reading in both directions, and the
held-out generalizability study requested in REVISE-271 remains the only thing that would
distinguish them. It remains un-run.

**Register composition note.** This register has now gone one cycle without a new entry, following
a cycle that added five. Per the standing structural concern recorded at the 2026-05-13 cycle note:
if the disposition criteria are correct, the upstream extractions are producing
well-formed-but-not-validation-ready items; if they are too strict, the register starves. This
run's reading is the first: eight of ten items requested a CHANGE rather than asserting a FACT, and
a request is not a premise. That reading is checkable — if the eight requested changes are made and
the underlying claims then validate, the criteria were right; if the requests are never actioned
and the items recur, the criteria were beside the point and PRESUMPTION-712's diagnosis applies to
this register too.

  Dispositions: DISPOSITION-615..624 (recorded in lit_search_returns.md, 2026-08-07 run section)
  MONITOR items: MONITOR-503 (PRESUMPTION-713), MONITOR-504 (PRESUMPTION-714)
  REVISE items: REVISE-284..291
  Consistency check performed against this register: NO CONTRADICTIONS FOUND, and none could arise,
    since no premise was minted. The premises this batch bears on — 004, 088, 100, 102, 103, 106,
    110, 111, 120, 121, 124, 138, 143, 146, 147, 148 — are all CONFIRMED rather than contradicted
    by the batch's findings. PREMISE-146 (the 4,000-token ceiling is unsatisfiable as specified) is
    directly relevant and is confirmed again: this run exceeded both the per-task and session
    budgets, and the twenty result files it had to read total ~264 KB.
--------------------------------------------------------------------------------


================================================================================
## 2026-08-10 — 15c cycle (3 premises minted: PREMISE-150..152)

**Why three premises after a cycle that minted none.** All three are cases where 15a and 15b, searching
independently, landed on the SAME literature and drew the SAME conclusion. The apparent for/against
opposition in the returns is an artefact of the items being written as defective premises: 15a supported
the corrective, 15b challenged the defect, and both were describing one finding. Where the two directions
genuinely diverged, the item went to MONITOR or REVISE, not here.

PREMISE-150:
  Date validated: 2026-08-10
  Source item: PRESUMPTION-729
  Item type: PRESUMPTION (unstated — extra weight: the system was unaware it was assuming this)
  Statement: A batch of defects that a detector failed to catch bounds THE DETECTOR'S COVERAGE, not
    merely that batch. A high adequacy score and a confirmed missed-defect class co-occur mechanistically
    and are not in tension; the score is computed over what the detector can see.
  Supporting evidence (15a, SUPPORTED/Strong): mutation-testing literature — Trail of Bits (2025), "Use
    mutation testing to find the bugs your tests don't catch"; test-adequacy survey arXiv:2212.06118.
  Challenges noted (15b, CHALLENGED/Strong — same direction, not opposed): "highest fidelity ever"
    co-occurring with confirmed undetectable defects is the exact signature mutation testing exists to
    expose; treating the finding as batch-local is unsupported.
  Confidence: High — a close structural match, not a distant analogy.
  Applicable to: every QC/fidelity/detector metric in this system, including the janitor and
    fidelity_check.py; and to any future claim that a batch "passed".
  Operational consequence: adequacy claims require SEEDED defects, not observed pass rates.
  Re-check due: 2026-09-10 (Monthly)
  Status: ACTIVE

PREMISE-151:
  Date validated: 2026-08-10
  Source item: PRESUMPTION-731
  Item type: PRESUMPTION (unstated)
  Statement: Repeated disclosure of an unremediated condition normalises it rather than resolving it. A
    disclosed-but-unremediated condition is not a controlled condition, and the disclosure record is
    evidence of incubation, not of management.
  Supporting evidence (15a, SUPPORTED/Strong): Vaughan, D. (1996), "The Challenger Launch Decision" —
    normalization of deviance; Buzbee, "Asymmetrical Regulation: Risk, Preemption, and the Floor/Ceiling
    Distinction," NYU Law Review (on structurally unmeetable ceilings).
  Challenges noted (15b, CHALLENGED/Strong — same direction): thirteen consecutive disclosed-but-
    unremediated days matches the documented incubation pattern preceding organisational failure.
  Confidence: High — both directions independently cited Vaughan.
  Applicable to: the standing disclosure practice in this pipeline, including the independence
    disclosure repeated by the 08-09 run and again by this one; the token-budget breach note; every
    "recorded rather than silently fixed" entry.
  Caveat carried: the floor/ceiling half — that a stated ceiling may be structurally unmeetable at fixed
    cost — is supported but is a separate claim, and is NOT incorporated here.
  Reflexive note, per the premise itself: THIS RUN discloses a token-budget breach and an independence
    limitation. Under PREMISE-151 those disclosures do not make the conditions managed.
  Re-check due: 2026-09-10 (Monthly)
  Status: ACTIVE

PREMISE-152:
  Date validated: 2026-08-10
  Source item: ASSUMPTION-814
  Item type: ASSUMPTION (stated)
  Statement: HOMOGENEOUS, UNGUIDED multi-agent debate does not outperform isolated self-correction at
    matched compute. Gains from debate require heterogeneity of agents, role guidance, or an explicit
    calibration mechanism. The scope conditions are part of the premise and may not be dropped.
  Supporting evidence (15a, SUPPORTED/Strong): "The Cost of Consensus: Isolated Self-Correction Prevails
    Over Unguided Homogeneous Multi-Agent Debate" (arXiv:2605.00914, 2026) [unverified — from search
    snippet]; convergent 2025-2026 results.
  Challenges noted (15b, PARTIALLY-CHALLENGED/Moderate): the finding is scoped to small (7-8B),
    homogeneous, unguided debate; arXiv:2510.20963 and arXiv:2502.08788 report debate outperforming when
    heterogeneous or guided. 15b's crux — whether C2A2 matches the scope — is why the scope conditions
    are written into the premise statement rather than stripped from it.
  Confidence: Moderate. Two of the three citations are unverified search snippets; verification is
    requested at the run's verification note.
  Applicable to: agents 01-11 and 17-20 (the tradition ensemble), the 15a/15b pair, and any future
    proposal to add debate rounds.
  OPEN and NOT settled by this premise: whether C2A2's tradition ensemble is in fact heterogeneous and
    guided in the sense the literature means. Carried at MONITOR-512.
  Re-check due: 2026-09-10 (Monthly)
  Status: ACTIVE

  Consistency check performed against this register: NO CONTRADICTIONS FOUND. PREMISE-152 is the first
    entry that bears directly on MONITOR-001 (ASSUMPTION-003, "independent FOR/AGAINST search prevents
    confirmation bias", monitoring since 2026-04-13 on the grounds that role assignment may activate
    motivated reasoning). PREMISE-152 says heterogeneity and guidance are what make multi-agent structure
    pay; the 15a/15b pair is guided (assigned directions) but homogeneous (one model). That is a partial
    answer to MONITOR-001 and is recorded there, not resolved here.
  Dispositions: DISPOSITION-630..653 (lit_search_returns.md, 2026-08-10 run section)
  MONITOR items: MONITOR-505..512 · REVISE items: REVISE-295..309
--------------------------------------------------------------------------------

PREMISE-153:
  Date validated: 2026-08-12
  Source item: PRESUMPTION-776 (clause P1 only; clause P2 NOT incorporated — see below)
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Statement: UNCOMMITTED WORK HELD ON EPHEMERAL COMPUTE IS AN ACTIVE DATA-LOSS EXPOSURE, NOT A
    SCHEDULING DEFERRAL, AND THE EXPOSURE IS DEFINITIONAL RATHER THAN PROBABILISTIC. Ephemeral
    storage is specified to be lost on stop, reboot, instance replacement, cluster upgrade,
    autoscaling event or host maintenance — none of which are failures, all of which are normal
    lifecycle events. Vendor and standards guidance is unqualified: place only scratch files,
    caches, or REBUILDABLE artefacts on ephemeral volumes. Generated wiki content is not a
    rebuildable artefact. Therefore "the commit is deferred" and "the work is at risk of total
    loss" are not two readings of one state; the second is the state, and the first is a
    description of intent that has no bearing on durability. SCOPE CONDITION (load-bearing, from
    15b): this premise is about the storage CLASS, not about any particular file count. It binds
    only once a path is established to be on ephemeral rather than host-mounted or replicated
    storage. 15b correctly observed that the originating item never verified the storage class of
    its 191 paths; that verification is a precondition of applying the premise to that incident,
    and is carried at MONITOR-520. The premise itself does not depend on the incident.
  Supporting evidence (15a, PARTIALLY-SUPPORTED overall; P1 SUPPORTED/Strong): converging vendor and
    standards documentation on ephemeral-storage semantics (MongoDB "What is Ephemeral Storage in
    Kubernetes?"; simplyblock "Persistent Storage"; appsecuritystandards.org "Ephemeral Workloads";
    ITU Online) [unverified — from search snippets; vendor/standards documentation, authoritative as
    practice rather than primary research]. See lit_search_results/for/PRESUMPTION-776_for.md.
  Challenges noted (15b, PARTIALLY-CHALLENGED/Moderate): two challenges, both accepted and both
    folded in rather than outweighed. (1) The storage class was never verified — now the scope
    condition above. (2) Git was never a valid yield substrate in the first place (GitClear /
    Pragmatic Engineer git-metric critique; SPACE framework, arXiv:2511.20955 [unverified]), so the
    metric half of the originating item is a pre-existing invalidity and not a consequence of the
    unwritable git. That is why clause P2 is excluded from this premise. See
    lit_search_results/against/PRESUMPTION-776_against.md.
  Confidence: Moderate. The proposition is definitional and uncontested in substance, but every
    citation supporting it is a vendor or practitioner document read from a search snippet, none
    verified at source, and PREMISE-132 (citing is not verifying) applies to this entry as written.
    Confidence is capped at Moderate for that reason alone, not because the claim is doubtful.
  Applicable to: any agent producing durable content in the Cowork/container workspace; the
    convergence step that pushes to git; the yield metric; and any future decision to treat an
    unwritable store as a deferral.
  CLAUSE P2 NOT INCORPORATED — AND 15a's NOVELTY FLAG IS REFUTED BY THIS REGISTER. 15a raised a
    NOVELTY-FLAG on P2 ("a metric whose producers cannot write the measured store is measuring
    durability rather than production"), reporting no literature. P2 is not novel: PREMISE-140
    (2026-08-02) already holds that a metric derived from one observation channel must be named by
    its channel and not by the thing the channel proxies for, which is P2 exactly. The novelty flag
    is withdrawn here. This is the second finding of the run's consistency check and is recorded as
    a defect against 15a's charter, which directs it to read the tradition wikis but never
    validated_premises.md — so 15a can and did report as novel a premise this system validated ten
    days earlier.
  OPEN and NOT settled by this premise: whether the 191 paths named in the originating item are in
    fact on ephemeral storage. Carried at MONITOR-520.
  Re-check due: 2026-09-12 (Monthly)
  Status: ACTIVE

  Consistency check performed against this register: NO CONTRADICTIONS FOUND, but SIX NEAR-DUPLICATES
    and one refuted novelty flag were found across the batch, which is the principal finding of this
    run and is recorded in full in lit_search_returns.md. PREMISE-153 itself has no near-neighbour:
    no existing premise addresses durability, storage class, or the ephemeral/persistent boundary.
    It is the only one of fourteen items whose corrective proposition was not already carried.
  Dispositions: DISPOSITION-667..680 (lit_search_returns.md, 2026-08-12 run section)
  MONITOR items: MONITOR-514..521 · REVISE items: REVISE-317..322
--------------------------------------------------------------------------------

================================================================================
## 2026-08-13 — 15c cycle (5 premises minted: PREMISE-154..158, from PRESUMPTION-778..786)

**POLARITY, stated once and binding on all five entries.** All nine items in this batch are 14b
PRESUMPTIONS worded "That [belief the system holds]", where the belief is the unsafe thing. 15a
searched FOR the CORRECTIVE CONVERSE, so "15a SUPPORTED/Strong" means 14b's worry is well grounded.
Every premise below is therefore stated in CORRECTIVE form. None of them validates a presumption as
14b worded it.

**WHY FIVE, AND WHY NONE OF THEM ADDS A CONTROL.** Five mints in one batch is high for this register
(the 2026-08-12 batch minted one of fourteen) and register inflation is a live hazard under
PREMISE-105. Each of the five was checked against the register before minting and each closes a gap
the register can be shown not to hold — 154 discharges a gap PREMISE-133 NAMES IN ITS OWN TEXT; 155,
156, 157 and 158 have no antecedent on identity-vs-name, shared-input dependence, the recording
threshold, or two-sidedness respectively. More importantly, and in direct response to 15b's
SYSTEMIC-RISK-FLAG of the same date: NOT ONE of the five mandates a new universal control. Four of
them CHANGE A CRITERION or REMOVE work (156 removes downstream checks; 157 replaces a trigger without
lowering a threshold; 158 replaces per-reading re-derivation with a one-time profile; 155 converts an
alert into a displayed number), and 154 binds its mechanism to a trigger rather than a clock. That
was the flag's recommendation (1) and it is satisfied by construction rather than by promise.

**THE FOUR ITEMS NOT MINTED ARE THE OTHER HALF OF THE FINDING.** PRESUMPTION-778 and -785 went to
MONITOR because the register already holds their cheap half and their residual turns on an in-house
test both search directions specified identically. PRESUMPTION-781 and -783 went to REVISE WITHOUT A
MINT, because both are ENFORCEMENT gaps against premises this register already holds (PREMISE-067 /
PREMISE-144(5) for 781; PREMISE-133 for 783) and minting them a second time is barred by PREMISE-138
clause (1) and by the batch's own central finding that the binding constraint on this system is
propagation, not validation.

PREMISE-154:
  Date validated: 2026-08-13
  Source item: PRESUMPTION-779
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Statement: SCOPE-EXTENSION OF PREMISE-133 TO THE DEFERRAL/QUEUE COHORT, IN TRIGGER-BOUND FORM.
    PREMISE-133 requires that a suspension name what would discharge it, who adjudicates, and a
    deadline, and its own Applicable-to note explicitly DECLINES to license the backlog/queue cohort:
    it records that cohort as exhibiting the same outcome BY ANALOGY ONLY and as "needing its own
    grounds." Those grounds now exist and are supplied here. A hold placed in a work queue is a
    committal state, not a null one, and it does not maintain itself — the reject option is optimal
    only relative to a cost ratio the environment is free to change, and every domain that has
    institutionalised deferral has independently attached a re-assessment mechanism to the deferral
    rather than to the original decision. THEREFORE a hold is legitimate only if, AT PLACEMENT, it
    records (a) the observable whose change would make it wrong — its release condition — and (b) the
    party or process that reads that observable. LOAD-BEARING FORM CONDITION, from 15b and not
    optional: the discharging mechanism must be TRIGGER-BOUND, NOT A CLOCK. Time-based expiry and
    scheduled full re-audit are the specific remedies with the worst documented record in the nearest
    analogous domain — automatic closure of deferred items destroys accumulated triage state and
    forces re-derivation of judgements already made — and a repeated re-audit prompt across six
    queues is predicted by the alert-fatigue evidence to become a rubber stamp within a few cycles,
    which manufactures a false record of having looked and is the fail-open pattern PREMISE-110 names.
    EXPLICITLY NOT INCORPORATED: "a hold decays with elapsed time." No located source supports a
    decay model on the clock and none supplies a correct interval; every domain sets its own by risk
    tier. What is established is that a hold with no statable release condition has NO STATE
    TRANSITION OUT OF HOLDING, which is a defect AT PLACEMENT, not a defect of duration. ALSO NOT
    INCORPORATED: that a 100% hold rate is itself pathological. A conservative gate on a low-quality
    intake stream should hold most things, and PREMISE-133 protects principled abstention as
    conformant behaviour.
  Supporting evidence (15a, SUPPORTED/Strong): Friedman, J. (2017), "Why Suspend Judging?", Noûs
    51(2):302-326 — suspension is a committal attitude with its own warrant conditions. Chow, C.K.
    (1970), IEEE Trans. IT 16(1):41-46, and El-Yaniv & Wiener (2010) — the reject option's optimality
    is defined against a fixed cost ratio. Saha, Khurshid & Perry (2014), "An Empirical Study of Long
    Lived Bugs," CSMR-WCRE — unfixed bugs open a median 437 days [figure from a search snippet of the
    paper, not read in full]. Wattanakriengkrai et al. (2023), arXiv:2305.18150 — the ecosystem built
    an expiry mechanism because unbounded holds are a defect class [listing verified; authorship not
    independently confirmed]. Watchful-waiting / active-surveillance protocol structure (PubMed
    34495289; PMC9119349 — 76.5% of watchfully-waited follicular-lymphoma patients required
    second-line treatment within five years). Access recertification practice (ISO 27001 A.9.2.5 and
    equivalents) [clause numbers not verified].
  Challenges noted (15b, PARTIALLY-CHALLENGED/Moderate — folded in as the form condition rather than
    outweighed): the stale-bot natural experiment ("Should I Stale or Should I Close?", BotSE 2019;
    Zimmermann 2021 [personal blog, non-peer-reviewed]); prostate active-surveillance evidence that a
    correctly-scoped hold sustained over years achieves comparable outcomes (PubMed 38697055,
    18765115); Ancker et al. (2017), BMC Med Inform Decis Mak 17:36 — reminder acceptance falls ~30%
    per additional prompt per encounter. 15b's crux is accepted in full: "the honest version of the
    finding is not 'holds decay' but 'holds were placed without release conditions'."
  CORRELATION DISCLOSURE (per PREMISE-124): 15a's sources 1 and 2 (Friedman; Chow / El-Yaniv &
    Wiener) are THE SAME SOURCES this register used to validate PREMISE-133. This entry is an
    extension of PREMISE-133 and must NOT be counted as independent corroboration of it. Its
    genuinely disjoint evidence is the bug-triage, stale-bot, clinical-surveillance and
    access-recertification material, plus the whole of 15b's file.
  NOTED TENSION WITH PREMISE-049, surfaced rather than silently reconciled (charter §5): PREMISE-049
    prescribes "a revisit/expiry forcing function" for the UNVERIFIED quarantine, i.e. it names expiry
    where this premise prefers a trigger. The two agree on purpose — the hold must not become "flag
    and forget" — and differ on mechanism. This is recorded as a tension for reconciliation, NOT as a
    contradiction, and PREMISE-049 is not amended here. If the trigger form is adopted, PREMISE-049's
    mechanism clause should be re-read against it.
  Confidence: Moderate. The claim is largely already held by this register under a different word,
    the two strongest sources are non-independent of PREMISE-133, and the form condition rests partly
    on non-peer-reviewed practitioner material.
  Applicable to: the six queues reported at 100% hold for up to eleven consecutive runs; the ~174-item
    15d re-trigger backlog and the MONITOR-420/423 fired-trigger cohort, which PREMISE-133 named and
    declined to license and which this premise now covers; the MONITOR queue generally; 14a/14b
    intake, which must record a release condition at the moment an item is queued.
  OPEN MEASUREMENT NAMED AT VALIDATION (both directions specified it independently, which is why it
    is recorded here rather than as a separate MONITOR): sample the six held queues and measure two
    numbers — the fraction of holds for which a release condition can be stated at all, and, among
    those, the fraction whose condition has already changed. Statable conditions present and few
    changed -> the remedy is annotation and this premise is cheap to satisfy. Conditions largely
    absent -> the placement defect is confirmed directly. In-house, bounded.
  Re-check due: 2026-09-13 (Monthly)
  Status: ACTIVE

PREMISE-155:
  Date validated: 2026-08-13
  Source item: PRESUMPTION-780
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Statement: A STATE ASSERTION BINDS TO A RESOLVED ARTEFACT IDENTITY, NOT TO A NAME, AND AN
    ASSERTION TAKEN AT AN INTERNAL STAGE IS NOT A GUARANTEE FOR CONSUMERS. Two clauses. (1) IDENTITY:
    a check written against a NAME resolves to whichever object the running process can see, so two
    objects sharing a name can each satisfy the check while diverging from one another indefinitely.
    Any freshness, presence or state assertion must bind to a resolved identity — a resolved path, a
    hash, or a served response — and must resolve it THE WAY A CONSUMER RESOLVES IT. A name is not an
    identity. (2) OBSERVATION POINT: the divergence between what a system's own detector observes and
    what a consumer experiences is differential observability, and it is silent BY CONSTRUCTION
    rather than by oversight, because nothing in the architecture ever compares the two observation
    points. This extends PREMISE-089 (freshness is a per-source property) from ACROSS sources to
    WITHIN one source, and extends PREMISE-040 (measure the live artefact, not a copy) from
    documentation statistics to gates. ADD, DO NOT RELOCATE (load-bearing, from 15b): a snapshot-age
    check is a legitimate stage-latency instrument in every reference architecture; the defect is the
    ABSENCE of a second, consumption-side assertion, not the presence of the first, and removing the
    stage check loses the signal that localises the fault. EXPLICITLY NOT INCORPORATED: that a
    consumption-boundary assertion CLOSES the gap. It narrows it — a boundary check verifies only the
    path it was scripted for — so the set of consumption paths must be enumerated and any unmonitored
    path NAMED rather than assumed absent. FORM CONDITION, per the batch's systemic-risk flag: report
    artefact AGE as a displayed number rather than adding a pass/fail freshness alert per artefact per
    path. Freshness is a high-volume alert class and moving from alerting to display gets the signal
    without the acceptance decay.
  Supporting evidence (15a, SUPPORTED/Strong): Huang, P. et al. (2017), "Gray Failure: The Achilles'
    Heel of Cloud-Scale Systems," HotOS XVI — differential observability [canonical; already in this
    register under PREMISE-110, therefore NON-INDEPENDENT]. Google SRE Workbook, "Data Processing
    Pipelines," and Beyer et al. (2016) on black-box vs white-box monitoring [chapter URL verified].
    Data-freshness SLO practice (dbt Labs, Conduktor, Tacnode) and synthetic/black-box monitoring
    practice (Microsoft Engineering Fundamentals Playbook; Grafana; CloudWatch Synthetics) [vendor and
    practitioner documentation, verified as existing; documented practice, not measured effect].
    Batini et al. (2009), ACM Computing Surveys 41(3) [already in this register under PREMISE-006 —
    NON-INDEPENDENT].
  Challenges noted (15b, NO-CHALLENGE-FOUND on the core claim; PARTIALLY-CHALLENGED on the remedy):
    15b states plainly that the item "survives disconfirmatory search substantially intact." Its three
    challenges are all against the remedy and are all folded in above as clauses rather than
    outweighed — synthetic checks verify only scripted paths; a component check is a correct
    instrument rather than a wrong one; freshness is a high-volume alert family.
  Confidence: Moderate, AND THE CAP IS DELIBERATE. 15b's own search-scope note declares its
    NO-CHALLENGE-FOUND to be "a case of 'not enough searched' as much as 'searched and found
    nothing'", with almost all located sources vendor or practitioner material. That is NOT read as
    clearance here. Only one peer-reviewed source (Huang et al.) carries the core, and it is already
    register-held. Both directions independently name the same unsearched literature —
    cache-coherence and read-your-writes consistency — as the formal analogue; until that pass is
    run, Moderate is the ceiling.
  Applicable to: the freshness gate that reported 0.00h against a four-day-old published file of the
    same name; any gate, check or assertion in the pipeline that names its subject by filename rather
    than by resolved path; the vault publication step; PREMISE-089 and PREMISE-040, which this
    extends.
  NOT DUPLICATED HERE, AND NAMED INSTEAD: the one-read empirical question — do the two handles
    resolve to different files — is already queued as ASSUMPTION-1024 in the same 2026-08-12 intake.
    It is not re-queued as a MONITOR. Answering it confirms or refutes the incident; it does not bear
    on the premise, which is architectural.
  Re-check due: 2026-09-13 (Monthly)
  Status: ACTIVE

PREMISE-156:
  Date validated: 2026-08-13
  Source item: PRESUMPTION-782
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Statement: CHECKS THAT SHARE AN INPUT DATUM ARE ONE CHECK, AND METHOD-DIVERSITY REMEDIES DO NOTHING
    AGAINST THEM. This register's independence family — PREMISE-096 (a corroborating layer must draw
    on a genuinely disjoint evidence source), PREMISE-080 (shared method variance yields
    pseudo-convergence), PREMISE-004 (same-model-family convergence is not independent evidence),
    PREMISE-141(2) (a redundancy argument counting two instruments as two chances is counting one) —
    addresses, without exception, checks that share a METHOD or a MODEL. This premise adds the other
    direction of dependence: checks that share an INPUT DATUM. The distinction is operational, not
    taxonomic, because the standard remedies for method dependence — a different tool, a different
    model, a different frame — are worth exactly nothing against a wrong upstream key. Three
    consequences bind. (a) AGREEMENT AMONG ARTEFACTS DERIVED FROM A COMMON KEY MEASURES PROPAGATION
    INTEGRITY, AND IS NOT EVIDENCE ABOUT THE KEY. Thirteen mutually consistent files are one
    observation reported thirteen times; the count's comfort value is the hazard. (b) THE CONTROL
    BELONGS AT THE INGEST BOUNDARY, validated once against a referent OUTSIDE the derived population,
    because a downstream check is structurally blind to an upstream fault — every static check over
    those thirteen files was a discrepancy detector over quantities that all derived from the same
    key. (c) A KEY CARRIES A PROVENANCE MARK — EXTERNALLY-VERIFIED or ASSERTED — so that downstream
    agreement is read against the right prior. EXPLICITLY NOT INCORPORATED, and both exclusions are
    load-bearing: (i) that a single authoritative key is the error. It is not; storing a value once is
    what prevents divergence, and duplicating it trades a correlated-error failure for an
    inconsistency failure that is more frequent and harder to detect. The fault is at the boundary
    where a claim became a record without meeting an external referent. (ii) that the remedy is MORE
    CHECKS. Independently derived checks do not deliver independent failure; where redundancy is used
    at all, diversity must be FORCED and METHODOLOGICAL — a check that reads the source corpus
    directly is diverse from one that reads frontmatter; two checks that both read frontmatter are
    not, regardless of who or what wrote them.
  Supporting evidence (15a, SUPPORTED/Strong): Knight, J.C. & Leveson, N.G. (1986), "An Experimental
    Evaluation of the Assumption of Independence in Multi-Version Programming," IEEE TSE
    SE-12(1):96-109 — 27 independently written versions of ONE SPECIFICATION, one million tests,
    coincident failures far above the independence prediction, arising through DIFFERENT errors
    because the versions shared an upstream artefact [VERIFIED AT SOURCE this run —
    sunnyday.mit.edu/papers/nver-tse.pdf; this is the only primary source in the batch retrieved in
    full, and it is cited by BOTH directions]. Common-cause failure modelling: NUREG/CR-5485 (1998);
    IEC 61508-6 Annex D beta-factor treatment; SINTEF A26922 — CCF dominates the unreliability of
    redundant systems by defeating the coincidence redundancy purchases, and is addressed by attacking
    COUPLING FACTORS rather than root causes. Wimsatt (1981) on robustness and multiple determination
    [already register-held under PREMISE-004 — NON-INDEPENDENT]. Master/reference-data management
    practice on golden records and lineage [practitioner material].
  Challenges noted (15b, PARTIALLY-CHALLENGED/Moderate — and it agrees with the diagnosis): 15b's
    challenge is entirely against remedies and is folded in above as the two exclusions. Littlewood,
    B. & Miller, D. (1989), IEEE TSE 15(12):1596-1614 — forced methodological diversity can reduce
    correlated failure below the naive baseline, which is the constructive escape and the reason
    exclusion (ii) is stated as "forced and methodological" rather than as a flat prohibition.
    Normalisation / single-source-of-truth practice supplies exclusion (i).
  SOURCE-RETRIEVAL NOTE, recorded per PREMISE-132 (citing is not verifying): 15b cites arXiv:2606.20158
    ("N-Version Programming with Coding Agents," ASSERT-KTH) for a 2026 agent-based replication
    reporting 429 coincident failures against 115.36 predicted. That preprint was NOT reported as
    retrieved at full text by either direction; it is cited from a listing with figures taken from
    snippets. IT IS THE MOST INTERESTING SOURCE IN THE BATCH FOR THIS SYSTEM'S CLASS AND THIS PREMISE
    DOES NOT REST ON IT. The premise rests on Knight & Leveson, which was retrieved. If the
    replication is later verified, it strengthens the transfer to agent-authored checks specifically;
    if it fails to verify, nothing above changes.
  Confidence: High. Rare in this register and justified narrowly: the load-bearing primary source was
    retrieved in full, both search directions cited it and drew the same conclusion from it, the
    increment over existing premises is a distinction rather than a new claim, and the operational
    consequence REMOVES verification work rather than adding it — which means the premise is cheap to
    be wrong about in the direction it points.
  Applicable to: the `summa_ref` incident and any upstream key on which more than a small number of
    derived artefacts depend; the full static-check suite, whose independence claims are void for any
    quantity derived from a shared key; PREMISE-096 / 080 / 004 / 141(2), which this extends from
    shared-method to shared-input; any future proposal to add cross-checks as a remedy for a
    correlated-error finding.
  OPEN MEASUREMENT NAMED AT VALIDATION (both directions proposed it independently): enumerate the
    upstream keys on which more than three derived artefacts depend, and for each determine whether
    ANY check compares it to something outside the derived population. The count for which the answer
    is no IS the exposure and is measurable today. Sharper variant: corrupt one such key in a scratch
    copy and run the full static-check suite; the number of checks that still pass is the empirical
    measure of how much of this system's verification sits downstream of a single unverified claim.
  Re-check due: 2026-11-13 (Quarterly)
  Status: ACTIVE

PREMISE-157:
  Date validated: 2026-08-13
  Source item: PRESUMPTION-784
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Statement: THE RECORDING THRESHOLD FOR AN ARCHITECTURAL COMMITMENT KEYS ON REVERSIBILITY AND
    CROSS-AGENT DEPENDENCY, NOT ON IMPLEMENTATION EFFORT. Implementation cost and commitment cost are
    different quantities. An architecture is its set of design decisions rather than its set of
    components, from which it follows that "required no new tool, prompt or schema" is a statement
    about how a change was built and carries no information at all about whether a commitment was
    made. The trigger criteria in actual mainstream use are: the change is difficult to reverse; it
    crosses agent, team or service boundaries; it involves significant trade-offs; there is no
    existing basis for the decision. None of them is effort, and no located guidance offers effort as
    an exemption anywhere. Rationale is close to free to capture at the moment of decision and
    expensive-to-impossible to recover afterwards, which is the asymmetry that makes the threshold
    matter. EXPLICITLY NOT INCORPORATED, and this exclusion is the load-bearing half of the premise:
    "EVERY CHANGE NEEDS A DECISION RECORD." That is the documented failure mode of the practice —
    proliferation, fatigue, and significant decisions buried among trivial ones — and the same
    guidance that names the trigger criteria is explicit that changes limited in scope, time, risk and
    cost should be left unrecorded ON PURPOSE. This premise REPLACES a trigger; it does not LOWER a
    threshold, and it must not be cited in support of doing so. SEQUENCING CONDITION, from 15b's
    SYSTEMIC-RISK-FLAG of 2026-08-13 and binding: this premise must NOT be implemented before a
    retrieval trigger exists for the DECISION register (the condition PRESUMPTION-781 diagnoses and
    REVISE-323 carries). Absent one, applying it adds records to the population of unread registers
    the sibling item is about, and the sibling item's condition is graded Critical.
  Supporting evidence (15a, SUPPORTED/Moderate-to-Strong as filed; DISCOUNTED TO MODERATE HERE — see
    Confidence): Jansen, A. & Bosch, J. (2005), "Software Architecture as a Set of Architectural
    Design Decisions," WICSA 5 [canonical; not re-verified at source]; the architectural-knowledge-
    vaporization literature (Capilla, Babar, Pautasso and successors) [located records verified as
    existing; claims from abstracts]; Nygard, M. (2011), "Documenting Architecture Decisions"
    [canonical practitioner reference]; Amazon shareholder-letter one-way/two-way-door framing
    [widely reproduced; 15b notes it did not appear in retrieved sources and used it descriptively].
    Google Cloud Architecture Center, "Architecture decision records overview" [VERIFIED by 15b, and
    it is the source that states the four trigger criteria directly — the strongest verified source
    for this premise comes from the AGAINST file].
  Challenges noted (15b, PARTIALLY-CHALLENGED/Moderate — and it agrees with the diagnosis): "no
    mainstream ADR guidance uses implementation cost as its trigger, so if C2A2 is using 'did we build
    a new tool' as its threshold, it is using a proxy the field abandoned." Its two live objections
    are folded in above: the exclusion of threshold-lowering (consolidated practitioner exclusion
    criteria; Ancker et al. 2017 as the measured analogue of documentation fatigue) and the
    observation that the item argues from an absence and an elapsed-day count rather than from the
    reversibility of the tabs — which is why the instance question is left open below.
  Confidence: Moderate, and the discount is stated rather than absorbed. 15a's single most on-point
    source — arXiv:2604.05835, which names this exact anti-pattern as the "undocumented architectural
    experiment" — is a 2026 preprint known only through a search snippet and WAS NOT RETRIEVED. It is
    discounted here and the premise does not rest on it. What survives is a canonical definitional
    reframing not re-verified this run, plus verified practitioner guidance stating the criteria
    directly, plus agreement from the challenging direction. That is Moderate, not Strong.
  Applicable to: the DECISION register and whatever governs entry to it; any change that creates a
    dependency another agent will consume; the three tier-1 tabs added on day thirty-eight; 14b's own
    threshold for grading a change as an architectural commitment. Same shape of argument as
    PREMISE-073 (impact-tiered rather than effort-tiered gating for autonomous action) in a different
    domain; this is the documentation analogue, and PREMISE-073 is the nearest neighbour in the
    register.
  OPEN MEASUREMENT NAMED AT VALIDATION, and it is the instance question this premise deliberately
    does NOT settle: state what would break if the three T1 tabs were removed. Nothing that cannot be
    repaired in one session -> they were correctly undocumented under this premise's own criterion and
    PRESUMPTION-784 is mis-scoped on the instance while correct on the criterion. Another agent's
    output now depends on them -> the threshold was crossed at the moment that dependency formed, and
    the useful measurement is WHEN, which localises the failure to a run rather than to a policy. Run
    the same test on the last twenty changes that produced no DECISION; that fraction is the real size
    of the gap and is almost certainly far smaller than "every change requiring no new tooling."
  Re-check due: 2026-09-13 (Monthly — monthly rather than quarterly because the sequencing condition
    above depends on the unresolved state of REVISE-323)
  Status: ACTIVE

PREMISE-158:
  Date validated: 2026-08-13
  Source item: PRESUMPTION-786
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Statement: AN INSTRUMENT'S ERROR PROFILE IS TWO-SIDED, IS A DESIGNED AND DECLARABLE PROPERTY, AND
    MUST BE MEASURED ONCE AND STORED — AND NO SINGLE-SIDED FIGURE MAY BE REPORTED. Three clauses.
    (1) TWO-SIDEDNESS IS CONSTITUTIVE, NOT A DEFECT OF IMMATURE TOOLS. Every practical analyser makes
    deliberate unsound choices, trading soundness for automation and precision; a detector is a CURVE
    in error space, not a point, so a change that reduces one error type without altering
    discriminability has relocated the operating point rather than improved detection. It follows that
    a favourable reading after a directional fix is exactly what one would expect WHETHER OR NOT the
    instrument improved. (2) THE SIGN IS DECLARABLE AT CONSTRUCTION AND MEASURABLE ONCE. The
    professional standard is to DECLARE the soundness posture — a sound core plus enumerated
    deliberate under-approximations — and directional bias measured empirically is large and STABLE
    PER TOOL, which makes it a durable property to record, not a fresh unknown at each reading.
    (3) THEREFORE every instrument carries a stored two-sided profile — what it is designed to miss,
    what it is designed to over-report, and a measured estimate of each — and every reported figure
    is accompanied by the relevant side of it. A defect count without its companion false-positive or
    coverage estimate is the reportable defect. After any DIRECTIONAL remedy, re-check the OPPOSITE
    direction on the instrument that was changed; this is cheap because it is scoped to instruments
    just touched. EXPLICITLY NOT INCORPORATED, positively refuted by 15b and excluded as a scope
    guard: "a favourable metric movement is uninterpretable without RE-DERIVING the instrument." That
    is the expensive form of a cheap requirement, is unaffordable at this register's cadence, and its
    predicted outcome is either that it is ignored — producing a documented control that is not
    performed, PREMISE-110 again — or that unfavourable results are kept while favourable ones are
    discounted, an asymmetry worse than the original problem. ALSO NOT INCORPORATED: that the two
    error directions are symmetric IN COST. Fail-safe design deliberately biases toward one direction
    because the loss function is asymmetric, and PREMISE-110 was validated on exactly that reasoning.
    A directional remedy chosen with a STATED loss function and a MEASURED effect on both error rates
    is good practice; what this premise forbids is a directional remedy with neither recorded.
  Supporting evidence (15a, SUPPORTED/Strong): Livshits, B. et al. (2015), "In Defense of Soundiness:
    A Manifesto," CACM 58(2):44-46 [VERIFIED this run — CACM record and author PDF; cited by BOTH
    directions and it is the hinge on which they converge]. Green & Swets (1966), Signal Detection
    Theory and Psychophysics, and standard ROC/DET treatment [canonical; DET treatment verified via
    scikit-learn documentation]. Metrology: JCGM 100:2008 (GUM) and VIM definitions of bias and drift
    — without an external reference neither the magnitude nor the SIGN of an instrument's bias is
    determinable. Cristian, F. (1991), CACM 34(2) [already register-held under PREMISE-141 —
    NON-INDEPENDENT]. Mutation-based soundness evaluation (Ayewah et al. 2007/2008; arXiv:1806.09761,
    arXiv:2102.06829) — the only executable route to measuring the fail-open side is to SEED defects
    and count misses, which is the mechanism PREMISE-124 already requires for population estimates.
  Challenges noted (15b, CHALLENGED/Moderate-to-Strong — THE STRONGEST CHALLENGE IN THIS BATCH, and
    clauses (2) and (3) above ARE that challenge rather than a concession to it): error direction is a
    designed property readable a priori from soundness posture (Livshits et al.); deliberate
    unsoundness has been enumerated and experimentally quantified in a shipping analyser (Christakis,
    Müller & Wüstholz, VMCAI 2015 [author attribution from snippet; chapter and venue verified]);
    measured precision is large and stable per tool (arXiv:2101.08832, 18%-86% across six tools,
    inter-tool agreement under 10% [author list unconfirmed]); enterprise tools commonly and openly
    prioritise recall over precision. 15b's reading of the originating observation is accepted: four
    gates failing OPEN and four extractors failing CLOSED is what design intent predicts, and is
    confirmation rather than surprise. What survives 15b's challenge, and it is what 15a actually
    claimed, is that C2A2 has recorded NEITHER a declared posture NOR a second-direction measurement
    for any instrument — so the direction is unknown HERE for want of a profile, not unknowable in
    principle.
  REFLEXIVE APPLICATION, and it is not optional: this register's own detector premises are
    SINGLE-POLARITY. PREMISE-110 treats the fail-open direction; PREMISE-150 treats missed defects and
    therefore coverage. Under this premise each needs a two-sided companion, and the register
    currently exhibits the asymmetry the item names. This is recorded as a consequence at validation
    rather than deferred: neither premise is amended here, and neither is contradicted — 158 adds a
    requirement they do not meet rather than denying what they assert.
  Confidence: Moderate. The convergent narrowed form is well supported from three mature disciplines
    and both directions cite the same hinge source, but ROC methodology presupposes labelled ground
    truth that C2A2 does not have for any defect class, which leaves seeding as the only executable
    measurement route and makes clause (3) a real cost rather than a free one. Two of 15b's empirical
    citations carry unconfirmed author lists.
  Applicable to: every check, gate, extractor and detector in the pipeline; the four checks found
    failing open on 08-11 and the four extractors found failing closed on 08-12; PREMISE-110 and
    PREMISE-150 reflexively; any future report of a defect count, pass rate or fidelity score.
  OPEN MEASUREMENT NAMED AT VALIDATION: for the instruments adjusted on 08-11, measure the
    opposite-direction error rate before and after the remedy. If tightening the gates raised the
    fail-closed rate in the extractors, the finding is more specific and more serious than the item
    claims — a COUPLING between directional remedies — and is worth pursuing on its own terms. Note
    per PREMISE-140/777 that the counts "four" and "four" are unmarked agent self-reports; nothing
    above depends on the numbers, only on the opposite polarity of the two findings.
  Re-check due: 2026-09-13 (Monthly)
  Status: ACTIVE

  Consistency check performed against this register for all five: NO CONTRADICTIONS FOUND. ONE TENSION
    surfaced (PREMISE-154 vs PREMISE-049 on expiry-vs-trigger, recorded in 154 and not reconciled
    here). THREE OVERLAP-CHECK FAILURES BY 14b ADJUDICATED RATHER THAN REPEATED: (i) PRESUMPTION-783's
    "NONE — the string 'restraint' does not occur" is a string match against the queue's vocabulary
    rather than the register's; PREMISE-133 holds the claim under "abstention", verified at source
    this run, and 783 is therefore NOT MINTED and goes to REVISE-324 as an enforcement gap.
    (ii) PRESUMPTION-779's "NONE found" is wrong — PREMISE-133, 049, 126 and 144(4) all hold it,
    verified this run; PREMISE-133's own Applicable-to note names the queue cohort and declines to
    license it, which is why 154 is written as a SCOPE-EXTENSION and not as a new claim.
    (iii) PRESUMPTION-782's "NONE found" is too strong — PREMISE-096, 080, 004 and 141(2) all hold
    independence, verified this run, but every one of them concerns shared METHOD; 156 mints only the
    shared-INPUT distinction. 14b's overlap check for PRESUMPTION-784 was verified and is CORRECT.
    Five of nine items minted; four did not, and two of those four (781, 783) did not because the
    register already holds them and the gap is enforcement rather than knowledge.
  SYSTEMIC-RISK-FLAG (High, 15b, 2026-08-13) ADDRESSED IN EVERY DISPOSITION, not deferred: six of the
    nine items each pointed toward a new UNIVERSAL MANDATORY CONTROL, and four independent literatures
    find universal controls degrade with volume while trigger-bound selective ones work. The flag is
    accepted in full and its recommendation (1) is implemented by construction — no premise above
    mandates a universal control, 154 is trigger-bound rather than clock-bound, 155 converts an alert
    into a display, 156 removes downstream checks, 157 replaces a trigger without lowering a
    threshold, and 158 replaces per-reading re-derivation with a one-time stored profile. The flag's
    named internal contradiction — that 784's remedy worsens 781's diagnosed condition — is handled by
    the binding sequencing condition inside PREMISE-157. The flag's recommendation (3), instrument
    every control that is adopted, is NOT satisfied by anything above and is carried at REVISE-323.
  Dispositions: DISPOSITION-681..689 (lit_search_returns.md, 2026-08-13 run section)
  MONITOR items: MONITOR-522..523 · REVISE items: REVISE-323..324
--------------------------------------------------------------------------------

================================================================================
## 2026-08-14 — Agent 15c dispositions, 14b intake of 2026-08-13 (PRESUMPTION-787..797)
Seven INCORPORATE (PREMISE-159..165), one MONITOR (MONITOR-524), three REVISE (REVISE-325..327).
Every premise below is minted NARROW, after both directions were read and after the pre-existing
register coverage named by 15a's register checks was subtracted. Per PREMISE-138 and PREMISE-157,
items whose content is already held were NOT re-minted; two of the eleven (791, 796) are routed as
non-application / unargued-exemption findings rather than as knowledge.
--------------------------------------------------------------------------------

PREMISE-159:
  Date validated: 2026-08-14
  Source item: PRESUMPTION-787
  Statement: A repeated identical instrument reading obliges a LIVENESS TEST OF THE READER before any
    conclusion is drawn about the SUBJECT. The distinguishability of "stable world" from "stuck
    instrument" is NOT unreachable — it is a solved, standardised and cheap engineering problem — but
    it is unreachable from INSIDE the channel, so the obligation is to run a known-answer case on the
    same path as the real reading, not to reason harder about the reading.
  Item type: PRESUMPTION (unstated — surfaced by inference; extra weight, designers were unaware)
  Supporting evidence (15a): EEMUA 191 (Ed. 4, 2024) / ISA 18.2 — a STANDING alarm, whose condition
    persists, "fails the criteria of being an alarm" and is counted separately from the live alarm
    population. Every located method for separating stable subject from stuck instrument requires
    information from outside the channel (correlated second sensor, derivative test, counter).
  Challenges noted (15b): CHALLENGED, Moderate-to-Strong — and the challenge is what NARROWS this
    premise rather than what defeats it. NFPA 72 circuit supervision (trouble signal categorically
    distinct from both alarm and quiescent no-alarm), the Prometheus Watchdog / dead-man's-switch and
    `absent()` patterns, synthetic canary probes, and injected freshness heartbeats [all verified by
    15b this run] establish that the inference IS reachable given a supervisory control. 15b's stated
    risk of adopting 14b's claim at full strength — that no unchanged reading could ever be acted on,
    making a legitimately-held queue permanently unresolvable — is accepted, and is why this premise
    imposes a TEST rather than a prohibition.
  Confidence: Moderate
  Applicable to: any run that concludes "no work" / "no change" / "exhausted" from a queue, register or
    detector read; the review-queue readers specifically; Agents 15d and 16.
  SCOPE LIMITS, binding: (a) This is a SCOPE-EXTENSION of PREMISE-140 (streak framings barred) and
    PREMISE-154 (the eleven-consecutive-run hold cohort), which 15a's register check found already hold
    most of the item's content; 159 adds only the instrument-directed obligation. (b) The starvation /
    aging line in 14b's search direction SCOPES ITSELF OUT — PREMISE-119 records the review channel's
    service rate as ZERO, which is blockage, not starvation. Aging must NOT be recommended here.
    (c) 15a's sources for sensor self-diagnostics are patent- and trade-grade; the standards line is the
    load-bearing one.
  Re-check due: 2026-09-14 (Monthly — instrument-directed premises are re-checked monthly per 15d)
  Status: ACTIVE

PREMISE-160:
  Date validated: 2026-08-14
  Source item: PRESUMPTION-789
  Statement: A named defect explanation is discharged by ONE DISCONFIRMING CASE — an instance the
    explanation predicts should PASS — and by nothing else. Confirming only on cases the explanation
    already predicts raises the posterior by construction and is not testing. The failure is ASYMMETRIC
    CASE SELECTION, not stopped testing; both directions agree that "stop testing" is a decision with a
    computable threshold and is defensible, while asymmetric selection is licensed by no framework.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): Graber, Franklin & Gordon (2005), "Diagnostic Error in Internal Medicine,"
    Arch Intern Med 165(13):1493-1499 — 100 cases, cognitive factors in 74%, PREMATURE CLOSURE the
    single most common cognitive cause. SEARCH SATISFICING and DIAGNOSIS MOMENTUM (a label passed
    between actors hardening into fact without re-test) name the multi-run form and have no register
    antecedent. Çalıklı & Bener (PPIG 2010) carry it into software: confirmation bias in debugging
    leads programmers to MISIDENTIFY the reasons for failure, and individual experience does not reduce
    it.
  Challenges noted (15b): PARTIALLY-CHALLENGED, Moderate — Pauker & Kassirer (1980), NEJM
    302(20):1109-1117: above the test-treatment threshold further testing has NEGATIVE expected value,
    and a single high-prior cause covering a universal symptom is exactly the case the threshold model
    says to act on. This is accepted and is why 160 requires ONE case rather than a testing regime.
    15b's second challenge is CARRIED AS A BINDING PROHIBITION: Norman et al. (2017), Academic Medicine
    92(1):23-30 — bias-based accounts of diagnostic error are weakly supported and bias-RECOGNITION
    interventions have NO measured effect. Remediating this item by asking runs to "be more careful" or
    "consider alternatives" is therefore contraindicated by the strongest available synthesis.
  Confidence: High (on the narrow claim as stated; the mechanism is agreed by both directions)
  Applicable to: any run adopting a standing explanation for an anomalous reading; the cold-cache
    `fidelity: fail` account specifically; all fault-attribution in the metabolism and heartbeat lanes.
  CAVEATS, binding: (a) PREMISE-069 is the register's own COUNTER-INSTANCE — a system-wide anomaly in
    this very system WAS correctly attributed to a benign read-path artifact. The cold-cache account
    may simply be TRUE; 160 concerns WARRANT, not truth, and must not be cited as evidence against the
    account. (b) PREMISE-107's cost guard binds: the supported remedy is one discriminating test, not
    re-testing every case. (c) PREMISE-152 applies: six homogeneous runs concurring is weak evidence in
    BOTH directions. (d) 15b declares that the prior on the cold-cache account was ASSUMED high and not
    independently checked, and that the engineering/process-control confirmation-bias literature was not
    searched — the clinical-to-software transfer underpinning its lead sources is assumed, not shown.
  NAMED TEST, one command: re-run one failing fixture with a WARM cache. If it still fails, the account
    is refuted; if it passes, the account is discharged. Either outcome closes the item.
  Re-check due: 2026-11-14 (Quarterly)
  Status: ACTIVE

PREMISE-161:
  Date validated: 2026-08-14
  Source item: PRESUMPTION-790
  Statement: An UNARBITRATED disagreement between measurements of the same nominal quantity must be
    RECORDED AS A FINDING, and a decision taken across such a disagreement without a stated measurand
    and a stated uncertainty is UNDECIDABLE, not conservative. Where the disagreement spans a decision
    threshold, the conformity zone is reduced by the measurement uncertainty and no decision may be
    taken inside the resulting guard band.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): ISO 14253-1:2017, decision rules for verifying conformity — tolerance
    REDUCED by measurement uncertainty when proving conformity and EXPANDED when proving
    non-conformity, leaving an explicit zone in which NO conformity decision may be taken. Deming (no
    true value of a quantity defined by a procedure); Bland-Altman (the deliverable of a method
    comparison is the SPREAD, not a winner); Gauge R&R (quantifying the measurement system's own
    variation is a PRECONDITION of interpreting any reading against a tolerance); Dong, Berti-Équille &
    Srivastava (2009) — agreement among readings from runs sharing a codebase measures COPYING, not
    truth.
  Challenges noted (15b): PARTIALLY-CHALLENGED, Moderate-to-Strong on the general claim and WEAK on the
    decision case. JCGM VIM3/GUM measurand semantics and definitional uncertainty [verified this run],
    with `df`/`du` vendor documentation and AWS SQS `Approximate*` metric semantics as direct
    counterexamples on the exact measurands at issue: these instruments measure DIFFERENT THINGS by
    construction (deleted-but-open handles, sparse files, apparent vs allocated blocks; sampled and
    eventually-consistent queue counts). The system's conclusion was therefore probably RIGHT — but
    reached without entitlement, since no run stated a measurand, none stated an uncertainty, and none
    applied the compatibility criterion. Both directions agree on that gap, and 161 mints only it.
  Confidence: Moderate
  Applicable to: all corpus-level and capacity figures reported to the human; the 4.65 GB against
    3.2 GB free comparison specifically; the DB sizing and queue-count instruments.
  SCOPE LIMITS, binding: (a) This is an INSTANCE of PREMISE-114 (incommensurability, limits of
    agreement, the definitional exit) plus PREMISE-145 (which number reached the human), which 15a
    identifies as the heaviest register overlap in the batch. 161 carves out only the two things 114
    does not hold: the RECORDING obligation for an unarbitrated disagreement, and the guard-band rule.
    (b) 114's definitional exit is conditioned on a quantity DETERMINISTIC OVER A FROZEN SNAPSHOT; a
    live growing database is not, so four differing DB sizings may ALL be correct and forcing them to
    one definition would destroy information.
  OPEN VERIFICATION, must be discharged before use elsewhere: 15b concludes that CAPTURE-RECAPTURE DOES
    NOT APPLY to `df`/`du`-type instruments — deterministic functions of different definitions, not
    independent detectors of a hidden population — and that an estimator would manufacture uncertainty
    out of a definitional difference. 15b marks this inference AS ITS OWN AND NOT LITERATURE-VERIFIED,
    the least-supported claim in its batch. It bears directly on the Axis-2 estimator recommendation in
    SYSTEMIC-RISK-FLAG_2026-08-13 and MUST be checked before that recommendation is applied here or
    withdrawn. 161 does not depend on it.
  CROSS-ITEM LEAD, from 15b's 797 file: check whether the four DB sizings and seven queue counts were
    taken at DIFFERENT TIMES OF DAY. If so the disagreement may be TEMPORAL rather than instrumental
    and this premise's remedy changes to the as-of stamp of PREMISE-165.
  Re-check due: 2026-11-14 (Quarterly)
  Status: ACTIVE

PREMISE-162:
  Date validated: 2026-08-14
  Source item: PRESUMPTION-792
  Statement: A defect count produced by a run auditing its OWN instrument is a CATCH COUNT WITH NO
    DENOMINATOR. Residual-defect estimation requires either two independent detection streams or
    deliberately SEEDED defects; capture-recapture — the estimator named in the item's own search
    direction — requires at least two independent inspectors BY CONSTRUCTION, because the estimate
    derives from their overlap, and therefore cannot be applied to a self-audit at all. Self-audited
    instruments are not merely untested but UNMEASURABLE FROM INSIDE.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): Petersson, Thelin, Runeson & Wohlin (2004), "Capture-recapture in software
    inspections after 10 years research," JSS 72(2):249-264. Fagan's method separates author from
    reader by construction. Porter, Votta & Basili: detection value lives in MULTIPLE INDEPENDENT
    INDIVIDUAL PREPARATIONS, not in meetings; checklists do not substitute for a second reader.
  Challenges noted (15b): PARTIALLY-CHALLENGED, Weak-to-Moderate — the WEAKEST challenge in its batch
    and stated as such. 15b reports "no evidence that self-audit is adequate" as a searched-and-empty
    result, and challenges only the assumed REMEDY: Votta (1993) / Porter & Votta (1998) find nominal
    teams outperform real teams, meeting losses exceed gains, and ~90% of defects are found in
    individual preparation, so mandating an independent MEETING buys the least productive stage
    (~10% of yield, ~30% of interval cost). 15b independently derived the same structural obstacle as
    15a — arriving at it from the estimator's assumptions — which is the strongest fact about this item.
  Confidence: Moderate — and the SCOPE OF THIS PREMISE IS THE STRUCTURAL CLAIM ONLY.
  NOT INCORPORATED, stated explicitly rather than absorbed: the QUANTITATIVE half of the item is NOT
    validated here. (a) No single-inspector detection rate may be quoted from either file — 15a hit a
    widely repeated "20-40%" and a competing "~90%" attributed to Votta and did NOT resolve them.
    (b) The CONVERGENCE-OR-PLATEAU sub-question is unresolved, and 15a reports this as a SEARCH FAILURE
    rather than a literature gap, deliberately withholding a NOVELTY-FLAG on it (the error recorded
    against 15a at PREMISE-153). Targeted follow-up: software reliability growth models (Musa,
    Goel-Okumoto) and reinspection studies. (c) 15b states this item should NOT be closed on its search
    alone; the most relevant corpus — author-based review / desk checking / developer-testing
    effectiveness — was not reached by either direction.
  NEGATIVE FINDING, carried because omitting it would be cherry-picking: the intuitive "authors are
    blind to their own errors" mechanism has recently FAILED a registered replication (Burgoyne et al.,
    "Revisiting the self-generation effect in proofreading") and MUST NOT be cited in support of this
    premise. The case rests on ESTIMABILITY, not on authorial blindness.
  Applicable to: every corpus-level number this project publishes; the extractor specifically; Agents
    14a/14b self-audit; the register checks performed by 15a and 15b including those in this batch.
  Related: PREMISE-148 (data extraction: 28.3-31.2% error, FLAT across experience levels, structural
    duplication as the demonstrated control) already holds the quantitative result in the neighbouring
    domain and is the better basis for any numeric claim. PREMISE-124 (uncalibrated without an external
    baseline). PREMISE-144 (self-exempting layers fail in ways visible only from outside) — 162 is that
    claim reappearing as an ARITHMETIC obstacle rather than a structural one.
  CHEAPEST REMEDY, both directions converge: SEEDED DEFECTS — the only residual-defect estimator that
    works with a single auditor. Second choice, one independent reader working ALONE (not in a meeting),
    whose overlap with the self-audit would produce this project's first capture-recapture estimate.
  Re-check due: 2026-09-14 (Monthly — the quantitative half is expected to move)
  Status: ACTIVE

PREMISE-163:
  Date validated: 2026-08-14
  Source item: PRESUMPTION-793
  Statement: Production-completion is not lifecycle-completion. A producer may be retired only through
    a HANDOVER GATE THAT NAMES A SUCCESSOR OWNER for the open defect classes in its output; the
    producer's continued existence is NOT the control, and requiring it would install the zombie-project
    failure mode as policy.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): Avelino, Constantinou, Valente & Serebrenik (2019), "On the abandonment and
    survival of open source projects," ESEM 2019 (arXiv:1906.08058) — 1,932 popular GitHub projects,
    315 (16%) abandoned after loss of core developers, only 128 of those 315 (41%) survived by
    acquiring new core maintainers. THE LOAD-BEARING NUMBER IS ITS COMPLEMENT: 59% of abandoned popular
    projects never found a new owner. [PDF retrieved and read this run — one of only two sources 15a
    verified directly across five items.] Lehman's laws; sustainment practice treats
    transition-to-sustainment as a planned handover to a NAMED receiving owner.
  Challenges noted (15b): PARTIALLY-CHALLENGED, Moderate — and it supplies the LEVER this premise is
    written around. Beyer et al. (2016), Site Reliability Engineering, Production Readiness Review
    [verified this run]: ownership of a running artefact transfers through an explicit gate with a
    named successor, not through the producer's survival. Staw (1976) / Keil et al. meta-analysis: the
    documented organisational bias is OVER-continuation, not premature termination. Boundary condition
    accepted: Lehman's Continuing Change and Declining Quality are stated for E-TYPE systems tracking a
    moving domain, and a corpus generated once against a fixed 308-item spec may not qualify, so the
    maintenance tail is NOT automatic.
  Confidence: Moderate
  Applicable to: the OpenStory producer and its retirement recommendation; any scheduled task
    recommending its own retirement; the deferred/ and inbox/ lanes.
  SURVIVING FACTS, untouched by either direction: 307 against a spec of 308 is an INCOMPLETENESS, not a
    completion; and four open-and-growing defect classes are a live finding regardless of ownership.
  CAVEATS: (a) maintenance-share figures (67-90%) are secondary/industry material and their spread is
    itself a warning — transfer the order of magnitude, no number. (b) Domain transfer from software to
    a generated wiki corpus is an ARGUMENT, not a measurement. (c) The item's force depends on the
    corpus having downstream consumers, which neither direction established and which is measurable
    in-house. (d) 15b declares 793 the thinnest of its five — the orphaned-project defect-trajectory
    literature, the likeliest place to find evidence FOR 14b, was not reached.
  Related: PREMISE-026 (unowned work is an accountability defect), PREMISE-118 (a named defect triggers
    a retrospective obligation — which retirement without a successor would ORPHAN), PREMISE-143.3 (an
    instrument-defect record is not closable by the run that filed it).
  Re-check due: 2026-11-14 (Quarterly)
  Status: ACTIVE

PREMISE-164:
  Date validated: 2026-08-14
  Source item: PRESUMPTION-795
  Statement: The durability of a declared method substitution is a property of its ADDRESSING, not of
    its medium or its prominence: a record is durable only if it is written to a location the NEXT
    EXECUTOR'S OWN PROCEDURE REQUIRES IT TO READ. "Declare it more prominently" is therefore the WRONG
    REMEDY SHAPE for an addressing failure, and so is building a register with no scheduled reader.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): the lessons-learned literature is unambiguous that RECORDING was never the
    binding constraint, and its diagnostic sign is exactly 14b's — the same issue recurring despite
    being documented. Sculley et al. (2015), "Hidden Technical Debt in Machine Learning Systems,"
    NIPS 28, for the mirror concept of UNDECLARED CONSUMERS [NeurIPS record retrieved and read this run].
  Challenges noted (15b): PARTIALLY-CHALLENGED, Moderate — and it CONVERGES with 15a on the diagnosis
    from the opposite direction, which is the strongest fact about this item. NTSB: 12,480+ NARRATIVE
    recommendations since 1967 with a self-reported acceptance rate above 82% — prose is demonstrably
    durable at scale, so MEDIUM IS NOT THE VARIABLE; addressee, obligation and read path are. Bounded
    by GAO-19-686 (35% of aviation recommendations open >10 years not fully implemented absent a
    statutory deadline). ECSA 2024 ADR action-research study: WHERE documentation is stored has a
    massive influence on its usefulness [attribution provisional]. Correction carried: Tucker &
    Edmondson's mechanism is NON-disclosure, and C2A2's runs DID disclose, so the fleet sits on the
    second-order side of their distinction and that citation fits less well than assumed.
  Confidence: Moderate
  Applicable to: every declared method substitution; the four declared on 2026-08-13; the task-file
    layer generally; any proposal to create a new register.
  SCOPE LIMITS, binding: This item is NEARLY FULLY REGISTER-HELD and 164 mints only the addressing
    relocation. Five ACTIVE premises already cover it — PREMISE-151 (repeated disclosure normalises
    rather than resolves), PREMISE-143 (first-order workarounds suppress systemic repair, BUILT ON
    TUCKER & EDMONDSON — the very source the queue named as the search target, which the 08-13 intake
    header's pre-queue grep MISSED), PREMISE-123 (propagation must be engineered), PREMISE-108
    (transmission is not delivery), PREMISE-139 (prose records are claims about intent, not events).
    PREMISE-138 bars re-minting the rest.
  DO NOT CITE THIS PREMISE TO DISCOURAGE DECLARATION. PREMISE-143's sustained steelman applies: C2A2
    runs PATCH AND ANNOUNCE, which is more than the nurses did and is what made these substitutions
    visible at all.
  CHEAPEST REMEDY, requiring no register at all (15b): a substitution declared N times by the same task
    without the task file changing should ESCALATE ON A COUNTER. Three consecutive nights is already an
    actionable trigger and the condition is currently met.
  IN-HOUSE TEST (15a): for each of the four substitutions declared 2026-08-13, does the task file of the
    next scheduled run of that task NAME the file the substitution was written to as a required read?
    Four "no"s confirms the addressing claim in-system and makes the remedy a task-file edit.
  DO NOT PROPAGATE: arXiv:2605.24579 ("WhenLoss"), cited in 15b's 795 file, is UNVERIFIED — title seen
    only in a result listing and the abstract fetch was blocked. It is quarantined here.
  Re-check due: 2026-11-14 (Quarterly)
  Status: ACTIVE

PREMISE-165:
  Date validated: 2026-08-14
  Source item: PRESUMPTION-797
  Statement: A fleet's cron times ARE an unwritten dependency graph. Where a run reads another run's
    output but is triggered by the clock rather than by that run's completion, TEMPORAL COUPLING makes
    the truth of the run's assertion turn on a fact the run never checks and cannot represent — so
    whether a daily assertion is true BY CONSTRUCTION or BY MEASUREMENT is undecidable from the
    assertion. The remedy is to DISSOLVE the implicit edge (trigger on the artefact; declare a freshness
    contract; wait-and-escalate on absence) and, minimally and immediately, to STAMP EVERY ASSERTION
    WITH ITS AS-OF TIME AND THE AS-OF TIME OF ITS NEWEST INPUT.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): Sculley et al. (2015), NIPS 28 — data dependencies costlier than code
    dependencies and lacking the analysers and linkers that make code dependencies tractable;
    undeclared consumers; configuration debt [verified this run]. TEMPORAL COUPLING is a named design
    smell whose defining property is that the required ordering is not expressed in the artefact, which
    is precisely why a run reads its schedule position as an environment fact.
  Challenges noted (15b): PARTIALLY-CHALLENGED, Moderate — AND THE CHALLENGE LANDS ON THE REMEDY, NOT
    THE DIAGNOSIS. 15b found NO literature defending implicit time-encoded dependencies; the field
    treats them as a defect. But the established practice is to DISSOLVE the graph, not RECORD it:
    Airflow asset-aware scheduling (3.x) and Datasets (2.4+), Dagster asset freshness policies,
    reschedule-mode sensors with timeouts and alerting callbacks [all verified this run]. 15b's stated
    risk of the recording remedy is accepted in full and is why 165 does not mandate it: a hand-written
    dependency record is OFF THE EXECUTION PATH by construction, will drift on the first schedule
    change, and is blind to contention-induced staleness — the same hazard class as the register in
    PREMISE-164.
  Confidence: Moderate
  Applicable to: all 27 scheduled tasks; the three same-day cases in which a run's schedule position
    determined what it could truthfully report; the metabolism, heartbeat and review lanes.
  SCOPE LIMITS: (a) PREMISE-045 / PREMISE-046 hold the read-after-write and verify-the-side-effect
    MECHANISM and were not re-searched. (b) PREMISE-053 ALREADY states that scheduling is necessary but
    not sufficient and already prefers event/threshold-triggered regeneration over fixed cadence — the
    08-13 intake header understated this. 165's disjoint contribution is the REPRESENTATIONAL claim
    plus the as-of remedy. (c) PREMISE-053's own caveat applies reflexively: a declared graph that
    drifts out of alignment with the actual schedule reproduces the fault invisibly. (d) What transfers
    is the representational requirement (a field), NOT Airflow's enforcement engine (infrastructure).
  EVIDENTIAL GAP, declared: neither direction located empirical research measuring defect or staleness
    rates across scheduling paradigms. The effectiveness of declared dependencies is PRACTITIONER
    CONSENSUS, not a measured result, and 15b's strongest recommendation (bitemporal / as-of semantics)
    is carried as an UNSOURCED CANONICAL POINTER.
  IN-HOUSE TEST (15a): for each scheduled run, list which other run's output it reads and whether its
    trigger is that run's completion or the clock. Every "clock" entry is a place where a daily
    assertion is true by construction rather than by measurement.
  Re-check due: 2026-11-14 (Quarterly)
  Status: ACTIVE

--------------------------------------------------------------------------------
  15c RUN NOTES, 2026-08-14 (consistency checks and things NOT done)
  CONSISTENCY CHECK against existing premises: performed for all seven. No contradiction found with any
    ACTIVE premise. Four of the seven are written as SCOPE-EXTENSIONS or INSTANCES rather than new
    claims, on 15a's register findings — 159 (of 140+154), 161 (of 114+145), 162 (of 148+124+144),
    164 (of 151+143+123+108+139) — because minting them as free-standing would add records without
    adding rules, which PREMISE-138 and PREMISE-157 both caution against.
  TWO ITEMS DELIBERATELY NOT MINTED, and this is the run's most important routing decision:
    PRESUMPTION-791 is a NON-APPLICATION finding, not a knowledge finding — PREMISE-137 already
    mandates deliberate defect reintroduction verbatim and PREMISE-150 already requires seeded defects
    for adequacy claims. Minting an eighth premise saying it again is the failure mode this register is
    accumulating. Routed to REVISE-325. PRESUMPTION-796's criterion question was answered NOT by 15a
    (which filed a NOVELTY-FLAG on it) but INDEPENDENTLY BY 15b, which located checkable three-axis
    membership criteria in the IIA Standards. The novelty flag is therefore RETIRED, and the item is
    routed to REVISE-327 because what it requires is a determination about an existing artefact, not a
    new premise.
  THE INDEPENDENCE DESIGN PAID OFF, recorded because it is rarely observable: on 796, 15a searched and
    found no discriminating criterion and correctly flagged NOVELTY; 15b, searching the adversarial
    direction and barred from reading 15a, found the criterion in the assurance standards. Neither
    would have reached that state alone. Per PREMISE-111 and MONITOR-486 the independence itself
    remains unadjudicated, so this is offered as an instance, not as evidence of the mechanism.
  RECALL PROBLEM CONFIRMED TWICE MORE (ASSUMPTION-1052, five-of-nine string-grep recall): the 08-13
    pre-queue register check missed Tucker & Edmondson under PREMISE-143 (bearing on 795) and
    PREMISE-086's monitor-of-monitor requirement (bearing directly on 796). Every overlap list above is
    a LOWER BOUND.
  VERIFICATION HONESTY, carried from both directions: across all eleven items, very few sources were
    retrieved and read in full — 15a (793-797) declares exactly TWO. Weakest provenance: 796 (not one
    source read in full; ISO/IEC 17025 and 17011 paywalled), 788 (preprint and vendor grade), 787
    (patents and trade), 792 (industry-survey grade with an unresolved numeric discrepancy). No source
    in any of the twenty-two result files was invented; every one carries an in-line verification
    marker. Per PREMISE-124, nothing above is a calibrated measurement, and per PREMISE-151, saying so
    here does not make it managed.
  Dispositions: DISPOSITION-690..700 (lit_search_returns.md, 2026-08-14 run section)
  MONITOR items: MONITOR-524 · REVISE items: REVISE-325..327
  SYSTEMIC-RISK-FLAGs received: two, both from 15b, filed at
    lit_search_results/against/SYSTEMIC-RISK-FLAG_2026-08-14.md
--------------------------------------------------------------------------------

PREMISE-166:
  Date validated: 2026-08-15
  Source items: ASSUMPTION-1068 (14a) AND PRESUMPTION-799 (14b) — jointly grounded, minted once
  Statement: A MONITOR'S INDEPENDENCE FROM ITS SUBJECT IS A QUANTIFIED, PLACEMENT-DEPENDENT PROPERTY,
    NOT A BINARY ONE. Three clauses, each carried by both search directions: (1) PLACEMENT — a detector
    that shares runtime, scheduler and host with the population it monitors is not a second channel;
    the received signal must terminate at a receiver OUTSIDE the failure domain, which is what makes
    the regress of controls terminate rather than recur, because the external receiver only waits.
    (2) PROGRESS-BINDING — a heartbeat keyed to INVOCATION reports healthy through a stall of a started
    process, which is the fleet's ACTUAL failure mode; the ping must be emitted on the success path,
    bound to work completed, never at entry. A status artefact written at entry is a SELF-KICK proving
    the liveness of the wrong thing. (3) ARITHMETIC — residual common-cause dependence is a NON-ZERO
    FRACTION even for deliberately independent implementations, so the credit any monitor earns is
    BOUNDED and must be stated as a bound rather than claimed as independence.
  Item types: ASSUMPTION (stated) AND PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): dead-man's-switch and meta-monitoring practice (Healthchecks.io, Cronitor
    — detection requires a per-job check registered IN ADVANCE) [Healthchecks.io documentation VERIFIED
    and read this run]; PromLabs "End-to-End Watchdog Alerts" and the kube-prometheus `Watchdog` rule,
    in which meta-monitoring is ASSUMED breakable and the regress terminates at an external service
    alarming on the absence of an always-firing signal [VERIFIED and read this run]; IEC 61508 / 61511
    treating independence as a quantified fraction with a ~40-question assessment checklist.
  Challenges noted (15b): systemd `WatchdogSec` guidance — "if code keeps sending WATCHDOG=1 while it's
    stuck, systemd has nothing to act on"; Koopman "Proper Watchdog Timer Use" and Ganssle "Designing
    Great Watchdog Timers", where the NAMED ANTI-PATTERN is kicking the watchdog regardless of whether
    the work happened and the fix is the supervisor pattern over an independent timer; LOPA/CCPS —
    credit only ONE protection layer where common cause applies, so a same-plane watcher earns no
    credit while retiring the concern; IEC 61508-6 Annex D beta of 0.005-0.05 for programmable
    electronics, concentrated in shared-author SYSTEMATIC faults that no heartbeat detects.
  Confidence: Moderate
  Applicable to: `morning-system-health`; `openstory-agents-telemetry-refresh` and `REFRESH_STATUS.md`;
    the 05:45 launchd agent; every future proposal to add a monitor, watchdog or health check; and the
    reading of PREMISE-110 and PREMISE-086, which this premise narrows rather than replaces.
  SCOPE LIMITS, binding: PREMISE-110 already requires independence and PREMISE-086 has held
    monitor-of-monitor since June. This premise mints ONLY the three clauses above — WHERE the receiver
    sits, WHAT the ping is bound to, and that the credit is a BOUND rather than a property. It is NOT
    new support for "monitors should be independent," which is already held; any future citation of 166
    for that proposition is a re-minting of 110. DECLARED NEGATIVE: 15a searched for and did NOT find
    an empirical failure rate for self-hosted stall detectors, and 15b searched for and did NOT find
    one either — the effectiveness of the remedy is practitioner consensus, not a measured result. The
    only quantity the fleet actually holds is its own 35.5% non-completion rate (39 of 110 runs), which
    bounds same-plane detector coverage at ~64.5% BEFORE correlation is admitted, and less after.
  Re-check cadence: Monthly (15d) — earlier if any monitor is added or moved.
  Consistency check: performed against PREMISE-110, 086, 100, 141(2), 142, 096, 098, 156, 144, 159,
    053, 004. No contradiction found; 166 narrows 110 and 086 and contradicts neither.
  ALSO RECORDED: PRESUMPTION-799's risk grading is DOWNGRADED from Critical to High. Its Critical
    grading rested on the regress of controls being unterminable, and both search directions establish
    that it is terminated routinely and cheaply in ordinary practice. The three observations 14b made
    stand unaltered; only the grading moves.
  Dispositions: DISPOSITION-701, DISPOSITION-707
  PROVENANCE: Origin 14a + 14b · Chain [14a -> 15a, 15b -> 15c] and [14b -> 15a, 15b -> 15c] ·
    Current status: GROUNDED · Status: ACTIVE

PREMISE-167:
  Date validated: 2026-08-15
  Source items: ASSUMPTION-1070 (14a) AND PRESUMPTION-800 (14b) — jointly grounded, minted once
  Statement: AN ESCALATION AND A MEASUREMENT ARE DIFFERENT OBJECTS AND MUST BE STORED AS DIFFERENT
    OBJECTS. Three clauses: (1) REPRESENTATION — an escalation expressed only as a WITHHELD PASS-MARK
    has no representation on disk distinct from staleness, so any later writer re-computing the same
    predicate silently discharges it; an escalation requires a POSITIVE, ADDRESSED, PERSISTENT STATE.
    (2) CONCURRENCY — where two agents may write the same review state, the write must be
    VERSION-CONDITIONAL; the observed event is a textbook lost update, and "neither run cited the
    other" names a MISSING FIELD, not a discipline failure. Discipline cannot fix a blind write.
    (3) SPLIT-THE-OBJECT — a fresh measurement MAY freely supersede a prior measurement; it MUST NOT
    discharge a claim on the addressee's attention, which only the addressee can discharge. Storing
    both facts in one predicate forces a choice between an unfixable defect and an invisible one.
  Item types: ASSUMPTION (stated) AND PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): Berenson et al. (1995), "A Critique of ANSI SQL Isolation Levels" — P4
    Lost Update, where the fix is a version-conditional write rather than discipline; Starmer et al.
    (2014), NEJM 371:1803, the I-PASS handoff bundle with its owner field and receiver read-back;
    ISA-18.2 alarm shelving (attributed, credentialed, time-limited, auto-re-enabling); PagerDuty
    incident semantics, in which acknowledge is not resolve and auto-resolution is opt-in and never the
    default; Cullen on Piper Alpha permit handover.
  Challenges noted (15b): AHRQ *Making Healthcare Safer IV* — SBAR low-certainty and I-PASS
    moderate-certainty for outcomes, with implementations improving PROCESS rather than outcomes, so do
    not over-read the handoff-bundle evidence; incident.io escalation semantics — "you cannot
    acknowledge an alert, only an escalation" — which is where clause (3) comes from; and the decisive
    operational warning, that ESCALATION-AS-LOCK with a human gate dark twelve days converts every
    handed-up defect into an unfixable one. 15b also notes the second run in the observed event
    actually REPAIRED the defect; the live harm is a stale escalation nobody can see. Declared gap:
    aviation handover literature not reached, and no escalation-supersession rule was found in either
    direction.
  Confidence: Moderate
  Applicable to: `needs_review` and every predicate computed over timestamps; the summa reviewer and
    `summa-qc-sweep` contracts; any two agents that may write the same state; the escalate-versus-
    rewrite boundary generally; and the override-rate denominator in ASSUMPTION-1077 / MONITOR-525,
    which stale invisible escalations contaminate.
  SCOPE LIMITS, binding: PREMISE-108 covers the SENDER-TO-RECIPIENT axis (transmission is not
    delivery). This premise covers the THIRD-PARTY-PEER axis, which 108 does not, plus the data-model
    claim that a predicate computed over timestamps CANNOT represent an escalation. CONSISTENCY CHECK
    PERFORMED AND LOAD-BEARING: PREMISE-145 cuts the other way and is honoured in clause (3) — nothing
    here licenses withholding or delaying a fresh measurement, and any reading of 167 that produces a
    monotonic hold set drained only by an absent human is a MISREADING and is barred by 15b's warning.
  Re-check cadence: Monthly (15d).
  Consistency check: performed against PREMISE-108, 145, 138, 131, 133, 154, 119, 123, 164, 009, 050,
    096, 102/106, 114/161. No contradiction found once clause (3) is read as written; PREMISE-145 is
    the binding constraint and is quoted into the premise rather than left to inference.
  Dispositions: DISPOSITION-703, DISPOSITION-708
  PROVENANCE: Origin 14a + 14b · Chain [14a -> 15a, 15b -> 15c] and [14b -> 15a, 15b -> 15c] ·
    Current status: GROUNDED · Status: ACTIVE

PREMISE-168:
  Date validated: 2026-08-15
  Source item: PRESUMPTION-803 (14b)
  Statement: A YIELD FIGURE PUBLISHED WITHOUT ITS DENOMINATOR IS A STATEMENT ABOUT THE PRODUCER, NOT
    ABOUT THE SPACE. Any count of what the fleet produced ("eight proposals filed", "35 cards", "107
    stale halves") must be published WITH the enumerable set it was drawn from and WITH the frame's
    provenance — and must NOT be converted into a coverage percentage, which PREMISE-109 has already
    rejected as an instrument and which the software-engineering evidence independently shows to be a
    weak proxy that degrades once it becomes a target. The correct form is the STRATIFIED STATEMENT the
    fleet already writes when it is being careful — "read-verified by hand on 11 of the 20, grep-only
    on the other 9" — which dominates any single percentage and is already in use.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence (15a): Klees et al. (2018), "Evaluating Fuzz Testing," CCS 2018 — 57,142
    "unique" crashes resolving to 9 real bugs, the canonical demonstration that a producer-side count
    measures the producer; Geddes (1990) and ISA 530 on block samples not being projectable, covering
    the sampling-frame clause.
  Challenges noted (15b): Inozemtseva & Holmes, "Coverage Is Not Strongly Correlated with Test Suite
    Effectiveness," ICSE 2014 [primary PDF verified] — coverage correlates only low-to-moderately with
    effectiveness once suite size is controlled, and stronger coverage forms do not help; a documented
    case of 30% line coverage against 3% mutation coverage; and the Goodhart warning that a published
    coverage target invites filing THIN WORK for every scheduled tradition. 15b's objection is why this
    premise bars the percentage rather than requiring one.
  Confidence: Moderate
  Applicable to: the evening rollup and every "N filed / N cards / N items" figure in it; the metrics
    snapshots; tradition-agent scheduling reports; corpus audit reporting; and the SYSTEMIC-RISK-FLAG
    of 2026-08-15 on frame provenance, of which this premise is the reporting-side half.
  SCOPE LIMITS, binding: the denominator is itself a CHOSEN FRAME — "fifteen traditions" is a fleet
    decision, not a fact about the world — so this premise requires the frame's PROVENANCE to be stated
    alongside it, and does NOT license treating "4 of 15" as a measurement of coverage. Where the frame
    can be sourced outside the audited process (the launchd schedule, the tradition roster), it must
    be. DECLARED CONSTRAINT: PREMISE-109 bars the percentage, this premise bars the bare numerator, and
    no instrument was found that satisfies both — the surviving practice is the stratified statement,
    which is not a metric and cannot be trended.
  Re-check cadence: Quarterly (15d).
  Consistency check: performed against PREMISE-109 (complementary, not contradictory), 105, 124, 150,
    140, 097, 136, 101, 096, 141, 058. No contradiction found.
  Dispositions: DISPOSITION-711
  PROVENANCE: Origin 14b · Chain [14b -> 15a, 15b -> 15c] · Current status: GROUNDED · Status: ACTIVE

  ================================================================================
  2026-08-15 RUN SUMMARY — 15a / 15b / 15c, processing the 2026-08-14 intake
  ================================================================================
  FOURTEEN ITEMS DISPOSITIONED, THREE PREMISES MINTED. Five items were dispositioned INCORPORATE and
    only three premises were written, because ASSUMPTION-1068 and PRESUMPTION-799 are the same finding
    reached from the assumption side and the presumption side, as are ASSUMPTION-1070 and
    PRESUMPTION-800. Minting each separately would have reproduced exactly the duplication 15a flagged
    on PRESUMPTION-806. Recorded because the register's growth rate is itself now an instrument.
  THE INDEPENDENCE DESIGN PAID OFF TWICE, both times on items where it changed the disposition. On
    PRESUMPTION-799, 15a (searching FOR) and 15b (searching AGAINST, barred from 15a's directory)
    independently produced the SAME disjoint increment — independence as a quantified beta rather than
    a binary property — which is the whole of what PREMISE-166 clause (3) mints. On ASSUMPTION-1077,
    15a found the proposal already standardised as ISO 2859-3 skip-lot while 15b found that every named
    precedent fails its own entry conditions; NEITHER would have reached the actual finding alone,
    which is that the acceptance rule is set by the party bearing the risk and the proposal therefore
    CHANGES Tom's job rather than removing it.
  THE PIPELINE CORRECTED ITS OWN PRIOR OUTPUT. 15b established that REVISE-326's stated action —
    "compute the override rate; the cheapest decisive action needs no attendance" — is FALSE AS
    WRITTEN, because interpreting an override rate requires case-by-case adjudication of
    appropriateness. That is filed as REVISE-330, an explicit amendment, rather than folded into the
    MONITOR entry. A pipeline that quietly monitored past a known defect in its own recommendation
    would be doing the thing this register exists to catch.
  ONE PRESUMPTION WAS REFUTED BY ARITHMETIC THE FLEET ALREADY HELD. PRESUMPTION-806 inferred correlated
    failure from a nine-of-twenty-five cluster; 15b applied the fleet's own 35.5% base rate and got
    36.0%. The day is AT base rate. Filed as REVISE-333 so that the misdirected repair is not made.
  RECALL PROBLEM RESTATED (ASSUMPTION-1052, string-grep recall measured at 56% and at five-of-nine on
    successive runs): every register-overlap list in this run's twenty-eight result files is a LOWER
    BOUND, and the same grep was used for the pre-write checks because the replacement instrument
    ASSUMPTION-1052 requires HAS STILL NOT BEEN BUILT.
  VERIFICATION HONESTY, per Rule 12. Across twenty-eight result files, very few sources were retrieved
    and read in full — the 15a searchers declare two (Healthchecks.io documentation, the PromLabs
    watchdog page) plus one primary definition entry (VIM3 2.27) across nine files, and one 15b searcher
    declares that NO SOURCE IN ANY OF ITS FIVE FILES WAS READ IN FULL. Weakest provenance: the
    5% / 10-20% override benchmarks under ASSUMPTION-1077 come from ONE unrefereed practitioner source
    and must never be quoted as results; MIL-STD-1916's prevention orientation is asserted from memory
    and flagged unverified; the IEC 61511 bypass-management literature that probably holds the codified
    answer for ASSUMPTION-1075 was IDENTIFIED AND NOT REACHED. No source in any file was invented and
    every one carries an in-line verification marker. Per PREMISE-124 nothing in this cycle is a
    calibrated measurement, and per PREMISE-151 recording that here does not make it managed.
  Dispositions: DISPOSITION-701..714 (lit_search_returns.md, 2026-08-15 run section)
  MONITOR items: MONITOR-525..527 · REVISE items: REVISE-328..336
  SYSTEMIC-RISK-FLAGs received: two, both from 15b, escalated as REVISE-335 (frame provenance,
    Critical) and REVISE-336 (unidentified numbers / missing null model, High).
--------------------------------------------------------------------------------

################################################################################
# 2026-08-16 — 15c dispositions from the 2026-08-15 14a/14b intake
# Six premises minted (PREMISE-169..174) across seven INCORPORATE items.
# EVERY ONE IS DELIBERATELY NARROW. This cohort was heavily register-held; each
# entry below states explicitly what it adds beyond the premise it sits next to,
# and where it adds nothing the item was NOT incorporated (see MONITOR-528..531).
################################################################################

PREMISE-169:
  Date validated: 2026-08-16
  Source item: ASSUMPTION-1086
  Statement: THE REGISTRY IS THE COVERAGE. A scheduled job that has never started emits nothing —
    no log line, no exit code, no error — so it is invisible BY CONSTRUCTION to every monitor whose
    input is the job's own output. This is not a gap in instrumentation quality; it is a property of
    the signal. It follows that (1) heartbeat and dead-man's-switch designs detect a never-started job
    ONLY for jobs already registered with the receiver, so the registry of what ought to exist is the
    upper bound on coverage and is the artefact that must be independently maintained and audited;
    (2) an absent series is read by monitoring systems as "everything is fine" unless the expected set
    is pre-initialised, which is the same failure in a second domain; and (3) detection latency for
    this fault class is approximately HALF THE AUDIT INTERVAL, and is UNBOUNDED where no audit exists.
    WHAT THIS ADDS beyond PREMISE-166 (minted 2026-08-15 on the same launchd fault), PREMISE-141
    (a run that starts is not a run that reports), PREMISE-086 (alarm on the AGE of the last dated
    result) and PREMISE-110 (monitor/subject independence): those premises govern jobs that RUN and
    fail. This one governs jobs that never begin, and its content is the shift of the load-bearing
    artefact from the monitor to the ENUMERATION. Rebuilding the instrument does not help if the
    instrument asks the same incomplete registry what exists.
  Item type: ASSUMPTION (stated)
  Supporting evidence: PromLabs / J. Volz, "Dealing with Missing Time Series in Prometheus" — an
    absent series makes an alert "silently fail to fire, since Prometheus interprets an empty output
    as 'everything is fine'"; remedy is to pre-initialise the expected set [VERIFIED this run — page
    fetched and read]. Healthchecks.io cron-monitoring documentation — the check must be created
    BEFORE any ping is expected [VERIFIED this run]. SAP `absent-metrics-operator` README —
    hand-maintained absence rules fail through "typo or forgetting"; derive them from the manifest
    [VERIFIED this run]. IEC 61508 proof-test-interval form for the latency result [SNIPPET LEVEL].
  Challenges noted: 15b returned PARTIALLY-CHALLENGED (Moderate) and TWO of its findings are carried
    into this entry rather than outweighed. (a) THE HEADLINE COMPARISON IN THE 2026-08-15 SCHEDULER
    REPORT IS VOID: 78+4+0 = 82 checks against 78+1+5 = 84 checks is two different populations across
    a documented instrument replacement, and PREMISE-105 (a definitional change breaks the series)
    forbids reading a delta across it. The identical OK count is a coincidence, not a control. This is
    recorded as a defect of the source report and is NOT part of the premise. (b) THE REGRESS
    TERMINATES ONLY BY DIFFERING IN KIND — a better monitor of the same kind reproduces the fault,
    which is precisely why this premise names the registry rather than the monitor. 15b's stronger
    reading, that the remedy is therefore misdirected toward monitoring, is ACCEPTED and is the reason
    this premise is worded as an enumeration requirement.
  Declared negative, from BOTH directions independently: no published empirical detection-latency or
    prevalence figure for never-started scheduled jobs was located by either searcher. This reproduces
    PREMISE-166's declared negative of the previous day. The latency form above is analytic, not
    measured; per PREMISE-124 it is not a calibrated quantity.
  Confidence: Moderate
  Applicable to: the launchd/scheduled-task fleet and its health report; `list_scheduled_tasks` and any
    successor enumeration; the c2a2-* pipeline roster; any future monitor whose input is its subject's
    own output. Couples PREMISE-166, 141, 086, 110, 100, 105, 124.
  Re-check due: 2026-09-16
  Status: ACTIVE
--------------------------------------------------------------------------------

PREMISE-170:
  Date validated: 2026-08-16
  Source items: ASSUMPTION-1094 AND PRESUMPTION-811 (ONE premise minted for TWO items — they are the
    same finding approached from the stated and the unstated side, and minting two would have produced
    exactly the register duplication this run's own systemic flag concerns)
  Statement: A DEFECT RECORD IS INSTANCE-SCOPED, AND ITS IDENTIFIER IS AN ADDRESS, NOT A PREDICATE.
    Storing instance-level evidence in identifier-level form asserts a FUNCTIONAL dependency
    (id -> correction) where the evidence supports only a CONDITIONAL one (the correction holds on the
    subset where the body matches). Four clauses. (1) THE STANDARD IS ALREADY INSTANCE-SCOPED BY
    DESIGN: IEEE 1044-2009 and ODC treat defect type as an ANALYSIS ATTRIBUTE carrying no propagation
    authority, so the register is in standard form and needs no type-level tier — and a type-level tier
    would issue a sweep licence to the cheapest available reviewer, which is the failure mode.
    (2) PROPAGATION HAS A LARGE MEASURED ERROR RATE EVEN WHEN ENGINEERED FOR: Getafix, a deployed
    learn-from-past-fixes system, predicts the human-written fix at top-1 only 12-91% of the time by
    category; automated repair validated on its construction evidence is "as likely to break tests as
    to fix them" for programs that pass most tests. Verifying at the body before applying a recorded
    correction is therefore correct practice, not caution. (3) NON-PROPAGATION IS NOT FREE, AND THIS
    IS THE HALF THE ORIGINATING ITEMS DID NOT STATE: 22-33% of bugs require supplementary fixes, and
    roughly half of one year's in-the-wild zero-days were variants of already-patched bugs. Refusal to
    generalise leaves known-defective instances in place and produces a survivorship artefact, because
    verification runs only where the flag points. (4) THE RESOLUTION IS TWO OBJECTS, NOT ONE: the
    instance correction and the EXTENT-OF-CONDITION are separately recorded and separately
    dispositioned, on the nuclear corrective-action pattern. Extent-of-condition is a claim requiring
    its own warrant under PREMISE-135 (population, termination criterion, one severe out-of-sample
    test); it is not inferred from the record's form, and it is not discharged by declining to act.
  Item types: ASSUMPTION (stated) + PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Bader, Scott, Pradel & Chandra (2019), "Getafix: Learning to Fix Bugs
    Automatically," OOPSLA [SNIPPET LEVEL — venue and figures confirmed, paper not read].
    Smith, Barr, Le Goues & Brun (2015), "Is the Cure Worse Than the Disease? Overfitting in Automated
    Program Repair," ESEC/FSE [VERIFIED at abstract and §1]. Park, Kim, Ray & Bae (2012), "An Empirical
    Study of Supplementary Bug Fixes," MSR [SNIPPET LEVEL]. Google Project Zero, in-the-wild 0-day
    variant analysis [SNIPPET LEVEL]. Bettenburg, Premraj, Zimmermann & Kim (2008), "Duplicate Bug
    Reports Considered Harmful… Really?", ICSM [VERIFIED — read in full]: one enumerated cause of
    duplication is literally "multiple failures, one defect," and discarding duplicates loses
    information significant at p<.001 on every dimension — so the supported operation on repeated
    instances is MERGE, not COLLAPSE. Bohannon/Fan et al. on conditional functional dependencies
    [SNIPPET LEVEL]. IEEE 1044-2009 / IBM ODC [SNIPPET LEVEL]. US NRC extent-of-condition guidance
    [SNIPPET LEVEL].
  Challenges noted, and one grade struck: the "six of six" figure from the originating item is NOT a
    precision measurement — the sample was selected, the denominator is undeclared, and there are zero
    recorded propagations to compare against, so six refusals and zero corruptions is an UNIDENTIFIED
    RATE indistinguishable from a blanket no-sweep norm. 15b's steelman is sustained and recorded: six
    catches celebrated as the day's best work is a recovered failure encoded as a success (PREMISE-143
    clause 1). PREMISE-130's third-signature trigger is NOT met — six same-day refusals are one
    signature, not three distinct ones, and PREMISE-143 already declined to lower that threshold.
  Confidence: Moderate-High (clauses 1, 2 and 4 High; clause 3 Moderate — the rates are from other
    domains and per PREMISE-124 are not calibrated to this fleet)
  Applicable to: the band table and every id-keyed defect entry; 14a/14b intake templates; any proposed
    sweep, code-mod or bulk retag (including the standing [MISROUTED-INTERNAL-EMPIRICAL] retag awaiting
    Tom); REVISE-337's parser question. Couples PREMISE-135, 140, 143, 130, 113, 101, 136.
  Re-check due: 2026-09-16
  Status: ACTIVE
--------------------------------------------------------------------------------

PREMISE-171:
  Date validated: 2026-08-16
  Source item: PRESUMPTION-809
  Statement: A DECLARATION REGISTER IS NOT A FAILURE DETECTOR — ITS COMPLETENESS IS ZERO. A register
    that stores what was declared about a thing (loaded, configured, enabled, scheduled) reports on the
    DECLARATION, never on the thing; in Chandra & Toueg's terms it satisfies no completeness property
    whatever, so it is not a weak detector but not a detector at all. The vendor states the specific
    case outright: if the machine is off at the scheduled time, non-calendar launchd and cron jobs are
    SKIPPED and NEVER RUN, silently. THE MINIMAL SUFFICIENT REPAIR IS ONE FIELD, NOT A NEW SUBSYSTEM:
    store an EXPECTED-NEXT-FIRE alongside each declaration and alarm on the age of the gap between
    expected and observed. LOAD-BEARING NEGATIVE, carried from the challenging direction and part of
    this premise: DO NOT ANSWER THIS WITH A HEARTBEAT. Gray failure is defined as the detector
    observing health while the work path is sick, canonically via a heartbeat arriving over a path that
    bypasses the sick path; a heartbeat deployed here would install the failure it was bought to treat.
    The defensible architectures (Kubernetes spec/status, ITSM drift reconciliation, service-discovery
    registered-vs-ready) all KEEP the declaration and alarm on its DIVERGENCE from observation — they
    do not replace declarations with reports, because no perfect failure detector exists and what is
    purchasable is a better declaration, not an escape from declarations.
    WHAT THIS ADDS beyond PREMISE-086 (alarm on AGE of last dated result), PREMISE-100 ("liveness is
    not correctness"), PREMISE-110 (monitor pass-state reachable while subject is dead) and PREMISE-046
    (safety vs liveness): those govern a monitor's output. This governs a REGISTER'S SEMANTICS, gives
    the formal reason (completeness = 0), names the one-field repair, and — the genuinely new clause —
    RULES OUT the obvious remedy on gray-failure grounds.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Apple, "Scheduling Timed Jobs" / Daemons and Services Programming Guide —
    "if the computer is always off at the job's scheduled time, both cron jobs and launchd jobs never
    run" [VERIFIED this run — read in full]. Chandra, T.D. & Toueg, S. (1996), "Unreliable Failure
    Detectors for Reliable Distributed Systems," JACM 43(2):225-267 — completeness and accuracy as the
    defining properties [CANONICAL — not re-verified]. Huang et al. (2017), "Gray Failure: The
    Achilles' Heel of Cloud-Scale Systems," HotOS — differential observability [SNIPPET LEVEL].
    Kubernetes spec/status object model [SNIPPET LEVEL]. Fischer, Lynch & Paterson (1985) for the
    impossibility bound [CANONICAL].
  Challenges noted: 15b's PARTIALLY-CHALLENGED (Moderate) is largely ADOPTED rather than outweighed —
    the anti-heartbeat clause and the keep-the-declaration architecture are 15b's, not 15a's. 15b's
    remaining point is also recorded and is NOT dismissed: `runs = 0` is a defect only against a
    DECLARED expected fire, so the missing artefact really is one field rather than a schema class, and
    the generalisation from launchd to "every register" is broader than the evidence, which is why this
    premise is scoped to registers that are READ AS health signals.
  THE HIGHEST-VALUE OBSERVATION IN THIS COHORT, recorded here and escalated in the run note: PREMISE-086
    was ACTIVE and unenforced on the launchd surface for the entire period three agents sat at
    `runs = 0`. Nothing in this architecture measures PREMISE-TO-INSTRUMENT DIVERGENCE — the count of
    ACTIVE premises with no instrument on the surface they govern. On this evidence that is the highest
    -value unwritten number in the system. It is NOT minted as a premise here (it is a proposal, not a
    finding); it is carried as the discharge condition of MONITOR-528's sibling recommendation and named
    in the run footer.
  Confidence: Moderate-High
  Applicable to: the launchd/scheduled-task register; `list_scheduled_tasks`; any "loaded", "enabled",
    "configured" or "installed" field read as evidence of operation; the heartbeat proposals standing in
    monitor_queue.md. Couples PREMISE-169, 166, 141, 110, 100, 086, 089, 096, 046, 053.
  Re-check due: 2026-09-16
  Status: ACTIVE
--------------------------------------------------------------------------------

PREMISE-172:
  Date validated: 2026-08-16
  Source item: PRESUMPTION-810
  Statement: A PASS MARK IS A VERDICT ABOUT A (READER, FRAME, SCOPE) READING — NOT A PROPERTY OF THE
    FILE. Review is not idempotent across reviewers or across frames, so a mark carries no information
    about what was NOT examined and is therefore not transferable to a later reader with a different
    question. Three professions independently made scope a MANDATORY FIELD OF THE VERDICT rather than
    an optional note: audit practice (ISA 705 (Revised)) compels a MODIFIED opinion where scope is
    limited and a DISCLAIMER where the limitation is pervasive, with no clean-opinion form that
    silently omits what was not covered; systematic review requires the search and inclusion scope to
    be reported with the conclusion; and code-review research measures COVERAGE and PARTICIPATION as
    separate variables, each independently associated with post-release defects (low coverage ~2 extra
    defects, low participation ~5 — so participation OUTRANKS coverage and a coverage field alone takes
    the smaller half).
    EXPLICITLY NOT INCORPORATED — THE REMEDY. A self-reported coverage field is a self-produced artefact
    certifying a self-produced artefact (PREMISE-096) and cannot produce what PREMISE-162 establishes is
    actually needed: capture-recapture requires TWO INDEPENDENT READERS by construction, and a scope
    note creates no second stream. Google's 9-million-change review study records no such field. The
    obligation this premise creates is therefore to STATE THE FRAME, not to assert a coverage
    percentage — which would in any case collide with PREMISE-109 (bars the coverage percentage) and
    PREMISE-168 (bars the bare numerator).
    THE CHEAP PRIOR TEST, owed before any remedy is built: classify the seven defective pass-marked days
    as FRAME-MISMATCH (a different question would have caught it — scope metadata helps) versus
    WITHIN-FRAME MISS (the same question missed it — scope metadata is irrelevant, and inspection yield
    is bounded well below 100% inside a declared frame regardless). No remedy should be specified until
    that split is known, because the two classes have disjoint fixes.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: McIntosh, Kamei, Adams & Hassan (2014), "The Impact of Code Review Coverage and
    Code Review Participation on Software Quality," MSR '14, pp.192-201 [VERIFIED at abstract/record
    level]. ISA 705 (Revised), "Modifications to the Opinion in the Independent Auditor's Report"
    [SNIPPET LEVEL — primary text not reached, and this is the entry's weakest citation]. Petersson et
    al. (2004) via PREMISE-162, on capture-recapture and defect-content estimation [register-held].
    Sadowski et al. (2018), "Modern Code Review: A Case Study at Google," ICSE-SEIP [SNIPPET LEVEL].
    Bannerman on the professional resistance to a mark being read as a property of the examined thing
    [SNIPPET LEVEL].
  Challenges noted: 15b returned PARTIALLY-CHALLENGED (Moderate) and its two substantive points are
    both folded into the statement above rather than outweighed — the self-certification objection and
    the frame-mismatch/within-frame triage. 15b's cost objection (coverage metadata on every approval is
    rarely done and reduces throughput, and PREMISE-121 holds that the review queue degrades
    specifically on LOW-INFORMATION items) is the reason this premise obliges a frame statement rather
    than a metric.
  Confidence: Moderate
  Applicable to: every pass-mark, PASS/FAIL line and review card in the fleet; the 35-plus card review
    queue; the nightly changelog's check-records; 14a/14b's own pass marks over their own output.
    Couples PREMISE-162, 101, 148, 121, 109, 168, 096, 136.
  Re-check due: 2026-09-16
  Status: ACTIVE
--------------------------------------------------------------------------------

PREMISE-173:
  Date validated: 2026-08-16
  Source item: PRESUMPTION-812
  Statement: NAME THE FINAL ELEMENT. Adapted from IEC 61511's acceptance criterion for a safety
    instrumented function: a sensor with no FINAL ELEMENT is not a protection layer. Applied here, a
    proposed remedy that consists only of observing, recording, counting or reporting is NOT a remedy,
    and the acceptance test is a single question answerable in one line — WHAT ACTS ON THE SIGNAL, AND
    WHAT CHANGES WHEN IT FIRES? Two empirical supports make this more than a slogan. (1) In the most
    heavily instrumented detection domain in existence, the LEADING coded contributing factor across 98
    sentinel events with 80 deaths was ALARM SIGNALS INAPPROPRIATELY TURNED OFF (36 events), AHEAD OF
    absent or inadequate alarm systems (30) — detection capacity is not the binding constraint, and
    added detection without a final element degrades the detection that already exists. (2) Remediation
    capacity in the best-measured operational analogue runs at roughly 10% of open items per month
    REGARDLESS OF ENVIRONMENT SIZE, so closure capacity is approximately CONSTANT while detection
    scales — the gap widens by construction.
    SCOPE LIMIT, load-bearing, carried from the challenging direction: THIS PREMISE IS AN ACCEPTANCE
    TEST FOR PROPOSED REMEDIES. IT IS NOT A LICENCE TO BUY CLOSURE CAPACITY. The closure-gap literature
    does not prescribe closure capacity; in the two best-studied gaps the prescribed remedy is
    DETECTION-LAYER SELECTIVITY — filtering, triage, correlation, rule tuning — and the first named
    pathology in the patient-safety incident-reporting literature is OVERREPORTING. Theory of
    Constraints, which the originating argument invokes, sequences IDENTIFY then EXPLOIT before
    ELEVATE. Order of operations here is therefore: measure the detector's PRECISION, apply admission
    control (PREMISE-106 corollary ii), enforce routing (PREMISE-138 clause 2) — and only then discuss
    capacity.
    WHAT THIS ADDS beyond PREMISE-102 (fail-loud is reporting, not remediation) and PREMISE-138 (
    repetition inside a channel with no effector is not a remedy): those state the principle. This
    supplies the one-line ACCEPTANCE TEST that can be applied to a proposal before it is adopted, plus
    the two measured facts that price it. It does NOT re-mint 102; per PREMISE-138 clause (1) a
    re-mint would itself be in-channel repetition.
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: The Joint Commission, Sentinel Event Alert 50 (2013), "Medical device alarm
    safety in hospitals" [VERIFIED this run — read in full]: 85-99% of alarm signals require no
    intervention; the 98-event/80-death coded factor table. IEC 61511 / IEC 61508 safety-instrumented-
    function structure (sensor, logic solver, final element) [SNIPPET LEVEL — standard text not
    reached]. Cyentia Institute, "Prioritization to Prediction" remediation-capacity series [SNIPPET
    LEVEL — vendor-adjacent, quoted as a benchmark not a result]. Macrae, C. (2016), BMJ Qual Saf
    25:71-75, on the pathologies of incident reporting [SNIPPET LEVEL]. SOC alert-fatigue survey
    literature [SNIPPET LEVEL — figures NOT quoted, sources are vendor-derived and flagged unquotable
    in the result files].
  Challenges noted: 15b returned PARTIALLY-CHALLENGED (Moderate) and the entire SCOPE LIMIT paragraph
    above is 15b's, adopted verbatim in substance. 15b's arithmetic objection is also sustained and is
    recorded as a prohibition: the 1,105:78 detection-to-closure ratio quoted by the originating item
    DIVIDES A KNOWLEDGE REGISTER BY A DECISION REGISTER and must not be cited as a ratio. Both
    directions agree the standing defect is an ENFORCEMENT gap on PREMISE-102, not a knowledge gap.
  Confidence: Moderate-High
  Applicable to: every remedy proposed by 14a, 14b, 15a, 15b or 15c from this date; the monitor_queue
    and revision_flags entries themselves; the heartbeat, coverage-field and corpus-rule proposals now
    standing. Couples PREMISE-102, 138, 106, 121, 151, 155, 119.
  Re-check due: 2026-09-16
  Status: ACTIVE
--------------------------------------------------------------------------------

PREMISE-174:
  Date validated: 2026-08-16
  Source item: PRESUMPTION-817
  Statement: A REGISTER WITH EXPANSION AND NO CONTRACTION CANNOT REVISE — IT CAN ONLY ACCUMULATE, AND
    ITS GROWTH CURVE IS THEREFORE NOT A HEALTH SIGNAL. Three clauses. (1) FORMAL GROUNDING: belief
    revision is DEFINED as contraction followed by expansion; a knowledge base that can add but not
    retract cannot perform the operation, and the standard task list requires finding what was DERIVED
    from a withdrawn assumption and deleting it with its dependants. A findings register with no
    representable withdrawn state fails this by construction, and every downstream claim resting on a
    withdrawn finding remains asserted. (2) THE REPORTABLE STATISTIC IS CORRECTION LATENCY, NOT A
    RETRACTION RATE. A retraction or refutation rate is confounded with SCRUTINY — the same
    relationship that makes high-impact journals retract MORE — so it rises when 14a/14b/15a/15b/15c get
    sharper and falls when the pipeline is idle, measuring the auditor under the auditee's name. A
    published rate also creates an incentive to overturn less. Correction latency (time from a finding's
    assertion to its withdrawal) is not confounded in that direction and is the number to publish.
    (3) THE RECORD IS APPEND-ONLY: withdrawal is recorded by SUPERSESSION, never by mutating the prior
    night's entry, because timestamp order is what makes stopping bias auditable (PREMISE-145 clause 5)
    and mutation destroys it. This is also standard append-only/WORM audit-record practice.
    WHAT THIS ADDS beyond PREMISE-143: 143 already holds that a retraction COUNT measures the producing
    layer, and 143 clause (3) already OBLIGES the split into a corrected-output record and an
    instrument-defect record. This premise supplies (i) the formal reason the obligation cannot be met
    by the current schema, (ii) the substitute statistic, and (iii) the append-only constraint. IT IS
    NOT A RE-MINT OF 143 AND MUST NOT BE CITED AS INDEPENDENT CORROBORATION OF IT (PREMISE-120).
  DECLARED, NOT FIXED: PREMISE-143 clause (3) REMAINS UNDISCHARGED. It was minted 2026-08-05 and no
    register in this architecture has a representable withdrawn state for a FINDING as opposed to a
    measurement. This is the second instance in eleven days. Recorded in the run footer as an
    enforcement gap; not closed by this premise, and not closable by the run that filed it (143(3)).
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Supporting evidence: Shapiro, S.C., "Belief Revision and Truth Maintenance Systems: An Overview and a
    Proposal," CSE TR 98-10, SUNY Buffalo [VERIFIED this run — read in full]: "no KBS can guarantee
    that any assertion it contains is true… 'belief' would be a more accurate term than 'knowledge'."
    AGM (Alchourrón, Gärdenfors & Makinson) contraction/expansion/revision [CANONICAL]. Fang, F.C. &
    Casadevall, A., "Retracted Science and the Retraction Index," Infection and Immunity — retraction
    index correlates POSITIVELY with impact factor [SNIPPET LEVEL]. Append-only / WORM audit-record
    practice, SEC 17a-4 and SOX §404 [SNIPPET LEVEL].
  Challenges noted: 15b returned PARTIALLY-CHALLENGED (Moderate) and clauses (2) and (3) above are
    15b's contributions, adopted. 15b's arithmetic objection is sustained and recorded as a
    prohibition: the originating item's two data points enter as 2/2 = 100%, which PREMISE-124 forbids
    quoting. 15b's harm argument against over-hedged operational reporting is accepted as a scope limit —
    this premise obliges a WITHDRAWAL MECHANISM, not hedged prose, and PREMISE-117's publish-then-revise
    standard governs the prose side unchanged.
  Confidence: Moderate-High
  Applicable to: the nightly changelog; assumptions.md, presumptions.md, validated_premises.md,
    monitor_queue.md, revision_flags.md, lit_search_returns.md; the standing REVISE and MONITOR entries
    whose originating findings may later be withdrawn. Couples PREMISE-143, 145, 117, 118, 124, 105, 103.
  Re-check due: 2026-09-16
  Status: ACTIVE
--------------------------------------------------------------------------------

================================================================================
# ===== 2026-08-17 Agent 15c dispositions — 2026-08-16 intake cohort (10 items) =====

**NO PREMISE WAS MINTED BY THIS RUN. PREMISE-175 REMAINS UNALLOCATED.**
Ten items dispositioned: **7 REVISE** (REVISE-341..346) and **3 MONITOR** (MONITOR-532..534);
**0 INCORPORATE**. Every item's core claim was found already held by one or more ACTIVE premises, and
in one case CONTRADICTED by two. Per PREMISE-138(1) and PREMISE-135 no re-mint was made; per the
2026-08-13 precedent (PRESUMPTION-781/783) an ENFORCEMENT gap against a held premise is dispositioned
REVISE, not minted. That zero is not an absence of work — it is this cycle's finding, and it is the
same finding both 15b instances measured independently at 5 of 5 on disjoint sets (10 of 10 across the
cohort): remedies are being drafted before anything reads the register (OPEN-153 / REVISE-340).
Full reasoning: lit_search_returns.md, "## 15c DISPOSITIONS — 2026-08-17", DISPOSITION-729..738.

--------------------------------------------------------------------------------

REGISTER-CONTRADICTION NOTICE — 2026-08-17
  Raised by: Agent 15c at DISPOSITION-738, from PRESUMPTION-827.
  Premises affected: **PREMISE-042** (2026-05-21, ACTIVE, Moderate) and **PREMISE-043** (2026-05-21,
    ACTIVE, **HIGH**). **NEITHER ENTRY IS MUTATED BY THIS NOTICE.** Per PREMISE-174 clause (3) the
    record is append-only and withdrawal is recorded by SUPERSESSION, never by editing a prior entry;
    and per Agent 15c's own definition §5, where a new item CONTRADICTS an ACTIVE premise, BOTH are
    flagged for human review rather than either being overwritten. This notice is that flag. PREMISE-042
    and PREMISE-043 remain ACTIVE and citable until Tom rules; any agent citing either between now and
    the ruling must cite this notice alongside it.
  THE CONTRADICTION, stated once. PREMISE-043 holds at HIGH confidence, anchored on Manning, Raghavan &
    Schutze, that precision-first lexical/string-matching detection in this vault is a **HIGH-PRECISION
    LOWER BOUND** whose known weakness is **RECALL**. PREMISE-042 holds, anchored on Gentner (1983) and
    Hofstadter & Sander (2013), that literal overlap **SYSTEMATICALLY UNDERCOUNTS** genuine convergence,
    because real convergence is analogical. PRESUMPTION-827 asserts the **opposite error profile** — that
    the same instrument MANUFACTURES connections — and was graded **Critical** on that assumption, on one
    unreplicated instance, without citing either premise. Both error modes can coexist in different
    places; what cannot stand is that **neither rate has ever been measured** while two ACTIVE records
    give opposite guidance about one instrument. Per PREMISE-095's own precedent ("CONTRADICTS P-462 as
    held — dispositioned REVISE-195 rather than silently coexisting") this may not be left to coexist
    quietly, and per PREMISE-138 the answer is not a third entry beside them.
  BOTH SEARCH DIRECTIONS INDEPENDENTLY REACHED THE SAME VENUE, which is the strongest signal in the
    cohort. 15a: "Disposition should be a REVISE OF PREMISE-042/043 AT THEIR 2026-08-21 RE-CHECK — not a
    new premise, and NOT a silent coexistence." 15b: "PREMISE-042's quarterly re-check falls on
    2026-08-21 — four days after this search — and is the natural and correct place to reconcile the two
    rather than minting a contradictory item beside them." PREMISE-042's `Re-check due` is **2026-08-21
    (Quarterly)**; PREMISE-043's is 2026-11-21. **The 042 re-check is the designated venue and 043 must
    be pulled into it although its own date has not fallen**, because the HIGH-confidence precision claim
    is 043's, not 042's, and it is 043 that 827 contradicts.
  WHAT MUST BE MEASURED BEFORE EITHER PREMISE IS AMENDED — neither direction supports amending on
    argument alone, and 15c does not either:
    (i) **PRECISION.** Draw 20 of the 103 cross-connections at random; a DECORRELATED instance reads the
        underlying passages in BOTH traditions and grades each substantive / lexical-only / undecidable.
        Twenty with zero lexical-only findings bounds the false-connection rate at roughly 15% by the
        rule of three (Hanley & Lippman-Hand, JAMA 1983 [SNIPPET LEVEL, via 15b]). This is 827's rate.
    (ii) **RECALL.** Take two traditions with a known shared theme, hand-identify convergences by
        reading, and count how many the lexical layer found. This is 042/043's rate.
    PREMISE-168 requires both with denominators; PREMISE-109 bars reporting either as a read-set
    coverage percentage; PREMISE-096 bars the connection layer grading its own output, which is why (i)
    specifies a decorrelated reader.
  THE ASYMMETRIC RISK, recorded because it decides the ORDER of work. PREMISE-042 predicts that a remedy
    which discounts lexical matches will discard the REAL convergences first, since genuine convergence
    here is analogical and already surfaces sparsely. 15b supplies the formal version from Scotus's own
    argument (Ordinatio I d.3 nn.39-40, read this run inside Lyonhart 2024, Religions 15(8):994
    [VERIFIED at substantive-section level]): strip shared vocabulary of evidential force and "there is
    no more reason to conclude that God is formally wise from the notion of wisdom that we perceive in
    creatures than there is to conclude that God is formally a stone." **A network of 103 connections
    with unknown precision is a worse artefact than one of 30 with known precision, and a far better one
    than a network of 4.** Measure first; do not prune on argument.
  WHAT IS NOT IN DISPUTE AND SHOULD NOT BE LOST: the connection schema genuinely carries **no field
    recording whether an agreement is at the level of the words or of the commitments**, and the
    Philippians 2:12-13 case — two thinkers reaching for one verse "with no evidence of contact," filed
    as a convergence — is exactly where a shared citation and a shared commitment come apart. Both
    directions agree the observation is sound. Both also agree the proposed remedy is not: a
    `match_basis` field recorded by the layer that made the match is a self-produced artefact certifying
    a self-produced artefact (PREMISE-096), which PREMISE-172 refused in this exact shape on 2026-08-16
    and PREMISE-109 refused in its coverage form, with the prediction that such a field "would read green
    during exactly the failure it was built to catch." PREMISE-049's existing tagged UNVERIFIED
    quarantine with a revisit forcing function already carries the risk without schema surgery.
  Filed as: **REVISE-346** (revision_flags.md, 2026-08-17). See DISPOSITION-738.
  Status of this notice: **OPEN**, pending Tom's ruling at or after the 2026-08-21 re-check of
    PREMISE-042.
--------------------------------------------------------------------------------

SECONDARY REGISTER FLAG — 2026-08-17 (narrower; same notice discipline, no mutation)
  Raised by: Agent 15c at DISPOSITION-731, from ASSUMPTION-1112.
  Premise affected: **PREMISE-148** (2026-08-06, ACTIVE), **clause (5) only**. **NOT MUTATED.**
  THE ISSUE. PREMISE-148 clause (5) is a load-bearing NARROWING: "secondary sources may be perfectly
    adequate for IDENTITY-LEVEL facts — who, what, which triplet — while unreliable for magnitudes,
    effect claims, qualifications and conclusions... secondary route permitted for identity and
    existence, PRIMARY SOURCING REQUIRED for magnitudes and conclusions." [Quoted from the register
    entry, re-read in place by 15c this run.] ASSUMPTION-1112 is a **counterexample inside that
    safe-harbour**: a real source carrying a wrong DATE. A publication date is an identity-level fact —
    a *when* — and it failed. 15b puts it exactly: "1112 is a failure in the class the register judged
    SAFEST, which is a real finding and I record it as strengthening the item."
  WHAT IS **NOT** ESTABLISHED, and why this is a flag rather than an amendment. The instance is n=1, and
    both directions agree the item's headline claims (that the class is NEW, and that no URL-resolves
    check would have caught it) are false — Walters & Wilder (2023, Scientific Reports 13:14045
    [VERIFIED by 15a at running-prose level]) measured this class at 43% (GPT-3.5) / 24% (GPT-4) of
    NON-FABRICATED citations three years ago, and 15b fetched a live counterexample showing four
    defensible dates on one page (franciscanmedia.org, `published_time` 2023-01-01, `modified_time`
    2026-04-12, body adapted from a 2014 work with a 2024 edition), so "invented" presumes a uniqueness
    that live web sources often lack (PREMISE-101's (scope, method, time) reading).
  THE MEASUREMENT OWED BEFORE 148(5) IS AMENDED: the retrospective metadata sweep. Machine-compare every
    recorded date in `validated_premises.md` and the tradition wikis against Crossref (for DOIs) and
    against declared `published_time`/`modified_time` (for web pages); publish the mismatch rate WITH its
    denominator (PREMISE-168). Near zero and the instance was isolated; near the literature's 24% and
    148(5)'s safe harbour needs withdrawing rather than narrowing.
  PROPOSED NARROWING, for Tom to accept or refuse, NOT applied by this run: identity-level facts are
    adequate from a secondary route for **who** and **what**, and **NOT for when** — dates and other
    numeric bibliographic fields are moved into the primary-sourcing tier, since the measured field
    ranking is roughly 22% date error against under 7% author/title error (Walters & Wilder, as read by
    15a).
  Filed as: **REVISE-342** (revision_flags.md, 2026-08-17). See DISPOSITION-731.
  Status of this notice: **OPEN**, pending Tom's ruling and the metadata sweep.
--------------------------------------------------------------------------------


================================================================================
## Validated premises added 2026-08-18 (Agent 15c, DISPOSITION-739..761)

PREMISE-176:
  Date validated: 2026-08-18
  Source item: ASSUMPTION-1129
  Statement: FOR AN IRREVERSIBLE OPERATION, REVIEW IS NOT A CONTROL; REVERSIBILITY IS. A pass that can
    delete, retire or overwrite must be structurally reversible (quarantine / tombstone / staged
    deletion with a recovery window) BEFORE it is permitted to run, and the reversibility must be a
    property of the mechanism rather than of the reviewer's attention. The finding that founds this: two
    regex-scoped instruments were wrong BY CONSTRUCTION — both bound only the head id after a tradition
    name, so every trailing id in an enumerated citation read as absent — and a false absence is exactly
    the claim a retirement pass acts on.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Wang, Brown, Jennings & Stolee (2020), "An Empirical Study on Regular Expression
    Bugs," MSR '20 — incorrect regex SEMANTICS is the dominant root cause of regex defects (165/356,
    46.3%): silently wrong scope, not visible error. Krakovna et al. (NeurIPS 2020) on reachability /
    irreversibility penalties in agent design. The settled security-operations convention of
    quarantine-before-delete. 15a SUPPORTED (Strong).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate), and the challenge is load-bearing rather than
    incidental — Parasuraman & Riley (1997) and Parasuraman & Manzey (2010) find that human review of an
    automated aid degrades through automation bias and complacency, is NOT remediable by training or
    instruction, and produces an approval trail that makes an unreviewed pass look reviewed. 15b also
    notes that reversibility penalties in the literature are largely magnitude-insensitive, so a
    reversibility requirement does not by itself rank a small deletion below a large one.
  Confidence: High
  Applicable to: any retirement, deletion, retraction or overwrite pass; the memory-entry retirement
    pass specifically; agents holding write authority over the vault.
  QUALIFIES PREMISE-073, AND SAYS SO RATHER THAN COEXISTING QUIETLY. PREMISE-073 holds that high-impact
    or irreversible actions must be emitted as a report plus a ranked action list FOR HUMAN REVIEW, and
    warns that reports without a path to reviewed execution become HITL theater. This premise does not
    contradict that; it narrows what the review can be asked to carry. On the automation-bias evidence,
    review is a filter of unknown and probably poor sensitivity against a by-construction defect that
    looks correct on its face. PREMISE-073 remains ACTIVE and citable; any agent citing it for an
    IRREVERSIBLE action must cite PREMISE-176 alongside it. Flagged for Tom under REVISE-348.
  Re-check due: 2026-11-18 (Quarterly)
  Status: ACTIVE

PREMISE-177:
  Date validated: 2026-08-18
  Source item: ASSUMPTION-1126
  Statement: A RECORDED ROOT CAUSE IS AN INFERENCE THAT WAS NEVER TESTED, AND IT DOES NOT DECAY ON ITS
    OWN. An erroneous diagnosis written into a register survives every subsequent run that reads the
    register instead of the system, and it survives its own correction. Environment- and
    configuration-dependent failures are systematically misattributed to external dependencies, because
    the external dependency is the visible party. The founding instance: a check inert for nineteen
    consecutive runs, recorded throughout as an upstream (YouTube) problem, was a hardcoded `/tmp` path
    against a sticky directory owned by `nobody` in the sandbox.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Yin, Ma, Zheng, Zhou, Bairavasundaram & Pasupathy (2011), "An Empirical Study on
    Configuration Errors in Commercial and Open Source Systems," SOSP '11 — 546 real-world
    misconfigurations; environment and path errors are a dominant and often SILENT failure cause.
    Peerally, Carr, Waring & Dixon-Woods (2017), "The problem with root cause analysis," BMJ Qual Saf
    26(5):417-422 — recorded causes are causal narratives whose validity is rarely tested. Kellogg et
    al. (2017), BMJ Qual Saf 26(5):381-387, on the non-durability of recorded RCA causes. Hsiao &
    Schneider (2021), Quantitative Science Studies 2(4):1144-1169 — 94.6% of post-retraction citation
    contexts show no awareness of the retraction. 15a SUPPORTED (Strong).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate). Two challenges are folded into the statement
    rather than dismissed. (i) The new single-cause verdict was reached from one day's observation with
    no control or stratification, and inherits the same one-cause-per-field finality as the cause it
    replaced — Peerally et al. cuts against the correction as much as against the original. (ii) On
    Tal's model-based account of measurement and Bogen & Woodward's data/phenomena distinction, a
    MEASUREMENT is also a model-mediated inference, so this premise deliberately does NOT assert that
    numbers are harder than causes. That comparative claim is held open at MONITOR-536.
  Confidence: Moderate
  Applicable to: the diagnosis fields of every register; incident and streak records; any agent that
    reads a recorded cause instead of re-deriving it; 14a/14b intake.
  Re-check due: 2026-11-18 (Quarterly)
  Status: ACTIVE

PREMISE-178:
  Date validated: 2026-08-18
  Source item: ASSUMPTION-1131
  Statement: AN EXISTENCE CHECK AND A LABEL CHECK DO NOT ESTABLISH THAT A CITED SOURCE SUPPORTS THE
    SENTENCE IT ANCHORS. Verification at the identifier layer certifies that the referent exists and is
    named correctly; it is silent on the relation between the source's content and the anchoring claim.
    Reading the body is therefore not an optional strengthening of the check, it is the only step that
    tests the property at issue — and automated polarity classification is NOT an available substitute
    at present accuracy. Founding instance: four ids cited for claims their own bodies argue against,
    every one of which passed both checks.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Mogull (2017), "Accuracy of cited 'facts' in medical research articles," PLOS ONE
    12(9):e0184727 — quotation error rate 14.5% (95% CI 10.5-18.6), of which 64.8% are MAJOR errors
    where the source fails to substantiate, is unrelated to, or CONTRADICTS the assertion. Jergas &
    Baethge (2015), PeerJ 3:e1364 — total quotation error rate 25.4% (95% CI 19.5-32.4), major 11.9%,
    all in references that exist and are correctly identified; confirmed at ~32,000 quotations by the
    2025 update in Research Integrity and Peer Review (16.9% incorrect, 8.0% major). Liu, Zhang & Liang
    (2023) — 51.5% sentence support and 74.5% citation precision in generative search engines where
    every cited page resolved. 15a SUPPORTED (Strong).
  Challenges noted: 15b PARTIALLY-CHALLENGED (Moderate), and the challenge is folded into the statement
    as the clause forbidding an automated substitute: Bakker, Theis-Mahon & Brown (2023), "Evaluating
    the Accuracy of scite," found the leading production polarity classifier labelled 2 supporting and
    96 mentioning out of 98, where human raters found 42 supporting, 39 mentioning and 17 CONTRASTING —
    F-measures 0.0-0.58, recovering none of the contrasting citations. 15b further warns that a
    read-the-body RULE is itself an identifier-layer move if compliance is recorded rather than
    measured, which is carried to REVISE-349 and the G2 systemic flag.
  Confidence: High
  Applicable to: every citation-bearing field in the vault; PRS ids; CROSS entries; the review page's
    anchor checks; 15a/15b source lists including those written this run.
  CITES THE OPEN CONTRADICTION RATHER THAN STEPPING AROUND IT. The REGISTER-CONTRADICTION NOTICE of
    2026-08-17 (PREMISE-042 / PREMISE-043, unresolved, venue 2026-08-21) concerns the ERROR PROFILE of
    lexical matching — whether it under- or over-counts convergence. This premise is about POLARITY, a
    different axis: it holds whatever the lexical instrument's error profile turns out to be, because a
    perfectly-recalled, perfectly-precise lexical match still carries no sign. Any agent citing
    PREMISE-178 near PREMISE-042 or PREMISE-043 must cite the notice as well.
  Re-check due: 2026-11-18 (Quarterly)
  Status: ACTIVE

--------------------------------------------------------------------------------

REGISTER-REINFORCEMENT NOTICE — 2026-08-18
  Raised by: Agent 15c at DISPOSITION-744 (PRESUMPTION-829) and DISPOSITION-748 (PRESUMPTION-834).
  NO NEW PREMISE IS MINTED BY THIS NOTICE, DELIBERATELY. Both items were dispositioned INCORPORATE on
  the evidence, and both restate premises already ACTIVE in this register. Per PREMISE-138 the remedy
  for a claim that already has an entry is not a second entry beside it. What follows is the new
  evidence, attached to the existing premises.

  PRESUMPTION-829 ("that a scheduled task which fires has run") REINFORCES **PREMISE-100**, which
  already holds that a liveness signal is not evidence of correctness and that a health check unable to
  execute in its runtime context reports as PASSING rather than as ABSENT. New evidence, 15a SUPPORTED
  (Strong): Huang, Guo, Zhou, Lorch, Dang, Chintalapati & Yao (2017), "Gray Failure: The Achilles' Heel
  of Cloud-Scale Systems," HotOS '17, which formalises the exact gap as DIFFERENTIAL OBSERVABILITY and
  argues it is the dominant cloud-scale failure mode; grounded formally by Alpern & Schneider (1985),
  "Defining Liveness," IPL 21(4):181-185. Observed instance: seven of twenty-nine runs produced nothing
  on a day the scheduler logged 78 OK.
  15b PARTIALLY-CHALLENGED (Moderate), and the challenge is real and is NOT dischargeable: liveness is
  not monitorable from a finite trace (Alpern & Schneider), failure detectors are unreliable by
  construction (Chandra & Toueg 1996, JACM 43(2):225-267; FLP 1985). There is no complete remedy — only
  partial detectors with a stated false-negative posture. PREMISE-100 should be read as licensing an
  output-side check (did this run WRITE its artefact), never a claim of completeness.
  Residual gap, and it is an instrument gap rather than a literature question: no register records the
  count of runs that started and produced nothing. It exists only in this pipeline's own file, computed
  after the fact. Not authorised to any agent; carried to Tom with the standing measurement ask.

  PRESUMPTION-834 ("that an agent's capability is a property of its contract rather than of its
  session") REINFORCES **PREMISE-098**, which already holds that scripts correct interactively must not
  be presumed to behave identically headless, that each scheduled script asserts its context invariants
  (HOME, filesystem/mount reach, credentials, lock state) and fails loud, and that a per-delta preflight
  is required while full hermeticity is not. New evidence, 15a SUPPORTED (Strong), and it is the
  sharpest empirical anchor the premise has yet had: Zheng, Adams & Hassan (2025), "On Build Hermeticity
  in Bazel-based Build Systems," IEEE Software 42(6) — 150M traced filesystem calls across 70 projects,
  NONE fully hermetic, 2,439 host-supplied packages named in no build specification, 98.6% depending on
  undeclared top-level toolchains, median 12 host dependencies absent from a default install. This
  converts PREMISE-098's "full hermeticity is not required" clause from a concession into a measured
  fact.
  15b CHALLENGED (Moderate) on two counts that PREMISE-098 does not currently carry and should at its
  re-check: (i) the day's mount/no-mount split is a single-day univariable observational finding and
  cannot exclude confounding (Simpson's-paradox literature; no test detects spuriousness from
  observational data alone), so "the mount predicted outcome better than any contracted property" is
  suggestive, not established; (ii) a pre-flight capability check is TOCTOU-vulnerable — the invariant
  asserted at startup can lapse mid-run — so preflight bounds the failure window rather than closing it.
  Both are recorded at MONITOR-535's sibling reasoning and folded here rather than minted separately.

--------------------------------------------------------------------------------
## 2026-08-19 — c2a2-lit-search-pipeline (15c), 2026-08-18 intake cohort

PREMISE-179:
  Date validated: 2026-08-19
  Source item: ASSUMPTION-1149
  Statement: A regex-defined reader over an append-only, heterogeneous record file is a SILENT-FAILURE
    coordination interface: a record in an unanticipated shape is not rejected, it is not seen, and no
    error is raised. Consequently, divergent counts from two non-buggy parsers of the same log are the
    expected result of format drift, not evidence that one parser is broken; a count produced by a
    single regex parse is a FLOOR, never a measurement.
    SCOPE GUARD (load-bearing, both limbs withheld from the source item):
    (i) The remedy is NOT a more tolerant reader. Reader tolerance is the mechanism by which drift
    becomes permanent (Thomson, IETF draft-thomson-postel-was-wrong / draft-iab-protocol-maintenance);
    tolerance postpones the reconciliation and enlarges it. Write-side schema constraint, not read-side
    forgiveness.
    (ii) "The queue's depth has never been a measured quantity" is NOT incorporated. Little's Law
    recovers queue depth from filing and completion timestamps already present in the record, without
    any format decision. The premise licenses "single-parse counts are floors," not "depth is
    unmeasurable pending an unauthorised format decision."
  Item type: ASSUMPTION (stated)
  Supporting evidence: "DeepParse: Hybrid Log Parsing with LLM-Synthesized Regex Masks," arXiv:2604.20553
    [author list not verified]; LLM4Log, arXiv:2604.16359 (format drift → template fragmentation and
    erroneous merges) [author list not verified]
  Challenges noted: robustness-principle critique (above, folded into scope guard); log-parsing
    evaluation places refined-metric template accuracy near 0.2, so three-parse divergence is the field
    baseline rather than an anomaly — this weakens the item's alarm register while confirming its fact.
  Confidence: Moderate
  Applicable to: for_lit_search.md intake accounting; every backlog figure this pipeline reports; any
    regex-defined reader used as a coordination interface between agents.
  Re-check due: 2026-09-19 (Monthly, 15d)
  Status: ACTIVE
  Filed from: lit_search_results/for/ASSUMPTION-1149_for.md and against/ASSUMPTION-1149_against.md
  Related: G1 systemic flag; REVISE-362 (PRESUMPTION-841, absence-recording).
  PROVENANCE: Origin 14a · Chain [14a -> 15a, 15b -> 15c] · Current status: INCORPORATED

PREMISE-180:
  Date validated: 2026-08-19
  Source item: ASSUMPTION-1150
  Statement: Errors of large language models are substantially CORRELATED ACROSS MODELS, and the
    correlation RISES with capability — larger and more accurate models err together even across
    distinct architectures and providers. Therefore agreement among model-generated judgements is
    partly evidence about the models rather than about the claim, and any confidence weight that treats
    N agreeing model outputs as N independent votes OVERSTATES its evidential basis. Effective sample
    size, not raw count, is the correct quantity.
    SCOPE GUARD (load-bearing, and the reason this premise is narrower than the source item):
    (i) The correct predicate is DISCOUNT, not INVALIDATION. Correlated-vote Condorcet results (Ladha,
    JEBO) show aggregation gain degrading continuously while the group remains more reliable than the
    individual; de-entangled reweighting has been reported to BEAT majority voting (arXiv:2604.07650,
    +4.5%). Discarding concordance entirely replaces a biased estimator with none.
    (ii) The reflexive extension to 15a/15b is NOT incorporated. The cited work measures same-direction
    judge panels; 15a and 15b are adversarially assigned and mutually blinded. No cited source measures
    that configuration. The extension may still be true — it is untested, not established.
  Item type: ASSUMPTION (stated)
  Supporting evidence: Kim, E., Garg, A., Peng, K. & Garg, N. (2025). "Correlated Errors in Large
    Language Models." arXiv:2506.07962, ICML 2025 [abstract and author list verified 2026-08-19];
    Kuai et al. (2026), arXiv:2604.07650, 18 models / 6 families [verified] — names LLM-as-judge and
    ensemble verification as the affected designs.
  Challenges noted: Ladha (JEBO) correlated-vote jury theorem; de-entangled reweighting result (above).
    See also the REGISTER-VERIFICATION notice at DISPOSITION-763 concerning the unconfirmed "Kohli 2026"
    author attribution — this premise does not rest on it.
  Confidence: Moderate — deliberately NOT High. This premise was dispositioned by the pipeline whose
    method it constrains; the circularity is named and not resolved. Human adjudication remains the
    only decorrelated stream available to the system.
  Applicable to: every confidence weight in this pipeline; MMA assembly weighting; the 15a/15b
    disposition method (which since 2026-08-18 cites sources rather than agreement).
  Consistency check: CONSISTENT with, and strengthening of, the premise minted from ASSUMPTION-294
    ("evidential weight of agreement scales with formational INDEPENDENCE; same-formation agreement is
    redundant-but-real signal — a smaller effective N — NOT near-chance noise"). That premise already
    carries the discount-not-nullity correction. No existing premise contradicted or overwritten.
  Re-check due: 2026-09-19 (Monthly, 15d)
  Status: ACTIVE
  Filed from: lit_search_results/for/ASSUMPTION-1150_for.md and against/ASSUMPTION-1150_against.md
  Related: REVISE-350; G3 systemic flag; PREMISE at ASSUMPTION-294.
  PROVENANCE: Origin 14a · Chain [14a -> 15a, 15b -> 15c] · Current status: INCORPORATED

PREMISE-181:
  Date validated: 2026-08-19
  Source item: ASSUMPTION-1152
  Statement: An artifact read from a fixed, conventionally-named path can be a STALE artifact from a
    prior run, and the resulting failure mode's signature is a PASS — a run that silently fails to write
    and then parses the residue as its own output reports a clean verdict rather than an error. This is
    the documented "stale cache hit" class; it is structural, not incidental, and its adversarial form
    (cache poisoning) is the same mechanism.
    MITIGATIONS carried in the premise, cheapest first: `set -euo pipefail` and `noclobber` so a failed
    redirection halts rather than proceeds; atomic temp-then-rename so a partial write is never
    readable; per-run unique paths; and content-level provenance so the consumer can verify authorship.
    SCOPE GUARD (load-bearing): partial mitigation is NOT hermeticity. A study of 70 mature Bazel-based
    projects (~150M syscalls, IEEE Software 2025) found NONE fully hermetic. The premise licenses
    applying the mitigations; it does NOT certify that a mitigated pipeline is clean.
    SECOND GUARD: detection of this class is a DESIGN ACTIVITY, not luck. Gray-failure and
    differential-observability work, and a silent-failure taxonomy for agent runtimes (arXiv:2606.14589),
    make the detector specifiable. "We caught it by luck" is a statement about missing instrumentation.
  Item type: ASSUMPTION (stated)
  Supporting evidence: "Understanding and Detecting Flaky Builds in GitHub Actions," arXiv:2602.02307
    [author list not verified]; GitHub Actions cache-poisoning literature (adversarial form of the same
    mechanism).
  Challenges noted: the configuration-versus-architecture challenge (folded in as the mitigation list —
    treating a missing `set -euo pipefail` as an architectural discovery leaves the cheapest fix
    unapplied); the 0/70 hermeticity result (folded in as the scope guard).
  Confidence: Moderate
  Applicable to: every agent script redirecting to a fixed /tmp path; fidelity_check.py and its class —
    this EXTENDS PREMISE minted from ASSUMPTION-1126 (2026-08-18) from one script to the general case.
  Re-check due: 2026-09-19 (Monthly, 15d)
  Status: ACTIVE
  Filed from: lit_search_results/for/ASSUMPTION-1152_for.md and against/ASSUMPTION-1152_against.md
  Related: REVISE-359 (PRESUMPTION-837, path-as-identity — the deeper form of the same defect);
    G1 systemic flag; ASSUMPTION-1126.
  PROVENANCE: Origin 14a · Chain [14a -> 15a, 15b -> 15c] · Current status: INCORPORATED

**Total new PREMISEs this run (2026-08-19): 3 (PREMISE-179 silent regex readers / single-parse counts
are floors; PREMISE-180 correlated LLM error and effective sample size [discount, not nullity];
PREMISE-181 stale-artifact false-clean verdicts). All three are stated ASSUMPTIONs; all three carry
explicit scope guards withholding the source item's over-claim (tolerance-is-the-fix and
depth-unmeasurable; invalidation and reflexive transfer; partial-mitigation-is-hermeticity). Cumulative
through PREMISE-181. NOTE, filed against this run itself: PREMISE-180 and PRESUMPTION-845 (REVISE-364,
Critical) together say that a run which recognises its own method invalidated should perhaps not mint
premises at all. This run minted three anyway, because it has no clause permitting it to stop. That is
the finding of REVISE-364, restated here where the artefacts it concerns are recorded.**

--------------------------------------------------------------------------------

================================================================================
## 2026-08-23 — 15c run note: NO PREMISE MINTED (backlog draw, 2026-07-05 cohort cycle 5)

**Six items dispositioned. Zero INCORPORATE. Nothing was added to this register today.**

Recorded here rather than left as silence, because a register that only speaks when it grows cannot be
audited for the runs in which it should not have grown. Composition: 5 REVISE (REVISE-365..369), 1
MONITOR (MONITOR-544). Five of the six carry strong or moderate-strong challenges; the sixth is stuck on
a demarcation decision no literature can make.

**The abstention is deliberate.** On 2026-08-19 this pipeline recorded against itself (REVISE-364, and
the note at the foot of this register) that it had minted three premises in a run that had just declared
its own concordance evidence unreliable, "because it has no clause permitting it to stop." Today's run
faced no such temptation — no item came close to INCORPORATE — so this is not evidence that the missing
clause has been supplied. **It has not been. The gap REVISE-364 names is still open.** This note is
logged so that a later reader counting mint-rates does not read today's zero as the clause working.

**What today's run found about this register, which matters more than what it added to it.**
Four of the five REVISE items (365, 366, 367, 369) are members of an UNOBSERVABLE-NEGATIVE systemic flag
raised independently by 15b and accepted by 15c: each infers that a mechanism works from the absence of
an observed failure, on a channel with no read receipt and no heartbeat. **Every rule needed to catch all
four was already ACTIVE in this register and had been for the whole time the items sat in MONITOR:**

  · PREMISE-115 — the effectiveness check must be that the expected CONTENT appears, never that a file
    appears; "file existence is a liveness test and the fault class this premise concerns is precisely
    the one liveness tests miss." **The 2026-04-18 observation underlying three of these four items is a
    file-existence liveness test.** The register held the rule that invalidates that datum, and the datum
    was carried for four months and five cycles regardless.
  · PREMISE-100 — a liveness signal is not evidence of correctness; a check that cannot execute in its
    runtime context reports as PASSING rather than as absent.
  · PREMISE-086 — alarm on the AGE of the last dated PASS, with a monitor-of-monitor.
  · PREMISE-089 — freshness is a per-source property.
  · PREMISE-006 — flag transparently; do not silently reconcile.

**ENFORCEMENT GAP, NOT KNOWLEDGE GAP.** This is the same shape the 2026-08-17 run recorded ("SIX active
premises already hold this; deployment gap, not knowledge gap") and the same shape again on 08-19. It is
now the third consecutive run of this pipeline to reach that conclusion by a different route. The
structural reason is stated in DISPOSITION-773/775/778 and worth repeating where the premises live:
**15d can re-search an item but it cannot check an item against a premise.** A register whose contents
are never applied to the queue that generated them will keep re-deriving its own holdings, which is what
cycles 2–4 of this cohort did when they returned null on all four items — literature was never the
binding constraint.

**Recommended, not decided:** a premise-conformance pass over the MONITOR queue — for each item, does an
ACTIVE premise already settle it? 15c cannot institute that routing. Under PREMISE-096 this pipeline may
not amend its own intake gate (standing: OPEN-153, REVISE-340, unanswered).

**One consistency observation filed for 14a rather than as a flag.** ASSUMPTION-005 is INCORPORATED at
this register and holds that traditions are the right unit of analysis for organising research progress.
**It is silent on what counts as a tradition.** ASSUMPTION-064 has now spent five cycles stuck in exactly
that silence (MONITOR-544). No contradiction is asserted and no premise is amended; an INCORPORATED
premise being silent on the term it turns on is recorded as an observation.

--------------------------------------------------------------------------------
