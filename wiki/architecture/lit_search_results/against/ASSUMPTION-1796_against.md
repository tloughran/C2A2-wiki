SEARCH-AGAINST-ASSUMPTION-1796:
  Date searched: 2026-10-14
  Original item: ASSUMPTION-1796
  Original statement: [stated] Lit pipeline hypothesis over the 10-12 intake: "five of the six items share one weakness: each proposed fix replaces a failed proxy with another proxy that nobody checks against reality." Implied claim under test: substituting one monitoring proxy for another, without a ground-truth audit, relocates error rather than reducing it.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1796
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-10-13 transcripts (final 4 messages per session, read via subagents) and, where marked, from wiki artifacts.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Buyse M, Molenberghs G, Burzykowski T, Renard D, Geys H, 2000. "The validation of surrogate endpoints in meta-analyses of randomized experiments." Biostatistics. — Establishes that a proxy can be validated at the trial level (treatment effect on surrogate predicts effect on true endpoint across trials). Challenges the blanket form of the claim: proxy substitution is not inherently error-relocating if the new proxy has been validated once against outcomes; thereafter it can be used without a fresh ground-truth audit per use. [Level: search-snippet only; citation details confirmed in snippets, not read in full.]
    2. U.S. regulatory overview of validated surrogate endpoints (NCBI Bookshelf NBK453484, BEST/FDA-NIH resource, as summarised in search results). — Lists HIV-RNA, blood pressure, LDL-C and HbA1c as validated surrogates used for approval "without the need for additional studies to demonstrate the clinical benefit directly." Empirical counterexample: some proxies, once validated, reduce error durably. [Level: search-snippet only; exact page title not verified.]
    3. Landau-style redundancy / defence-in-depth reasoning, via Reason J, 2000. "Human error: models and management." BMJ (Swiss cheese model). — Layered imperfect defences reduce the probability of a failure passing all layers, even when no layer is ground-truth. Challenges the idea that adding a second proxy only relocates error; if holes are not aligned, stacking proxies reduces joint miss rate. [Level: snippet only; model widely known.]
    4. Manheim D, Garrabrant S, 2018. "Categorizing Variants of Goodhart's Law." arXiv:1803.04585. — Distinguishes regressional, extremal, causal and adversarial Goodhart (categories recalled, not verified in retrieved text). Boundary condition: proxy failure severity scales with optimization pressure on the proxy; a monitoring proxy that is observed but not optimized against is largely subject only to regressional error, which shrinks, not relocates, with additional independent proxies. [Level: abstract/snippet only; four-category list unverified in this run.]
    5. (Counter-challenge, reported for honesty) Knight JC, Leveson NG, 1986. "An Experimental Evaluation of the Assumption of Independence in Multiversion Programming." IEEE TSE 12(1):96-109. — 27 independently written versions showed coincident failures far above independence. This limits sources 3-4: independent-looking proxies often fail together, so layering yields less error reduction than naive multiplication predicts. [Level: snippet only.]
    6. (Counter-challenge) Fleming TR, DeMets DL, 1996. "Surrogate end points in clinical trials: are we being misled?" Ann Intern Med. — Many surrogates failed to predict clinical effects; validation is context-specific. [Level: snippet only.]

  Strength of challenge: Moderate

  Summary: The literature does not support the strong, general form of the claim ("each proxy replacement merely relocates error"). Surrogate-endpoint methodology shows proxies can be validated once and then reliably used without per-instance ground-truth checks, and defence-in-depth theory shows that stacking imperfect checks reduces joint miss probability when failures are not perfectly correlated. However, both challenges carry their own boundary conditions that cut back toward the original claim: validation requires at least one ground-truth calibration (which the 10-12 fixes reportedly lack), and Knight & Leveson show that "independent" checks frequently share failure modes. The defensible position is narrower: an UNVALIDATED replacement proxy, correlated with the one it replaces, relocates error; a validated or genuinely independent one reduces it. A further philosophical challenge (no "reality" check is itself proxy-free; any audit is a higher-fidelity proxy) was not searched to completion and is noted as untested.

  Specific risks: If the assumption is over-applied, C2A2 may reject cheap, adequate layered monitors in favour of costly "ground-truth audits" that are themselves proxies (e.g., one human spot-check), and may stall fixes awaiting an audit capacity that does not exist. Conversely, if the narrower form is ignored, correlated proxies (same data source, same agent family) will give false comfort.

  Mitigations available: One-time calibration of each new proxy against a small ground-truth sample (surrogate-validation logic); deliberate diversity of proxy data sources to reduce common-mode failure; tracking proxy-to-outcome agreement over time rather than per-fix audits.

  Recommendation: PARTIALLY-CHALLENGED

  Search scope: preliminary search — 5 web searches, 0 page fetches; all sources at snippet/abstract level. Broader search recommended on (a) ensemble/independent indicator performance in software monitoring and (b) epistemology of "ground truth" as proxy.

STEELMAN:
  Item: ASSUMPTION-1796
  Strongest counterargument: Every check on reality is itself a proxy; "ground truth" is just the proxy you have decided to trust. Medicine has run on validated surrogates (blood pressure, LDL, viral load) for decades with enormous net benefit, and safety engineering routinely achieves high reliability by stacking imperfect, individually unaudited barriers. What matters is not whether a proxy is checked against reality each time but whether its error is (a) characterised once and (b) not perfectly correlated with the other proxies in the stack. A fix that swaps one proxy for a different, partially independent proxy therefore usually reduces net error, even unaudited — so a blanket "it only relocates error" verdict would wrongly discard real improvements.
  What would need to be true for C2A2 to be safe: The replacement proxies draw on different signals/failure domains than the proxies they replace; at least one historical case exists where each proxy's output was compared with an independently observed outcome; proxies are monitored, not optimized against (low Goodhart pressure).
  How to test: For each of the five 10-12 fixes, record whether the new proxy reads a different data source than the old one; take a small sample (n~10-20) of past known failures and check whether old proxy, new proxy, both, or neither would have caught each — the joint miss rate versus single miss rate directly measures "reduce vs relocate."
