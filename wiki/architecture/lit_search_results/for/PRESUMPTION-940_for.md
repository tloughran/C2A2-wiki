SEARCH-FOR-PRESUMPTION-940:
  Date searched: 2026-09-10
  Original item: PRESUMPTION-940
  Original statement: [inferred] A configuration fix, once applied, stays applied — remediation needs
    verification at application but not thereafter.
  Routed question: does an applied configuration remediation persist, and does closed-loop
    verification after application change recurrence?
  Risk if wrong (carried from intake): Critical — all 218 revision flags become a record of intentions
    rather than states.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-940
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Generalised from ASSUMPTION-1298 — `permissionMode` found absent for six days after having
        been set, with the application rewriting its config from memory.
      15a: Searched for supporting literature (2026-09-10), FOR direction only. Register checked
        before searching.
    Current status: NO-SUPPORT-FOUND.

  PREMISE-REGISTER OVERLAP (checked before searching, per DEFECT-G): MODERATE-TO-HEAVY on the REMEDY;
    the DECAY RATE is not held anywhere and is what I searched for.
    Grepped for: PREMISE-139, 171, 177, 181, 183, 200; configuration drift, remediation regression,
    CAPA, effectiveness check, reconciliation.
    - PREMISE-171 (ACTIVE, Moderate-High) already holds the architectural answer this item needs:
      "A DECLARATION REGISTER IS NOT A FAILURE DETECTOR — ITS COMPLETENESS IS ZERO. A register that
      stores what was declared about a thing (loaded, configured, enabled, scheduled) reports on the
      DECLARATION, never on the thing." A revision flag recording that a fix was applied is exactly a
      declaration register. The premise's minimal repair — "store an EXPECTED-NEXT-FIRE alongside each
      declaration and alarm on the age of the gap between expected and observed" — generalises to
      "store the expected configuration state and alarm on divergence from observation," which is
      drift reconciliation. It also carries the LOAD-BEARING NEGATIVE: do not answer this with a
      heartbeat, because a heartbeat over a path that bypasses the sick path is the gray-failure
      pattern. And it names the defensible architectures by name: "Kubernetes spec/status, ITSM drift
      reconciliation, service-discovery registered-vs-ready — all KEEP the declaration and alarm on
      its DIVERGENCE from observation."
    - PREMISE-183(1) (ACTIVE): "Verifying that a fix was implemented is explicitly NOT the same as
      verifying that recurrence has stopped, and a failed effectiveness check REOPENS the item rather
      than closing it with a note." Adjacent but not identical: 183 is about EFFECTIVENESS (did the fix
      address the cause), 940 is about PERSISTENCE (is the fix still there). Both fail the presumption,
      by different mechanisms. PREMISE-183 also records, as a limitation on itself, that "no controlled
      evidence that effectiveness verification reduces recurrence was found" — so the estate already
      knows the CAPA limb of this item is unmeasured.
    - PREMISE-177 (ACTIVE, Moderate) carries Yin, Ma, Zheng, Zhou, Bairavasundaram & Pasupathy (2011),
      "An Empirical Study on Configuration Errors in Commercial and Open Source Systems," SOSP '11 —
      546 real-world misconfigurations, environment and path errors a dominant and OFTEN SILENT
      failure cause. That is the best peer-reviewed source in the whole configuration area and the
      estate already holds it.
    - PREMISE-200 (ACTIVE, High on limbs 2-3) supplies the instrument: "a per-file CONTENT HASH is the
      admissible evidence of substantive change," with a named in-house operational consequence
      (hash the vault now and after the next run; compare mtime-changed against hash-changed).
      Applied to a config file, that is precisely the post-application verification 940 denies is
      needed, and it is already ACTIVE.
    - PREMISE-181 (ACTIVE) and PREMISE-139 (ACTIVE) cover the adjacent classes: a stale artefact read
      as a fresh one produces a PASS; a documented check is not evidence the check ran.
    ASSESSMENT: the REMEDY is register-held at PREMISE-171 and the INSTRUMENT at PREMISE-200; between
    them the estate already has both halves of the answer, filed under other headings. PREMISE-138
    bars re-minting. NARROWING APPLIED: I did not re-derive Yin et al. or the gray-failure material.
    I searched only for (i) a measured persistence or decay rate for applied configuration fixes, and
    (ii) any evidence that a fix stays applied without re-verification.

  Supporting evidence found: No.

  Sources:
    1. Declarative infrastructure-as-code, immutable infrastructure, and GitOps continuous
       reconciliation.
       [VENDOR AND PRACTITIONER LEVEL ONLY — Spacelift, Octopus Deploy, Wiz, Legit Security, plus one
       article in a non-indexed venue (IJETCSIT, "Eliminating Configuration Drift at Scale Using
       Declarative…"). NO PEER-REVIEWED SOURCE LOCATED. NONE READ IN FULL. NOT ESTABLISHED, AND I
       DECLINE TO TREAT ANY FIGURE FROM THIS BODY AS EVIDENCE.]
       — Recorded because this is where the FOR case would live if it lived anywhere, and because what
       it actually says is the negation. The uniform reported claim is that a fix stays applied ONLY
       where something re-applies it: "automated agents continuously reconcile the live infrastructure
       against the repository's desired state"; "idempotent scripts and tools can be set to run
       continuously at fixed time intervals"; "drift detection capabilities periodically check
       infrastructure for discrepancies compared to repository state, then launch reconciliation jobs."
       Immutable infrastructure is described as preventing drift by making the resource unmodifiable
       after creation — which is not "verification is unnecessary" but "the state is made
       unfalsifiable by construction." WEIGHT: None as evidence. Direction: against, unanimously. The
       entire discipline exists on the premise that PRESUMPTION-940 is false; there is no branch of it
       that assumes fixes persist.
    2. Configuration-drift incidence claims. [PRESS-RELEASE AND VENDOR-SURVEY LEVEL — a 2026 Reach
       Security commissioned study reported via a syndicated finance page, claiming drift is "driving
       cybersecurity incidents across 97% of organizations." NOT VERIFIED, NOT OPENED, COMMISSIONED BY
       A VENDOR WITH A PRODUCT IN THE CATEGORY. I record the number only to mark that I saw it and am
       NOT using it.] WEIGHT: None.
    3. Vulnerability recurrence and re-open rate as vulnerability-management metrics.
       [VENDOR BLOG LEVEL ONLY — Legit Security, SentinelOne, Cymulate. NOT ESTABLISHED.] — Reported
       definitions: "recurrence rate measures how often a previously fixed vulnerability resurfaces in
       the environment"; "the vulnerability re-open rate shows how often teams mark vulnerabilities as
       resolved but reopen them due to patch failure or misconfiguration." WEIGHT: None as evidence.
       ITS ABSENCE IS THE FINDING, and it is the sharpest thing in this item: the metric is universally
       RECOMMENDED across the industry and its VALUE is published nowhere I could reach. Every source
       tells you to measure it; none tells you what it is. I could not locate a single traceable base
       rate for how often an applied configuration fix reverts.
    4. "Process-based Indicators of Vulnerability Re-Introducing Code Changes: An Exploratory Case
       Study," arXiv:2510.26676. [TITLE AND ABSTRACT-SNIPPET ONLY — not opened, venue status
       unconfirmed.] And "Rethinking Software Misconfigurations in the Real World: An Empirical Study
       and Literature Analysis," arXiv:2412.11121 [TITLE AND SNIPPET ONLY]. — Recorded to establish
       that the re-introduction phenomenon is named in the research-adjacent literature and is
       therefore not a novel construct. Neither supplies a rate I can quote. WEIGHT: None as evidence;
       sufficient to bar a novelty claim about the PHENOMENON.
    5. Register-held and not re-searched: Yin et al. (2011) SOSP, at PREMISE-177; the Kubernetes
       spec/status and ITSM drift-reconciliation architectures, at PREMISE-171. These are the two
       best-quality items bearing on 940 and both were already in the estate before this search.

  Strength of support: None.

  Summary: I found nothing supporting PRESUMPTION-940 and I want to be plain that this is not a thin
  search returning nothing — it is a well-populated area returning the opposite conclusion uniformly.
  Every body of practice I reached is organised around the assumption that an applied configuration
  does not stay applied: declarative infrastructure-as-code, GitOps reconciliation loops, drift
  detection, immutable infrastructure, ITSM drift reconciliation and Kubernetes spec/status all exist
  to answer this problem, and each of them answers it by RE-VERIFYING CONTINUOUSLY or by making the
  state unmodifiable, never by verifying once at application. The estate already holds the correct
  architecture under two other headings — PREMISE-171's keep-the-declaration-and-alarm-on-divergence,
  and PREMISE-200's content hash as the admissible evidence of change — so no new premise is needed
  to act. What I could NOT find, anywhere, is a number: no traceable recurrence rate, re-open rate or
  decay curve for applied configuration fixes exists in what I searched, despite "recurrence rate"
  being a metric every vendor recommends tracking. That gap matters here because the intake rates the
  risk Critical on 218 revision flags, and a Critical rating with no base rate is an assertion. The
  estate is unusually well placed to close it: PREMISE-200's operational consequence already specifies
  the mechanism, and applying it to the config surface — hash each remediated configuration at
  application and re-hash on a schedule — would produce the estate's own decay curve in weeks and
  would be the first such figure I could find anywhere.

  Caveats:
  (a) CITATION QUALITY IS THE WORST OF MY SIX ITEMS. Sources 1-3 are vendor and practitioner material
      with no traceable research behind any figure; sources 4 are title-level. NOTHING in this item was
      read in full. The only good sources bearing on 940 are ones the register already held. This
      result should be read as a clean negative plus a gap declaration, not as new evidence.
  (b) THE NEGATIVE IS ASYMMETRIC BY CONSTRUCTION. Nobody publishes "our fixes stayed applied." A
      literature of remedies will always look like evidence that the problem is universal. The honest
      inference is narrower than it looks: the ABSENCE of any defence of one-time verification is
      strong, but the PREVALENCE of drift is unquantified in what I reached.
  (c) THE ITEM CONFLATES TWO FAILURE MODES AND THE REGISTER SEPARATES THEM. PERSISTENCE (is the fix
      still there — drift, reversion, rewrite-from-memory as in ASSUMPTION-1298) and EFFECTIVENESS (did
      the fix address the cause — PREMISE-183(1), CAPA). Both defeat 940 but they need different
      instruments: persistence needs a state hash on a schedule, effectiveness needs a recurrence
      condition defined at fix time. A single "verified" field would collapse them and would install
      the green-metric defect PREMISE-108 warns about.
  (d) THE FOUNDING INSTANCE IS THE STRONGEST EVIDENCE IN THE ITEM AND IT IS IN-HOUSE, n=1.
      ASSUMPTION-1298 — `permissionMode` absent for six days, the application rewriting its config from
      memory — is a case where the reverting agent was the application itself, which no drift-detection
      product's threat model addresses better than a scheduled re-read would. It is one instance, per
      PREMISE-194 it should be evidenced by an artefact rather than by recollection, and it does not
      establish a rate.
  (e) SEARCH SCOPE: PRELIMINARY — BROADER SEARCH RECOMMENDED, AND THIS ITEM IS THE ONE MOST LIKELY TO
      REWARD A SECOND PASS. Four query families run (configuration drift recurrence; vulnerability
      reintroduction/regression; declarative reconciliation and immutable infrastructure; CAPA
      effectiveness, which the register had already closed). NOT REACHED and specifically named as the
      productive seams: the MSR (Mining Software Repositories) literature on reverted commits and
      "fix-inducing changes," which is peer-reviewed and would supply a real re-introduction rate; the
      SOSP/OSDI configuration-error line beyond Yin et al. (Xu & Zhou's misconfiguration surveys); the
      SRE literature on "toil" and self-healing; and USENIX LISA/SREcon operational reports, where a
      measured drift rate is most likely to exist if it exists at all.

  Recommendation: NO-SUPPORT-FOUND
    (Strength: None. Nothing located supports verification-at-application-only. The only regimes in
     which an applied fix reliably persists are those that verify continuously or make the state
     immutable, both of which are the presumption's negation implemented.)

  NOVELTY-FLAG: RAISED — IN THE UNFAVOURABLE SENSE, AND NARROWLY SCOPED.
    Item: PRESUMPTION-940
    Searched: configuration drift and recurrence; vulnerability reintroduction and re-open rates;
      declarative/immutable infrastructure and continuous reconciliation; CAPA effectiveness
      verification (register-held, not re-run).
    Finding: no source anywhere I reached claims or assumes that a configuration fix persists without
      re-verification.
    Implication: this is NOT an original contribution. It is novelty in the unfavourable sense — the
      claim is unstated in the literature because it is not a position anyone holds, and an entire
      engineering discipline exists on the contrary premise. Per PREMISE-184(1) this must not be filed
      as a literature gap and must not draw a research response; the correct response is engineering,
      and the engineering is already specified at PREMISE-171 and PREMISE-200.
    SEPARATE AND GENUINE MEASUREMENT GAP, recorded distinctly so the two are not confused: no published
      decay rate, recurrence rate or re-open rate for applied configuration remediations was locatable,
      despite the metric being universally recommended. That is a real gap in the field's own
      measurement, and it is cheap for this estate to close for itself across its 218 revision flags.
    Recommended status: NOT NOVEL (claim); MEASUREMENT-GAP (rate).

  DISPOSITION STEER FOR 15c: do NOT mint a new premise for the architecture — PREMISE-171 holds it and
    PREMISE-200 holds the instrument. The two actionable outputs are: (1) extend PREMISE-171's
    applicability line explicitly to REMEDIATION RECORDS (revision flags), which it currently does not
    name, since a "fix applied" flag is a declaration register in the exact sense 171 defines; and
    (2) treat the 218 revision flags as a sampling frame — re-check a random sample against present
    system state and report the fraction still holding. That single number would convert this item from
    a Critical assertion into a measured rate, and would be, as far as this search could establish, the
    only such figure in existence.
