SEARCH-FOR-PRESUMPTION-373:
  Date searched: 2026-06-23
  Original item: PRESUMPTION-373
  Original statement: "[inferred] That the both-paths fix fully and durably resolves the token-read problem — exactly two payload schemas, no future migration silently re-zeroing reads, no recurrence guard installed"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-373
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated durability premise behind ASSUMPTION-335's fix
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (None-Weak)

  Sources:
    1. (None support presuming a migration fix is durable without a guard.) Weakest shelter: if the schema is truly frozen at two payloads, a both-paths read is sufficient — but nothing in the literature licenses presuming the schema will never change again.

  Strength of support: None-Weak

  Summary: No literature supports presuming durability of a schema-read fix absent a recurrence guard; the supportive case requires an assumption (schema frozen forever) that is itself unwarranted. Schema-evolution practice treats further migrations as expected, not exceptional. The supportive direction is effectively empty.

  Caveats: The "exactly two schemas, no future migration" premise is the unsupported part; a both-paths read handles the past, not the next migration.

  Search scope: schema-stability assumptions. Comprehensive for supportive direction.

  Recommendation: NO-SUPPORT-FOUND
