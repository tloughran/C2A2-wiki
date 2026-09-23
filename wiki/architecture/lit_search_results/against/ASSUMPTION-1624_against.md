SEARCH-AGAINST-ASSUMPTION-1624:
  Date searched: 2026-09-23
  Original item: ASSUMPTION-1624
  Original statement: Two same-model agents with separate contexts but identical tools and
    claim wording produce searches independent enough to count as FOR and AGAINST evidence.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1624
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the fix claim; verified the reported writes; flagged the tension with
           PREMISE-004 to 14b.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Reflexivity note: This 15a/15b pipeline is itself an instance of the claim. This file was
  produced by one same-family model instance working under the independence rule (it did not
  read any *_for.md file). Following that rule does not remove the correlation the sources
  below describe.

  Challenging evidence found: Yes

  Sources:
    1. Kim et al. (2025) (Semantic Scholar lists first authors as Kim and Garg). "Correlated Errors in Large Language Models." ICML 2025,
       PMLR v267 (arXiv:2506.07962). Across 350+ LLMs, when two models are both wrong they give
       the same wrong answer about 60% of the time on HELM, around double random baselines or
       more. Agreement is highest for models sharing a provider or architecture: one
       same-family pair reached 0.97. It also finds that larger, more accurate models have
       highly correlated errors even across providers. Two instances of the same model are the
       limiting case of "same family." Direct challenge.
    2. Zhang, H., Cui, Z., Chen, J., Wang, X., Zhang, Q., Wang, Z., Wu, D., & Hu, S. (2025).
       "Stop Overvaluing Multi-Agent Debate — We Must Rethink Evaluation and Embrace Model
       Heterogeneity." arXiv:2502.08788 (position paper). Five multi-agent debate methods
       across 9 benchmarks and 4 base models often fail to beat single-agent Chain-of-Thought
       or Self-Consistency. Using different base models per agent is the one intervention the
       authors call a "universal antidote." This implies that same-model agents give little
       independent information beyond resampling one agent.
    3. "Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness."
       arXiv:2603.06612 (2026; authors not confirmed from the fetched page). The plurality
       answer flipped in only 2.9% of question-model pairs between T=0.7 and T=1.0. On 53% of
       MATH questions where several models erred, they converged on the same wrong answer. The
       paper argues that no aggregation rule relying only on internal signals can tell a
       unanimous right answer from a unanimous wrong one when errors are correlated.
    4. [unverified — from background knowledge] Adversarial-collaboration practice
       (Mellers, Hertwig & Kahneman 2001, Psychological Science) gets its value from the
       parties having genuinely different priors and methods. Assigning a direction ("find
       FOR" / "find AGAINST") to identical reasoners does not provide that.

  Strength of challenge: Strong

  Summary: The peer-reviewed evidence (Kim et al., ICML 2025) is that LLM errors are strongly
  correlated, and most strongly within a model family. Identical instances with identical
  tools and wording sit at the extreme end of that range. The multi-agent-debate critiques find
  that homogeneous agents add little beyond single-agent resampling, and that heterogeneity
  (different base models) is what restores useful diversity. Separate contexts and opposite
  directive labels change what each agent is asked to look for. They do not change the shared
  priors, the query-formulation habits, the search engine's ranking, or the shared blind spots
  that decide what either agent can find. FOR and AGAINST searches can therefore be
  directionally opposite but still correlated in their errors of omission, because both miss
  the same literature for the same reasons.

  Specific risks: The 14a/14b reconciliation table treats "both find nothing" or "15a
  supports, 15b weak" as evidence. If both agents share query habits, their joint silence on a
  literature says more about the model's retrieval blind spot than about the literature. The
  resulting SUPPORTED statuses would be overconfident. Any error in the shared claim wording
  (for example an idiosyncratic phrase) is also passed identically to both agents.

  Mitigations available: Use a different model family for one side. Rewrite the claim
  independently for each agent. Use different search backends or seed-query lists. Measure
  overlap between the 15a and 15b source lists as a running correlation estimate. Periodically
  inject a known-answer item (a claim with a known published refutation) and check whether 15b
  finds it.

  Search scope: Moderate — 6 searches plus 2 page fetches across correlated LLM errors,
  multi-agent-debate homogeneity, LLM crowd wisdom, and persona diversity.

  Excluded results: dev.to post titled "Do Multiple Personas on One LLM Give Real Diversity, or
  Do You Need Different Model Families?" (blog; title closely echoes the claim's framing);
  emergentmind.com topic pages and "Lacuna" aggregator pages (secondary aggregators, no primary
  authorship); GitHub repositories.

  Recommendation: CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1624
  Strongest counterargument: (This steelmans the original claim against the challenge.)
    Independence is not all-or-nothing. The FOR/AGAINST design needs only enough decorrelation
    that each side surfaces some sources the other would not, not the statistical independence
    of a wisdom-of-crowds aggregate. Self-consistency (Wang et al., ICLR 2023) shows that
    resampling one model with one prompt already yields reasoning paths diverse enough to
    improve accuracy. A directional instruction ("search AGAINST") is a much stronger
    intervention than temperature: it changes the query terms, which changes the retrieved set.
    The correlated-error literature measures convergence on answers to closed questions. It
    does not measure overlap between search result sets under opposite search objectives, which
    is the quantity that matters here.
  What would need to be true for C2A2 to be safe: The 15a and 15b source lists overlap little.
    Each side reliably surfaces known sources in its own direction when tested with seeded
    items. The reconciliation step treats "both found nothing" as weak evidence at most.
  How to test: For N past items, compute the Jaccard overlap of the cited sources and of the
  issued queries between 15a and 15b. Run the same items with a different-family model on one
  side and compare the overlap and the number of unique sources. Seed items with known
  published refutations and measure 15b's recall.
