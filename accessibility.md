---
title: Accessibility
nav_exclude: true
description: "Accessibility statement for ncsu.software: conformance target, how the site is tested, what is known to be outstanding, and how to report a barrier."
---

# Accessibility

## Where to send a problem

If any part of this site blocks you, tell us and we will fix it:

- email [timm@ieee.org](mailto:timm@ieee.org)
- or open an issue: [github.com/ncsu-software/ncsu-software.github.io/issues](https://github.com/ncsu-software/ncsu-software.github.io/issues)

Say which page, what you were trying to do, and what you use to browse (screen
reader, magnifier, keyboard only, and so on). We aim to reply within five
working days.

## Conformance target

This site aims at **WCAG 2.1 Level AA**, the standard referenced by NC State's
IT accessibility policy and by Section 508. As of **19 Nov 2026** every page
below passes every machine-checkable Level A and AA rule, and the manual
criteria listed further down have been verified in a real browser.

Pages covered: home, AI &amp; SE, Alumni, Contact / Visit, Faculty &amp; Labs,
Internships, Keynotes &amp; Talks, News &amp; Publications, Pick Your Professor,
Student Life, Why Live in Raleigh, and this page.

## How it is tested

`make a11y` builds the site, serves it locally, and runs `tools/a11y/scan.js`.
The scan fails the build if anything regresses, so the claim above is
reproducible rather than remembered. It runs:

1. **axe-core 4.14** (rulesets `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`) over
   every page in four states: desktop at 1280px, 320px (equivalent to 400%
   zoom), narrow with the navigation menu open, and with
   `prefers-reduced-motion: reduce`.
2. **Criteria axe cannot decide**, per page:
   - 2.4.3 / 2.4.7 — the tab ring is walked with real <kbd>Tab</kbd> presses and
     every stop is checked for a visible focus indicator.
   - 4.1.2 — the Chrome accessibility tree (what a screen reader is handed) is
     dumped and checked for any button, link, or field without a name.
   - 2.4.4 link purpose, 1.3.1 heading structure and landmarks, 1.1.1 alt-text
     quality, 2.4.2 page titles, 3.1.1 language, 2.2.1 / 2.2.4 auto-refresh,
     3.3.2 labels.
   - 1.4.12 — the standard text-spacing override is injected and the page is
     checked for clipped or cut-off text.
3. **Behaviour**, because markup alone proves nothing:
   - the photo slideshow stops when paused and resumes when played;
   - it never starts under reduced motion, and the "we're hiring" badge stops
     animating there;
   - the Pick Your Professor matrix can be driven with <kbd>Tab</kbd> and
     <kbd>Enter</kbd>;
   - the narrow-window menu button opens with <kbd>Enter</kbd>;
   - the campus map pans with the arrow keys.

Colour contrast was additionally measured by hand on the sidebar, where axe
returns "incomplete" because a CSS gradient sits behind the text. Lowest
measured text ratio on the site is 5.4:1 against a 4.5:1 requirement.

## Colour and type

Colour and typography follow the university brand:
[colour](https://brand.ncsu.edu/designing-for-nc-state/color/) and
[typography](https://brand.ncsu.edu/designing-for-nc-state/typography/).
Wolfpack Red leads, Wolfpack Black carries headings and body copy, and several
expanded-palette colours are varied across partner pills, map pins and the
topic matrix. Type is Roboto throughout, with Roboto Slab for captions, at the
theme's sizes (16px on a desktop, 14px on a phone) and 140% leading, inside the
brand's 130-160% range. The brand's 16px floor is a recommendation rather than
a rule, and WCAG sets no minimum size: what AA requires is that text survives
200% zoom and reflows at 320px, both of which `make a11y` checks on every
page.

Two brand colours cannot be used as-is for small text and are handled the way
the brand guide allows:

- Hunt Yellow (#FAC800) is 1.5:1 on white. The honour marks (award rosette,
  keynote mic) keep the Hunt Yellow fill and are outlined in a **shade** of it,
  #7A6200, so the shape itself clears 3:1; each also has text beside it, so no
  meaning rides on the colour. The "AI" mark is live text, which an outline
  cannot rescue, so it sits as black type on a Hunt Yellow field (11.9:1) —
  which is the brand rule for Hunt Yellow anyway.
- Wolfpack Red tints in the topic matrix are decoration only: each level also
  carries a glyph and a text label, so nothing depends on colour alone.

## Known limitations

Stated plainly, because they are the honest edges of the claim above:

- **No testing with disabled users, and no end-to-end screen-reader session.**
  Names, roles, and reading order were verified through the accessibility tree
  and by keyboard, not by a VoiceOver or NVDA user working through a task.
- **Linked PDFs are not audited.** Slide decks under `pdfs/` and PDFs on other
  sites are likely untagged and are not claimed to conform. Ask us and we will
  supply the content in another format.
- **Third-party components.** The campus map is Leaflet and the icons come from
  Font Awesome; both are kept keyboard-operable and named here, but their
  internals are not ours to fix.
- **External links.** Pages at `ncsu.edu`, lab sites, and publisher sites follow
  their own accessibility practices.
- **WCAG 2.2** (for example 2.4.11 focus not obscured, 2.5.8 target size) is not
  yet claimed.

## What was fixed, Nov 2026

Contrast on the gold "AI" mark, the keynote and award icons, the deadline
badge, the sidebar footer, and the matrix totals; a keyboard-reachable
pause control plus reduced-motion handling for the slideshow and the hiring
badge; keyboard operation and a non-colour cue for the Pick Your Professor
matrix; accessible names for the map markers; a focus ring on the search box;
a keyboard-reachable scroll container for wide tables; and distinct names for
repeated "feature" and "photo" links.
