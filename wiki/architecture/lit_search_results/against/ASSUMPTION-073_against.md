SEARCH-AGAINST-ASSUMPTION-073:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-073
  Original statement: "The 15c heuristic 'PRESUMPTION + strong challenge → REVISE' is operative as a spec rule"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-073
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Critique of risk-classification asymmetry literature (Black & Baldwin 2010 "Really Responsive Risk-Based Regulation") — tag-asymmetric rules can produce systematic over-conservatism; the asymmetry can be a stylistic legacy of the framework's authors rather than empirically justified.
    2. Bayesian-coherence literature (Edwards et al. 1963; Howson & Urbach 2006) — under coherent updating, the prior class (ASSUMPTION vs PRESUMPTION) should not affect the posterior conditional on equivalent evidence; tag-asymmetric posterior dispositions violate Bayesian coherence in a strict sense.
    3. Empirical record on tag-asymmetric heuristics in safety review (Macrae 2014 "Close Calls") — finds that tag-asymmetric rules tend to be over-applied in steady state and require periodic recalibration.
    4. C2A2 operational record: 13/14 PRESUMPTIONs with strong challenges → REVISE; 1 exception (PRESUMPTION-072) was reframed as "should be made explicit." The high concordance rate could indicate either (a) the rule is sound or (b) the agent is mechanically applying the rule without examining each case — the data does not distinguish these.

  Strength of challenge: Weak

  Summary: There is a principled critique of tag-asymmetric disposition rules from Bayesian-coherence and regulatory-review angles: in strict probabilistic updating, the prior class should not change the posterior given the same evidence. The C2A2 heuristic might be over-conservative or stylistically legacy rather than empirically grounded. However, the practical case for asymmetry — that PRESUMPTION items have less prior scrutiny and warrant more caution — is reasonable.

  Specific risks: (a) Mechanical application of the rule may obscure cases where a PRESUMPTION's challenge is weaker than the rule treats it; (b) the inverse case (ASSUMPTION + strong challenge) may be under-treated relative to its actual risk.

  Mitigations available: (a) Periodically audit a sample of REVISE dispositions to confirm asymmetric weighting is empirically warranted; (b) check that ASSUMPTION + strong-challenge cases are not under-flagged.

  Recommendation: PARTIALLY-CHALLENGED (Weak — the rule is defensible but is not empirically calibrated; "spec rule" framing should be softened to "default heuristic with audit")

  STEELMAN:
    Item: ASSUMPTION-073
    Strongest counterargument: Treating "PRESUMPTION + strong challenge → REVISE" as a spec rule rather than a default heuristic risks mechanical application and over-conservatism. From a strict Bayesian standpoint, the same evidence should yield the same posterior regardless of prior tag; the asymmetry is a legacy of the agent definition's narrative framing rather than a calibrated parameter.
    What would need to be true for C2A2 to be safe: A periodic audit of dispositions against an independent reviewer (or against distributed-cadence dispositions) confirms the asymmetric weighting is empirically warranted.
    How to test: Sample 5 PRESUMPTION + strong-challenge REVISEs and 5 ASSUMPTION + strong-challenge dispositions; have an independent reviewer assess whether the asymmetric weighting is justified case-by-case.


---

SEARCH-AGAINST-ASSUMPTION-073 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-17
  Original item: ASSUMPTION-073
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a→15a,15b→15c→15d→15a,15b→15c]
    Original item: ASSUMPTION-073
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-05): re-triggered on weekly cadence; next_check 2026-05-12 elapsed
      15b (cycle 1, 2026-05-17): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Daily-pipeline drain of 15d-owned cohort (see SYSTEMIC-RISK-FLAG in lit_search_returns.md 2026-05-17 RUN section). 15d schedule failure since 2026-05-05.

  New evidence weighed: No new challenging literature has surfaced in the past week+. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-AGAINST-ASSUMPTION-073 (RE-TRIGGER cycle 2):
  Date searched: 2026-05-25
  Original item: ASSUMPTION-073
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c->15d->15a,15b->15c] (cycle 2)
    Original item: ASSUMPTION-073
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..1: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-072 cycle 2)
      15b (cycle 2, 2026-05-25): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new challenging literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of challenge: Unchanged from prior cycle.
  Summary: Cycle-2 refresh confirms the prior cycle's finding; the challenging literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Specific risks: Unchanged from prior cycle.
  Mitigations available: Unchanged from prior cycle.
  Recommendation: refreshed; carry forward prior recommendation
