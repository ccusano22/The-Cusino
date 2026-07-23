#!/usr/bin/env python3
"""Run dependency-free preflight checks for the GitHub Pages source tree."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "_config.yml",
    "index.html",
    "catalog.md",
    "house-rules.md",
    "404.html",
    "assets/css/style.css",
    "assets/js/catalog.js",
    "_layouts/default.html",
    "_layouts/page.html",
    "_layouts/game.html",
    "_includes/game-card.html",
    ".github/workflows/pages.yml",
)
REQUIRED_GAME_KEYS = (
    "title",
    "slug",
    "order",
    "catalog_group",
    "category",
    "family",
    "players",
    "pot_format",
    "special_cards",
    "call_before_deal",
    "summary",
    "tip",
    "traits",
    "suit",
    "permalink",
)
REQUIRED_BODY_HEADINGS = (
    "## Deal and play",
    "## Winning condition",
    "## Variations",
    "## Source",
)


def parse_simple_front_matter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path.relative_to(ROOT)} has no YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path.relative_to(ROOT)} has unterminated YAML front matter")
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, object] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = ""
        elif value.startswith(('"', "[", "{")):
            data[key] = json.loads(value)
        elif value.isdigit():
            data[key] = int(value)
        else:
            data[key] = value
    return data, body


def read_categories() -> set[str]:
    path = ROOT / "_data/categories.yml"
    categories = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^- name:\s*(.+?)\s*$", line)
        if match:
            categories.add(match.group(1))
    return categories


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    categories = read_categories()
    game_files = sorted((ROOT / "_games").glob("*.md"))
    titles: set[str] = set()
    slugs: set[str] = set()
    orders: list[int] = []
    permalinks: set[str] = set()

    for path in game_files:
        try:
            data, body = parse_simple_front_matter(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(str(exc))
            continue

        missing = [key for key in REQUIRED_GAME_KEYS if key not in data]
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing keys: {', '.join(missing)}")
            continue

        title = str(data["title"])
        slug = str(data["slug"])
        permalink = str(data["permalink"])
        order = data["order"]
        category = str(data["category"])

        if path.stem != slug:
            errors.append(f"{path.relative_to(ROOT)} filename does not match slug {slug}")
        if permalink != f"/games/{slug}/":
            errors.append(f"{path.relative_to(ROOT)} has unexpected permalink {permalink}")
        if title in titles:
            errors.append(f"Duplicate title: {title}")
        if slug in slugs:
            errors.append(f"Duplicate slug: {slug}")
        if permalink in permalinks:
            errors.append(f"Duplicate permalink: {permalink}")
        if not isinstance(order, int):
            errors.append(f"{path.relative_to(ROOT)} order is not an integer")
        else:
            orders.append(order)
        if category not in categories:
            errors.append(f"{path.relative_to(ROOT)} uses unknown category {category}")
        for heading in REQUIRED_BODY_HEADINGS:
            if heading not in body:
                errors.append(f"{path.relative_to(ROOT)} missing body heading {heading}")

        titles.add(title)
        slugs.add(slug)
        permalinks.add(permalink)

    if orders and sorted(orders) != list(range(1, len(orders) + 1)):
        errors.append(f"Game order must be contiguous from 1 through {len(orders)}")

    catalog_text = (ROOT / "catalog.md").read_text(encoding="utf-8")
    main_match = re.search(r"^main_catalog_games:\s*([0-9]+)\s*$", catalog_text, re.MULTILINE)
    supplemental_match = re.search(r"^supplemental_calls:\s*([0-9]+)\s*$", catalog_text, re.MULTILINE)
    if main_match and supplemental_match:
        expected = int(main_match.group(1)) + int(supplemental_match.group(1))
        if len(game_files) != expected:
            errors.append(f"Expected {expected} game files from catalog counts, found {len(game_files)}")
    else:
        errors.append("catalog.md is missing game-count front matter")

    if errors:
        print("Site validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(game_files)} game pages, {len(categories)} categories, and all required site files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
