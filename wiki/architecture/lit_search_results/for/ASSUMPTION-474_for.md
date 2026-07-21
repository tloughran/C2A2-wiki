SEARCH-FOR-ASSUMPTION-474:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-474
  Original statement: The vault census measures machine-dump volume rather than knowledge-graph health; the week-over-week delta mixes ~+145 real growth with ~+80 definitional difference, and the series needs a break-marker or a re-derivation.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-474
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 sewing weekly and bootstrap audit transcripts
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. European Commission, Knowledge for Policy glossary, "Break in time series." — Authoritative definition: "when data collected in a specific year are not fully comparable with the data of the previous and/or following years, we say that we have a break in the time series." Establishes that a definitional change in the counted population is a recognised, named condition requiring explicit annotation, not a nuisance to be absorbed into the delta.
    2. van den Brakel, J.A. and Roels, J. (2010). "Intervention analysis with state-space models to estimate discontinuities due to a survey redesign." Annals of Applied Statistics (arXiv:1011.2328). — Direct methodological precedent for the item's proposed remedy. States that adjustments to a survey process "have a systematic effect on the parameter estimates" and that "it is important that the effects of a survey redesign on the estimated series are explained and quantified." The item's in-house test — run both resolvers over one frozen snapshot to isolate the definitional component — is precisely the parallel-run design this literature prescribes.
    3. Ditzen, J., Karavias, Y. and Westerlund, J. (2025). "Testing and estimating structural breaks in time series and panel data in Stata." Stata Journal (arXiv:2110.14550). — Supplies the formal apparatus for detecting and dating a break when the change point is not known a priori; supports the weaker fallback if the definitional component cannot be isolated by re-derivation.
    4. Goodhart, C. (1975), as summarised in "Goodhart's Law | Laws of Software Engineering" and Chao, C. (2026), "Goodhart's Law: The Tyranny of Metrics." — Supports the first clause. The proxy-substitution pattern is named directly ("publication counts for research quality"), and the standard framing is that the failure "is not in the choice of metric but in the decision to crank up the pressure on it," which converts a measuring instrument into a target. A file count standing in for knowledge-graph health is a textbook instance. Recommended mitigation — "multiple metrics that are difficult to simultaneously game" — supports adding connectivity/orphan measures alongside volume rather than replacing one scalar with another.

  Strength of support: Strong (for the break-marker and Goodhart clauses); Weak (for the specific connectivity-metric prescription)

  Summary: Both halves of ASSUMPTION-474 have established grounding, from two separate literatures. The break-in-series half is settled official-statistics methodology: a change in the definition of what is counted makes adjacent periods non-comparable, this condition has a standard name, and the standard remedies are exactly the two the item proposes — annotate the break, or re-derive the series under one definition. The intervention-analysis literature goes further and specifies the parallel-run design for quantifying the discontinuity, which is the item's own stated in-house test. The proxy half is supported by Goodhart's law in its standard formulation, with the additional refinement that mixing a definitional shift into a reported growth number is worse than a bad proxy: it is an uninterpretable proxy, since the reader cannot tell which portion of +225 reflects the system and which reflects the ruler.

  Caveats: (a) The official-statistics literature assumes a designated statistical authority that publishes revisions; C2A2 has no such authority (this is the gap PRESUMPTION-501 names independently). (b) No literature was found measuring knowledge-graph or wiki health specifically via orphan/connectivity metrics — the search returned Goodhart material but nothing on wiki-specific connectivity indices. The claim that connectivity is the *right* replacement metric is therefore unsupported here; only the claim that raw volume is the *wrong* one is supported. That sub-claim is a partial NOVELTY. (c) Break-marker conventions assume a series with a stable publication cadence and a known revision policy; a 14-day-old series has no established baseline against which a break is meaningful.

  Recommendation: SUPPORTED
