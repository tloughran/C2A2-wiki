SEARCH-FOR-ASSUMPTION-276:
  Date searched: 2026-06-06
  Original item: ASSUMPTION-276
  Original statement: P3 ("one app, two projections") with a Q2 quality-gate promotion pipeline as the membrane between directory and graph is the correct target architecture; graph membership earned by self-articulation makes the graph a measurement surface.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-276
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a stated target-architecture commitment to a quality-gated promotion pipeline between a directory tier and a graph tier.
      15a: Searched staged / quality-gated data-pipeline literature (progressive promotion, tiered visibility).
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Databricks / Microsoft Learn, "Medallion lakehouse architecture (Bronze/Silver/Gold)." — Canonical staged pipeline that incrementally improves data quality across tiers, with quality enforced at transition points between layers rather than once at the end. Strong analogous support for a directory->graph "membrane" that promotes records as they meet a quality bar.
    2. DataKitchen, "The Race for Data Quality in a Medallion Architecture"; Great Expectations gate practice. — Documents quality gates applied AT transitions (schema/completeness/conformity at Bronze->Silver), validating the idea of a Q2 gate as an explicit checkpoint that records must pass to be promoted.
    3. Tiered-visibility / progressive-promotion patterns (medallion Gold = curated, consumption-ready). — Supports "graph membership earned by promotion": the curated tier is precisely the promoted, validated subset, and treating it as the trusted/measurement surface is standard.

  Strength of support: Moderate-Strong (analogous)

  Summary: The staged, quality-gated promotion pipeline is a mainstream, well-validated data-architecture pattern (medallion bronze/silver/gold with gates at each transition), giving strong analogous support to P3's directory->graph membrane and to treating the promoted/curated tier as the trusted surface. The mechanism — admit raw to a low tier, promote to a higher tier only on passing a quality gate — is exactly the proposed architecture. Support is PARTIAL rather than full because the analogy is domain-transferred: medallion gates measure data-quality attributes, whereas P3's gate measures community self-articulation, importing a normative criterion (see PRESUMPTION-308) that the data-pipeline literature does not vouch for.

  Caveats: The data-pipeline literature endorses quality-gated promotion for DATA quality, not for PARTICIPATION/visibility. The transfer carries two risks the source literature does not cover: (a) the gate criterion (self-articulation) is normative, not a neutral quality metric (308); (b) once the graph is a "measurement surface," the gate's criterion becomes a target communities optimize for (Goodhart) — see 15b. So the architecture pattern is supported; the specific criterion and its measurement-surface status are not validated by this literature.

  Recommendation: PARTIALLY-SUPPORTED
