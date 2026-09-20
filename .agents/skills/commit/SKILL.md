---
name: commit
description: Group AllyWorld working-tree changes into logical commits with branch-aware message format ([#N] on a feature branch, conventional on main). Never pushes.
---

# Commit

Turn the current working tree into clean, logically grouped commits.

## Steps

1. **Inspect** (in parallel): `git diff --cached`, `git diff`, `git status`,
   `git log --oneline -5`. Note the current branch.
2. **If changes are already staged:** commit only what is staged (skip
   grouping).
3. **Otherwise group** changed files into 1–4 logical commits by concern —
   moderate splitting, not exhaustive:
   - Bug fixes separate from new features
   - Config/build changes separate from app logic
   - Tests separate from implementation (only if substantial)
   - Never stage `.env`, secrets, or large binaries; never `git add -A`
4. **Message format is branch-aware:**
   - On `codex/N-*`, `feat/N-*`, `fix/N-*`, or `chore/N-*`: `[#N] <imperative subject>`
     for feature work; `[#N] chore: <subject>` for support work (likewise
     `fix:`, `test:`, `docs:`). Subjects all lowercase except proper nouns
     (GitHub, PR, AllyWorld).
   - On `main` or any non-ticket branch: conventional format —
     `<type>(<scope>): <subject>` (`feat:`, `fix:`, `refactor:`, `chore:`,
     `test:`, `docs:`, `style:`).
   - Subject ≤ 72 chars; add 2–4 body bullets when the change is not
     self-evident. Include only commit trailers configured for the current
     agent/session; never invent attribution or a session URL.
5. **Commit each group sequentially.** Honor any configured pre-commit hooks; this repository currently has
   no lint-staged or Prettier hook configured. If a hook FAILS: fix the
   issue, re-stage, create a NEW commit — never `--amend`, never
   `--no-verify`.
6. **Report** each commit hash + subject. Do NOT push (that is
   `/commit-and-push`).
