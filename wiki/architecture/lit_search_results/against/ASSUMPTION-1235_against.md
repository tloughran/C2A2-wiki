SEARCH-AGAINST-ASSUMPTION-1235:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1235
  Original statement: "This agent has no business running `git` at all" — a read-only analysis agent
    should not hold a version-control capability.
  Generalizable limb searched: Does narrowing an agent's capability set to the ex-ante-declared
    task scope produce net benefit, once the cost of suppressed legitimate work is counted?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Moderate. 3 queries (budget cap). One directly on-point agentic-security
    preprint with a quantitative statement of the confinement/utility tradeoff; the remainder is
    practitioner/vendor literature, which is systematically biased toward selling least-privilege
    tooling and therefore under-reports its costs. I read titles, URLs and search-result snippets
    only — I did not read the full text of the arXiv papers cited. Treat all quantitative figures
    below as snippet-level, unverified against the primary source.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1235
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced from a run in which an out-of-scope `git` call was made and flagged; stated as
           a normative capability rule.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Anonymous/arXiv, 2026. "LinuxArena: A Control Setting for AI Agents in Live Production
       Software Environments." arXiv preprint 2604.15384. — Snippet states that simple sandboxing
       is not a viable substitute for monitoring in production Linux environments, because
       restricting capabilities removes much of the attack surface but also prevents the agent
       from completing a large fraction of legitimate work. This is the closest thing found to a
       *measured* statement of the exact cost 1235 ignores. Snippet only; not read in full.
    2. Anonymous/arXiv, 2026. "Beyond Static Sandboxing: Learned Capability Governance for
       Autonomous AI Agents." arXiv preprint 2604.11839. — Title and framing assert that a static,
       pre-declared capability boundary is the thing being moved away from. Title/URL seen only;
       I did not read the abstract or body, so this is weak corroboration of direction, not of
       any specific finding.
    3. Material Security, n.d. "Why Least Privilege Policies Fail at Scale (and How to Fix Them)."
       Vendor knowledge base. — Argues that friction between strict access control and daily
       productivity is a primary cause of least-privilege programme failure: blocked work produces
       ticket floods and pressure to re-broaden access. Vendor source; directionally useful,
       evidentially weak.
    4. TheFence, n.d. "Implementing the Principle of Least Privilege: Challenges, Pitfalls and
       Practical Solutions." Vendor knowledge base. — Documents the shadow-workaround failure mode:
       when governance is perceived as too restrictive, users obtain access outside the supervised
       path, producing unaudited privilege that outlives its need. Vendor source.
    5. Microsoft Security Blog, 2026-07-16. "Least privilege for AI agents: Identity, access, and
       tool binding." — Supports tool binding but frames the design problem as scoping to the
       *task*, which presupposes the task is known; does not defend blanket capability denial.
       Cited as a limit on 1235's generality rather than a refutation.

  Strength of challenge: Moderate

  Summary: The literature does not support the unconditional form of 1235. The confinement/utility
  tradeoff is real and, in at least one agentic setting, described as costing "a large fraction of
  legitimate work" — the same shape as the counter-case already in C2A2's own record, where the
  out-of-scope `git` call produced the run's only verified follow-through finding. The stronger
  point is that 1235 is stated as a capability-type rule ("no business running `git` at all") when
  the actual risk is action-type: `git log`, `git diff` and `git show` are read operations, while
  `git push --force`, `git reset --hard` and `git clean` are destructive. A rule that denies the
  binary rather than the mutating subcommands buys almost no risk reduction and pays the full
  utility cost. Separately, no source found offers a measured incident-rate benefit for narrowing
  an *already read-only* agent's tool list; the benefit is asserted throughout the vendor corpus
  and measured nowhere I could see.

  Specific risks: If 1235 is enforced as written, C2A2 loses cheap access to the vault's own change
  history — which is the natural ground truth for every week-over-week delta claim the pipeline
  makes (see ASSUMPTION-1237, PRESUMPTION-897). The pipeline would then be reasoning about change
  from reconstructed snapshots while a authoritative change log sits one denied command away. A
  second risk is the shadow-workaround mode: the capability gets re-obtained through a less
  observable path (a shell wrapper, a copied working tree) that is worse than the original.

  Mitigations available: Replace the capability-level ban with an action-level allowlist — permit
  `git log`, `git diff`, `git show`, `git status`, `git ls-files`; deny everything that writes.
  Alternatively run against a read-only clone or with `GIT_DIR` pointed at a snapshot. Both keep
  the finding-producing capability and remove the destructive one. Log every git invocation so the
  out-of-scope-use signal 14a wanted is preserved without the denial.

  STEELMAN:
    Strongest counterargument: The value of the one finding is not evidence that the capability
    should have been granted — it is exactly the survivorship pattern that makes over-provisioning
    self-perpetuating, since the useful excursions are visible and the near-misses are not. An
    agent that reaches for tools outside its declared scope has already demonstrated that its scope
    declaration does not bind its behaviour, which is a control failure independent of whether this
    particular excursion paid off. Vendor sources documenting "friction costs" are describing human
    users who can escalate through a manager; an autonomous agent has no such channel, so the
    failure mode of over-restriction is a stalled run, not a shadow workaround. And the read/write
    split within `git` is not as clean as it looks: `git` respects hooks and config that can
    execute arbitrary code, so "read-only git" is not obviously read-only.
    What would need to be true for C2A2 to be safe: Either (a) the specific subcommands granted are
    genuinely non-mutating under the actual repo configuration, including hooks and aliases, and
    this is verified rather than assumed; or (b) the scope-declaration mechanism is enforced such
    that out-of-scope reaches are impossible rather than merely logged, and the loss of follow-
    through findings is accepted as a known, priced cost.
    How to test: Take the last N runs. For each out-of-scope tool call, classify the outcome —
    verified finding, no effect, or harm. Compute the ratio. If verified findings dominate and no
    harm has ever occurred, the confinement rule is costing more than it returns and the burden is
    on 1235. Separately, audit the repo for hooks/aliases to establish whether read-only git is
    achievable at all.

  Recommendation: CHALLENGED
