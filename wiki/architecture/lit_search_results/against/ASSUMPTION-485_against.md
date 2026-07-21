SEARCH-AGAINST-ASSUMPTION-485:
  Date searched: 2026-07-21
  Original item: ASSUMPTION-485
  Original statement: Replacing a possibly-wrong objective with an unmeasurable one converts it into no objective; do not remove convergence from Rung-2 scoring before a separable alternative exists.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-485
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from REVISE-235
      15b: Searched for challenging literature (McNamara fallacy, ITT validity, unmeasurable objectives)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Search scope: Moderate — two clusters: the named fallacy covering the item's exact inference, and the validity literature on the instrument the item proposes as replacement.

  Sources:
    1. The McNamara fallacy, as documented in Wikipedia "McNamara fallacy" and Yankelovich's original formulation (retrieved 2026-07-21). The fallacy's canonical four-step progression is: measure what is measurable; assign arbitrary values to or disregard what is not; presume what cannot be measured is unimportant; conclude that what cannot be measured does not exist. The item's inference — unmeasurable therefore not an objective — is step three stated as a principle. This is a direct hit on the claim's logical form, not merely an analogy.
    2. Sørensen and colleagues, "Evaluation of Digitalisation in Healthcare and the Quantification of the 'Unmeasurable'." Journal of General Internal Medicine, doi 10.1007/s11606-023-08405-y (retrieved 2026-07-21). Measurement becomes counterproductive when applied to what resists quantification; the recommended response is mixed qualitative and quantitative assessment, not retention of a defective quantitative measure until a quantitative replacement appears.
    3. Brand, Stafford and colleagues, 2025. "The Ideological Turing Test: A Behavioral Measure of Open-Mindedness and Perspective-Taking." Cognitive Science, doi 10.1111/cogs.70126 (also PMC12519043). Establishes ITT as a usable behavioural measure — supporting the item's proposed alternative — but the retrieved discussion also documents its limits: no normative ground truth (imitative equivalence is not insight), sensitivity to prompt interpretation, temporal validity problems as attitudes shift across samples and time, and, for model-generated arguments, artifacts of regularisation producing excess coherence. The proposed separable alternative is therefore not a clean instrument either.

  Strength of challenge: Moderate
  Summary: The practical counsel — do not delete a scoring dimension before its replacement exists — is prudent and I found nothing contradicting it. The stated principle underneath it is another matter: "unmeasurable therefore no objective" is a textbook statement of the McNamara fallacy, the specific error of concluding that what resists measurement is unimportant or non-existent. The healthcare-evaluation literature gives the constructive alternative: where quantification is inappropriate, the answer is mixed assessment, not the retention of a defective quantitative proxy pending a quantitative substitute. And the item's own proposed replacement instrument is not the clean escape it appears to be — the ITT paper that establishes it also documents that it has no normative ground truth, that imitative equivalence is not comprehension, and that it is prompt-sensitive and temporally unstable. Keeping convergence in place while the ITT baseline is built is defensible; asserting that an unmeasurable objective is no objective is not.
  Specific risks: If the principle is adopted as stated, C2A2 acquires a standing rule that systematically retains measurable-but-wrong objectives over unmeasurable-but-right ones — which is precisely the failure mode PRESUMPTION-509 flags in the same batch, arriving through a different door. Second risk: the ITT is adopted as the separable alternative without its documented validity limits, and a measure with no ground truth replaces a measure that at least had a defined operation.
  Mitigations available: Restate the principle in its defensible form: do not delete an instrumented dimension before a replacement is instrumented — a sequencing rule, not a claim about what counts as an objective. Instrument convergence, mutual registration and ITT in parallel as the item's own test proposes, and rank-correlate them; that answers the question empirically without committing to the principle. Pre-register the ITT baseline before any dialogue, per the item, and record prompt version and date so the temporal-validity problem is at least visible.
  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-485
    Strongest counterargument: The item's operational advice is sound and its stated principle is a named fallacy. "Replacing a possibly-wrong objective with an unmeasurable one converts it into no objective" is step three of the McNamara progression — measure what is measurable, disregard what is not, presume the unmeasurable is unimportant, conclude it does not exist — and the fallacy is named after a case where following that logic for seven years produced systematically confident wrong conclusions. The evaluation literature's answer to unmeasurable objectives is mixed qualitative and quantitative assessment, not the retention of a defective quantitative proxy as a placeholder. Worse for the item, its own proposed escape hatch is compromised: the Cognitive Science paper establishing the Ideological Turing Test also records that it lacks normative ground truth, that passing it demonstrates imitative equivalence rather than insight, that it is sensitive to prompt interpretation, and that its temporal validity degrades as attitudes shift — and for LLM-generated arguments, that model regularisation produces artificially excessive coherence. So the item defends a possibly-wrong measure by appeal to a principle that would defend any wrong measure, and points at a replacement whose own validity is contested.
    What would need to be true for C2A2 to be safe: That the retention rule is applied as a sequencing constraint with an expiry — convergence stays until date X while ITT is instrumented — rather than as a standing principle about objectives, which would license indefinite retention of any measurable proxy.
    How to test: Instrument all three (convergence, mutual registration, ITT with a mandatory pre-dialogue baseline) over the existing dialogue corpus and compute rank correlations, per the item's own in-house test. If convergence rank-correlates with ITT, the objection is moot. If it anti-correlates, the item's caution has kept a measure that is actively pointing the wrong way.
