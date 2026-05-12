SEARCH-FOR-PRESUMPTION-107:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-107
  Original statement: "Two same-session org-limit interrupts presumed Anthropic-side service issue, not usage-pattern issue"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-107
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 attribution pattern: two same-session interrupts attributed to service-side rather than examined as pattern-side
      15a: Searched for supporting literature on LLM API throttling instrumentation and attribution heuristics
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. SRE / debugging literature (Beyer et al. 2016 Ch. 12 "Effective Troubleshooting"; Allspaw 2012) — service-side-first attribution without instrumented usage-side investigation is documented anti-pattern; balanced enumeration is canonical.
    2. Anthropic / OpenAI quota documentation — usage-pattern triggers (concurrent-session count, rapid-fire calls, agent-loops) are documented quota-trigger causes; equally weighted with service-side issues.
    3. Cloud-API instrumentation literature (Burns 2020 "Designing Distributed Systems") — attribution requires both sides instrumented; one-sided attribution is documented as availability-bias.
    4. Statistical-attribution literature (Pearl 2009 "Causality") — N=2 same-session events do not support service-side attribution alone; both-side enumeration required.
    5. C2A2-internal: PRESUMPTION-104 (same-throttling, naming-mismatch) — same-session interrupt is consistent with quota event (ASSUMPTION-088), but service-side-vs-pattern attribution is undetermined.

  Strength of support: None — service-side attribution as default is documented anti-pattern.

  Summary: Supportive literature for "two same-session interrupts = service-side issue" does not exist. SRE / debugging / instrumentation / causal-attribution literatures all require balanced two-side enumeration; one-sided attribution at N=2 is treated as availability bias. The presumption short-circuits the very investigation that operational discipline requires.

  Caveats: (a) The presumption may be operationally correct in some cases (when service-side does have a known issue), but as a default attribution it is unsupported; (b) supportive literature requires both sides instrumented before attribution — C2A2's usage-pattern instrumentation is not first-class, which is the structural gap; (c) NO-SUPPORT here is uniformly recommendation against the pattern.

  Recommendation: NO-SUPPORT-FOUND — service-side-first attribution is documented anti-pattern; two-side enumeration is canonical
