SEARCH-FOR-PRESUMPTION-311:
  Date searched: 2026-06-06
  Original item: PRESUMPTION-311
  Original statement: [inferred] Deferring the join to the P3 promotion pipeline presumes curated communities and directory records are the same kind of object that should eventually share an id space; the alternative — categorically distinct, should never join — was never raised.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-311
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that two record types are one object across a maturity lifecycle.
      15a: Searched for support for entity unification and staged-maturity (same object across lifecycle stages) record models.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. CRM lifecycle modeling (lead -> contact -> customer as one evolving entity). — A widely-deployed pattern where one real-world entity is represented across maturity stages and shares an id space as it is promoted; supports "directory seed -> curated community" as one object across stages.
    2. Medallion architecture (same record promoted Bronze->Silver->Gold). — Records routinely retain identity while being promoted across quality tiers; supports a shared id space spanning the directory and graph tiers.
    3. Master Data Management / entity unification literature. — MDM exists to unify records describing the same entity across systems into a single golden record/id; supports the unifiability premise where the records do describe the same entities.

  Strength of support: Moderate

  Summary: The staged-maturity / lifecycle record model is a recognized and widely-deployed pattern (CRM lead-to-customer, medallion promotion, MDM golden records), so the presumption that a directory seed and a curated community can be one object across maturity stages sharing an id space has solid pattern support — IF they genuinely describe the same entities. This is real support for the conceptual move. Its load-bearing condition is identity: all three precedents assume the records refer to the same real-world entity. That is exactly the unexamined premise — whether a curated community and a directory pointer are the same entity or merely associated — which 15b contests and which couples tightly to PRESUMPTION-306's feasibility doubt.

  Caveats: Lifecycle/unification models support shared id space only when the entities are the same across stages. They do NOT license merging categorically distinct entity types, and the literature on data modeling treats "association" and "identity" as different relations. So the FOR case supports "if same object, then shared id space is appropriate," leaving the antecedent (same object?) unproven and contested.

  Recommendation: PARTIALLY-SUPPORTED
