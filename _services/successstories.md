---
title: "Success Stories"
date: 2018-12-28T15:14:39+10:00
weight: 1
about: Where are our previous students now
eyebrow: "Alumni"
heading: "Where our graduates are now"
lead: "Our PhD alumni lead research and teaching at universities and industry labs across the country."
---

<section class="section section-compact">
  <div class="container">
    <div class="alumni-grid">
      {% for alum in site.data.alumni %}
      <article class="alum-card">
        <img src="{{ alum.photo | relative_url }}" alt="{{ alum.name }}" loading="lazy" width="320" height="320" />
        <div class="alum-body">
          <p class="alum-org">{{ alum.org }}</p>
          <h3>{{ alum.name }}</h3>
          <p class="alum-role">{{ alum.role }}</p>
          <p class="alum-links">
            {% if alum.website %}<a href="{{ alum.website }}">Website</a>{% endif %}
            {% if alum.papers %}<a href="{{ alum.papers }}">Publications</a>{% endif %}
          </p>
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div class="cta-inner">
      <h2>Your story could be next.</h2>
      <div class="cta-actions">
        <a class="button button-light" href="{{ '/services/students/' | relative_url }}">Graduate study</a>
        <a class="button button-ghost" href="{{ '/services/researchers/' | relative_url }}">Meet our faculty</a>
      </div>
    </div>
  </div>
</section>
