---
layout: page
title: Stock-helper
description: A multi-agent assistant for US equity investors that delivers market briefs and real-time alerts.
img: assets/img/projects/stock-helper.svg
importance: 2
category: side projects
---

<div class="project-page" markdown="1">

<figure class="project-hero"><img src="/assets/img/projects/stock-helper.svg" alt="Stock-helper"></figure>

<div class="project-links">
  <a href="https://github.com/PengfeiHePower/Stock-helper" class="btn btn-sm z-depth-0" role="button"><i class="fab fa-github"></i> Code</a>
  <br>
  <img src="https://img.shields.io/badge/python-3.12%2B-3776ab?logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/LangGraph-multi--agent-1c3c3c" alt="LangGraph">
  <img src="https://img.shields.io/badge/Telegram%20%7C%20Email-delivery-26a5e4?logo=telegram&logoColor=white" alt="Telegram and email">
</div>

<div class="tldr">
<strong>TL;DR</strong> &mdash; Meet <strong>Moka-chan</strong>, a team of LLM agents that reads the market news so I don't have to. She sends a brief before the open, a recap after the close, and a review every Friday, and pings me when something on my watchlist moves.
</div>

<div class="stat-grid">
  <div class="stat"><span class="number">3</span><span class="label">scheduled briefs: morning, close, weekly</span></div>
  <div class="stat"><span class="number">8</span><span class="label">layer CIO decision pipeline</span></div>
  <div class="stat"><span class="number">30+</span><span class="label">industries tracked</span></div>
  <div class="stat"><span class="number">中 / EN</span><span class="label">bilingual reports</span></div>
</div>

## The agent pipeline

Every brief runs through a LangGraph pipeline of specialized agents:

<div class="flow">
  <span class="step">🌍 Macro</span><span class="arrow">→</span>
  <span class="step">🏭 Sectors</span><span class="arrow">→</span>
  <span class="step">📊 Stocks</span><span class="arrow">→</span>
  <span class="step">🔍 Agent picks</span><span class="arrow">→</span>
  <span class="step">⚠️ Risk</span>
</div>

The final brief is assembled in code in a fixed order, so it is never truncated by the LLM and always has the same structure.

## A trading day with Moka-chan

<div class="feature-grid">
  <div class="feature"><div class="icon">🌅</div><h4>7:00 ET &middot; Morning brief</h4><p>Pre-market snapshot, macro backdrop, sectors and stocks to watch, watchlist earnings, and star IPOs.</p></div>
  <div class="feature"><div class="icon">🔔</div><h4>All day &middot; Real-time alerts</h4><p>Telegram pings for SEC filings, material headlines, and watchlist price moves.</p></div>
  <div class="feature"><div class="icon">🌆</div><h4>16:45 ET &middot; Close brief</h4><p>Closing recap with a <em>Morning vs. Reality</em> section comparing the morning outlook with what actually happened.</p></div>
  <div class="feature"><div class="icon">📅</div><h4>Friday &middot; Weekly review</h4><p>Macro and tracking trends, sector rotation, and next week's earnings.</p></div>
</div>

## Thinking long term

Beyond daily briefs, a **Market Reasoning Agent** writes monthly and biweekly reports that track hypotheses (hold, weaken, invalidated) with evidence scores. A **CIO Investment Agent** then turns the analysis into an allocation view through an eight-layer pipeline:

<div class="flow">
  <span class="step">Regime</span><span class="arrow">→</span>
  <span class="step">Theme</span><span class="arrow">→</span>
  <span class="step">Industry</span><span class="arrow">→</span>
  <span class="step">Stock</span><span class="arrow">→</span>
  <span class="step">Portfolio</span><span class="arrow">→</span>
  <span class="step">Scenario</span><span class="arrow">→</span>
  <span class="step">Triggers</span><span class="arrow">→</span>
  <span class="step">Monitor</span>
</div>

Each layer follows an *evidence → hypothesis → counter-argument → decision* pattern.

## Under the hood

Data comes from Finnhub (news, quotes, earnings and IPO calendars), SEC EDGAR filings, and FRED macro series. Models are routed by cost: Gemini Flash-Lite classifies news, and Claude Sonnet writes the analysis, with a per-run budget tracker. Briefs go out through Telegram and HTML email, and Moka-chan also chats in Chinese or English with persistent memory.

</div>
