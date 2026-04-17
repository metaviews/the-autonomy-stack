# Sources

This directory contains source material used to build the Autonomy Stack.

## Metaviews: Future of Authority

The primary source corpus is the *Metaviews: Future of Authority* newsletter — the workshop, laboratory, and stress-testing environment for the Autonomy Stack. 296 issues, running October 2024 through March 2026.

Raw newsletter issues are stored in `metaviews.substack.com/posts/` as individual HTML files alongside the Substack export metadata.

Extracted artifacts are written to `extractions/` — one markdown file per issue, named `YYYY-MM-DD--slug.md`. Each extraction is structured by category: signals, pattern candidates, stack material, concepts, provocations, and other.

## Extraction Pipeline

Run from the repository root:

```bash
pip install -r scripts/requirements.txt
python scripts/extract.py                          # process all unprocessed issues
python scripts/extract.py --limit 10              # process next 10 issues only
python scripts/extract.py --model <openrouter-id> # override model
python scripts/extract.py --reset                 # clear checkpoint and reprocess all
```

Requires `OPENROUTER_API_KEY` in the environment. Default model: `google/gemini-flash-1.5`.

Progress is checkpointed after each issue in `extractions/.checkpoint.json` — safe to interrupt and resume.

## Philosophers of Autonomy

`philosophers/` is a compiled knowledge corpus for thinkers and concepts that illuminate autonomy, self-governance, freedom, agency, authority, and related tensions.

It follows a Compiled Knowledge Infrastructure pattern:

- `raw/` preserves source records and bibliographic notes.
- `wiki/` contains agent-maintained synthesis pages.
- `schema.md` defines the workflow and page conventions.
- `index.yaml` gives agents a lightweight routing layer.

Compiled pages must distinguish source claims, interpretive synthesis, and Stack application.
