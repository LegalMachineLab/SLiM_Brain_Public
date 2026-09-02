# Node: Claim

A claim is a central thesis or hypothesis that a paper advances as part of its contribution, especially when supported through arguments or empirical data.
It is one proposition — one contention that stands or falls together.
Every source claims something, so there is at least one claim per source.

```yaml
id: CLM-0001-003                  # <source id number>-<running number within source>
source: SRC-0001
statement:                        # one proposition, in English, in the source's own modality (is / should / may / found that); length and splitting per the one-proposition test below
premise:                          # the ground the source gives for the claim, in one sentence; when it is filled or empty: division of labour below
quotes: []                        # 1 to 3 anchors, each {quote, location, quote_translation?}: quote is a verbatim passage from the source's markdown conversion (the file the Source record's `file` field names), original language, at most 50 words, each anchor supporting a component of the one proposition — two anchors may corroborate the same component, but the anchor set must never stitch independent ideas into a proposition the source does not argue; location is a page number or, without pagination, section heading plus paragraph ordinal (e.g. "3.2, para 4"); quote_translation only when the original is not in English
claim_type:                       # descriptive | interpretive | normative | empirical | conceptual | predictive | methodological
positive_form:                    # set per "Definitions of positive_form" below
basis:                            # always filled — what the source offers for the claim: case_law | legislation | dataset_or_experiment | argument | literature | none_stated (the source offers no ground); dominant-ground rule under division of labour below
basis_qualifier:                  # only when basis is case_law: holding | dictum | unclear; records what the source claims the case stands on, not what is true
claim_jurisdiction: []            # legal system(s) the claim is about, in order of dominance; codes and the general | undetermined | geographical_proxy split in the extract-claims skill
jurisdiction_relation:            # only when claim_jurisdiction has more than one entry: eu_law_in_member_state | comparative | cumulative
jurisdiction_inferred: false      # true when the jurisdiction was assigned from context rather than stated by the source
legal_reference: []               # instruments and provisions the claim is about, as written in the source, e.g. "AI Act, Art. 5"; "GDPR, Art. 22"; "Mata v. Avianca (S.D.N.Y. 2023)"; empty when none
legal_reference_normalised: []    # canonical citation forms; filled by the team during verification; the model NEVER fills this field
temporal_reference:               # date or period of the legal or factual state the claim describes, when stated; otherwise "as_of_publication"
concepts: []                      # concept ids; count, per-family cap, and the never-impute rule in schema/concept.md
dataset:                          # dataset id when the claim rests on a dataset in the corpus; otherwise omit; see division of labour below
fidelity:                         # high | medium | low; bands under "Definitions of fidelity" below
verification_status: unverified   # always "unverified" when you write it; human vocabulary below
superseded_by:                    # set only when a correction or re-extraction replaces this claim with a new id — never at extraction; exclusion scope under Verification vocabulary below
extraction_model:
run_id:                           # the session's run id, shared by every record the session writes; format and minting defined once in schema/SCHEMA.md
schema_version:
```


## The one-proposition test

The test is semantic, never syntactic. Split two candidate parts into separate claims when a reader could accept one and reject the other, when they need different claim types or jurisdictions, or when an edge could attack one without touching the other. Keep them in one claim when they stand or fall together as a single contention. Sentence shape decides nothing: "LLMs hallucinate case citations, and courts should therefore sanction their unverified use" is one source sentence but two claims (empirical; normative — separately acceptable), unless one half is merely the ground for the other, in which case it belongs in the other's `premise`. Conversely, a multi-pronged thesis the paper argues as one position is one claim, stated across sentences, with an anchor per prong.

## Definitions of `fidelity`

`fidelity` is the SEMANTIC adherence of the statement to its anchor quotes — how fully their meaning warrants what the statement says. Textual overlap is irrelevant: a synthesized statement fully warranted by its quotes is `high`; a near-verbatim restatement that shifts the meaning is not.

- `high`: the anchors' meaning fully warrants the statement.
- `medium`: minor interpretive bridging connects the anchors to the statement.
- `low`: the statement rests on substantial interpretation of ambiguous or diffuse passages.

## Division of labour between neighbouring fields

Stated once so no pair is redundant:

- `basis` is the closed-list category of ground (what kind of support the source offers); `premise` is the free-text content of that ground in one sentence (which case, which provision, which result, which argument). Fill `premise` whenever the source states a ground; it is empty exactly when `basis` is `none_stated`. Keep a filled `premise` consistent with `basis`; when the source offers several kinds of ground, `basis` records the dominant one and `premise` may carry the others.
- `Claim.dataset` records, at claim level, that this claim rests on a dataset node; the `USES` edge records the source-level relation (semantics: `schema/edges.md`). The edge is derivable from the claim fields plus the introduction of the dataset; it is kept because the map is drawn at source level. The write gate checks the consistency of the two (schema/write-gate.md).
- `fidelity` (claim), `plausibility` (edge, schema/edges.md) and `jurisdiction_inferred` (claim) are three constructs and therefore three fields: semantic adherence of a statement to its anchor quotes, the graded plausibility of the relation an edge asserts (defined separately for extracted and inferred edges in schema/edges.md), and a marker that a jurisdiction was assigned from context. A single confidence field collapsing the three cannot be interpreted by a reader or scored by an evaluator.

## Definitions of `claim_type`

- `descriptive`: states what the law is, what courts or regulators do, or what a practice is. Lex lata.
- `interpretive`: offers a reading of a legal text, judgment, or concept that goes beyond restating it.
- `normative`: states what the law, policy, design, or practice should be. Lex ferenda. Markers: should, ought, must (where not quoting a legal text), we propose, we recommend, it is desirable.
- `empirical`: reports a finding from data, an experiment, a benchmark, interviews, or observation.
- `conceptual`: defines, distinguishes, or classifies a notion.
- `predictive`: states what will or is likely to happen.
- `methodological`: states how something should be studied, measured, or built.

## Definitions of `positive_form`

(Baude, Chilton and Malani 2017.) Set the field on every descriptive claim: choose one of the five forms when the claim describes what courts, legislators, or regulators do; write `not_applicable` on every other descriptive claim; omit the field on non-descriptive claims. The five forms: `general_rule` (courts generally decide X in way Y), `trend` (increasingly, over time), `split` (disagreement between courts or jurisdictions), `frequency` (courts have often confronted X), `existence` (at least one court has decided X).

## Verification vocabulary

`verification_status` takes exactly these values. You (the model) write only the first; human evaluators, identified in the record, write the rest.

- `unverified`: the state of every model-written claim.
- `verified`: an evaluator confirmed the statement against the source.
- `verified_with_correction`: the evaluator confirmed the substance but corrected the record; written on the OLD record when the correction is applied (steps below).
- `rejected`: the evaluator found the statement unfaithful to the source; the record stays in `claims.jsonl`, under the exclusion scope below.
- `unresolved`: the evaluators disagree and adjudication is pending.

Exclusion scope for rejected and superseded claims: exclude every claim that is rejected or carries `superseded_by` — and every edge touching such a claim — from all page sections (distribution counts included), candidate sets, coverage and structure tables, absence detection, and query answers. Keep the records and their edges untouched in the jsonl files: exclusion is a rendering rule, not a deletion. One listing survives: the evaluation section of the source page lists claims carrying a human verdict, rejected and corrected records included, because that section reports the evaluation itself, not the graph's content (`write-wiki`).

Human verdicts carry `verified_by` (evaluator identifier) and `verified_date`. Apply a communicated verdict only when it carries both; when the evaluator identifier or the date is missing, ask for them first. With this vocabulary the evaluation writes into the graph rather than beside it.

Apply verdicts — like deprecations and mapping changes — only when the team communicates them. Copying a communicated verdict verbatim into the record is among the sanctioned in-place updates listed in `schema/write-gate.md`. Applying a verdict includes its consequences. When applying a correction, you: (1) write the corrected record through the gate as a NEW claim id — never reuse the old id — with `verification_status: unverified`; (2) set `verification_status: verified_with_correction` and `superseded_by: <new id>` on the OLD record, and log the act; (3) run the new claim through ingest step 6 (`ingest-source`, Sequential processing); (4) mark stale every synthesis page resting on the superseded claim, and log the marking for the team; (5) regenerate every page owning the claim or owning any edge touching it (`write-wiki` ownership rules). When applying a rejection, you: (1) write `rejected`, with `verified_by` and `verified_date`, on the record; (2) apply steps (4) and (5) above to the rejected claim. Marking the stale page and logging it complete the verdict application; disposal of a stale page (rewrite or delete) follows the synthesis rules in `write-wiki`.
