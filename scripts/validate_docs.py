#!/usr/bin/env python
"""Validate agent-facing documentation indexes and local links."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(path: Path) -> dict[str, str]:
    text = read(path)
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def markdown_files() -> list[Path]:
    ignored_parts = {".git", "__pycache__", ".qwen"}
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if ignored_parts.intersection(path.parts):
            continue
        files.append(path)
    return files


def check_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for path in markdown_files():
        text = read(path)
        for match in link_pattern.finditer(text):
            target = match.group(1).strip()
            if not target or re.match(r"^(https?:|mailto:|#)", target):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.split("#", 1)[0]
            if not target:
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"{rel(path)} links outside repo: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{rel(path)} has missing link target: {target}")


def parse_index_entries(index_path: Path, id_key: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    item_start = re.compile(rf"^\s*-\s+{re.escape(id_key)}:\s*(.+?)\s*$")
    field = re.compile(r"^\s{4,}([a-zA-Z0-9_-]+):\s*(.+?)\s*$")
    for line in read(index_path).splitlines():
        start = item_start.match(line)
        if start:
            if current:
                entries.append(current)
            current = {id_key: start.group(1)}
            continue
        if current:
            found = field.match(line)
            if found:
                current[found.group(1)] = found.group(2)
    if current:
        entries.append(current)
    return entries


def parse_section_entries(index_path: Path, section: str, id_key: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_section = False
    item_start = re.compile(rf"^\s*-\s+{re.escape(id_key)}:\s*(.+?)\s*$")
    field = re.compile(r"^\s{4,}([a-zA-Z0-9_-]+):\s*(.+?)\s*$")

    for line in read(index_path).splitlines():
        if re.match(r"^[a-zA-Z0-9_-]+:", line):
            if line.startswith(f"{section}:"):
                in_section = True
                continue
            if in_section:
                break
        if not in_section:
            continue

        start = item_start.match(line)
        if start:
            if current:
                entries.append(current)
            current = {id_key: start.group(1)}
            continue
        if current:
            found = field.match(line)
            if found:
                current[found.group(1)] = found.group(2)

    if current:
        entries.append(current)
    return entries


def check_tool_index(errors: list[str]) -> None:
    tools_dir = ROOT / "stack" / "tools"
    index_path = tools_dir / "index.yaml"
    entries = parse_section_entries(index_path, "tools", "tool_id")
    indexed_ids: set[str] = set()
    required = {
        "tool_id",
        "title",
        "status",
        "primary_question",
        "applies_to",
        "related_layers",
        "related_requirements",
        "related_docs",
    }

    for entry in entries:
        tool_id = entry["tool_id"]
        indexed_ids.add(tool_id)
        if "path" not in entry:
            errors.append(f"{rel(index_path)} tool {tool_id} missing path")
            continue
        tool_path = tools_dir / entry["path"]
        if not tool_path.exists():
            errors.append(f"{rel(index_path)} tool {tool_id} path missing: {entry['path']}")
            continue
        fm = frontmatter(tool_path)
        missing = sorted(required - set(fm))
        if missing:
            errors.append(f"{rel(tool_path)} missing frontmatter fields: {', '.join(missing)}")
        if fm.get("tool_id") != tool_id:
            errors.append(f"{rel(tool_path)} tool_id does not match index entry {tool_id}")

    for path in tools_dir.glob("*.md"):
        fm = frontmatter(path)
        tool_id = fm.get("tool_id")
        if tool_id and tool_id not in indexed_ids:
            errors.append(f"{rel(path)} has tool_id {tool_id} but is not listed in stack/tools/index.yaml")


def check_protocol_index(errors: list[str]) -> None:
    tools_dir = ROOT / "stack" / "tools"
    index_path = tools_dir / "index.yaml"
    entries = parse_section_entries(index_path, "protocols", "protocol_id")
    tool_ids = {
        entry["tool_id"] for entry in parse_section_entries(index_path, "tools", "tool_id")
    }
    indexed_ids: set[str] = set()
    required = {"protocol_id", "title", "status", "tool", "primary_audience"}

    for entry in entries:
        protocol_id = entry["protocol_id"]
        indexed_ids.add(protocol_id)
        if "path" not in entry:
            errors.append(f"{rel(index_path)} protocol {protocol_id} missing path")
            continue
        protocol_path = tools_dir / entry["path"]
        if not protocol_path.exists():
            errors.append(
                f"{rel(index_path)} protocol {protocol_id} path missing: {entry['path']}"
            )
            continue
        fm = frontmatter(protocol_path)
        missing = sorted(required - set(fm))
        if missing:
            errors.append(
                f"{rel(protocol_path)} missing frontmatter fields: {', '.join(missing)}"
            )
        if fm.get("protocol_id") != protocol_id:
            errors.append(
                f"{rel(protocol_path)} protocol_id does not match index entry {protocol_id}"
            )
        tool_ref = fm.get("tool", "").replace("../", "").replace(".md", "")
        if tool_ref and tool_ref not in tool_ids:
            errors.append(f"{rel(protocol_path)} references unknown tool: {fm.get('tool')}")

    protocols_dir = tools_dir / "protocols"
    for path in protocols_dir.glob("*.md"):
        if path.name == "README.md":
            continue
        fm = frontmatter(path)
        protocol_id = fm.get("protocol_id")
        if protocol_id and protocol_id not in indexed_ids:
            errors.append(
                f"{rel(path)} has protocol_id {protocol_id} but is not listed in stack/tools/index.yaml"
            )


def extract_current_counts(corpora_path: Path) -> dict[str, int]:
    text = read(corpora_path)
    match = re.search(
        r"corpus_id:\s*philosophers-of-autonomy.*?current_counts:\s*"
        r"\n\s+thinkers:\s*(\d+)\s*"
        r"\n\s+concepts:\s*(\d+)\s*"
        r"\n\s+tensions:\s*(\d+)",
        text,
        re.S,
    )
    if not match:
        return {}
    return {
        "thinkers": int(match.group(1)),
        "concepts": int(match.group(2)),
        "tensions": int(match.group(3)),
    }


def count_files(directory: Path) -> int:
    return len([p for p in directory.glob("*.md") if p.name != "README.md"])


def check_corpus_counts(errors: list[str]) -> None:
    corpora_path = ROOT / "stack" / "indexes" / "corpora.yaml"
    expected = extract_current_counts(corpora_path)
    if not expected:
        errors.append(f"{rel(corpora_path)} missing philosophers current_counts block")
        return

    base = ROOT / "sources" / "philosophers" / "wiki"
    actual = {
        "thinkers": count_files(base / "thinkers"),
        "concepts": count_files(base / "concepts"),
        "tensions": count_files(base / "tensions"),
    }
    for key, value in expected.items():
        if actual[key] != value:
            errors.append(
                f"{rel(corpora_path)} {key} count is {value}, filesystem has {actual[key]}"
            )


def check_philosopher_index_paths(errors: list[str]) -> None:
    index_path = ROOT / "sources" / "philosophers" / "index.yaml"
    text = read(index_path)
    for match in re.finditer(r"^\s+(page|stack_reference):\s*(.+?)\s*$", text, re.M):
        target = match.group(2).strip()
        path = (index_path.parent / target).resolve()
        if not path.exists():
            errors.append(f"{rel(index_path)} missing {match.group(1)} target: {target}")
    for match in re.finditer(r"^\s+-\s+(raw/[^]\s]+\.md)\s*$", text, re.M):
        target = match.group(1).strip()
        path = (index_path.parent / target).resolve()
        if not path.exists():
            errors.append(f"{rel(index_path)} missing raw source target: {target}")


def main() -> int:
    errors: list[str] = []
    check_markdown_links(errors)
    check_tool_index(errors)
    check_protocol_index(errors)
    check_corpus_counts(errors)
    check_philosopher_index_paths(errors)

    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
