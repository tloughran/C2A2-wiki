SEARCH-FOR-ASSUMPTION-1739:
  Date searched: 2026-10-03
  Original item: ASSUMPTION-1739
  Original statement: General web search indexes new arXiv postings with a lag of days.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1739
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 9815cc97.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. arXiv, "Availability of submissions". https://info.arxiv.org/help/availability.html [search-result] — Papers are announced Sunday to Thursday, with no announcements on Friday or Saturday, on a fixed cutoff schedule (e.g. submissions received Mon 14:00 to Tue 14:00 are announced Tue 20:00). This creates a built-in lag of up to about 3 days between submission and public visibility, before any search engine crawls the paper.
    2. arXiv, "Subscribe to email listings" (https://info.arxiv.org/help/subscribe.html) and the arXiv blog on the rewritten RSS feed (https://blog.arxiv.org/2024/01) [search-result] — Daily per-category email listings, RSS feeds, and the public Atom API give direct access to new announcements. This supports the item's proposed alternative lane: these channels avoid search-engine latency.
    3. Google Scholar Blog (2010, via search snippet). https://scholar.googleblog.com/2010/06/ [search-result] — Snippet says Scholar "adds new articles twice a week". If accurate, this implies a lag of days for Scholar. Not verified by fetch; may be outdated.
    4. Moed, Bar-Ilan & Halevi, 2016. "A new methodology for comparing Google Scholar and Scopus." Journal of Informetrics (arXiv:1512.05741) [search-result; author names are background-knowledge, not verified on page] — Reports Google Scholar indexes faster than Scopus (median difference about 2 months for Scopus-covered journals). This supports "fast" relative to bibliographic databases, but does not measure days for arXiv specifically.
    5. Martín-Martín et al., 2018. "Google Scholar as a data source for research assessment" (arXiv:1806.04435) [search-result; authorship is background-knowledge] — A review that discusses Scholar's indexing speed. It was not fetched, and no specific figure for arXiv lag was retrieved.
    6. conductscience.com / cgnetworks.org indexing FAQs [search-result] — General statements that Google web search can index new content "within days or weeks" and that Scholar is more cautious. These are low-quality, non-empirical sources.

  Strength of support: Weak

  Summary: The claim is plausible and consistent with several sources. arXiv's own announcement cycle adds 0–3 days. Scholar reportedly updates about twice weekly, and Scholar is documented as faster than Scopus. No source found measures the latency from an arXiv announcement to its appearance in general web search (Google/Bing) or in an LLM search tool. "A lag of days" is therefore a reasonable order-of-magnitude statement without a direct empirical anchor. There is clear support that arXiv's API, RSS feeds and listings are the authoritative low-latency channel.

  Caveats: (a) Latency for the general web index probably varies by page type (abs page vs PDF), by crawl priority, and by search provider. The search tool C2A2 uses may sit on a different index. (b) The Scholar "twice a week" figure comes from a snippet and may be outdated. (c) Comparisons between Scholar and Scopus concern journal articles, not preprints. (d) The lag could also be shorter than days (arXiv abs pages are heavily crawled) or longer (for discovery by query rather than by URL). The assumption gives no bound.

  Search scope: preliminary search (2 searches, 0 fetches); web-only. No empirical crawl-latency studies found. Broader search recommended (webometrics, IR freshness literature).

  Recommendation: PARTIALLY-SUPPORTED
