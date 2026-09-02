---
id: "CPT-case-based-reasoning"
label: "Case-based reasoning"
status: "anchor"
concept_type: "technique_class"
definition: "Reasoning from precedent cases by factor or dimension comparison."
aliases: []
broader: []
sources: ["SRC-0004", "SRC-0014", "SRC-0033", "SRC-0038"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Case-based reasoning

_Status: anchor; family: technique_class._

## Definition

Reasoning from precedent cases by factor or dimension comparison.

Conceptual claims on this concept, each with its source:
- Mumford et al. (2021): Factor-based explanations of the CATO kind explain well cases in which the dispute turns on the balance of the ascribed factors, but are less satisfactory in cases where the losing party contended that other factors were present, or where the presence of a factor was itself contested; in such cases the explanation the losing party needs is why the claim that other factors were present was rejected, or why a factor was held to apply. [CLM-0004-002]
- Mumford et al. (2021): The ascription of factors that correspond to ranges on well-ordered dimensions can be explained in terms of the precedents that establish those ranges, but this kind of explanation does not seem applicable to factor ascriptions that rest on detailed consideration of very particular facts, which may involve analogy or some kind of common-sense ontology. [CLM-0004-006]
- T.Y.S.S. et al. (2024): Knowledge-based approaches to legal AI explicitly model legal reasoning and can achieve high faithfulness of representation and explainability of inferences, but they face the knowledge acquisition bottleneck because they require large amounts of legal expertise and modeling effort. [CLM-0014-011]
- T.Y.S.S. et al. (2024): Legal reasoning is defeasible rather than monotonic: rules applicable on their face can be trumped by special exceptions, conflicting superior rules, or by distinguishing the precedent from which the rule derives, and legal argumentation is an exercise in competitive theory formation before an arbitrator in which each side constructs arguments from evidence, written law, cases and other authority. [CLM-0014-018]
- Zhang et al. (2026): A distinction between a current case and a precedent is significant if and only if it can be emphasized and cannot be downplayed. A significant distinction is a fundamental factual difference between the cases that is not easily explained away; it points to a core weakness in the analogical argument and provides a strong basis for arguing for a different outcome. [CLM-0038-002]

## Claims about the concept

### Descriptive

**general**

- Mumford et al. (2021) state that There has been little or no work in AI and Law on explaining why factors are present or absent in a case, because most research since HYPO has taken the factors as given. [CLM-0004-003]. — jurisdiction: general; basis: literature
- Maurya (2025) state that Early rule-based legal expert systems (such as TAXMAN and LEGOL) and case-based reasoning systems (such as HYPO and CATO) were overwhelmed by law's real-world complexity: they worked well for closely bounded domains such as tax or social benefits but failed at open-texture language and variable interpretation. [CLM-0033-003]. — jurisdiction: general; basis: literature

### Normative

**general**

- Mumford et al. (2021) argue that Explanations of legal decisions must go beyond the factors present in a case and the preferences between them: they must also explain the ascription and non-ascription of the factors themselves, that is, why particular factors are held to be present or absent. [CLM-0004-001]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that Symbolic AI & Law research has thought about how to incorporate legal expertise into models more deeply than most current legal NLP work, so the common view of it as mere precursor work to statistical methods does not do justice to its insights; knowledge-based approaches to legal argument support deserve the attention of the modern NLP community, and the two fields should merge and learn from one another. [CLM-0014-013]. — jurisdiction: general; basis: argument

**geographical_proxy:US**

- Zhang et al. (2026) argue that Because the ability to identify significant distinctions is important to legal practice, the current inability of LLMs to perform this task reliably raises concerns about their readiness for real-world legal applications: effective legal AI must be capable of multi-step, multi-level abstraction and synthesis, and the current generation of LLMs, despite impressive surface-level capabilities, lacks the sophisticated reasoning mechanisms necessary for the nuanced analysis required in legal practice. [CLM-0038-010]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Empirical

**geographical_proxy:US**

- Zhang et al. (2026) report that Reasoning LLMs show a systematic decline in accuracy as the complexity of hierarchical legal reasoning tasks increases: all evaluated models reach 100% accuracy on identifying surface-level distinctions between cases (Task 1), accuracy degrades to 64.82%-92.09% on hierarchical reasoning about the argumentative roles of a distinction (Task 2), and collapses to 11.46%-33.99% on the integrated identification of all significant distinctions (Task 3), which suggests that the integration of multiple reasoning steps is a challenge for current reasoning LLMs. [CLM-0038-003]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Zhang et al. (2026) report that The intermediate reasoning process of thinking models, enabled by reinforcement-learning-based post-training, is beneficial for navigating the hierarchical structure of legal knowledge: the qwen3 thinking model reached 78.66% accuracy on analysing the argumentative roles of a distinction (Task 2) against 30.04% for its non-thinking counterpart, and retained 33.99% accuracy on identifying all significant distinctions (Task 3) where the non-thinking model scored 0.00%. [CLM-0038-004]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Conceptual

**US**

- Zhang et al. (2026) argue that A distinction between a current case and a precedent is significant if and only if it can be emphasized and cannot be downplayed. A significant distinction is a fundamental factual difference between the cases that is not easily explained away; it points to a core weakness in the analogical argument and provides a strong basis for arguing for a different outcome. [CLM-0038-002]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**general**

- Mumford et al. (2021) argue that The ascription of factors that correspond to ranges on well-ordered dimensions can be explained in terms of the precedents that establish those ranges, but this kind of explanation does not seem applicable to factor ascriptions that rest on detailed consideration of very particular facts, which may involve analogy or some kind of common-sense ontology. [CLM-0004-006]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that Knowledge-based approaches to legal AI explicitly model legal reasoning and can achieve high faithfulness of representation and explainability of inferences, but they face the knowledge acquisition bottleneck because they require large amounts of legal expertise and modeling effort. [CLM-0014-011]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) argue that Legal reasoning is defeasible rather than monotonic: rules applicable on their face can be trumped by special exceptions, conflicting superior rules, or by distinguishing the precedent from which the rule derives, and legal argumentation is an exercise in competitive theory formation before an arbitrator in which each side constructs arguments from evidence, written law, cases and other authority. [CLM-0014-018]. — jurisdiction: general; basis: literature

**geographical_proxy:US**

- Mumford et al. (2021) argue that Factor-based explanations of the CATO kind explain well cases in which the dispute turns on the balance of the ascribed factors, but are less satisfactory in cases where the losing party contended that other factors were present, or where the presence of a factor was itself contested; in such cases the explanation the losing party needs is why the claim that other factors were present was rejected, or why a factor was held to apply. [CLM-0004-002]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: argument

### Predictive

**geographical_proxy:US**

- Zhang et al. (2026) argue that The core limitation in hierarchical reasoning that a formal factor-based representation exposes may also exist, but be obfuscated, when LLMs operate on contextual narrative legal work, especially in areas well represented in their pre-training data or accessible through retrieval-augmented generation: in such cases models might appear to reason effectively by retrieving and adapting existing solutions, masking an underlying deficit in hierarchical problem-solving. [CLM-0038-009]. — jurisdiction: geographical_proxy:US; basis: argument

### Methodological

**US**

- Zhang et al. (2026) argue that The process of identifying significant distinctions between a current case and a precedent in case-based legal reasoning can be formalised, in the CATO tradition, as a decomposed framework of three increasingly complex tasks: (1) identify distinctions, (2) analyse the argumentative roles of a distinction (emphasis versus downplaying) through a hierarchy of factors, legal concerns and legal issues, and (3) identify all significant distinctions. Cases are modelled as sets of factors, the hierarchy as a directed acyclic graph with strong and weak support edges, and a symbolic solver computes ground truth from formal rules about distinctions, support, blocking, and emphasis/downplay, bridging abstract legal theory and computational implementation. [CLM-0038-001]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**general**

- Mumford et al. (2021) argue that Explanations of the presence and absence of particular factors could be delivered by extending an issue-based explanation dialogue so that the user may ask WHY? of any factor used to explain an issue and WHY NOT? of any factor not mentioned in the explanation of an issue. [CLM-0004-005]. — jurisdiction: general; basis: argument
- Mumford et al. (2021) argue that The key role for machine learning in reasoning with legal cases is not the prediction of outcomes but the identification of the factors present in a case. [CLM-0004-007]. — jurisdiction: general; basis: argument
- T.Y.S.S. et al. (2024) argue that One intuitive way to combine legal knowledge and machine learning in NLP is to ascribe factors from case texts by text processing and then proceed with formalized legal inference; rather than training factor classifiers against an exhaustively defined factor list, the more likely scenario is that generative models are prompted with specific facts to subsume them under a factor pattern description. [CLM-0014-019]. — jurisdiction: general; basis: literature

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Jurisprudence at its operational core is binary and deterministic (a statute is active or repealed, a deadline met or missed, jurisdiction present or absent), whereas an LLM represents knowledge as a continuous latent space in which a hallucinated case name sits close to a real one; the Rule of Law and deterministic AI architecture are therefore convergent, and the Neuro-Symbolic Sandwich reveals the logic the law has always demanded rather than imposing an alien one. [CLM-0049-006] is in tension with the claim that Legal reasoning is defeasible rather than monotonic: rules applicable on their face can be trumped by special exceptions, conflicting superior rules, or by distinguishing the precedent from which the rule derives, and legal argumentation is an exercise in competitive theory formation before an arbitrator in which each side constructs arguments from evidence, written law, cases and other authority. [CLM-0014-018] (inferred, high). Note: One holds that jurisprudence is at its operational core binary and deterministic; the other characterises legal reasoning as defeasible, ambiguous and discretionary.

## Distribution

Sources with claims on this concept: 4; claims: 17.

**By contribution type**

| value | sources |
|---|---|
| technical | 3 |
| theoretical | 3 |
| empirical_quantitative | 2 |
| survey | 2 |
| normative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 3 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 3 |
| geographical_proxy:US | 2 |
| US | 1 |

**By year**

| value | sources |
|---|---|
| 2021 | 1 |
| 2024 | 1 |
| 2025 | 1 |
| 2026 | 1 |

## What the sources do not address

- No interpretive claim on CPT-case-based-reasoning. [ABS-1378] candidate readings: gap_in_literature | extraction_shadow | tacit_link

Explicit questions occurring verbatim in claim or premise text and answered by no claim on this concept:
- "Explanations of the presence and absence of particular factors could be delivered by extending an issue-based explanation dialogue so that the user may ask WHY?" — raised in [CLM-0004-005] [ABS-1379] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- "of any factor used to explain an issue and WHY NOT?" — raised in [CLM-0004-005] [ABS-1380] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

The explicit questions listed above are candidates for the register (query-graph skill); no hypothesis has been entered yet.
