# SLiM Brain

A knowledge graph and wiki of the AI-and-law literature, built as the substrate for a **mapping review**: what has been published, by whom, on which concepts, in which jurisdictions, with which kinds of claims — and where the literature is dense and where it is thin.

It is deliberately **not** the review itself. The repository extracts and classifies; it never grades papers, never answers a research question directly, and never lets a model's judgment enter the record unlabelled. Every claim in the graph is anchored to verbatim quotes in a source and carries the metadata a human needs to verify it; every record passes a write-gate checklist the agent must run before every write and may not alter.

**Explore the graph: [SLiM Brain Explorer](https://claude.ai/code/artifact/71bfac22-0b50-42cc-80a4-191ed1413e71)** — the interactive viewer over the current build (50 sources, 892 claims, `schema_version: 4.0`), generated with Fable 5.1 (high reasoning).

## How it works

```
raw/*.pdf ──(docling, cached)──► raw/*.md ──(extraction)──► claims + concepts + edges ──► wiki/
                                                │                    │
                                        write gate (rejects       queries answered only
                                        unanchored records)       from the graph, with
                                                                  claim ids after every
                                                                  statement
```

An LLM agent (Claude Code) runs the entire pipeline. Every safeguard is a fixed procedure the agent must execute and may not alter; the only code is the PDF conversion and the read-only viewer builder. The agent's instructions are split so that only what must always hold is always loaded:

- **[CLAUDE.md](CLAUDE.md)** — the always-loaded core: the extraction/analysis mode boundary, the invariants, the clean-context subagent guidance, the corpus boundary, and a routing table mapping each task to a skill.
- **[schema/](schema/)** — the data dictionary: node types (Source, Claim, Concept, Dataset), the nine edge types, the three-family concept grid, absence records, and the write gate ([index](schema/SCHEMA.md)).
- **[.claude/skills/](.claude/skills/)** — eight task skills the agent loads on demand: `convert-source`, `ingest-source` (the orchestrator), `extract-claims`, `map-concepts`, `create-edges`, `write-wiki`, `query-graph`, `publish-viewer`.
- **[tools/](tools/)** — `convert_source.py` (PDF-to-markdown cannot be done in a prompt) and `viewer.py` with its HTML template, which renders the read-only explorer `viewer.html` — deliberately the only code in the repository.

The tree above is the sole normative specification.

## Design principles

- **A claim is what a paper argues.** A central thesis or hypothesis the paper advances as part of its contribution — one proposition per claim, at least one claim per source, with the ground the source offers carried as the claim's `premise`. Reported positions and definitions are deliberately not claims.
- **Verbatim anchoring.** Every claim is anchored to verbatim quotes that must occur in the source's own markdown conversion (limits, locations, and fidelity bands: [schema/claim.md](schema/claim.md)). No quotes, no claim.
- **Two modes, kept apart.** Extraction transcribes under rules; analysis (inferred edges, query answers, syntheses) is admitted only under labels that keep it separable and can never enter the claim record.
- **Procedure-bound.** Records reach the graph only through a write-gate checklist the agent runs on every record before writing; concept promotion and wiki regeneration are mechanical procedures with fixed thresholds; citation normalisation belongs to the team. The trade-off is accepted: enforcement is procedural rather than mechanical, with the human verification vocabulary in the schema as the backstop.
- **Absences are records, not numbers.** What the corpus does not address is captured as typed absence records ([schema/absences.md](schema/absences.md)).
- **All papers are equal inputs.** No weighting by venue, citations, reputation, or graph connectivity.

## Getting started

```bash
# one-time: the conversion venv (docling pinned to the corpus tool version)
python3 -m venv ~/.venvs/bad_brain
~/.venvs/bad_brain/bin/pip install "docling==2.123.1"

# convert new PDFs in raw/ (cached — already-converted files are skipped)
~/.venvs/bad_brain/bin/python tools/convert_source.py

# cache status
~/.venvs/bad_brain/bin/python tools/convert_source.py --check

# rebuild the interactive explorer (viewer.html) from the wiki; no venv needed
python3 tools/viewer.py            # --verify checks the page against the wiki without writing
```

Conversion caching lives in `raw/_conversions.json` (per PDF: SHA-256, docling version, settings, and the exact `conversion_tool` string the Source node records). A docling upgrade never silently reconverts: mismatched files are reported *stale* and touched only with `--force`, because the `.md` files are the canonical text every quote is verified against.

Everything downstream of conversion runs through Claude Code: open the repo and ask it to ingest, query, or apply your decisions — [CLAUDE.md](CLAUDE.md) routes it to the right skill.

## Status

| Piece | State |
|---|---|
| Specification (schema + skills) | ✅ complete, `schema_version: 4.0` |
| PDF → markdown conversion | ✅ implemented and run (50 sources converted) |
| Write gate | ✅ checklist the agent runs pre-write ([schema/write-gate.md](schema/write-gate.md)) |
| Concept promotion / maintenance | ✅ mechanical, applied at ingest when the threshold is reached |
| Citation normalisation | left to the team; the model never fills the field |
| Interactive viewer | ✅ [SLiM Brain Explorer](https://claude.ai/code/artifact/71bfac22-0b50-42cc-80a4-191ed1413e71), regenerated from the wiki by the `publish-viewer` skill |
| Corpus | 50 sources, 892 claims extracted under 4.0 with Fable 5.1 (high reasoning) |

The corpus definition (research questions, eligibility, search, screening) belongs to the review protocol, not this repository; this repository governs what happens to a source once it is in `raw/`.

## Schema versioning

Record versioning, run ids, and what counts as a schema change — and therefore forces re-extraction of the corpus — are defined in [schema/SCHEMA.md](schema/SCHEMA.md). The version-by-version history of the specification lives in [changelog.md](changelog.md).
