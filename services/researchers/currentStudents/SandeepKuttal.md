---
layout: default
title: Sandeep Kuttal's Current Students
---
<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;">
  <h1 style="text-align: center;">{{ page.title }}</h1>
  {% for row in site.data.researchers.current_students.SandeepKuttal %}
  <div style="text-align: left; margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
      <div style="font-weight: bold; margin-top: 5px; margin-left: 20px;">
        {{ row.student_name }}
      </div>
      <div style="font-size: 18px; margin-left: 20px;">
        {{ row.student_website_link }}
      </div>
      <div style="font-size: 18px; margin-left: 20px;">
{% assign email = row.email %}
<a href="mailto:{{ email }}">{{ email }}</a>
      </div>
  </div>
  {% endfor %}
</div>


