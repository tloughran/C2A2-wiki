SEARCH-AGAINST-ASSUMPTION-329:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-329
  Original statement: "The one-time seed apply_summaries.py must never be rerun (it would clobber hand-edits from approved_summaries.json)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-329
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the one-shot-seed operational constraint
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (challenge is to the GUARD, not the constraint)

  Sources:
    1. Idempotency principle (distributed systems / Nygard, "Release It!") — operations should be safe to repeat; a script that does irreversible damage on a second run is an anti-pattern. The fix is to make the seed idempotent or guarded-in-code, not to rely on "never rerun."
    2. Run-once enforcement in migration frameworks (Flyway, Rails) — applied-once state is tracked IN CODE precisely because humans forget which scripts are one-shot; convention/memory is the known-unreliable mechanism this tooling was built to replace.
    3. "Armed footgun left in the repo" — leaving a destructive, runnable script whose only safety is that everyone remembers not to run it is a recognized latent hazard that worsens as contributors and time increase.

  Strength of challenge: Moderate-Strong (on the guard) / None (on the constraint)

  Summary: The constraint "rerunning would clobber hand-edits" is correct — 15b does not dispute it. What the literature challenges is the safety MODEL: relying on memory/convention to prevent a destructive rerun is an anti-pattern; idempotency and code-level run-once guards exist exactly because "never rerun" by discipline fails as teams and time grow. The risk is latent and grows silently.

  Specific risks: A future contributor (or an automated/agentic process) reruns apply_summaries.py and silently destroys all hand-approved bios; the damage is irreversible and the only prior safeguard was human recall.

  Mitigations available: Make the seed idempotent (merge rather than overwrite); add a guard clause (refuse to run if approved_summaries.json shows hand-edits, or require an explicit --force flag with confirmation); or remove the armed script from the repo after seeding and keep it in history only.

  STEELMAN:
    Strongest counterargument: The script already did its one job; "never rerun" is a perfectly true description of its remaining role, and adding guard code to a dead script is gold-plating a thing that should simply be deleted — so the assumption isn't wrong, it just stops one step short (it should say "and therefore disarm/remove it," not "and therefore remember not to run it").
    What would need to be true for C2A2 to be safe: The destructive path cannot be taken accidentally — enforced by code or by removing the script — not merely documented.
    How to test: Attempt a naive rerun in a sandbox; if it clobbers approved bios with no guard tripping, the memory-only safeguard is insufficient.

  Search scope: idempotency/fail-safe design; run-once enforcement; armed-destructive-tooling-in-repo. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
