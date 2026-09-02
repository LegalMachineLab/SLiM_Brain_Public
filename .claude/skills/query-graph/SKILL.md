---
name: query-graph
description: Use when answering any question about the literature from the graph ("what does the literature say about X", questions about legal instruments, gaps, trends, disagreements). Covers the retrieval filters, the two-part answer, absence statements, and the hypothesis register.
---

# Query the graph and keep the hypothesis register

Answer questions in analysis mode (CLAUDE.md) and write nothing produced here into the claim record. Coverage tables and the index are current as of the last batch close-out (regeneration timing: `ingest-source`). Mint and stamp the session's run_id per `schema/SCHEMA.md`.

## When asked a question about the literature

1. Retrieve under the bounded path. Read `wiki/index.md` and the concept registry (`map-concepts`, Retrieval discipline) first. Then read `wiki/claims/claims.jsonl` filtered by whichever of concept, claim type, and jurisdiction the question fixes (bounded retrieval: CLAUDE.md). Then read `wiki/graph/edges.jsonl` filtered by the retrieved claim ids, and `wiki/absences.jsonl` filtered by the concepts the question touches. Every claim in the record is what its source argues (`schema/claim.md`), so "what does the literature say about X" cannot silently return positions sources cite in order to reject.
2. Answer with claim ids after every statement. State the jurisdictions and years the answer rests on. State the claim types (a normative answer is not a descriptive one). Exclude claims and edges from the answer per the exclusion scope in `schema/claim.md` (Verification vocabulary).
3. Give the answer in two parts: first what rests on claims and extracted edges; then, under a separate heading, what rests on inferred edges (`schema/edges.md`), with their plausibility. Never blend the two.
4. State what the corpus does not contain on the question. Give every gap the answer states an ABS record, created or cited per the create-or-cite rule in `schema/absences.md`. If a retrieved ABS record's absence is now answered by the claims you retrieved, mark it lapsed per `schema/absences.md` instead of citing it. Distinguish "no source addresses this" from "sources address this but disagree".
5. Answer from the corpus alone. When the corpus cannot answer the question, say so.
6. Record in `wiki/hypotheses.md` any trend or contradiction the answer suggests that is not yet in the wiki. For a gap, add a `hypotheses.md` entry only when the gap grounds a testable conjecture beyond the ABS statement itself; list the ABS ids it rests on in its `absences` field (the gap's ABS record from step 4 exists either way). If the answer is substantive enough to be reused, file it as a synthesis page (`write-wiki` skill). Do not edit concept pages from a query.

Answer questions about legal instruments (for example "what does the literature say about Article 5 of the AI Act?") by filtering `legal_reference` and, where populated, `legal_reference_normalised`, then proceed as above.

## Hypothesis register

`wiki/hypotheses.md` holds conjectures about the literature that cannot yet be settled from the corpus. Each entry:

```yaml
id: HYP-0001
date:
statement:                        # for example "No source addresses liability for hallucinated citations under the law of a civil-law jurisdiction"
concepts: []                      # concept ids the conjecture is about; retest triggers below
absences: []                      # ABS ids the conjecture rests on, when it rests on absences
query:                            # the filter on claims.jsonl that would confirm or refute it
graph_state:                      # number of sources, claims, edges at the time; schema version; model; run id
status: open | confirmed | refuted
evidence: []                      # claim ids
retests: []                       # list of {date, run_id, retest_type: query_sharpened | corpus_updated | model_changed, result, evidence}
```

Retest an open hypothesis in exactly two cases: when a query session touches its concepts, and when the team asks — a standing sweep is neither. To retest: re-run the hypothesis's stored `query`. If new claims answer it, append a retest entry with its `retest_type`, update `status` and `evidence`, and add a line to `wiki/log.md`. Keep every entry; delete none. A retest after sharpening the query tells whether a finding was an artifact of how it was asked; a retest after adding sources tells whether it was an artifact of when; a retest after a model change is not evidence about the field — label it as such.
