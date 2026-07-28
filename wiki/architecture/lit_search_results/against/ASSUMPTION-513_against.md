SEARCH-AGAINST-ASSUMPTION-513:
  Date searched: 2026-07-24
  Original item: ASSUMPTION-513
  Original statement: A validated finding does not reach the agent it governs unless an explicit propagation mechanism carries it (the know-do gap); scope-guard: the ~17yr lag does NOT transfer to a single-maintainer system.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-513
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from PREMISE-123 report
      15b: Searched for evidence that findings CAN propagate without an explicit mechanism
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Rogers, E.M. (2003). "Diffusion of Innovations" (5th ed.). — Some authors reserve "diffusion" for the spontaneous, unplanned spread of ideas; innovations demonstrably propagate through informal interpersonal channels and opinion leaders without any formal dissemination mechanism. This challenges the strong "does NOT reach unless explicit" form.
    2. Tacit-knowledge / community-of-practice literature (Wenger; Nonaka). — Practice can change through situated participation and imitation rather than an explicit carrier; the "mechanism" may be social and implicit, not an engineered edge.

  Strength of challenge: Weak (for C2A2's context)

  Summary: The absolute wording ("does not reach ... unless an explicit propagation mechanism") is too strong in human organizations, where diffusion theory shows ideas spreading via informal, unplanned interpersonal channels. However, this challenge depends on the existence of a social substrate — opinion leaders, imitation, communities of practice — that a single-maintainer, file-based agent system does not possess. There are no informal peer channels between C2A2 agents; a finding in validated_premises.md has no social path to an agent spec. So the challenge largely fails to transfer, and its failure to transfer actually reinforces the assumption for C2A2's context.

  Specific risks: If the assumption were over-generalized, C2A2 might build heavy propagation machinery where lightweight/implicit routing would do — but there is no evidence of an implicit channel here.

  Mitigations available: Confirm empirically (the in-house test) that no finding has ever edited an agent spec without an explicit edit; if confirmed, the diffusion challenge is moot.

  STEELMAN:
    Item: ASSUMPTION-513
    Strongest counterargument: In systems with a shared substrate, valid ideas propagate on their own via imitation and social proof, so mandating an explicit propagation mechanism can be wasteful ceremony. The know-do gap is partly an artifact of fragmented human bureaucracies, not a law of information.
    What would need to be true for C2A2 to be safe: there must genuinely be NO implicit channel by which a finding influences an agent (no shared context read at runtime, no operator memory). If any such channel exists, "explicit mechanism required" is false.
    How to test: audit whether any agent's behavior has changed in response to a finding it was never explicitly handed.

  Recommendation: PARTIALLY-CHALLENGED (challenge does not transfer to single-agent context)
