SEARCH-FOR-ASSUMPTION-461:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-461
  Original statement: Today's delivery/producer failures were infrastructure-connection errors (evening cowork->chat: ConnectionRefused; c282 wiki: 'Connection closed mid-response') - a third distinct cause in the sync-outage family after login-out and 07-13 quota-exhaustion.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-461
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15a: Searched for supporting literature; result PARTIALLY-SUPPORTED (strength Weak)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Fault-taxonomy literature: distinguishing failure signatures by error string and surviving artifact is standard triage; a third distinct signature (connection errors) after login and quota is a legitimate taxonomy expansion.

  Strength of support: Weak

  Summary: Weakly supported as an empirical classification: connection-refused / connection-closed are a distinct failure class from login-out and quota-exhaustion, so a three-signature taxonomy is defensible. Support is weak because the item is EMPIRICAL (classify each crash tail) and its real force is contesting A-444's single-cause framing, which is carried by P-485.

  Caveats: EMPIRICAL; the classification is the evidence, not the literature.

  Recommendation: PARTIALLY-SUPPORTED
