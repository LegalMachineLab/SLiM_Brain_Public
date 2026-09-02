---
id: "CPT-argument-mining"
label: "Argument mining"
status: "anchor"
concept_type: "legal_task"
definition: "Identifying and structuring argumentative units and rhetorical roles in legal text."
aliases: []
broader: []
sources: ["SRC-0007", "SRC-0014"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Argument mining

_Status: anchor; family: legal_task._

## Definition

Identifying and structuring argumentative units and rhetorical roles in legal text.

## Claims about the concept

### Descriptive

**IN**

- Malik et al. (2022) state that In India's common law system a decision may not follow the statute exactly, since the judiciary may adopt its own interpretation and overrule existing precedents, which introduces subjectivity into the identification of rhetorical roles in a judgment; competition law and income tax law display a relatively greater degree of consistency and objectivity in judicial reliance on statutory provisions, and focusing on these domains reduces that subjectivity. [CLM-0007-005]. — jurisdiction: IN; basis: argument; positive form: general_rule

**general**

- Malik et al. (2022) state that Few works have focused on creating annotated corpora for rhetorical roles and on the task of automatic rhetorical role labeling in legal documents. [CLM-0007-003]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that Legal argument mining work has focused on text segmentation, argument span detection and span classification, with fewer models engaging in argument graph construction; modeling the relationships and comparative strength between conflicting arguments is a crucial piece for connecting extractive argument mining to structured argumentation that remains largely unaddressed by existing works. [CLM-0014-014]. — jurisdiction: general; basis: literature

### Normative

**general**

- T.Y.S.S. et al. (2024) argue that Legal NLP efforts should be evaluated and reviewed in terms of how well models support the production, structuring and assessment of arguments about legal conclusions for practitioners, and research on evaluation criteria that better capture the practical utility of legal NLP systems in real-world settings should be among the field's top priorities. [CLM-0014-010]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that There is value in NLP that produces, structures and assesses arguments about legal conclusions in an explainable way using domain knowledge representation: even with powerful LLMs available, argumentation support systems for legal practitioners benefit from structured representations of legal information and argumentation and should produce arguments transparently, offering users an intuitive way of resolving multiple complex arguments towards a justification of a decision. [CLM-0014-012]. — jurisdiction: general; basis: argument

### Empirical

**IN**

- Malik et al. (2022) report that Inter-annotator agreement on rhetorical roles is substantial but differs between legal domains: Fleiss kappa is 0.65 for income tax and 0.87 for competition law (macro F1 0.73 versus 0.88); the lower agreement in income tax is attributed, following the law professors, to the presence of more precedents and a greater number of statutory provisions in income tax law, which produce more subjectivity in interpreting judicial decisions. [CLM-0007-007]. — jurisdiction: IN; basis: dataset_or_experiment

**geographical_proxy:IN**

- Malik et al. (2022) report that Annotating judgments with rhetorical roles is a challenging task even for legal experts: annotators must combine facts, arguments and implicit context nontrivially, have access only to the judgment as a secondary account of what happened in court, and are left making educated guesses; not all roles are equally susceptible to this variation, and annotators disagreed most on the ruling by the lower court, followed by the ratio of the decision. [CLM-0007-006]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that A single sentence of a judgment can sometimes represent multiple rhetorical roles, although this is not common: annotators assigned a secondary role in about 5-7 percent of sentences and a tertiary role in about 0.5-1 percent. [CLM-0007-009]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that Rhetorical role labels do not change abruptly across consecutive sentences of a judgment: in the training data, when a sentence carries a label, the next sentence carries the same label 88 percent of the time, though this label-shift inertia fades beyond the second consecutive sentence. [CLM-0007-010]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that A multitask learning model (MTL-BiLSTM-CRF) that uses label shift prediction as an auxiliary task outperforms existing rhetorical role prediction models, including the BiLSTM-CRF of Bhattacharya et al. (2019) and BERT-based baselines, reaching average macro F1 of 0.70 on income tax, 0.69 on competition law and 0.71 on the combined domain; the label shift prediction task is what contributes the superior performance. [CLM-0007-011]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that LEGAL-BERT performs slightly better than pre-trained BERT on Indian competition-law judgments but slightly worse on income-tax judgments, which might be because LEGAL-BERT was trained on EU legal documents, including European competition law, and not on Indian income tax law documents. [CLM-0007-012]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that The rhetorical role prediction model performs best on the facts label and worst on the ruling-by-lower-court label, mirroring the pattern of agreement observed among the human annotators. [CLM-0007-013]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that The MTL model's performance on income-tax cases comes close to the average inter-annotator agreement, while a gap remains for competition law; the model performs better on income tax than on competition law, the opposite of the trend among annotators, possibly because the selected income-tax documents are restricted to specific sections of the law and the model learned solely from them without external knowledge, whereas annotators drew on knowledge of the entire income tax law. [CLM-0007-014]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that The MTL rhetorical role model generalises better across legal sub-domains than the BiLSTM-CRF baseline when transferred between the competition-law and income-tax corpus and a criminal and civil case dataset, and both models perform better on the criminal/civil test set when trained on the combined income-tax and competition-law training set. [CLM-0007-015]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that Because rhetorical role annotation is tedious while unlabelled legal documents are abundant, self-training based model distillation on unlabelled documents can improve rhetorical role prediction: after two iterations on the income-tax domain, results improve for the majority of labels (macro F1 from 0.68 to 0.72, with a 0.11 gain for the ruling-by-lower-court label in the first iteration) and the variance of F1 across labels decreases. [CLM-0007-016]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that Feeding a judgment-prediction model only the sentences carrying gold ratio-of-decision and ruling-by-present-court rhetorical roles improves judgment prediction F1 over using the last 512 tokens of the document (0.58 versus 0.55, statistically significant), whereas using predicted rhetorical roles yields performance comparable to the baseline; improving rhetorical role prediction for these two roles would therefore enhance judgment prediction. [CLM-0007-017]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that Inter-annotator agreement on the 'None' rhetorical role label is as low as 0.45 F1 in both the income-tax and competition-law domains, implying that even legal experts do not agree on whether a sentence belongs to no rhetorical role, which justifies excluding such sentences from prediction experiments. [CLM-0007-019]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment
- Malik et al. (2022) report that Annotators agree most on judgments that are written with explicit indicators before each rhetorical role, follow a consistent order of roles, and are relatively short, whereas judgments that lack such indicators, move back and forth between roles, discuss precedents in detail, or blur whether the judge is reiterating counsel's arguments or stating a view leave scope for individual discretion and subjective interpretation. [CLM-0007-020]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

### Methodological

**IN**

- Malik et al. (2022) argue that A new corpus of 100 Indian judgments (50 competition-law and 50 income-tax cases) is introduced, annotated at sentence level by legal experts with 13 fine-grained rhetorical role labels, including primary, secondary and tertiary role levels; it is about twice the size of the earlier 8-role corpus of Bhattacharya et al. (2019), uses a more fine-grained label set, and covers different legal sub-domains. [CLM-0007-004]. — jurisdiction: IN; basis: dataset_or_experiment

**general**

- Malik et al. (2022) argue that Legal documents are long, unstructured, noisy and written in a specialised lexicon, which makes conventional text-processing techniques and pre-trained neural models ineffective on them; a legal document processing system would benefit substantially if documents were segmented into coherent information units (rhetorical roles), which could aid summarisation, legal judgment prediction, information extraction and prior case retrieval. [CLM-0007-001]. — jurisdiction: general; basis: argument

**geographical_proxy:IN**

- Malik et al. (2022) argue that Sentence-level annotation is the appropriate granularity for rhetorical role labeling of judgments, because a pilot study showed it balances topical coherence between phrase-level units, which are too short to carry labels, and paragraph-level units, which are too long and carry too many labels. [CLM-0007-008]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 2; claims: 21.

**By contribution type**

| value | sources |
|---|---|
| empirical_quantitative | 1 |
| normative | 1 |
| survey | 1 |
| technical | 1 |
| theoretical | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| IN | 1 |
| general | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 2 |
| IN | 1 |
| geographical_proxy:IN | 1 |

**By year**

| value | sources |
|---|---|
| 2022 | 1 |
| 2024 | 1 |

## What the sources do not address

- No interpretive claim on CPT-argument-mining. [ABS-1369] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No conceptual claim on CPT-argument-mining. [ABS-1370] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No predictive claim on CPT-argument-mining. [ABS-1371] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
