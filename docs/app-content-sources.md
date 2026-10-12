# Content and asset sources

Verified September 20, 2026.

- Six released iOS apps: Apple Lookup API records in `app-store-sources.json`, containing App Store URLs and the original screenshot URLs. Downloaded screenshots use the same Apple image source at a larger requested size. No screenshots were generated or retouched. App icons and screenshot files are under `assets/apps/`. Store copy is reference material; page text is edited for the hub.
- AllyScore/AllyScores: sibling AllyScore repository README and AGENTS product descriptions; app-shell Google Drive configuration and token service, persistence implementation, and reader/editor public icons. Both are labeled in development. Screenshots were recaptured October 11, 2026 from the live editor and reader (Modern Studio) in headless Chrome. They show a public-domain melody, *Ode to Joy* by Ludwig van Beethoven, entered in browser storage. The reader capture renders that exported file through the public share route (`/s/:fileId`), answering the Drive download locally. The public library was not used because its books carry a real church's branding. Icons are the shared Modern Studio mark from the apps' `public/icon-512.png`.
- AllyStation: sibling repository AGENTS and game README. App icon from `game/icon.png`. Active development, no public download linked.
- AlexFighters: sibling repository README, `framework/core/save_manager.gd`, and `game/assets/icon/app_icon_1024.png`. The public web demo is linked; the full game is labeled in development.
- AllyFast editions: existing AllyWorld privacy/support pages and sibling allyfast repository CLAUDE, app-group persistence, plans, and view code. Lite copy avoids claiming parity with the paid edition.
- AllyMetronome editions: sibling README, edition controls, and existing AllyWorld Lite support/privacy pages.
- AllyClock privacy: existing sibling `apps/web/public/privacy.html`.
- AllyPiano privacy: existing sibling `apps/web/src/app/pages/privacy.component.ts`.
- Support contact: existing AllyWorld support and privacy pages.

Website analytics updated September 21, 2026: the promotional website uses Umami Cloud with the shared AllyWorld Apps property, matching the tracker in the sibling AllyClock, AllyPiano, and AllyScore web entry points. Tracking is limited to `allyworld.netlify.app` and the public `triad7th.github.io` mirror. The website privacy disclosure reflects the [data listed in Umami’s FAQ](https://docs.umami.is/docs/faq), including page views, referring URLs, browser/device information, and approximate location. Umami’s tracker does not use cookies; the website includes no advertising code.

App-specific privacy descriptions distinguish local records, optional Google Drive authentication/storage, and external App Store/TestFlight/itch.io services. No wellness outcome, rating, testimonial, or download-count claims are made.

## October 11, 2026 refresh

Each change was checked against what users can get today, not against development plans:

- AllyPiano: App Store version 1.1 (released September 26, 2026). Its release notes and description cover the Salamander Grand purchase, restore, background-audio mixing, Infinite sustain, and the new icon. The store record, icon, and screenshots were refreshed from the Apple Lookup API; the second screenshot is now the Salamander Grand keyboard. The web picker includes Salamander Grand at no cost (sibling `instrument-picker-sheet` spec). Transpose (AllyPiano #19) is in neither App Store 1.1 nor the live web bundle, so it is not described.
- AllyScore/AllyScores: the editor and reader deploy from `main` on every push; the last deploy before this refresh included #447 (score versions) and #448 (ending brackets).
- AlexFighters: the itch.io build was last deployed October 4, 2026 (`65a9a86`), with the complete SEA stage, original sound and music, and the retry flow. The later HD art pass (#201/#202) is not deployed and is not described.
- AllyStation: no public download. TestFlight builds include the warmup and Mommy rescue. The Brother rescue (#129) is still in progress and is not promised.
- Web-app analytics: the live AllyClock, AllyPiano, AllyScore, and AllyScores web apps load the shared Umami Cloud tracker. Their privacy sections now disclose it. Before this refresh, AllyClock and AllyPiano wrongly said they had no analytics. The iOS apps contain no analytics code.
- AllyFast, AllyFastLite, AllyMetronome, AllyMetronomeLite, and AllyClock: Apple lookup versions, screenshots, and descriptions are unchanged.
