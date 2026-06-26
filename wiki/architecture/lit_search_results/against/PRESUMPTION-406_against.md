SEARCH-AGAINST-PRESUMPTION-406:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-406
  Original statement: "That the 06-23 approval/proposal mismatch is a reconcilable tooling defect - presumes a recoverable ground truth despite position-based decision IDs"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-406
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: mismatch presumed reconcilable / ground truth presumed recoverable despite positional IDs
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Stable-vs-positional identifier literature (database keys; URI/permalink design). - Positional/ordinal identifiers are a known anti-pattern: when order changes (insert/delete/reorder), every positional reference silently re-points; the original linkage is not recoverable from position alone.
    2. Audit-log integrity literature (append-only + stable keys + idempotency). - Trustworthy decision provenance requires immutable, stable identifiers and append-only records; without them, corrupted linkages cannot be reconstructed.
    3. Referential-integrity / dangling-reference theory. - Identity by position rather than by stable key produces exactly the silent mis-linkage observed in the approval/proposal mismatch.

  Strength of challenge: Strong

  Summary: The presumption assumes a recoverable ground truth, but if approvals were linked to proposals by position (ordinal index) and the underlying ordering shifted, the literature says the mapping is not reliably recoverable from the corrupted artifact itself - positional IDs carry no stable anchor to reconstruct intent. Calling it a "reconcilable tooling defect" may be optimistic: it could be an irrecoverable provenance hole, and five governance approvals may not be confidently re-attributable. At minimum, recoverability is contingent on an independent stable-keyed/append-only record existing - which is the open question, not a given.

  Specific risks: Five governance approvals mis- or un-attributable; silent decision-provenance corruption presented as a fixable bug; loss of auditability/trust in the governance record.

  Mitigations available: Replace positional decision IDs with stable immutable IDs + append-only log + idempotency keys (correct-by-construction going forward); for the existing mismatch, attempt recovery ONLY via any independent stable record, and if none exists, record the approvals as unverifiable rather than guessing.

  STEELMAN:
    Item: PRESUMPTION-406
    Strongest counterargument: Positional identity has no recovery anchor: once order drifts, the artifact cannot tell you what it originally pointed to, so "reconcilable" presumes a ground truth the data structure was never capable of preserving - the honest possibility is irrecoverable corruption of five approvals.
    What would need to be true for C2A2 to be safe: An independent stable-keyed/append-only record of each approval exists and can be replayed to reconstruct the linkage.
    How to test: Check for any immutable secondary log keyed by stable ID; if absent, recoverability cannot be assumed and should be reported as such.

  Search scope: Stable vs positional IDs; audit integrity; referential integrity. Comprehensive.

  Recommendation: CHALLENGED
