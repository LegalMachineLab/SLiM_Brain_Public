---
name: map-concepts
description: Use when mapping extracted claims to concepts (step 3 of ingest-source) or when deciding whether to create a candidate concept. The concept vocabulary is the three-family grid in schema/concept.md, which also fixes the per-claim mapping caps. Defines the concept registry (Retrieval discipline) and the retrofit on creation.
---

# Map claims to concepts

Read `schema/concept.md` (node schema, statuses, the anchor grid and its three families) before mapping. 

## Retrieval discipline

Decide whether a concept exists from the concept registry: the anchor grid in `schema/concept.md` plus the `wiki/concepts/` directory listing (a page's filename is its id). Consult a page's frontmatter only to check its label, aliases, and one-line definition against a suspected synonym. Never load full concept page bodies to decide whether a concept exists.

## Rules for concepts

- Map every claim within the count and per-family cap rules of `schema/concept.md`.
- When an anchor and a non-anchor concept both fit a claim without distortion, map both (within the cap). "Prefer anchors" means only this: never coin or use a candidate where an anchor alone captures the claim.
- Leave unengaged families absent, per `schema/concept.md`.
- Create a candidate concept only when at least one claim cannot be placed under any anchor of any family without distortion. Give the candidate the family it extends (`concept_type: legal_task | technique_class | normative_concern`), or `other` when none fits. Give it a label that is a noun phrase of at most five words, in the source's own terms. Write its `wiki/concepts/` page frontmatter immediately at creation — the page listing is the registry entry the next mapping reads; the page body regenerates at the batch close-out (`ingest-source`).
- Before creating a candidate, check the concept registry for an existing concept with the same meaning under another name; if you find one, add an alias to it instead of creating.
- Queue a claim for adjudication in `wiki/log.md` only when, after applying every mapping rule here, you cannot choose between two concrete mappings — including whether a candidate is warranted. A claim that fits no existing concept is the candidate-creation case, never a queue case. Never resolve the choice by guessing.
- When you queue a claim, set its whole source aside — a claim cannot pass the gate without a concept, so the whole source waits — following the set-aside procedure in `ingest-source` (Sequential processing). Exception: the retrofit stands (Retrofit on creation below).
- Set `concept_type` (the family) on every concept; it is mandatory. It drives the two-dimensional maps of the field (legal task against technique class, normative concern against claim jurisdiction).
- Do not create a concept for a jurisdiction, an instrument, a court, a person, an institution, or a paper. These are attributes or sources.
- Label the notion, not a source. "Ardian (controls Maxeda)" is the kind of label that must never occur: information from one source must not be carried into a label that other sources share.
- Promotion and deprecation follow `schema/concept.md` (threshold, counting, timing); neither is ever a mapping judgment.

## Retrofit on creation

A concept created at source n must reach the claims mapped before it existed. Run the retrofit immediately after creating the candidate:

1. Read only the `id` and `statement` fields of every claim in `wiki/claims/claims.jsonl` that is not `rejected` and does not carry `superseded_by` — the field projection is this pass's filter (bounded retrieval: CLAUDE.md). The pass stays affordable because candidate creation is rare and decays as the registry grows.
2. Add the new concept, in place, to every such claim that engages the notion, under the same mapping rules as step 3 (Rules for concepts above). A retrofit addition is a sanctioned in-place update (`schema/write-gate.md`). Retrofit only ever ADDS a concept — removing or replacing an existing mapping is a team decision. Log each addition in `wiki/log.md`.
3. When a claim is already at the per-family cap in the candidate's family (`schema/concept.md`), add nothing to that claim and log the collision in `wiki/log.md` for team adjudication.
4. Run the retrofit's edge generation as part of the CURRENT ingest's step 6, never mid-step-3 — procedure and pair-dedup rule in `create-edges`.
5. Retrofit additions are records modified this batch; their owning pages join the batch's close-out queue (`ingest-source`).

For what a set-aside of the triggering source leaves standing — and the completion work owed before moving on — see `ingest-source` (Sequential processing).
