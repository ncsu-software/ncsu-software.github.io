---
layout: default
title: Current Students 
---

<script>
  function checkEmail(email){
    const emailToCheck = localStorage.getItem('email');
    console.log(`email param : ${emailToCheck} csv: ${email}`);
    return emailToCheck ===(email);
  }
</script>

<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;">
  <h1 style="text-align: center;">{{ page.title }}</h1>
  <ul style="list-style-position: outside;">
  {% for row in site.data.researchers.currentStudents %}
        <script>
      if (checkEmail("{{ row.email }}")) {
        document.write('<div style="text-align: left; margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;"><div style="font-weight: bold; margin-top: 5px; margin-left: 20px">{{ row.student_name }}</div><div style="font-size: 18px; margin-left: 20px;">{{ row.student_website_link }}</div><div style="font-size: 18px; margin-left: 20px;">{% assign student_email = row.student_email %}<a href="mailto:{{ student_email }}">{{ student_email }}</a></div></div>');
      }
    </script>
  {% endfor %}
  </ul>
</div>