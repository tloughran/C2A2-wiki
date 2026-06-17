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
