---
layout: default
title: News
---
<div style="display: flex; flex-direction: column; align-items: left; border: 80px solid #ccc; padding: 20px;">
  <h1 style="text-align: center;">{{ page.title }}</h1>
  {% for row in site.data.researchers.news.KathrynStolee %}
  <div style="text-align: left; margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
      <div style="font-weight: bold; margin-top: 5px; margin-left: 20px;">
        <!-- &nsbp; -->
         <a href="{{row.link}}">{{ row.link }}</a>
      </div>
  </div>
  {% endfor %}
</div>



