---
id: "CPT-summarisation"
label: "Summarisation"
status: "anchor"
concept_type: "legal_task"
definition: "Producing condensed versions of legal documents such as judgments or contracts."
aliases: []
broader: []
sources: ["SRC-0005", "SRC-0007", "SRC-0015", "SRC-0019", "SRC-0023", "SRC-0028", "SRC-0044"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Summarisation

_Status: anchor; family: legal_task._

## Definition

Producing condensed versions of legal documents such as judgments or contracts.

Conceptual claims on this concept, each with its source:
- Mandal et al. (2021): Document-specific catchphrases, short one-word or multiword phrases that collectively give a concise representation of a legal document, combine domain-specific legal importance with document-specific importance; they therefore differ from the domain-specific legal dictionaries widely used in legal summarization algorithms, because catchphrases also capture document-specific important terms that may not be legal keywords. [CLM-0005-001]
- Tan et al. (2024): Determining whether two sentences make the same point is a more difficult task for legal text than for other text such as news, because legal texts involve complex reasoning and long legal documents sometimes require contextual understanding of the whole case to decide whether two sentences make the same point. [CLM-0015-004]
- Tan et al. (2024): The pointwise evaluation methodology focuses on the content of a summary and does not account for more subjective aspects of a text such as writing style and flow, which are nevertheless an important part of a well-written legal summary. [CLM-0015-017]

## Claims about the concept

### Descriptive

**general**

- Mandal et al. (2021) state that Popular legal case summarization algorithms generally estimate sentence importance using domain-specific legal dictionaries, and none of them use document-specific catchphrases. [CLM-0005-007]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Mandal et al. (2021) state that Most summarization algorithms developed for the legal domain are extractive and unsupervised, mainly because large training data is lacking in the legal domain. [CLM-0005-008]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Tan et al. (2024) state that Existing research on automated evaluation metrics for generated text, and the meta-datasets used to evaluate generated summaries, have focused mainly on short summaries of a few sentences, while very little work has been done on long-form summaries. [CLM-0015-001]. — jurisdiction: general; basis: literature
- Tan et al. (2024) state that Long-form abstractive summarization is a task of particular importance in the legal domain, and there is a pressing need for effective automated evaluation metrics for the long-form legal summaries that large language models can now generate. [CLM-0015-002]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Tan et al. (2024) state that Beyond performance, an advantage of the pointwise evaluation method over existing metrics is its interpretability and explainability: it shows exactly which reference points are included in or missing from a candidate summary, and which candidate points are absent from the reference, which allows targeted improvement of the summarizing LLM's prompts. [CLM-0015-007]. — jurisdiction: general; basis: argument
- Tan et al. (2024) state that A small released meta-dataset for benchmarking evaluation methods for long-form legal summarization, consisting of seven UK Supreme Court cases each with the court's press summary as the human-written reference and five LLM-generated candidate summaries annotated with a variation of the LitePyramid method, is, as far as is known, the first such dataset to be made available. [CLM-0015-008]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Tan et al. (2024) state that Creating a meta-evaluation dataset for long-form legal summaries is very resource-intensive, which restricts such datasets to a small size; extending a dataset to more cases and across more jurisdictions would allow more representative and statistically significant tests. [CLM-0015-018]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Deroy et al. (2024) state that LLMs have not been much tried for legal document summarization, and no prior work has systematically compared the three families of summarization models (extractive models, legal-domain abstractive models, and general-domain LLMs) for legal case judgement summarization. [CLM-0028-016]. — jurisdiction: general; basis: literature
- Deroy et al. (2023) state that As of 2023, there has been little attempt to analyse how abstractive summarization methods and LLMs such as ChatGPT perform in summarizing legal case judgements, and, as far as is known, hallucination and the consistency of abstractive summaries have not previously been studied in the context of legal summarization. [CLM-0044-008]. — jurisdiction: general; basis: literature

**geographical_proxy:GB, geographical_proxy:IN**

- Deroy et al. (2024) state that The extreme length of legal case judgements is a domain-specific challenge for summarization: judgements are often much longer than what summarization models or LLMs can take as input at once, so a divide-and-conquer chunking strategy has to be followed. [CLM-0028-017]. — jurisdiction: geographical_proxy:GB, geographical_proxy:IN (cumulative); basis: dataset_or_experiment

### Interpretive

**geographical_proxy:IN, geographical_proxy:GB**

- Deroy et al. (2024) read Summarisation as follows: Legal-LED's hallucination of US court and statute names in summaries of Indian and UK judgements is probably due to the model having been trained on US legal document-summary pairs, which gives it a tendency to generate US court and statute names seen during training. [CLM-0028-005]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment

### Normative

**general**

- Khadloya et al. (2025) argue that Judicial tools for long records should target direct, auditable navigation to the exact anchored locus in the record rather than free-form summarization, because adjudication prioritizes verifiability and summaries can hide citations and miss pivotal passages. [CLM-0019-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:IN**

- Deroy et al. (2023) argue that Pre-trained abstractive summarization models and general-domain large language models are not yet ready for fully automatic deployment for legal case judgement summarization; a human-in-the-loop approach, in which a legal expert monitors the generated summaries and manually checks for inconsistencies, is more suitable at present. [CLM-0044-001]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) argue that Better methods need to be designed to detect complex types of errors in abstractive summaries of legal case judgements, because some errors committed by abstractive models, such as confusing the names of appellants with the names of the lawyers representing them or a judge's name with a lawyer's name, are subtle, very difficult to detect by automatic methods, and can make the summaries misleading. [CLM-0044-007]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

**geographical_proxy:IN, geographical_proxy:GB, geographical_proxy:US**

- Deroy et al. (2024) argue that For complex domains like law, LLMs and pre-trained abstractive summarization models are not yet ready for fully automatic deployment; a human-in-the-loop approach in which a legal expert monitors the generated summaries may be more appropriate, and better methods are needed to detect complex errors in abstractive summaries. [CLM-0028-015]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB, geographical_proxy:US (cumulative); basis: dataset_or_experiment

### Empirical

**general**

- Tan et al. (2024) report that Entailment (NLI) models fine-tuned on short summaries, such as the A2CU NLI model trained on the RoSE dataset, perform less well on long-form summaries and do not perform well when presented with more than a few sentences, even though they can theoretically take in longer text. [CLM-0015-005]. — jurisdiction: general; basis: none_stated
- Hartung et al. (2026) report that Legal text generation and summarization played a rather limited role in Legal NLP over the first decade of the 2013-2024 period but picked up speed in the last few years: text generation has grown remarkably since 2022, whereas summarization has grown too, but not to the same extent. [CLM-0023-009]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024

**geographical_proxy:GB**

- Tan et al. (2024) report that For automated point extraction from long-form legal summaries, a Dense X proposition-extraction model fine-tuned on legal data and an LLM prompted with examples both improve on the Dense X baseline by 3-6 percentage points on recall- and precision-oriented easiness scores, and outperform sentence splitting and the A2CU content-unit generator. [CLM-0015-009]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that The A2CU content-unit generator, trained on non-legal data, produces points from legal text that are too granular, fail to capture the complex meaning of the original text and are sometimes not proper declarative propositions, whereas an LLM prompted with examples produces points that are correct and properly capture the original meaning. [CLM-0015-010]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that For deciding whether two points from legal summaries make the same point, an LLM given the full reference summary, the surrounding points, an explanation of what making the same point means in a court case, and examples performs much better (in F1) than cosine similarity and NLI-based methods, indicating that the LLM can better distinguish the nuances of complex legal statements than simpler models; few-shot and many-shot example regimes perform similarly. [CLM-0015-011]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that Comparing two sentences to determine whether they make the same point in a legal context appears to be quite tricky for automated methods, even for state-of-the-art LLMs given full context, as shown by absolute pairwise matching precision scores that are not high. [CLM-0015-012]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that Fully automated LLM-based pointwise evaluation metrics correlate better with human recall scores for long-form legal summaries than ROUGE, BERTScore, A2CU and A3CU at summary, system and population level; the population-level improvement over the best baseline is strongly statistically significant (p < 0.001), and the root mean squared error against human scores is less than half that of the best baseline. [CLM-0015-014]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that A non-LLM pointwise variant (fine-tuned Dense X for point extraction and fine-tuned A2CU-NLI for point matching) performs better than the baseline metrics in some correlation categories but not as well as the LLM-based pointwise variants, which shows that the use of advanced LLM models yields a significant advantage in evaluating complex legal text. [CLM-0015-015]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Tan et al. (2024) report that The particularly pronounced population-level correlation improvement and the small root mean squared error indicate that the LLM-based pointwise method produces consistent results across court cases and absolute recall scores close to the human scores, so that it gives an accurate idea of the absolute quality of a single LLM-generated summary rather than merely ranking the candidate summaries of each case. [CLM-0015-016]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

**geographical_proxy:GB, geographical_proxy:IN**

- Deroy et al. (2024) report that Abstractive summarization models and general-domain LLMs generally perform better than extractive summarization methods for legal case judgement summarization, both on traditional summary-quality metrics (ROUGE, METEOR, BERTScore) and in human evaluation; on the Indian Supreme Court dataset the abstractive models (including LLMs) perform at par with the best extractive models rather than clearly above them. [CLM-0028-001]. — jurisdiction: geographical_proxy:GB, geographical_proxy:IN (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that General-domain LLMs (Text-Davinci-003, Turbo-GPT-3.5, Llama2-70b and GPT-4 Turbo) perform well on legal case judgement summarization even without any legal-domain training, when used in zero-shot mode without in-context learning or fine-tuning. [CLM-0028-002]. — jurisdiction: geographical_proxy:GB, geographical_proxy:IN (cumulative); basis: dataset_or_experiment

**geographical_proxy:GB, geographical_proxy:IN, geographical_proxy:US**

- Deroy et al. (2024) report that Breaking a long legal document into chunks that are summarized independently involves a trade-off: chunking yields summaries with better information quality, but leads to redundancy and lack of coherence at chunk boundaries, whereas models that can take most case judgements as a whole (chatgpt-16k-long, GPT-4 Turbo) generate summaries with less redundancy and higher coherence. [CLM-0028-011]. — jurisdiction: geographical_proxy:GB, geographical_proxy:IN, geographical_proxy:US (cumulative); basis: dataset_or_experiment

**geographical_proxy:IN**

- Mandal et al. (2021) report that Using document-specific catchphrases can improve the performance of existing unsupervised extractive legal case summarization algorithms: when catchphrases extracted by PSLegal or D2V-BiGRU-CRF are incorporated, both DELSumm and CaseSummarizer show improvement across all performance metrics on a set of Indian Supreme Court case documents. [CLM-0005-003]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Mandal et al. (2021) report that In every tested variation, DELSumm with document-specific catchphrases produces better summaries than the original DELSumm on Indian Supreme Court case documents; the best performance is obtained when DELSumm uses catchphrases identified by PSLegal, where the Rouge-2 F-score rises from 0.4217 to 0.4435, and this improvement comes on top of DELSumm already outperforming several other summarization methods on the same dataset. [CLM-0005-004]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Mandal et al. (2021) report that In every tested variation, CaseSummarizer with document-specific catchphrases (from D2V-BiGRU-CRF and/or PSLegal, with or without the legal dictionary) produces better summaries than the original CaseSummarizer on Indian Supreme Court case documents. [CLM-0005-005]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2024) report that For ChatGPT, Text-Davinci-003 and Llama2-70b summarizing legal judgements chunk by chunk, a chunk size of 1024 words gives the best results on most metrics, possibly because the LLMs find it difficult to capture the context when chunks become too large. [CLM-0028-010]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that On Indian Supreme Court judgements, legal domain-specific abstractive summarization models achieve slightly higher ROUGE, METEOR and BLEU scores than extractive summarization models (and than general-domain LLMs), but the improvement over the best extractive model is statistically significant only for the ROUGE-L metrics. [CLM-0044-002]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that Summaries of legal case judgements generated by pre-trained abstractive summarization models and LLMs often contain inconsistent or hallucinated information, including wrong dates, wrong person names and confusion between different persons associated with a case, as well as incomplete sentences or words and sentences merged meaninglessly, the latter mostly occurring at the boundaries of input chunks. [CLM-0044-003]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that Further fine-tuning legal domain-specific abstractive summarization models (Legal-Pegasus and Legal-LED, originally fine-tuned on US legal documents) on Indian judgement-summary pairs improves their performance in terms of both match with gold-standard summaries and consistency with the source document, and can help to reduce hallucinations. [CLM-0044-004]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that Legal-LED, an abstractive summarization model fine-tuned on US legal document-summary pairs, generates names of US courts and US statutes in its summaries of Indian case judgements that are unrelated to the input document, probably because the model tends to reproduce court and statute names seen during training; this type of error was not observed in the summaries generated by the LLMs ChatGPT and DaVinci. [CLM-0044-005]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) report that General-domain LLMs (Turbo-GPT-3.5/ChatGPT and Text-Davinci-003) applied zero-shot to Indian case judgements achieve lower metric values than the best-performing abstractive and extractive models, yet their performance is creditable, since without any training on legal data they outperform some legally-trained extractive and abstractive models on certain metrics; however, these LLMs also sometimes generate inconsistent text in their summaries. [CLM-0044-006]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

**geographical_proxy:IN, geographical_proxy:GB**

- Deroy et al. (2024) report that Summaries of legal case judgements generated by LLMs and legal-domain abstractive summarizers frequently contain hallucinations and inconsistencies: wrongly reported names and monetary values, hallucinated court and statute names, incomplete statute names, incomplete sentences, and merged words or sentences; such errors were found in almost all manually checked summaries. [CLM-0028-003]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that When the legal-domain abstractive model Legal-LED summarizes Indian or UK case judgements, names of US courts and US statutes that are entirely unrelated to the input document appear in its summaries. [CLM-0028-004]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that Further fine-tuning legal-domain abstractive summarizers (Legal-Pegasus, Legal-LED) on data from the target domain improves both the match of their summaries with reference summaries and the consistency of the summaries, and removes the gross hallucinations of US court and statute names; where target-domain data are available, using them for fine-tuning seems an effective approach. [CLM-0028-006]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that Adding an explicit instruction to the prompt to avoid hallucinations and inconsistencies and to output complete sentences raises the consistency metrics of LLM-generated legal summaries but lowers their ROUGE, METEOR and BERTScore, because the resulting summaries carry less key information such as named entities; reducing hallucinations by prompting may therefore come with a reduction in summary quality. [CLM-0028-007]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that A semantic-similarity post-processing approach, which replaces every named entity or number that appears in an LLM-generated summary but not in the source judgement with the most semantically similar entity or number in the judgement (by cosine similarity of pre-trained language-model embeddings), reduces hallucinations and inconsistencies and also improves the summaries' ROUGE, METEOR and BERTScore. [CLM-0028-008]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that Not all hallucinations and inconsistencies in abstractive legal summaries can be corrected by the semantic-similarity replacement approach; complex errors such as confusion between names or numbers are difficult to detect or prevent completely, so the correction of hallucinations in abstractive summaries remains an open research problem. [CLM-0028-009]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment
- Deroy et al. (2024) report that Summaries of legal judgements produced by GPT-4 Turbo are generally shorter than those produced by Turbo-GPT-3.5 (ChatGPT); as a result ChatGPT summaries obtain higher ROUGE recall and F1 scores while GPT-4 summaries obtain higher ROUGE precision scores. [CLM-0028-012]. — jurisdiction: geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment

**geographical_proxy:US**

- Deroy et al. (2024) report that On US government reports (GOVREPORT), both general-domain LLMs and legal-domain abstractive models perform much better than the extractive CaseSummarizer, which is expected because CaseSummarizer is designed specifically for summarizing legal case judgements rather than other types of legal documents. [CLM-0028-014]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

**geographical_proxy:US, geographical_proxy:IN, geographical_proxy:GB**

- Deroy et al. (2024) report that Summarizing legal case judgements seems to be a more complicated task than summarizing US government reports, since the same summarization models obtain higher metric values, especially ROUGE scores, on the GOVREPORT dataset than on the Indian and UK Supreme Court datasets. [CLM-0028-013]. — jurisdiction: geographical_proxy:US, geographical_proxy:IN, geographical_proxy:GB (cumulative); basis: dataset_or_experiment

### Conceptual

**general**

- Mandal et al. (2021) argue that Document-specific catchphrases, short one-word or multiword phrases that collectively give a concise representation of a legal document, combine domain-specific legal importance with document-specific importance; they therefore differ from the domain-specific legal dictionaries widely used in legal summarization algorithms, because catchphrases also capture document-specific important terms that may not be legal keywords. [CLM-0005-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Tan et al. (2024) argue that Determining whether two sentences make the same point is a more difficult task for legal text than for other text such as news, because legal texts involve complex reasoning and long legal documents sometimes require contextual understanding of the whole case to decide whether two sentences make the same point. [CLM-0015-004]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Tan et al. (2024) argue that The pointwise evaluation methodology focuses on the content of a summary and does not account for more subjective aspects of a text such as writing style and flow, which are nevertheless an important part of a well-written legal summary. [CLM-0015-017]. — jurisdiction: general; basis: argument

### Predictive

**general**

- Mandal et al. (2021) argue that An appropriate amalgamation of document-specific and domain-specific sentence importance may provide new useful information to legal summarization algorithms, which can subsequently improve their performance; document-specific catchphrases can supply this combined information. [CLM-0005-002]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Methodological

**general**

- Mandal et al. (2021) argue that Document-specific catchphrases can be incorporated into existing legal case summarizers by substituting them for the summarizer's static domain-specific component: in DELSumm, the fixed set of legal-dictionary content words is replaced by catchphrases extracted from the input document to be summarized, so that sentences containing document-specific catchphrases are given more importance; in CaseSummarizer, the entity count in the sentence-scoring expression is replaced by the number of document-specific catchphrases in the sentence. [CLM-0005-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Malik et al. (2022) argue that Legal documents are long, unstructured, noisy and written in a specialised lexicon, which makes conventional text-processing techniques and pre-trained neural models ineffective on them; a legal document processing system would benefit substantially if documents were segmented into coherent information units (rhetorical roles), which could aid summarisation, legal judgment prediction, information extraction and prior case retrieval. [CLM-0007-001]. — jurisdiction: general; basis: argument
- Tan et al. (2024) argue that Single-clause semantic units of the kind used by the Pyramid method and A2CU, which work well for fact-focused news summaries, are not a good representation of legal text such as court judgments, because legal sentences involve logical reasoning and it matters which party or court says something; longer points should therefore be used as the base unit for evaluating legal summaries. [CLM-0015-003]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Tan et al. (2024) argue that An interpretable two-step pointwise evaluation methodology, which breaks the reference and candidate summaries into individual points, determines for each point whether the other summary contains a point saying the same thing, and computes recall and precision scores, is suited to the complexities of long-form legal text, and both of its steps can be automated. [CLM-0015-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Tan et al. (2024) argue that The pointwise evaluation methodology is appropriate for use cases where there is an objective standard for the content that a text should or should not include, and less appropriate for use cases where a topic admits many possible interpretations, such as arguing for or against a particular issue. [CLM-0015-019]. — jurisdiction: general; basis: argument
- Deroy et al. (2024) argue that The quality of the chunks into which long legal documents are segmented significantly influences the findings of chunk-based summarization studies: a basic token-level segmentation can end a chunk's last sentence abruptly and mix different topics within a chunk, so better segmentation strategies for long legal documents should be explored. [CLM-0028-018]. — jurisdiction: general; basis: argument

**geographical_proxy:GB**

- Tan et al. (2024) argue that Because many false-positive matches involve the same candidate point being matched to multiple reference points, an assignment algorithm that allows each candidate point to match only one reference point mitigates the effect of such errors on the downstream summary recall score. [CLM-0015-013]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

**geographical_proxy:IN**

- Deroy et al. (2023) argue that Because LLMs such as Text-Davinci-003 and Turbo-GPT-3.5 limit the input (prompt plus generated text) to 4,096 tokens while legal case judgements average more than 4,300 words, long judgements must be summarized with a divide-and-conquer strategy that chunks the document, summarizes each chunk and appends the chunk summaries in order; summarization performance may depend on the chunk size, and allocating every chunk the same target summary length is an inherent limitation, since not all parts of a judgement are equally important but there is no simple way of knowing the relative importance of different chunks. [CLM-0044-009]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Deroy et al. (2023) argue that The consistency metrics NumPrec and NEPrec, which measure the fraction of numbers and named entities in a generated summary that also appear in the source document, depend on the ability to detect numbers and named entities accurately; because identifying all types of named entities in Indian legal documents is quite challenging, the metric values are conditioned on the accuracy of the Spacy toolkit used for entity recognition. [CLM-0044-010]. — jurisdiction: geographical_proxy:IN; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Most summarization algorithms developed for the legal domain are extractive and unsupervised, mainly because large training data is lacking in the legal domain. [CLM-0005-008] is in tension with the claim that The CanLII database, with more than two million Canadian court and tribunal decisions from fourteen jurisdictions in parsable format with structured metadata, statutes and regulations with section-level tables of contents, and millions of hyperlinked citations extracted and standardised by the Reflex citator, already constitutes a highly structured 'map' of Canadian law that is available as a significant dataset for training machine-learning algorithms. [CLM-0001-004] (inferred, low). Note: One says large training data is lacking in the legal domain; the other presents a two-million-decision database as a significant training dataset — compatible if 'training data' means task-labelled data such as summaries rather than raw corpora.
- The claim that The Human-in-the-Loop paradigm, as mandated by Article 14 of the EU AI Act and widely adopted as the default safeguard in corporate AI governance, is a structural placebo: mandating human oversight in the absence of architectural guardrails does not prevent catastrophic errors but merely redistributes liability onto operators who are cognitively and technically unequipped to intercept them. [CLM-0049-007] is in tension with the claim that For complex domains like law, LLMs and pre-trained abstractive summarization models are not yet ready for fully automatic deployment; a human-in-the-loop approach in which a legal expert monitors the generated summaries may be more appropriate, and better methods are needed to detect complex errors in abstractive summaries. [CLM-0028-015] (inferred, medium). Note: One prescribes a human in the loop as the remedy for unreliable legal AI; the other holds that this paradigm fails under automation bias.

## Distribution

Sources with claims on this concept: 7; claims: 58.

**By contribution type**

| value | sources |
|---|---|
| empirical_quantitative | 7 |
| technical | 7 |
| survey | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| IN | 4 |
| general | 3 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 7 |
| geographical_proxy:IN | 3 |
| geographical_proxy:GB | 2 |
| geographical_proxy:US | 1 |

**By year**

| value | sources |
|---|---|
| 2024 | 2 |
| 2021 | 1 |
| 2022 | 1 |
| 2023 | 1 |
| 2025 | 1 |
| 2026 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
