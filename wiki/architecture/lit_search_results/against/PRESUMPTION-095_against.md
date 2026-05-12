SEARCH-AGAINST-PRESUMPTION-095:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-095
  Original statement: "Phase-2 zero-result = exhaustion not method-failure; no fallback search-strategy variation"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-095
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated counterpart of ASSUMPTION-084
      15b: Searched for challenging literature on query-form sensitivity in 60-day-window academic search
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Information-retrieval literature (Manning, Raghavan & Schütze 2008) — query-form sensitivity is well-documented; single-strategy null is consistent with both exhaustion and method failure.
    2. Cochrane LSR (Elliott et al. 2017) — null acceptance requires multi-source, multi-query depth; single-strategy null treated as method-failure unless documented otherwise.
    3. Search-theory literature (Stone 1975) — exhaustion claims require coverage of the search space, not coverage of one query form.
    4. Bibliometric literature (Borgman 1989; Bornmann & Mutz 2015) — academic search has high query-form variance; same-week 60-day window can vary by ±50% in returns based on query form alone.
    5. C2A2-internal: ASSUMPTION-074 (carry-forward null reporting) was specifically conditioned on documented depth; PRESUMPTION-095 reuses null-acceptance without depth.

  Strength of challenge: Strong

  Summary: Single-strategy null is consistent with both exhaustion and method failure; literature is unambiguous that multi-strategy variation is the canonical disambiguation. PRESUMPTION-095 operates without that variation as an unstated default. The challenge is strong because the literature is unanimous and PRESUMPTION-status removes the prompt to vary.

  Specific risks: (a) Method failure misdiagnosed as exhaustion; (b) Phase-2 query form has ±50% variance per bibliometric literature — single-strategy null is statistically weak evidence for exhaustion; (c) compounds ASSUMPTION-084's cross-phase compensation argument.

  Mitigations available: (a) Vary query form before declaring exhaustion; (b) document Phase-2 search depth; (c) joint remediation with ASSUMPTION-084.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE

  STEELMAN:
    Item: PRESUMPTION-095
    Strongest counterargument: Bibliometric literature reports ±50% variance in returns from query-form alone for the same time window. Single-strategy null in a 60-day window is statistically weak evidence for exhaustion — it's at best evidence that one query form returned nothing, which is not the same. PRESUMPTION-095's "no fallback" stance silently elevates one query form to the standard for the whole search space, which is exactly the method-failure-misdiagnosis pattern the literature names.
    What would need to be true for C2A2 to be safe: (a) At least 2–3 query-form variations attempted before exhaustion; (b) search depth documented; (c) joint remediation with ASSUMPTION-084.
    How to test: Re-run Phase-2 with three alternative query forms; if any yields non-zero, original "exhaustion" was method-bound.
