# CLAUDE.md — literature knowledge graph

This repository builds a knowledge graph and wiki from which a mapping review of the AI and law literature can be produced. It is **not** the review. A mapping review structures a field — what has been published, by whom, on which concepts, in which jurisdictions, with which kinds of claims, where the literature is dense and where it is thin. It does not grade the quality of individual papers and it does not answer a narrow research question.

The full specification is split into a data dictionary (`schema/`) and task skills (`.claude/skills/`). This file holds only what must always hold; everything else loads on demand. **For any of the tasks below, invoke the skill and follow it; do not improvise a procedure from memory of this file.**

## Which skill for which task

| Task | Skill to invoke | Key schema files it uses |
|---|---|---|
| Convert new PDFs in `raw/` to markdown (always precedes ingest; cached, so safe to re-run) | `convert-source` | — |
| Add new source file(s) from `raw/` to the graph | `ingest-source` (the orchestrator) | `schema/source.md`, `schema/write-gate.md` |
| Extract claims from a source (ingest step 2; also when the gate rejects a record) | `extract-claims` — invoked by `ingest-source` | `schema/claim.md`, `schema/write-gate.md` |
| Map claims to concepts (the three-family grid), create candidate concepts (ingest step 3) | `map-concepts` — invoked by `ingest-source` | `schema/concept.md`, `schema/claim.md` |
| Create edges (ingest steps 4–6) | `create-edges` — invoked by `ingest-source` | `schema/edges.md`, `schema/write-gate.md` |
| Write or update wiki pages and tables (ingest step 7 and the batch close-out); file synthesis pages | `write-wiki` — invoked by `ingest-source`; also after a query | `schema/absences.md` |
| Answer a question about the literature | `query-graph` | `schema/absences.md` |
| Rebuild the interactive viewer and refresh the shared artifact | `publish-viewer` | — |
| Apply a team decision (verification verdict, deprecation, mapping change) | only when the user requests it — execute per `schema/claim.md` and `schema/concept.md`, then regenerate affected pages via `write-wiki` | `schema/claim.md`, `schema/concept.md` |
| Asked to add a requirement or change the schema | read `schema/SCHEMA.md` (change policy) | — |

`ingest-source` is the entry point for all extraction work: it invokes `extract-claims`, `map-concepts`, `create-edges` and `write-wiki` at the right steps. Run the extraction skills (`extract-claims`, `map-concepts`, `create-edges`) only during an ingest or when executing a team-directed change on the affected records (a correction's new claim, or re-extracted claims of a changed source; see `ingest-source`, Sequential processing). Run the pre-checks in `ingest-source` before starting any ingest. `write-wiki` also runs outside an ingest: for synthesis pages and when applying team decisions. Read a schema file when a skill directs you to it, not preemptively.

Every rule in this specification has exactly one home: schema files own definitions, field semantics, closed lists and the gate checklist; skills own procedure and POINT to schema files for every definition; this file owns only the mode test, the invariants, routing and layout. NEVER restate a rule in a second file — when editing the specification, add a pointer, not a copy.

## The two modes: read vs inferred

Everything you write about the literature is either **read** (extraction mode) or **inferred** (analysis mode). This is not a phase of the pipeline — ingest step 6 produces both kinds in the same sitting — it is a property of each individual record and sentence, and you decide it at the moment of writing with one test:

**Where is this written?**

- **In one source, in words you can quote verbatim** → read. This is a claim: it carries its anchor quotes (`schema/claim.md`) and passes the write-gate checklist (`schema/write-gate.md`).
- **In a citation** — one source explicitly names or cites the other on this point → read. This is an extracted edge (SUPPORTS, ATTACKS, extracted SAME_AS — fields per `schema/edges.md`).
- **Nowhere** — you compared two claims, noticed a pattern, generalised → inferred. Write inferred judgment only in the containers built for it: a COMPATIBLE_WITH, IN_TENSION_WITH, or inferred SAME_AS edge (fields per `schema/edges.md`); the separate second part of a query answer; a synthesis page (`write-wiki`); or a hypothesis entry. Always display it apart — **nothing inferred ever enters the claim record**.

If you cannot say where it is written, it is inferred. Doubt moves a label down (extracted → inferred, strong → weak), never up. Mark on every edge and every answer which of the two it is — the marking, not the workflow step, is what keeps what is read apart from what is inferred.

## Invariants (every mode, every task)

- Keep to the four node types (Source, Claim, Concept, Dataset) and nine edge types of the schema. Do not add node types. If something does not fit, record it as a claim, a concept, or an attribute, and note the difficulty in `wiki/log.md`.
- Extract and classify. Do not evaluate whether a paper is good, rigorous, or important. Do not grade, rank, or score sources, or weight them by venue, citation count, author reputation, or graph connectivity.
- Treat all papers in the corpus as equal inputs. A ten-page technical paper and a hundred-page essay are both sources; each contributes what it argues, no more and no less. Do not privilege empirical or technical papers in the number or prominence of extracted claims.
- Never invent, complete, or correct a claim with outside knowledge of the law or of the literature. Never fill gaps in a source with outside knowledge.
- Record what the sources argue at claim level, with enough metadata for a human to verify every statement. Record what they do not say only as typed absence records, under the recording and rendering rules of `schema/absences.md` — never interpreted by you.
- Do not create nodes for legislation, cases, courts, persons, or institutions. Do not merge claims from different sources into one node.
- Write the team-owned claim fields (`verification_status`, `legal_reference_normalised`) only as the verification vocabulary of `schema/claim.md` allows.
- Never alter or delete an existing record: corrections and re-extractions supersede per `schema/claim.md`; concepts are deprecated per `schema/concept.md`, never deleted.
- Produce every statement about corpus or graph content through the retrieval path of the relevant skill, read at the time of writing — including when asked for a summary "from what you remember". Never state what the graph, the wiki, or a source contains from memory.
- `raw/` is read-only for you, with one exception: `tools/convert_source.py`, run through the `convert-source` skill, writes the markdown conversions and their cache manifest into `raw/`. Nothing else writes there (conversion rules: `convert-source` skill).
- Every new record passes the write gate before it is written (scope, checklist, and sanctioned in-place updates: `schema/write-gate.md`).
- Check and apply concept promotion only at the point, and under the threshold, that `schema/concept.md` defines.
- Keep retrieval bounded: read `claims.jsonl` and `edges.jsonl` only through filters (read-only search commands are part of the retrieval path, not pipeline code); never read them unfiltered.
- When a check and a convenient outcome conflict, the check wins. Executing a procedure never licenses bending it.
- When the gate rejects a record, follow the rejection procedure in `schema/write-gate.md`; never alter the gate.

## Clean-context subagents

When the harness provides subagents (an Agent/Task tool), run extraction (ingest step 2) — and only extraction — in a clean-context subagent: an extractor that holds only one source cannot import an entity, label, or quote from a neighbouring document, so the known contamination failure mode becomes impossible by construction. `ingest-source` names the subagent's exact inputs; give it those, plus the `extract-claims` skill, and nothing else. Its output enters the pipeline through the same gate as any other. Run everything else — gate checks, edge judgment, page writing — inline; the procedures bind you directly (a throughput decision: the subagent tax is paid only where isolation buys the most). When no subagent capability is available, extraction too binds you directly.

## Corpus boundary

The corpus consists only of academic publications (journal articles, conference papers, book chapters, working papers, preprints, reports by research institutions). Primary legal sources (legislation, case law, regulatory guidance) are not part of the corpus and must not become nodes; claims in the literature about legal instruments are captured through the `legal_reference` field of a claim. The research questions, eligibility criteria, search strategy and screening procedure that define the corpus belong to the review protocol, not to this repository. This repository governs what happens to a source once it is in `raw/`.

## Repository layout

```
CLAUDE.md                 this file; the tree below is the sole normative specification
                          (CLAUDE_ORIGINAL.md is the superseded v1 monolith, kept for provenance only)
schema/                   data dictionary: nodes, edges, the concept grid, absences, write gate (index: schema/SCHEMA.md)
.claude/skills/           the eight task skills
tools/                    convert_source.py, viewer.py and viewer_template.html 
raw/                      source PDFs and their cached markdown conversions, one .md per .pdf (convert-source skill);
                          the .md files are the canonical text layer that quotes are verified against;
                          read-only for you (invariant above)
  _conversions.json       conversion cache manifest: per PDF, its sha256, docling version, settings, conversion_tool
wiki/
  index.md                catalogue of all pages
  log.md                  append-only record of every operation, rejection and adjudication
  hypotheses.md           register of conjectures generated at query time
  coverage.md             distribution tables
  structure.md            structural report on the graph
  absences.jsonl          typed absence records
  sources/SRC-0001.md     one page per source
  concepts/CPT-<id>.md    one page per concept
  datasets/DST-0001.md    one page per dataset
  syntheses/SYN-0001.md   pages written from queries
  claims/claims.jsonl     one JSON object per claim, all fields of schema/claim.md
  graph/edges.jsonl       one JSON object per edge (shape and carried fields: schema/edges.md)
viewer.html               generated explorer page over the graph (publish-viewer skill)
```

## Schema version

Which fields each record type carries, the `run_id` format and minting, the current schema version, and the change policy (what requires re-extraction, what does not) are all defined in `schema/SCHEMA.md`. Read it before agreeing to any new requirement.
