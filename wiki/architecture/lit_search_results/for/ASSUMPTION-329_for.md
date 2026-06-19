SEARCH-FOR-ASSUMPTION-329:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-329
  Original statement: "The one-time seed apply_summaries.py must never be rerun (it would clobber hand-edits from approved_summaries.json)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-329
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the operational constraint on a one-shot seed script
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Database migration / seed-script practice — one-shot seed and data-migration scripts are a recognized category; a non-idempotent seed that overwrites downstream hand-edits is correctly understood to be unsafe to rerun. The FACTUAL claim ("rerunning would clobber edits") is well-grounded.
    2. "Run-once" migration conventions (Flyway/Rails schema_migrations etc.) — frameworks record which migrations have run precisely so a one-shot transform is not re-applied; this validates the underlying concern that one-shot transforms must be prevented from re-running.

  Strength of support: Moderate (for the factual constraint) / Weak (for "guarded by memory")

  Summary: The literature supports the FACT that a non-idempotent one-shot seed which overwrites later hand-edits must not be re-run — that is exactly why migration frameworks track applied-once state. So the constraint itself ("never rerun") is correct and well-precedented. What the literature does NOT support is leaving the enforcement to memory/convention; the precedent is to enforce run-once IN CODE (applied-state ledger, guard clause, idempotency). Support is therefore for the constraint, not the chosen guard mechanism.

  Caveats: The supportive precedent (migration frameworks) actually argues for a code-level guard, which is the disconfirming angle developed under PRESUMPTION-366. "Must never be rerun" being TRUE does not make "documented as never-rerun" a SUFFICIENT safeguard.

  Search scope: one-shot/run-once migrations; non-idempotent seed scripts; applied-state ledgers. Comprehensive.

  Recommendation: PARTIALLY-SUPPORTED
