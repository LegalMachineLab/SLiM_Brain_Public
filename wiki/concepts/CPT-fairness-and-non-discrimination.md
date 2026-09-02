---
id: "CPT-fairness-and-non-discrimination"
label: "Fairness and non-discrimination"
status: "anchor"
concept_type: "normative_concern"
definition: "Bias, disparate impact, and equal treatment in AI-supported legal processes."
aliases: []
broader: []
sources: ["SRC-0014", "SRC-0018", "SRC-0019", "SRC-0020", "SRC-0024", "SRC-0026", "SRC-0030", "SRC-0031", "SRC-0034", "SRC-0049"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Fairness and non-discrimination

_Status: anchor; family: normative_concern._

## Definition

Bias, disparate impact, and equal treatment in AI-supported legal processes.

## Claims about the concept

### Descriptive

**general**

- Hou et al. (2025) state that Some legal datasets may contain gender or racial biases, existing methods offer little discussion of how to clean biased datasets, and AI models trained on such datasets could produce unfair decisions in practical judicial applications. [CLM-0034-018]. — jurisdiction: general; basis: argument

### Interpretive

**general**

- Li et al. (2024) read Large language models as follows: The application of large language models in the legal domain raises three concerns: because LLMs derive decisions from statistical patterns in training data rather than professional knowledge and logical reasoning, they often fall short of ensuring reliability and explainability; they may produce misleading and factually incorrect content (hallucination) that could mislead legal practitioners; and they may reflect biases in their training data, leading to unfair treatment of certain groups and undermining the fairness of judicial proceedings. [CLM-0030-002]. — jurisdiction: general; basis: literature

**geographical_proxy:NL**

- Gridin (2026) read Explainability and transparency as follows: The Dutch childcare benefits scandal shows that a black-box fraud-detection algorithm whose logic the overseeing humans could not audit produced mass injustice that cannot afterwards be 'rewound' to establish culpability in individual cases; a Neuro-Symbolic Sandwich using closed libraries and an immutable Codification Table would prevent such outcomes by guaranteeing absolute retrospective auditability of every parameter weighed. [CLM-0049-015]. — jurisdiction: geographical_proxy:NL [jurisdiction inferred]; basis: literature

### Normative

**general**

- T.Y.S.S. et al. (2024) argue that Any data-driven legal NLP system intended for practical deployment must undergo rigorous scrutiny of its performance, behavior and intended application to ensure compliance with applicable equal treatment and transparency imperatives, because training on historical data and inheriting biases from pre-training data may introduce biases into the system. [CLM-0014-021]. — jurisdiction: general; basis: literature
- Steenhuis (2025) argue that Bias is an important risk to consider when using LLMs for legal intake classification, because biased classification may lead to unfair allocations of scarce low-cost and free legal help resources; these concerns are stronger when the LLM has a higher error rate and particularly when the errors show a pattern that is uneven across the distribution of applicants and problem types. [CLM-0018-012]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Nay et al. (2023) argue that Rigorous safeguards should be put in place as LLMs are deployed for legal services, given the sensitive nature of legal work: increasing data privacy, minimising bias, maintaining accountability for decisions made with the models' help, and evaluating the suitability of the LLM for each use case, which makes systematic evaluations necessary. [CLM-0024-018]. — jurisdiction: general; basis: argument
- Guha et al. (2023) argue that Because legal applications involve significant risk and LLMs are capable of generating offensive, misleading and factually incorrect content whose harms would fall disproportionately on marginalised and under-resourced populations, there is a pressing need to develop infrastructure and processes for benchmarking LLMs in legal contexts, and answering empirically what legal tasks LLMs can perform is vital for their safe and ethical use. [CLM-0026-003]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Westermann and Savelka (2024) argue that If a multi-modal LLM form-extraction tool is provided to the public, one has to remain aware of its implications for the digital divide, because a modern phone and good lighting conditions are important for good results, which may exclude certain groups from using such tools. [CLM-0031-009]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Gridin (2026) argue that The equalising potential of deterministic legal AI is contingent on equitable access to the infrastructure; if such systems are deployed only by well-resourced entities at prices beyond individual practitioners, legal aid organisations and public defenders, the technology risks exacerbating rather than equalising power asymmetries, so public authorities, bar associations and legal aid bodies should explore shared-infrastructure models, open-source deterministic verification layers, and subsidised licensing. [CLM-0049-042]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Empirical

**general**

- Zhu et al. (2025) report that Dealmaking between LLM agents acting on behalf of consumers and merchants in consumer settings is an inherently imbalanced game: different LLM agents show large disparities in their ability to obtain the best deals for the users they represent. [CLM-0020-001]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:CN**

- Li et al. (2024) report that At the Ethic level of legal cognitive ability, even GPT-4, which shows relatively good performance, remains far from satisfactory, and the unsatisfactory performance of LLMs on ethics-related legal tasks poses serious challenges to their safe application in real-life scenarios. [CLM-0030-021]. — jurisdiction: geographical_proxy:CN; basis: dataset_or_experiment

**geographical_proxy:US**

- Steenhuis (2025) report that The errors of the small-model ensemble classifier on legal intake queries showed no observable pattern: they did not appear biased towards one type of legal problem over another, similar categories were not consistently confused, and the safety concerns revealed by the errors appear minimal. [CLM-0018-004]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Predictive

**general**

- Westermann and Savelka (2024) argue that The preference of multi-modal LLMs for more common data shows that the token distributions embedded in the models can affect their extraction performance and may risk introducing biases in society if not properly evaluated. [CLM-0031-008]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

### Methodological

**general**

- Khadloya et al. (2025) argue that A judge-facing AI interface should show only passages grounded in visible anchors in the document, never free text, and should offer a disambiguation list or withhold an answer when evidence is insufficient; this grounding and abstention keeps evidence verifiable and auditable and mitigates the bias and overconfidence risks of generative models. [CLM-0019-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 10; claims: 14.

**By contribution type**

| value | sources |
|---|---|
| technical | 8 |
| empirical_quantitative | 7 |
| theoretical | 5 |
| normative | 2 |
| survey | 2 |
| doctrinal | 1 |
| empirical_qualitative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| US | 4 |
| general | 4 |
| CN | 1 |
| CoE | 1 |
| EU | 1 |
| IN | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 10 |
| geographical_proxy:CN | 1 |
| geographical_proxy:NL | 1 |
| geographical_proxy:US | 1 |

**By year**

| value | sources |
|---|---|
| 2025 | 4 |
| 2024 | 3 |
| 2023 | 2 |
| 2026 | 1 |

## What the sources do not address

- No conceptual claim on CPT-fairness-and-non-discrimination. [ABS-1408] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
