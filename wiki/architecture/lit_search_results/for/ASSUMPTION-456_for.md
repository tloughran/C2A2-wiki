SEARCH-FOR-ASSUMPTION-456:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-456
  Original statement: A task with a current lastRunAt is presumed to have produced a valid, non-empty output artifact; firing is read as success, so the watchdog called 07-14 healthy while four tasks crashed mid-response and wrote nothing.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-456
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15a: Searched for supporting literature; result SUPPORTED (strength Strong)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Liveness vs correctness literature (PulsAPI 'Heartbeat vs Health Check' 2024; SRE School 2026): a heartbeat/lastRunAt answers 'did it run?' not 'did it produce correct output?'; conflating the two is the canonical monitoring error.
    2. Gray-failure literature: a component that fires but produces nothing passes liveness checks while the user-visible outcome silently breaks - only a correctness/artifact check exposes it.

  Strength of support: Strong

  Summary: Strongly supported. The distinction between liveness (fired) and correctness (produced a valid artifact) is foundational in monitoring literature, and reading lastRunAt as success is precisely the mistake that lets gray failures through. The 07-14 event - four crashes that fired and wrote nothing while the watchdog reported healthy - is a textbook instance. This is the firing-health family at the detector itself.

  Caveats: EMPIRICAL: comparing the set with current lastRunAt against the set that produced a valid artifact is a one-day check; the four 07-14 crashes are a ready sample.

  Recommendation: SUPPORTED
