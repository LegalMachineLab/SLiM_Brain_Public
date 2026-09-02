---
name: publish-viewer
description: Use when the interactive graph explorer needs rebuilding from the wiki or the shared artifact needs refreshing — after a batch close-out, after a team decision changes records, or on request. Runs tools/viewer.py (read-only over the graph), verifies the result, and republishes viewer.html to the project's canonical artifact URL.
---

# Rebuild and publish the viewer

`viewer.html` at the repository root is a generated, self-contained explorer page over the graph: it embeds a snapshot of `wiki/` (claims, edges, absences, page frontmatters) plus quotation budgets computed from `raw/`. It is a **read-only rendering outside the pipeline** — building it writes nothing into `wiki/` or `raw/`, so no write gate applies, and nothing in it is ever a retrieval path for answering questions about the literature (that remains `query-graph`).

Never hand-edit `viewer.html`. Content problems are wiki problems — fix the record through the responsible skill and rebuild. Look-and-feel problems (styles, markup, page JS) live in `tools/viewer_template.html`; edit that, then rebuild.

## Procedure

1. **Build.** From the repository root:

   ```bash
   python3 tools/viewer.py
   ```

   It prints the record counts it embedded and the output size. If it dies, the error names the offending file or record; do not work around it by editing `viewer.html`.

2. **Verify.** Confirm the written page matches the wiki:

   ```bash
   python3 tools/viewer.py --verify
   ```

   It must print `OK`. `STALE` immediately after a fresh build means the builder itself is broken — stop and report; do not patch the output.

3. **Publish.** Republish `viewer.html` with the Artifact tool to a new artifact:

   - `file_path`: the repository's `viewer.html`
   - `favicon`: `🧠` (keep it stable)
   

4. **Report.** Tell the user the embedded counts and the artifact link. Leave the regenerated `viewer.html` uncommitted — git history belongs to the user.
