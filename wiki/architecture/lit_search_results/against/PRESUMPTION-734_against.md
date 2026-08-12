SEARCH-AGAINST-PRESUMPTION-734:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-734
  Original statement: That the strict/loose pair is a safeguard rather than an alarm nobody reads; it now reports monotone register decay — eleven REVISE ids over two days with zero new strict blocks, DISPOSITION shortfall 32 -> 46, premises max-minus-blocks 43 -> 44, presumptions loose exceeding max by 2 — measured only by 14a, reported by no run, repaired by nothing. NOTE: extends PRESUMPTION-687.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-734
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read six days of 14a's own strict/loose measurements as a trend rather than as a nightly figure
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. VaultSpeed, "Why Data Completeness Fails without Referential Integrity" and Acceldata, "Understanding Referential Integrity" — establish that orphaned/pseudo-orphan records (values that don't join back to a valid parent) are a known, well-studied failure class in append-only and dimensional systems, supporting the presumption's underlying concern that an unresolved register drift is a real risk category, not a novel one. [unverified — from search snippet]
    2. Designgurus.io, "How do you enforce immutability and append-only audit trails?" and hash-chain literature on append-only ledgers — standard practice for append-only logs is to pair immutability with active verification (hash chains, periodic reconciliation jobs), not with immutability alone; the mere existence of a measurement (14a's nightly strict/loose count) without an automated reconciliation/alerting step is a documented anti-pattern in audit-log design, matching the presumption's "measured... reported by no run, repaired by nothing" diagnosis. [unverified — from search snippet]
    3. General internal-audit literature (Wolters Kluwer, "Internal audit performance measures"; on Goodhart's Law dynamics) — a countervailing point: internal audit practice explicitly tolerates unreconciled internal indicators as normal working state between formal audit cycles; a metric being "measured but not yet acted on" for six days is not inherently pathological in continuous-monitoring frameworks, which distinguish "detection latency" from "detection absence." This weakens the presumption's framing of any lag as decay rather than a normal monitoring cadence. [unverified — from search snippet]

  Strength of challenge: Weak

  Summary: The core mechanism the presumption worries about — a measured signal that nobody consumes, resembling an orphaned/pseudo-orphan pattern in append-only systems — is well documented as a genuine design risk in data-integrity and audit-log literature, and the "measurement without reconciliation" pattern matches known anti-patterns in append-only ledger design. However, continuous-monitoring and internal-audit literature also normalizes a gap between "measured" and "acted upon" as long as detection latency stays bounded, meaning two days of unactioned figures does not, by itself, establish "decay" rather than ordinary lag; the presumption would need a longer window or an explicit staleness threshold to be more than an early warning.

  Specific risks: If the strict/loose divergence continues unaddressed past a bounded detection-latency window, register-level orphaned/inconsistent entries can accumulate silently (the acknowledged data-integrity risk), degrading trust in downstream disposition counts and making eventual reconciliation more expensive the longer it is deferred.

  Mitigations available: Standard mitigation from audit-log/data-integrity practice: define an explicit staleness/latency SLA for the strict/loose metric (e.g., must be actioned within N days), implement automated reconciliation or dead-letter handling for orphaned register entries, and route the nightly 14a measurement to an owner rather than leaving it as a passive figure.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-734
  Strongest counterargument: Two days of an unactioned metric is not evidence of systemic neglect — audit and monitoring literature explicitly distinguishes bounded detection latency (normal) from detection absence (pathological), and a single-run snapshot cannot distinguish "this metric will be actioned on day 3" from "this metric is permanently unread." Treating any gap between measurement and action as "decay" risks manufacturing urgency from an artifact of the reporting cadence itself.
  What would need to be true for C2A2 to be safe: There would need to be an explicit staleness threshold (e.g., "strict/loose divergence unaddressed for >N cycles = alarm") that the six-day pattern is shown to violate, plus evidence that no owning process exists at all (not just that none acted within the observed window).
  How to test: Extend the observation window past the point where a reasonable SLA would require action, and check whether any run ever consumes the 14a strict/loose figures; absence over a longer, defined window is stronger evidence than absence over two days.

Search scope: Preliminary search — broader search recommended (general data-integrity/audit-log literature only; no direct precedent found for multi-agent register-decay specifically).
