---
layout: default
title: Research Papers
---
<style>
  .carousel-inner {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  .row-content {
    /* max-height: 300px; */
    overflow: hidden;
    word-break: break-word;
  }
  .carousel-inner img {
    flex: 0 0 auto;
    width: auto;
    max-height: 200px; /* Adjust the maximum height as needed */
    object-fit: contain;
    margin-right: 10px; /* Adjust the spacing between images */
  }
</style>

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
     console.log("Onload labPage")
    localStorage.setItem("email",email)
  }

  function compare(email1,email2){
    return email1 ===(email2);
  }
  let html2;
  let emailstored;
</script>

<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;" onload="onLoad()">
<script type="text/javascript">
onLoad();
</script>
<h1 style="text-align: center;">{{ page.title }}</h1>
<ul>
  {% assign rowIndex = 1 %}
  {% for row in site.data.researchers.researchPapers %}
    <script>
        console.log("inside lab page recent publications");
        if(compare(localStorage.getItem("email"),`{{row.email}}`)){
        html2= `<div style="text-align: left; margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;"> <a href="{{ row.DOI }}" target="_blank" style="text-decoration: none; color: inherit; display: inline-block;"><div style="margin-left: 20px;">&bull; <span style="/*font-weight: bold*/;font-family: arial">{{ row.Authors | replace:',', ', ' }}:</span> </div><div style="/*font-weight: bold*/;font-family: arial; margin-top: 5px; margin-left: 20px;"> {{ row.Title }}</div><div style="font-size: 18px; margin-left: 20px;"> <span style="text-decoration: underline;">{{ row.Journal }}</span>, <span style="text-decoration: underline;">{{ row.Volume }}</span></div></a></div>`;
        document.write(html2);
        }
    </script>
  {% endfor %}
</ul>
</div>

<script>
  // Initialize all carousels on the page
  document.addEventListener("DOMContentLoaded", function() {
    const carousels = document.querySelectorAll(".carousel");
    carousels.forEach(function(carousel) {
      carousel.querySelector(".carousel-inner").firstElementChild.classList.add("active");
    });
  });
</script>
