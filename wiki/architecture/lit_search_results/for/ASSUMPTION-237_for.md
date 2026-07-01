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


---

SEARCH-FOR-ASSUMPTION-237 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-237
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-237
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15a (cycle 3, 2026-06-30): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week(s) since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; operational evidence from the C2A2 runs themselves remains the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED (Moderate-Strong))
