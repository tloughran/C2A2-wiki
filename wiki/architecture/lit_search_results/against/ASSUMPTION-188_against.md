SEARCH-AGAINST-ASSUMPTION-188:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-188
  Original statement: "Sandbox cannot write .git; commits must come from host shell (ACL + stale lock)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-188
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: sandbox git writes failed (ACL + stale lock); commits routed through host shell.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Docker / OCI runtime docs. — A bind-mounted .git with appropriate uid/gid and a writable mount is technically achievable; sandbox git-write is a permissions configuration, not an inherent impossibility.
    2. Chacon, S. & Straub, B. "Pro Git" (index.lock section). — A stale index.lock from a crashed/interrupted process is a removable condition, not evidence that writes are categorically blocked.

  Strength of challenge: Moderate

  Summary: The challenge targets the framing, not the practice: 'cannot write .git' overstates a situation that is really 'is not currently permitted to, by ACL + a removable stale lock.' Both contributors (ACL and stale lock) are configurable/clearable. Conflating a configuration choice with an impossibility risks foreclosing a future where sandbox writes are deliberately enabled.

  Specific risks: Encoding 'cannot' as architecture ossifies a config accident into a permanent constraint; masks the stale-lock root cause shared with ASSUMPTION-189.

  Mitigations available: Restate as 'commits are routed through the host by policy'; track the ACL/lock as the actual mechanism; clear stale locks via the serialization fix in REVISE-033.

  Recommendation: PARTIALLY-CHALLENGED (framing only)

  STEELMAN:
    Item: ASSUMPTION-188
    Strongest counterargument: Calling it 'cannot' is a category error: the sandbox is not permitted to write .git under the current ACL, and a stale lock is a transient failure, not a wall. Architecture built on 'cannot' will not notice when the underlying config changes.
    What would need to be true for C2A2 to be safe: Safe if the constraint is documented as a policy choice with the mechanism named (ACL + lock), so it stays revisable.
    How to test: Attempt a configured writable bind-mount in a throwaway sandbox; if it succeeds, 'cannot' is falsified and the premise becomes a policy, not a fact.
