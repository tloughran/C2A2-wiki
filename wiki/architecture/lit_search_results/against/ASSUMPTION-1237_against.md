SEARCH-AGAINST-ASSUMPTION-1237:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1237
  Original statement: Reproducing five top-hub counts licenses treating week-over-week deltas as
    real.
  Generalizable limb searched: Can a positive control drawn from the most stable stratum of a
    population license inference about the changing strata?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Moderate. 3 queries (cap). Two returned directly usable methodological sources
    (positive-control selection in assay validation; validation-split construction under domain
    shift). The third, aimed at hub-stability in networks, returned only tangential material — the
    specific intersection of "control selection" and "network hub statistics" appears not to be a
    literature. Snippet-level reading only; no full texts.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1237
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Stated as the validity warrant for the run's week-over-week delta claims.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kroetsch et al. (author list not verified beyond the listing), 2024. "Selection of positive
       controls and their impact on anti-drug antibody assay performance." Journal of Immunological
       Methods; PubMed 38479453. — Finds that different positive controls yield different response
       profiles and different apparent analytical sensitivity for the same assay, and concludes that
       positive-control selection materially determines what the assay is judged able to detect.
       This is the general form of the objection: a control chosen from the easy end of the range
       certifies sensitivity the assay does not have. Abstract/snippet only.
    2. Anonymous/arXiv, 2024. "Clustering-Based Validation Splits for Model Selection under Domain
       Shift." arXiv preprint 2405.19461. — Argues that training/validation splits should be
       constructed to *maximise* distribution mismatch between the two sets, because a validation
       set drawn from the same easy region as training does not select models that generalise.
       Directly inverts 1237's logic, which validates on the region least subject to the effect of
       interest. Snippet only.
    3. Recht et al.-style replication finding, quoted at second hand inside a search result summary
       (original not located this session): reproduced experiments show published accuracies
       dropping 3-15% on CIFAR and >11% on ImageNet when the evaluation set is redrawn. Recorded as
       a snippet I saw quoted, NOT as a source I read; attribution to Recht et al. 2019 is my
       inference from the figures and should be verified before onward citation.
    4. Anonymous/arXiv, 2024. "Mean-field and fluctuations for hub dynamics in heterogeneous random
       networks." arXiv 2408.11178 (also PMC12185667). — Snippet states that because hubs interact
       with a large number of nodes, the failure of a few nodes does not change overall hub
       dynamics. Read against 1237: high-degree nodes are mathematically the stratum *least*
       sensitive to peripheral change, so their stability across a week is close to guaranteed by
       the degree distribution rather than by pipeline correctness. Snippet only.
    5. INTERNAL (recorded as evidence, not literature): the series in PRESUMPTION-897 shows the
       vault growing 3,031 → 4,729 pages with orphans growing 2,337 → 3,985 while connected pages
       moved by 69. All the change is in the disconnected periphery; the control is five top hubs.
       The control is drawn from the one stratum where, by construction, nothing was happening.

  Strength of challenge: Strong

  Summary: The control is anti-correlated with the thing it is supposed to validate. Top-hub counts
  are the highest-degree, most-linked, most-stable nodes in the graph; the week's actual change was
  almost entirely orphan accumulation in the periphery. A control that sits in the stable stratum
  can pass under essentially any pipeline fault that affects the periphery — a changed orphan
  detector, a changed link parser, a changed inclusion rule — because hub counts are dominated by
  structure that those faults do not touch. The assay-validation literature makes exactly this point
  about positive controls chosen from the easy end of the dynamic range, and the domain-shift
  literature makes the complementary point that validation sets should be built to differ from the
  training region, not to resemble it. A control that cannot plausibly fail carries no information
  about the measurement, and therefore licenses nothing.

  Specific risks: Every week-over-week delta the pipeline reports currently rests on this warrant.
  If the warrant is void, the deltas are unvalidated — which matters most for the orphan series,
  the single largest and most consequential reported movement, and precisely the quantity the
  control cannot speak to. Worse, a passing control creates positive assurance, so a genuine
  peripheral-counting fault would be reported as a validated finding rather than caught. The
  vault-growth conclusions in PRESUMPTION-897 inherit this defect directly.

  Mitigations available: Move the control into the changing stratum — pick N pages known by
  independent means to have been added, moved, or de-orphaned this week and verify the pipeline
  classifies them correctly. Add a negative control: inject a synthetic orphan and a synthetic
  connected page and confirm each lands in the right bucket. Add a control that *should* fail: run
  the counter against last week's snapshot and confirm it reproduces last week's numbers, including
  the orphan count. Cheapest of all, spot-check a random sample of the 1,648 newly-counted orphans
  by hand — the delta is large enough that a sample of 30 would detect a gross miscount.

  STEELMAN:
    Strongest counterargument: A positive control is not supposed to be sensitive to the effect
    under study — that is what makes it a control. Its job is to confirm the instrument is
    connected, the input parsed, the graph built, the counter running. Five hub counts reproducing
    exactly does rule out a large class of catastrophic failures (wrong vault, truncated read,
    parser collapse, off-by-N in the whole pipeline), and ruling those out is genuinely worth
    something. Demanding that the control also validate the periphery is demanding it be a second
    measurement rather than a control. Additionally, exact reproduction of five independent integers
    is a low-probability coincidence under most fault models, so the check is not vacuous.
    What would need to be true for C2A2 to be safe: The fault modes that could corrupt orphan counts
    would have to be a subset of the fault modes that would also corrupt hub counts. Given that
    orphan detection is a distinct code path keyed on absence-of-inbound-links, this is very
    unlikely to hold — and it is the crux. If the two quantities share no code path beyond the
    parser, the hub control is silent on the orphan claim.
    How to test: Trace the code paths. If orphan counting and hub counting diverge after the parse
    step, the hub control validates only the shared prefix, and 1237's licensing claim must be
    narrowed to that prefix. Then re-run the counter against a snapshot with known-correct orphan
    counts.

  Recommendation: CHALLENGED
