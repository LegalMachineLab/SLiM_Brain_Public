---
id: "CPT-ediscovery"
label: "E-discovery"
status: "anchor"
concept_type: "legal_task"
definition: "Identifying responsive or relevant documents in litigation document review."
aliases: []
broader: []
sources: ["SRC-0027", "SRC-0046", "SRC-0049"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# E-discovery

_Status: anchor; family: legal_task._

## Definition

Identifying responsive or relevant documents in litigation document review.

Conceptual claims on this concept, each with its source:
- Mahoney et al. (2021): In legal document review a document is considered responsive when any portion of it contains responsive information, which is not always true of other text classification tasks such as topic classification, where the entire document may concern the topic; consequently, locating the responsive text snippets in a responsive document would let attorneys easily evaluate a model's document classification decisions. [CLM-0027-007]

## Claims about the concept

### Descriptive

**US**

- Mahoney et al. (2021) state that Although attorneys have used machine learning text classification (predictive coding) for more than ten years to cull large volumes of electronically stored data and identify responsive documents, reducing the discovery costs of legal matters, the technology faces a perception challenge: lawyers sometimes regard it as a 'black box', because typically no extra information is provided to explain why documents are classified as responsive. [CLM-0027-008]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**general**

- Mahoney et al. (2021) state that The three rationale-identification methods differ in implementation effort: the Document-Level Model Method is the simplest because it requires no extra work, the Snippet Model Method is also simple but takes more time to score each snippet, and the Iterative Snippet Model Method takes significantly more time because of the training iterations required to reach the final snippet model, while each method identifies rationales reasonably well. [CLM-0027-014]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2019) state that Existing studies of active learning for legal document review assume human review of all documents the predictive model identifies as relevant and focus on expediting that process through continuous prioritization until target recall is reached; there is a lack of studies focusing on Simple Active Learning and on how to most efficiently train an active learning model that achieves a high level of recall with minimal human review of training documents. [CLM-0046-013]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Mahoney et al. (2019) state that The MID_75RC strategy, which selects additional training documents nearest the cut-off score that yields 75 percent recall of all responsive documents, is a novel active learning selection strategy not previously seen in the literature. [CLM-0046-016]. — jurisdiction: general [jurisdiction inferred]; basis: literature

**undetermined**

- Mahoney et al. (2019) state that In real-world legal matters where minimizing the time or cost of classifying a data set is paramount, for reasons such as monetary costs, sensitivity of data, or time to classify a population, the heavy human review of Continuous Active Learning is often less than ideal for lawyers classifying a population for production to an opposing party or for attorney-client privilege, and the strategy is instead to minimize human review effort and classify the population with minimal human intervention. [CLM-0046-014]. — jurisdiction: undetermined; basis: argument
- Mahoney et al. (2019) state that In real-world legal document reviews, a recall of 75 percent is a commonly used minimum performance metric when classifiers are used to designate documents for production. [CLM-0046-015]. — jurisdiction: undetermined; basis: none_stated

### Interpretive

**US**

- Gridin (2026) read Fed. R. Civ. P. 37(e) as follows: Deploying standard black-box LLMs exposes corporations to spoliation risk under FRCP Rule 37(e), because generative sessions are ephemeral and chat histories are routinely overwritten or lost through context window degradation, so that an auto-deleted drafting history of a contested contract could be ruled an intentional destruction of evidence. [CLM-0049-026]. — jurisdiction: US; basis: legislation
- Gridin (2026) read Fed. R. Civ. P. 37(e) as follows: An immutable micro-ledger in which every human prompt, every LLM generation, and every Linear AI validation is cryptographically hashed and appended to the document's metadata makes a 'lost chat history' technically impossible, ensures preservation of electronically stored information, and lets a subpoenaed corporation produce its Codification Reference Directory so that a judge can reconstruct the document's generative history, insulating the corporation from FRCP Rule 37(e) sanctions. [CLM-0049-027]. — jurisdiction: US; basis: argument

**general**

- Mahoney et al. (2019) read E-discovery as follows: The conflicting conclusions of Cormack and Grossman (that top-scored document selection consistently outperforms other active learning strategies) and of Chhatwal et al. (that always selecting the highest-scoring documents may not be the most efficient approach) are due to evaluating the selection strategies differently, on the training set alone versus on both the selected documents and the documents classified by the model, and both are understandable given the dual purpose of active learning: quickly finding as many relevant documents as possible and training an effective final model in as few rounds as possible. [CLM-0046-012]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Normative

**undetermined**

- Mahoney et al. (2019) argue that Legal teams should consider the MID_75RC active learning selection strategy (selecting training documents nearest the 75 percent recall cut-off score) in their predictive coding process to help reduce review costs. [CLM-0046-007]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Empirical

**geographical_proxy:US**

- Mahoney et al. (2021) report that Both the Snippet Model Method and the Iterative Snippet Model Method outperform a document-level training classification method in identifying responsive text snippets (rationales) in responsive documents: on three datasets from real legal matters they identified 50% more responsive documents than the document-level model at the [0.9, 1] snippet-score threshold, and on Datasets A and C they achieved much higher average document-score reductions when the identified rationales were removed (0.7 and 0.67 versus 0.47 on Dataset A; 0.52 and 0.46 versus 0.34 on Dataset C), while on Dataset B all three models achieved similar reductions slightly above 0.3. [CLM-0027-002]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that The accuracy of the document-level model on the document classification task has an important impact on the rationale detection performance of the two snippet model methods: the snippet methods perform much better than the document-level model only when the document model is accurate, because responsive training snippets are identified by the document-level model, so an inaccurate document model yields many misidentified responsive training snippets that degrade the trained snippet model. [CLM-0027-003]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that The Snippet Model Method almost always performs slightly better than the Iterative Snippet Model Method at identifying rationales, probably because classification errors propagate through the sequence of models the iterative method builds, starting from a document model that is never 100% accurate. [CLM-0027-004]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that Snippet models always remove more tokens as identified rationales than document-level models, which means they detect more rationales per document, and this implies that the higher document-score reductions achieved by snippet models are partly caused by the larger number of rationales they identify. [CLM-0027-005]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that It is feasible to build machine learning models that automatically identify rationales without using annotated text snippets for training, and automating the identification of training text snippets without human review could make the application of snippet-trained predictive models a practical approach in legal document review, since snippet-trained models have higher precision than models trained on whole documents but manually annotating training snippets is not generally practical during a review. [CLM-0027-009]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Mahoney et al. (2021) report that For the Snippet and Iterative Snippet models, removing snippets with higher snippet scores in most cases produces larger average document-score reductions, and the reductions in the [0.9, 1] snippet-score threshold are much higher than in the other threshold ranges. [CLM-0027-013]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

**undetermined**

- Mahoney et al. (2019) report that Seed set selection strategies have only a very modest impact on the performance of active learning strategies in predictive coding, especially after many rounds of active learning. [CLM-0046-001]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Among active learning document selection strategies, the top-ranked (TOP) strategy is the most sensitive to the seed set selection strategy, which implies that in the Continuous Active Learning protocol the seed set selection strategy has an impactful role and should be considered carefully. [CLM-0046-002]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that On a low richness document population, the seed set selection strategy has a greater impact on active learning performance, and judgmental seed set selection strategies using keywords or clustering outperform randomly selected seed sets in the early rounds. [CLM-0046-003]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Active learning selection strategies such as uncertainty sampling (selecting documents with scores nearest 0.5) and random selection can generate an effective predictive coding model within fewer rounds than the popular top-ranked (TOP) selection strategy. [CLM-0046-004]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Selecting additional training documents nearest to the model's cut-off score for 75 percent recall (the MID_75RC strategy) performs best in almost all experimental scenarios, and would be the most effective active learning strategy when the objective is to achieve 75 percent recall. [CLM-0046-005]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that In the first 50 rounds of active learning, the MID_75RC strategy consistently requires less review to reach 75 percent recall than the top-ranked (TOP) strategy across all four data sets, with a maximum saving close to 20 percent of the document population. [CLM-0046-006]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that The dominant factor in reaching the optimum performance round (the earliest round at which the review required to reach 75 percent recall is lowest) is the active learning document selection strategy, not the seed set selection strategy: random, uncertainty (MID-50) and MID_75RC strategies consistently take fewer rounds to reach the optimum round, and fewer rounds to reach a satisficing goal within 5, 10 or 15 percent of the optimum. [CLM-0046-008]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that When data sets with extremely low richness are excluded, training with documents nearest the 75 percent recall cut-off score (MID_75RC) results in significantly higher performing models in early training rounds such as round 10 or 20, rounds often associated with stopping points for Simple Active Learning; in all three data sets with richness above 10 percent, MID_75RC reached performance within roughly 10 percent of the optimum within 10 rounds of active learning. [CLM-0046-009]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Mahoney et al. (2019) report that Seed sets derived from keyword search have a higher richness (positive class rate) than the overall data set, while randomly sampled seed sets generally have a richness similar to that of the overall data set. [CLM-0046-017]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Conceptual

**general**

- Mahoney et al. (2021) argue that In legal document review a document is considered responsive when any portion of it contains responsive information, which is not always true of other text classification tasks such as topic classification, where the entire document may concern the topic; consequently, locating the responsive text snippets in a responsive document would let attorneys easily evaluate a model's document classification decisions. [CLM-0027-007]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Predictive

**US**

- Mahoney et al. (2021) argue that Incremental improvement in the precision of a text classification model at certain recall rates can have a significant impact on the cost of the legal document review process; for a matter in which a model identifies 1 million responsive documents for review, a 5 percent improvement in precision could result in cost savings of at least $50,000. [CLM-0027-010]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**general**

- Mahoney et al. (2021) argue that Because training documents in a legal document review matter can contain tens of thousands of tokens, most of which are likely not responsive content, document-level models trained on such documents may be less accurate in identifying short responsive text snippets than a method that derives its training data at the snippet level. [CLM-0027-011]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Methodological

**general**

- Mahoney et al. (2021) argue that Two machine learning methods, the Snippet Model Method and the Iterative Snippet Model Method, can train models that locate responsive text snippets (rationales) within responsive documents in legal document review without using human-annotated training text snippets. The Snippet Model Method applies a document-level text model to score all overlapping text snippets of the training documents, selects high-scoring snippets from responsive documents and randomly selected snippets from non-responsive documents as training data, and trains a snippet-level detection model on them; the Iterative Snippet Model Method repeats this while halving the snippet size at each iteration until a user-defined minimum size is reached. [CLM-0027-001]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2021) argue that When no labeled text snippets are available, rationale detection models cannot be evaluated with conventional metrics such as precision and recall; they can instead be evaluated by measuring the reduction in a document's classification score when the identified rationales are removed from it, together with the number of responsive documents for which rationales are detected, the model with the higher average score reduction being considered the better rationale identifier. [CLM-0027-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2021) argue that Prediction-based explanations that provide a vector of real-valued weights over features are not ideal for text classification because of the high dimensionality of the feature space; since a document usually belongs to a category because some passages of its text support the classification, a small portion of the document text can instead serve as evidence justifying the classification decision. [CLM-0027-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2019) argue that Focusing active learning training around the dynamic recall cut-off score from round to round makes sense in theory: documents just above the cut-off score are the positives the model includes with the least certainty, offering the most opportunity to improve precision, and documents just below it are the excluded negatives with the highest richness, offering the most opportunity to improve recall. [CLM-0046-010]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mahoney et al. (2019) argue that In an active learning scenario, the percentage of documents requiring review to achieve a target recall is computed after each round over two sets of documents, those selected and reviewed during training and those the model categorizes as positive at its cut-off score, because as rounds increase the documents reviewed for training could constitute a considerable portion of the population requiring review, unlike in passive learning where they have a negligible impact. [CLM-0046-011]. — jurisdiction: general [jurisdiction inferred]; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 3; claims: 33.

**By contribution type**

| value | sources |
|---|---|
| technical | 3 |
| empirical_quantitative | 2 |
| doctrinal | 1 |
| normative | 1 |
| theoretical | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| US | 3 |
| CoE | 1 |
| EU | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| US | 2 |
| general | 2 |
| geographical_proxy:US | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2019 | 1 |
| 2021 | 1 |
| 2026 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.
