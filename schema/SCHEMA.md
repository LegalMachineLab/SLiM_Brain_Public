# SCHEMA.md — version and change policy

`schema_version: 4.0`

This directory is the data dictionary of the knowledge graph. Together with `CLAUDE.md` and the skills it is the sole normative specification;

## What the schema is

The schema consists of:

- the files in this directory;
- the conversion layer — the tool and settings of `tools/convert_source.py` as governed by the `convert-source` skill — because it produces the canonical text layer (`CLAUDE.md`, Repository layout) that every quote is anchored to and the quotation budget is computed over;
- the extraction rules in the `extract-claims` skill (what counts as a claim, granularity, verbatim anchor, jurisdiction, time, language, fidelity, and its failure-mode rules);
- the concept-mapping rules in the `map-concepts` skill;
- the cross-source edge rules in the `create-edges` skill;
- the invariants, mode boundary, and repository layout in `CLAUDE.md`.

Claim and Source records carry `schema_version`, the model identifier, and the run id; every other record (edges, absences, dataset nodes, hypothesis retests) carries at least the run id.

`run_id` is defined once, here, for the whole specification. Format: `RUN-<YYYY-MM-DD>-<NN>`. Mint one run id at the start of each ingest, query, or team-decision session; `NN` is the next free number for that date (find it by searching `wiki/log.md`). Write that one run id into every record the session produces.

## Files

| File | Defines |
|---|---|
| `source.md` | Source node (one per publication) |
| `claim.md` | Claim node and the verification vocabulary |
| `concept.md` | Concept node, statuses, and the three-family concept grid |
| `dataset.md` | Dataset node |
| `edges.md` | The nine edge types, their grounding vocabulary, and carried fields |
| `absences.md` | Typed absence records (ABS) |
| `write-gate.md` | The pre-write checklist every record must pass |

