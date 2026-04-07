# c282 Wiki Agent Network — Executive Summary

## Vision
Build a living knowledge system where research programs (traditions) maintain their own Wikis, report discoveries upward to a master integration hub, and enable inter-tradition dialogue. AI agents accelerate the identification of novel cross-program connections and paradigm shifts.

## 24-Hour MVP Scope
Prove the concept works at the HTML level with your existing "Resurrecting Civility" structure. Agents ingest conversations, extract PRS triplets (Problem-Resource-Solution), update the Wiki structure, and surface novel connections. No infrastructure migration yet.

## 13-Agent Architecture

### Program-Specific Agents (11 total)
One agent per research program. Each maintains a dedicated Wiki focused on that tradition's questions, discoveries, and track record.

1. **Michael Levin Agent** — bioelectricity, morphogenesis, collective cognition
2. **Karl Friston Agent** — free energy principle, active inference
3. **Donald Hoffman Agent** — interface theory of perception
4. **Jeff Hawkins Agent** — hierarchical temporal memory, neuroscience
5. **Iain McGilchrist Agent** — brain hemispheres, meaning-making
6. **Barbara Fredrickson Agent** — positive psychology, flourishing
7. **Eleonore Stump Agent** — Thomistic philosophy, cognitive science
8. **Sean Carroll Agent** — physics, cosmology, cosmological reasoning
9. **Nima Arkani-Hamed Agent** — particle physics, fundamental structures
10. **Stephen Wolfram Agent** — computational systems, hypergraph theory
11. **Bernardo Kastrup Agent** — idealism, consciousness frameworks

**Program Agent Responsibilities:**
- Maintain the PRS structure for its research program
- Monitor conversations within that tradition for new problems, resources, solutions
- Extract novel questions and discoveries
- Push findings upstream to Master Agent
- Never crawl; only report

### Integration Agents (2 total)

**12. Master c282 Wiki Agent**
- Receives contributions from all 11 program agents
- Integrates them into the master c282 Wiki
- Maintains cross-program indices and relationships
- Records which questions appear in multiple programs
- Write-access only to master Wiki

**13. Pattern Detector Agent**
- Watches for novel connections between programs
- Flags when an insight from one tradition illuminates another
- Surfaces potential paradigm shifts
- Reports to Master Agent for inclusion in master Wiki

## Data Flow

```
Program Agent → discovers new PRS triplet → reports to Master Agent
                                                    ↓
                                         Master Agent updates c282 Wiki
                                                    ↓
                                         Pattern Detector scans for cross-program resonance
                                                    ↓
                                         Flags & insights feed back to Master Wiki
```

## MVP Deliverable
A running instance where:
- Conversation transcripts can be ingested
- PRS triplets are extracted and organized by program
- The HTML structure updates to reflect new discoveries
- Cross-program connections surface as they emerge

## Success Metric
Within 24 hours: agents maintain their respective Wikis, identify one novel cross-program insight, and demonstrate that the system scales to multiple concurrent agents.

---

**Next Decision Point:** After MVP validation, choose infrastructure path (static Wiki, MediaWiki, Git-based, etc.) for scalability and public/private toggle capability.
