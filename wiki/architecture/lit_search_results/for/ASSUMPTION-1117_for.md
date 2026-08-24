SEARCH-FOR-ASSUMPTION-1117:
  Date searched: 2026-08-17
  Original item: ASSUMPTION-1117
  Original statement: A monitoring cadence tick records nothing about the monitored item. Two
    disjoint draws: 17 of 17 items reported "stable, no new sources" had new material once searched.
    "The variable is the search, not the time."
  Risk if wrong: **High**.
  Search question (as queued): condition-based versus time-based maintenance; surveillance-interval
    evidence in screening; polling versus event-driven monitoring; the empirical basis for re-check
    intervals in systematic-review updating.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is already in corrective polarity. This
  file searched FOR it as stated, in four clauses:
    (C1) A CALENDAR TICK IS NOT AN OBSERVATION. Time-based intervention carries information only where
         the hazard is a function of elapsed time; where it is not, the schedule is uninformative by
         construction, and the maintenance discipline has said so since 1978.
    (C2) FIXED RE-CHECK INTERVALS MISS EVENTS BETWEEN TICKS AT MEASURED, NON-TRIVIAL RATES, and the
         miss rate grows with the gap — the interval has a measurable cost.
    (C3) IN THE FIELD THAT MOST CLOSELY MATCHES C2A2'S TASK — keeping a literature-derived summary
         current — THE DISCIPLINE HAS MOVED OFF FIXED INTERVALS to signal-triggered and continuous
         surveillance, because the time-to-obsolescence distribution is too wide for any single
         interval to be right for more than a minority of items.
    (C4) A "NO CHANGE" REPORT NOT BACKED BY A PERFORMED OBSERVATION IS NOT A NULL RESULT, IT IS A
         MISSING ONE, and conflating the two is a named error.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1117
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from two disjoint draws — 17/17 items reported "stable, no new sources" had new
        material once searched.
      15a: Register pre-check, then searched for supporting literature on the stated proposition.
    Current status: SUPPORTED (Strong)

  REGISTER CHECK (grep for: cadence, interval, polling, condition-based, clock, decay, expiry,
  re-audit, stale, monitor):
    - **PREMISE-154** (2026-08-13, ACTIVE) — the closest neighbour by a distance, containing the
      item's conclusion in almost its wording: "**the discharging mechanism must be TRIGGER-BOUND, NOT
      A CLOCK.** Time-based expiry and scheduled full re-audit are the specific remedies with the
      worst documented record in the nearest analogous domain ... a repeated re-audit prompt ... is
      predicted by the alert-fatigue evidence to become a rubber stamp within a few cycles, **which
      manufactures a false record of having looked**." It also records, explicitly as NOT
      INCORPORATED: "**No located source supports a decay model on the clock and none supplies a
      correct interval; every domain sets its own by risk tier.**"
    - **PREMISE-110** (2026-07-20, ACTIVE) — the fail-open / stuck-at-nominal family;
      "absence-of-complaint is an unsafe polarity for a health signal."
    - **PREMISE-133** (ACTIVE, via 154) — a suspension must name what would discharge it.
    CONCLUSION: **HIGH OVERLAP — PREMISE-154 PREDICTED THIS EXACT OBSERVATION FOUR DAYS BEFORE IT WAS
    MADE. NO NOVELTY-FLAG.** The disposition should be a **confirmation and scope-extension of
    PREMISE-154 from the deferral/queue cohort to the monitoring cohort**; minting again is barred by
    PREMISE-138(1)/PREMISE-135. Two genuine residuals:
      (R1) **154 IS ABOUT DISCHARGE; 1117 IS ABOUT OBSERVATION.** Same shape, different object, and
           154's Applicable-to does not reach the monitoring cohort.
      (R2) **1117 SUPPLIES THE MEASUREMENT 154 SAID WAS MISSING.** 154 declined a clock-decay model
           because no source supplied a correct interval; 17/17 across two disjoint draws is in-system
           evidence that for *this* cadence the interval is not merely wrong but non-operative — the
           reports were not searches.
    DECLARED LIMITATION: grep at ~56% recall (ASSUMPTION-1052); overlap likely larger.

  Supporting evidence found: Yes

  Sources:
    1. **Nowlan, F.S. & Heap, H.F. (1978), *Reliability-Centered Maintenance*, United Airlines /
       U.S. DoD (AD-A066579).** — **Support for (C1), and the founding document of the condition-based
       position.** Across the studied fleet, **only ~11% of items exhibited an age-related wear-out
       pattern for which a scheduled overhaul interval could be effective; ~89% did not.** The
       doctrinal consequence, which is 1117's claim in maintenance vocabulary: **for a component whose
       hazard is not a function of elapsed time, a time-based intervention cannot reduce failure and
       can increase it** (reintroducing infant mortality at each overhaul). The replacement is
       on-condition maintenance — act on a measured indicator, not on the calendar.
       [SNIPPET LEVEL — the DAU and Reliabilityweb hosted PDFs were **located this run and not
       opened**; the 11/89 split is from retrieved summaries and established knowledge. **CARRY THE
       CRITIQUE (caveat b): the 89% figure is actively disputed** — retrieved critiques (Accendo
       Reliability; ReliaMag; Acuitas) argue the sample was parts removed at fixed intervals, so
       wear-out beyond that interval was unobservable, and that the figure has been over-generalised
       across industries. Both finding and objection were retrieved this run.]
    2. **Shojania, K.G., Sampson, M., Ansari, M.T., Ji, J., Doucette, S. & Moher, D. (2007), "How
       Quickly Do Systematic Reviews Go Out of Date? A Survival Analysis," *Annals of Internal
       Medicine* 147(4):224–233.** — **Support for (C3), and the most transferable quantitative result
       here.** Survival analysis of 100 quantitative systematic reviews (1995–2005), with a "signal
       for updating" defined as a change in statistical significance or a ≥50% relative change in
       effect magnitude on a primary outcome. **50% of reviews were out of date within 5.5 years; 23%
       within 2 years.** The distribution is the point: **shorter survival was associated with
       cardiovascular topics and with heterogeneity in the original review** — obsolescence is
       predicted by *properties of the item*, not by elapsed time alone. **A single cadence applied
       uniformly is therefore wrong for nearly every item, in one direction or the other.**
       [SNIPPET LEVEL — ACP Journals page and the AHRQ "Identifying Signals for Updating Systematic
       Reviews" Bookshelf record read at retrieved-summary level; **neither opened.** Authors, journal,
       year, volume and pages confirmed; figures reported as retrieved.]
    3. **Elliott, J.H. et al. (2014), "Living Systematic Reviews: An Emerging Opportunity to Narrow
       the Evidence-Practice Gap," *PLOS Medicine* 11(2):e1001603; Elliott et al. (2017), "Living
       systematic review: 1. Introduction," *J. Clin. Epidemiol.*; Garner, P. et al. (2016), "When and
       how to update systematic reviews: consensus and checklist," *BMJ* 354:i3507.** — **The
       disciplinary response and the shape of the remedy 1117 implies.** A living systematic review is
       one "continually updated, incorporating relevant new evidence as it becomes available" — the
       explicit replacement of a scheduled re-issue by **continuous surveillance with a stated search
       frequency and a stated incorporation trigger**. Garner et al. frame updating as a judgement
       about the currency of the evidence and the likely impact of new evidence on conclusions —
       condition-based — and supply a checklist rather than an interval.
       [SNIPPET LEVEL — PLOS Medicine, JCE and Cochrane Methods slides located; **none opened.** The
       definition is quoted from a retrieved summary; the BMJ article number is from established
       knowledge — confirm before quoting.]
    4. **Interval-cancer evidence in population mammography screening (Houssami, N. & Hunter, K.
       (2017), "The epidemiology, radiology and biological characteristics of interval breast cancers
       in population mammography screening," *npj Breast Cancer* 3:12; plus programme audit
       literature).** — **Support for (C2): a measurement of what a fixed re-check interval misses.**
       Interval cancers arise after a negative screen and before the next scheduled round. Reported
       magnitudes: **~30% of breast cancers in screened populations, a proportion roughly constant
       across three decades of technology improvement**; rates of 7.0–49.3 per 10,000 screens across
       programmes, **<8 per 10,000 for annual screening or year 1 of a biennial programme, rising to
       8.4–21.1 per 10,000 across the two years of a biennial programme, with a larger proportion in
       the second year.** Two findings transfer: **the miss rate is a function of the gap**,
       concentrated at its far end; and **better instruments did not fix it** — the proportion stayed
       flat while technology changed, which is "the variable is the search, not the time" in another
       register.
       [SNIPPET LEVEL — the npj paper, a PMC interval-cancer audit survey and a JCO 2025
       screening-interval paper read at retrieved-summary level; **none opened.** All figures as
       retrieved; the 30% figure comes from a secondary summary — re-check before quoting as a
       headline.]
    5. **Nyquist–Shannon sampling theorem, and aliasing.** — The formal limit behind (C1): a periodic
       sampler cannot resolve change faster than half its sampling rate, and faster change is
       **aliased** — reported as something else. For a monitoring cadence this is the strongest form
       of the item's claim: a fixed tick has structural blindness against fast-changing items, and its
       artefact is a *plausible wrong reading* rather than a gap.
       [CANONICAL — cited from established knowledge, **NOT verified this run**; no sampling-theory
       source retrieved. A pointer and an argument, not a finding. **The transfer is loose**: the
       theorem governs bandlimited signals, and "new sources appearing" is a point process; the
       correct apparatus would be renewal theory or a Poisson-arrival model, not searched.]
    6. **Altman, D.G. & Bland, J.M. (1995), "Absence of evidence is not evidence of absence," *BMJ*
       311:485.** — **(C4), and the cleanest statement of what 17/17 demonstrates.** "Stable, no new
       sources" is not a null observation but a *missing* one wearing the costume of a null. The
       distinction matters because a null carries a denominator (how hard did you look) and a missing
       value does not, so they cannot be aggregated.
       [CANONICAL — cited from established knowledge, **NOT verified this run**; journal, year and
       volume from memory. Doing conceptual rather than evidential work.]
    7. **Register: PREMISE-154 and PREMISE-110.** See the REGISTER CHECK.
       [**ALREADY REGISTER-HELD — no independent external weight**, and the strongest reason for a
       narrow disposition.]

  Strength of support: **Strong** on (C1), (C3), (C4); **Moderate-to-Strong** on (C2).
    (C1) rests on the founding empirical study of an entire engineering discipline whose *doctrine* is
    uncontested even where its headline number is disputed — nobody argues time-based intervention
    helps where the hazard is time-independent. (C3) is the strongest transfer: same task, measured,
    and the field's own response was to abandon fixed intervals. (C4) is definitional. (C2) is
    downgraded because screening figures are heterogeneous across programmes, were read only at
    summary level, and trade a miss rate against over-screening harms with no C2A2 analogue.
    **The item's own evidence should not be understated: 17/17 across two disjoint draws, with a
    two-sided exact 95% interval of roughly [0.80, 1.00] on the "tick was uninformative" proportion,
    is consistent with the ticks carrying no information at all.** The literature explains *why* that
    is the expected result; it does not have to establish it.

  Summary: The item is well supported, and the strongest support is that the register predicted it.
  PREMISE-154 recorded on 2026-08-13 that a discharging mechanism must be trigger-bound rather than
  clock-bound, and that a repeated scheduled re-audit "manufactures a false record of having looked";
  1117 is that prediction landing in a different cohort four days later. Outside the vault the
  position is settled in three independent fields. Maintenance engineering established in 1978 that
  scheduled intervention is effective only against age-related wear-out, found such patterns in a
  small minority of items, and replaced the calendar with on-condition action. Screening programmes
  measure what a fixed interval misses and find both that the miss rate is a function of the gap and —
  the finding that transfers hardest — that three decades of better instruments did not change the
  proportion of cancers arising between screens. Most directly, the field whose task is C2A2's task
  measured the time-to-obsolescence distribution, found it so wide (23% within two years, 50% within
  5.5) and so predicted by properties of the item rather than by elapsed time that the discipline
  moved to living reviews with continuous surveillance and signal-based triggers. What 1117 adds is
  not the principle but a stronger fact: in this system the ticks were not merely mistimed, they were
  **empty** — 17 of 17 "stable, no new sources" reports were false on first contact with an actual
  search. That is not a wrong interval. It is a report generated without an observation, and its
  correct category is Altman and Bland's: absence of evidence recorded as evidence of absence.

  Caveats:
    (a) THIS IS SUBSTANTIALLY PREMISE-154 IN A NEW COHORT. Per PREMISE-151, a second recording of an
        unremediated condition is evidence of **incubation, not confirmation**. Disposition should be
        a scope-extension, not a new premise.
    (b) THE 89% FIGURE IS CONTESTED AND MUST NOT BE QUOTED BARE. The retrieved critiques are
        substantive: the sample consisted of parts removed at fixed intervals, so wear-out beyond that
        interval was unobservable by construction, and the figure has been over-extended to plant with
        very different failure physics. **What survives the critique is the doctrine, not the
        number** — and the doctrine is what 1117 needs.
    (c) THE ITEM OVERSHOOTS IF READ AS "CADENCE IS USELESS." Every source replaces a fixed interval
        with something that still has a frequency: living reviews specify a search frequency;
        on-condition maintenance specifies an inspection frequency for the condition indicator. **The
        supported claim is that the tick must carry a performed observation and a recorded search
        scope**, not that scheduling is wrong. Abolishing cadence without installing a trigger would
        leave items unwatched.
    (d) 17/17 IS SMALL AND POSSIBLY NON-RANDOM. The two draws being disjoint is the strongest feature
        of the evidence, but nothing establishes the 17 were selected without regard to suspicion. If
        they were drawn because they looked stale, the rate is inflated. **Cheapest fix: record the
        draw method.**
    (e) DOMAIN TRANSFER FROM SCREENING CARRIES A COST TERM C2A2 LACKS. Screening intervals are set
        against over-diagnosis, dose and anxiety; C2A2's only cost of searching more often is compute
        and attention. **The optimal-interval literature does not transfer, only the miss-rate
        structure does.** Do not import an interval.
    (f) SOURCE VERIFICATION IS WEAK THROUGHOUT. **No source in this file was opened and read in
        full**, and sources 5 and 6 were not retrieved at all.

  Search scope: GOOD breadth across the four requested angles, **but shallow**. NOT SEARCHED, each
    material: (i) **polling versus event-driven monitoring in the systems literature proper** — the
    queue asked for it and the search returned nothing usable (push vs pull, webhook/watch APIs, the
    cost model in continuous distributed monitoring) — a clearly-labelled negative result; (ii)
    **renewal-process / Poisson-arrival treatment of what a periodic check misses when arrivals are a
    point process**, the correct formalism, which would replace the loose Nyquist analogy in source 5;
    (iii) **the AHRQ "signals for updating" methodology** (Bookshelf NBK56777, located but not
    opened) — the operational checklist form of (C3) and the most directly reusable artefact
    identified this run; (iv) **alert-fatigue evidence on scheduled re-audit prompts**, already cited
    by PREMISE-154 and not re-searched here.

  Recommendation: **SUPPORTED (Strong)**, with a narrow disposition.
    1. NO NEW PREMISE. Extend **PREMISE-154** from the deferral/queue cohort to the monitoring cohort:
       *a monitoring tick must be trigger-bound or observation-backed; a clock alone discharges
       nothing and records nothing.*
    2. MAKE THE TICK CARRY ITS SEARCH. A "stable, no new sources" report must record **what was
       searched, over what window, with what query** — or emit the non-applicable value
       ASSUMPTION-1106 argues for rather than a null. Without a recorded search scope the report has
       no denominator and cannot be aggregated (Altman & Bland).
    3. STRATIFY CADENCE BY ITEM PROPERTY, NOT BY CALENDAR. Shojania et al. find obsolescence predicted
       by topic volatility and by heterogeneity in the original — properties knowable at writing time.
       A per-item volatility tier is the supported design and is cheaper than uniform re-checking.
    4. RECORD THE DRAW METHOD FOR THE 17. One sentence; raises the item's own evidence from suggestive
       to decisive.
    5. DO NOT IMPORT AN INTERVAL FROM ANY OF THESE SOURCES. PREMISE-154 already recorded that no
       located source supplies a correct interval. This search found nothing to change that — and
       found the reason: the time-to-obsolescence distribution is too wide for one interval to be
       right for most items.
