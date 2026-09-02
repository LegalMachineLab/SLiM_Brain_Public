# Edges

| edge | from | to | grounding | when |
|---|---|---|---|---|
| MAKES | Source | Claim | n/a | always, one per claim |
| ABOUT | Claim | Concept | n/a | always (multiplicity: schema/concept.md) |
| CITES | Source | Source | n/a | only when both are in the corpus |
| USES | Source | Dataset | n/a | when the source uses or introduces the dataset |
| SUPPORTS | Claim | Claim | extracted only | one source explicitly gives reasons or evidence for a claim in another source, naming or citing it on that point |
| ATTACKS | Claim | Claim | extracted only | one source explicitly denies or gives reasons against a claim in another source, naming or citing it on that point |
| COMPATIBLE_WITH | Claim | Claim | inferred only | you judge from content alone that two claims from different sources reinforce each other, with no citation link on the point |
| IN_TENSION_WITH | Claim | Claim | inferred only | you judge from content alone that two claims from different sources are in tension, with no citation link on the point |
| SAME_AS | Claim | Claim | extracted or inferred | two claims from different sources assert the same proposition for the same jurisdiction and claim type |

MAKES and ABOUT are implicit in the claim record — MAKES from `Claim.source`, ABOUT from `Claim.concepts` — and are never written to `edges.jsonl`; pages and `structure.md` derive them from `claims.jsonl`. Write the other seven edge types to `edges.jsonl`.

SAME_AS identity (the `when` cell above) is strict on all three elements: a descriptive claim about the EU and the same sentence about the United States are not SAME_AS; a normative claim and its descriptive counterpart are not SAME_AS.

The grounding column is a hard pairing, so the strength of the label never exceeds the strength of the evidence (enforced by the gate, schema/write-gate.md).

Write every `edges.jsonl` object as `{type, from, to, run_id}`. The five cross-source claim edge types — SUPPORTS, ATTACKS, COMPATIBLE_WITH, IN_TENSION_WITH, SAME_AS — additionally carry:

```yaml
grounding: extracted | inferred   # extracted: one of the two sources names or cites the other on this point; inferred: judged from content alone
plausibility: high | medium | low # on an extracted edge, how squarely the named citation addresses the target claim; on an inferred edge, how plausible the relation is from content alone — not claim fidelity (schema/claim.md)
note:                             # one sentence saying why the edge holds; on SUPPORTS and ATTACKS, name the citation link that grounds the edge
```

Edges touching a rejected or superseded claim follow the exclusion scope in schema/claim.md.

The procedural rules for creating cross-source claim edges — candidate-set generation, target selection for extracted edges, direction — are in the `create-edges` skill.
