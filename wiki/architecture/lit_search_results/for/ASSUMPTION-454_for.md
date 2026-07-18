SEARCH-FOR-ASSUMPTION-454:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-454
  Original statement: Two of the scheduler watchdog's three output-verification checks point at unmounted paths and can never pass - a permanent blind spot until the folders are mounted or the rows dropped.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-454
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15a: Searched for supporting literature; result SUPPORTED (strength Strong)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Health-check vs heartbeat literature (PulsAPI 2024; SRE School 'Heartbeat' 2026): a monitor that can never observe the thing it claims to verify produces a permanent gray-failure blind spot - the check contributes no information yet reads as coverage.
    2. 'Unfalsifiable green check' pattern (gray-failure / silent-failure discussions): a verification step wired to an unreachable target is worse than no check, because it manufactures false assurance.
    3. R.I. Cook (1998): 'complex systems run in degraded mode' - latent broken defenses accumulate unnoticed; a check that structurally cannot fail is a textbook latent failure.

  Strength of support: Strong

  Summary: The monitoring literature strongly supports the assumption: a verification check pointed at an unmounted (unreachable) path is a canonical 'unfalsifiable green check' - it can never fail, so it never signals, and its presence inflates apparent coverage. Because the watchdog is the fleet's sole failure detector, two of three checks being structurally inert is a serious latent blind spot exactly of the kind resilience literature warns about.

  Caveats: EMPIRICAL: the specific claim (two of three paths unmounted) is a one-command check on the task's sandbox mounts; literature confirms the anti-pattern, not C2A2's particular config.

  Recommendation: SUPPORTED
