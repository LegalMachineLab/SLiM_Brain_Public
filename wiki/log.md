# Log

Append-only record of every operation, rejection and adjudication (CLAUDE.md). Newest entries at the bottom.

## 2026-09-02 — RUN-2026-09-02-01 — first ingest batch (model: claude-fable-5-1; schema_version 4.0)

- Run id minted: RUN-2026-09-02-01 (no earlier entries for this date).
- Conversion: all 55 PDFs in raw/ already converted (raw/_conversions.json, docling 2.123.1, ocr=off, table_structure=on, page_markers=false); SHA-256 of every PDF matches the manifest; no reconversion run. The project venv (~/.venvs/bad_brain) is absent on this machine; no conversion was needed, so it was not bootstrapped. Conversions carry no page markers, so anchor locations use "section heading, para N" (schema/claim.md fallback).
- Two conversions are very short: W0448 (abstract-only, one-page document) and W0926 (keynote abstract). The PDFs themselves are one-page documents, so this is not the scanned-source case; no OCR reconversion.
- Anchor concept pages (36) written as the concept registry (schema/concept.md grid; map-concepts retrieval discipline); definitions are grid-level, not source-derived.
- Version-pair pre-checks (ingest-source): W0206 → ingest v1 (IOS Press published version, doi:10.3233/FAIA230962), v2 recorded as other version. W0368 → ingest v2 (ACM camera-ready format, 2025), v1 (preprint) recorded as other version. W0518 → v1 and v2 differ only in heading levels; ingest v1, record v2. W0525 → ingest v2 (later camera-ready), v1 (arXiv, Aug 2023) recorded as other version. W0693 → v1 (arXiv:2410.03492, authors printed) ingested; v2 is a later extended manuscript with no identifiable venue whose conversion lost the author line (docling artifact: author names rendered as bare commas); recorded as other version. Swapping any of these is a team decision.
- Container check: no file is a proceedings volume, edited book, or journal issue; all 50 remaining files are single publications.
- Throughput note: step-2 extraction runs in clean-context subagents (CLAUDE.md), which hold only their own source; extraction of several sources runs concurrently ahead of the sequential steps 3–8, which are processed one source at a time in ingest order. Extraction reads no graph state, so this changes nothing in the results (ingest-source, Sequential processing rationale).
- Helper commands for gate checks, gated appends and bounded projections live in the session scratchpad (not in the repository); they implement schema/write-gate.md verbatim and write only through it.

### SRC-0001 (ingest position 1) — raw/W0013__Facts2Law_Using_Deep_Learning_to_Provide_a_Legal_Qualification_to_a_Se.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 10 (CLM-0001-001…010), all gate-passed on first submission; quotation budget 19.9% of file.
- Candidate concept created: CPT-legal-data-resources (family other) — motivated by CLM-0001-004 (CanLII as a structured training resource), which no anchor captures without distortion. Retrofit over existing claims: none existed (first source); no retrofit edges.
- Dataset: DST-0001 CanLII (external, used); USES SRC-0001→DST-0001 written before the claims naming it.
- CITES: none (first source in the corpus). Cross-source claim edges: none (candidate sets empty for every claim — size 0 ×10).
- Source page and dataset page written; 8 concept pages queued for the close-out (CPT-information-retrieval, CPT-pre-llm-neural, CPT-classical-statistical-ml, CPT-entity-and-citation-extraction, CPT-legal-data-resources).
- Difficulties: no page markers (locations are section + paragraph ordinal); year 2019 and venue type taken from the DOI series and the text's own timeline, not printed; bullet glyphs rendered as "g120" and a stray "Item" token in section 1 (conversion artifact, avoided in quotes); the source reports no numerical results. Dataset language (en, fr) is inferred from the description of a pan-Canadian corpus, not stated. Medium-fidelity claims: CLM-0001-006, CLM-0001-010 (no log entry required).

### SRC-0002 (ingest position 2) — raw/W0050__Plain_Language_Assessment_of_Statutes.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 10 (CLM-0002-001…010), all gate-passed on first submission; quotation budget 19.6%.
- Candidate concept created: CPT-plain-language-readability (legal_task) — readability assessment of legal texts fits no anchor without distortion (motivating CLM-0002-003/004). Retrofit over the 10 existing claims: none engages the notion; no additions.
- Dataset: DST-0002 (introduced); USES SRC-0002→DST-0002 written before the claims naming it.
- CITES: none (no reference to SRC-0001). Cross-source edges: candidate sets of size 0 for nine claims; CLM-0002-010 had a set of 1 (CLM-0001-003, via CPT-classical-statistical-ml) — no relation found; 0 edges.
- Difficulties: year and venue type from the DOI series, not printed; "Anglo-American jurisdictions" has no code, so method claims take general (jurisdiction_inferred) and dataset-backed claims take geographical_proxy for the five dataset jurisdictions; EU kept in CLM-0002-001 because the source names the Better Regulation Agenda. Medium fidelity: CLM-0002-004.
- Correction to the SRC-0001 entry: five (not eight) concept pages were queued.

### SRC-0003 (ingest position 3) — raw/W0060__A_Dataset_for_Statutory_Reasoning_in_Tax_Law_Entailment_and_Question_A.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 16 (CLM-0003-001…016), all gate-passed on first submission; quotation budget 8.7%.
- Candidate concepts created: none (statutory reasoning is captured by CPT-question-answering, whose grid definition covers entailment over statutory text). No retrofit.
- Datasets: DST-0003 SARA (introduced), DST-0004 tax-law text corpus (introduced), DST-0005 case.law (external), DST-0006 legal-term identification set (introduced); four USES edges written before the claims naming them. The PASCAL RTE sanity check is not recorded as a dataset (no record fields stated, no claim rests on it).
- CITES: none (no reference to SRC-0001 or SRC-0002).
- Cross-source edges: candidate sets — sizes per claim: 001:0, 002:0, 003:9, 004:0, 005:3, 006:7, 007:7, 008:7, 009:7, 010:5, 011:5, 012:7, 013:7, 014:1, 015:1, 016:1 (via CPT-information-retrieval, CPT-pre-llm-neural, CPT-accuracy-and-reliability, CPT-symbolic-rule-based, CPT-legal-data-resources, CPT-entity-and-citation-extraction). Edges written: 3 COMPATIBLE_WITH (inferred, medium), 1 IN_TENSION_WITH (inferred, low); no extracted edge (no citation link).
- Difficulties: author/affiliation blocks scattered by the conversion (authors taken from the ACM reference block); dropped hyphens inside words; Table 3 garbled (unused). SARA annotation recorded human_single (author-built cases vetted by one law professor). Claims 003, 014, 016 take general with jurisdiction_inferred. No medium or low fidelity claims.

### SRC-0004 (ingest position 4) — raw/W0085__why_the_decision_represents_the_proper_application_of_the_law_1_..md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 12 (CLM-0004-001…012), all gate-passed on first submission; quotation budget 19.0%. Title taken from the document text ("Explaining Factor Ascription"); the filename is a fragment of a footnote.
- Candidate concepts: none; datasets: none; CITES: none.
- Cross-source edges: candidate sets of size 0 except CLM-0004-009 and CLM-0004-011 (size 11 each, via CPT-pre-llm-neural); no relation found; 0 edges.
- Difficulties: year and venue type from the DOI series; source_jurisdiction general (UK affiliations, US trade-secret cases used only as illustrations); CLM-0004-002 takes geographical_proxy:US with the three cases in legal_reference; CLM-0004-004 (right to explanation) takes general with jurisdiction_inferred. Future-work proposals recorded as methodological claims in the source's modality. No medium or low fidelity claims.

### SRC-0005 (ingest position 5) — raw/W0090__Arpan_Mandal_a_Paheli_Bhattacharya_b_Sekhar_Mandal_a_Saptarshi_Ghosh_b.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 9 (CLM-0005-001…009), all gate-passed on first submission; quotation budget 11.8%. Title taken from the document text; the conversion prints "U sing" for "Using" (artifact corrected in the title field only; quotes untouched).
- Candidate concepts: none. Dataset: DST-0007 (external, Bhattacharya et al. 2021); USES written before the claims naming it. CITES: none.
- Cross-source edges: candidate sets — 001:4, 002:0, 003:13, 004:2, 005:2, 006:2, 007:0, 008:5, 009:17. Written: 3 COMPATIBLE_WITH (inferred, medium), 1 IN_TENSION_WITH (inferred, low).
- Difficulties: year/venue type from DOI series; source_jurisdiction IN (Indian affiliations, Indian Supreme Court data). The extractor flagged that the source's "improvement across all metrics" statement is not fully borne out by its own Table 1 (Rouge-L recall lower in three variations); claims record what the source states — flagged for verification. No medium/low fidelity claims.

### SRC-0006 (ingest position 6) — raw/W0176__Parameter-Efficient_Legal_Domain_Adaptation.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 19 (CLM-0006-001…019), all gate-passed on first submission; quotation budget 13.5%.
- Candidate concepts: none. Datasets: DST-0008 Legal Advice Reddit (introduced), DST-0009 Law Stack Exchange (introduced), DST-0010 ECHR violation dataset (external), DST-0011 C4 subset (external; used as a general-domain adaptation control, recorded because the source runs an experiment on it). Four USES edges written before the claims. CITES: none.
- Cross-source edges: candidate set of 23 (via CPT-pre-llm-neural, CPT-legal-data-resources, CPT-accuracy-and-reliability, CPT-cost-efficiency-labour) plus the CPT-outcome-prediction and CPT-explainability-and-transparency claims of SRC-0004 (8); sizes per claim between 0 and 31. Written: 4 COMPATIBLE_WITH (inferred, medium), 1 IN_TENSION_WITH (inferred, low).
- Difficulties: venue and year not printed (year 2022 from the latest references; venue recorded unknown, venue_type other); run-together words and a garbled equation in the conversion; forum-data jurisdiction undetermined, language en not stated by the source. Method-performance claims resting on all three datasets take general with jurisdiction_inferred. The explanatory mechanism claim (CLM-0006-003) is typed conceptual as the closest fit. No medium/low fidelity claims.

### SRC-0007 (ingest position 7) — raw/W0180__Semantic_Segmentation_of_Legal_Documents_via_Rhetorical_Roles.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 20 (CLM-0007-001…020), all gate-passed on first submission; quotation budget 8.2%.
- Candidate concepts: none (rhetorical-role labelling falls under CPT-argument-mining by its grid definition). Datasets: DST-0012 rhetorical-roles corpus (introduced), DST-0013 Bhattacharya et al. 2019 dataset (external), DST-0014 ILDC (external; size and annotation not stated by this source); three USES edges written before the claims. CITES: none.
- Cross-source edges: candidate sets via CPT-pre-llm-neural, CPT-legal-data-resources, CPT-accuracy-and-reliability, CPT-outcome-prediction, CPT-summarisation, CPT-cost-efficiency-labour, CPT-autonomy-and-human-oversight; sizes per claim between 0 and 36. Written: 7 COMPATIBLE_WITH (inferred, medium); no tension, no extracted edge.
- Difficulties: venue and year not printed (year 2022 from latest references; venue unknown); stray glyph lines and garbled equation in the conversion; ILDC fields unknown from this source. Medium fidelity: CLM-0007-018 (synthesised from Introduction and Ethical Considerations), CLM-0007-020 (synthesised across qualitative case studies).

### SRC-0008 (ingest position 8) — raw/W0186__Can_GPT-3_Perform_Statutory_Reasoning.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 21 (CLM-0008-001…021), all gate-passed on first submission; quotation budget 11.1%.
- Candidate concepts: none. Datasets: DST-0003 SARA (existing; USES added, page regenerated), DST-0015 U.S. Code section sample (introduced), DST-0016 synthetic statutes (introduced).
- CITES: SRC-0008 → SRC-0003 (reference [8], cited for the SARA dataset). The source page of SRC-0003 was regenerated to show the incoming citation. No extracted claim edge: the citation addresses the dataset, not any proposition of SRC-0003; the BERT-based state of the art it compares against is Holzenberger and Van Durme 2021, not in the corpus (unmatched citation logged here).
- Cross-source edges: candidate sets via CPT-question-answering, CPT-large-language-models, CPT-pre-llm-neural, CPT-accuracy-and-reliability, CPT-legal-data-resources; sizes between 1 and 43 per claim. Written: 1 IN_TENSION_WITH (inferred, high — CLM-0008-002 against the prediction CLM-0003-010), 3 COMPATIBLE_WITH (inferred, medium).
- Difficulties: front matter scrambled by the conversion (abstract interleaved with affiliations and Figure 1); run-together words kept verbatim in quotes; synthetic-statute claims take general with jurisdiction_inferred. Medium fidelity: CLM-0008-007 (contamination check synthesised from two probes).

### SRC-0009 (ingest position 9) — raw/W0206__v1__From_Text_to_Structure_Using_Large_Language_Models_to_Support_the_Deve.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 14 (CLM-0009-001…014), all gate-passed on first submission; quotation budget 15.9%. Other version recorded: W0206 v2 (same text without the publisher line).
- Candidate concepts: none. Dataset: DST-0017 (introduced; language left empty because the source does not say which language version of the bilingual Code was used).
- CITES: SRC-0009 → SRC-0008 (reference [5], a passing related-work mention "perform statutory reasoning [5,13]"); no claim of SRC-0009 rests on it, so no extracted claim edge. SRC-0008's page regenerated for the incoming citation.
- Cross-source edges: candidate sets via CPT-rule-formalisation, CPT-symbolic-rule-based, CPT-large-language-models, CPT-accuracy-and-reliability, CPT-cost-efficiency-labour, CPT-autonomy-and-human-oversight, CPT-access-to-justice-tools; sizes between 5 and 45 per claim. Written: 6 COMPATIBLE_WITH (inferred; 1 high, 5 medium), 1 IN_TENSION_WITH (inferred, low).
- Difficulties: Table 2 garbled (percentages taken from prose); source_jurisdiction CA-QC as the source names Quebec; Cyberjustice Laboratory affiliation carries no discipline (recorded unknown). No medium/low fidelity claims.

### SRC-0010 (ingest position 10) — raw/W0210__Human_Performance_on_the_AI_Legal_Case_Verdict_Classi_cation_Task.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 17 (CLM-0010-001…017), all gate-passed on first submission; quotation budget 18.3%.
- Candidate concepts: none. Dataset: DST-0018 (introduced; case count not stated). CITES: none — the authors' self-citations are to JURIX 2022 and ICAIL 2023 papers outside the corpus, not to SRC-0004.
- Cross-source edges: candidate sets via CPT-outcome-prediction, CPT-accuracy-and-reliability, CPT-legal-data-resources, CPT-computational-argumentation, CPT-cost-efficiency-labour, CPT-information-retrieval, CPT-legal-education; sizes between 15 and 40 per claim. Written: 1 IN_TENSION_WITH (inferred, medium), 3 COMPATIBLE_WITH (inferred; 2 medium, 1 low).
- Difficulties: year and venue type from the DOI series; the source says "four motivations" where Section 1 lists three (recorded as printed); CLM-0010-017 rests on cited social-science literature of unstated jurisdiction (undetermined). No medium/low fidelity claims.

### SRC-0011 (ingest position 11) — raw/W0221__Prompt_Engineering_and_Provision_of_Context_in_Domain_Specific_Use_of.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 12 (CLM-0011-001…012), all gate-passed on first submission; quotation budget 17.1%.
- Candidate concept created: CPT-msme-insolvency-regimes (family other) — the source's doctrinal and normative claims about MSME insolvency law (CLM-0011-005/006/007) are about a legal notion that no anchor of any family captures. Retrofit over the 148 existing claims: none engages the notion; no additions.
- Datasets: DST-0019 unseen test set (introduced), DST-0020 UK Business Forum developmental query set (introduced), DST-0021 Insolvency Bot knowledge base (introduced; proprietary in part); three USES edges written before the claims. CITES: none.
- Cross-source edges: candidate sets via CPT-large-language-models, CPT-question-answering, CPT-accuracy-and-reliability, CPT-retrieval-augmented-or-tool-using (none yet), CPT-information-retrieval, CPT-access-to-justice-tools, CPT-access-to-justice; sizes between 0 and 60 per claim. Written: 5 COMPATIBLE_WITH (inferred, medium).
- Difficulties: internal inconsistencies flagged by the extractor (test vs training questions in the gpt-4 comparison; 29% vs 30%; p-values vs t-statistics), recorded as the source states them; the Conclusion's "prompt engineering tool" comparison has no reported results and was not extracted. Medium fidelity: CLM-0011-002, CLM-0011-009.

### SRC-0012 (ingest position 12) — raw/W0328__upon_proprietary_data_by.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 15 (CLM-0012-001…015), all gate-passed on first submission; quotation budget 10.3%. Title from the document text (the filename is a fragment of a footnote).
- Candidate concepts: none (legal violation detection maps to CPT-compliance-and-monitoring; violation entity recognition to CPT-entity-and-citation-extraction). Dataset: DST-0022 LegalLens shared-task dataset (introduced; the original LegalLens dataset is folded into it as the source describes). CITES: none (the Holzenberger citation is to a 2023 paper outside the corpus).
- Cross-source edges: candidate sets via CPT-entity-and-citation-extraction, CPT-pre-llm-neural, CPT-large-language-models, CPT-accuracy-and-reliability, CPT-legal-data-resources, CPT-information-retrieval, CPT-explainability-and-transparency, CPT-access-to-justice; sizes between 0 and 75 per claim. Written: 4 COMPATIBLE_WITH (inferred, medium).
- Difficulties: figures rendered as spurious headings inside Section 2; several internal inconsistencies flagged by the extractor (NER plateau "around 70%" against Table 3 weighted F1 0.31–0.42, attribution of the winning NER system, dataset sizes) — claims record what the source states. Jurisdiction of the data inferred as US (geographical_proxy) from class-action complaints and the TCPA domain; the team may prefer undetermined. Medium fidelity: CLM-0012-004.

### SRC-0013 (ingest position 13) — raw/W0336__The_CLC-UKET_Dataset_Benchmarking_Case_Outcome_Prediction_for_the_UK_E.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 28 (CLM-0013-001…028), all gate-passed on first submission; quotation budget 10.0%.
- Candidate concept created: CPT-court-procedure-and-documents (family other) — the source's claims about the structure of tribunal proceedings and decision documents (CLM-0013-023/024/027, and 018/019 as they bear on prediction) are about a notion no anchor holds. Retrofit over the 175 existing claims (id/statement projection): CLM-0001-008 (Canadian administrative tribunal decisions cite few cases) and CLM-0007-020 (judgment structure and annotator agreement) engage the notion and were added in place; CLM-0007-004 (India's common-law subjectivity) does not. Retrofit edge generation at step 6: the newly-sharing pairs (CLM-0001-008/CLM-0007-020 against the SRC-0013 claims and against each other) were compared; no relation found.
- Datasets: DST-0023 CLC-UKET (introduced; on_request), DST-0024 Cambridge Law Corpus UKET subset (external); two USES edges written before the claims. CITES: none.
- Cross-source edges: candidate sets via CPT-outcome-prediction, CPT-large-language-models, CPT-pre-llm-neural, CPT-accuracy-and-reliability, CPT-legal-data-resources, CPT-access-to-justice, CPT-retrieval-augmented-or-tool-using, CPT-entity-and-citation-extraction; sizes between 4 and 80 per claim. Written: 1 SAME_AS (inferred, medium), 3 IN_TENSION_WITH (inferred, medium), 8 COMPATIBLE_WITH (inferred; 1 high, 7 medium).
- Difficulties: venue and year not printed (year 2024 from references and a December 2023 workshop acknowledgement); CLC-UKET annotation mixed (GPT-4 automatic for train/val, single expert for test outcomes) recorded as automatic; availability on_request per the Ethics Statement. No medium/low fidelity claims.

### Gate rejection — SRC-0014 draft, claim index 16 (would-be CLM-0014-017)

- 2026-09-02, RUN-2026-09-02-01. Rejected condition: `premise` filled while `basis` is `none_stated` (schema/claim.md, division of labour: premise is empty exactly when basis is none_stated). The extractor had recorded the source's stated purpose ("offered to sensitize readers") as a premise; it is not a ground. Re-extraction: the source states the proposition (virtually all AI & Law research comes from civil- or common-law backgrounds) without offering a ground, so `basis` stays `none_stated` and `premise` is emptied. Resubmitted with the rest of the source's draft; no other field changed. A stale edge file was then refused by the gate's duplicate check (12 SRC-0013 edges already present); nothing was written for SRC-0014 in that pass.

### SRC-0014 (ingest position 14) — raw/W0337__Towards_Supporting_Legal_Argumentation_with_NLP_Is_More_Data_Really_Al.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 21 (CLM-0014-001…021) on resubmission after the rejection logged above; quotation budget 9.4%.
- Candidate concept created: CPT-legal-traditions (family other) — motivated by CLM-0014-017. Retrofit over the existing claims (id/statement projection): CLM-0009-013 (results tied to the civil-code drafting tradition) and CLM-0007-005 (India's common-law system as a source of annotation subjectivity) added in place; their source pages regenerated. Retrofit edge generation at step 6: newly-sharing pairs compared — COMPATIBLE_WITH CLM-0014-017→CLM-0009-013 (medium), CLM-0014-017→CLM-0007-005 (medium), CLM-0009-013→CLM-0007-005 (low).
- Datasets: none (position paper). CITES: SRC-0014 → SRC-0010 (Mumford et al. 2023b, cited on the near-random human performance and the absence of a domain-knowledge effect). Extracted edges: 2 SUPPORTS (CLM-0014-004 → CLM-0010-006, → CLM-0010-007; plausibility medium: the citation is approving evidence within a converging-results argument). Citations to Mumford et al. 2022/2023a, Holzenberger & Van Durme 2021/2023 and Malik et al. 2021 are to works outside the corpus (unmatched). SRC-0010's page regenerated for the incoming citation and edges.
- Cross-source edges (inferred): 1 SAME_AS (high; CLM-0014-020 / CLM-0004-004), 2 IN_TENSION_WITH (1 medium, 1 low), 29 COMPATIBLE_WITH (10 high, 18 medium, 1 low). Candidate sets ranged from 1 to 110 claims per claim (CPT-outcome-prediction, CPT-accuracy-and-reliability, CPT-large-language-models and CPT-explainability-and-transparency dominate).
- Difficulties: venue and year not printed (year 2024 from references; venue recorded unknown, venue_type other); "&amp;" entities in headings and quotes; author disciplines unknown (universities only). CLM-0014-020 takes general with jurisdiction_inferred. No medium/low fidelity claims.

### SRC-0015 (ingest position 15) — raw/W0338__Towards_an_Automated_Pointwise_Evaluation_Metric_for_Generated_Long-Fo.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 19 (CLM-0015-001…019), all gate-passed on first submission; quotation budget 9.9%.
- Candidate concepts: none. Dataset: DST-0025 UKSC meta-dataset (introduced). CITES: none.
- Cross-source edges: candidate sets via CPT-summarisation, CPT-large-language-models, CPT-pre-llm-neural, CPT-accuracy-and-reliability, CPT-legal-data-resources, CPT-explainability-and-transparency, CPT-cost-efficiency-labour; sizes between 10 and 95 per claim. Written: 7 COMPATIBLE_WITH (inferred; 6 medium, 1 low).
- Difficulties: venue and year not printed (year 2024 from references and models named); third author's block interposed mid-paragraph; Figure 1 examples unavailable (image). Medium fidelity: CLM-0015-018.

### SRC-0016 (ingest position 16) — raw/W0368__v2__LLMs_Provide_Unstable_Answers_to_Legal_Questions.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 16 (CLM-0016-001…016), all gate-passed on first submission; quotation budget 14.6%. Other version recorded: W0368 v1 (preprint).
- Candidate concepts: none. Dataset: DST-0026 legal instability dataset (introduced). CITES: none (no reference to a corpus source, the authors' own SRC-0003 and SRC-0008 included).
- Cross-source edges: candidate sets via CPT-large-language-models, CPT-accuracy-and-reliability, CPT-question-answering, CPT-outcome-prediction, CPT-legal-data-resources, CPT-explainability-and-transparency, CPT-adjudicative-decision-support; sizes between 3 and 120 per claim. Written: 1 IN_TENSION_WITH (inferred, medium; against the temperature-0 reproducibility claim of SRC-0008), 9 COMPATIBLE_WITH (inferred, medium).
- Difficulties: venue placeholders in the ACM template (recorded preprint); Introduction split by the copyright block and a spurious title heading; second author's discipline unknown. No medium/low fidelity claims.

### SRC-0017 (ingest position 17) — raw/W0386__ConC_provides_public_access_to_its_case_law_via_the_NALUS_database._2.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 9 (CLM-0017-001…009), all gate-passed on first submission; quotation budget 11.2%. Title from the document text ("Comparison of Embedding Methods for Retrieval Under Noisy Institutional Labels"); the filename is a footnote fragment.
- Candidate concepts: none. Datasets: DST-0027 ConC decisions with NALUS keywords (introduced), DST-0028 CzCDC (external). CITES: none.
- Cross-source edges: candidate sets via CPT-information-retrieval, CPT-pre-llm-neural, CPT-accuracy-and-reliability, CPT-legal-data-resources, CPT-adjudicative-decision-support, CPT-cost-efficiency-labour; sizes between 15 and 100 per claim. Written: 6 COMPATIBLE_WITH (inferred; 5 medium, 1 low).
- Difficulties: year from the DOI series; author names with detached diacritics in the conversion (recorded as Novotná, Harašta); the compiled corpus is recorded as introduced (the team may prefer external). Medium fidelity: CLM-0017-007.

### SRC-0018 (ingest position 18) — raw/W0415__That_s_So_FETCH_Fashioning_Ensemble_Techniques_for_LLM_Classi_cation_i.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 17 (CLM-0018-001…017), all gate-passed on first submission; quotation budget 11.7%.
- Candidate concepts: none (legal intake and referral classification maps to CPT-access-to-justice-tools). Dataset: DST-0029 Oregon State Bar referral queries (introduced). CITES: none — the Westermann works cited (JusticeBot methodology, thesis, Dallma, AI4A2J, and Steenhuis & Westermann JURIX 2024) are outside the corpus.
- Cross-source edges: candidate sets via CPT-access-to-justice-tools, CPT-large-language-models, CPT-classical-statistical-ml, CPT-cost-efficiency-labour, CPT-fairness-and-non-discrimination, CPT-accuracy-and-reliability, CPT-legal-data-resources, CPT-access-to-justice; sizes between 5 and 125 per claim. Written: 4 COMPATIBLE_WITH (inferred, medium).
- Difficulties: year from the DOI series; "1 3" for the fraction one third and other artifacts kept verbatim; section 7.2 not a markdown heading. Medium fidelity: CLM-0018-012.

### SRC-0019 (ingest position 19) — raw/W0428__CourtNav_Voice-Guided_Anchor-Accurate_Navigation_of_Long_Legal_Documen.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 13 (CLM-0019-001…013), all gate-passed on first submission; quotation budget 14.8%.
- Candidate concepts: none. Dataset: DST-0030 Indian-Legal-Retrieval-Generation (introduced, public). CITES: none.
- Cross-source edges: candidate sets via CPT-information-retrieval, CPT-adjudicative-decision-support, CPT-retrieval-augmented-or-tool-using, CPT-large-language-models, CPT-accuracy-and-reliability, CPT-explainability-and-transparency, CPT-cost-efficiency-labour, CPT-autonomy-and-human-oversight, CPT-summarisation, CPT-legal-data-resources, CPT-court-procedure-and-documents, CPT-fairness-and-non-discrimination, CPT-privacy-and-data-protection (none), CPT-accountability-and-liability, CPT-security-and-misuse (none), CPT-symbolic-rule-based, CPT-question-answering; sizes between 3 and 130 per claim. Written: 9 COMPATIBLE_WITH (inferred; 1 high, 8 medium).
- Difficulties: venue not printed (year 2025 from reference access dates); authors' affiliation is a company (discipline other); affiliations spliced mid-paragraph; internal inconsistency between abstract medians and Table 1 means recorded as stated. Medium fidelity: CLM-0019-011, CLM-0019-012.

### SRC-0020 (ingest position 20) — raw/W0448__The_Automated_but_Risky_Game_Modeling_Agent-to-Agent_Negotiations_and.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 3 (CLM-0020-001…003), all gate-passed on first submission; quotation budget 19.2%.
- PARTIAL SOURCE FILE — for the team: the PDF in raw/ is a single page holding only the title, authors, abstract and a footer; the footer (dropped by the conversion, read from the PDF's text streams to diagnose the artifact) reads "Proceedings of the Natural Legal Language Processing Workshop 2025, pages 16–26, November 8, 2025, ©2025 Association for Computational Linguistics", so the corpus file is the first page of an eleven-page paper. The three claims rest on the abstract only. Year and venue on the Source record come from that footer, not from the conversion. Replacing the PDF with the full paper is a team decision; after replacement the source is re-extracted per schema/claim.md and these claims superseded.
- Candidate concept created: CPT-automated-negotiation (legal_task) — agent-to-agent dealmaking and transaction execution fit no anchor task. Retrofit over the 298 existing claims: none engages the notion.
- Datasets: none (unnamed framework). CITES: none (no reference list in the file); reverse check: no ingested source cites this title.
- Cross-source edges: candidate sets via CPT-agentic-systems (none), CPT-large-language-models, CPT-fairness-and-non-discrimination, CPT-accuracy-and-reliability, CPT-autonomy-and-human-oversight; sizes between 60 and 135. Written: 3 COMPATIBLE_WITH (inferred; 2 medium, 1 low).
- Difficulties: author order scrambled by the conversion (recorded top to bottom); affiliations without departments (discipline unknown). No medium/low fidelity claims.
- Procedure note: from this source on, step 5 also runs a reverse check (grep of every ingested source's markdown for the new source's title), so that a citation from an earlier-ingested source to a later-ingested one is not missed; the earlier sources (SRC-0001…0019) will be checked pairwise at the batch close-out and any missing CITES edge added and logged.

### SRC-0021 (ingest position 21) — raw/W0463__ARTIFICIAL_MEANING_Thomas_R._Lee_Jesse_Egbert.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 27 (CLM-0021-001…027), all gate-passed on first submission; quotation budget 6.4%. Title as printed ("Artificial Meaning?").
- Candidate concepts created: CPT-ordinary-meaning-interpretation (legal_task) and CPT-corpus-linguistics (technique_class) — the interpretation of ordinary meaning and corpus-based evidence of meaning fit no anchor of any family. Retrofit over the 301 existing claims (id/statement projection): no claim engages either notion; no additions.
- Datasets: DST-0031 COCA (external), DST-0032 iWeb (external); two USES edges written before the claims. CITES: none; reverse check: no ingested source cites this title.
- Cross-source edges: candidate sets via CPT-large-language-models, CPT-explainability-and-transparency, CPT-accuracy-and-reliability, CPT-rule-of-law-and-legitimacy, CPT-adjudicative-decision-support, CPT-autonomy-and-human-oversight, CPT-professional-responsibility; sizes between 0 and 140 per claim. Written: 9 COMPATIBLE_WITH (inferred; 2 high, 6 medium, 1 low).
- Difficulties: HeinOnline-style conversion with footnotes interleaved mid-paragraph, scattered mid-word spaces and duplicated fragments; venue not printed (recorded working paper, year 2025 from "last visited Jan. 2025" footnotes); appendices B–E absent from the conversion; most claim jurisdictions assigned from context (jurisdiction_inferred). No medium/low fidelity claims.

### SRC-0022 (ingest position 22) — raw/W0464__Large_Language_Models_for_Legal_Interpretation_Don_t_Take_Their_Word_f.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 21 (CLM-0022-001…021), all gate-passed on first submission; quotation budget 5.3%.
- Candidate concepts: none new (CPT-ordinary-meaning-interpretation and CPT-corpus-linguistics, created at SRC-0021, capture the source). Datasets: none.
- CITES: SRC-0022 → SRC-0021 (Lee and Egbert, cited in footnote 7 and repeatedly in the text). Extracted edges: 2 SUPPORTS (CLM-0022-003/004 → CLM-0021-013, quoting Lee and Egbert on the unknown provenance of chatbot training data), 2 ATTACKS (CLM-0022-008 → CLM-0021-017 and → CLM-0021-018: the 100-query and manipulation demonstrations are said to be answerable by random seeds and careful prompting). Footnote 186's scoping remark on "artificial meaning" grounds no edge (it says the concern does not apply to the dialectical approach). Reverse check: SRC-0021 does not cite this source. SRC-0021's page regenerated.
- Inferred edges: 15 COMPATIBLE_WITH (2 high, 13 medium). Candidate sets between 3 and 150 per claim.
- Difficulties: no venue, date or affiliations printed (working paper; year 2025 from internal evidence; disciplines unknown though the text describes the team as computer science, linguistics and law); spurious heading from a broken LLM completion; fragmented footnote 197. CLM-0022-018 lists nine jurisdictions cumulatively with basis case_law (dictum) grounded on two US concurrences. No medium/low fidelity claims.

### SRC-0023 (ingest position 23) — raw/W0508__Natural_Language_Processing_in_the_Legal_Domain.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 23 (CLM-0023-001…023), all gate-passed on first submission; quotation budget 15.3%.
- Candidate concept created: CPT-legal-nlp-research-field (family other) — the source's bibliometric claims are about the research field itself, which no anchor holds. Retrofit over the 349 existing claims: CLM-0003-016 (legal NLP growing but resource-poor), CLM-0014-002 (contemporary legal NLP applies classifiers without domain representation), CLM-0014-009 (evaluation in legal NLP underdeveloped) and CLM-0014-017 (civil- and common-law provenance of AI & Law research) added in place; SRC-0003 and SRC-0014 pages regenerated. Retrofit edge generation at step 6: newly-sharing pairs (CLM-0014-002/009/017 against CLM-0003-016) compared — no relation beyond those already written.
- Dataset: DST-0033 legal NLP papers corpus (introduced). CITES: none possible — the manuscript is anonymised and its citations were removed "to avoid de-anonymization" (logged as an extraction difficulty); reverse check: no ingested source cites this title.
- Cross-source edges: 7 COMPATIBLE_WITH (inferred, medium). Candidate sets between 0 and 100 per claim.
- Difficulties: year 2026 inferred from "as of September 2025" data and a 2026 reference; venue unknown; dataset availability recorded public on the strength of a review-time link. Medium fidelity: CLM-0023-020.

### Reverse citation found at SRC-0023 — CITES SRC-0014 → SRC-0023

- 2026-09-02, RUN-2026-09-02-01. SRC-0014 (Santosh et al. 2024) cites "Katz et al. 2023b, Natural language processing in the legal domain, arXiv:2302.12039", the 2023 version of the living survey whose 2026 manuscript is SRC-0023 (which itself refers to "an earlier version of the survey"). Per the version rule of ingest-source, the identifier is recorded in SRC-0023's other_versions and the CITES edge written; the citation is a passing one (bar-exam and survey context), so no claim edge. Pages of SRC-0014 and SRC-0023 regenerated.

### SRC-0024 (ingest position 24) — raw/W0518__v1__Large_Language_Models_as_Tax_Attorneys_A_Case_Study_in_Legal_Capabilit.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 19 (CLM-0024-001…019), all gate-passed on first submission; quotation budget 10.4%. Other version recorded: W0518 v2 (identical text, heading levels differ).
- Candidate concept created: CPT-ai-governance-and-alignment (normative_concern) — motivated by CLM-0024-016/019 (law-informed alignment, AI governance regimes), which no anchor concern holds. Retrofit over the 395 existing claims: none engages the notion.
- Datasets: DST-0034 synthetic tax exams (introduced), DST-0035 subsection vector databases of Title 26 and the CFR (used; a corpus derived from primary sources, recorded as a dataset because retrieval experiments run over it, not as a legal-instrument node). CITES: none (no corpus author appears in the text); reverse check: none.
- Cross-source edges: 2 IN_TENSION_WITH (inferred, medium), 16 COMPATIBLE_WITH (inferred; 4 high, 12 medium). Candidate sets between 10 and 150 per claim.
- Difficulties: no venue or date printed (year 2023 from citations); accuracy figures only in figures, so accuracy claims are qualitative; footnotes interleaved. No medium/low fidelity claims.

### SRC-0025 (ingest position 25) — raw/W0521__Specification_Validation_and_Verification_of_Social_Legal_Ethical_Empa.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 18 (CLM-0025-001…018), all gate-passed on first submission; quotation budget 6.3%.
- Candidate concepts: none new (CPT-ai-governance-and-alignment, created at SRC-0024, holds the operationalisation-of-principles claims). Datasets: none (hand-built RoboChart models). CITES: none; reverse check: none.
- Cross-source edges: 3 COMPATIBLE_WITH (inferred; 1 high, 2 medium). Candidate sets via CPT-rule-formalisation, CPT-symbolic-rule-based, CPT-compliance-and-monitoring, CPT-agentic-systems, CPT-ai-governance-and-alignment, CPT-autonomy-and-human-oversight, CPT-accuracy-and-reliability; sizes between 4 and 130.
- Difficulties: title and author block rendered mid-document; spurious "let" heading; garbled Table 5 and exploded Figure 7 labels; venue and date not printed (year 2023 from reference access dates). Jurisdiction general throughout (no legal instrument discussed). Medium fidelity: CLM-0025-017, CLM-0025-018.

### SRC-0026 (ingest position 26) — raw/W0525__v2__LEGAL_BENCH_AC_OLLABORATIVELY_BUILT_BENCHMARK_FOR_MEASURING_LEGAL_REAS.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 28 (CLM-0026-001…028), all gate-passed on first submission; quotation budget 1.8% of a 676 KB file. Other version recorded: W0525 v1 (arXiv, August 2023).
- Candidate concepts: none new. Datasets: DST-0036 LEGALBENCH (introduced); USES also to DST-0003 SARA, whose entailment and numeric tasks are LEGALBENCH constituents the source runs (DST-0003 page regenerated).
- CITES: SRC-0026 → SRC-0008 (ref. 12, "SARA poses a significant challenge to NLP models"; LLMs on existing benchmarks), → SRC-0003 (ref. 63, SARA and its numeric metric), → SRC-0023 (ref. 70, the 2023 version of the living survey, per the version rule). All passing citations; no extracted claim edge. Refs. 21 (LexGLUE) and 137 (Waldon et al., CogSci) are not yet, or not, in the corpus; LexGLUE will be matched by the reverse check at its ingest. Pages of SRC-0003, SRC-0008 and SRC-0023 regenerated.
- Cross-source edges: 26 COMPATIBLE_WITH (inferred; 4 high, 22 medium). Candidate sets between 20 and 170 per claim.
- Difficulties: docling rendered paragraphs and table cells as headings; PDF line numbers embedded in 5.2 prose (anchors taken from the clean appendix duplicate); model-performance claims take geographical_proxy:US with jurisdiction_inferred though a few tasks use Canadian, EU and multinational materials. Medium fidelity: CLM-0026-019, CLM-0026-021.

### SRC-0027 (ingest position 27) — raw/W0546__Explainable_Text_Classification_Techniques_in_Legal_Document_Review_Lo.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 14 (CLM-0027-001…014), all gate-passed on first submission; quotation budget 9.6%.
- Candidate concepts: none. Dataset: DST-0037 three document-review matter datasets (introduced; recorded as one node because the source names them only by letter and uses them jointly — the team may prefer three). CITES: none; reverse check: none.
- Cross-source edges: 3 COMPATIBLE_WITH (inferred, medium). Candidate sets via CPT-ediscovery (none), CPT-explainability-and-transparency, CPT-classical-statistical-ml, CPT-accuracy-and-reliability, CPT-cost-efficiency-labour, CPT-legal-data-resources; sizes between 15 and 100.
- Difficulties: year (2021) and venue not printed; garbled pseudo-code listings; jurisdiction and language of the datasets inferred from US e-discovery framing (jurisdiction_inferred on empirical claims). No medium/low fidelity claims.

### Reverse citations found at SRC-0026 (LEGALBENCH)

- 2026-09-02, RUN-2026-09-02-01. CITES written: SRC-0014 → SRC-0026 (related work: "LegalBench (Guha et al., 2023) recently presented the first aggregated benchmark…"), SRC-0017 → SRC-0026 (ref. 13, "evaluation is hindered by scarce legal benchmarks"), SRC-0019 → SRC-0026 (related work, "broader evaluation suites like LegalBench"), SRC-0021 → SRC-0026 (footnote 172, naming LEGALBENCH as the study Engel and McAdams rely on), SRC-0023 → SRC-0026 (listed by title in the survey's table of papers; the anonymised manuscript has no reference list). All passing citations; no claim edge. Six pages regenerated.

### SRC-0028 (ingest position 28) — raw/W0590__Applicability_of_Large_Language_Models_and_Generative_Models_for_Legal.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 18 (CLM-0028-001…018), all gate-passed on first submission; quotation budget 3.6%.
- Candidate concepts: none. Datasets: DST-0038 IN-Abs, DST-0039 UK-Abs, DST-0040 GOVREPORT (all external, used); multi-dataset claims carry the first-listed dataset. CITES: none (the Ghosh-group references are to other papers, not SRC-0005); reverse check: none.
- Cross-source edges: 14 COMPATIBLE_WITH (inferred; 1 high, 13 medium). Candidate sets via CPT-summarisation, CPT-large-language-models, CPT-pre-llm-neural, CPT-classical-statistical-ml, CPT-accuracy-and-reliability, CPT-autonomy-and-human-oversight, CPT-legal-data-resources, CPT-legal-nlp-research-field; sizes between 20 and 180.
- Difficulties: year and venue not printed (year 2024 from references); abstract's "generally perform better" against section 6.3's parity on IN-Abs recorded as the source's qualified position. No medium/low fidelity claims.

### SRC-0029 (ingest position 29) — raw/W0597__ELLA_Empowering_LLMs_for_Interpretable_Accurate_and_Informative_Legal.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 14 (CLM-0029-001…014), all gate-passed on first submission; quotation budget 10.9%.
- Candidate concepts: none. Datasets: DST-0041 LeCaRD (external; annotation not described by the source, recorded none), DST-0042 ELLA response-interpretation set (introduced, unnamed in the source). CITES: none; reverse check: none.
- Cross-source edges: 2 IN_TENSION_WITH (inferred, medium; against SRC-0017's finding that a general embedder beats a domain encoder), 7 COMPATIBLE_WITH (inferred; 4 high, 3 medium). Candidate sets between 10 and 180.
- Difficulties: venue and year not printed; section order scrambled by the conversion; Chinese appendix transcripts unused; source_jurisdiction CN from the law treated as its own. Medium fidelity: CLM-0029-008, CLM-0029-014.

### SRC-0030 (ingest position 30) — raw/W0607__LexEval_A_Comprehensive_Chinese_Legal_Benchmark_for_Evaluating_Large_L.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 29 (CLM-0030-001…029), all gate-passed on first submission; quotation budget 4.4%.
- Candidate concepts: none new. Datasets: DST-0043 LexEval (introduced), DST-0044 JEC-QA (external), DST-0041 LeCaRD (existing; USES added, page regenerated), DST-0045 CAIL 2018–2022 (external); the constituents are recorded as used because LexEval tasks are reformatted subsets of them.
- CITES: SRC-0030 → SRC-0026 (ref. 19, LegalBench as an English legal-reasoning benchmark) and → SRC-0028 (ref. 14, among works on LLM challenges in the legal domain); both passing, no claim edge. Ref. 5 (LexGLUE) is not yet in the corpus. Pages of SRC-0026 and SRC-0028 regenerated. Reverse check: none.
- Cross-source edges: 2 IN_TENSION_WITH (inferred, medium; few-shot gains against SRC-0024 and SRC-0008), 26 COMPATIBLE_WITH (inferred; 7 high, 19 medium). Candidate sets between 15 and 190.
- Difficulties: venue and year not printed; result bullets rendered as headings; "Rough-L" spelling kept in quotes; garbled task-example tables unused. No medium/low fidelity claims.

### Correction — reverse citation check at SRC-0030

- The reverse check reported SRC-0008 and SRC-0026 as citing LexEval; inspection shows no mention of LexEval in either file (the helper's author-name heuristic matched unrelated references by authors named Li). No CITES edge was written. The helper now matches on the title fragment only.

### SRC-0031 (ingest position 31) — raw/W0628__Analyzing_Images_of_Legal_Documents_Toward_Multi-Modal_LLMs_for_Access.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 13 (CLM-0031-001…013), all gate-passed on first submission; quotation budget 10.1%.
- Candidate concepts: none. Dataset: DST-0046 (introduced). CITES: SRC-0031 → SRC-0008 (ref. 22, "conducting statutory reasoning") and → SRC-0009 (ref. 33, "transform legal articles into structured representations"); both passing related-work citations, no claim edge; pages regenerated. Reverse check: none.
- Cross-source edges: 5 COMPATIBLE_WITH (inferred, medium). Candidate sets between 15 and 170.
- Difficulties: figure fragments rendered as headings; "lightning" for "lighting" kept verbatim; reference [36] missing from the converted list. No medium/low fidelity claims.

### SRC-0032 (ingest position 32) — raw/W0693__v1__Toward_Robust_Legal_Text_Formalization_into_Defeasible_Deontic_Logic_u.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 17 (CLM-0032-001…017), all gate-passed on first submission; quotation budget 11.2%. Other version recorded: W0693 v2 (later extended manuscript; its conversion lost the author line).
- Candidate concepts: none. Dataset: DST-0047 TCP Code gold standard of Dragoni et al. 2017 (external). CITES: none (the JURIX 2024 volume references are to non-corpus papers); reverse check: none.
- Cross-source edges: 1 IN_TENSION_WITH (inferred, medium; non-determinism against SRC-0008's temperature-0 claim), 14 COMPATIBLE_WITH (inferred; 5 high, 9 medium). Candidate sets between 10 and 150.
- Difficulties: evaluation criteria and part of a prompt listing rendered as headings; figure-axis garbage interleaved in Section 4.5; Listing 3 missing; venue and year not printed (year 2025 from the models evaluated and works cited). Medium fidelity: CLM-0032-017.

### SRC-0033 (ingest position 33) — raw/W0713__Scaling_Legal_AI_Benchmarking_Mamba_and_Transformers_for_Statutory_Cla.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 13 (CLM-0033-001…013), all gate-passed on first submission; quotation budget (11.0%).
- Candidate concepts: none (state-space models are mapped under CPT-pre-llm-neural as non-LLM neural architectures). Datasets: DST-0048 ECtHR (LexGLUE), DST-0049 EUR-Lex (LexGLUE), DST-0050 SCOTUS (LexGLUE), DST-0051 LCR/ECtHR (all external; annotation provenance not stated, recorded automatic as the extractor's placeholder), DST-0014 ILDC (existing; USES added, page regenerated). The abstract's "new benchmark suite" names nothing, so no introduced dataset. CITES: none; reverse check: none.
- Cross-source edges: 7 COMPATIBLE_WITH (inferred, medium). Candidate sets between 10 and 120.
- Difficulties: throughput range garbled ("3549k"); text-versus-table inconsistencies on ILDC and EUR-Lex recorded as the source states them; venue, year and discipline not printed (inferred). No medium/low fidelity claims.

### SRC-0034 (ingest position 34) — raw/W0722__Large_Language_Models_Meet_Legal_Artificial_Intelligence_A_Survey.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 33 (CLM-0034-001…033), all gate-passed on first submission; quotation budget 9.8%.
- Candidate concepts: none new. Datasets: none (survey). CITES: SRC-0034 → SRC-0026 (LegalBench), → SRC-0028 (Deroy et al. on LLM summarisation), → SRC-0030 (LexEval), → SRC-0008 (Blair-Stanek et al. on chain-of-thought legal reasoning), → SRC-0009 (Janatian et al.); all passing, no claim edge. The Ribeiro de Faria, Xie and Steffek 2024 reference is a different paper from SRC-0013. LexGLUE not yet in the corpus. Five pages regenerated. Reverse check: none.
- Cross-source edges: 1 IN_TENSION_WITH (inferred, medium), 24 COMPATIBLE_WITH (inferred; 2 high, 22 medium). Candidate sets between 10 and 200.
- Difficulties: venue and year not printed (year 2025 from the survey's own cut-off statement); dropped hyphens kept verbatim; the ~10% indicative-phrase corpus is unnamed (claim jurisdiction undetermined). No medium/low fidelity claims.

### SRC-0035 (ingest position 35) — raw/W0841__UA-Legal-Bench_A_Benchmark_for_Evaluating_Large_Language_Models_on_Ukr.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 15 (CLM-0035-001…015), all gate-passed on first submission; quotation budget 13.6%.
- Candidate concepts: none. Dataset: DST-0052 UA-Legal-Bench (introduced, public). CITES: SRC-0035 → SRC-0026 (LegalBench named among the English-only benchmarks; passing). Reverse check: none.
- Cross-source edges: 15 COMPATIBLE_WITH (inferred; 5 high, 10 medium). Candidate sets between 10 and 200.
- Difficulties: venue and date not printed (year 2026 from cited 2026 preprints); company affiliation (discipline unknown); spaced numerals kept verbatim; dataset agreement figure is agreement with an LLM judge, not human inter-annotator agreement. No medium/low fidelity claims.

### SRC-0036 (ingest position 36) — raw/W0842__Multi-Legal-Bench_Evaluating_LLMs_on_Legal_Reasoning_Across_Jurisdicti.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 17 (CLM-0036-001…017), all gate-passed on first submission; quotation budget 10.5%.
- Candidate concepts: none. Datasets: DST-0053 Multi-Legal-Bench (introduced), DST-0054 SecondLayer Legal Corpus (external), DST-0052 UA-Legal-Bench (existing; USES added, page regenerated).
- CITES: SRC-0036 → SRC-0035 (companion UA-Legal-Bench, same author, cited throughout) and → SRC-0026 (LegalBench named among prior benchmarks; passing). Extracted edge: SUPPORTS CLM-0036-004 → CLM-0035-005 (high; the source reports the Ukrainian few-shot pattern reproducing across six jurisdictions). Pages regenerated. Reverse check: none. Note for promotion counting: SRC-0035 and SRC-0036 share an author.
- Inferred edges: 11 COMPATIBLE_WITH (3 high, 8 medium). Candidate sets between 10 and 200.
- Difficulties: venue and date not printed (year 2026 inferred); figures dropped with stray axis labels; multi-jurisdiction empirical claims carry one geographical_proxy code per evidence jurisdiction (cumulative). Medium fidelity: CLM-0036-005.

### SRC-0037 (ingest position 37) — raw/W0849__Know_Your_Limits_On_the_Faithfulness_of_LLMs_as_Solvers_and_Autoformal.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 18 (CLM-0037-001…018), all gate-passed on first submission; quotation budget 15.9%.
- Candidate concepts: none. Datasets: DST-0055 re-annotated ContractNLI subset (introduced), DST-0056 ContractNLI (external; original annotation not described, recorded none). CITES: SRC-0037 → SRC-0003 (SARA cited among neuro-symbolic legal work relying on simplified or manually annotated data; passing, no claim edge); SRC-0003's page regenerated. Other Holzenberger references are to papers outside the corpus. Reverse check: none.
- Cross-source edges: 14 COMPATIBLE_WITH (inferred; 3 high, 11 medium). Candidate sets between 5 and 190.
- Difficulties: author block scrambled (two names inside the Introduction; order uncertain); venue and date not printed (year 2026 from cited works); jurisdiction of the NDAs unstated (undetermined). No medium/low fidelity claims.

### SRC-0039 (ingest position 39) — raw/W0880__Extraordinary_Meaning_Judge_Newsom_s_A.I._Experiments_in_Textualist_In.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 26 (CLM-0039-001…026), all gate-passed on first submission; quotation budget 4.8%.
- Candidate concepts: none new. Datasets: none (ad hoc prompt runs). CITES: SRC-0039 → SRC-0021 (Lee and Egbert, notes 4, 40, 64 and following). Reverse: SRC-0022 → SRC-0039 written — Waldon et al. cite Miller's Note as forthcoming under a different title ("An Examination of Judge Kevin Newsom's Use of Generative Artificial Intelligence for Judicial Interpretation"), recorded in other_versions. Extracted edges: ATTACKS CLM-0039-002 → CLM-0021-001 (medium; note 64 cites Lee and Egbert's "not up to the task" claim, which the Note's endorsement of Newsom's reasoning argues against), SUPPORTS CLM-0039-001 → CLM-0021-014 (medium; approving citation of the RLHF-representativeness point). Pages of SRC-0021 and SRC-0022 regenerated.
- Inferred edges: 3 IN_TENSION_WITH (medium), 10 COMPATIBLE_WITH (4 high, 6 medium). Candidate sets between 15 and 200.
- Difficulties: HeinOnline OCR conversion with footnotes interleaved and "GenAl" artifacts kept verbatim; appendices fragmented; most claim jurisdictions assigned from context (jurisdiction_inferred). Medium fidelity: CLM-0039-010, CLM-0039-016.

### SRC-0040 (ingest position 40) — raw/W0893__Defensible_Moats_for_Vertical_AI_Application_Companies_in_a_New_Compet.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 21 (CLM-0040-001…021), all gate-passed on first submission; quotation budget 18.3%.
- Candidate concept created: CPT-legal-technology-market (family other) — the source's claims about vendors, incumbents and defensibility fit no anchor. Retrofit over the 685 existing claims: CLM-0023-021 (commercial interest of publishers, firms and courts) and CLM-0023-022 (language-centric legal technology) added in place; SRC-0023's page regenerated. Retrofit edge generation: pairs with the new claims compared — the two COMPATIBLE_WITH edges to those claims are recorded above; no other relation.
- Datasets: none. CITES: none; reverse check: none. Note: a business-strategy essay whose non-legal claims about vertical AI generally map to the market concept and to agentic systems, compliance and oversight.
- Cross-source edges: 5 COMPATIBLE_WITH (inferred, medium). Candidate sets between 0 and 110.
- Difficulties: no venue, affiliation or date (year 2026 from the latest reference); "&amp;" and heading-level artifacts; the FINRA report claim has basis literature for want of a regulatory-guidance value. No medium/low fidelity claims.

### SRC-0041 (ingest position 41) — raw/W0925__Judgments_as_bulk_data.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 15 (CLM-0041-001…015), all gate-passed on first submission; quotation budget 17.7%.
- Candidate concepts: none new (CPT-legal-data-resources, CPT-court-procedure-and-documents and CPT-legal-technology-market hold the claims). Datasets: none (the Justice Data Matters survey is cited literature). CITES: none; reverse check: none.
- Cross-source edges: 1 IN_TENSION_WITH (inferred, medium; against SRC-0034's account of courts' leakage concerns), 6 COMPATIBLE_WITH (inferred; 1 high, 4 medium, 1 low). Candidate sets between 10 and 130.
- Difficulties: split ligatures and diacritics kept verbatim; England and Wales coded GB; two body paragraphs displaced under the "Corresponding author" heading. No medium/low fidelity claims.

### SRC-0042 (ingest position 42) — raw/W0926__Law_Language_and_AI_Integrating_Fluency_and_Truth.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 3 (CLM-0042-001…003), all gate-passed on first submission; quotation budget 17.7%. The source is a one-page keynote abstract (the PDF itself is one page); the text's "held in conjunction with ICAIL 2019" conflicts with its own June 2023 date — year 2023 recorded per the proceedings date and copyright line.
- Candidate concepts: none. Datasets: none. CITES: none; reverse check: none.
- Cross-source edges: 3 COMPATIBLE_WITH (inferred; 2 medium, 1 low). Candidate sets between 60 and 130.
- Difficulties: typographic omissions in the source text kept verbatim in anchors. No medium/low fidelity claims.

### SRC-0044 (ingest position 44) — raw/W0937__How_Ready_are_Pre-trained_Abstractive_Models_and_LLMs_for_Legal_Case_J.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 10 (CLM-0044-001…010), all gate-passed on first submission; quotation budget 5.5%. Pre-check: the source is the 2023 workshop paper that SRC-0028 (2024) extends under a different title; both carry corpus identifiers, so they are treated as distinct publications (SRC-0028 cites this one), not as versions. Note for promotion counting: SRC-0028 and SRC-0044 share authors.
- Dataset: DST-0038 IN-Abs (existing; USES added, page regenerated). CITES: none outgoing (the Grabmair-group references are other papers). Reverse CITES written: SRC-0028 → SRC-0044, SRC-0030 → SRC-0044, SRC-0034 → SRC-0044.
- CORRECTION FOR THE TEAM: at the ingest of SRC-0030 and SRC-0034 the reference "Deroy, Ghosh and Ghosh 2023, How ready are pre-trained abstractive models and LLMs for legal case judgement summarization?" was matched to SRC-0028 (the 2024 "Applicability…" paper) instead of this source. The two edges CITES SRC-0030 → SRC-0028 and CITES SRC-0034 → SRC-0028 are therefore wrong; under the never-delete invariant they are left in edges.jsonl and flagged here for team removal. The correct edges are written above. Pages of SRC-0028, SRC-0030 and SRC-0034 regenerated.
- Inferred edges: 10 COMPATIBLE_WITH (6 high, 4 medium), most against the same authors' later SRC-0028. Candidate sets between 20 and 190.
- Difficulties: paragraphs split around floating tables; reference [25] missing from the converted list; sub-heading promoted to a section. No medium/low fidelity claims.

### SRC-0045 (ingest position 45) — raw/W0939__Automatic_Judgement_Forecasting_for_Pending_Applications_of_the_Europe.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 19 (CLM-0045-001…019), all gate-passed on first submission; quotation budget 9.4%.
- Candidate concepts: none. Dataset: DST-0060 ECtHR communicated cases, admissibility decisions and judgments (introduced, unnamed in the source). CITES: none outgoing (the Westermann references are other papers). Reverse: SRC-0014 → SRC-0045 written (Santosh et al. cite "Medvedeva et al. (2021)" for the forecasting decline on communicated cases); extracted edge SUPPORTS CLM-0014-006 → CLM-0045-003 (high). SRC-0014's page regenerated.
- Inferred edges: 2 IN_TENSION_WITH (1 medium, 1 low), 10 COMPATIBLE_WITH (4 high, 6 medium). Candidate sets between 10 and 170.
- Difficulties: result tables garbled (figures quoted from prose); dataset unnamed; source_jurisdiction CoE by the procedure the work situates itself in. No medium/low fidelity claims.

### SRC-0046 (ingest position 46) — raw/W0944__Evaluation_of_Seed_Set_Selection_Approaches_and_Active_Learning_Strate.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 17 (CLM-0046-001…017), all gate-passed on first submission; quotation budget 12.0%.
- Candidate concepts: none. Dataset: DST-0061 four legal-matter document sets (external, confidential; language and jurisdiction unstated). CITES: none (the author-name hits are the byline and a self-citation outside the corpus); reverse check: none. Note for promotion counting: SRC-0027 and SRC-0046 share authors.
- Cross-source edges: 3 COMPATIBLE_WITH (inferred; 1 high, 1 medium, 1 low). Candidate sets between 15 and 110.
- Difficulties: abstract split by the conversion; escaped underscores in strategy names kept verbatim; datasets' jurisdiction and language unstated (empirical claims undetermined); Table 2 header duplicated. No medium/low fidelity claims.

### SRC-0047 (ingest position 47) — raw/W0972__KEYNOTE_ADDRESS_TO_OXFORD_CIVIL_JUSTICE_SYSTEMS_IN_THE.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 24 (CLM-0047-001…024), all gate-passed on first submission; quotation budget 19.9%. Title from the text ("AI and Civil Justice: Preparing for the Tsunami"); author printed by title only ("Lord Briggs of Westbourne").
- Candidate concepts: none new (CPT-court-procedure-and-documents, CPT-ai-governance-and-alignment and the anchors hold the claims). Datasets: none. CITES: none; reverse check: none.
- Cross-source edges: 1 IN_TENSION_WITH (inferred, low), 14 COMPATIBLE_WITH (inferred; 12 medium, 2 low). Candidate sets between 10 and 140.
- Difficulties: a judicial speech with no abstract or data; ligature splits and misnumbered bullets in the conversion; England and Wales coded GB; most claim jurisdictions assigned from context. Medium fidelity: CLM-0047-011, CLM-0047-015, CLM-0047-017.

### Reverse citations found at SRC-0045 (Medvedeva et al. 2021)

- 2026-09-02, RUN-2026-09-02-01. CITES written: SRC-0004 → SRC-0045 (Mumford et al. cite the paper as an example of machine learning to predict legal decisions; passing) and SRC-0013 → SRC-0045 (Xie et al. cite it for the prediction-versus-classification distinction). Extracted edge: SUPPORTS CLM-0013-025 → CLM-0045-001 (medium). Three pages regenerated.

### SRC-0048 (ingest position 48) — raw/W0973__LexGLUE_A_Benchmark_Dataset_for_Legal_Language_Understanding_in_Englis.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 17 (CLM-0048-001…017), all gate-passed on first submission; quotation budget 7.6%.
- Candidate concepts: none. Datasets: DST-0062 LexGLUE (introduced); constituents ECtHR, SCOTUS and EUR-LEX matched to the existing LexGLUE-derived nodes DST-0048, DST-0050, DST-0049 (pages regenerated); DST-0063 LEDGAR, DST-0064 UNFAIR-ToS, DST-0065 CaseHOLD, DST-0066 CUAD (external; annotation of the originals not described, recorded as the extractor's provisional values).
- CITES: SRC-0048 → SRC-0045 (Medvedeva et al. 2021, among judgment-prediction works; passing). Reverse CITES written from every ingested source that names LexGLUE: ['SRC-0006', 'SRC-0014', 'SRC-0023', 'SRC-0026', 'SRC-0030', 'SRC-0033', 'SRC-0034', 'SRC-0035', 'SRC-0036'] (all passing mentions; pages regenerated).
- Cross-source edges: 4 IN_TENSION_WITH (inferred, medium; the legal-pre-training advantage against four sources finding none), 19 COMPATIBLE_WITH (inferred; 5 high, 14 medium). Candidate sets between 10 and 200.
- Difficulties: ligatures dropped ("o er", "di erent") and kept verbatim in anchors; a figure caption promoted to a heading splits the Introduction; venue and year not printed (year 2021 from references). Medium fidelity: CLM-0048-003, CLM-0048-008, CLM-0048-014, CLM-0048-015.

### SRC-0049 (ingest position 49) — raw/W1016__DIGITAL_JURISPRUDENCE_BY_DESIGN_The_Digital_Warrant_Neuro-Symbolic_Com.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 51 (CLM-0049-001…051), all gate-passed on first submission; quotation budget 9.4% of a 231 KB file. The extractor kept the statutory-mapping propositions (AI Act Arts. 9, 13, 14; FRCP 37(e); FRE 901; DTSA; ABA Rules; BIPA) as separate claims because a reader could accept one mapping and reject another.
- Candidate concepts: none new (the anchors, CPT-ai-governance-and-alignment, CPT-legal-traditions and CPT-legal-technology-market hold the claims). Datasets: none — Table 5's operational metrics are unpublished internal data, recorded as a medium-fidelity empirical claim (CLM-0049-046) without a Dataset node. CITES: none; reverse check: none.
- Cross-source edges: 7 IN_TENSION_WITH (inferred; 1 high — the determinacy-of-law thesis against the defeasibility claim of SRC-0014 — 5 medium, 1 low), 19 COMPATIBLE_WITH (inferred; 5 high, 14 medium). Candidate sets between 5 and 200.
- Difficulties: spurious headings from a displayed formula; duplicated section numbers; inconsistent sub-heading conversion; lost hyphenation; methodology section numbering mismatching the final headings; venue and date not printed (year 2026 from the stated scope cut-off); author affiliation a property-management company (discipline law per the LL.M.). Medium fidelity: CLM-0049-046.

### SRC-0050 (ingest position 50) — raw/W1036__Anna_Neumann_Holli_Sargeant_and.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Claims written: 22 (CLM-0050-001…022), all gate-passed on first submission; quotation budget 5.3%. Title from the document text ("Prompt Governance? On Governing Technologies Governed by Natural Language"); the filename is an author fragment.
- Candidate concepts: none new (CPT-ai-governance-and-alignment holds the claims). Dataset: DST-0067 systematic-review corpus of 287 papers (introduced; a review corpus rather than a benchmark — the team may prefer to drop the node). CITES: none (author-name hits were other authors named Zhang, Ali and Hammond, and a 2025 Janeček blog post outside the corpus); reverse check: none.
- Cross-source edges: 13 COMPATIBLE_WITH (inferred; 2 high, 11 medium). Candidate sets between 10 and 200.
- Difficulties: figure text garbled; research questions printed out of order; "Executive Order 14139" in the Introduction against 14319 elsewhere (legal_reference uses 14319); affiliations without departments (discipline unknown). No medium/low fidelity claims.

### SRC-0038 (ingest position 38) — raw/W0876__Thinking_Longer_Not_Always_Smarter_Evaluating_LLM_Capabilities_in_Hier.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Ingested in time after SRC-0050: the earlier attempt was held by the citation guard (its only hit was the LegalBench reference) and no record was written, so id and position 38 remained free and are consumed now. Claims written: 12 (CLM-0038-001…012), all gate-passed on first submission; quotation budget 6.3%.
- Candidate concepts: none. Dataset: DST-0057 factor-based case-pair scenarios (introduced, unnamed in the source). CITES: SRC-0038 → SRC-0026 (LegalBench named among isolated-skill benchmarks; passing); SRC-0026's page regenerated. Reverse check: none.
- Cross-source edges: 11 COMPATIBLE_WITH (inferred; 1 high, 9 medium, 1 low), judged against the complete candidate sets as they stand at this later time. Candidate sets between 10 and 200.
- Difficulties: front matter interleaved into Section 1; the source's "consistently" more tokens on incorrect responses is contradicted by its own Table 2 for one model (recorded as stated); author order differs between header and reference line. No medium/low fidelity claims.

### SRC-0043 (ingest position 43) — raw/W0934__Prior_Case_Retrieval_using_Evidence_Extraction_from_Court_Judgements.md

- 2026-09-02, RUN-2026-09-02-01, claude-fable-5-1, schema 4.0. Ingested in time after SRC-0050: the earlier attempt was held by the citation guard (its only hit was an unrelated reference) and no record was written, so id and position 43 remained free and are consumed now. Claims written: 17 (CLM-0043-001…017), all gate-passed on first submission; quotation budget 10.9%.
- Candidate concepts: none. Datasets: DST-0058 Indian Supreme Court judgments 1952–2012 (external), DST-0059 prior-case-retrieval query set with pooled relevance (introduced). CITES: none; reverse check: none.
- Cross-source edges: 8 COMPATIBLE_WITH (inferred; 1 high, 5 medium, 2 low), judged against the complete candidate sets as they stand at this later time. Candidate sets between 10 and 130.
- Difficulties: mathematical-italic Unicode glyphs kept verbatim in anchors; algorithms and tables interleaved with section prose; reference [17] missing from the converted list; annotator count for relevance verification not stated. No medium/low fidelity claims.

### Pairwise citation check before the close-out

- 2026-09-02, RUN-2026-09-02-01. Every ingested source's markdown was checked for the title of every other ingested source (45-character normalised fragment), since the reverse check was introduced only at SRC-0020. Two citations were missing and are now written: CITES SRC-0026 → SRC-0007 (LegalBench's task descriptions cite the rhetorical-roles paper; passing) and CITES SRC-0034 → SRC-0023 (the survey cites "Natural language processing in the legal domain", the 2023 version of the living survey, per the version rule; passing). Four pages regenerated. Total CITES edges: 46.

## Batch close-out — RUN-2026-09-02-01 (2026-09-02, claude-fable-5-1, schema 4.0)

- Batch: SRC-0001…SRC-0050 (50 sources from 55 files; 5 version twins recorded in other_versions and not ingested). Totals after close-out: 892 claims, 632 edges (459 COMPATIBLE_WITH inferred, 37 IN_TENSION_WITH inferred, 2 SAME_AS inferred, 8 SUPPORTS extracted, 3 ATTACKS extracted, 47 CITES, 76 USES), 67 dataset nodes, 47 concepts (36 anchors, 11 created this batch), 2,524 absence records (1,355 from source pages, 756 from coverage, 317 from structure, 96 from concept pages), 0 lapsed (first batch: no earlier zero to fill).
- Promotion check (schema/concept.md; counting pairwise author-independent sources in each candidate's `sources` list): PROMOTED to emergent — CPT-legal-data-resources (35 sources), CPT-legal-nlp-research-field (21), CPT-legal-traditions (13), CPT-court-procedure-and-documents (9), CPT-ai-governance-and-alignment (7), CPT-legal-technology-market (6), CPT-ordinary-meaning-interpretation (3: SRC-0021, SRC-0022, SRC-0039). Remain candidate — CPT-corpus-linguistics (2 sources), CPT-plain-language-readability (1), CPT-msme-insolvency-regimes (1), CPT-automated-negotiation (1). Promotion applied before the concept pages were regenerated, so the pages carry the new status.
- Regenerated: all 47 concept pages (close-out queue: every concept touched during the batch, which is all of them), coverage.md, structure.md, index.md; hypotheses.md created (empty register). Absence records were created under the create-or-cite rule for every zero-bearing cell (closed vocabularies and the grid cross-tabs) and for every anchor pair without a linking claim; none lapsed.
- Order note for provenance: SRC-0038 and SRC-0043 were written in time after SRC-0050 (see their entries); ingest_position records the id order. Their edge judgments used the complete candidate sets as they stood at write time, so pair coverage is unaffected (ingest-source, Sequential processing rationale).
- Open items for the team: (1) two wrong CITES edges (SRC-0030 → SRC-0028, SRC-0034 → SRC-0028) left in place under the never-delete invariant — see the SRC-0044 entry; (2) SRC-0020's raw file holds only the first page of an eleven-page paper; (3) dataset nodes the team may prefer to drop or split: DST-0011 (C4 subset), DST-0037 and DST-0061 (matter sets recorded as one node each), DST-0067 (a systematic-review corpus); (4) source_jurisdiction and jurisdiction_inferred choices flagged in individual entries; (5) helper commands used for the gate, page rendering and close-out live in the session scratchpad, not in the repository — the team may wish to place them under tools/ so that future ingests and page regenerations reuse them.
- Correction at close-out: the promotion of the seven candidates had not reached the page files (the status field is written quoted and the first replacement missed it); the seven frontmatters now read `status: "emergent"`, and the concept pages, coverage.md, structure.md and index.md were regenerated once more (absence records cited, none duplicated).
