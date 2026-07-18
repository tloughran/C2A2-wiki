SEARCH-FOR-ASSUMPTION-439:
  Date searched: 2026-07-11
  Original item: ASSUMPTION-439
  Original statement: "The Jul-6 write-stop and same-day corruption recurrence share one cause — the OpenStory runtime has been continuously down ~102h."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-439
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-10 EOD daily run
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. [NASA (Jones, H.), 2016. "Common Cause Failures and Ultra Reliability." NASA Technical Reports Server 20160005837. — Establishes that multiple failures clustered in a short time window are disproportionately likely to share a common cause rather than be independent coincidences; independence of near-simultaneous failures is the assumption that requires justification, not the shared cause.]
    2. [Rausand, M. / NTNU, "Risk Assessment, Chapter 15: Common Cause Failures" (course text, Norwegian University of Science and Technology). — Provides the root-cause + coupling-factor framework: same-day co-occurrence of a write-stop and corruption in components coupled through one runtime is the canonical CCF signature, supporting a single-cause first hypothesis.]
    3. [Wikipedia/standard references, "Occam's razor," with medical-diagnosis applications (e.g., The American Journal of Medicine, 2020, "The Diagnostic Approach in Complex Patients: Parsimony or Plenitude?"). — Diagnostic parsimony doctrine: prefer the single explanation that accounts for all findings before invoking multiple unrelated causes, because it minimizes unsupported assumptions. Direct theoretical grounding for 14a's attribution style.]
  Strength of support: Moderate
  Summary: The reasoning pattern behind the assumption — attribute temporally clustered failures in coupled components to one cause — has solid theoretical grounding. CCF literature from reliability engineering treats same-window multiple failures as prima facie common-cause events, and diagnostic parsimony (Occam's razor) is an established heuristic for exactly this inference. Both the write-stop and the corruption recurrence plausibly couple through the OpenStory runtime, matching the root-cause/coupling-factor structure. The support is for the inference method and its prior probability, not for the specific factual claim about the ~102h outage, which no literature can adjudicate.
  Caveats: The same literature that supports parsimony bounds it: Hickam's dictum and the CCF texts both stress that parsimony is a heuristic, not proof, and that complex failures often combine an initiating cause with pre-existing contributing conditions (a corrupted DB may be a latent condition the outage merely exposed). The item is QUEUED-EMPIRICAL and should stay so — literature supports the hypothesis's priority ordering, not its confirmation. Search scope confidence is high for the reasoning-pattern question; no software-incident-specific study quantifying common-cause vs coincident base rates was found.
  Recommendation: PARTIALLY-SUPPORTED
