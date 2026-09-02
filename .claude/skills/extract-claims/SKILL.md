---
name: extract-claims
description: Use when extracting claims from a source during ingest (step 2 of ingest-source), and when the write gate rejects a record. Covers the extraction procedure only — where to find the propositions a paper argues, splitting, propositions-first anchoring, jurisdiction and time assignment, language, fidelity grading, and the known failure modes. The claim definition and record schema are in schema/claim.md; the write gate is schema/write-gate.md.
---

# Extract claims

Read `schema/claim.md` first — it defines the claim, the one-proposition test, every field, and the fidelity bands; nothing in this file redefines them. Submit every record through the gate in `schema/write-gate.md`, which also owns the rejection procedure; `ingest-source` sets the write timing. Run this skill in extraction mode (CLAUDE.md's read-vs-inferred test).

## What to extract

Extract the propositions the source argues, per the definition in `schema/claim.md`. The paper's originality assertion — first to do X, a gap no prior work fills — is such a proposition when the paper argues it.

Do not extract:

- restatements of a claim already extracted (a restatement adds nothing);
- headings, section titles, or signposting ("this section discusses");
- mandatory ethics-section boilerplate (a required disclaimer is not something the paper argues);
- facts about the paper itself (number of pages, funding), which belong to the Source node;
- quotations of primary legal sources without comment (a quotation of Article 5 AI Act is not a claim; the authors' statement of what they argue about Article 5 can be);
- graph metadata rendered as assertion (that a source is classified `technical`, or maps to a concept, is a fact about the graph, never a claim the source makes).

## Formulation

State it so it can be understood without the source, in as many sentences as the proposition needs — the limit is semantic, never syntactic (the one-proposition test in `schema/claim.md`). Never use the extra room to smuggle in a second proposition. 

State it so it can be understood without the source. Resolve all anaphoric and document-dependent references. Elements like "this work", "the authors" etc must be avoided.

Keep the modality of the source. If the source says "may", the statement says "may". Do not upgrade "suggests" to "shows", or "should" to "must".

Apply the same effort to essay-style and doctrinal papers as to empirical and technical ones. A paper with no methods section, no dataset, and no results still argues a thesis; extract it with the ground it actually offers (`basis` rules in `schema/claim.md`).

When a paper is long, read all of it. The thesis a paper advertises in its abstract and the thesis it actually argues can differ.


## Propositions first, then anchors

Derive before you anchor. After the full read, state the propositions the paper argues, at the altitude the paper argues them — synthesize across sections where the argument is distributed; do not limit yourself to sentences that happen to be quotable. Only then anchor each proposition, following the `quotes` field rules in `schema/claim.md`. Take every quote from the source's own markdown conversion under `raw/` (the ingest input — `ingest-source`); a quote from any other file is a contamination error (see failure modes below). The gate enforces the per-source quotation budget (`schema/write-gate.md`).

If no passage warrants a proposition, do not record the claim.

## Jurisdiction

Record two jurisdictions, and keep them apart:

- `source_jurisdiction` (Source node): the legal system the work is situated in, inferred from the law it treats as its own, the authors' affiliations as printed, and the venue. Use `general` for work that does not situate itself in any legal system (most technical papers).
- `claim_jurisdiction` (Claim node): the legal system the claim is about. A paper written in Germany that makes a claim about the United States Supreme Court has `source_jurisdiction: [DE]` and, for that claim, `claim_jurisdiction: [US]`.

Codes: ISO 3166-1 alpha-2 for states, `EU` for the European Union, `CoE` for the Council of Europe system, `INT` for public international law. For federal systems, add the sub-unit only when the source does (`US-CA`).

Three special values cover what a single `general` would conflate, because they are three different situations:

- `general`: the claim is explicitly not tied to any legal system (the source presents it as jurisdiction-independent).
- `undetermined`: the source does not say and the context does not settle it. Never resolve `undetermined` by falling back on the source jurisdiction.
- `geographical_proxy:<code>`: the claim itself is general but its evidence comes entirely from one jurisdiction's materials (for example, a claim about model performance demonstrated on a benchmark of US judgments takes `geographical_proxy:US`). The code marks the origin of the evidence, not the legal scope of the claim.

List multiple jurisdictions in order of dominance, as `contribution_type` already is, and carry a `jurisdiction_relation` on the ordered list:

- `eu_law_in_member_state`: EU law as applied in a member state; `[EU, NL]` means EU law as applied in the Netherlands.
- `comparative`: the claim explicitly compares the listed legal orders.
- `cumulative`: the claim concerns each listed legal order independently.

Without this field, `[EU, NL]` would be ambiguous between the first and the third reading.

Never infer a claim jurisdiction from the source jurisdiction. When you assign a jurisdiction from context rather than from an explicit statement, set `jurisdiction_inferred: true`. Context here means the claim's surrounding text and the materials the source cites on the point — never the source's own jurisdiction, affiliations, or venue.

## Time

Record the `year` of the source. Record `temporal_reference` on a claim only when the claim describes a legal or factual state at a time the source specifies (for example "before the AI Act entered into force", "as of 2023"). Otherwise write `as_of_publication`. Do not update claims to reflect later legal developments; the claim records what the source said when it said it.

## Language

Sources may be in any language; statement and quote language follow the field rules in `schema/claim.md`. Do not translate legal terms of art when the source leaves them in the original (keep "Rechtsstaat", "bonne foi"). When a claim's concept mapping crosses a language or legal tradition, record the original term as an alias on the concept; the mapping is a comparative judgment, and it is recorded as such rather than presented as a translation.

## Fidelity

Grade `fidelity` by the bands in `schema/claim.md`. Keep low-fidelity claims; never drop them. For every claim graded `low`, record in `wiki/log.md` why the statement required that much interpretation of its anchors. Medium needs no log entry.

## Known failure modes to guard against

These were observed in an edge-level check of an earlier brain (Schrepel 2026, section 4.2) and each has a rule here:

- An entity, label, or claim imported from a neighbouring document in the same corpus. Rule: every quote must come from the claim's own source file (propositions-first anchoring above); concept labels are governed by the labeling rules in `map-concepts`.
- A legal basis read as a substantive finding (a provision cited for procedure treated as an outcome). Rule: `legal_reference` records what the claim is about; it never by itself generates a claim; `basis_qualifier` records holding against dictum as the source presents it.
- An inference from a described activity to a named entity. Rule: name only what the source names; otherwise grade `fidelity: low` and log the reason (Fidelity above).
- Graph-internal metadata rendered as an assertion about what a source says. Rule: the last exclusion under "What to extract" above, and the rendering templates of the `write-wiki` skill.

The invariants in CLAUDE.md apply to every extraction.
