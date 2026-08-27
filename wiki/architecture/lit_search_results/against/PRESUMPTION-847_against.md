SEARCH-AGAINST-PRESUMPTION-847:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-847
  Original statement: [inferred] That a terminal marker is an account — that a run which stops
    has thereby explained itself.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-847
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from four identical terminal markers over four different failure surfaces.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Comprehensive across resilience-engineering and operational-forensics
    literature. Queries: "root cause analysis fallacy myth complex systems incident postmortem
    Cook Dekker proximate cause insufficient"; "process killed OOM killer no log entry silent
    exit exit code 137 cron job dies without error message"; "Google SRE monitoring symptom
    versus cause"; "gray failure differential observability". Venues: resilience-engineering
    writing (Cook, Dekker, Allspaw), Google SRE Book, Kubernetes/Linux operational
    documentation and engineering blogs. Date range 1998–2026.
    Gaps: Cook's "How Complex Systems Fail" and Dekker's Field Guide were reached through
    secondary sources quoting them, not through the primary documents; I mark those citations
    accordingly. No quantitative study found on what fraction of scheduler terminations carry
    a diagnostically sufficient marker.

  Challenging evidence found: Yes

  Sources:
    1. Dekker, quoted in "There is no such thing as a root cause [and therefore] there is
       technically no such thing as the beginning of a mishap."
       https://safetyinsights.org/2025/04/06/there-is-no-such-thing-as-a-root-cause-and-therefore-there-is-technically-no-such-thing-as-the-beginning-of-a-mishap-dekker/
       — "What you call 'root cause' is simply the place where you stop looking any further."
       Directly against the presumption: a terminal marker is where the record stops, which is
       an artifact of instrumentation, not a causal claim. SNIPPET-ONLY (secondary quotation
       of Dekker; primary source not retrieved).
    2. Cook, "How Complex Systems Fail," as summarised in SentinelOne, "The Myth of the Root
       Cause: How Complex Web Systems Fail."
       https://www.sentinelone.com/blog/the-myth-of-the-root-cause-how-complex-web-systems-fail-2/
       — Intuitive one-cause-per-outage models fit modern systems poorly; failures emerge from
       confluences of conditions. ABSTRACT-ONLY / secondary summary. [Cook's original essay
       details unverified.]
    3. Allspaw, "Each necessary, but only jointly sufficient." Kitchen Soap, 2012.
       https://www.kitchensoap.com/2012/02/10/each-necessary-but-only-jointly-sufficient/
       — Accidents emerge from combinations of conditions each necessary but only jointly
       sufficient; no single marker carries the explanation. FULL-TEXT.
    4. "exit code 137 — SIGKILL, and why it is not always out-of-memory."
       https://semicolony.dev/errors/exit-code-137
       — The mechanism that makes this presumption dangerous in practice: "SIGKILL gives the
       process no chance to write a farewell," so "the logs typically just stop mid-sentence."
       Moreover the same code is emitted by OOM kills, stop-timeout escalations, CI runners
       and orchestrators — one marker, many causes, requiring an *out-of-band* check
       (dmesg / journalctl -k / the orchestrator's OOMKilled flag) to disambiguate.
       FULL-TEXT. This is a direct empirical counterexample to "a run that stops has explained
       itself": the loudest, most common terminal marker in scheduled-job operations is
       explicitly documented as non-diagnostic on its own.
    5. Practitioner guidance on distinguishing OOM kills from other SIGKILL sources, recovered
       across the exit-137 result set (e.g. https://spacelift.io/blog/oomkilled-exit-code-137,
       https://cast.ai/blog/oomkilled-exit-code-137/) — all of them require consulting kernel
       logs or orchestrator metadata *outside* the job's own output. SNIPPET-ONLY.
    6. Beyer et al. (eds.), 2016. Site Reliability Engineering, "Monitoring Distributed
       Systems." https://sre.google/sre-book/monitoring-distributed-systems/
       — "What versus why is one of the most important distinctions in writing good
       monitoring." The terminal marker answers *what*; the presumption treats it as an answer
       to *why*. FULL-TEXT.
    7. Huang et al., 2017. "Gray Failure." HotOS '17. DOI 10.1145/3102980.3103005.
       — Reinforces that the recorded observation and the actual condition diverge; a marker
       that says "stopped" may coexist with an underlying degradation the marker cannot name.
       ABSTRACT-ONLY.

  Strength of challenge: Strong

  Summary: Two independent literatures converge against this presumption. The resilience-
  engineering tradition (Dekker, Cook, Allspaw) holds that a designated cause is a stopping
  point in an investigation rather than a property of the incident, that failures in complex
  systems arise from jointly sufficient combinations, and that mistaking the proximate trigger
  for the explanation is the characteristic error of postmortem practice. The operational
  literature supplies a hard empirical counterexample: SIGKILL terminations write no farewell
  message, so the log simply stops, and the single most common terminal signature in scheduled
  work — exit 137 — is explicitly documented as ambiguous between OOM kill, stop-timeout
  escalation, and external kill, resolvable only by consulting kernel or orchestrator records
  outside the job. The item's own evidence is decisive here: four identical terminal markers
  over four different failure surfaces is a demonstration that the marker's information content
  about cause is approximately zero. The presumption confuses "the record ends here" with
  "this is why it ended," which is precisely the what/why conflation the SRE literature warns
  against.

  Specific risks: If this presumption is false, C2A2's incident record is systematically
  misleading rather than merely thin. Four different faults are filed under one signature, so
  recurrence looks like a single known issue rather than four unaddressed ones, and any fix
  aimed at the marker will appear to work while three causes remain live. Trend analysis on
  terminal markers will produce confident, wrong conclusions. Because the diagnostically
  decisive evidence (kernel logs, orchestrator kill reasons, memory pressure at the moment of
  death) is out-of-band and time-limited, it is likely to have aged out by the time anyone
  notices, making the failures permanently unexplainable after the fact. And the presumption
  suppresses the search itself: a run that has "explained itself" generates no investigation.

  Mitigations available:
    - Capture out-of-band termination evidence at the moment of death: kernel log grep for
      oom-kill, orchestrator termination reason / OOMKilled flag, exit signal, resident memory
      high-water mark (exit-137 diagnostic guidance, semicolony.dev and the Kubernetes OOM
      literature).
    - Distinguish "the process wrote an ending" from "the process stopped": a run without an
      explicit completion record should be classified as *unexplained*, not as explained by
      its last line. This is the operational form of Dekker's point.
    - Separate what from why in the monitoring design; alert on symptoms, investigate causes
      separately (Beyer et al., SRE Book).
    - Treat postmortems as multi-condition: record contributing conditions rather than a single
      root cause (Allspaw, "each necessary, but only jointly sufficient").
    - Emit periodic in-run progress checkpoints so the *shape* of the truncation (where it
      stopped, how far it got, how long the last step took) carries information the terminal
      marker does not.

  STEELMAN:
    Item: PRESUMPTION-847
    Strongest counterargument: A terminal marker records where the writing stopped, and the
    writing stops for reasons that are frequently the same reasons the process stopped — which
    means the marker is systematically least informative exactly when the failure is most
    severe. A graceful error path can explain itself; a SIGKILL cannot, by construction, and
    the operational literature documents that its logs "just stop mid-sentence." Dekker's
    formulation generalises this: the designated cause is the place the investigator stopped
    looking, not a fact about the world. The item's own observation is the empirical proof —
    if four distinct failure surfaces produce one marker, the marker is a signature of the
    *logging architecture*, not of any of the four causes, and reading it as an account is
    reading a property of the instrument as a property of the event.
    What would need to be true for C2A2 to be safe: (a) every terminal marker is written by
    the run itself on a path that only executes when the run knows why it is ending — i.e.
    markers are affirmative, not inferred from the last line present; (b) runs that end without
    such a marker are automatically classed unexplained and trigger collection of out-of-band
    evidence; (c) the marker vocabulary distinguishes at least as many states as there are
    plausible failure surfaces, so identical markers across different causes are impossible by
    construction; (d) out-of-band evidence (kernel logs, memory, orchestrator reason) is
    retained long enough to be consulted after the delay imposed by items 846 and 1160.
    How to test: Directly and cheaply. Induce four different failures on purpose — SIGKILL
    mid-run, an unhandled exception, an external API timeout, and a credential failure at
    startup — and compare the resulting terminal records. If two or more are
    indistinguishable, the presumption is falsified for those surfaces. Then check, for each,
    whether enough evidence survives 24 hours later to identify which one occurred.

  Recommendation: CHALLENGED
