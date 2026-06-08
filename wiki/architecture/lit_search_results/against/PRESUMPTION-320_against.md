SEARCH-AGAINST-PRESUMPTION-320:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-320
  Original statement: [inferred] Handing the user blind multi-command shell blocks presumes the agent's model of the user's repo state is accurate enough to script state-mutating sequences.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-320
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that the agent's repo-state model is accurate enough to script blind state-mutating sequences.
      15b: Searched for evidence that blind, state-dependent compound command sequences are unsafe.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Idempotency / "make retries safe" literature (AWS Builders' Library, "Making retries safe with idempotent APIs"; forward-recovery saga design). — Blind compound sequences fail ambiguously: when step k fails the operator cannot know how much happened, and a non-idempotent rerun multiplies side effects. The recommended design is idempotent, state-checking steps — the opposite of a blind imperative block.
    2. Shell-scripting-for-production guidance (set -euo pipefail; check-before-mutate; "shell commands always report changed"). — Production shell practice insists each state-mutating step verify preconditions and be safe to rerun, because the script's model of the starting state is routinely wrong (uncommitted changes, detached HEAD, diverged branch, dirty tree).
    3. Declarative/convergent configuration (Ansible/Terraform rationale). — The field moved AWAY from imperative blind sequences toward declarative convergence precisely because scripting absolute state transitions from a presumed starting state is fragile; convergence reconciles to a desired state regardless of where it started.

  Strength of challenge: Moderate-Strong

  Summary: Handing an operator a blind, state-dependent, multi-command block is challenged across idempotency, production-shell, and configuration-management literature. The agent's model of the user's repo state is frequently inaccurate (dirty tree, diverged branch, partial prior runs), and an imperative sequence assuming a starting state fails ambiguously mid-way with no rollback and no operator visibility. The endorsed alternatives are idempotent, check-before-mutate steps or declarative convergence.

  Specific risks: A mid-sequence failure leaves the repo in an unknown partial state that neither the agent (no visibility) nor the operator (couldn't see intermediate state) can confidently recover; a non-idempotent rerun compounds damage (duplicate commits, force-push over real work, lost stash). Compounds PRESUMPTION-317 (the agent also mismodels the environment, not just the repo state).

  Mitigations available: Make each step idempotent and safe to fail (check-before-mutate, guard clauses); have the sequence first PRINT/inspect state (git status/branch) and stop on surprise rather than mutate blindly; prefer one reversible step at a time over a compound block; never script force-push/reset blind; where possible use a declarative/convergent operation instead of an imperative transition.

  STEELMAN:
    Item: PRESUMPTION-320
    Strongest counterargument: A blind multi-command block bets the user's repository on the agent's unverified mental model of its current state — a model that is wrong often enough (uncommitted work, diverged branch, leftover state from a prior partial run) that the bet is reckless when steps are state-mutating and irreversible. Because the operator was handed the block precisely because they cannot see intermediate state, a failure at step k strands the repo in an unknown partial state with no safe rerun, and a non-idempotent retry actively destroys work. The safe unit is one reversible, state-checking step, not a compound imperative script.
    What would need to be true for C2A2 to be safe: Every state-mutating step checks its precondition and is idempotent/reversible, and the sequence halts on any state surprise rather than proceeding blindly.
    How to test: Run the block against a deliberately dirty/diverged repo and check whether it detects-and-stops or proceeds to corrupt state.

  Recommendation: CHALLENGED
