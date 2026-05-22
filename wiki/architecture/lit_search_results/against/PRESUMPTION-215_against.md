SEARCH-AGAINST-PRESUMPTION-215:
  Date searched: 2026-05-20
  Original item: PRESUMPTION-215
  Original statement: "Training-corpus is an adequate stand-in for live literature when grounding premises."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-215
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — premise grounding relies on the model's training-corpus knowledge as a stand-in for live literature search.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kandpal, N. et al. (2023). "LLMs Struggle to Learn Long-Tail Knowledge" (ICML). — Parametric recall is unreliable for long-tail facts; a training-corpus stand-in systematically fails there.
    2. Lewis, P. et al. (2020). "Retrieval-Augmented Generation" (NeurIPS). — Retrieval beats parametric recall for knowledge-intensive and changing tasks; live literature is materially better grounding.
    3. Maynez, J. et al. (2020); Ji, Z. et al. (2023). — Parametric generation produces plausible-but-fabricated citations; a training-corpus convention risks exactly the fabrication this pipeline flags elsewhere (ASSUMPTION-198).
    4. Knowledge-cutoff effect. — By construction, the training corpus cannot contain post-cutoff literature; for any recency-dependent premise it is inadequate.

  Strength of challenge: Strong

  Summary: The challenge is strong and self-applying: training-corpus grounding cannot see post-cutoff or long-tail literature and risks fabricated citations — the symmetric danger to the transcript fabrication in ASSUMPTION-198. This very pipeline run grounds its premises in training-corpus knowledge, so the presumption describes the system's own current method. It is adequate for stable, well-attested facts but inadequate as a blanket stand-in. Anchors SYSTEMIC-RISK-FLAG E and couples ASSUMPTION-199 (REVISE-035).

  Specific risks: The self-awareness register is grounded on parametric recall it cannot fully verify; fabricated citations enter premises; recency-dependent claims are mis-grounded; the system's epistemic backbone shares the failure mode it audits for.

  Mitigations available: Label citation provenance (training-corpus vs live-verified) on every result; live-verify a sample of high-stakes citations; require live search for recency-dependent or long-tail premises; reserve training-corpus grounding for well-attested foundations.

  Recommendation: CHALLENGED (REVISE)

  STEELMAN:
    Item: PRESUMPTION-215
    Strongest counterargument: A training-corpus stand-in cannot, by construction, see post-cutoff or long-tail literature and is prone to fabricating plausible citations — the same failure (ASSUMPTION-198) the pipeline exists to catch. Used as a blanket convention it grounds the system's self-knowledge on unverifiable parametric recall.
    What would need to be true for C2A2 to be safe: Safe if used only for well-attested foundations, with citation provenance labeled and high-stakes/recent citations live-verified.
    How to test: Live-verify a random sample of training-corpus citations from this register; measure the rate of unverifiable or non-existent references.
