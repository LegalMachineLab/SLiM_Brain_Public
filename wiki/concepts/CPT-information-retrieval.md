---
id: "CPT-information-retrieval"
label: "Information retrieval"
status: "anchor"
concept_type: "legal_task"
definition: "Finding relevant legal documents or passages (cases, statutes, precedents) for a query."
aliases: []
broader: []
sources: ["SRC-0001", "SRC-0003", "SRC-0010", "SRC-0011", "SRC-0012", "SRC-0017", "SRC-0019", "SRC-0024", "SRC-0029", "SRC-0033", "SRC-0034", "SRC-0043", "SRC-0048"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Information retrieval

_Status: anchor; family: legal_task._

## Definition

Finding relevant legal documents or passages (cases, statutes, precedents) for a query.

Conceptual claims on this concept, each with its source:
- Hagag et al. (2024): Identifying legal violations on the open web presents two primary challenges: determining where to search among massive amounts of online content of varying credibility and relevance, and accurately interpreting whether the information found indicates a legal violation, which requires applying legal knowledge to determine the legal grounds and to identify victims who may be entitled to compensation. [CLM-0012-007]
- Hagag et al. (2024): Information sparsity is a challenge for identifying cases of legal violation on the open web: the salient details of a case are often spread across multiple online sources and individually offer little insight, so that a holistic understanding and evaluation of the case is possible only when the individual details are stitched together. [CLM-0012-014]

## Claims about the concept

### Descriptive

**CA**

- Mokanov (2019) state that In Canada, administrative tribunal decisions are very factual and do not usually contain many references to other cases, in contrast to judicial decisions, which cite other decisions abundantly; because of this drafting pattern, citation-parsing algorithms are of little use for identifying other cases of interest from administrative decisions. [CLM-0001-008]. — jurisdiction: CA; basis: argument; positive form: general_rule

**CN**

- Hu et al. (2024) state that A legal case retrieval module has rarely been integrated into existing legal-domain LLMs in civil law systems; Chinese legal-domain LLMs can currently only answer users on the basis of internal legal knowledge and externally retrieved legal articles, and cannot provide relevant legal cases for reference. [CLM-0029-003]. — jurisdiction: CN; basis: none_stated

**CZ**

- Novotná and Harašta (2025) state that The keywords manually assigned to Czech Constitutional Court decisions by court staff in the NALUS database, although treated as a gold standard, carry noise and inconsistency that grow over time because of staff turnover, the absence of formal assignment rules, and emerging legal issues; this problem is well known in Czechia, but its impact, including on automation, remains understudied. [CLM-0017-003]. — jurisdiction: CZ; basis: dataset_or_experiment
- Novotná and Harašta (2025) state that Searching for similar decisions constitutes a large part of the work of analysts, clerks and judges at the Czech Constitutional Court, and retrieving relevant case law remains a time-consuming task. [CLM-0017-008]. — jurisdiction: CZ; basis: none_stated

**general**

- Mokanov (2019) state that The full-text search queries lawyers use to research a client's situation are often limited in scope and may miss nuances of the situation, and existing 'more like this' systems are typically bag-of-words approaches with limited understanding of content that do not consider citations, which are reliable indicators of popularity and authority. [CLM-0001-003]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Holzenberger et al. (2020) state that Although tools exist to help lawyers retrieve documents relevant to a case, no strong capabilities in automatic statutory reasoning (systems that suggest legal opinions by applying rules to a case) are known to exist. [CLM-0003-003]. — jurisdiction: general [jurisdiction inferred]; basis: none_stated
- Khadloya et al. (2025) state that Existing legal question-answering and retrieval benchmarks operate at the document level, returning entire cases rather than pinpointed spans, and are not designed for judge-facing interaction loops; most legal QA and summarization systems return text without a user interface that enforces verification. [CLM-0019-003]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Khadloya et al. (2025) state that Prior legal question-answering, summarization and document visual question-answering work does not focus on navigation, and to the best of available knowledge CourtNav is the first attempt to build a voice-guided, anchor-first interface mapping spoken commands to highlighted paragraphs for the legal domain. [CLM-0019-004]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Maurya (2025) state that The growth of legal text outpaces human capacity and the lexical, keyword-based query mechanisms and hard-coded taxonomies on which traditional legal research relies, so that as legal corpora balloon the gap between the promise of legal information and practical legal intelligence widens. [CLM-0033-002]. — jurisdiction: general; basis: argument
- Hou et al. (2025) state that The prevailing paradigm for using LLMs in legal retrieval is a two-stage retrieval and re-ranking framework, which has demonstrated significant improvements in legal case and law article retrieval. [CLM-0034-031]. — jurisdiction: general; basis: literature
- Ali et al. (2021) state that No earlier paper had applied natural language processing techniques to extract evidence information from court judgements and used that information to retrieve relevant prior court cases; prior work on evidence retrieval and evidence detection did not combine sentence-level evidence extraction, a rich structured representation, and prior case retrieval. [CLM-0043-001]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Interpretive

**general**

- Ali et al. (2021) read Information retrieval as follows: Because SemMatch computes matching scores for individual Evidence Structure instances, it can provide better interpretation of each relevant document, in terms of the actual sentences that produced the maximum matching score, than BM25-based techniques that score the whole document. [CLM-0043-013]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Ali et al. (2021) read Information retrieval as follows: Taking the maximum matching score of any single Evidence Structure instance as the whole document's score is a limitation of SemMatch relative to BM25-based techniques, which compute a matching score for the whole document directly because they do not rely on sentence structure. [CLM-0043-014]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Normative

**general**

- Khadloya et al. (2025) argue that Judicial tools for long records should target direct, auditable navigation to the exact anchored locus in the record rather than free-form summarization, because adjudication prioritizes verifiability and summaries can hide citations and miss pivotal passages. [CLM-0019-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Empirical

**geographical_proxy:CN**

- Hu et al. (2024) report that Current legal article retrieval models used with legal-domain LLMs cannot ensure that all relevant legal articles are retrieved and all irrelevant ones excluded; missed articles reduce the completeness of the LLM's response, while irrelevant retrieved articles introduce noise that leads the LLM to produce incomplete, incorrect or inconsistent advice. [CLM-0029-001]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: argument
- Hu et al. (2024) report that Fine-tuning the BGE embedding model on the LeCaRD training split significantly increases NDCG@10, @20 and @30 for Chinese legal case retrieval over both BM25 and untuned BGE, which shows that the fine-tuned model learns legal knowledge and better distinguishes legal cases that are semantically similar but not legally relevant; nonetheless CaseEncoder, SAILER and CaseFormer still outperform the fine-tuned BGE. [CLM-0029-009]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment
- Hu et al. (2024) report that In a user study, retrieving relevant legal cases proved beneficial for 77% of consultation queries on average: although the retrieved cases might not exactly match the user's situation, they provide a reference point to gauge possible outcomes, and highlighting the sentences of a case relevant to the query significantly streamlines reading and improves reading efficiency. [CLM-0029-013]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:CZ**

- Novotná and Harašta (2025) report that For retrieving semantically similar Czech Constitutional Court decisions, a general-purpose OpenAI embedder (text-embedding-3-large) consistently and statistically significantly outperforms a domain-specific BERT encoder pre-trained from scratch on about 34,000 of the court's decisions, across all cut-offs (k = 10, 20, 100) and both relevance thresholds (0.20, 0.28), in nDCG, P@k and HitRate@k. [CLM-0017-001]. — jurisdiction: geographical_proxy:CZ; basis: dataset_or_experiment
- Novotná and Harašta (2025) report that The likely reason the from-scratch domain BERT lags behind the general-purpose embedder is scale and training objective: the general embedder benefits from vastly more pretraining data and a broader semantic curriculum, while the domain model is smaller, trained only with masked language modelling, and lacks contrastive or retrieval-aware supervision. Under noisy labels, pretraining scale and semantic breadth outweigh domain restriction. [CLM-0017-002]. — jurisdiction: geographical_proxy:CZ; basis: dataset_or_experiment
- Novotná and Harašta (2025) report that When keyword overlap is used as the relevance gold standard, absolute nDCG values are conservative lower bounds rather than evidence of poor retrieval utility, because keyword overlap is a noisy and incomplete gold standard; relative differences between models nonetheless remain large and statistically significant. [CLM-0017-005]. — jurisdiction: geographical_proxy:CZ; basis: dataset_or_experiment
- Novotná and Harašta (2025) report that Splitting long court decisions into overlapping 512-token windows and averaging the window embeddings increases a BERT encoder's exposure to long texts but adds little new signal, because overlapping segments are semantically redundant and averaging them can dilute discriminative cues. [CLM-0017-007]. — jurisdiction: geographical_proxy:CZ; basis: argument
- Novotná and Harašta (2025) report that For document embeddings of Czech Constitutional Court decisions produced by a from-scratch domain BERT, self-attention pooling of window hidden states consistently outperforms mean pooling in retrieval. [CLM-0017-009]. — jurisdiction: geographical_proxy:CZ; basis: dataset_or_experiment

**geographical_proxy:CoE, geographical_proxy:IN, geographical_proxy:EU, geographical_proxy:US**

- Maurya (2025) report that Among the benchmarked models, SSD-Mamba achieves the best overall balance of scalability, accuracy and efficiency, making it a strong candidate for large-scale, real-world legal AI applications involving statutes and long-form case law; for resource-constrained deployments such as large-scale statutory analysis, court policy studies or law-firm knowledge management it provides state-of-the-art accuracy at dramatically lower computational cost. [CLM-0033-010]. — jurisdiction: geographical_proxy:CoE, geographical_proxy:IN, geographical_proxy:EU, geographical_proxy:US (cumulative); basis: dataset_or_experiment

**geographical_proxy:GB**

- Ribary et al. (2023) report that The case-retrieval component of the Insolvency Bot, which combines zero-shot classification over text-embedding-ada-002 embeddings with keyword matching, identified the correct cases with 49% precision and 57% recall on the training questions and performed slightly worse on the test questions, with 24% precision and 33% recall. [CLM-0011-010]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

**geographical_proxy:IN**

- Khadloya et al. (2025) report that In a pilot on Indian charge sheets, pleadings and orders, the voice-guided anchor-first navigator cut time-to-relevance from minutes to seconds compared with manual navigation in a stock PDF reader: it halved time-to-relevance on temporal commands (10 s to 5 s) and reduced contextual queries from about 200 s to about 6 s, with median time-to-relevance dropping from 3-5 minutes to 10-15 seconds (30-45 seconds including quick visual verification). [CLM-0019-009]. — jurisdiction: geographical_proxy:IN [jurisdiction inferred]; basis: dataset_or_experiment
- Khadloya et al. (2025) report that Retrieval mode significantly influences strict-hit F1 at paragraph or table-cell level on long Indian legal records: keyword search performs well on statute or party mentions, dense-only retrieval aids paraphrase but misses exact citations, a simple hybrid improves further, and a windowed late-interaction plus keyword variant achieves the best strict-hit F1 within the same latency budget. [CLM-0019-010]. — jurisdiction: geographical_proxy:IN [jurisdiction inferred]; basis: dataset_or_experiment
- Ali et al. (2021) report that Multiplying the Evidence-Structure similarity score by a Sentence-BERT sentence similarity score is necessary because errors in the automated semantic role labelling tool may produce imperfect Evidence Structure instances, and a structure-independent sentence similarity provides a complementary view; a variant of SemMatch without the Sentence-BERT factor reached average R-Precision 0.36 and MAP 0.30 over 10 queries, lower than the full method but comparable in R-Precision to BM25 on testimony and evidence sentences and better than Sentence-BERT alone. [CLM-0043-008]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that For prior case retrieval over Indian Supreme Court judgements, the SemMatch technique applied to testimony and evidence sentences is the best performing technique averaged across 10 diverse queries in both R-Precision and Average Precision, and the most consistent across queries (minimum R-Precision 0.24), compared with BM25 and Sentence-BERT baselines that fall to an R-Precision of 0 on some queries. [CLM-0043-009]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that Representing a court judgement by only its evidence and testimony sentences, rather than all its sentences, results in better prior case retrieval performance, as BM25 restricted to those sentences outperforms BM25 over all sentences on average. [CLM-0043-010]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that Using only witness testimony sentences for prior case retrieval, as in the earlier approach of Ghosh et al., loses key information about the evidences mentioned in a case; techniques that use only testimony sentences perform poorly compared with the corresponding techniques using both testimony and evidence sentences, which highlights the importance of evidence information for prior case retrieval. [CLM-0043-011]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that For queries containing negation, Sentence-BERT and SemMatch capture the query's meaning better than BM25, and SemMatch handles negation in a more principled manner because the Evidence Structure Instance captures negation as one of its arguments. [CLM-0043-012]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that The main causes of SemMatch scoring a relevant document low or a non-relevant document high are three: missing or incorrect arguments within Evidence Structure instances, misleading high cosine similarity between argument phrases, and the presence of unresolved co-references. [CLM-0043-015]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

**geographical_proxy:US**

- Nay et al. (2023) report that The similarity-search retrieval pipeline used (out-of-domain GTR-large embeddings over subsection-level vector databases of the U.S. Code and CFR, with default hyperparameters) failed to supply the most relevant 'gold truth' sources to the LLM a significant portion of the time, as shown by GPT-4's clear performance boost when given the gold-truth documents instead; better retrieval will be important where humans do not supply the exact legal documents. [CLM-0024-011]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

**geographical_proxy:US, geographical_proxy:IN**

- Maurya (2025) report that Attention-based transformer models are particularly effective at capturing fine-grained semantic distinctions when context length is moderate: on SCOTUS issue classification DeBERTa achieves the strongest overall performance (Micro-F1 83.8, Accuracy 84.0) with Longformer close behind, and on ILDC retrieval Longformer and DeBERTa outperform Mamba on Recall@10 and nDCG@10. [CLM-0033-008]. — jurisdiction: geographical_proxy:US, geographical_proxy:IN (cumulative); basis: dataset_or_experiment

### Conceptual

**general**

- Hagag et al. (2024) argue that Identifying legal violations on the open web presents two primary challenges: determining where to search among massive amounts of online content of varying credibility and relevance, and accurately interpreting whether the information found indicates a legal violation, which requires applying legal knowledge to determine the legal grounds and to identify victims who may be entitled to compensation. [CLM-0012-007]. — jurisdiction: general; basis: argument
- Hagag et al. (2024) argue that Information sparsity is a challenge for identifying cases of legal violation on the open web: the salient details of a case are often spread across multiple online sources and individually offer little insight, so that a holistic understanding and evaluation of the case is possible only when the individual details are stitched together. [CLM-0012-014]. — jurisdiction: general; basis: argument

### Predictive

**general**

- Mokanov (2019) argue that Transformer XL and XL Net embeddings are expected to yield significant gains over the Doc2Vec embeddings originally used in Facts2Law, but this has yet to be confirmed by the evaluation under way. [CLM-0001-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mokanov (2019) argue that Predicting relevant sources of law from the text of a document enables legal researchers to search the law in an entirely new way, by describing their problem in plain language, and the results obtained will constitute a good starting point for sorting the issues and subsequently exploring the applicable rules. [CLM-0001-010]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Methodological

**CA**

- Mokanov (2019) argue that Using the Facts2Law approach, pertinent cases that could have been cited in a Canadian administrative tribunal decision can nevertheless be identified even though the decision-maker chose not to cite other relevant case law. [CLM-0001-009]. — jurisdiction: CA [jurisdiction inferred]; basis: argument

**general**

- Mokanov (2019) argue that For producing whole-document embeddings of legal documents, BERT, although an improvement over Doc2Vec, is less optimal because of the computing power it requires and its small document size of 512 tokens, whereas Transformer XL requires much less processing, works on much larger text sequences, and uses left-to-right context to give different meanings to ambiguous words; XL Net, which is very similar to Transformer XL but does not take word order into account, has shown to lead to even better results. [CLM-0001-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mumford et al. (2023) argue that To enhance the accuracy of legal verdict classification, future research should incorporate explicit references to other cases (particularly leading cases that frequently form the reference basis for judgements) and temporal context, so as to establish references to key precedents, and advanced information/document retrieval NLP techniques are well suited to implementing these measures within AI classification systems. [CLM-0010-016]. — jurisdiction: general; basis: argument
- Hagag et al. (2024) argue that A system for efficiently detecting legal violations in online digital data must scan large amounts of data, isolate relevant information, contextualise the findings by linking them to specific legal grounds, clearly explain potential violations, and identify the affected individuals or entities who may be entitled to legal recourse. [CLM-0012-008]. — jurisdiction: general; basis: argument
- Novotná and Harašta (2025) argue that Under noisy, heterogeneous relevance labels with many threshold-relevant items, Recall@k is less informative, whereas graded nDCG (which is threshold-independent) together with head-oriented metrics such as P@k, HitRate@k and RBP better reflect user utility in case-law retrieval evaluation. [CLM-0017-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Khadloya et al. (2025) argue that Trustworthy highlighting in long legal records requires layout-aware parsing that emits canonical spans with stable coordinates and identifiers (page, bounding box, span id, character range, type), because pure text extraction loses the geometry needed for highlights and vision-only pipelines are compute-heavy and brittle on low-quality scans. [CLM-0019-005]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Khadloya et al. (2025) argue that Because latency and predictability are critical in court, spoken commands should be interpreted by a grammar-first, LLM-backed router: a compact command grammar parses transcribed speech into typed intents and slots first, and a lightweight LLM back-off produces a structured action with confidence and disambiguating rewrites only when parsing fails or is ambiguous. [CLM-0019-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Maurya (2025) argue that Applying a sliding window with 20% overlap and aggregating window-level outputs (averaging probabilities or logits for classification, mean-pooling embeddings for retrieval) lets the whole of a long legal document contribute to the prediction and avoids loss of context due to truncation; because Mamba and SSD-Mamba handle longer contexts directly, they reduce window fragmentation and preserve global coherence, producing more faithful document embeddings and better retrieval. [CLM-0033-007]. — jurisdiction: general; basis: argument
- Chalkidis et al. (2021) argue that Legal information retrieval datasets (relevant case law retrieval, regulatory compliance) were excluded from the first version of LexGLUE because they rely on processing multiple long documents and require more task-specific neural architectures (e.g., siamese networks) and different evaluation measures, which would make the benchmark more complex and a less attractive entry point for newcomers to legal NLP. [CLM-0048-017]. — jurisdiction: general; basis: argument
- Ali et al. (2021) argue that Semantic similarity between a query and a court judgement sentence can be computed by representing both as Evidence Structure Instances and combining cosine similarities between the phrase embeddings of their corresponding arguments, which yields a semantically sound similarity score; a document's relevance is the maximum score over its instances. [CLM-0043-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Ali et al. (2021) argue that Computing sentence similarity by averaging word embeddings, as in earlier full-text search over legal document collections, gives a lossy representation in which the relative order of words is lost, whereas representing sentences as Evidence Structure Instances preserves relative ordering through the structure itself. [CLM-0043-016]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:CA**

- Mokanov (2019) argue that Where no training data exists for the question of which sources of law are relevant to a given legal text, citations in case law can act as stand-ins for relevance, because court decisions are opinions very similar in content and form to legal opinions and briefs, and the citations they contain are typically the result of a human being's research and relevance evaluation. [CLM-0001-001]. — jurisdiction: geographical_proxy:CA [jurisdiction inferred]; basis: argument
- Mokanov (2019) argue that Learning from the existing citations in the CanLII database makes it possible to predict which sources of law are relevant to the text of a legal brief, a legal opinion, or a plain-language description of a legal issue, whether or not the input text itself contains legal citations. [CLM-0001-002]. — jurisdiction: geographical_proxy:CA [jurisdiction inferred]; basis: dataset_or_experiment
- Mokanov (2019) argue that The production Facts2Law model takes as input a brief and a target document and outputs its confidence that the brief should cite the target: whole-document embeddings of both documents, together with a weighted summary of the embeddings of neighbouring nodes in the citation graph and relevant metadata, are fed through fully connected layers, merged, modulated by the age of the brief, and passed to a final fully connected layer that outputs the prediction. This architecture allows heuristics to select a subset of the corpus that could be relevant to a document and then rank that subset efficiently. [CLM-0001-005]. — jurisdiction: geographical_proxy:CA [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:CN**

- Hu et al. (2024) argue that A general-purpose retrieval embedding model such as BGE, pre-trained only on a general corpus, lacks legal-domain knowledge and cannot distinguish terminologies or cases that are semantically similar but have different meanings in the legal domain; it therefore needs to be fine-tuned on a legal corpus before being used to match response sentences to legal articles or to retrieve legal cases. [CLM-0029-007]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: argument

**geographical_proxy:CZ**

- Novotná and Harašta (2025) argue that Retrieval of case law can be evaluated robustly under an imperfect, noisy gold standard of the kind typical of legacy judicial databases by using IDF-weighted keyword overlap as graded relevance, two data-driven relevance thresholds (0.20 balanced, 0.28 strict), paired bootstrap significance testing, and nDCG diagnostics. [CLM-0017-004]. — jurisdiction: geographical_proxy:CZ; basis: dataset_or_experiment

**geographical_proxy:IN**

- Khadloya et al. (2025) argue that Long-record navigation systems should be evaluated with a protocol measuring time-to-relevance, strict-hit accuracy at anchor (paragraph or table-cell) level, and end-to-end latency, against a manual stock-PDF-reader baseline, using lawyer-authored speakable queries paired with gold anchors; a near hit is not enough, the system must land on the exact paragraph or cell. [CLM-0019-008]. — jurisdiction: geographical_proxy:IN [jurisdiction inferred]; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that A general-purpose retrieval embedding model such as BGE, pre-trained only on a general corpus, lacks legal-domain knowledge and cannot distinguish terminologies or cases that are semantically similar but have different meanings in the legal domain; it therefore needs to be fine-tuned on a legal corpus before being used to match response sentences to legal articles or to retrieve legal cases. [CLM-0029-007] is in tension with the claim that For retrieving semantically similar Czech Constitutional Court decisions, a general-purpose OpenAI embedder (text-embedding-3-large) consistently and statistically significantly outperforms a domain-specific BERT encoder pre-trained from scratch on about 34,000 of the court's decisions, across all cut-offs (k = 10, 20, 100) and both relevance thresholds (0.20, 0.28), in nDCG, P@k and HitRate@k. [CLM-0017-001] (inferred, medium). Note: One holds that a general-purpose embedding model lacks the legal knowledge needed to retrieve legal texts; the other finds a general-purpose embedder outperforming a domain-specific encoder on legal case retrieval.
- The claim that Fine-tuning the BGE embedding model on the LeCaRD training split significantly increases NDCG@10, @20 and @30 for Chinese legal case retrieval over both BM25 and untuned BGE, which shows that the fine-tuned model learns legal knowledge and better distinguishes legal cases that are semantically similar but not legally relevant; nonetheless CaseEncoder, SAILER and CaseFormer still outperform the fine-tuned BGE. [CLM-0029-009] is in tension with the claim that For retrieving semantically similar Czech Constitutional Court decisions, a general-purpose OpenAI embedder (text-embedding-3-large) consistently and statistically significantly outperforms a domain-specific BERT encoder pre-trained from scratch on about 34,000 of the court's decisions, across all cut-offs (k = 10, 20, 100) and both relevance thresholds (0.20, 0.28), in nDCG, P@k and HitRate@k. [CLM-0017-001] (inferred, medium). Note: One finds legal-domain fine-tuning of an embedding model significantly improves case retrieval; the other finds a general embedder beating a domain-trained encoder — reconcilable if fine-tuning a general model differs from training a small domain model from scratch.
- The claim that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002] is in tension with the claim that For retrieving semantically similar Czech Constitutional Court decisions, a general-purpose OpenAI embedder (text-embedding-3-large) consistently and statistically significantly outperforms a domain-specific BERT encoder pre-trained from scratch on about 34,000 of the court's decisions, across all cut-offs (k = 10, 20, 100) and both relevance thresholds (0.20, 0.28), in nDCG, P@k and HitRate@k. [CLM-0017-001] (inferred, medium). Note: One finds legal-oriented encoders better than generic ones; the other finds a general-purpose embedder beating a domain-trained encoder on legal retrieval.

## Distribution

Sources with claims on this concept: 13; claims: 55.

**By contribution type**

| value | sources |
|---|---|
| technical | 12 |
| empirical_quantitative | 11 |
| survey | 2 |
| theoretical | 2 |
| doctrinal | 1 |
| empirical_qualitative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 5 |
| IN | 2 |
| US | 2 |
| CA | 1 |
| CN | 1 |
| CZ | 1 |
| GB | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 10 |
| geographical_proxy:IN | 3 |
| geographical_proxy:US | 2 |
| CA | 1 |
| CN | 1 |
| CZ | 1 |
| geographical_proxy:CA | 1 |
| geographical_proxy:CN | 1 |
| geographical_proxy:CZ | 1 |
| geographical_proxy:CoE | 1 |
| geographical_proxy:EU | 1 |
| geographical_proxy:GB | 1 |

**By year**

| value | sources |
|---|---|
| 2025 | 4 |
| 2023 | 3 |
| 2021 | 2 |
| 2024 | 2 |
| 2019 | 1 |
| 2020 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
