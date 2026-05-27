SEARCH-AGAINST-ASSUMPTION-138:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-138
  Original statement: "Pathways 18-25 are a 'deliberate post-ISME breadth arc, not demo-path advancement'; allocation question for 8-week runway"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-138
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from breadth-arc framing
      15b: Searched for counter-evidence on post-demo work competing with demo-critical work for cognitive bandwidth
    Current status: CHALLENGED (Moderate)

  Sources:
    1. Reinertsen (2009) "Principles of Product Development Flow" — WIP exceeds capacity → throughput degrades nonlinearly; breadth-arc work added to runway WIP is documented anti-pattern even when framed as "post-demo."
    2. Forsgren et al. (2018) "Accelerate" — context-switching cost; "framing as post-demo" doesn't eliminate the cognitive context-switch cost of authoring breadth-arc content during runway.
    3. Brooks (1995) "Mythical Man-Month" — second-system effect; ambition expansion during constrained runway is the canonical failure pattern; "deliberate" framing does not preclude it — the failure pattern is recognized post-hoc, not in real time.
    4. Sweller (1988) cognitive load theory — cognitive bandwidth is finite; "deliberate" allocation framing doesn't change the cognitive substrate.
    5. Empirical: 8 pathway docs drafted in one day inside an 8-week runway is a direct data point against the enforcement claim; the framing did not prevent breadth allocation during runway.
    6. PRESUMPTION-173 paired — cognitive-bandwidth allocation tension implicit and unaudited.
    7. PRESUMPTION-178 paired — runway as countdown without probability-weighting; demo-readiness drift not modeled.

  Strength of challenge: Moderate

  Summary: The "deliberate post-ISME breadth arc, not demo-path advancement" framing is honest acknowledgment of the risk but doesn't constitute mitigation. WIP/throughput literature (Reinertsen, Forsgren et al.) shows that adding breadth-arc work to constrained runway degrades throughput regardless of framing — the cognitive substrate is the same. The empirical record from 2026-05-14 itself (8 pathway docs in one day) is data against the enforcement claim: the framing was applied and breadth work still happened. Moderate challenge: the assumption is honest in self-acknowledgment but does not include the mitigations the literature suggests are required (WIP cap, time-boxing, explicit return-to-demo-track gate). PRESUMPTION-173 and PRESUMPTION-178 are the paired audit items.

  Specific risks: (a) Breadth-arc work consumes cognitive bandwidth needed for demo-critical pathways; (b) Context-switching cost between breadth and demo work is unbounded; (c) "Deliberate framing" without enforcement mechanism is decorative; (d) 8-week runway without probability-weighted contingency planning.

  Mitigations available: (a) WIP cap (max N breadth-arc docs per week); (b) Time-box breadth-arc work to specific days; (c) Return-to-demo-track gate (no further breadth until demo-critical pathway X is at state Y); (d) PRESUMPTION-178 probability-weighted runway planning; (e) Track breadth-arc days against demo-critical-progress days as an explicit metric.

  Recommendation: CHALLENGED (Moderate) — framing is honest acknowledgment but lacks enforcement; literature recommends WIP cap and explicit gates

  STEELMAN:
    Item: ASSUMPTION-138
    Strongest counterargument: "Deliberate post-ISME breadth arc, not demo-path advancement" is the right framing but does not constitute a mitigation. The cognitive-bandwidth and WIP/throughput literature is clear: adding work to a constrained runway degrades throughput regardless of how the work is labeled. The 2026-05-14 record itself — 8 pathway docs drafted in one day inside an 8-week runway — is direct evidence that the framing alone doesn't prevent breadth allocation during runway. The honest acknowledgment in "allocation question for 8-week runway" is correct but the implementation needs WIP caps, time-boxing, or return-to-demo-track gates to actually enforce the post-demo framing.
    What would need to be true for C2A2 to be safe: (a) WIP cap on breadth-arc work during runway; (b) Time-box breadth work to specific days; (c) Probability-weighted runway plan (PRESUMPTION-178); (d) Demo-critical-progress days tracked as primary metric.
    How to test: Count breadth-arc-doc days vs. demo-critical-progress days over the 8-week runway; check whether the ratio stays within plan.


---

SEARCH-AGAINST-ASSUMPTION-138 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-25
  Original item: ASSUMPTION-138
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c] (cycle 1)
    Original item: ASSUMPTION-138
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-151 cycle 1)
      15b (cycle 1, 2026-05-25): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new challenging literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of challenge: Unchanged from prior cycle.
  Summary: Cycle-1 refresh confirms the prior cycle's finding; the challenging literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Specific risks: Unchanged from prior cycle.
  Mitigations available: Unchanged from prior cycle.
  Recommendation: refreshed; carry forward prior recommendation
