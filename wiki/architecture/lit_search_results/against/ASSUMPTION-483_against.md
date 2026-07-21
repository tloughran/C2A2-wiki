SEARCH-AGAINST-ASSUMPTION-483:
  Date searched: 2026-07-21
  Original item: ASSUMPTION-483
  Original statement: The read channel is not the dominant correlation source between 15a and 15b; the 2026-07-19 change removed the weakest of at least four. Relabel as "read-channel independence enforced"; do not re-run the 905-pair record.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-483
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from REVISE-233 adjudication block
      15b: Searched for challenging literature (blinding trials, correlated LLM judge errors, shared-pretraining entanglement)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Search scope: Moderate — two clusters, one on the empirical size of blinding effects, one on measured correlation in LLM judge panels. Searched for evidence that the read channel IS dominant; found none, and found instead evidence that sharpens the second half of the item against the first.

  Sources:
    1. van Rooyen, Godlee, Evans, Smith and Black, 1998. "Effect of Blinding and Unmasking on the Quality of Peer Review: A Randomized Trial." JAMA 280(3):234–237. PMID 9676666. 527 consecutive BMJ manuscripts, each sent to two reviewers; review quality 2.82 masked vs 2.96 unmasked, 2.87 blinded vs 2.90 unblinded; blinding and unmasking made no editorially significant difference to quality, recommendation, or time taken. Supports the item's claim that removing the read channel is a small intervention.
    2. "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels." arXiv:2605.29800 (retrieved 2026-07-21). Roughly three quarters of a panel's nominal independence is lost to shared error; actual panel accuracy falls 8–22 percentage points short of the independent-voting expectation. Challenges the item's remedy: if the surviving correlation is that large, "relabel and proceed" leaves the 905-pair record standing on a measured, quantified deficit rather than an unquantified one.
    3. "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles." arXiv:2604.07650 (retrieved 2026-07-21). Where models share training lineage or alignment signal, agreement reflects correlated failure rather than independent verification; proposes auditing entanglement and reweighting rather than assuming independence. Directly relevant because 15a and 15b share model, prompt lineage, corpus and search tool.
    4. "A Systematic Methodology for Evaluating Failure Independence in LLM-Generated Code." arXiv:2607.02808 (retrieved 2026-07-21). Same-model outputs are more correlated in failure than cross-model ensembles, and heterogeneous ensembles yield only limited improvement — so the obvious mitigation (run 15b on a different model) is a partial fix at best.

  Strength of challenge: Moderate
  Summary: The claim itself survives: nothing retrieved suggests the read channel was the dominant correlation source, and van Rooyen's randomised trial — the closest empirical analogue, run on human reviewers with far stronger incentives to be swayed than an agent reading a file — found the blinding effect near zero. So "weakest of at least four" is well supported and the proposed relabel is the honest wording. The challenge lands on the second half. If the read channel was the weakest of four, three stronger channels remain, and the LLM-judge literature now puts numbers on what they cost: roughly three quarters of nominal independence, 8–22 points of accuracy. "Do not re-run the 905-pair record" is defensible as a use-of-resources decision but is not licensed by the finding — the finding says the record is more compromised than the blinding fix addresses, not less. The item reads as reassurance where the literature supports a quantified discount.
  Specific risks: The relabel is adopted, the record is left standing, and "read-channel independence enforced" is read downstream as "15a/15b are independent." Every subsequent argument that cites 15a/15b agreement as corroboration then inherits an unpriced correlation of roughly the size the panel literature measures.
  Mitigations available: Adopt the relabel and pair it with a standing numeric caveat: agreement between 15a and 15b is worth substantially less than two independent observations, with the panel literature's 8–22 point figure cited as an order-of-magnitude anchor. Run the item's own test — 15a/15b source-citation overlap under full blocking — which measures the surviving correlation directly and costs one item. Do not re-run 905 pairs; the confound (blinding varies with model version, prompt and corpus) makes the delta uninterpretable anyway.
  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-483
    Strongest counterargument: The item is right about the read channel and draws the wrong operational conclusion from being right. If the removed channel was the weakest of four, the correct inference is that the record is worse off than anyone had priced, not that it can be left alone. The LLM evaluation-panel literature has now measured what the remaining channels cost: a nine-judge panel retains about two effective votes, and panel accuracy falls 8–22 points below the independent-voting expectation, because models sharing training lineage make the same mistakes on the same items. 15a and 15b share more than lineage — they share model, prompt ancestry, corpus and search tool — which is the high end of the entanglement range, not the low end. So "do not re-run" is a reasonable budget decision and an unreasonable epistemic one, and the danger is that the relabel makes the compromise sound resolved. The honest position is that read-channel independence is enforced, total independence is low and now roughly quantifiable, and every downstream use of 15a/15b concordance should carry that discount explicitly.
    What would need to be true for C2A2 to be safe: That 15a/15b agreement is never cited as independent corroboration anywhere downstream without a stated discount. Given that the pipeline's confidence upgrades appear to run on exactly such concordance, this condition is unlikely to hold by default.
    How to test: Run the item's own in-house test — one item, both agents under full blocking, measure source-citation overlap. Overlap above roughly 50% establishes that shared corpus and search tool, not the read channel, carry the correlation, and gives a house number to attach to the caveat.
