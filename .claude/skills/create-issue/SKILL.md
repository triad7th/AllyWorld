---
name: create-issue
description: Create a GitHub issue for a new AllyWorld feature, fix, or chore and add it to the Kanban board (Status Ready). Run at the end of a brainstorm, or directly for ad-hoc bugs and tasks.
---

# Create Issue

Create the GitHub issue that becomes the unit of work for the ticket flow
(`/implement` → `/create-pr` → `/approve-pr`).

## Constants

- Repo: `triad7th/AllyWorld` — Project: `18` (owner `triad7th`)
- Project ID: `PVT_kwHOALPoSc4BkDYs`
- Status field `PVTSSF_lAHOALPoSc4BkDYszhi1buM`: Backlog `f75ad846`, Ready
  `61e4505c`, In progress `47fc9ee4`, In review `df73e18b`, Done `98236657`
- Priority field `PVTSSF_lAHOALPoSc4BkDYszhi1b2Y`: P0 `79628723`, P1
  `0a877460`, P2 `da944a9c`
- Size field `PVTSSF_lAHOALPoSc4BkDYszhi1b2c`: XS `6c6483d2`, S `f784b110`,
  M `7515a9f1`, L `817d0097`, XL `db339eb2`

If an `item-edit` call fails, the IDs may have changed — re-derive them with
`gh project field-list 18 --owner triad7th --format json` and continue.

## Steps

1. **Compose the issue.** Title: short, imperative. Body scales with size:
   - Small feature/fix: the body IS the spec — a Goal line plus concrete
     acceptance criteria (checkboxes).
   - Large feature: link the approved design/plan docs in
     `docs/superpowers/specs/` and `docs/superpowers/plans/`; the body holds
     the one-paragraph summary and the doc links.
2. **Prepare the final issue** (title + body + label + proposed Priority/Size).
   If the user has already asked to create it, proceed under that authorization.
   Otherwise present the complete draft for approval before publishing.
   Use an existing label such as `enhancement`, `bug`, or `documentation`.
3. **Create and board it:**

   ```bash
   gh issue create -R triad7th/AllyWorld --title "<title>" --label "<label>" --assignee triad7th --body-file <issue-body.md>
   gh project item-add 18 --owner triad7th --url <issue-url> --format json   # note the item id
   gh project item-edit --id <ITEM_ID> --project-id PVT_kwHOALPoSc4BkDYs \
     --field-id PVTSSF_lAHOALPoSc4BkDYszhi1buM --single-select-option-id 61e4505c   # Status: Ready
   ```

   Set Priority and Size the same way with their field/option IDs.

4. **Report** the issue number and URL. The number is the handle for
   `/implement <N>` and every `[#N]` commit after it.

## Attaching images

AllyWorld is public, but screenshots should normally use GitHub attachments
rather than adding issue-only binaries to the repository. If screenshots are
requested, use the available browser's supported attachment flow, preserve
existing body text, and pass the updated body with `gh issue edit --body-file`.
Tell the user before a clipboard-based upload overwrites their clipboard.
Do not post a separate comment just to obtain an attachment URL.
