---
id: "CPT-explainability-and-transparency"
label: "Explainability and transparency"
status: "anchor"
concept_type: "normative_concern"
definition: "Whether AI outputs and processes can be explained, inspected, or understood."
aliases: []
broader: []
sources: ["SRC-0004", "SRC-0006", "SRC-0012", "SRC-0014", "SRC-0015", "SRC-0016", "SRC-0019", "SRC-0021", "SRC-0022", "SRC-0026", "SRC-0027", "SRC-0029", "SRC-0033", "SRC-0034", "SRC-0037", "SRC-0039", "SRC-0043", "SRC-0045", "SRC-0047", "SRC-0049", "SRC-0050"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Explainability and transparency

_Status: anchor; family: normative_concern._

## Definition

Whether AI outputs and processes can be explained, inspected, or understood.

Conceptual claims on this concept, each with its source:
- Mumford et al. (2021): Factor-based explanations of the CATO kind explain well cases in which the dispute turns on the balance of the ascribed factors, but are less satisfactory in cases where the losing party contended that other factors were present, or where the presence of a factor was itself contested; in such cases the explanation the losing party needs is why the claim that other factors were present was rejected, or why a factor was held to apply. [CLM-0004-002]
- Mumford et al. (2021): The ascription of factors that correspond to ranges on well-ordered dimensions can be explained in terms of the precedents that establish those ranges, but this kind of explanation does not seem applicable to factor ascriptions that rest on detailed consideration of very particular facts, which may involve analogy or some kind of common-sense ontology. [CLM-0004-006]
- T.Y.S.S. et al. (2024): Knowledge-based approaches to legal AI explicitly model legal reasoning and can achieve high faithfulness of representation and explainability of inferences, but they face the knowledge acquisition bottleneck because they require large amounts of legal expertise and modeling effort. [CLM-0014-011]
- Lee and Egbert (2025): LLM chatbot responses to ordinary-meaning questions are neither a corpus linguistic analysis of natural language use nor a survey of human intuitions about ordinary meaning; at most they present the intuitions of a single artificial entity, functioning as an artificial expert witness that simulates one well-read human, and those artificial intuitions are no more transparent, replicable, or generalizable than the intuitions of an ordinary person or a judge. [CLM-0021-002]
- Lee and Egbert (2025): The core case for modern textualism, that a careful judicial investigation into ordinary communicative content constrains judicial discretion, rests on three pillars, transparency, replicability, and generalizability, and the viability of any tool offering evidence of empirical linguistic fact should be measured by the degree to which it lives up to those three standards. [CLM-0021-003]
- Mahoney et al. (2021): In legal document review a document is considered responsive when any portion of it contains responsive information, which is not always true of other text classification tasks such as topic classification, where the entire document may concern the topic; consequently, locating the responsive text snippets in a responsive document would let attorneys easily evaluate a model's document classification decisions. [CLM-0027-007]
- Neumann et al. (2026): Regulators necessarily interpret natural-language prompts through social, legal and institutional understandings of meaning, obligation and intent, which is not comparable to how language models process instruction text through layers of statistical pattern matching shaped by training and sensitive to phrasing and context; linguistic accessibility therefore risks importing human interpretive assumptions into machine governance. [CLM-0050-010]

## Claims about the concept

### Descriptive

**US**

- Mahoney et al. (2021) state that Although attorneys have used machine learning text classification (predictive coding) for more than ten years to cull large volumes of electronically stored data and identify responsive documents, reducing the discovery costs of legal matters, the technology faces a perception challenge: lawyers sometimes regard it as a 'black box', because typically no extra information is provided to explain why documents are classified as responsive. [CLM-0027-008]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**US, EU**

- Neumann et al. (2026) state that Emerging governance instruments in the United States (Executive Order 14319 and the OMB memorandum on Unbiased AI Principles) and the European Union (General-Purpose AI Code of Practice) treat system prompts as legible artefacts that can be disclosed, inspected and revised to support oversight, on the presumption that prompt language shapes system behaviour, so that regulators treat prompt language as a proxy for model performance. [CLM-0050-004]. — jurisdiction: US, EU (comparative); basis: legislation; positive form: general_rule

**general**

- Mumford et al. (2021) state that There has been little or no work in AI and Law on explaining why factors are present or absent in a case, because most research since HYPO has taken the factors as given. [CLM-0004-003]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that Contemporary legal NLP increasingly applies models that statistically classify legal conclusions from text with little or no explicit domain representation; while conceptually simpler, these approaches often fall short in providing usable justifications that connect to appropriate legal concepts, at the cost of interpretability. [CLM-0014-002]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that The working assumption of legal outcome classification research that better benchmark performance means models encode more legal knowledge extractable as explanations has not been fulfilled: rationale-alignment studies, low expert agreement, reliance on shallow predictors, and the limited utility of saliency maps for humans all cast doubt on the assumption that, at least for classifier models, benchmark performance correlates with better explanations. [CLM-0014-004]. — jurisdiction: general; basis: literature
- Tan et al. (2024) state that Beyond performance, an advantage of the pointwise evaluation method over existing metrics is its interpretability and explainability: it shows exactly which reference points are included in or missing from a candidate summary, and which candidate points are absent from the reference, which allows targeted improvement of the summarizing LLM's prompts. [CLM-0015-007]. — jurisdiction: general; basis: argument
- Blair-Stanek and Van Durme (2025) state that Why leading LLMs are unstable even with temperature 0 and a fixed seed cannot be determined with certainty, because the models are proprietary; possible causes are nondeterminism in the ordering of floating-point accumulation, cloud hosting in which identical API calls are handled by different servers with slightly different floating-point implementations, and parallelisation across servers or processors whose varying loads change the order of execution. [CLM-0016-005]. — jurisdiction: general; basis: literature
- Khadloya et al. (2025) state that Existing legal question-answering and retrieval benchmarks operate at the document level, returning entire cases rather than pinpointed spans, and are not designed for judge-facing interaction loops; most legal QA and summarization systems return text without a user interface that enforces verification. [CLM-0019-003]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Waldon et al. (2025) state that Even with perfectly curated fine-tuning data, the direct-query method is flawed because it mistakenly assumes that LLMs can faithfully articulate plain-language characterisations of their underlying linguistic generalisations. LLM chatbots answering metalinguistic questions are pseudolinguists rather than artificial linguists: their stated judgments about language are poorly calibrated to what the models have actually learned about the statistics of language, so direct querying is a coarse and unreliable means of probing the linguistic knowledge LLMs encode. [CLM-0022-005]. — jurisdiction: general; basis: literature
- Waldon et al. (2025) state that Direct chatbot queries are not reproducible: chatbot responses depend on hidden system prompts that developers may change unobserved, on prior exchanges and cross-session chat history, and on sampling randomness governed by seed and temperature settings that may be inaccessible to users. Consequently, even the disclosures Judge Newsom made in Snell and Deleon (exact prompts, models, number of queries) are not enough to fully reproduce his procedures. [CLM-0022-007]. — jurisdiction: general; basis: argument
- Waldon et al. (2025) state that Closed-source chatbot platforms rely on inaccessible training data, non-transparent models and hidden system prompts and change constantly under opaque circumstances, so it is not possible to assess the underlying LLM's ability to reflect ordinary linguistic meaning; a closed model cannot be 'called to the stand' for re-questioning by dissenting views or on appeal, making decisions based on its outputs inscrutable. Fully open-source solutions are the only ones that enable fully transparent reporting of LLM interactions. [CLM-0022-012]. — jurisdiction: general; basis: argument
- Medvedeva et al. (2021) state that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015]. — jurisdiction: general; basis: argument

### Interpretive

**EU**

- Gridin (2026) read AI Act, Art. 13(1) as follows: Deploying a raw, unconstrained generative LLM in a high-stakes legal setting is a fundamental and inescapable violation of Article 13 of the EU AI Act, because a deep neural network with hundreds of billions of weights cannot provide a transparent, linear logic path enabling deployers to interpret its output, and any post-hoc explanation the LLM generates is merely another probabilistic guess. [CLM-0049-023]. — jurisdiction: EU; basis: legislation
- Gridin (2026) read AI Act, Art. 13(1) as follows: The transparency requirement of Article 13 of the EU AI Act can be satisfied not by explaining the deep neural network but by structurally barricading the deployer from it: when the output delivered to the human is certified by a deterministic Linear AI agent operating on observable Boolean conditions, and each action leaves a micro-code decodable through the organisation's Codification Reference Directory, the deployer receives exact, interpretable criteria. [CLM-0049-024]. — jurisdiction: EU; basis: legislation
- Neumann et al. (2026) read General-Purpose AI Code of Practice (EU, 10 July 2025), Measure 7.1 as follows: The EU General-Purpose AI Code of Practice treats the system prompt as part of the model specification to be disclosed to evaluation teams for models presenting systemic risk, but it does not operationalise the multiple layers of system-level instructions across the AI supply chain and does not require prompt versioning, change logs, or triggers for re-evaluation when system prompts are updated, so that disclosure can quickly become outdated. [CLM-0050-006]. — jurisdiction: EU; basis: legislation

**US**

- Lee and Egbert (2025) read United States v. DeLeon, 116 F.4th 1260 (11th Cir. 2024) as follows: Judge Newsom's identification in DeLeon of a 'common core' across the varying responses to his serial AI queries is not the result of a transparent, replicable experiment about ordinary meaning but the product of a subjective determination by an individual judge of what should count as the core ordinary meaning, because 'common core' is not operationalized in a transparent, replicable way and the conclusion glosses over the quantitative questions embedded in it. [CLM-0021-020]. — jurisdiction: US; basis: argument
- Miller (2025) read Ordinary meaning interpretation as follows: Weighed against the general unfamiliarity of new methods and the subjectivity inherent in LLM construction, the public accessibility of generative AI and the ability to manage some subjectivity through standardized interpretive techniques and judicial communication give reason to think that consulting generative AI offers superior transparency benefits (predictability and fair notice) over dictionaries when appropriate, since dictionaries themselves leave something to be desired on transparency. [CLM-0039-019]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Gridin (2026) read Fed. R. Civ. P. 37(e) as follows: An immutable micro-ledger in which every human prompt, every LLM generation, and every Linear AI validation is cryptographically hashed and appended to the document's metadata makes a 'lost chat history' technically impossible, ensures preservation of electronically stored information, and lets a subpoenaed corporation produce its Codification Reference Directory so that a judge can reconstruct the document's generative history, insulating the corporation from FRCP Rule 37(e) sanctions. [CLM-0049-027]. — jurisdiction: US; basis: argument
- Neumann et al. (2026) read Executive Order 14319, Preventing Woke AI in the Federal Government (July 2025), Sec. 3 as follows: The United States federal procurement framework (Executive Order 14319 and the OMB memorandum implementing it) treats system prompts as an optional transparency artefact whose disclosure may evidence compliance with the Unbiased AI Principles, does not require empirical evaluation of their behavioural effects, and, by excluding system prompts from its model-evaluations section, embeds an implicit assumption that inspecting prompt language is sufficient. [CLM-0050-005]. — jurisdiction: US; basis: legislation

**general**

- Ali et al. (2021) read Information retrieval as follows: Because SemMatch computes matching scores for individual Evidence Structure instances, it can provide better interpretation of each relevant document, in terms of the actual sentences that produced the maximum matching score, than BM25-based techniques that score the whole document. [CLM-0043-013]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:NL**

- Gridin (2026) read Explainability and transparency as follows: The Dutch childcare benefits scandal shows that a black-box fraud-detection algorithm whose logic the overseeing humans could not audit produced mass injustice that cannot afterwards be 'rewound' to establish culpability in individual cases; a Neuro-Symbolic Sandwich using closed libraries and an immutable Codification Table would prevent such outcomes by guaranteeing absolute retrospective auditability of every parameter weighed. [CLM-0049-015]. — jurisdiction: geographical_proxy:NL [jurisdiction inferred]; basis: literature

**geographical_proxy:US**

- Gridin (2026) read State v. Loomis, 881 N.W.2d 749 (Wis. 2016) as follows: Corporations frequently obscure their algorithms behind commercial secrecy not to protect advanced technology but to mask the immaturity, bias, and rudimentary nature of their models and thereby evade liability; there is no legitimate justification for deploying opaque logic in environments that demand absolute legal certainty. [CLM-0049-014]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: literature

### Normative

**EU**

- Gridin (2026) argue that Transparency and explainability mandates are necessary but insufficient: Article 14 of the EU AI Act identifies human oversight as a requirement but provides no architectural specification for achieving it, so future regulatory instruments, including the AI Act's implementing acts and harmonised standards, should incorporate minimum architectural requirements for AI in high-risk legal contexts - mandatory deterministic validation layers, immutable audit logging, and formalised access-authorisation protocols for biometric evidentiary data. [CLM-0049-038]. — jurisdiction: EU; basis: argument
- Gridin (2026) argue that The industry norm of releasing generative foundation models as standalone products with post-hoc XAI layers appended must be abandoned; as enforcement under Articles 9 and 14 of the EU AI Act emerges, the liability trajectory for providers of unguarded high-risk systems will become untenable, and releasing the LLM only within a pre-packaged deterministic validation environment is the commercially rational and legally defensible product architecture for the high-stakes legal market. [CLM-0049-039]. — jurisdiction: EU; basis: argument

**GB**

- Briggs of Westbourne (2026) argue that There will need to be complete transparency about how far AI is assisting, or in certain areas replacing, the work of human judges, so that what actually happens behind the scenes does not get out of step with public expectations. [CLM-0047-016]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

**US**

- Lee and Egbert (2025) argue that Corpus linguistic tools are, to date, the one main set of tools that can produce transparent, replicable, and generalizable empirical evidence relevant to ordinary-meaning questions like those in Snell and DeLeon, and judges should continue to rely on corpus data in place of LLM AI queries. [CLM-0021-006]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Miller (2025) argue that Judges who use generative AI for interpretation should be required to preregister research plans specifying the models, versions, prompts, and any temperature or parameter alterations, and to give a supplemental rationale for any deviation; preregistration eliminates unexplained subjectivity in selecting between models and results, though it raises unresolved practicality concerns about who would police the plans and how contested deviations would be reviewed. [CLM-0039-003]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Miller (2025) argue that Generative AI interpretation should be standardized to a narrow range of high-quality models with an established track record, trained on data too expansive to easily alter (such as ChatGPT, Gemini, and Claude), using the most current version freely available to the public, so that the public has access to the models used by the court; a judge's decision to go beyond that subset should be rationalized in the preregistered research plan. [CLM-0039-004]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Miller (2025) argue that Judges using generative AI for interpretation should be required to export the results of their investigation as a digital file providing a clear transcript of the research process, so that interested parties can compare the results against the preregistered research plan and detect deviation; this serves as an additional layer of public reassurance reinforcing the credibility of judicial results rather than ensuring their accuracy, and parties submitting their own generative AI results should likewise be required to export complete, consolidated accounts. [CLM-0039-017]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Gridin (2026) argue that In US AI-malpractice litigation, courts should recognise that a functional, documented deterministic audit trail constitutes evidence of a reasonable standard of care under the Learned Hand negligence calculus and should treat the presence or absence of a CAC-equivalent architecture as a material factor in corporate liability, a development within federal courts' existing authority under FRCP Rule 37(e) and FRE Rules 901-902; new federal AI legislation is not required. [CLM-0049-021]. — jurisdiction: US; basis: argument

**general**

- Mumford et al. (2021) argue that Explanations of legal decisions must go beyond the factors present in a case and the preferences between them: they must also explain the ascription and non-ascription of the factors themselves, that is, why particular factors are held to be present or absent. [CLM-0004-001]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that Traditional machine-learning explanations of predicted legal outcomes, such as listing or highlighting the most influential words in the text, are unhelpful and inappropriate in a legal context, because the right to explanation requires an explanation capable of persuading the losing party and withstanding appeal: not an account of how the decision was reached, but of why the decision represents the proper application of the law. [CLM-0004-004]. — jurisdiction: general [jurisdiction inferred]; basis: literature Same proposition asserted by: T.Y.S.S. et al. (2024) [CLM-0014-020].
- Li et al. (2022) argue that Calibration is important for legal models: a properly calibrated model reduces misuse because software systems can better handle cases where the model is uncertain, it improves interpretability of model confidence, and it is especially important in the legal domain given the high-stakes nature of legal decision making; when providing predictions to laypersons, output logits must accurately reflect the model's confidence. [CLM-0006-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- T.Y.S.S. et al. (2024) argue that Legal NLP efforts should be evaluated and reviewed in terms of how well models support the production, structuring and assessment of arguments about legal conclusions for practitioners, and research on evaluation criteria that better capture the practical utility of legal NLP systems in real-world settings should be among the field's top priorities. [CLM-0014-010]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that There is value in NLP that produces, structures and assesses arguments about legal conclusions in an explainable way using domain knowledge representation: even with powerful LLMs available, argumentation support systems for legal practitioners benefit from structured representations of legal information and argumentation and should produce arguments transparently, offering users an intuitive way of resolving multiple complex arguments towards a justification of a decision. [CLM-0014-012]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that Any data-driven legal NLP system intended for practical deployment must undergo rigorous scrutiny of its performance, behavior and intended application to ensure compliance with applicable equal treatment and transparency imperatives, because training on historical data and inheriting biases from pre-training data may introduce biases into the system. [CLM-0014-021]. — jurisdiction: general; basis: literature
- Khadloya et al. (2025) argue that Judicial tools for long records should target direct, auditable navigation to the exact anchored locus in the record rather than free-form summarization, because adjudication prioritizes verifiability and summaries can hide citations and miss pivotal passages. [CLM-0019-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Waldon et al. (2025) argue that Until AI interpretability research has progressed far enough to say what a given model has learned about English from its training data, there is no fully responsible way to use LLMs as proxies for ordinary meaning, because without knowing what LLMs learn one cannot measure whether and to what extent their linguistic competence diverges from ordinary competence. [CLM-0022-006]. — jurisdiction: general; basis: argument
- Maurya (2025) argue that For real-world adoption of state-space models such as SSD-Mamba in legal practice it is critical to provide transparent rationales for predictions, and future research should explore passage highlighting, causal attribution and human-interpretable justifications to make their outputs explainable to practitioners. [CLM-0033-013]. — jurisdiction: general; basis: argument
- Hou et al. (2025) argue that Interpretability is critical in legal tasks and has not been adequately explored; LLM-based approaches should provide explanations and logical reasoning during task completion to meet ethical standards, and future research should enhance interpretability so that models offer justifiable explanations alongside accurate legal decisions. [CLM-0034-026]. — jurisdiction: general; basis: argument
- Wang et al. (2026) argue that Legal ambiguity should be treated not as a failure of the system but as an inherent property of legal text that AI alone cannot resolve. A proposed lawyer-centred approach has SMT solvers surface Minimal Correction Subsets, the minimal set of axioms whose acceptance would shift a classification from Neutral to Entailment or Contradiction, and presents them to legal practitioners as structured entry points for resolving ambiguity, positioning the lawyer as the decision-maker for well-scoped interpretive questions and constraining human review to precisely the assumptions that matter rather than requiring exhaustive document-level verification. [CLM-0037-016]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Wang et al. (2026) argue that Progress in faithful legal AI will require not only better models but methods that make the boundary between valid inference and unjustified assumption explicit and actionable, surfacing the minimal assumptions underlying each inference for targeted human review rather than requiring exhaustive verification. [CLM-0037-017]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Medvedeva et al. (2021) argue that Machine learning models that forecast or classify court judgements cannot and should not be used for making decisions in courts, especially where human rights are at stake, nor in other high-stakes situations, because such models cannot deal with new legal developments and interpretations or previously unobserved issues, lack transparency, and raise cybersecurity concerns. [CLM-0045-010]. — jurisdiction: general; basis: argument
- Gridin (2026) argue that Post-hoc explainable AI is not merely insufficient but actively dangerous in high-stakes jurisprudential contexts, because post-hoc explanations bear no guaranteed mathematical relationship to a model's actual computations and generate legally plausible narratives that mask bias; a hallucinated explanation of a black box is more dangerous than no explanation at all, so models that are interpretable by design should be used instead. [CLM-0049-013]. — jurisdiction: general; basis: literature
- Gridin (2026) argue that In high-stakes legal and administrative environments the claimed trade-off between accuracy and interpretability is a false dichotomy: the cost of a black-box error exponentially outweighs marginal gains in computational accuracy, high-stakes decisions rarely require more than 5 to 10 key metrics, and any correlation an LLM discovers that cannot be linearly and transparently proven to a human auditor is legally void and must not influence a human's fate. [CLM-0049-016]. — jurisdiction: general; basis: literature
- Neumann et al. (2026) argue that Prompt versioning and documentation of justified prompt modifications enable meaningful re-evaluation by multiple stakeholders, and evaluations of system-level instructions should be mindful of the prompt stack, including how instructions from multiple stakeholders interact in related or conflicting configurations; effective governance further requires cross-disciplinary collaboration because neither linguistic nor technical expertise alone suffices to specify, implement, or assess instruction-based controls. [CLM-0050-018]. — jurisdiction: general; basis: argument

### Empirical

**CN**

- Hu et al. (2024) report that In a user study, roughly 30% of the Chinese judicial interpretations displayed alongside LLM legal advice served to clarify specific legal terminology or special cases, while for the remaining 70% users were already familiar with their content; users nonetheless asserted that judicial interpretations help them comprehend responses when interpretation is required, make accurate judgments about their situations, and pursue further tailored consultation. [CLM-0029-012]. — jurisdiction: CN [jurisdiction inferred]; basis: dataset_or_experiment

**general**

- Hu et al. (2024) report that Legal terminology embedded in LLM-generated legal advice without sufficient explanation may pose understanding difficulties for users without domain knowledge; special cases lacking a clear definition in legal articles are likewise hard for non-professional users to understand. [CLM-0029-004]. — jurisdiction: general [jurisdiction inferred]; basis: literature

**geographical_proxy:CN**

- Hu et al. (2024) report that In a user study, users reported that the legal article basis of the LLM's response was accurately identified for approximately 95% of queries, that cross-referencing responses with the identified articles let them swiftly determine whether a response was reliable, and that in about 73% of queries the response already contained parts of the legal article but not a full rephrasing, so that the displayed basis gave convenient access to the complete article. [CLM-0029-011]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:US**

- Guha et al. (2023) report that Variation in LLM performance across rule-application tasks is consistent with lawyers' subjective impressions of task difficulty, and LLM explanations fail in identifiable ways: incorrect arithmetic or numerical comparisons, citing the wrong portion of a rule, hallucinating facts not in the fact pattern, giving a bare prediction without explanation, or merely restating the facts and rule without explaining how the outcome is reached. [CLM-0026-019]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that Both the Snippet Model Method and the Iterative Snippet Model Method outperform a document-level training classification method in identifying responsive text snippets (rationales) in responsive documents: on three datasets from real legal matters they identified 50% more responsive documents than the document-level model at the [0.9, 1] snippet-score threshold, and on Datasets A and C they achieved much higher average document-score reductions when the identified rationales were removed (0.7 and 0.67 versus 0.47 on Dataset A; 0.52 and 0.46 versus 0.34 on Dataset C), while on Dataset B all three models achieved similar reductions slightly above 0.3. [CLM-0027-002]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that The accuracy of the document-level model on the document classification task has an important impact on the rationale detection performance of the two snippet model methods: the snippet methods perform much better than the document-level model only when the document model is accurate, because responsive training snippets are identified by the document-level model, so an inaccurate document model yields many misidentified responsive training snippets that degrade the trained snippet model. [CLM-0027-003]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that Snippet models always remove more tokens as identified rationales than document-level models, which means they detect more rationales per document, and this implies that the higher document-score reductions achieved by snippet models are partly caused by the larger number of rationales they identify. [CLM-0027-005]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that It is feasible to build machine learning models that automatically identify rationales without using annotated text snippets for training, and automating the identification of training text snippets without human review could make the application of snippet-trained predictive models a practical approach in legal document review, since snippet-trained models have higher precision than models trained on whole documents but manually annotating training snippets is not generally practical during a review. [CLM-0027-009]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that For the Snippet and Iterative Snippet models, removing snippets with higher snippet scores in most cases produces larger average document-score reductions, and the reductions in the [0.9, 1] snippet-score threshold are much higher than in the other threshold ranges. [CLM-0027-013]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

### Conceptual

**US**

- Lee and Egbert (2025) argue that The core case for modern textualism, that a careful judicial investigation into ordinary communicative content constrains judicial discretion, rests on three pillars, transparency, replicability, and generalizability, and the viability of any tool offering evidence of empirical linguistic fact should be measured by the degree to which it lives up to those three standards. [CLM-0021-003]. — jurisdiction: US [jurisdiction inferred]; basis: literature

**general**

- Mumford et al. (2021) argue that The ascription of factors that correspond to ranges on well-ordered dimensions can be explained in terms of the precedents that establish those ranges, but this kind of explanation does not seem applicable to factor ascriptions that rest on detailed consideration of very particular facts, which may involve analogy or some kind of common-sense ontology. [CLM-0004-006]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that Knowledge-based approaches to legal AI explicitly model legal reasoning and can achieve high faithfulness of representation and explainability of inferences, but they face the knowledge acquisition bottleneck because they require large amounts of legal expertise and modeling effort. [CLM-0014-011]. — jurisdiction: general; basis: literature
- Lee and Egbert (2025) argue that LLM chatbot responses to ordinary-meaning questions are neither a corpus linguistic analysis of natural language use nor a survey of human intuitions about ordinary meaning; at most they present the intuitions of a single artificial entity, functioning as an artificial expert witness that simulates one well-read human, and those artificial intuitions are no more transparent, replicable, or generalizable than the intuitions of an ordinary person or a judge. [CLM-0021-002]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2021) argue that In legal document review a document is considered responsive when any portion of it contains responsive information, which is not always true of other text classification tasks such as topic classification, where the entire document may concern the topic; consequently, locating the responsive text snippets in a responsive document would let attorneys easily evaluate a model's document classification decisions. [CLM-0027-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Neumann et al. (2026) argue that Regulators necessarily interpret natural-language prompts through social, legal and institutional understandings of meaning, obligation and intent, which is not comparable to how language models process instruction text through layers of statistical pattern matching shaped by training and sensitive to phrasing and context; linguistic accessibility therefore risks importing human interpretive assumptions into machine governance. [CLM-0050-010]. — jurisdiction: general; basis: argument

**geographical_proxy:US**

- Mumford et al. (2021) argue that Factor-based explanations of the CATO kind explain well cases in which the dispute turns on the balance of the ascribed factors, but are less satisfactory in cases where the losing party contended that other factors were present, or where the presence of a factor was itself contested; in such cases the explanation the losing party needs is why the claim that other factors were present was rejected, or why a factor was held to apply. [CLM-0004-002]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: argument

### Predictive

**general**

- Mumford et al. (2021) argue that Because there is a considerable conceptual gap between facts and outcomes, which must be bridged by reasoning through factors and issues, but no such gap between facts and factors, machine-learning explanation of the ascription of factors may be more satisfactory than the unsatisfactory standard machine-learning explanations of outcomes; this requires empirical investigation. [CLM-0004-008]. — jurisdiction: general; basis: argument
- Hou et al. (2025) argue that Retrieval-augmented generation may be an important component for the interpretability of LLM-based approaches in the legal domain. [CLM-0034-027]. — jurisdiction: general; basis: literature

### Methodological

**US**

- Lee and Egbert (2025) argue that Existing LLM-based AI tools are not up to the task of the empirical inquiry into ordinary meaning that modern textualism calls for: their outputs are a form of artificial intuition rather than empirical analysis, and they are in no position to produce reliable datapoints on questions such as whether installing an in-ground trampoline is 'landscaping' or whether holding a victim at gunpoint is 'physically restraining' him. [CLM-0021-001]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Lee and Egbert (2025) argue that Corpus data provide the fine-grained detail, how common a given sense of a term is and how often the term is applied to a given referent, that lets a court articulate an operative standard of ordinary meaning and transparently apply it; AI chatbot responses instead give bottom-line conclusions hedged with words like 'can', 'generally' and 'typically' that skate over the embedded questions of the ordinary-meaning standard, delegate the selection of the standard to the AI, and so are not 'datapoints' to be considered alongside other evidence. [CLM-0021-012]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**general**

- Mumford et al. (2021) argue that Explanations of the presence and absence of particular factors could be delivered by extending an issue-based explanation dialogue so that the user may ask WHY? of any factor used to explain an issue and WHY NOT? of any factor not mentioned in the explanation of an issue. [CLM-0004-005]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that Explainable case-outcome prediction can be produced by a hybrid system that separates the two stages of reasoning with cases: factor ascription is performed by a machine-learning natural language processing layer (a Hierarchical BERT model outputting, for each base-level factor, a binary 'ascribed' or 'not ascribed' classification), and the decision is reached by balancing the factors within a pre-determined, non-cyclic Abstract Dialectical Framework derived from expert knowledge. [CLM-0004-009]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that A Hierarchical BERT model is suited to factor ascription because it combines strong classification performance with sentence-level attention weights that could sufficiently express the relevant facts explaining a given factor's ascription or non-ascription. [CLM-0004-011]. — jurisdiction: general; basis: argument
- Hagag et al. (2024) argue that A system for efficiently detecting legal violations in online digital data must scan large amounts of data, isolate relevant information, contextualise the findings by linking them to specific legal grounds, clearly explain potential violations, and identify the affected individuals or entities who may be entitled to legal recourse. [CLM-0012-008]. — jurisdiction: general; basis: argument
- Tan et al. (2024) argue that An interpretable two-step pointwise evaluation methodology, which breaks the reference and candidate summaries into individual points, determines for each point whether the other summary contains a point saying the same thing, and computes recall and precision scores, is suited to the complexities of long-form legal text, and both of its steps can be automated. [CLM-0015-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Blair-Stanek and Van Durme (2025) argue that Because the tested LLMs are proprietary and their APIs and underlying models are developed behind closed doors, experimental results obtained on them cannot be guaranteed to be reproducible in the future. [CLM-0016-016]. — jurisdiction: general; basis: argument
- Khadloya et al. (2025) argue that A judge-facing AI interface should show only passages grounded in visible anchors in the document, never free text, and should offer a disambiguation list or withhold an answer when evidence is insufficient; this grounding and abstention keeps evidence verifiable and auditable and mitigates the bias and overconfidence risks of generative models. [CLM-0019-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Lee and Egbert (2025) argue that The 'transparency' claimed for LLM AIs is only openness about the model selected, the prompt, and the temperature setting, or transparency relative to a dictionary-centric current practice, not the transparency of method and evidentiary basis that renders an inquiry replicable; because LLM AIs rest on black-box algorithms whose operations cannot be understood, evaluated, or modified, they fall short of the transparency and replicability an empirical linguistic tool requires. [CLM-0021-016]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Lee and Egbert (2025) argue that LLM technology could be leveraged within corpus linguistic analysis without sacrificing transparency, replicability, and generalizability: corpus tools could adopt a conversational chatbot interface that asks clarifying questions, reports the exact operational definitions and methods used, and saves search settings so that the same search on the same corpus reproduces the same results; and an AI could be trained to apply a human-developed coding framework to concordance lines, with its accuracy evaluated against human coders and the approach abandoned if satisfactory accuracy is never reached. [CLM-0021-026]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Waldon et al. (2025) argue that Anyone using LLMs to aid legal interpretation should follow five best practices that encourage (though do not guarantee) robustness and reproducibility: (i) use open models and interfaces; (ii) document interaction settings, including model designation, version date, the complete interaction protocol, temperature, maximum output length, prior context and API details; (iii) use multiple models and prompts; (iv) independently verify specific claims in LLM output, because LLMs hallucinate; and (v) recruit domain experts in linguistics and AI. [CLM-0022-011]. — jurisdiction: general; basis: argument
- Guha et al. (2023) argue that Rule-application by an LLM should be evaluated on the generated explanation along two dimensions, correctness (no misstatement of rule, facts or outcome, and no logic or arithmetic error) and analysis (the explanation contains the inferences from the facts that are relevant under the rule), because an explanation that merely restates rule, facts and a correct outcome is error-free yet conclusory and unsatisfactory in legal work. [CLM-0026-008]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2021) argue that Two machine learning methods, the Snippet Model Method and the Iterative Snippet Model Method, can train models that locate responsive text snippets (rationales) within responsive documents in legal document review without using human-annotated training text snippets. The Snippet Model Method applies a document-level text model to score all overlapping text snippets of the training documents, selects high-scoring snippets from responsive documents and randomly selected snippets from non-responsive documents as training data, and trains a snippet-level detection model on them; the Iterative Snippet Model Method repeats this while halving the snippet size at each iteration until a user-defined minimum size is reached. [CLM-0027-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2021) argue that When no labeled text snippets are available, rationale detection models cannot be evaluated with conventional metrics such as precision and recall; they can instead be evaluated by measuring the reduction in a document's classification score when the identified rationales are removed from it, together with the number of responsive documents for which rationales are detected, the model with the higher average score reduction being considered the better rationale identifier. [CLM-0027-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2021) argue that Prediction-based explanations that provide a vector of real-valued weights over features are not ideal for text classification because of the high dimensionality of the feature space; since a document usually belongs to a category because some passages of its text support the classification, a small portion of the document text can instead serve as evidence justifying the classification decision. [CLM-0027-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hu et al. (2024) argue that Visually presenting, for each sentence of an LLM's legal advice, the legal article that serves as its basis (found by similarity matching with a legal-domain fine-tuned embedding model) lets users verify the reliability of the response and trust the advice; a sentence for which no legal basis is found can be viewed as a warning that the sentence may be incorrect. [CLM-0029-005]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Medvedeva et al. (2021) argue that Beyond predicting judgements, it is beneficial to gain insight into how a prediction system reaches its outcome; determining the basis of the classification is important particularly for the classification task, where determining an already known judgement has no practical use in itself. [CLM-0045-014]. — jurisdiction: general; basis: argument

## Disagreements

- Miller (2025) holds: Judge Newsom's reasoning that generative AI's predictive responses, patterned on extensive and varied use of language, could inform ordinary meaning makes intuitive sense and matches the value that any contemporary dictionary could provide. [CLM-0039-002]; Lee and Egbert (2025) holds: Existing LLM-based AI tools are not up to the task of the empirical inquiry into ordinary meaning that modern textualism calls for: their outputs are a form of artificial intuition rather than empirical analysis, and they are in no position to produce reliable datapoints on questions such as whether installing an in-ground trampoline is 'landscaping' or whether holding a victim at gunpoint is 'physically restraining' him. [CLM-0021-001]; note: Miller cites Lee and Egbert (note 64) for the claim that 'existing AI tools are not up to the task' and argues against it that Judge Newsom's reasoning — LLM responses patterned on vast, varied language use can inform ordinary meaning — is sound.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Weighed against the general unfamiliarity of new methods and the subjectivity inherent in LLM construction, the public accessibility of generative AI and the ability to manage some subjectivity through standardized interpretive techniques and judicial communication give reason to think that consulting generative AI offers superior transparency benefits (predictability and fair notice) over dictionaries when appropriate, since dictionaries themselves leave something to be desired on transparency. [CLM-0039-019] is in tension with the claim that Accessibility, low cost, ease of use, and the growing adoption of LLM AIs in the legal profession are not sufficient grounds for adopting them as sources of evidence of ordinary meaning; because their responses are bare opinions rather than empirical facts, the 'good enough' snowball effect is troubling, as judges may be impressed by responses that confirm their own experience or be so drawn in by the seductive appeal of the AI's views as to give them controlling weight subconsciously. [CLM-0021-023] (inferred, medium). Note: One counts the public accessibility of chatbots as a genuine advantage over dictionaries; the other denies that accessibility is a sufficient ground for using them as evidence of meaning.
- The claim that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015] is in tension with the claim that Traditional machine-learning explanations of predicted legal outcomes, such as listing or highlighting the most influential words in the text, are unhelpful and inappropriate in a legal context, because the right to explanation requires an explanation capable of persuading the losing party and withstanding appeal: not an account of how the decision was reached, but of why the decision represents the proper application of the law. [CLM-0004-004] (inferred, medium). Note: One holds that SVM coefficients and attention over facts let the basis of a classification be determined to some extent; the other holds that such word- or feature-level explanations are unhelpful and inappropriate in a legal context.
- The claim that Post-hoc explainable AI is not merely insufficient but actively dangerous in high-stakes jurisprudential contexts, because post-hoc explanations bear no guaranteed mathematical relationship to a model's actual computations and generate legally plausible narratives that mask bias; a hallucinated explanation of a black box is more dangerous than no explanation at all, so models that are interpretable by design should be used instead. [CLM-0049-013] is in tension with the claim that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015] (inferred, low). Note: One deems post-hoc explanation of black-box outputs actively dangerous in legal contexts; the other finds coefficients and attention adequate to determine a classifier's basis to some extent.

## Distribution

Sources with claims on this concept: 21; claims: 83.

**By contribution type**

| value | sources |
|---|---|
| technical | 15 |
| empirical_quantitative | 13 |
| theoretical | 10 |
| normative | 8 |
| doctrinal | 4 |
| empirical_qualitative | 4 |
| survey | 4 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 9 |
| US | 7 |
| CoE | 2 |
| IN | 2 |
| CN | 1 |
| EU | 1 |
| GB | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 19 |
| US | 5 |
| geographical_proxy:US | 4 |
| EU | 2 |
| CN | 1 |
| GB | 1 |
| geographical_proxy:CN | 1 |
| geographical_proxy:NL | 1 |

**By year**

| value | sources |
|---|---|
| 2025 | 7 |
| 2021 | 4 |
| 2024 | 4 |
| 2026 | 4 |
| 2022 | 1 |
| 2023 | 1 |

## What the sources do not address


Explicit questions occurring verbatim in claim or premise text and answered by no claim on this concept:
- "Explanations of the presence and absence of particular factors could be delivered by extending an issue-based explanation dialogue so that the user may ask WHY?" — raised in [CLM-0004-005] [ABS-1406] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- "of any factor used to explain an issue and WHY NOT?" — raised in [CLM-0004-005] [ABS-1407] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

The explicit questions listed above are candidates for the register (query-graph skill); no hypothesis has been entered yet.
