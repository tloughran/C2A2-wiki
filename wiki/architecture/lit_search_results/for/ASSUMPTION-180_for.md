SEARCH-FOR-ASSUMPTION-180:
  Date searched: 2026-05-19
  Original item: ASSUMPTION-180
  Original statement: "Levin/Friston count discrepancy — sewing-agent sees 0 Levin / 1 Friston in pending/; specialist claims Levin:2 / Friston:1 / Total:3; only Friston count is concordant."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: ASSUMPTION-180
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14b: Surfaced from sewing-agent vs specialist run-report reconciliation
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Helland, P., 2015. "Immutability Changes Everything." CACM 59(1) — the canonical counter-pattern is: durable artifact wins over self-report. A specialist's claimed-count without write-receipt is a self-report; a scan of the durable pending/ directory is durable artifact. Concordance on Friston alone signals one true write, two unverified claims.
    2. Humble, J. & Farley, D., 2010. "Continuous Delivery." Addison-Wesley, ch. on deployment pipelines — discusses "claimed deployments vs verified deployments"; the standard remediation is a deployment manifest emitted by the deployer, checked by an independent verifier. This maps directly to write-claimed vs file-exists.
    3. Allspaw, J., 2012. "Fault Injection in Production." ACM Queue 10(8) — operational lesson that agent-internal counters routinely drift from observable state; a 2-out-of-3 discrepancy is consistent with the "phantom write" failure mode (the writer believed it wrote but no file resulted, often due to silent path-resolution errors or exception-swallowing).
    4. Beyer, B. et al. (eds.), 2016. "Site Reliability Engineering." O'Reilly, ch. 6 — SRE doctrine: when claim ≠ artifact, trust artifact and investigate claim path; concordance on a subset is diagnostic for partial-failure modes (path-specific, tradition-specific filtering).

  Strength of support: Strong

  Summary: The pattern "2-out-of-3 discrepancy, concordant on one item" is a well-recognized signature of partial-failure: silent write-drop, path-resolution misconfiguration, or exception-swallowed exception in the writer. Standard SRE/CD doctrine treats durable artifacts as ground truth over self-report and recommends write-receipt manifests as the canonical fix. The claim that "only Friston count is concordant" is a precise, useful diagnostic finding under this framework.

  Caveats: Naming the failure mode requires more evidence than concordance alone — the sewing-agent scan could itself miss Levin files (PRESUMPTION-204). Until a write-receipt manifest exists, "specialist over-claimed" and "scanner under-counted" are both consistent with the observation.

  Recommendation: SUPPORTED


---

SEARCH-FOR-ASSUMPTION-180 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-01
  Original item: ASSUMPTION-180
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-180
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-31): re-triggered on weekly cadence; next_check 2026-05-31 elapsed
      15a (cycle 1, 2026-06-01): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-05-31 (weekly cadence fired on time; next_check 2026-05-31 elapsed). Unlike the 2026-05-17 run, there is NO overdue 15d-schedule backlog — this is a normal on-cadence refresh.
  Landscape check: Automated landscape spot-check this cycle (3 genuine web searches across distinct clusters: passwordless/one-tap-link & SMS-auth security; Levin-Hoffman-Kastrup idealist convergence; multi-agent LLM systems instantiating research traditions/consensus). All three reaffirmed prior for/against profiles; no material literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted in the past week; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven literature scan or operational evidence from the C2A2 runs themselves would be the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED)
