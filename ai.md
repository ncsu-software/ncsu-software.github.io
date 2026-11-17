---
title: "AI & SE @ NC State"
nav_order: 4
---

<a class="hiring" href="https://jobs.ncsu.edu/postings/237085"
   title="We're hiring: open-call Professor position, NC State Computer Science">
  <i class="fa-solid fa-certificate"></i>
  <span>WE'RE<br>HIRING</span>
</a>

# <i class="fa-solid fa-robot"></i> AI & SE @ NC State

**AI, carefully**: AI enthusiasm plus engineering rigor. That is
how a top-five software engineering group uses AI. Reading our
2025&ndash;26 papers, five themes emerge. One warning, before
the hype: this faculty recently co-edited an IEEE Software
special issue on [AI and
productivity](https://doi.org/10.1109/MS.2026.3683172) whose
bottom line was *"AI coding tools are genuinely useful — but they
do not substitute for human judgment."* That attitude — that we should carefully
assess both the benefits and costs of AI — runs through all our
work.

## 1. Humans and AI, side by side

We model how real developers actually work with AI — and how AI
could join the team. Kuttal's HFXE lab predicts where
collaborating developers will navigate next ([CHI 2026 Honorable
Mention](https://doi.org/10.1145/3772318.3791506)) and maps how
LLM early adopters are reshaping software work ([EMSE
2026](https://link.springer.com/article/10.1007/s10664-026-10917-0)).
Stolee and Xu jointly modeled 76 developers' intentions, actions,
and emotions while coding with AI ([FSE
2026](https://doi.org/10.1145/3808120)), and Xu's human-AI code
comprehension work took a **Distinguished Paper Award** at [ICPC
2026](https://arxiv.org/abs/2504.04553).

## 2. Testing the AI

AI is software; somebody has to check it. D'Amorim tests the deep
learning libraries everything else depends on, via fuzzing and
[neurosymbolic constraint learning (ICSE
2026)](https://damorim.github.io/publications/Naziri_ETAL_ICSE26_1.pdf).
Ore measures how [dependably LLMs generate
code](https://doi.org/10.1016/j.jss.2025.112548). Xu probes
privacy leaks and [backdoors in code
LLMs](https://arxiv.org/abs/2510.13992) (IEEE TCSE Distinguished
Paper, ICSME 2026). Assunção checks whether LLMs can even [tell
when two programs are the same](https://arxiv.org/abs/2608.23961).

## 3. AI as the engineer

We put LLM agents to work on the chores developers dread:
[end-to-end dependency upgrades (ICSME
2026)](https://doi.org/10.1109/ICSME67971.2026.00122), [agentic
runtime healing (CACM
2026)](https://dl.acm.org/doi/abs/10.1145/3800691), and
LLM-assisted backporting for the Robot Operating System
(Assunção + Xu, ICSE 2026) — always with a human in the loop.

## 4. Frugal AI: how low can you go?

Against the bigger-is-better tide: Menzies' [data-light
challenge](https://dl.acm.org/doi/10.1145/3808192) shows a few
dozen labels often match massive optimizers across 100+ SE tasks;
the [EZR toolkit](https://onlinelibrary.wiley.com/journal/1097024x)
packs a dozen classic learners into under 1000 lines; the
[MOOT repository](https://github.com/timm/moot) gives everyone
the data to check us. Kuttal's lab made the same point from the
HCI side: a sub-10ms behavioral model beat a 32B-parameter LLM at
predicting developer navigation (VL/HCC 2026).

## 5. Teaching SE in the AI era

Our stance: *we do not need classes on how to prompt; we need
classes on how to govern.* In the AI era, our graduates need to:

- understand code more deeply, and how it can be improved;
- treat testing as imperative when using AI tools;
- understand both symbolic and subsymbolic (LLM) systems;
- know when an LLM service can be replaced by something cheaper;
- integrate AI tools into existing systems.

Heckman's six-year study of a CS2 course traces how students'
help-seeking moved from forums and office hours to GenAI
([SIGCSE 2026](https://sigcsevirtual2026.acm.org/details/sigcse-virtual-2026-papers/19/From-Covid-to-GenAI-Tracing-Long-term-Changes-of-Students-Help-seeking-Behaviors-in)),
and Stolee and Ore study how students comprehend and review
code — the exact skill that matters most when the code was
written by a machine.
