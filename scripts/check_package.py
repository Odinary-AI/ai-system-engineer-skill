#!/usr/bin/env python3
"""Validate the exact ASE v4.2.1 source package and its self-containment."""

from __future__ import annotations

import re
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
EXPECTED_FILES = {
    "SKILL.md",
    "references/ai-coding-delivery.md",
    "references/codebase-architecture-scan.md",
    "references/guided.md",
    "scripts/check_package.py",
}
CACHE_NAMES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
FORBIDDEN = [
    ".." + "/docs/",
    ".." + "/tests/",
    ".." + "/archives/",
    "/Users" + "/",
    "/home" + "/",
    ".codex" + "/skills/",
]
BACKTICK_FILE = re.compile(r"`([^`\n]+\.(?:md|py))`")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)")
FILE_TOKEN = re.compile(
    r"(?<![\w./-])"
    r"((?:/|\.\.?/)?(?:[A-Za-z0-9_.-]+/)*"
    r"[A-Za-z0-9_.-]+\.(?:md|py)(?:#[A-Za-z0-9_-]+)?)"
)
URI_TOKEN = re.compile(
    r"(?<![\w.+-])([A-Za-z][A-Za-z0-9+.-]*" + r":(?!\*\*)[^\s<>()`]+)"
)


def package_entries() -> set[str]:
    return {
        path.relative_to(SKILL_DIR).as_posix()
        for path in SKILL_DIR.rglob("*")
        if path.is_file() or path.is_symlink()
    }


def frontmatter_values(text: str) -> tuple[list[str], dict[str, str]]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return [], {}
    entries: list[tuple[str, str]] = []
    for line in match.group(1).splitlines():
        entry = re.fullmatch(r"([A-Za-z0-9_-]+): (.*)", line)
        if not entry:
            return [], {}
        entries.append((entry.group(1), entry.group(2)))
    return [key for key, _ in entries], dict(entries)


def valid_plain_scalar(value: str) -> bool:
    if not value or value != value.strip():
        return False
    if value[0] in "!&*{}[],#|>@`\"'%":
        return False
    if value.startswith(("- ", "? ", ": ")):
        return False
    return re.search(r":(?:[ \t]|$)", value) is None and " #" not in value


def file_dependencies(text: str) -> set[str]:
    dependencies = {match.group(1) for match in BACKTICK_FILE.finditer(text)}
    dependencies.update(match.group(1) for match in MARKDOWN_LINK.finditer(text))
    dependencies.update(match.group(1) for match in FILE_TOKEN.finditer(text))
    dependencies.update(match.group(1) for match in URI_TOKEN.finditer(text))
    return {
        token[1:-1] if token.startswith("<") and token.endswith(">") else token
        for token in dependencies
    }


def external_reference(token: str) -> bool:
    target = token.split("#", 1)[0].split("?", 1)[0]
    return (
        target.startswith(("/", "../"))
        or "/../" in target
        or "\\" in target
        or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) is not None
    )


def internal_matches(token: str) -> list[str]:
    target = token.split("#", 1)[0].split("?", 1)[0]
    while target.startswith("./"):
        target = target[2:]
    if not target:
        return []
    return [
        candidate
        for candidate in EXPECTED_FILES
        if candidate == target or Path(candidate).name == target
    ]


def main() -> int:
    findings: list[str] = []
    actual = package_entries()

    for rel in sorted(actual - EXPECTED_FILES):
        findings.append(f"{rel}: unexpected package file")
    for rel in sorted(EXPECTED_FILES - actual):
        findings.append(f"{rel}: missing package file")

    for path in SKILL_DIR.rglob("*"):
        rel = path.relative_to(SKILL_DIR)
        if path.is_symlink():
            findings.append(f"{rel}: symlink is not allowed")
        if any(part in CACHE_NAMES for part in rel.parts):
            findings.append(f"{rel}: cache artifact is not allowed")

    texts: dict[str, str] = {}
    for rel in sorted(EXPECTED_FILES & actual):
        path = SKILL_DIR / rel
        if path.is_symlink() or not path.is_file():
            continue
        try:
            texts[rel] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"{rel}: package file is not valid UTF-8")

    for rel, text in texts.items():
        for token in FORBIDDEN:
            if token in text:
                findings.append(f"{rel}: forbidden external reference {token!r}")
        for token in sorted(file_dependencies(text)):
            if token.startswith("#"):
                continue
            if external_reference(token):
                findings.append(f"{rel}: forbidden external reference {token!r}")
                continue
            matches = internal_matches(token)
            if not matches:
                findings.append(f"{rel}: dangling internal reference `{token}`")
            elif len(matches) > 1:
                findings.append(f"{rel}: ambiguous internal reference `{token}`")

    skill_text = texts.get("SKILL.md", "")
    fields, values = frontmatter_values(skill_text)
    if len(fields) != 2 or set(fields) != {"name", "description"}:
        findings.append("SKILL.md: frontmatter fields must be name and description")
    if values.get("name") != "ai-system-engineer":
        findings.append("SKILL.md: name must be ai-system-engineer")
    if not valid_plain_scalar(values.get("description", "")):
        findings.append("SKILL.md: description must be a valid plain scalar")
    if "Version 4.2.1." not in skill_text:
        findings.append("SKILL.md: version must be 4.2.1")

    if findings:
        print(f"FAIL: {len(findings)} finding(s)")
        for finding in findings:
            print(f"  - {finding}")
        return 1

    print("PASS: package structure and self-containment checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
