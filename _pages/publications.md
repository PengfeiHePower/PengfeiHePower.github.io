---
layout: page
permalink: /Publications/
title: Publications
years: [2026, 2025, 2024, 2023, 2022]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->
<div class="publications">

{%- if site.data.citations.citations %}
<p class="text-center">
  <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}"><i class="ai ai-google-scholar"></i> Google Scholar</a>:
  {{ site.data.citations.citations }} citations · h-index {{ site.data.citations.h_index }}
</p>
{%- endif %}

<h1>Publications</h1>
{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f {{ site.scholar.bibliography }} -q @inproceedings[year={{y}}]* %}
  {% bibliography -f {{ site.scholar.bibliography }} -q @article[year={{y}}]* %}
{% endfor %}

<h1>Preprints</h1>
{% bibliography -f {{ site.scholar.bibliography }} -q @misc* %}

</div>
