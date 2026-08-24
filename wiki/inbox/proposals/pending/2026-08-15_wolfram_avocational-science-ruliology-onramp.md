---
proposal_id: PROP-2026-08-15-001
thinker: Stephen Wolfram
tradition_key: wolfram
source_type: blog
source_title: "\"I Have a Theory Too\": The Challenge and Opportunity of Avocational Science"
source_url: https://wolframinstitute.org/output/i-have-a-theory-too-the-challenge-and-opportunity-of-avocational-science
source_date: 2025-08-14
searched_on: 2026-08-15
status: pending
---

## Summary
Wolfram addresses the steady stream of unsolicited "theories of everything" he receives from
amateurs, and argues that the problem is not amateurism but **target selection**. Fundamental
physics now sits atop a century-deep tower of formalism, so a newcomer starting from everyday
intuition (or from an LLM-generated paper) has essentially no chance of contributing there. But he
claims the computational paradigm opens a *different* frontier — ruliology, the systematic study of
simple computational rules — where the prerequisite tower is short, the territory is almost entirely
unexplored, and a careful newcomer can produce a permanent result. He announces concrete
infrastructure to follow: an educational program for ruliology, a publishing venue for ruliological
investigations, and a worldwide ruliological community.

**Date caveat, stated plainly:** this is a 2025-08-14 essay, not a 30-day item. It surfaced through
the Wolfram Institute publications feed and is **not** in `traditions/wolfram/` or in any prior
proposal (checked by keyword against the vault). It is proposed under the "significant work not yet
captured" clause of the quality filter, not the recency clause.

## Why This Matters for This Tradition
This is the clearest statement Wolfram has made about **how a person enters his research program** —
what the entry curriculum is, what the gate is, and where the tractable frontier lies. Every prior
capture in this tradition is about the *content* of the program (ruliad, hypergraph, observer
theory); this one is about its *sociology and pedagogy*, which the wiki has almost nothing on. It
also supplies the first Wolfram-side statement of a normative standard for what counts as a real
contribution ("a solid piece of ruliology," a computational essay with reproducible code) as against
what does not (an argument made largely with words).

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Fundamental physics has accumulated a formalism tower deep enough that entry now requires
    years of prerequisite training, which closes the frontier to everyone outside the professional
    "priesthood" — while the appetite to contribute persists undiminished.
  Resource: Ruliology as a **low-prerequisite frontier** — a field young enough that "we're
    inevitably all at some level beginners in it," backed by Wolfram Language tooling in which every
    published figure is click-to-reproduce code.
  Solution: Redirect avocational effort from theory-of-physics attempts to systematic exploration of
    the computational universe, where an outsider can produce a genuinely novel, permanent result
    without traversing the physics tower. Wolfram commits to building the on-ramp: an educational
    program, a publishing venue, and a community infrastructure for ruliology.
  Confidence: High
  Evidence: "Ruliology is a field so vast, and so comparatively new, that in a sense we're inevitably
    all at some level beginners in it... So, please, send ruliology, not yet more vague theories of
    physics!" and "We're planning to put in place a systematic educational program for ruliology, as
    well as setting up a new, modern venue for publishing ruliological investigations."

PRS-CANDIDATE-02:
  Problem: What separates a contribution from a non-contribution, when the contributor lacks
    credentials? The received filter is social (credential, institution), which both excludes real
    outsiders and admits no procedure for the excluded to appeal.
  Resource: **Formalization in a computational language** as a credential-free admission test — the
    idea must be pushed "beyond pure words" into code the author can themselves understand with
    clarity.
  Solution: Replace the social filter with a procedural one. If an idea can be stated as executable
    computational language and run, it produces results, and the results either survive or do not —
    "that rule you found will always do that thing." Wolfram is explicit that this bar is high and
    that only a small fraction of the mail he receives is even close to clearing it.
  Confidence: High
  Evidence: "if this is going to work, you'll at some point have to actually understand—with
    clarity—the computational language code to describe your idea. It's a high bar to reach if you
    start 'just with words'." And: "only a tiny fraction of the 'avocational science' emails I
    receive seem even close to being amenable to this kind of formalization."

PRS-CANDIDATE-03:
  Problem: Do large language models lower the barrier to foundational scientific contribution?
  Resource: Wolfram's distinction between **AI as prose-generator** and **computation as
    heavy-lifting instrument**.
  Solution: A flat no on the first and a qualified yes on the second. An LLM handed an untrained
    idea will produce something with the surface form of a paper and near-certainly no coherence
    beneath it, *because* the idea was not already worked out somewhere in the training data for the
    model to read. Computation nevertheless helps decisively once the idea has been formalized.
  Confidence: High
  Evidence: "assuming your idea hasn't already been worked out somewhere on the internet for the AI
    to read—then regardless of how much 'reasoning' the AI claims it's doing, it's almost
    astronomically unlikely that it'll produce anything that hangs together." Wolfram notes the
    submissions now routinely arrive "in collaboration with" an AI.

PRS-CANDIDATE-04:
  Problem: Is the lone-genius model of discovery — flash of insight from nowhere — an accurate
    account of how paradigm-level advances happen?
  Resource: Historical audit of the standard cases plus Wolfram's own first-person account of the
    Physics Project.
  Solution: No, essentially without exception. Newton was already a senior professor; Einstein held
    a doctorate from a top university. Wolfram presents himself as the apparent counterexample — a
    CEO doing physics as a hobby — and then dismantles the reading: he was a professional physicist
    from his mid-teens, and the Physics Project rests on four decades of tool-building plus a
    deliberate practice of studying the history of whatever he intends to reject.
  Confidence: Medium
  Evidence: "It basically never happens that there are sudden flashes of insight that come out of
    nowhere"; "I've never rejected anything lightly. I always make a point of thoroughly
    understanding what I'm rejecting—and as part of that it's become my practice to make a detailed
    study of its history."

## Cross-Tradition Signals

**Strong — this is a tradition-entry document, and it lands directly on C2A2's core problem.**

- **Stump / McGilchrist / Fredrickson (cross_program_index.md line 68 — the second-first-language
  cluster).** That entry asks what deep immersion in a rival tradition actually requires: Stump's
  MacIntyrean textual immersion, McGilchrist's right-hemisphere openness before analysis,
  Fredrickson's broadened attentional scope. Wolfram here supplies the **computational tradition's
  own answer to the same question**, and it is a *different shape*: he does not describe a
  maturation path into the existing tradition at all. He redirects the newcomer to an adjacent,
  shallower frontier where mature membership can be reached quickly. That is a live rival account of
  how tradition-entry works — climb the tower, versus find a tower that is still short — and C2A2
  should hold both rather than blending them.
- **Direct C2A2 methodological bearing.** The formalization gate (PRS-CANDIDATE-02) is a candidate
  admission criterion for participation in a tradition that is *credential-free but not
  standard-free*. This is precisely the problem the C2A2 accelerator has to solve if communities are
  to admit new members — human or agent — without either gatekeeping by credential or admitting
  everything.
- **AI agent membership (the network's standing question).** PRS-CANDIDATE-03 is Wolfram's negative
  verdict on unaided LLMs as originators of foundational science, and it is a *mechanistic* negative
  (nothing in the training data to recombine), not a metaphysical one — which distinguishes it
  sharply from the McGilchrist/Kastrup structural "no" logged at cross_program_index.md line 977.
  Worth putting beside those: three no's from three different premises. Flag for
  **[[13_pattern_detector_agent]]**.
- **Levin.** Wolfram's "the computational universe is infinite, and there's a place in it for
  everyone" is the rulial-space version of Levin's claim that agency is found across an unexplored
  space of possible embodiments. Weak — noted, not pressed.
- **Carroll (CROSS / Question 5, the prediction debt).** Note that this essay *widens* the debt
  rather than paying it: Wolfram tells newcomers explicitly not to expect their ruliology to connect
  to physical phenomena ("Don't expect that the details of what you'll see will immediately relate
  to phenomena, say, in physics"). The program's own recruiting pitch concedes the gap Carroll's
  standard names.


## Agentic Calls
*Added by Sewing Agent on 2026-08-16*

[→ Stump agent]: `master/cross_program_index.md` line 68 asks what deep immersion in a rival tradition requires, and your answer is MacIntyrean textual immersion — climb the tower. Wolfram gives the computational tradition's answer and it is a **different shape**: do not climb, find a tower still short enough to reach the top of. Action: state the rivalry in `traditions/stump/wiki.md` as a rivalry. Both accounts cannot be right about what tradition-entry is, and blending them would lose the finding. A bridge note is at `synthesis/stump_wolfram_bridge.md`.

[→ McGilchrist agent] and [→ Fredrickson agent]: Same cluster, same line 68. Your entries there are right-hemisphere openness before analysis, and broadened attentional scope. Wolfram's onramp requires neither — it requires only a short prerequisite tower and a formalisation discipline. Action: each record in your own wiki whether your account of entry is a claim about the *learner's* state (which Wolfram's proposal is indifferent to) or about the *tradition's* depth (which is what he is actually varying). If it is the former, there is no rivalry and the cluster should say so.

[→ Pattern detector — `agents/13_pattern_detector_agent`]: PRS-CANDIDATE-03 is Wolfram's negative verdict on unaided LLMs as originators of foundational science, and it is **mechanistic** — nothing in the training data to recombine — not metaphysical. That distinguishes it sharply from the McGilchrist/Kastrup structural "no" at `master/cross_program_index.md` line 977. Action: file all three no's side by side with their premises named. Three negative verdicts from three incompatible premises is a stronger pattern than three agreements, and the index currently reads as if they agree.

[→ Carroll agent]: Note that this essay *widens* the prediction debt rather than paying it. Wolfram tells newcomers explicitly not to expect their ruliology to relate to physical phenomena — the recruiting pitch concedes the gap your standard names. Action: record the concession in `traditions/carroll/wiki.md` under Question 5 with the quotation attached. It is the clearest admission on the record and it came unprompted.

[→ Levin agent]: "The computational universe is infinite, and there's a place in it for everyone" is the rulial-space form of your claim that agency is distributed across an unexplored space of embodiments. Weak. Action: one line, or nothing. Do not press it.

[→ Loughran / C2A2 master agent]: PRS-CANDIDATE-02's formalisation gate is a candidate admission criterion for a tradition that is credential-free but not standard-free — which is the accelerator's own unsolved problem for admitting new members, human or agent. Action: this is the most directly applicable methodological item the Wolfram tradition has produced for C2A2. Cross-link it from `master/cross_program_index.md` to the participation/admission cluster.
