SEARCH-FOR-ASSUMPTION-038:
  Date searched: 2026-04-17
  Original item: ASSUMPTION-038
  Original statement: "Pattern-based session-name filter (C2a2, morning-health, wiki-agent-daily, heartbeats, dated prefixes) reliably identifies automated sessions"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-038
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — stated classifier design for session-exclusion
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Rule-based classifier literature (Jurafsky & Martin 2023, "Speech and Language Processing"): high-precision prefix/substring rules perform well when the underlying naming convention is tightly controlled and the taxonomy is stable.
    2. Log-analysis / observability practice (Brazma et al. on log parsing conventions; Splunk / Elastic documentation): pattern-matched session filters are the industry-standard first-line classifier for automated vs. interactive traffic.
    3. NER-by-rule literature (Chiticariu et al. 2013 "Rule-Based Information Extraction is Dead! Long Live Rule-Based Information Extraction Systems!"): rule-based classifiers remain competitive for narrow, well-bounded tasks with controlled vocabularies.

  Strength of support: Moderate

  Summary: Rule-based prefix/substring classifiers are well-supported as a first-line tool when the naming convention is under the operator's control and the taxonomy is reasonably stable. For a setup where the operator controls the session-naming scheme for automated sessions, this is a reasonable and supportable design. The evidence base is industry practice and documented rule-based IE efficacy for controlled vocabularies.

  Caveats: Support depends on the naming convention being actually enforced (drift in naming conventions routinely degrades rule-based classifiers). No literature addresses the specific filter combination used, and false-positive / false-negative rates can only be established empirically via audit (tracked as OPEN-025).

  Recommendation: PARTIALLY-SUPPORTED

---

SEARCH-FOR-ASSUMPTION-038 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: ASSUMPTION-038
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a → 15c → 15d → 15a] (cycle 1)
    Original item: ASSUMPTION-038
    Item type: ASSUMPTION
    Transform at each step:
      14a (cycle 0): Originally extracted/inferred
      15a (cycle 0): Searched for supporting literature → see prior result block above
      15c (cycle 0): Initial disposition issued
      15d: Re-triggered on weekly cadence (2026-04-26 trigger; processed 2026-04-27)
      15a (cycle 1): Re-searched for supporting literature
    Current status: PARTIALLY-SUPPORTED (refreshed; no new supporting literature surfaced this cycle)

  New evidence weighed: No new supporting literature has surfaced in the week since the last cycle. The prior result stands as the operative finding. Item remains in its existing disposition state until either new operational evidence (from C2A2's own runs) or new external literature alters the picture.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted in the past week; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven literature scan or operational evidence from the C2A2 runs themselves would be the more sensitive signal for status change.

  Recommendation: PARTIALLY-SUPPORTED (refreshed; carry forward prior recommendation)
