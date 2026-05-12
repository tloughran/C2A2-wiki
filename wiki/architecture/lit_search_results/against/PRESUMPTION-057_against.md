SEARCH-AGAINST-PRESUMPTION-057:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-057
  Original statement: "The 49 RC Wiki files are stable enough (no churn-rate audit performed)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-057
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from absence of churn-rate audit in caching-architecture deliverables
      15b: Searched for challenging literature
    Current status: STRONGLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Measure, don't assume" literature (Google SRE book 2016; Nygard 2007 "Release It!"; Fowler 2018 "Patterns of Enterprise Application Architecture"): foundational principle of performance architecture — any capacity or rate assumption that drives a design decision must be measured before commitment, not declared.
    2. Wiki-activity burst patterns (Halfaker et al. 2013 "The rise and decline of an open collaboration system"; knowledge-management research 2010-2020): wiki edits cluster in bursts during active research phases, not smooth distributions. Average churn rates under-represent peak invalidation rates during the periods when reference content is being refined.
    3. Cache-hit-rate sensitivity to invalidation rate (Fowler 2018; CDN cache-optimization literature): cache economics are nonlinear — modest churn rate increases (e.g., 2× from baseline) can cut cache-hit rate by 50% or more. The region of high-sensitivity is exactly where "slow-changing" intuition breaks down.
    4. C2A2 operational-drift pattern (internal): five days of Chrome-channel issues, git-lock staleness, PRS freshness gaps — the system has independent evidence that operational assumptions about stability break down in practice. Presuming file-stability while other stability presumptions are actively failing is inconsistent.
    5. PRESUMPTION-057 couples to ASSUMPTION-052 cost projection: the 70-80% cost saving depends on the cache hitting; cache hitting depends on file stability; file stability is presumed without measurement. This is a three-link causal chain, any link of which can fail silently.

  Strength of challenge: Strong

  Summary: "Measure, don't assume" is the canonical capacity-architecture principle across SRE, performance engineering, and caching literature. The presumption violates it directly: RC Wiki files are declared "slow-changing" without a git-log audit, on a reference-typology argument that does not measure actual behavior. The test is cheap (git log over 4-8 weeks) and the stakes compound with ASSUMPTION-052's cost projection. The presumption is systematically at odds with both general engineering principle and C2A2's own observed operational drift in adjacent stability claims.

  Specific risks: (a) Actual churn rate exceeds presumed — cache-hit rate drops and cost projection fails; (b) burst-edit patterns invalidate cache during research-push weeks (exactly when cost matters most); (c) mid-day file edits create read-after-write race between editing and running sessions; (d) the presumption is a dependency of ASSUMPTION-052, so it inherits the cost-projection's downstream consequences.

  Mitigations available: (a) Run git log on the 49 files over the past 4-8 weeks; compute daily-edit-frequency histogram; compare against cache-invalidation-rate break-point; (b) set a cache-invalidation-rate alarm that triggers if weekly rate exceeds threshold; (c) edit-lock / mid-day-edit-avoidance policy during active caching periods; (d) document actual churn as part of the rollout gate.

  Recommendation: CHALLENGED (strong; "slow-changing" must be measured not declared; audit is cheap; ASSUMPTION-052 cost projection depends on this presumption holding)

  STEELMAN:
    Item: PRESUMPTION-057
    Strongest counterargument: "Measure, don't assume" is the canonical principle of capacity-architecture across SRE, performance engineering, and caching literature. The presumption violates it directly — "slow-changing" is used descriptively without a measurement. The test is cheap: git log on the 49 files over 4-8 weeks produces a churn-rate distribution and identifies burst patterns. Cache-hit-rate sensitivity to invalidation rate is nonlinear, so "probably slow enough" is an untested claim at exactly the point of highest downside. The presumption is a dependency of ASSUMPTION-052's cost projection, so it inherits the cost-projection's consequences: if churn is higher than presumed, the 70-80% saving is pessimistic (the assumption's critique of ASSUMPTION-052's specific number inherits this).
    What would need to be true for C2A2 to be safe: Run git log on the 49 static-prefix files over the past 4-8 weeks; compute daily-edit-frequency; verify the distribution is consistent with acceptable cache-invalidation-rate; set an alarm for exceedance.
    How to test: Pre-rollout, `git log --follow --format=%ad -- <file>` on each of the 49 files over a 56-day window; aggregate; compare against the invalidation-rate threshold derived from ASSUMPTION-052's cost projection.
