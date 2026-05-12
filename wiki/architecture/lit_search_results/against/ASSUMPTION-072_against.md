SEARCH-AGAINST-ASSUMPTION-072:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-072
  Original statement: "A 5-day lit-search backlog is drainable in a single 15a/15b/15c cycle"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-072
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Hertwig & Pleskac (2010) "Decisions from experience: Why small samples?" — evaluation fatigue effects in batch settings are documented; later items in a batch receive systematically less attention.
    2. Danziger, Levav & Avnaim-Pesso (2011) "Extraneous factors in judicial decisions" PNAS — cognitive-batch position effects: judgment quality decays measurably across batch position.
    3. Kahneman (2011) "Thinking, Fast and Slow" — anchoring effects in concentrated batches; early items establish anchors that distort later items.
    4. Cooper et al. (2010) "Stage-Gate Systems" — saturation point for single-cycle drains is empirical and N-dependent; "drainable" claims at unfamiliar Ns require validation.
    5. Distributed-cadence literature (Sutton 1996 "Generalization in reinforcement learning"): distributed evaluation outperforms concentrated batches on most quality metrics, though throughput differs.

  Strength of challenge: Moderate

  Summary: The literature documents systematic batch-evaluation effects: position-decay, anchoring, fatigue. The claim that a 5-day backlog is drainable in a single cycle is feasible at the throughput level but is challenged at the quality-equivalence level. Distributed-cadence evaluation is the literature-preferred design for high-stakes review.

  Specific risks: (a) Items late in the batch receive systematically less depth; (b) anchoring from early items may distort later dispositions; (c) the "single-cycle drain" framing may obscure quality variance across batch position.

  Mitigations available: (a) Randomize item order within the batch to spread anchoring; (b) document depth-per-item and flag any items processed below depth threshold; (c) cross-check a sample against distributed-cadence baseline.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-072
    Strongest counterargument: Single-cycle drains are throughput-feasible but quality-asymmetric. The literature documents that batch-position, fatigue, and anchoring effects distort late-batch evaluations relative to early-batch ones. Treating a 5-day backlog drain as equivalent to 5 distributed daily cycles confuses throughput with quality and obscures the systematic asymmetry.
    What would need to be true for C2A2 to be safe: (a) items are processed in randomized order within the batch; (b) depth-per-item is documented; (c) a sample is cross-validated against a distributed-cadence run.
    How to test: Run a single-cycle drain and a distributed-cadence drain on independently-but-comparably-difficult batches; compare disposition agreement rate. >90% agreement would weaken the challenge; <80% would strengthen it.
