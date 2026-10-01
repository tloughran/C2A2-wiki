SEARCH-AGAINST-PRESUMPTION-1102:
  Date searched: 2026-10-01
  Original item: PRESUMPTION-1102
  Original statement: Polling schedules sized for active work should back off when the work completes (adaptive scheduling).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1102
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Susumun, n.d. "Exponential Backoff vs. Fixed-Interval Retries: When Growing Wait Times Actually Help". https://dev.to/susumun/exponential-backoff-vs-fixed-interval-retries-when-growing-wait-times-actually-help-1dj — backoff pays off with many clients on one resource; for a single client fixed intervals are simpler and equally effective; growing waits add latency. [fetched]
    2. Thundering-herd references (Wikipedia, Algoroq, Medium/Agrawal), n.d. — backoff without jitter synchronizes retries. [search-snippet, not read]

  Strength of challenge: Moderate

  Summary: Challenge is about transfer, not refutation. For one scheduler polling one source, a fixed interval avoids added latency, missed-event risk and configuration. Source concerns retry-after-failure, not idle polling after completion, which it does not address.

  STEELMAN: Backoff after completion trades cost savings against detection latency: new work arriving during a long backoff waits as long as the interval. A fixed cheap poll or an event trigger gives bounded latency with no state to get wrong (e.g., a backoff counter that fails to reset).

  Caveats: Single blog post about retries, not scheduled polling. Reset-on-new-work is where bugs occur, but no source documents it.

  Search scope: preliminary search — broader search recommended (web-only, 4 searches / 4 fetches across all four items; no academic sources; independent of 15a — 15a results were not read).

  Recommendation: PARTIALLY-CHALLENGED
