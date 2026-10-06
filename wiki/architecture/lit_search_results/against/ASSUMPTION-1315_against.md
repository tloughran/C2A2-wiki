SEARCH-AGAINST-ASSUMPTION-1315:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1315
  Original statement: "the C2A2 wiki took its largest single-night ingest of the series at 22:00 (85 new
    PRS entries across ten registers, plus CROSS-132 through CROSS-135), **which re-opens 147
    absence-declinations across 74 syntheses as unverified**; two were hand-checked and both still hold."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1315
    Item type: ASSUMPTION (stated — from a sibling project, Summa)
    Transform at each step:
      14a: Extracted verbatim. Cross-project and therefore inside PRESUMPTION-945's open scope question.
        Recorded because it is the one place in the estate where today's ingest was treated as
        INVALIDATING rather than as accretion. No C2A2-side run drew that consequence.
      15b: Searched for challenging literature and computed the sampling bound directly; the sampling
        limb is refuted by an exact calculation, and the invalidation rule is challenged as unscoped
        rather than as wrong.
    Current status: CHALLENGED (sampling limb, decisively) / PARTIALLY-CHALLENGED (invalidation limb)

  Register pre-check:
    - PREMISE-182 (ACTIVE) — "A CORROBORATION COUNT LICENSES FAR LESS THAN IT APPEARS TO, AND THE EXACT
      AMOUNT IS A CLOSED-FORM IDENTITY. Under n-for-n agreement with zero observed failures, the
      one-sided lower confidence bound on the underlying success rate is R_L = (1 − C)^(1/n) — the
      Clopper–Pearson exact limit specialised to zero failures." **This is a complete, exact, ACTIVE
      pre-answer to the sampling limb, and the run's own register already contained it.** No search was
      needed; only arithmetic.
    - PREMISE-136 (ACTIVE) — the achievable denominator of a settling quantity is fixed by its declared
      scope; statistical power is a property of the accrual design.
    - PREMISE-172 (ACTIVE) — a PASS mark is a verdict about a (reader, frame, scope) READING, not a
      property of the file, and is not transferable to a later reader with a different question. Supports
      the invalidation rule in principle.
    - PREMISE-126 (ACTIVE) — a staleness-triggered re-check that only advances the date certifies
      "not-yet-expired," which is categorically weaker than "re-tested against current state."
    - PREMISE-124 (ACTIVE) — self-measurement without an external baseline is UNCALIBRATED.
    - PREMISE-189 (ACTIVE) — detection of omission requires an independently maintained expectation about
      what should be present.
    - PREMISE-154 / PREMISE-133 (ACTIVE) — a deferral must name what would discharge it, who adjudicates,
      and a deadline. 145 re-opened claims currently have none of the three.
    - PREMISE-174 (ACTIVE) — a register that can expand but not contract cannot revise. Bears on whether
      "re-opened as unverified" is a state anything ever exits.

  Challenging evidence found: Yes — decisively on the sampling limb

  LIMB STRUCTURE — two limbs, explicitly separated by the register entry itself:
    LIMB A — "an absence claim is invalidated by any later ingest into its scope." (Framework commitment.)
    LIMB B — "2 of 147 hand-checks license the rest." (The testable limb.)

  Sources:
    1. **Exact hypergeometric calculation, VERIFIED (computed by me, 2026-09-11, exact combinatorics over
       N=147, zero failures observed).** For a population of 147 absence-declinations and n items
       hand-checked with zero failures, the 95%-confidence upper bound on the number that could still be
       stale is:

           n =  2  →  up to **113 of 147 (76.9%)** could be stale
           n =  5  →  up to    65 of 147 (44.2%)
           n = 10  →  up to    36 of 147 (24.5%)
           n = 20  →  up to    19 of 147 (12.9%)
           n = 29  →  up to    12 of 147  (8.2%)
           n = 45  →  up to     7 of 147  (4.8%)
           n = 59  →  up to     5 of 147  (3.4%)

       To exclude, at 95% confidence, that 10% or more are stale requires **n = 26**. To exclude that 5%
       or more are stale requires **n = 45**. The run checked 2.
       By PREMISE-182's closed form the same result in rate terms: R_L = (1 − 0.95)^(1/n), so n=2 gives
       **R_L = 0.2236** — a 2-for-2 clean result licenses only the claim that at least 22% of the
       remaining declinations still hold. n=10 gives 0.741; n=29 gives 0.902; n=59 gives 0.950.
       **LIMB B is not weak; it is close to vacuous.** Two clean checks are consistent with more than
       three-quarters of the 147 being stale.
    2. PREMISE-182 (in-register, ACTIVE) — VERIFIED (read in `premises_index.md`) — the register already
       holds the identity. This item is the second consecutive cycle in which a run has published a
       corroboration count that an ACTIVE premise already prices. That is a finding about propagation
       (PREMISE-123: a validated finding does not reach the agent it governs unless a mechanism carries
       it), not about statistics.
    3. Incremental view maintenance / delta processing literature: Koch et al., DBToaster (arXiv
       1207.0137); Nikolic & Olteanu, "Incremental View Maintenance with Triple Lock Factorization
       Benefits" (SIGMOD'18 / arXiv 1703.07484); Koch, "Incremental View Maintenance for Collection
       Programming" (PODS 2016); practitioner synthesis at materializedview.io. — SECONDARY (abstracts
       and summaries retrieved; DBToaster and the Olteanu paper are open-access PDFs I did not read in
       full) — **This is the challenge to LIMB A, and it is a scoping challenge rather than a refutation.**
       The reported speedup of a delta query over a full recomputation is O(|DB| / |ΔDB|) — orders of
       magnitude in practice. The established engineering answer to "new data arrived, which derived
       results are now wrong?" is *not* to invalidate every derived result; it is to propagate the delta
       through a dependency graph and invalidate only the affected subset. Here ΔDB is 85 triplets across
       ten named registers plus four CROSS entries; the affected subset of the 147 declinations is
       computable, and it is almost certainly far smaller than 147.
    4. On the closed-world side, supporting LIMB A: a negative conclusion drawn under a closed-world
       assumption is genuinely non-monotonic — adding facts can retract it — so the *principle* that an
       ingest can invalidate an absence claim is correct. — SECONDARY/general; I searched for a direct
       treatment tying CWA non-monotonicity to cache invalidation and did not find one, so this is stated
       as principle, not as a cited result.
    5. PREMISE-172 (in-register) — VERIFIED — supports LIMB A independently: a declination is a verdict
       about a reading, and a new ingest changes the scope of the reading.

  Strength of challenge: **Strong on LIMB B** (an exact calculation, not a literature judgement).
    Moderate on LIMB A — the rule is right in principle and unscoped in practice.

  Summary: The run deserves credit for the rarest act in this estate — treating an ingest as invalidating
    rather than as accretion — and then attached to it a sampling claim that does not survive contact
    with arithmetic. Two clean hand-checks out of 147 exclude, at 95% confidence, only the hypothesis
    that more than 113 of the 147 are stale. Put the other way: a population in which three-quarters of
    the declinations had gone stale would have produced two clean checks about 5% of the time, so the
    observation is barely informative. Reaching a 10% ceiling needs 26 checks; a 5% ceiling needs 45. The
    register already contained this result in closed form as PREMISE-182, which means the defect here is
    not statistical ignorance but propagation — an ACTIVE premise that prices corroboration counts
    exactly did not reach the run that published one. On the framework limb, the principle is sound but
    the implementation is unscoped: the established engineering treatment of "new data invalidates
    derived results" is delta propagation through a dependency graph, not global invalidation, and the
    delta here is small and named (ten registers, four CROSS entries). Invalidating all 147 is a
    full-recomputation strategy in a system that has the dependency information to do better, and at
    scale it produces a re-verification queue that grows with every ingest — which this estate already
    knows it cannot service (PREMISE-095, PREMISE-106).

  Specific risks: The immediate risk is that 145 claims now sit in a state nobody will exit. They have no
    owner, no deadline and no discharge test, which is exactly what PREMISE-133/154 forbid, and
    PREMISE-174 says a register that can expand but not contract cannot perform revision — so
    "re-opened as unverified" may be a terminal state in practice. The second risk is the opposite and
    worse: the "two were hand-checked and both still hold" clause reads as reassurance and will be
    quoted as such once the caveat is stripped (PREMISE-188). A reader encountering that sentence takes
    away "spot-checked, fine"; the arithmetic says "consistent with 77% stale." That is a
    false-reassurance channel with a measured gap between what the sentence conveys and what it licenses.
    The third risk is structural: if every ingest invalidates every prior absence claim in scope, and
    ingests are nightly, then the re-verification arrival rate is proportional to ingest volume while the
    service rate is a human hand-check. That is PREMISE-095's unstable regime by construction, and the
    147 will be 300 after the next large night.

  Mitigations available:
    - **Scope the invalidation to the delta.** The 85 triplets landed in ten named registers and the four
      CROSS entries are identified. Compute which of the 147 declinations have scopes intersecting those,
      and invalidate only those. This is the IVM answer and it is mechanical, not judgemental.
    - Re-check by stratified sample, not by convenience. If a global figure is wanted, n=26 gives a 10%
      ceiling and n=45 gives a 5% ceiling; pick the ceiling the estate can defend and check that many.
      Two is not a sample, it is an anecdote.
    - Report the bound, not the count. Replace "two were hand-checked and both still hold" with "2 of 147
      hand-checked, zero failures; this excludes at 95% confidence only that more than 113 are stale."
      That is one sentence and it removes the false-reassurance channel entirely.
    - Give the re-opened set a discharge rule per PREMISE-133/154: what closes a re-opened declination,
      who adjudicates, by when. Without it the state is not a state.
    - Prioritise the re-checks by *prior probability of change* rather than at random: declinations whose
      subject matter overlaps the ten ingested registers are the ones most likely to have flipped, and
      checking those first is both cheaper and more informative than a uniform sample.

  STEELMAN:
    Item: ASSUMPTION-1315
    Strongest counterargument: The hypergeometric objection assumes the 147 declinations are exchangeable
      and that the two checked were drawn at random, and neither is likely true. If the run checked the
      two declinations *most likely* to have been invalidated — the ones whose scope most directly
      overlaps the night's ingest — then the sample is adversarial rather than random, and two clean
      adversarial checks license far more than two clean random ones. Adversarial or worst-case sampling
      is a recognised and efficient design precisely because it concentrates power where the failure
      probability is highest. Beyond that, the "2 of 147" clause is not doing the work the objection
      attributes to it: the run's substantive act was to *re-open all 147*, which is the conservative
      move, and the hand-checks were offered as a sanity probe on that decision, not as a licence to skip
      the rest. Reading a probe as a sampling claim and then refuting it as a sampling claim attacks a
      sentence rather than the decision. And the invalidation rule itself is the right one: an absence
      claim under a closed-world assumption is non-monotonic by construction, and 307 synthesis files
      were verified with zero hard citation drift on the same night, which is the real evidence base.
    What would need to be true for C2A2 to be safe: (1) if the two checks were adversarially selected,
      that selection rule must be *recorded* — an adversarial sample with an unrecorded selection rule is
      indistinguishable from a convenience sample and licenses nothing; (2) the 147 must have a discharge
      path with an owner and a date, or the conservative re-opening is a way of losing them; (3) the
      invalidation must be scoped to the delta, or the re-verification queue diverges; and (4) the
      "both still hold" sentence must not travel without its bound.
    How to test: Two things, and the first is free. (a) **Ask what rule selected the two.** If the answer
      is "the two most likely to have flipped," the steelman holds and the file should say so; if it is
      "the first two," the arithmetic above stands unmodified. This is one question to the run's author
      and it changes the verdict. (b) Check 24 more, chosen by scope-overlap with the ten ingested
      registers. At n=26 with zero failures the 95% ceiling drops to 10% of the population — a defensible
      number — and if any of the 24 fails, the estate learns the far more valuable fact that the
      invalidation rule was catching something real. Either outcome is worth 24 checks; the current
      state, 145 claims in limbo with a two-item probe, is worth nothing.

  Search scope: comprehensive on the sampling limb (which was settled by computation against an ACTIVE
    premise rather than by literature); preliminary on the invalidation limb. Searched: incremental view
    maintenance and delta processing; dependency-tracked vs global cache invalidation; closed-world
    assumption and non-monotonic retraction; acceptance sampling and zero-defect sampling plans. Computed
    locally: exact hypergeometric bounds for N=147 at n ∈ {2,5,10,20,29,45,59} and the Clopper–Pearson
    zero-failure limit. NOT searched: the truth-maintenance-system literature (Doyle/de Kleer), which is
    the formal home of "retract conclusions when their justifications change" and would give LIMB A a
    proper citation rather than a principle; and the certificate-revocation / CRL-vs-OCSP literature,
    which is the best-engineered analogue for "how much re-validation does a change oblige."

  Recommendation: CHALLENGED — resting on LIMB B, where the challenge is an exact calculation and not a
    matter of judgement: 2 of 147 with zero failures licenses only the exclusion of >113 stale at 95%
    confidence. LIMB A is PARTIALLY-CHALLENGED: correct in principle, unscoped in practice, and
    unsustainable at nightly-ingest scale without delta propagation. **Note for the register:
    PREMISE-182 already contained the closed form. This is a propagation failure (PREMISE-123), not a
    novel finding, and the same observation applies to ASSUMPTION-1309, -1311 and -1312 in this batch.**
