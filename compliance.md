---
title: Compliance
nav_exclude: true
redirect_from:
  - /accessibility.html
description: "How ncsu.software meets NC State's rules for a research-group website: which regulations apply, typography, colour, and accessibility — with the open items named."
---

# Compliance

All of the content on this page was checked with the department IT group on
**19 Nov 2026**. That review raised points on typography and colour schemes,
all of which have since been fixed — [FAQ 1](#type) and [FAQ 2](#colour) are
here because of that feedback.

What follows is which rules apply to this site, and how we meet them.

- [FAQ 1. Does this site follow NC State's typography conventions?](#type)
- [FAQ 2. Does this site follow NC State's colour conventions?](#colour)
- [FAQ 3. Does this site meet NC State's accessibility requirements?](#a11y)
- [FAQ 4. What regulations apply to a research lab running a website at NC State?](#rules)
- [FAQ 5. Is this an official departmental website?](#official)
- [FAQ 6. What are the open issues with this site?](#outstanding)

## FAQ 1. Does this site follow NC State's typography conventions?
{: #type}

Yes.

The conventions, from
[brand.ncsu.edu/designing-for-nc-state/typography](https://brand.ncsu.edu/designing-for-nc-state/typography/):

| The rule | What we do |
|---|---|
| Roboto and Roboto Condensed are primary; use most prominently | Roboto throughout, every page |
| Roboto Slab is secondary — pull quotes, captions, facts set apart | Roboto Slab on captions and pull quotes only |
| Regular weight for body copy, bold for emphasis | As specified |
| Arial is the approved fallback when a platform forces it | Arial, then `system-ui`, in every font stack |
| Web body text 16px or larger | 16px desktop, 14px phone |
| Line height 130–160% | 140% |
| Never squeeze, stretch or skew a typeface | No transforms on type |
| Never force-justify a copy block | No justified text |
| Never set body copy in all caps | Caps only on short nav section headings |
| Do not use Roboto Flex, Mono or Serif | None used |
| Meet WCAG AA / Section 508 | [FAQ 3](#a11y) |

On the 16px floor: the brand states it as a recommendation, and WCAG sets no
minimum text size at all. What AA requires is that text survives 200% zoom and
reflows at 320px — both checked on every page by `make a11y`.

## FAQ 2. Does this site follow NC State's colour conventions?
{: #colour}

Yes.

The conventions, from
[brand.ncsu.edu/designing-for-nc-state/color](https://brand.ncsu.edu/designing-for-nc-state/color/):

| The rule | What we do |
|---|---|
| Core palette: Wolfpack Red `#CC0000`, Black `#000000`, White `#FFFFFF` | Exactly these values |
| Wolfpack Red should predominate | Red carries every link, button, rule and accent |
| Core palette more prominent than any other | Red and black dominate; secondaries are small accents |
| Use several expanded-palette colours, to keep them subordinate to red | Reynolds Red, Pyroman Flame, Hunt Yellow, Genomic Green, Carmichael Aqua, Innovation Blue and Bio-Indigo, varied across partner pills, map pins and legends |
| Black type over Hunt Yellow, never white | The "AI" mark is black on Hunt Yellow, 11.9:1 |
| Adhere to WCAG AA for all colour combinations | Lowest measured text ratio on the site is 5.4:1 against a 4.5:1 requirement |

Two brand colours cannot be used as-is for small text, and are handled the way
the brand guide allows:

- **Hunt Yellow** (`#FAC800`) is 1.5:1 on white. The honour marks (award
  rosette, keynote mic) keep the Hunt Yellow fill and are outlined in a shade of
  it, `#7A6200`, so the shape clears 3:1; each also has text beside it, so no
  meaning rides on colour. The "AI" mark is live text, which an outline cannot
  rescue, so it sits as black type on a Hunt Yellow field — the brand rule for
  Hunt Yellow anyway.
- **Wolfpack Red tints** in the topic matrix are decoration only: each level
  also carries a glyph and a text label, so nothing depends on colour alone.

## FAQ 3. Does this site meet NC State's accessibility requirements?
{: #a11y}

### Conformance target

This site aims at **WCAG 2.1 Level AA**, the standard referenced by NC State's
IT accessibility policy and by Section 508. As of **19 Nov 2026** every page
below passes every machine-checkable Level A and AA rule, and the manual
criteria listed further down have been verified in a real browser.

Pages covered: home, AI &amp; SE, Alumni, Contact / Visit, Faculty &amp; Labs,
Internships, Keynotes &amp; Talks, News &amp; Publications, Pick Your Professor,
Student Life, Why Live in Raleigh, and this page.

### How it is tested

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

### Known limitations

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
  yet claimed. The sidebar navigation rows are deliberately under the 24×24px
  target size that 2.2 would require.

### What was fixed, Nov 2026

Contrast on the gold "AI" mark, the keynote and award icons, the deadline
badge, the sidebar footer, and the matrix totals; a keyboard-reachable
pause control plus reduced-motion handling for the slideshow and the hiring
badge; keyboard operation and a non-colour cue for the Pick Your Professor
matrix; accessible names for the map markers; a focus ring on the search box;
a keyboard-reachable scroll container for wide tables; and distinct names for
repeated "feature" and "photo" links.

## FAQ 4. What regulations apply to a research lab running a website at NC State?
{: #rules}

1. **Accessibility**, which carries the legal weight. NC State's IT
   accessibility policy and Section 508 both point at **WCAG 2.1 Level AA**.
   See [FAQ 3](#a11y).
2. **Typography and colour**, specified down to the hex value:
   [typography](https://brand.ncsu.edu/designing-for-nc-state/typography/),
   [colour](https://brand.ncsu.edu/designing-for-nc-state/color/).
   See [FAQ 1](#type) and [FAQ 2](#colour).
3. **Marks and identity.** The [logo rules](https://brand.ncsu.edu/logos/) cover
   versions, minimum sizes and clear space;
   [brand architecture](https://brand.ncsu.edu/brand-architecture/) adds that
   units identify with the NC State brick plus an optional typographic unit
   name, rather than a mark of their own. See [FAQ 6](#outstanding).
4. **URLs.** [RUL 08.00.15](https://policies.ncsu.edu/rule/rul-08-00-15/)
   expects official university URLs to end in `.ncsu.edu`.
   See [FAQ 6](#outstanding).

## FAQ 5. Is this an official departmental website?
{: #official}

No. We run this as a project inside the software engineering group, not as an
official department site.

NC State policy is to require standardised university websites: "All
departmental websites use the WordPress content management system with the NC
State v4 theme" ([COE IT](https://it.engr.ncsu.edu/get-resources/websites/),
[ECE](https://my.ece.ncsu.edu/communications/websites/)). We acknowledge that
requirement, and note that this is not an official website. It is a small
experiment in LLM-guided information architecture: we are trying to learn the
skills that let language models maintain a website.

Having searched the NC State web pages, we can find no rule that forbids a
research group from running a static site of its own. So we adopt this policy:
we run it ourselves, and we will not ask the department IT group or college
communications to modify or otherwise maintain it. This site is Jekyll on
GitHub Pages, in version control, with an automated accessibility gate on every
commit — building and maintaining systems is what this group does.

## FAQ 6. What are the open issues with this site?
{: #outstanding}

Two, named here so the passes above mean something.

**The domain, by choice.** [RUL 08.00.15](https://policies.ncsu.edu/rule/rul-08-00-15/)
expects official university URLs to end in `.ncsu.edu`, with outside domains
approved through Network Procedures. But we are a software engineering group,
and building and maintaining systems is an ongoing research task that we apply
to all of our activities. So this website is itself a research project, trying
to learn effective practices for using LLMs to build and maintain websites (see
[lessons learned](lessons.html)). Hence we publish at `ncsu.software`, and are
not seeking `.ncsu.edu` status.

**Identity marks.** Our favicon is a `{W}` tile, and the NC State brick appears
on no page. [Brand architecture](https://brand.ncsu.edu/brand-architecture/)
says units should identify with the brick, not a mark of their own. TBD.

## Where to send a problem

If any part of this site blocks you, tell us and we will fix it:

- email [timm@ieee.org](mailto:timm@ieee.org)
- or open an issue: [github.com/ncsu-software/ncsu-software.github.io/issues](https://github.com/ncsu-software/ncsu-software.github.io/issues)

Say which page, what you were trying to do, and what you use to browse (screen
reader, magnifier, keyboard only, and so on). We aim to reply within five
working days.
