SEARCH-FOR-PRESUMPTION-337:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-337
  Original statement: The single-human attended commit gate scales with parallel-session output (local-only queues can accumulate indefinitely without integration risk).

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-337
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced unstated presumption by inference from commit-gate workflow (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No
  Sources:
    1. Fowler, M. "Continuous Integration." martinfowler.com. — Foundational statement that integration risk grows with integration delay; frequent small integrations exist precisely because queued unintegrated work accumulates conflict and divergence risk.
    2. Atlassian, "Trunk-based Development." — Long-lived unintegrated branches deviate from trunk and raise conflicting-update risk; the industry consensus is the direct negation of "accumulate indefinitely without integration risk."
    3. Shopify Engineering, "Successfully Merging the Work of 1000+ Developers." — Empirical practice: even with automation, batch size is capped (≈8) because larger unmerged batches raise failure-isolation and rollback costs; single-gate throughput is treated as a hard constraint to engineer around.
    4. software.com /src blog & kodus.io, code-review bottleneck analyses. — Documented pattern of a single experienced approver becoming the throughput limit as parallel PR volume rises; queues grow superlinearly with reviewer saturation.
  Strength of support: None
  Summary: The search found no literature supporting either clause. On the gate: the code-review and delivery-pipeline literature uniformly documents single-approver saturation as the canonical bottleneck under parallel output, with wait times and conflict rates growing as queue depth rises. On the queues: the CI/trunk-based-development literature's core finding is that unintegrated work accrues integration risk with age and batch size — merge conflicts, semantic divergence, and harder failure isolation — which is why batch caps and frequent integration exist. One partial mitigation applies to this project: risk accrual is driven by overlap on shared artifacts, so if parallel sessions touch disjoint files (separate wiki pages), conflict incidence stays low and the presumption degrades more slowly than in typical codebases. That is a scope condition, not support; shared hubs (index files, the generated HTML, the queue files themselves) re-create the standard risk.
  Caveats: The mitigating disjointness condition is fragile here because several artifacts (for_lit_search.md, generated visualization, master indexes) are shared write targets across sessions. No source examined human attention limits for review-quality (vs throughput) at scale, which would likely worsen the picture.
  Search scope: 1 WebSearch ("batch size delayed integration risk continuous integration merge conflict frequency single approver code review bottleneck").
  Recommendation: NO-SUPPORT-FOUND
