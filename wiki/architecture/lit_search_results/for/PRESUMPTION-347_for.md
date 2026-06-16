SEARCH-FOR-PRESUMPTION-347:
  Date searched: 2026-06-16
  Original item: PRESUMPTION-347
  Original statement: "[inferred] A model identifier pinned in a scheduled-task config stays valid indefinitely (06-14 morning scrape died on unavailable 'claude-fable-5')."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-347
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from the 2026-06-14 scrape failure
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Dependency pinning / reproducible-build practice (software engineering consensus). — Pinning exact versions is widely endorsed for reproducibility and deterministic behavior: an unpinned dependency that floats can break a pipeline silently, so pinning IS best practice. This supports the DECISION to pin (the config did the right thing by naming an exact model), even though it does not support the inferred belief that a pin stays valid forever.
    2. AWS Well-Architected Reliability Pillar, REL05-BP01 "Implement graceful degradation to transform hard dependencies into soft dependencies." — Endorses pinning a known-good dependency while pairing it with a fallback so the hard dependency becomes soft. The supportive reading: pinning is correct AS LONG AS it is paired with degradation — i.e., pinning per se is sound engineering.

  Strength of support: Weak

  Summary: The literature supports pinning as a practice (reproducibility, determinism) but does NOT support the inferred premise that a pinned external, hosted model identifier remains valid indefinitely. The strongest honest FOR reading is narrow: pinning the model was a defensible choice; the failure was not the act of pinning but the absence of a validity/fallback layer around the pin. Support is therefore for "pin" and not for "a pin is permanent" — the premise as literally inferred is essentially unsupported.

  Caveats: Pinning is only safe for dependencies whose artifacts are immutable and durably hosted (e.g., content-addressed packages). A vendor-hosted model alias like "claude-fable-5" is neither immutable in availability nor under the pinner's control; the reproducibility argument for pinning quietly assumes durable availability, which does not hold here. So even the narrow support comes with the exact condition the failure violated.

  Search scope: Dependency-pinning/reproducibility practice; graceful-degradation reliability patterns. Comprehensive; the FOR direction is genuinely thin because the literature treats "pinned == permanently available" as a known fallacy.

  Recommendation: PARTIALLY-SUPPORTED
