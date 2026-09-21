# AllyWorld social preview

The homepage title is **AllyWorld | Apps for everyday, music and play**. Other pages retain their own app, support, or privacy title. All pages provide their description, the shared brand image, and its actual dimensions in static Open Graph and X metadata.

The primary sharing origin is `https://allyworld.netlify.app/`, configured in `site_content.py`. GitHub Pages remains available; its share metadata points to the same Netlify canonical page and public image.

## Publish and verify

```bash
python3 scripts/build.py
python3 scripts/check_site.py
npx --yes netlify-cli deploy --site allyworld --dir dist --no-build --prod
```

The Netlify project uses manual deployments. Source changes also need to be pushed to `main` for the existing GitHub Pages deployment.

Facebook and X may retain an earlier preview. For Facebook, enter the page URL in the [Sharing Debugger](https://developers.facebook.com/tools/debug/) and request a fresh scrape. Existing posts may retain their original card. This update does not edit or create social posts.

## Image provenance

- Asset: `assets/social/allyworld-share-v1.png`
- Dimensions: 1734 × 907 pixels
- Generated with the built-in imagegen tool for this project. Illustrations are abstract brand artwork, not app screenshots.
- Use a new versioned filename when replacing the artwork so image caches can distinguish the revision.

Final generation prompt:

```text
Use case: ads-marketing
Asset type: Landscape social-sharing preview card for AllyWorld, a polished independent app studio homepage. Aim for a 1200x630 canvas, roughly 1.91:1 landscape.
Scene/backdrop: Clean white to very light cool gray background with generous negative space.
Primary request: A refined branded card with crisp editorial typography on the left and a tasteful compact arrangement of abstract app-inspired illustrations on the right.
Composition: Keep all important content comfortably inside a generous 8% safe margin. On the left, show a small dark rounded-square brand mark containing a white lowercase "a." beside the large brand name "AllyWorld". Below that place the larger headline over two or three balanced lines, followed by the supporting line. On the right, arrange a stylized clock, a short piano keyboard, a metronome, and a game controller with subtle dimensionality and soft grounded shadows. These are abstract illustrations, not screenshots or app cards. Let the typography dominate; the illustrations should feel calm, simple, and carefully spaced.
Color palette: dark ink #161b25, vivid blue #315bea, white and light cool gray. Use blue as a confident accent on parts of the illustrations.
Text (verbatim, and no other text): "a." in the small brand mark; "AllyWorld"; "Make time for what you love."; "Everyday tools. Music. Games."
Typography: Clean contemporary sans serif. Strong dark headline, excellent small-thumbnail legibility, intentional line breaks, accurate spelling.
Mood: Elegant, spacious, friendly, premium craft. Sharp geometric forms with subtle dimensionality.
Constraints: No emojis, no em dashes, no watermarks, no invented app badges, no store badges, no extra captions or lettering. Avoid busy collage, heavy gradients, visual clutter, fake screenshots, and crowded edges. Render one finished image.
```

Metadata references: [Open Graph protocol](https://ogp.me/), [Meta sharing documentation](https://developers.facebook.com/docs/sharing/webmasters/).
