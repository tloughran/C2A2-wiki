SEARCH-AGAINST-ASSUMPTION-322:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-322
  Original statement: "PRS-triplet production = first git appearance of each (tradition, PRS-NN) in traditions/*/prs_triplets.md."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-322
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the operational definition dating PRS production to first git appearance
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kalliamvakou et al. 2014, "The Promises and Perils of Mining GitHub" (MSR) — first-commit timestamps are unreliable creation markers: history is rewritten (rebase/squash), content is often authored elsewhere and landed in one commit, and the commit date can postdate or batch the real creation. Challenges "first git appearance = production event."
    2. Construct-validity caution (Cronbach & Meehl 1955) — equating a construct ("production") with a single convenient operation ("first appearance in one file") risks construct underrepresentation: creation involves drafting/iteration that the first-commit instant collapses to a point.
    3. Software-evolution dating — "introduction" in version history can lag conceptual creation (work done before the file is tracked) or precede completion (a stub committed first); the first-appearance instant is not the production event for iteratively-authored artifacts.

  Strength of challenge: Moderate

  Summary: The first-git-appearance rule is a convenient operationalization but the MSR literature explicitly warns it is a noisy proxy for creation: rebases/squashes rewrite when things "first appear," content authored out-of-band lands as a single late commit, and stubs can appear before the triplet is really produced. So "production = first appearance" conflates a capture event with a creation event. The rule is fine as a defined, reproducible PROXY; it is challenged as an EQUALITY ("production =").

  Specific risks: A yield series dated to first-appearance can misplace or compress real production (batch landings inflate a day; pre-VCS work is invisible), and any downstream rhythm/velocity reading inherits the error.

  Mitigations available: Label the metric "first tracked appearance," not "production"; cross-check against author-date and against out-of-band drafts; flag batch/squashed commits; treat the series as a proxy with a stated resolution boundary (consistent with prior MONITOR-346/348 on commit-timestamp fidelity).

  STEELMAN:
    Strongest counterargument: For a born-in-repo artifact whose only existence is its committed file, first appearance in the authoritative store IS its creation in any operational sense that matters — there is no truer creation event to appeal to, so the equality is not a conflation but a definition, and demanding a "real" creation moment behind the git record is metaphysics the metric does not need.
    What would need to be true for C2A2 to be safe: PRS triplets are genuinely born-in-repo (no pre-VCS drafting, no out-of-band authoring), and history is not rewritten in ways that move first-appearance off the true landing.
    How to test: Audit a sample of triplets for pre-commit drafts and for rebased/squashed history; compare author-date vs commit-date; check for batch landings.

  Search scope: MSR creation-dating reliability (Kalliamvakou 2014); construct underrepresentation; software-evolution introduction dating. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED


---

SEARCH-AGAINST-ASSUMPTION-322 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-322
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-322
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15b (cycle 1, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)
