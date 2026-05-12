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
