#!/usr/bin/env python3
"""Roll common tabletop dice expressions."""

from __future__ import annotations

import argparse
import json
import random
import re
from dataclasses import dataclass


PATTERN = re.compile(
    r"^\s*(?P<count>\d*)d(?P<sides>\d+)(?P<explode>!)?(?:(?P<keep>k[hl])(?P<keep_n>\d+))?(?P<mod>[+-]\d+)?\s*$",
    re.IGNORECASE,
)


@dataclass
class RollResult:
    expression: str
    rolls: list[int]
    kept: list[int]
    modifier: int
    total: int
    note: str


def roll_expression(expression: str) -> RollResult:
    expr = expression.strip().lower()
    if expr in {"adv", "advantage"}:
        expr = "2d20kh1"
    if expr in {"dis", "disadvantage"}:
        expr = "2d20kl1"

    match = PATTERN.match(expr)
    if not match:
        raise ValueError(f"Unsupported dice expression: {expression}")

    count = int(match.group("count") or "1")
    sides = int(match.group("sides"))
    if count <= 0 or sides <= 0:
        raise ValueError("Dice count and sides must be positive.")
    if count > 100:
        raise ValueError("Refusing to roll more than 100 dice at once.")

    explode = bool(match.group("explode"))
    keep_mode = match.group("keep")
    keep_n = int(match.group("keep_n") or count)
    modifier = int(match.group("mod") or "0")

    rolls: list[int] = []
    for _ in range(count):
        value = random.randint(1, sides)
        rolls.append(value)
        while explode and value == sides:
            value = random.randint(1, sides)
            rolls.append(value)

    kept = list(rolls)
    note = "kept all dice"
    if keep_mode:
        if keep_n <= 0:
            raise ValueError("Keep count must be positive.")
        sorted_rolls = sorted(rolls, reverse=(keep_mode == "kh"))
        kept = sorted_rolls[:keep_n]
        note = f"kept {'highest' if keep_mode == 'kh' else 'lowest'} {keep_n}"

    total = sum(kept) + modifier
    return RollResult(expression=expression, rolls=rolls, kept=kept, modifier=modifier, total=total, note=note)


def main() -> None:
    parser = argparse.ArgumentParser(description="Roll tabletop dice expressions.")
    parser.add_argument("expression", help="Dice expression, for example 2d20+3, 4d6kh3, or 3d6!")
    args = parser.parse_args()
    result = roll_expression(args.expression)
    print(json.dumps(result.__dict__, indent=2))


if __name__ == "__main__":
    main()

