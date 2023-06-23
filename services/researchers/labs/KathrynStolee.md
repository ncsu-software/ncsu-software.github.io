---
layout: default
title: Labs
---
<style>
  .carousel-inner {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .carousel-inner img {
    flex: 0 0 auto;
    width: auto;
    max-height: 200px; /* Adjust the maximum height as needed */
    object-fit: contain;
    margin-right: 10px; /* Adjust the spacing between images */
  }
</style>

<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;">
  <h1 style="text-align: center;">{{ page.title }}</h1>
  {% assign labsData = site.data.researchers.labs.KathrynStolee %}
  {% assign labs = labsData | group_by: 'labName' %}
  {% for lab in labs %}
    <h2>{{ lab.name }}</h2>
    <div id="carousel-{{ lab.name }}" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        {% assign labImages = site.data.researchers.labs.KathrynStolee | where: 'labName', lab.name %}
        {% for image in labImages %}
          <div class="carousel-item{% if forloop.first %} active{% endif %}">
            <img src="{{ image.labImage }}" alt="{{ lab.name }}">
          </div>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
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
