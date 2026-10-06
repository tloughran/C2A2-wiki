SEARCH-FOR-PRESUMPTION-1113:
  Date searched: 2026-10-04
  Original item: PRESUMPTION-1113
  Original statement (presumption under test): One PASS/FAIL field can carry both whether a run succeeded and whether its data are fresh.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1113
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (lane: observability; job health vs data freshness/SLOs; data-pipeline freshness monitoring).
      15a: Searched for supporting literature; found precedent for freshness folded into a single health status, but always as graded states and computed separately from run success; strength: Weak
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. "Your Service Is Healthy, but Its Data Isn't: Rethinking Cloud-Native Health Checks." Cloud Native Now (contributed content) [search-result]: Argues that freshness "should be treated as an application-health signal". This supports folding freshness into a health verdict. The article recommends intermediate states (healthy → degraded → stale) rather than a binary.
    2. Health-endpoint examples (e.g. worldmonitor.app health endpoints docs; a Hugging Face data_flow_monitor) [search-result]: Production health endpoints that return a single roll-up status in which staleness is a failure condition (green/yellow/red by data age; HEALTHY/WARNING/DEGRADED/UNHEALTHY with per-key STALE flags). This is empirical precedent for a single field carrying freshness. The fields have more than two states and come with per-component detail.
    3. dbt Labs, `dbt source freshness` (docs; Paradime/Hevo guides) [search-result]: Freshness yields pass/warn/error, and an error fails the command. This is precedent that freshness can be expressed as a PASS/FAIL-type verdict. It is a *separate* command from `dbt run`/`dbt build`, so run success and freshness are reported in distinct results, not one field.
    4. Data-SLO practice (dev.to "Designing batch data pipelines around SLAs and SLOs"; Airbyte, Metabase on data freshness) [search-result]: Explicitly advises against using job success as the SLI. This is listed for completeness. It indicates the two signals are treated as distinct in the observability literature.

  Strength of support: Weak

  Summary: There is real-world precedent for collapsing freshness into a single health or status verdict: health endpoints that go red when data are stale, and dbt freshness errors that fail a command. In that narrow sense one status field *can* encode freshness, especially as a conjunctive "OK only if ran AND fresh" roll-up. However, every precedent found either (i) uses more than two states to distinguish "ran but stale" from "failed", or (ii) computes freshness as a separate check from run success, even where the results are later rolled up. No source endorses a single binary field as sufficient to carry both dimensions without loss.

  Caveats: (a) A conjunctive PASS can be sound (PASS implies both), but FAIL then cannot say which dimension failed. Supportive sources address this with multi-level statuses or per-component detail. (b) Most sources are practitioner and vendor material, not peer-reviewed. (c) The presumption may hold if PASS is defined strictly as "succeeded AND fresh". Whether C2A2's usage defines it that way is outside the scope of this search.

  Search scope: preliminary (2 searches, 0 fetches): data-observability/freshness SLO material, dbt freshness docs, health-check design articles. Not searched: Google SRE workbook data-pipeline SLO chapter (background suggests it separates freshness, correctness and coverage SLOs), Nagios/Prometheus roll-up status semantics.

  Recommendation: PARTIALLY-SUPPORTED (a conjunctive roll-up has precedent; a single binary field carrying both without loss is unsupported)
