SEARCH-AGAINST-PRESUMPTION-718:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-718
  Original statement: That the vault is a sufficient evidence base for questions about C2A2; "can't be determined from inside the vault" was treated as terminal rather than as a routing instruction, and the answer lay one call away in a session transcript — outside the producing agents' artefact set.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-718
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a stated limit treated as a stopping point rather than a handoff, then crossed it
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Observability Tells You What Happened. Evidence Proves It." (rack2cloud.com, 2026) [unverified — vendor blog, not peer-reviewed]. Argues that a critical failure state exists when a system has internal observability but no way to reconstruct authorization, provenance, or execution legitimacy from the observed artefacts alone — the bounded artefact set is necessary but not sufficient evidence.
    2. "Automated evidence collection: how it actually works and where it fails" (scrut.io, 2026) [unverified — vendor blog]. Documents that evidence-mapping frameworks systematically over- or under-state coverage when the assumed in-scope evidence population doesn't match reality — directly analogous to treating "the vault" as the complete evidence base when relevant evidence (session transcripts) lives outside it.
    3. Internal audit independence / self-assessment literature (IIA Standard 1100, theiia.org; "Internal auditor independence as a situated practice," Accounting, Auditing & Accountability Journal, Emerald, 2024). Establishes that self-contained, self-referential evidence review — auditing only what is inside the system being audited — is a recognized structural blind spot in assurance work, which is why external validation at intervals is generally required.

  Strength of challenge: Moderate

  Summary: There is a recurring theme across AI-observability critique, compliance evidence-mapping, and internal-audit theory that a bounded artefact store is routinely mistaken for the complete evidence base, and that failures concentrate exactly at that boundary. The AI-evidence sources are vendor blogs and unverified for rigor, which caps the strength of the challenge; the audit-theory sources are more solidly grounded and independently support the same structural point: self-scoped evidence review under-detects what sits just outside its own boundary.

  Specific risks: Any question routed to a vault-only search that actually requires session-transcript or other out-of-vault evidence will silently return a false negative ("can't be determined") that gets treated as a real, terminal answer rather than an incomplete search — propagating false UNTESTED or absence conclusions downstream.

  Mitigations available: Yes — treat "not determinable from the vault" as a typed routing signal (escalate to session transcripts or other external logs) rather than a terminal answer; this mirrors the standard audit-literature fix of multi-source evidence corroboration and periodic external validation.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-718
  Strongest counterargument: Self-scoped evidence review is a known structural failure mode in assurance disciplines — an evaluator that only searches its own artefact store will systematically produce false "cannot be determined" verdicts whenever the true answer lives in an adjacent, out-of-scope system (here, session transcripts), and has no built-in mechanism to notice that its own search boundary, not the absence of an answer, caused the null result.
  What would need to be true for C2A2 to be safe: Every "cannot be determined from the vault" result would need to be non-terminal by construction — automatically tagged with the searched scope and routed as a candidate for broader evidence lookup, rather than recorded as a final UNTESTED status.
  How to test: Sample past "cannot be determined from the vault" verdicts and check, using out-of-vault sources (session transcripts), how many were actually answerable; a nonzero recovery rate would empirically confirm the presumption is false.
