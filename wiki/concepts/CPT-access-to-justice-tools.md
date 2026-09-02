---
id: "CPT-access-to-justice-tools"
label: "Access-to-justice tools"
status: "anchor"
concept_type: "legal_task"
definition: "Tools that help laypeople or under-resourced parties navigate legal processes or documents."
aliases: []
broader: []
sources: ["SRC-0006", "SRC-0009", "SRC-0011", "SRC-0018", "SRC-0029", "SRC-0031", "SRC-0047"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Access-to-justice tools

_Status: anchor; family: legal_task._

## Definition

Tools that help laypeople or under-resourced parties navigate legal processes or documents.

Conceptual claims on this concept, each with its source:
- Li et al. (2022): Data from the Legal Advice Subreddit is especially helpful for training machine learning models to help laypersons in law, because questions are in the format and language regular people write in, whereas the non-personal, hypothetical nature of Law Stack Exchange data makes it less valuable for helping laypersons; both forum datasets are closer to laypersons' legal questions than formal documents such as ECHR cases. [CLM-0006-016]

## Claims about the concept

### Descriptive

**US**

- Steenhuis (2025) state that Correctly classifying the applicant's legal problem is central to legal intake and referral: applicants struggle to distinguish between abstract legal categories and their own idea of the kind of lawyer they need may be wrong, and a wrong triage or referral means the applicant may lose access to timely legal help and risk liberty, physical abuse or injury, loss of housing, or custody of a child. [CLM-0018-010]. — jurisdiction: US [jurisdiction inferred]; basis: literature
- Steenhuis (2025) state that The 244-node legal issue taxonomy maintained by the Oregon State Bar is national in its application and represents a superset of alternative issue taxonomies such as the 135-node SALI Legal Matter Specification Standard and the smaller civil legal aid-focused LIST taxonomy. [CLM-0018-017]. — jurisdiction: US [jurisdiction inferred]; basis: none_stated

**general**

- Li et al. (2022) state that Public legal forums such as Legal Advice Reddit and Law Stack Exchange are valuable data sources for legal machine learning: they provide labelled data (such as mapping legal questions to areas of law), hundreds of thousands of legal questions usable for domain adaptation, and starting points for tasks without direct labels; such forum data has been vastly underexplored for the legal domain. [CLM-0006-015]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Janatian et al. (2023) state that Structuring the pathway of criteria and conclusions is only one part of building a JusticeBot legal decision support tool; the work also requires simplifying the content, drafting layperson explanations of the individual criteria, and adding case-law summaries to the question blocks. [CLM-0009-014]. — jurisdiction: general; basis: literature
- Steenhuis (2025) state that Because an ensemble classifier can generate follow-up questions automatically when it lacks sufficient confidence, a legal referral tool built on it can gather more information from the applicant without a human having to call the applicant. [CLM-0018-014]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Westermann and Savelka (2024) state that AI and LLM methods that bridge laypeople's knowledge and legally relevant formulations often assume that the user can provide the relevant information to a computer system, which may introduce friction, since much of that information is contained in paper forms, certificates, contracts, letters or other documents that the user must locate, interpret and type in. [CLM-0031-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Westermann and Savelka (2024) state that One hurdle to overcoming the access-to-justice gap is the difficulty laypeople have in filling out forms and drafting legal documents: self-represented litigants struggle to decide which forms to use and how to fill them out, and often struggle to craft a legally sound narrative. [CLM-0031-013]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Normative

**general**

- Li et al. (2022) argue that Calibration is important for legal models: a properly calibrated model reduces misuse because software systems can better handle cases where the model is uncertain, it improves interpretability of model confidence, and it is especially important in the legal domain given the high-stakes nature of legal decision making; when providing predictions to laypersons, output logits must accurately reflect the model's confidence. [CLM-0006-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Steenhuis (2025) argue that Bias is an important risk to consider when using LLMs for legal intake classification, because biased classification may lead to unfair allocations of scarce low-cost and free legal help resources; these concerns are stronger when the LLM has a higher error rate and particularly when the errors show a pattern that is uneven across the distribution of applicants and problem types. [CLM-0018-012]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Westermann and Savelka (2024) argue that If a multi-modal LLM form-extraction tool is provided to the public, one has to remain aware of its implications for the digital divide, because a modern phone and good lighting conditions are important for good results, which may exclude certain groups from using such tools. [CLM-0031-009]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

### Empirical

**general**

- Li et al. (2022) report that Prefix domain adaptation — pre-training a deep prefix prompt with the masked language modelling task on a large unsupervised domain-specific corpus and then using that prompt to initialise prefix tuning for downstream tasks — matches or exceeds the few-shot performance of LEGAL-BERT and related techniques on legal classification tasks while tuning only approximately 0.1% of model parameters. [CLM-0006-001]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that LEGAL-BERT performs worse than other techniques, and shows more instability across random seeds, on datasets with more informal language such as the Legal Advice Reddit dataset, because the LEGAL-BERT-SC model was trained only on very formal legal text and did not see the colloquialisms and slang prevalent in informal text. [CLM-0006-005]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that On Legal Advice Reddit data, prefix domain adaptation is comparable to full finetuning and consistently outperforms regular prefix tuning as the number of training samples increases, and finetuning is less stable across runs than prefix domain adaptation. [CLM-0006-009]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that Prefix domain adaptation scales to larger models: with RoBERTa-large it remains comparable to or outperforms full finetuning, and at few-shot sizes 32 to 128 prefix domain adaptation with RoBERTa-base is even comparable to full finetuning with RoBERTa-large. [CLM-0006-010]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Hu et al. (2024) report that Legal terminology embedded in LLM-generated legal advice without sufficient explanation may pose understanding difficulties for users without domain knowledge; special cases lacking a clear definition in legal articles are likewise hard for non-professional users to understand. [CLM-0029-004]. — jurisdiction: general [jurisdiction inferred]; basis: literature

**geographical_proxy:CA-ON**

- Westermann and Savelka (2024) report that GPT-4o, given photographs or screenshots of a filled-in residential lease form, correctly extracted 73% of the target fields on average across all scenarios and image formats; the results are promising but reveal limitations, for example when image quality is low. [CLM-0031-001]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment
- Westermann and Savelka (2024) report that Extraction accuracy of GPT-4o decreased as the scenario became harder: 89% of fields were correct in the scenario with common names and all fields filled, 71% in the scenario with less common names, two tenants and one missing value, and 59% in the scenario with uncommon names resembling common ones and several missing fields. [CLM-0031-002]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment
- Westermann and Savelka (2024) report that Image format and quality strongly affect the accuracy of multi-modal LLM extraction from forms: typed PDF screenshots were processed almost perfectly, while handwritten printed forms, and especially sloppily filled forms photographed in poor conditions, produced notably lower accuracy. [CLM-0031-003]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment

**geographical_proxy:US**

- Steenhuis (2025) report that A weighted ensemble of three inexpensive LLMs (GPT-5-nano, Gemini 2.5-flash, Mistral small) combined with keyword matching and the traditional-ML Spot classifier meets or slightly exceeds the classification accuracy of the frontier model GPT-5 alone on legal problem classification of real-world referral queries (97.37% versus 96.66% hits@2), while greatly exceeding the accuracy of each inexpensive model used alone; the 0.71-point margin over GPT-5 is likely statistically insignificant. [CLM-0018-001]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Steenhuis (2025) report that The weighted ensemble of inexpensive small LLMs outperforms the state-of-the-art GPT-5 model on a cost basis by a factor of more than three for legal intake classification, and the small LLMs also have much lower latency than GPT-5. [CLM-0018-002]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Steenhuis (2025) report that Small-model LLM ensembles substantially improve on the performance of older machine-learning and keyword-matching approaches to classifying legal problems: keyword matching set a baseline of about 54% hits@2, the Spot classifier scored about 59%, and TF-IDF fared worst at about 31%, against 97.37% for the ensemble. [CLM-0018-003]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Steenhuis (2025) report that The errors of the small-model ensemble classifier on legal intake queries showed no observable pattern: they did not appear biased towards one type of legal problem over another, similar categories were not consistently confused, and the safety concerns revealed by the errors appear minimal. [CLM-0018-004]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Steenhuis (2025) report that Examination of the ensemble classifier's errors on legal intake queries revealed probable human annotation errors in the human-labelled dataset (four of the eleven errors) and two duplicate entries, and these annotation errors and ambiguities suggest that human baseline performance may match the ensemble; the errors genuinely attributable to the LLM appear remarkably few (approximately 2%) and consistent with the kind of challenges humans face in similar circumstances. [CLM-0018-006]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Steenhuis (2025) report that Automatically generated follow-up questions, produced by the LLM ensemble when its classification confidence is low, can help clarify an applicant's intent and draw legal distinctions the applicant may not be aware of; initial qualitative results on ambiguous queries suggest that such follow-up questions would further improve the classification system's performance in real-world usage. [CLM-0018-007]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Steenhuis (2025) report that Unlike in earlier work on LLM-based legal intake, no instances of model 'censorship' or refusal to classify situations involving violence or abuse were observed, which is a promising indication of the suitability of LLMs for problems in the legal domain. [CLM-0018-011]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Conceptual

**general**

- Li et al. (2022) argue that Data from the Legal Advice Subreddit is especially helpful for training machine learning models to help laypersons in law, because questions are in the format and language regular people write in, whereas the non-personal, hypothetical nature of Law Stack Exchange data makes it less valuable for helping laypersons; both forum datasets are closer to laypersons' legal questions than formal documents such as ECHR cases. [CLM-0006-016]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Predictive

**GB**

- Ribary et al. (2023) argue that An LLM-based system that triages potential insolvency cases for stakeholders of micro, small and medium enterprises at a competency comparable to a Level 6 or 7 law student could, if successful enough, help solo practitioners and smaller law firms, which often lack sufficient expertise in this area of law, to expand the scope of their services. [CLM-0011-004]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that AI is going to revolutionise access to justice for litigants in person: publicly available LLM platforms, free or cheaply subscribed, can generate passable Particulars of Claim from a lay complainant's description of a grievance and give basic legal advice without any lawyer, which is likely to lead to a tsunami of small to moderate value civil claims. [CLM-0047-006]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

**general**

- Li et al. (2022) argue that LEGAL-BERT is not expected to be an effective initialisation for tasks involving legal questions asked by laypersons, which typically do not use formal legal language. [CLM-0006-006]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) argue that Seeking legal advice from lawyers is expensive, and a machine learning system that can help answer legal questions could greatly aid laypersons in making informed legal decisions and make legal services more accessible to the public. [CLM-0006-018]. — jurisdiction: general [jurisdiction inferred]; basis: none_stated
- Steenhuis (2025) argue that Presenting an LLM-backed referral classifier to applicants through a consistent form metaphor, rather than as a chatbot, is hypothesised both to reduce effort for applicants and to reduce the 'uncanny valley' effect that users experience when talking to an LLM. [CLM-0018-013]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Steenhuis (2025) argue that A routing method in which a frontier model such as GPT-5 is asked to classify only the 'hardest' legal intake cases is a promising technique for further narrowing the small remaining error rate of a small-model ensemble classifier. [CLM-0018-016]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Westermann and Savelka (2024) argue that Multi-modal LLMs have considerable potential to support laypeople and self-represented litigants in access to justice by extracting and analysing data contained in images of printed forms, legal documents or letters, especially in collaboration with a human who verifies and corrects the captured data, for applications such as filling out new forms or providing relevant legal information. [CLM-0031-010]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Westermann and Savelka (2024) argue that Because multi-modal models are much more recent than purely text-based LLMs, further improvements in their performance at extracting data from images of forms may be expected in the coming months. [CLM-0031-011]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:CA-ON**

- Westermann and Savelka (2024) argue that The almost perfect extraction results on typed PDF versions of forms show that multi-modal LLMs could already be useful for analysing electronic legal documents. [CLM-0031-004]. — jurisdiction: geographical_proxy:CA-ON; basis: dataset_or_experiment

**geographical_proxy:CA-QC**

- Janatian et al. (2023) argue that An LLM pathway generator used in conjunction with a human expert (augmented intelligence) has the potential to support annotators with a strong draft, making annotation more efficient and even yielding more logically correct pathways; LLMs can thus potentially support humans in creating predictable and safe legal expert systems more efficiently, with possible beneficial impacts on access to justice. [CLM-0009-012]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment

**geographical_proxy:US**

- Steenhuis (2025) argue that Because the ensemble classifier's errors on legal intake queries show no pattern of confused categories, enriching the category descriptions or adding further clarifying instructions in the prompt is not likely to significantly improve classification performance. [CLM-0018-005]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Steenhuis (2025) argue that Expressing a legal issue taxonomy to the LLM simply as a list of category names, without any additional explanation, achieves high classification accuracy, which offers promise that applying the ensemble technique to future classification tasks may not require extensive prompt engineering and that it would expand beyond the context of Virginia and Oregon. [CLM-0018-008]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Methodological

**general**

- Janatian et al. (2023) argue that A legislative article or paragraph can be converted into a JusticeBot pathway by prompting GPT-4 with the legislation as the user message and a system message instructing it to extract requirements and legal conclusions and link them; the model's JSON output of logic blocks and connections is converted to JusticeCreator format, where legal experts verify and adjust the pathway as a starting point for a decision support tool. [CLM-0009-003]. — jurisdiction: general; basis: argument
- Steenhuis (2025) argue that For a legal referral classifier whose interface presents applicants with the top two categories, hits@2 reflects the practical success criterion more directly than top-1 accuracy, because the goal is not to force a single label but to offer two plausible options from which the applicant can choose the most appropriate referral. [CLM-0018-009]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hu et al. (2024) argue that Visually presenting, for each sentence of an LLM's legal advice, the legal article that serves as its basis (found by similarity matching with a legal-domain fine-tuned embedding model) lets users verify the reliability of the response and trust the advice; a sentence for which no legal basis is found can be viewed as a warning that the sentence may be incorrect. [CLM-0029-005]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:US**

- Steenhuis (2025) argue that Although 419 queries is a relatively large dataset for the legal intake domain, it may not adequately cover the 244 nodes of the full legal issue taxonomy, so the classification findings are strongest when considering only the 15 top-level categories. [CLM-0018-015]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that LEGAL-BERT performs worse than other techniques, and shows more instability across random seeds, on datasets with more informal language such as the Legal Advice Reddit dataset, because the LEGAL-BERT-SC model was trained only on very formal legal text and did not see the colloquialisms and slang prevalent in informal text. [CLM-0006-005] is in tension with the claim that Further training Bert-Base-Cased with the masked language model objective on 900M tokens of case law yields a Legal BERT that is much better adapted to legal queries: on the natural-language questions and answers of the SARA dataset its perplexity is 2.7, against 14.4 for Bert-Base-Cased. [CLM-0003-011] (inferred, low). Note: One finds a case-law-adapted BERT much better adapted to legal queries; the other finds LEGAL-BERT worse and less stable on informal legal questions — reconcilable if adaptation helps only on formal legal text.

## Distribution

Sources with claims on this concept: 7; claims: 42.

**By contribution type**

| value | sources |
|---|---|
| empirical_quantitative | 6 |
| technical | 6 |
| doctrinal | 2 |
| empirical_qualitative | 2 |
| normative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| GB | 2 |
| general | 2 |
| CA-QC | 1 |
| CN | 1 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 5 |
| GB | 2 |
| US | 1 |
| geographical_proxy:CA-ON | 1 |
| geographical_proxy:CA-QC | 1 |
| geographical_proxy:US | 1 |

**By year**

| value | sources |
|---|---|
| 2023 | 2 |
| 2024 | 2 |
| 2022 | 1 |
| 2025 | 1 |
| 2026 | 1 |

## What the sources do not address

- No interpretive claim on CPT-access-to-justice-tools. [ABS-1358] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
