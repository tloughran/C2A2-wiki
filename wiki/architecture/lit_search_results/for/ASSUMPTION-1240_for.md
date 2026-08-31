SEARCH-FOR-ASSUMPTION-1240:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1240
  Original statement: "Read-only agents get read-only tool grants, enforced rather than assumed."
  Generalizable limb searched: Does technical/architectural enforcement of an access boundary
    outperform advisory or instruction-level restriction for LLM agents, and is there measured
    evidence of the gap?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. The
    headline quantitative finding (4-37% unauthorized tool selection under prompt-only restriction)
    was seen in a search snippet attributed to arXiv:2605.18414 and was not verified against the
    paper's abstract or full text.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1240
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced as the proposed remedy paired with ASSUMPTION-1235
      15a: Searched for supporting literature (2026-08-31)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "Prompts Don't Protect: Architectural Enforcement via MCP Proxy for LLM Tool Access Control,"
       2026. arXiv:2605.18414. — The closest available direct test of the enforced-vs-advisory
       question. Snippet reports that when an unauthorized tool is the most task-relevant one,
       prompt-level restriction fails and the model selects it in 4-37% of adversarial cases,
       varying by model. This is exactly the "assumed" failure mode the assumption targets. Title
       alone states the conclusion.
    2. OWASP Gen AI Security Project, 2025. "LLM06:2025 Excessive Agency." OWASP Top 10 for LLM
       Applications. — Explicitly prescribes the enforcement half: an agent needing read access to
       a products table "should not have access to other tables, nor the ability to insert, update
       or delete records. This should be enforced by applying appropriate database permissions for
       the identity that the LLM extension uses to connect." Enforcement at the identity layer, not
       the instruction layer, is the stated remedy.
    3. SafeHarness (authors not captured in snippet), 2026. arXiv:2604.13630. — Enforces least
       privilege at the tool-execution boundary with tools classified read_only / write / execute /
       network / destructive. Demonstrates that a read-only tier is an implementable, standard
       primitive rather than an aspiration.
    4. "Runtime Governance for AI Agents: Policies on Paths," 2026. arXiv:2603.16586; and
       "A Deterministic Control Plane for LLM Coding Agents," 2026. arXiv:2606.26924. — Both argue
       for a deterministic layer in front of every tool call. Snippet framing: rule-following in a
       model is "a probabilistic, learned behavior, not a deterministic execution path."
    5. Oso (osohq.com), n.d. "Why Prompt-Based Safety Is Not Enough." Vendor engineering essay. —
       Non-peer-reviewed but states the mechanism cleanly: prompts shape behaviour but do not
       control execution; prompt compliance is probabilistic and any user-controlled input can
       attempt to override a system-prompt restriction, an attack vector architectural enforcement
       eliminates by construction.

  Strength of support: Strong

  Summary: This is the best-supported item in the set. The claim has two limbs and both are backed.
    On the *normative* limb, OWASP LLM06 does not merely recommend read-only grants for read-only
    roles, it specifies that the restriction be implemented in the connecting identity's
    permissions rather than in instructions. On the *comparative* limb — enforced beating advisory —
    there is at least one 2026 paper that appears to measure the gap directly, reporting failure of
    prompt-level restriction in 4-37% of adversarial cases depending on model, with the failure rate
    highest precisely when the forbidden tool is the most useful one for the task. The mechanistic
    account is consistent across sources: instruction-following is a probabilistic behaviour, so a
    restriction expressed only as an instruction has a non-zero and model-dependent violation rate,
    while a restriction expressed as a withheld capability has a violation rate of zero by
    construction. Several independent 2025-2026 architectures (MCP proxies, capability brokers,
    policy engines at the pre_tool_call interception point) implement the same conclusion.

  Caveats: (a) The 4-37% figure is snippet-level and unverified; the adversarial framing may not
    transfer to a benign agent drifting out of scope by ordinary reasoning rather than under attack.
    (b) Most of this literature is very recent (2025-2026) and much of it is vendor or preprint
    material; peer-reviewed replication is limited. (c) Enforcement has a stated cost the sources
    acknowledge: one snippet notes "invasive" protection mechanisms can interfere with normal agent
    functioning, and the TBAC literature flags policy-authoring complexity. (d) Enforcement is only
    as good as the classification behind it — "read-only" must be correctly assigned per tool, and
    tools like `git` or a shell are genuinely mixed-mode, so the enforcement layer inherits the
    boundary-drawing problem rather than dissolving it. That handoff is where this item touches
    PRESUMPTION-902.

  Recommendation: SUPPORTED
