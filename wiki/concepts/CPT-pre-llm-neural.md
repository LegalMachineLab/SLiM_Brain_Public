---
id: "CPT-pre-llm-neural"
label: "Pre-LLM neural models"
status: "anchor"
concept_type: "technique_class"
definition: "Neural models predating large language models: CNNs, RNNs, BiLSTMs, and encoder models such as BERT fine-tuned for a task."
aliases: []
broader: []
sources: ["SRC-0001", "SRC-0003", "SRC-0004", "SRC-0005", "SRC-0006", "SRC-0007", "SRC-0008", "SRC-0012", "SRC-0013", "SRC-0014", "SRC-0015", "SRC-0017", "SRC-0023", "SRC-0028", "SRC-0029", "SRC-0033", "SRC-0043", "SRC-0044", "SRC-0045", "SRC-0048"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Pre-LLM neural models

_Status: anchor; family: technique_class._

## Definition

Neural models predating large language models: CNNs, RNNs, BiLSTMs, and encoder models such as BERT fine-tuned for a task.

Conceptual claims on this concept, each with its source:
- Holzenberger et al. (2020): BERT-based models can outperform trained lawyers at identifying Black's Law Dictionary legal terms in case law because the models learn the dictionary's well-developed inclusion standards from the training set, with which lawyers are not necessarily familiar, and because pre-processing dropped some legal terms that were subsets of too many others, which the lawyers tended to identify. [CLM-0003-013]
- Li et al. (2022): Prefix domain adaptation achieves better few-shot performance than regular prefix tuning because, after the domain adaptation step, the pre-trained prompts start closer to an effective prompt for the downstream task — analogous to how full domain adaptation moves model parameters closer to optimal parameters. [CLM-0006-003]

## Claims about the concept

### Descriptive

**general**

- Li et al. (2022) state that No prior work has trained a prefix prompt for a specific domain using an unsupervised pre-training task (masked language modelling) to better initialise it for downstream tasks, and prefix domain adaptation is among the first explorations of parameter-efficient methods for tuning language models in the legal domain. [CLM-0006-017]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- T.Y.S.S. et al. (2024) state that Contemporary legal NLP increasingly applies models that statistically classify legal conclusions from text with little or no explicit domain representation; while conceptually simpler, these approaches often fall short in providing usable justifications that connect to appropriate legal concepts, at the cost of interpretability. [CLM-0014-002]. — jurisdiction: general; basis: literature
- Maurya (2025) state that To date there is no systematic, large-scale comparative analysis of state-space models such as Mamba against transformer models on statutory and case-law tasks; existing legal NLP benchmarks focus almost exclusively on transformer baselines, so the linear scaling and throughput gains of Mamba have not been mapped against practical legal workflows. [CLM-0033-001]. — jurisdiction: general; basis: literature
- Maurya (2025) state that Transformer architectures suffer from quadratic computational complexity as sequence length increases, which for legal documents spanning dozens to hundreds of pages and relying on long-range context is a severe barrier: inputs must be truncated or windowed at the risk of losing crucial context, and sparse-attention variants (Longformer, BigBird, Reformer) extend context windows but still fall short of full-document, fully contextual analysis of massive legal corpora without sacrificing efficiency. [CLM-0033-005]. — jurisdiction: general; basis: literature
- Maurya (2025) state that Mamba's selective state-space mechanism updates state representations in linear time and decouples memory and compute needs from sequence length, allowing the processing of sequences vastly longer than transformers feasibly manage on typical hardware, with higher inference throughput on long-document tasks. [CLM-0033-006]. — jurisdiction: general; basis: literature
- Medvedeva et al. (2021) state that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015]. — jurisdiction: general; basis: argument
- Chalkidis et al. (2021) state that LexGLUE is the first unified benchmark for assessing the performance of NLP models on legal natural language understanding: it collects seven existing, publicly available and documented English legal NLP datasets (ECtHR Tasks A and B, SCOTUS, EUR-LEX, LEDGAR, UNFAIR-ToS, CaseHOLD) under a standardized evaluation, with tasks simplified to make them accessible to newcomers and generic models. [CLM-0048-001]. — jurisdiction: general; basis: dataset_or_experiment

### Interpretive

**geographical_proxy:IN, geographical_proxy:GB**

- Deroy et al. (2024) read Summarisation as follows: Legal-LED's hallucination of US court and statute names in summaries of Indian and UK judgements is probably due to the model having been trained on US legal document-summary pairs, which gives it a tendency to generate US court and statute names seen during training. [CLM-0028-005]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment

### Normative

**general**

- Maurya (2025) argue that For real-world adoption of state-space models such as SSD-Mamba in legal practice it is critical to provide transparent rationales for predictions, and future research should explore passage highlighting, causal attribution and human-interpretable justifications to make their outputs explainable to practitioners. [CLM-0033-013]. — jurisdiction: general; basis: argument

**geographical_proxy:IN**

- Deroy et al. (2023) argue that Pre-trained abstractive summarization models and general-domain large language models are not yet ready for fully automatic deployment for legal case judgement summarization; a human-in-the-loop approach, in which a legal expert monitors the generated summaries and manually checks for inconsistencies, is more suitable at present. [CLM-0044-001]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

### Empirical

**general**

- Li et al. (2022) report that Prefix domain adaptation — pre-training a deep prefix prompt with the masked language modelling task on a large unsupervised domain-specific corpus and then using that prompt to initialise prefix tuning for downstream tasks — matches or exceeds the few-shot performance of LEGAL-BERT and related techniques on legal classification tasks while tuning only approximately 0.1% of model parameters. [CLM-0006-001]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that In few-shot settings, prefix domain adaptation outperforms both regular prefix tuning and full finetuning in most tasks across few-shot sizes, despite training considerably fewer parameters, and is comparable to full domain adaptation, in some settings even outperforming it. [CLM-0006-002]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that Regular prefix tuning (P-Tuning v2) falls behind full parameter tuning in few-shot settings. [CLM-0006-004]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that LEGAL-BERT performs worse than other techniques, and shows more instability across random seeds, on datasets with more informal language such as the Legal Advice Reddit dataset, because the LEGAL-BERT-SC model was trained only on very formal legal text and did not see the colloquialisms and slang prevalent in informal text. [CLM-0006-005]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that On Legal Advice Reddit data, prefix domain adaptation is comparable to full finetuning and consistently outperforms regular prefix tuning as the number of training samples increases, and finetuning is less stable across runs than prefix domain adaptation. [CLM-0006-009]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that Prefix domain adaptation scales to larger models: with RoBERTa-large it remains comparable to or outperforms full finetuning, and at few-shot sizes 32 to 128 prefix domain adaptation with RoBERTa-base is even comparable to full finetuning with RoBERTa-large. [CLM-0006-010]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that The calibration (expected calibration error) of prefix domain adaptation is better than that of full finetuning across tasks and comparable to LEGAL-BERT; on the well-formulated Law Stack Exchange questions legal models are better calibrated, while on Reddit data prefix domain adaptation is very competitive. [CLM-0006-011]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that More optimisation steps during the prefix domain adaptation step lead to better downstream performance, because a longer training time means the prefix starts closer to an ideal one for the downstream task. [CLM-0006-013]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that Although each optimisation step is faster with regular prefix tuning, regular prefix tuning converges slowly and is therefore not necessarily faster than finetuning; prefix domain adaptation converges faster than regular prefix tuning because its prompts start closer to a desired solution and fewer training steps are needed. [CLM-0006-014]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Tan et al. (2024) report that Entailment (NLI) models fine-tuned on short summaries, such as the A2CU NLI model trained on the RoSE dataset, perform less well on long-form summaries and do not perform well when presented with more than a few sentences, even though they can theoretically take in longer text. [CLM-0015-005]. — jurisdiction: general; basis: none_stated
- Hartung et al. (2026) report that Individual eras of NLP methods (from tf-idf and SVM via word2vec, RNN and LSTM to transformers, LLMs and RAG) can be traced in the Legal NLP literature; most methods seem to reach peak popularity in Legal NLP some time after they were first published, but that delay tends to get shorter for newer methods, and the data show persistent progress within the field toward cutting-edge models at any given point in time. [CLM-0023-010]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Chalkidis et al. (2021) report that Legal documents are usually much longer (thousands of words) than the texts typically considered in NLP tasks, so standard Transformer-based models that process up to 512 sub-word units cannot be directly applied across all LexGLUE datasets unless documents are severely truncated; even models specifically designed for long text (Longformer, BigBird, up to 4096 sub-words) are largely exceeded in three of the seven LexGLUE tasks, so handling long legal documents remains a challenge. [CLM-0048-007]. — jurisdiction: general; basis: dataset_or_experiment

**geographical_proxy:CN**

- Hu et al. (2024) report that Fine-tuning the BGE embedding model on the LeCaRD training split significantly increases NDCG@10, @20 and @30 for Chinese legal case retrieval over both BM25 and untuned BGE, which shows that the fine-tuned model learns legal knowledge and better distinguishes legal cases that are semantically similar but not legally relevant; nonetheless CaseEncoder, SAILER and CaseFormer still outperform the fine-tuned BGE. [CLM-0029-009]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:CZ**

- Novotná and Harašta (2025) report that For retrieving semantically similar Czech Constitutional Court decisions, a general-purpose OpenAI embedder (text-embedding-3-large) consistently and statistically significantly outperforms a domain-specific BERT encoder pre-trained from scratch on about 34,000 of the court's decisions, across all cut-offs (k = 10, 20, 100) and both relevance thresholds (0.20, 0.28), in nDCG, P@k and HitRate@k. [CLM-0017-001]. — jurisdiction: geographical_proxy:CZ; basis: dataset_or_experiment
- Novotná and Harašta (2025) report that The likely reason the from-scratch domain BERT lags behind the general-purpose embedder is scale and training objective: the general embedder benefits from vastly more pretraining data and a broader semantic curriculum, while the domain model is smaller, trained only with masked language modelling, and lacks contrastive or retrieval-aware supervision. Under noisy labels, pretraining scale and semantic breadth outweigh domain restriction. [CLM-0017-002]. — jurisdiction: geographical_proxy:CZ; basis: dataset_or_experiment
- Novotná and Harašta (2025) report that Splitting long court decisions into overlapping 512-token windows and averaging the window embeddings increases a BERT encoder's exposure to long texts but adds little new signal, because overlapping segments are semantically redundant and averaging them can dilute discriminative cues. [CLM-0017-007]. — jurisdiction: geographical_proxy:CZ; basis: argument
- Novotná and Harašta (2025) report that For document embeddings of Czech Constitutional Court decisions produced by a from-scratch domain BERT, self-attention pooling of window hidden states consistently outperforms mean pooling in retrieval. [CLM-0017-009]. — jurisdiction: geographical_proxy:CZ; basis: dataset_or_experiment

**geographical_proxy:CoE**

- Li et al. (2022) report that On the ECHR binary violation prediction task, whose train and test splits have different distributions, prefix-tuning-based approaches perform better than full finetuning in very-low-data settings (4 to 16 examples), which suggests that prefix tuning approaches are more robust to changes in distribution and possibly to noise. [CLM-0006-007]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Li et al. (2022) report that Finetuned BERT with truncation to 500 tokens performs much better on the ECHR violation prediction task (macro F1 of 66.5) than reported by Chalkidis et al. (2019), who report an F1 of 17, worse than random guessing; the underperformance reported there could be caused by a mistake in their training process. [CLM-0006-008]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that Forecasting judgements of the European Court of Human Rights from communicated cases is a much harder task than classifying final judgements from the facts section of the judgement: on identical sets of cases, forecasting macro F-scores (about 0.57 to 0.67) are substantially lower than classification macro F-scores (about 0.75 to 0.92) for all test years except 2020. [CLM-0045-003]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that Although H-BERT and LEGAL-BERT generally outperform a linear SVM when classifying final judgements of the European Court of Human Rights, they do not improve over the SVM when forecasting judgements from communicated cases. [CLM-0045-004]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment

**geographical_proxy:CoE, geographical_proxy:EU**

- Maurya (2025) report that On long-text legal corpora such as ECtHR and EUR-Lex, Mamba and SSD-Mamba match or surpass transformer models in classification performance while maintaining two to three times higher throughput, demonstrating that state-space models handle extreme input lengths without the windowing overhead that degrades transformer performance. [CLM-0033-009]. — jurisdiction: geographical_proxy:CoE, geographical_proxy:EU (cumulative); basis: dataset_or_experiment

**geographical_proxy:CoE, geographical_proxy:EU, geographical_proxy:US, geographical_proxy:IN**

- Maurya (2025) report that Attention-based models and state-space models capture complementary aspects of legal reasoning: transformers (Longformer, DeBERTa) retain small advantages in Macro-F1 and Recall@10 on specific datasets and emphasise local contextual nuances, whereas Mamba-based models excel in throughput, scalability and long-sequence stability, preserving global coherence over thousands of tokens. [CLM-0033-011]. — jurisdiction: geographical_proxy:CoE, geographical_proxy:EU, geographical_proxy:US, geographical_proxy:IN (cumulative); basis: dataset_or_experiment

**geographical_proxy:CoE, geographical_proxy:IN, geographical_proxy:EU, geographical_proxy:US**

- Maurya (2025) report that Among the benchmarked models, SSD-Mamba achieves the best overall balance of scalability, accuracy and efficiency, making it a strong candidate for large-scale, real-world legal AI applications involving statutes and long-form case law; for resource-constrained deployments such as large-scale statutory analysis, court policy studies or law-firm knowledge management it provides state-of-the-art accuracy at dramatically lower computational cost. [CLM-0033-010]. — jurisdiction: geographical_proxy:CoE, geographical_proxy:IN, geographical_proxy:EU, geographical_proxy:US (cumulative); basis: dataset_or_experiment

**geographical_proxy:CoE, geographical_proxy:US**

- Chalkidis et al. (2021) report that On the LexGLUE datasets with long documents (ECtHR Task A, ECtHR Task B, SCOTUS), a hierarchical variant of BERT that encodes each paragraph independently and then contextualises the paragraph representations with a second-level Transformer encoder clearly outperforms standard BERT fed with documents truncated to 512 tokens (+12.2%, +10.6% and +3.5% respectively); the gains are lower in SCOTUS, a topic classification task where long-range reasoning is not needed, than in the ECtHR tasks, where multiple distant facts need to be combined. [CLM-0048-005]. — jurisdiction: geographical_proxy:CoE, geographical_proxy:US (cumulative); basis: dataset_or_experiment

**geographical_proxy:GB**

- Xie et al. (2024) report that Fine-tuned transformer models outperform zero-shot and few-shot large language models on the UK Employment Tribunal four-class case outcome prediction task, with fine-tuned T5 as the best-performing model, and all tested models significantly outperform a random-guess baseline. [CLM-0013-005]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that For automated point extraction from long-form legal summaries, a Dense X proposition-extraction model fine-tuned on legal data and an LLM prompted with examples both improve on the Dense X baseline by 3-6 percentage points on recall- and precision-oriented easiness scores, and outperform sentence splitting and the A2CU content-unit generator. [CLM-0015-009]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that The A2CU content-unit generator, trained on non-legal data, produces points from legal text that are too granular, fail to capture the complex meaning of the original text and are sometimes not proper declarative propositions, whereas an LLM prompted with examples produces points that are correct and properly capture the original meaning. [CLM-0015-010]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that For deciding whether two points from legal summaries make the same point, an LLM given the full reference summary, the surrounding points, an explanation of what making the same point means in a court case, and examples performs much better (in F1) than cosine similarity and NLI-based methods, indicating that the LLM can better distinguish the nuances of complex legal statements than simpler models; few-shot and many-shot example regimes perform similarly. [CLM-0015-011]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that A non-LLM pointwise variant (fine-tuned Dense X for point extraction and fine-tuned A2CU-NLI for point matching) performs better than the baseline metrics in some correlation categories but not as well as the LLM-based pointwise variants, which shows that the use of advanced LLM models yields a significant advantage in evaluating complex legal text. [CLM-0015-015]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

**geographical_proxy:GB, geographical_proxy:IN**

- Deroy et al. (2024) report that Abstractive summarization models and general-domain LLMs generally perform better than extractive summarization methods for legal case judgement summarization, both on traditional summary-quality metrics (ROUGE, METEOR, BERTScore) and in human evaluation; on the Indian Supreme Court dataset the abstractive models (including LLMs) perform at par with the best extractive models rather than clearly above them. [CLM-0028-001]. — jurisdiction: geographical_proxy:GB, geographical_proxy:IN (cumulative); basis: dataset_or_experiment

**geographical_proxy:IN**

- Mandal et al. (2021) report that Using document-specific catchphrases can improve the performance of existing unsupervised extractive legal case summarization algorithms: when catchphrases extracted by PSLegal or D2V-BiGRU-CRF are incorporated, both DELSumm and CaseSummarizer show improvement across all performance metrics on a set of Indian Supreme Court case documents. [CLM-0005-003]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that A multitask learning model (MTL-BiLSTM-CRF) that uses label shift prediction as an auxiliary task outperforms existing rhetorical role prediction models, including the BiLSTM-CRF of Bhattacharya et al. (2019) and BERT-based baselines, reaching average macro F1 of 0.70 on income tax, 0.69 on competition law and 0.71 on the combined domain; the label shift prediction task is what contributes the superior performance. [CLM-0007-011]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that LEGAL-BERT performs slightly better than pre-trained BERT on Indian competition-law judgments but slightly worse on income-tax judgments, which might be because LEGAL-BERT was trained on EU legal documents, including European competition law, and not on Indian income tax law documents. [CLM-0007-012]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that The rhetorical role prediction model performs best on the facts label and worst on the ruling-by-lower-court label, mirroring the pattern of agreement observed among the human annotators. [CLM-0007-013]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that The MTL model's performance on income-tax cases comes close to the average inter-annotator agreement, while a gap remains for competition law; the model performs better on income tax than on competition law, the opposite of the trend among annotators, possibly because the selected income-tax documents are restricted to specific sections of the law and the model learned solely from them without external knowledge, whereas annotators drew on knowledge of the entire income tax law. [CLM-0007-014]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that The MTL rhetorical role model generalises better across legal sub-domains than the BiLSTM-CRF baseline when transferred between the competition-law and income-tax corpus and a criminal and civil case dataset, and both models perform better on the criminal/civil test set when trained on the combined income-tax and competition-law training set. [CLM-0007-015]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that Because rhetorical role annotation is tedious while unlabelled legal documents are abundant, self-training based model distillation on unlabelled documents can improve rhetorical role prediction: after two iterations on the income-tax domain, results improve for the majority of labels (macro F1 from 0.68 to 0.72, with a 0.11 gain for the ruling-by-lower-court label in the first iteration) and the variance of F1 across labels decreases. [CLM-0007-016]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that Feeding a judgment-prediction model only the sentences carrying gold ratio-of-decision and ruling-by-present-court rhetorical roles improves judgment prediction F1 over using the last 512 tokens of the document (0.58 versus 0.55, statistically significant), whereas using predicted rhetorical roles yields performance comparable to the baseline; improving rhetorical role prediction for these two roles would therefore enhance judgment prediction. [CLM-0007-017]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that On Indian Supreme Court judgements, legal domain-specific abstractive summarization models achieve slightly higher ROUGE, METEOR and BLEU scores than extractive summarization models (and than general-domain LLMs), but the improvement over the best extractive model is statistically significant only for the ROUGE-L metrics. [CLM-0044-002]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that Summaries of legal case judgements generated by pre-trained abstractive summarization models and LLMs often contain inconsistent or hallucinated information, including wrong dates, wrong person names and confusion between different persons associated with a case, as well as incomplete sentences or words and sentences merged meaninglessly, the latter mostly occurring at the boundaries of input chunks. [CLM-0044-003]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that Further fine-tuning legal domain-specific abstractive summarization models (Legal-Pegasus and Legal-LED, originally fine-tuned on US legal documents) on Indian judgement-summary pairs improves their performance in terms of both match with gold-standard summaries and consistency with the source document, and can help to reduce hallucinations. [CLM-0044-004]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that Legal-LED, an abstractive summarization model fine-tuned on US legal document-summary pairs, generates names of US courts and US statutes in its summaries of Indian case judgements that are unrelated to the input document, probably because the model tends to reproduce court and statute names seen during training; this type of error was not observed in the summaries generated by the LLMs ChatGPT and DaVinci. [CLM-0044-005]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that Instantiating Evidence Structures with a pre-trained semantic role labelling model achieved 86% accuracy for Observation Frame extraction and 88% for Evidence Frame extraction on 260 instances from 100 random evidence and testimony sentences of Indian Supreme Court judgements, with most incorrect extractions due to parsing errors in the SRL model. [CLM-0043-006]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that Multiplying the Evidence-Structure similarity score by a Sentence-BERT sentence similarity score is necessary because errors in the automated semantic role labelling tool may produce imperfect Evidence Structure instances, and a structure-independent sentence similarity provides a complementary view; a variant of SemMatch without the Sentence-BERT factor reached average R-Precision 0.36 and MAP 0.30 over 10 queries, lower than the full method but comparable in R-Precision to BM25 on testimony and evidence sentences and better than Sentence-BERT alone. [CLM-0043-008]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that For prior case retrieval over Indian Supreme Court judgements, the SemMatch technique applied to testimony and evidence sentences is the best performing technique averaged across 10 diverse queries in both R-Precision and Average Precision, and the most consistent across queries (minimum R-Precision 0.24), compared with BM25 and Sentence-BERT baselines that fall to an R-Precision of 0 on some queries. [CLM-0043-009]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Ali et al. (2021) report that For queries containing negation, Sentence-BERT and SemMatch capture the query's meaning better than BM25, and SemMatch handles negation in a more principled manner because the Evidence Structure Instance captures negation as one of its arguments. [CLM-0043-012]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

**geographical_proxy:IN, geographical_proxy:GB**

- Deroy et al. (2024) report that Summaries of legal case judgements generated by LLMs and legal-domain abstractive summarizers frequently contain hallucinations and inconsistencies: wrongly reported names and monetary values, hallucinated court and statute names, incomplete statute names, incomplete sentences, and merged words or sentences; such errors were found in almost all manually checked summaries. [CLM-0028-003]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that When the legal-domain abstractive model Legal-LED summarizes Indian or UK case judgements, names of US courts and US statutes that are entirely unrelated to the input document appear in its summaries. [CLM-0028-004]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that Further fine-tuning legal-domain abstractive summarizers (Legal-Pegasus, Legal-LED) on data from the target domain improves both the match of their summaries with reference summaries and the consistency of the summaries, and removes the gross hallucinations of US court and statute names; where target-domain data are available, using them for fine-tuning seems an effective approach. [CLM-0028-006]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment

**geographical_proxy:US**

- Holzenberger et al. (2020) report that On the SARA statutory reasoning tasks, straightforward application of contemporary machine reading models (BERT-based and feedforward models) performs comparably to a majority or constant baseline regardless of the underlying method, and performance remains mostly unchanged when the statutes, or the statutes and the context, are removed from the input, meaning that the models are not utilising the statutes. [CLM-0003-008]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Holzenberger et al. (2020) report that Adapting BERT or word vectors to the legal domain (Legal BERT further trained on case law; tax-specific word2vec vectors) has no noticeable effect on performance on the SARA statutory reasoning tasks. [CLM-0003-009]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Holzenberger et al. (2020) report that Further training Bert-Base-Cased with the masked language model objective on 900M tokens of case law yields a Legal BERT that is much better adapted to legal queries: on the natural-language questions and answers of the SARA dataset its perplexity is 2.7, against 14.4 for Bert-Base-Cased. [CLM-0003-011]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Holzenberger et al. (2020) report that On the downstream task of identifying legal terms (tokens or collocations defined in Black's Law Dictionary) in case-law text, a fine-tuned Legal BERT achieves F1 = 0.44 against F1 = 0.35 for fine-tuned Bert-Base-Cased, while two trained lawyers given the same task achieve F1 = 0.26; this indicates that Legal BERT is much better adapted to the legal domain than Bert-Base-Cased. [CLM-0003-012]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that Straightforward prompting of GPT-3 (text-davinci-003) on the SARA statutory-reasoning benchmark yields accuracy better than the previous best published, BERT-based results, with far less human input: the best setting (zero-shot with the statute included) reaches 71% aggregate accuracy on the 100 entailment test cases, significantly better than the BERT-based state of the art (p approximately 0.038) and the majority baseline. [CLM-0008-002]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Hagag et al. (2024) report that In the LegalLens Shared Task 2024, the top-performing teams in both the LegalLens-NER and LegalLens-NLI sub-tasks consistently relied on fine-tuning pretrained language models, and these fine-tuned models outperformed legal-specific models and few-shot methods. [CLM-0012-001]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:US, geographical_proxy:EU, geographical_proxy:CoE**

- Chalkidis et al. (2021) report that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002]. — jurisdiction: geographical_proxy:US, geographical_proxy:EU, geographical_proxy:CoE (cumulative); basis: dataset_or_experiment
- Chalkidis et al. (2021) report that The match between a model's legal pre-training corpus and the legal domain of a task seems to drive its performance: in-domain legal knowledge appears most critical on the two LexGLUE datasets built from US case law (SCOTUS and CaseHOLD), where legal-oriented models improve by approximately 5% over generically pre-trained models; CaseLaw-BERT, trained solely on US case law, performs marginally better than Legal-BERT there, while Legal-BERT, exposed to a wider variety of legal corpora (EU legislation, ECtHR cases, US contracts), performs slightly better on EUR-LEX, LEDGAR and UNFAIR-ToS. [CLM-0048-003]. — jurisdiction: geographical_proxy:US, geographical_proxy:EU, geographical_proxy:CoE (cumulative); basis: dataset_or_experiment
- Chalkidis et al. (2021) report that No single pre-trained Transformer model performs best in all LexGLUE tasks, and the baseline results show that there is still large scope for improvement on the benchmark. [CLM-0048-004]. — jurisdiction: geographical_proxy:US, geographical_proxy:EU, geographical_proxy:CoE (cumulative); basis: dataset_or_experiment

**geographical_proxy:US, geographical_proxy:IN**

- Maurya (2025) report that Attention-based transformer models are particularly effective at capturing fine-grained semantic distinctions when context length is moderate: on SCOTUS issue classification DeBERTa achieves the strongest overall performance (Micro-F1 83.8, Accuracy 84.0) with Longformer close behind, and on ILDC retrieval Longformer and DeBERTa outperform Mamba on Recall@10 and nDCG@10. [CLM-0033-008]. — jurisdiction: geographical_proxy:US, geographical_proxy:IN (cumulative); basis: dataset_or_experiment

**undetermined**

- Mandal et al. (2021) report that The unsupervised catchphrase extraction method PSLegal and the supervised sequence-tagging model D2V-BiGRU-CRF both extract meaningful catchphrases from legal case documents that agree with those chosen by law domain experts. [CLM-0005-009]. — jurisdiction: undetermined; basis: literature

### Conceptual

**general**

- Li et al. (2022) argue that Prefix domain adaptation achieves better few-shot performance than regular prefix tuning because, after the domain adaptation step, the pre-trained prompts start closer to an effective prompt for the downstream task — analogous to how full domain adaptation moves model parameters closer to optimal parameters. [CLM-0006-003]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:US**

- Holzenberger et al. (2020) argue that BERT-based models can outperform trained lawyers at identifying Black's Law Dictionary legal terms in case law because the models learn the dictionary's well-developed inclusion standards from the training set, with which lawyers are not necessarily familiar, and because pre-processing dropped some legal terms that were subsets of too many others, which the lawyers tended to identify. [CLM-0003-013]. — jurisdiction: geographical_proxy:US; basis: argument

### Predictive

**general**

- Mokanov (2019) argue that Transformer XL and XL Net embeddings are expected to yield significant gains over the Doc2Vec embeddings originally used in Facts2Law, but this has yet to be confirmed by the evaluation under way. [CLM-0001-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Li et al. (2022) argue that LEGAL-BERT is not expected to be an effective initialisation for tasks involving legal questions asked by laypersons, which typically do not use formal legal language. [CLM-0006-006]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) argue that Prefix domain adaptation will make few-shot data more usable, and thus reduce data labelling costs, while using parameter-efficient methods to reduce computational and storage costs; the domain-adapted deep prompt is very small (approximately 0.1% of the base model) and therefore easy to store and distribute. [CLM-0006-019]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Maurya (2025) argue that Hybrid architectures combining state-space modelling with selective attention may enable models to capture long-range dependencies and fine-grained token interactions simultaneously, yielding the best of both paradigms. [CLM-0033-012]. — jurisdiction: general; basis: argument
- Chalkidis et al. (2021) argue that Existing legal pre-trained language models rely on relatively small pre-training corpora (12-36 GB), sometimes covering only a narrowly defined area such as US or Chinese court opinions; future work could curate a legal version of the C4 corpus containing multijurisdictional legislation, court decisions, contracts and legal literature at a size of hundreds of GBs, and a large language model capable of processing long structured text pre-trained on such a corpus might excel in LexGLUE. [CLM-0048-016]. — jurisdiction: general; basis: argument

**geographical_proxy:US**

- Holzenberger et al. (2020) argue that Performance on the SARA statutory reasoning dataset will not be improved through straightforward application of a large-scale language model, unlike on other datasets such as COPA, SQuAD 2.0 and SWAG where large pre-trained models produced large gains. [CLM-0003-010]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Methodological

**CA**

- Mokanov (2019) argue that Using the Facts2Law approach, pertinent cases that could have been cited in a Canadian administrative tribunal decision can nevertheless be identified even though the decision-maker chose not to cite other relevant case law. [CLM-0001-009]. — jurisdiction: CA [jurisdiction inferred]; basis: argument

**general**

- Mokanov (2019) argue that For producing whole-document embeddings of legal documents, BERT, although an improvement over Doc2Vec, is less optimal because of the computing power it requires and its small document size of 512 tokens, whereas Transformer XL requires much less processing, works on much larger text sequences, and uses left-to-right context to give different meanings to ambiguous words; XL Net, which is very similar to Transformer XL but does not take word order into account, has shown to lead to even better results. [CLM-0001-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mumford et al. (2021) argue that Explainable case-outcome prediction can be produced by a hybrid system that separates the two stages of reasoning with cases: factor ascription is performed by a machine-learning natural language processing layer (a Hierarchical BERT model outputting, for each base-level factor, a binary 'ascribed' or 'not ascribed' classification), and the decision is reached by balancing the factors within a pre-determined, non-cyclic Abstract Dialectical Framework derived from expert knowledge. [CLM-0004-009]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that A Hierarchical BERT model is suited to factor ascription because it combines strong classification performance with sentence-level attention weights that could sufficiently express the relevant facts explaining a given factor's ascription or non-ascription. [CLM-0004-011]. — jurisdiction: general; basis: argument
- Maurya (2025) argue that Applying a sliding window with 20% overlap and aggregating window-level outputs (averaging probabilities or logits for classification, mean-pooling embeddings for retrieval) lets the whole of a long legal document contribute to the prediction and avoids loss of context due to truncation; because Mamba and SSD-Mamba handle longer contexts directly, they reduce window fragmentation and preserve global coherence, producing more faithful document embeddings and better retrieval. [CLM-0033-007]. — jurisdiction: general; basis: argument
- Ali et al. (2021) argue that Computing sentence similarity by averaging word embeddings, as in earlier full-text search over legal document collections, gives a lossy representation in which the relative order of words is lost, whereas representing sentences as Evidence Structure Instances preserves relative ordering through the structure itself. [CLM-0043-016]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:CA**

- Mokanov (2019) argue that Learning from the existing citations in the CanLII database makes it possible to predict which sources of law are relevant to the text of a legal brief, a legal opinion, or a plain-language description of a legal issue, whether or not the input text itself contains legal citations. [CLM-0001-002]. — jurisdiction: geographical_proxy:CA [jurisdiction inferred]; basis: dataset_or_experiment
- Mokanov (2019) argue that The production Facts2Law model takes as input a brief and a target document and outputs its confidence that the brief should cite the target: whole-document embeddings of both documents, together with a weighted summary of the embeddings of neighbouring nodes in the citation graph and relevant metadata, are fed through fully connected layers, merged, modulated by the age of the brief, and passed to a final fully connected layer that outputs the prediction. This architecture allows heuristics to select a subset of the corpus that could be relevant to a document and then rank that subset efficiently. [CLM-0001-005]. — jurisdiction: geographical_proxy:CA [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:CN**

- Hu et al. (2024) argue that A general-purpose retrieval embedding model such as BGE, pre-trained only on a general corpus, lacks legal-domain knowledge and cannot distinguish terminologies or cases that are semantically similar but have different meanings in the legal domain; it therefore needs to be fine-tuned on a legal corpus before being used to match response sentences to legal articles or to retrieve legal cases. [CLM-0029-007]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that LEGAL-BERT performs worse than other techniques, and shows more instability across random seeds, on datasets with more informal language such as the Legal Advice Reddit dataset, because the LEGAL-BERT-SC model was trained only on very formal legal text and did not see the colloquialisms and slang prevalent in informal text. [CLM-0006-005] is in tension with the claim that Further training Bert-Base-Cased with the masked language model objective on 900M tokens of case law yields a Legal BERT that is much better adapted to legal queries: on the natural-language questions and answers of the SARA dataset its perplexity is 2.7, against 14.4 for Bert-Base-Cased. [CLM-0003-011] (inferred, low). Note: One finds a case-law-adapted BERT much better adapted to legal queries; the other finds LEGAL-BERT worse and less stable on informal legal questions — reconcilable if adaptation helps only on formal legal text.
- The claim that Straightforward prompting of GPT-3 (text-davinci-003) on the SARA statutory-reasoning benchmark yields accuracy better than the previous best published, BERT-based results, with far less human input: the best setting (zero-shot with the statute included) reaches 71% aggregate accuracy on the 100 entailment test cases, significantly better than the BERT-based state of the art (p approximately 0.038) and the majority baseline. [CLM-0008-002] is in tension with the claim that Performance on the SARA statutory reasoning dataset will not be improved through straightforward application of a large-scale language model, unlike on other datasets such as COPA, SQuAD 2.0 and SWAG where large pre-trained models produced large gains. [CLM-0003-010] (inferred, high). Note: One predicts that straightforward application of a large-scale language model will not improve SARA performance; the other reports that straightforward GPT-3 prompting beats the previous BERT-based state of the art on SARA. The later source cites the earlier one only for the dataset, not on this prediction, so the edge is inferred.
- The claim that The near-random human performance at classifying case outcomes from fact descriptions raises questions about the feasibility of classifying legal outcomes solely from descriptions of facts, the approach that has been dominant in prior machine-learning work on legal judgement prediction. [CLM-0010-015] is in tension with the claim that Finetuned BERT with truncation to 500 tokens performs much better on the ECHR violation prediction task (macro F1 of 66.5) than reported by Chalkidis et al. (2019), who report an F1 of 17, worse than random guessing; the underperformance reported there could be caused by a mistake in their training process. [CLM-0006-008] (inferred, medium). Note: One questions the feasibility of classifying legal outcomes from fact descriptions alone after humans performed at chance; the other reports a fine-tuned BERT reaching macro F1 66.5 on ECHR violation prediction from case facts — above chance, though on a different task formulation.
- The claim that Fine-tuned transformer models outperform zero-shot and few-shot large language models on the UK Employment Tribunal four-class case outcome prediction task, with fine-tuned T5 as the best-performing model, and all tested models significantly outperform a random-guess baseline. [CLM-0013-005] is in tension with the claim that Straightforward prompting of GPT-3 (text-davinci-003) on the SARA statutory-reasoning benchmark yields accuracy better than the previous best published, BERT-based results, with far less human input: the best setting (zero-shot with the statute included) reaches 71% aggregate accuracy on the 100 entailment test cases, significantly better than the BERT-based state of the art (p approximately 0.038) and the majority baseline. [CLM-0008-002] (inferred, medium). Note: One finds fine-tuned transformers beating prompted GPT models on outcome prediction; the other finds prompted GPT-3 beating the fine-tuned BERT-based state of the art on statutory reasoning — opposite rankings on different tasks.
- The claim that Across multiple-choice exams on U.S. tax law (one based on the Code of Federal Regulations, one on the U.S. Code), answer accuracy increases with each subsequently released OpenAI model (davinci, text-davinci-002, gpt-3.5-turbo, GPT-4); the underlying model is the primary experimental factor producing consistent accuracy gains when averaged across retrieval and prompting factors, which evidences emerging legal understanding capabilities in LLMs. [CLM-0024-001] is in tension with the claim that Performance on the SARA statutory reasoning dataset will not be improved through straightforward application of a large-scale language model, unlike on other datasets such as COPA, SQuAD 2.0 and SWAG where large pre-trained models produced large gains. [CLM-0003-010] (inferred, medium). Note: One predicts that scaling language models will not straightforwardly improve statutory reasoning; the other reports accuracy on tax-law questions rising with each model release.
- The claim that A general-purpose retrieval embedding model such as BGE, pre-trained only on a general corpus, lacks legal-domain knowledge and cannot distinguish terminologies or cases that are semantically similar but have different meanings in the legal domain; it therefore needs to be fine-tuned on a legal corpus before being used to match response sentences to legal articles or to retrieve legal cases. [CLM-0029-007] is in tension with the claim that For retrieving semantically similar Czech Constitutional Court decisions, a general-purpose OpenAI embedder (text-embedding-3-large) consistently and statistically significantly outperforms a domain-specific BERT encoder pre-trained from scratch on about 34,000 of the court's decisions, across all cut-offs (k = 10, 20, 100) and both relevance thresholds (0.20, 0.28), in nDCG, P@k and HitRate@k. [CLM-0017-001] (inferred, medium). Note: One holds that a general-purpose embedding model lacks the legal knowledge needed to retrieve legal texts; the other finds a general-purpose embedder outperforming a domain-specific encoder on legal case retrieval.
- The claim that Fine-tuning the BGE embedding model on the LeCaRD training split significantly increases NDCG@10, @20 and @30 for Chinese legal case retrieval over both BM25 and untuned BGE, which shows that the fine-tuned model learns legal knowledge and better distinguishes legal cases that are semantically similar but not legally relevant; nonetheless CaseEncoder, SAILER and CaseFormer still outperform the fine-tuned BGE. [CLM-0029-009] is in tension with the claim that For retrieving semantically similar Czech Constitutional Court decisions, a general-purpose OpenAI embedder (text-embedding-3-large) consistently and statistically significantly outperforms a domain-specific BERT encoder pre-trained from scratch on about 34,000 of the court's decisions, across all cut-offs (k = 10, 20, 100) and both relevance thresholds (0.20, 0.28), in nDCG, P@k and HitRate@k. [CLM-0017-001] (inferred, medium). Note: One finds legal-domain fine-tuning of an embedding model significantly improves case retrieval; the other finds a general embedder beating a domain-trained encoder — reconcilable if fine-tuning a general model differs from training a small domain model from scratch.
- The claim that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015] is in tension with the claim that Traditional machine-learning explanations of predicted legal outcomes, such as listing or highlighting the most influential words in the text, are unhelpful and inappropriate in a legal context, because the right to explanation requires an explanation capable of persuading the losing party and withstanding appeal: not an account of how the decision was reached, but of why the decision represents the proper application of the law. [CLM-0004-004] (inferred, medium). Note: One holds that SVM coefficients and attention over facts let the basis of a classification be determined to some extent; the other holds that such word- or feature-level explanations are unhelpful and inappropriate in a legal context.
- The claim that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002] is in tension with the claim that In the LegalLens Shared Task 2024, the top-performing teams in both the LegalLens-NER and LegalLens-NLI sub-tasks consistently relied on fine-tuning pretrained language models, and these fine-tuned models outperformed legal-specific models and few-shot methods. [CLM-0012-001] (inferred, medium). Note: One finds legal-oriented pre-trained models overall better than generic ones on legal NLU tasks; the other finds fine-tuned generic models beating legal-specific ones on violation detection.
- The claim that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002] is in tension with the claim that Legal-specific LLMs do not always perform better than general LLMs on legal tasks; two speculated reasons are that legal-specific models are limited by base models weaker than models such as GPT-4, and that continuous pre-training on legal corpora may impair the abilities of the original base models, so appropriate training objectives for legal-specific LLMs still need to be designed. [CLM-0030-012] (inferred, medium). Note: One finds legal pre-training beneficial overall; the other finds legal-specific LLMs not always better than general LLMs.
- The claim that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002] is in tension with the claim that For retrieving semantically similar Czech Constitutional Court decisions, a general-purpose OpenAI embedder (text-embedding-3-large) consistently and statistically significantly outperforms a domain-specific BERT encoder pre-trained from scratch on about 34,000 of the court's decisions, across all cut-offs (k = 10, 20, 100) and both relevance thresholds (0.20, 0.28), in nDCG, P@k and HitRate@k. [CLM-0017-001] (inferred, medium). Note: One finds legal-oriented encoders better than generic ones; the other finds a general-purpose embedder beating a domain-trained encoder on legal retrieval.
- The claim that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002] is in tension with the claim that Adapting BERT or word vectors to the legal domain (Legal BERT further trained on case law; tax-specific word2vec vectors) has no noticeable effect on performance on the SARA statutory reasoning tasks. [CLM-0003-009] (inferred, medium). Note: One finds legal-oriented pre-training helps on legal NLU benchmarks; the other finds domain adaptation of BERT has no effect on statutory reasoning.
- The claim that Post-hoc explainable AI is not merely insufficient but actively dangerous in high-stakes jurisprudential contexts, because post-hoc explanations bear no guaranteed mathematical relationship to a model's actual computations and generate legally plausible narratives that mask bias; a hallucinated explanation of a black box is more dangerous than no explanation at all, so models that are interpretable by design should be used instead. [CLM-0049-013] is in tension with the claim that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015] (inferred, low). Note: One deems post-hoc explanation of black-box outputs actively dangerous in legal contexts; the other finds coefficients and attention adequate to determine a classifier's basis to some extent.

## Distribution

Sources with claims on this concept: 20; claims: 88.

**By contribution type**

| value | sources |
|---|---|
| technical | 19 |
| empirical_quantitative | 17 |
| theoretical | 4 |
| survey | 3 |
| normative | 2 |
| empirical_qualitative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 9 |
| IN | 4 |
| US | 2 |
| CA | 1 |
| CN | 1 |
| CZ | 1 |
| CoE | 1 |
| GB | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 10 |
| geographical_proxy:IN | 6 |
| geographical_proxy:US | 5 |
| geographical_proxy:CoE | 4 |
| geographical_proxy:GB | 3 |
| geographical_proxy:EU | 2 |
| CA | 1 |
| geographical_proxy:CA | 1 |
| geographical_proxy:CN | 1 |
| geographical_proxy:CZ | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2024 | 6 |
| 2021 | 5 |
| 2022 | 2 |
| 2023 | 2 |
| 2025 | 2 |
| 2019 | 1 |
| 2020 | 1 |
| 2026 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
