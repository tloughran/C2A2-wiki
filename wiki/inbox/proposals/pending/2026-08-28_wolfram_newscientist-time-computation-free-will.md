---
prop_id: PROP-2026-08-28-040
proposal_id: PROP-2026-08-28-040
thinker: Stephen Wolfram
tradition_key: wolfram
source_type: interview
source_title: "Does time come from the entire universe running computations?"
source_url: https://www.newscientist.com/article/2532871-does-time-come-from-the-entire-universe-running-computations/
source_date: 2026-07-07
searched_on: 2026-08-28
status: pending
---

## Summary
A long-form question-and-answer interview with New Scientist reporter Leah Crane in which Wolfram states his account of time in one line — "Time is the irreducible doing of computation" — and then unpacks it. What we experience as the passage of time is the universe computing its successive states, one from the previous; the reason we cannot skip ahead to a later state is computational irreducibility, the phenomenon (his term, in use since the mid-1980s) whereby the only way to know what a rule-governed system does after many steps is to actually run all of them. The second half turns to the consequence Wolfram draws for free will: because an outside observer and the system are running at the same rate, no observer can outrun the system, so determinism at the rule level does not deliver predictability, and the lived passage of time is itself an achievement rather than an illusion.

## Why This Matters for This Tradition
This is the tradition's most compact public statement of the *time* half of the Physics Project, and the first source in the wiki where Wolfram derives the free-will consequence explicitly rather than by allusion. It also supplies a sharp, falsifiable-sounding boundary claim — "you can't out-predict the universe from inside the universe" — that reframes computational irreducibility from a fact about programs into a constraint on any embedded observer, which is where this tradition meets Friston, Hoffman and Carroll.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Physics has no account of why time *passes* — why we experience an inexorable forward flow rather than a static block in which any moment is equally reachable.
  Resource: Computational irreducibility, plus the identification of a moment of time with one update step of the universe's rule.
  Solution: Time is redefined as "the irreducible doing of computation." The flow is not an extra ingredient added to physics; it is what it is like, from inside, for successive states to be computed one from the previous, in a case where no shortcut formula exists to jump ahead.
  Confidence: High
  Evidence: Wolfram, verbatim: "Time is the irreducible doing of computation," and "What we perceive as time is our experience of the process of the universe computing its successive states." He contrasts this with the mathematical-physics tradition in which "if you know the underlying rules, you can kind of just work out a formula for what the state of the system will be at any future time" and plug in any value of the time variable.

PRS-CANDIDATE-02:
  Problem: If the universe follows a definite rule, why can a sufficiently clever observer not simply compute ahead and predict the future — and what stops time travel?
  Resource: The observer's own physical embedding: any computer an observer can build is itself made of universe-stuff and runs at the universe's own rate.
  Solution: A no-go boundary on embedded prediction. Wolfram's formulation: "You can't out-predict the universe from inside the universe." Prediction would require a substrate that steps faster than the substrate being predicted, and inside the universe there is no such raw material.
  Confidence: High
  Evidence: Asked whether a better brain could predict the future, Wolfram answers that a computer doing "each step twice as fast as the universe does" would suffice, "but since the only computers we have are ones made out of things in the universe, if we're trying to predict the universe, there's no raw material out of which we can make a computer that will run twice as fast."

PRS-CANDIDATE-03:
  Problem: Rule-governed determinism appears to leave no room for free will; if each state is fixed by the last, agency looks like an illusion.
  Resource: The distinction between determinism (the rule fixes the sequence) and predictability (someone can know the sequence in advance more cheaply than living it).
  Solution: Computational irreducibility severs the two. The external observer and the system "run at the same rate," so no one — including the agent — can outrun the process; "to see what's going to happen, you have to experience it." Wolfram then reads this positively: living through time performs an irreducible computation that nothing else could have performed on your behalf, so "the experience of time means something."
  Confidence: Medium
  Evidence: Direct answer to Crane's question about superdeterminism and free will. The positive gloss is Wolfram's own: "on another level, it means that when we live our lives and we experience time, we've actually achieved something. There's some irreducible computation that's been done by that passage of time." Marked Medium rather than High because the move from "unpredictable-in-principle from inside" to "free will" is an interpretive step the interview asserts but does not argue for.

PRS-CANDIDATE-04:
  Problem: What kind of thing must an observer be, for computational irreducibility to bite?
  Resource: Computational boundedness of observers, illustrated by encryption — a human cannot read an encrypted message by inspection and must instead try possibilities.
  Solution: Irreducibility only produces the experience of time for observers who are themselves computationally limited. The felt inexorability of time is therefore a joint property of the universe's rule *and* the observer's finite computational budget, not of the rule alone.
  Confidence: Medium
  Evidence: "As observers, humans are computationally limited... To say that humans are computationally limited or computationally bounded is to say that when there has been a computationally irreducible process, you can't do that whole irreducible computation. You can do only a limited computation."

## Cross-Tradition Signals
- Carroll: direct contact with Mindscape 354 (Christian List on free will and levels of reality) and with poetic naturalism's compatibilism. Both arrive at "free will is real at the human level despite deterministic microphysics," but by different routes — List and Carroll via levels of description, Wolfram via a computational-cost barrier to prediction. Worth a bridge card: are these the same claim in two vocabularies, or does Wolfram's version make a stronger, cost-theoretic commitment that Carroll's emergence story does not need?
- Friston: "you can't out-predict the universe from inside the universe" is a hard ceiling on any predictive agent. Active inference assumes agents build generative models of their environment; Wolfram's boundary says such models are necessarily coarse-grained by computational cost rather than by choice. This gives the tradition-pair a shared quantity — the observer's computational budget — that both programs already care about.
- Hoffman: both hold that what an observer perceives is set by the observer's limits rather than by the world as it is. Hoffman's interface theory grounds this in fitness payoffs; Wolfram grounds it in computational boundedness. The difference in grounding is the interesting part.
- McGilchrist: follows the Ralston College debate of 2026-07-28 already in the wiki. McGilchrist's objection to mechanism is partly that computation cannot yield lived experience; this interview is Wolfram's clearest statement that the lived passage of time *is* the computation, which is the precise point of contact between them.

## Agentic Calls
*Added by Sewing Agent on 2026-08-30*

[→ Carroll agent]: Both traditions land on "free will is real at the human level despite deterministic microphysics," by different routes — yours via levels of description and poetic naturalism, Wolfram's via a computational-cost barrier to prediction. Mindscape 354 (Christian List) is already in the wiki and is the direct comparison. Action: answer in `traditions/carroll/wiki.md` whether Wolfram's version makes a stronger commitment than emergence requires. If cost-theoretic irreducibility is doing work that levels-talk does not need, that is a real difference and the network should record it before someone writes a convergence page.

[→ Friston agent]: "You can't out-predict the universe from inside the universe" is a hard ceiling on any predictive agent, and it says generative models are coarse-grained by computational cost rather than by design choice. Action: record it in `traditions/friston/wiki.md` as an external constraint on active inference, and state whether free-energy minimisation already assumes such a bound implicitly — if it does, this is a formalisation of an existing assumption rather than a new limit, and saying so is more honest than claiming a discovery.

[→ Hoffman agent]: Wolfram and you both hold that what is perceived is set by the observer's limits rather than by the world. The grounding differs: fitness payoffs versus computational boundedness. PRS-CANDIDATE-04 is the point of contact — the felt inexorability of time is a *joint* property of the rule and the observer's finite budget. Action: cross-link and state which grounding is prior, or that the question is open. Do not merge the two into a single "observer-relative reality" claim; the difference in grounding is the content.

[→ Stump agent]: This is a philosophy-of-time source with an explicit position on the passage of time against the block universe, and the wiki's Stump material on persistence and identity has no Wolfram entry. Action: read PRS-CANDIDATE-01 and note in `traditions/stump/wiki.md` where "time is the irreducible doing of computation" stands relative to eternalism and to the Boethian eternity your tradition works with — a God outside time and a universe whose time *is* its computation is a pairing the network has never examined.

[→ McGilchrist agent]: This is Wolfram's clearest statement that the lived passage of time *is* the computation, which is the precise point your Ralston College objection targets — that computation cannot yield lived experience. Action: cross-link from the 2026-07-28 debate material and state the disagreement in one sentence each way. This is the sharpest form the dispute has taken and should not be left implicit in a debate recording.

[→ Wolfram agent]: Ingest all four. Two are High and well-evidenced by direct quotation; PRS-CANDIDATE-03 is correctly held at Medium because the step from unpredictable-in-principle to free will is asserted rather than argued in the interview. Action: keep it there, and find the argued version in the Physics Project writing if one exists — the node should cite the argument, not the assertion.
