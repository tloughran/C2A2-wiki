SEARCH-FOR-ASSUMPTION-1149:
  Date searched: 2026-08-19
  Original item: ASSUMPTION-1149
  Original statement: The literature-search intake queue held thirteen items no parser was looking at:
    "they live in a one-line-per-item format the queue's own parser misses", and "Three different parses
    of the queue file give three different backlog figures." The queue's depth has never been a measured
    quantity.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1149
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the hidden-item discovery, the three-parse divergence, and the standing 07-21
        residue of 26 unsearched items.
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "DeepParse: Hybrid Log Parsing with LLM-Synthesized Regex Masks." arXiv:2604.20553.
       (author list not verified) — States directly that a single misplaced character can cause *silent*
       parsing failures when manually written regular expressions are used for log analysis. This is the
       exact mechanism ASSUMPTION-1149 describes: a regex-defined reader that fails without signalling.
    2. "LLM4Log: A Systematic Review of Large Language Model-based Log Analysis." arXiv:2604.16359.
       (author list not verified) — Documents *format drift*: log formats change as code evolves,
       dependencies upgrade, and developers revise wording, so an initially accurate template inventory
       becomes stale, producing template fragmentation (one event split across templates) or erroneous
       merges. Directly supports the claim that heterogeneous record formats accumulate in long-lived
       append-only records and defeat a fixed parser.
    3. "Characterizing and Fixing Silent Data Loss in Spark-on-AWS-Lambda with Open Table Formats."
       arXiv:2604.20081. (author list not verified) — Establishes the general class: pipeline steps that
       silently degrade or drop data while the job reports success. Supports the "invisible work items"
       limb, i.e. that absent records leave no error trace.
    4. Grey/practitioner literature on schema drift and dead-letter queues (Netwrix "Dark data" briefing;
       "Dead Letter Queue Triage Checklist," Moments Log; "Silent Data Loss in ClickHouse," Medium) —
       Consistently report that (a) an absent or implicit schema produces silent rather than loud errors,
       (b) failed/unparsed items accumulate as a quiet backlog nobody has inventoried, and (c) the risk is
       not the single failure but that nobody knows what the unread items represent. These are grey
       sources; they corroborate the pattern but do not establish rates.

  Strength of support: Moderate-to-Strong

  Summary: The two claimed mechanisms are separately well attested in the log-analysis and data-pipeline
  literature. First, regex-defined readers over semi-structured records fail silently: DeepParse
  (arXiv:2604.20553) states that one misplaced character suffices, with no error raised. Second, formats
  in long-lived append-only records drift, and drift produces both fragmentation and erroneous merges
  (LLM4Log, arXiv:2604.16359) — which is precisely why three parses of one file can return three
  different counts without any of them being buggy in the ordinary sense. The claim that a backlog can
  exist without ever having been a measured quantity is the standard "silent data loss / dark data"
  finding: absence of a record leaves no signal, so the true denominator is unavailable by construction.
  Support for the *general mechanism* is strong; support for the *specific vault instance* is by analogy
  only, since no source studies a markdown-based agent work queue.

  Caveats: All sources are drawn from machine-generated log analysis and data-ingestion pipelines, not
  from human-and-agent-authored prose work queues; the domain transfer is plausible but untested. None of
  the sources quantifies how often multi-parse divergence occurs, so the "three parses, three figures"
  observation is supported as a known failure mode rather than as a rate. The two most on-point arXiv
  items are recent preprints whose peer-review status was not verified. Search scope: preliminary —
  covered log parsing, schema drift, silent data loss, dead-letter queues; did NOT cover the software
  engineering literature on grammar/format specification robustness or the CSCW literature on
  articulation work, either of which may hold stronger evidence.

  Recommendation: SUPPORTED
