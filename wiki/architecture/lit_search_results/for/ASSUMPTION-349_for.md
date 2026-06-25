SEARCH-FOR-ASSUMPTION-349:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-349
  Original statement: "Triple-column + adjudicator ~= 3-4x agent/token load per thinker track"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-349
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a cost estimate (low priority; flagged measure-at-pilot)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Wang et al. 2022. 'Self-Consistency...' ICLR 2023. - Multi-sample reasoning cost scales ~linearly in the number of sampled paths.
    2. General ensemble/self-consistency practice: N independent passes cost ~Nx the single-pass token/compute, plus aggregation overhead.
    3. (Adjacent) LLM-as-judge pipelines add one judge pass per comparison, a modest additive term on top of the N generation passes.

  Strength of support: Moderate

  Summary: The estimate is basically arithmetic and is consistent with established ensemble/self-consistency costing: three generation columns are ~3x a single pass, and one adjudicator pass adds roughly a fractional-to-1x term, landing the total in the claimed 3-4x band. The literature supports linear-in-passes scaling as the right first-order model. This is a forecast best confirmed by direct measurement, which the assumption itself acknowledges.

  Caveats: Real multipliers can exceed 4x if adjudication requires long shared contexts, retries, or multi-round arbitration; could fall below if columns share cached context. Literature is secondary to direct pilot measurement here.

  Search scope: Ensemble/self-consistency cost scaling. Adequate; empirical confirmation pending.

  Recommendation: PARTIALLY-SUPPORTED
