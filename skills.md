---
title: Skills
nav_exclude: true
description: "Copy-paste AI skills for maintaining ncsu.software: setup, student directory, news, bios, lab wins, issues, accessibility."
---

# Skills for editing this site

This site is maintained with help from an AI assistant (we use
[Claude](https://claude.ai)). Do the one-time setup, then copy a
skill (a prompt), fill in the `<...>` parts, and paste.

**Index**

0. [One-time setup](#setup)
1. [Update the student directory from Drive](#directory)
2. [Add news, honors, or a paper](#news)
3. [Edit your faculty bio](#bio)
4. [Add your lab's wins to Student Life](#wins)
5. [Add an internship or alumni entry](#alumni)
6. [Fix an open issue](#issues)
7. [Check accessibility](#a11y)
8. [Email students about the directory](#email)

## 0. One-time setup
{: #setup}

1. **Get write access.** Ask Tim Menzies (tjmenzie@ncsu.edu) to add
   your GitHub account as a collaborator on
   [ncsu-software/ncsu-software.github.io](https://github.com/ncsu-software/ncsu-software.github.io).
   Accept the email invite.
2. **Install the tools.** Sign in at [claude.ai](https://claude.ai).
   Install [Claude in Chrome](https://claude.ai/chrome) so the
   assistant can read pages you have open.
3. **Connect your accounts.** In Claude's settings, connect GitHub
   and Google Drive (your NC State Google account, so it can read the
   shared `students` folder).
4. **Know the rules.** Pages are plain Markdown (Jekyll,
   just-the-docs theme). Facts need a link ("receipts, not
   adjectives"). Collaborators push straight to `main`; GitHub
   rebuilds [ncsu.software](https://ncsu.software) in about a
   minute and runs an accessibility scan (see the Actions tab).
   Every skill below says "push to main" so the assistant does not
   stop at a branch or pull request.

Then check it works:

> Clone github.com/ncsu-software/ncsu-software.github.io. Tell me if
> you can push to it, and list the site's pages with their titles and
> where each sits in the sidebar.

## 1. Update the student directory from Drive
{: #directory}

Students fill in one Google Doc plus a photo each in the Drive
`students` folder. This turns them into [directory](directory.html)
entries.

> Read the Google Docs in Drive folder
> https://drive.google.com/drive/folders/1itxDXsxfMofSIjq0TxuG7X9s5ua5DQAa
> (and its `doing` subfolder) that changed since `<date>`. Skip any
> doc that still says "your 4-10 lines here". Email and home page
> are required: list docs missing either.
>
> For each filled-in doc, add or update an entry in
> `_data/students.yml` in the repo
> github.com/ncsu-software/ncsu-software.github.io: name, slug
> (first-last), lab key, email, home page URL, and the bio cut to 3-5 lines, third
> person, plain English, no emoji. Keep every fact the student gave;
> add none.
>
> Photos must be `img/students/<slug>.jpg`, square, about 240x240.
> List any photo I need to add myself.
>
> Commit and push to main (no branch, no pull request). When the
> GitHub Actions build finishes, check the live
> [directory](https://ncsu.software/directory.html) shows each new
> entry with its photo.
>
> Then move each processed doc and its photo into `students/done`
> in Drive (ask me first; if you cannot move files, list them for me
> to move).
>
> Last, draft the two broadcast emails in [skill 8](#email) for me
> to send.

## 2. Add news, honors, or a paper
{: #news}

> In github.com/ncsu-software/ncsu-software.github.io, add this item
> to `pubs.md` (and, if it is big news, the front page `README.md`):
> `<what happened, who, when>`. Receipt: `<URL>`.
> Match the style of nearby items: one or two lines, the venue or
> award in bold, a link to the source. No adjectives the source does
> not support. Show me the diff, then commit and push to main.

## 3. Edit your faculty bio
{: #bio}

> In github.com/ncsu-software/ncsu-software.github.io, find my
> paragraph on `faculty.md` (I am `<name>`). Rewrite it from this:
> `<your notes or CV link>`. Keep it the same length as the other
> bios, plain English, with links for each claim. Commit and push to
> main, and show me the before and after.

## 4. Add your lab's wins to Student Life
{: #wins}

> In github.com/ncsu-software/ncsu-software.github.io, add a section
> for `<lab name>` (`<professor>`) to `students.md`, matching the
> existing lab sections: a 2-line lab summary, then bullets for these
> wins: `<defenses, awards, internships, papers, with links>`. Add
> face tiles for students who already have photos in
> `img/students/`. Link the section to the lab's part of
> `directory.html`. Commit and push to main.

## 5. Add an internship or alumni entry
{: #alumni}

> In github.com/ncsu-software/ncsu-software.github.io, add
> `<student>` (`<lab>`, `<degree and year>`) to
> `<internships.md or alumni.md>`: `<company/role or where they are
> now>`. Receipt: `<URL>`. Match the existing format. Commit and
> push to main.

## 6. Fix an open issue
{: #issues}

> Read the open issues at
> https://github.com/ncsu-software/ncsu-software.github.io/issues.
> List each with a one-line plan. Then fix issue `#<n>`, push to
> main, and draft a comment for the issue that says what
> changed. Do not close the issue or post the comment yourself.

## 7. Check accessibility
{: #a11y}

> In github.com/ncsu-software/ncsu-software.github.io, read
> `accessibility.md` and the a11y scanner in `tools/a11y`. Check the
> pages I changed (`<files>`) against WCAG 2.1 AA: alt text, heading
> order, link text, color contrast. Fix what you can, push to main,
> and list anything you could not check.

## 8. Email students about the directory
{: #email}

Usually run as the last step of [skill 1](#directory).

> Using the `students` Drive folder and `_data/students.yml`, draft
> two broadcast emails for me to send (do not send them):
> (1) to students now in the [directory](https://ncsu.software/directory.html):
> check your entry, report fixes as GitHub issues;
> (2) to students not yet in it: how to add themselves (doc, photo,
> move to `students/doing`), with links to the directory and the
> Drive folder. Give a recipient list for each, grouped by lab.
> Drive docs are shared domain-wide, so student emails may not be
> visible: if so, address email (2) to the lab faculty and ask them
> to forward it.
