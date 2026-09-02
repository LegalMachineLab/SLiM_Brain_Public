# Node: Dataset

One node per dataset, benchmark, or corpus that a source uses or introduces. Create a Dataset node only when a USES edge is warranted (`schema/edges.md`); never from a passing mention.

```yaml
id: DST-0001
name:
introduced_by:                    # source id, when the dataset is introduced in the corpus; otherwise "external"
used_by: []                       # source ids
language: []                      # ISO 639-1 codes of the texts in the dataset
jurisdiction: []                  # legal system(s) the texts come from; jurisdiction codes in the extract-claims skill
document_types: []                # e.g. judgments, statutes, contracts, exam questions, synthetic
size:                             # as stated in the source, with unit
annotation:                       # none | automatic | human_single | human_multiple
agreement_reported:               # yes | no | not_applicable (whether an inter-annotator agreement figure is given)
availability:                     # public | on_request | proprietary | not_stated
run_id:
```

Draft the Dataset record in memory at ingest step 4; write it as the dataset page's frontmatter in `wiki/datasets/` at ingest step 7 (the record's only materialized form). On a set-aside (procedure: the ingest-source skill), discard the draft; the id remains free.
