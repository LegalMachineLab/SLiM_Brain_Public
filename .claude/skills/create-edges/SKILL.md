---
name: create-edges
description: Use when creating edges during ingest (steps 4–6 of ingest-source) — CITES, USES, and the cross-source claim edges SUPPORTS, ATTACKS, SAME_AS, COMPATIBLE_WITH, IN_TENSION_WITH. Defines candidate-set generation, target selection for extracted edges, edge direction, and retrofit pair-dedup. Edge-type semantics and carried fields in schema/edges.md.
---

# Create edges

Read `schema/edges.md` before creating edges — it fixes the nine edge types, the type-to-grounding pairing, and the carried fields. The edge vocabulary enforces the mode boundary in CLAUDE.md; when in doubt between a strong and a weak label, let the citation link decide — none means weak (doubt moves the label down: CLAUDE.md).

## Candidate-set generation (retrieval discipline)

For each new claim, build the candidate set: every claim from a different source in `wiki/claims/claims.jsonl` that shares at least one concept with it (same-source pairs are barred by `schema/edges.md`). Obtain it by filtering `claims.jsonl` on the claim's concept ids with a read-only search (bounded retrieval: CLAUDE.md). Include only claims the exclusion scope in `schema/claim.md` admits. Take the whole set: apply no jurisdiction filter and no size cap. Compare every candidate in the set. Log the candidate-set size for each claim (it enters the step-8 log entry). Run inferred comparisons only within the candidate set. (The narrow claim definition keeps candidate sets tractable.)

When a candidate set is too large to compare in one pass, compare it completely in slices, log its size in `wiki/log.md` for the team, and finish the ingest — never truncate, never halt.

Retrofit edge generation (the `map-concepts` retrofit, which fixes its timing): compare each newly-sharing pair exactly once — process retrofitted claims in claim-id order, comparing each only against newly-sharing claims that are not retrofitted or that have a lower claim id.

An extracted relation does not depend on retrieval: when the source explicitly names or cites another corpus source on the point of a claim, create the SUPPORTS, ATTACKS, or SAME_AS edge directly, whether or not the target appears in the candidate set. Find the target by filtering `claims.jsonl` on the cited source's id and taking the claim whose proposition the citation addresses. When no extracted claim of that source states the cited point, create no edge and log the unmatched citation in `wiki/log.md`.

Judge each new claim's inferred relations in one pass over its whole candidate set — never pair by pair.

## Rules for cross-source claim edges

- SAME_AS: apply the identity conditions in `schema/edges.md`.
- Keep both claims as separate nodes linked by SAME_AS (the never-merge invariant, CLAUDE.md); the wiki groups them.
- Direction of SUPPORTS and ATTACKS: create the edge in both directions only when each source addresses the other's position; otherwise create one edge, from the later source's claim (by publication year) to the earlier one's.
- Direction of inferred edges (COMPATIBLE_WITH, IN_TENSION_WITH): always create one edge, from the later source's claim to the earlier one's — later by publication year, ties broken by taking the claim of the lower source id as target. (The bidirectional case cannot arise: inferred edges have no citation link.)
- Treat an inferred edge as a hypothesis about the literature, not a fact about it. Keep it, label it, and show it apart from extracted material (the `write-wiki` skill displays inferred material separately in its pages and rendering templates). Run inferred-edge audits only on explicit team request.

## Other edges

- Create CITES and USES under the `when` column of `schema/edges.md`; create Source nodes only for works in the corpus. Keep USES edges consistent with every `Claim.dataset` field (checked by the gate, `schema/write-gate.md`).
