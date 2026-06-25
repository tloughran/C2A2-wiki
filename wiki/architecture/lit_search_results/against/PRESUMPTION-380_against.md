SEARCH-AGAINST-PRESUMPTION-380:
  Date searched: 2026-06-24
  Original item: PRESUMPTION-380
  Original statement: "That a 14-thinker keyword/relevance score (>0.4) is the right instrument for cross-tradition relevance, merely mis-tuned (page-as-unit / keyword-match unexamined)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-380
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the instrument's class is taken as given; only its threshold is questioned
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Keyword vs embedding for relevance (arXiv 2403.18855: TF-IDF baseline MAP 10.5%/MAR 34.6% vs embeddings 25.4%/65.3%). - Keyword matching substantially underperforms embeddings for relevance and link prediction, especially where conceptual (not lexical) overlap is required.
    2. Cross-domain bridging needs semantics (KG embeddings survey, MDPI 13(3):485). - Cross-tradition relevance is conceptual; lexical keyword overlap misses analogical/structural correspondence - the construct-validity error of measuring concept-relatedness with word-match.
    3. Page-as-unit. - Scoring whole pages collapses heterogeneous content; passage/claim-level units are standard for relevance.

  Strength of challenge: Moderate-Strong

  Summary: Moderate-strong challenge. The presumption holds the instrument's CLASS fixed (keyword match over whole pages) and questions only its threshold (>0.4). But the evidence is that keyword/TF-IDF is the weak baseline precisely for the cross-domain, conceptual relevance the project needs, with embeddings roughly doubling MAP and MAR. Cross-tradition bridges are analogical/structural, where lexical overlap is least informative. And page-as-unit scoring blurs the signal further. So the instrument is plausibly the wrong class, not merely mis-tuned - re-tuning a keyword threshold cannot recover conceptual matches it never represents.

  Specific risks: Cross-tradition seeding driven by a keyword score will surface lexical coincidences and miss genuine conceptual bridges - low precision AND low recall on exactly the links that matter.

  Mitigations available: Use embedding/semantic relevance (or multi-channel keyword+embedding) at passage/claim granularity; validate precision/recall against a labelled cross-tradition set before seeding.

  STEELMAN:
    Strongest counterargument: If the keyword score is only a cheap pre-filter feeding a semantic re-ranker, then it is a legitimate first stage and 'merely mis-tuned' is fair for that stage.
    What would need to be true for C2A2 to be safe: A semantic/embedding stage must do the actual cross-tradition relevance judgment.
    How to test: Compare keyword-only vs embedding vs hybrid against human cross-tradition relevance labels; measure precision/recall.

  Search scope: keyword vs embedding; cross-domain relevance; unit granularity. Comprehensive.

  Recommendation: CHALLENGED
