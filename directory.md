---
title: Directory
parent: For Students
nav_order: 1
description: "Who's who among NC State software engineering students, by lab."
---

{% include badges.html %}

# <i class="fa-solid fa-address-book" aria-hidden="true"></i> Student Directory

Who works on what, lab by lab.<br>
Student here and not listed (or something is wrong)? See
[add yourself](#add).

{% for lab in site.data.students.labs %}
{% assign folks = site.data.students.people | where: "lab", lab.key | sort: "name" %}
{% if folks.size > 0 %}
<h2 id="{{ lab.key }}">{{ lab.name }} <small>({{ lab.prof }})</small></h2>
<div class="dir">
{% for p in folks %}
{% if p.nophoto %}{% assign src = "/img/students/placeholder.svg" | relative_url %}{% else %}{% assign src = "/img/students/" | append: p.slug | append: ".jpg" | relative_url %}{% endif %}
<div class="dir-card" id="{{ p.slug }}">
  <img src="{{ src }}" alt="{{ p.name }}" loading="lazy">
  <div>
    <b>{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</b>{% if p.note %} <span class="dir-note">({{ p.note }})</span>{% endif %}
    <span class="dir-links">{% if p.email %}<a href="mailto:{{ p.email }}">{{ p.email }}</a>{% endif %}{% if p.email and p.url %} &middot; {% endif %}{% if p.url %}<a href="{{ p.url }}" aria-label="{{ p.name }} home page">home page</a>{% endif %}</span>
    <p>{% if p.pending %}<span class="dir-pending">Entry pending — this student has not written their few lines yet. <a href="#add">How to add yours</a>.</span>{% else %}{{ p.bio }}{% endif %}</p>
  </div>
</div>
{% endfor %}
</div>
{% endif %}
{% endfor %}

## Add yourself (or fix your entry)
{: #add}

1. Open the [students folder](https://drive.google.com/drive/folders/1itxDXsxfMofSIjq0TxuG7X9s5ua5DQAa)
   (NC State login) and find the Google Doc with your name.
   No doc? Copy any other one and rename it `first-last`.
2. Fill in the doc in place: name, **NC State email**, **home page
   URL** (GitHub page, personal site, or LinkedIn), and 4 to 10
   lines about you.
3. Put a square head-and-shoulders photo next to it, named
   `first-last.jpg`, at least 240x240.
4. Move the doc and photo into `students/doing`.

Corrections to a listed entry: open an
[issue](https://github.com/ncsu-software/ncsu-software.github.io/issues).
