---
layout: default
title: Current Students- services/researchers\timothy_menzies.md
---
<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;">
  <h1 style="text-align: center;">{{ page.title }}</h1>
    <h1>HERE WE will display the Current Students and their details</h1>
  {% for row in site.data.researchers.current_students.timothy_menzies %}
  <div style="text-align: left; margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
      <div style="font-weight: bold; margin-top: 5px; margin-left: 20px;">
        {{ row.student_name }} -{{ row.student_website_link }}
      </div>
      <div style="font-size: 18px; margin-left: 20px;">
        student
      </div>
  </div>
  {% endfor %}
</div>



