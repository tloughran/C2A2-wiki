SEARCH-FOR-PRESUMPTION-317:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-317
  Original statement: [inferred] The prior task design presumed execution-context uniformity — that scheduled tasks inherit the attended Cowork environment's capabilities (push, $HOME, writable .git).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-317
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that the scheduled runtime equals the interactive runtime in capabilities.
      15a: Searched for any support that interactive and scheduled execution contexts can be expected to be uniform.
    Current status: NO-SUPPORT-FOUND (weak conditional only)

  Supporting evidence found: No (weak/conditional)

  Sources:
    1. The Twelve-Factor App, Factor X "Dev-prod parity" — the ASPIRATION. — The methodology's GOAL is to make environments as similar as possible, including running admin/one-off processes in an environment identical to long-running processes; insofar as that goal is met, expecting parity is reasonable. This is support for the GOAL, not evidence that parity holds by default.
    2. Managed-runtime parity guarantees (e.g., container images shared across interactive and scheduled invocations). — When the same image/config is reused, many capabilities DO carry over; this is the only condition under which the presumption is safe.

  Strength of support: Weak (conditional on engineered parity)

  Summary: The only thing the literature supports is that environment parity is a worthy GOAL and can be engineered; it does not support an assumption that parity exists by default. Capabilities such as outbound push credentials, $HOME, and a writable .git are environment-provisioning facts that hold only when deliberately arranged. The supportive case for PRESUMPTION-317 is therefore thin and entirely conditional.

  Caveats: The presumption asserts inheritance as a default, which dev/prod-parity literature treats as something you must WORK to achieve, not assume. The AGAINST search documents the much stronger opposite finding (the canonical environment-mismatch bug class). This is close to a NO-SUPPORT-FOUND result for the presumption as stated.

  Recommendation: NO-SUPPORT-FOUND
