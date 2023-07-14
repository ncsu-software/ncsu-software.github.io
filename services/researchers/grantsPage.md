---
layout: default
title: Grants
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
    console.log("Compare grants Page")
    return email1 ===(email2);
  }
  let html2;
  let emailstored;
</script>

<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;">
<script type="text/javascript">
onLoad();
</script>
  <h1 style="text-align: center;">{{ page.title }}</h1>
  {% for row in site.data.researchers.sheets.GrantsResponses %}
      <script>
          console.log("inside grants page");
        if(compare(localStorage.getItem("email"),`{{row.EmailAddress}}`)){
            html2=`
            <div style="text-align: left; margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
      <div style="font-weight: bold; margin-top: 5px; margin-left: 20px;">
        <h3><a href="{{row.Link}}">{{ row.Title }}</a></h3>
        <p>Sponsor: {{ row.Sponsor }}</p>
        <p>Year: {{ row.Year }}</p>
        <p>Amount: {{ row.Amount }}</p>
      <div style="margin-top: 5px; margin-left: 20px; color: #333;">
      {% if row.Summary %}
      {{ row.Summary }}
      {% endif %}
    </div>
  </div>
      </div>`;
      document.write(html2);
      }
    </script>
  {% endfor %}
</div>