SEARCH-AGAINST-PRESUMPTION-918:
  Date searched: 2026-09-07
  Original item: PRESUMPTION-918
  Original statement: [inferred] A context that has lost evaluator independence can accurately assess how
    much that loss mattered; declaring a bias discharges it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-918
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-09-06 run's practice of the orchestrator writing AGAINST files after
        reading FOR files and then declaring the compromised independence (see the 15b transform line in
        PRESUMPTION-915_against.md, 2026-09-06).
      15b: Searched for challenging literature (2026-09-07) by a delegated 15b subagent (one subagent, all
        three items, AGAINST direction only; did not read any FOR file).
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Pronin, E., Lin, D.Y. & Ross, L., 2002. "The Bias Blind Spot: Perceptions of Bias in Self Versus
       Others." Personality and Social Psychology Bulletin 28(3):369–381. [VERIFIED: Sage landing page
       fetched; authors, journal, date, DOI 10.1177/0146167202286008 and abstract seen] — Three studies:
       people rate themselves less biased than peers; and, critically for this item, participants who
       showed a bias "insisted that their self-assessments were accurate and objective even after reading a
       description of how they could have been affected by the relevant bias." Knowing the bias exists does
       not produce accurate self-assessment of its magnitude.
    2. Pronin, E. & Kugler, M.B., 2007. "Valuing thoughts, ignoring behavior: The introspection illusion as
       a source of the bias blind spot." Journal of Experimental Social Psychology 43(4):565–578.
       [VERIFIED: title/venue/volume/pages/DOI via search listings; abstract from search snippet; full text
       NOT retrieved] — The blind spot arises because actors assess their own bias by introspecting on
       intentions rather than by examining behaviour, and bias does not show up in introspection. A context
       that asks itself "did reading the FOR file affect me?" is using exactly the channel that cannot
       detect the effect.
    3. Wilson, T.D. & Brekke, N., 1994. "Mental Contamination and Mental Correction: Unwanted Influences on
       Judgments and Evaluations." Psychological Bulletin 116(1):117–142. [VERIFIED: title/venue/pages and
       abstract via search and Semantic Scholar listing; full text NOT retrieved] — Correction of a
       contaminating influence requires four things to all hold: awareness of the influence, motivation to
       correct, awareness of its direction and magnitude, and the ability to adjust. People usually fail at
       the third; even when aware they are biased, they cannot correct because they do not know by how
       much. This is the direct theoretical refutation of "can accurately assess how much that loss
       mattered."
    4. Cain, D.M., Loewenstein, G. & Moore, D.A., 2005. "The Dirt on Coming Clean: Perverse Effects of
       Disclosing Conflicts of Interest." Journal of Legal Studies 34(1):1–25. [VERIFIED: University of
       Chicago Press landing page fetched; abstract, DOI 10.1086/426699 and pages seen] — Two perverse
       effects of disclosure: recipients do not discount biased advice enough even when told of the
       conflict; and disclosure increases the bias, because advisors feel "morally licensed and
       strategically encouraged" to lean further. Declaring a bias does not discharge it and can amplify
       it. (The 2025 Theory and Society paper "Why I declare a conflict of interest and you should not",
       Acem et al., appears in the Crossref citing list — title seen only, NOT verified further.)
    5. Nisbett, R.E. & Wilson, T.D., 1977. "Telling More Than We Can Know: Verbal Reports on Mental
       Processes." Psychological Review 84(3):231–259. [VERIFIED: venue/volume/pages via multiple listings
       and PDF mirrors; content from search snippet and prior knowledge; full text NOT re-read] — Reports on
       why one judged as one did are generated from a priori causal theories, not from access to the
       process. A retrospective statement of how much a prior reading influenced a later judgement is a
       theory about oneself, not an observation.
    6. Huang, J., Chen, X., Mishra, S., Zheng, H.S., Yu, A.W., Song, X. & Zhou, D., 2024. "Large Language
       Models Cannot Self-Correct Reasoning Yet." ICLR 2024; arXiv:2310.01798. [VERIFIED: arXiv PDF fetched;
       title, authors, affiliations and abstract read] — Intrinsic self-correction (no external feedback)
       fails to improve LLM reasoning and sometimes degrades it. An LLM context that has read the FOR file
       and then tries to "correct for" that reading is performing intrinsic self-correction, the setting
       the paper finds unreliable. The transfer is direct because the compromised context in the 09-06 run
       was an LLM.

  Strength of challenge: Strong

  Summary: The presumption has two halves and the literature contradicts both. On self-assessment: the
  bias blind spot (Pronin et al. 2002) shows that being told about a bias does not make self-assessment of
  it accurate; the introspection-illusion account (Pronin & Kugler 2007; Nisbett & Wilson 1977) explains
  why — the assessment is made by introspection, and bias is invisible to introspection. Wilson & Brekke
  (1994) make the point structurally: correction requires knowing the direction and magnitude of the
  contamination, which is precisely what the contaminated judge lacks. On disclosure: Cain, Loewenstein &
  Moore (2005) show that declaring a conflict does not discharge it, is under-discounted by readers, and
  licenses the discloser to lean further. Huang et al. (2024) close the loop for the LLM case: a model
  reviewing its own output without external signal does not reliably fix it. Together these say the
  09-06 practice ("read FOR, write AGAINST, declare it") produced a file whose independence was
  compromised by an unknown amount that the writer was not in a position to estimate, and whose
  declaration may have made readers (14b reconciliation) trust it more than warranted.

  Specific risks: (a) The reconciliation rule (15a supports + 15b finds weak challenges → SUPPORTED,
  moderate confidence) is applied to an AGAINST file that was anchored on the FOR file; the "weak
  challenge" may be an artefact of anchoring, and the item is promoted on the strength of a search that
  was not independent. (b) The declaration in the transform line is read by 14b/14a as a discount
  instruction, but Cain et al. predict under-discounting; the file is treated as ~90% of an independent
  file when it may be ~50%. (c) Moral licensing: a context that has declared compromise may, per Cain et
  al., feel freer to lean on the FOR file's framing, since it has "come clean". (d) The practice, once
  accepted, becomes a template: any future breach of 15a/15b separation is cured by a sentence, and the
  design's only anti-confirmation-bias mechanism becomes optional.

  Mitigations available: Do not ask the compromised context to estimate its own contamination; the
  literature's answer is procedural, not introspective. Options: (1) re-run the search in a fresh context
  that has not seen the FOR file and diff the two AGAINST files — the diff is the empirical measure of how
  much the loss mattered, replacing self-report; (2) reconciliation treats a declared-compromised AGAINST
  file as absent (status UNTESTED for 15b) rather than as discounted; (3) require that the declaration be
  accompanied by the specific FOR sources seen, so a later auditor can check for anchoring (shared
  sources, mirrored framing); (4) structural: the orchestrator never writes AGAINST files; if the subagent
  fails, the item stays queued.

  Search scope: Preliminary — 6 queries, all suggested lines run. Covered: bias blind spot, introspection
  illusion, mental contamination/correction, disclosure and moral licensing, introspection limits, LLM
  intrinsic self-correction. Not covered: the "debiasing works when procedural" literature (Larrick 2004;
  Lilienfeld et al. 2009), which would support the mitigation rather than the presumption; the
  contamination literature on judicial "disregard the evidence" instructions (Steblay et al. 2006
  meta-analysis), which would strengthen the challenge; and newer LLM self-evaluation work post-2024
  that may report partial successes under specific conditions. The direction of the uncovered literature
  is mostly toward the challenge, not away from it.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-918
  Strongest counterargument: The ability to say "I was compromised" and the ability to say "by this much"
  are different capacities, and the second is exactly what a compromised judge lacks. Wilson & Brekke's
  model requires knowledge of the contamination's magnitude for correction; Pronin's work shows that
  self-assessment of bias proceeds by introspection, which cannot see the bias, so that even a judge who
  has just been told about the bias insists their own judgement is clean. Disclosure then compounds the
  problem: readers under-discount disclosed bias, and disclosers lean further because they have been
  honest. For an LLM context, Huang et al. add that self-review without an external signal does not
  reliably repair the output. The 09-06 declaration is therefore not a measurement and not a cure; it is
  a plausible-sounding self-theory attached to a file whose actual independence is unknown, and the
  system's reconciliation logic has no way to price that.
  What would need to be true for C2A2 to be safe: There is an external, non-introspective measure of the
  contamination (a fresh-context re-run and diff), and the reconciliation step consumes that measure
  rather than the declaration; or declared-compromised files are excluded from reconciliation entirely.
  How to test: For PRESUMPTION-915 (the 09-06 case), launch a fresh 15b subagent that has not seen the FOR
  file and have it write an independent AGAINST file. Compare: source overlap with the FOR file, strength
  rating, and whether the same "other half" of a FOR source is cited. If the fresh file diverges
  materially (different strength, different sources, no mirrored framing), the declaration under-priced
  the loss and the presumption fails on C2A2's own data.
