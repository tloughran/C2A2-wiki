SEARCH-AGAINST-ASSUMPTION-1739:
  Date searched: 2026-10-03
  Original item: ASSUMPTION-1739
  Original statement: General web search indexes new arXiv postings with a lag of days.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1739
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 9815cc97.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. arXiv, "Availability of submissions", https://info.arxiv.org/help/availability.html [search-result] — Announcements Sun–Thu at 20:00 ET, none Fri/Sat; a Thursday-afternoon-to-Friday submission is not public until Sunday night. So arXiv's own pipeline adds 1–3 days before anything exists to index; "lag" measured from submission is larger than indexing lag alone.
    2. arXiv blog, "Attention arXiv users: re-implemented RSS" (2024-01-31), https://blog.arxiv.org/2024/01/31/attention-arxiv-users-re-implemented-rss [search-result] — arXiv provides daily RSS and an API listing of each day's announcements; these expose new postings at announcement time with essentially zero indexing lag, so general web search is the slow, not the authoritative, channel.
    3. Martín-Martín, Orduna-Malea, Delgado López-Cózar et al., 2018, "Google Scholar as a data source for research assessment" (arXiv:1806.04435) and Orduna-Malea et al. "Google Scholar: the 'big data' bibliographic tool" (arXiv:1806.06351) [search-result] — Google Scholar indexing speed is "irregular and unpredictable" and source-dependent; median GS-vs-Scopus difference ~2 months for journal documents; version-merging happens on major index updates. Shows that "web search" lag varies by engine from hours to months.
    4. Google Scholar inclusion guidance as reported by PKP forum / conductscience / SSRN support [search-result] — Scholar can take weeks to months for new items; general Google Search typically days to weeks.
    5. [background-knowledge] Google general web search usually indexes arXiv abstract pages quickly (often within a day) because arXiv is a high-authority, frequently crawled site; but ranking for a thinker's name + topic query is a separate issue from being indexed — a newly indexed page may not surface in top results for weeks.

  Strength of challenge: Moderate (as a boundary-condition challenge, not a refutation)

  Summary: "A lag of days" is roughly right for Google's general web index but is not a single number: it depends on the engine (general web vs Scholar vs Bing-backed AI search tools), on arXiv's weekend announcement gap, and on ranking (indexed is not the same as retrievable for a name query). Google Scholar, which many search tools lean on for papers, lags weeks to months with irregular, unpredictable timing. The claim's framing also understates that the authoritative low-latency channels (arXiv API, RSS, listing pages) exist and make web-search lag avoidable.

  STEELMAN:
    Item: ASSUMPTION-1739
    Strongest counterargument: Indexing latency is engine-specific, unpublished, and unstable; scholarly indexes measurably lag by weeks to months and on irregular schedules, while general engines may index in hours but not rank the item for the queries a monitoring agent actually issues. Treating "days" as a known constant lets a 30-day search window look safe when its effective recall for the last 1–4 weeks is unknown and engine-dependent.
    What would need to be true for C2A2 to be safe: The search tool used is backed by a general web index that crawls arXiv daily, and queries target arXiv directly (site:arxiv.org or the arXiv API by author), not general topic queries.
    How to test: For a sample of new arXiv postings by tracked thinkers, record announcement time and the first time the web search tool returns them for an author-name query; compute the distribution.

  Specific risks: Recent postings near the end of the window are systematically missed; the lag is mistaken for absence of work.

  Mitigations available: Query the arXiv API/RSS by author; supplement with Semantic Scholar/OpenAlex APIs; extend the lookback window to overlap prior runs.

  Caveats: No direct measurement of Google general-web latency for arXiv found; the "hours" point is background knowledge. Most found evidence concerns Google Scholar, not general web search.

  Search scope: preliminary search (3 searches, 0 fetches); independent of 15a.

  Recommendation: PARTIALLY-CHALLENGED
