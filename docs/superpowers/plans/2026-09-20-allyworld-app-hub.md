# AllyWorld App Hub Implementation Plan

> Execute in this session using the approved design and proportionate verification.

**Goal:** Create the central promotional, information, and support site for all ten AllyWorld apps.

**Architecture:** A static site generated from a Python app catalog with shared HTML templates, CSS, and native HTML disclosures. Generated HTML remains at the root for existing GitHub Pages hosting; a public-file-only dist copy supports Sites packaging.

**Tech stack:** Python standard library, HTML, CSS.

**Spec:** ../specs/2026-09-20-allyworld-app-hub-design.md

## Global constraints

- Preserve the existing public URLs and static hosting architecture.
- Use verified app assets and destinations.
- Distinguish App Store, web, demo, and development availability.
- Keep app-specific privacy claims grounded in source policies.
- No dependency installation or JavaScript required to read core content.

## Tasks

- [x] Gather the app catalog, store listings, icons, screenshots, and source policies; retain provenance in docs/app-content-sources.md.
- [x] Build the shared shell, theme, homepage, and a representative app page in scripts/build.py, site_content.py, and assets/site.css; open the meaningful local preview.
- [x] Generate all product/support/privacy pages, preserve legacy routes, and complete responsive navigation.
- [x] Add scripts/check_site.py to verify every generated route, local link, asset reference, unique title, app coverage, and legacy routes; build and run it.
- [ ] Document each app's App Store Connect URLs, save the validated source, and publish the private Sites preview.
