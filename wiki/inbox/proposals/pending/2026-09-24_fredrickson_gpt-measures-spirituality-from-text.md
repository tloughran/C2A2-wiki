---
proposal_id: PROP-2026-09-24-001
thinker: Barbara Fredrickson
tradition_key: fredrickson
source_type: paper
source_title: "Can an Algorithm Tell How Spiritual You Are? Using Generative Pretrained Transformers for Sophisticated Forms of Text Analysis"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12592590/
source_date: 2024-12-12
searched_on: 2026-09-24
status: pending
---

> **Filter note for reviewer (read first).** This passes the "not yet captured" and "substantive" tests but is borderline on two others, so it is flagged rather than presented as a clean pass:
> 1. **Recency.** Published online 2024-12-12; issue date December 2025 (*Journal of Personality* 93(6):1258–1270). Not within 30 days. Submitted under the "significant work not yet captured" clause — it appears on the PEP Lab's own 2025 publication list but nowhere in the vault (grep for the title returned nothing).
> 2. **Authorship.** Fredrickson is fifth of six authors (Prinzing, Bounds, Melton, Glanzer, Fredrickson, Schnitker). Lead author Michael Prinzing is a PEP Lab alumnus; the work comes out of the Baylor Science of Virtues Lab (Schnitker). It is Fredrickson-lab work, not Fredrickson's own argument.
> No other Fredrickson material from the past 30 days surfaced: the PEP Lab publication page's newest entries (the two 2026 *SCAN* papers) and its news page (the *Positive Emotions* book) are already in the vault.

## Summary
Two studies test whether GPT models can score a subtle psychological construct — spirituality — from people's free-written text as well as trained human coders can. In Study 1 (2,199 US undergraduates, 6,597 written goals), GPT-3.5 and GPT-4 agreed with human coders almost perfectly (Cohen's κ ≥ 0.93 and ≥ 0.95; the two humans agreed at κ = 0.96), and GPT-4's ratings predicted religiousness, meaning in life, depression, and anxiety *beyond* what people's own self-reports predicted. In Study 2 (357 community adults, 714 short essays written to prompts that never mentioned spirituality), GPT-4 and a trained research assistant correlated at r = 0.85, and both correlated equally with self-report (r = 0.42 vs 0.41) and with a behavioral choice task (r = 0.24 vs 0.26). The human coding took about 11 weeks; GPT-4 took about 20 minutes and roughly $20 in API fees.

## Why This Matters for This Tradition
It extends the Fredrickson lab's measurement program (compare "Positively in-sync," already ingested) from shared positive affect to a self-transcendent construct, and it is the lab's first direct test of an LLM *as a rater of human interiority*. For C2A2 the larger point is methodological: if a model can score a tradition-shaped trait from ordinary prose as reliably as a trained coder, the "detector" half of the accelerator/detector design has a validated precedent.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Manual text analysis is the gold standard for nuanced psychological constructs, but it is slow and expensive (weeks of trained labor), and fixed-response questionnaires miss how people describe their own inner lives — several participants wrote in to object that the standard spirituality scales mischaracterized their experience.
  Resource: GPT-3.5/GPT-4 prompted with an explicit working definition (Piedmont 1999: the inclination to stand outside one's immediate time and place and see life from a broader, interconnected perspective) and an observer-report version of the Spiritual Transcendence Scale.
  Solution: LLM coding matches trained human coders on reliability and on validity against independent measures, at a tiny fraction of the cost, and adds predictive power over self-report (incremental validity for religiousness, meaning in life, depression, anxiety).
  Confidence: High (for the narrow claim, in these samples)
  Evidence: Study 1 κ ≥ 0.95 GPT-4 vs humans; Study 2 GPT–human r = 0.85; equal correlations with self-report (z = 0.11, p = .91) and behavioral task (z = −0.90, p = .37).

PRS-CANDIDATE-02:
  Problem: If LLMs rate interior states, do they carry demographic or religious bias — scoring Christians differently from members of other religions or the non-religious?
  Resource: Moderation tests: regressions checking whether age, sex, race, education, or religious affiliation change how GPT-4's ratings track self-report and behavior.
  Solution: No moderation found — a first-pass sign that GPT-4 scored spirituality consistently across groups.
  Confidence: Speculative
  Evidence: The authors themselves say Study 2 was not powered to detect small interactions; samples were convenience samples and disproportionately female; only one human rater in Study 2; the studies were not preregistered. "No detected bias" here is weak evidence of no bias.

## Cross-Tradition Signals
- **C2A2 / Loughran (strong).** This is a validated instance of using a language model to *read* a tradition-constituted interior quality out of ordinary prose. That is the operation the accelerator/detector system needs if it is to detect whether a participant is becoming "second-first-language" competent in another tradition. The caveat carries over: the construct was defined *for* the model in one tradition-neutral psychological vocabulary (Piedmont). Whether an LLM can score maturity *by a given tradition's own standards* — Thomist, Buddhist, Levinite — is untested.
- **Stump (moderate).** Stump's "Franciscan knowledge" is non-propositional, second-person knowledge conveyed through narrative. The Study 2 design (essays that let spirituality show without being asked about) is a narrative-elicitation measure. Open question for the Stump agent: is what GPT-4 detects here propositional content or something closer to what Stump means by the knowledge of persons?
- **McGilchrist (moderate, adversarial).** McGilchrist would predict that a left-hemisphere-style system can categorize explicit markers of the transcendent but not apprehend it. The finding that GPT scores *predict behavior and mental-health outcomes beyond self-report* is a direct test case for that claim, and the Level-2 stream should record it as contested, not settled.
- **Kastrup / Hoffman (weak).** The working definition — all living beings "interconnected and unified by bonds that transcend biological life and death" — is closer to idealist or conscious-realist framings than to a mechanist one; worth noting that the field's operational definition of spirituality already leans that way.
