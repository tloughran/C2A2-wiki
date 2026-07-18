SEARCH-AGAINST-ASSUMPTION-426:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-426
  Original statement: "A tradition agent can reliably reject hallucinated web-search results by cross-checking against its own knowledge of a thinker's appearance catalog."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-426
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extraction (stated assumption, MEDIUM, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Can LLMs Detect Their Own Hallucinations?" 2025. arXiv:2511.11087. — Empirical study finding GPT-3.5-Turbo with chain-of-thought detected only 58.2% of its own hallucinations; self-checks also produced more false-positive "hallucination-free" judgments than false negatives, i.e. the checker errs toward accepting bad content.
    2. "Large Language Models Hallucination: A Comprehensive Survey." 2025. arXiv:2510.06265. — Survey documenting that self-consistency/self-verification methods fail precisely when the model is confidently wrong; overconfident parametric beliefs defeat internal cross-checking.
    3. "When LLMs Lag Behind: Knowledge Conflicts from Evolving APIs in Code Generation." 2026. arXiv:2604.09515. — Shows models confidently treat stale parametric knowledge as ground truth against genuinely new external facts; directly relevant to the false-rejection failure mode (a real post-cutoff appearance rejected because it is absent from the agent's catalog).

  Strength of challenge: Strong

  Summary: The literature challenges both directions of this claim. Direction 1 (missed hallucinations): LLM self-verification detects barely more than half of the model's own hallucinations in controlled tests, and fails systematically when the model is confidently wrong — so cross-checking against "its own knowledge" is an unreliable filter for fabricated search results. Direction 2 (false rejections): the agent's appearance catalog is itself parametric/curated knowledge with a cutoff; knowledge-conflict studies show models default to treating stale internal knowledge as authoritative, so genuinely new appearances that are not yet in the catalog will be wrongly rejected. The mechanism is not "reliable" in either the precision or recall sense; it is a weak prior-based heuristic.

  Specific risks: For C2A2, tradition agents may (a) admit fabricated events into the wiki when a hallucinated result happens to be plausible relative to the catalog, and (b) systematically reject real new appearances — the exact events the pipeline exists to capture — because catalog incompleteness is indistinguishable from result fabrication under this test. Silent recall loss on new events is the more insidious failure since nothing surfaces it.

  Mitigations available: Require independent external corroboration (second source, primary-source URL fetch and content check) rather than internal-knowledge cross-check; treat "not in catalog" as UNVERIFIED-NEW rather than REJECT; log all rejections for periodic human audit; use retrieval-grounded verification (fetch the cited page and confirm the claim appears there) which the hallucination-detection literature finds far stronger than self-verification.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: The claim is not that self-verification is perfect but that it is a useful first-pass filter in a narrow, well-known domain. A tradition agent's catalog of one thinker's appearances is a small, dense knowledge set where the agent's priors are strong and mostly correct; hallucinated search results in this domain tend to be flagrantly inconsistent (wrong venue types, impossible dates, misattributed co-panelists) and are caught by even a 60%-sensitive filter, while downstream steps (URL fetch, human review) catch the rest. Reliability of the layered system, not the single check, is what matters.
    What would need to be true for C2A2 to be safe: The catalog check must be one layer in a stack that includes source-fetch verification and human review; rejections must be logged and auditable, not silent; the agent must distinguish "contradicts catalog" from "absent from catalog."
    How to test: Seed a batch of known-real post-cutoff appearances plus synthetic fabricated ones into the search-result stream and measure the agent's precision/recall on accept/reject decisions; check the rejection log for false rejections of the real items.
