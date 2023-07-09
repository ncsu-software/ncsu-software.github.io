---
layout: default
title: Employment Opportunity
---

<script>
  function checkEmail(email){
    const urlParams = new URLSearchParams(window.location.search);
    const emailToCheck = urlParams.get('email');
    return emailToCheck ===(email);
  }
</script>

<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;">
  <h1 style="text-align: center;">{{ page.title }}</h1>
  <ul style="list-style-position: outside;">
  {% for row in site.data.researchers.sheets.EmploymentOpportunityResponses %}
         <script>
      if (checkEmail("{{ row.EmailAddress }}")) {
        document.write('<li style="margin-left: 20px;"><div style="margin-top: 5px;">{{ row.opportunity }}</div></li>');
      }
    </script>
  {% endfor %}
  </ul>
</div>