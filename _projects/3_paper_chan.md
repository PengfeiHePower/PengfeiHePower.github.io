---
layout: page
title: Paper-chan
description: A personal research assistant that sends daily paper digests and answers questions on Telegram.
img: assets/img/projects/cover-paper.svg
venue: Side project
topics: [LLM assistant, Telegram, arXiv]
importance: 2
category: side projects
---

<div class="project-page" markdown="1">

<figure class="project-hero"><img src="/assets/img/projects/cover-paper.svg" alt="{{ page.title }}"></figure>

<div class="project-links">
  <a href="https://github.com/PengfeiHePower/paper-chan" class="btn btn-sm z-depth-0" role="button"><i class="fab fa-github"></i> Code</a>
  <br>
  <img src="https://img.shields.io/badge/python-3.12%2B-3776ab?logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/Telegram-bot-26a5e4?logo=telegram&logoColor=white" alt="Telegram bot">
  <img src="https://img.shields.io/badge/LLM-OpenAI%20%7C%20Anthropic-555" alt="OpenAI or Anthropic">
</div>

<div class="tldr">
<strong>TL;DR</strong> &mdash; Too many new papers, not enough mornings. Paper-chan reads arXiv for me every day, sends a digest of what is worth my time, and answers follow-up questions right in Telegram.
</div>

## How it works

<div class="flow">
  <span class="step">📥 arXiv · Semantic Scholar · RSS · YouTube</span><span class="arrow">→</span>
  <span class="step">🎯 Match my topics &amp; followed authors</span><span class="arrow">→</span>
  <span class="step">🧠 LLM summaries &amp; top picks</span><span class="arrow">→</span>
  <span class="step">💬 Telegram</span>
</div>

## Features

<div class="feature-grid">
  <div class="feature"><div class="icon">☀️</div><h4>Daily digest</h4><p>A morning summary of new papers on my topics, with top picks, a dedicated surveys &amp; benchmarks section, and source links.</p></div>
  <div class="feature"><div class="icon">🎙️</div><h4>Content discovery</h4><p>New blog posts, talks, and podcasts from curated RSS feeds and YouTube channels.</p></div>
  <div class="feature"><div class="icon">👀</div><h4>Author alerts</h4><p>Follow researchers and get notified when they post new papers.</p></div>
  <div class="feature"><div class="icon">📖</div><h4>Deep reading</h4><p>Ask it to read a paper in depth, compare two papers side by side, or find the code repository.</p></div>
  <div class="feature"><div class="icon">🔖</div><h4>Reading list</h4><p>Save, tag, and track papers I have read or want to read.</p></div>
  <div class="feature"><div class="icon">🌏</div><h4>Chat in Chinese or English</h4><p>Natural-language requests like 「仔细阅读 2401.xxxxx」 or 「比较 A 和 B」 work alongside slash commands.</p></div>
</div>

## Commands

| Command | What it does |
|---|---|
| `/digest` | Today's paper digest on demand |
| `/search <query>` | Search arXiv and Semantic Scholar |
| `/save <arxiv_id>` · `/list` | Manage the reading list |
| `/discover` | Latest blogs and talks |
| `/watch <name>` · `/authors` | Follow authors and see their new papers |
| `/ask <question>` | Ask about saved papers or a topic |

## Under the hood

A deliberately lightweight Python app with no agent framework: a custom intent router and skills on top of direct OpenAI or Anthropic API calls, `python-telegram-bot` for chat, SQLite for storage, and a scheduler that runs the bot around the clock and sends the digest at a fixed time each morning.

</div>
