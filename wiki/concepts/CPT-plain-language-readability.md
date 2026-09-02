---
id: "CPT-plain-language-readability"
label: "Plain language and readability"
status: "candidate"
concept_type: "legal_task"
definition: "Assessing or improving the readability and plain-language quality of legal texts such as statutes, including metrics that operationalise drafting guidelines (motivating claims: CLM-0002-003, CLM-0002-004)."
aliases: ["readability metrics", "plain legal language"]
broader: []
sources: ["SRC-0002"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Plain language and readability

_Status: candidate; family: legal_task._

## Definition

Assessing or improving the readability and plain-language quality of legal texts such as statutes, including metrics that operationalise drafting guidelines (motivating claims: CLM-0002-003, CLM-0002-004).

Aliases: readability metrics, plain legal language.

## Claims about the concept

### Descriptive

**CA, US, GB, EU**

- Alschner et al. (2020) state that Several Anglo-American jurisdictions have recently passed guidelines and laws requiring statutes to be written in plain language, building on decades of scholarly work that urges legal drafters to use shorter, simpler sentences, ordinary words in their normal sense, and the active voice. [CLM-0002-001]. — jurisdiction: CA, US, GB, EU (cumulative); basis: legislation; positive form: trend

**US-NC, US-FL, US-OR**

- Alschner et al. (2020) state that There is a disconnect between the domain-specific principles set out in plain legal language laws, guidelines and scholarship and the way legal readability is checked in practice, which relies on generic metrics developed outside the legal context such as Flesch-Kincaid scores; North Carolina, Florida and Oregon, for example, have enacted legislation requiring government documents to meet a minimum Flesch-Kincaid score. [CLM-0002-002]. — jurisdiction: US-NC, US-FL, US-OR (cumulative); basis: legislation; positive form: existence

### Empirical

**geographical_proxy:US, geographical_proxy:NZ, geographical_proxy:AU, geographical_proxy:GB, geographical_proxy:ZA**

- Alschner et al. (2020) report that On an original dataset of statutes from five Anglo-American jurisdictions, each in its originally enacted version and a plain language rewrite, rules-based readability metrics derived from plain language guidelines track the changes between the versions: the rewrites show a significant decrease of 'shall' with a concomitant increase of 'must', and use fewer compound phrases, fewer nominalizations, less passive voice, fewer total words and less legalese than the original versions. [CLM-0002-005]. — jurisdiction: geographical_proxy:US, geographical_proxy:NZ, geographical_proxy:AU, geographical_proxy:GB, geographical_proxy:ZA (cumulative); basis: dataset_or_experiment
- Alschner et al. (2020) report that Results on before-and-after plain language rewrites of statutes suggest that rules-based readability metrics derived from plain language guidelines provide a more holistic and nuanced representation of a statute's readability than traditional techniques such as Flesch-Kincaid scores, and can help drafters review or rewrite statutes on the basis of plain language criteria. [CLM-0002-006]. — jurisdiction: geographical_proxy:US, geographical_proxy:NZ, geographical_proxy:AU, geographical_proxy:GB, geographical_proxy:ZA (cumulative); basis: dataset_or_experiment
- Alschner et al. (2020) report that Rules-based identification of the more complex plain language features (nominalizations, compound phrases and conditional phrases) approximates but does not perfectly match manual feature detection even after iterative refinement, whereas simple features such as shall/must, total word count and all-caps are identified well; in particular, detecting nominalizations by typical word endings overcounts words that have nominalization endings but no verb as root ('business') and valid nominalizations that are not used in problematic ways ('information'). [CLM-0002-007]. — jurisdiction: geographical_proxy:US, geographical_proxy:NZ, geographical_proxy:AU, geographical_proxy:GB, geographical_proxy:ZA (cumulative); basis: dataset_or_experiment
- Alschner et al. (2020) report that Sentence counts on statutory text are initially unreliable because of incorrect sentence boundary detection, but these errors can be addressed by pre-processing the text to eliminate confounding punctuation, namely external references with problematic punctuation, list elements and numerical characters. [CLM-0002-008]. — jurisdiction: geographical_proxy:US, geographical_proxy:NZ, geographical_proxy:AU, geographical_proxy:GB, geographical_proxy:ZA (cumulative); basis: dataset_or_experiment

### Methodological

**general**

- Alschner et al. (2020) argue that Generic readability metrics such as Flesch-Kincaid scores, which assess readability by counting syllables per word and words per sentence, are problematic proxies for how effectively drafters follow plain language guidelines in statutes: they capture plain legal language recommendations at best only indirectly and at worst may be negatively correlated with them, and beyond shorter words and sentences they give drafters no specific guidance on how to write more readable texts. [CLM-0002-003]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Alschner et al. (2020) argue that Plain language drafting guidelines can be operationalized for statutory readability through a rules-based approach that detects lexical (shall/must, legalese), grammatical (compound phrases, conditional phrases, nominalizations), stylistic (passive voice, all-caps) and structural (word, sentence and syllable counts) properties of statutory text, the properties being chosen by ranking the recommendations of English-language plain language scholarship and drafting guidelines by frequency and focusing on top-ranking principles that are difficult to evaluate manually. [CLM-0002-004]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Alschner et al. (2020) argue that Because plain language guidelines and the formatting of statutory texts vary across jurisdictions, rules-based readability metrics built from one set of jurisdictions' guidelines likely require adaptation for use in different jurisdictions. [CLM-0002-009]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Alschner et al. (2020) argue that Rules-based readability assessment of statutes could be complemented with machine learning: rules suit prominent plain language guidelines that are simple to implement (e.g. shall/must), whereas more complex features such as problematic nominalizations require a more nuanced approach, for which human expert labelling scaled through machine learning classifiers offers an alternative; in combination, the two approaches provide a scalable means to operationalize plain language assessments of statutes. [CLM-0002-010]. — jurisdiction: general [jurisdiction inferred]; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 1; claims: 10.

**By contribution type**

| value | sources |
|---|---|
| empirical_quantitative | 1 |
| technical | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| CA | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| CA | 1 |
| EU | 1 |
| GB | 1 |
| US | 1 |
| US-FL | 1 |
| US-NC | 1 |
| US-OR | 1 |
| general | 1 |
| geographical_proxy:AU | 1 |
| geographical_proxy:GB | 1 |
| geographical_proxy:NZ | 1 |
| geographical_proxy:US | 1 |
| geographical_proxy:ZA | 1 |

**By year**

| value | sources |
|---|---|
| 2020 | 1 |

## What the sources do not address

- No interpretive claim on CPT-plain-language-readability. [ABS-1431] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No normative claim on CPT-plain-language-readability. [ABS-1432] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No conceptual claim on CPT-plain-language-readability. [ABS-1433] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No predictive claim on CPT-plain-language-readability. [ABS-1434] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
