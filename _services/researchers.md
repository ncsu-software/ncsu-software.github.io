---
title: "For Researchers"
date: 2018-12-28T15:14:39+10:00
weight: 4
about: Elevating the Future of Software Engineering through Advanced Research & innovation!
---
<style>
  .hidden-details {
    display: none;
  }
  
  .row-content {
    /* max-height: 300px; */
    overflow: hidden;
    word-break: break-word;
  }
  
  .show-more-btn {
    display: none;
    margin-top: 10px;
    background-color: #CC0000;
    color: #ffffff;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .show-more-container {
    margin-top: 10px;
  }
    .inline-content {
        display: flex;
        flex-wrap: wrap;
    }
    
    .inline-content p {
        margin-right: 20px;
    }


</style>

<div>
  <ul style="list-style-type: none;">
    {% for story in site.data.researchers.researchersNew %}
      <li style="margin-bottom: 20px;">
        <div style="background-color: #f5f5f5; border-radius: 10px; padding: 10px; overflow: hidden; display: flex;">
          {% if story.ProfilePicture %}
            <div style="margin-right: 20px;">
              <img src="{{ story.ProfilePicture }}" alt="{{ story.TitleAndName }}" style="max-width: 200px; height: auto;">
            </div>
          {% endif %}
          <div class="row-content">
            {% if story.YourPersonalWebsiteLink %}
            <a href="{{ story.YourPersonalWebsiteLink }}" target="_blank"><h2>{{ story.Name }}</h2></a>
            {% endif %}
            <h4>{{ story.Title }}</h4>
            {% if story.MissionOrMantra %}
            <p><strong>Mantra/Mission: </strong>{{ story.MissionOrMantra }}</p>
            {% endif %}
            {% if story.LabName %}
            <p><strong>Lab Name: </strong>{{ story.LabName }}</p>
            {% endif %}
            {% if story.CoreResearchAreas %}
              <p><strong>Core Research Areas: </strong>{{ story.CoreResearchAreas }}</p>
            {% endif %}
            <div class="inline-content">
    {% if story.CurrentStudents %}
        <p><a href="{{ story.CurrentStudents }}" target="_blank">Current Students</a></p>
    {% endif %}
    {% if story.DBLPPapers %}
        <p><a href="{{ story.DBLPPapers }}" target="_blank">DBLPPapers</a></p>
    {% endif %}
    {% if story.Grants %}
        <p><a href="{{ story.Grants }}" target="_blank">Grants</a></p>
    {% endif %}
    {% if story.Mission %}
        <p><strong>Mission: </strong>{{ story.Mission }}</p>
    {% endif %}
    {% if story.News %}
        <p><a href="{{ story.News }}" target="_blank">News</a></p>
    {% endif %}
    {% if story.EmploymentOpportunity %}
        <p><a href="{{ story.EmploymentOpportunity }}" target="_blank">Employment Opportunity</a></p>
    {% endif %}
    {% if story.Labs %}
        <p><a href="{{ story.Labs }}" target="_blank">Labs</a></p>
    {% endif %}
</div>

            {% if story.about %}
              <div class="show-more-container">
                <div class="hidden-details">
                  <p><strong>About:</strong> {{ story.about }}</p>
                  <!-- Add any additional fields you want to display here -->
                </div>
                <button class="show-more-btn" onclick="toggleDetails(this)">Show More</button>
              </div>
            {% endif %}
          </div>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>

<script>
  function toggleDetails(button) {
    var hiddenDetails = button.previousElementSibling;
    if (hiddenDetails.style.display === 'none') {
      hiddenDetails.style.display = 'block';
      button.innerText = 'Show Less';
    } else {
      hiddenDetails.style.display = 'none';
      button.innerText = 'Show More';
    }
  }
</script>






<!-- <div>
  <span>_services\researchers.md</span>
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
              <div class="hidden-details" style="display: none;">
                <p><strong>About:</strong> {{story.who_are_you}}</p>
                <p><strong>Their work:</strong> {{story.what_do_you_do}}</p>
                <p><strong>How can they help:</strong> {{story.how_can_you_help_me}}</p>
                {% if story.web_page %}
                  <p><a href="{{ story.web_page }}" target="_blank">Website</a></p>
                {% endif %}
                <p><a href="{{ story.papers_link }}" target="_blank">DBLP</a></p>
                {% if story.html_file %}
                  <p><a href="{{ story.html_file }}" target="_blank">Research Papers In Our Website</a></p>
                {% endif %}
              </div>
              <button onclick="toggleDetails(this)" style="background-color: #CC0000; color: #ffffff;">Show More</button>
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
</script> -->

<!-- <div>
  <span>_services\researchers.md</span>
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
                <p><a href="{{ story.papers_link }}" target="_blank">DBLP</a></p>
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

 -->
