SEARCH-AGAINST-ASSUMPTION-140:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-140
  Original statement: "Morning chat-scrape succeeded second consecutive day; sign-in fix from 2026-05-13 is holding (two data points)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-140
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-14 operational summary
      15b: Searched for counter-evidence on credential-layer-vs-architectural-layer distinctions
    Current status: CHALLENGED (Moderate)

  Sources:
    1. Reason (1990) "Human Error" — credential-level "fixes" that restore service without addressing systemic failure mode reliably recur. The drought-recovery-recurrence pattern is canonical.
    2. Allspaw (2009) "10+ Deploys Per Day" — post-incident recovery: surface-level fixes have ~70% recurrence within the same failure-cycle.
    3. SRE practice — "MTBF" must be measured over multiple incident cycles; one-cycle recovery is below the canonical bar.
    4. PRESUMPTION-159 carry-forward (REVISE 2026-05-14) — credential-layer-as-architectural-fix anti-pattern remains unresolved; ASSUMPTION-140 implicitly relies on the framing that PRESUMPTION-159 disputes.
    5. PRESUMPTION-177 paired — Chrome-MCP-offline failure today recurs after only one successful day; degraded-mode protocol treats it as credential issue rather than recurring architectural failure mode.
    6. Same-day data: ASSUMPTION-141 records evening cowork-to-chat FAILED — the credential-layer is not fully restored at the system level.

  Strength of challenge: Moderate

  Summary: The narrow claim (morning chat-scrape succeeded two consecutive days) is factually correct but the inference ("sign-in fix is holding") is contradicted by same-day data: PRESUMPTION-177 records Chrome-MCP failure recurring after one good day; ASSUMPTION-141 records evening cowork-to-chat failure. The "holding" inference treats two morning-chat-scrape successes as evidence for a broader credential-layer stability claim that other same-day data points refute. PRESUMPTION-159 (REVISE) is the architectural counterpart: credential-layer-as-architectural-fix is a documented anti-pattern. Moderate challenge: the data points exist; the inference over-extends from one successful sub-system to a credential-layer claim.

  Specific risks: (a) "Holding" inference over-extends from chat-scrape to credential-layer broadly; (b) Same-day failures (PRESUMPTION-177, ASSUMPTION-141) contradict the broader stability claim; (c) Credential-layer-as-architectural-fix anti-pattern (PRESUMPTION-159 REVISE) carry-forward; (d) N=2 below stability-claim threshold even for the narrow chat-scrape sub-system.

  Mitigations available: (a) Restrict the claim to the chat-scrape sub-system, not credential-layer broadly; (b) Resolve PRESUMPTION-159 substrate-decomposition gate before claiming credential-layer stability; (c) Track failure recurrence by sub-system explicitly; (d) Demote "holding" to "two successes recorded; insufficient sample for stability claim."

  Recommendation: CHALLENGED (Moderate) — narrow claim ok; "holding" inference over-extends; load-bearing concern is the credential-layer vs sub-system scope

  STEELMAN:
    Item: ASSUMPTION-140
    Strongest counterargument: The factual claim ("two consecutive successful chat-scrapes") is correct, but the inferential claim ("sign-in fix is holding") makes a broader credential-layer stability claim that same-day data refutes. PRESUMPTION-177 records Chrome-MCP failure today; ASSUMPTION-141 records evening cowork-to-chat failure today. The credential-layer is not "holding" — one sub-system within it is. The honest framing would be "morning chat-scrape sub-system: 2/2 successes; other credential-layer sub-systems: failures observed today." The over-extension is the failure mode.
    What would need to be true for C2A2 to be safe: (a) Restrict claim to chat-scrape sub-system; (b) PRESUMPTION-159 substrate-decomposition audit resolved before credential-layer stability claims; (c) Per-sub-system failure tracking; (d) N ≥ 7 before "holding" inference.
    How to test: Track all credential-layer-dependent sub-systems (chat-scrape, Chrome-MCP, cowork-to-chat, sign-in) over the next 7 days; check whether all are stable, not just chat-scrape.
