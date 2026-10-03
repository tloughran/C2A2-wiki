SEARCH-FOR-PRESUMPTION-1107:
  Date searched: 2026-10-03
  Original item: PRESUMPTION-1107
  Original statement (presumption under test): A monitoring task's successful action (a ping, a prior PASS, a registry entry) is a valid measure of the outcome the task exists to secure.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1107
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across three sessions; generalises PRESUMPTION-890.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial (conditional only)

  Sources:
    1. Beyer, Jones, Petoff & Murphy (eds.), 2016. *Site Reliability Engineering*, Ch. 6 "Monitoring Distributed Systems" (Rob Ewaschuk). https://sre.google/sre-book/monitoring-distributed-systems/ [search-result] — Black-box monitoring "tests externally visible behavior as a user would see it" and is symptom-oriented ("the system isn't working correctly, right now"). This is conditional support: a synthetic probe *is* a valid outcome measure when it exercises the same path and success criterion as the real outcome. The same chapter recommends alerting on user-facing symptoms rather than internal proxies.
    2. Prentice, R. L., 1989. "Surrogate endpoints in clinical trials: definition and operational criteria." Statistics in Medicine 8 [search-result via JCI reference list and MRC/UHasselt documents] — Sets out formal conditions under which a surrogate validly stands in for the true endpoint. This gives theoretical grounding that a proxy *can* be valid, but only after those criteria are shown to hold.
    3. Fleming, T. R. & DeMets, D. L., 1996. "Surrogate end points in clinical trials: are we being misled?" Annals of Internal Medicine [search-result; bibliographic details partly background-knowledge] — Cited for the CAST trial, where the surrogate (arrhythmia suppression) improved while mortality rose. This is a cautionary source. It is listed for completeness and supports the presumption only in the narrow sense that validated surrogates exist.
    4. Buyse & Molenberghs et al. (meta-analytic surrogate evaluation; Buyse 1998 PDF; Molenberghs 2022 slides) [search-result] — "A correlate does not a surrogate make." Validity has to be shown empirically.
    5. Manheim, D. & Garrabrant, S., 2018. "Categorizing Variants of Goodhart's Law." arXiv:1803.04585 [search-result] — Defines the Goodhart effect as the collapse of the proxy–goal relationship under optimisation. This implies a proxy can be valid while it is *not* optimised against. That is weak, conditional support.

  Strength of support: Weak

  Summary: The literature supports the presumption only under specific conditions. (i) The monitored action is itself the outcome-producing mechanism. For example, if the platform's own docs say requests to the database prevent pausing, then a successful request is close to the outcome. (ii) The action is an end-to-end black-box probe of the same path and criterion as the real outcome (SRE). (iii) The proxy has been validated against the true outcome, as with Prentice-style surrogate validation. Outside those conditions, every relevant framework (surrogate-endpoint methodology, SRE symptom-based alerting, Goodhart's law) treats an unvalidated proxy as a weak measure. A prior PASS or a registry entry, which are stale or declarative signals, received no support at all.

  Caveats: (a) Evidence comes mainly from medicine and SRE, and transferring it to LLM-agent scheduled tasks is by analogy. (b) The three proxy types differ. A live ping is the closest to valid, a prior PASS is a temporal proxy subject to staleness, and a registry entry measures intent rather than outcome. Support applies, weakly, only to the first. (c) The supportive sources themselves stress validation requirements.

  Search scope: preliminary search (2 searches, 0 fetches); clinical surrogate-endpoint methodology, Google SRE book, Goodhart literature. Broader search recommended (synthetic monitoring vs RUM studies; Campbell's law).

  Recommendation: PARTIALLY-SUPPORTED (conditional; the general form is unsupported)
