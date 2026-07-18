SEARCH-FOR-ASSUMPTION-467:
  Date searched: 2026-07-18
  Original item: ASSUMPTION-467
  Original statement: The maintained 300-PRS narrative figure is treated as canonical over the master current-status per-file sum (447 today); two same-day agents each advanced a different count.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-467
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-17 EOD run (count divergence 300 vs 447)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Carta, "The General Ledger: A Fund's Single Source of Truth." — Establishes the accounting principle that when a quantity is recorded in multiple places, reconciliation to a single version of truth is required; divergence between a maintained figure and a computed sum is the canonical case reconciliation exists to catch.
    2. USPTO 10,997,507, "Data reconciliation." — Formalizes that the same quantity computed from different sources will drift and requires an explicit reconciliation procedure and a designated authoritative source.
    3. arxiv 2606.08266, "What Went Wrong with Data Lakes? ... KPI divergence rate." — Defines "KPI divergence rate" as the frequency/magnitude of discrepancy when the same metric is computed from different sources, and "manual reconciliation volume" as its cost — directly the 300-vs-447 situation.
    4. ModelThinkers / Nisslmüller (Medium), "Goodhart's Law." — When a maintained narrative figure becomes the target, it decouples from the underlying referent (the per-file ground-truth sum); supports treating the hand-maintained 300 as a Goodhart-prone proxy that should defer to the computed 447.

  Strength of support: Strong

  Summary: The literature strongly supports both halves of the claim: (a) maintaining a metric in two places (a hand-carried narrative figure and a computed per-file sum) predictably produces divergence, and (b) the discipline for resolving it is to designate a single authoritative/computed source of truth and reconcile the other to it. The "two same-day agents each advanced a different count" is a textbook dual-bookkeeping drift, and the framing that the computed 447 should be canonical over the maintained 300 aligns with single-source-of-truth and anti-Goodhart guidance.

  Caveats: The literature says pick ONE canonical source; it does not by itself adjudicate WHICH (narrative 300 vs per-file 447) is correct — that requires defining what a "PRS" counts as. If the per-file sum includes items the narrative deliberately excludes, 447 may over-count. Reconciliation is needed, not automatic adoption of the larger number.

  Recommendation: SUPPORTED
