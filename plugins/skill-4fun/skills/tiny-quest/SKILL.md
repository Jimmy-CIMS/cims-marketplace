---
name: tiny-quest
description: Generate a small real-world quest that can be completed in about 5 to 15 minutes. Use when the user wants a tiny task, playful productivity prompt, quick reset, micro-adventure, or daily mini quest.
---

# Tiny Quest

Give the user one compact, doable quest.

## Workflow

1. Choose a quest category from `references/quest_tables.md`.
2. Keep the task concrete and completable in 5-15 minutes.
3. Include a clear success condition.
4. Optionally add a reward line if the user wants game flavor.
5. Avoid tasks that require spending money, unsafe travel, or sensitive personal disclosure unless requested.

## Output shape

```text
Quest: ...
Success: ...
Reward: ...
```

