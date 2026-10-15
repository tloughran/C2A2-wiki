SEARCH-AGAINST-PRESUMPTION-1146:
  Date searched: 2026-10-15
  Original item: PRESUMPTION-1146
  Original statement: "Web search can serve as the sampling frame for an author's recent output. Literature question: what do index-coverage and bias studies (deep/invisible web; Lewandowski) imply for that use?"
  Independence: run by a separate subagent that did not read 15a output. (Shared web-fetch cache not used by either: no fetches.)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1146
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-14 transcripts.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Search scope: PRELIMINARY — broader search recommended. Titles/URLs only; no full text read; UNVERIFIED items from background knowledge.

  Sources:
    1. Lewandowski, 2008. Freshness study (as above). — Engines vary in index freshness; many pages stale. Title only.
    2. Bar-Yossef & Gurevich, 2006/2008. — Sampling from an engine's index is biased and hard to correct; an engine is not a neutral frame. Title only.
    3. Bharat & Broder, 1998. "A technique for measuring the relative size and overlap of public Web search engines." WWW7. — UNVERIFIED (background). Each engine covers part of the web; overlap small.
    4. Lawrence & Giles, 1999. "Accessibility of information on the web." Nature. — UNVERIFIED (background). Coverage incomplete and biased to popular, well-linked pages.
    5. Lewandowski, 2015 JASIST retrieval-effectiveness paper — UNVERIFIED; the DOI that surfaced may be a different paper. Not relied on.

  Strength of challenge: Strong (title-level evidence; unread)

  Summary: A search engine is a non-random, incomplete, time-lagged subset of the web. Recent items are the weakest part of the frame (indexing lag); paywalled, dynamic and login-gated content is excluded; popularity biases surfacing. Ranking, personalisation and result caps make queries a non-probability sample that varies by engine, time and place. This undermines both completeness and representativeness for an author's recent output.

  Specific risks: Recent publications under-represented; popular outputs over-represented; paywalled/PDF/social/non-English venues missed; name ambiguity adds noise; irreproducible across engine/date/locale; the error is a silent undercount with no signal that anything is missing.

  Mitigations available: Triangulate engines; use authoritative registries as the frame (ORCID, Crossref, OpenAlex, DBLP, publisher/institutional pages, the author's CV) with search as supplement; log queries and dates; estimate recall by capture-recapture or against a ground-truth subset; label the sample non-exhaustive.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1146
  Strongest counterargument / conditions for safety / test: For a prolific, well-linked author with a stable web presence the index may cover nearly all recent output, and the goal may be a convenience sample. Safe if the claim is limited to 'output discoverable via search', the items are indexed within the recency window, and a recall check comes out high. Test: take a ground-truth list (CV/ORCID) and measure the fraction search finds by item age and venue type.
