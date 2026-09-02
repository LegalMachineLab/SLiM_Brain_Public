---
id: "CPT-legal-nlp-research-field"
label: "The legal NLP research field"
status: "emergent"
concept_type: "other"
definition: "The legal NLP and AI and Law research field itself as an object of study: its growth, task and language coverage, method eras, reproducibility practices, evaluation culture and disciplinary provenance (motivating claims: CLM-0023-001, CLM-0023-002, CLM-0023-014)."
aliases: ["computational legal studies", "legal NLP literature"]
broader: []
sources: ["SRC-0003", "SRC-0014", "SRC-0023", "SRC-0026", "SRC-0028", "SRC-0030", "SRC-0032", "SRC-0033", "SRC-0034", "SRC-0035", "SRC-0036", "SRC-0037", "SRC-0038", "SRC-0041", "SRC-0042", "SRC-0043", "SRC-0044", "SRC-0045", "SRC-0046", "SRC-0048", "SRC-0049"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# The legal NLP research field

_Status: emergent; family: other._

## Definition

The legal NLP and AI and Law research field itself as an object of study: its growth, task and language coverage, method eras, reproducibility practices, evaluation culture and disciplinary provenance (motivating claims: CLM-0023-001, CLM-0023-002, CLM-0023-014).

Conceptual claims on this concept, each with its source:
- Hartung et al. (2026): Legal NLP tasks can be characterised from two intersecting perspectives, a lawyer-centric (substantive law) perspective and an engineering perspective (summarization, generation, classification, retrieval and similar tasks), and this dualism affects the vast majority of Legal NLP papers. [CLM-0023-006]
- Hou et al. (2025): Applications of large language models to legal tasks divide into two kinds: fine-tuned legal LLMs, and LLM-based frameworks that leverage existing LLMs within a task framework without training them. [CLM-0034-002]
- Hou et al. (2025): The tasks of legal benchmark datasets for general legal capabilities can be grouped into seven core capabilities: arithmetic, classification, information extraction, knowledge assessment, question answering, reasoning, and retrieval. [CLM-0034-008]
- Chalkidis et al. (2021): Legal text has distinct characteristics — terms uncommon in generic corpora, terms whose senses differ from everyday language, older expressions such as pronominal adverbs, uncommon expressions from other languages, and long sentences with unusual word order — to the extent that legal language is often classified as a 'sublanguage'. [CLM-0048-006]

Aliases: computational legal studies, legal NLP literature.

## Claims about the concept

### Descriptive

**CoE, CN, US, FR, PH, TR, TH, GB, DE, CH**

- Chalkidis et al. (2021) state that Legal judgment prediction, a core task of legal NLP, has been pursued in at least three lines of work — predicting violations of human rights in cases of the European Court of Human Rights, predicting relevant law articles, criminal charges and penalty terms in Chinese criminal cases, and predicting outcomes of cases of the Supreme Court of the United States — and the same or similar task has also been studied on court cases of many other jurisdictions, including France, the Philippines, Turkey, Thailand, the United Kingdom, Germany and Switzerland. [CLM-0048-010]. — jurisdiction: CoE, CN, US, FR, PH, TR, TH, GB, DE, CH (cumulative); basis: literature

**EU, US**

- Gridin (2026) state that Existing scholarship has not produced a formalised legal-architectural framework that simultaneously satisfies the transparency mandates of the EU AI Act, the evidentiary requirements of US procedural law, and the biometric privacy obligations under GDPR and BIPA while remaining operationally deployable by legal practitioners without specialised engineering expertise. [CLM-0049-047]. — jurisdiction: EU, US (cumulative); basis: none_stated

**UA**

- Ovcharov (2026) state that No prior benchmark exists for Ukrainian legal reasoning; UA-Legal-Bench is the first legal reasoning benchmark for a Cyrillic-script, civil-law jurisdiction. [CLM-0035-002]. — jurisdiction: UA; basis: literature

**UA, PL, CZ, LT**

- Ovcharov (2026) state that No prior benchmark exists for Ukrainian, Polish, Czech, or Lithuanian legal reasoning. [CLM-0036-003]. — jurisdiction: UA, PL, CZ, LT (cumulative); basis: literature

**general**

- Holzenberger et al. (2020) state that The intersection between natural language processing and the legal domain is a growing area of research, but one with few large-scale systematic resources. [CLM-0003-016]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- T.Y.S.S. et al. (2024) state that Contemporary legal NLP increasingly applies models that statistically classify legal conclusions from text with little or no explicit domain representation; while conceptually simpler, these approaches often fall short in providing usable justifications that connect to appropriate legal concepts, at the cost of interpretability. [CLM-0014-002]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that Qualified evaluation in legal NLP is underdeveloped: because legal practice support tasks are often ill-defined, convenient but uninformative benchmark metrics receive exaggerated attention, and although many legal NLP works specify use cases, few account for them in their evaluation by conducting studies with legal experts or benchmarking automatic metrics against human evaluations. [CLM-0014-009]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that Despite some recent diversification, virtually all AI & Law research comes from either civil law or common law backgrounds and makes corresponding assumptions about legal systems. [CLM-0014-017]. — jurisdiction: general; basis: none_stated
- Hartung et al. (2026) state that The primary technical challenge limiting transformative technological solutions in law is the complexity of legal language itself (the 'natural language barrier'), and the performance of both academic and commercial Legal NLP applications has conventionally been confounded by computers' inability to accurately and reliably process legal language. [CLM-0023-003]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Hartung et al. (2026) state that The transferability of general-purpose language models to complex specific domains such as law remains an open question: general models have shown real progress on legal tasks, but there remain reasons to believe that some combination of domain-specific pre-training, prompt and context engineering, and other model tuning efforts yields better results across many substantive use cases. [CLM-0023-004]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Hartung et al. (2026) state that The increase in the availability of replication resources in Legal NLP research is, at the same time, an effect of a move towards open availability of legal data in many jurisdictions. [CLM-0023-015]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Guha et al. (2023) state that Most existing legal benchmarks focus on tasks that models learn by fine-tuning or training on task-specific data, and so do not measure the few-shot, many-task capability of large language models that generates excitement for law; benchmarking efforts that instead target professional certification exams such as the Uniform Bar Exam are not always representative of actual use-cases for LLMs. [CLM-0026-001]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Guha et al. (2023) state that Existing legal benchmarks coarsely treat every task involving legal data or laws as measuring 'legal reasoning', whereas lawyers recognise legal reasoning as an umbrella term for many distinct types of reasoning requiring different skills and bodies of knowledge; because the benchmarks do not draw these distinctions, legal professionals find it difficult to contextualise LLM performance within their own understanding of legal competency. [CLM-0026-002]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Guha et al. (2023) state that LEGALBENCH is, to the authors' knowledge, the first open-source legal benchmarking effort and the first steps towards an interdisciplinary, collaboratively constructed legal reasoning benchmark for the English language. [CLM-0026-006]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Deroy et al. (2024) state that LLMs have not been much tried for legal document summarization, and no prior work has systematically compared the three families of summarization models (extractive models, legal-domain abstractive models, and general-domain LLMs) for legal case judgement summarization. [CLM-0028-016]. — jurisdiction: general; basis: literature
- Horner et al. (2025) state that Few prior efforts have addressed the formalization of legal text with the granularity and formal logic representation of a full Defeasible Deontic Logic encoding: recent LLM-based work on legal formalization has been confined to very small scales, such as a single article of the European Arrest Warrant Framework Decision or four rules of the UK Highway Code translated into Prolog via Logical English. [CLM-0032-017]. — jurisdiction: general; basis: literature
- Maurya (2025) state that To date there is no systematic, large-scale comparative analysis of state-space models such as Mamba against transformer models on statutory and case-law tasks; existing legal NLP benchmarks focus almost exclusively on transformer baselines, so the linear scaling and throughput gains of Mamba have not been mapped against practical legal workflows. [CLM-0033-001]. — jurisdiction: general; basis: literature
- Maurya (2025) state that Early rule-based legal expert systems (such as TAXMAN and LEGOL) and case-based reasoning systems (such as HYPO and CATO) were overwhelmed by law's real-world complexity: they worked well for closely bounded domains such as tax or social benefits but failed at open-texture language and variable interpretation. [CLM-0033-003]. — jurisdiction: general; basis: literature
- Maurya (2025) state that The statistical machine-learning models applied to law in the 1990s and 2000s (decision trees, support vector machines, latent semantic analysis, early predictive analytics) laid a foundation but struggled with longer context dependencies, cross-referencing and nuanced explanation, so a true leap required deeper linguistic modelling. [CLM-0033-004]. — jurisdiction: general; basis: literature
- Hou et al. (2025) state that A systematic review and analysis of studies applying large language models in the legal domain was lacking; the survey of 16 legal LLM series, 47 LLM-based frameworks, 15 benchmarks and 29 datasets is the first systematic review covering both traditional and LLM-specific Legal AI datasets together with legal LLMs and LLM-based frameworks. [CLM-0034-001]. — jurisdiction: general; basis: literature
- Hou et al. (2025) state that Benchmark datasets for general legal capabilities of LLMs are typically built by reformatting existing traditional legal datasets to the LLM paradigm, often into a question-answering format. [CLM-0034-010]. — jurisdiction: general; basis: literature
- Hou et al. (2025) state that Judicial practice involves materials beyond text, such as images, videos and recordings, yet almost all legal datasets and the majority of current LLM-based approaches focus only on the text modality. [CLM-0034-020]. — jurisdiction: general; basis: argument
- Hou et al. (2025) state that Most existing legal datasets and LLM-based methods are monolingual rather than multilingual, and research has concentrated on Chinese and English, while other languages require more attention. [CLM-0034-022]. — jurisdiction: general; basis: literature
- Hou et al. (2025) state that Legal AI tasks are evaluated with different metrics: ROUGE is the primary metric for generative tasks such as legal reasoning, summarization and question answering; classification and information extraction tasks typically use accuracy, precision, recall and F1; and precision is often used for retrieval tasks. [CLM-0034-032]. — jurisdiction: general; basis: literature
- Ovcharov (2026) state that Existing legal NLP benchmarks are overwhelmingly English-centric: the major benchmarks (LegalBench, LexGLUE, CUAD) are English-only and predominantly common-law, and multilingual efforts (LEXTREME, MultiLegalPile) cover EU languages but exclude Cyrillic-script jurisdictions and civil-law systems outside Western Europe, so failure modes in morphologically rich, non-Latin-script languages go undetected. [CLM-0035-001]. — jurisdiction: general; basis: literature
- Ovcharov (2026) state that Before Multi-Legal-Bench, no benchmark evaluated identical legal tasks on native court decisions from multiple national legal systems using frontier LLMs; Multi-Legal-Bench is the first legal benchmark with identical tasks evaluated across multiple jurisdictions. [CLM-0036-002]. — jurisdiction: general; basis: literature
- Wang et al. (2026) state that Prior work that uses the LLM itself as the solver reports that this approach outperforms alternatives while reducing syntax errors, but does not evaluate whether the performance boost and error reduction come at the cost of faithfulness to the results a symbolic solver would generate; likewise, round-trip equivalence checking of formalizations detects formalization drift but does not address which unstated assumptions are justified. [CLM-0037-015]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Janeček (2023) state that There is a widespread belief, reinforced by the lawyers' mindset and by lawyers' dominance of the debate, that judgments are always a jurisprudential record of the law to be studied by doctrinal legal analysis only. Because legal thinking is worlds apart from statistical, data-driven reasoning, lawyers often disregard arguments about access to judgments as bulk data as not being arguments about access to judgments at all, so debates about access to judgments for text and data mining purposes are often at cross-purposes. [CLM-0041-008]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hammond (2023) state that The impact of generative AI systems such as ChatGPT differs from that of earlier technologies because it is grounded in language; as a result it is affecting fields that have been somewhat resistant to technological change in the past, and fields that are themselves grounded in language, such as law, are now trying to find ways to adapt to the technology. [CLM-0042-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Deroy et al. (2023) state that As of 2023, there has been little attempt to analyse how abstractive summarization methods and LLMs such as ChatGPT perform in summarizing legal case judgements, and, as far as is known, hallucination and the consistency of abstractive summaries have not previously been studied in the context of legal summarization. [CLM-0044-008]. — jurisdiction: general; basis: literature
- Medvedeva et al. (2021) state that Many current studies that claim to 'predict judicial decisions' are in fact classifying previously made judgements rather than forecasting future ones, because their input data was created after the decision was reached. [CLM-0045-002]. — jurisdiction: general; basis: literature
- Medvedeva et al. (2021) state that Only very few studies focus on forecasting judgements, and most of them report lower performance than studies on judgement classification, which may be indicative of the higher difficulty of forecasting. [CLM-0045-017]. — jurisdiction: general; basis: literature
- Mahoney et al. (2019) state that Existing studies of active learning for legal document review assume human review of all documents the predictive model identifies as relevant and focus on expediting that process through continuous prioritization until target recall is reached; there is a lack of studies focusing on Simple Active Learning and on how to most efficiently train an active learning model that achieves a high level of recall with minimal human review of training documents. [CLM-0046-013]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Mahoney et al. (2019) state that The MID_75RC strategy, which selects additional training documents nearest the cut-off score that yields 75 percent recall of all responsive documents, is a novel active learning selection strategy not previously seen in the literature. [CLM-0046-016]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Chalkidis et al. (2021) state that LexGLUE is the first unified benchmark for assessing the performance of NLP models on legal natural language understanding: it collects seven existing, publicly available and documented English legal NLP datasets (ECtHR Tasks A and B, SCOTUS, EUR-LEX, LEDGAR, UNFAIR-ToS, CaseHOLD) under a standardized evaluation, with tasks simplified to make them accessible to newcomers and generic models. [CLM-0048-001]. — jurisdiction: general; basis: dataset_or_experiment
- Ali et al. (2021) state that No earlier paper had applied natural language processing techniques to extract evidence information from court judgements and used that information to retrieve relevant prior court cases; prior work on evidence retrieval and evidence detection did not combine sentence-level evidence extraction, a rich structured representation, and prior case retrieval. [CLM-0043-001]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Interpretive

**CN**

- Li et al. (2024) read Legal data resources as follows: Existing Chinese legal LLM benchmarks built from traditional natural language processing datasets, such as LawBench and LaiW, do not provide a standardized and comprehensive evaluation: traditional datasets test specific capabilities from a computer-centric perspective that does not always reflect practical legal use of LLMs, these benchmarks often overlook legal ethics, and their evaluation metrics vary significantly. [CLM-0030-004]. — jurisdiction: CN; basis: argument

**general**

- Li et al. (2024) read The legal NLP research field as follows: Existing general-purpose LLM evaluation benchmarks, such as C-Eval, provide limited guidance for the legal domain because they assess generalist abilities on non-professional or semi-professional texts and are unable to reflect or capture the complexity of judicial cognition and decision-making. [CLM-0030-003]. — jurisdiction: general; basis: argument
- Mahoney et al. (2019) read E-discovery as follows: The conflicting conclusions of Cormack and Grossman (that top-scored document selection consistently outperforms other active learning strategies) and of Chhatwal et al. (that always selecting the highest-scoring documents may not be the most efficient approach) are due to evaluating the selection strategies differently, on the training set alone versus on both the selected documents and the documents classified by the model, and both are understandable given the dual purpose of active learning: quickly finding as many relevant documents as possible and training an effective final model in as few rounds as possible. [CLM-0046-012]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Normative

**general**

- Hartung et al. (2026) argue that Publications in computational legal studies and natural legal language processing should be more than mere papers and should ideally contain both code and data for reproduction, because making code as well as data available significantly facilitates and accelerates subsequent research. [CLM-0023-019]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Guha et al. (2023) argue that Rigorously evaluating the legal reasoning capabilities of LLMs requires the legal community to take a more proactive, participatory role in benchmark construction, with domain experts crafting evaluation tasks; legal professionals have an essential role to play in the assessment and development of LLMs for law. [CLM-0026-004]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Guha et al. (2023) argue that A paradigm of expert-driven evaluation that defines fine-grained measures of performance, allowing model capabilities to be discussed with precision and specificity, is essential for specialised domains like law. [CLM-0026-005]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Guha et al. (2023) argue that Performance on a generalised benchmark such as LEGALBENCH offers only a preliminary understanding of LLM capability and is not a substitute for in-depth, context-specific evaluation: the deployment of any AI application in the law must be accompanied by evaluation on in-domain data and assessments of ethical and legal compliance, practitioners should perform their own use-case-specific data collection and validation, and the benchmark should not be used to predict the legality of real-world events, the outcome of lawsuits, or as legal advice. [CLM-0026-026]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Li et al. (2024) argue that Continuous technological innovation and interdisciplinary cooperation are needed to bring about more powerful legal LLMs and improve the efficiency and quality of legal services. [CLM-0030-024]. — jurisdiction: general; basis: argument
- Hou et al. (2025) argue that Future research could explore how to combine multimodal data with text to improve model performance on legal tasks adapted to real-world scenarios. [CLM-0034-021]. — jurisdiction: general; basis: argument
- Hou et al. (2025) argue that Future studies should focus on multilingual legal LLMs or LLM-based frameworks that address linguistic differences between legal systems, to ensure broader applicability in transnational legal contexts. [CLM-0034-024]. — jurisdiction: general; basis: argument
- Ovcharov (2026) argue that Legal NLP evaluation needs multilingual legal benchmarks with appropriate, class-aware metrics, because patterns such as accuracy masking majority-class prediction and few-shot prompting compensating for model scale are invisible in English-only, accuracy-only evaluation. [CLM-0035-015]. — jurisdiction: general; basis: dataset_or_experiment
- Chalkidis et al. (2021) argue that Because legal documents are typically written in the official language of their country of origin, there is an increasing need for developing legal NLP models for languages other than English; the current lack of legal NLP datasets in languages other than English (with the exception of Chinese) makes a multilingual extension of LexGLUE challenging. [CLM-0048-011]. — jurisdiction: general; basis: argument

### Empirical

**CN**

- Hou et al. (2025) report that The benchmark evaluation system for Chinese legal LLMs is more comprehensive than that of any other language; benchmarks for other languages such as English and Korean primarily evaluate general LLMs rather than legal LLMs. [CLM-0034-014]. — jurisdiction: CN [jurisdiction inferred]; basis: literature

**general**

- Hartung et al. (2026) report that Legal NLP is beginning to match not only the methodological sophistication of general NLP but also the professional standards of data availability and code reproducibility observed within the broader scientific community; the field is growing rapidly in volume and significantly in diversity of languages and sophistication of methods. [CLM-0023-001]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that The number of Legal NLP papers published per year increased nearly seven-fold between 2013 and 2024, with the annual total doubling roughly every three years, and more than a third of the papers in a near-complete corpus of 932 Legal NLP papers were written after 2022, coinciding with the wide availability of LLMs. [CLM-0023-002]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that Legal NLP papers spanning two or more engineering task categories are a recent phenomenon: before 2018 virtually no Legal NLP paper was categorised in more than one task category, overlaps appeared around 2018 and 2019 coinciding with advances such as GPT and BERT, and in 2023 and 2024 more than half of the documented papers fell within multiple categories. These recurring combinations ('motifs') characterise a new, technically more complicated type of research likely enabled by the ubiquity of LLMs. [CLM-0023-007]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that The Resources category of Legal NLP papers (taxonomies, ontologies, benchmarks, datasets, code libraries) rose sharply in the last two years of the 2013-2024 period, driven by a large number of evaluation papers that apply different LLMs to legal tasks in specific substantive or practice areas and evaluate the results against human subject-matter experts or existing benchmarks; the rise of such papers represents a shift from purely technical to increasingly legal evaluations and points to the proliferation of NLP tools in legal research. [CLM-0023-008]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that Legal text generation and summarization played a rather limited role in Legal NLP over the first decade of the 2013-2024 period but picked up speed in the last few years: text generation has grown remarkably since 2022, whereas summarization has grown too, but not to the same extent. [CLM-0023-009]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that Individual eras of NLP methods (from tf-idf and SVM via word2vec, RNN and LSTM to transformers, LLMs and RAG) can be traced in the Legal NLP literature; most methods seem to reach peak popularity in Legal NLP some time after they were first published, but that delay tends to get shorter for newer methods, and the data show persistent progress within the field toward cutting-edge models at any given point in time. [CLM-0023-010]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that English is the most common language of the legal corpora analysed in Legal NLP papers (54% of the 2013-2024 corpus), followed by Chinese (10%) and EU law (just under 8%, labelled separately because EU legal documents appear in many languages), while German, French, Portuguese, Japanese and Italian each make up between 3% and 5%, likely reflecting their digitally available legal corpora and disproportionately large research communities in computer science and law. [CLM-0023-011]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that Over 2013-2024 the proportion of Legal NLP papers analysing English-language corpora remained roughly constant, papers analysing Chinese-language corpora increased substantially and more strongly in later years, particularly after 2023, and the overall diversity of languages increased, with the sum of less common languages growing over time. [CLM-0023-012]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that Legal NLP authors have become markedly more inclined over time to make replication resources publicly available: the proportion of papers with no working resource links (Class I) decreased from 92% in 2013 to 20% in 2022, papers with well-documented code and data repositories (Class III) increased from 4% to 46.1% over the same period, growth accelerated strongly in 2023 and 2024, and by then more than half of the papers make their code available and three quarters provide a dataset, indicating increased commitment to reproducibility and increasing rigor and professionalism within the Legal NLP community. [CLM-0023-014]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: 2013-2024
- Hartung et al. (2026) report that Legal NLP papers containing datasets, code, or both gain considerably more citations on average than those without; an analysis of variance shows that the availability of either a dataset or code significantly boosts citations while providing both has no additional effect, and the effect size is rather negligible, suggesting that many other factors, including publication age, drive citations more strongly than resource availability alone. [CLM-0023-016]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: as of September 2025
- Hartung et al. (2026) report that Citation counts in Legal NLP display the expected bibliometric skew towards the top papers, and publication age is a weak but significant contributor to citation count (rho = 0.281), suggesting a more sustained citation accumulation than bibliometric burst-and-decay models would predict, which may be explained in part by Legal NLP results remaining relevant for longer periods than in faster-moving fields. [CLM-0023-017]. — jurisdiction: general; basis: dataset_or_experiment; temporal reference: as of September 2025
- Hou et al. (2025) report that Across existing benchmarks of general legal capabilities, classification (for example clause classification and legal judgement prediction) is emphasised by all benchmarks, whereas arithmetic (for example crime amount calculation) and knowledge assessment (for example legal concept memorization) are underrepresented. [CLM-0034-009]. — jurisdiction: general; basis: literature
- Hou et al. (2025) report that Most existing legal LLMs have between 6B and 13B parameters, and most adopt the LLaMA architecture as their base model. [CLM-0034-012]. — jurisdiction: general; basis: literature
- Hou et al. (2025) report that Of the 96 works on LLM-related legal datasets and approaches covered by the survey, 4 are GitHub repositories; of the papers, 34 are preprints, 21 appeared in NLP conferences or workshops, 20 at machine learning or AI venues, 11 at data mining venues and 6 at other venues. [CLM-0034-033]. — jurisdiction: general; basis: literature

### Conceptual

**general**

- Hartung et al. (2026) argue that Legal NLP tasks can be characterised from two intersecting perspectives, a lawyer-centric (substantive law) perspective and an engineering perspective (summarization, generation, classification, retrieval and similar tasks), and this dualism affects the vast majority of Legal NLP papers. [CLM-0023-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hou et al. (2025) argue that Applications of large language models to legal tasks divide into two kinds: fine-tuned legal LLMs, and LLM-based frameworks that leverage existing LLMs within a task framework without training them. [CLM-0034-002]. — jurisdiction: general; basis: argument
- Hou et al. (2025) argue that The tasks of legal benchmark datasets for general legal capabilities can be grouped into seven core capabilities: arithmetic, classification, information extraction, knowledge assessment, question answering, reasoning, and retrieval. [CLM-0034-008]. — jurisdiction: general; basis: literature
- Chalkidis et al. (2021) argue that Legal text has distinct characteristics — terms uncommon in generic corpora, terms whose senses differ from everyday language, older expressions such as pronominal adverbs, uncommon expressions from other languages, and long sentences with unusual word order — to the extent that legal language is often classified as a 'sublanguage'. [CLM-0048-006]. — jurisdiction: general; basis: literature

### Predictive

**general**

- Hartung et al. (2026) argue that Because large language models have fully entered public perception, players historically disinterested in Legal NLP research, such as publishing houses, law firms and courts, now have viable commercial interest in it; possessing vast data collections, they might be increasingly willing to share them with researchers, which is likely to lead to an uptick in research using real-world, commercial, or administrative datasets. [CLM-0023-021]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hartung et al. (2026) argue that Within the larger world of legal technology, language-centric technologies are likely to play an ever-increasing role, and public players will likely focus on deployment in the context of digital justice, leveraging neural-era models to reduce case backlogs, improve access, and develop the ability to deliver justice at scale. [CLM-0023-022]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hartung et al. (2026) argue that The developments observed in Legal NLP point to a growing awareness and better understanding of computational legal studies among traditional legal scholars and other empirically-minded scholars, which might well result in increased intra-disciplinary collaboration and a greater openness toward quantitative methods, thereby fostering the relevance of Legal NLP in the academic community. [CLM-0023-023]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Methodological

**CoE**

- Medvedeva et al. (2021) argue that Predicting the list of articles of the European Convention on Human Rights potentially violated in a case has no clear practical use, because the articles involved are known as soon as the application is submitted; a realistic scenario for the European Court of Human Rights would only involve deciding whether or not a given article was violated. [CLM-0045-016]. — jurisdiction: CoE; basis: argument

**general**

- Hartung et al. (2026) argue that Identifying which papers belong to Legal NLP requires qualitative human judgment, because law is an intellectual domain at the intersection of the humanities and social sciences whose boundaries are famously open-textured; a workable guiding principle is to include any technical paper whose target audience is a legal scholar or practitioner. [CLM-0023-005]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hartung et al. (2026) argue that Because only papers themselves written in English were surveyed, which introduces a relevant bias, and because significant scholarship on non-English legal languages is likely published only in those languages, the reported language distribution of Legal NLP research should be considered a lower-bound estimate of the field's linguistic diversity. [CLM-0023-013]. — jurisdiction: general; basis: argument
- Hartung et al. (2026) argue that A hybrid, human-in-the-loop approach to information management, combining state-of-the-art natural language processing tools to find and curate publications for review with subject-matter-expert human control, and realised as a living, interactive survey with web infrastructure accepting community contributions, is suggested as the way to survey the fast-growing and linguistically and methodologically diverse Legal NLP literature. [CLM-0023-018]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hartung et al. (2026) argue that The effects of training data, model architectures, and modeling techniques in Legal NLP, as compared with the continuous increase in scale of general models, require extensive further research. [CLM-0023-020]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Ovcharov (2026) argue that Existing legal NLP benchmarks either evaluate a single language or aggregate tasks that differ fundamentally from one jurisdiction to another, which makes cross-lingual comparison impossible: when the tasks differ, performance differences confound language ability with task difficulty. [CLM-0036-001]. — jurisdiction: general; basis: literature
- Chalkidis et al. (2021) argue that A legal NLU benchmark should include datasets that check the ability of systems to understand and reason about legal text in order to perform tasks meaningful for legal practitioners, that leave large scope for improvement for state-of-the-art methods, that are publicly available and documented by published articles, and that are not very small (fewer than 5K documents); unlike SuperGLUE, datasets requiring legal domain expertise should be favoured rather than ruled out. [CLM-0048-008]. — jurisdiction: general; basis: argument
- Zhang et al. (2026) argue that Existing legal AI benchmarks such as CUAD, LegalBench and COLIEE focus primarily on isolated skills rather than the integrated application of a reasoning chain; structuring evaluation around a principled, decomposed reasoning process instead of atomic components enables detailed analysis of where models succeed and fail and provides a methodology for fine-grained analysis of LLM reasoning capabilities in complex domains, identifying limitations before deployment. [CLM-0038-011]. — jurisdiction: general [jurisdiction inferred]; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that The intersection between natural language processing and the legal domain is a growing area of research, but one with few large-scale systematic resources. [CLM-0003-016] is in tension with the claim that The CanLII database, with more than two million Canadian court and tribunal decisions from fourteen jurisdictions in parsable format with structured metadata, statutes and regulations with section-level tables of contents, and millions of hyperlinked citations extracted and standardised by the Reflex citator, already constitutes a highly structured 'map' of Canadian law that is available as a significant dataset for training machine-learning algorithms. [CLM-0001-004] (inferred, low). Note: One states that legal NLP has few large-scale systematic resources; the other presents a two-million-decision database with an extracted citation network as a significant training resource — the tension dissolves if 'systematic resource' means an annotated benchmark rather than a raw corpus.

## Distribution

Sources with claims on this concept: 21; claims: 78.

**By contribution type**

| value | sources |
|---|---|
| technical | 18 |
| empirical_quantitative | 16 |
| theoretical | 10 |
| normative | 4 |
| survey | 4 |
| doctrinal | 2 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 11 |
| US | 5 |
| CoE | 2 |
| IN | 2 |
| CN | 1 |
| EU | 1 |
| GB | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 20 |
| CN | 3 |
| CoE | 2 |
| UA | 2 |
| US | 2 |
| CH | 1 |
| CZ | 1 |
| DE | 1 |
| EU | 1 |
| FR | 1 |
| GB | 1 |
| LT | 1 |
| PH | 1 |
| PL | 1 |
| TH | 1 |
| TR | 1 |

**By year**

| value | sources |
|---|---|
| 2026 | 6 |
| 2023 | 4 |
| 2021 | 3 |
| 2024 | 3 |
| 2025 | 3 |
| 2019 | 1 |
| 2020 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
