SEARCH-AGAINST-PRESUMPTION-908:
  Date searched: 2026-09-05
  Original item: PRESUMPTION-908
  Original statement: [inferred] Eight parallel workers with no shared context produce mutually consistent
    classifications, and the one consistency check performed (the row-header rule, ~40 cells) is
    representative of inter-batch drift in general.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-908
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the single-axis consistency check and the batch architecture.
      15b: Searched for challenging literature (2026-09-05). NOTE ON AUTHORSHIP: run by the 15c
        orchestrating context after the delegated 15b subagent was interrupted; PRESUMPTION-908_for.md
        was NOT read. See PRESUMPTION-906_against.md for the full independence declaration.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Barrie, Palmer & Spirling (attribution NOT verified in this search), "Prompt Stability Scoring for
       Text Annotation with Large Language Models," arXiv:2407.02039 [VERIFIED: title/ID] — Items near a
       decision boundary flip label under repeated runs of the same prompt and under semantically
       equivalent rephrasings; decoding stochasticity is an independent source of run-to-run variation.
       Challenge: eight workers are eight runs; boundary cells (III.3 vs III.4, 146 vs 151 cells) are
       precisely where the literature predicts disagreement, and that axis was never checked.
    2. "What Is Actually Being Annotated? Inter-Prompt Reliability…," arXiv:2604.16413 [VERIFIED:
       title/ID; authors NOT verified] — Single-prompt LLM annotation instability is systematic, not
       random, and is reduced only by controlled aggregation across prompts/runs; discrete categories
       show markedly lower inter-prompt agreement than continuous scores. Challenge: the pipeline has one
       prompt, one run per cell, discrete labels, and no aggregation.
    3. "Rubric-conditioned large language model labeling: Agreement, uncertainty, and label consistency
       in subjective text annotation," Computers in Human Behavior 2026, S0747563226000853 [VERIFIED:
       title/journal/ID; authors NOT verified] — Written rubrics improve but do not close consistency
       gaps on subjective boundaries. Challenge: the CLASSIFY_SPEC is a rubric; the literature says a
       rubric is necessary and insufficient.
    4. "Temporal Simultaneity Predicts Annotation Quality in Sentiment Corpora," arXiv:2605.27239
       [VERIFIED: title/ID; authors NOT verified] — Annotation quality co-varies with when/how annotation
       sessions are run; annotator-specific biases accumulate over a session. Analogous challenge for
       long-context workers whose interpretation drifts across a batch.
    5. Annotation-practice sources (OpenTrain / Claru glossaries; galileo.ai on judge calibration)
       [VERIFIED: pages located; practitioner, not peer-reviewed] — Standard practice for independent
       annotators under written guidelines is a double-annotated overlap sample with reported κ, plus
       mid-campaign re-labelling of a random sample to detect drift; reported initial κ values of 0.25
       and α of 0.13 before guideline revision show how low unadjudicated agreement can be. Challenge:
       the pipeline ran zero overlap and reports no κ.

  Strength of challenge: Moderate

  Summary: The literature does not say parallel LLM workers are inconsistent in general — intra-model
  agreement on clear cases is high — but it says consistency collapses precisely at decision boundaries
  and under discrete labels, and that the only way to know where a given corpus sits is an overlap sample
  with a reported agreement statistic. The presumption's second limb is the weaker one: no source
  supports generalising from one checked axis (a syntactic row-header rule, the easiest kind of case) to
  the semantic node-choice axis where the literature predicts the drift to be. The single check was run
  on the axis least likely to show a problem.

  Specific risks:
    - "Thin" flags on I.3.1, I.3.3, I.5 may be batch artefacts (one worker's boundary policy) rather than
      corpus facts.
    - The III.3/III.4 near-tie (146 vs 151) is inside the range a boundary-policy difference between
      two workers could produce.
    - Facet fields (`about`, `discipline`, `work_order`) were never cross-checked at all.

  Mitigations available:
    - 50-cell overlap across two batches; report κ per field (already named by 14b).
    - Mid-run re-label of a random sample to detect within-batch drift.
    - Aggregate two decorrelated runs on boundary nodes only, per the inter-prompt reliability result.

  Search scope: Preliminary — 2 queries specific to this item plus one shared with PRESUMPTION-906.
  Not covered: the crowd-sourcing literature on batch effects in human annotation (Snow et al. and
  successors), which would supply base rates for inter-batch drift.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-908
    Strongest counterargument: Consistency was checked where it was cheapest and least informative. A
      row-header rule is a syntactic test with a near-deterministic answer; node choice at III.3/III.4 is
      a semantic boundary, and the prompt-stability literature says that is where the same model, same
      prompt, flips. Eight workers with no overlap is a design that cannot detect its own drift: every
      count in toc_sandbox.csv is the sum of eight possibly different boundary policies, and the
      near-ties and "thin" flags that the summary reports as findings are within the range that one
      worker's policy could manufacture. The field's standard remedy costs 50 cells.
    What would need to be true for C2A2 to be safe: κ ≥ ~0.7 on node choice and on each facet over an
      overlap sample spanning at least two batches; or all boundary-adjacent cells re-run with
      aggregation.
    How to test: The 14b-named 50-cell overlap, extended to report κ per field, with the sample
      deliberately enriched for III.3/III.4 and I.3.x cells.
