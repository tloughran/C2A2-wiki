SEARCH-AGAINST-ASSUMPTION-038:
  Date searched: 2026-04-17
  Original item: ASSUMPTION-038
  Original statement: "Pattern-based session-name filter (C2a2, morning-health, wiki-agent-daily, heartbeats, dated prefixes) reliably identifies automated sessions"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-038
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — stated pattern-match classifier
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Rule-based classifier failure-mode literature (Chiticariu et al. 2013; Cunningham 2006): rule-based classifiers degrade as naming conventions drift; they are brittle to naming variants not anticipated by the rule-author.
    2. Security / detection literature (Hofmeyr & Forrest 2000 on intrusion detection): pattern-match rules show both false positives (legitimate sessions matching automated-pattern) and false negatives (automated sessions not matching any rule) — rates typically 5-15% for narrow controlled vocabularies, higher for uncontrolled ones.
    3. NER-rule decay literature: rule-based NER systems require ongoing maintenance as the naming corpus evolves.
    4. "Self-describing names" literature (naming-convention audits): naming discipline degrades over time; rule-sets that assume perfect naming quickly become inaccurate.

  Strength of challenge: Moderate

  Summary: The literature warns that pattern-based classifiers are brittle to naming-convention drift and have known miss rates. The specific filter combines several well-formed patterns, but new session types (future automated agents; ad-hoc scheduled tasks; dated prefixes that don't follow the expected pattern) will either false-positive or false-negative at rates the literature describes as non-trivial. The classifier is a reasonable first pass but should not be treated as reliable without empirical audit.

  Specific risks: Automated sessions that don't match the filter are treated as interactive and included in analysis (skew); interactive sessions whose names happen to match (Tom typing "C2a2" in an interactive session title) are excluded and lost; maintenance burden rises as new session types are added without the filter being updated.

  Mitigations available:
    - Audit of the most recent N sessions with manual classification (OPEN-025 scope)
    - Secondary signal beyond name (e.g., session metadata: scheduled-task origin, initiator identity)
    - Periodic rule-set review; alert when session-type diversity outstrips the rule set

  Recommendation: CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-038
    Strongest counterargument: Pattern-based classifiers on uncontrolled or semi-controlled naming are known to decay; relying on names alone rather than metadata is a weaker classifier than one that uses the structural property (was this session scheduled vs. user-initiated?). The filter is brittle and unaudited; "reliably" is a claim that requires empirical measurement.
    What would need to be true for C2A2 to be safe: Audit produces miss-rate below acceptable threshold; filter updated when new session types are introduced; metadata-based fallback for ambiguous names.
    How to test: Manual classification audit of recent sessions; compare against filter output; compute precision/recall.

---

SEARCH-AGAINST-ASSUMPTION-038 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: ASSUMPTION-038
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b] (cycle 1)
    Original item: ASSUMPTION-038
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
