---
name: write-wiki
description: Use when writing or regenerating wiki pages — source and dataset pages at ingest step 7; concept pages, coverage.md, structure.md and index.md at the batch close-out; synthesis pages filed from queries; the affected pages when applying team decisions. Defines page ownership, page structure, the fixed rendering templates, absence detection on pages, and the citation discipline.
---

# Write the wiki

The wiki is the human-readable layer. Cite at least one claim id in square brackets, for example `[CLM-0012-004]`, after every sentence that states something about the literature. Limit citation-free sentences to structure and navigation. Render every absence stated on any page as an ABS record, cited by id and rendered per `schema/absences.md`. When regenerating a page, mark lapsed (per `schema/absences.md`) any ABS record the page cites whose absence is now filled, and drop it from the page's absence listing. The file layout is in CLAUDE.md.

## Retrieval discipline

Regenerate each page from `wiki/claims/claims.jsonl` and `wiki/graph/edges.jsonl` filtered to the records that page owns (bounded retrieval and never-from-memory: CLAUDE.md invariants).

Ownership is defined as follows. A source page owns its source's claims plus every edge with either end on them. A concept page owns the claims that map to its concept plus every edge with either end on those claims. A dataset page owns its USES edges plus the claims naming the dataset. The affected pages of an ingest or of a team decision are every page owning a record written or modified by it — regenerate exactly those.

Apply the exclusion scope of `schema/claim.md` (Verification vocabulary) to every section of every page, its evaluation-section exemption included.

When the records a page owns exceed the context, regenerate over the complete set in successive slices and note the slicing in `wiki/log.md`; a truncated set never stands in for the whole.


## Source page

Frontmatter: all Source fields (`schema/source.md`; its lifecycle governs materialization, the first gated write, and later in-place updates).

Body, in this order:

1. What the source argues (one paragraph, citing its claims).
2. Claims, grouped by claim type, each as one entry: statement (which may span several sentences), claim jurisdiction, basis, claim id, plus the optional classifications per the rendering templates.
3. Concepts addressed (links).
4. Datasets used (links), or "none".
5. Relations to other sources in the corpus: cites, is cited by, supports, attacks, compatible with, in tension with, same as (with claim ids and grounding; list extracted relations before inferred ones).
6. What this source does not address: list each anchor concept that shares a grid family with a concept the source's claims map to but appears on none of its claims — use no other notion of adjacency. Record each as an ABS record under the create-or-cite rule in `schema/absences.md`. State each absence plainly; do not speculate why.
7. Evaluation: claims carrying a human verification mark, when any exist — the exclusion scope's exempt section (`schema/claim.md`, Verification vocabulary).

## Concept page

Frontmatter: all Concept fields (`schema/concept.md`). Body, in this order:

1. Definition, from the concept node's `definition` field (for candidate and emergent concepts it derives from the claims that motivated the concept — cite those claim ids); where conceptual claims on this concept define it differently, list each with its source. Broader concepts as links, from the `broader` field.
2. Claims about the concept, grouped first by claim type (descriptive, interpretive, normative, empirical, conceptual, predictive, methodological) and within each type by claim jurisdiction. Each claim as one entry with its id, plus the optional classifications per the rendering templates. Group SAME_AS claims in one entry with all ids.
3. Disagreements: every ATTACKS edge touching a claim on this page, as "Source A holds X [id]; Source B holds not-X [id]; note". Then, under the separate heading "Inferred", every IN_TENSION_WITH edge, with plausibility.
4. Distribution: number of sources by contribution type, by source jurisdiction, by claim jurisdiction, by year. Plain table.
5. What the sources do not address: claim types or jurisdictions with no claims on this concept, and questions raised inside extracted claim or premise text but not answered by any claim (cite the claim id that raises the question). Count only explicit questions or expressly flagged open issues occurring verbatim in claim or premise text; never infer an implied question. Record each as an ABS record under the create-or-cite rule in `schema/absences.md`.
6. Open questions for the hypothesis register (`query-graph` skill).

Assemble the concept page from `claims.jsonl` and `edges.jsonl` under the Retrieval discipline above. Delete any sentence you cannot trace to a claim id. Draw summaries on all sources with claims on the concept, not primarily on the most connected ones; report connectedness in `structure.md`, never as a weight (the no-weighting invariant, CLAUDE.md).

## Dataset page

Frontmatter: all Dataset fields, written per the lifecycle in `schema/dataset.md`. Body: which sources use it and for which claims; language and jurisdiction of the texts; whether annotation was human and whether agreement was reported, as stated in the sources.

## coverage.md

Regenerated at the batch close-out (`ingest-source`). Tables of: sources by contribution type; sources by source jurisdiction; claims by claim type; claims by claim jurisdiction; claims per source; claims per concept; claims by concept family, and the two-dimensional maps drawn from the families (legal task against technique class, normative concern against claim jurisdiction); concepts with fewer than three sources; claims by fidelity; edges by type and grounding. These tables are the raw material for identifying where the literature is dense and where it is thin, and for checking that extraction has not skewed toward one paper type.

Compute every table with read-only aggregation commands over `claims.jsonl` and `edges.jsonl` (group-by counts) — the filtered read of CLAUDE.md's bounded-retrieval invariant. The exclusion scope (above) applies to every table.

Zeros:

- Read zeros only from the cells `schema/absences.md` defines as zero-bearing.
- When a table shows a zero, write an ABS record under the create-or-cite rule in `schema/absences.md` and cite its id beside the zero.
- When a zero that triggered an ABS record is now populated, mark the record lapsed (`schema/absences.md`; this happens here, at the batch close-out).
- Exception: the claims-per-source table — a zero there is an extraction failure (`ingest-source` step 2), never a literature absence.

## structure.md

Regenerated alongside `coverage.md` and `index.md` (the batch close-out, `ingest-source`). Report, from `edges.jsonl` and the derived MAKES/ABOUT relations of `claims.jsonl` (`schema/edges.md`): the most connected concepts (structural anchors); disconnected components (groups of sources or concepts with no cross-source claim edge or CITES edge to the rest); concepts many claims are about with no defining conceptual claim in the record (used but never defined there); pairs of anchor concepts with no claim linking them. Compute these with read-only aggregation commands over the jsonl files, as for `coverage.md`.

These are descriptive facts about the graph; centrality measures attention, not endorsement (the no-weighting invariant, CLAUDE.md). Record every absence reported here as an ABS record under the create-or-cite rule in `schema/absences.md`.

## Rendering templates

Render wiki sentences derived from claims and edges with fixed templates, so that the sentence never says more than the data (edge-type semantics: `schema/edges.md`):

- Claim: "<Authors> (<year>) argue that <statement> [<id>]." For descriptive claims: "state that"; for empirical claims: "report that"; for interpretive claims: "read <legal_reference or concept> as".
- ATTACKS: "<Authors A> (<year>) reject <Authors B>'s claim that <statement B> [<id A>, <id B>]."
- SUPPORTS: "<Authors A> (<year>) give reasons for <Authors B>'s claim that <statement B> [<id A>, <id B>]."
- IN_TENSION_WITH: "The claim that <statement A> [<id A>] is in tension with the claim that <statement B> [<id B>] (inferred, <plausibility>)."
- COMPATIBLE_WITH: "The claim that <statement A> [<id A>] is compatible with the claim that <statement B> [<id B>] (inferred, <plausibility>)."
- Optional classifications, appended to a claim line: on descriptive claims, `positive_form` when its value is one of the five forms (field semantics: `schema/claim.md`); `basis_qualifier` in parentheses after the basis (e.g. "case_law (dictum)"); `temporal_reference` when it is not `as_of_publication`.
- Never render concept membership or contribution type as something the source "argues" or "raises".

## Synthesis pages

A substantive query (`query-graph` skill) may be filed back into the wiki as a synthesis page, so that later answers can build on earlier ones. A synthesis page:

- has frontmatter `type: synthesis`, the query that produced it, the date, the run id, the model, and the list of claim ids it rests on;
- cites a claim id after every sentence about the literature, like every other page;
- is linked from `index.md` and from the concept pages it draws on;
- is never cited as evidence: a later query cites claims, not synthesis pages.

When a claim a synthesis page rests on is superseded or rejected, the page is marked `stale: true` and the marking logged per the verdict paragraph of `schema/claim.md`. Rewrite or delete a stale page only on the team's instruction — a page that is stale, logged, and awaiting the team is not "silently kept". Treat new claims on its concepts as grounds for a team-requested rewrite, not as automatic staleness.
