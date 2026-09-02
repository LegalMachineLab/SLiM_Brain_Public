---
id: "CPT-computational-argumentation"
label: "Computational argumentation"
status: "anchor"
concept_type: "technique_class"
definition: "Formal models of argument structure, attack, and defeat applied to legal reasoning."
aliases: []
broader: []
sources: ["SRC-0004", "SRC-0010", "SRC-0014", "SRC-0038"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Computational argumentation

_Status: anchor; family: technique_class._

## Definition

Formal models of argument structure, attack, and defeat applied to legal reasoning.

Conceptual claims on this concept, each with its source:
- T.Y.S.S. et al. (2024): Knowledge-based approaches to legal AI explicitly model legal reasoning and can achieve high faithfulness of representation and explainability of inferences, but they face the knowledge acquisition bottleneck because they require large amounts of legal expertise and modeling effort. [CLM-0014-011]
- T.Y.S.S. et al. (2024): Legal reasoning is defeasible rather than monotonic: rules applicable on their face can be trumped by special exceptions, conflicting superior rules, or by distinguishing the precedent from which the rule derives, and legal argumentation is an exercise in competitive theory formation before an arbitrator in which each side constructs arguments from evidence, written law, cases and other authority. [CLM-0014-018]

## Claims about the concept

### Descriptive

**general**

- T.Y.S.S. et al. (2024) state that Legal argument mining work has focused on text segmentation, argument span detection and span classification, with fewer models engaging in argument graph construction; modeling the relationships and comparative strength between conflicting arguments is a crucial piece for connecting extractive argument mining to structured argumentation that remains largely unaddressed by existing works. [CLM-0014-014]. — jurisdiction: general; basis: literature

### Normative

**general**

- T.Y.S.S. et al. (2024) argue that Legal NLP efforts should be evaluated and reviewed in terms of how well models support the production, structuring and assessment of arguments about legal conclusions for practitioners, and research on evaluation criteria that better capture the practical utility of legal NLP systems in real-world settings should be among the field's top priorities. [CLM-0014-010]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that There is value in NLP that produces, structures and assesses arguments about legal conclusions in an explainable way using domain knowledge representation: even with powerful LLMs available, argumentation support systems for legal practitioners benefit from structured representations of legal information and argumentation and should produce arguments transparently, offering users an intuitive way of resolving multiple complex arguments towards a justification of a decision. [CLM-0014-012]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that Symbolic AI & Law research has thought about how to incorporate legal expertise into models more deeply than most current legal NLP work, so the common view of it as mere precursor work to statistical methods does not do justice to its insights; knowledge-based approaches to legal argument support deserve the attention of the modern NLP community, and the two fields should merge and learn from one another. [CLM-0014-013]. — jurisdiction: general; basis: argument

### Empirical

**geographical_proxy:CoE**

- Mumford et al. (2023) report that Neither the level of legal domain experience of participants (computer science students, law students without ECHR study, law students with ECHR study) nor access to an ANGELIC domain model of Article 6 ECHR produced a statistically significant increase in verdict-classification performance; the best-performing group was the moderate-experience law students. [CLM-0010-007]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment
- Mumford et al. (2023) report that Access to an ANGELIC domain model (ADM) of Article 6 ECHR produced a statistically significant increase in participant productivity at the verdict-classification task, even though it did not significantly improve classification performance. [CLM-0010-013]. — jurisdiction: geographical_proxy:CoE; basis: dataset_or_experiment

### Conceptual

**general**

- T.Y.S.S. et al. (2024) argue that Knowledge-based approaches to legal AI explicitly model legal reasoning and can achieve high faithfulness of representation and explainability of inferences, but they face the knowledge acquisition bottleneck because they require large amounts of legal expertise and modeling effort. [CLM-0014-011]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) argue that Legal reasoning is defeasible rather than monotonic: rules applicable on their face can be trumped by special exceptions, conflicting superior rules, or by distinguishing the precedent from which the rule derives, and legal argumentation is an exercise in competitive theory formation before an arbitrator in which each side constructs arguments from evidence, written law, cases and other authority. [CLM-0014-018]. — jurisdiction: general; basis: literature

### Methodological

**US**

- Zhang et al. (2026) argue that The process of identifying significant distinctions between a current case and a precedent in case-based legal reasoning can be formalised, in the CATO tradition, as a decomposed framework of three increasingly complex tasks: (1) identify distinctions, (2) analyse the argumentative roles of a distinction (emphasis versus downplaying) through a hierarchy of factors, legal concerns and legal issues, and (3) identify all significant distinctions. Cases are modelled as sets of factors, the hierarchy as a directed acyclic graph with strong and weak support edges, and a symbolic solver computes ground truth from formal rules about distinctions, support, blocking, and emphasis/downplay, bridging abstract legal theory and computational implementation. [CLM-0038-001]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**general**

- Mumford et al. (2021) argue that Explainable case-outcome prediction can be produced by a hybrid system that separates the two stages of reasoning with cases: factor ascription is performed by a machine-learning natural language processing layer (a Hierarchical BERT model outputting, for each base-level factor, a binary 'ascribed' or 'not ascribed' classification), and the decision is reached by balancing the factors within a pre-determined, non-cyclic Abstract Dialectical Framework derived from expert knowledge. [CLM-0004-009]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that If domain expertise is of paramount importance in establishing an appropriate Abstract Dialectical Framework, data-driven approaches are less effective at the level of factors and above; accordingly, in a hybrid ML-ADF system only the architecture of the NLP layer should be adjusted by learning, while the expert-derived ADF layer remains unchanged from its initial state. [CLM-0004-010]. — jurisdiction: general; basis: literature
- Mumford et al. (2021) argue that Because the Boolean acceptance conditions of an Abstract Dialectical Framework are governed by a discontinuous Heaviside step function, backpropagation is not in general appropriate for propagating errors from a wrong decision through the ADF; instead, errors can be propagated backwards through a non-cyclic graphical scaffold of the ADF, in which each node is a linearly separable function and children can only attack their parent, yielding for each base-level factor a tuple of weights (ascribed, not ascribed) that determines the proportion of classification tasks assigned to the NLP layer in the next training epoch. [CLM-0004-012]. — jurisdiction: general; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Jurisprudence at its operational core is binary and deterministic (a statute is active or repealed, a deadline met or missed, jurisdiction present or absent), whereas an LLM represents knowledge as a continuous latent space in which a hallucinated case name sits close to a real one; the Rule of Law and deterministic AI architecture are therefore convergent, and the Neuro-Symbolic Sandwich reveals the logic the law has always demanded rather than imposing an alien one. [CLM-0049-006] is in tension with the claim that Legal reasoning is defeasible rather than monotonic: rules applicable on their face can be trumped by special exceptions, conflicting superior rules, or by distinguishing the precedent from which the rule derives, and legal argumentation is an exercise in competitive theory formation before an arbitrator in which each side constructs arguments from evidence, written law, cases and other authority. [CLM-0014-018] (inferred, high). Note: One holds that jurisprudence is at its operational core binary and deterministic; the other characterises legal reasoning as defeasible, ambiguous and discretionary.

## Distribution

Sources with claims on this concept: 4; claims: 12.

**By contribution type**

| value | sources |
|---|---|
| technical | 3 |
| theoretical | 3 |
| empirical_quantitative | 2 |
| normative | 1 |
| survey | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 3 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 2 |
| US | 1 |
| geographical_proxy:CoE | 1 |

**By year**

| value | sources |
|---|---|
| 2021 | 1 |
| 2023 | 1 |
| 2024 | 1 |
| 2026 | 1 |

## What the sources do not address

- No interpretive claim on CPT-computational-argumentation. [ABS-1381] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No predictive claim on CPT-computational-argumentation. [ABS-1382] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
