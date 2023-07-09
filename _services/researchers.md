---
title: "For Researchers"
date: 2018-12-28T15:14:39+10:00
weight: 4
about: Future of Software Engineering through Advanced Research & innovation!
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
<script>
  function onLoad(){
    const urlParams = new URLSearchParams(window.location.search);
    const email = urlParams.get('email');
    console.log("Onload researchers")
    localStorage.removeItem("email")
  }
</script>

<div onLoad="onLoad()">
<script type="text/javascript">
onLoad();
</script>
  <ul style="list-style-type: none;">
    {% for story in site.data.researchers.sheets.ResearchersResponses %}
      <li style="margin-bottom: 20px;">
        <div style="background-color: #f5f5f5; border-radius: 10px; padding: 10px; overflow: hidden; display: flex;">
          {% if story.ProfilePicture %}
            <div style="margin-right: 20px;">
              <img src="{{ story.ProfilePicture | replace: 'open?id=', 'uc?export=download&id=' }}" alt="{{ story.TitleAndName }}" style="max-width: 200px; height: auto;">
            </div>
          {% endif %}
          <div class="row-content">
            {% if story.YourPersonalWebsiteLink %}
            <a href="{{ story.YourPersonalWebsiteLink }}" target="_blank"><h2>{{ story.Name }}</h2></a>
            {% endif %}
            <h4>{{ story.Title }}</h4>
            <!-- {% if story.MissionOrMantra %}
            <p><strong>Mantra/Mission: </strong>{{ story.MissionOrMantra }}</p>
            {% endif %} -->
            {% if story.LabName %}
            <p><strong>Lab Name: </strong>{{ story.LabName }}</p>
            {% endif %}
            {% if story.CoreResearchAreas %}
              <p><strong>Core Research Areas: </strong>{{ story.CoreResearchAreas }}</p>
            {% endif %}
            <div class="inline-content">
     {% assign employment = {{story.EmailAddress}} %}
        <p><a href="researchPapers?email={{ employment }}" >Research Papers</a></p>
        <!-- <p><a href="{{ story.DBLPPapers }}" >Research Papers</a></p> -->
    {% assign employment = {{story.EmailAddress}} %}
        <p><a href="grantsPage?email={{ employment }}" >Grants</a></p>
        <!-- <p><a href="{{ story.Grants }}">Grants</a></p> -->
        {% assign employment = {{story.EmailAddress}} %}
        <p><a href="newsPage?email={{ employment }}" >News</a></p>
        <!-- <p><a href="{{ story.News }}">News</a></p> -->
        {% assign employment = {{story.EmailAddress}} %}
        <p><a href="employmentPage?email={{ employment }}" >Employment Opportunity</a></p>
        {% assign employment = {{story.EmailAddress}} %}
        <p><a href="labPage?email={{ employment }}" >Lab Page</a></p>
        <!-- <p><a href="{{ story.Labs }}">Labs</a></p> -->
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



