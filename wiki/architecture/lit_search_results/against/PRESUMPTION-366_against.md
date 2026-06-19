SEARCH-AGAINST-PRESUMPTION-366:
  Date searched: 2026-06-19
  Original item: PRESUMPTION-366
  Original statement: "[inferred] A documentation-only caveat is a sufficient guard for an armed destructive script (never-rerun by memory, not by code)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-366
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated reliance on documentation as the safeguard
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Fail-safe / guard-by-code (Nygard "Release It!"; safety engineering) — safeguards for destructive operations must be enforced by the system (idempotency, guard clauses, confirmation), not by human memory; documentation is advisory and is the recognized WEAKEST control.
    2. Hierarchy of controls (safety engineering) — "administrative controls" (warnings, procedures, docs) rank BELOW elimination and engineering controls precisely because they depend on humans behaving perfectly every time; for an armed destructive script, docs are near the bottom of the hierarchy.
    3. Latent-error growth with contributors/time/automation — a documented "don't run this" degrades as new contributors arrive, memory fades, and agentic processes act; the probability of the destructive path being taken trends upward while the safeguard stays flat.

  Strength of challenge: Strong

  Summary: A documentation-only caveat is strongly challenged as a SUFFICIENT guard for a destructive script: fail-safe design and the safety hierarchy-of-controls both rank documentation as the weakest control, reliable only if every human (and agent) remembers perfectly forever. As contributors, time, and automation grow, the destructive path's probability rises while the doc-only guard stays flat. This is a recognized anti-pattern, not a safe minimum.

  Specific risks: Eventually someone/something reruns the script and irreversibly clobbers hand-approved bios; the only thing that stood between the repo and that loss was a sentence in the docs.

  Mitigations available: Replace/supplement the caveat with a code guard (idempotent merge; refuse-if-edits-present; require --force + confirmation) or disarm by removing the script post-seed; if docs are kept, treat them as a complement to, never a substitute for, an engineering control.

  STEELMAN:
    Strongest counterargument: In a single-maintainer repo the maintainer's memory is in fact reliable for the foreseeable future, and adding guard code to a one-shot script that should simply be deleted is wasted effort — the right move is disarmament (delete), which is cheaper than either docs or guards.
    What would need to be true for C2A2 to be safe: The destructive path is removed or code-guarded, so safety does not depend on anyone remembering — even if the docs are never read.
    How to test: Could a new contributor or an agent, reading only the repo, run the script and lose data? If yes, the doc-only guard is insufficient.

  STEELMAN note: Strong twin of ASSUMPTION-329 — 329 states the (correct) never-rerun constraint; 366 makes explicit the (insufficient) doc-only guard relied upon to enforce it.

  Search scope: fail-safe/guard-by-code; safety hierarchy of controls; latent-error growth of administrative controls. Comprehensive.

  Recommendation: CHALLENGED
