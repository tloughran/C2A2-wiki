SEARCH-FOR-PRESUMPTION-718:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-718
  Original statement: That the vault is a sufficient evidence base for questions about C2A2; "can't be determined from inside the vault" was treated as terminal rather than as a routing instruction, and the answer lay one call away in a session transcript — outside the producing agents' artefact set.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-718
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a stated limit treated as a stopping point rather than a handoff, then crossed it
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. AICPA/PCAOB scope-limitation doctrine, summarized in "Scope Limitation" (AccountingTools; Wikipedia; AU-C Section 705 under GAAS/ISA 705) — establishes formally that when an auditor cannot obtain sufficient appropriate evidence from the engagement's defined scope, the correct response is not silent acceptance but an explicit qualified opinion, disclaimer, or scope expansion — i.e., "insufficient evidence within scope" is treated procedurally as an escalation trigger, not a terminal answer. Directly analogous in structure (though not domain) to treating "can't be determined from inside the vault" as a stop rather than a routing instruction.
    2. Recent LLM/RAG knowledge-boundary literature, e.g. "Enhancing LLM Reliability via Explicit Knowledge Boundary Modeling" (arXiv:2503.02233) and "Do Retrieval Augmented Language Models Know When They Don't Know?" (arXiv:2509.01476) — [unverified — from search snippet] frame "knowing what you don't know" and the choice between refusal and escalation to a broader knowledge/retrieval source as a live, named research problem; both sources note that refusal (treating an internal-knowledge gap as terminal) trades away helpfulness that could be recovered by escalating to external retrieval — structurally the same trade-off 14b flags for the vault-vs-transcript case.
    3. Root-cause-analysis literature on investigation-scope traps (Baker Hughes "Avoid the biggest failures in root cause analysis"; ECRI/ISMP "Getting the Most out of Root-Cause Analyses") — [unverified — from search snippet] documents that RCA commonly fails via "stopping at the first plausible cause" or artificially bounding the investigation to available records, and identifies "restricted access to historical data" as a named, recurring driver of incomplete investigations — supporting the general pattern that an artefact-bounded evidence set is a known trap across investigative disciplines, not a C2A2-specific quirk.

  Strength of support: Moderate

  Summary: No literature was found that addresses this exact scenario (a self-auditing multi-agent documentation system with a vault as its bounded evidence base). However, three adjacent, well-established bodies of work — audit scope-limitation doctrine, LLM knowledge-boundary/refusal-vs-retrieval research, and root-cause-analysis investigation-scope failure patterns — all converge on the same structural point: treating "insufficient evidence within the defined artefact set" as terminal (rather than as a signal to escalate/expand scope) is a recognized failure mode across very different fields, each with established countermeasures (qualified opinions, escalation-to-retrieval policies, deliberately widening RCA data sources). This gives reasonable theoretical grounding for the presumption's core claim, by analogy rather than direct precedent.

  Caveats: All three source bodies are analogical, not domain-matched — none discuss a vault-as-artefact-set for an LLM multi-agent architecture record specifically. The audit-scope-limitation analogy is procedural/institutional (external auditors have formal escalation paths mandated by standards); C2A2's agents may not have an equivalent formalized escalation protocol, which is arguably the actual gap 14b is pointing at. The RAG/knowledge-boundary papers are for single-model question answering, not multi-agent systems with separable artefact stores (vault vs. session transcripts) — the transfer from "internal parametric knowledge vs. external retrieval" to "vault vs. session transcript" is a reasonable but unverified structural mapping.

  Recommendation: PARTIALLY-SUPPORTED
