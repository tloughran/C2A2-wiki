SEARCH-FOR-PRESUMPTION-247:

  Date searched: 2026-05-25
  Original item: PRESUMPTION-247
  Original statement: "Extracting "stated assumptions" from agent output on a no-human day presumes an agent's stated rationale == a designer-aware commitment -- blurring the ASSUMPTION (designer-aware) vs PRESUMPTION (surfaced-after-the-fact) distinction the provenance protocol exists to protect."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-247
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: original inference of unstated presumption
      15a: Searched for supporting literature (cycle 0)
    Current status: SEARCHED

  Supporting evidence found: Yes (the vulnerability is strongly supported)

  Sources:
    1. Nisbett, R. E. & Wilson, T. D. (1977). "Telling more than we can know: Verbal reports on mental processes." Psychological Review 84(3), 231-259. — Subjects confabulate reasons; reports on one's own higher-order processes are often post-hoc reconstructions, not faithful accounts. Directly undercuts treating a *stated* rationale as a window onto an actual commitment.
    2. Turpin, M., Michael, J., Perez, E. & Bowman, S. (2023). "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." NeurIPS 2023. — LLM-stated reasoning is frequently unfaithful to the actual cause of the output; training does not incentivize faithful self-report.
    3. Provenance-protocol design rationale (C2A2 internal) + epistemic-status frameworks. — The ASSUMPTION (designer-aware) vs PRESUMPTION (surfaced-after-the-fact) distinction exists precisely to mark whether a premise was a conscious commitment; equating agent-stated rationale with designer-awareness collapses that marker.

  Strength of support: Strong

  Summary: The presumption is strongly supported across two literatures. The introspection-illusion result (Nisbett & Wilson) shows even *human* stated reasons are unreliable guides to actual processes; the CoT-faithfulness result (Turpin et al.) shows the same for LLM agents specifically. Therefore extracting "stated assumptions" from agent output on a no-human day and tagging them ASSUMPTION (designer-aware) blurs exactly the distinction the provenance protocol was built to protect — an agent's stated rationale is not a designer-aware commitment.

  Caveats: Agent-stated rationale is not worthless evidence; it is defeasible. The fix is correct typing/provenance, not discarding the items.

  Recommendation: SUPPORTED
