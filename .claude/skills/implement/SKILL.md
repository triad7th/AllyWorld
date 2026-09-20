---
name: implement
description: Implement a GitHub issue by number on a fresh feature branch with [#N] commits — the working step of the AllyWorld ticket flow. Usage - /implement ISSUE_NUMBER.
---

# Implement Issue

Take an issue from Ready to implemented-and-verified on a feature branch.
Ends at local review — never pushes; `/create-pr` is the next step.

## Constants

- Repo: `triad7th/AllyWorld` — Project: `18` (owner `triad7th`)
- Project ID: `PVT_kwHOALPoSc4BkDYs`
- Status field `PVTSSF_lAHOALPoSc4BkDYszhi1buM`: In progress `47fc9ee4`
- Board item lookup: `gh project item-list 18 --owner triad7th --format json --limit 200`,
  match both `content.repository` to `triad7th/AllyWorld` and
  `content.number` to the issue number; paginate if needed.

## Steps

1. **Preflight.** `git status` must be clean and on `main`; then
   `git pull origin main`. If dirty or mid-branch, STOP and report — never
   mix a ticket with unrelated work.
2. **Read the ticket.** `gh issue view <N> -R triad7th/AllyWorld`. If the
   body links spec/plan docs, read them — they are the requirements. Re-read
   applicable `AGENTS.md`/`CLAUDE.md` files if present, and inspect the
   current project tooling before choosing verification commands.
3. **Branch locally.** Use `git switch -c codex/<N>-<short-slug>` from fresh
   `main`. Follow a different branch name if the user explicitly requests it.
   Keep the branch local until `/create-pr`; its `Closes #N` links the ticket.
4. **Board: In progress + assignee.** Ensure the ticket is assigned
   (`gh issue edit <N> -R triad7th/AllyWorld --add-assignee triad7th`),
   look up the board item id, then:

   ```bash
   gh project item-edit --id <ITEM_ID> --project-id PVT_kwHOALPoSc4BkDYs \
     --field-id PVTSSF_lAHOALPoSc4BkDYszhi1buM --single-select-option-id 47fc9ee4
   ```

5. **Implement with TDD**, scaled to the ticket:
   - Small (XS/S): failing test → smallest change → focused tests, directly
     in this session.
   - Large (M+ with a linked plan): follow the plan task-by-task
     (superpowers:subagent-driven-development when the plan calls for it).
6. **Verify** the touched files using the repository's current tooling.
   AllyWorld currently serves static HTML at `/`, `/customer-support/`, and
   `/privacy-policy/`, with no package manifest, build, lint, or test scripts.
   For page changes, serve the repository on an agent-owned loopback port and
   check the affected routes, links, browser errors, and relevant desktop/mobile
   layouts. Use `pixel-verify` for drawn changes. For skills-only changes,
   validate frontmatter, referenced paths, copy parity, and whitespace.
   If tooling is added later, use its actual configured checks. Never claim
   an unavailable, failed, or incomplete check passed.
7. **Commit** as work naturally splits — multiple commits per ticket is
   normal. Message format:
   - Feature work: `[#N] <imperative subject>`
   - Support work: `[#N] chore: <subject>` (likewise `fix:`, `test:`,
     `docs:`)
   - Subjects all lowercase except proper nouns (GitHub, PR, AllyWorld)
   - Include only trailers configured for the current agent/session.
     Stage files explicitly — never `git add -A`, never
     `--no-verify`. If the pre-commit hook fails: fix, re-stage, NEW commit
     (never `--amend`).
8. **Stop for review.** Report what changed, the verification evidence, and
   the commit list. Do NOT push. The user reviews locally, requests fixes
   (more `[#N]` commits), then runs `/create-pr`.
