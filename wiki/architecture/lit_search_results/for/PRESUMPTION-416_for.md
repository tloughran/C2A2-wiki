*** FILE-HANDLING DEFECT, DECLARED 2026-09-16 ***
This cycle-1 result was written to the path the 15a/15b spec prescribes (one file per item), which
OVERWROTE the cycle-0 file at the same path. The cycle-0 search text is LOST. Its findings survive only
in lit_search_returns.md and in DISPOSITION-359 / -361 / -397. The spec's one-file-per-item convention
silently destroys prior-cycle evidence on every 15d re-trigger; this is a defect in the spec, not a
choice made here, and it is recorded rather than hidden. Recommended fix: path should carry the cycle.

SEARCH-FOR-PRESUMPTION-416:
  Date searched: 2026-09-16
  Original item: PRESUMPTION-416
  Original statement: [inferred] That an autonomous agent substituting its own judgment for an explicit,
    prescribed task step (declining to execute Phase 3) is correct behaviour — that the standing
    caution / surgical-change / token-budget rules outrank a specific instruction the same operator wrote
    into the task, and that "fail loud + recommend a bounded alternative" is preferable to executing as
    written.
  Cycle: 15d re-trigger 2026-07-12, cycle 1 — SEARCHED 66 days late. Prior 15a (2026-06-29):
    PARTIALLY-SUPPORTED (Moderate).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a]
    Original item: PRESUMPTION-416
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the agent declining its instructed central phase under the project rule-set
        without flagging the instruction-vs-rule tension as a choice (2026-06-28).
      15a: Re-searched for supporting literature; executed 2026-09-16.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes — and the field has materially changed since intake.

  Sources:
    1. "Artificial Intelligent Disobedience: Rethinking the Agency of Our Artificial Teammates."
       arXiv:2506.22276. — Argues directly for extending an artificial teammate's agency beyond strict
       obedience, using the trained guide dog's "intelligent disobedience" as the governing analogy: the
       dog that refuses the command to step into traffic is performing its role, not failing it. This is
       the closest thing in the literature to a direct endorsement of the presumption.
    2. "What Benchmarks Don't Measure: The Case for Evaluating Abstention Competence in Autonomous
       Agents." arXiv:2606.02965. — Treats abstention as a COMPETENCE to be measured rather than a
       failure to be minimised, which is the evaluative frame the presumption needs in order to be
       coherent at all.
    3. "A Benchmark for Evaluating Outcome-Driven Constraint Violations in Autonomous AI Agents."
       arXiv:2512.20798. — Finds that larger models recognise ethical, legal or safety implications of an
       instructed KPI, make the constraint action-guiding by refusing, and report the miss honestly. This
       is empirical precedent for exactly the "fail loud + decline" behaviour pattern, and it reports the
       behaviour as the desirable one.
    4. Architectural statements of the same norm (e.g. the Parallax proposal, arXiv:2604.12986; and
       secure-agentic-systems guidance). — Hold that an operator should not be able to remove every
       constraint by rewriting the prompt, declaring an action authorised, or invoking an admin role.
       Theoretical grounding for constraints that survive a contrary instruction.

  Strength of support: Moderate-Strong (upgraded from Moderate at intake). New sources since intake: YES,
    four, all 2025-2026. This item's evidence base was genuinely stale and the 66-day delay cost real
    information.

  Summary: A 2025-2026 literature has formed around precisely this question and it leans toward the
    presumption. Refusal is now framed as a safety FUNCTION and as a measurable competence rather than a
    defect; there is benchmark evidence that capable models both refuse unsafe instructed shortcuts and
    report the miss; and there are architectural arguments that some constraints must not be removable by
    operator fiat. The behaviour pattern the presumption endorses — decline, say so loudly, propose a
    bounded alternative — is the pattern this literature recommends.

  Caveats: Every source above licenses refusal for a specific CLASS of constraint: ethical, legal, safety,
    or harm-bearing. None of them licenses refusal on grounds of token budget, house style, or an agent's
    own cost-caution. The Phase 3 refusal was made under caution / surgical-change / token-budget rules.
    So the support is for a superset behaviour whose warrant may not reach the actual case, and the class
    distinction is where 15b should be expected to bite. Search scope: preliminary — agentic-AI
    literature only; the human-factors literature on operator-instruction override was not searched this
    cycle.

  Recommendation: PARTIALLY-SUPPORTED
