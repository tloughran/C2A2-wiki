# Pilot Tome — Table of Contents v2 (approved 2026-09-04, with rulings)

Generated 2026-09-04 from `tome_units.csv` / `tome_headings.csv` (A1 extraction, verified) by the seam sweep. **Nothing in `rc_document_explorer.html` has been changed.** Source of truth for this proposal is `toc_v2.csv`; this file is a rendering of it.

## What the sweep found

The current ToC reproduces the heading levels of the ChatGPT export verbatim, and those levels track the model's formatting habits, not the conversation's structure. Measured against the 1,106 paragraphs:

- **102 H1s, of which 87 are not seams.** Most are the model's status lines ("Word Count So Far:", "Current Progress:", "Quick Reassurance:"), each promoted to top level. Only 15 of the 40 chapter boundaries below coincide with an existing H1.
- **Three giant H1s at the front** swallow everything: "Comprehensive Bibliography of Michael Levin" (p.4, 11.3k words) contains the Hoffman, Wolfram, Hawkins, Carroll and Hossenfelder bibliographies as unheaded prose (p.17-40); "Sean Carroll's Critique" (p.41, 15.7k words) contains the Hoffman, Levin, Friston, Wright/Rohr, Fredrickson and Wolfram research agendas as H2/H3; "God's Knowledge ... De Veritate" (p.104, 16.9k words) contains all the MacIntyre, cultural-exchange, authorship and paper-planning material.
- **One giant H1 at the back**: "Revised Structure for Section IV" (p.372, 26.9k words) silently holds the whole Kastrup arc, Deacon, the synergistic coils table, Paper 2 (Resurrecting Thomism), your DCEC draft and the Stump lecture.
- **The seams are your prompts.** They are embedded mid-paragraph ("Let's put a pause on ... add another bio ... Sabine Hossenfelder", "Back from exercise, but I'd like to interject a research project", "I transformed section iv, not v"). None became a heading. Each new seam below quotes the prompt that marks it.
- **Two blocks of your own prose are filed as the model's**: your submitted draft (p.216-220, "Enter Mike Levin...") under "Task Fidelity Check", and your DCEC draft (p.451-457) under an H3 titled "Suggested Next Steps". Both matter for A4 (voice), flagged here so the ToC names them.
- **An authored outline exists inside the source** (p.396-399): at your request the model wrote a five-phase outline of the conversation. The Part layer below adopts its five phase titles verbatim and adds a sixth for everything after p.401, which it predates.
- Heading text was wrapped mid-phrase in 65 places ("Sean Carroll's Critique of Consciousness-Centric" / "Universe Models"); those are reconstituted in `tome_headings.csv` and shown joined here.

## Rules used (candidates for the extractable ToC skill)

1. Top layer = an authored outline if the source contains one; extend, never override.  2. A chapter seam = a change of task, marked by the human turn that requested it; quote it.  3. A section seam within a chapter = a change of dominant figure (name-mention run detection, confirmed by reading the boundary).  4. Existing headings are retained *beneath* the seam they fall under; none deleted, levels re-derived from position.  5. Status/apparatus headings (word counts, ETAs, "Ready when you are") drop to the lowest level, the Sandbox's X division.  6. Anchors are units, so a seam with no heading is still linkable at paragraph precision.

## Tom's rulings (2026-09-04)

1. Granularity: 40 chapters stands.  2. Part V/VI split stands.  3. Digressions (C15, C17) stay chapters, titled "Digression: …".  4. Tom's two draft blocks are titled "Experiments in co-authorship: …" (C19, C38).  5. Status headings: my call — **123 headings classified `apparatus`** in `tome_headings.csv` (`toc_role` column; rule: title matches a status/ETA/word-count/next-step pattern, or is a ≤4-word label ending in ":", AND carries <250 words of prose beneath it, AND is not on the content whitelist — Corrected Restatement, Ultimate Model, Brutal Reply, Task Fidelity Check, My Recommendation). 502 remain `structural`. **UI**: apparatus headings are hidden from the sidebar by default behind a per-chapter "working apparatus (n)" disclosure, in muted type; they keep their anchors so shelfmarks and old links resolve; the ToC filter box searches them too. Rationale: they are the conversation's scaffolding, worth preserving for provenance and useless for navigation.

## ToC v2

Format: `pages | words | anchor` then the evidence/note. Anchor is an existing heading id where one begins the span, else the first unit id.


## P1. Project Launch and Research Foundations  (p1-40, 11,497 words)

*authored outline, phase I (p396)*

### C1 Opening: an AI-ethics mind map
`p1-3 | 214w | tome:p001h00s01 | 0 existing headings inside`  
Tom: "Can you draw a mind map for AI ethics"

### C2 Bibliographic deep dives, thinker by thinker
`p3-40 | 11,399w | tome:p003h00s03 | 19 existing headings inside`  

- **S1 Michael Levin: comprehensive bibliography and overview** — `p3-16 | 4,825w | tome:p003h00s03` — existing H1 p4; Tom p16: "Now, based on these sources, can you provide a 1000 word overview"
- **S2 Donald Hoffman: bibliography, biography, podcasts** — `p17-23 | 1,938w | tome:p017h00s05` — NEW SEAM. No heading. Tom p17: "Yes, please do, but expect to backfill each section with his more recent work"
- **S3 Stephen Wolfram: biography, works, podcasts** — `p24-26 | 819w | tome:p024h00s12` — NEW SEAM. No heading. Model p24: "Stephen Wolfram is a distinguished computer scientist..."
- **S4 Jeff Hawkins: books, career, podcasts** — `p27-30 | 1,135w | tome:p027h00s15` — NEW SEAM. No heading. p27 "Books: 1. On Intelligence"; Tom p28: "you left out his podcast appearances"
- **S5 Sean Carroll: publications, Mindscape, biography** — `p31-37 | 1,941w | tome:p031h00s19` — NEW SEAM at p31 (Tom: "top 100 guests ... Mindscape ... After this fifth research set"); existing H3s p33-37 were filed under Levin
- **S6 Sabine Hossenfelder: a leading critic** — `p38-40 | 741w | p38-biography` — Tom p38: "Let us put a pause ... add another bio, not of a leading contributor but a leading commentator/critic"; existing H3 "Biography" p38 was under Levin

## P2. Framework Integration and Thematic Convergence  (p41-103, 15,721 words)

*authored outline, phase II*

### C3 Sean Carroll's critique of consciousness-centric universe models
`p41-53 | 4,346w | p41-sean-carroll-s-critique-of-consciousness | 8 existing headings inside`  
existing H1 p41 (wrapped heading, reconstituted); includes QHT vs WPP comparison p51-53

### C4 Current and potential research agendas, thinker by thinker
`p54-100 | 10,424w | p54-structure-for-each-thinker | 69 existing headings inside`  
Tom p54: "Now let us look over all these thinkers and their programs, using the lens of current actionable research"
- **S7 Structure (for each thinker)** — `p54 | 255w | p54-structure-for-each-thinker` — existing H3
- **S8 Donald Hoffman: research agenda** — `p55-58 | 937w | p55-donald-hoffman-current-and-potential-res` — existing H2, was buried under Carroll H1
- **S9 Michael Levin: research agenda; basins of morphological attraction** — `p59-63 | 1,125w | p59-michael-levin-current-and-potential-rese` — existing H2 + H3s
- **S10 Karl Friston: biography and scientific contributions** — `p64-67 | 872w | p64-conceptual-formalism-potential` — existing H2; Tom p64 pivot "shall we pivot now to..."
- **S11 Levin x Friston: extensions via free energy and least action** — `p68-70 | 608w | p68-potential-extensions-of-levin-s-research` — existing H2 (reconstituted)
- **S12 Toward a theory of communal active inference and morphogenesis** — `p71-76 | 984w | p71-toward-a-theory-of-communal-active-infer` — existing H2 (reconstituted)
- **S13 Theological reframing: N.T. Wright, Richard Rohr, Christic morphogenesis** — `p77-84 | 1,684w | p77-community-morphogenesis-and-the-body-of` — existing H2 p77; Tom p78: "Now, let us integrate this with theological language drawn from N.T. Wright and Richard Rohr"
- **S14 Barbara Fredrickson: biography, podcasts, Love 2.0** — `p85-91 | 1,814w | p85-step-1-bio-bibliography-of-barbara-fredr` — existing H2 "Step 1: Bio/Bibliography of Barbara Fredrickson"; Tom p85 "I will peel out..."
- **S15 Reframing love across scientific and theological registers** — `p92-96 | 1,287w | tome:p092h00s02` — existing H2 p93; Tom p92-93 poses the three questions
- **S16 Stephen Wolfram: research agenda** — `p97-100 | 858w | p97-stephen-wolfram-current-and-potential-re` — existing H2; Tom p97: "Now let us proceed" to Wolfram

### C5 Reflecting on the turn: from synthesis to truth-seeking
`p101-103 | 951w | p101-reflecting-on-the-turn-from-synthesis-to | 2 existing headings inside`  
existing H2 p101; Tom p101: "I will want to draw on work by Alasdair MacIntyre and Thomas Aquinas. But first, let us pause to reflect on this change of direction"

## P3. Methodological Strategy: Synergistic Planks and Traditions-in-Dialogue  (p104-167, 16,751 words)

*authored outline, phase III*

### C6 Aquinas, De Veritate q.2 a.14: God's knowledge as the cause of things
`p104-107 | 1,506w | p104-god-s-knowledge-as-the-cause-of-things-i | 3 existing headings inside`  
existing H1 (reconstituted)

### C7 Designated perspective, mind-to-mind correspondence, synergy planks
`p108-121 | 3,049w | tome:p108h00s03 | 18 existing headings inside`  
existing H2s I-IV p109-111 (wrapped, reconstituted) + plank template Step 1/Step 2

### C8 Summary of progress and strategic positioning
`p122-124 | 653w | p122-summary-of-progress-and-strategic-positi | 13 existing headings inside`  
existing H2 p122

### C9 MacIntyre: traditions as social information processors; toward a tradition of inquiry
`p125-139 | 3,933w | p125-1-a-co-constitutional-dialogue | 14 existing headings inside`  
Tom p125: "Let us proceed to weave in MacIntyre"; existing H2s 1-4, Summary Reflection, CNL summary, Next Steps

### C10 Two uploaded papers: Four Models of Cultural Exchange; Computational Natural Law
`p140-144 | 1,505w | p140-document-1-four-models-of-cultural-excha | 9 existing headings inside`  
existing H2 Document 1 / Document 2; Tom p140 uploads the PDFs

### C11 Reframing the arc: game and team; two amendments; adjusted working framework
`p145-150 | 1,440w | p145-reflection-and-confirmation-of-your-refr | 8 existing headings inside`  
existing H2s p145-149

### C12 Authorship, AI collaboration, and the graduate-student analogy
`p151-163 | 3,604w | p151-1-affirmation-of-your-strategic-progress | 16 existing headings inside`  
Tom p151: "I had an outline, not yet shared with you, of each of two papers"; existing H2s p151-162

### C13 The immediate paper project and a working structure
`p164-167 | 1,061w | p164-understanding-your-immediate-paper-proje | 9 existing headings inside`  
existing H2 p164 "Understanding Your Immediate Paper Project"

## P4. Structural Refinement and Presentation Development  (p168-371, 46,291 words)

*authored outline, phase IV*

### C14 The reformulated thesis: Being, Life, Intelligence (BLI)
`p168-172 | 1,258w | p168-step-1-comparing-your-reformulated-thesi | 8 existing headings inside`  
existing H1 "Step 1: Comparing Your Reformulated Thesis"

### C15 Digression: podcast appearances by pair; Iain McGilchrist added
`p173-185 | 2,716w | tome:p173h00s03 | 6 existing headings inside`  
Tom p173: "Back from exercise, but I would like to interject a research project"; McGilchrist bio p179 (existing H3s); revised joint table p181

### C16 Mapping an emerging interdisciplinary network, 2014-2024 (deep research)
`p186-198 | 4,447w | p186-mapping-an-emerging-interdisciplinary-ne | 8 existing headings inside`  
existing H1 (reconstituted)

### C17 Digression: the output-files gap — task fidelity, self-critique, working protocols
`p199-211 | 2,673w | tome:p199h00s03 | 15 existing headings inside`  
Tom p199: "Have I missed links to the two output documents?"; model p203: "Let me be very direct"; p205-210 protocols

### C18 Dataset of documented connections and a first sociogram
`p212-215 | 854w | p212-intellectual-relationships-among-selecte | 4 existing headings inside`  
existing H1 p212; Tom p212: "aim at the scientific dataset. Remove Rohr and Wright"

### C19 Experiments in co-authorship: the submitted draft (Intro + Sections I-II) and the cold critical review
`p216-229 | 4,316w | tome:p216h00s03 | 20 existing headings inside`  
NEW SEAM p216. Tom: "Let us put a pin in this portion of the research, and move on to the paper. I have thus far written an introduction and section 2"; his draft prose runs p216-220 ("Enter Mike Levin..."), VOICE=TL — confirmed by the model at p221: "You fulfill the planned content for the Introduction, Section I, and Section II"; existing H1s Task Fidelity Check, Cold Critical Review

### C20 Critical action plan; rewritten Introduction and Sections I-II
`p230-242 | 2,194w | p230-6-preempt-rival-interpretations-briefly | 28 existing headings inside`  
existing H1s p228-238 (Critical Action Plan, Rewritten Introduction/Section I/II)

### C21 Plan for the full paper: structure, target, work method
`p243-254 | 2,237w | p243-here-s-the-plan | 18 existing headings inside`  
Tom p243 approves expanding the outline; existing H1s Here is the Plan / Work Method

### C22 Section 1 draft and the corrected restatement of the model
`p255-268 | 3,182w | p255-section-1-introduction-and-initial-objec | 17 existing headings inside`  
Tom p255: "Yes, do show me section 1"; existing H1 Section 1; Corrected Restatement / Ultimate Model p264-266

### C23 Section 2: thinker profiles
`p269-298 | 5,992w | p269-michael-levin | 45 existing headings inside`  
Tom-approved profiles: Levin, Hoffman (+NAH revision), Wolfram, Hawkins, Friston, McGilchrist, Fredrickson; assembled Parts 1-2 p290-298
- **S17 Levin and Hoffman profiles** — `p269-273 | 1,252w | p269-michael-levin` — existing H1s p269-272
- **S18 Wolfram and Hawkins profiles** — `p277-279 | 710w | p277-stephen-wolfram` — existing H1s
- **S19 Friston, McGilchrist, Fredrickson profiles** — `p283-289 | 1,203w | p283-karl-friston` — existing H1s
- **S20 Section 2 assembled: Part 1 (Levin, Hoffman, Wolfram, Hawkins), Part 2 (Friston, McGilchrist, Fredrickson)** — `p290-298 | 1,977w | p290-summary` — existing H1s Section 2 Part 1 / Part 2 (reconstituted)

### C24 Section 1 rewritten; remaining work plan
`p299-308 | 2,041w | p299-next-step | 13 existing headings inside`  
Tom p299: "Yes, please do that rewriting quickly ... then revisit the brutal reply set"

### C25 Brutal replies reframed; revised scope; the 20-minute outline
`p309-319 | 2,338w | p309-brutal-reply-1-reframed | 19 existing headings inside`  
existing H1s Brutal Reply #1/#2, Revised Scope, New Brutally Precise Outline

### C26 Wireframe first draft and self-evaluation
`p320-326 | 1,399w | p320-wireframe-first-draft-conscious-realism | 14 existing headings inside`  
Tom p320: "Let us sketch a wireframe first draft"

### C27 Draft prose: Introduction (two passes), II, III, IV (two versions), V, VI
`p327-346 | 5,240w | p327-draft-introduction-full-prose-alive-with | 16 existing headings inside`  
existing H1s p327-346

### C28 ACPQ submission: guidelines, abstract, objections and responses, targeted revisions, footnotes
`p347-371 | 5,404w | p347-acpq-submission-guidelines-key-requireme | 30 existing headings inside`  
existing H1 ACPQ Submission Guidelines p347; footnotes 4-8 p367; Carroll-dominant p369-371

## P5. Section IV Rewrite, Formatting, and Compliance  (p372-401, 7,421 words)

*authored outline phases IV (Section IV rewrite) and V (formatting)*

### C29 Revised Section IV: scholars table, individual summaries, interactions
`p372-381 | 2,604w | p372-revised-structure-for-section-iv-empiric | 5 existing headings inside`  
Tom p372: "brief introduction to each, alone ... then a separate paragraph highlighting interactions"; existing H1 is the 27k-word catch-all

### C30 Section IV replaces IV (not V); Section V restored and revised
`p382-388 | 2,069w | p382-your-objective | 4 existing headings inside`  
Tom p382: "I transformed section iv, not v, and it should replace section iv"

### C31 Manuscript formatting, footnotes (MacIntyre 3RV, Arkani-Hamed), ACPQ export
`p389-395 | 1,374w | tome:p389h00s05 | 9 existing headings inside`  
Tom p389: "Let us add a couple of footnotes"; p393 Arkani-Hamed footnote

### C32 Outline of the conversation's main phases; stages plan for what follows
`p396-401 | 1,374w | p396-outline-of-the-main-phases-of-the-conver | 17 existing headings inside`  
Tom p396: "reload this entire conversation, and add to it an outline of its main phases"; Tom p401 sets Stages 1-4

## P6. Extending the Cluster and the Second Paper  (p402-471, 17,025 words)

*beyond the authored outline (which ends at p401)*

### C33 Bernardo Kastrup: biography, thought, relations to each researcher, integration, conversations
`p402-415 | 2,730w | p402-next-steps-after-the-first-4-stages | 45 existing headings inside`  
Stage 1 (a)-(e); existing H2/H3s p402-415

### C34 Alignment test: truth within the CR paradigm versus Kastrup
`p416-421 | 1,562w | p416-clarifying-the-alignment-task | 10 existing headings inside`  
Tom p416 asks how truth is understood in the CR paradigm

### C35 Synergistic coils: the PRS table; one coil, multiple rows
`p422-424 | 622w | p422-alignment-check-restating-the-synergisti | 6 existing headings inside`  
Stage 2; existing H3s

### C36 Terrence Deacon: biography, core concepts; brainstorm in brutal mode
`p425-436 | 2,823w | tome:p425h00s02 | 27 existing headings inside`  
existing H3 Biography p426; Tom p428: "I would like to brainstorm a bit here"

### C37 Paper 2: Resurrecting Thomism at the dawn of the CR paradigm (DCEC)
`p437-449 | 3,231w | p437-project-goal-as-i-understand-it | 26 existing headings inside`  
Tom p437 sets the goal; abstract p439; Kastrup/Friston/Walker parallels p443-445

### C38 Experiments in co-authorship: the DCEC draft text
`p450-457 | 3,002w | p450-suggested-next-steps | 1 existing headings inside`  
NEW SEAM. Tom p450: "Let me re-present here not only the outline, but substantially more content"; VOICE=TL; currently filed under H3 "Suggested Next Steps"

### C39 Response to the draft; status of the two papers; Introduction revised
`p458-463 | 1,514w | p458-initial-response-and-overview | 12 existing headings inside`  
existing H3s p458-462

### C40 Eleonore Stump's 2025 Maritain Lecture; twenty rich communities
`p464-471 | 1,541w | tome:p464h00s03 | 3 existing headings inside`  
existing H3s p464-471; Tom p468 upload attempt

## P7. Appendix: Works Consulted  (p472, 2,516 words)

*page marker page-appendix; 128 bibliography units; 22 unclassed h4 headings*

## Not done
No change to `rc_document_explorer.html`. No commit. Next increment: render this ToC in the explorer sidebar (local HTTP review before push), then apply the same skill to the Sandbox.