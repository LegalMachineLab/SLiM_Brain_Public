# Write gate

Run this checklist on every record before appending it to `claims.jsonl`, `edges.jsonl`, or `absences.jsonl`, and on every Source record before its first write as the source page's frontmatter (lifecycle: `schema/source.md`). Nothing reaches those destinations unchecked.

The gate checks new records at append time. Do not resubmit sanctioned in-place updates — they are not gate submissions: verdict fields copied from a communicated team decision (`verification_status`, `verified_by`, `verified_date`); `superseded_by` set by a correction or re-extraction; retrofit concept additions (`map-concepts`); Source extraction-field updates on re-extraction and `claims_extracted` recomputation at source-page regeneration (`schema/source.md`); and lapsed marks on ABS records (`schema/absences.md`).

Reject a record when any condition below holds:

- `quotes` is empty, any anchor's quote is empty, or `quotes` breaches an anchor constraint of `schema/claim.md` (anchor count, quote length, verbatim presence in the conversion the Source node's `file` field names, after whitespace and hyphenation normalisation);
- the source's quotation budget is breached (copyright limitation) — compute it at gate time: sum the character counts of every anchor quote of the source's claims in `wiki/claims/claims.jsonl` that are neither rejected nor carrying `superseded_by`, plus the candidate's anchors; reject when that sum exceeds 50 percent of the source file's character count (`wc -c`); keep no running ledger; when in doubt, quote less;
- any anchor lacks a `location`;
- `claim_jurisdiction` is empty;
- `claim_type`, `basis`, `basis_qualifier`, `fidelity`, `positive_form`, or `jurisdiction_relation` holds a value outside the defined lists (`schema/claim.md`);
- a claim's `concepts` breach the count or per-family cap of `schema/concept.md`;
- `positive_form` is set on a claim that is not descriptive;
- `basis_qualifier` is set while `basis` is not `case_law`;
- `jurisdiction_relation` is set while `claim_jurisdiction` has fewer than two entries, or `claim_jurisdiction` has more than one entry while `jurisdiction_relation` is empty;
- `legal_reference_normalised` is non-empty in a model-written record (`schema/claim.md`);
- `verification_status` is anything other than `unverified`;
- `superseded_by` is non-empty in a newly extracted record (`schema/claim.md`);
- `dataset` names a dataset id with no Dataset record or no corresponding USES edge for the source (at gate time the Dataset record is the draft; lifecycle: `schema/dataset.md`);
- a cross-source claim edge lacks a carried field required by `schema/edges.md`, or connects two claims from the same source;
- an edge's grounding contradicts its type's grounding column in `schema/edges.md`;
- an absence record selects a `resolved_reading`, or omits any of the three `candidate_readings` values (`schema/absences.md`);
- a Source record has no `title`, `year`, `extraction_model`, `conversion_tool` or `ingest_position`.

When you reject a record: write the rejection to `wiki/log.md` with the reason and the failed condition, then re-extract and resubmit the record (`extract-claims`). Drop a rejected record instead only when the re-read shows no passage warrants the proposition and the source still retains at least one admitted claim. Never change the checklist to admit a record.


