SEARCH-AGAINST-PRESUMPTION-972:
  Date searched: 2026-09-13
  Original item: PRESUMPTION-972
  Original statement: "[inferred] That an empty 30- or 60-day window is evidence about a research
    tradition's activity, rather than about a single source's availability. The Wolfram specialist had
    to argue explicitly that a seven-week silence following a bereavement 'reflects that hiatus, not a
    quiet research program.'"

  READ-CHANNEL INDEPENDENCE ATTESTATION, AND ITS LIMIT: I did not read
    `architecture/lit_search_results/for/`, any 15a output, or `lit_search_returns.md` at any point in
    this run. Per PREMISE-111 (ACTIVE) that closes the weakest of at least four correlation channels
    and is not independence. See `PRESUMPTION-975_against.md` for the mechanism actually used.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-972
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the fact that the argument had to be made at all, and from the absence of any
        status in the hunt's vocabulary between active and quiet. Four traditions were read as quiet
        today under that vocabulary.
      15b: Searched for the statistical and bibliometric basis of silence-window inference and for
        career-interruption base rates; computed the window's false-positive rate directly rather than
        relying on a cited figure; re-ran the register pre-check and found **two ACTIVE covering
        premises the intake's pre-check did not report**.
    Current status: CHALLENGED

  REGISTER PRE-CHECK — **the intake's pre-check is WRONG, and the correction is the most important
    thing in this file.** The intake states: "grepped for `recency`, `window`, `dormant`, `cadence` —
    **PREMISE-154 bears adjacently** (on non-yielding cards) but does not cover the active/dormant
    distinction." **Two ACTIVE premises cover it, and one of them covers it in general form.**
    - **PREMISE-141 (ACTIVE, Confidence High, validated 2026-08-05, re-check due 2026-09-05 — 8 days
      overdue)** — decisive, and it is the generalisation the intake says does not exist. Clause (1),
      read verbatim: "ABSENCE OF A REPORT IS A THIRD TERMINAL STATE, NOT A VALUE OF THE OTHER TWO...
      C2A2's scheduled-run data model is two-valued and therefore CANNOT REPRESENT what was observed...
      Until the model carries a third state ... **each reader supplies the missing value from their own
      prior, and nothing downstream can distinguish work not done from work done and discarded.**"
      PRESUMPTION-972 is that sentence with "scheduled run" replaced by "research tradition" and
      "verdict" replaced by "publication." The intake's own phrasing — "the absence of any status in
      the hunt's vocabulary between active and quiet" — is a two-valued model, which is exactly what
      141 says cannot represent an omission. **The estate does not need a new premise here; it needs
      141 enforced in a second subsystem.** 141 already records itself as the finding that PREMISE-086
      "is not enforced for scheduled agent sessions"; this is the third subsystem where it is unenforced.
    - **PREMISE-089 (ACTIVE, validated 2026-06-30, re-check due 2026-09-06 — 7 days overdue)** — covers
      the item's second limb exactly. Read verbatim: "Freshness/liveness is a per-source property; the
      liveness of any one feed ... must never be taken as evidence for the liveness of another. Each
      axis requires its own freshness signal." The supporting evidence line records that "cross-source
      liveness inference is a **known anti-pattern**." The item's claim — that the window is evidence
      about "a single source's availability" rather than about the tradition — is the per-source
      doctrine restated. 089's refinement also pre-empts the obvious fix: "freshness-independence does
      NOT imply failure-independence — feeds sharing an upstream scheduler can freeze together," which
      in the hunt's case means the four traditions read as quiet today may be one search-layer event,
      not four findings.
    A grep for `dormant` and `cadence` would not surface either premise; a grep for `absence`,
    `liveness`, `freshness`, or `per-source` would surface both. This is the keyword-matching failure
    ASSUMPTION-1343 names, occurring in a pre-check that claims to have performed the correction.
    Routed to the SYSTEMIC-RISK-FLAG.

  Challenging evidence found: **Yes — decisively, and the decisive part is arithmetic rather than
    citational.**

  Sources:
    1. **THE FALSE-POSITIVE RATE OF AN EMPTY WINDOW — MY OWN COMPUTATION, NOT A CITATION.** Labelled
       as such so it is never later quoted as a retrieved figure. Under the *most favourable possible*
       model for the hunt — homogeneous Poisson arrival, which assumes away burstiness — the
       probability that a genuinely active program emits **nothing** in a window of length *d* days at
       rate *k* outputs/year is exp(−dk/365):

         outputs/yr (k)   P(empty 30-day window)   P(empty 60-day window)
              6                   0.61                     0.37
             12                   0.37                     0.14
             24                   0.14                     0.019

       A program producing one significant output a month — a high rate for any of the fourteen
       traditions — is silent across a 30-day window **37% of the time** and across a 60-day window
       **14% of the time**, while being maximally active. At six outputs a year the 30-day window is
       empty **more often than not**. The test does not have the discriminating power the vocabulary
       assumes, and this is true before any bereavement, any embargo, and any search-layer gap. Four
       traditions read as quiet on one day is well inside what this table predicts from arrival
       statistics alone. **Arithmetic checked; exp(−0.493)=0.611, exp(−0.986)=0.373, exp(−1.973)=0.139,
       exp(−3.945)=0.0194.**
    2. Barabási, A.-L. (2005), "The origin of bursts and heavy tails in human dynamics," *Nature*
       435:207–211, doi:10.1038/nature03459. — **VERIFIED** (abstract retrieved and read directly from
       nature.com this run). Read verbatim: "Current models of human dynamics, used from risk
       assessment to communications, assume that human actions are randomly distributed in time and
       thus well approximated by Poisson processes. In contrast, there is increasing evidence that the
       timing of many human activities ... follow non-Poisson statistics, **characterized by bursts of
       rapidly occurring events separated by long periods of inactivity**" — the mechanism being a
       decision-based queuing process in which "most tasks [are] rapidly executed, whereas a few
       experience very long waiting times." **This makes source 1's table a lower bound.** Under
       heavy-tailed inter-event times, long silences are strictly *more* probable than the Poisson
       calculation gives, so the real false-"quiet" rate is worse than 37–61%. It also supplies the
       positive characterisation the hunt's vocabulary lacks: a long gap is not an anomaly requiring
       explanation, it is the modal shape of productive human work.
    3. Kwok-style bibliometric coverage divergence: Visser, van Eck & Waltman, and Martín-Martín et al.
       (2021), *Scientometrics*, on coverage overlap across Google Scholar, Scopus, Web of Science,
       Microsoft Academic, Dimensions and COCI. — **UNVERIFIED** (search-layer summaries only; no
       primary retrieved). Reported: Microsoft Academic found 82% of Scopus and 86% of WoS citations;
       Dimensions found 98% of COCI; unique-citation proportions vary by source. **No figure from this
       source is used in the rating.** What it establishes structurally, and all that is claimed here,
       is that "what a database shows in a window" is a property of the database. Under PREMISE-089
       that is already in-house doctrine.
    4. Publication lag: Björk & Solomon (2013), "The publishing delay in scholarly peer-reviewed
       journals," *J. Informetrics*; and the biomedical systematic-review literature on
       submission-to-publication time. — **UNVERIFIED** (search-layer summaries only; neither primary
       retrieved; the sciencedirect page was not fetched). Reported: mean submission-to-publication of
       roughly twelve months across fields and just over fourteen in the social sciences, with
       discipline ranges from ~2.5 to ~34.6 months. **The figures are NOT used.** The structural point,
       which does not depend on the exact number, is that the *signal* the hunt samples lags the
       *activity* it wants to measure by roughly a year, so a 30-day window is measuring a year-old
       state of the world through a one-month aperture. Anyone wishing to cite a lag figure must
       re-fetch the primary.
    5. Career-interruption base rates: Morgan, Way, Hoefer, Larremore, Galesic & Clauset (2021), "The
       unequal impact of parenthood in academia," *Science Advances* 7:eabd1996; plus survey work on
       caregiving prevalence among faculty. — **UNVERIFIED** (search-layer summaries only; primaries
       not retrieved). Reported: from a survey of 3,064 tenure-track faculty across 450 departments,
       parenthood lowers short-term productivity, with roughly **five years** for mothers' output to
       recover to the comparison trajectory; and ~19% of faculty aged 55+ report ongoing caregiving.
       **No figure is used in the rating and none should be until re-fetched.** The direction is what
       matters: interruptions that suppress *output* for multiple years while the *program* continues
       are common enough to be studied at population scale, which means the Wolfram case is not an
       exception the hunt got unlucky on — it is a draw from a well-populated distribution.
    6. **EXPLICITLY EXCLUDED.** The search layer offered several aggregate claims about academic
       career breaks with no retrievable methodology. None is recorded here even as UNVERIFIED,
       because the 2026-09-12 cycle was burned by exactly that. If the estate wants a career-break
       base rate it must commission the retrieval.

  Strength of challenge: **Strong** on the inferential claim; **Strong** and in-house on the
    vocabulary claim; **Moderate** on quantifying the base rate.

    Limb split:
      - "An empty window is evidence about the tradition's activity": **Strong** challenge. Source 1
        shows the test's false-"quiet" rate against genuinely active programs is 37–61% at plausible
        output rates, and source 2 shows that number is a lower bound. A test whose false-positive rate
        exceeds a third is not evidence in any operative sense; the classification is dominated by the
        reader's prior, which is PREMISE-141's sentence.
      - "The vocabulary needs a third state": **Strong**, and it is already settled in-house.
        PREMISE-141 is ACTIVE at High confidence and says absence is a third terminal state. The
        finding is an enforcement gap in the hunt, not a knowledge gap.
      - "It is about a single source's availability": **Strong**, and also settled in-house.
        PREMISE-089 forbids cross-source liveness inference and names it a known anti-pattern; the
        external bibliometric-coverage literature (source 3, unverified) points the same way.
      - "Career interruption is common enough to be the default hypothesis": **Moderate** challenge —
        directionally supported by sources 4 and 5 but **I have no verified base rate** and am not
        supplying one. This is the limb where a broader search would help.
      - The one thing the item gets right and which no source disputes: silence over a **long enough**
        window, per-source, with the observer's own liveness verified, genuinely is informative. The
        challenge is to 30 and 60 days, not to the idea.

  Summary: The inference is not weakly supported; it is arithmetically unsound at the window lengths in
    use. Even granting the most generous arrival model, a tradition producing six significant outputs a
    year will show an empty 30-day window more often than not, and one producing an output a month will
    show an empty 60-day window 14% of the time — and Barabási's result, verified from the primary,
    establishes that human productive activity is bursty rather than Poisson, so those figures
    understate the true rate of false "quiet" verdicts. Layered on top are a publication lag of roughly
    a year between activity and signal, source-coverage divergence that makes the window partly a
    property of the database, and a career-interruption literature large enough to be studied at
    population scale. None of this is new to the estate: PREMISE-141 already holds, at High confidence,
    that absence of a report is a third terminal state which a two-valued model cannot represent, and
    PREMISE-089 already forbids inferring one feed's liveness from another's. The intake's pre-check
    reported no covering premise; both premises are ACTIVE, both are overdue for re-check, and the
    grep terms chosen could not have found either.

  Specific risks:
    - **Four traditions were classified as quiet today on a test with a false-positive rate above a
      third.** Whatever downstream allocation follows from "quiet" — reduced monitoring, lower
      priority, a narrative of decline — has been applied to a set that, on the arithmetic, probably
      contains at least one and plausibly two active programs.
    - **The error is systematically biased, not noisy.** Silence windows misclassify in one direction
      only: they never report a dormant program as active. So repeated application does not average
      out; it accumulates a monotone drift toward "the field is quiet," which is indistinguishable from
      the hunt losing coverage.
    - **PREMISE-089's refinement predicts correlated misclassification.** If the four traditions were
      read through one search layer on one day, that is potentially one event wearing four labels —
      PREMISE-141 clause (2), correlated termination, applied to the hunt. Any count of "how many
      traditions are quiet" computed as four independent observations is then wrong in the way 141
      says such counts are wrong.
    - **Reputational exposure is asymmetric and personal.** The instance that surfaced this was a
      **bereavement**. A system that publishes "quiet research program" about a named living person
      during their leave is not making a technical error; it is making a claim about someone's working
      life from a database gap. That belongs in the risk register explicitly.
    - **Two overdue covering premises mean the estate is carrying an unenforced rule it believes is
      enforced.** PREMISE-141 (due 2026-09-05) and PREMISE-089 (due 2026-09-06) are both past
      re-check. Their status line still reads ACTIVE.

  Mitigations available:
    - **Add the third state, per PREMISE-141, and name it.** NOT-OBSERVED, distinct from ACTIVE and
      QUIET. This is a vocabulary change in the hunt's output schema and costs nothing; it is also
      already required by an ACTIVE premise, so it is enforcement rather than new policy.
    - **Publish the window's operating characteristic alongside every "quiet" verdict.** One line: at
      this window length, an active program at rate k is silent p% of the time. The table in source 1
      is the whole implementation. This converts an assertion into a measurement and makes the verdict
      self-limiting without anyone having to read a caveat — which matters, because PRESUMPTION-979
      (searched this same run) establishes that the caveat would not be read.
    - **Verify the observer before reading the observation.** Per PREMISE-089 and PREMISE-086, no
      "quiet" verdict should be emitted unless the feed for that tradition returned a non-empty result
      for *some* query in the window. Absence of results from a dead feed is not silence.
    - **Lengthen the window or change the unit.** If the hunt needs a real activity signal, sample at
      the cadence the signal actually has — 6 to 12 months for publications — or switch to a
      higher-rate proxy (preprints, talks, grants, lab-site updates) whose arrival rate makes a short
      window informative. Choosing a window without reference to the arrival rate is the actual defect.
    - **Do not import a career-break base rate.** Sources 4 and 5 are unverified here, measured on
      different populations, and would be doing the same work the estate criticised in REVISE-342. Use
      them as the reason to widen the window, not as a number.
    - **Re-check PREMISE-141 and PREMISE-089**, both overdue, and record this item as a second and
      third unenforced site for each.

  STEELMAN:
    Item: PRESUMPTION-972
    Strongest counterargument: The arithmetic is correct and beside the point, because the hunt is not
      running a hypothesis test on individual traditions — it is triaging attention under a budget, and
      for that purpose a noisy signal with a known bias is better than no signal. Any monitoring system
      must act on incomplete evidence; demanding a test with a low false-positive rate before you may
      form a provisional view is a standard that no operational triage anywhere meets, and the
      alternative on offer — lengthen the window to six or twelve months — would make the hunt blind to
      exactly the changes it exists to catch, since a tradition that genuinely goes dormant would not
      be flagged until a year after it mattered. The cost structure is also asymmetric in the direction
      opposite to the one this file assumes: a false "quiet" costs one wasted re-check next cycle, a
      false "active" costs continued allocation to a dead field, and the cheap correction for the
      former already exists and was applied — the Wolfram specialist *did* catch it, in the same run,
      by reading the case rather than the window. That is the system working. Moreover the demand for a
      third state proves less than it appears: NOT-OBSERVED is only useful if something distinguishes
      it from QUIET, and for a research tradition there is no equivalent of a heartbeat — silence from
      a person genuinely is the only signal available, so relabelling it does not add information, it
      adds a category that will be populated by the same guess under a more cautious name. And the two
      premises invoked against the item were both validated on *machine* subsystems with dead-man's
      switches available; transferring them to human research programs is precisely the domain transfer
      that 15b exists to challenge when other agents do it.
    What would need to be true for C2A2 to be safe: (a) the "quiet" verdict must genuinely be
      provisional in practice, not merely in intent — which requires showing that a tradition marked
      quiet is re-examined on a schedule and that the mark expires, and **no such expiry is in
      evidence**; (b) the catch must be systematic rather than lucky — the Wolfram case was caught
      because a specialist happened to know about the bereavement, which is not a control, it is a
      near-miss, and under the estate's own near-miss doctrine a caught error tells you nothing about
      the uncaught ones; (c) the asymmetric-cost argument must actually hold, and it does not hold for
      outbound artifacts, where a false "quiet" about a named living person is not a wasted re-check
      but a published claim about their career; (d) NOT-OBSERVED must be distinguishable from QUIET,
      and here the steelman is answerable — the distinguisher is the *observer's* liveness, not the
      subject's: did the feed return anything at all, for anyone, in this window. That is a genuine
      heartbeat and it is available. (d) defeats the steelman's strongest move; (a) and (b) are open
      and are the ones to test.
    How to test: **Retrospective labelling, cheap and decisive.** Take every tradition marked quiet in
      the last six months of hunt output (N is small and in-house). For each, run an unrestricted
      search with no date filter and record whether the program produced anything in the twelve months
      surrounding the window — preprints, talks, grants, students, lab-site changes. The proportion of
      "quiet" marks that were wrong is the empirical false-positive rate, with a denominator, per
      PREMISE-168. If it comes in near zero, source 1's table is being rescued by something real about
      how these fourteen traditions publish, and the item is refuted by the estate's own data. If it
      comes in near the 37–61% the arithmetic predicts, the vocabulary change is not optional. Second,
      smaller test for limb (a): grep the hunt's output for any tradition that was marked quiet and
      later marked active, and record the interval. If no such transition exists in the record, the
      mark is terminal in practice whatever it is in intent.

  Search scope: **Adequate on the inferential limb, preliminary on the base-rate limb.** Searched:
    human-activity burstiness and inter-event statistics, bibliographic database coverage divergence,
    publication lag, academic career-interruption prevalence, and the register itself. **One external
    primary was retrieved and read (Barabási 2005, abstract from nature.com); everything else external
    is labelled UNVERIFIED and no external figure enters the rating.** The decisive quantitative
    content is my own arithmetic and is labelled as such. **The highest-yield step was the register
    pre-check**, which found two ACTIVE covering premises the intake reported as absent. The
    under-searched limb is the career-interruption base rate: I have direction but no verified number,
    and I am reporting that as insufficient search rather than as absence of evidence. Recommended next
    step is retrieval of Morgan et al. 2021 and Björk & Solomon 2013 as primaries, and it was not done.

  Recommendation: **CHALLENGED**
