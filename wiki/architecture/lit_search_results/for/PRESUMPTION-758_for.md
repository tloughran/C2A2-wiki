SEARCH-FOR-PRESUMPTION-758:
  Date searched: 2026-08-18
  Original item: PRESUMPTION-758
  Original statement: Whether an unbounded exception clause defeats a recall window. Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-758
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from operational review; queued as literature-testable.
      15a: Searched for supporting literature; found strong support for the general principle in legal doctrine and control-assurance practice, but no source addressing the information-retrieval formulation the item states.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Logan, Wayne A., 2001. "An Exception Swallows a Rule: Police Authority to Search Incident to Arrest." Yale Law & Policy Review, vol. 19 (2001). [Page range reported inconsistently across indexes — FSU College of Law repository record ir.law.fsu.edu/articles/195 confirms title, author and venue; page cited variously as 281 and 381.] — The canonical treatment of the structure the item names: an exception drawn without a limiting principle expands until the residual scope of the rule is whatever the exception does not reach, at which point the rule no longer constrains.
    2. Johnson v. United States, 576 U.S. 591 (2015) (U.S. Supreme Court). [Verified via Congressional Research Service product IF13091 and Cornell LII Constitution Annotated.] — Struck the Armed Career Criminal Act's residual clause as void for vagueness, holding it created "grave uncertainty" about scope and offered "no reliable way" to determine what fell within it; the Court treated nine years of failed attempts to fix a consistent standard as itself evidence that the clause was indeterminate. Directly supports the claim that an open-ended residual provision destroys the definiteness of the boundary it sits inside.
    3. "Policy Exception Rate" (company-analysis guide, Umbrex, Risk Management & Internal Audit series). [Practitioner/grey literature — no named author; cited as evidence of professional practice, not as research.] — Treats the rate at which exceptions are granted as a first-class indicator of whether a control is real, on the reasoning that a high exception rate means compliance risk is accumulating behind a nominally-satisfied policy.

  Strength of support: Moderate

  Summary: The general principle is well-supported and long-established outside the item's own domain. Logan (2001) named the failure mode — an exception without a limiting principle inverts the rule/exception relation until the rule's operative scope is merely the exception's complement — and Johnson (2015) is a binding judicial holding that an open-ended residual clause is not merely weak but void for indefiniteness, with the court explicitly rejecting the argument that clarity in *some* applications rescues the provision. That last point maps closely onto the item: a recall window that is clear in most cases is not thereby saved if the exception clause has no stated bound. Control-assurance practice supplies the operational counterpart, treating exception rate as the measure of whether a stated control binds at all. What I did not find is any source in information retrieval that studies a temporal recall window paired with an unbounded override; the temporal-IR literature located treats time-windowed retrieval as an efficiency device whose recall cost depends on whether relevance is actually recency-biased, which is a related but distinct concern.

  Caveats: The support is analogical, and the analogy is load-bearing. Legal vagueness doctrine turns on notice to a regulated party and on judicial administrability, neither of which applies to an automated recall filter; the conclusion transfers as a structural argument about scope, not as evidence about retrieval behaviour. Source 3 is practitioner material with no named author and no empirical basis, and should carry little weight. No source quantifies the effect — i.e. none tells you how large the exception's actual usage must be before the window stops constraining, which is the question an operator would need answered. The item's specific IR formulation appears to be un-attested rather than refuted.

  Search scope: exception clause swallows the rule; residual clause vagueness and legal certainty; catch-all and open-ended provisions; policy exception and override rates in internal audit; management override of internal controls; temporal information retrieval and recall horizons; time-boxed retrieval and recency bias; defeasible scope parsing of deontic rules. Preliminary — broader search recommended on the IR arm specifically (suggested terms not yet tried: filter bypass rate, selective-predicate pushdown recall loss, human-in-the-loop override in screening cascades).

  Recommendation: PARTIALLY-SUPPORTED

  NOVELTY-FLAG:
    Item: PRESUMPTION-758
    Searched: Legal doctrine on exceptions and residual clauses; internal-audit exception/override literature; temporal information retrieval and recall windows.
    Finding: The structural claim — that an unbounded exception collapses the scope of the rule containing it — is thoroughly established in law and reflected in control-assurance practice. The item's own formulation, which applies that structure to a *recall window in a retrieval or review pipeline*, returned no matching source. Temporal IR studies recall loss from windowing, but as a recency-bias/efficiency tradeoff, with no treatment of an override clause as the mechanism of defeat.
    Implication: The principle can be imported with reasonable confidence, but the domain-specific version is unsupported by direct evidence and should not be presented as an established retrieval result. If C2A2 relies on it operationally, the cheap test is internal: measure what fraction of items actually enter via the exception rather than the window.
    Recommended status: NOVEL (in formulation; not in underlying principle)
