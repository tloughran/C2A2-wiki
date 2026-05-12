SEARCH-AGAINST-ASSUMPTION-052:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-052
  Original statement: "70–80% aggregate cost reduction (~50% Levin per-run) projected from the caching architecture as the vault grows"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-052
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Monday Report cost projection decomposition
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Cost-projection-vs-realized-savings literature (FinOps Foundation 2023 "Unit Economics"; multiple LLM cost case studies 2024-2026): realized savings from prompt-caching in production typically under-perform projections by 20-40% due to cache-miss rate, context-window churn, and edge-case fallback paths (non-cached requests during rate-limit events).
    2. Workload-transfer hazard (Avi Chawla article, task-brief source; general case-study transfer): the 70-90% ranges cited in published case studies are measured on the authors' workloads, not C2A2's. The presumption-level concern (PRESUMPTION-055) about binary partition suitability interacts directly with this number.
    3. Composition of projections (forecasting literature; Tetlock 2005 "Expert Political Judgment"): point-estimates compounded across multiple assumptions (PRESUMPTION-055, 056, 057 all must hold) typically over-state realized outcomes.
    4. Prefix-not-dominating-budget counter-case (published LLM cost studies 2024-2026): if the dynamic suffix grows to rival the static prefix (which it will as the vault accumulates daily activity), per-session savings degrade even as aggregate savings grow. The stated 50% Levin per-run figure likely overstates steady-state savings once the vault matures.
    5. Dev-to-prod cost-delta patterns (FinOps 2023-2025): prototype cost projections understate costs from retry logic, failed requests, monitoring overhead, and non-cached fallback paths — typical dev-to-prod inflation factor is 1.2-1.5×.

  Strength of challenge: Moderate

  Summary: The 70-80% aggregate number falls within the published envelope, but realized savings consistently under-perform projections in comparable deployments by 20-40%. More important, the projection compounds three unaudited presumptions (PRESUMPTION-055, 056, 057) — if any is wrong the projection is over-stated. The "as the vault grows" clause is ambiguous: short-term the prefix dominates and savings are high; long-term the dynamic suffix grows and per-session savings degrade even if aggregate savings accumulate. The projection conflates these regimes.

  Specific risks: (a) Realized savings 20-40% below projection is the base rate; (b) presumption-compounding risk amplifies downside; (c) per-session steady-state savings may decline as dynamic suffix grows; (d) cost projections that drive architectural decisions create pressure toward confirming the projection rather than measuring honestly.

  Mitigations available: (a) Treat 70-80% as the optimistic-case upper bound; plan for 40-60% realized as the realistic range; (b) instrument per-run and aggregate cost before and after deployment; (c) define what would trigger a re-architecture (e.g., if 4-week realized savings < 30%, revisit partition scheme); (d) report projected-vs-realized publicly to prevent cognitive anchoring.

  Recommendation: PARTIALLY-CHALLENGED (the number is optimistic-plausible; literature base-rate says plan for ~65-75% of the projection as the realistic outcome)

  STEELMAN:
    Item: ASSUMPTION-052
    Strongest counterargument: Cost-reduction projections for caching architectures consistently miss their target by 20-40% in published production cases. The 70-80% projection is an optimistic point-estimate that compounds three unaudited presumptions — any one failing pushes the actual number down. Moreover, per-session savings degrade as the vault's daily activity grows, so the "as the vault grows" clause cuts both ways: aggregate savings accumulate but per-session savings attenuate. A realistic plan would treat 70-80% as the optimistic ceiling and 40-60% as the likely realized outcome, with instrumentation to detect divergence.
    What would need to be true for C2A2 to be safe: Realized-cost instrumentation on deploy; a documented trigger threshold below which the architecture would be revisited; no implicit pressure to confirm rather than measure.
    How to test: Instrument per-session cost before rollout; measure 4-week post-rollout; compare realized-vs-projected; if < 60% of projection, investigate.
