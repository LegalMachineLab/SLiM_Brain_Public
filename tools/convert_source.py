#!/usr/bin/env python3
"""Convert source PDFs in raw/ to markdown with docling, with caching.

The markdown conversion is the canonical text layer of the corpus: the write
gate verifies claim quotes against it and the quotation budget is computed
over it. This script is therefore the single, held-fixed conversion tool the
schema requires (Source field `conversion_tool`), and its output is never
hand-edited.

Caching: raw/_conversions.json records, per PDF, the source SHA-256, the
docling version, and the settings used. A PDF is skipped when its .md exists
and the recorded SHA-256 and docling version match; the recorded settings are
per-file and preserved (a file converted with --ocr stays as converted even
when later runs omit the flag). A docling version mismatch marks the file
stale but never reconverts it silently: --force is required, because a tool
change can alter the canonical text quotes are anchored to and must be a
logged event. --force also reconverts to apply new settings to a file.

Usage:
  convert_source.py [PDF ...]     convert the given PDFs (default: all raw/*.pdf)
  convert_source.py --check       report cache status only, convert nothing
  convert_source.py --force ...   reconvert even when cached
  convert_source.py --ocr ...     enable OCR (scanned sources only; deviation
                                  from the corpus-wide settings must be logged)
"""

import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
MANIFEST = RAW / "_conversions.json"
PAGE_BREAK_SENTINEL = "\x00DOCLING-PAGE-BREAK\x00"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {}


def save_manifest(manifest: dict) -> None:
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def docling_version() -> str:
    from importlib.metadata import version
    return version("docling")


def settings_fingerprint(ocr: bool) -> dict:
    return {"do_ocr": ocr, "do_table_structure": True, "page_markers": True}


def conversion_tool_string(ocr: bool) -> str:
    s = settings_fingerprint(ocr)
    return (
        f"docling {docling_version()}, tools/convert_source.py, "
        f"ocr={'on' if s['do_ocr'] else 'off'}, table_structure={'on' if s['do_table_structure'] else 'off'}"
    )


def cache_state(pdf: Path, manifest: dict) -> str:
    """'cached' | 'stale_version' (tool changed since conversion) | 'missing'.

    Deliberately ignores the current run's flags: the settings a file was
    converted with are per-file and preserved, so a plain run never undoes a
    documented per-file deviation (e.g. one scanned source converted --ocr).
    """
    entry = manifest.get(pdf.name)
    if entry is None:
        return "missing"
    md = RAW / entry.get("md_file", "")
    if not md.exists() or entry.get("sha256") != sha256_of(pdf):
        return "missing"
    if entry.get("docling_version") != docling_version():
        return "stale_version"
    return "cached"


def number_page_markers(md: str) -> str:
    # Page 1 starts at the top of the file; each sentinel opens the next page.
    parts = md.split(PAGE_BREAK_SENTINEL)
    if len(parts) == 1:
        return md
    out = [parts[0]]
    for i, part in enumerate(parts[1:], start=2):
        out.append(f"\n\n<!-- page: {i} -->\n\n")
        out.append(part)
    return "".join(out)


def convert_one(pdf: Path, ocr: bool):
    from docling.datamodel.base_models import ConversionStatus, InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    opts = PdfPipelineOptions()
    opts.do_ocr = ocr
    opts.do_table_structure = True
    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )
    result = converter.convert(pdf)
    if result.status not in (ConversionStatus.SUCCESS, ConversionStatus.PARTIAL_SUCCESS):
        raise RuntimeError(f"conversion failed with status {result.status}")

    try:
        md = result.document.export_to_markdown(page_break_placeholder=PAGE_BREAK_SENTINEL)
        md = number_page_markers(md)
        page_markers = True
    except TypeError:
        # docling-core without page_break_placeholder support: no page markers;
        # claim `location` must then use section heading + paragraph ordinal.
        md = result.document.export_to_markdown()
        page_markers = False

    if len(md.strip()) < 500:
        print(f"  WARNING: only {len(md.strip())} characters extracted from {pdf.name}; "
              f"likely a scanned PDF - rerun with --ocr and log the deviation.", file=sys.stderr)

    return md, result.status.name, page_markers


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdfs", nargs="*", type=Path, help="PDFs to convert (default: all raw/*.pdf)")
    ap.add_argument("--force", action="store_true", help="reconvert even when cached")
    ap.add_argument("--check", action="store_true", help="report cache status only")
    ap.add_argument("--ocr", action="store_true", help="enable OCR (scanned sources)")
    args = ap.parse_args()

    pdfs = args.pdfs or sorted(RAW.glob("*.pdf"))
    if not pdfs:
        print("no PDFs found in raw/")
        return 1

    manifest = load_manifest()

    if args.check:
        labels = {
            "cached": "cached",
            "missing": "needs conversion",
            "stale_version": "stale (converted with docling "
                             "{v}, installed {cur}; --force to reconvert, log the tool change)",
        }
        for pdf in pdfs:
            state = cache_state(pdf, manifest)
            label = labels[state].format(
                v=manifest.get(pdf.name, {}).get("docling_version"), cur=docling_version())
            print(f"{pdf.name}: {label}")
        return 0

    converted, skipped, stale, failed = [], [], [], []
    for pdf in pdfs:
        if not pdf.is_absolute():
            pdf = (ROOT / pdf).resolve()
        state = cache_state(pdf, manifest)
        if not args.force:
            if state == "cached":
                skipped.append(pdf.name)
                print(f"cached, skipping: {pdf.name}")
                continue
            if state == "stale_version":
                stale.append(pdf.name)
                print(f"STALE, not reconverting: {pdf.name} was converted with docling "
                      f"{manifest[pdf.name].get('docling_version')} but {docling_version()} is installed. "
                      f"A tool change alters the canonical text; reconvert with --force and log it in wiki/log.md.",
                      file=sys.stderr)
                continue
        print(f"converting: {pdf.name}")
        try:
            md, status, page_markers = convert_one(pdf, args.ocr)
        except Exception as e:
            failed.append((pdf.name, str(e)))
            print(f"  FAILED: {e}", file=sys.stderr)
            continue
        md_file = pdf.with_suffix(".md").name
        (RAW / md_file).write_text(md, encoding="utf-8")
        settings = settings_fingerprint(args.ocr)
        settings["page_markers"] = page_markers
        manifest[pdf.name] = {
            "md_file": md_file,
            "sha256": sha256_of(pdf),
            "docling_version": docling_version(),
            "settings": settings,
            "conversion_tool": conversion_tool_string(args.ocr),
            "conversion_status": status,
            "converted_at": date.today().isoformat(),
        }
        save_manifest(manifest)
        converted.append(md_file)
        print(f"  wrote raw/{md_file} ({len(md)} chars)")

    print(f"\ndone: {len(converted)} converted, {len(skipped)} cached, "
          f"{len(stale)} stale (kept), {len(failed)} failed")
    if converted:
        print(f"Source.conversion_tool for these files:\n  {conversion_tool_string(args.ocr)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
