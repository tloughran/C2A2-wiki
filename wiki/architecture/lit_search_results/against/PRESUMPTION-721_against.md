SEARCH-AGAINST-PRESUMPTION-721:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-721
  Original statement: That a blocker named on one day is the same blocker the next; two ceilings declared hard on 08-06 (3.3 GB disk, 45-second wall) both cleared today by an unlogged TMPDIR change, with no representation in the system for "currently not biting" as distinct from "repaired".

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-721
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by reading today's two successes against 08-06's impossibility claims for the same operations
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Configuration Drift Explained" (Wiz, 2026) and "Configuration Drift: How It Happens, Top Sources + How to Stop It" (Puppet, 2026). Establish that undocumented, unlogged environment changes are the dominant cause of configuration drift, and that root-cause analysis becomes unreliable precisely because "the root cause of an issue might stem from undocumented changes" that leave no trace linking a fix to the original failure.
    2. Configuration-drift risk writeups (Acsense, 2026; Aqua Security cloud-native academy, 2026). Document the canonical "temporary fix becomes permanent, unrecorded state" pattern — a config changed to resolve one incident silently altering conditions for unrelated failures, with no record connecting the two. Directly analogous to an unlogged TMPDIR change clearing two separately-declared hard ceilings.
    3. "What is Configuration Drift?" (IBM, ibm.com/think, 2026). Notes that systems "no longer match their documented configurations," creating a gap between recorded state (blocker still "hard") and actual state (blocker cleared by an untracked change) — the exact structural gap this presumption identifies.

  Strength of challenge: Moderate

  Summary: The configuration-management literature consistently shows that unlogged environment changes decouple a system's actual state from its documented/declared state, and that this decoupling is a common, well-documented failure mode rather than an edge case. It supports treating "the blocker didn't bite today" as distinct from "the blocker is fixed" — the literature's standard failure pattern is exactly an untracked, incidental change silently altering conditions, with no audit trail linking cause to effect. Sources are practitioner/vendor content rather than peer-reviewed research, which caps the strength of the challenge at moderate.

  Specific risks: If TMPDIR (or another unlogged environment variable) reverts, or if the change masked rather than fixed the disk/wall-clock ceilings, the blockers could reappear without warning; any downstream plan that treated 08-06's "hard ceiling" as retired will be caught unprepared, since the system currently has no state for "conditionally clear, mechanism unverified."

  Mitigations available: Yes — standard configuration-management practice is to log every environment change with an explicit causal link to the incident it addresses, and to add an intermediate status ("not currently reproducing, mechanism unconfirmed") distinct from both "blocked" and "resolved."

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-721
  Strongest counterargument: An unlogged TMPDIR change clearing two independently-declared hard ceilings on the same day is a textbook configuration-drift signature — the fix and the failure were never causally linked, so there is no way to know whether the ceilings were genuinely raised, coincidentally avoided, or merely deferred; treating "cleared today" as equivalent to "the 08-06 blocker is resolved" substitutes one successful trial for a validated causal fix, exactly the substitution the drift literature warns produces silent regressions.
  What would need to be true for C2A2 to be safe: The TMPDIR change would need to be logged with an explicit causal hypothesis (why it should affect disk usage or wall-clock time), then re-tested under the original 08-06 conditions to confirm the mechanism, before the ceilings are marked resolved rather than merely "not observed today."
  How to test: Revert the TMPDIR change (or reproduce the original environment) and rerun the two operations that hit the 08-06 ceilings; if they fail again, the presumption is empirically confirmed false — the blocker was masked, not repaired.
