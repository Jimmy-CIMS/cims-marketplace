---
name: dice-roller
description: Roll tabletop dice and resolve dice notation such as d6, 2d20+3, advantage, disadvantage, exploding dice, and keep highest or lowest results. Use when the user asks to roll dice, simulate a tabletop check, choose by dice, or resolve RPG-style random outcomes.
---

# Dice Roller

Use this skill when the user wants dice rolled or a dice expression resolved.

## Workflow

1. Parse the requested dice notation and modifiers.
2. Use `scripts/roll_dice.py` for deterministic parsing and actual random rolls when possible.
3. Return the final total first, then show the roll breakdown.
4. If the request includes stakes, briefly interpret the outcome only within the user's stated rules.

## Supported notation

- `d6`, `2d20+3`, `4d6-1`
- `advantage` or `adv`: roll `2d20`, keep highest
- `disadvantage` or `dis`: roll `2d20`, keep lowest
- `khN`: keep highest N, for example `4d6kh3`
- `klN`: keep lowest N, for example `4d6kl2`
- `!`: exploding dice, for example `3d6!`

## Running the script

```bash
python3 scripts/roll_dice.py "2d20kh1+3"
python3 scripts/roll_dice.py "4d6kh3"
python3 scripts/roll_dice.py "3d6!"
```

If a user gives an ambiguous request, choose the common tabletop interpretation and state it briefly.

