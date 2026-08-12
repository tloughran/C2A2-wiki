SEARCH-FOR-PRESUMPTION-025:
  Date searched: 2026-08-11
  Original item: PRESUMPTION-025
  Original statement: [inferred] "Resuming a paused deployment was justified by epistemic progress, not just operational cleanup."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 5)
    Original item: PRESUMPTION-025
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated presumption — the unpause decision invoked epistemic grounds, but operational cleanup may have been the actual trigger
      15a (cycle 1, 2026-04-15): initial supporting search — Perpetual Pilot Trap, decision theory under uncertainty, incremental deployment; PARTIALLY-SUPPORTED, Weak
      15d: re-triggered for cycle 5 monitoring
      15a (cycle 5, 2026-08-11): re-searched for supporting literature; checked for new sources since April 2026
    Current status: PARTIALLY-SUPPORTED (Weak)

  Search scope: Real-options and staged-commitment project literature; incremental deployment and learning-by-deploying; pilot-trap and pilot-to-production statistics (2026); operational readiness review practice; coordinated pausing in frontier AI. Comprehensive for the resumption-under-uncertainty angle; the specific epistemic-vs-operational-readiness distinction returned nothing and a broader search — likely in philosophy of science or R&D management rather than deployment practice — is recommended.

  Supporting evidence found: Partial (Weak)

  Sources:
    1. Annals of Operations Research, 2025. "A real options methodology for multi-stage project selection: an application to NASA's SBIR program." (10.1007/s10479-025-06509-8). — NEW and the first peer-reviewed source in this file. Formalises deferral, staged implementation, and resumption as options whose exercise is justified when new information raises expected value. Supports resumption on *information* grounds specifically, which is the closest formal analogue to "epistemic progress" located.
    2. Agility-at-Scale, "Scaling AI from Pilots to Enterprise-Wide Deployment: The Architecture of Compounding Capability"; CloudX, "How to escape the pilot trap in enterprise AI." — Carried forward and refreshed with a 2026 figure: 88% of AI pilots never reach production at all, regardless of company size. Supports the general proposition that resumption/commitment is often the correct move against indefinite pausing.
    3. MLflow, "Building Production-Ready AI Agents in 2026"; Sivaro, "AI Agent Deployment Pipeline: A Practitioner's Guide for 2026." — NEW (2026 practitioner). Incremental scaling with shadow deployments and rollback checkpoints consistently outperforms big-bang rollout; each increment is framed as generating the learning that licenses the next — a learning-by-deploying argument that supports resumption as itself epistemically productive.
    4. "Do Real Options Lead to Escalation of Commitment?" (ResearchGate 271685521). — Reported for honesty: real-options framing can be used post hoc to rationalise continuation, and is a documented vector for escalation of commitment. This is the precise failure mode PRESUMPTION-025 was surfaced to test for.
    5. Wikipedia / industry, "Operations readiness and assurance"; Moments Log, "How to Design a Production Readiness Review." — Establish operational readiness as a distinct, formalised construct with its own review gates. Indirectly supportive of the presumption only in the sense that the field keeps the two constructs separate; no source treats operational readiness as a substitute for epistemic grounds.

  Strength of support: Weak

  NEW SINCE LAST CYCLE: Yes, but not on the load-bearing point — sources 1, 3, and 4 are new since April 2026. What they add: a peer-reviewed real-options formalisation in which resumption is justified by new information (the nearest thing to support for the epistemic reading), 2026 practitioner evidence for learning-by-deploying, and a named counter-mechanism (real options as escalation-of-commitment rationalisation). What they do not add: any treatment of the epistemic-versus-operational distinction, which was the specific gap flagged in April and remains open after four months.

  Evidence trajectory (supporting): stable

  Summary: Four months on, the literature still does not address the question this presumption turns on. There is decent and now peer-reviewed support for the general shape of the move — resuming a paused programme is justified when new information raises expected value, and indefinite pausing has a documented failure mode with an 88% pilot-mortality figure behind it. There is no source anywhere in the searched literature that licenses treating operational cleanup as equivalent to epistemic progress, or that offers a criterion for distinguishing the two at a resumption gate. The real-options literature actually supplies the sharpest reason for caution: the same framing that justifies resumption on information grounds is a documented vehicle for post-hoc rationalisation of escalating commitment. Support remains Weak and the recommendation carries forward unchanged.

  Caveats: (a) The core distinction — "we fixed the plumbing" versus "we resolved the foundational questions" — is untreated in the literature, so any support here is by analogy from contexts where the two are not separated. (b) Real-options support is conditional on new information genuinely arriving; operational cleanup is not new information about the underlying uncertainty, so the source supports the presumption only if the epistemic claim is true independently. (c) Deployment-practice sources are enterprise/grey literature, not research-system design. (d) C2A2's own state at the resumption — REVISE items outstanding, contested findings, and items such as this one still in MONITOR five cycles later — is exactly the configuration under which escalation-of-commitment risk is highest, and no located source addresses it.

  Recommendation: PARTIALLY-SUPPORTED (Weak)
