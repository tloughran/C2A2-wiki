SEARCH-AGAINST-PRESUMPTION-182:
  Date searched: 2026-05-15
  Original item: PRESUMPTION-182
  Original statement: "'Cowork drafts, Tom amends' pattern naturalizes Tom as canonical validator; non-Carpathi-instance ratification protocol absent; human-in-the-loop Carpathi-instance-specific"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-182
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as inference
      15b: Searched for counter-evidence on single-validator-role portability across instances
    Current status: NO-CHALLENGE-FOUND (Weak)

  Sources:
    1. The literature largely supports the presumption.
    2. Counter-pattern: BDFL succession in some FLOSS (Python 2018) has been smooth; portability via succession is possible.
    3. Counter-pattern: federated systems (Mastodon) allow per-instance validator without explicit ratification protocol; instance-local validation may be sufficient.

  Strength of challenge: Weak

  Summary: The literature supports the presumption. Counter-patterns are limited (smooth BDFL succession exists; federated instance-local validation can work). Weak challenge: the inference stands; ratification-protocol audit is load-bearing.

  Specific risks: (a) Non-Carpathi instances have no validator-role protocol; (b) Cluster: PRESUMPTION-175/176/166 carry-forward; (c) Pathway 18/19/22 dependencies.

  Mitigations available: (a) Ratification protocol documented (Tom-equivalent role at non-Carpathi instances); (b) Instance-local validation model (Mastodon-style); (c) Cluster audit.

  Recommendation: NO-CHALLENGE-FOUND (Weak) — inference well-grounded; ratification protocol audit is load-bearing

  STEELMAN:
    Item: PRESUMPTION-182
    Strongest counterargument: Instance-local validation (Mastodon model) may be sufficient — non-Carpathi instances have their own validator-equivalents. The presumption is correct that the protocol is unspecified; the load-bearing question is whether instance-local suffices or whether cross-instance ratification is needed.
    What would need to be true for C2A2 to be safe: (a) Ratification protocol documented; (b) Instance-local vs cross-instance choice made; (c) Cluster audit.
    How to test: Prototype a non-Carpathi instance and specify validator role; check whether the toolkit assumes Tom-equivalent or works with instance-local validator.
