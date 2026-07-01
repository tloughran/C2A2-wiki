SEARCH-AGAINST-ASSUMPTION-249:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-249
  Original statement: ISME is now ~5.5 weeks out; demo-path-shaped work is the prioritization tiebreaker.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-249
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on demo-path heuristic biases and ISME-deadline negotiability.
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Challenging evidence found: Partial

  Sources:
    1. Brooks (1975) — Documents that demo-driven prioritization systematically de-prioritizes load-bearing infrastructure; the dimensional bias is documented.
    2. DeMarco & Lister (1987) "Peopleware" — Demo-orientation produces visible-progress bias; non-visible work (infrastructure, testing, refactoring) is under-resourced.
    3. Goldratt (1984) — While ToC supports deadline-orientation, it explicitly warns against optimizing-for-the-visible at the expense of the actual bottleneck.
    4. Heath & Heath (2013) "Decisive" — Documented bias: "what's available to demo" anchors decisions even when other work is higher-value.
    5. C2A2-internal: REVISE-056, REVISE-057, REVISE-058 (PRS-extraction backlog, ingest-state gap, route-rate-fact) are all non-demo load-bearing items that the demo-path tiebreaker can systematically defer.

  Strength of challenge: Weak-Moderate

  Summary: Demo-path tiebreaking IS supported (15a) for true tiebreakers, but the LITERATURE on demo-driven bias is robust. Brooks, DeMarco & Lister, Goldratt, and decision-science all document that "demo-path-shaped" framing systematically obscures non-visible load-bearing work. The current C2A2 backlog (FLAG-I cluster: PRS-extraction, ingest, route-rate) is precisely the non-demo work that demo-tiebreaking can defer. The challenge is not to deadline-orientation but to demo-path AS the tiebreaker.

  Specific risks: (a) Non-demo FLAG-I cluster work (REVISE-056..058) systematically deferred; (b) post-ISME the deferred load-bearing work emerges as compounded debt; (c) demo-path tiebreaker becomes the cover for the binary-framing pattern (PRESUMPTION-267); (d) ISME deliverables ship but on top of un-remediated foundations.

  Mitigations available: (a) Use demo-path AS one tiebreaker among several (load-bearing weight, FLAG-I exposure, etc.); (b) reserve N% of pre-ISME capacity for non-demo load-bearing work; (c) explicit accounting for what demo-tiebreaking is deferring.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate)

  STEELMAN:
    Item: ASSUMPTION-249
    Strongest counterargument: Demo-driven prioritization literature (Brooks, DeMarco & Lister, Goldratt) consistently documents that "what's demo-able" anchors decisions even when non-demo work is the actual bottleneck. C2A2's own active FLAG-I cluster (REVISE-056/057/058) is the direct internal example of non-demo work that demo-tiebreaking can defer. The 5.5-week window may ship a presentation atop unremediated foundations.
    What would need to be true for C2A2 to be safe: Demo-path is one of multiple tiebreakers; non-demo load-bearing work gets reserved capacity; explicit "what's being deferred" log per prioritization decision.
    How to test: Track FLAG-I cluster items deferred to post-ISME; audit at ISME-end for compounded-debt emergence.


---

SEARCH-AGAINST-ASSUMPTION-249 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-249
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-249
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15b (cycle 3, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED (Weak-Moderate))
