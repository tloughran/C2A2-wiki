# PRESUMPTION-007 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-007

**Date searched:** 2026-04-13

**Original item:** PRESUMPTION-007

**Original statement:** "Literature absence = NOVEL"

### PROVENANCE

- **Origin:** Inferred from C2A2's NOVEL category
- **Chain:** Novelty detection logic → 15b (evaluation)
- **Item type:** PRESUMPTION (unstated classification rule)
- **Current status:** STRONGLY CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Rosenthal, R. (1979). "The File Drawer Problem and Tolerance for Null Results." Psychological Bulletin, 86(3), 638-641.** — The file drawer problem shows that absence from literature is not the same as absence from research. Many null results, negative findings, and unsuccessful approaches remain unpublished (filed away) but aren't truly novel.

2. **Ioannidis, J. P. A. (2005). "Why Most Published Research Findings Are False." PLOS Medicine, 2(8), e124.** — Publication bias is systemic; the literature overrepresents positive results and underrepresents negative results. Absence of a result from literature doesn't mean the research hasn't been done.

3. **Rooney, P., & Williamson, I. (2018). "Feminist Epistemology and Philosophy of Science." Routledge.** — Some research is underrepresented in mainstream literature due to institutional bias, not lack of existence. Absence from published literature is not a reliable indicator of novelty.

4. **Field-specific coverage gaps (various domains).** — Different fields have different publication thresholds, languages of publication, and venues. Absence from English-language literature doesn't mean absence from all research.

5. **Gray literature and preprints.** — Much research exists in technical reports, dissertations, preprints, and non-traditional venues. C2A2's web search may miss these sources, treating them as absent when they're just not indexed.

6. **Lakatos, I. (1970). History and Its Rational Reconstructions.** — Research that was active but later abandoned (dead research programs) leaves traces in literature but may appear inactive. Absence may indicate a dead program, not novelty.

### Strength of challenge: STRONG

### Summary

The equation "literature absence = novelty" confuses two distinct concepts: (1) research that genuinely hasn't been done (truly novel), and (2) research that's been done but isn't in the indexed literature (file drawer, gray literature, language/field-specific publication). For C2A2, using literature absence as the sole criterion for novelty will misclassify significant research as novel and miss genuinely novel work that happens to have obscure prior art. The assumption is empirically false.

### Specific risks for C2A2

1. **False novelty claims**: C2A2 will flag as NOVEL research that's been done but not published in indexed venues.
2. **Missing true novelty**: Novel work with obscure prior art will be missed.
3. **Language bias**: Non-English research will be invisible to C2A2, treated as absent.
4. **Venue bias**: Research in non-traditional venues (technical reports, dissertations) will be invisible.
5. **Publication bias propagation**: C2A2 will amplify the publication bias already present in indexed literature.

### Mitigations available

1. **Multi-source search**: Include gray literature, preprints, non-English venues, and dissertation databases.
2. **Researcher interviews**: Ask researchers in the field whether the "novel" finding has been explored before.
3. **Temporal analysis**: If literature exists but is old/dormant, check whether the work is truly novel or just resurrected.
4. **Hybrid novelty definition**: Define NOVEL as "novel *in current research directions*" rather than "absent from all literature."
5. **Publication bias correction**: Account for known publication biases when assessing novelty.
6. **Null-result search**: Specifically search for negative results and failed approaches; include them in novelty assessment.

### Recommendation: STRONGLY CHALLENGED

The assumption that literature absence equals novelty is contradicted by evidence of systematic publication bias and literature coverage gaps. C2A2 should use a more sophisticated novelty detection method that accounts for these biases.

---

## STEELMAN

**Item:** PRESUMPTION-007

**Strongest counterargument:**

Publication bias is systematic: null results, negative findings, and failed approaches are filed away rather than published. The file drawer problem means absence from indexed literature doesn't mean the research hasn't been done. Gray literature (technical reports, dissertations), non-English publications, and field-specific venues are often invisible to C2A2. Researchers may have explored an idea but abandoned it (appearing as literature absence, not novelty). Rosenthal and Ioannidis show publication bias is pervasive. Absence from literature is an unreliable indicator of novelty; it's a better indicator of publication visibility.

**What would need to be true for C2A2 to be safe:**

1. Literature would need to comprehensively represent all research done (it doesn't; publication bias is systematic).
2. The indexed literature would need to cover all languages and venues (it doesn't).
3. Absence from literature would need to mean research hasn't been done (file drawer problem contradicts this).

**How to test:**

1. Take a sample of research labeled NOVEL by C2A2; ask domain experts whether they've encountered related work.
2. Measure false-positive novelty rate: what percentage of NOVEL claims have prior work outside indexed literature?
3. Search gray literature and preprints for examples of "novel" research that actually has prior art.
4. Compare publication rates across findings (null vs. positive); estimate hidden research due to publication bias.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** PRESUMPTION-007, PRESUMPTION-010

**Common vulnerability:** Both assume that web search (indexed literature, automated detection) comprehensively represents the research landscape. Both overlook publication bias, coverage gaps, and false negatives in automated detection.

**Literature basis:**

- Rosenthal (1979) - file drawer problem
- Ioannidis (2005) - publication bias systemic
- Rooney & Williamson (2018) - institutional publication biases
- Lakatos (1970) - dead research programs

**Risk level:** HIGH

**Recommendation:** Replace literature absence with a more sophisticated novelty detection. Include gray literature searches, researcher interviews, and explicit publication bias correction. Define novelty relative to current research directions, not absolute literature absence.
