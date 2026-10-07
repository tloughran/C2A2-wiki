SEARCH-FOR-ASSUMPTION-1303 (OWED NARROW QUESTION ONLY: does improving precision RESTORE attention to an abandoned channel?):
  Date searched: 2026-10-07
  Original item: ASSUMPTION-1303 (derived question, MONITOR-598; the item itself went INCORPORATE as
    PREMISE-201, limb-split)
  Original statement: A gate whose actionable rate is around 2% (418 hits, single-digit actionable) is a
    gate that will stop being read, and the remedy is threshold amendment.
  Question searched: is there any before/after measurement showing that improving alert precision /
    amending a threshold RESTORES attention (reading or response rate, NOT alert volume) to a channel
    already degraded or abandoned through alarm fatigue? Lanes: clinical alarm/CDS-alert interventions;
    SRE alert precision; signal-detection vigilance at low base rates. Per 15d, a second null counts as a
    finding.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-20; processed 2026-10-07)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: ASSUMPTION-1303
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: ~2%-actionable gate will stop being read; remedy is threshold amendment
      15a (cycle 0, 2026-09-10): PARTIALLY-SUPPORTED; L1 Strong, L2 (remedy) Moderate. Paine et al. 2016
        alarm review; Bessey et al. (Coverity)
      15c: DISPOSITION-923 → INCORPORATE as PREMISE-201; 15b's declared literature gap → MONITOR-598
      15d: re-triggered cycle 1 2026-09-20; owed = before/after restoration-of-attention evidence
      15a (cycle 1, 2026-10-07): 3 searches, 2 fetches; see below
    Current status: PARTIALLY-SUPPORTED (the null is NOT repeated; weak positive evidence found)

  Search scope: 3 web searches (alarm-fatigue interventions with response-rate outcomes; CDS alert
    optimisation with override/acceptance before-after; signal-detection prevalence-effect reversibility).
    2 fetches: Baysari et al. 2021 JAMIA systematic review (abstract plus evaluation table read in full);
    Wolfe & Van Wert 2010 Curr Biol (full text). SRE alert-precision lane: no peer-reviewed before/after
    found in these searches. That lane is effectively UNREACHED again.

  Supporting evidence found: Partial. Before/after measurements of RESPONSE RATE (not just volume) in
    channels with ~85–95% non-response exist, and they show small, inconsistent restoration.

  Sources:
    1. Baysari, M. T. et al., 2021. "Optimizing clinical decision support alerts in electronic medical
       records: a systematic review of reported strategies adopted by hospitals." JAMIA 28(1).
       PMC7810441. [fetched: abstract + Table 4 evaluation results] The primary studies it tabulates are
       the closest thing to the owed measurement:
       - Bhakta et al.: turned off 802 of 875 moderate DDI alerts (27% volume cut). Alerts ACKNOWLEDGED rose
         11.8% → 13.7%; alerts leading to an order modification rose 5% → 7.3%.
       - Simpao et al. 2015 (JAMIA 22:361): deactivated 63 DDI alerts. PHARMACIST override fell
         95.14 → 84.38 per 100 alerts (significant). PROVIDER override was unchanged, 84.22 → 84.91 (n.s.).
       - Parke et al.: severity re-ranking shifted pharmacist override reasons, with "not clinically
         significant" down 22%.
       These are channels at 85–95% override, i.e. functionally near-abandoned, measured on a response
       metric before and after a precision/threshold change. Restoration is real but small for pharmacists
       and absent for providers. That pattern is CONSISTENT WITH PARTIAL HYSTERESIS as much as with
       restoration.
    2. Wolfe, J. M. & Van Wert, M. J., 2010. "Varying target prevalence reveals two, dissociable decision
       criteria in visual search." Current Biology 20(2):121. PMC2818748. [fetched, full text] Prevalence
       was varied sinusoidally (100% → 0% → 100%) over 1,000 trials. The decision criterion TRACKED
       prevalence back up (r = −0.92) with sensitivity unchanged, over an integration window of "about
       four-dozen trials". In the lab, the low-prevalence criterion shift is reversible and roughly
       symmetric, which is the signal-detection analogue of "restore precision → restore responding".
       Same lab (search-result): the prevalence effect is "stubborn" (Wolfe et al. 2007) and is mitigated
       by bursts of high-prevalence trials WITH FEEDBACK.
    3. Paine et al. 2016, J Hosp Med (alarm review), plus the burn-ICU and PICU QI studies. [search-result]
       Interventions cut alarm volume 75–82% with sustained effect, and nursing SURVEYS reported
       "improved capacity to respond". That is self-report, not a measured response rate, so it is weak.

  Strength of support: Weak to Moderate. Real before/after response-rate data exist, but the effects are
    small and role-dependent. The cleanest reversibility evidence is laboratory and short-timescale.

  Summary: The owed measurement is not wholly absent. Hospital CDS optimisation studies measured
    acknowledgement/override rates before and after cutting low-value alerts, in channels where 85–95% of
    alerts were overridden. Response improved modestly for some users (pharmacist overrides 95% → 84%;
    acknowledgement 11.8% → 13.7%) and not at all for others (providers flat at ~84%). Signal-detection
    work shows that the criterion shift caused by low prevalence reverses when prevalence is restored,
    within tens of trials, in a lab with feedback. Together: precision improvement can restore some
    attention, partially and unevenly. The provider null fits the hysteresis concern in MONITOR-598.
    Nothing found shows FULL restoration of a documented-abandoned channel.

  Caveats: (i) "High override" is not the same as "abandoned/unread". Overriding is a response, so these
    channels were still being seen. The strict "abandoned channel" condition in MONITOR-598 is
    approximated, not met. (ii) The primary studies (Bhakta, Simpao, Parke) were read only through the
    review's table. (iii) Lab prevalence studies use feedback on every trial. Real channels, including the
    estate's gate, lack trial-level feedback, and that is the condition under which the effect is
    "stubborn". (iv) The SRE lane is unreached on two consecutive passes. (v) Publication bias: QI studies
    reporting no improvement are less likely to be published.

  Recommendation: PARTIALLY-SUPPORTED. For MONITOR-598 this is NOT a clean second null. It is weak evidence
    of partial, role-dependent restoration and is equally readable as partial hysteresis. Either way it
    favours PREMISE-201 clause (3)'s "pair the amendment" over "amend alone". Per 15d's instruction, no
    third literature pass is recommended; re-route as an in-house before/after series on the 418-hit gate
    (measure read/act rate, not hit count).

  NOVELTY-FLAG: No.
