SEARCH-FOR-ASSUMPTION-052:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-052
  Original statement: "70–80% aggregate cost reduction (~50% Levin per-run) projected from the caching architecture as the vault grows"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-052
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Monday Report decomposition of cost projection
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Anthropic prompt-caching documentation (2024-2025): published cached-token cost is ~10% of non-cached input-token cost (90% reduction on cache-hit tokens); aggregate savings depend on prefix:suffix ratio and cache-hit rate. A 70-80% aggregate saving is plausible only when cached tokens substantially dominate the token budget.
    2. Chawla, Avi (2024). "Prompt Caching" (task brief source): reports cost-deltas in the 50-90% range depending on workload shape; ASSUMPTION-052's 70-80% range falls within published empirical envelope.
    3. OpenAI prompt-caching (2024-2026): automatic prefix-caching produces ~50% cost reduction on cached tokens (less aggressive than Anthropic's 90%); aggregate savings depend on prefix dominance.
    4. LLM cost-observability case studies (FinOps Foundation 2023-2025; vendor case studies on prompt caching 2024-2026): reported aggregate savings cluster in the 40-80% range for reference-heavy agent workloads; C2A2's 49-file RC Wiki prefix fits the "reference-heavy" pattern where high savings are expected.
    5. Amortization theory (Cormen et al. "Introduction to Algorithms" 3rd ed. ch. 17): amortized cost converges to cached-token cost as operation count per session grows. For C2A2's per-agent-run session (multiple proposals against one prefix), amortization favors the projected range.

  Strength of support: Moderate

  Summary: The 70-80% aggregate cost reduction falls within the empirical envelope reported by Anthropic, OpenAI, and independent case studies of prompt-caching deployments on reference-heavy workloads. Achievability depends on (a) prefix:suffix ratio actually being dominated by the static RC Wiki, (b) cache-hit rate being near-ideal (which depends on PRESUMPTION-057 stability), and (c) the pipeline-as-appended-turns reorganization (ASSUMPTION-053) functioning as projected. The specific 70-80% number is a point estimate; the literature supports the range but provides no independent calibration for C2A2's specific workload shape until empirical measurement lands.

  Caveats: (a) The claim is a forward projection, not yet a measurement — it awaits 2026-04-27 Levin v1.0 data; (b) the Avi Chawla article cited in the task brief describes a different workload; transfer validity is not audited; (c) if PRESUMPTION-057 is wrong (files churn more than presumed) the projection is high; (d) if PRESUMPTION-055 is wrong (two-tier is suboptimal) the projection could be low — direction of error is not one-sided.

  Recommendation: PARTIALLY-SUPPORTED (range is plausible, specific point estimate awaits measurement; depends on other presumptions holding)


---

SEARCH-FOR-ASSUMPTION-052 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-17
  Original item: ASSUMPTION-052
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a→15a,15b→15c→15d→15a,15b→15c]
    Original item: ASSUMPTION-052
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-05): re-triggered on weekly cadence; next_check 2026-05-12 elapsed
      15a (cycle 1, 2026-05-17): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: This run drained the 2026-05-05 RE-TRIGGER cohort via the daily c2a2-lit-search-pipeline (15a/15b/15c) rather than the 15d-owned weekly cycle, because the weekly 15d scheduled-task has not fired since 2026-05-05 (12 days; cohort 5 days past next_check). See SYSTEMIC-RISK-FLAG raised in lit_search_returns.md 2026-05-17 RUN section.

  New evidence weighed: No new supporting literature surfaced in the week since the last cycle. The prior cycles' findings stand. Item remains in its established disposition state until either new operational evidence (from C2A2's own runs) or new external literature alters the picture.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted in the past week+; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven literature scan or operational evidence from the C2A2 runs themselves would be the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation
