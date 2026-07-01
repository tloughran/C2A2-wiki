SEARCH-AGAINST-PRESUMPTION-298:
  Date searched: 2026-06-03
  Original item: PRESUMPTION-298
  Original statement: [inferred] A single live spot-check generalizes to full correctness — the fade fix was verified on one isolate (`levin`) and one focus pair (`levin ~ summa`) and signed off as "works" for all isolates/foci.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-298
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an induction risk — one isolate + one focus signed off for all.
      15b: Searched when one representative case is sufficient evidence; cost of exhaustive UI verification for personal tools.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Equivalence-class partitioning as a VALIDITY argument (TestBench; Myers ch.4). — If the fade is a single uniform code path with no per-node branching, all isolates ARE one equivalence class and one representative is legitimately sufficient; the method endorses minimal cases when the partition is genuine.
    2. Cost of exhaustive UI verification (YAGNI for personal tools; smoke-testing minimal-journey guidance). — Checking every isolate/focus by hand is disproportionate for a personal visualization; 1–2 high-value cases is standard smoke practice.
    3. Implementation determines class structure. — A CSS/opacity rule applied uniformly to all nodes/edges genuinely has no boundary variation by identity; the "boundaries" 15a worries about (zero-link isolate, dense focus) may collapse to the same code path.

  Strength of challenge: Moderate

  Summary: The challenge is the mirror of 15a's: whether one spot-check suffices is entirely a function of the partition. If the fade fix is one uniform opacity rule with no identity-dependent branching, then `levin` and `levin~summa` are valid representatives and exhaustive per-isolate checking would be wasteful YAGNI for a personal tool. The presumption's risk is real ONLY if the fade logic branches on node degree, link count, or focus structure. So the disposition turns on a code fact (is the fade path uniform?) that an autonomous run can check by reading the implementation, not by more UI clicking.

  Specific risks: Over-reacting mandates exhaustive UI verification for a personal tool (wasted effort); under-reacting ships a fade bug on an unexercised boundary IF the path branches. The cost asymmetry favors a quick code-path check over either extreme.

  Mitigations available: Read the fade implementation: if it is a single uniform rule, one representative is sufficient (record that justification); if it branches, add cases at the branch boundaries (zero-link isolate, max-degree focus). Cheap and decisive either way.

  STEELMAN:
    Item: PRESUMPTION-298
    Strongest counterargument: For a personal visualization whose fade is a single uniform opacity rule, one isolate plus one focus pair are valid equivalence-class representatives, and demanding exhaustive per-isolate verification is wasted effort. The generalization is sound precisely when the implementation has no identity-dependent branching — which is the common case for a CSS/opacity fade.
    What would need to be true for C2A2 to be safe: The fade code path is uniform (no branching on degree/links/focus), making the tested cases genuine representatives; if it branches, boundary cases must be added.
    How to test: Read the fade function; confirm whether opacity assignment branches on per-node properties. Uniform → one case suffices; branching → test the boundaries.

  Recommendation: PARTIALLY-CHALLENGED


---

SEARCH-AGAINST-PRESUMPTION-298 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: PRESUMPTION-298
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-298
    Item type: PRESUMPTION
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

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)
