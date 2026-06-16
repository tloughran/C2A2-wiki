SEARCH-FOR-ASSUMPTION-316:
  Date searched: 2026-06-12
  Original item: ASSUMPTION-316
  Original statement: "Session-scoped (provenance-clean) commits keep repository provenance clean and the repo healthy."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-316
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption from 2026-06-11 EOD session
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Herzig, Kim, and Andreas Zeller. 2013. "The Impact of Tangled Code Changes." In Proceedings of the 10th Working Conference on Mining Software Repositories (MSR 2013), pp. 121–130. IEEE. — Herzig and Zeller define "tangled commits" as commits that group together several unrelated activities (e.g., fixing a bug and adding a new feature in a single commit). Their empirical analysis of real-world repositories found that composite commits account for 11–40% of real-world commits and introduce measurable distortions in defect prediction models, bug counting, and change traceability. The converse — atomic, cohesive commits addressing a single concern — preserves traceability and repository provenance. Session-scoped commits that bundle only session-related changes are the provenance-clean analogue of Herzig and Zeller's recommended atomic commits.

    2. Herzig, Kim, Sascha Just, and Andreas Zeller. 2016. "The Impact of Tangled Code Changes on Defect Prediction Models." IEEE Transactions on Software Engineering 42(12): 1200–1212. — This extended study found a 6–50% error rate (harmonic mean 17%) when applying bug-counting models to repositories containing composite commits versus atomically split commits, quantifying the downstream provenance harm. Clean, atomic commits are demonstrably necessary for reliable software analytics and repository health — directly supporting the assumption that session-scoped provenance-clean commits maintain repo health.

    3. Swicegood, Travis. 2008. Pragmatic Version Control Using Git. Pragmatic Bookshelf. — This widely-used practitioner text articulates the industry consensus that commits should be atomic: each commit should represent a single, self-contained logical change. Atomic commits are easier to review, bisect, revert, and understand, all of which contribute to repository health. The principle is stated as a best practice across Git workflows.

    4. Loeliger, Jon, and Matthew McCullough. 2012. Version Control with Git, 2nd ed. O'Reilly Media. — O'Reilly's standard Git reference explicitly recommends cohesive commits — each representing one logical unit of work — as fundamental to maintaining a clean and navigable project history. The emphasis on commit cohesion as a repository health practice directly supports the assumption that session-scoped, provenance-clean commits maintain repo health.

    5. Zeller, Andreas. 2009. Why Programs Fail: A Guide to Systematic Debugging, 2nd ed. Morgan Kaufmann. — Zeller's discussion of delta debugging and change isolation presupposes atomic, semantically coherent commits: his automated debugging techniques require that individual commits represent single, logically coherent changes so that faulty changes can be isolated and reverted. This provides a formal motivation for commit atomicity from a software-reliability perspective, reinforcing the assumption from the direction of repo health and debuggability.

  Strength of support: Strong

  Summary: Atomic, cohesive commits are industry consensus and empirically supported best practice in software engineering. Herzig and Zeller (2013, 2016) provide the strongest empirical evidence: tangled commits degrade repository traceability, distort defect prediction, and compromise provenance. The converse — session-scoped, single-concern commits — preserves provenance and repo health. Practitioner literature (Swicegood, Loeliger and McCullough) codifies this as standard Git workflow. Zeller's debugging research provides a formal motivation from the direction of change isolation and reliability. The assumption is well-supported from both empirical research and industry practice.

  Caveats: The literature addresses commits in software development repositories. The C2A2 wiki repository is a knowledge repository rather than a code repository; the principle of commit cohesion applies by analogy. The specific notion of "session-scoped" commits as the unit of cohesion is a C2A2-internal design decision; the literature supports cohesion as a principle but does not prescribe the session as the natural boundary. This is a sound application of the general principle to the C2A2 context.

  Search scope: Software engineering literature on atomic and tangled commits (Herzig and Zeller 2013, 2016), mining software repositories, Git workflow best practices (Swicegood, Loeliger and McCullough), systematic debugging and change isolation (Zeller), version control provenance literature.

  Recommendation: Accept as SUPPORTED. The principle of commit cohesion is empirically grounded and industry-standard. Session-scoped commits are a sound instantiation of this principle in the C2A2 context. No qualification needed beyond noting that "session" as the unit of cohesion is a C2A2-internal design choice.
