SEARCH-AGAINST-PRESUMPTION-1063:
  Date searched: 2026-09-22
  Original item: PRESUMPTION-1063
  Original statement: Substituting oldest-day work for an empty queue is a choice, not a
    necessity, and its costs and yields have never been set against each other.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1063
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Noted that twenty-nine runs chose one response to an empty queue and none named an
        alternative.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Parkinson, C.N. (1955, popularized in "Parkinson's Law: Why Work Expands to Fill the
       Time Allotted," and secondary coverage e.g. Asana/monday.com explainers, 2025) — observes
       that given surplus time/capacity, people (and by extension automated agents given
       surplus cycles) do not typically sit idle; they "polish" — i.e., some work naturally
       expands to fill idle capacity. This offers a mild challenge to the "choice, not necessity"
       framing: if idle capacity reliably gets filled by *something* regardless of design, the
       question is not whether to fill it but what fills it, softening the claim that leaving it
       empty was ever a live, undiscussed alternative.
    2. Featherbedding/make-work literature (TIME archive, "Featherbedding: Make-Work Imperils
       Economic Growth"; Wikipedia "Featherbedding," "Busy work") — documents the historical cost
       side the claim says was "never set against" alternatives: featherbedding research
       explicitly quantifies the cost of manufactured work (e.g., $500M/year cited in 1958 US
       rail featherbedding), which is direct precedent for treating "make-work when idle" as a
       real, measured cost category — supporting the claim's underlying concern rather than
       challenging it, but showing the cost/yield comparison the claim says has "never" been done
       is a well-established analytical exercise in adjacent domains (labor economics), so the
       gap is one of application to this specific system, not of missing methodology.

  Strength of challenge: Weak

  Summary: This presumption is largely a procedural/absence claim (no one considered
  alternatives) rather than a substantive empirical claim, so it is hard to find literature that
  directly contradicts it — most relevant sources instead corroborate the concern that idle-time
  substitution carries real, measurable costs (featherbedding literature) or complicate the
  "choice, not necessity" framing by suggesting idle capacity tends to get filled by something
  regardless of deliberate design (Parkinson's Law). Neither source establishes that the specific
  choice made (oldest-day work) was in fact necessary or costless; if anything the literature
  strengthens the underlying worry about unexamined make-work.

  Specific risks: Low direct risk to the claim itself; the greater systemic risk is that "no one
  named an alternative in 29 runs" could reflect either (a) a genuinely unexamined default (as
  the claim suggests) or (b) convergent good judgment that oldest-day work is in fact the
  sensible default and alternatives weren't worth stating — the search did not find literature
  resolving this ambiguity either way.

  Mitigations available: Run a controlled comparison (idle vs. oldest-day-work vs. a third
  option) and measure yield per unit cost, directly answering the claim's own call for a
  cost/yield comparison, rather than relying on absence-of-alternatives as evidence of
  suboptimality.

  Search scope: Preliminary — 1 search (Parkinson's Law / featherbedding / make-work). Did not
  find literature specific to "idle-worker policy in automated/agentic review systems" or
  "observer effects in repeated inspection," both named in the literature lane; those appear to
  be under-published as distinct topics, or require more specialized queries (e.g., queueing
  theory server-idling policies, N-policy/vacation queueing models) not attempted here.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1063
  Strongest counterargument: Parkinson's-Law-style observations suggest idle capacity rarely
  stays idle in practice — something fills it — so framing "leave the queue empty" as a genuinely
  available, costless alternative may be unrealistic; the real choice space may be narrower than
  the claim implies (oldest-day work vs. some other filler, not oldest-day work vs. true idleness).
  If so, "no run named an alternative" may reflect convergent recognition that idleness isn't a
  real option, not an unexamined default.
  What would need to be true for C2A2 to be safe: Idle capacity would need to be genuinely
  costless to leave unused (no drift, no decay of readiness, no expectation to show throughput)
  for "do nothing" to be a real alternative worth comparing against oldest-day work.
  How to test: Instrument a subset of runs to actually leave the queue empty when it empties,
  and compare downstream outcomes (error rate, backlog, reviewer trust, throughput) against the
  oldest-day-work default over enough cycles to measure real cost and yield, directly resolving
  the claim's central "never been set against each other" gap.
