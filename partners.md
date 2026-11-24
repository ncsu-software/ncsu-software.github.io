---
title: Partners
parent: For Industry
nav_order: 2
description: "Industry partners of NC State software engineering."
---

{% include badges.html %}

# <i class="fa-solid fa-handshake" aria-hidden="true"></i> Partners

<p class="partnerhead">who we work with:</p>
<ul class="partner-grid">
{%- for p in site.data.partners %}
  <li class="partner-cell"{% if p.full %} title="{{ p.full }}"{% endif %}>
  {%- if p.logo %}
    <img src="{{ p.logo | relative_url }}" alt="{{ p.full | default: p.name }}">
  {%- else %}
    <span class="chip">{{ p.name }}</span>
  {%- endif %}
  </li>
{%- endfor %}
</ul>
