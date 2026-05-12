SEARCH-AGAINST-PRESUMPTION-107:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-107
  Original statement: "Two same-session org-limit interrupts presumed Anthropic-side service issue, not usage-pattern issue"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-107
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 attribution pattern
      15b: Searched for counter-evidence on service-vs-pattern attribution for repeated quota errors
    Current status: CHALLENGED

  Challenging evidence found: Yes (strong)

  Sources:
    1. Beyer et al. (2016) "SRE" Ch. 12 (Effective Troubleshooting) — service-side-default attribution at low N is documented as availability bias; balanced two-side enumeration is canonical.
    2. Anthropic / OpenAI quota documentation — usage-pattern triggers (concurrent-session, agent-loops, rapid-fire calls) are explicitly documented as legitimate quota causes equally weighted with service-side issues.
    3. Cloud-provider postmortems (AWS / GCP 2018–2024) — multiple cases where "same-session repeated quota" was eventually traced to client-side usage pattern (loop, concurrency, ramp), not service-side issue.
    4. Pearl (2009) "Causality" — N=2 same-session events are insufficient to support service-side attribution alone; both-side enumeration required.
    5. C2A2-internal: ASSUMPTION-088 (work-blocking quota) and PRESUMPTION-104 (naming misclassification) — usage-pattern instrumentation absence is the structural gap that this presumption manifests.

  Strength of challenge: Strong

  Summary: Service-side-default attribution at N=2 is documented availability bias. SRE / quota / postmortem / causal-inference literatures uniformly require balanced two-side enumeration. The presumption short-circuits the very investigation that operational discipline requires. Multiple cloud-provider postmortems document cases where the actual cause was usage-pattern-side, not service-side.

  Specific risks: (a) Misattribution leads to misdirected escalation effort to Anthropic for usage-pattern issue; (b) usage pattern (e.g., concurrent agent loops, rapid-fire calls) goes unfixed; (c) compounds with PRESUMPTION-104 (misclassification) — both presumptions short-circuit investigation.

  Mitigations available: (a) Instrument usage-pattern signals (call rate, concurrency, session duration); (b) capture wire-level response signature for each interrupt; (c) run two-side enumeration before service-side framing.

  Recommendation: CHALLENGED — service-side-default attribution at N=2 is documented anti-pattern.

  STEELMAN:
    Item: PRESUMPTION-107
    Strongest counterargument: Service-side-default attribution at N=2 is the canonical availability-bias trap. Quota documentation, SRE practice, postmortem corpora, and causal-inference literature uniformly require balanced two-side enumeration. The presumption short-circuits the investigation needed to distinguish service-side from pattern-side cases.
    What would need to be true for C2A2 to be safe: (a) usage-pattern instrumentation; (b) two-side enumeration before attribution; (c) wire-level response capture.
    How to test: Instrument the next session — call rate, concurrency, session duration, sequence to interrupt; if usage-pattern crosses documented thresholds, pattern-side attribution is supported; if not, service-side investigation is justified.
