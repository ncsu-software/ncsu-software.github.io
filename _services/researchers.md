---
title: "For Researchers"
date: 2018-12-28T15:14:39+10:00
weight: 3
about: Future of Software Engineering through Advanced Research & innovation!
eyebrow: "Research"
heading: "What we work on"
lead: "Six research themes, and the people behind each one."
---

<section class="section section-compact" id="themes">
  <div class="container">
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
<section class="section section-tinted section-compact">
  <div class="container">
    {% include poster-gallery.html %}
  </div>
</section>
{% endif %}
