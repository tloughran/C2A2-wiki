SEARCH-AGAINST-ASSUMPTION-033:
  Date searched: 2026-04-17
  Original item: ASSUMPTION-033
  Original statement: "Phrase-triggered plugin activation (not SessionStart hook) is the correct architectural choice for session-resume functionality"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-033
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — stated architectural choice
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Ammari et al. (2019) "Music, Search, and IoT: How People (Really) Use Voice Assistants" — trigger-miss rates in the 10-30% range for un-corpus-grounded intent taxonomies; user phrasing reliably diverges from designer expectation.
    2. Voice UX literature (Clark et al. 2019 "What makes a good conversation?"): phrase-triggered systems impose a recall burden on the user — users must remember the specific trigger, which many won't.
    3. Conversational AI adoption studies (Luger & Sellen 2016 "Like Having a Really Bad PA"): opt-in trigger systems have documented "trigger-guessing fatigue" — users give up rather than learn the taxonomy.
    4. Hook-vs-trigger design pattern discussions (VS Code plugin architecture docs; JetBrains SDK): SessionStart hook is explicitly designed for persistent-orientation tasks where ambient availability is preferred; phrase triggers are for optional/lightweight activation.

  Strength of challenge: Moderate

  Summary: The challenge is not to phrase-triggered activation per se but to its appropriateness for session-resume specifically. If session-resume is a common-enough intent to warrant ambient availability, hook-based activation avoids the trigger-miss / trigger-guess burden entirely. The literature suggests phrase triggering is the correct choice for bursty optional commands, not for "I want to pick up where I left off" which is a frequent, high-value, naturally-expressed intent.

  Specific risks: Silent trigger miss when Tom uses an out-of-taxonomy phrase; user learned-helplessness if the plugin often misses ("I'll just start fresh"); under-utilization of the resume capability; hidden miss rate invisible to the plugin (cannot count what wasn't triggered).

  Mitigations available:
    - Corpus-based taxonomy expansion (track actual missed utterances)
    - Hybrid approach: phrase-triggered + SessionStart hook as belt-and-suspenders
    - Observable miss indicator (plugin logs non-match sessions where resume intent was plausible)
    - Post-deployment trigger-coverage audit

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-033
    Strongest counterargument: For a high-value, frequent intent like "resume prior session," requiring the user to recall a specific trigger phrase imposes a recall tax that conversational-AI literature consistently shows fails. Hook-based activation for a persistent orientation capability is the literature-supported pattern; phrase triggers are for optional, rare, or context-specific commands. The choice as stated privileges architectural purity over user recall ergonomics.
    What would need to be true for C2A2 to be safe: Tom actually remembers and uses the trigger phrases reliably; miss rate (known via future audit) below acceptable threshold.
    How to test: 2026-04-18 stress test; log match/miss counts; compare Tom's actual resumption phrasings to the taxonomy.

---

SEARCH-AGAINST-ASSUMPTION-033 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: ASSUMPTION-033
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b] (cycle 1)
    Original item: ASSUMPTION-033
    Item type: ASSUMPTION
    Transform at each step:
      14a (cycle 0): Originally extracted/inferred
      15b (cycle 0): Searched for challenging literature → see prior result block above
      15c (cycle 0): Initial disposition issued
      15d: Re-triggered on weekly cadence (2026-04-26 trigger; processed 2026-04-27)
      15b (cycle 1): Re-searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (refreshed; no new challenging literature surfaced this cycle)

  New evidence weighed: No new challenging literature has surfaced in the week since the last cycle. The prior result stands as the operative finding. The system's challenge profile for this item is unchanged.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted in the past week; no new disconfirmatory sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: PARTIALLY-CHALLENGED (refreshed; carry forward prior recommendation)
