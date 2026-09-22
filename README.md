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

## Social link previews

The primary sharing address is [allyworld.netlify.app](https://allyworld.netlify.app/). Every page includes its own title and description, an absolute canonical URL, and Open Graph and X large-image card metadata. The shared AllyWorld artwork is `assets/social/allyworld-share-v1.png`. The build reads the image dimensions directly, and the site checker verifies the metadata and packaged image.

See [social preview details](docs/social-preview.md) for the image source, regeneration brief, deployment command, and refreshing cached previews.

## Website analytics

Every page uses Umami Cloud with the existing shared [AllyWorld Apps property](https://cloud.umami.is/analytics/us/websites/09974c1b-f7d4-43a1-9404-d50a40210e16). Filter by **Host** in Umami to separate `allyworld.netlify.app` from the other Ally apps. The GitHub Pages mirror is recorded under `triad7th.github.io`, with page paths starting with `/AllyWorld/`.

The public website ID and allowed production hostnames are configured in `site_content.py`. The deferred tracker is included by the shared page template. Its `data-domains` allowlist excludes localhost, Netlify deploy previews, and the private Sites preview. The site checker verifies the tracker on all 35 generated pages. Website privacy notices disclose the analytics data collected; Umami’s tracker does not use cookies.

Build and check before publishing, then deploy the public-only directory to the linked Netlify project:

```bash
npx --yes netlify-cli deploy --dir dist --no-build --prod
```

After deployment, visit the public site and check **Realtime** in Umami for the corresponding host and page. Ad blockers or a local Umami opt-out can prevent a test visit from being recorded. See the official [tracker configuration](https://docs.umami.is/docs/tracker-configuration) and [data practices](https://docs.umami.is/docs/faq).
