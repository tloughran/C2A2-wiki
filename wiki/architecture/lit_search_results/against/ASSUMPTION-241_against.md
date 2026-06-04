SEARCH-AGAINST-ASSUMPTION-241:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-241
  Original statement: The operational rule "pasted review-page state is the source of truth; intent supersedes UI state when explicitly stated" is the right closure on the Gmail-misfire loop ahead of any generation-side fix.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-241
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on intent-supersedes-UI rules and audit-trail gaps.
    Current status: PARTIALLY-CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. NIST SP 800-92 (audit logging) — verbal/stated-intent overrides without explicit logging create audit-trail gaps that are documented to compound; "speech acts" alone don't satisfy auditability requirements.
    2. Norman (1988) "The Design of Everyday Things" — when UI categorization is wrong, fixing the UI is the documented preferred remediation; "intent supersedes UI" is a stopgap that masks the underlying UI defect.
    3. Bainbridge (1983) "Ironies of Automation" — operational rules that route around automation failures tend to calcify; "ahead of generation-side fix" is documented as the pattern of becoming the permanent solution.
    4. ITIL audit principles — multi-surface authority hierarchies require explicit canonization AND explicit logging; verbal-intent rules without machine-readable records are documented as audit gaps.
    5. Cook & Woods second-story: routing around defects with operational rules is documented as common but treated as deferred-debt, not as resolution.

  Strength of challenge: Moderate

  Summary: The operational rule has known failure modes. Intent-supersedes-UI rules without explicit logging create audit-trail gaps. Fixing UI is the documented preferred remediation when UI categorization is wrong. "Ahead of generation-side fix" is a documented pattern that often becomes the permanent solution. The rule defers the underlying defect rather than addressing it.

  Specific risks: (a) Audit-trail gap when intent overrides without log entry; (b) "stopgap becomes permanent" pattern; (c) UI defect remains and re-recurs; (d) the rule extends to "intent supersedes UI" without checking that the UI itself was the cause of the original Gmail misfire — combining two issues into one rule.

  Mitigations available: (a) Require explicit logging when intent supersedes UI; (b) document a hard deadline for the underlying UI/generation fix; (c) treat the rule as time-limited, not canonical; (d) separate the Gmail-misfire rule from the UI-misfire rule.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: ASSUMPTION-241
    Strongest counterargument: Operational rules that route around UI defects are documented as becoming permanent. Without explicit logging, intent-supersedes-UI rules create audit-trail gaps. The proper response is to fix the UI/generation-side defect, not to canonize a rule that bypasses it. The rule is a stopgap that may become permanent.
    What would need to be true for C2A2 to be safe: (a) explicit logging required when intent overrides UI; (b) hard deadline for underlying fix; (c) rule treated as time-limited.
    How to test: 30-day audit: how often was the rule invoked; was the underlying UI/generation defect addressed; did the rule become the default rather than the exception.
