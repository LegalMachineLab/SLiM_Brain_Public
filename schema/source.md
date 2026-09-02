# Node: Source

One node per publication in the corpus.

```yaml
id: SRC-0001                      # stable, never reused; consumed only when the record is first written
file: raw/<filename>.md           # path of the markdown conversion
conversion_tool:                  # tool and version used for the PDF-to-markdown conversion, with parameters; copy the exact string from raw/_conversions.json, e.g. "docling 2.123.1, tools/convert_source.py, ocr=off, table_structure=on"
ingest_position:                  # integer; running order of ingest across the corpus (provenance; order has no designed effect on extraction or edges)
title:                            # from the document text, never from the filename (filenames never enter the graph as titles)
authors: []                       # as printed, family name first
year:
venue:                            # journal, conference, publisher, or repository
venue_type:                       # journal | conference | book_chapter | working_paper | preprint | report | thesis | other
language:                         # ISO 639-1 code of the main text
pages_or_length:                  # page range, or approximate word count when no pagination
contribution_type: []             # one or more of the values below, in order of dominance
source_jurisdiction: []           # legal system(s) the work is situated in; jurisdiction rules in the extract-claims skill; use "general" when none
discipline_of_authors: []         # law | computer_science | economics | philosophy | other | unknown (from affiliations as printed)
other_versions: []                # source ids or external identifiers of preprint/offprint twins, if any (see the ingest-source skill)
claims_extracted:                 # integer; counting rule in Lifecycle below
extraction_model:                 # model identifier and version used for this source
run_id:
extraction_date:
schema_version:
```

Lifecycle:

- Draft the Source record in memory at ingest step 1; write nothing at that point. Run the write gate (`schema/write-gate.md`) on the record, then write it as the source page's frontmatter in `wiki/sources/` at ingest step 7 (the record's only materialized form). On a set-aside (procedure: the ingest-source skill), discard the draft; the id and `ingest_position` were never consumed and remain free.
- On re-extraction of the source, update this record's extraction fields in place: `claims_extracted` (count only claims that are neither rejected nor superseded), `extraction_model`, `run_id`, `extraction_date`, `schema_version`. Never change `id` or `ingest_position`. Also recompute `claims_extracted` whenever the source page is regenerated (a verdict can change the count). These are among the sanctioned in-place updates listed in `schema/write-gate.md`.

Definitions of `contribution_type` (assign every value that applies, in order of dominance):

- `doctrinal`: describes, systematises or interprets existing law (lex lata).
- `normative`: argues what the law or policy should be (lex ferenda), including reform proposals and ethical arguments.
- `theoretical`: builds or criticises concepts, taxonomies, or frameworks without primarily describing law or reporting data.
- `empirical_quantitative`: reports measurements, experiments, benchmarks, statistics, or surveys with numerical results.
- `empirical_qualitative`: reports interviews, case studies, content analysis, or observation.
- `technical`: proposes or evaluates a system, model, dataset, or method.
- `survey`: reviews other literature as its main contribution.
