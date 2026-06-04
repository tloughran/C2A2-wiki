SEARCH-FOR-PRESUMPTION-293:
  Date searched: 2026-06-02
  Original item: PRESUMPTION-293
  Original statement: [inferred] ASSUMPTION-264's clean-reload remedy presumes the verifier operates outside the degraded regime -- that the reload is immune to the same lag/batching/throttling it adjudicates. It assumes a fault-free vantage point exists from which to judge an unreliable session.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-293
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated epistemic presumption embedded in ASSUMPTION-264's remedy (a fault-free vantage point exists).
      15a: Searched independence-of-monitor-from-monitored, out-of-band verification, and common-mode-failure avoidance.
    Current status: SUPPORTED (the concern is well-grounded)

  Supporting evidence found: Yes

  Sources:
    1. Knight & Leveson (1986) experimental evaluation of independence in multi-version programming; "A Reply to the Criticisms." — Empirically established that independently produced versions do NOT fail independently; correlated/common-mode failures occur far above chance. A verifier built on the same substrate as the monitored system cannot be assumed fault-independent.
    2. Common-mode failure avoidance (IEEE CMF survey; NASA common-cause-failure analyses; ScienceDirect "Correlated Failures in Multi-Version Software"). — The standard remedy for a checker that may share the monitored system's fault is diversity / out-of-band independence; a same-regime re-check is a common-mode dependency.
    3. Monitor-independence principle (observability/SRE practice: external/out-of-band health checks). — A monitor must not ride the same failure-shared path as the system it monitors, or it goes dark with it — directly the "fault-free vantage point" the presumption questions.

  Strength of support: Strong (the concern is well-grounded)

  Summary: The presumption is strongly grounded by the Knight-Leveson result and the common-mode-failure literature: independence of a checker from the checked system cannot be assumed and is frequently violated. A "clean reload" performed inside the same Chrome/claude.ai session regime whose lag/batching/throttling it is adjudicating is a same-regime verifier — a textbook common-mode dependency. A genuinely authoritative re-verification must be out-of-band (a path that does not share the degraded regime's failure mode).

  Caveats: Common-mode risk is a matter of degree; if a reload demonstrably resets the specific fault (e.g., a fresh process/profile not subject to the throttling), partial independence may hold. The empirical question of whether the reload shares the fault couples REVISE-073 / PRESUMPTION-278 (rAF/background-tab throttling).

  Recommendation: SUPPORTED
