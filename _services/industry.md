---
title: "For Industry"
date: 2018-12-28T15:14:39+10:00
weight: 2
about: Ask us how to innovate on time, on budget.
eyebrow: "Industry partnerships"
heading: "Innovate on time, on budget"
lead: "We work with industry all the time, turning hard software problems into research that ships."
---

<section class="section section-compact">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Ways to work with us</p>
      <h2>Bring us a hard problem</h2>
    </div>
    <div class="engage-grid">
      <div class="engage-card">
        <span class="engage-index">01</span>
        <h3>Sponsored research</h3>
        <p>Fund a project on a problem that matters to your team, and work alongside our faculty and students to solve it.</p>
      </div>
      <div class="engage-card">
        <span class="engage-index">02</span>
        <h3>Collaborate</h3>
        <p>Share data, tools or case studies. Our research themes span AI and SE, testing, analytics and human factors.</p>
      </div>
      <div class="engage-card">
        <span class="engage-index">03</span>
        <h3>Recruit</h3>
        <p>Meet graduate students trained in modern software engineering research, and host them as interns.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-tinted section-compact">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Partners</p>
      <h2>Who we have worked with</h2>
    </div>
    <div class="partners">
      {% assign partners = "csiro.jpeg,grammatech.png,ibm.png,lexisnexis.png,msoft.png,nasa.png" | split: "," %}
      {% for logo in partners %}
      <div class="partner"><img src="{{ '/images/logo/' | append: logo | relative_url }}" alt="{{ logo | split: '.' | first }} logo" loading="lazy" /></div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div class="cta-inner">
      <h2>Ask us how.</h2>
      <div class="cta-actions">
        <a class="button button-light" href="{{ '/people/' | relative_url }}">Find an expert</a>
        <a class="button button-ghost" href="{{ '/contact/' | relative_url }}">Contact us</a>
      </div>
    </div>
  </div>
</section>
