PROVENANCE:
  Origin: 15b | Chain: [14a/14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1) → SYSTEMIC-RISK flag]
  Item type: SYSTEMIC-RISK (cross-item) | Items: PRESUMPTION-896, PRESUMPTION-897, ASSUMPTION-508, ASSUMPTION-1303
  Transform at this step: pattern flag across per-item AGAINST results (header added by orchestrator 2026-10-07; 15b omitted it)
  Current status: FLAGGED — noted in DISPOSITION-1046..1050

SYSTEMIC-RISK-FLAG:
  Date: 2026-10-07
  Raised by: 15b (re-trigger cycle 1 cohort)
  Affected items: PRESUMPTION-896, PRESUMPTION-897, ASSUMPTION-508, ASSUMPTION-1303 (derived, MONITOR-598)
  Related prior flag: SYSTEMIC-RISK-FLAG_2026-10-03_action-as-outcome-proxy (this is a distinct,
    narrower pattern: the write side is treated as completing the work; the read/drain side is unmeasured).

  Common vulnerability: Each item treats a WRITE-side act as if it closed a loop whose READ/DRAIN side is
    unowned and unmeasured, and the literature found this run shows the undrained deposit decays rather
    than waiting:
      - 896: filing a defect. External drain baseline: median 36.7% of static-analysis alerts acted on,
        median 96 days to fix 4-line changes (Imtiaz et al. 2019); 61% triage (Guo & Engler 2009).
      - 897: ingesting a page. Orphans are causally under-read (Arora, West & Gerlach 2024, ICWSM);
        retrieval precision falls with index size (Reimers & Gurevych 2021). Vault: 97% of growth orphaned.
      - 508: applying a Speculative/verify flag. Wikipedia's {citation needed} backlog >350,000 articles
        (Redi et al. 2019); the item's own flag undischarged 53 days after its re-open condition fired.
      - 1303: emitting into an alert channel. Once the reader stops draining it, improving what is
        deposited does not restore draining (Harlem ICU, CHEST 2017: response 60% → 12% after alarm cut).
    In each case the estate measures the deposit (entries filed, pages added, flags set, hits emitted)
    and has no figure for the drain (fixed, read/linked, verified, attended).

  Literature basis: Imtiaz, Murphy & Williams 2019 [search-result]; Guo & Engler 2009 [search-result];
    Arora, West & Gerlach 2024 arXiv:2306.03940 [fetched abstract]; Reimers & Gurevych 2021
    arXiv:2012.14210 [fetched abstract]; Redi et al. 2019 arXiv:1902.11116 [fetched, intro only];
    Kunadu et al. 2017 via The Hospitalist [fetched secondary report].
  Secondary shared weakness: the licensing mechanism once offered for 896 is weakened (Kuper & Bott 2019,
    fetched) — the shared risk now rests on rate data, not psychology, which makes it MORE robust.

  Risk level: High
  Recommendation (what to consider, not a directive): one drain metric per channel — filed→fixed ratio
    and age (896), connected fraction + probe-question retrieval score (897), open-flag count and age
    since re-open condition (508), read/response rate on surviving hits (1303). MONITOR-585 already notes
    that a single closure-capacity number decides more than one item; this flag extends that observation
    to four. These in-house measurements, not further literature, now decide the cohort.
