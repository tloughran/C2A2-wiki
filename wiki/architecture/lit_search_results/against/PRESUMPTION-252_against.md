SEARCH-AGAINST-PRESUMPTION-252:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-252
  Original statement: The "approved" status counter for proposals is silently misaligned with the underlying tradition-wiki state — 34 of 131 approved (26%) are not yet in the tradition wikis; "approved" reads as "ingested" but means "approved and possibly-ingested-or-not."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-252
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced.
      15b: Searched for challenging literature on status-field semantic-drift / Goodhart on approval counters.
    Current status: NO-CHALLENGE-FOUND (Weak — the challenge to the presumption is weak; the presumption is largely sustained)

  Sources:
    1. Counter-case: Stage-throughput tracking literature (Lean) — stage metrics are LEGITIMATE in their own right; "approved" can be a valid metric distinct from "ingested" if both are reported.
    2. The 26% gap is one observation; some delay between approval and ingest is normal in any pipeline (Forsgren et al. 2018).
    3. C2A2-internal: the 2026-05-26 commit closed a 36-file backlog, demonstrating that the lag does eventually close.

  Strength of challenge: Weak

  Summary: The challenge to the presumption is weak. The presumption's central claim (silent decoupling + headline-conflation Goodhart pattern) is well-supported by FOR-direction sources. The strongest counter is "stage-metrics are legitimate" — but that argument only succeeds if BOTH stages are reported, which is precisely what the presumption challenges.

  Specific risks (if the presumption is wrong): (a) Over-correcting via collapsed-state-machine that forces approval and ingest to be atomic adds rigidity; (b) the headline-framing risk may be smaller than the presumption suggests if reviewers are aware of the lag.

  Mitigations available: (a) Report both metrics explicitly; (b) atomic approval+ingest only where engineering supports it; (c) display the lag prominently.

  Recommendation: NO-CHALLENGE-FOUND (the presumption stands)

  STEELMAN:
    Item: PRESUMPTION-252
    Strongest counterargument (to the presumption): Stage metrics are legitimate; reporting "approved" is not silently misleading if the lag is visible. The gap closed on 2026-05-26 demonstrates the pipeline does eventually true-up.
    What would need to be true for C2A2 to be safe (if relying on the current approach): Both "approved" and "ingested" counts visible prominently in any headline framing; lag actively monitored; commit cadence reliable enough that the gap stays bounded.
    How to test: Survey daily reports — does "approved" appear without "ingested"? If yes, surrogation risk is active.
