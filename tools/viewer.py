#!/usr/bin/env python3
"""Build viewer.html — the self-contained explorer for this knowledge graph.

Reads wiki/ (claims and edges jsonl, absences, page frontmatters) and raw/
(quotation budgets), fills tools/viewer_template.html with the data blob, and
writes viewer.html at the repository root. Read-only over the graph: nothing
in wiki/ or raw/ is ever written. Run through the `publish-viewer` skill.

    python3 tools/viewer.py [--verify] [--name NAME]

--verify builds in memory and compares against the existing viewer.html
(record counts and analytics) without writing; exit 1 on mismatch.
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "viewer_template.html"

# Facet definitions per tab. Data-driven: a field no record carries is dropped,
# so graphs from different schema generations show only what they actually have.
FACET_SPEC = {
    "claims": [
        {"f": "source", "label": "Source", "multi": False, "fmt": "source"},
        {"f": "claim_type", "label": "Claim type", "multi": False, "fmt": "plain"},
        {"f": "basis", "label": "Basis", "multi": False, "fmt": "plain"},
        {"f": "claim_jurisdiction", "label": "Claim jurisdiction", "multi": True, "fmt": "plain"},
        {"f": "concepts", "label": "Concept", "multi": True, "fmt": "concept"},
        {"f": "positive_form", "label": "Positive form", "multi": False, "fmt": "plain"},
        {"f": "fidelity", "label": "Fidelity", "multi": False, "fmt": "plain"},
        {"f": "verification_status", "label": "Verification", "multi": False, "fmt": "plain"},
        {"f": "dataset", "label": "Dataset", "multi": False, "fmt": "plain"},
        {"f": "_jinf", "label": "Jurisdiction inferred", "multi": False, "fmt": "plain"},
    ],
    "sources": [
        {"f": "contribution_type", "label": "Contribution type", "multi": True, "fmt": "plain"},
        {"f": "source_jurisdiction", "label": "Source jurisdiction", "multi": True, "fmt": "plain"},
        {"f": "venue_type", "label": "Venue type", "multi": False, "fmt": "plain"},
        {"f": "_year", "label": "Year", "multi": False, "fmt": "plain"},
        {"f": "discipline_of_authors", "label": "Discipline", "multi": True, "fmt": "plain"},
    ],
    "concepts": [
        {"f": "status", "label": "Status", "multi": False, "fmt": "plain"},
        {"f": "concept_type", "label": "Concept type", "multi": False, "fmt": "plain"},
        {"f": "sources", "label": "Has claims from", "multi": True, "fmt": "source"},
    ],
    "datasets": [
        {"f": "jurisdiction", "label": "Jurisdiction", "multi": True, "fmt": "plain"},
        {"f": "language", "label": "Language", "multi": True, "fmt": "plain"},
        {"f": "availability", "label": "Availability", "multi": False, "fmt": "plain"},
        {"f": "annotation", "label": "Annotation", "multi": False, "fmt": "plain"},
        {"f": "introduced_by", "label": "Introduced by", "multi": False, "fmt": "source"},
    ],
    "edges": [
        {"f": "type", "label": "Edge type", "multi": False, "fmt": "plain"},
        {"f": "_grounding", "label": "Grounding", "multi": False, "fmt": "plain"},
        {"f": "_plaus", "label": "Plausibility", "multi": False, "fmt": "plain"},
    ],
    "absences": [
        {"f": "scope", "label": "Scope", "multi": False, "fmt": "plain"},
        {"f": "detected_in", "label": "Detected in", "multi": False, "fmt": "plain"},
        {"f": "resolved_reading", "label": "Resolved reading", "multi": False, "fmt": "plain"},
    ],
    # The graph tab draws all four node kinds at once, so its facets are the
    # union of the node facets. "owner" names the kind that carries the field:
    # a selected facet constrains only that kind and leaves the others alone,
    # which is what keeps a source-only filter from emptying the canvas of
    # claims. It also keeps colliding field names apart (Source.language is
    # not Dataset.language).
    "graph": [
        {"f": "_kind", "label": "Node type", "multi": False, "fmt": "kind", "owner": None},

        {"f": "contribution_type", "label": "Contribution type", "multi": True, "fmt": "plain", "owner": "sources"},
        {"f": "source_jurisdiction", "label": "Source jurisdiction", "multi": True, "fmt": "plain", "owner": "sources"},
        {"f": "venue_type", "label": "Venue type", "multi": False, "fmt": "plain", "owner": "sources"},
        {"f": "_year", "label": "Year", "multi": False, "fmt": "plain", "owner": "sources"},
        {"f": "discipline_of_authors", "label": "Discipline", "multi": True, "fmt": "plain", "owner": "sources"},

        {"f": "source", "label": "Claim: source", "multi": False, "fmt": "source", "owner": "claims"},
        {"f": "claim_type", "label": "Claim type", "multi": False, "fmt": "plain", "owner": "claims"},
        {"f": "basis", "label": "Claim basis", "multi": False, "fmt": "plain", "owner": "claims"},
        {"f": "basis_qualifier", "label": "Basis qualifier", "multi": False, "fmt": "plain", "owner": "claims"},
        {"f": "claim_jurisdiction", "label": "Claim jurisdiction", "multi": True, "fmt": "plain", "owner": "claims"},
        {"f": "concepts", "label": "Claim maps to concept", "multi": True, "fmt": "concept", "owner": "claims"},
        {"f": "positive_form", "label": "Positive form", "multi": False, "fmt": "plain", "owner": "claims"},
        {"f": "temporal_reference", "label": "Temporal reference", "multi": False, "fmt": "plain", "owner": "claims"},
        {"f": "fidelity", "label": "Fidelity", "multi": False, "fmt": "plain", "owner": "claims"},
        {"f": "verification_status", "label": "Verification", "multi": False, "fmt": "plain", "owner": "claims"},
        {"f": "dataset", "label": "Claim rests on dataset", "multi": False, "fmt": "plain", "owner": "claims"},
        {"f": "_jinf", "label": "Jurisdiction inferred", "multi": False, "fmt": "plain", "owner": "claims"},

        {"f": "status", "label": "Concept status", "multi": False, "fmt": "plain", "owner": "concepts"},
        {"f": "concept_type", "label": "Concept family", "multi": False, "fmt": "plain", "owner": "concepts"},
        {"f": "broader", "label": "Broader concept", "multi": True, "fmt": "concept", "owner": "concepts"},
        {"f": "sources", "label": "Concept has claims from", "multi": True, "fmt": "source", "owner": "concepts"},

        {"f": "jurisdiction", "label": "Dataset jurisdiction", "multi": True, "fmt": "plain", "owner": "datasets"},
        {"f": "language", "label": "Dataset language", "multi": True, "fmt": "plain", "owner": "datasets"},
        {"f": "availability", "label": "Availability", "multi": False, "fmt": "plain", "owner": "datasets"},
        {"f": "annotation", "label": "Annotation", "multi": False, "fmt": "plain", "owner": "datasets"},
        {"f": "agreement_reported", "label": "Agreement reported", "multi": False, "fmt": "plain", "owner": "datasets"},
        {"f": "introduced_by", "label": "Introduced by", "multi": False, "fmt": "source", "owner": "datasets"},
    ],
}

CLAIM_EDGE_TYPES = {"SUPPORTS", "ATTACKS", "COMPATIBLE_WITH", "IN_TENSION_WITH", "SAME_AS"}


def die(msg):
    sys.exit(f"viewer.py: {msg}")


def read_jsonl(path):
    if not path.exists():
        die(f"missing {path}")
    out = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as e:
            die(f"{path}:{i}: bad JSON ({e})")
    return out


def parse_value(v):
    v = v.strip()
    if v == "":
        return None
    if v in ("true", "false"):
        return v == "true"
    if v.startswith("["):
        try:
            return json.loads(v)
        except json.JSONDecodeError:
            return [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
    v = v.strip("\"'")
    return int(v) if re.fullmatch(r"\d+", v) else v


def frontmatter(path):
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"---\r?\n(.*?)\r?\n---", txt, re.S)
    if not m:
        die(f"no frontmatter in {path}")
    out, cur = {}, None
    for line in m.group(1).splitlines():
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*:", line):
            k, _, v = line.partition(":")
            cur = k
            out[k] = parse_value(v)
        elif line.strip().startswith("- ") and cur is not None:
            if not isinstance(out.get(cur), list):
                out[cur] = []
            out[cur].append(line.strip()[2:].strip().strip("\"'"))
    return out


def read_pages(dirpath):
    if not dirpath.is_dir():
        die(f"missing directory {dirpath}")
    return sorted((frontmatter(p) for p in sorted(dirpath.glob("*.md"))), key=lambda r: str(r.get("id", "")))


def counting(c):
    """schema/claim.md, Verification vocabulary: a rejected or superseded claim,
    and every edge touching it, is excluded from distribution counts and tables.
    Exclusion is a rendering rule — the record itself is kept untouched."""
    return not (c.get("verification_status") == "rejected" or c.get("superseded_by"))


def count_field(records, field):
    c = Counter()
    for r in records:
        v = r.get(field)
        if v in (None, "", []):
            continue
        for x in (v if isinstance(v, list) else [v]):
            c[str(x)] += 1
    return dict(c.most_common())


def build_data(name):
    w = ROOT / "wiki"
    claims = read_jsonl(w / "claims" / "claims.jsonl")
    edges = read_jsonl(w / "graph" / "edges.jsonl")
    absences = read_jsonl(w / "absences.jsonl") if (w / "absences.jsonl").exists() else []
    sources = read_pages(w / "sources")
    concepts = read_pages(w / "concepts")
    datasets = read_pages(w / "datasets") if (w / "datasets").is_dir() else []
    if not claims or not sources:
        die("empty graph: need at least one claim and one source page")

    # derived per-record fields
    for s in sources:
        fam = str((s.get("authors") or ["?"])[0]).split(",")[0].strip()
        s["short"] = f"{fam} {s.get('year', '')}".strip()
        s["_year"] = str(s.get("year", "")) or None
        s["_kind"] = "sources"
    for c in claims:
        qs = c.get("quotes") or []
        c["quote"] = " ⧦ ".join(q.get("quote", "") for q in qs)          # search-compat
        c["location"] = "; ".join(str(q.get("location", "")) for q in qs)      # search-compat
        c["_jinf"] = bool(c.get("jurisdiction_inferred"))
        c["_excluded"] = not counting(c)
        c["_kind"] = "claims"
    for d in datasets:
        d["_kind"] = "datasets"
    for e in edges:
        e["_grounding"] = e.get("grounding") or "n/a"
        e["_plaus"] = e.get("plausibility") or "n/a"

    counted = [c for c in claims if counting(c)]

    fam_of = {c["id"]: c.get("concept_type") for c in concepts}
    label_of = {c["id"]: c.get("label", c["id"]) for c in concepts}

    # Concept tallies. Read by the concept rows, the overview table and the
    # drawer; no concept page carries them (schema/concept.md defines no such
    # field), so they are derived here and never written back to the wiki.
    for k in concepts:
        about = [c for c in counted if k["id"] in (c.get("concepts") or [])]
        k["n_claims"] = len(about)
        k["n_sources"] = len({c["source"] for c in about})
        k["_kind"] = "concepts"

    # facets: keep a definition only when some record carries the field
    pools = {"claims": claims, "sources": sources, "concepts": concepts,
             "datasets": datasets, "edges": edges, "absences": absences,
             "graph": sources + claims + concepts + datasets}
    facets = {}
    for tab, defs in FACET_SPEC.items():
        kept = []
        for d in defs:
            vals = set()
            pool = pools[tab]
            if d.get("owner"):
                pool = [r for r in pool if r.get("_kind") == d["owner"]]
            for r in pool:
                v = r.get(d["f"])
                if v in (None, "", []):
                    continue
                for x in (v if isinstance(v, list) else [v]):
                    vals.add(str(x))
            if vals:
                d2 = dict(d)
                d2["list"] = sorted(vals)
                kept.append(d2)
        facets[tab] = kept

    # links (jsonl edges, then implicit MAKES/ABOUT for the ego graph) + adjacency
    links = [{"f": e["from"], "t": e["to"], "ty": e["type"], "g": e.get("grounding"),
              "p": e.get("plausibility"), "n": e.get("note"), "i": i, "im": False}
             for i, e in enumerate(edges)]
    for c in claims:
        links.append({"f": c["source"], "t": c["id"], "ty": "MAKES",
                      "g": None, "p": None, "n": None, "i": -1, "im": True})
        for k in c.get("concepts", []):
            links.append({"f": c["id"], "t": k, "ty": "ABOUT",
                          "g": None, "p": None, "n": None, "i": -1, "im": True})
    adjacency = defaultdict(list)
    for i, l in enumerate(links):
        adjacency[l["f"]].append(i)
        adjacency[l["t"]].append(i)

    # analytics — all of it over `counted`, per the exclusion scope above
    concern, family = Counter(), Counter()
    for c in counted:
        fams = set()
        for k in c.get("concepts", []):
            f = fam_of.get(k)
            if f:
                fams.add(f)
            if f == "normative_concern":
                concern[label_of[k]] += 1
        for f in fams:
            family[f] += 1

    budgets = {}
    for s in sources:
        raw = ROOT / str(s.get("file", ""))
        chars = len(raw.read_text(encoding="utf-8", errors="ignore")) if raw.exists() else 0
        quoted = sum(len(q.get("quote", "")) for c in claims if c["source"] == s["id"]
                     for q in (c.get("quotes") or []))
        budgets[s["id"]] = {"share": round(quoted / chars, 5) if chars else 0, "chars": chars}

    tbs = defaultdict(Counter)
    for c in counted:
        tbs[c["source"]][c.get("claim_type", "?")] += 1

    # Edges touching an excluded claim are excluded with it (schema/claim.md).
    dropped = {c["id"] for c in claims if not counting(c)}
    live = [e for e in edges if e["from"] not in dropped and e["to"] not in dropped]

    # The two-dimensional map of the field: legal task against technique class.
    # Claims carry no facet fields of their own — the classification is carried
    # entirely by Claim.concepts (schema/claim.md) — so the axes are the concept
    # grid itself, read through concept_type.
    def axis(fam):
        return [k for k in concepts if k.get("concept_type") == fam and not k.get("deprecated")]
    rows_c, cols_c = axis("legal_task"), axis("technique_class")
    matrix = None
    if rows_c and cols_c:
        cells = [[sum(1 for c in counted
                      if r["id"] in (c.get("concepts") or []) and k["id"] in (c.get("concepts") or []))
                  for k in cols_c] for r in rows_c]
        matrix = {"rows": [r.get("label", r["id"]) for r in rows_c],
                  "cols": [k.get("label", k["id"]) for k in cols_c],
                  "row_ids": [r["id"] for r in rows_c], "col_ids": [k["id"] for k in cols_c],
                  "cells": cells}

    by_tg = Counter((e["type"], e["_grounding"]) for e in live)
    analytics = {
        "claims_by_type": count_field(counted, "claim_type"),
        "claims_by_family": dict(family.most_common()),
        "claims_by_basis": count_field(counted, "basis"),
        "claims_by_fidelity": count_field(counted, "fidelity"),
        "claims_by_jurisdiction": count_field(counted, "claim_jurisdiction"),
        "claims_by_concern": dict(concern.most_common()),
        "sources_by_contribution": count_field(sources, "contribution_type"),
        "edges_by_type_grounding": {f"{t} ({g})": n for (t, g), n in by_tg.most_common()},
        "n_extracted": sum(1 for e in live if e["type"] in CLAIM_EDGE_TYPES and e.get("grounding") == "extracted"),
        "n_inferred": sum(1 for e in live if e["type"] in CLAIM_EDGE_TYPES and e.get("grounding") == "inferred"),
        "n_cites": sum(1 for e in live if e["type"] == "CITES"),
        "matrix": matrix,
        "budgets": budgets,
        "claims_by_type_by_source": {k: dict(v) for k, v in tbs.items()},
    }

    # absence index: every source/concept id named in a record's description
    known = {r["id"] for r in sources} | {r["id"] for r in concepts}
    absence_index = defaultdict(list)
    for a in absences:
        for mid in sorted(set(re.findall(r"SRC-\d{4}|CPT-[a-z0-9-]+", str(a.get("description", ""))))):
            if mid in known:
                absence_index[mid].append(a["id"])

    versions = sorted({str(c.get("schema_version", "?")) for c in claims})
    models = Counter(str(c.get("extraction_model", "")) for c in claims)
    meta = {
        "name": name,
        "generated": date.today().isoformat(),
        "schema_version": "/".join(versions),
        "extraction_model": models.most_common(1)[0][0] if models else "",
        "root": ROOT.name,
        "lede": (f"A knowledge graph over the AI-and-law literature: {len(sources)} sources and "
                 f"{len(claims)} claims, built under a schema that keeps what was read apart from what "
                 "was inferred. Every claim is anchored to verbatim passages in its own source, and "
                 "nothing reached this graph without passing a write gate."),
        "a2": (f"This corpus carries {analytics['n_extracted']} extracted claim relations — where one "
               f"source names or cites the other on the point — against {analytics['n_inferred']} the "
               "model inferred from content alone."),
        "extracted_empty": ("None on this record. An extracted relation requires one of the two sources "
                            "to name or cite the other on this point (schema/edges.md)."),
        "n_banner": (f"<b>n = {len(sources)}.</b> These distributions describe this corpus, not the "
                     f"AI-and-law literature. No quantitative claim about the field follows from "
                     f"{len(sources)} sources."),
        "graph_lede": ("The graph as it is stored: sources, the claims they make, the concepts those "
                       "claims are about, and the datasets they rest on. Solid green edges were read "
                       "in the sources; dashed amber ones were inferred by the model; grey ones are "
                       "structural. Faint grey links are implied by a claim record rather than written "
                       "to edges.jsonl, and are never counted as edges."),
        "graph_caption": ("Position and connectedness in this drawing measure attention, not endorsement "
                          "or authority. Nothing here ranks a source (C.7)."),
        "graph_collapsed_note": ("Claims are collapsed in this view: a source-to-concept link stands for "
                                 "the claims mapping that source to that concept, and a source-to-source "
                                 "link for relations between their claims. Such a link is an aggregation "
                                 "for drawing, never a record in the graph — and an extracted relation is "
                                 "never merged with an inferred one."),
        "graph_large_note": ("Large graph: claims are collapsed automatically so the drawing stays legible. "
                             "Switch to Full to draw every claim node, or filter first."),
    }

    return {"meta": meta, "sources": sources, "claims": claims, "concepts": concepts,
            "datasets": datasets, "edges": edges, "absences": absences, "facets": facets,
            "links": links, "adjacency": dict(adjacency), "analytics": analytics,
            "absence_index": dict(absence_index)}


def render(data, name):
    if not TEMPLATE.exists():
        die(f"missing {TEMPLATE}")
    tpl = TEMPLATE.read_text(encoding="utf-8")
    for ph in ("__PAGE_TITLE__", "__BRAIN_DATA__"):
        if ph not in tpl:
            die(f"{TEMPLATE.name} lacks placeholder {ph}")
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return tpl.replace("__PAGE_TITLE__", name).replace("__BRAIN_DATA__", blob)


def embedded(path):
    m = re.search(r'id="brain-data">(.*?)</script>', path.read_text(encoding="utf-8"), re.S)
    return json.loads(m.group(1)) if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--name", default="SLiM Brain Explorer")
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()

    data = build_data(a.name)
    out = ROOT / "viewer.html"

    if a.verify:
        cur = embedded(out) if out.exists() else None
        if cur is None:
            die(f"--verify: no existing {out} to compare against")
        problems = []
        for k in ("sources", "claims", "concepts", "datasets", "edges", "absences"):
            if len(cur.get(k, [])) != len(data[k]):
                problems.append(f"{k}: built {len(data[k])}, embedded {len(cur.get(k, []))}")
        for k, v in data["analytics"].items():
            if k in ("budgets",):
                continue
            if cur.get("analytics", {}).get(k) != v:
                problems.append(f"analytics.{k} differs")
        if problems:
            print("STALE — viewer.html does not match the wiki:")
            for p in problems:
                print(" -", p)
            sys.exit(1)
        print(f"OK — viewer.html matches the wiki "
              f"({len(data['claims'])} claims, {len(data['edges'])} edges, {len(data['absences'])} absences).")
        return

    html = render(data, a.name)
    out.write_text(html, encoding="utf-8")
    chk = embedded(out)
    assert chk and len(chk["claims"]) == len(data["claims"]), "post-write verification failed"
    print(f"wrote {out} — {len(data['sources'])} sources, {len(data['claims'])} claims, "
          f"{len(data['edges'])} edges, {len(data['links'])} links, {len(data['absences'])} absences, "
          f"{len(html) // 1024} KB")


if __name__ == "__main__":
    main()
