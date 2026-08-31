SEARCH-AGAINST-ASSUMPTION-1240:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1240
  Original statement: "Read-only agents get read-only tool grants, enforced rather than assumed."
  Generalizable limb searched: Does *enforced* access control deliver the incident reduction it is
    credited with, and does a read-only grant actually bound the risk it is taken to bound?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Moderate-to-good on the "read-only is not safe" limb (a well-known, widely
    replicated threat model). Weak on the "enforcement reduces incidents" limb — I found essentially
    no rigorous measurement in either direction, which is itself the finding. 3 queries (cap).
    Snippet-level reading only; no full texts.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1240
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Stated as a remediation rule following the out-of-scope capability observation.
      15b: Searched for challenging literature (2026-08-31)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Simon Willison, 2025-06-16. "The lethal trifecta for AI agents: private data, untrusted
       content, and external communication." simonwillison.net. — The canonical statement that
       *read* access to private data is one of the three legs of a working exfiltration pipeline.
       A read-only grant does not remove the risk; it supplies leg one. Directly limits what
       "read-only" buys.
    2. NHI Management Group, 2026. "AI agent lethal trifecta exposes a governance gap in access
       control." nhimg.org. — Argues that partial mitigations (read-only egress, tokenised data)
       sit between leg-present and leg-absent, and that a binary yes/no audit column produces false
       confidence. This is precisely the failure mode of "enforced rather than assumed" when the
       enforcement is recorded as a boolean. Trade source, snippet only.
    3. Unit 42 / Palo Alto Networks finding, as reported by Sonrai Security, 2026 ("Why 92% of Cloud
       Permissions Are Never Used, and What That Costs You," also carried by Security Boulevard,
       2026-05). — Reports analysis of >680,000 cloud identities finding 99% held excessive
       permissions unused for 60+ days, and that ~92% of cloud permissions are never used. Read as
       secondary reporting of a vendor telemetry study; I did not see the Unit 42 primary. Bears on
       1240 because these are environments that *do* have enforced access control: enforcement is
       ubiquitous and over-provisioning is nonetheless the empirical norm. Enforcement constrains
       the grant, not the grant's rightness.
    4. Anonymous/arXiv, 2026. "Security-First Approach to API Pipeline Development with Zero-Trust
       Architecture." arXiv preprint 2606.09062. — Snippet reports a mean 35% incident reduction
       (SD 18.0%) across cases after zero-trust intervention. This is the ONLY quantitative
       incident-reduction figure I found. It is a single unrefereed preprint, bundles least
       privilege with an entire zero-trust programme, and has no control for secular trend or
       attention effects. Cited here not as support but to record how thin the measured base is.
    5. PortSwigger Web Security Academy, n.d. "Access control vulnerabilities and privilege
       escalation." — Standard reference documenting broken access control as an enforcement
       failure: the control exists and is bypassed. Establishes that "enforced" is a claim about
       intent, not about effect.

  Strength of challenge: Moderate

  Summary: 1240 survives as a policy preference but not as the risk-eliminating measure it is
  phrased as. Two independent problems. First, the incident-reduction benefit of enforced least
  privilege is close to unmeasured — the corpus is almost entirely vendor advocacy, and the one
  quantitative figure I located is an unrefereed preprint confounding least privilege with a whole
  zero-trust rollout. Second, and more serious for C2A2, "read-only" does not bound the risk: under
  the lethal-trifecta model a read-only agent that also sees untrusted content and has any egress
  channel is a complete exfiltration path, and read access to the private corpus is the leg that
  makes it work. C2A2's agents read a vault containing arbitrary ingested third-party text and emit
  files and web searches — that is all three legs. The enforcement 1240 proposes would leave that
  intact while creating a record that says the risk was handled.

  Specific risks: The named risk is false closure. If read-only grants are marked "enforced" and the
  item is retired, the pipeline loses the prompt to examine the actual exposure — untrusted vault
  content steering a read-only agent's WebSearch queries or written outputs. A second risk is that
  enforcement is recorded as a boolean and never re-checked against effective privilege, which is
  the exact over-provisioning-under-enforcement pattern the cloud telemetry describes.

  Mitigations available: Track effective privilege (what was actually invoked) rather than granted
  privilege, and reconcile them periodically — this is the CIEM pattern from the cloud literature
  and is directly portable. Treat the egress leg, not the read leg, as the control point: constrain
  what an agent may write and where it may send, since read is the leg C2A2 cannot remove. Replace
  the boolean audit column with a three-state one (leg absent / partially reduced / present), per
  source 2.

  STEELMAN:
    Strongest counterargument: "Enforced rather than assumed" is not a claim that enforcement
    eliminates incidents — it is a claim about where the failure surfaces. An assumed constraint
    fails silently and is discovered post hoc; an enforced one fails loudly at the boundary and is
    observable. That is worth having even at zero measured incident reduction, because it converts
    an unknown into a logged event. The lethal-trifecta objection is real but is an argument for
    *additional* controls on the egress leg, not against enforcing the read leg — nobody claims
    read-only is sufficient, only that an unenforced grant is strictly worse than an enforced one.
    The over-provisioning telemetry likewise shows that enforcement without lifecycle review fails,
    which argues for review, not against enforcement.
    What would need to be true for C2A2 to be safe: The read-only grant would have to be paired with
    an explicit account of the egress leg — what a read-only agent can write, where, and who reads
    it — and that account would have to show either no untrusted content in the read corpus or no
    attacker-influencable egress. Neither is currently established.
    How to test: Red-team it. Plant a benign marker instruction inside a vault page (a page an agent
    will plausibly read) and observe whether it propagates into any agent's queries, written output,
    or downstream file. If it propagates, read-only enforcement is not the binding control and the
    item should be re-scoped to egress.

  Recommendation: PARTIALLY-CHALLENGED
