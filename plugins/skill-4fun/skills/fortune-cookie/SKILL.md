---
name: fortune-cookie
description: Generate short fortune-cookie messages, lucky sayings, tiny prophecies, gentle advice, or playful one-line omens. Use when the user asks for a fortune, lucky cookie, daily saying, tiny prophecy, or short whimsical guidance.
---

# Fortune Cookie

Create a concise fortune with a memorable turn of phrase.

## Workflow

1. Identify tone: classic, gentle, absurd, zen, workday, romantic, ominous, or custom.
2. Read `references/fortune_styles.md` when the user asks for a named tone or when variety is needed.
3. Write 1-3 fortunes unless the user asks for a specific count.
4. Keep each fortune under 25 words.
5. Avoid claiming certainty about real future events.

## Output shape

Use a simple list for multiple fortunes. For a single fortune, return just the fortune unless the user asks for explanation.

