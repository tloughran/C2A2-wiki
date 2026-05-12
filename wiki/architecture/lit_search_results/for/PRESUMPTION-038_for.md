SEARCH-FOR-PRESUMPTION-038:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-038
  Original statement: "The Anthropic billing-propagation bug will clear by Saturday morning without action beyond waiting"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-038
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — recovery-by-waiting strategy for billing-state
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. SaaS billing propagation timescales (Stripe engineering blog; AWS postmortems): typical propagation-lag windows are minutes to hours, but literature does not validate any specific timescale for a given event; "by Saturday" is not a window supportable from any documented distribution.
    2. Distributed systems literature (Abadi PACELC): eventual consistency is time-bounded only probabilistically; waiting-strategy durations are empirically discovered, not predicted.

  Strength of support: None

  Summary: Literature confirms that billing-state propagation is typically short-window (minutes to hours) but does not support a specific confidence that it will clear by a specific future timestamp without escalation. Recovery-by-waiting is a defensible first-line strategy but the time-bound ("by Saturday") is not predicted by any literature. The presumption is an operator prior, not a literature-backed claim.

  Caveats: No direct support for the specific time commitment. Active escalation paths (support ticket with billing-propagation-lag signal) are the literature-supported hedge against long-tail propagation lag.

  Recommendation: NO-SUPPORT-FOUND
