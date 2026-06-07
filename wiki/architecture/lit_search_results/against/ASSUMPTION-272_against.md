SEARCH-AGAINST-ASSUMPTION-272:
  Date searched: 2026-06-05
  Original item: ASSUMPTION-272
  Original statement: Draining the 36-file ingest backlog should proceed as small, attended-authorized batches (~5-8 files/run), not a single bulk ingest, to protect PRS-triplet quality and avoid sweeping unrelated working-tree changes into the commit.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-272
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated small-attended-batch ingest policy.
      15b: Searched batch-size lower-bound theory and the throughput/overhead cost of per-batch human authorization.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Reinertsen / SAFe Principle #6 (transaction-cost half). InformIT. — The same batch-size theory 15a cites has a U-shaped cost curve: when per-batch transaction cost (here, attended authorization) is high, batches that are too small raise total cost and stall flow. ~5-8 files/run with a mandatory attended gate each time may sit LEFT of the optimum, not at it.
    2. Nuvento, "The Hidden Cost of Human-in-the-Loop AI." / Elementum AI. — An attended gate per small batch quietly re-injects large amounts of manual time; across a 36-file backlog drained 5-8 at a time that is ~5-7 separate attended sessions, each with fixed setup/re-hydration overhead. The oversight layer's cost is real and recurring, not free.
    3. Codebridge / StackAI, "Human-in-the-Loop Approval Workflows." 2026. — Documents the rubber-stamping failure: when an attended queue backs up, reviewers batch-approve to clear it, recreating the very quality risk the small-batch gate was meant to prevent. The attended gate can therefore DEGRADE the PRS-quality it is supposed to protect.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is not to small batches per se (15a's support is solid) but to the conjunction of small batches WITH a mandatory attended authorization on each one. Batch-size theory cuts both ways: the optimal batch grows with per-transaction cost, and an attended gate is a high per-transaction cost, pushing the optimum UP from 5-8. The human-in-the-loop literature adds that repeated small attended gates accrue fixed per-session overhead and, when they queue up, induce rubber-stamping that erodes the curation quality the policy exists to defend. For a finite, bounded, one-time 36-file backlog, a single (or two) carefully-scoped attended bulk ingest may dominate many tiny gated runs on both throughput and realized quality.

  Specific risks: Over-fragmenting a 36-item one-time backlog into 5-7 attended sessions risks (a) never finishing it because each session needs Tom present — the same availability bottleneck that stalled the 06-03 sync; and (b) rubber-stamped approvals once the runs feel routine, defeating the quality rationale.

  Mitigations available: Tune batch size to the attended-overhead cost rather than fixing 5-8 a priori; for a bounded one-time backlog, consider one attended bulk-ingest with strong automated pre-checks (schema/dedup/scope) so the human gate reviews a single well-scoped changeset. The "avoid sweeping unrelated working-tree changes" concern is better solved by committing the ingest on a clean dedicated branch/index than by shrinking batch size.

  STEELMAN:
    Item: ASSUMPTION-272
    Strongest counterargument: Small-batch dogma is being applied to a problem shape it doesn't fit. Lean small-batches optimize a CONTINUOUS, high-variability flow; a 36-file one-time backlog is a bounded, low-variability task where the dominant cost is the recurring attended authorization, not per-item defect propagation. When the gate is expensive and the work is finite, the cost-optimal batch is large, and forcing it small manufactures both an availability dependency on Tom and a rubber-stamping hazard — trading a theoretical quality gain for two concrete failure modes.
    What would need to be true for C2A2 to be safe: Per-batch attended overhead must be genuinely low (near-instant authorization) AND defects must be likely to propagate/compound across files within a run; only then does 5-8 sit at or right of the cost optimum.
    How to test: Time the real attended authorization + setup overhead per run; estimate within-run defect-propagation probability. If overhead is non-trivial and files are independent, model total cost for batch sizes {5-8, 18, 36} — the minimum will likely not be at 5-8.

  Recommendation: PARTIALLY-CHALLENGED
