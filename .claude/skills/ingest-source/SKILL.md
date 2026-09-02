---
name: ingest-source
description: Use when adding one or more new source files from raw/ into the knowledge graph. Orchestrates pre-checks per file (conversion, container, duplicate version, title), eight numbered steps per source — Source node, claim extraction, concept mapping, dataset nodes, CITES edges, cross-source claim edges, source/dataset pages, logging — and one batch close-out (concept pages, tables, lapse marking, promotion) after the last source. Covers sequential processing, set-asides, and bounded retrieval.
---

# Ingest a source

This skill orchestrates the whole pipeline. It delegates to four other skills: `extract-claims` (step 2), `map-concepts` (step 3), `create-edges` (steps 4–6), `write-wiki` (step 7). Invoke each at its step and follow it exactly. Apply the read-vs-inferred test in CLAUDE.md to every record, not to steps: steps 1–5 write only what passes the test as read; step 6 writes both kinds (edge vocabulary and grounding: `schema/edges.md`).

Draft first, write late: steps 1–4 draft their records in memory. Write nothing, and consume no id, until ALL of the source's claims have cleared step 3 (and step 4, where a dataset is involved); then gate-check and write each record (`schema/write-gate.md`), claims to `wiki/claims/claims.jsonl` — an adjudication set-aside then leaves no records behind. The Source and Dataset records follow the lifecycles in `schema/source.md` and `schema/dataset.md`.

## Pre-checks, for each new file in `raw/`

Work from the markdown conversion (`raw/<name>.md`); the PDF beside it is the original, never the ingest input. Run these checks before step 1:

- Ensure the markdown conversion exists: run the `convert-source` skill if it does not — it owns caching, the held-fixed tool, and tool-change logging. Fill `conversion_tool` at step 1 per `schema/source.md`.
- Check whether the file is a container (a full proceedings volume, an edited book, a journal issue) rather than one publication. Do not ingest containers; log them and stop. (An ingested container would enter the graph as a false hub connected to everything.)
- Check whether the file is another version of a source already in the corpus (preprint and published version, SSRN and arXiv twin). If a version of the source is already in the corpus, do not ingest the new file: add its identifier to the existing Source's `other_versions` and log it — swapping to a published version is a team decision, never an ingest act. When the source is new and several versions are on hand, ingest the published version, or the preprint only when no published version exists; record each other version in `other_versions` and log the choice.
- Take the title as `schema/source.md` directs.

## The eight steps, for each file that passes

1. Draft the Source record in memory (schema and lifecycle: `schema/source.md`). Assign it the next free id (find it by listing `wiki/sources/`) and the next `ingest_position`; fill every field from the document itself, `unknown` where you cannot.
2. Read the full text of the markdown conversion. Extract draft claim records following the `extract-claims` skill; write nothing yet (draft first, write late — above). When the harness provides clean-context subagents (CLAUDE.md), run this step in one, giving it only this source's `.md`, the `extract-claims` skill, and the schema files that skill names. Treat a source that yields no claims as an extraction failure, not a result (`schema/claim.md`): re-read and re-extract before proceeding.
3. Map each claim to concepts using the concept registry (defined in `map-concepts`, Retrieval discipline), following the `map-concepts` skill. Create candidate concepts only under its rules; creating one triggers its retrofit over existing claims (`map-concepts`, "Retrofit on creation"), whose edge generation runs at this ingest's step 6. Steps 2 and 3 together complete a claim record before submission (the gate requires concepts: `schema/concept.md`).
4. Draft Dataset records where applicable (schema and lifecycle: `schema/dataset.md`), each with its USES edge from the source (`create-edges` skill). The gate checks claim–dataset–USES consistency (`schema/write-gate.md`), so draft both before submitting the claim naming the dataset — this step interleaves with steps 2–3 when needed. In the post-clearance write batch, gate and append each USES edge before any claim naming its dataset.
5. Create CITES edges to sources already in the corpus: check the source's reference list and in-text citations against the `title` and `authors` frontmatter of the pages in `wiki/sources/`, and create a CITES edge for each match.
6. Generate cross-source claim edges for each new claim against its candidate set, following the `create-edges` skill (vocabulary and carried fields: `schema/edges.md`); run edge generation here for the claims retrofitted during this ingest's step 3 as well (`create-edges` gives the pair-dedup rule).
7. Write the source page and its dataset pages (`write-wiki`), and add every other affected page — ownership and "affected" defined in `write-wiki` — to the batch's close-out queue.
8. Append to `wiki/log.md`: date, the run id minted at the start of this ingest (`schema/SCHEMA.md`), model, source id, ingest position, number of claims, candidate concepts created, edges created by type and grounding, candidate-set sizes, difficulties, schema version.

## Batch close-out

A batch is all the sources ingested in one session. After the last source's step 8, run the close-out once:

- Regenerate every page in the close-out queue (`write-wiki`) — chiefly the concept pages touched during the batch.
- Regenerate `coverage.md`, `structure.md` and `index.md`. While regenerating the tables, mark lapsed the coverage- and structure-detected absence records in `wiki/absences.jsonl` whose triggering zero is now populated, matching record to cell by `scope` and `description` (lapse semantics: `schema/absences.md`).
- Check and apply concept promotion for every candidate touched during the batch (rules and timing: `schema/concept.md`), logging each promotion; then regenerate the pages promotion touched.
- Log the close-out in `wiki/log.md`.

If a batch ends without its close-out (an interruption), run the close-out before the next batch's first source.

## Sequential processing

Process sources one at a time; complete all eight steps before starting the next. Write no partial extraction.

When a claim of a source enters the adjudication queue (`map-concepts` skill):

- Set the whole source aside and discard its drafts — the Source draft, its claims, its dataset drafts, and its edges. Write none of its records; consume no ids — the drafted id and `ingest_position` remain free.
- Log the source as pending in `wiki/log.md`.
- Continue with the next source; the queue never blocks it.
- Re-ingest the set-aside source from step 1 once the team has adjudicated.

Three things stand even when the triggering source is set aside: a candidate concept created during its step 3 (its page frontmatter is already written — `map-concepts`), that concept's retrofit additions to other sources' claims, and the retrofit's edges. Never roll back concepts or mappings. Before moving to the next source, run the retrofit's edge generation the aborted ingest can no longer carry (step 6, retrofitted claims only) and queue the pages owning retrofitted claims for the close-out. Then log the set-aside and what it left standing in `wiki/log.md`.

Run every claim that enters `claims.jsonl` outside an ingest (a correction's new id, re-extracted claims of a changed source) through step 6 as part of executing that change.

Sequential processing carries no order cost for edges (rationale, not an instruction): candidate sets are complete, so every cross-source pair of claims that both entered through an ingest is compared exactly once — at the ingest of the later claim — and edge judgment is pairwise on claim content, so given a fixed concept mapping, ingest order affects neither which pairs are compared nor the judgments. Candidate-concept naming can still vary with order (the first source to need a concept coins its label), but the retrofit-on-creation rule (`map-concepts`) makes the mapping itself — and hence pair coverage — order-independent. What remains for the review protocol to report as the limitation is label wording and model nondeterminism.

## Bounded retrieval

No step other than step 6's candidate comparison depends on more than a filtered slice of the graph. Step 6's candidate set is complete by design; an oversized set follows the slicing rule in `create-edges`. Each skill states exactly what it retrieves. Read `claims.jsonl` and `edges.jsonl` only as CLAUDE.md's bounded-retrieval invariant directs — by concept id, by source id, or as a field projection.
