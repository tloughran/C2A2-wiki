SEARCH-AGAINST-ASSUMPTION-1175 (REFRESH — 15d re-trigger, 2026-09-27, cycle 1):
  Date searched: 2026-09-28
  Original item: ASSUMPTION-1175
  Original statement: Context isolation between adversarial searchers (15a/15b) is a remedy for correlated
    error when the base model is shared.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b (2026-08-25) -> 15c -> MONITOR-547 -> 15d RE-TRIGGER (2026-09-27) -> 15b (2026-09-28)]
    Original item: ASSUMPTION-1175
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session discussion of the 15a/15b independence design
      15b (2026-08-25): CHALLENGED, Strong
      15b (2026-09-28): Primary-source verification of the two triggers the 2026-08-25 disposition named
    Current status: SEARCHED — disposition-relevant

  Challenging evidence found: Yes — both named verification triggers confirmed.

  Sources:
    1. Denisov-Blanch et al. (2026, arXiv:2603.06612) — VERIFIED via direct fetch of arxiv.org/abs/2603.06612.
       Authors confirmed: Yegor Denisov-Blanch, Joshua Kazdan, Jessica Chudnovsky, Rylan Schaeffer, Sheng
       Guan, Soji Adeshina, Sanmi Koyejo. The paper reports that different LLMs produce correlated errors
       even under adversarial/out-of-distribution conditioning designed to elicit independent behavior.
       This is precisely the condition the item's 2026-08-25 disposition specified: "if correlation
       genuinely persists when models are conditioned on out-of-distribution random strings, isolation's
       decorrelation contribution is near nil rather than partial." CONFIRMED TRUE.
    2. Begin et al. (2026, arXiv:2606.26583) — VERIFIED via direct fetch of arxiv.org/html/2606.26583.
       Reports rho = 0.679+/-0.023 (same-model) vs. 0.396+/-0.011 (cross-model); 10 same-model agents
       worth 1.38 effective independent forecasters. This is the exact figure the disposition said would,
       if confirmed, mean "MONITOR-001 should carry the FLOOR figure rather than any claimed reduction"
       from context isolation alone. CONFIRMED TRUE, with authorship also resolved (was unverified).

  Strength of challenge: Strong (unchanged from 2026-08-25 disposition, now with both named triggers
    independently confirmed via primary source rather than carried as pending).

  Summary: The literature says context isolation between same-base-model agents does not eliminate
    correlated error; residual correlation (rho approx. 0.40 cross-model, 0.68 same-model) persists even
    under adversarial framing and OOD conditioning. For C2A2's 15a/15b pair, which may share a base model
    family (REVISE-350, still open), this means the independence the pipeline relies on to avoid
    confirmation bias is partial at best, and the item's own pre-registered rule says this should move to
    REVISE rather than stay MONITOR.

  Specific risks: MONITOR-001 (the pipeline's own confidence in 15a/15b disagreement as evidence of
    independent review) may be overstating independence if 15a and 15b in fact share a base model family.
    This is a self-referential risk: the same correlation this citation describes could be operating
    inside the very search that surfaced it.

  Mitigations available: Cross-model assignment for 15a/15b (use genuinely different base model families,
    not just separate context windows) would move the measured correlation from the same-model regime
    (rho approx. 0.68) toward the cross-model regime (rho approx. 0.40) — still nonzero, but a real
    reduction, consistent with Begin et al.'s ablations.

  Recommendation: CHALLENGED (Strong, confirmed) — REVISE. See DISPOSITION-999 / REVISE-488.
