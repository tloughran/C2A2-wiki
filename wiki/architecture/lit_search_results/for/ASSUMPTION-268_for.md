SEARCH-FOR-ASSUMPTION-268:
  Date searched: 2026-06-03
  Original item: ASSUMPTION-268
  Original statement: A valid pre-push constitutional review requires live verification in a real foreground browser tab served over HTTP (not headless/asserted), with explicit observable evidence (opacity split, cross-link count, clean console) plus Tom's sign-off.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-268
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the pre-push review gate requiring a real served browser tab with observable evidence + sign-off.
      15a: Searched in-situ / real-environment verification, asserted-vs-observed state, and human-in-the-loop release gates.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Test-in-the-real-environment guidance (cloudbees "Why and How You Should Test in Production"; Harness lecture "Only a Full Pipeline Run Counts as Real Verification"). — Verifying in the same environment users experience (served, real config) gives confidence that asserted/lower-environment checks do not; directly supports "real foreground tab over HTTP, not asserted."
    2. Smoke / pre-promotion release gate practice (Harness smoke-testing; GeeksforGeeks smoke testing). — A fast go/no-go check of essentials in the just-deployed environment is canonical; the opacity-split + cross-link-count + clean-console checks are exactly such a smoke gate.
    3. Human-in-the-loop release gate + asserted-vs-observed gap (this register's verify-the-effect family, PREMISE-045/046). — Observing the rendered effect (not inferring it from "the code should do X") is the same verify-the-side-effect principle already incorporated; Tom's sign-off adds an out-of-band human vantage.

  Strength of support: Strong

  Summary: The assumption aligns with strong, convergent guidance: real-environment (in-situ) verification beats asserted or lower-environment checks, a lightweight observable smoke gate at the release boundary is best practice, and a human sign-off supplies an independent vantage. For a constitutional pre-push gate on a self-contained ~4MB visualization, requiring live observable evidence in a served browser tab is the proportionate, well-grounded standard — and it instantiates the same verify-the-effect principle already incorporated as PREMISE-045/046.

  Caveats: The literature also values automation: a purely manual foreground review does not scale and can be skipped under time pressure; the durable form is to encode the observable checks as automated assertions AND keep human sign-off (see 15b). Support is for live-observed verification, not for it remaining manual-only.

  Recommendation: SUPPORTED
