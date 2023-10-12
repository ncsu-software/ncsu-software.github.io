---
title: "Success Stories"
date: 2018-12-28T15:14:39+10:00
weight: 1
about: Where are our previous students now
---
<style>
.success-stories {
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.story-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.story {
  margin-bottom: 20px;
}

.story-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.story-image {
  width: 200px;
  height: 200px;
  object-fit: cover;
  margin-right: 20px;
}

.story-content {
  flex: 1;
  margin-left: 20px;
  margin-right: 200px;
  padding:
</style>
<section class="success-stories">
  <h2>Success Stories</h2>
  <ul class="story-list">
    {% for story in site.data.researchers.sheets.SuccessStories %}
      <li class="story">
        <div class="story-container">
          <img src="{{ story.image | relative_url | replace: 'open?id=', 'uc?export=download&id=' }}" alt="{{ story.name }}" class="story-image" />
          <div class="story-content">
            <h3 class="story-title">{{ story.name }}</h3>
            <p class="story-description"><strong>What they are doing now:</strong> {{ story.current_work }}</p>
            {% if story.web_page %}
              <p class="story-link"><a href="{{ story.web_page }}" target="_blank">Website</a></p>
            {% endif %}
            <p class="story-link"><a href="{{ story.papers_link }}" target="_blank">Research Papers Link</a></p>
          </div>
        </div>
      </li>
    {% endfor %}
  </ul>
</section>