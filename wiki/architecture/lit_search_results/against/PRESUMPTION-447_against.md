SEARCH-AGAINST-PRESUMPTION-447:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-447
  Original statement: "[inferred] That snippet-level screening establishes source novelty when the primary source is unfetchable."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-447
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from search-session behavior that novelty judgments about a source were being made from snippets/abstracts because the primary document could not be fetched
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Gartlehner, G. et al., 2020. "Error rates of human reviewers during abstract screening in systematic reviews." (PMC6959565 / PubMed 31935267). — Human reviewers screening on titles/abstracts alone falsely exclude relevant studies at material rates; single-reviewer abstract screening is a known weak filter.
    2. Meta-research study (J Clin Epidemiol, 2026): "Evaluating the accuracy of screening titles and abstracts... one vs two independent reviewers." — Single-reviewer sensitivity for progression to full text ranged 48.8%–66.3% in some reviews; even optimistic literature reports 86.5%–97.5% sensitivity, meaning snippet-level judgments miss relevant content in a non-trivial fraction of cases.
    3. Li, G. et al., 2017. "A scoping review of comparisons between abstracts and full reports in primary biomedical research." BMC Med Res Methodol (PMC5747940). — Median 39% inconsistency (range 4%–78%) between abstracts and full texts; major inconsistencies median 19%. What the snippet says is frequently not what the paper says.
    4. "Do not make clinical decisions based on abstracts of healthcare research: A systematic review." J Clin Epidemiol, 2021. — Systematic review concluding abstracts alone are an unsafe basis for substantive judgments; conclusions in abstracts are often stronger than the full text supports.
    5. Gianola, S. et al., 2022. "Spin of information and inconsistency between abstract and full text in RCTs investigating upper limb rehabilitation after stroke." — Documents spin: abstracts overemphasize findings relative to full text; 22% of trials with nonsignificant results showed high spin in conclusions.
    6. ReadCube, "Why Abstracts Aren't Enough: The Case for Full-Text Access." — Practitioner synthesis of the above: abstract-level screening systematically misrepresents novelty and contribution claims.

  Strength of challenge: Strong

  Summary: The systematic-review methodology literature directly challenges snippet-level novelty screening. Abstract-vs-full-text comparison studies find a median 39% inconsistency rate, and novelty/contribution claims are exactly the abstract elements most subject to spin — authors overstate what is new. Screening-accuracy studies show single-pass title/abstract screening misses relevant content at rates from a few percent to over 50% depending on protocol. Web snippets are strictly worse than abstracts (shorter, algorithmically excerpted, often from secondary pages), so these figures are a floor on the error rate. The challenge is proportionate to use: as a triage step snippet screening is legitimate and standard; as the terminal basis for asserting "this source is/is not novel" in an evidence-bearing wiki, it is unsupported. The item's LOW criticality is consistent with this — the practice fails as a confirmation, not as a filter.

  Specific risks: A source judged "not novel" from a snippet may contain a genuinely new claim in its body (false negative), or a source ingested as novel may merely re-describe known work with spun abstract language (false positive), contaminating the wiki's provenance chain; downstream triangulation (see ASSUMPTION-024) then counts a misclassified source as an independent line of evidence.

  Mitigations available: Tag any novelty judgment made without full-text access as PROVISIONAL with an explicit "snippet-only" provenance flag; retry primary fetch via alternate routes (DOI resolver, preprint servers, archive.org, library MCP tools) before concluding unfetchability; require full-text confirmation before the source is cited as load-bearing evidence; periodic re-fetch sweep of snippet-only items.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-447
  Strongest counterargument: Novelty is precisely the property snippets are worst at establishing: it requires comparing a paper's actual contribution against the existing corpus, while abstracts and search snippets are marketing surfaces that overstate contribution (spin literature: median 39% abstract/full-text inconsistency, conclusions routinely stronger than the body supports). The systematic-review field — the discipline that has studied this exact question for decades — mandates full-text screening before inclusion decisions and explicitly warns against acting on abstracts, and web snippets carry even less information than abstracts. An evidence-bearing system that records "novel" on snippet evidence is therefore encoding a judgment the methodological literature says cannot be made from that input.
  What would need to be true for C2A2 to be safe: Snippet-based novelty calls must be marked provisional and non-load-bearing until full text is obtained; no downstream claim may cite a snippet-only source as confirmed evidence.
  How to test: Sample past snippet-only novelty judgments, obtain full texts, and measure the reversal rate; if it approaches the literature's ~19–39% inconsistency band, the provisional-flag protocol is mandatory.
