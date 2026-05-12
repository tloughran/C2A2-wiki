SEARCH-FOR-PRESUMPTION-055:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-055
  Original statement: "Binary static/dynamic partition is the correct primitive for the caching layer (multi-tier alternatives not considered)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-055
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from exclusive two-tier framing in caching-architecture deliverables
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Anthropic prompt-caching documentation (2024-2025): the platform itself exposes a binary "cached prefix + uncached suffix" primitive. Binary partition is the native model — multi-tier is simulated by layering cache-breakpoints, not fundamentally different.
    2. Chawla, Avi (2024). "Prompt Caching" (task-brief source): presents a two-tier design as the canonical illustration.
    3. Simplicity principle / Occam-razor application in systems design (Fowler 2018; "Release It!" Nygard 2007): two-tier designs are easier to reason about, monitor, and diagnose than N-tier; starting binary and extending if evidence demands is a standard approach.
    4. Anthropic multi-breakpoint caching (2024-2025 API updates): the platform permits up to 4 cache breakpoints, meaning up to 4 tiers — BUT the default and recommended pattern remains binary for simple workloads.

  Strength of support: Moderate

  Summary: Binary partition is the native primitive exposed by Anthropic's prompt-caching platform and is the canonical illustration in introductory references. It is supported as a simple, well-understood starting point. However, the platform itself supports up to 4 breakpoints — so "binary is optimal" is not literature-established; "binary is a reasonable default" is.

  Caveats: (a) Anthropic permits up to 4 cache breakpoints; a multi-tier design may extract more value if freshness-gradients exist in the content; (b) "correct primitive" is stronger than the literature supports — the literature supports "common starting primitive"; (c) the PRESUMPTION is about whether multi-tier was CONSIDERED and REJECTED vs. defaulted to; literature can support the binary CHOICE but cannot support the MISSING DELIBERATION.

  Recommendation: PARTIALLY-SUPPORTED (binary partition is a reasonable default; the presumption's strength is weaker than stated because the literature also supports multi-tier designs for specific workloads, and the deliberation that should have evaluated the alternatives appears to be absent from the design record)
