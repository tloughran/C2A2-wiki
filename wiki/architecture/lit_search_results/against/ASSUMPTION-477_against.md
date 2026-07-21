SEARCH-AGAINST-ASSUMPTION-477:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-477
  Original statement: 15a/15b independence became structural on 2026-07-19 for the first time; every prior disposition in the record was produced under an asserted rather than enforced independence.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-477
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline transcript
      15b: Searched for challenging literature (measured effect of blinding in peer review, anchoring between paired reviewers, confounds in before/after blinding comparisons)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Note: this item concerns the isolation regime under which the present agent is operating. It has been searched adversarially on the same terms as every other item; no attempt was made to soften the finding that the enforcement it celebrates may buy less than it claims.

  Sources:
    1. van Rooyen, S. et al., "Effect of blinding and unmasking on the quality of peer review: a randomized trial," *JAMA* (1998), PMID 9676666. 527 consecutive manuscripts submitted to the BMJ. Blinding and unmasking "made no editorially significant difference to review quality, reviewers' recommendations, or time taken to review": masked 2.82 vs unmasked 2.96; blinded 2.87 vs unblinded 2.90. The largest randomized trial of enforced blinding found essentially no effect.
    2. McNutt, R.A. et al., "The effects of blinding on the quality of peer review. A randomized trial," *JAMA* (1990), PMID 2304216. 127 manuscripts at the Journal of General Internal Medicine; blinded reviews scored 3.5 vs 3.1 on a 5-point scale. A small positive effect in a much smaller trial — the study that is usually cited for blinding's value, and it is the weaker of the two.
    3. "The impact of blinding on trial results: a systematic review and meta-analysis" (medRxiv 2023.03.05.23286821) and "Bias due to lack of patient blinding in clinical trials" (PMC4258786). Establish that blinding effects are real but heterogeneous and frequently smaller than assumed, and that measured differences between blinded and unblinded arms are commonly confounded by co-varying design features.

  Strength of challenge: Strong

  Summary: The factual claim — that independence was asserted before 2026-07-19 and enforced after — is a structural fact about this pipeline and is not challenged. What is challenged is the implication carried by the item's framing, that the pre-07-19 record was therefore materially contaminated and that the 905 existing pairs should be discounted. The largest randomized trial of blinding in the closest available analogue, van Rooyen's 527-manuscript BMJ trial, found that enforcing blinding made no editorially significant difference to review quality or to reviewers' recommendations; the small positive result usually cited, McNutt 1990, is four times smaller and reports a 0.4-point difference on a 5-point scale. If enforcement of blinding produces effects of that magnitude among human reviewers with strong professional and social incentives to be influenced by author identity, the prior for a large contamination effect in this pipeline is low, not high. The item's own proposed test is additionally confounded: re-running pre-07-19 dispositions under structural blocking will differ from the originals for reasons that include model version, prompt revision, changes in retrievable literature, and the intervening year of vault content — so any delta in 15b challenge strength is not attributable to blinding and cannot serve as the contamination estimate the item proposes.

  Specific risks: The costly error here is over-correction. If the pre-07-19 record is discounted or re-run on the strength of an unmeasured contamination assumption, the pipeline spends its scarcest resource — the drain rate that ASSUMPTION-478 identifies as the binding constraint — re-deriving 905 pairs to correct an effect the closest empirical analogue sizes near zero. The symmetric risk is subtler: declaring independence "now structural" invites the belief that the remaining sources of correlation between 15a and 15b are handled. They are not. Both agents share a model, a prompt lineage, a vault, and a search tool; structural blocking removes only the read channel, which the peer-review evidence suggests is the smaller of the correlation sources.

  Mitigations available: Do not re-run the record; instead take a small matched sample and run it under both regimes in the same session with everything else held fixed, so the blinding delta is isolated from version and corpus drift. Record the estimate with its confidence interval and stop. Separately, address the correlation sources that structural blocking does not touch: shared model, shared retrieval corpus, shared prompt ancestry. Report independence as "read-channel independence enforced" rather than "independence achieved," which is both accurate and prevents the false-security failure this vault has already named in PRESUMPTION-505.

  Recommendation: CHALLENGED

STEELMAN:
  Item: ASSUMPTION-477
  Strongest counterargument: The item treats the transition from asserted to enforced independence as an epistemic event large enough to cast doubt on 905 prior pairs, but the best available measurement of exactly this intervention says the effect is negligible. van Rooyen's BMJ trial randomized 527 manuscripts and found no editorially significant difference in review quality or recommendations between blinded and unblinded reviewers — human reviewers, with careers, rivalries, and reputational stakes in author identity, which is a far stronger contamination channel than one agent's ability to read another's file. The one trial that found an effect, McNutt 1990, is a quarter the size and reports 3.5 versus 3.1. So the empirical prior on enforcement's value is low, and the item has assumed it is high. Worse, the announcement itself carries a risk the vault has already catalogued: "independence became structural" reads as a solved problem, when the enforced channel is one of at least four correlation sources and plausibly the weakest — 15a and 15b share a model, a prompt lineage, a corpus, and a search tool, none of which structural blocking touches. And the proposed test cannot measure what it claims: re-running old dispositions under blocking varies blinding together with model version, prompt, and available literature, so the resulting delta is uninterpretable as a contamination estimate.
  What would need to be true for C2A2 to be safe: The read channel would have to be the dominant correlation source between 15a and 15b — which the peer-review evidence gives no reason to believe — and the contamination estimate would have to come from a design that varies blinding alone.
  How to test: Take 20 pre-07-19 items. In one session, with one model version, one prompt, and one corpus snapshot, run each item twice: once with 15a's file readable and once with it blocked. The paired difference in 15b challenge strength is the blinding effect, cleanly isolated. Anything larger than that design measures drift. Separately, estimate the residual correlation by running 15a and 15b on the same item under full blocking and measuring how often they cite the same sources — if the overlap is high under enforced blocking, the shared corpus is the real channel and the 07-19 change addressed the wrong one.

  Search scope: Moderate — targeted at the strongest available analogue (randomized trials of blinding in peer review). Not comprehensive on anchoring between paired evaluators outside peer review.
