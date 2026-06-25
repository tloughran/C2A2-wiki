SEARCH-FOR-ASSUMPTION-348:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-348
  Original statement: "Per-thinker/per-claim dissensus rate is a meaningful detector output (evidence about positions under rich information)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-348
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the pathway's claimed payoff (disagreement-as-data, constitutional detector aim)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Aroyo & Welty 2015. 'Truth Is a Lie: Crowd Truth and the Seven Myths of Human Annotation.' AI Magazine. - Annotator disagreement is signal (ambiguity/vagueness), not merely noise.
    2. Pavlick & Kwiatkowski 2019. 'Inherent Disagreements in Human Textual Inferences.' TACL. - Disagreement reflects genuine, stable variation in interpretation, not just error.
    3. Plank 2022. 'The Problem of Human Label Variation.' EMNLP. - Systematizes disagreement as informative signal across many NLP tasks; motivates label-distribution modeling.
    4. Nie, Zhou & Bansal 2020. 'What Can We Learn from Collective Human Opinions on NLI?' EMNLP. - Disagreement distributions carry task-relevant information about item difficulty/ambiguity.

  Strength of support: Strong

  Summary: There is a strong and now-mainstream literature treating inter-annotator disagreement (here, inter-column/inter-thinker dissensus) as a meaningful output rather than noise to be averaged away. Disagreement reliably tracks item ambiguity, difficulty, and the presence of multiple plausible positions - precisely the 'evidence about positions under rich information' the assumption asserts. The perspectivist/human-label-variation turn in NLP provides direct methodological precedent for reporting a dissensus rate as a first-class measurement.

  Caveats: The literature supports that disagreement CAN be signal; it does not guarantee that any given disagreement IS signal rather than instrument noise. Distinguishing genuine under-determination from bad axes or an erratic adjudicator (PRESUMPTION-388) requires test-retest / error-vs-variation separation.

  Search scope: Disagreement-as-signal / perspectivist NLP; human label variation. Comprehensive.

  Recommendation: SUPPORTED
