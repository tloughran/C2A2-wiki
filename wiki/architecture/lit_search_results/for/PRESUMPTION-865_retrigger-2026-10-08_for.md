SEARCH-FOR-PRESUMPTION-865 (OWED LIMB ONLY: recoverability):
  Date searched: 2026-10-08
  Original item: PRESUMPTION-865
  Original statement: "Reducing collection breadth is low-cost when the collected items are not being consumed."
  Limbs searched: the RECOVERABILITY limb only, i.e. whether non-uniform coverage introduced by an
    adaptive collection policy into a not-yet-consumed corpus can be recovered once consumption begins.
    "Support" = evidence that such a coverage gap can be corrected after the fact, by reweighting or by
    back-fill re-search. The breadth limb (cycle 0, comprehensive) is not re-searched.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-13, MONITOR-552; processed 2026-10-08)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-865
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the asymmetry between the stated cost (queue depth) and the unstated cost (coverage)
      15a (cycle 0, 2026-08-25): SUPPORTED, Moderate. Comprehensive on breadth (Halladay 2015; Bramer
        2017; 2022 metaresearch), preliminary on recoverability, which was flagged as the unaddressed
        sub-claim
      15b (cycle 0): PARTIALLY-CHALLENGED, Moderate, with no targeted query; one analogical cost-inversion source
      15c: DISPOSITION-812 → MONITOR-552 (HIGH)
      15d: re-triggered cycle 1 2026-09-13; owed = adaptive-sampling bias/IPW; SR database-coverage bias;
        file-drawer at the never-searched level; 15d did not evaluate evidence
      15a (cycle 1, 2026-10-08): 3 searches, 2 fetches; see below
    Current status: PARTIALLY-SUPPORTED (recoverable under two stated conditions; not recoverable by
      reweighting where a channel had zero collection probability)

  Search scope: 3 web searches: (a) IPW / AIPW for adaptively collected data; (b) Rubin ignorability and
    informative sampling designs; (c) the impact of restricted or selective database searching on
    meta-analytic estimates, with retrospective re-search. Fetches: par.nsf.gov/biblio/10311708 (Hadad et
    al., PNAS abstract) and abstracts.cochrane.org 2015-vienna (Hartling et al., full abstract). All three
    owed literatures reached. The file-drawer limb was reached only indirectly, through the
    restricted-search studies, which are its "never searched" form. Preliminary scope.

  Supporting evidence found: Partial (conditional)

  Sources:
    1. Hadad, V., Hirshberg, D. A., Zhan, R., Wager, S. & Athey, S., 2021. "Confidence intervals for policy
       evaluation in adaptive experiments." PNAS 118(15). [fetched, abstract; author list from
       search-result] "With adaptively collected data, common estimators based on sample means and inverse
       propensity-weighted means can be biased or heavy-tailed", especially for "parameters that were not
       targeted by the data-collection mechanism". The authors present adaptively reweighted AIPW
       estimators that are asymptotically normal. Supportive reading: bias from an adaptive collection
       policy is correctable after the fact when the policy's selection probabilities were LOGGED and
       stayed above zero. The same abstract defines the limit: as propensities decay toward zero the
       correction degrades, and at zero it is undefined.
    2. Rubin (1976/1987) ignorability, as stated in Sugden & Smith 1984 (Biometrika) and related sources.
       [search-result] If selection depends only on observed data, the mechanism can be ignored for
       likelihood/Bayesian inference but NOT for design-based inference. Sugden & Smith add that a design
       which is ignorable when fully known "may become informative" when the analyst has only partial
       information about it. Supportive reading, again conditional: recoverability turns on a record of
       which channels were searched, and why.
    3. Hartling, L., Featherstone, R., Nuspl, M., Shave, K. & Vandermeer, B., 2015. "The impact of selective
       searching on the results of systematic reviews." Cochrane Colloquium, Vienna (oral). [fetched, full
       abstract] Re-ran the primary meta-analyses of 57 ARI reviews using MEDLINE only and MEDLINE plus each
       other database, after searching 13 databases for the reference set. 65 of 398 studies were not in
       MEDLINE. The mean point-estimate ratio was 1.06 for MEDLINE alone and fell to 1.03 with BIOSIS; 5
       meta-analyses changed significance with MEDLINE alone and 1 with MEDLINE+EMBASE. The method is the
       evidence: a channel omitted at collection time was searched retrospectively and its contribution
       recovered. That is the back-fill route, done at scale, on a corpus whose consumption (the original
       review) had already happened.
    4. Restricted-search metaresearch (unnamed meta-research study in search summary; ISPOR 13th meeting
       presentation; Duyx et al. 2019 abstract-reporting case study). [search-result] Restricted searches
       missed studies in up to 100 meta-analyses. Deviation in effect size was log-linearly related to the
       proportion missed, and the direction was unpredictable (Duyx: pooled RR 1.10 on 12 detectable
       articles vs 1.03 on all 28). Recorded as the boundary: the gap is not self-correcting and its sign
       cannot be known in advance, so recovery requires an actual back-fill, not an adjustment.

  Strength of support: Moderate for the conditional; Weak for the unconditioned claim.

  Summary: The literature supports recoverability, but only through two distinct routes, each with a
    precondition. (a) Statistical correction: adaptive-design inference (Hadad et al.) corrects bias from
    an adaptive collection policy after the fact, provided the policy's selection probabilities are logged
    and nonzero. Survey theory (Rubin; Sugden & Smith) adds that the design must be known to the analyst,
    not merely have happened. (b) Back-fill: Hartling et al. show that in bibliographic collection the
    omitted channels can be searched retrospectively and their contribution measured and restored. This
    works because the channels persist and are re-queryable. Where neither precondition holds (a channel
    that had zero probability of collection and is no longer queryable as it stood, or a selection policy
    that was not recorded), nothing found supports recoverability. The restricted-search studies show the
    resulting error is unsigned. The file-drawer problem relocated to "never searched" is therefore real,
    but it is repairable under (a) or (b).

  Caveats: (i) Hadad et al. concern treatment-effect estimation in bandit experiments, so the transfer to
    channel-selection in a literature corpus is by analogy. (ii) Hartling et al. is a conference abstract
    with interim (ARI-only) results. (iii) Rubin/Sugden & Smith were read at search-result level. (iv) The
    back-fill route presumes that what a channel would have returned then is still retrievable now. For
    fast-moving or ephemeral sources (preprint versions, news, retracted items) that presumption is
    untested here. (v) The "never searched" sub-claim is not addressed by any source as an explicit bias
    term. The support is assembled from adjacent literatures.

  Recommendation: PARTIALLY-SUPPORTED. Recoverable if the collection policy's channel-selection is
    logged with nonzero probabilities, or if the omitted channels remain re-queryable for back-fill. Not
    recoverable by reweighting alone for zero-probability channels. Maps to MONITOR-552's "INCORPORATE in
    narrowed form" branch, conditional on those two preconditions being met in C2A2.

  NOVELTY-FLAG: Partial. Item PRESUMPTION-865. Addressed: post-hoc correction of adaptive-collection bias
    (IPW/AIPW); retrospective back-fill of omitted databases. Unaddressed: selective NON-SEARCH of channels
    treated as an explicit bias term in a deferred-consumption corpus. No source models it directly.

  Independence attestation: Read: 15a definition; provenance_protocol.md; for/PRESUMPTION-897_retrigger-
    2026-10-07_for.md; for/PRESUMPTION-865_for.md; for_lit_search.md owed-limb note; MONITOR-552. NOT read:
    any against/ file dated 2026-10-08.
