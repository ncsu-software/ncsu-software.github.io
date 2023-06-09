---
title: "For Researchers"
date: 2018-12-28T15:14:39+10:00
weight: 4
about: Elevating the Future of Software Engineering through Advanced Research & innovation!
---
<div>
  <span>_services\successstories.md</span>
  <ul style="list-style-type: none;">
    {% for story in site.data.researchers.researchers %}
      <li style="margin-bottom: 20px;">
        <div style="background-color: #f5f5f5; border-radius: 10px; padding: 10px;">
          <div style="display: flex; flex-direction: {% if forloop.index0 | modulo: 2 == 0 %}row{% else %}row-reverse{% endif %};">
            <div style="flex: left;">
              <img src="{{ story.image | relative_url }}" alt="{{ story.name }}" style="width: 200px; height: auto;">
            </div>
            <div style="flex: 1; margin-left: {% if forloop.index0 | modulo: 2 == 0 %}20px{% else %}0{% endif %}; margin-right: {% if forloop.index0 | modulo: 2 == 0 %}0{% else %}20px{% endif %};">
              <h2>{{ story.name }}</h2>
              <p><strong>Mantra: </strong>{{story.comments}}</p>
              <p><strong>Lab (if they have one): </strong>{{story.comments}}</p>
              <p><strong>Mission: </strong>{{story.comments}}</p>
              {% if story.current_students_file %}
                  <p><a href="{{ story.current_students_file }}" target="_blank">Current Students</a></p>
              {% endif %}
              <button onclick="toggleDetails(this)" style="background-color: #CC0000; color: #ffffff;">Show More</button>
              <div class="hidden-details" style="display: none;">
                <p><strong>About:</strong> {{story.who_are_you}}</p>
                <p><strong>Their work:</strong> {{story.what_do_you_do}}</p>
                <p><strong>How can they help:</strong> {{story.how_can_you_help_me}}</p>
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
        </div>
      </li>
    {% endfor %}
  </ul>
</div>

<script>
  function toggleDetails(button) {
    var hiddenDetails = button.parentElement.getElementsByClassName('hidden-details')[0];
    if (hiddenDetails.style.display === 'none') {
      hiddenDetails.style.display = 'block';
      button.innerText = 'Show Less';
    } else {
      hiddenDetails.style.display = 'none';
      button.innerText = 'Show More';
    }
  }
</script>


