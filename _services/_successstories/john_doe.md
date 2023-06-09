---
layout: default
title: John Doe's sResearch Papers
---
<div>
  <h1>John Doe's sResearch Papers</h1>
  <!-- Display the research papers for John Doe -->
{% assign csv_file = site.data.my_csv %}
{% assign rows = csv_file.rows %}
{% for row in rows %}
<div style="font-family: 'Open Sans', sans-serif;">
  <div style="font-weight: bold;">
    {{ forloop.index }}. Authors:
  </div>
  <div>
    {{ row.Authors | replace:',', ', ' }}
  </div>
  <div style="font-weight: bold;">
    Title, Journal, Volume (Year):
  </div>
  <div>
    {{ row.Title }}, {{ row.Journal }}, {{ row.Volume }} ({{ row.Year }})
  </div>
</div>
{% endfor %}
</div>

