---
name: pixel-verify
description: Use when verifying any change that alters drawn output, or when a visual shift/regression is reported with screenshots — compares before/after images at pixel precision and explains measured differences.
---

# Pixel-Level Visual Verification

Use a programmatic pixel diff to locate changes, then inspect the source
crops to identify the affected elements. Pixel measurements establish exact
deltas; visual interpretation explains them.

## When

- Before handing off ANY feature or bug fix that can change drawn output:
  the handoff evidence is a before/after diff that is either clean or shows
  exactly the intended deltas, stated numerically.
- When a user reports "X moved/shifted/looks different" with screenshots:
  diff their pair before hypothesizing.

## Protocol

1. **Collect the pair.** Two images of the same region at the same
   viewport/zoom: the user's screenshots, or captures taken before/after
   the change. Mismatched framing ruins the diff — recrop first if needed.

2. **Pixel diff (PIL, in the scratchpad):**

   ```python
   from PIL import Image, ImageChops
   import numpy as np
   a = Image.open(A).convert('RGB'); b = Image.open(B).convert('RGB')
   diff = ImageChops.difference(a, b)
   print('bbox', diff.getbbox())                      # None = pixel-identical
   d = np.asarray(diff).sum(axis=2)
   # Row/column heat profiles localize the moved region:
   hot = lambda v: [i for i, x in enumerate(v) if x > v.max() * 0.25]
   print('cols', hot(d.sum(axis=0)), 'rows', hot(d.sum(axis=1)))
   ```

   A `None` bbox is the clean-verification result. Otherwise crop the bbox
   from BOTH images, enlarge 4x with NEAREST, stack them vertically with a
   white gap, and save the composite.

3. **Interpret the measured difference.** Inspect the original images and
   enlarged composite with the current assistant's image tools. Describe which
   elements changed, direction, and measured deltas in ORIGINAL pixels (divide
   enlarged coordinates by four). Distinguish measured results from uncertain
   interpretation; do not claim exact motion from appearance alone. Use an
   available image-capable reader only if source pixels cannot be inspected.

4. **Convert findings to geometry, then to tests.** Pixels are for
   DISCOVERY; regression tests assert geometry. Map each measured delta to
   a code-level cause (baseline math, font family/weight, rasterization
   mode, a hit box that moved or vanished). Where regression coverage is
   warranted and tooling exists, assert DOM geometry or behavior directly.
   AllyWorld currently has no test suite; report measured evidence and any
   missing automated coverage without inventing test commands.

## Traps

- Two screenshots with a uniform 1px registration offset (window moved
  between captures): the heat profile shows EVERYTHING hot at low
  intensity. Subtract the common shift before reading per-element deltas —
  Verify the registration offset before interpreting individual elements.
- Antialiasing differences (HTML subpixel vs SVG grayscale text) read as
  "bolder", not as movement. They are real user-visible deltas — fix with
  rasterization-matching CSS, not by dismissing them.
- Generated-vs-measured width mismatches often show as one END of a label
  moving while the other stays — that is an anchor bug, not a translation.
