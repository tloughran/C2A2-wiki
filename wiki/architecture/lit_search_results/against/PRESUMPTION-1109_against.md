SEARCH-AGAINST-PRESUMPTION-1109:
  Date searched: 2026-10-03
  Original item: PRESUMPTION-1109
  Original statement (presumption under test): Web search over a 30-day window reliably shows a thinker's recent work, so '0 proposals' means nothing new.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1109
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a stated caveat in 9815cc97.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Martín-Martín, Orduna-Malea, Delgado López-Cózar et al., 2018, "Google Scholar as a data source for research assessment" (arXiv:1806.04435) [search-result] — Indexing speed is "irregular and unpredictable" and source-dependent; median GS lag vs Scopus about 2 months. Within a 30-day window, much genuine recent output may not yet be retrievable.
    2. Gusenbauer, M., 2022, "Search where you will find most: Comparing the disciplinary coverage of 56 bibliographic databases", Scientometrics 127:2683–2745; and a related 2024 JASIST study (ideas.repec.org/a/bla/jinfst/v75y2024i1p43-58) [search-result] — Coverage differs widely across search systems; academic search engines miss ~10–12% of Crossref-registered records (GS 9.8%, Semantic Scholar 10%). No single search tool gives complete recall.
    3. Google Scholar inclusion guidance as reported by PKP forum / SSRN support / conductscience [search-result] — New items can take weeks to months to appear; general Google search days to weeks.
    4. arXiv "Availability of submissions" [search-result] — weekend announcement gap; authoritative per-author feeds exist (API/RSS) that web search does not replace.
    5. [background-knowledge] A thinker's "recent work" for this wiki includes talks, podcasts, interviews, Substack posts and books, which are indexed and ranked inconsistently and are often date-ambiguous in search results (publish vs crawl vs event date); web search ranking favours popular older pages for name queries, so the 30-day filter depends on correct date metadata.

  Strength of challenge: Strong (as applied to the inference "0 proposals => nothing new")

  Summary: The literature on search coverage and indexing latency does not support treating a null web-search result as evidence of absence. Coverage of any single search system is incomplete (around 10% misses even for DOI-registered work), scholarly indexes lag by weeks to months with unpredictable timing, and a 30-day window is shorter than these lags. A 0 count therefore mixes "nothing new" with "new but not yet indexed, not ranked, or misdated". The source session's own stated caveat points the same way.

  STEELMAN:
    Item: PRESUMPTION-1109
    Strongest counterargument: Absence of evidence counts as evidence of absence only when the detector's recall is known and high; here recall is unknown, time-dependent (lowest for the newest items, exactly those the window targets) and channel-dependent (papers vs talks vs posts). Each run with a 30-day window and multi-week indexing lag looks mainly at items from about 2–6 weeks ago, so work can fall between runs and never be proposed. Repeated zeros will look like stability when they may be a coverage hole.
    What would need to be true for C2A2 to be safe: Searches use authoritative per-channel feeds (arXiv API by author, OpenAlex/Semantic Scholar author endpoints, the thinker's own site/Substack/YouTube RSS), lookback windows overlap prior runs with deduplication, and "0 proposals" is logged as "0 found (recall unverified)".
    How to test: Back-test: for each tracked thinker, compile ground-truth outputs for a past 30-day window from their own sites and bibliographic APIs, then rerun the web search as of that date-equivalent and measure recall.

  Specific risks: Thinker pages go stale while monitoring reports no change; systematic under-representation of thinkers whose output is non-paper (talks, posts).

  Mitigations available: Per-author API/RSS feeds; overlapping windows; periodic recall audits; recording null results as unverified.

  Caveats: No study found that measures recall of LLM-tool web search for a named author's last-30-day output specifically; challenge is inferred from general coverage/latency literature.

  Search scope: preliminary search (1 dedicated search plus 2 shared with ASSUMPTION-1739, 0 fetches); independent of 15a.

  Recommendation: CHALLENGED
