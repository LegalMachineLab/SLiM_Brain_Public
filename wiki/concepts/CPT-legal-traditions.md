---
id: "CPT-legal-traditions"
label: "Legal traditions and their assumptions"
status: "emergent"
concept_type: "other"
definition: "Differences between civil-law, common-law and other legal traditions, and the assumptions AI and Law work makes about the legal system it is built on or generalises to (motivating claims: CLM-0014-017, CLM-0009-013)."
aliases: ["civil law versus common law", "drafting tradition"]
broader: []
sources: ["SRC-0007", "SRC-0009", "SRC-0014", "SRC-0029", "SRC-0030", "SRC-0034", "SRC-0035", "SRC-0036", "SRC-0043", "SRC-0047", "SRC-0048", "SRC-0049", "SRC-0050"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Legal traditions and their assumptions

_Status: emergent; family: other._

## Definition

Differences between civil-law, common-law and other legal traditions, and the assumptions AI and Law work makes about the legal system it is built on or generalises to (motivating claims: CLM-0014-017, CLM-0009-013).

Conceptual claims on this concept, each with its source:
- Li et al. (2024): Although the legal cognitive ability taxonomy is primarily designed for the Chinese legal system, it can be extended to legal tasks in other countries, because the six ability levels are universal across different legal systems. [CLM-0030-006]

Aliases: civil law versus common law, drafting tradition.

## Claims about the concept

### Descriptive

**CN**

- Hu et al. (2024) state that A legal case retrieval module has rarely been integrated into existing legal-domain LLMs in civil law systems; Chinese legal-domain LLMs can currently only answer users on the basis of internal legal knowledge and externally retrieved legal articles, and cannot provide relevant legal cases for reference. [CLM-0029-003]. — jurisdiction: CN; basis: none_stated

**EU, US**

- Gridin (2026) state that The global landscape of AI regulation is fracturing into two opposed paradigms: the European Union, through the AI Act, has codified strict ex-ante preventative control with pre-market audits and heavy fines, while the United States, following the repeal of Executive Order 14110 and the issuance of Executive Order 14179 in 2025, has embraced algorithmic deregulation that leaves AI safety to the market and ex-post tort liability; this places multinational legal entities in a structurally irresolvable compliance tension. [CLM-0049-018]. — jurisdiction: EU, US (comparative); basis: legislation; positive form: split
- Neumann et al. (2026) state that The EU and US approaches diverge: the EU Code of Practice operationalises system-level instructions as artefacts for evaluation practice by providing them to model evaluation teams, whereas the US framework positions system prompts as optional transparency artefacts without specifying how their behavioural effects should be assessed and more strongly implies that writing high-level normative commitments into system-level instructions can support alignment with articulated values. [CLM-0050-007]. — jurisdiction: EU, US (comparative); basis: legislation; positive form: split

**IN**

- Malik et al. (2022) state that In India's common law system a decision may not follow the statute exactly, since the judiciary may adopt its own interpretation and overrule existing precedents, which introduces subjectivity into the identification of rhetorical roles in a judgment; competition law and income tax law display a relatively greater degree of consistency and objectivity in judicial reliance on statutory provisions, and focusing on these domains reduces that subjectivity. [CLM-0007-005]. — jurisdiction: IN; basis: argument; positive form: general_rule

**IN, CN**

- Ali et al. (2021) state that An evidence information extraction approach designed for Chinese court records, which follow a relatively structured representation, may suit those records well but does not suit Indian court records, which contain descriptive and varied formats of the court proceedings. [CLM-0043-017]. — jurisdiction: IN, CN (comparative); basis: argument

**UA**

- Ovcharov (2026) state that Ukrainian legal text is hard for large language models because three factors compound: subword tokenizers fragment Ukrainian legal text at rates about 1.6 times higher than English, inflating prompt length and reducing effective context; Ukrainian morphological richness (seven cases, three genders, synthetic verb forms) creates surface variation invisible to English-trained models; and the civil-law reasoning pattern of statute application, rather than case precedent, differs from the common-law data that dominates LLM pretraining corpora, so that English benchmarks do not capture the reasoning it requires. [CLM-0035-003]. — jurisdiction: UA; basis: argument

**US, EU**

- Neumann et al. (2026) state that Emerging governance instruments in the United States (Executive Order 14319 and the OMB memorandum on Unbiased AI Principles) and the European Union (General-Purpose AI Code of Practice) treat system prompts as legible artefacts that can be disclosed, inspected and revised to support oversight, on the presumption that prompt language shapes system behaviour, so that regulators treat prompt language as a proxy for model performance. [CLM-0050-004]. — jurisdiction: US, EU (comparative); basis: legislation; positive form: general_rule

**general**

- T.Y.S.S. et al. (2024) state that Despite some recent diversification, virtually all AI & Law research comes from either civil law or common law backgrounds and makes corresponding assumptions about legal systems. [CLM-0014-017]. — jurisdiction: general; basis: none_stated
- Ovcharov (2026) state that Existing legal NLP benchmarks are overwhelmingly English-centric: the major benchmarks (LegalBench, LexGLUE, CUAD) are English-only and predominantly common-law, and multilingual efforts (LEXTREME, MultiLegalPile) cover EU languages but exclude Cyrillic-script jurisdictions and civil-law systems outside Western Europe, so failure modes in morphologically rich, non-Latin-script languages go undetected. [CLM-0035-001]. — jurisdiction: general; basis: literature

### Normative

**GB, BR**

- Briggs of Westbourne (2026) argue that In preparing for the tsunami of AI-generated cases, it is instructive to consider the approaches of jurisdictions that were early adopters of AI: without judging whether Brazil's rules are effective or sufficient, the Brazilian framework highlights the kinds of policy choices and problems that rules will have to address if civil courts and judges are to use AI platforms transparently and with public approval, and these ought to be thought about in earnest now. [CLM-0047-021]. — jurisdiction: GB, BR (comparative) [jurisdiction inferred]; basis: argument

**general**

- Hou et al. (2025) argue that Future studies should focus on multilingual legal LLMs or LLM-based frameworks that address linguistic differences between legal systems, to ensure broader applicability in transnational legal contexts. [CLM-0034-024]. — jurisdiction: general; basis: argument
- Ovcharov (2026) argue that Model selection for legal AI applications must be task-specific and jurisdiction-specific: practitioners should evaluate candidate models on jurisdiction-specific benchmarks rather than relying on evaluations in another language or on tokenizer statistics alone. [CLM-0036-007]. — jurisdiction: general; basis: dataset_or_experiment
- Chalkidis et al. (2021) argue that Because legal documents are typically written in the official language of their country of origin, there is an increasing need for developing legal NLP models for languages other than English; the current lack of legal NLP datasets in languages other than English (with the exception of Chinese) makes a multilingual extension of LexGLUE challenging. [CLM-0048-011]. — jurisdiction: general; basis: argument

### Empirical

**geographical_proxy:UA**

- Ovcharov (2026) report that The performance gap between Ukrainian and English legal benchmarks for frontier LLMs is task-dependent rather than uniform across all legal reasoning: Ukrainian case-type classification results (96-98%) are consistent with the above-90% accuracy frontier models reach on comparable LegalBench tasks, whereas Ukrainian case-outcome prediction (23-41% macro-F1) and cause category prediction (44-55%) show substantially more variance. [CLM-0035-013]. — jurisdiction: geographical_proxy:UA; basis: dataset_or_experiment

**geographical_proxy:UA, geographical_proxy:FR, geographical_proxy:NL, geographical_proxy:PL, geographical_proxy:CZ, geographical_proxy:LT**

- Ovcharov (2026) report that No single LLM dominates legal classification tasks across jurisdictions: model rankings shift with both task and jurisdiction, so a model recommended on the basis of English or French legal evaluation may perform poorly on Polish or Czech legal text. [CLM-0036-006]. — jurisdiction: geographical_proxy:UA, geographical_proxy:FR, geographical_proxy:NL, geographical_proxy:PL, geographical_proxy:CZ, geographical_proxy:LT (cumulative); basis: dataset_or_experiment

### Conceptual

**general**

- Li et al. (2024) argue that Although the legal cognitive ability taxonomy is primarily designed for the Chinese legal system, it can be extended to legal tasks in other countries, because the six ability levels are universal across different legal systems. [CLM-0030-006]. — jurisdiction: general; basis: argument

### Predictive

**general**

- Janatian et al. (2023) argue that The results on LLM pathway extraction may not generalise: they rest on Civil Code of Quebec articles, drafted in a civil-code tradition that aims at lay readability, so they may not translate to jurisdictions without that aim, and they may not replicate for very complex articles or articles that can only be read in conjunction with other articles. [CLM-0009-013]. — jurisdiction: general; basis: argument
- Li et al. (2024) argue that Because statute law systems and case law systems differ significantly in the interpretation of laws and the basis for decisions, the performance of LLMs may differ between the two legal systems, so findings from a benchmark that mainly covers a statute law system require further in-depth exploration in case law systems. [CLM-0030-025]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Because many systems are deployed on global platforms hosting foundation models, system prompt constraints set to satisfy one jurisdiction may be applied across borders by multinational vendors to reduce operational complexity, so that jurisdictions which did not adopt those requirements may nonetheless experience their effects; and if prompt requirements are perceived as functional, other jurisdictions may adopt similar approaches, in a dynamic resembling the Brussels Effect. [CLM-0050-020]. — jurisdiction: general; basis: argument

### Methodological

**general**

- Hou et al. (2025) argue that Building effective multilingual LLM-based legal approaches requires not only access to diverse legal corpora but also careful alignment with the legal doctrines of each jurisdiction, because such approaches face challenges from jurisdiction-specific laws, legal traditions and cultural contexts. [CLM-0034-023]. — jurisdiction: general; basis: argument
- Ovcharov (2026) argue that Existing legal NLP benchmarks either evaluate a single language or aggregate tasks that differ fundamentally from one jurisdiction to another, which makes cross-lingual comparison impossible: when the tasks differ, performance differences confound language ability with task difficulty. [CLM-0036-001]. — jurisdiction: general; basis: literature
- Ovcharov (2026) argue that Cross-lingual legal evaluation should draw from native judicial corpora in each jurisdiction rather than translate a single dataset, because native corpora preserve authentic legal language, jurisdiction-specific terminology and domain reasoning patterns that translation flattens. [CLM-0036-017]. — jurisdiction: general; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 13; claims: 22.

**By contribution type**

| value | sources |
|---|---|
| technical | 9 |
| empirical_quantitative | 8 |
| theoretical | 6 |
| normative | 4 |
| survey | 3 |
| doctrinal | 2 |
| empirical_qualitative | 2 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 6 |
| CN | 2 |
| IN | 2 |
| CA-QC | 1 |
| CoE | 1 |
| EU | 1 |
| GB | 1 |
| RU | 1 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 8 |
| CN | 2 |
| EU | 2 |
| IN | 2 |
| US | 2 |
| geographical_proxy:UA | 2 |
| BR | 1 |
| GB | 1 |
| UA | 1 |
| geographical_proxy:CZ | 1 |
| geographical_proxy:FR | 1 |
| geographical_proxy:LT | 1 |
| geographical_proxy:NL | 1 |
| geographical_proxy:PL | 1 |

**By year**

| value | sources |
|---|---|
| 2026 | 5 |
| 2024 | 3 |
| 2021 | 2 |
| 2022 | 1 |
| 2023 | 1 |
| 2025 | 1 |

## What the sources do not address

- No interpretive claim on CPT-legal-traditions. [ABS-1424] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
