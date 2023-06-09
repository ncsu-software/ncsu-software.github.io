---
title: "Success Stories"
date: 2018-12-28T15:14:39+10:00
weight: 1
about: Elevating the Future of
---
<div>
  <span>_services\successstories.md</span>
  <ul style="list-style-type: none;">
    {% for story in site.data.success_stories %}
      <li style="margin-bottom: 20px;">
        <div style="background-color: #f5f5f5; border-radius: 10px; padding: 10px;">
          <div style="display: flex; flex-direction: {% if forloop.index0 | modulo: 2 == 0 %}row{% else %}row-reverse{% endif %};">
            <div style="flex: 1;">
              <img src="{{ story.image | relative_url }}" alt="{{ story.name }}" style="width: 200px; height: auto;">
            </div>
            <div style="flex: 1; margin-left: {% if forloop.index0 | modulo: 2 == 0 %}20px{% else %}0{% endif %}; margin-right: {% if forloop.index0 | modulo: 2 == 0 %}0{% else %}20px{% endif %};">
              <h2>{{ story.name }}</h2>
              <p><strong>What they did:</strong> {{ story.work }}</p>
              <p><strong>What they are doing now:</strong> {{ story.current_work }}</p>
              <p><strong>Comments: </strong>{{story.comments}}</p>
              <p><strong>Mantra: </strong>{{story.comments}}</p>
              {% if story.web_page %}
                <p><a href="{{ story.web_page }}" target="_blank">Website</a></p>
              {% endif %}
              <p><a href="{{ story.papers_link }}" target="_blank">Research Papers Link</a></p>
              {% if story.html_file %}
                <p><a href="{{ story.html_file }}" target="_blank">Research Papers In Our Website</a></p>
              {% endif %}
            </div>
          </div>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>


<!-- <div>
  <span>_services\successstories.md</span>
  <ul>
    {% for story in site.data.success_stories %}
      <li style="display: flex; flex-direction: {% if forloop.index0 | modulo: 2 == 0 %}row{% else %}row-reverse{% endif %}; margin-bottom: 20px;">
        <div style="flex: 1;">
          <img src="{{ story.image | relative_url }}" alt="{{ story.name }}" style="width: 200px; height: auto;">
        </div>
        <div style="flex: 1; margin-left: {% if forloop.index0 | modulo: 2 == 0 %}20px{% else %}0{% endif %}; margin-right: {% if forloop.index0 | modulo: 2 == 0 %}0{% else %}20px{% endif %};">
          <h2>{{ story.name }}</h2>
          <p><strong>What they did:</strong> {{ story.work }}</p>
          <p><strong>What they are doing now:</strong> {{ story.current_work }}</p>
          <p><strong>Comments: </strong>{{story.comments}}</p>
          <p><strong>Mantra: </strong>{{story.comments}}</p>
          {% if story.web_page %}
            <p><a href="{{ story.web_page }}">Website</a></p>
          {% endif %}
          <p><a href="{{ story.papers_link }}" target="_blank">Research Papers Link</a></p>
          {% if story.html_file %}
            <p><a href="{{ story.html_file }}">Research Papers In Our Website</a></p>
          {% endif %}
        </div>
      </li>
    {% endfor %}
  </ul>
</div> -->
