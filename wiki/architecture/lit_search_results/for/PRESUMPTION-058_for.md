SEARCH-FOR-PRESUMPTION-058:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-058
  Original statement: "Splitting the Levin+Friston joint entry without reviewing its original rationale is correct"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-058
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Levin Agent Template deliverable committing to split without reviewing prior rationale
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Single-responsibility / single-purpose agent literature (Weng 2023 "LLM Powered Autonomous Agents"; Park et al. 2023 "Generative Agents"): single-focus agents typically produce tighter outputs than multi-focus agents; taken at face value, splitting a joint agent into two single-tradition agents is consistent with this principle.
    2. Modularity in agent-framework design (LangChain / LangGraph agent composition 2024-2026): decomposition of complex agents into specialized sub-agents is a common pattern.

  Strength of support: Weak (and indirect)

  Summary: Literature supports single-purpose agents in general, which provides indirect support for splitting as a reasonable default. However, the PRESUMPTION is not "splitting is correct" — it is "splitting WITHOUT REVIEWING the original rationale is correct." No literature supports reversing a prior decision without reviewing its motivation; indeed, decision-archaeology / ADR (Architecture Decision Record) literature (Nygard 2011; ThoughtWorks 2014-2024) explicitly recommends reading prior decisions before reversing them. The absence of that review is the item's vulnerability, and no literature supports skipping it.

  Caveats: (a) If the original rationale is retrievable and simply was not consulted, this is a process gap, not a design flaw; (b) if the joint entry was motivated by cross-tradition-signal capture (Levin developmental bioelectricity ↔ Friston free-energy principle), splitting could lose the corridor that motivated the pairing — this is a risk dimension literature would tell us to check; (c) the decision is reversible if it turns out to be wrong, reducing stakes.

  Recommendation: NO-SUPPORT-FOUND (no literature supports skipping rationale-review when reversing a prior decision; weak indirect support for the split itself does not address the methodological gap the presumption surfaces)
