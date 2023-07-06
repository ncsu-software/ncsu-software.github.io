---
layout: default
title: News
---

<script>
  function checkEmail(email){
    const urlParams = new URLSearchParams(window.location.search);
    const emailToCheck = urlParams.get('email');
    return emailToCheck ===(email);
  }
  function getEmail(){
    const urlParams = new URLSearchParams(window.location.search);
    const email = urlParams.get('email');
    console.log(`get email log: ${email}`)
    return email
  }
    function onLoad(){
    const urlParams = new URLSearchParams(window.location.search);
    const email = urlParams.get('email');
     console.log("Onload grants Page")
    localStorage.setItem("email",email)
  }

  function compare(email1,email2){
    return email1 ===(email2);
  }
  let html2;
  let emailstored;
</script>

<div style="display: flex; flex-direction: column; align-items: center; border: 4px solid #2c3e50; padding: 30px; background-color: #f2f2f2; font-family: Arial, sans-serif;">
<script type="text/javascript">
onLoad();
</script>
    <h1 style="text-align: center; color: #2c3e50; font-size: 32px;">{{ page.title }}</h1>
  {% for row in site.data.researchers.newsData %}
      <script>
        if(compare(localStorage.getItem("email"),`{{row.email}}`)){
            html2=`
  <div style="text-align: left; margin-bottom: 20px; border-bottom: 2px solid #CC0000; padding-bottom: 10px;">
    <div style="font-weight: bold; margin-top: 5px; margin-left: 20px; text-decoration: underline;">
      {% if row.link %}
      <h3><a href="{{row.link}}">{{ row.heading }}</a></h3>
      <!-- <a href="{{row.link}}" style="color: #CC0000; font-size: 24px; text-decoration: none;">{{ row.heading }}</a> -->
      {% else %}
      {{ row.heading }}
      {% endif %}
    </div>
    <div style="margin-top: 5px; margin-left: 20px; color: #333;">
      {% if row.summary %}
      {{ row.summary }}
      {% endif %}
    </div>
    </div>`;
      document.write(html2);
      }
    </script>
  {% endfor %}
</div>