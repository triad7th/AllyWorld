---
name: create-pr
description: Push the current AllyWorld feature branch and open its pull request (Status In review). Run after locally reviewing /implement's work.
---

# Create PR

Publish the reviewed feature branch as a pull request tied to its issue.

## Constants

- Repo: `triad7th/AllyWorld` — Project: `18` (owner `triad7th`)
- Project ID: `PVT_kwHOALPoSc4BkDYs`
- Status field `PVTSSF_lAHOALPoSc4BkDYszhi1buM`: In review `df73e18b`
- Board item lookup: `gh project item-list 18 --owner triad7th --format json --limit 200`,
  match both `content.repository` to `triad7th/AllyWorld` and
  `content.number` to the issue number; paginate if needed.

## Steps

1. **Preflight.** Current branch must match `<type>/<N>-*` (extract `N`);
   worktree clean (uncommitted work → run `/commit` first or stop and ask).
   Confirm the verification gate from `/implement` is still valid; if
   commits were added since, re-run the focused tests for what changed.
2. **Push.** `git push -u origin <branch>`.
3. **Open the PR.** Write the exact Markdown body to a temporary file. Lead
   with the problem and resulting behavior, then the verification evidence.
   Include `Closes #N`. Add only an attribution/session footer configured for
   the current agent; do not fabricate a Claude session or URL.

   ```bash
   gh pr create -R triad7th/AllyWorld \
     --title "[#N] <issue title>" --body-file <pr-body.md>
   ```

4. **Board: In review.** Look up the item id, then `gh project item-edit`
   with option id `df73e18b`.
5. **Report** the PR URL. The user reviews the PR; review fixes are more
   `[#N]` commits on this branch pushed with `/commit-and-push` (the PR
   updates automatically). `/approve-pr <N>` finishes the ticket.
