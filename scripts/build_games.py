#!/usr/bin/env python3
"""Generate Jekyll collection pages from the templated master catalog."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "catalog.md"
OUTPUT_DIR = ROOT / "_games"
CATEGORY_BY_SLUG = {
    "3-5-7-guts": "Match-the-pot",
    "7-27": "Target & banking",
    "anaconda": "Pass & arrangement",
    "badugi": "Draw",
    "baseball": "Stud",
    "burn-the-biffel": "Community",
    "connect-four": "Draw",
    "crazy-pineapple": "Community",
    "criss-cross": "Community",
    "elevator": "Community",
    "follow-the-queen": "Stud",
    "guts": "Match-the-pot",
    "horse": "Mixed rotation",
    "in-between": "Target & banking",
    "iron-cross": "Community",
    "jacks-or-better": "Draw",
    "kings-and-little-ones": "Stud",
    "monterey": "Stud",
    "no-holds-barred": "Community",
    "omaha": "Community",
    "omaha-burn": "Community",
    "outhouse": "Progressive & elimination",
    "piranha": "Match-the-pot",
    "position-poker": "Stud",
    "pregnant-3s": "Draw",
    "razz": "Stud",
    "roll-your-own": "Stud",
    "russian-poker": "Pass & arrangement",
    "sevens-take-all": "Stud",
    "shifting-sands": "Stud",
    "stud": "Stud",
    "texas-holdem": "Community",
    "good-bad-ugly": "Stud",
    "three-legged-race": "Draw",
    "two-more-inches": "Match-the-pot",
    "five-card-draw": "Draw",
    "high-chicago": "Stud",
    "low-chicago": "Stud",
    "wild-widow": "Draw",
}

SUITS = ("spades", "hearts", "clubs", "diamonds")

GAME_HEADING_RE = re.compile(
    r'^<a id="(?P<slug>[^"]+)"></a>\n'
    r'^## (?:(?P<number>[0-9]+)\. )?(?P<title>.+)$',
    flags=re.MULTILINE,
)


def yaml_value(value: object) -> str:
    """Return JSON syntax, which is valid YAML and safely quoted."""
    return json.dumps(value, ensure_ascii=True)


def extract_one_line(section: str, label: str) -> str:
    pattern = re.compile(r"^\*\*" + re.escape(label) + r":\*\*\s*(.+)$", re.MULTILINE)
    match = pattern.search(section)
    if not match:
        raise ValueError(f"Missing field: {label}")
    return match.group(1).strip()


def extract_optional_one_line(section: str, label: str) -> str:
    pattern = re.compile(r"^\*\*" + re.escape(label) + r":\*\*\s*(.+)$", re.MULTILINE)
    match = pattern.search(section)
    return match.group(1).strip() if match else ""


def extract_block(section: str, start_pattern: str, end_pattern: str, label: str) -> str:
    pattern = re.compile(start_pattern + r"\s*(.*?)\s*" + end_pattern, re.DOTALL | re.MULTILINE)
    match = pattern.search(section)
    if not match:
        raise ValueError(f"Missing block: {label}")
    return match.group(1).strip()


def parse_index_summaries(text: str) -> dict[str, str]:
    summaries: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not (line.startswith("|") and line.endswith("|")):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        link_match = None
        for cell in cells:
            link_match = re.search(r"\[[^\]]+\]\(#([^)]+)\)", cell)
            if link_match:
                break
        if not link_match or not cells:
            continue
        summaries[link_match.group(1)] = cells[-1]
    return summaries


def infer_traits(*, family: str, pot_format: str, special_cards: str, variations: str) -> list[str]:
    combined = " ".join((family, pot_format, special_cards, variations)).lower()
    traits: list[str] = []

    def add(label: str) -> None:
        if label not in traits:
            traits.append(label)

    if "wild" in combined and not special_cards.lower().startswith("no wild"):
        add("Wild cards")
    if "split" in combined or "high-low" in combined:
        add("Split pot")
    if "match-the-pot" in combined or "match the pot" in combined or "drop-and-match" in combined:
        add("Match-the-pot")
    if "lowball" in combined or "low hand" in combined or "low half" in combined:
        add("Lowball")
    if "declare" in combined or "declaration" in combined:
        add("Declaration")
    if "pay card" in combined:
        add("Pay cards")
    if "kill" in combined:
        add("Kill cards")
    if "pass" in combined:
        add("Passing")
    if "draw" in family.lower():
        add("Draw")
    if "stud" in family.lower():
        add("Stud")
    if "community" in family.lower() or "hold'em" in family.lower() or "omaha" in family.lower():
        add("Community")

    return traits[:4]


def parse_games(text: str) -> list[dict[str, object]]:
    summaries = parse_index_summaries(text)
    main_count_match = re.search(r"^main_catalog_games:\s*([0-9]+)\s*$", text, re.MULTILINE)
    supplemental_count_match = re.search(r"^supplemental_calls:\s*([0-9]+)\s*$", text, re.MULTILINE)
    if not main_count_match or not supplemental_count_match:
        raise ValueError("Front matter must define main_catalog_games and supplemental_calls")
    main_count = int(main_count_match.group(1))
    supplemental_count = int(supplemental_count_match.group(1))
    expected_game_count = main_count + supplemental_count

    house_rules_position = text.find("# House-rule checklist")
    if house_rules_position < 0:
        raise ValueError("Could not find the House-rule checklist boundary")
    supplemental_position = text.find("# Supplemental dealer calls")
    if supplemental_position < 0:
        raise ValueError("Could not find the Supplemental dealer calls boundary")

    all_matches = list(GAME_HEADING_RE.finditer(text))
    game_matches = [
        match
        for match in all_matches
        if match.group("number") is not None
        or (supplemental_position < match.start() < house_rules_position
            and match.group("title").strip() != "Supplemental quick index")
    ]

    if len(game_matches) != expected_game_count:
        raise ValueError(
            f"Expected {expected_game_count} game sections from front matter, found {len(game_matches)}. "
            "Check the catalog counts, headings, and anchor structure."
        )

    games: list[dict[str, object]] = []
    supplemental_order = main_count

    for index, match in enumerate(game_matches):
        slug = match.group("slug").strip()
        title = match.group("title").strip()
        number = match.group("number")
        if number is not None:
            order = int(number)
            catalog_group = "Main catalog"
        else:
            supplemental_order += 1
            order = supplemental_order
            catalog_group = "Supplemental call"

        next_start = game_matches[index + 1].start() if index + 1 < len(game_matches) else house_rules_position
        section = text[match.end():next_start]

        try:
            family = extract_one_line(section, "Family")
            players = extract_one_line(section, "Players")
            pot_format = extract_one_line(section, "Pot format")
            special_cards = extract_one_line(section, "Wild / kill / pay cards")
            call_before_deal = extract_one_line(section, "Call before the deal")
            deal_and_play = extract_block(
                section,
                r"^### Deal and play\s*$",
                r"^\*\*Winning condition:\*\*",
                "Deal and play",
            )
            winning_condition = extract_one_line(section, "Winning condition")
            variations = extract_block(
                section,
                r"^\*\*Variations:\*\*\s*$",
                r"^> \*\*Game tip:\*\*",
                "Variations",
            )
            tip_match = re.search(r"^> \*\*Game tip:\*\*\s*(.+)$", section, re.MULTILINE)
            if not tip_match:
                raise ValueError("Missing field: Game tip")
            tip = tip_match.group(1).strip()
            source = extract_one_line(section, "Source")
            editorial_note = extract_optional_one_line(section, "Editorial note")
        except ValueError as exc:
            raise ValueError(f"{title}: {exc}") from exc

        category = CATEGORY_BY_SLUG.get(slug)
        if not category:
            raise ValueError(f"No browsing category configured for {title} ({slug})")

        summary = summaries.get(slug, special_cards)
        traits = infer_traits(
            family=family,
            pot_format=pot_format,
            special_cards=special_cards,
            variations=variations,
        )

        games.append(
            {
                "slug": slug,
                "title": title,
                "order": order,
                "catalog_group": catalog_group,
                "category": category,
                "family": family,
                "players": players,
                "pot_format": pot_format,
                "special_cards": special_cards,
                "call_before_deal": call_before_deal,
                "deal_and_play": deal_and_play,
                "winning_condition": winning_condition,
                "variations": variations,
                "tip": tip,
                "source": source,
                "editorial_note": editorial_note,
                "summary": summary,
                "traits": traits,
                "suit": SUITS[(order - 1) % len(SUITS)],
            }
        )

    orders = [int(game["order"]) for game in games]
    if orders != list(range(1, expected_game_count + 1)):
        raise ValueError(f"Game order is not contiguous: {orders}")

    return games


def render_game(game: dict[str, object]) -> str:
    front_matter = [
        "---",
        "layout: game",
        f"title: {yaml_value(game['title'])}",
        f"slug: {yaml_value(game['slug'])}",
        f"order: {game['order']}",
        f"catalog_group: {yaml_value(game['catalog_group'])}",
        f"category: {yaml_value(game['category'])}",
        f"family: {yaml_value(game['family'])}",
        f"players: {yaml_value(game['players'])}",
        f"pot_format: {yaml_value(game['pot_format'])}",
        f"special_cards: {yaml_value(game['special_cards'])}",
        f"call_before_deal: {yaml_value(game['call_before_deal'])}",
        f"summary: {yaml_value(game['summary'])}",
        f"tip: {yaml_value(game['tip'])}",
        f"traits: {yaml_value(game['traits'])}",
        f"suit: {yaml_value(game['suit'])}",
        f"permalink: {yaml_value('/games/' + str(game['slug']) + '/')}",
        "generated_from: catalog.md",
        "---",
        "",
    ]

    body = [
        "## Deal and play",
        "",
        str(game["deal_and_play"]).strip(),
        "",
        "## Winning condition",
        "",
        str(game["winning_condition"]).strip(),
        "",
        "## Variations",
        "",
        str(game["variations"]).strip(),
        "",
        "## Source",
        "",
        str(game["source"]).strip(),
        "",
    ]

    editorial_note = str(game["editorial_note"]).strip()
    if editorial_note:
        body.extend([f"> **Editorial note:** {editorial_note}", ""])

    return "\n".join(front_matter + body).rstrip() + "\n"


def generate(*, check_only: bool) -> int:
    text = SOURCE.read_text(encoding="utf-8")
    games = parse_games(text)
    rendered = {str(game["slug"]): render_game(game) for game in games}

    if check_only:
        mismatches: list[str] = []
        for slug, expected in rendered.items():
            path = OUTPUT_DIR / f"{slug}.md"
            if not path.exists():
                mismatches.append(f"missing: {path.relative_to(ROOT)}")
            elif path.read_text(encoding="utf-8") != expected:
                mismatches.append(f"out of date: {path.relative_to(ROOT)}")
        existing = {path.stem for path in OUTPUT_DIR.glob("*.md")}
        for stale in sorted(existing - set(rendered)):
            mismatches.append(f"stale: {(OUTPUT_DIR / (stale + '.md')).relative_to(ROOT)}")
        if mismatches:
            print("Generated game pages are not synchronized:", file=sys.stderr)
            for mismatch in mismatches:
                print(f"- {mismatch}", file=sys.stderr)
            return 1
        print(f"Validated {len(games)} synchronized game pages.")
        return 0

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    for slug, content in rendered.items():
        (OUTPUT_DIR / f"{slug}.md").write_text(content, encoding="utf-8")

    print(f"Generated {len(games)} game pages in {OUTPUT_DIR.relative_to(ROOT)}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate that committed game pages match catalog.md without rewriting them.",
    )
    args = parser.parse_args()
    try:
        return generate(check_only=args.check)
    except (OSError, ValueError) as exc:
        print(f"Catalog build failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
