# Absence records

An absence is a typed record, not a number. Whenever coverage, structure, a source or concept page, or a query identifies something the corpus does not address, write an absence record to `wiki/absences.jsonl`:

```yaml
id: ABS-0001
date:
scope:                            # concept | concept_pair | concept_jurisdiction | claim_type_on_concept | other
description:                      # one sentence stating exactly what is absent
detected_in:                      # coverage | structure | source_page | concept_page | query ("lint" is a historic value from before 2.2's lint redesign; it is no longer produced)
candidate_readings: [gap_in_literature, extraction_shadow, tacit_link]   # always all three, verbatim; never select among them
resolved_reading: unresolved      # human-only: gap_in_literature | extraction_shadow | tacit_link; stays "unresolved" until the team decides
evidence_checked: []              # the filters and registries consulted before recording the absence
lapsed: false                     # set true (with date and run_id) when the recorded absence is filled: at the ingest batch close-out for coverage- and structure-detected records, and at any page regeneration or query that touches a source_page/concept_page/query-detected record and finds its absence answered; lapsed records are kept, never deleted
run_id:
```

Creation rules:

- Create a new ABS record for a zero only when no unlapsed ABS record with the same scope and description exists; otherwise cite the existing record (this keeps regenerated tables from duplicating records for a persisting zero).
- Read zeros over closed vocabularies and the concept grid's cross-tabs, never over rows that exist only when populated.
- The zero, confirmed via the filters recorded in `evidence_checked`, is sufficient to trigger the record (what pages may present: Rendering below).

Rendering: `coverage.md`, `structure.md` and `hypotheses.md` refer to absences by ABS id and render all three candidate readings with them. `coverage.md` and `structure.md` list lapsed records under a Lapsed heading, never among current absences. Never present a bare count (for example "0 claims") as a finding anywhere in the wiki: the numerical fact triggers the ABS record (Creation rules above), and the record is the finding.
