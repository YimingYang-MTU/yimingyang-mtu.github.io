---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D. in Electrical and Computer Engineering, 2021 - Spring/Summer 2026 (expected)
* M.S. in Automation Engineering, Chang'an University, 2017 - 2020
* B.S. in in Control Science and Engineering, Chang'an University, 2013 - 2017
  
Skills
======
* Laguages: Python, C++
* Softwares: Matlab, Simulink
* Hardware: MicroAutoBox

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
