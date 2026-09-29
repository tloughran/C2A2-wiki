SUPPLEMENT — second 15a pass, 2026-09-29 (concurrent-writer collision)

  PROVENANCE:
    Origin: 14a / 14b (items as listed)
    Chain: [14a|14b → 15a (second pass)]
    Transform at this step: A second, concurrent run of scheduled task `c2a2-lit-search-pipeline` ran 15a on
      the same 7-item cohort. Its per-item files were written to this folder and then overwritten by the
      first run's shorter files (the versions now on disk). This supplement is RECONSTRUCTED from the second
      15a agent's final report, not from its lost files; citations below keep the fetch status that agent
      reported. The first run's files are untouched.
    Current status: SUPPLEMENTARY — not dispositioned separately (see for_lit_search.md 2026-09-29 addendum)

  ASSUMPTION-1682 — SUPPORTED, Strong (as a necessary condition only). Mayo 2018, Statistical Inference as
    Severe Testing (author interview fetched; book not read); Lakens 2017, SPPS 8(4), equivalence tests
    (search-result level); Popper, Platt — unverified (background knowledge). Caveat: "could observe either
    outcome" is necessary, not sufficient — detection probability must also be adequate.

  ASSUMPTION-1684 — PARTIALLY-SUPPORTED, Moderate. PCAOB AS 2201 para. B29 (fetched): a prior baseline may
    be carried forward without re-testing if the item is verified unchanged and change controls operate.
    Engström et al. 2010, regression test selection (search-result level); ISO 17021 (unverified). Every
    precedent also requires a periodic fresh full review (~3-year cycle). Differs from the on-disk file
    (NO-SUPPORT-FOUND / None, one query).

  ASSUMPTION-1690 — SUPPORTED, Strong. Supabase docs "Project Pausing" (fetched; last modified 2026-09-28):
    7-day window confirmed; criterion is "sufficient" database activity (docs suggest a few requests per
    day), so a single keep-warm ping may not reset the clock; warning email ~1 week before pause; paused
    projects restorable for up to 1 year with data retained.

  ASSUMPTION-1692 — PARTIALLY-SUPPORTED: Moderate that a second searcher adds diversity, Weak that it is
    worth the cost. Waffenschmidt et al. 2019 (second screener recovers median ~5% of studies a single
    screener misses; abstract via search only); Bramer et al. 2017 (overlapping databases each add unique
    records; search-result level; fetch hit HTTP 429); Krogh & Vedelsby 1995 (unverified).

  ASSUMPTION-1693 — SUPPORTED, Strong. Schäfer & Schwarz 2019, Frontiers in Psychology (fetched): median
    r = 0.36 without preregistration vs 0.16 with. Button et al. 2013 (search-result level); Ioannidis 2005,
    GRADE (unverified).

  PRESUMPTION-1088 — PARTIALLY-SUPPORTED, Weak. Shermis & Hamner (automated essay scoring agrees with human
    graders on short prompted essays; search-result level); Page (unverified). Scope does not reach
    interpretive prose; the AES literature is itself contested.

  PRESUMPTION-1089 — NO-SUPPORT-FOUND, None as stated (Weak for a version with verification). PCAOB B29
    (fetched) permits reliance on prior work only after the record is verified; Bikhchandani et al. 1992
    (unverified). Literature mostly argues the other way.

  NOVELTY: none flagged.
  Fetch failures: PubMed (Button, Waffenschmidt) empty; PMC blocked by CAPTCHA (not attempted); Springer 429.
  Excluded: echo-titled GitHub issue ("[SB-01] … FREE plan …"); Supabase SEO blogs; compliance-vendor pages;
    RAG-Fusion explainers; USPTO PDFs; a self-published Zenodo "falsifiability audit" record.
