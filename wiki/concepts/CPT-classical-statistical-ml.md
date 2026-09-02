---
id: "CPT-classical-statistical-ml"
label: "Classical statistical machine learning"
status: "anchor"
concept_type: "technique_class"
definition: "Feature-based learners such as SVMs, logistic regression, random forests, and n-gram models."
aliases: []
broader: []
sources: ["SRC-0001", "SRC-0002", "SRC-0005", "SRC-0018", "SRC-0023", "SRC-0027", "SRC-0028", "SRC-0033", "SRC-0043", "SRC-0044", "SRC-0045", "SRC-0046", "SRC-0049"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Classical statistical machine learning

_Status: anchor; family: technique_class._

## Definition

Feature-based learners such as SVMs, logistic regression, random forests, and n-gram models.

Conceptual claims on this concept, each with its source:
- Gridin (2026): Deterministic linear models such as decision trees, logistic regression, and rule-based expert systems cannot hallucinate, because their logic is hardcoded and observable; they can only evaluate input data against pre-defined factual datasets, and so provide absolute transparency at the cost of the linguistic creativity and processing capacity of an LLM. [CLM-0049-004]

## Claims about the concept

### Descriptive

**US**

- Mahoney et al. (2021) state that Although attorneys have used machine learning text classification (predictive coding) for more than ten years to cull large volumes of electronically stored data and identify responsive documents, reducing the discovery costs of legal matters, the technology faces a perception challenge: lawyers sometimes regard it as a 'black box', because typically no extra information is provided to explain why documents are classified as responsive. [CLM-0027-008]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**general**

- Mokanov (2019) state that The full-text search queries lawyers use to research a client's situation are often limited in scope and may miss nuances of the situation, and existing 'more like this' systems are typically bag-of-words approaches with limited understanding of content that do not consider citations, which are reliable indicators of popularity and authority. [CLM-0001-003]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Maurya (2025) state that The statistical machine-learning models applied to law in the 1990s and 2000s (decision trees, support vector machines, latent semantic analysis, early predictive analytics) laid a foundation but struggled with longer context dependencies, cross-referencing and nuanced explanation, so a true leap required deeper linguistic modelling. [CLM-0033-004]. — jurisdiction: general; basis: literature
- Medvedeva et al. (2021) state that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015]. — jurisdiction: general; basis: argument
- Mahoney et al. (2019) state that The MID_75RC strategy, which selects additional training documents nearest the cut-off score that yields 75 percent recall of all responsive documents, is a novel active learning selection strategy not previously seen in the literature. [CLM-0046-016]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Interpretive

**general**

- Mahoney et al. (2019) read E-discovery as follows: The conflicting conclusions of Cormack and Grossman (that top-scored document selection consistently outperforms other active learning strategies) and of Chhatwal et al. (that always selecting the highest-scoring documents may not be the most efficient approach) are due to evaluating the selection strategies differently, on the training set alone versus on both the selected documents and the documents classified by the model, and both are understandable given the dual purpose of active learning: quickly finding as many relevant documents as possible and training an effective final model in as few rounds as possible. [CLM-0046-012]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Normative

**undetermined**

- Mahoney et al. (2019) argue that Legal teams should consider the MID_75RC active learning selection strategy (selecting training documents nearest the 75 percent recall cut-off score) in their predictive coding process to help reduce review costs. [CLM-0046-007]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Empirical

**general**

- Hartung et al. (2026) report that Individual eras of NLP methods (from tf-idf and SVM via word2vec, RNN and LSTM to transformers, LLMs and RAG) can be traced in the Legal NLP literature; most methods seem to reach peak popularity in Legal NLP some time after they were first published, but that delay tends to get shorter for newer methods, and the data show persistent progress within the field toward cutting-edge models at any given point in time. [CLM-0023-010]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024

**geographical_proxy:CoE**

- Medvedeva et al. (2021) report that Forecasting judgements of the European Court of Human Rights from communicated cases is a much harder task than classifying final judgements from the facts section of the judgement: on identical sets of cases, forecasting macro F-scores (about 0.57 to 0.67) are substantially lower than classification macro F-scores (about 0.75 to 0.92) for all test years except 2020. [CLM-0045-003]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that Although H-BERT and LEGAL-BERT generally outperform a linear SVM when classifying final judgements of the European Court of Human Rights, they do not improve over the SVM when forecasting judgements from communicated cases. [CLM-0045-004]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that The higher performance of judgement classification over forecasting is not explained by the larger amount of text in final judgements; the results suggest instead that the facts in final judgements are formulated in a way that is affected by the final ruling. [CLM-0045-005]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment

**geographical_proxy:GB, geographical_proxy:IN**

- Deroy et al. (2024) report that Abstractive summarization models and general-domain LLMs generally perform better than extractive summarization methods for legal case judgement summarization, both on traditional summary-quality metrics (ROUGE, METEOR, BERTScore) and in human evaluation; on the Indian Supreme Court dataset the abstractive models (including LLMs) perform at par with the best extractive models rather than clearly above them. [CLM-0028-001]. — jurisdiction: geographical_proxy:GB, geographical_proxy:IN (cumulative); basis: dataset_or_experiment

**geographical_proxy:IN**

- Mandal et al. (2021) report that Using document-specific catchphrases can improve the performance of existing unsupervised extractive legal case summarization algorithms: when catchphrases extracted by PSLegal or D2V-BiGRU-CRF are incorporated, both DELSumm and CaseSummarizer show improvement across all performance metrics on a set of Indian Supreme Court case documents. [CLM-0005-003]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Mandal et al. (2021) report that In every tested variation, DELSumm with document-specific catchphrases produces better summaries than the original DELSumm on Indian Supreme Court case documents; the best performance is obtained when DELSumm uses catchphrases identified by PSLegal, where the Rouge-2 F-score rises from 0.4217 to 0.4435, and this improvement comes on top of DELSumm already outperforming several other summarization methods on the same dataset. [CLM-0005-004]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Mandal et al. (2021) report that In every tested variation, CaseSummarizer with document-specific catchphrases (from D2V-BiGRU-CRF and/or PSLegal, with or without the legal dictionary) produces better summaries than the original CaseSummarizer on Indian Supreme Court case documents. [CLM-0005-005]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that On Indian Supreme Court judgements, legal domain-specific abstractive summarization models achieve slightly higher ROUGE, METEOR and BLEU scores than extractive summarization models (and than general-domain LLMs), but the improvement over the best extractive model is statistically significant only for the ROUGE-L metrics. [CLM-0044-002]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that For prior case retrieval over Indian Supreme Court judgements, the SemMatch technique applied to testimony and evidence sentences is the best performing technique averaged across 10 diverse queries in both R-Precision and Average Precision, and the most consistent across queries (minimum R-Precision 0.24), compared with BM25 and Sentence-BERT baselines that fall to an R-Precision of 0 on some queries. [CLM-0043-009]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

**geographical_proxy:US**

- Steenhuis (2025) report that A weighted ensemble of three inexpensive LLMs (GPT-5-nano, Gemini 2.5-flash, Mistral small) combined with keyword matching and the traditional-ML Spot classifier meets or slightly exceeds the classification accuracy of the frontier model GPT-5 alone on legal problem classification of real-world referral queries (97.37% versus 96.66% hits@2), while greatly exceeding the accuracy of each inexpensive model used alone; the 0.71-point margin over GPT-5 is likely statistically insignificant. [CLM-0018-001]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Steenhuis (2025) report that Small-model LLM ensembles substantially improve on the performance of older machine-learning and keyword-matching approaches to classifying legal problems: keyword matching set a baseline of about 54% hits@2, the Spot classifier scored about 59%, and TF-IDF fared worst at about 31%, against 97.37% for the ensemble. [CLM-0018-003]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Mahoney et al. (2021) report that Both the Snippet Model Method and the Iterative Snippet Model Method outperform a document-level training classification method in identifying responsive text snippets (rationales) in responsive documents: on three datasets from real legal matters they identified 50% more responsive documents than the document-level model at the [0.9, 1] snippet-score threshold, and on Datasets A and C they achieved much higher average document-score reductions when the identified rationales were removed (0.7 and 0.67 versus 0.47 on Dataset A; 0.52 and 0.46 versus 0.34 on Dataset C), while on Dataset B all three models achieved similar reductions slightly above 0.3. [CLM-0027-002]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that The Snippet Model Method almost always performs slightly better than the Iterative Snippet Model Method at identifying rationales, probably because classification errors propagate through the sequence of models the iterative method builds, starting from a document model that is never 100% accurate. [CLM-0027-004]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that It is feasible to build machine learning models that automatically identify rationales without using annotated text snippets for training, and automating the identification of training text snippets without human review could make the application of snippet-trained predictive models a practical approach in legal document review, since snippet-trained models have higher precision than models trained on whole documents but manually annotating training snippets is not generally practical during a review. [CLM-0027-009]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Deroy et al. (2024) report that On US government reports (GOVREPORT), both general-domain LLMs and legal-domain abstractive models perform much better than the extractive CaseSummarizer, which is expected because CaseSummarizer is designed specifically for summarizing legal case judgements rather than other types of legal documents. [CLM-0028-014]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

**undetermined**

- Mandal et al. (2021) report that The unsupervised catchphrase extraction method PSLegal and the supervised sequence-tagging model D2V-BiGRU-CRF both extract meaningful catchphrases from legal case documents that agree with those chosen by law domain experts. [CLM-0005-009]. — jurisdiction: undetermined; basis: literature
- Mahoney et al. (2019) report that Seed set selection strategies have only a very modest impact on the performance of active learning strategies in predictive coding, especially after many rounds of active learning. [CLM-0046-001]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Among active learning document selection strategies, the top-ranked (TOP) strategy is the most sensitive to the seed set selection strategy, which implies that in the Continuous Active Learning protocol the seed set selection strategy has an impactful role and should be considered carefully. [CLM-0046-002]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that On a low richness document population, the seed set selection strategy has a greater impact on active learning performance, and judgmental seed set selection strategies using keywords or clustering outperform randomly selected seed sets in the early rounds. [CLM-0046-003]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Active learning selection strategies such as uncertainty sampling (selecting documents with scores nearest 0.5) and random selection can generate an effective predictive coding model within fewer rounds than the popular top-ranked (TOP) selection strategy. [CLM-0046-004]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Selecting additional training documents nearest to the model's cut-off score for 75 percent recall (the MID_75RC strategy) performs best in almost all experimental scenarios, and would be the most effective active learning strategy when the objective is to achieve 75 percent recall. [CLM-0046-005]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that In the first 50 rounds of active learning, the MID_75RC strategy consistently requires less review to reach 75 percent recall than the top-ranked (TOP) strategy across all four data sets, with a maximum saving close to 20 percent of the document population. [CLM-0046-006]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that The dominant factor in reaching the optimum performance round (the earliest round at which the review required to reach 75 percent recall is lowest) is the active learning document selection strategy, not the seed set selection strategy: random, uncertainty (MID-50) and MID_75RC strategies consistently take fewer rounds to reach the optimum round, and fewer rounds to reach a satisficing goal within 5, 10 or 15 percent of the optimum. [CLM-0046-008]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that When data sets with extremely low richness are excluded, training with documents nearest the 75 percent recall cut-off score (MID_75RC) results in significantly higher performing models in early training rounds such as round 10 or 20, rounds often associated with stopping points for Simple Active Learning; in all three data sets with richness above 10 percent, MID_75RC reached performance within roughly 10 percent of the optimum within 10 rounds of active learning. [CLM-0046-009]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Seed sets derived from keyword search have a higher richness (positive class rate) than the overall data set, while randomly sampled seed sets generally have a richness similar to that of the overall data set. [CLM-0046-017]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Conceptual

**general**

- Gridin (2026) argue that Deterministic linear models such as decision trees, logistic regression, and rule-based expert systems cannot hallucinate, because their logic is hardcoded and observable; they can only evaluate input data against pre-defined factual datasets, and so provide absolute transparency at the cost of the linguistic creativity and processing capacity of an LLM. [CLM-0049-004]. — jurisdiction: general; basis: argument

### Predictive

**general**

- Mahoney et al. (2021) argue that Because training documents in a legal document review matter can contain tens of thousands of tokens, most of which are likely not responsive content, document-level models trained on such documents may be less accurate in identifying short responsive text snippets than a method that derives its training data at the snippet level. [CLM-0027-011]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Methodological

**general**

- Alschner et al. (2020) argue that Rules-based readability assessment of statutes could be complemented with machine learning: rules suit prominent plain language guidelines that are simple to implement (e.g. shall/must), whereas more complex features such as problematic nominalizations require a more nuanced approach, for which human expert labelling scaled through machine learning classifiers offers an alternative; in combination, the two approaches provide a scalable means to operationalize plain language assessments of statutes. [CLM-0002-010]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mandal et al. (2021) argue that Document-specific catchphrases can be incorporated into existing legal case summarizers by substituting them for the summarizer's static domain-specific component: in DELSumm, the fixed set of legal-dictionary content words is replaced by catchphrases extracted from the input document to be summarized, so that sentences containing document-specific catchphrases are given more importance; in CaseSummarizer, the entity count in the sentence-scoring expression is replaced by the number of document-specific catchphrases in the sentence. [CLM-0005-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2021) argue that Two machine learning methods, the Snippet Model Method and the Iterative Snippet Model Method, can train models that locate responsive text snippets (rationales) within responsive documents in legal document review without using human-annotated training text snippets. The Snippet Model Method applies a document-level text model to score all overlapping text snippets of the training documents, selects high-scoring snippets from responsive documents and randomly selected snippets from non-responsive documents as training data, and trains a snippet-level detection model on them; the Iterative Snippet Model Method repeats this while halving the snippet size at each iteration until a user-defined minimum size is reached. [CLM-0027-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2019) argue that Focusing active learning training around the dynamic recall cut-off score from round to round makes sense in theory: documents just above the cut-off score are the positives the model includes with the least certainty, offering the most opportunity to improve precision, and documents just below it are the excluded negatives with the highest richness, offering the most opportunity to improve recall. [CLM-0046-010]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2019) argue that In an active learning scenario, the percentage of documents requiring review to achieve a target recall is computed after each round over two sets of documents, those selected and reviewed during training and those the model categorizes as positive at its cut-off score, because as rounds increase the documents reviewed for training could constitute a considerable portion of the population requiring review, unlike in passive learning where they have a negligible impact. [CLM-0046-011]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:IN**

- Ali et al. (2021) argue that In the absence of publicly annotated datasets for identifying evidence and testimony sentences in court judgements, such sentences can be identified without manually annotated training data by a two-step weakly supervised approach: high-precision linguistic rules first, then a BiLSTM multi-label sentence classifier trained on the rule-identified sentences to improve recall. [CLM-0043-004]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015] is in tension with the claim that Traditional machine-learning explanations of predicted legal outcomes, such as listing or highlighting the most influential words in the text, are unhelpful and inappropriate in a legal context, because the right to explanation requires an explanation capable of persuading the losing party and withstanding appeal: not an account of how the decision was reached, but of why the decision represents the proper application of the law. [CLM-0004-004] (inferred, medium). Note: One holds that SVM coefficients and attention over facts let the basis of a classification be determined to some extent; the other holds that such word- or feature-level explanations are unhelpful and inappropriate in a legal context.
- The claim that Post-hoc explainable AI is not merely insufficient but actively dangerous in high-stakes jurisprudential contexts, because post-hoc explanations bear no guaranteed mathematical relationship to a model's actual computations and generate legally plausible narratives that mask bias; a hallucinated explanation of a black box is more dangerous than no explanation at all, so models that are interpretable by design should be used instead. [CLM-0049-013] is in tension with the claim that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015] (inferred, low). Note: One deems post-hoc explanation of black-box outputs actively dangerous in legal contexts; the other finds coefficients and attention adequate to determine a classifier's basis to some extent.

## Distribution

Sources with claims on this concept: 13; claims: 41.

**By contribution type**

| value | sources |
|---|---|
| technical | 13 |
| empirical_quantitative | 11 |
| theoretical | 3 |
| normative | 2 |
| survey | 2 |
| doctrinal | 1 |
| empirical_qualitative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| US | 4 |
| IN | 3 |
| general | 3 |
| CA | 2 |
| CoE | 2 |
| EU | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 9 |
| geographical_proxy:IN | 4 |
| geographical_proxy:US | 3 |
| undetermined | 2 |
| US | 1 |
| geographical_proxy:CoE | 1 |
| geographical_proxy:GB | 1 |

**By year**

| value | sources |
|---|---|
| 2021 | 4 |
| 2019 | 2 |
| 2025 | 2 |
| 2026 | 2 |
| 2020 | 1 |
| 2023 | 1 |
| 2024 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
