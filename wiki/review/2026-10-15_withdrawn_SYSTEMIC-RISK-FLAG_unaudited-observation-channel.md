SYSTEMIC-RISK-FLAG:
  Date: 2026-10-15

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1141, PRESUMPTION-1146
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced both presumptions on 2026-10-14 from transcripts and a 14a ls check.
      15b: Searched for challenging literature on each item (2026-10-15); identified a shared vulnerability across the two results.
    Current status: CHALLENGED (both items, 15b direction only; awaiting 15a and 14b reconciliation)

  Affected items: PRESUMPTION-1141, PRESUMPTION-1146

  Common vulnerability: Both treat what an unaudited observation channel shows as direct evidence about the process behind it, without a record of how that observation was generated.
    - 1141: a valid-looking file is taken to mean "my pipeline ran correctly", although the writer, run and freshness are unrecorded.
    - 1146: an empty search result is taken to mean "the thinker produced nothing", although the search channel's coverage, lag and reproducibility are unmeasured.
  In both, a weak oracle (syntax/timestamp check; search hit/no-hit) stands in for knowledge of the generating process. Errors are silent and one-sided: a false PASS, or a false "silence". Neither job records enough metadata (run ID; channels checked and their coverage) to detect the gap later.

  Literature basis: W3C PROV-Overview (Groth & Moreau 2013; read). Barr et al. 2015, "The Oracle Problem in Software Testing" (abstract read). Lewandowski & Mayr 2006, "Exploring the Academic Invisible Web" (abstract read). Lewandowski et al. 2006/2008, freshness studies (snippet). Gusenbauer & Haddaway 2020, reproducibility of academic search (quoted via PLOS blog, read). Pirkola 2009 coverage bias (abstract read).

  Risk level: High

  Recommendation (for 14b/Agent 12 consideration; 15b makes no design decision): Consider a cross-cutting rule that any agent verdict based on presence or absence of an observation also records the channel and generating process (run ID; channels searched with dates). Unattributed or uncovered observations would carry a distinct status (e.g. UNATTRIBUTED / NOT-SAMPLED) rather than PASS or "nothing new". Check other presumptions (e.g. PRESUMPTION-1147, unreconciled counts) for the same pattern.
