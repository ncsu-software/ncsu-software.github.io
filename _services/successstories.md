---
title: "Success Stories"
date: 2018-12-28T15:14:39+10:00
weight: 1
about: Where are our previous students now
---
<div>
  <ul style="list-style-type: none;">
    {% for story in site.data.researchers.sheets.SuccessStories %}
      <li style="margin-bottom: 20px;">
        <div style="background-color: #f5f5f5; border-radius: 10px; padding: 10px;">
          <div style="display: flex; flex-direction: {% if forloop.index0 | modulo: 2 == 0 %}row{% else %}row-reverse{% endif %};">
            <div style="flex: 1;">
              <img src="{{ story.image | relative_url | replace: 'open?id=', 'uc?export=download&id=' }}" alt="{{ story.name }}" style="width: 200px; height: 200px;">
            </div>
            <div style="flex: 1; margin-left: 20px; margin-right: 200px;">
              <h2>{{ story.name }}</h2>
              <p><strong>What they are doing now:</strong> {{ story.current_work }}</p>
              {% if story.web_page %}
                <p><a href="{{ story.web_page }}" target="_blank">Website</a></p>
              {% endif %}
              <p><a href="{{ story.papers_link }}" target="_blank">Research Papers Link</a></p>
            </div>
          </div>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>
