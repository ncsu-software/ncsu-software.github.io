---
layout: default
title: Research Papers- services\researchers\papers\timothy_menzies.md
---
<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;">
  <h1 style="text-align: center;">{{ page.title }}</h1>
  {% for row in site.data.researchers.papers.timothy_menzies %}
  <div style="text-align: left; margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
    <a href="{{ row.DOI }}" target="_blank" style="text-decoration: underline; color: inherit; display: inline-block;">
      <div style="margin-left: 20px;">
        {{ forloop.index }}. <span style="font-weight: bold;">{{ row.Authors | replace:',', ', ' }}:</span>
      </div>
      <div style="font-weight: bold; margin-top: 5px; margin-left: 20px;">
        {{ row.Title }}
      </div>
      <div style="font-size: 18px; margin-left: 20px;">
        {{ row.Journal }}, {{ row.Volume }} ({{ row.Year }})
      </div>
    </a>
  </div>
  {% endfor %}
</div>

