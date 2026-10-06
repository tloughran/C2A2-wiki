SYSTEMIC-RISK-FLAG:
  Date: 2026-09-29
  Raised by: 15b (Literature Search AGAINST), second pass. A concurrent 15b writer also left a
    SYSTEMIC-RISK run note in for_lit_search.md (not read by this pass). The orchestrator should
    merge the two.
  Affected items: ASSUMPTION-1684, PRESUMPTION-1088, PRESUMPTION-1089 (related: ASSUMPTION-1682)
  Common vulnerability: A PASS or disposition, once recorded, is kept going by a signal that cannot
    detect the failure it certifies against:
      - 1684: After one full review, structural checks maintain the pass. They cannot see semantic
        edits or evidence drift (CHALLENGED, Moderate).
      - 1088: Structural checks stand in for semantic review of interpretive prose. Surface
        measures track meaning poorly, even purpose-built ones (CHALLENGED, Moderate).
      - 1089: Later runs defer to earlier dispositions, including a record known to hold an error.
        Experts converge on shown priors even when those priors are random (CHALLENGED, Moderate).
      - 1682 (related): A null is accepted when the instrument could in principle show either
        outcome, without showing that it would detect the effect (PARTIALLY-CHALLENGED).
    Together these form a loop. A text passes once. Structural QC keeps it passing (1684/1088).
    Later reviewers defer to that pass (1089). Any error introduced after, or missed by, the first
    review is never re-examined, and each re-ratification adds apparent consensus.
  Literature basis:
    - Urbach et al. (2014). NEJM 370:1029 (checklist compliance without outcome change).
    - Shojania et al. (2007). Ann Intern Med 147:224 (substantive passes decay; 23% within 2 years).
    - Ramprasad & Wallace (2024). arXiv:2411.16638 (factuality metrics reducible to surface features).
    - Manheim & Garrabrant (2018). arXiv:1803.04585 (Goodhart variants).
    - Teplitskiy et al. (2019/2020). Social influence among experts (47% moved toward random priors).
    - Stelmakh et al. (2020/2023). arXiv:2011.15083 (no herding when independent opinion comes first
      — the boundary condition, i.e. the mitigation).
    - Mayo (2018). Severe testing.
  Risk level: High
  Recommendation: The system should consider (a) labelling structure-only passes distinctly from
    semantic passes; (b) making semantic passes expire on content change or age; (c) a
    blind-first rule for reviewers before they read prior dispositions; and (d) a seeded-error
    audit to measure how many planted semantic errors the current QC-plus-deference regime
    catches. This is reported as literature evidence, not a design decision; reconciliation
    belongs to 14a/14b.
  Same-model caveat: Raised by the same model family as 15a and the QC agents. See
    SYSTEMIC-RISK-FLAG_2026-09-23_same-model-independence.
  Possible recurrence: The filename SYSTEMIC-RISK-FLAG_2026-09-10_no-second-look_1297-939-940-944
    suggests overlap. Its content was not read this run. If it is the same vulnerability, this is
    a recurrence about 19 days later, which would itself indicate the earlier flag was not acted on.
