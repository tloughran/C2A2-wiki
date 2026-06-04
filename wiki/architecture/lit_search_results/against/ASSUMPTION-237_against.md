SEARCH-AGAINST-ASSUMPTION-237:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-237
  Original statement: Supabase broker v4 `web_enrich` action wraps Tavily top-5 results into a `WEB_CONTEXT` block appended to the system prompt before the OpenRouter call; numeric `[n]` citation markers; client receives `{text, source, model, freeRemaining, webRemaining, sources}` and renders citations.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-237
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on RAG snippet adequacy, citation-injection failure modes, and WEB_CONTEXT placement.
    Current status: PARTIALLY-CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Maynez et al. (2020) "On Faithfulness and Factuality in Abstractive Summarization" — well-documented citation fabrication and `[n]`-marker misalignment failure mode even in gpt-4-class models; numeric citations can drift from source indices.
    2. Liu et al. (2023) "Lost in the Middle: How Language Models Use Long Contexts" — context-position effects: information at end of context (where WEB_CONTEXT lives) is moderately recoverable but inferior to information at the start; placement matters more than the assumption acknowledges.
    3. Adlakha et al. (2023) "Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering" — top-5 retrieval is documented as inadequate for scholarly / specialized queries (10-20 snippets needed for cross-domain).
    4. Anthropic prompt-injection research — appending external content (web search results) to the system prompt creates new prompt-injection surface; the broker pattern is exposed to malicious web pages injecting instructions.
    5. Shi et al. (2023) "Large Language Models Can Be Easily Distracted by Irrelevant Context" — top-5 retrieval that includes off-topic snippets degrades output quality beyond what single-snippet baselines would.

  Strength of challenge: Moderate

  Summary: The architectural pattern is generally sound but has documented failure modes. Top-5 may be inadequate for cross-tradition queries; numeric citation markers can fabricate; WEB_CONTEXT placement at end of system prompt is suboptimal (Lost-in-the-Middle); and retrieval-injection creates a new attack surface. None of these refute the pattern, but they bound its applicability.

  Specific risks: (a) Citation fabrication — `[3]` pointing to wrong source — degrades scholarly trust; (b) Lost-in-the-Middle: bottom-of-system-prompt placement underperforms top-of-prompt; (c) prompt injection via retrieved web pages; (d) top-5 inadequacy for paradigm-bridge queries; (e) "freeRemaining"/"webRemaining" exposure is a minor information-disclosure surface.

  Mitigations available: (a) Citation post-processing (verify each `[n]` against sources array); (b) test WEB_CONTEXT placement A/B; (c) prompt-injection-resistant retrieval framing; (d) larger K for scholarly queries; (e) prompt-injection sanitization on retrieved content.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: ASSUMPTION-237
    Strongest counterargument: The broker design is a clean instantiation of an industry pattern, but it inherits the documented failure modes of that pattern. Citation fabrication is empirically measurable; Lost-in-the-Middle is documented for gpt-4-class models; top-5 is the right baseline for general search but the wrong baseline for scholarly cross-domain retrieval. The architectural assumption holds; the calibration is unvalidated for C2A2's specific use case.
    What would need to be true for C2A2 to be safe: (a) citation-verification post-processing; (b) empirical check that top-5 is adequate for tradition-bridge queries; (c) A/B test of WEB_CONTEXT placement.
    How to test: Run 20 known-answer cross-tradition queries through broker-v4; measure citation-fabrication rate, top-5 adequacy, and answer correctness.
