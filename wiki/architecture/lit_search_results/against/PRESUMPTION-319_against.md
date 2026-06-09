SEARCH-AGAINST-PRESUMPTION-319:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-319
  Original statement: [inferred] The data/code guard presumes PRS-data regeneration is deterministic/safe enough to publish unreviewed (data treated as review-exempt).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-319
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that regenerated data is review-exempt.
      15b: Searched for evidence that derived-data regeneration is neither reliably deterministic nor safe to publish unreviewed.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Sculley et al. 2015, "Hidden Technical Debt in ML Systems" (data dependencies cost more than code dependencies; CACE principle; pipeline jungles). — Derived-data steps are a documented source of silent, unbounded failure; "review-exempt data" is precisely the debt this literature warns against. Strong direct challenge.
    2. Data-quality / "data downtime" and silent-regression literature (data observability). — Data errors are detected late, propagate widely, and are published as fact; absence of human review on the data path removes the only check that catches plausible-but-wrong output. Challenges "safe enough."
    3. Non-determinism in practice (ordering, dedup, hashing/seed, input drift, the manufactured-identity case REVISE-091). — Real generators are frequently non-deterministic or input-sensitive in ways that change output without any code change; "deterministic enough" is an empirical claim that the system has not verified.

  Strength of challenge: Strong

  Summary: The presumption that regenerated data is deterministic and safe enough to skip review is challenged on both halves. Determinism is asserted, not verified, and real pipelines drift via ordering/dedup/input changes; and even deterministic-from-approved-inputs data can be plausibly wrong and is then published as evidence with no human or automated check. The data path, treated as review-exempt, is the quietest and most propagating failure surface — the opposite of "safe."

  Specific risks: A wrong-but-well-formed datum (mis-merged entity, manufactured id, duplicated edge) auto-publishes into the connectome as fact and propagates to every derived artifact, undetected because nothing — human or gate — was looking. For a system whose product is evidence-about-traditions, this corrupts the output itself. Couples ASSUMPTION-284 (the split that creates the unguarded path).

  Mitigations available: Replace "review-exempt" with AUTOMATED data-quality gates (schema + invariants + referential checks + diff-magnitude/anomaly thresholds); verify generator determinism empirically (re-run, compare) before trusting it; bound auto-publish to small diffs and escalate anomalies/large diffs to human review; record per-run data diffs so regressions are observable.

  STEELMAN:
    Item: PRESUMPTION-319
    Strongest counterargument: "Data is safe to publish unreviewed" is the most dangerous half of the auto-publish design because data failures are quiet, late-detected, widely-propagating, and published as truth — and because "deterministic enough" was assumed rather than measured. The same system already manufactured an identity by fiat (REVISE-091): a concrete instance of well-formed, wrong, load-bearing data that an unreviewed pipeline would publish straight into the connectome. Exempting data from review removes the last check exactly where the most corrosive errors live.
    What would need to be true for C2A2 to be safe: Generator determinism is empirically verified, AND automated data-quality/anomaly gates stand in for the absent human, AND large/anomalous diffs escalate to review.
    How to test: Re-run the generator on identical inputs and diff (determinism check); inject a plausible-but-wrong datum and confirm a gate catches it before publish.

  Recommendation: CHALLENGED
