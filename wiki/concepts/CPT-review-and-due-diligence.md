---
id: "CPT-review-and-due-diligence"
label: "Review and due diligence"
status: "anchor"
concept_type: "legal_task"
definition: "Reviewing documents (contracts, filings) for risks, clauses, or issues."
aliases: []
broader: []
sources: ["SRC-0026", "SRC-0037", "SRC-0048"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Review and due diligence

_Status: anchor; family: legal_task._

## Definition

Reviewing documents (contracts, filings) for risks, clauses, or issues.

## Claims about the concept

### Descriptive

**general**

- Guha et al. (2023) state that Interpretation tasks, and clause classification tasks in particular, are among the most studied and practically useful legal tasks for LLMs because they capture an actual current-day use case: manual review of long legal documents requires legal training and is extremely expensive, which raises access-to-justice concerns since most individuals cannot consult lawyers before entering agreements that may contain predatory or unconscionable terms. [CLM-0026-028]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Wang et al. (2026) state that ContractNLI is the only publicly available dataset of real legal contracts for entailment and a notable exception to the tendency of legal datasets to simplify text or focus on narrow subfields, but its labels reflect legal interpretation rather than strict logical entailment, and legal datasets in general rarely address the role of implicit assumptions in interpretation. [CLM-0037-014]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Normative

**general**

- Wang et al. (2026) argue that Legal ambiguity should be treated not as a failure of the system but as an inherent property of legal text that AI alone cannot resolve. A proposed lawyer-centred approach has SMT solvers surface Minimal Correction Subsets, the minimal set of axioms whose acceptance would shift a classification from Neutral to Entailment or Contradiction, and presents them to legal practitioners as structured entry points for resolving ambiguity, positioning the lawyer as the decision-maker for well-scoped interpretive questions and constraining human review to precisely the assumptions that matter rather than requiring exhaustive document-level verification. [CLM-0037-016]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Empirical

**general**

- Wang et al. (2026) report that The central challenge for faithful legal reasoning, by humans and LLMs alike, is that it is fundamentally unclear which assumptions are permissible: the boundary between valid inference and unjustified assumption is ambiguous. LLMs resolve this ambiguity by injecting ungrounded assumptions, while formal methods expose it through conservative reasoning. [CLM-0037-011]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:US**

- Guha et al. (2023) report that Large commercial LLMs are highly performant on legal interpretation tasks that involve binary classification over short clauses (balanced accuracy of at least 88% averaged across the 38 CUAD contract-clause tasks), but performance degrades on tasks with longer text sequences or multi-class classification (74-75% on one-to-two-page supply chain disclosures, 47.8% for GPT-4 on the multiple-choice MAUD merger tasks), and nearly all models struggle to label the legal role of a question or opinion excerpt among six or more categories. [CLM-0026-021]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

**undetermined**

- Wang et al. (2026) report that A substantial proportion of ContractNLI's original Entailment and Contradiction labels are not logically entailed under strict formal semantics. Manual re-annotation of 400 ContractNLI examples under formal entailment definitions produced a predominant shift from Entailment and Contradiction to Neutral (71 Entailment-to-Neutral and 18 Contradiction-to-Neutral transitions), revealing a systematic and measurable gap between pragmatic legal interpretation and strict formal entailment that reflects the prevalence of missing, unstated assumptions in real-world legal contract text. [CLM-0037-001]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Wang et al. (2026) report that Introducing formal structure improves LLM accuracy on legal contract entailment classification. LLM-based formal reasoning, in which the premise and hypothesis are autoformalized into first-order logic and the LLM is prompted to produce a classification by reasoning over the formal representation, achieves the highest accuracy for several of the five evaluated models, outperforming both pure LLM classification and the Z3 solver-based neuro-symbolic pipeline. [CLM-0037-002]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Wang et al. (2026) report that There is a consistent trade-off between benchmark accuracy and logical faithfulness in LLM legal entailment reasoning. The accuracy gains of LLM-based methods, particularly LLM reasoning over formal representations, do not imply faithful reasoning, because those methods achieve higher accuracy by leveraging implicit or unverified assumptions that are not grounded in the premise, whereas solver-based reasoning enforces strict logical validity and therefore produces more conservative outputs. [CLM-0037-003]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Wang et al. (2026) report that Across models and methods, the dominant error in LLM legal entailment classification is predicting Entailment for Neutral cases, while Entailment-Contradiction confusions are rare. This indicates that LLMs systematically introduce implicit assumptions to bridge missing information and that the primary difficulty lies in insufficient information rather than logical inconsistency, whereas solver-based reasoning shows the opposite tendency, frequently classifying cases as Neutral because explicit constraints are missing. [CLM-0037-009]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Wang et al. (2026) report that Human re-annotation of contractual entailment under strict logical definitions reaches substantial but imperfect inter-annotator agreement (81.0% agreement, Cohen's kappa 0.627), with disagreements concentrated between Entailment and Neutral. This shows that even human annotators struggle to determine whether a hypothesis is sufficiently supported by the premise and sometimes disagree on whether additional assumptions are required. [CLM-0037-010]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Chalkidis et al. (2021) report that The annotation practices of the CUAD contract-review dataset — mixing entity-level and paragraph-level answers within the same categories, annotating indirect mentions (party roles) instead of the actual entities, and including semi-redacted or fully redacted text — blur its task definition and introduce noise in training and evaluation; together with its limited number of annotations, these points seem to strongly affect the performance of Transformer models on CUAD (approximately 10-20% token-level F1 across all models tested), underestimating the models' true potential, which is why CUAD was excluded from LexGLUE. [CLM-0048-013]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Methodological

**general**

- Wang et al. (2026) argue that A legal entailment benchmark aligned with solver-based formal reasoning defines its labels formally: a hypothesis H is entailed by a premise P if P and not-H is unsatisfiable, contradicted if P and H is unsatisfiable, and all remaining cases are Neutral, where Neutral deliberately includes both semantically irrelevant cases and cases in which the premise is insufficient to support the inference without additional assumptions. [CLM-0037-013]. — jurisdiction: general [jurisdiction inferred]; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Jurisprudence at its operational core is binary and deterministic (a statute is active or repealed, a deadline met or missed, jurisdiction present or absent), whereas an LLM represents knowledge as a continuous latent space in which a hallucinated case name sits close to a real one; the Rule of Law and deterministic AI architecture are therefore convergent, and the Neuro-Symbolic Sandwich reveals the logic the law has always demanded rather than imposing an alien one. [CLM-0049-006] is in tension with the claim that The central challenge for faithful legal reasoning, by humans and LLMs alike, is that it is fundamentally unclear which assumptions are permissible: the boundary between valid inference and unjustified assumption is ambiguous. LLMs resolve this ambiguity by injecting ungrounded assumptions, while formal methods expose it through conservative reasoning. [CLM-0037-011] (inferred, medium). Note: One asserts the determinacy of law's operational core; the other finds the boundary of permissible assumptions in legal entailment fundamentally unclear even for humans.

## Distribution

Sources with claims on this concept: 3; claims: 12.

**By contribution type**

| value | sources |
|---|---|
| empirical_quantitative | 3 |
| technical | 3 |
| theoretical | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 2 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 2 |
| undetermined | 2 |
| geographical_proxy:US | 1 |

**By year**

| value | sources |
|---|---|
| 2021 | 1 |
| 2023 | 1 |
| 2026 | 1 |

## What the sources do not address

- No interpretive claim on CPT-review-and-due-diligence. [ABS-1445] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No conceptual claim on CPT-review-and-due-diligence. [ABS-1446] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No predictive claim on CPT-review-and-due-diligence. [ABS-1447] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
