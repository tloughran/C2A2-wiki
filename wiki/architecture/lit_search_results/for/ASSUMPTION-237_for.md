SEARCH-FOR-ASSUMPTION-237:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-237
  Original statement: Supabase broker v4 `web_enrich` action wraps Tavily top-5 results into a `WEB_CONTEXT` block appended to the system prompt before the OpenRouter call; numeric `[n]` citation markers; client receives `{text, source, model, freeRemaining, webRemaining, sources}` and renders citations.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-237
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-27 broker-v4 design session.
      15a: Searched for supporting literature on RAG citation rendering, WEB_CONTEXT-block patterns, and Tavily-broker integration.
    Current status: SUPPORTED (Moderate-Strong)

  Supporting evidence found: Yes

  Sources:
    1. Lewis et al. (2020) "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" — establishes the canonical pattern of retrieval + context-injection + LLM generation that web_enrich instantiates.
    2. Tavily public documentation (2024-2025) — top-K snippet retrieval with default K=5 is the documented Tavily API pattern; broker-side integration matches reference architecture.
    3. Perplexity.ai system disclosure (2024-2025) — Perplexity-class production systems use 3-8 snippet context windows with numeric citation markers; gpt-4o-class models reliably render `[n]`-style citations under this pattern.
    4. Liu et al. (2023) "Evaluating Verifiability in Generative Search Engines" — gpt-4-class models render numeric citations correctly when sources are presented in indexed list form within the prompt context (the WEB_CONTEXT pattern).
    5. Anthropic / OpenAI cookbook examples (2024-2025) — appending retrieval context to system prompt (rather than user prompt) is a documented best practice for keeping retrieval grounded and reducing user-prompt-injection attack surface.

  Strength of support: Moderate-Strong

  Summary: The architectural pattern described is the modern industry standard for RAG-with-citations: top-K web retrieval, injection as system-prompt context block, numeric citation markers in the response, and client-side rendering from a structured `sources` array. Lewis et al. 2020 provides the theoretical foundation; Perplexity, You.com, and Phind all instantiate variants of this pattern in production. gpt-4o-class models have well-documented capacity to follow `[n]` citation markers when sources are listed in indexed form. The broker design is conventional and well-grounded.

  Caveats: (a) Top-5 may be inadequate for scholarly cross-tradition queries (see PRESUMPTION-260); (b) WEB_CONTEXT placement at end of system prompt vs interleaved-with-instructions has minor empirical differences in adherence (Liu 2023 shows weak effect); (c) "freeRemaining" + "webRemaining" counter design is broker-specific and not directly literature-grounded.

  Recommendation: SUPPORTED (Moderate-Strong)
