---
name: spell-generator
description: Generate fantasy, sci-fi, or absurd spells with a name, effect, cost, casting gesture, limitation, and optional mishap. Use when the user asks for a spell, magical effect, incantation, ritual, artifact power, or game ability idea.
---

# Spell Generator

Generate a spell that feels playable and has a tradeoff.

## Workflow

1. Match the requested genre and power level.
2. Use `references/spell_tables.md` for components and limitations.
3. Include a cost or constraint so the spell is not unlimited.
4. Avoid real-world harmful instructions.
5. If the user names a game system, keep mechanics light unless they request stat blocks.

## Output shape

```text
Spell:
School:
Effect:
Cost:
Gesture:
Limit:
Mishap:
```

