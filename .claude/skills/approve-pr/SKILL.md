---
name: approve-pr
description: Merge an approved AllyWorld pull request - rebase-merge into main, delete the branch, close out the board (Status Done). Usage - /approve-pr PR_NUMBER | /approve-pr issue ISSUE_NUMBER | /approve-pr (resolve from context).
---

# Approve PR

The user has reviewed the PR and this command is their approval: merge it,
clean up, and close the ticket.

## Constants

- Repo: `triad7th/AllyWorld` — Project: `18` (owner `triad7th`)
- Project ID: `PVT_kwHOALPoSc4BkDYs`
- Status field `PVTSSF_lAHOALPoSc4BkDYszhi1buM`: Done `98236657`
- Board item lookup: `gh project item-list 18 --owner triad7th --format json --limit 200`,
  match both `content.repository` to `triad7th/AllyWorld` and
  `content.number` to the issue number; paginate if needed.

## Steps

1. **Resolve the PR from the argument.** (Issues and PRs share GitHub's
   number sequence, so the two numbers usually differ.)
   - `/approve-pr <N>` — `N` is the PR NUMBER (the default). `gh pr view <N>`
     must be an OPEN PR; derive the issue number `M` from its head branch
     `<type>/<M>-*`.
   - `/approve-pr issue <N>` (or `issue #N`) — `N` is the ISSUE number. Find
     the open PR whose head branch matches `<type>/<N>-*`.
   - `/approve-pr` (no argument) — resolve from context: if the current
     branch is a ticket branch with an open PR, use it; else if exactly ONE
     open PR exists, use it.
   - **Ambiguity → ask, never guess.** If a bare number is not an open PR
     but does match a ticket branch (or vice versa), if no-arg resolution
     finds zero or multiple candidates, or if the head branch yields no
     issue number — ask the user a follow-up question naming the candidates
     (PR number, branch, title) and wait.
     Always state which PR and which issue you resolved before merging.
2. **Skill-drift guard.** For every skill present in both trees, the copies
   must be identical:

   ```bash
   diff -rq .claude/skills .agents/skills
   ```

   `.claude/skills` is canonical; `.agents/skills` contains real,
   byte-identical copies. Resolve drift within the authorized changes before
   merging; preserve unrelated edits and report any remaining mismatch.

3. **Mergeability.** `gh pr view <PR#> --json mergeable,mergeStateStatus`.
   Resolve conflicts within the approved scope, re-run relevant verification,
   and update only the feature branch. A rewritten feature branch uses
   `git push --force-with-lease`; never force-push `main`. Ask only when a
   conflict requires a product decision that the existing request cannot resolve.
4. **Merge (rebase & merge) + cleanup.** Preserve unrelated working-tree
   changes. Run each command separately and inspect its result before continuing;
   if another worktree owns `main`, update it there without disrupting its work.
   Record the previous main tip before merging for the final report.

   ```bash
   gh pr merge <PR#> -R triad7th/AllyWorld --rebase --delete-branch
   git switch main
   git pull --ff-only origin main
   git branch -d <branch>   # only if gh did not already remove it
   ```

   `Closes #N` in the PR body closes the issue on merge.

5. **Board: Done.** Look up the item id, then `gh project item-edit` with
   option id `98236657`. (GitHub's built-in workflow may have done this on
   close — setting it again is harmless.)
6. **Report** the merged commit range on `main` (`git log --oneline` since
   the previous main tip) and confirm issue closed + branch deleted.
