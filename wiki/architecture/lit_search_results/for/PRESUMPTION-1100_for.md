SEARCH-FOR-PRESUMPTION-1100:
  Date searched: 2026-10-01
  Original item: PRESUMPTION-1100
  Original statement: Status records that conflate attempt outcome with system state produce misleading health signals.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1100
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Fowler, 2005. "Focusing on Events" (Event Narrative). https://martinfowler.com/eaaDev/EventNarrative.html — immutable event records kept separate from derived state; audit trail. [fetched]
    2. Beyer et al., 2016. SRE book ch. 6 — monitoring should separate symptoms from causes; ambiguous signals are a red flag. [fetched]
    3. Overeem, Spoor, Jansen, Brinkkemper, 2021. An empirical characterization of event sourced systems and their schema evolution. J. Systems & Software. — empirical precedent on event-sourced practice. [search-snippet]

  Strength of support: Weak-Moderate

  Summary: Event-sourcing literature supports separating immutable attempt/event records from derived current state; SRE guidance supports separating symptom from cause. No source directly shows that conflating attempt outcome with system health produces misleading dashboards. Support is by analogy.

  Caveats: Event sourcing is a design pattern, not an empirical study of monitoring errors. No quantitative evidence for the failure mode.

  Search scope: preliminary search — broader search recommended (web-only; practitioner and vendor sources dominate; no peer-reviewed primary studies located for the specific claim; fetched pages were passed through a summarizing model, so wording is paraphrase).

  Recommendation: PARTIALLY-SUPPORTED
