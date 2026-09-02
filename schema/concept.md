# Node: Concept

A concept is a notion that claims are about. Three concept statuses exist: anchor concepts, given in advance, define the field; candidate concepts are created during extraction when claims are about a notion no anchor captures; a candidate is promoted to emergent status under the promotion rule below.


```yaml
id: CPT-outcome-prediction        # kebab-case, stable
label:                            # plain label (labeling rules: map-concepts skill)
status: anchor | candidate | emergent
concept_type:                     # the concept's family: legal_task | technique_class | normative_concern | other
definition:                       # one or two sentences; for candidate and emergent concepts, derived from the sources, with claim ids
aliases: []                       # alternative terms found in the sources; a term mapped from another language or legal tradition is recorded here with its source language
broader: []                       # concept ids
sources: []                       # source ids with at least one claim about the concept that is neither rejected nor superseded
deprecated: false                 # a merged or abandoned concept is marked deprecated with a pointer, never deleted (invariant: CLAUDE.md)
replaced_by:                      # concept id, only when deprecated
created:
```

Maintain `sources` yourself: when you map a claim to the concept (retrofit additions included), add the claim's source id to the list; when a rejection or supersession leaves a source with no counting claim about the concept, remove its id as part of executing that verdict or correction. The promotion check below reads exactly this list.

## Anchor concepts: the grid

```
legal_task
  CPT-information-retrieval        CPT-question-answering
  CPT-summarisation                CPT-outcome-prediction
  CPT-argument-mining              CPT-entity-and-citation-extraction
  CPT-drafting-and-generation      CPT-review-and-due-diligence
  CPT-ediscovery                   CPT-compliance-and-monitoring
  CPT-rule-formalisation           CPT-adjudicative-decision-support
  CPT-access-to-justice-tools      CPT-legal-education

technique_class
  CPT-symbolic-rule-based          CPT-case-based-reasoning
  CPT-computational-argumentation  CPT-classical-statistical-ml
  CPT-pre-llm-neural               CPT-large-language-models
  CPT-retrieval-augmented-or-tool-using
  CPT-agentic-systems              CPT-neuro-symbolic-hybrid

normative_concern
  CPT-accuracy-and-reliability     CPT-explainability-and-transparency
  CPT-fairness-and-non-discrimination
  CPT-due-process-and-fair-trial   CPT-accountability-and-liability
  CPT-privacy-and-data-protection  CPT-professional-responsibility
  CPT-autonomy-and-human-oversight CPT-access-to-justice
  CPT-rule-of-law-and-legitimacy   CPT-cost-efficiency-labour
  CPT-environmental-cost           CPT-security-and-misuse
```

Map every claim to at least one concept, and to at most 3 concepts per `concept_type` value, `other` included. Leave any concept_type the claim does not engage absent.

The grid of concepts is restricted by design. It excludes every notion that the whole corpus would trigger. 
A concept attaching to nearly every source discriminates nothing — spotting such a false hub is a team judgment, made from `coverage.md`'s claims-per-concept table and executed as a team-directed deprecation (below) — which is why the subject the corpus is defined by does not appear here. Candidate concepts absorb what the grid does not reach (creation and type assignment: the `map-concepts` skill), and the promotion rule below decides which of them the field actually supports. The `concept_type`also drive the two-dimensional maps of the field (legal task against technique class, normative concern against claim jurisdiction) in `coverage.md`. How the grid was arrived at, and how it is to be checked against the corpus, belong to the review protocol.

The rules for mapping claims to concepts and creating candidate concepts are in the `map-concepts` skill. Promotion (candidate to emergent) is mechanical, never a mapping judgment: check and apply it once per batch, at the `ingest-source` batch close-out, counting every addition made during the batch (retrofit additions included). Promote when the concept's `sources` list (above) holds three independent sources — independent means no two sharing an author, comparing author lists as printed. "The moment a candidate reaches the threshold" means the batch that brings the third independent source, never mid-extraction. Deprecation is a team decision: execute one only when the team requests it, never on your own judgment. Record every promotion and deprecation in the log.
