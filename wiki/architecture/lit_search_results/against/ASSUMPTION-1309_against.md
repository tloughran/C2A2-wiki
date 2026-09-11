SEARCH-AGAINST-ASSUMPTION-1309:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1309
  Original statement: "*Five of six items were already answered by `validated_premises.md` before either
    agent searched* — second consecutive cycle (9 of 11 items across two). Three minted nothing because
    an ACTIVE premise already denies them. **That's a routing defect, not a search defect: a register
    grep belongs *before* 14a/14b routes.**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1309
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed, with the register's own interest declared (the proposed
        pre-route grep would sit in 14a/14b). Rate measured across two cycles (9/11, 82%).
      15b: Searched for challenging literature; found the rate's confidence interval is too wide to
        support the diagnosis, found the duplicate-suppression remedy is measurably counterproductive in
        its best-studied analogue, and found the proposal makes the register unfalsifiable.
    Current status: CHALLENGED

  Register pre-check:
    - PREMISE-174 (ACTIVE) — "A REGISTER WITH EXPANSION AND NO CONTRACTION CANNOT REVISE — IT CAN ONLY
      ACCUMULATE, AND ITS GROWTH CURVE IS THEREFORE NOT A HEALTH SIGNAL. Belief revision is DEFINED as
      contraction followed by expansion; a knowledge base that can add but not retract cannot perform
      it." **This is the decisive pre-answer and it denies the remedy outright.** A pre-route grep that
      suppresses search on premise-match removes the only route by which a premise is ever re-exposed,
      converting a non-contracting register into a formally unrevisable one.
    - PREMISE-160 (ACTIVE) — a named defect explanation is discharged by ONE DISCONFIRMING CASE, and
      confirming only on cases the explanation already predicts raises the posterior by construction.
      A pre-route grep guarantees that only confirming cases are ever seen.
    - PREMISE-107 (ACTIVE) — "A remedy attached to an observation without being validated against the
      actual mechanism costs effort AND leaves the fault in place; where two candidate mechanisms present
      the same symptom, the discriminating test is the operative construct and skipping it is the
      defining error of fault isolation." Two mechanisms present here: (a) routing is redundant, (b) the
      register has grown to cover the domain and the pipeline is approaching saturation. Not discriminated.
    - PREMISE-136 (ACTIVE) — the achievable denominator of a settling quantity is fixed by its declared
      scope; a quantity scoped to single-digit events per run has bounded power. n=11 is inside that bound.
    - PREMISE-124 (ACTIVE) — a favorable number produced from inside the instrument being evaluated does
      not calibrate it. The 82% is the pipeline measuring its own efficiency.
    - PREMISE-126 (ACTIVE) — a re-check that only advances the date certifies "not-yet-expired," not
      "re-tested." Suppressed re-search is the limiting case of that.
    - PREMISE-172 (ACTIVE) — a PASS is a verdict about a (reader, frame, scope) reading, not transferable
      to a later reader with a different question. An old premise "answering" a new item is exactly a
      transfer across frames.
    - OPEN-192 already poses this question and this register declares itself the constrained party.

  Challenging evidence found: Yes

  LIMB STRUCTURE — three limbs and they fail separately:
    LIMB A — "the 82% rate is real." (Measurement.)
    LIMB B — "it is a ROUTING defect." (Diagnosis.)
    LIMB C — "a pre-route grep is the remedy." (Prescription.)

  Sources:
    1. Wilson score interval on the observed rate. — **VERIFIED (computed by me)** — 9/11 = 0.818, Wilson
       95% CI **[0.523, 0.949]**. The single-cycle 5/6 = 0.833, CI [0.436, 0.970]. The interval spans
       everything from "half the items" to "almost all of them." An 82% point estimate with a floor of
       52% does not distinguish a routing defect from a register that has simply grown large relative to
       the topic space, and it certainly does not support a structural change to the routing layer.
    2. Bettenburg, N., Premraj, R., Zimmermann, T. & Kim, S. (2008). "Duplicate Bug Reports Considered
       Harmful ... Really?" *ICSM 2008*. — SECONDARY (abstract and findings retrieved via search and via
       the VU Amsterdam record; a full-text PDF is hosted at people.csail.mit.edu but I did not read it,
       so the quantitative claims are SECONDARY) — **The direct analogue, and it runs against the
       remedy.** Most developers had experienced duplicate reports but few considered them a serious
       problem; the additional information duplicates carry helps resolve bugs faster, and the authors
       showed automatic triaging *improves* when duplicates are used. Their recommendation is to MERGE
       duplicates, not to suppress them at intake. Transposed: an item that an ACTIVE premise already
       answers is a duplicate report, and the measured finding is that duplicates are informative.
       (Noting explicitly: Zimmermann is a co-author here. This is ICSM'08 and is a different paper from
       the ICSE'12 work misattributed in a prior cycle — I have not conflated them.)
    3. Deming / SPC "tampering" (Deming Alliance; SPC for Excel "Profound Knowledge Part 2";
       ScienceDirect, "Deming's tampering revisited: definition and future research agenda"). —
       SECONDARY — reacting to common-cause variation as if it were special-cause increases process
       variation. Two cycles is not a control chart. (The frequently-repeated "94% common cause / 6%
       special cause" attribution to Deming is folklore-grade in the sources I saw and I give it no
       weight.)
    4. Systematic-review search practice, generally: reviews re-run searches at update rather than
       excluding previously-answered questions, precisely because the answer can change. — SECONDARY /
       general-practice, no single citation retrieved; weak support only.
    5. PREMISE-174 (in-register) — VERIFIED (read in `premises_index.md`) — the formal argument. Under
       AGM, revision = contraction + expansion. Suppressing search on premise-match removes the input
       that could ever motivate contraction. The register would then satisfy the formal definition of a
       system that cannot revise, and its 158 ACTIVE premises become unfalsifiable by construction.

  Strength of challenge: Strong (LIMB A: Weak — the count is probably right as a count. **LIMB B: Strong
    challenge** — n=11 cannot carry the diagnosis and a competing mechanism was never excluded.
    **LIMB C: Strong challenge** — the remedy is denied by PREMISE-174 and by the duplicate literature.)

  Summary: The count is not in dispute; the inference from it is. An 82% rate over eleven items carries a
    95% Wilson interval of [52%, 95%], which is compatible with a routing defect and equally compatible
    with a register that has simply accumulated 158 premises over a bounded topic space — and those two
    mechanisms produce the identical symptom, which is the condition PREMISE-107 says requires a
    discriminating test before any remedy is attached. None was run. The prescription is worse than the
    diagnosis. In the best-studied analogue, duplicate bug reports, suppression at intake is precisely
    what the empirical work advises against: duplicates carry additional information and improve triage,
    and the recommendation is to merge rather than to filter. And PREMISE-174, already ACTIVE, supplies
    the formal objection: a register that can expand but not contract cannot revise, and a pre-route grep
    that suppresses search on premise-match removes the last channel through which a premise could ever
    be exposed to disconfirming evidence. The estate would purchase efficiency by making its own
    knowledge base unfalsifiable. That is not a routing fix; it is a change in the epistemic status of
    every ACTIVE premise.

  Specific risks: If limb C is adopted, the 158 ACTIVE premises become permanently ACTIVE. Any premise
    minted on weak evidence — and the register knows of at least one, PREMISE-201 with a clause resting
    on an unretrievable quotation (see ASSUMPTION-1311) — is thereafter shielded from the only process
    that could downgrade it. PREMISE-160's asymmetric-case-selection failure becomes structural rather
    than occasional: the pipeline would see only items the register does not answer, i.e. only cases the
    explanation does not predict, and would never again test a premise on a case it does predict. The
    efficiency gain is real but bounded (roughly 80% of a dozen items per cycle); the epistemic cost is
    unbounded and irreversible. If limb B is wrong and the real mechanism is domain saturation, the grep
    also treats a *success* signal — the register has learned the domain — as a defect, and the correct
    response would have been to widen the intake scope, not to narrow the search.

  Mitigations available:
    - Run PREMISE-107's discriminating test before anything else, and it is cheap: PRESUMPTION-948
      already names it — count premises that have EVER changed status after minting. If the answer is
      zero across 158, the register is already monotonic as a matter of fact and the grep changes
      nothing but the accounting; if it is non-zero, the grep destroys the mechanism that produced those
      changes. Either result settles limb C in one grep.
    - Adopt the Bettenburg remedy rather than the suppression remedy: do not skip the search, MERGE the
      result. Route the item, search it, and record the outcome as either "premise confirmed on a new
      case" (which is evidence, and currently discarded) or "premise contradicted" (which is the only
      contraction path the register has).
    - Cheaper still, and it preserves falsifiability: keep routing unchanged and ADD the grep as an
      annotation rather than a gate — 14a already does this informally ("each carries a note where an
      ACTIVE premise plainly bears on it"). Annotation costs nothing and suppresses nothing.
    - Suspend the diagnosis until n ≥ 30. At 9/11 the interval is [0.52, 0.95]; a structural change to
      the routing layer deserves a tighter reading than that.

  STEELMAN:
    Item: ASSUMPTION-1309
    Strongest counterargument: Search is not free, and the binding constraint on this pipeline is
      documented: PREMISE-106 holds that the lit-search queue is already in the unstable regime, with
      arrivals exceeding service and the backlog growing without bound. In that regime, spending eight of
      every eleven search slots on questions already answered is not a rounding error — it is the direct
      cause of the 170 untagged `[RE-TRIGGER by 15d]` items, oldest 2026-07-05, unserved for six
      consecutive cycles. The falsifiability objection assumes the choice is search-or-suppress, but the
      register already has a dedicated re-examination lane (15d) whose entire purpose is periodic
      re-validation; routing pre-answered items to 15d rather than to 15a/15b is not suppression, it is
      correct triage, and it would give the starved lane the input it has never had. The 82% is the
      sharpest efficiency finding the pipeline has produced and the confidence interval objection would
      forbid acting on any operational measurement this system is ever able to take.
    What would need to be true for C2A2 to be safe: (1) the 15d re-trigger lane must actually run — it
      has not, for six cycles, so routing to it today is routing to /dev/null and PREMISE-102 applies;
      (2) the grep must be a ROUTER, not a FILTER: every pre-answered item must arrive somewhere that
      re-examines it, with an owner and a cadence; (3) premises must be capable of status change in fact,
      not just in principle (PRESUMPTION-948's count); and (4) the grep's own precision must be measured
      — a regex over premise text will produce false "already answered" matches, and PREMISE-187 holds
      that a gate which appears to check what it cannot decide is worse than no gate.
    How to test: Two in-house measurements, both cheap, and they are complementary. (a) Retrospective:
      run the proposed grep over the last 40 routed items and hand-check every "already answered" hit for
      whether the premise really does answer the item, or merely shares vocabulary. That is the grep's
      precision, and PREMISE-113 warns that rule-based detectors run 76-90% false positives as a matter
      of course. (b) Prospective and decisive for the falsifiability objection: take 5 items the grep
      would have suppressed, search them anyway in full, and record whether any produced evidence
      bearing against the matching premise. If none did across a reasonable n, suppression is safe. If
      any did, the grep would have hidden a contraction and limb C is refuted empirically.

  Search scope: comprehensive on the duplicate-suppression analogue and the small-sample objection;
    preliminary on knowledge-base maintenance. Searched: duplicate bug report detection and its costs
    (Bettenburg 2008 lineage, Cavalcanti et al. bug-report-duplication studies); Wilson/binomial interval
    computation (done locally); Deming tampering and common-vs-special-cause variation; systematic-review
    update practice. NOT searched and worth searching: the AGM belief-revision literature directly
    (PREMISE-174 cites it but a primary source would strengthen the formal limb), and the
    information-retrieval literature on deduplication precision, which bears on the grep's own error rate.

  Recommendation: CHALLENGED — resting on LIMB B and LIMB C jointly. LIMB A stands. The single most
    useful next act is not a search at all: it is PRESUMPTION-948's count of premises that have ever
    changed status, which decides limb C by itself.
