---
id: "CPT-outcome-prediction"
label: "Outcome prediction"
status: "anchor"
concept_type: "legal_task"
definition: "Predicting the outcome, verdict, or decision of a legal case or proceeding."
aliases: []
broader: []
sources: ["SRC-0004", "SRC-0006", "SRC-0007", "SRC-0010", "SRC-0013", "SRC-0014", "SRC-0016", "SRC-0034", "SRC-0035", "SRC-0036", "SRC-0045", "SRC-0048"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Outcome prediction

_Status: anchor; family: legal_task._

## Definition

Predicting the outcome, verdict, or decision of a legal case or proceeding.

Conceptual claims on this concept, each with its source:
- Xie et al. (2024): The terminology 'prediction' rather than 'classification' is appropriate for a case outcome task when explicit information about case outcomes is deliberately excluded from the input and only descriptions of facts and claims are kept, so that outcomes are predicted solely from facts and claims. [CLM-0013-025]
- Medvedeva et al. (2021): Forecasting judgements and classifying judgements are distinct tasks that should be kept apart. Forecasting requires textual data about the facts of a case that was created before the decision was reached, so that the input is not influenced by the outcome; classification uses textual data created after the decision was reached. [CLM-0045-001]

## Claims about the concept

### Descriptive

**CoE**

- Mumford et al. (2023) state that Article 6 ECHR (the right to a fair trial) is often selected for training and testing AI legal-prediction systems, largely because of the procedural nature of the article and the relative abundance of data: more Article 6 cases are available on HUDOC than for any other Convention article. [CLM-0010-004]. — jurisdiction: CoE; basis: argument
- Medvedeva et al. (2021) state that Communicated cases of the European Court of Human Rights, which contain a summary of the facts and the Court's questions to the respondent government and are often published years before the case is judged, provide a unique opportunity to forecast the judgements of pending applications; the questions often reflect the Court's legal characterisation of the complaint. [CLM-0045-008]. — jurisdiction: CoE; basis: argument; positive form: general_rule
- Medvedeva et al. (2021) state that A publicly released dataset containing all communicated cases, admissibility decisions and final judgements of the European Court of Human Rights published between 1960 and 2020, with raw text, metadata and pre-processed sections, and with case numbers linked across the stages of proceedings, is the first benchmark dataset for forecasting judgements of pending applications. [CLM-0045-013]. — jurisdiction: CoE; basis: dataset_or_experiment

**CoE, CN, US, FR, PH, TR, TH, GB, DE, CH**

- Chalkidis et al. (2021) state that Legal judgment prediction, a core task of legal NLP, has been pursued in at least three lines of work — predicting violations of human rights in cases of the European Court of Human Rights, predicting relevant law articles, criminal charges and penalty terms in Chinese criminal cases, and predicting outcomes of cases of the Supreme Court of the United States — and the same or similar task has also been studied on court cases of many other jurisdictions, including France, the Philippines, Turkey, Thailand, the United Kingdom, Germany and Switzerland. [CLM-0048-010]. — jurisdiction: CoE, CN, US, FR, PH, TR, TH, GB, DE, CH (cumulative); basis: literature

**GB**

- Xie et al. (2024) state that AI-based prediction of UK court decisions is under-explored: the only notable legal judgment prediction paper on UK law predates the emergence of large language models and is limited to the binary task of whether UK Supreme Court judges allow or dismiss an appeal. [CLM-0013-001]. — jurisdiction: GB; basis: literature
- Xie et al. (2024) state that The CLC-UKET dataset comprises two components built from the UK Employment Tribunal subset of the Cambridge Law Corpus: CLC-UKET anno, 19,090 UKET judgments heard between 2011 and 2023 with metadata and legal annotations, and CLC-UKET pred, 14,582 cases with fact and claim statements and general outcome labels designed for a multi-class case outcome prediction task; the dataset is to be made available via the Cambridge Law Corpus website. [CLM-0013-004]. — jurisdiction: GB; basis: dataset_or_experiment

**general**

- Mumford et al. (2023) state that No prior work in the AI and Law literature on classifying the outcome of a legal case from a description of its facts has asked how well humans perform that same task. [CLM-0010-001]. — jurisdiction: general; basis: literature
- Xie et al. (2024) state that Knowing the likely outcome of a court procedure improves access to justice and facilitates amicable dispute resolution. [CLM-0013-002]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- T.Y.S.S. et al. (2024) state that Contemporary legal NLP increasingly applies models that statistically classify legal conclusions from text with little or no explicit domain representation; while conceptually simpler, these approaches often fall short in providing usable justifications that connect to appropriate legal concepts, at the cost of interpretability. [CLM-0014-002]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that The working assumption of legal outcome classification research that better benchmark performance means models encode more legal knowledge extractable as explanations has not been fulfilled: rationale-alignment studies, low expert agreement, reliance on shallow predictors, and the limited utility of saliency maps for humans all cast doubt on the assumption that, at least for classifier models, benchmark performance correlates with better explanations. [CLM-0014-004]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that Early large language models evaluated on case outcome classification benchmarks score relatively low on quantitative metrics, which stands in contrast to their scores on some bar exams. [CLM-0014-015]. — jurisdiction: general; basis: literature
- Medvedeva et al. (2021) state that Many current studies that claim to 'predict judicial decisions' are in fact classifying previously made judgements rather than forecasting future ones, because their input data was created after the decision was reached. [CLM-0045-002]. — jurisdiction: general; basis: literature
- Medvedeva et al. (2021) state that Because courts provide little access to documents that exist before a judgement is made, forecasting future judgements is impossible for many online available datasets, and for this reason the large majority of machine learning systems for legal data classify court judgements rather than forecast them. [CLM-0045-012]. — jurisdiction: general; basis: argument
- Medvedeva et al. (2021) state that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015]. — jurisdiction: general; basis: argument
- Medvedeva et al. (2021) state that Only very few studies focus on forecasting judgements, and most of them report lower performance than studies on judgement classification, which may be indicative of the higher difficulty of forecasting. [CLM-0045-017]. — jurisdiction: general; basis: literature

**undetermined**

- Mumford et al. (2023) state that Although true expert knowledge could lead to substantial improvements in verdict classification over student performance, social-science literature suggests that judges themselves do not reach sound verdicts as a function of the facts alone. [CLM-0010-017]. — jurisdiction: undetermined; basis: literature; positive form: general_rule

### Interpretive

**CoE**

- Medvedeva et al. (2021) read Outcome prediction as follows: Applications to the European Court of Human Rights found inadmissible on the merits can, from a legal point of view, be characterised as clearer 'non-violation' cases, similar to cases judged as showing no violation, because the Court has decided similar applications many times before and they do not merit a full judgement. [CLM-0045-018]. — jurisdiction: CoE; basis: argument

**GB**

- Xie et al. (2024) read Outcome prediction as follows: Whether precision or recall provides better guidance from an outcome predictor depends on the specific situation of a potential claimant; since the UK Employment Tribunal currently charges no fees and claimants can represent themselves, recall may be the preferable score if the claim matters to the potential claimant. [CLM-0013-015]. — jurisdiction: GB; basis: argument
- Xie et al. (2024) read Outcome prediction as follows: The possibility of multi-step UK Employment Tribunal proceedings, in which a judgment may decide only a preliminary issue (such as disability or employee status) rather than finally resolving the claim, increases the complexity of outcome prediction and has likely had a negative effect on the scores of both models and human predictors. [CLM-0013-018]. — jurisdiction: GB; basis: argument
- Xie et al. (2024) read Outcome prediction as follows: Where the UK Employment Tribunal renders a procedural decision instead of deciding the substance of a claim (labelled 'other'), both models and human annotators may predict a substantive outcome instead, a complexity that may have contributed to low evaluation scores for the 'claimant partly wins' and 'other' categories. [CLM-0013-019]. — jurisdiction: GB; basis: argument
- Xie et al. (2024) read Outcome prediction as follows: Because employment and procedural law evolved over the 2011-2023 period covered by the dataset, predicting a case outcome without knowing the precise decision date may lead to mistakes; models and human predictors did not have direct access to the decision date, though they may have inferred it from the case identifier. [CLM-0013-022]. — jurisdiction: GB; basis: argument

**geographical_proxy:GB**

- Xie et al. (2024) read Outcome prediction as follows: Facts automatically extracted from tribunal judgments may not include all the elements needed to form an outcome prediction (for example the parties' behaviour relevant to costs, a respondent's failure to challenge the claim, or procedural facts such as late submission), leading to incorrect predictions by both models and human experts. [CLM-0013-020]. — jurisdiction: geographical_proxy:GB; basis: argument

### Normative

**general**

- Mumford et al. (2021) argue that Explanations of legal decisions must go beyond the factors present in a case and the preferences between them: they must also explain the ascription and non-ascription of the factors themselves, that is, why particular factors are held to be present or absent. [CLM-0004-001]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that Traditional machine-learning explanations of predicted legal outcomes, such as listing or highlighting the most influential words in the text, are unhelpful and inappropriate in a legal context, because the right to explanation requires an explanation capable of persuading the losing party and withstanding appeal: not an account of how the decision was reached, but of why the decision represents the proper application of the law. [CLM-0004-004]. — jurisdiction: general [jurisdiction inferred]; basis: literature Same proposition asserted by: T.Y.S.S. et al. (2024) [CLM-0014-020].
- T.Y.S.S. et al. (2024) argue that Outcome prediction systems in the legal domain should ideally rely on information available before proceedings start and legal conclusions are determined, such as the parties' argumentative memoranda, rather than on fact statements taken from judgments. [CLM-0014-006]. — jurisdiction: general; basis: literature
- Hou et al. (2025) argue that Existing legal tasks have been simplified, for example by filtering out samples with multiple charges or multiple defendants in legal judgement prediction; since such scenarios exist in the real world, ignoring them limits the practical application of legal LLMs and LLM-based frameworks, and tasks with complex situations need to be fully explored. [CLM-0034-029]. — jurisdiction: general; basis: literature
- Medvedeva et al. (2021) argue that Classification performance on already decided judgements should not be used as an indication of how well judicial outcome prediction systems are able to forecast future judgements of a court. [CLM-0045-006]. — jurisdiction: general; basis: dataset_or_experiment
- Medvedeva et al. (2021) argue that Machine learning models that forecast or classify court judgements cannot and should not be used for making decisions in courts, especially where human rights are at stake, nor in other high-stakes situations, because such models cannot deal with new legal developments and interpretations or previously unobserved issues, lack transparency, and raise cybersecurity concerns. [CLM-0045-010]. — jurisdiction: general; basis: argument

**geographical_proxy:GB**

- Xie et al. (2024) argue that The reported evaluation scores for the UK Employment Tribunal outcome prediction task are baseline results that both models (for example through retrieval-augmented generation or chain-of-thought) and human experts (through more time and research) could improve upon, so caution should be applied when drawing conclusions for legal practice from them. [CLM-0013-017]. — jurisdiction: geographical_proxy:GB; basis: argument

### Empirical

**general**

- Li et al. (2022) report that Prefix domain adaptation — pre-training a deep prefix prompt with the masked language modelling task on a large unsupervised domain-specific corpus and then using that prompt to initialise prefix tuning for downstream tasks — matches or exceeds the few-shot performance of LEGAL-BERT and related techniques on legal classification tasks while tuning only approximately 0.1% of model parameters. [CLM-0006-001]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:CoE**

- Li et al. (2022) report that On the ECHR binary violation prediction task, whose train and test splits have different distributions, prefix-tuning-based approaches perform better than full finetuning in very-low-data settings (4 to 16 examples), which suggests that prefix tuning approaches are more robust to changes in distribution and possibly to noise. [CLM-0006-007]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Li et al. (2022) report that Finetuned BERT with truncation to 500 tokens performs much better on the ECHR violation prediction task (macro F1 of 66.5) than reported by Chalkidis et al. (2019), who report an F1 of 17, worse than random guessing; the underperformance reported there could be caused by a mistake in their training process. [CLM-0006-008]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Overall mean human performance at classifying the verdict (violation or no violation) of ECtHR Article 6 cases from the facts sections of the judgments closely resembles that of a random classifier, with an approximate mean accuracy of 0.5 and an MCC score of about 0.0. [CLM-0010-006]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Neither the level of legal domain experience of participants (computer science students, law students without ECHR study, law students with ECHR study) nor access to an ANGELIC domain model of Article 6 ECHR produced a statistically significant increase in verdict-classification performance; the best-performing group was the moderate-experience law students. [CLM-0010-007]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that The absence of any effect of legal domain experience on human verdict-classification performance suggests a limited effectiveness of university education for training law students to reconcile legal case descriptions into case outcomes. [CLM-0010-008]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Human participants achieved statistically significantly higher verdict-classification performance in the few-shot setting (after seeing eight practice cases with actual verdicts) than in the zero-shot setting, but mean accuracy and MCC scores were very low in both settings and there was no correlation between an individual's zero-shot and few-shot performance. [CLM-0010-009]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Self-reported participant confidence is not a strong predictor of human verdict-classification performance on ECtHR Article 6 cases: the correlation is slightly positive but not statistically significant. [CLM-0010-010]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Human verdict-classification performance after reading only the circumstances of an ECtHR Article 6 case and after additionally reading the relevant legal framework are strongly positively correlated, and there is no statistically significant difference in performance between the two conditions. [CLM-0010-011]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Participant productivity (number of classifications made in the eight hours of classification work) is statistically significantly and positively correlated with verdict-classification performance. [CLM-0010-012]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Access to an ANGELIC domain model (ADM) of Article 6 ECHR produced a statistically significant increase in participant productivity at the verdict-classification task, even though it did not significantly improve classification performance. [CLM-0010-013]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Descriptions of the facts of a case alone are insufficient for accurate legal verdict classification, independently of the classifier's legal background. [CLM-0010-014]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that Forecasting judgements of the European Court of Human Rights from communicated cases is a much harder task than classifying final judgements from the facts section of the judgement: on identical sets of cases, forecasting macro F-scores (about 0.57 to 0.67) are substantially lower than classification macro F-scores (about 0.75 to 0.92) for all test years except 2020. [CLM-0045-003]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that Although H-BERT and LEGAL-BERT generally outperform a linear SVM when classifying final judgements of the European Court of Human Rights, they do not improve over the SVM when forecasting judgements from communicated cases. [CLM-0045-004]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that The higher performance of judgement classification over forecasting is not explained by the larger amount of text in final judgements; the results suggest instead that the facts in final judgements are formulated in a way that is affected by the final ruling. [CLM-0045-005]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that For the 2020 test year, classification of European Court of Human Rights judgements performed much lower than usual, so that forecasting from communicated cases outperformed classification; no explanation for this pattern was found in case length, vocabulary, State distribution, court policy or case format, and the 2020 results are treated as an anomaly. [CLM-0045-007]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Medvedeva et al. (2021) report that When forecasting European Court of Human Rights judgements from communicated cases, all models perform better on the 'violation' label than on the 'non-violation' label, whereas the gap between the two labels is considerably smaller for classification from final judgements; this reflects that a communicated case summarises only the applicant's side of the events and may be subjective and incomplete. [CLM-0045-009]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment

**geographical_proxy:CoE, geographical_proxy:US**

- Chalkidis et al. (2021) report that On the LexGLUE datasets with long documents (ECtHR Task A, ECtHR Task B, SCOTUS), a hierarchical variant of BERT that encodes each paragraph independently and then contextualises the paragraph representations with a second-level Transformer encoder clearly outperforms standard BERT fed with documents truncated to 512 tokens (+12.2%, +10.6% and +3.5% respectively); the gains are lower in SCOTUS, a topic classification task where long-range reasoning is not needed, than in the ECtHR tasks, where multiple distant facts need to be combined. [CLM-0048-005]. — jurisdiction: geographical_proxy:CoE, geographical_proxy:US (cumulative); basis: dataset_or_experiment

**geographical_proxy:GB**

- Xie et al. (2024) report that Fine-tuned transformer models outperform zero-shot and few-shot large language models on the UK Employment Tribunal four-class case outcome prediction task, with fine-tuned T5 as the best-performing model, and all tested models significantly outperform a random-guess baseline. [CLM-0013-005]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that Human legal experts predicting UK Employment Tribunal case outcomes from facts and claims substantially outperform all baseline models in a baseline setting, with a noticeable gap between machine and human performance. [CLM-0013-006]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that Including few-shot examples that share jurisdiction codes with the target case improves the outcome-prediction F-score of large language models more effectively than randomly sampled examples, showing that integrating task-related information into few-shot prompts enhances prediction performance. [CLM-0013-008]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that Simply increasing the number of few-shot examples provided to GPT-based models is not sufficient to significantly boost case outcome prediction performance. [CLM-0013-009]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that GPT-4 generally outperforms GPT-3.5 on UK Employment Tribunal case outcome prediction, but the margin of outperformance is rather small. [CLM-0013-010]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that Cases that human legal experts flag as hard to predict from the given facts and claims are also more difficult for prediction models: both human and model performance is significantly worse on the low-confidence subset of test cases, so human difficulty assessments align well with empirical results. [CLM-0013-011]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that Distinguishing cases where the claimant wins outright from cases where the claimant partly wins makes case outcome prediction inherently more challenging; when the two labels are aggregated, all baseline models improve consistently across all metrics and human annotators predict outcomes effectively. [CLM-0013-012]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that Most baseline prediction models show high recall and relatively low precision when predicting 'claimant wins' and, conversely, high precision and relatively low recall when predicting 'claimant loses', reflecting distinct precision-recall trade-offs; legal experts show the same pattern. [CLM-0013-013]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that The outcome labels 'claimant partly wins' and 'other' consistently receive lower evaluation scores across all models and human predictors, which may be attributed to the inherent difficulty of identifying cases in these categories compounded by the imbalanced distribution of cases across the four categories. [CLM-0013-014]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that The F-score of GPT-4 with two jurisdiction-matched few-shot examples for the 'claimant partly wins' label outperforms the human predictors, which may indicate an ability of the large language model to navigate more complex litigation involving multiple claims or multiple parties. [CLM-0013-016]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that Two specialised legal experts independently predicting UK Employment Tribunal case outcomes from facts and claims reach only moderate agreement (Cohen's Kappa 0.421), highlighting the inherent complexity of the UKET outcome prediction task. [CLM-0013-028]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

**geographical_proxy:IN**

- Malik et al. (2022) report that Feeding a judgment-prediction model only the sentences carrying gold ratio-of-decision and ruling-by-present-court rhetorical roles improves judgment prediction F1 over using the last 512 tokens of the document (0.58 versus 0.55, statistically significant), whereas using predicted rhetorical roles yields performance comparable to the baseline; improving rhetorical role prediction for these two roles would therefore enhance judgment prediction. [CLM-0007-017]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

**geographical_proxy:UA**

- Ovcharov (2026) report that On Ukrainian court-decision tasks, the five UA-Legal-Bench tasks form a clear difficulty gradient for large language models: case-type classification is nearly solved (all frontier models exceed 96% zero-shot accuracy), judgment form classification is substantially harder (74-84% zero-shot), cause category prediction sits between (44-51% accuracy), and case-outcome prediction from masked facts is the hardest task (frontier models reach only 23-41% macro-F1 zero-shot). [CLM-0035-004]. — jurisdiction: geographical_proxy:UA; basis: dataset_or_experiment

**geographical_proxy:UA, geographical_proxy:FR, geographical_proxy:NL, geographical_proxy:PL, geographical_proxy:CZ, geographical_proxy:LT**

- Ovcharov (2026) report that The difficulty ordering of legal tasks for LLMs — court-type classification easiest, then judgment-form classification, then cause-category prediction, with case-outcome prediction hardest — is stable across six civil-law jurisdictions with different languages and label sets, which suggests that the cognitive demands of each task type are inherent to the task structure rather than artifacts of a particular language. [CLM-0036-012]. — jurisdiction: geographical_proxy:UA, geographical_proxy:FR, geographical_proxy:NL, geographical_proxy:PL, geographical_proxy:CZ, geographical_proxy:LT (cumulative); basis: dataset_or_experiment

**geographical_proxy:US**

- Blair-Stanek and Van Durme (2025) report that Measured against the party that actually prevailed in the court decision from which each question was distilled, gpt-4o and claude-3.5 perform slightly better than chance with statistical significance, while gemini-1.5 performs worse than chance. [CLM-0016-011]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek and Van Durme (2025) report that The three LLMs agree with each other on which party should prevail far more often than any of them agrees with the actual court decision; possible explanations are that the summarisation of each case into five paragraphs biases the question in one direction, whereas the court had full briefing and the full record, or that similar legal training corpora and training methods make the models tend to answer in the same way. [CLM-0016-012]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Conceptual

**general**

- Xie et al. (2024) argue that The terminology 'prediction' rather than 'classification' is appropriate for a case outcome task when explicit information about case outcomes is deliberately excluded from the input and only descriptions of facts and claims are kept, so that outcomes are predicted solely from facts and claims. [CLM-0013-025]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Medvedeva et al. (2021) argue that Forecasting judgements and classifying judgements are distinct tasks that should be kept apart. Forecasting requires textual data about the facts of a case that was created before the decision was reached, so that the input is not influenced by the outcome; classification uses textual data created after the decision was reached. [CLM-0045-001]. — jurisdiction: general; basis: argument

### Predictive

**CoE**

- Medvedeva et al. (2021) argue that Forecasting judgements from communicated cases does not allow forecasting for every future case, since not all applications are communicated to the State; forecasting from other data available before the judgement may likely be even harder, because the uniform documents the Court creates for communicated cases are likely beneficial. [CLM-0045-019]. — jurisdiction: CoE; basis: argument

**general**

- Mumford et al. (2021) argue that Because there is a considerable conceptual gap between facts and outcomes, which must be bridged by reasoning through factors and issues, but no such gap between facts and factors, machine-learning explanation of the ascription of factors may be more satisfactory than the unsatisfactory standard machine-learning explanations of outcomes; this requires empirical investigation. [CLM-0004-008]. — jurisdiction: general; basis: argument

### Methodological

**CoE**

- Medvedeva et al. (2021) argue that Predicting the list of articles of the European Convention on Human Rights potentially violated in a case has no clear practical use, because the articles involved are known as soon as the application is submitted; a realistic scenario for the European Court of Human Rights would only involve deciding whether or not a given article was violated. [CLM-0045-016]. — jurisdiction: CoE; basis: argument

**GB**

- Xie et al. (2024) argue that Framing the outcome prediction task from the perspective of the claimant (claimant wins, loses, partly wins, other) makes sense because it is first for the claimant to decide whether to apply for a tribunal decision, after which the respondent decides how to react; but models and human predictors achieve different scores depending on whether 'wins' or 'loses' is predicted. [CLM-0013-026]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

**general**

- Mumford et al. (2021) argue that The key role for machine learning in reasoning with legal cases is not the prediction of outcomes but the identification of the factors present in a case. [CLM-0004-007]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that Explainable case-outcome prediction can be produced by a hybrid system that separates the two stages of reasoning with cases: factor ascription is performed by a machine-learning natural language processing layer (a Hierarchical BERT model outputting, for each base-level factor, a binary 'ascribed' or 'not ascribed' classification), and the decision is reached by balancing the factors within a pre-determined, non-cyclic Abstract Dialectical Framework derived from expert knowledge. [CLM-0004-009]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that If domain expertise is of paramount importance in establishing an appropriate Abstract Dialectical Framework, data-driven approaches are less effective at the level of factors and above; accordingly, in a hybrid ML-ADF system only the architecture of the NLP layer should be adjusted by learning, while the expert-derived ADF layer remains unchanged from its initial state. [CLM-0004-010]. — jurisdiction: general; basis: literature
- Mumford et al. (2021) argue that A Hierarchical BERT model is suited to factor ascription because it combines strong classification performance with sentence-level attention weights that could sufficiently express the relevant facts explaining a given factor's ascription or non-ascription. [CLM-0004-011]. — jurisdiction: general; basis: argument
- Malik et al. (2022) argue that Legal documents are long, unstructured, noisy and written in a specialised lexicon, which makes conventional text-processing techniques and pre-trained neural models ineffective on them; a legal document processing system would benefit substantially if documents were segmented into coherent information units (rhetorical roles), which could aid summarisation, legal judgment prediction, information extraction and prior case retrieval. [CLM-0007-001]. — jurisdiction: general; basis: argument
- Mumford et al. (2023) argue that Evaluating the performance of AI systems for legal case verdict classification requires a human benchmark, established across participants with varying levels of legal domain experience. [CLM-0010-002]. — jurisdiction: general; basis: argument Same proposition asserted by: Xie et al. (2024) [CLM-0013-007].
- Mumford et al. (2023) argue that Using post-decision material (the outcome-categorisation task) rather than pre-decision material for a human verdict-classification study allows categorising inaccuracies to be attributed more confidently to the participants' judgment than to gaps in the information provided. [CLM-0010-003]. — jurisdiction: general; basis: argument
- Mumford et al. (2023) argue that To enhance the accuracy of legal verdict classification, future research should incorporate explicit references to other cases (particularly leading cases that frequently form the reference basis for judgements) and temporal context, so as to establish references to key precedents, and advanced information/document retrieval NLP techniques are well suited to implementing these measures within AI classification systems. [CLM-0010-016]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that Classification benchmarks for legal outcome prediction risk decoupling a sense of technical progress from support of realistic tasks such as legal argumentation, because they reduce case outcomes to a highly reductive representation (typically a binary target based on the majority opinion) although outcomes are highly contextual in time, procedure and socio-legal purpose and judges on the same bench frequently reason differently. [CLM-0014-003]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that Conveniently available legal NLP datasets come with structural assumptions, noise and biases that must be accounted for: fact descriptions taken from judgments are often highly selective summaries tailored to the decision that can introduce confounding effects, and datasets are subject to selection bias regarding which cases reach which court, which are published, and which are settled before or during trial. [CLM-0014-005]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) argue that One intuitive way to combine legal knowledge and machine learning in NLP is to ascribe factors from case texts by text processing and then proceed with formalized legal inference; rather than training factor classifiers against an exhaustively defined factor list, the more likely scenario is that generative models are prompted with specific facts to subsume them under a factor pattern description. [CLM-0014-019]. — jurisdiction: general; basis: literature
- Medvedeva et al. (2021) argue that Removing named entities such as locations from the text, while understandable when building a decision-making system, is not appropriate for judgement forecasting or classification: locations may offer relevant information about a case, so such models benefit from keeping this information, which is also known to judges. [CLM-0045-011]. — jurisdiction: general; basis: argument
- Medvedeva et al. (2021) argue that Beyond predicting judgements, it is beneficial to gain insight into how a prediction system reaches its outcome; determining the basis of the classification is important particularly for the classification task, where determining an already known judgement has no practical use in itself. [CLM-0045-014]. — jurisdiction: general; basis: argument

**geographical_proxy:CoE**

- Mumford et al. (2023) argue that Because the verdict distribution in a dataset of ECtHR Article 6 cases is not balanced (60.0% violations in the reviewed cases, and even more skewed towards violations in the court's real decisions), the Matthews correlation coefficient is a better indicator of classification performance than accuracy. [CLM-0010-005]. — jurisdiction: geographical_proxy:CoE; basis: argument
- Mumford et al. (2023) argue that The near-random human performance at classifying case outcomes from fact descriptions raises questions about the feasibility of classifying legal outcomes solely from descriptions of facts, the approach that has been dominant in prior machine-learning work on legal judgement prediction. [CLM-0010-015]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment

**geographical_proxy:GB**

- Xie et al. (2024) argue that Using facts and claims extracted from judges' written decisions as the input for outcome prediction could introduce information biases at the input stage, because judges know the result when writing and their texts may inherently contain biased information (such as sentiment words revealing their inclinations) that models and legal experts may pick up. [CLM-0013-021]. — jurisdiction: geographical_proxy:GB; basis: argument

**geographical_proxy:UA**

- Ovcharov (2026) argue that Accuracy is a dangerously misleading metric on imbalanced legal classification tasks, and imbalanced legal benchmarks require class-aware metrics such as macro-F1: on Ukrainian case-outcome prediction (61% majority class) the model with the highest accuracy is a majority-class predictor with the lowest macro-F1 among frontier models, while macro-F1 identifies the model that genuinely distinguishes outcome classes. [CLM-0035-007]. — jurisdiction: geographical_proxy:UA; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that The near-random human performance at classifying case outcomes from fact descriptions raises questions about the feasibility of classifying legal outcomes solely from descriptions of facts, the approach that has been dominant in prior machine-learning work on legal judgement prediction. [CLM-0010-015] is in tension with the claim that Finetuned BERT with truncation to 500 tokens performs much better on the ECHR violation prediction task (macro F1 of 66.5) than reported by Chalkidis et al. (2019), who report an F1 of 17, worse than random guessing; the underperformance reported there could be caused by a mistake in their training process. [CLM-0006-008] (inferred, medium). Note: One questions the feasibility of classifying legal outcomes from fact descriptions alone after humans performed at chance; the other reports a fine-tuned BERT reaching macro F1 66.5 on ECHR violation prediction from case facts — above chance, though on a different task formulation.
- The claim that Human legal experts predicting UK Employment Tribunal case outcomes from facts and claims substantially outperform all baseline models in a baseline setting, with a noticeable gap between machine and human performance. [CLM-0013-006] is in tension with the claim that Overall mean human performance at classifying the verdict (violation or no violation) of ECtHR Article 6 cases from the facts sections of the judgments closely resembles that of a random classifier, with an approximate mean accuracy of 0.5 and an MCC score of about 0.0. [CLM-0010-006] (inferred, medium). Note: One finds human legal experts substantially outperforming all models at predicting tribunal outcomes from facts; the other finds human performance at classifying court outcomes from facts no better than random — different courts, tasks and participant expertise.
- The claim that Fine-tuned transformer models outperform zero-shot and few-shot large language models on the UK Employment Tribunal four-class case outcome prediction task, with fine-tuned T5 as the best-performing model, and all tested models significantly outperform a random-guess baseline. [CLM-0013-005] is in tension with the claim that Straightforward prompting of GPT-3 (text-davinci-003) on the SARA statutory-reasoning benchmark yields accuracy better than the previous best published, BERT-based results, with far less human input: the best setting (zero-shot with the statute included) reaches 71% aggregate accuracy on the 100 entailment test cases, significantly better than the BERT-based state of the art (p approximately 0.038) and the majority baseline. [CLM-0008-002] (inferred, medium). Note: One finds fine-tuned transformers beating prompted GPT models on outcome prediction; the other finds prompted GPT-3 beating the fine-tuned BERT-based state of the art on statutory reasoning — opposite rankings on different tasks.
- The claim that Using facts and claims extracted from judges' written decisions as the input for outcome prediction could introduce information biases at the input stage, because judges know the result when writing and their texts may inherently contain biased information (such as sentiment words revealing their inclinations) that models and legal experts may pick up. [CLM-0013-021] is in tension with the claim that Using post-decision material (the outcome-categorisation task) rather than pre-decision material for a human verdict-classification study allows categorising inaccuracies to be attributed more confidently to the participants' judgment than to gaps in the information provided. [CLM-0010-003] (inferred, medium). Note: One warns that facts extracted from judges' post-decision texts may carry information bias; the other defends post-decision material as the input that lets inaccuracies be attributed to the predictor's judgment.
- The claim that Outcome prediction systems in the legal domain should ideally rely on information available before proceedings start and legal conclusions are determined, such as the parties' argumentative memoranda, rather than on fact statements taken from judgments. [CLM-0014-006] is in tension with the claim that Using post-decision material (the outcome-categorisation task) rather than pre-decision material for a human verdict-classification study allows categorising inaccuracies to be attributed more confidently to the participants' judgment than to gaps in the information provided. [CLM-0010-003] (inferred, medium). Note: One says outcome prediction should rely on information available before proceedings; the other defends post-decision material as the appropriate input for a human verdict-classification study.
- The claim that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015] is in tension with the claim that Traditional machine-learning explanations of predicted legal outcomes, such as listing or highlighting the most influential words in the text, are unhelpful and inappropriate in a legal context, because the right to explanation requires an explanation capable of persuading the losing party and withstanding appeal: not an account of how the decision was reached, but of why the decision represents the proper application of the law. [CLM-0004-004] (inferred, medium). Note: One holds that SVM coefficients and attention over facts let the basis of a classification be determined to some extent; the other holds that such word- or feature-level explanations are unhelpful and inappropriate in a legal context.
- The claim that Removing named entities such as locations from the text, while understandable when building a decision-making system, is not appropriate for judgement forecasting or classification: locations may offer relevant information about a case, so such models benefit from keeping this information, which is also known to judges. [CLM-0045-011] is in tension with the claim that Masking all company names, including defendant and plaintiff names, in the LegalLens datasets was necessary to prevent bias and ensure broader applicability, because models were found to be prone to overfitting when the masking was not applied. [CLM-0012-011] (inferred, low). Note: One argues that removing named entities such as locations is inappropriate for forecasting because they are informative; the other masks company names to prevent overfitting — different tasks and rationales.
- The claim that Post-hoc explainable AI is not merely insufficient but actively dangerous in high-stakes jurisprudential contexts, because post-hoc explanations bear no guaranteed mathematical relationship to a model's actual computations and generate legally plausible narratives that mask bias; a hallucinated explanation of a black box is more dangerous than no explanation at all, so models that are interpretable by design should be used instead. [CLM-0049-013] is in tension with the claim that Linear SVC (through inspection of coefficients) and H-BERT (through attention over facts) allow the basis of a classification to be determined to some extent, whereas LEGAL-BERT by itself cannot be used for this: although it often produces very high scores for final judgement classification, one cannot see within the black box. [CLM-0045-015] (inferred, low). Note: One deems post-hoc explanation of black-box outputs actively dangerous in legal contexts; the other finds coefficients and attention adequate to determine a classifier's basis to some extent.

## Distribution

Sources with claims on this concept: 12; claims: 88.

**By contribution type**

| value | sources |
|---|---|
| technical | 10 |
| empirical_quantitative | 9 |
| theoretical | 4 |
| normative | 2 |
| survey | 2 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 8 |
| CoE | 1 |
| GB | 1 |
| IN | 1 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 8 |
| geographical_proxy:CoE | 4 |
| CoE | 3 |
| GB | 2 |
| geographical_proxy:UA | 2 |
| geographical_proxy:US | 2 |
| CH | 1 |
| CN | 1 |
| DE | 1 |
| FR | 1 |
| PH | 1 |
| TH | 1 |
| TR | 1 |
| US | 1 |
| geographical_proxy:CZ | 1 |
| geographical_proxy:FR | 1 |
| geographical_proxy:GB | 1 |
| geographical_proxy:IN | 1 |
| geographical_proxy:LT | 1 |
| geographical_proxy:NL | 1 |
| geographical_proxy:PL | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2021 | 3 |
| 2022 | 2 |
| 2024 | 2 |
| 2025 | 2 |
| 2026 | 2 |
| 2023 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
