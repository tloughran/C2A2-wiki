SEARCH-AGAINST-ASSUMPTION-1311:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1311
  Original statement: "*Two verification failures recorded rather than glossed:* the AJR mammography
    quote load-bearing for PREMISE-201 clause (3) failed retrieval and is flagged unverified; and **the
    Zimmermann ICSE'12 paper does not publish the reopen rate its search summary implied** — 15b caught
    that by reading it, and the 'mid-teens to low twenties' estimate in REVISE-445 inherits the weakness
    and is labelled a prompt to measure, not a finding."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1311
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim. First time a minted premise (PREMISE-201) carries a clause resting on an
        unverified quotation, and first time a lit-search summary was caught misreporting its source by
        reading the source. Both credits to the run; recorded against it that PREMISE-201 was minted
        anyway and REVISE-445 still stands on the weakened number. See PRESUMPTION-954.
      15b: Searched for challenging literature; found the measured base rate is far worse than two
        instances suggest, which makes the item's general limb not merely false but badly calibrated.
    Current status: NO-CHALLENGE-FOUND (the general limb is refuted in the item's own direction)

  Register pre-check:
    - PREMISE-132 (ACTIVE) — "CITING IS NOT VERIFYING... in generated text the measured rate of full
      support between a sentence and its own citation is roughly half." **Exact pre-answer.** The general
      limb was already denied before either agent searched.
    - PREMISE-148 (ACTIVE) — disclosure of a provenance route is not an audit of it; object-level content
      carries the higher measured error rate. Quotation error rates are named here.
    - PREMISE-178 (ACTIVE) — an existence check and a label check do not establish that a cited source
      supports the sentence it anchors.
    - PREMISE-188 (ACTIVE) — an evidentiary qualifier travels with the claim or it does not travel; a
      caveat in a header does not govern the body once quoted, and the stripping is systematic rather
      than careless. **Directly governs REVISE-445's inherited caveat.**
    - PREMISE-103 (ACTIVE) — absence of primary text is a kind-difference in evidence; downgrading
      confidence is not a valid substitute for an explicit "unfounded pending retrieval" state.
      **Directly governs PREMISE-201 clause (3)**, which was minted with the clause rather than held.
    - PREMISE-118 (ACTIVE) — an instrument found out of tolerance triggers a RETROSPECTIVE impact
      assessment over every result produced since last known-good. Two caught misreports imply an
      uncounted population of uncaught ones.
    - PREMISE-143 (ACTIVE) — METRIC INVERSION: reliable catching of small failures actively suppresses
      the count. A catch count is a measure of the producing layer, not the catching layer.
    - PREMISE-162 (ACTIVE) — a defect count produced by a run auditing its own instrument is a CATCH
      COUNT WITH NO DENOMINATOR; residual-defect estimation requires two independent streams or seeded
      defects.

  Challenging evidence found: No — in the direction the charter asked me to search. See below.

  LIMB STRUCTURE — three limbs:
    LIMB A — the two instances as reported. (Settled as to fact, in-house.)
    LIMB B — "search summaries carry their sources' claims faithfully." (The general limb, stated as the
      thing the two instances refute.)
    LIMB C — "the rate is low enough that verification is not worth its cost." (The charter asked me to
      look for this. I looked. It is not supported.)

  Sources:
    1. Liu, N.F., Zhang, T. & Liang, P. (2023). "Evaluating Verifiability in Generative Search Engines."
       *Findings of EMNLP 2023*. — **VERIFIED** (full PDF retrieved from cs.stanford.edu/~nfliu and the
       figures read directly in the abstract and §4.2: "on average, a mere 51.5% of generated sentences
       are fully supported by citations, and only 74.5% of citations support their associated sentence")
       — Across four generative search engines (Bing Chat, NeevaAI, perplexity.ai, YouChat) with human
       evaluation: **citation recall 51.5%, citation precision 74.5%.** Roughly a quarter of citations do
       not support the sentence they are attached to, and roughly half of generated sentences are not
       fully supported. This is the base rate against which "two instances" should be read.
    2. PREMISE-132 (in-register, ACTIVE) — VERIFIED (read in `premises_index.md`) — the register already
       holds the ~50% figure and already concludes that "all items do cite external referents" is not
       evidence of anything. The general limb was pre-answered.
    3. On LIMB C specifically — nothing found supports it. I searched for evidence that verification cost
       exceeds benefit and found none applicable: at a 25.5% citation-precision failure rate, the
       expected number of misattributed load-bearing claims in any batch of four is one. The cost of
       verifying a load-bearing quotation is one retrieval. The cost of not verifying it is a minted
       premise resting on a claim its source does not make — which is what PREMISE-201 clause (3)
       currently is.
    4. **Self-referential datum from this cycle, VERIFIED by my own experience today.** In writing these
       eleven files I attempted retrieval on the load-bearing sources for four items and was blocked
       four times: Schwenk 1990 (paywalled, RePEc carries no abstract), Schulz-Hardt 2002 (paywalled),
       the Hróbjartsson 2012 BMJ record (PubMed served a reCAPTCHA, which I did not bypass), and the
       OpenReview TMLR devil's-advocate paper (browser-verification challenge; the PDF endpoint returned
       empty). In every one of those cases a search-engine summary offered me a confident, specific,
       quantitative claim which I could not check. **That is the mechanism.** The failure is not that
       summaries lie; it is that the summary is always available and the source frequently is not, so the
       cheapest path and the correct path diverge systematically. I have marked each of those SECONDARY
       or UNVERIFIED in the relevant files rather than quote them as findings.

  Strength of challenge: None

  Summary: The charter asked me to find measured rates that say otherwise and to find evidence the rate
    is low enough not to matter. Neither exists. The best direct measurement — Liu, Zhang & Liang's
    human evaluation of four generative search engines, which I retrieved and read — puts citation
    precision at 74.5% and citation recall at 51.5%, meaning roughly one citation in four does not
    support its own sentence. The item's two instances are not an unlucky pair; they are close to what
    the base rate predicts for a cycle of this size. If anything the item understates the problem in two
    ways. First, by PREMISE-143's metric inversion, the two caught cases measure the producing layer, and
    a catch count has no denominator without seeded defects (PREMISE-162) — the uncaught population is
    unknown. Second, the remedy actually applied was insufficient on the register's own standards:
    PREMISE-201 was minted anyway with an unverified clause, which PREMISE-103 says is not a permissible
    substitute for an explicit unfounded state, and REVISE-445's caveat will not travel with the number
    once the number is quoted, which is PREMISE-188's systematic stripping. I could not construct a
    serious case against this item and I am recording that plainly rather than manufacturing one.

  Specific risks: The risk is not that limb B is true; it is that the estate treats "two failures
    recorded" as a control. It is not a control — it is two observations drawn from an unmeasured
    population. PREMISE-118 requires a retrospective impact assessment over every result since last
    known-good whenever an instrument is found out of tolerance, and no such assessment has been run over
    prior lit-search output. With citation precision measured at roughly three-quarters in the closest
    analogue, the expected number of unsupported load-bearing claims already sitting in 158 ACTIVE
    premises is not small, and none of them carries a verification grade. The second risk is the
    inheritance path the item itself names: REVISE-445 stands on a weakened number with the weakness
    recorded in a *different document*, which PREMISE-188 predicts will be stripped on first quotation.

  Mitigations available:
    - Add a per-claim verification grade (VERIFIED / SECONDARY / UNVERIFIED) as a required field on every
      load-bearing quantity, stored *with the number* rather than in a header. This is PREMISE-188's
      remedy shape and it is the cheapest thing on this list. These eleven files use it; the registers do
      not.
    - Hold rather than mint. PREMISE-103 gives the state that PREMISE-201 clause (3) should have had:
      unfounded pending retrieval. Minting-with-caveat is the substitution that premise forbids.
    - Get a denominator. PREMISE-162 names the method: seed 5 deliberately misattributed claims into a
      cycle's search output and count how many the verification step catches. Without that, "two caught"
      is a catch count and PREMISE-143 says it inverts.
    - Triage by load-bearingness rather than verifying everything. The Liu et al. rate means universal
      verification is unaffordable and unnecessary; what must be verified is any figure a premise clause
      rests on. That is a small set and it is enumerable.
    - Record retrieval failures as first-class events. Four of my own load-bearing retrievals failed
      today for structural reasons (paywall, bot challenge). If that rate is typical, a large fraction of
      this pipeline's citations can never be verified at all, and the register needs to know which.

  STEELMAN:
    Item: ASSUMPTION-1311
    Strongest counterargument: The steelman here must be for the item's *opponent*, and the only honest
      one is a cost argument: verification consumes the scarcest resource in a pipeline that PREMISE-106
      already says is in the unstable regime, and a policy of reading every source would reduce items
      serviced per cycle below the arrival rate by an even larger margin, trading a known citation-
      fidelity problem for a known queue-divergence problem. On that view the two recorded failures are
      evidence the *existing* informal discipline works — they were caught, by reading, without a
      mandated universal-verification policy — and formalising it would cost more than it saves. The
      register should keep verifying opportunistically and spend the saved capacity on the 170 unserved
      re-trigger items.
    What would need to be true for C2A2 to be safe: (1) the opportunistic catching must actually have a
      measurable hit rate, which requires seeded defects, because otherwise "we caught two" is consistent
      with catching two of two and with catching two of twenty; (2) the set of load-bearing quantities
      must be small and enumerable, so that targeted verification is affordable; (3) verification grades
      must travel with numbers, or the distinction is lost on first quotation; and (4) unverifiable
      sources must be routed to an explicit unfounded state rather than minted with a caveat.
    How to test: Seed and count, one cycle, and it is the same test PREMISE-162 already names. Insert
      five synthetic claims into a cycle's search output, each attributing a plausible but fabricated
      quantitative finding to a real, retrievable paper. Count how many survive to a minted premise. That
      number is the escape rate, it has a denominator, and it converts this whole item from two anecdotes
      into an instrument characteristic. Run it against 15a and 15b separately; the difference between
      the two is also informative about ASSUMPTION-1310.

  Search scope: comprehensive. Searched: citation fidelity and verifiability in generative search
    (Liu/Zhang/Liang 2023, retrieved and read); attribution and grounding evaluation; quotation-error
    rates in the scholarly literature; LLM hallucinated-citation rate studies; and specifically for any
    evidence that verification cost exceeds benefit or that fidelity rates are high enough to ignore —
    none found.

  Recommendation: NO-CHALLENGE-FOUND. LIMB A is settled in-house. LIMB B is refuted by measurement in
    the item's own direction and was already pre-answered by PREMISE-132. LIMB C is unsupported. The
    item should be strengthened rather than challenged: the two instances are consistent with a base rate
    of roughly one bad citation in four, and the estate currently has no denominator, no per-claim
    verification grade, and no retrospective impact assessment.
