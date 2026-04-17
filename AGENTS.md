# Repository Guidelines

## Project Structure & Module Organization

The Autonomy Stack is a documentation-first governance framework. Most work is Markdown, with Python scripts for corpus processing.

- `stack/` contains the conceptual core. Start with `stack/entry.md`, `stack/00-overview.md`, and `stack/STATE.md`.
- `stack/modules/` holds the five completed domain modules.
- `stack/cases/` holds case studies, the case study template, and candidate workflow files.
- `patterns/` contains recurring governance dynamics with a shared section structure.
- `signals/` contains short timestamped orientation artifacts.
- `sources/` contains source material and structured extraction outputs.
- `scripts/` contains Python automation for extraction, pattern generation, and case generation.

## Build, Test, and Development Commands

There is no application build system and no formal test suite. Use the scripts only when working on generated or corpus-derived content.

```bash
pip install -r scripts/requirements.txt
python scripts/extract.py --limit 10
python scripts/generate_patterns.py --pattern "Pattern Name"
python scripts/find_cases.py --limit 10
python scripts/write_cases.py --case "Case Name"
```

Scripts read `.env` from the repository root. Required values are `OPENROUTER_API_KEY` and `OPENROUTER_MODEL`.

## Coding Style & Naming Conventions

Write Markdown in a direct, analytic voice. Prefer clear claims, explicit assumptions, and short sections over decorative prose. Keep cross-references relative, for example `[STATE.md](stack/STATE.md)`.

Use kebab-case file names for content files. Signals and extractions follow `YYYY-MM-DD--kebab-case-title.md`. Patterns use stable descriptive slugs such as `platform-capture.md`.

Python scripts should remain standard-library oriented where possible, use 4-space indentation, and keep command-line behavior explicit through `argparse`.

## Testing Guidelines

For Markdown-only changes, verify links, headings, and naming conventions manually. For script changes, run the narrowest relevant command with a small limit first, such as:

```bash
python scripts/find_cases.py --limit 3
```

Pipeline scripts checkpoint progress and are designed to resume safely. Avoid full corpus runs unless the change requires it.

## Commit & Pull Request Guidelines

Recent commits use short, plain-English summaries such as `added case example generation` and `finished first roadmap pass`. Follow that style: concise, lower-friction, and focused on the change.

Pull requests should include a short description, the affected paths, and any commands run. For conceptual changes, note which core documents informed the edit, especially `PRINCIPLES.md`, `stack/STATE.md`, and `stack/PROVOCATIONS.md`.

## Agent-Specific Instructions

Before major structural additions, read `PRINCIPLES.md` and `stack/PROVOCATIONS.md`. Many apparent gaps are already framed as unresolved tensions. Preserve the project’s content flow: narrative source material informs extractions, signals, patterns, stack layers, modules, and case studies through editorial judgment rather than automation alone.
