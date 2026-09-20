---
name: lint-and-format
description: Use when asked to lint or format AllyWorld, applying its available tooling and reporting changes or remaining problems.
---

# Lint and Format

Lint first, then format, using the repository's actual configuration.
AllyWorld currently has static HTML and a shell script, with no package
manifest, lint scripts, formatter configuration, or pre-commit hooks.

## Steps

1. **Inspect** `git status --short`, the requested scope, and any current lint
   or formatter configuration. Preserve unrelated user edits.
2. **Lint** with configured tools when present. Run applicable targets
   sequentially; if one fails, do not assume later targets ran. Apply supported
   automatic fixes, then rerun lint to establish what remains.
3. **Format** after lint fixes. Use a configured formatter if one exists.
   Otherwise use an already available suitable formatter on the requested
   files, preserving the existing style. Do not install dependencies or add a
   build system just to satisfy this workflow. Report unavailable checks.
4. **Verify** formatter check mode when available and review the actual diff
   for unintended edits. For imported skills, compare the entire skill trees:

   ```bash
   diff -rq .claude/skills .agents/skills
   ```

   `.claude/skills` is canonical; refresh matching real copies in
   `.agents/skills` after editing. Check whitespace with `git diff --check`;
   inspect untracked files separately because Git does not include them.

5. **Report** what was checked, fixed, reformatted, skipped, and what remains
   with file/line locations. Do not commit; use `/commit` or `/commit-and-push`
   when requested.
