SEARCH-AGAINST-ASSUMPTION-814:
  Date searched: 2026-08-10
  Original item: ASSUMPTION-814
  Original statement: "The 2026 multi-agent-debate literature reports that homogeneous, unguided debate can underperform a single self-correcting agent — C2A2's exact configuration."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-814
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted a literature return that bears on C2A2's own architecture rather than on a tradition's content
      15b: Searched for challenging literature (adversarial pass)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Chan et al.-style original multi-agent debate line and its 2026 successors (arxiv abs/2502.08788, "Stop Overvaluing Multi-Agent Debate — We Must Rethink Evaluation and Embrace Model Heterogeneity"; Springer/King Saud Univ. 2025, "Adaptive heterogeneous multi-agent debate for enhanced educational and factual reasoning") — report multi-agent debate outperforming single-agent chain-of-thought/self-consistency by 4-10 percentage points in several benchmarks, and find that heterogeneity (not homogeneity per se) is the key moderator that makes debate work. This directly challenges any blanket claim that debate underperforms single-agent methods: the literature's actual position is conditional on homogeneity/guidance, not a general indictment of multi-agent debate. [unverified — from search snippet]
    2. arxiv 2510.20963v2, "When and Why Does Multi-Agent Debate Fail and Does It Really Underperform?" — the title itself signals the 2026 literature is actively contesting the underperformance claim, framing it as task- and condition-dependent rather than settled; per search snippet, "multi-agent debate methods generally outperform single-agent settings... consistent with findings that debate can leverage diverse knowledge... [but] does not always guarantee improvement." This is a direct partial contradiction of ASSUMPTION-814's framing as a settled 2026 consensus. [unverified — from search snippet]
    3. arxiv 2605.00914, "The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate" — this is very likely the paper ASSUMPTION-814 is drawing on; per snippet it scopes its finding explicitly to "the 7-8B instruction-tuned model class," identifying sycophantic conformity, contextual fragility, and consensus collapse as the mechanisms, and explicitly notes heterogeneous/structured-role debate as an alternative that performs better. This is a genuine boundary condition: the underperformance finding is scoped to small/mid-size homogeneous models without structured roles, not a general claim about all multi-agent debate architectures, including ones like C2A2 that may use larger or more differentiated agent roles. [unverified — from search snippet]

  Strength of challenge: Moderate

  Summary: The 2026 literature does contain the underperformance finding ASSUMPTION-814 cites, but it is neither unanimous nor unconditional: multiple concurrent 2025-2026 papers report debate outperforming single-agent baselines when agents are heterogeneous or role-differentiated, and even the paper most likely underlying the claim scopes its result to a specific model class (7-8B homogeneous, unguided, role-undifferentiated) and specific failure mechanisms (sycophancy, contextual fragility, consensus collapse) rather than asserting debate universally underperforms. Whether "C2A2's exact configuration" matches that scoped condition (model size, homogeneity, absence of guidance/roles) is itself unverified from these snippets and is the crux the assumption should be tested against, not assumed.

  Specific risks: If C2A2 assumes debate is disfavored based on an overgeneralized reading of a scope-limited finding, it may prematurely abandon or under-invest in structured/heterogeneous debate mechanisms that the same literature shows can outperform isolated self-correction — potentially locking in a worse architecture than an alternative the literature actually recommends (heterogeneity + guided roles, not "single agent" per se).

  Mitigations available: Verify whether C2A2's specific configuration (agent model(s), degree of role differentiation/guidance, model homogeneity) matches the scoped conditions under which underperformance was found; if C2A2's agents are already heterogeneous/role-guided (as its own agent-type structure suggests — 14a, 14b, 15a, 15b are role-differentiated, not homogeneous unguided debaters), the cited finding may not transfer to C2A2 at all.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-814
  Strongest counterargument: The literature's underperformance finding is explicitly conditioned on homogeneity, small-to-mid model scale, and absence of structured roles/guidance — three conditions that arguably do NOT describe C2A2, whose agents (14a/14b/15a/15b, master, pattern-detector, etc.) are role-differentiated and guided by distinct prompts/responsibilities, not identical unguided peers voting to consensus. If C2A2 is actually heterogeneous-and-guided rather than "homogeneous, unguided," the cited 2026 finding may not transfer to it at all, making the assumption's self-description ("C2A2's exact configuration") the weakest link rather than the literature.
  What would need to be true for C2A2 to be safe: C2A2's agents would need to be meaningfully heterogeneous (different models, prompts, or roles) and operate under explicit guidance/structure (defined roles, not simple majority-vote consensus) for the disfavored "homogeneous unguided" pattern not to apply — conditions the system's own multi-role agent design plausibly already satisfies.
  How to test: Directly compare C2A2's agent architecture against the scoping conditions in arxiv 2605.00914 (model class, homogeneity, guidance/role structure) rather than relying on the paper's title-level claim; if C2A2 fails the "homogeneous, unguided" test, the assumption doesn't apply as stated regardless of the underlying literature's validity.

Search scope: Preliminary search — moderate confidence (multiple 2025-2026 arxiv papers found on both sides of the debate-vs-single-agent question; could not verify full text of the specific "Cost of Consensus" paper beyond search snippets, so scoping details are marked unverified).
