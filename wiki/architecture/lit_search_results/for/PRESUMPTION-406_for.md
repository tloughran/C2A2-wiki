SEARCH-FOR-PRESUMPTION-406:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-406
  Original statement: "That the 06-23 approval/proposal mismatch is a reconcilable tooling defect - presumes a recoverable ground truth despite position-based decision IDs"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-406
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: mismatch presumed reconcilable / ground truth presumed recoverable despite positional IDs
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Append-only audit-log + signature-chain integrity literature. - IF an independent append-only event log or signature chain exists, ground truth can sometimes be reconstructed by replaying/verifying the chain.

  Strength of support: Weak

  Summary: Recoverability is CONDITIONALLY supported: where an immutable append-only record or signature chain captured each approval independently of the positional index, the original linkage can sometimes be reconstructed. That is the only route by which the "reconcilable" presumption could hold. It depends entirely on the existence of a stable secondary record; absent that, positional IDs offer no recovery anchor (see 15b). Support is weak and contingent.

  Caveats: Support holds ONLY if an append-only/stable-key record exists alongside the positional IDs. If decisions were keyed purely by position, this support does not apply.

  Search scope: Audit-log integrity; recoverability. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
