SEARCH-AGAINST-ASSUMPTION-292:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-292
  Original statement: The existing 571-session DB is representative enough to prove the pipeline without a full reseed.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-292
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated design assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Etikan, Musa, Alkassim, 2016. "Comparison of Convenience Sampling and Purposive Sampling." Am. J. Theoretical & Applied Statistics. — Convenience samples (data that happens to be on hand) systematically under-represent subgroups absent from the collection channel; findings generalize only to the channel, not the population.
    2. Quiñonero-Candela, Sugiyama, Schwaighofer, Lawrence (eds.), 2009. "Dataset Shift in Machine Learning." MIT Press. — Pipelines validated on one data distribution fail in characteristic ways (covariate shift, prior shift) when the full distribution arrives; "it ran on the sample" does not bound behavior on the reseed.
    3. Numberanalytics/Checkbox survey-methods syntheses, 2024-25 ("Avoiding Convenience Sampling Bias"). — Precision-vs-representativeness distinction: large convenient N gives tight confidence intervals around a biased answer; 571 sessions can confidently mislead.
    4. Hellerstein, J., 2008. "Quantitative Data Cleaning for Large Databases." UNECE. — Data-quality pathologies (missing fields, format drift, encoding changes) cluster in older/edge-case records — precisely the records a partial DB excludes, so the sample is easiest where the pipeline is least at risk.
  Strength of challenge: Moderate
  Summary: The challenge depends on what "prove the pipeline" means. For *mechanical* validation (schema parsing, joins, rendering), the literature on pilot studies explicitly endorses convenience samples — this use is safe. But the 571-session DB is a convenience sample shaped by the known capture gap, so it is biased exactly along the dimensions that matter for the Agent Explorer's content claims: which agents exist, their relative volumes, and edge densities. Dataset-shift results warn that code paths and distributional summaries validated on the partial DB can both break on reseed (new session types, older formats, higher volumes). The risk concentrates where PRESUMPTION-326 already points: low-frequency and uncaptured agents.
  Specific risks: Pipeline "proven" on captured-session types fails on uncaptured ones at reseed; worse, it doesn't fail but silently produces an explorer whose agent roster and rankings were calibrated on a biased sample and are trusted thereafter.
  Mitigations available: Scope the claim explicitly to mechanical validation; enumerate known ways reseed data differs (date range, session types, formats) and test one exemplar of each; treat all distributional outputs (counts, rankings, edges) as provisional until post-reseed regeneration; add row-count and schema assertions that will surface shift loudly.
  STEELMAN:
    Strongest counterargument: This is precisely the textbook-sanctioned use of a convenience sample: a feasibility pilot where the question is "does the machinery work," not "what is the population parameter." 571 sessions across 7+ agent types exercises every join, parser, and renderer; a full reseed before proving the pipeline would be premature optimization and delay feedback. The pipeline is rerunnable, so any reseed-time breakage is cheap to fix.
    What would need to be true for C2A2 to be safe: No conclusions about agent population structure are frozen from the partial DB; reseed is actually performed before the explorer is treated as authoritative; the sample spans all structurally distinct session formats.
    How to test: After full reseed, diff per-agent session counts and explorer edge structure against the 571-session version; large rank reorderings falsify "representative enough."
  Search scope: 1 search — "convenience sample not representative pilot data validation bias generalization failure". Plus established dataset-shift literature.
  Recommendation: PARTIALLY-CHALLENGED
