SEARCH-AGAINST-PRESUMPTION-1201:
  Date searched: 2026-10-31
  Original item: PRESUMPTION-1201
  Original statement: "[inferred] Second firings now present themselves as verification ('I checked its work and changed none of it'; 'I checked it against the chat, found it accurate'). This presumes a second run of the sa[me process counts as independent verification]" (truncated in source)
  Claim tested (literature): N-version programming and independent-verifier literature (e.g., Knight & Leveson 1986 on correlated failures); whether re-running the same process counts as independent verification; LLM self-consistency vs self-verification limits.
  Reading used for the AGAINST direction: Evidence that a re-run of the same process (same model/prompt/inputs) is not independent verification: correlated errors defeat redundancy (Knight & Leveson), and LLM self-correction/self-verification without external feedback does not reliably find errors. Boundary conditions where a second run adds value: random/transient errors, and sampling-plus-voting (self-consistency), which helps when errors are uncorrelated across samples.
  Search scope: PRELIMINARY. 3 web searches, 0 fetches. Searched: Huang et al. self-correction; Knight & Leveson independence; Wang et al. self-consistency. Not reached: full texts (all sources are search-result titles/URLs only); LLM-as-judge self-preference bias literature; reports of self-verification success cases; same-model vs cross-model verification studies.
  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1201
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from 2026-10-30 local pass second-firing notes ("checked its work and changed none of it")
      15b: Searched for challenging literature (preliminary; 3 searches, 0 fetches)
    Current status: SEARCHED-15b — CHALLENGED
  Challenging evidence found: Yes
  Sources:
    1. Huang et al., 2023/ICLR 2024. Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 [snippet only: title/URL seen; claim that intrinsic self-correction without external feedback fails is from memory, unverified] — same-model re-review is not independent verification and may degrade answers.
    2. Tyen et al., 2023. LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/html/2311.08516v3 [snippet only: title seen] — the title itself indicates error-finding is the weak step, i.e. a second pass that "found nothing" is weak evidence of correctness.
    3. Knight & Leveson, 1986. An Experimental Evaluation of the Assumption of Independence in Multi-Version Programming. https://libraopen.lib.virginia.edu/public_view/jd472w463 (also kth.se PDF copy) [snippet only: title seen; finding that independently written versions failed coincidentally more than independence predicts is from memory, unverified] — even independently developed versions have correlated faults; a same-process re-run is more correlated still (inference).
    4. Wang et al., 2022. Self-Consistency Improves Chain of Thought Reasoning in Language Models. https://arxiv.org/pdf/2203.11171v2 [snippet only: title seen; majority-vote gains from memory, unverified] — boundary condition: multiple sampled runs plus vote can add value, but that is voting over independent samples of answers, not a single re-read that "changed none of it".
    Balance (weakens the challenge): Source 4 shows repeated runs can help when errors are random and a mechanical aggregation rule exists. Checking against an external artifact (the chat transcript) is not purely self-verification; it is a comparison with ground truth, which can catch real errors, so "checked against the chat" is stronger than a bare re-read. Sources 1-3 were not read, and none addresses this pipeline directly.
  Strength of challenge: Moderate
  Summary: The literature gives good reason to doubt that a second firing by the same model with the same context counts as independent verification: correlated errors (N-version work) and weak intrinsic self-verification (LLM self-correction work). Value is plausible only for transient errors or when the second run compares against an external, independent reference or uses a different method. The item's phrasing ("changed none of it") reports agreement, which is exactly what correlated errors predict. Evidence here is title-level only; strength is rated Moderate rather than Strong for that reason.
  Specific risks: Agreement between runs recorded as verification; shared blind spots (same model, prompt, context) pass unchallenged; "verified" label propagates downstream as if an independent check occurred.
  Mitigations available: Label second firings "re-run/consistency check" not "verification"; require an external reference (source document, test, tool output) and record what was compared; vary model/prompt/method; have the checker try to find errors against a rubric; cite checked items explicitly.
  Recommendation: CHALLENGED
  STEELMAN:
    Item: PRESUMPTION-1201
    Strongest counterargument: A second pass is often cheap, catches slips (typos, omitted items, transient generation errors), and when it compares output to the source chat it is a genuine check against ground truth rather than self-assessment. Self-consistency results show repeated sampling improves accuracy. Treating it as zero-value verification would be as wrong as treating it as full independence.
    What would need to be true for C2A2 to be safe: The second run uses information the first did not (external source, different method/model) or the failure modes of interest are random rather than systematic; and the record states what the check covered.
    How to test: Seed known errors into first-run outputs (including systematic ones the model tends to make) and measure second-run detection rate versus a different-model or tool-based checker.
  SYSTEMIC-RISK note: yes — 'a named check treated as a check performed' (the label "verified" substitutes for evidence of independent checking).
