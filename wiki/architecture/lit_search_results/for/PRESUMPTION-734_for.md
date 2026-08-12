SEARCH-FOR-PRESUMPTION-734:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-734
  Original statement: That the strict/loose pair is a safeguard rather than an alarm nobody reads; it now reports monotone register decay — eleven REVISE ids over two days with zero new strict blocks, DISPOSITION shortfall 32 -> 46, premises max-minus-blocks 43 -> 44, presumptions loose exceeding max by 2 — measured only by 14a, reported by no run, repaired by nothing. NOTE: extends PRESUMPTION-687.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-734
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: read six days of 14a's own strict/loose measurements as a trend rather than as a nightly figure
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Alert fatigue literature (Icinga, Datadog, Splunk, LogicMonitor practitioner guides, 2025-2026): well-documented pattern that monitoring signals which are generated but not acted upon lose their function as safeguards; recommended remediation is "if a warning is always ignored, remove it or convert it to a dashboard metric" — directly on point for a strict/loose pair that measures decay but triggers no action. [unverified — from search snippets, industry sources]
    2. "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime" (arXiv, 2606.14589, 2026). Documents production LLM-agent systems where errors are logged diligently, recover silently, and leave a gap that surfaces only much later in a downstream report — closely analogous to a metric being measured (by 14a) but never aggregated or reported.
    3. Referential-integrity / orphaned-record detection literature (database engineering practitioner sources, e.g. Acceldata, MoldStud): establishes that append-only or loosely-constrained data stores accumulate orphaned/inconsistent records unless an active reconciliation process runs; passive logging without reconciliation is described as insufficient by design. [unverified — from search snippets, industry sources, not peer-reviewed]
    4. "A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents" (arXiv, 2606.12320, 2026) — argues governance signals in agent runtimes require a distinct "observability plane" that aggregates and surfaces drift metrics; a measurement plane without an aggregation/response plane is characterized as non-functional oversight, matching the presumption's claim that the metric is "measured only by 14a, reported by no run, repaired by nothing."

  Strength of support: Moderate

  Summary: There is solid analogous support from alert-fatigue research and from recent (2026) papers on LLM-agent runtime governance and silent-failure taxonomies: a metric that is measured but not aggregated, reported, or acted on functions as a record rather than a safeguard, and this is a recognized failure mode in both classical monitoring and emerging agentic-system observability literature. No source addresses a "strict/loose" register pair specifically, but the general claim — that unread/unaggregated audit signals are not safeguards — is well established across two independent literatures (SRE/monitoring and AI-agent governance).

  Caveats: Much of the strongest material is 2026 arXiv preprints on AI-agent governance, which are recent and not yet independently replicated or peer-reviewed; industry blog sources on alert fatigue are practitioner consensus rather than controlled studies. No literature examines the specific numeric pattern described (DISPOSITION shortfall growth, max-minus-blocks drift) — the presumption's quantitative specifics remain untested by any external source.

  Recommendation: PARTIALLY-SUPPORTED
