SEARCH-FOR-PRESUMPTION-320:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-320
  Original statement: [inferred] Handing the user blind multi-command shell blocks presumes the agent's model of the user's repo state is accurate enough to script state-mutating sequences.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-320
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that the agent's model of repo state is accurate enough to script blind state-mutating sequences.
      15a: Searched for support that scripted multi-command sequences handed to an operator are an acceptable pattern.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Runbook / runbook-automation practice. — Pre-written command sequences for operators are standard and valuable; a well-formed runbook is a legitimate, supported artifact.
    2. Infrastructure-as-code / declarative convergence (Ansible, Terraform). — Scripting state changes IS standard — but the supported version is DECLARATIVE and convergent (describe desired state; the tool reconciles), not an imperative blind sequence.

  Strength of support: Weak-Moderate

  Summary: Handing an operator a prepared command sequence is a supported pattern in the abstract (runbooks, IaC). The support, however, is for sequences that are idempotent/convergent and that check state before mutating it — not for blind imperative blocks that assume a particular starting repo state. So the practice is endorsed only in its state-checking, idempotent form.

  Caveats: The support evaporates exactly where PRESUMPTION-320 lives — when the sequence is imperative, state-dependent, and the operator cannot see intermediate state. The AGAINST search develops the failure mode (ambiguous mid-sequence failure with no rollback) and the "make each step safe to fail" remedy.

  Recommendation: PARTIALLY-SUPPORTED
