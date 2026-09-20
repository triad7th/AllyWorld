# AllyWorld

The app showcase, product information, support, and privacy hub for the AllyWorld family.

## Update and preview

Edit `site_content.py` for app information, `scripts/build.py` for shared page templates, and `assets/site.css` for design. App Store source metadata and asset provenance live in `docs/`.

```bash
python3 scripts/build.py
python3 scripts/check_site.py
python3 -m http.server 4873 --bind 127.0.0.1
```

Open `http://127.0.0.1:4873/`. No third-party dependencies are needed.

The build generates root-level HTML for GitHub Pages and copies only public HTML and assets to `dist/` for a Sites preview. Relative URLs work both at the domain root and under `/AllyWorld/`. Existing support and privacy routes remain available.

## App Store Connect

Use the app-specific links in [App Store Connect URLs](docs/app-store-connect-urls.md). The current public origin is `https://triad7th.github.io/AllyWorld/`. Preview URLs are not a replacement for public App Store support or privacy links.

Before publishing a content update, verify store destinations and make sure each privacy page reflects the version being distributed. New launch dates, features, data practices, and prices should not be inferred from development plans.
