---
title: Lessons Learned
nav_exclude: true
description: "A working checklist for a university research-group website: who it is for, what it must contain, how it is maintained, and the anti-patterns we are trying to avoid."
---

# Lessons Learned

A university tells you how a site must *look* — fonts, colours, marks,
accessibility. It does not tell you what a research group's site should
**contain**. As far as we can find, no such checklist exists.

So we are building one. This site is a small distributed research project: a
dozen contributors, an LLM-guided information architecture, and two intake
channels that let new material arrive faster than anyone could hand-edit it —
a [shared Drive folder](https://drive.google.com/drive/folders/1Vl-guuURRJ6mT1gpYiJbhFDAQ8dhxXWa)
where students and faculty drop text and photos, and a
[public issue tracker](https://github.com/ncsu-software/ncsu-software.github.io/issues)
for everything else. Both feed a static site in version control. What follows
is the checklist as it stands. It is incomplete, and we would rather be told
so than guess.

## 1. Follow the rules that actually apply

Accessibility, typography, colour, marks, URLs. We keep the detail on a
separate page so it can be audited rather than asserted: see
[compliance](compliance.html). The short version — WCAG 2.1 AA with an
automated gate, the university palette and typefaces, and an honest list of
what is still open.

Three things we would do differently, or did and would again:

- **Get the requirements as a list before you start.** The brand guidance is
  spread over several pages and reads as prose. Ask an LLM to collapse it into
  a checklist — typefaces, weights, the hex values, the line-height band, what
  may never be done to a typeface — and build against that from the first
  commit. Retrofitting a palette is far more work than adopting one.
- **Check it in phone mode.** That is where most of this site is read, and it
  is where layouts break first: a sidebar that collapses badly, a table that
  overflows, type that reflows into a column two words wide. Narrow is the
  default case, not the edge case.
- **Automate the check so it cannot rot.** A standard you verify once is a
  standard you used to meet.

## 2. Know who you are writing for

Most academic sites fail here first: they are written for the people who made
them. Ours serves, in rough order of traffic we care about:

1. **Prospective graduate students**, deciding where to apply. They want
   people, topics, and a deadline — not a mission statement.
2. **Current students**, who need the directory, deadlines and internships.
3. **Faculty peers and reviewers**, checking that the work is real.
4. **Industry partners**, looking for tools, data and a way in.
5. **Press and university communications**, who need a quotable, sourced fact.
6. **Search engines and language models**, which increasingly mediate every
   audience above.

Each of those wants a different first screen. That is why the navigation has
one section per audience rather than one per committee.

## 3. Use LLMs to edit the site

This is the part that changed how the site is maintained.

A half-formed description of a job is enough. You do not have to name the
files, the selectors, or the order of operations — "the left-hand menu looks
crowded, and the red rules need more air" is a workable brief. The model finds
the stylesheet, makes the change, and shows you the result.

The leverage shows up when one page turns out to be wrong. We found compliance
and usability problems on a single page; checking the rest by hand would have
been an afternoon's work. Instead it took about ten minutes to sweep every
page for the same faults, fix them, and write up what had been fixed — and that
write-up became [compliance](compliance.html).

Two habits make this work rather than make a mess:

- **Say what is wrong, not how to fix it.** Describe the symptom you can see.
  A prescribed fix narrows the search to whatever you happened to think of.
- **Make the result checkable.** Every change lands as a diff in version
  control and has to survive the accessibility gate. The model is fast, which
  means it is fast at being wrong too; the gate is what makes the speed safe.

## 4. What the site contains

Abstracting over our own pages, this is the content list. Twenty-one items. We did
not start with it — it is what the site turned out to need, which is why we
think it is worth writing down.

**The claim, and its evidence**

1. **A headline claim on the first screen**, dated, scoped and sourced. Ours is
   a rank; the chart beside it shows the neighbours so the number can be
   checked rather than believed.
2. **Photographs of people doing things.** Dinners, conferences, labs. Not
   buildings.
3. **Recent papers**, each with venue, year and a link to the paper.
4. **Honours and awards**, attributed to the person who won them.
5. **Invited talks and keynotes**, with slides where we have them.
6. **Service** — editorships, chairs, programme committees. The least
   glamorous evidence that a group is load-bearing in its field.

**The people**

7. **Faculty and labs**: one entry per lab, saying what it actually studies.
8. **A student directory**: photo, lab, email, home page, and a few lines in
   the student's own words.
9. **Alumni destinations.** Where graduates went is the single most predictive
   thing a prospective student can read.
10. **Internships.** Where current students spent their summers.

**Getting in**

11. **A way to match interests to an advisor.** Ours is a topic-by-professor
    matrix; a list would do.
12. **How to apply**, and the deadline, stated as a date.
13. **The live deadlines, on every page.** Not only on the admissions page. An
    open faculty posting and the graduate application deadline ride as badges
    across the whole site, because a reader who arrives at a paper or a student
    profile should still see them. They put themselves up and take themselves
    down on their own dates.
14. **Contact and visit**: address, map, parking, and faculty email one click
    away.
15. **The place.** Nobody moves to a department; they move to a city.

**For people who are not students**

16. **Tools and data that ship**, with links to the repositories.
17. **Partners**, named.
18. **How the group uses AI** — or whatever the field's live question is this
    decade.

**About the site itself**

19. **A compliance statement** with the open items named.
20. **The maintenance prompts**, checked in, so the work is repeatable.
21. **This page**: what we learned building it.

Items 1–6 are the ones most often missing, and 7–10 are the ones that decide
where a student applies.

## 5. Content goals

- **Receipts, not adjectives.** Every claim carries a link to its source. If a
  sentence cannot be sourced, it is cut rather than softened.
- **Date and scope every ranking.** "Top five" is meaningless without the year,
  the region and the source; all three travel with the number.
- **Know your dates, and be driven by them.** A faculty search opens; graduate
  applications close on 15 December. Those are the moments the site exists for,
  and they are the only times most of its readers will ever visit. Ours carries
  two badges on every page: one for the open professor posting, and one that
  shows itself between 1 September and the deadline, then takes itself down. A
  deadline still being advertised in March is worse than no badge at all.
- **People, not buildings.** Photographs are of students and faculty doing
  things. No empty atriums.
- **Students are the product.** A directory that shows who is here, with their
  own words and their own links.
- **Let people add themselves.** A student should be able to join the site
  without learning git: write a doc, drop a photo, done.
- **Several front doors.** Students, industry and researchers each get a
  section, and none of them has to read the others.
- **Everything one level deep.** If a page needs two clicks, the structure is
  wrong.
- **Say what is missing.** An outstanding-issues list is worth more than a page
  of passes.
- **Machine-readable, without overclaiming.** Structured data describes the
  page and the people honestly; it does not assert an identity the university
  has not granted.
- **Prune.** Pages are removed when they stop being true. A site that only
  grows is a site nobody is reading.

## 6. Write for answer engines, not just search engines

Audience 6 in the list above is machines, and it is the one changing fastest.
Search optimisation is about ranking a link; answer optimisation is about being
the thing a model quotes when somebody asks "who works on testing at NC State?"
The two want different artefacts.

- **A one-sentence description on every page**, in the front matter. It feeds
  the meta description, the structured data, and the machine index below —
  written once, used three ways.
- **[`/llms.txt`](llms.txt)**, a plain-text map of the site: a paragraph on who
  we are, every page with its description, every faculty member with a link,
  and the admissions URL. Generated from the same front matter, so it cannot
  drift from the pages it describes.
- **`robots.txt` that names the AI crawlers explicitly** — GPTBot,
  OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended,
  Applebot-Extended, CCBot and the rest — rather than leaving them to a
  wildcard. If you want to be quoted, say so in the file they read first.
- **Structured data that does not overclaim.** The JSON-LD describes the page,
  names the university as the organisation, and lists the faculty as people the
  page mentions. It does not assert that this group is an organisation in its
  own right, because it is not.
- **Facts as text, not as pictures.** Our ranking is an HTML table with real
  numbers in it. A screenshot of the same table is invisible to every reader in
  this section.
- **Stable URLs.** When a page is renamed, the old address redirects rather
  than 404s. Models cite URLs they found months ago.

The honest caveat: none of this is measurable from here. You cannot A/B test an
answer engine, and we have no way to tell which of these six things is doing
the work. We do them because each is cheap and none can hurt.

## 7. How it is built and kept alive

The common thread is **distributed production**: nobody owns the site, several
people touch it in a given week, and each works in whatever medium they already
know — a Google Doc, a GitHub issue, a commit, a prompt. The machinery below
exists to let those meet in one place without anyone coordinating them.

- **Static, in well-known version control.** No CMS, no database, no server to
  patch, and every change has an author and a diff. Where possible use tools
  your audience already knows — GitHub, in our case, because the people
  maintaining a computer science site can already use it. A familiar tool needs
  no training, no account requests, and no one person who understands it.
- **Data as data.** People, topics and labs live in YAML, not in prose, so the
  pages can be regenerated rather than retyped.
- **An automated gate.** Accessibility is checked on every commit and fails the
  build; the claim is reproducible rather than remembered.
- **A written intake pipeline.** Contributions move `todo` → `doing` → `done`
  in the shared Drive, so at any moment it is clear what is waiting.
- **One place for the work queue.** Everything that is not a Drive drop is a
  GitHub issue — bug, fix, idea, "this page reads badly". The tracker is public,
  so a student can file against the site without asking anyone's permission,
  and nothing lives in somebody's inbox.
- **Harvest the prompts that worked.** When a half-formed request turns out to
  do a job well, it gets cleaned up and added to [skills](skills.html) — the
  routine work (ingesting student entries, adding news, checking accessibility)
  is now a page of prompts anyone can copy. A prompt that stays in one person's
  chat history has been written once and lost; in `skills` it is repeatable by
  whoever is holding the site this month.
- **Low bus factor.** Anything only one person can do is a defect. The prompts
  exist so the site does not depend on its author.
- **Few external dependencies.** Every third-party script is one outage away
  from being your problem.

## 8. Anti-patterns

The failure modes we watch for, most of them visible on somebody's department
site right now:

- **Nothing impressive.** The commonest failure, and the quietest: a site that
  never gives a reader a reason to care. Rankings, awards, keynotes, where the
  graduates went — those are the strongest things any group has, and they
  belong on the first screen with their sources attached, not three clicks
  down under "News". Put your best foot forward. Modesty reads as nothing to
  report.
- **The dead news page.** "Latest news" with a 2019 dateline does more damage
  than no news page at all.
- **Faculty-only.** A group site listing professors and no students tells a
  prospective student exactly where they would rank.
- **Adjectives without receipts.** "World-class", "cutting-edge",
  "internationally recognised" — all unfalsifiable, all ignored.
- **Undated claims.** A ranking with no year is a claim with no expiry date,
  which is to say no credibility.
- **PDF as the website.** Content only reachable as an untagged PDF is content
  excluded from search, from phones, and from screen readers.
- **Org-chart navigation.** Menus that mirror the administrative structure
  rather than the reader's question.
- **Logo soup.** Partner marks pasted in without permission, which is a
  trademark problem as well as a design one.
- **The locked CMS.** A site nobody can edit because the one person with the
  password graduated.
- **Contact routes that go nowhere.** A form, or an address, that no one reads.
- **Login walls.** Anything a prospective student must authenticate to see is
  something they will not see.
- **Template residue.** Placeholder text and stock photos left live.
- **Fake freshness.** An auto-updating date on a page whose content has not
  changed since 2021.

## Tell us what we are missing

This checklist is the part of the project we are least sure about. If you run a
research-group site and we have got something wrong, or left out something
obvious, open an
[issue](https://github.com/ncsu-software/ncsu-software.github.io/issues).
