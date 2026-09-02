---
id: "CPT-retrieval-augmented-or-tool-using"
label: "Retrieval-augmented or tool-using systems"
status: "anchor"
concept_type: "technique_class"
definition: "Language models combined with retrieval, external knowledge sources, or tools at inference time."
aliases: []
broader: []
sources: ["SRC-0011", "SRC-0013", "SRC-0019", "SRC-0024", "SRC-0029", "SRC-0030", "SRC-0034", "SRC-0042"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Retrieval-augmented or tool-using systems

_Status: anchor; family: technique_class._

## Definition

Language models combined with retrieval, external knowledge sources, or tools at inference time.

## Claims about the concept

### Descriptive

**CN**

- Hu et al. (2024) state that A legal case retrieval module has rarely been integrated into existing legal-domain LLMs in civil law systems; Chinese legal-domain LLMs can currently only answer users on the basis of internal legal knowledge and externally retrieved legal articles, and cannot provide relevant legal cases for reference. [CLM-0029-003]. — jurisdiction: CN; basis: none_stated

**general**

- Khadloya et al. (2025) state that Retrieval-augmented generation reduces LLM hallucinations but does not fully eliminate them, and absolute guarantees on LLM-based query routing are impossible because of the stochastic nature of queries, even with a model instructed to abstain when retrieved content is insufficient. [CLM-0019-013]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Hou et al. (2025) state that The prevailing paradigm for using LLMs in legal retrieval is a two-stage retrieval and re-ranking framework, which has demonstrated significant improvements in legal case and law article retrieval. [CLM-0034-031]. — jurisdiction: general; basis: literature

### Normative

**general**

- Ribary et al. (2023) argue that Incorporating trusted knowledge sources into conventional LLMs is important for answering domain-specific queries; the insolvency-law results are presented as demonstrating this general point beyond the specific domain tested. [CLM-0011-002]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

### Empirical

**geographical_proxy:CN**

- Hu et al. (2024) report that Current legal article retrieval models used with legal-domain LLMs cannot ensure that all relevant legal articles are retrieved and all irrelevant ones excluded; missed articles reduce the completeness of the LLM's response, while irrelevant retrieved articles introduce noise that leads the LLM to produce incomplete, incorrect or inconsistent advice. [CLM-0029-001]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: argument
- Hu et al. (2024) report that In a user study on complex marriage consultation queries, the top three automatically retrieved legal articles were found not entirely correct for an average of 83% of queries (about 20% of responses incorrect because of noise from irrelevant articles, 25% incomplete because relevant articles were missing, 38% containing irrelevant information), whereas in 80% of cases users obtained correct responses by selecting the relevant legal articles and having the LLM regenerate its answer. [CLM-0029-010]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment
- Hu et al. (2024) report that In a user study, users reported that the legal article basis of the LLM's response was accurately identified for approximately 95% of queries, that cross-referencing responses with the identified articles let them swiftly determine whether a response was reliable, and that in about 73% of queries the response already contained parts of the legal article but not a full rephrasing, so that the displayed basis gave convenient access to the complete article. [CLM-0029-011]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment
- Hu et al. (2024) report that In a user study, retrieving relevant legal cases proved beneficial for 77% of consultation queries on average: although the retrieved cases might not exactly match the user's situation, they provide a reference point to gauge possible outcomes, and highlighting the sentences of a case relevant to the query significantly streamlines reading and improves reading efficiency. [CLM-0029-013]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2024) report that Most LLMs perform best at the Understanding and Logic Inference levels of legal cognitive ability: within a given context or when provided with the relevant legal provisions, LLMs can effectively use their inherent reasoning abilities to provide reasonable answers, although complex tasks such as multi-hop reasoning remain challenging. [CLM-0030-018]. — jurisdiction: geographical_proxy:CN; basis: dataset_or_experiment

**geographical_proxy:GB**

- Ribary et al. (2023) report that Adding a curated, domain-specific knowledge base (statutes, HMRC forms and case law retrieved into the prompt) to an LLM produces statistically more accurate answers to insolvency-law evaluation questions than the unmodified LLM: on an unseen test set of twelve questions marked with a law-school-style scheme, the knowledge-base-enhanced gpt-3.5-turbo scored 29-30% against 20% for raw gpt-3.5-turbo, and the enhanced gpt-4 scored 47% against 21% for raw gpt-4, both differences being significant under a two-sided paired t-test. [CLM-0011-001]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Ribary et al. (2023) report that The case-retrieval component of the Insolvency Bot, which combines zero-shot classification over text-embedding-ada-002 embeddings with keyword matching, identified the correct cases with 49% precision and 57% recall on the training questions and performed slightly worse on the test questions, with 24% precision and 33% recall. [CLM-0011-010]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment
- Xie et al. (2024) report that Including few-shot examples that share jurisdiction codes with the target case improves the outcome-prediction F-score of large language models more effectively than randomly sampled examples, showing that integrating task-related information into few-shot prompts enhances prediction performance. [CLM-0013-008]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

**geographical_proxy:IN**

- Khadloya et al. (2025) report that In a pilot on Indian charge sheets, pleadings and orders, the voice-guided anchor-first navigator cut time-to-relevance from minutes to seconds compared with manual navigation in a stock PDF reader: it halved time-to-relevance on temporal commands (10 s to 5 s) and reduced contextual queries from about 200 s to about 6 s, with median time-to-relevance dropping from 3-5 minutes to 10-15 seconds (30-45 seconds including quick visual verification). [CLM-0019-009]. — jurisdiction: geographical_proxy:IN [jurisdiction inferred]; basis: dataset_or_experiment
- Khadloya et al. (2025) report that Retrieval mode significantly influences strict-hit F1 at paragraph or table-cell level on long Indian legal records: keyword search performs well on statute or party mentions, dense-only retrieval aids paraphrase but misses exact citations, a simple hybrid improves further, and a windowed late-interaction plus keyword variant achieves the best strict-hit F1 within the same latency budget. [CLM-0019-010]. — jurisdiction: geographical_proxy:IN [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:US**

- Nay et al. (2023) report that Giving an LLM more legal text, and legal text more relevant to the specific tax question asked (moving from no source material, through similarity-search retrieval, to the correct 'gold truth' source), weakly increases answer accuracy for most models. [CLM-0024-004]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) report that LLMs, particularly GPT-4 combined with the correct legal texts, few-shot and chain-of-thought prompting, can answer tax law questions at high levels of accuracy but not yet at expert tax lawyer level; a professional tax lawyer would be expected to answer such questions with near-perfect accuracy. [CLM-0024-005]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) report that The similarity-search retrieval pipeline used (out-of-domain GTR-large embeddings over subsection-level vector databases of the U.S. Code and CFR, with default hyperparameters) failed to supply the most relevant 'gold truth' sources to the LLM a significant portion of the time, as shown by GPT-4's clear performance boost when given the gold-truth documents instead; better retrieval will be important where humans do not supply the exact legal documents. [CLM-0024-011]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Predictive

**GB**

- Ribary et al. (2023) argue that An LLM-based system that triages potential insolvency cases for stakeholders of micro, small and medium enterprises at a competency comparable to a Level 6 or 7 law student could, if successful enough, help solo practitioners and smaller law firms, which often lack sufficient expertise in this area of law, to expand the scope of their services. [CLM-0011-004]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

**general**

- Ribary et al. (2023) argue that A knowledge-base-enhanced LLM system for insolvency queries has the potential to be expanded to other jurisdictions and to cross-jurisdictional queries, and can be further improved by matching on-point legal information to user queries. [CLM-0011-011]. — jurisdiction: general [jurisdiction inferred]; basis: none_stated
- Ribary et al. (2023) argue that Because insolvency law is a fairly stable area of law in which legislative changes are rare, implementing a curated-knowledge-base system of the Insolvency Bot kind may be more challenging in areas of law subject to more rapid legislative change, such as immigration law. [CLM-0011-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hou et al. (2025) argue that Retrieval-augmented generation may be an important component for the interpretability of LLM-based approaches in the legal domain. [CLM-0034-027]. — jurisdiction: general; basis: literature

### Methodological

**general**

- Khadloya et al. (2025) argue that A judge-facing AI interface should show only passages grounded in visible anchors in the document, never free text, and should offer a disambiguation list or withhold an answer when evidence is insufficient; this grounding and abstention keeps evidence verifiable and auditable and mitigates the bias and overconfidence risks of generative models. [CLM-0019-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hu et al. (2024) argue that Visually presenting, for each sentence of an LLM's legal advice, the legal article that serves as its basis (found by similarity matching with a legal-domain fine-tuned embedding model) lets users verify the reliability of the response and trust the advice; a sentence for which no legal basis is found can be viewed as a warning that the sentence may be incorrect. [CLM-0029-005]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hu et al. (2024) argue that Allowing users to participate in legal article retrieval by interactively selecting, from the top retrieved articles, those that fit their situation increases the consistency between the user's situation and the legal articles the LLM refers to, enabling the LLM to generate more complete and accurate responses while avoiding noise from irrelevant articles. [CLM-0029-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hammond (2023) argue that Systems built from a synthesis of data, analytics, and language models can be both expressive and truthful: they leverage the fluency at the core of language models while providing access to knowledge, and the inference it supports, that lies well beyond the reach of language models alone. [CLM-0042-003]. — jurisdiction: general [jurisdiction inferred]; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 8; claims: 25.

**By contribution type**

| value | sources |
|---|---|
| technical | 7 |
| empirical_quantitative | 6 |
| theoretical | 3 |
| doctrinal | 1 |
| empirical_qualitative | 1 |
| survey | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| CN | 2 |
| GB | 2 |
| general | 2 |
| IN | 1 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 5 |
| geographical_proxy:CN | 2 |
| geographical_proxy:GB | 2 |
| CN | 1 |
| GB | 1 |
| geographical_proxy:IN | 1 |
| geographical_proxy:US | 1 |

**By year**

| value | sources |
|---|---|
| 2023 | 3 |
| 2024 | 3 |
| 2025 | 2 |

## What the sources do not address

- No interpretive claim on CPT-retrieval-augmented-or-tool-using. [ABS-1443] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No conceptual claim on CPT-retrieval-augmented-or-tool-using. [ABS-1444] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
