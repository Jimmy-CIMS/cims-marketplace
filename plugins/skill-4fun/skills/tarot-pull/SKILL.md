---
name: tarot-pull
description: Draw and interpret a single tarot card with upright or reversed meaning, keywords, and a short reflection. Use when the user asks for a tarot pull, one-card reading, daily card, symbolic prompt, or reflective card interpretation.
---

# Tarot Pull

Use this skill for light symbolic tarot readings and creative reflection.

## Workflow

1. Randomly select one card from `references/major_arcana.md` unless the user names a card.
2. Randomly choose upright or reversed unless the user specifies.
3. Return card, orientation, keywords, and a short interpretation.
4. Frame readings as reflection, not fixed prediction.
5. For serious medical, legal, or financial questions, keep the reading reflective and suggest practical due diligence.

## Output shape

```text
Card: The Star, upright
Keywords: renewal, trust, quiet confidence
Reading: ...
```

