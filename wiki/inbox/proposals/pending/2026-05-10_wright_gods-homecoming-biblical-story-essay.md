---
proposal_id: PROP-2026-05-10-002
thinker: N.T. Wright
tradition_key: wright
source_type: blog
source_title: "God's Homecoming: The Biblical Story We Were Never Taught"
source_url: https://ntwrightpage.com/2026/03/04/gods-homecoming-the-biblical-story-we-were-never-taught/
source_date: 2026-03-04
searched_on: 2026-05-10
status: pending
---

## Summary
Primary-source essay by Wright on his official site, posted ~2 weeks after the *God's Homecoming* book release. Functions as the public-facing distillation of the book's central argument: that the inherited "biblical story" most Western Christians have absorbed (creation → fall → individual salvation → soul goes to heaven) is *not* the story the canonical texts actually tell when read in second-temple-Jewish context, and that the story they do tell is structured by God's homecoming-to-creation rather than by the soul's escape from it. The essay is short, polished, citable, and explicitly addresses the *catechesis problem*: why the wrong story has been taught for so long, and what the corrective looks like when applied at sermon and pastoral scale. Likely to circulate widely as a teaching text in 2026–27.

## Why This Matters for This Tradition
Two reasons. First: it gives us a primary, *short* Wright text from 2026 that the Summa-2026 daily-batch agent can cite when it needs Wright's voice without quoting an entire book. Second, and more importantly: the essay foregrounds the *catechetical / pedagogical* dimension of the homecoming reframe — why the wrong story stuck, and how the right story has to be re-taught. This is directly relevant to the C2A2 project's own architecture: the Karpathy-style tradition wikis are themselves a catechetical apparatus, and Wright's reflection on what it takes to dislodge a deeply-embedded but malformed received story is methodologically applicable to the C2A2 project's own pedagogy. Sharpens the wright-wiki active research question on five-act faithful improvisation as a model for AI-agent extension of inherited research programs.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Even when a research program (or a religious tradition) has access to a more accurate articulation of its founding texts, the inherited *malformed* version persists for generations because catechesis operates below the level of explicit argument. Simply publishing the corrective is insufficient.
  Resource: Wright's essay on *why* the wrong biblical story has been taught for so long: the catechetical apparatus (sermons, hymns, popular books, devotional literature) was built around the wrong frame and continues to reinforce it even when the underlying scholarship has moved. He proposes a replacement-catechesis strategy, not just replacement-scholarship.
  Solution: A model for how to upgrade a research program's *received version* — not by publishing better arguments but by replacing the catechetical apparatus that transmits the received version. Direct application to C2A2: the wiki agents are the catechetical apparatus for the research programs, and their job is exactly this kind of patient, sustained replacement.
  Confidence: High
  Evidence: Wright's explicit framing in the essay; corroborated by his lifelong engagement with both academic and popular audiences (e.g., the parallel academic / popular publication strategy of the *Christian Origins* series alongside *For Everyone* commentaries).

PRS-CANDIDATE-02:
  Problem: The C2A2 project's master agent needs a way to detect when a tradition's "official" claim has drifted from its founding texts (i.e., when the catechesis no longer matches the scholarship). Currently the master agent has no formal way to flag such divergences.
  Resource: Wright's diagnostic moves in the essay — pointing out the specific places where the received story (souls-go-to-heaven) is supported by *no canonical text actually read in context* and is in fact contradicted by texts the tradition takes as central (e.g., Romans 8, Revelation 21).
  Solution: A diagnostic protocol for the master agent: when a tradition's wiki claim is challenged, check whether the claim is supported by the program's founding texts read in *their* context, not in the tradition's later context. Operationalizes Wright's critical-realist hermeneutic as a master-agent quality-control method.
  Confidence: Medium
  Evidence: Wright's essay's argumentative structure; the broader critical-realist methodology in *The New Testament and the People of God*.

## Cross-Tradition Signals
- **MacIntyre (strong):** Wright's "we have been catechized into a malformed received story" is structurally identical to MacIntyre's "epistemological crisis" diagnosis — a tradition's standard self-narration has come into conflict with its own founding texts, and resolution requires returning to the founding texts in their original context, not refining the received story. Strong convergence; recommend the macintyre agent be flagged.
- **Stump (medium):** Stump's hermeneutic of biblical narrative-as-source-of-knowledge benefits from Wright's catechesis-correction frame — *which* narrative is being absorbed matters as much as *that* narrative is being absorbed.
- **Loughran / C2A2 master (strong):** Wright's catechesis diagnostic is directly applicable to the C2A2 wiki agents' job; the master agent should consider adopting a "context-of-source-vs-context-of-tradition" check as a routine quality-control move on tradition wiki claims.
- **Summa 2026 (direct relevance):** Wright's catechesis-replacement strategy is the precise methodology of the Summa 2026 project itself — re-presenting the canonical text in 2026 contemporary-science context to produce a corrective catechesis. Flag for the synthesis agent as a meta-methodological warrant.

## Agentic Calls
*Added by Sewing Agent on 2026-05-10*

[→ Loughran / C2A2 master agent]: PRS-CANDIDATE-02 here proposes a master-agent quality-control protocol: when a tradition's wiki claim is challenged, check whether the claim is supported by the program's *founding* texts read in *their* context, not in the tradition's later context. Action: operationalize this as a routine check in the master agent's revision flow. Specifically — add a "context-of-source-vs-context-of-tradition" diagnostic to `architecture/provenance_protocol.md` so that any wiki claim flagged for revision triggers a founding-texts-in-original-context audit before any catechesis-level edit lands.

[→ Wright agent]: This is a 2026-03-04 short, polished, citable Wright essay distilling *God's Homecoming*'s central argument. Action: ingest as a primary 2026 Wright text the Summa-2026 daily-batch agent can cite without quoting an entire book; create `traditions/wright/2026_gods_homecoming_essay.md` with the essay's argumentative spine and link it from the wright wiki anchor. The catechesis-replacement frame (PRS-CANDIDATE-01) should be promoted to a wright-wiki active-research-question alongside the existing five-act faithful-improvisation question.

[→ MacIntyre agent]: The proposal's strong cross-tradition flag here is exact: Wright's "we have been catechized into a malformed received story" is structurally identical to MacIntyre's epistemological-crisis diagnosis, and the resolution Wright proposes (return to founding texts in original context, not refinement of the received story) is MacIntyre's prescription. Action: cross-link from `traditions/macintyre/` to this essay as a contemporary working example of epistemological-crisis repair, and propose `synthesis/macintyre_wright_bridge.md` framing catechesis-replacement as the operational mechanism by which a tradition recovers from internal crisis.

[→ Stump agent]: PRS-CANDIDATE-02's diagnostic move — pointing out where the received story is supported by no canonical text actually read in context — is methodologically adjacent to Stump's biblical-narrative epistemology. Action: review Stump's *Wandering in Darkness* methodology for compatibility with Wright's "context-of-source" diagnostic; a synthesis page on second-person narrative knowledge + critical-realist context-reading would consolidate two parallel hermeneutical commitments into a single cross-tradition method.
