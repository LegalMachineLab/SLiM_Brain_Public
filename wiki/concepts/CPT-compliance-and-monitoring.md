---
id: "CPT-compliance-and-monitoring"
label: "Compliance and monitoring"
status: "anchor"
concept_type: "legal_task"
definition: "Checking conduct, systems, or documents against legal or regulatory requirements."
aliases: []
broader: []
sources: ["SRC-0012", "SRC-0024", "SRC-0025", "SRC-0040", "SRC-0049", "SRC-0050"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Compliance and monitoring

_Status: anchor; family: legal_task._

## Definition

Checking conduct, systems, or documents against legal or regulatory requirements.

Conceptual claims on this concept, each with its source:
- Hagag et al. (2024): Identifying legal violations on the open web presents two primary challenges: determining where to search among massive amounts of online content of varying credibility and relevance, and accurately interpreting whether the information found indicates a legal violation, which requires applying legal knowledge to determine the legal grounds and to identify victims who may be entitled to compensation. [CLM-0012-007]
- Hagag et al. (2024): Information sparsity is a challenge for identifying cases of legal violation on the open web: the salient details of a case are often spread across multiple online sources and individually offer little insight, so that a holistic understanding and evaluation of the case is possible only when the individual details are stitched together. [CLM-0012-014]
- Nay et al. (2023): Methods that improve LLMs' legal analysis skills are relevant to aligning AI with humans and governing AI: an LLM that grasps the law could 'self-police' to act in accordance with law, or separate models could apply legal and ethical standards to confirm whether another AI is properly aligned with the law (the 'Law Informs Code' approach). [CLM-0024-016]
- Mandal and Sinha (2026): Built-in compliance is a medium-to-high, sticky moat for a vertical application: beyond the table-stakes base layer, meeting complex regulatory and policy compliance requirements with ongoing conformance guarantees means supplying the determinism, explainability and auditability that foundation models lack; horizontal players rarely absorb this burden, and once a firm wires compliance into its supervision and recordkeeping stack, switching means re-validating from scratch. [CLM-0040-012]
- Mandal and Sinha (2026): Compliance requirements facing a vertical application fall on a spectrum of three tiers — a strict liability tier of rules requiring absolute adherence on pain of criminal liability or catastrophic fines (such as GDPR, HIPAA or the EU AI Act's prohibited and high-risk categories), a tolerable penalty tier where non-compliance is a manageable business cost, and a cautionary or advisory tier with opportunities to correct and minimal penalties — and verticals and workflows in the more stringent tiers can create much deeper moats through specialised solutions. [CLM-0040-013]

## Claims about the concept

### Descriptive

**US**

- Mandal and Sinha (2026) state that In wealth management, which is governed by overlapping regimes of SEC recordkeeping and fiduciary rules, FINRA supervision and communications rules for broker-dealers, and state-level RIA rules, compliance rather than note-taking is the moat of the advisor productivity tool Jump, and compliance is what allows Jump to command a price premium over horizontal recording tools. [CLM-0040-014]. — jurisdiction: US [jurisdiction inferred]; basis: argument
- Mandal and Sinha (2026) state that FINRA's 2026 regulatory oversight report explicitly pivots from AI guidance to accountability, demanding that firms document how their AI systems are supervised. [CLM-0040-015]. — jurisdiction: US [jurisdiction inferred]; basis: literature; positive form: trend

**general**

- Hagag et al. (2024) state that Prior work on automated detection of legal violations focused on domain-specific use cases such as privacy protection and lacks the versatility needed to address the broad spectrum of legal violations across contexts; LegalLens (Bernsohn et al., 2024) was the first to introduce legal violation detection as a general natural language inference task across multiple domains and the first to establish a cross-domain approach for detecting legal violations. [CLM-0012-013]. — jurisdiction: general; basis: literature
- Getir Yaman et al. (2023) state that Existing formal verification approaches for autonomous systems mostly focus on the agents' safety requirements, and prior work on verifying ethical and legal constraints of robots does not address the operationalisation of such requirements and provides no notation dedicated to encoding SLEEC-related concerns as requirements; the SLEEC framework is distinctive in addressing the operationalisation of norms while leaving the identification of rules to complementary work. [CLM-0025-016]. — jurisdiction: general; basis: literature
- Getir Yaman et al. (2023) state that Many autonomous systems learn, adapt and evolve in operation, for example in response to changes in their environment, and therefore cannot be fully verified at development time; runtime verification of autonomous-agent decisions against SLEEC rules and online synthesis of SLEEC-compliant adaptation plans are needed to cover this evolution. [CLM-0025-018]. — jurisdiction: general; basis: argument

### Interpretive

**EU**

- Gridin (2026) read AI Act, Art. 9(1) as follows: Satisfying Article 9 of the EU AI Act (a continuous, iterative risk management system throughout the lifecycle of a high-risk system) solely through manual human audits is economically and practically impossible given the volume and velocity of legal data processing; passing every LLM output through deterministic Linear AI wrappers before execution performs a systematic risk audit on every transaction and thereby automates compliance with Article 9. [CLM-0049-022]. — jurisdiction: EU; basis: legislation

### Normative

**EU, US**

- Gridin (2026) argue that The transatlantic regulatory chasm is architecturally bridgeable: by establishing a single apex internal 'High Trust' standard (Risk Interoperability) whose Neuro-Symbolic architecture satisfies the EU AI Act's strictest transparency criteria while generating the cryptographic audit trail required by US tort law, a corporation can dissolve the binary compliance trap without legislative harmonisation, and sandboxed 'Shadow AI Governance' deployment lets it achieve US innovation velocity while producing the evidentiary logs European regulators require. [CLM-0049-019]. — jurisdiction: EU, US (comparative); basis: argument

**general**

- Hagag et al. (2024) argue that The broader research community, particularly interdisciplinary researchers, should contribute resources, methodologies and diverse perspectives to legal violation detection, because collaboration across disciplines will be crucial to advancing the state of the art in this area. [CLM-0012-015]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Systematic prompt tests with clear thresholds should be set and met before public release to minimise trial-and-error deployment, and any standardisation of system-level instructions should not target specific words or prompt templates unless robustness across implementations has been shown; specialised intermediary roles could translate governance objectives into prompt specifications and validate their behavioural effects. [CLM-0050-017]. — jurisdiction: general; basis: argument

### Empirical

**general**

- Getir Yaman et al. (2023) report that In the robotic assistive dressing (RAD) case study, the SLEEC framework found the four expert-defined rules to be free of conflict and redundancy and the RoboChart design to satisfy three of them, but detected a violation of the fourth rule: an extra design requirement to call support within one minute of a user fall is incompatible with the rule requiring a two-minute delay for a retry agreement before support is called when dressing is abandoned. [CLM-0025-014]. — jurisdiction: general; basis: dataset_or_experiment

**geographical_proxy:US**

- Hagag et al. (2024) report that In the LegalLens Shared Task 2024, the top-performing teams in both the LegalLens-NER and LegalLens-NLI sub-tasks consistently relied on fine-tuning pretrained language models, and these fine-tuned models outperformed legal-specific models and few-shot methods. [CLM-0012-001]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that In the LegalLens Shared Task 2024, progress over the baseline was substantial for legal violation entity recognition (the best team improved the NER F1 score by 7.11%) but marginal for legal natural language inference (only one team outperformed the NLI baseline, by 5.7%), so significant room remains for advances in handling the complexities of natural legal language inference. [CLM-0012-002]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that Success in one LegalLens sub-task does not necessarily translate into success in the other: the challenges posed by legal violation entity recognition (LegalLens-NER) and legal violation inference (LegalLens-NLI) are distinct and require different approaches and strengths. [CLM-0012-003]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that In the LegalLens-NER sub-task there appears to be a performance ceiling: the top four teams achieve scores around 70% F1, which seems to be a plateau. [CLM-0012-004]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that Systems in the LegalLens-NER sub-task showed a significant drop in performance when identifying the "Violated By" and "Violated On" entities compared with the Law and Violation entities; this gap indicates room for improvement and suggests the potential of integrating other information extraction techniques, possibly from outside the legal domain. [CLM-0012-005]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Hagag et al. (2024) report that In the LegalLens-NLI sub-task, performance varied significantly by legal domain: systems underperformed in the Wage domain, likely because of its smaller dataset size and the implicit nature of its violations, and while models fine-tuned on larger datasets showed better overall performance, models specialising in domain-specific tasks demonstrated only marginal improvements, revealing a gap in domain adaptation. [CLM-0012-006]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

### Conceptual

**general**

- Hagag et al. (2024) argue that Identifying legal violations on the open web presents two primary challenges: determining where to search among massive amounts of online content of varying credibility and relevance, and accurately interpreting whether the information found indicates a legal violation, which requires applying legal knowledge to determine the legal grounds and to identify victims who may be entitled to compensation. [CLM-0012-007]. — jurisdiction: general; basis: argument
- Hagag et al. (2024) argue that Information sparsity is a challenge for identifying cases of legal violation on the open web: the salient details of a case are often spread across multiple online sources and individually offer little insight, so that a holistic understanding and evaluation of the case is possible only when the individual details are stitched together. [CLM-0012-014]. — jurisdiction: general; basis: argument
- Nay et al. (2023) argue that Methods that improve LLMs' legal analysis skills are relevant to aligning AI with humans and governing AI: an LLM that grasps the law could 'self-police' to act in accordance with law, or separate models could apply legal and ethical standards to confirm whether another AI is properly aligned with the law (the 'Law Informs Code' approach). [CLM-0024-016]. — jurisdiction: general; basis: argument
- Mandal and Sinha (2026) argue that Built-in compliance is a medium-to-high, sticky moat for a vertical application: beyond the table-stakes base layer, meeting complex regulatory and policy compliance requirements with ongoing conformance guarantees means supplying the determinism, explainability and auditability that foundation models lack; horizontal players rarely absorb this burden, and once a firm wires compliance into its supervision and recordkeeping stack, switching means re-validating from scratch. [CLM-0040-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mandal and Sinha (2026) argue that Compliance requirements facing a vertical application fall on a spectrum of three tiers — a strict liability tier of rules requiring absolute adherence on pain of criminal liability or catastrophic fines (such as GDPR, HIPAA or the EU AI Act's prohibited and high-risk categories), a tolerable penalty tier where non-compliance is a manageable business cost, and a cautionary or advisory tier with opportunities to correct and minimal penalties — and verticals and workflows in the more stringent tiers can create much deeper moats through specialised solutions. [CLM-0040-013]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Predictive

**general**

- Nay et al. (2023) argue that If LLMs understand the law well enough, they could be deployed by governments, citizens and researchers to identify inconsistencies in existing laws, flag potentially outdated law or areas where the law is silent although guidance exists in similar circumstances, provide clear explanations of complex laws and regulations, and eventually help predict the likely impacts of new laws or policies. [CLM-0024-017]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that The relatively low complexity of SLEEC rules is expected to make verification of a system's compliance with each individual rule feasible, provided the system's tock-CSP model is itself of manageable size; this assumption may not always hold because of state explosion, in particular as the FDR model checker is not optimised for timed (tock-CSP) models, but RoboChart's support for theorem proving, simulation and testing offers alternative verification routes. [CLM-0025-012]. — jurisdiction: general; basis: argument

### Methodological

**general**

- Hagag et al. (2024) argue that A system for efficiently detecting legal violations in online digital data must scan large amounts of data, isolate relevant information, contextualise the findings by linking them to specific legal grounds, clearly explain potential violations, and identify the affected individuals or entities who may be entitled to legal recourse. [CLM-0012-008]. — jurisdiction: general; basis: argument
- Hagag et al. (2024) argue that Existing named entity recognition methods and entity types, including those used in legal-domain NER tasks (such as plaintiff and defendant), are not tailored to detecting legal violations, fail to capture the ambiguity of legal language, and lack the complexity needed for the task. [CLM-0012-009]. — jurisdiction: general; basis: literature
- Hagag et al. (2024) argue that Beyond mapping detected violations to legal grounds, the LegalLens-NLI task can serve the additional purpose of identifying individuals who may have been harmed by a violation, by using descriptions of violations (such as court-filed complaints or articles) as premises and online content in which people describe personal experiences (such as reviews or posts) as hypotheses. [CLM-0012-010]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that SLEEC (social, legal, ethical, empathetic and cultural) rules for autonomous agents can be given end-to-end tool-supported formal treatment through a framework comprising a domain-specific language for specifying the rules and their defeaters, a formal semantics for that language in the process algebra tock-CSP, and methods for detecting conflicts and redundancy within a rule set and for verifying an agent's compliance with the rules. [CLM-0025-002]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that Conflict freedom of two SLEEC rules can be checked automatically with the FDR model checker using two assertions on the parallel conjunction of the rule processes, a standard deadlock-freedom assertion and a timed-deadlock-freedom assertion; deadlock freedom alone is insufficient, because a rule pair can pass the deadlock check while still reaching a state in which only the passage of time is possible. [CLM-0025-008]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that Compliance of an autonomous agent design with a SLEEC rule can be verified as traces refinement in tock-CSP, with the specification given by the process capturing the semantics of the rule: the events of the system under verification must occur in the order and time the rule specifies, projected onto the rule's alphabet and with matching values of the measures the rule reads, while the conforming system may engage in additional events and read additional measures. [CLM-0025-011]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that When a system design is found to violate a SLEEC rule, the SLEEC and requirements stakeholders have to be consulted to decide the outcome; possible resolutions include a domain expert relaxing an over-strict design deadline, or distinguishing capabilities so that different types of call to support are represented by distinct events. [CLM-0025-015]. — jurisdiction: general; basis: argument
- Gridin (2026) argue that AI should be deployed in high-stakes legal environments only through a Neuro-Symbolic 'Sandwich' architecture in which a generative LLM is encapsulated by hundreds of specialised, rule-based Linear AI micro-agents (for example citation, chronological, and arithmetic agents) that verify its output against closed libraries and deterministically halt the workflow on error; delegating creativity to the neural network and factual verification to the linear algorithm is the only computationally sound method to deploy AI in such environments. [CLM-0049-005]. — jurisdiction: general; basis: argument

**geographical_proxy:US**

- Hagag et al. (2024) argue that The enhanced LegalLens dataset built for the shared task is a more comprehensive and challenging benchmark than the original LegalLens dataset: improved prompt practices, better annotator guidelines, human expert validation and feedback on the original paper improve the generation process and the annotations, yielding more realistic content, better data quality and reduced bias. [CLM-0012-012]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002] is in tension with the claim that In the LegalLens Shared Task 2024, the top-performing teams in both the LegalLens-NER and LegalLens-NLI sub-tasks consistently relied on fine-tuning pretrained language models, and these fine-tuned models outperformed legal-specific models and few-shot methods. [CLM-0012-001] (inferred, medium). Note: One finds legal-oriented pre-trained models overall better than generic ones on legal NLU tasks; the other finds fine-tuned generic models beating legal-specific ones on violation detection.

## Distribution

Sources with claims on this concept: 6; claims: 32.

**By contribution type**

| value | sources |
|---|---|
| technical | 4 |
| theoretical | 4 |
| empirical_qualitative | 3 |
| normative | 3 |
| empirical_quantitative | 2 |
| doctrinal | 1 |
| survey | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 4 |
| US | 2 |
| CoE | 1 |
| EU | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 6 |
| US | 2 |
| EU | 1 |
| geographical_proxy:US | 1 |

**By year**

| value | sources |
|---|---|
| 2026 | 3 |
| 2023 | 2 |
| 2024 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
