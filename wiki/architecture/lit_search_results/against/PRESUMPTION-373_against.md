SEARCH-AGAINST-PRESUMPTION-373:
  Date searched: 2026-06-23
  Original item: PRESUMPTION-373
  Original statement: "[inferred] That the both-paths fix fully and durably resolves the token-read problem — exactly two payload schemas, no future migration silently re-zeroing reads, no recurrence guard installed"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-373
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated durability premise behind ASSUMPTION-335's fix
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Conduktor / Branch Boston schema-evolution best practices. — Schemas evolve repeatedly; durability comes from contract tests and compatibility policies, not from a one-time both-paths read.
    2. Migration-testing literature (Functionize; thedataops). — Recurrence guards = canary assertions + regression tests on derived metrics; without them, the next migration can silently re-zero reads.
    3. C2A2-internal: same silent-read failure class as PRESUMPTION-369/REVISE-129 and over-trust family (PREMISE-049, MONITOR-296).

  Strength of challenge: Strong

  Summary: The durability presumption is strongly challenged: schema-evolution practice expects further migrations and secures reads with contract tests and canary assertions, not a static both-paths patch. Without a recurrence guard, the next field relocation re-instantiates the exact silent-zeroing failure (the 369 class). This is the same fail-loud gap the system already flagged.

  Specific risks: A future migration silently re-zeros token (or other) reads with no alarm — the original failure recurs, undetected, defeating the 335 correction.

  Mitigations available: Install a canary assertion / schema-contract test on token reads that fails loudly on a zeroed or missing path; add a derived-metric regression test across migrations; assert non-null/continuity on each run.

  STEELMAN:
    Strongest counterargument: If the payload schema is genuinely stable (no further migrations planned), a both-paths read is a complete and durable fix, and adding guard infrastructure is YAGNI overhead.
    What would need to be true for C2A2 to be safe: "No further migrations" must be guaranteed, not presumed; for an actively-developed system that guarantee is false, so the guard is warranted.
    How to test: Introduce a deliberate test migration in staging; if token reads zero with no alarm, the fix is not durable and a guard is required.

  Search scope: schema-evolution durability; canary/contract testing; silent-read family. Comprehensive.

  Recommendation: CHALLENGED
