---
name: debug-app
description: Inspect the running AllyWorld website when debugging page behavior, layout, broken links, loading failures, or browser errors.
---

# Debug the Running App

AllyWorld currently contains static HTML pages, with no application state
bridge or framework dev server. Inspect the DOM, computed styles, resource
loading, and browser errors before inferring a cause from screenshots.

## Getting a session

Start an agent-owned server from the repository root on an available loopback
port, recording the process/session so only that server is stopped later:

```bash
python3 -m http.server <free-port> --bind 127.0.0.1
```

Open `http://127.0.0.1:<free-port>/` through the available browser tools.
Check `/customer-support/` and `/privacy-policy/` when relevant. Do not take
over an existing server or disturb the user's live browser session.

## Diagnose

1. Reproduce the reported behavior on the affected route at the relevant
   viewport size. Record the browser, viewport, zoom, and exact steps.
2. Inspect only the relevant DOM nodes, computed CSS, and bounding boxes;
   summarize the results instead of returning the entire document.
3. Check console errors, failed resource requests, link targets, and relative
   URL resolution as supported by the active browser tools.
4. Capture before/after screenshots for visual questions and use
   `pixel-verify` to measure differences. Keep viewport, zoom, fonts, and
   scroll position consistent.
5. Verify the original reproduction after fixing the cause, and stop only
   the server process you started.

Use the current browser tool documentation for supported inspection APIs.
If an app framework or debug bridge is added later, inspect its actual
implementation before assuming an API exists.
