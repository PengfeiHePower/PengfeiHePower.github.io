---
layout: page
title: Projects
permalink: /projects/
description: Benchmarks, frameworks, and tools I have built.
nav: true
nav_order: 2
display_categories: [research, side projects]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
{%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
{% endfor %}
</div>
