SEARCH-AGAINST-ASSUMPTION-251:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-251
  Original statement: Three un-numbered DECISION candidates (048 3rd cycle, 049 2nd cycle, AI-search-delegation 1st cycle) constitute a tracking blind spot of its own; registry stops being source of truth.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-251
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on numbering-ceremony as friction-gate.
    Current status: PARTIALLY-CHALLENGED (Weak)

  Challenging evidence found: Partial

  Sources:
    1. Nygard (2011) ADR — The original ADR proposal explicitly notes that numbering ceremony can BE the friction-gate; the assumption locates the failure on the registry side, but Nygard locates it on the ceremony side.
    2. Bass et al. (2021) — Documents that "candidate-tracking blind spot" can mean either (a) registry-discipline-failure OR (b) ceremony-too-heavy; the assumption picks (a) without ruling out (b).
    3. Beck (2002) — YAGNI principle suggests un-numbered candidates may legitimately persist without ceremony; the "blind spot" framing presumes ceremony is owed.
    4. Cunningham (1992) — Tech-debt vocabulary applies if numbering is the deferred work; same vocabulary applies if the decision content is the deferred work.
    5. C2A2-internal: PRESUMPTION-271 directly elaborates this challenge.

  Strength of challenge: Weak

  Summary: The challenge is to the locus, not the existence, of the problem. Nygard's ADR literature, Beck's YAGNI, and Cunningham's tech-debt framework all admit either reading. PRESUMPTION-271 internally elaborates: numbering ceremony may itself be the FLAG-I gate. The assumption's framing ("registry stops being source of truth") presumes the registry is owed the numbering; if numbering ceremony IS the gate, the registry's "source of truth" status survives even un-numbered candidates.

  Specific risks: (a) Locating the failure on the registry side prescribes wrong remediation (more registry discipline) instead of right remediation (lower-friction numbering); (b) repeated cycles of "registry hygiene" pushes don't resolve the underlying ceremony-friction; (c) the blind-spot label can compound the bottleneck.

  Mitigations available: (a) Consider PRESUMPTION-271 framing as equally valid; (b) test both remediations (lower friction OR more discipline); (c) measure whether un-numbered candidates have content-debt or only ceremony-debt.

  Recommendation: PARTIALLY-CHALLENGED (Weak)

  STEELMAN:
    Item: ASSUMPTION-251
    Strongest counterargument: Nygard's original ADR proposal locates the failure mode precisely on the ceremony side, not the registry side. The framing "registry stops being source of truth" presumes the registry is owed the numbering — but if the candidates have stable content and only lack ceremony, the registry is actually doing fine and the friction-gate is the problem. The wrong-side-of-the-failure framing prescribes wrong remediation.
    What would need to be true for C2A2 to be safe: Measure whether un-numbered candidates have content-debt or only ceremony-debt; if only ceremony, reduce friction; if content, then the registry-side framing applies.
    How to test: Audit the 3 candidates — do they have stable, decided content that just isn't numbered? Or are they un-decided? Different framings imply different fixes.
