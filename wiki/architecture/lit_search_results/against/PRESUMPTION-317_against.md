SEARCH-AGAINST-PRESUMPTION-317:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-317
  Original statement: [inferred] The prior task design presumed execution-context uniformity — that scheduled tasks inherit the attended Cowork environment's capabilities (push, $HOME, writable .git).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-317
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption of interactive/scheduled capability parity.
      15b: Searched for evidence that interactive and scheduled execution contexts routinely DIFFER in capability.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. The Twelve-Factor App, Factor X "Dev-prod parity" + the entire "works on my machine" problem. — The canonical, decades-old failure class is precisely that one execution context has capabilities another lacks; parity is something you must engineer, never assume. The presumption is the textbook anti-pattern.
    2. Cron/scheduled-job environment differences (non-interactive shells lack the interactive PATH/$HOME/agent/credentials; classic "works interactively, fails in cron"). — Scheduled/non-interactive contexts routinely lack ssh-agent keys, $HOME, login-shell env, and write tokens that the interactive session has. Direct, specific contradiction of the presumed inheritance.
    3. Least-privilege batch/service identities (Saltzer & Schroeder; service accounts deliberately scoped DOWN vs interactive users). — Good security design gives automated contexts FEWER capabilities on purpose, so parity is not just absent by accident but often withheld by design. Strong challenge.

  Strength of challenge: Strong

  Summary: This presumption is contradicted by one of the most established lessons in software operations. Interactive and scheduled/non-interactive contexts differ in environment and credentials as a rule, not an exception; "works in cron" failures and the "works on my machine" class are this exact bug. Worse, least-privilege design INTENTIONALLY scopes automated contexts down, so the presumed inheritance is frequently withheld by design. The 2026-06-07 incident (scheduled task could not push) is a direct instance.

  Specific risks: Any scheduled task built against presumed-inherited capabilities fails at run time, silently or loudly, exactly when no human is attending — the worst time. Because the failure surfaces only on the scheduled run, it can sit undetected (couples ASSUMPTION-283's silent-cron risk). The whole auto-publish design rests on a capability the runtime may not have.

  Mitigations available: Capability discovery FIRST — probe the scheduled context for push/$HOME/writable-.git BEFORE building on them (PRESUMPTION-318); fail loudly and early if a required capability is absent; engineer explicit parity (same image/credentials) or design the task for the LEAST-capable context; never assume inheritance — assert it.

  STEELMAN:
    Item: PRESUMPTION-317
    Strongest counterargument: Assuming the scheduled runtime is "the same computer" as the attended session is the single most common and most expensive environment bug in the field, and it is invisible until the unattended run fails. The presumption is doubly unsafe here because security best practice deliberately gives batch identities fewer rights than interactive ones — so the missing capability is not a fluke but the expected, designed state. Building auto-push on presumed inheritance guarantees a failure that surfaces only when no one is watching.
    What would need to be true for C2A2 to be safe: The scheduled context's capabilities (push credential, $HOME, writable .git) are explicitly verified present before any task depends on them, or the task is designed to degrade safely when they are absent.
    How to test: Run a capability-probe task in the scheduled context and diff its environment/credentials against the attended session; the incident predicts they differ.

  Recommendation: CHALLENGED
