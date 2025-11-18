"""Utility to view repository entries grouped by prefix and suffix.

The tool scans the directory tree and groups files and folders by their
leading and trailing alphabetic segments, ignoring file extensions.
"""
from __future__ import annotations

import argparse
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Sequence


def strip_all_suffixes(name: str) -> str:
    base = name
    while True:
        stem, ext = os.path.splitext(base)
        if not ext:
            return base
        base = stem


def leading_alpha_segment(text: str) -> str:
    match = re.match(r"[A-Za-z]+", text)
    return match.group(0) if match else ""


def trailing_alpha_segment(text: str) -> str:
    match = re.search(r"[A-Za-z]+$", text)
    return match.group(0) if match else ""


def iter_entries(root: Path, include_hidden: bool) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not include_hidden and any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        yield path


def normalize_group_value(value: str, fallback: str) -> str:
    return value if value else fallback


def group_entries(paths: Sequence[Path], fallback: str) -> dict[str, List[Path]]:
    groups: dict[str, List[Path]] = defaultdict(list)
    for path in paths:
        base_name = strip_all_suffixes(path.name)
        prefix = normalize_group_value(leading_alpha_segment(base_name), fallback)
        suffix = normalize_group_value(trailing_alpha_segment(base_name), fallback)
        groups[prefix].append(path)
        groups[suffix].append(path)
    return groups


def display_groups(title: str, groups: dict[str, List[Path]], root: Path) -> None:
    print(title)
    for group_name in sorted(groups):
        entries = sorted(groups[group_name], key=lambda p: p.relative_to(root).as_posix())
        print(f"- {group_name} ({len(entries)} entries)")
        for entry in entries:
            print(f"  • {entry.relative_to(root)}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        type=Path,
        help="directory to scan (defaults to current working directory)",
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="include hidden files and directories",
    )
    parser.add_argument(
        "--fallback-label",
        default="<none>",
        help="label to use when no alphabetic prefix or suffix is found",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    entries = list(iter_entries(root, include_hidden=args.include_hidden))
    prefix_groups: dict[str, List[Path]] = defaultdict(list)
    suffix_groups: dict[str, List[Path]] = defaultdict(list)

    for path in entries:
        base_name = strip_all_suffixes(path.name)
        prefix = normalize_group_value(leading_alpha_segment(base_name), args.fallback_label)
        suffix = normalize_group_value(trailing_alpha_segment(base_name), args.fallback_label)
        prefix_groups[prefix].append(path)
        suffix_groups[suffix].append(path)

    print(f"Scanning directory: {root}")
    print(f"Include hidden: {'yes' if args.include_hidden else 'no'}")
    print()

    display_groups("Entries grouped by prefix (ignoring file type)", prefix_groups, root)
    display_groups("Entries grouped by suffix (ignoring file type)", suffix_groups, root)


if __name__ == "__main__":
    main()
