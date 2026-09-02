---
name: convert-source
description: Use when PDFs in raw/ need their markdown conversion — before any ingest, when new PDFs arrive, or when a conversion looks garbled. Runs tools/convert_source.py (docling), which caches results in raw/_conversions.json and skips PDFs already converted. Covers the held-fixed-tool policy, reconversion flags, and page markers.
---

# Convert source PDFs to markdown

Ingest works from the markdown conversion, never from the PDF (the ingest-input rule of the `ingest-source` skill). The `.md` in `raw/` is the canonical text layer (CLAUDE.md layout; quote verification and the quotation budget: `schema/write-gate.md`). The PDF stays in `raw/` beside its `.md` as the original; consult it only to diagnose a conversion artifact.

## Running the conversion

The conversion tool is `tools/convert_source.py`, which wraps docling with pinned settings. It requires the project venv:

```bash
# one-time bootstrap if the venv is missing (version pinned to the corpus tool;
# keep in sync with the docling_version in raw/_conversions.json):
python3 -m venv ~/.venvs/bad_brain
~/.venvs/bad_brain/bin/pip install "docling==2.123.1"

# convert everything not yet converted (cached files are skipped):
~/.venvs/bad_brain/bin/python tools/convert_source.py

# cache status only:
~/.venvs/bad_brain/bin/python tools/convert_source.py --check

# reconvert ONE garbled or scanned file (flags apply only to the files named):
~/.venvs/bad_brain/bin/python tools/convert_source.py --force --ocr raw/<name>.pdf
```

Caching: `raw/_conversions.json` records each PDF's SHA-256, the docling version, and the settings it was converted with. A PDF whose `.md` exists and whose recorded SHA-256 and docling version match is skipped — the recorded settings are per-file and preserved, so a plain run never undoes a per-file deviation such as one `--ocr` source. A changed PDF reconverts. A changed docling version marks the file **stale**, but the script never reconverts a stale file silently — it refuses until `--force`, because a tool change is a logged event (Rules below). `--force` is also how new settings are applied to a file.

## Rules

- Hold one conversion tool fixed across the corpus. A docling upgrade or a settings change (for example `--ocr` for a scanned source) can change extraction, so it is a logged event: note it in `wiki/log.md`. The script itself records the per-file version and settings in `raw/_conversions.json`, so write nothing else.
- The script prints the exact `conversion_tool` string after converting (the manifest's `conversion_tool` entry holds it per file); at ingest it fills the Source node's field per `schema/source.md`.
- Never hand-edit a generated `.md`. When a conversion is wrong (garbled columns, mangled footnotes, missing text), fix it by reconverting — different settings, a newer docling, `--ocr` — and log the change; or log the difficulty and live with it. (A hand-edited file would contain text that exists in no source, and quotes anchored to it would be fabrications.)
- Page markers: the script numbers pages as `<!-- page: N -->` comments (page 1 is the top of the file). Use them for the `location` of each anchor in a claim's `quotes`. If a file has no markers (older docling without page-break support), each anchor's `location` falls back as `schema/claim.md` provides.
- OCR is off by default (academic PDFs carry a text layer; OCR adds nondeterminism). The script warns when a PDF yields suspiciously little text — that is the scanned-source case for `--ocr`.

## After converting

Skim each new `.md` for the two failure shapes law-review PDFs produce: interleaved two-column text and footnotes merged into the body. If a file shows them, reconvert before ingesting; if the artifact persists, record it in `wiki/log.md` at ingest so extraction difficulties can be traced to conversion.

Conversion does not ingest. When the markdown is in place, ingest through the `ingest-source` skill, which runs its own pre-checks.
