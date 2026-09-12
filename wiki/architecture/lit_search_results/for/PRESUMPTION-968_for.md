SEARCH-FOR-PRESUMPTION-968:
  Date searched: 2026-09-12
  Original item: PRESUMPTION-968
  Original statement: "[inferred] That a search layer's date errors are incidents rather than a base
    rate."

  READ-CHANNEL INDEPENDENCE ATTESTATION (PREMISE-111 / PREMISE-197):
    I did not read `architecture/lit_search_results/against/` at any point in this run, and did not read
    any 15b output for this item or any other. Agreement between this file and 15b's is not independent
    confirmation and carries PREMISE-111's standing discount.

  DIRECTION NOTE: "FOR" means literature supporting the presumption as stated — that date errors in a
    search layer are **isolated incidents** rather than a **standing base rate**. I searched for that
    support and did not find it. Everything located points the other way. "No support found" is a valid
    and informative result and this is one.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-968
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the estate's handling of two in-house date-error instances, each filed
        individually as an incident, with no denominator constructed and no rate implied.
      15a: Register pre-check performed; found partial pre-answer on the inferential limb only.
        Searched the external-base-rate limb, which is the limb the item was routed out for.
    Current status: NO-SUPPORT-FOUND

  Register pre-check:
    - **PREMISE-124 (ACTIVE, High — SUPPORTED + NO-CHALLENGE-FOUND)** — PARTIALLY pre-answers. Clause
      (a) holds that "a raw defect CATCH COUNT is not an estimate of defects PRESENT without
      capture-recapture or fault seeding." Two caught date errors are a catch count. 124 therefore
      already forbids inferring a rate from them — **but it forbids the inference in BOTH directions,
      and that is the point.** Two instances do not establish a base rate; neither do they establish
      that there isn't one. The presumption treats the absence of a constructed denominator as evidence
      for the incident reading, which is precisely the move 124 prohibits.
    - **PREMISE-174 (ACTIVE, Moderate-High)** — its recorded prohibition is the exact arithmetic
      analogue: the originating item's two data points "enter as 2/2 = 100%, which PREMISE-124 forbids
      quoting." Same n, same prohibition.
    - PREMISE-143 (ACTIVE, Moderate) — a count of this kind measures the producing layer. Bears on which
      layer a date-error count is about.
    - PREMISE-115 (ACTIVE, Moderate) — silent failure is the modal profile (75.17% of MAS failures emit
      no hard error signal). Bears sharply here and is the reason the incident reading is fragile: a date
      error that is never noticed produces no incident, so an incident count is a count of DETECTED
      errors and the undetected fraction is unbounded from inside.
    Recording the hits per OPEN-192. **Pre-answer status: PARTIAL.** The register already governs what
    may be inferred from n=2. It contains nothing whatever about an external base rate for retrieval
    date errors, which is why routing this item out was the right call and why I searched.

  LIMB SPLIT:
    Limb A (INFERENCE FROM n=2): pre-answered by PREMISE-124 / PREMISE-174. Not searched.
    Limb B (EXTERNAL BASE RATE): is there a measured, external rate of date/freshness metadata error in
      retrieval systems, against which two in-house instances could be read? **SEARCHED. This is the
      item.**
    Limb C (WHY DO INDIVIDUALLY-FILED NEAR-MISSES NOT PRODUCE A DENOMINATOR?): **SEARCHED**, because it
      explains the estate's filing behaviour structurally rather than treating it as an oversight.

  Supporting evidence found: **No**

  Sources:
    1. SalahEldeen, H.M. & Nelson, M.L. (2013). "Carbon Dating The Web: Estimating the Age of Web
       Resources." arXiv:1304.5213 (WWW'13 companion / TempWeb).
       — **VERIFIED at abstract level** — I retrieved the ar5iv full-text rendering
       (https://ar5iv.labs.arxiv.org/html/1304.5213) and read the abstract in full; the body exceeded my
       retrieval budget and I did not read the evaluation section, so **no accuracy figure from this
       paper is quoted here.** The abstract's structural claim is what matters and I am quoting it
       exactly: "In the course of web research it is often necessary to estimate the creation datetime
       for web resources (**in the general case, this value can only be estimated**)." Their tool polls
       multiple independent sources of evidence — bitly first-shortening, social-media first-mention,
       archive first-capture, and others — precisely because no single authoritative creation date is
       retrievable.
       **This is the strongest finding in this file and it refutes the presumption structurally rather
       than statistically.** A date error is not an event that happens to a correctly-functioning
       retrieval of a known fact. The creation datetime of a web resource is not a stored fact at all —
       it is an inference from weak evidence. Errors in an inference from weak evidence are a base rate
       by construction. There is no configuration in which they are "incidents."
    2. Ouyang, J., Pan, T., Cheng, M., Yan, R., Luo, Y., Lin, J. & Liu, Q. (2025). "HoH: A Dynamic
       Benchmark for Evaluating the Impact of Outdated Information on Retrieval-Augmented Generation."
       arXiv:2503.04800. USTC State Key Lab of Cognitive Intelligence.
       — **VERIFIED** — I retrieved https://arxiv.org/html/2503.04800v1 and read the abstract and
       introduction in full. Quoting the paper's own summary of its results: "**even when current
       information is successfully retrieved, the mere presence of outdated information in the context
       leads to at least 20% performance drop in mainstream LLMs, with some models performing worse than
       random guessing (-2.77%)**." The paper further notes that outdated facts "inevitably accumulate
       across various sources, **particularly in search engine scenarios where content is cached and
       redistributed**," and that models become "highly prone to generating confident but incorrect
       responses when encountering outdated information" while maintaining appropriate uncertainty when
       nothing is retrieved.
       **Read carefully for what it does and does not establish.** It is a measured, externally-produced,
       peer-reviewable figure for temporal error in exactly this class of system, and the ≥20% is a
       performance-degradation magnitude, not a prevalence. It is NOT a rate of date-metadata errors. But
       its framing — a benchmark, a rate, a systematic phenomenon requiring architectural remedy — is the
       opposite of an incident framing, and the field it comes from treats temporal error as a standing
       property of retrieval systems.
    3. CMS / sitemap / republication date-drift mechanisms (Search Engine Land byline-date guidance and
       related SEO-practitioner material).
       — **UNVERIFIED** — snippet level across several practitioner sources; I retrieved none. Reported
       mechanisms, which are consistent across sources and mechanically plausible: CMS dates change on
       republication; sitemap `lastmod` values are regenerated automatically when a page is rebuilt, a
       plugin runs, or a site is migrated, making old pages appear newly modified; `Last-Modified` HTTP
       headers are frequently cached or dynamically generated; schema `datePublished`/`dateModified` can
       conflict with visible on-page dates, in which case the search engine may ignore the schema or
       pick a different signal. **These are practitioner sources with a commercial interest in the topic
       and no measured rate is quoted from them.** They are reported only as a mechanism inventory: the
       drift is produced by routine infrastructure operations, not by anomalies, which is the same
       structural point source 1 makes from the other direction.
    4. The **"38% of online articles lack clear publication dates"** figure, attributed in search results
       to a 2022 Reuters Institute study.
       — **UNVERIFIED AND NOT USABLE.** I could not locate the underlying study, could not confirm the
       attribution, and did not retrieve any Reuters Institute publication. **It is recorded here solely
       so that a later run does not rediscover it and mistake it for a finding of this one.** Do not
       cite it. If the estate wants a missing-date prevalence figure, this attribution is the lead to
       chase, and chasing it is the work.
    5. NASA Aviation Safety Reporting System — programme description.
       — **VERIFIED** — I retrieved
       https://www.nasa.gov/human-systems-integration-division/aviation-safety-reporting-system-overview/
       and read it in full. Confirms: ASRS has operated since 1976, has "collected and analyzed over 2
       million safety reports to date," and is "a **voluntary**, confidential, non-punitive, safety
       reporting system." Reports "describe unsafe occurrences, near-misses or close calls, hazardous
       situations, and descriptions of best practices."
       — **EXPLICIT VERIFICATION FAILURE, recorded per the house rule.** The characterisation I was
       actually after — that ASRS reports cannot be used to infer prevalence because they are not a
       random sample, and that the database therefore yields **definitive lower-bound estimates** rather
       than rates — appeared in a search summary attributed to the ASRS Program Briefing PDF. **I could
       not retrieve that PDF** (outside my fetch provenance set) and the NASA overview page I did
       retrieve does **not** contain that language. So: the voluntary, non-random character of ASRS is
       VERIFIED; the lower-bound-not-a-rate conclusion is **UNVERIFIED** and is my own inference from
       the verified premise, which is a short inference but is mine, not NASA's.
       The point for C2A2 stands on the verified part alone. Fifty years and two million reports do not
       produce a rate, because the denominator — the number of occurrences that did not get reported —
       is unavailable by construction. Two in-house filings will not produce one either, and the reason
       is structural rather than a matter of insufficient n.

  Strength of support: **None.** No source located supports the incident reading. Sources 1 and 2 are
    verified and both point the other way; source 3 supplies the mechanism; source 5 explains why the
    estate's own filings cannot settle it either way.

  Summary: The FOR direction returns nothing for this item and the reason is more interesting than the
    result. The strongest finding is structural, not statistical: SalahEldeen and Nelson establish that
    the creation datetime of a web resource is, in the general case, **only estimable** — their tool
    exists because it must poll several independent weak signals to guess a date no source
    authoritatively holds. An error in an estimate from weak evidence is a base rate by construction;
    there is no arrangement under which such errors are incidents. The practitioner literature fills in
    the mechanism from the other end, and the mechanisms are all routine infrastructure operations —
    republication, site migration, sitemap regeneration, header caching — rather than faults. The HoH
    benchmark supplies the only verified magnitude I obtained: at least a 20% performance drop in
    mainstream LLMs from the mere presence of outdated information in context even when current
    information was successfully retrieved, with some models falling below random. That is not a
    date-metadata error rate and I am not presenting it as one, but it is a measured, external,
    systematically-framed figure for temporal error in this exact class of system, and its existence
    means the field treats this as a property to be benchmarked rather than an incident to be logged.
    Finally, ASRS explains the estate's filing behaviour without attributing it to carelessness: fifty
    years and two million voluntarily-submitted reports still do not yield a rate, because the
    denominator is unobtainable by construction. C2A2's two filed instances are in the same position,
    and no number of additional filings will change it. The denominator has to be built deliberately or
    imported from outside, and this file is the attempt to import it.

  Caveats:
    (i) **The base rate the item actually wants does not exist in anything I found.** A measured error
      rate for date/freshness metadata specifically, in an LLM search-grounding layer, against ground
      truth, is not a figure I located. Sources 1-3 establish that the errors are structural; none
      quantifies how often. **Do not let the ≥20% from source 2 stand in for it** — that is a
      performance-degradation magnitude on a QA benchmark, not a prevalence of date errors, and
      conflating them would be exactly the unverified-snippet-as-source failure the house rule exists to
      prevent.
    (ii) **Two of five sources verified; one is an explicit verification failure with the failure
      recorded; one is unusable and is flagged as unusable.** That is the honest state of this file.
    (iii) **Source 1 is from 2013.** The web's date-metadata practices have changed since — schema.org
      adoption, AMP, structured-data guidance — and it is possible the situation has improved. Nothing I
      found suggests it has, and sources 3's mechanisms are all still current, but the staleness is real
      and I am flagging it rather than assuming continuity. This is also, in passing, a date-provenance
      problem of the kind the item is about.
    (iv) **Publication-bias direction is unusual here and worth naming.** For most items a FOR search
      risks over-representing support. Here the entire located literature runs against the presumption,
      which could reflect a genuine consensus or could reflect that nobody publishes a paper reporting
      that retrieval dates are mostly fine. I cannot distinguish these from what I retrieved.
    (v) **PREMISE-173 binds the remedy and the remedy here is unusually well-shaped.** The obvious
      response — file date errors more diligently — is a detection-layer addition with no final element
      and 173 excludes it. What has a final element is a denominator: sample N retrievals, check each
      date against an independent source, report the rate. That is capture-recapture in PREMISE-124's
      sense, it is cheap, it produces a number that can move, and it is the only thing in this file that
      would actually settle the item.

  Search scope: comprehensive on mechanism, unsuccessful on prevalence. Searched: search-engine and CMS
    publication-date metadata accuracy and republication drift; web-resource creation-date estimation;
    LLM search-grounding and RAG temporal errors, outdated-information benchmarks and measured
    degradation rates; near-miss reporting and the denominator problem in aviation. **Did NOT search:
    the medical near-miss / incident-reporting denominator literature** (named in my intake alongside
    aviation; Macrae's work on incident-reporting pathologies is already carried by PREMISE-173, so the
    marginal return looked low), **web-archive republication drift in the Memento/temporal-coherence
    literature** (Ainsworth, Nelson et al. on archived-page temporal violations — this is the closest
    thing to a measured drift rate that exists and is the single highest-value untouched body if the
    estate wants a real number), and **news-article date-extraction tool accuracy benchmarks**, which
    would give a direct extraction-error rate.

  NOVELTY-FLAG:
    Item: PRESUMPTION-968
    Searched: web publication-date metadata accuracy and drift mechanisms; web-resource creation-date
      estimation; RAG/LLM temporal error benchmarks; voluntary near-miss reporting and the denominator
      problem.
    Finding: The **structural** claim is thoroughly covered and the presumption is refuted by it. The
      **quantitative** question the item was routed out to answer — what fraction of dates returned by
      an LLM search-grounding layer are wrong, measured against ground truth — has **no published answer
      that I could locate.** The adjacent literatures each measure something else: SalahEldeen & Nelson
      measure how well a date can be *estimated*, HoH measures how much outdated *content* degrades
      answers, the SEO material describes mechanisms without rates.
    Implication: The gap is narrow, real, and cheaply closable in-house — and closing it would produce
      a number nobody else appears to have. This is a genuine measurement opportunity rather than a
      theoretical contribution.
    Recommended status: **NOVEL on the specific metric only.** The presumption itself is not novel, it
      is simply wrong; do not let the novelty flag on the metric be read as support for the item.

  Recommendation: **NO-SUPPORT-FOUND.** I searched for evidence that search-layer date errors are
    incidents and found none; the verified evidence establishes that they are structural. The register
    already forbids the inference the estate was making from n=2 (PREMISE-124, and PREMISE-174's
    recorded 2/2 prohibition), so this is an enforcement gap on the inferential limb. On the empirical
    limb the honest position is that the estate has neither a base rate nor grounds to assume there
    isn't one, and the only thing that changes that is a sampled denominator.
