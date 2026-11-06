---
title: "For Researchers"
date: 2018-12-28T15:14:39+10:00
weight: 3
about: Future of Software Engineering through Advanced Research & innovation!
eyebrow: "Research"
heading: "Research at NC State"
lead: "Our faculty work across AI for software engineering, testing and analysis, software analytics, human factors, and more."
---

<section class="section section-compact" id="faculty">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Faculty</p>
      <h2>Meet the researchers</h2>
    </div>
    <div class="faculty-grid">
      {% for person in site.people %}
      <a class="faculty-card" href="{{ person.url | relative_url }}">
        <img src="{{ person.photo | relative_url }}" alt="{{ person.name }}" loading="lazy" width="320" height="320" />
        <div class="faculty-body">
          <h3>{{ person.name }}</h3>
          <p class="faculty-role">{{ person.role }}</p>
          <p class="faculty-areas">{{ person.areas | slice: 0, 3 | join: " · " }}</p>
        </div>
      </a>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section section-tinted section-compact" id="themes">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">What we work on</p>
      <h2>Research themes</h2>
    </div>
    <div class="themes">
      {% for theme in site.data.research_themes %}
      <article class="theme">
        <h3>{{ theme.title }}</h3>
        <p>{{ theme.summary }}</p>
        <p class="theme-people">{% for name in theme.people %}{% include person-link.html name=name %}{% unless forloop.last %} · {% endunless %}{% endfor %}</p>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

{% if site.data.posters and site.data.posters.size > 0 %}
<section class="section section-compact">
  <div class="container">
    {% include poster-gallery.html %}
  </div>
</section>
{% endif %}
