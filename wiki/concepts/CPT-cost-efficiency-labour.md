---
id: "CPT-cost-efficiency-labour"
label: "Cost, efficiency and labour"
status: "anchor"
concept_type: "normative_concern"
definition: "Cost savings, efficiency gains, and effects on legal labour and the legal profession."
aliases: []
broader: []
sources: ["SRC-0003", "SRC-0006", "SRC-0007", "SRC-0009", "SRC-0010", "SRC-0014", "SRC-0015", "SRC-0017", "SRC-0018", "SRC-0019", "SRC-0024", "SRC-0026", "SRC-0027", "SRC-0032", "SRC-0033", "SRC-0034", "SRC-0039", "SRC-0046", "SRC-0047", "SRC-0049"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Cost, efficiency and labour

_Status: anchor; family: normative_concern._

## Definition

Cost savings, efficiency gains, and effects on legal labour and the legal profession.

Conceptual claims on this concept, each with its source:
- T.Y.S.S. et al. (2024): Knowledge-based approaches to legal AI explicitly model legal reasoning and can achieve high faithfulness of representation and explainability of inferences, but they face the knowledge acquisition bottleneck because they require large amounts of legal expertise and modeling effort. [CLM-0014-011]
- Gridin (2026): Under a modified Learned Hand calculus (RISK_total = P(failure) x L_legal + C_compliance, and TC = C_dev + min(C_compliance, P_fine + P_lawsuit)), deploying deterministic Linear AI agents drives the probability of hallucination-driven failure to near zero, so that the cost of internal self-regulation is structurally bounded and vastly cheaper than the unbounded aggregate risk of US tort litigation or EU fines; the modelling is stylised and illustrates structural incentives rather than actuarial estimates. [CLM-0049-020]

## Claims about the concept

### Descriptive

**BR**

- Briggs of Westbourne (2026) state that Brazil has struggled for some years with a staggering backlog of approximately 80 million cases, so it is no surprise that AI has gained traction there as an attractive tool for speeding up court processes. [CLM-0047-020]. — jurisdiction: BR; basis: literature

**CZ**

- Novotná and Harašta (2025) state that Searching for similar decisions constitutes a large part of the work of analysts, clerks and judges at the Czech Constitutional Court, and retrieving relevant case law remains a time-consuming task. [CLM-0017-008]. — jurisdiction: CZ; basis: none_stated

**IN**

- Khadloya et al. (2025) state that High-volume courts in India routinely face long filings and crowded dockets that lead to massive case delays, and despite near-universal digitization through e-Courts the core problem of how a judge can interrogate a voluminous record quickly and faithfully remains unsolved. [CLM-0019-002]. — jurisdiction: IN [jurisdiction inferred]; basis: literature

**RU**

- Gridin (2026) state that In the Russian Federation, semiconductor sanctions and hardware constraints have driven leading technology conglomerates and financial institutions (MTS Web Services' MWS AI Agents Platform, Sberbank's multi-agent cash-collection and cybersecurity systems, GigaChat Enterprise) to adopt linear multi-agent architectures, producing a de facto convergence with the Neuro-Symbolic Sandwich model achieved through economic necessity rather than regulatory design; the architecture is therefore a technically neutral infrastructure belonging to no regulatory paradigm. [CLM-0049-044]. — jurisdiction: RU; basis: literature

**general**

- Holzenberger et al. (2020) state that Generating carefully constructed training data for statutory reasoning is comparatively difficult and expensive, because legal texts are written for and by lawyers, who are cost-prohibitive to employ in bulk, unlike most machine reading settings where everyday texts can be annotated through crowdsourcing services. [CLM-0003-014]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Janatian et al. (2023) state that Encoding legislative text in a formal representation is a prerequisite for tasks in AI and Law such as rule-based legal expert systems, but understanding and encoding a legal rule is not easy, may require legal training and considerable time, and can therefore represent a bottleneck in the creation of legal decision support tools. [CLM-0009-001]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that Modern large language models help alleviate the knowledge acquisition bottleneck of knowledge-based legal domain models by enabling (semi-)automated construction of rule-based structures, but whether LLMs can systematize large complexes of legal source material into well-formed, legally correct representations remains an open question. [CLM-0014-008]. — jurisdiction: general; basis: literature
- Tan et al. (2024) state that Creating a meta-evaluation dataset for long-form legal summaries is very resource-intensive, which restricts such datasets to a small size; extending a dataset to more cases and across more jurisdictions would allow more representative and statistically significant tests. [CLM-0015-018]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Steenhuis (2025) state that Because an ensemble classifier can generate follow-up questions automatically when it lacks sufficient confidence, a legal referral tool built on it can gather more information from the applicant without a human having to call the applicant. [CLM-0018-014]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Guha et al. (2023) state that Complete or representative legal data is difficult to acquire because many legal documents are unpublished or available only on request or on paper, and because legal annotation is exceedingly expensive (a modest 500-contract dataset was estimated to cost about two million US dollars), so legal benchmark tasks are typically small samples or synthetic data. [CLM-0026-011]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Guha et al. (2023) state that Interpretation tasks, and clause classification tasks in particular, are among the most studied and practically useful legal tasks for LLMs because they capture an actual current-day use case: manual review of long legal documents requires legal training and is extremely expensive, which raises access-to-justice concerns since most individuals cannot consult lawyers before entering agreements that may contain predatory or unconscionable terms. [CLM-0026-028]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Mahoney et al. (2021) state that The three rationale-identification methods differ in implementation effort: the Document-Level Model Method is the simplest because it requires no extra work, the Snippet Model Method is also simple but takes more time to score each snippet, and the Iterative Snippet Model Method takes significantly more time because of the training iterations required to reach the final snippet model, while each method identifies rationales reasonably well. [CLM-0027-014]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Horner et al. (2025) state that Manual encoding of legal provisions into machine-readable form is a knowledge representation bottleneck: an experienced coder encodes only about 4 to 5 pages per day, encoding large regulatory frameworks raises burnout concerns, and parallel encoding by a team very likely produces mutually incompatible parts whose reconciliation carries considerable overhead, so there is a pressing need for tools that assist with encoding legal instruments. [CLM-0032-016]. — jurisdiction: general; basis: literature
- Maurya (2025) state that Transformer architectures suffer from quadratic computational complexity as sequence length increases, which for legal documents spanning dozens to hundreds of pages and relying on long-range context is a severe barrier: inputs must be truncated or windowed at the risk of losing crucial context, and sparse-attention variants (Longformer, BigBird, Reformer) extend context windows but still fall short of full-document, fully contextual analysis of massive legal corpora without sacrificing efficiency. [CLM-0033-005]. — jurisdiction: general; basis: literature
- Maurya (2025) state that Mamba's selective state-space mechanism updates state representations in linear time and decouples memory and compute needs from sequence length, allowing the processing of sequences vastly longer than transformers feasibly manage on typical hardware, with higher inference throughput on long-document tasks. [CLM-0033-006]. — jurisdiction: general; basis: literature

**undetermined**

- Mahoney et al. (2019) state that In real-world legal matters where minimizing the time or cost of classifying a data set is paramount, for reasons such as monetary costs, sensitivity of data, or time to classify a population, the heavy human review of Continuous Active Learning is often less than ideal for lawyers classifying a population for production to an opposing party or for attorney-client privilege, and the strategy is instead to minimize human review effort and classify the population with minimal human intervention. [CLM-0046-014]. — jurisdiction: undetermined; basis: argument

### Normative

**general**

- Hou et al. (2025) argue that Developing smaller legal LLMs with performance comparable to larger models is a promising future direction, because smaller models can be deployed at lower cost, which matters for future applications in judicial practice. [CLM-0034-030]. — jurisdiction: general; basis: argument
- Gridin (2026) argue that Because manual verification of black-box outputs now often takes human operators longer than performing the original task, raw LLMs are economically and operationally meaningless in law; the regulatory trajectory must pivot from forcing operators into verification loops toward architectures that preemptively eliminate the error at its root. [CLM-0049-017]. — jurisdiction: general; basis: literature

**undetermined**

- Mahoney et al. (2019) argue that Legal teams should consider the MID_75RC active learning selection strategy (selecting training documents nearest the 75 percent recall cut-off score) in their predictive coding process to help reduce review costs. [CLM-0046-007]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Empirical

**general**

- Li et al. (2022) report that Prefix domain adaptation — pre-training a deep prefix prompt with the masked language modelling task on a large unsupervised domain-specific corpus and then using that prompt to initialise prefix tuning for downstream tasks — matches or exceeds the few-shot performance of LEGAL-BERT and related techniques on legal classification tasks while tuning only approximately 0.1% of model parameters. [CLM-0006-001]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that In few-shot settings, prefix domain adaptation outperforms both regular prefix tuning and full finetuning in most tasks across few-shot sizes, despite training considerably fewer parameters, and is comparable to full domain adaptation, in some settings even outperforming it. [CLM-0006-002]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2022) report that Although each optimisation step is faster with regular prefix tuning, regular prefix tuning converges slowly and is therefore not necessarily faster than finetuning; prefix domain adaptation converges faster than regular prefix tuning because its prompts start closer to a desired solution and fewer training steps are needed. [CLM-0006-014]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:CoE**

- Mumford et al. (2023) report that Access to an ANGELIC domain model (ADM) of Article 6 ECHR produced a statistically significant increase in participant productivity at the verdict-classification task, even though it did not significantly improve classification performance. [CLM-0010-013]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment

**geographical_proxy:CoE, geographical_proxy:EU**

- Maurya (2025) report that On long-text legal corpora such as ECtHR and EUR-Lex, Mamba and SSD-Mamba match or surpass transformer models in classification performance while maintaining two to three times higher throughput, demonstrating that state-space models handle extreme input lengths without the windowing overhead that degrades transformer performance. [CLM-0033-009]. — jurisdiction: geographical_proxy:CoE, geographical_proxy:EU (cumulative); basis: dataset_or_experiment

**geographical_proxy:CoE, geographical_proxy:IN, geographical_proxy:EU, geographical_proxy:US**

- Maurya (2025) report that Among the benchmarked models, SSD-Mamba achieves the best overall balance of scalability, accuracy and efficiency, making it a strong candidate for large-scale, real-world legal AI applications involving statutes and long-form case law; for resource-constrained deployments such as large-scale statutory analysis, court policy studies or law-firm knowledge management it provides state-of-the-art accuracy at dramatically lower computational cost. [CLM-0033-010]. — jurisdiction: geographical_proxy:CoE, geographical_proxy:IN, geographical_proxy:EU, geographical_proxy:US (cumulative); basis: dataset_or_experiment

**geographical_proxy:IN**

- Khadloya et al. (2025) report that In a pilot on Indian charge sheets, pleadings and orders, the voice-guided anchor-first navigator cut time-to-relevance from minutes to seconds compared with manual navigation in a stock PDF reader: it halved time-to-relevance on temporal commands (10 s to 5 s) and reduced contextual queries from about 200 s to about 6 s, with median time-to-relevance dropping from 3-5 minutes to 10-15 seconds (30-45 seconds including quick visual verification). [CLM-0019-009]. — jurisdiction: geographical_proxy:IN [jurisdiction inferred]; basis: dataset_or_experiment
- Khadloya et al. (2025) report that Under fixed time budgets, a navigation-first design increases the breadth of the record a judge actually consults while preserving the judge's control and transparency. [CLM-0019-011]. — jurisdiction: geographical_proxy:IN [jurisdiction inferred]; basis: argument

**geographical_proxy:RU**

- Gridin (2026) report that Deploying deterministic linear agents to monitor and execute specific tasks is exponentially cheaper, faster and more secure than attempting to train a monolithic LLM to perform flawlessly across all domains, and multi-agent systems inherently provide the 'Explainable Monitoring Layer' regulators require because the interaction between discrete agents leaves a verifiable algorithmic trail. [CLM-0049-045]. — jurisdiction: geographical_proxy:RU [jurisdiction inferred]; basis: literature
- Gridin (2026) report that In a property-management legal workflow in the Republic of Karelia (2023-2026), the introduction of generative LLMs reduced document drafting time from 1-4 hours to 15-30 minutes, raised daily output from 2-3 to 10-15 complex documents, cut the document error rate from 80% to near 0%, reduced regulatory fines from 3-5 per month to zero, and shortened the litigation resolution cycle from 1-1.5 years to about 6 months, according to internal operational data; these figures are presented as illustrative rather than evidentially established. [CLM-0049-046]. — jurisdiction: geographical_proxy:RU; basis: dataset_or_experiment; temporal reference: 2023-2026

**geographical_proxy:US**

- Steenhuis (2025) report that The weighted ensemble of inexpensive small LLMs outperforms the state-of-the-art GPT-5 model on a cost basis by a factor of more than three for legal intake classification, and the small LLMs also have much lower latency than GPT-5. [CLM-0018-002]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Mahoney et al. (2021) report that It is feasible to build machine learning models that automatically identify rationales without using annotated text snippets for training, and automating the identification of training text snippets without human review could make the application of snippet-trained predictive models a practical approach in legal document review, since snippet-trained models have higher precision than models trained on whole documents but manually annotating training snippets is not generally practical during a review. [CLM-0027-009]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

**undetermined**

- Mahoney et al. (2019) report that Active learning selection strategies such as uncertainty sampling (selecting documents with scores nearest 0.5) and random selection can generate an effective predictive coding model within fewer rounds than the popular top-ranked (TOP) selection strategy. [CLM-0046-004]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Selecting additional training documents nearest to the model's cut-off score for 75 percent recall (the MID_75RC strategy) performs best in almost all experimental scenarios, and would be the most effective active learning strategy when the objective is to achieve 75 percent recall. [CLM-0046-005]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that In the first 50 rounds of active learning, the MID_75RC strategy consistently requires less review to reach 75 percent recall than the top-ranked (TOP) strategy across all four data sets, with a maximum saving close to 20 percent of the document population. [CLM-0046-006]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that When data sets with extremely low richness are excluded, training with documents nearest the 75 percent recall cut-off score (MID_75RC) results in significantly higher performing models in early training rounds such as round 10 or 20, rounds often associated with stopping points for Simple Active Learning; in all three data sets with richness above 10 percent, MID_75RC reached performance within roughly 10 percent of the optimum within 10 rounds of active learning. [CLM-0046-009]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Conceptual

**US, EU**

- Gridin (2026) argue that Under a modified Learned Hand calculus (RISK_total = P(failure) x L_legal + C_compliance, and TC = C_dev + min(C_compliance, P_fine + P_lawsuit)), deploying deterministic Linear AI agents drives the probability of hallucination-driven failure to near zero, so that the cost of internal self-regulation is structurally bounded and vastly cheaper than the unbounded aggregate risk of US tort litigation or EU fines; the modelling is stylised and illustrates structural incentives rather than actuarial estimates. [CLM-0049-020]. — jurisdiction: US, EU (cumulative); basis: argument

**general**

- T.Y.S.S. et al. (2024) argue that Knowledge-based approaches to legal AI explicitly model legal reasoning and can achieve high faithfulness of representation and explainability of inferences, but they face the knowledge acquisition bottleneck because they require large amounts of legal expertise and modeling effort. [CLM-0014-011]. — jurisdiction: general; basis: literature

### Predictive

**GB**

- Briggs of Westbourne (2026) argue that The AI-enabled increase in the number of civil claims will produce better access to justice only if the courts, staff and judges have the capacity to manage and adjudicate them within a reasonable time rather than adding them to a backlog; because an AI platform drafts a claim in seconds while court managers and judges take orders of magnitude longer to read and respond to it, and the taxpayer is unlikely to fund a big increase in civil court staff and judges, that capacity cannot be expected to come from more human resources. [CLM-0047-008]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that It is inevitable that AI will have to be used by the civil courts to increase the productivity of court staff and judges: the robotisation of the courts' response to incoming AI-prepared claims will have to proceed apace if the civil courts are not to sink under the tsunami of claims, and this has already started to happen. [CLM-0047-009]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that Using AI only as a labour-saving device for tasks at the edges of the process for determining civil claims, such as summarising documents, initial legal research, checking draft judgments and streamlining case management, will speed up what remains a human-run process but will not increase productivity by anything approaching the amount needed to cope with the tsunami of AI-generated claims. [CLM-0047-010]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

**IN**

- Malik et al. (2022) argue that NLP-based technology that helps legal practitioners extract relevant information from legal documents could make the legal process more streamlined and efficient and help deal with the backlog of pending cases in India; such technology could not fully automate judgment prediction but could augment the work of a judge or legal practitioner to expedite the legal process in highly populated countries. [CLM-0007-018]. — jurisdiction: IN; basis: argument

**US**

- Mahoney et al. (2021) argue that Incremental improvement in the precision of a text classification model at certain recall rates can have a significant impact on the cost of the legal document review process; for a matter in which a model identifies 1 million responsive documents for review, a 5 percent improvement in precision could result in cost savings of at least $50,000. [CLM-0027-010]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Miller (2025) argue that Construction of a publicly controlled, interpretation-specific model by the legal community raises significant questions of practicality and utility: the decisions required to build it would likely devolve into political deadlock, and hand-picked curation of training data by legal experts would dilute the value of generative AI for ordinary meaning, which rests on its representation of massive, relatively unfiltered bodies of text. [CLM-0039-005]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Miller (2025) argue that Although accessing LLMs may be inexpensive, perfectionist approaches to generative AI research methods could quickly impose unreasonable demands on parties' time both in applying the method and in developing the skills to do so, and courts' lack of technical expertise could prevent intricate research strategies from being adopted and employed successfully. [CLM-0039-026]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**general**

- Li et al. (2022) argue that Seeking legal advice from lawyers is expensive, and a machine learning system that can help answer legal questions could greatly aid laypersons in making informed legal decisions and make legal services more accessible to the public. [CLM-0006-018]. — jurisdiction: general [jurisdiction inferred]; basis: none_stated
- Li et al. (2022) argue that Prefix domain adaptation will make few-shot data more usable, and thus reduce data labelling costs, while using parameter-efficient methods to reduce computational and storage costs; the domain-adapted deep prompt is very small (approximately 0.1% of the base model) and therefore easy to store and distribute. [CLM-0006-019]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Steenhuis (2025) argue that A routing method in which a frontier model such as GPT-5 is asked to classify only the 'hardest' legal intake cases is a promising technique for further narrowing the small remaining error rate of a small-model ensemble classifier. [CLM-0018-016]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Nay et al. (2023) argue that LLMs could disrupt the legal services industry to the extent they replicate much of a skilled lawyer's work, but this possibility should not be overstated: current best models underperform a professional tax lawyer, answering clear-cut legal questions is only a small part of a practising lawyer's work, and clients rely on contextual advice, ethical counsel and nuanced judgement that LLMs cannot yet provide as consistently as most human lawyers; nevertheless there is no strong reason to believe LLMs could not eventually accomplish a wide range of legal tasks with greater performance. [CLM-0024-013]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Nay et al. (2023) argue that Even without replacing trained lawyers, LLMs can assist a lawyer or produce a first draft for the lawyer to check, which could significantly increase lawyers' productivity, decrease the cost of legal services and improve access to legal counsel for people who currently cannot afford it; LLMs could also provide useful legal information to consumers not engaging a traditional lawyer. [CLM-0024-014]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Gridin (2026) argue that Deterministic AI architectures do not replace the legal professional's functions of research, drafting, and strategic judgment but reallocate cognitive resources from the first two to the third; the lawyer of the coming decade is a 'Legal Architect' who translates human objectives into machine-executable legal specifications and interprets algorithmic outputs in terms of rights and legitimacy, and the trajectory of ABA Model Rule 1.1 Comment 8 is toward mandatory AI literacy as a licensing prerequisite. [CLM-0049-040]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:CA-QC**

- Janatian et al. (2023) argue that An LLM pathway generator used in conjunction with a human expert (augmented intelligence) has the potential to support annotators with a strong draft, making annotation more efficient and even yielding more logically correct pathways; LLMs can thus potentially support humans in creating predictable and safe legal expert systems more efficiently, with possible beneficial impacts on access to justice. [CLM-0009-012]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Using AI only as a labour-saving device for tasks at the edges of the process for determining civil claims, such as summarising documents, initial legal research, checking draft judgments and streamlining case management, will speed up what remains a human-run process but will not increase productivity by anything approaching the amount needed to cope with the tsunami of AI-generated claims. [CLM-0047-010] is in tension with the claim that Because legal systems are human-centric and human accountability is paramount for trust in a democratically governed society, the vision of AI & Law is one of AI supporting human decision makers rather than replacing or unduly influencing them, and predictive systems should not be directly applied within courts. [CLM-0014-016] (inferred, low). Note: One predicts that confining AI to labour-saving edge tasks around a human-run process will not cope with AI-driven claim volumes; the other's vision keeps AI in exactly that supporting role — a tension of expectation rather than of principle.

## Distribution

Sources with claims on this concept: 20; claims: 51.

**By contribution type**

| value | sources |
|---|---|
| technical | 17 |
| empirical_quantitative | 15 |
| normative | 4 |
| theoretical | 4 |
| doctrinal | 3 |
| survey | 3 |
| empirical_qualitative | 2 |

**By source jurisdiction**

| value | sources |
|---|---|
| US | 8 |
| general | 7 |
| IN | 2 |
| CA-QC | 1 |
| CZ | 1 |
| CoE | 1 |
| EU | 1 |
| GB | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 13 |
| US | 3 |
| geographical_proxy:US | 3 |
| IN | 2 |
| geographical_proxy:CoE | 2 |
| geographical_proxy:IN | 2 |
| BR | 1 |
| CZ | 1 |
| EU | 1 |
| GB | 1 |
| RU | 1 |
| geographical_proxy:CA-QC | 1 |
| geographical_proxy:EU | 1 |
| geographical_proxy:RU | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2025 | 7 |
| 2023 | 4 |
| 2022 | 2 |
| 2024 | 2 |
| 2026 | 2 |
| 2019 | 1 |
| 2020 | 1 |
| 2021 | 1 |

## What the sources do not address

- No interpretive claim on CPT-cost-efficiency-labour. [ABS-1385] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No methodological claim on CPT-cost-efficiency-labour. [ABS-1386] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
