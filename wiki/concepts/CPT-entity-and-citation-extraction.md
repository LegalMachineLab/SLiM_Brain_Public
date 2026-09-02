---
id: "CPT-entity-and-citation-extraction"
label: "Entity and citation extraction"
status: "anchor"
concept_type: "legal_task"
definition: "Extracting named entities, citations, and structured elements from legal text."
aliases: []
broader: []
sources: ["SRC-0001", "SRC-0003", "SRC-0005", "SRC-0012", "SRC-0013", "SRC-0031", "SRC-0035", "SRC-0036", "SRC-0043", "SRC-0044"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Entity and citation extraction

_Status: anchor; family: legal_task._

## Definition

Extracting named entities, citations, and structured elements from legal text.

Conceptual claims on this concept, each with its source:
- Holzenberger et al. (2020): BERT-based models can outperform trained lawyers at identifying Black's Law Dictionary legal terms in case law because the models learn the dictionary's well-developed inclusion standards from the training set, with which lawyers are not necessarily familiar, and because pre-processing dropped some legal terms that were subsets of too many others, which the lawyers tended to identify. [CLM-0003-013]
- Mandal et al. (2021): Document-specific catchphrases, short one-word or multiword phrases that collectively give a concise representation of a legal document, combine domain-specific legal importance with document-specific importance; they therefore differ from the domain-specific legal dictionaries widely used in legal summarization algorithms, because catchphrases also capture document-specific important terms that may not be legal keywords. [CLM-0005-001]
- Ali et al. (2021): Evidence information in court judgement sentences can be represented in an Evidence Structure consisting of an optional Observation Frame (the source of the information and the agent disclosing it, with an observer verb and evidence object) and a mandatory Evidence Frame (the action or event revealed, with semantic-role arguments such as agent, patient, location, time, cause, manner and negation). [CLM-0043-002]
- Ali et al. (2021): Witness testimony information can be represented using the same Evidence Structure as evidence information, by treating statement verbs (such as 'stated' or 'said') like observation verbs in Observation Frames and other action or event verbs in Evidence Frames; representing both in one structure allows both sources of information to be used seamlessly for prior case retrieval. [CLM-0043-003]

## Claims about the concept

### Descriptive

**CA**

- Mokanov (2019) state that The CanLII database, with more than two million Canadian court and tribunal decisions from fourteen jurisdictions in parsable format with structured metadata, statutes and regulations with section-level tables of contents, and millions of hyperlinked citations extracted and standardised by the Reflex citator, already constitutes a highly structured 'map' of Canadian law that is available as a significant dataset for training machine-learning algorithms. [CLM-0001-004]. — jurisdiction: CA; basis: dataset_or_experiment
- Mokanov (2019) state that In Canada, administrative tribunal decisions are very factual and do not usually contain many references to other cases, in contrast to judicial decisions, which cite other decisions abundantly; because of this drafting pattern, citation-parsing algorithms are of little use for identifying other cases of interest from administrative decisions. [CLM-0001-008]. — jurisdiction: CA; basis: argument; positive form: general_rule

**IN, CN**

- Ali et al. (2021) state that An evidence information extraction approach designed for Chinese court records, which follow a relatively structured representation, may suit those records well but does not suit Indian court records, which contain descriptive and varied formats of the court proceedings. [CLM-0043-017]. — jurisdiction: IN, CN (comparative); basis: argument

**general**

- Ali et al. (2021) state that No earlier paper had applied natural language processing techniques to extract evidence information from court judgements and used that information to retrieve relevant prior court cases; prior work on evidence retrieval and evidence detection did not combine sentence-level evidence extraction, a rich structured representation, and prior case retrieval. [CLM-0043-001]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Empirical

**geographical_proxy:CA-ON**

- Westermann and Savelka (2024) report that GPT-4o, given photographs or screenshots of a filled-in residential lease form, correctly extracted 73% of the target fields on average across all scenarios and image formats; the results are promising but reveal limitations, for example when image quality is low. [CLM-0031-001]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment
- Westermann and Savelka (2024) report that Extraction accuracy of GPT-4o decreased as the scenario became harder: 89% of fields were correct in the scenario with common names and all fields filled, 71% in the scenario with less common names, two tenants and one missing value, and 59% in the scenario with uncommon names resembling common ones and several missing fields. [CLM-0031-002]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment
- Westermann and Savelka (2024) report that Image format and quality strongly affect the accuracy of multi-modal LLM extraction from forms: typed PDF screenshots were processed almost perfectly, while handwritten printed forms, and especially sloppily filled forms photographed in poor conditions, produced notably lower accuracy. [CLM-0031-003]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment
- Westermann and Savelka (2024) report that Where GPT-4o extracted a field incorrectly, it always captured at least some matching letters or numbers, which indicates that the model had no trouble locating the relevant information on the page, even in low-quality images where the form labels themselves are hard to read. [CLM-0031-005]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment
- Westermann and Savelka (2024) report that Fields whose values are predefined on the form or drawn from real-world entities (province, city, street names) were extracted perfectly or almost perfectly across all image formats, which may indicate that a multi-modal LLM benefits from its pre-training to 'guess' the correct value even when image quality is lacking. [CLM-0031-006]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment
- Westermann and Savelka (2024) report that GPT-4o often 'corrected' uncommon handwritten names into more common ones, with misreadings that were not always obvious; this behaviour shows that LLMs may behave somewhat differently from traditional OCR approaches. [CLM-0031-007]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment

**geographical_proxy:IN**

- Ali et al. (2021) report that On a corpus of Indian Supreme Court judgements, linguistic rules for evidence sentences reached 85% precision on 100 human-verified random sentences, while the weakly supervised sentence classifier reached 72% precision for evidence sentences and 68% for testimony sentences; the classifier's lower precision is attributed to its being applied to a more difficult set of sentences for which the rules assign no label. [CLM-0043-005]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that Instantiating Evidence Structures with a pre-trained semantic role labelling model achieved 86% accuracy for Observation Frame extraction and 88% for Evidence Frame extraction on 260 instances from 100 random evidence and testimony sentences of Indian Supreme Court judgements, with most incorrect extractions due to parsing errors in the SRL model. [CLM-0043-006]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that Representing a court judgement by only its evidence and testimony sentences, rather than all its sentences, results in better prior case retrieval performance, as BM25 restricted to those sentences outperforms BM25 over all sentences on average. [CLM-0043-010]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that Using only witness testimony sentences for prior case retrieval, as in the earlier approach of Ghosh et al., loses key information about the evidences mentioned in a case; techniques that use only testimony sentences perform poorly compared with the corresponding techniques using both testimony and evidence sentences, which highlights the importance of evidence information for prior case retrieval. [CLM-0043-011]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that The main causes of SemMatch scoring a relevant document low or a non-relevant document high are three: missing or incorrect arguments within Evidence Structure instances, misleading high cosine similarity between argument phrases, and the presence of unresolved co-references. [CLM-0043-015]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

**geographical_proxy:UA**

- Ovcharov (2026) report that Legal norm extraction from Ukrainian court decisions is the only benchmark task on which small models match frontier performance (F1 0.318-0.391 across all models), and few-shot prompting has negligible effect on it, suggesting that norm extraction relies on pattern recognition rather than deep legal reasoning. [CLM-0035-011]. — jurisdiction: geographical_proxy:UA; basis: dataset_or_experiment

**geographical_proxy:UA, geographical_proxy:PL, geographical_proxy:CZ**

- Ovcharov (2026) report that Measured legal norm-extraction performance across jurisdictions is dominated by evaluation methodology (exact string matching versus normalised matching of norm references), not by model capability, so that cross-jurisdictional comparison of norm extraction requires jurisdiction-specific normalisation pipelines. [CLM-0036-014]. — jurisdiction: geographical_proxy:UA, geographical_proxy:PL, geographical_proxy:CZ (cumulative); basis: dataset_or_experiment

**geographical_proxy:US**

- Holzenberger et al. (2020) report that On the downstream task of identifying legal terms (tokens or collocations defined in Black's Law Dictionary) in case-law text, a fine-tuned Legal BERT achieves F1 = 0.44 against F1 = 0.35 for fine-tuned Bert-Base-Cased, while two trained lawyers given the same task achieve F1 = 0.26; this indicates that Legal BERT is much better adapted to the legal domain than Bert-Base-Cased. [CLM-0003-012]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Hagag et al. (2024) report that In the LegalLens Shared Task 2024, the top-performing teams in both the LegalLens-NER and LegalLens-NLI sub-tasks consistently relied on fine-tuning pretrained language models, and these fine-tuned models outperformed legal-specific models and few-shot methods. [CLM-0012-001]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that In the LegalLens Shared Task 2024, progress over the baseline was substantial for legal violation entity recognition (the best team improved the NER F1 score by 7.11%) but marginal for legal natural language inference (only one team outperformed the NLI baseline, by 5.7%), so significant room remains for advances in handling the complexities of natural legal language inference. [CLM-0012-002]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that Success in one LegalLens sub-task does not necessarily translate into success in the other: the challenges posed by legal violation entity recognition (LegalLens-NER) and legal violation inference (LegalLens-NLI) are distinct and require different approaches and strengths. [CLM-0012-003]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that In the LegalLens-NER sub-task there appears to be a performance ceiling: the top four teams achieve scores around 70% F1, which seems to be a plateau. [CLM-0012-004]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that Systems in the LegalLens-NER sub-task showed a significant drop in performance when identifying the "Violated By" and "Violated On" entities compared with the Law and Violation entities; this gap indicates room for improvement and suggests the potential of integrating other information extraction techniques, possibly from outside the legal domain. [CLM-0012-005]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

**undetermined**

- Mandal et al. (2021) report that The unsupervised catchphrase extraction method PSLegal and the supervised sequence-tagging model D2V-BiGRU-CRF both extract meaningful catchphrases from legal case documents that agree with those chosen by law domain experts. [CLM-0005-009]. — jurisdiction: undetermined; basis: literature

### Conceptual

**general**

- Mandal et al. (2021) argue that Document-specific catchphrases, short one-word or multiword phrases that collectively give a concise representation of a legal document, combine domain-specific legal importance with document-specific importance; they therefore differ from the domain-specific legal dictionaries widely used in legal summarization algorithms, because catchphrases also capture document-specific important terms that may not be legal keywords. [CLM-0005-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Ali et al. (2021) argue that Evidence information in court judgement sentences can be represented in an Evidence Structure consisting of an optional Observation Frame (the source of the information and the agent disclosing it, with an observer verb and evidence object) and a mandatory Evidence Frame (the action or event revealed, with semantic-role arguments such as agent, patient, location, time, cause, manner and negation). [CLM-0043-002]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Ali et al. (2021) argue that Witness testimony information can be represented using the same Evidence Structure as evidence information, by treating statement verbs (such as 'stated' or 'said') like observation verbs in Observation Frames and other action or event verbs in Evidence Frames; representing both in one structure allows both sources of information to be used seamlessly for prior case retrieval. [CLM-0043-003]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:US**

- Holzenberger et al. (2020) argue that BERT-based models can outperform trained lawyers at identifying Black's Law Dictionary legal terms in case law because the models learn the dictionary's well-developed inclusion standards from the training set, with which lawyers are not necessarily familiar, and because pre-processing dropped some legal terms that were subsets of too many others, which the lawyers tended to identify. [CLM-0003-013]. — jurisdiction: geographical_proxy:US; basis: argument

### Predictive

**geographical_proxy:CA-ON**

- Westermann and Savelka (2024) argue that The almost perfect extraction results on typed PDF versions of forms show that multi-modal LLMs could already be useful for analysing electronic legal documents. [CLM-0031-004]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment

### Methodological

**general**

- Hagag et al. (2024) argue that Existing named entity recognition methods and entity types, including those used in legal-domain NER tasks (such as plaintiff and defendant), are not tailored to detecting legal violations, fail to capture the ambiguity of legal language, and lack the complexity needed for the task. [CLM-0012-009]. — jurisdiction: general; basis: literature
- Ali et al. (2021) argue that Semantic similarity between a query and a court judgement sentence can be computed by representing both as Evidence Structure Instances and combining cosine similarities between the phrase embeddings of their corresponding arguments, which yields a semantically sound similarity score; a document's relevance is the maximum score over its instances. [CLM-0043-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:GB**

- Xie et al. (2024) argue that Large language models (GPT-4-turbo) can be used to automatically annotate tribunal decisions with legal information (facts, claims, statutory and precedent references, outcomes, orders and reasons), reducing the burden of extensive manual annotation; the resulting annotations are generally satisfactory according to expert quality checks, although the practice is not without flaws. [CLM-0013-003]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

**geographical_proxy:IN**

- Deroy et al. (2023) argue that The consistency metrics NumPrec and NEPrec, which measure the fraction of numbers and named entities in a generated summary that also appear in the source document, depend on the ability to detect numbers and named entities accurately; because identifying all types of named entities in Indian legal documents is quite challenging, the metric values are conditioned on the accuracy of the Spacy toolkit used for entity recognition. [CLM-0044-010]. — jurisdiction: geographical_proxy:IN; basis: argument
- Ali et al. (2021) argue that In the absence of publicly annotated datasets for identifying evidence and testimony sentences in court judgements, such sentences can be identified without manually annotated training data by a two-step weakly supervised approach: high-precision linguistic rules first, then a BiLSTM multi-label sentence classifier trained on the rule-identified sentences to improve recall. [CLM-0043-004]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that The intersection between natural language processing and the legal domain is a growing area of research, but one with few large-scale systematic resources. [CLM-0003-016] is in tension with the claim that The CanLII database, with more than two million Canadian court and tribunal decisions from fourteen jurisdictions in parsable format with structured metadata, statutes and regulations with section-level tables of contents, and millions of hyperlinked citations extracted and standardised by the Reflex citator, already constitutes a highly structured 'map' of Canadian law that is available as a significant dataset for training machine-learning algorithms. [CLM-0001-004] (inferred, low). Note: One states that legal NLP has few large-scale systematic resources; the other presents a two-million-decision database with an extracted citation network as a significant training resource — the tension dissolves if 'systematic resource' means an annotated benchmark rather than a raw corpus.
- The claim that Most summarization algorithms developed for the legal domain are extractive and unsupervised, mainly because large training data is lacking in the legal domain. [CLM-0005-008] is in tension with the claim that The CanLII database, with more than two million Canadian court and tribunal decisions from fourteen jurisdictions in parsable format with structured metadata, statutes and regulations with section-level tables of contents, and millions of hyperlinked citations extracted and standardised by the Reflex citator, already constitutes a highly structured 'map' of Canadian law that is available as a significant dataset for training machine-learning algorithms. [CLM-0001-004] (inferred, low). Note: One says large training data is lacking in the legal domain; the other presents a two-million-decision database as a significant training dataset — compatible if 'training data' means task-labelled data such as summaries rather than raw corpora.
- The claim that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002] is in tension with the claim that In the LegalLens Shared Task 2024, the top-performing teams in both the LegalLens-NER and LegalLens-NLI sub-tasks consistently relied on fine-tuning pretrained language models, and these fine-tuned models outperformed legal-specific models and few-shot methods. [CLM-0012-001] (inferred, medium). Note: One finds legal-oriented pre-trained models overall better than generic ones on legal NLU tasks; the other finds fine-tuned generic models beating legal-specific ones on violation detection.

## Distribution

Sources with claims on this concept: 10; claims: 34.

**By contribution type**

| value | sources |
|---|---|
| technical | 10 |
| empirical_quantitative | 9 |
| theoretical | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 4 |
| IN | 3 |
| CA | 1 |
| GB | 1 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 3 |
| geographical_proxy:IN | 2 |
| geographical_proxy:UA | 2 |
| geographical_proxy:US | 2 |
| CA | 1 |
| CN | 1 |
| IN | 1 |
| geographical_proxy:CA-ON | 1 |
| geographical_proxy:CZ | 1 |
| geographical_proxy:GB | 1 |
| geographical_proxy:PL | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2024 | 3 |
| 2021 | 2 |
| 2026 | 2 |
| 2019 | 1 |
| 2020 | 1 |
| 2023 | 1 |

## What the sources do not address

- No interpretive claim on CPT-entity-and-citation-extraction. [ABS-1397] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No normative claim on CPT-entity-and-citation-extraction. [ABS-1398] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
