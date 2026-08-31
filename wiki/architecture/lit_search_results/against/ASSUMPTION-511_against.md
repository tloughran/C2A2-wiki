SEARCH-AGAINST-ASSUMPTION-511:
  Date searched: 2026-08-30
  Original item: ASSUMPTION-511
  Queue ref: for_lit_search.md — 2026-07-21 EOD batch (Priority Medium)
  Original statement:
    The pending queue at 7 is healthy re-accumulation after the 07-20 blanket approval; it will re-
      accumulate until the next decision email.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-511
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from the 2026-07-22 daily run pending-queue note
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: WebSearch, 2026-08-30, clustered query — "vacation and batch-service queueing models; stability despite long idle periods". Snippet-level only; zero
    full-text and zero abstract-level reads. Search confidence: MODERATE. This item was searched on its
    GENERALIZABLE limb only; the internal-empirical limb (a claim about this repository's own file state)
    is not adjudicable by literature and is marked NOT-SEARCHED, per the 2026-08-29 run's split-limb
    finding.

  Challenging evidence found: Yes

  Sources:
    1. Vacation-queue literature (M/G/1 with multiple/working vacations; finite-buffer M/G/1/N with
       vacations, PMC8622463). — a server idle for long stretches can still yield a stable, bounded
       queue provided mean service over the full cycle covers arrivals.
    2. Bulk/batch-service queueing models (MDPI Axioms 14(1):18; AAM 21(1):4). — batch service starting
       only at threshold 'a' produces long zero-service intervals that are nonetheless stable.
    3. Implication: a service rate measured per-day as ~0 does not establish instability if clearing occurs
       in bursts; the measurement timescale must match the vacation cycle.

  Strength of challenge: Moderate-Strong

  Summary:
    The challenge changes the conclusion rather than echoing it. Vacation and batch-service queueing models
      describe servers idle for long stretches that are nonetheless stable, provided mean service across the
      full cycle covers arrivals; finite-buffer M/G/1/N models with vacations are stable by construction. A
      review stage that clears in bursts on decision emails is a vacation queue, not a dead server, and a
      per-day service rate of ~0 measured between bursts is the wrong statistic at the wrong timescale.

  STEELMAN:
    the 07-20 blanket approval cleared the whole queue at once. That is a batch service event of
      size ~34. Averaged over the vacation cycle the service rate is emphatically not zero, and re-
      accumulation to 7 is exactly what a stable vacation queue looks like mid-cycle. 'Healthy' may be right
      for reasons the item did not give.

  Recommendation: CHALLENGED
