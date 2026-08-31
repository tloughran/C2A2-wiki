SEARCH-FOR-PRESUMPTION-894:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-894
  Original statement: [inferred] In-session memory is treated as an independent copy (i.e. an agent's own
    recollection of what it did is treated as corroborating evidence of what it did).
  Generalizable limb searched: Is an actor's own recollection of its own actions admissible as *independent*
    corroboration of those actions? Two sub-limbs: (a) the human cognitive-psychology limb — is recall
    reconstructive and confabulation-prone; (b) the assurance limb — do audit standards exclude self-generated
    evidence from counting as corroboration. Third sub-limb added in Pass 2: (c) does the same hold for LLM agents
    specifically.
  DIRECTION NOTE: the item is a presumption filed as unsafe. "Support" means literature supporting 14b's finding
    that self-recollection is not an independent copy.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. Unusually strong source
    base for a snippet-level search — the assurance limb rests on primary standards text (PCAOB AS 1105, AS 2310)
    and the cognitive limb on a century-old, heavily replicated literature.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-894
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the incident handling — the register's post-incident state was reconciled against what the
           acting agent recalled doing, with that recollection counted as a second source rather than as the same
           source restated.
      15a: Searched for supporting literature (2026-08-31)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. PCAOB, AS 1105: Audit Evidence (current standard; supersedes Auditing Standard No. 15). pcaobus.org —
       Snippet: "Evidence obtained from a knowledgeable source that is independent of the company is more reliable
       than evidence obtained only from internal company sources." Primary standards text; directly on the
       independence question.
    2. European Court of Auditors, "Audit evidence." ECA AWARE methodology portal (methodology.eca.europa.eu) —
       Snippet: evidence from interviews needs corroboration from other sources; is more reliable when obtained
       directly by the auditor rather than indirectly, and from independent sources outside the entity rather than
       generated within the auditee organisation. A second, institutionally independent standards body stating the
       same rule.
    3. PCAOB, AS 2310: The Auditor's Use of Confirmation. pcaobus.org — The existence of a dedicated standard
       requiring third-party confirmation is structural evidence that internally-generated assertions are not
       self-sufficient. Snippet-level; I did not read the standard.
    4. Accounting Today, undated (opinion). "AI cannot audit itself, and the profession knows why." — Snippet
       carries the argument in its sharpest form: "Management's representation of its own reliability is not
       sufficient evidentiary ground for professional reliance," and when management says controls are effective
       and every document reviewed was prepared under those same controls, "that is not corroboration." Opinion
       piece, not standards text, but it states the item's exact structure and applies it to AI.
    5. "Reconstructive memory" and "Confabulation," Wikipedia (accessed 2026-08-31), plus ScienceDirect Topics
       overview "Reconstructive Memory" — Recall is a reconstruction influenced by perception, imagination,
       motivation, semantic memory and beliefs; gaps are filled with plausible material without intent to deceive;
       people nonetheless experience their memories as coherent and error-free. Tertiary sources summarising a
       primary literature (Bartlett; Loftus) that I did not read directly.
    6. PMC11332036 (2024). "A reduction in self-reported confidence accompanies the recall of memories distorted by
       prototypes." — Peer-reviewed; relevant because it addresses the confidence/accuracy relationship, i.e.
       whether the rememberer can tell. Snippet-level only; I did not read the abstract in full and note that its
       finding (confidence *does* drop) is a partial qualifier rather than pure support.
    7. "Can LLMs Introspect? A Reality Check." arXiv:2605.26242 — Snippet: genuine introspection cannot be
       distinguished from confabulation through conversation alone; behavioural evidence alone is inherently
       insufficient to establish introspective claims. Directly on the agent-specific limb. Unverified preprint;
       snippet only.
    8. "LLM Self-Explanations Fail Semantic Invariance." arXiv:2603.01254 — Snippet: all four tested frontier models
       fail semantic invariance tests, with self-reports shifting with semantic expectations rather than tracking
       task state. If self-reports track expectation rather than state, they cannot corroborate state. Unverified
       preprint; snippet only.
    9. Anthropic, 2025. "Emergent Introspective Awareness in Large Language Models." transformer-circuits.pub —
       Found in results and noted for completeness because it argues for *some* introspective capacity; I did not
       read it and flag it as the strongest available counterweight rather than as support.

  Strength of support: Strong

  Summary: Three independent literatures converge on the item's finding. Audit standards state the rule directly:
  evidence from a source independent of the entity is more reliable than internally-generated evidence, interview
  evidence requires corroboration from elsewhere, and a representation about one's own reliability is not
  evidentiary ground for relying on it. Cognitive psychology supplies the mechanism for why the recollection is not
  merely weaker but actively unreliable — recall is reconstructive, gaps are filled with contextually plausible
  material, and the resulting account is experienced by the rememberer as a faithful record. The agent-specific
  literature closes the transfer gap: recent preprints report that model self-reports shift with semantic framing
  rather than tracking task state, and that introspection cannot be separated from confabulation on behavioural
  evidence alone. Taken together these support the item strongly. The independence failure is structural, not a
  question of the agent's honesty: a recollection produced by the same process that produced the action is one
  source counted twice, and no amount of good faith converts it into two.

  Caveats: (i) Anthropic's "Emergent Introspective Awareness" work argues for some genuine introspective capacity
  and is a real counterweight I did not read; the support here should not be read as "agent self-report is
  worthless," only as "it does not constitute an independent copy." (ii) Audit standards govern reliance for
  opinion purposes, not all reasoning — a self-report may still be a useful lead, hypothesis, or tie-breaker where
  no reliance is placed on it. (iii) The cognitive-psychology limb is human; transfer to an LLM agent is by
  analogy, and the analogy is imperfect in both directions (context-window loss is not decay-plus-reconstruction).
  (iv) The two arXiv preprints (2605.26242, 2603.01254) were seen only as snippets and I could not verify their
  provenance or review status.

  Recommendation: SUPPORTED
