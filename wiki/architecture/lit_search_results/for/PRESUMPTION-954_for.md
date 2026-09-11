SEARCH-FOR-PRESUMPTION-954:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-954
  Original statement: "[inferred] That a caveat attached to a number neutralises the number's
    load-bearing role — that labelling an estimate 'a prompt to measure, not a finding' prevents it from
    functioning as a finding downstream."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-954
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the gap between a run's own honesty and the shape of the artefact it shipped;
        surfaced with the credit stated — catching a misreported source by reading it is the best
        verification act the pipeline has performed.
      15a: Searched for supporting literature; found none in the FOR direction, and found that an ACTIVE
        premise already states the contrary position almost verbatim.
    Current status: NO-SUPPORT-FOUND

  Register pre-check: **PREMISE-188 states the contrary of this presumption in near-identical terms and
    is ACTIVE.** 14b's note to check this is confirmed. Quoting the register index entry:
      PREMISE-188: "AN EVIDENTIARY QUALIFIER TRAVELS WITH THE CLAIM OR IT DOES NOT TRAVEL. A caveat
      placed in a document header does not govern the claims in the body once those claims are quoted,
      and the loss is systematic rather than careless. (1) THE STRIPPING IS SELECTIVE, NOT ACCIDENTAL.
      Hedged statements diffuse..."
    This is not a premise that merely bears on the item; it is the item's negation, already validated.
    Also bearing:
    - PREMISE-132 (ACTIVE) — citing is not verifying; in generated text the measured rate of full
      support between a sentence and its own citation is roughly half.
    - PREMISE-148 (ACTIVE) — quotation error rates are measured and are not small.
    - PREMISE-178 (ACTIVE) — an existence check and a label check do not establish that a cited source
      supports the sentence it anchors.
    - PREMISE-103 (ACTIVE) — absence of primary text is a kind-difference in evidence; downgrading
      confidence is not a valid substitute for an explicit "unfounded pending retrieval" state. **This
      one bears on PREMISE-201's clause (3) directly**: the AJR mammography quote that failed retrieval
      should, under PREMISE-103, have produced an unfounded-pending-retrieval state rather than an
      unverified flag on a minted premise.
    Recording the hits per OPEN-192; searched anyway, which is the only way PREMISE-188 could ever be
    re-exposed — i.e. this item is a live instance of PRESUMPTION-948's question.

  LIMB SPLIT:
    Limb A (ADJACENCY SUFFICES): a caveat written in the same sentence or the same record neutralises
      the number it qualifies for all downstream consumers.
    Limb B (RELABELLING IS REMOVAL): an artefact whose claim is relabelled rather than withdrawn no
      longer carries the claim.

  Supporting evidence found: No

  Sources:
    1. Hedge-omission finding in the citation literature, as reported in the uncertainty-cue and
       citation-fidelity work (arXiv:1710.08327, "A Scalable and Adaptive Method for Finding
       Semantically Equivalent Cue Words of Uncertainty"). — SECONDARY — "When scientists paraphrase
       assertions containing hedges from publications in the literature, they often omit the original
       hedges, and such omissions may distort the uncertainty expressed in the original assertions."
       This is the direct measured refutation of Limb A: the qualifier is exactly what is dropped at the
       point of reuse.
    2. Diachronic hedging study in *Science* research articles, 1997–2021, reported in Scientometrics
       (dl.acm.org/doi/abs/10.1007/s11192-023-04759-6) and in secondary coverage. — SECONDARY — Hedging
       words such as "might" and "probably" fell by **about 40%** over two decades in one leading
       journal. Note this is a claim about *authors' own writing*, not about downstream stripping, and
       the ~40% figure reached me through a secondary summary of the paper rather than the paper itself
       — it is SECONDARY and should not be quoted as if read.
    3. "The Noisy Path from Source to Citation: Measuring How Scholars Engage with Past Research"
       (arXiv:2502.20581). — SECONDARY (abstract-level) — Citation-fidelity work measuring systematic
       differences in what is preserved and lost when a source is cited. Located but not read in full;
       named because it is the current primary source for this question and should be retrieved if the
       item is pursued.
    4. "Citation accuracy, citation noise, and citation bias: A foundation of citation analysis"
       (arXiv:2508.12735). — SECONDARY (abstract-level) — Frames citation distortion as a structural
       property of reuse rather than an author-level lapse. Consistent with PREMISE-188's clause that
       the stripping is systematic rather than careless.
    5. "Citations and certainty: a new interpretation of citation counts," Scientometrics (2019),
       doi 10.1007/s11192-019-03016-z. — SECONDARY (abstract-level) — Argues citation counts partly
       track the *certainty* attributed to a claim, i.e. repeated citation converts a qualified claim
       into a settled one. This is the mechanism by which REVISE-445's "mid-teens to low twenties"
       estimate will harden if it is cited twice more.

  Strength of support: None

  Summary: I searched the FOR direction and found nothing supporting either limb, and a coherent body of
    work refuting both. The specific measured finding is that hedges are dropped at the paraphrase step
    — which is the step every downstream consumer in this estate performs — and the broader finding is
    that repeated citation itself increases the perceived certainty of a claim independent of its
    evidential basis. The estate's own register reached this conclusion first: PREMISE-188 states that
    an evidentiary qualifier travels with the claim or it does not travel, and that the loss is
    systematic rather than careless. That makes this item, as 14b noted, an instance of PRESUMPTION-948
    rather than an independent question — and it is worth recording that searching it anyway produced
    something useful, namely the confirmation that PREMISE-188's claim survives a fresh independent
    search. Two concrete consequences follow for the named artefacts. REVISE-445 carries the
    "mid-teens to low twenties" estimate relabelled rather than removed; under the hedge-omission
    finding, the relabel will not survive the next paraphrase, so the estimate should be *removed* from
    the artefact body and held in a provenance field, not re-worded. PREMISE-201's clause (3) rests on
    an unretrievable AJR quote; PREMISE-103 (ACTIVE) says confidence-downgrading is not a valid
    substitute for an explicit unfounded-pending-retrieval state, so the clause should be excised
    pending retrieval rather than flagged — and the fact that the register has no mechanism to do this
    is PRESUMPTION-948 again, exactly as 14b said.

  Caveats: The citation-fidelity literature concerns human scholarly writing at scale; this estate is a
    small closed system where a determined consumer could be *required* to read the provenance field.
    That is a real disanalogy and it is the only route by which Limb A could be rescued — not by the
    caveat's adjacency but by an enforced read. The provenance protocol's epistemic-weight table keys on
    item type and status and has no such field, which 14b already observed. None of the five sources was
    retrieved as full text; all are SECONDARY at abstract or summary level, and the ~40% hedging-decline
    figure in particular should not be quoted as verified.

  Search scope: comprehensive — searched hedge-stripping in citation chains, uncertainty propagation
    through document reuse, citation fidelity and distortion, diachronic hedging trends, and
    certainty-attribution effects of citation counts. Did not search the risk-communication literature
    on disclaimer efficacy (FTC/advertising disclosure comprehension studies), which is the one
    remaining place a FOR-direction finding could plausibly live and which would be the right next step
    if anyone wants to defend Limb A.

  Recommendation: NO-SUPPORT-FOUND. Both limbs fail and the recommendation rests on both. The item is
    already answered adversely by PREMISE-188 and the fresh search independently confirms it, which is a
    useful result for OPEN-192: re-exposing a settled claim cost one search and returned a
    corroboration rather than a saving-that-was-wasted. The actionable residue is the two named
    artefacts — REVISE-445 and PREMISE-201 clause (3) — and the in-house test 14b specifies (follow both
    forward one cycle and see whether any consumer cites the estimate without the caveat) will settle
    the instance in a cycle. The general claim does not need settling; it is settled.
