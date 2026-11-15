---
layout: page
title: PEAR
description: Planner-Executor Agent Robustness benchmark for security vulnerabilities in LLM multi-agent systems (EACL 2026).
img: assets/img/projects/pear.png
importance: 2
category: research
---

<div class="project-page" markdown="1">

<div class="project-links">
  <a href="https://github.com/MingxuanZhangPurdue/multiagent-vulnerable" class="btn btn-sm z-depth-0" role="button"><i class="fab fa-github"></i> Code</a>
  <a href="https://arxiv.org/abs/2510.07505" class="btn btn-sm z-depth-0" role="button"><i class="ai ai-arxiv"></i> Paper</a>
  <br>
  <img src="https://img.shields.io/badge/EACL-2026-c0392b" alt="EACL 2026">
  <img src="https://img.shields.io/github/stars/MingxuanZhangPurdue/multiagent-vulnerable?style=flat&logo=github&color=yellow" alt="GitHub stars">
  <img src="https://img.shields.io/badge/arXiv-2510.07505-b31b1b" alt="arXiv">
</div>

<div class="tldr">
<strong>TL;DR</strong> &mdash; Planner-executor multi-agent systems get a lot done, and they are easy to hijack. PEAR measures both sides at once: how useful the system is, and how often an attacker can make it do harm.
</div>

<div class="stat-grid">
  <div class="stat"><span class="number">4</span><span class="label">scenarios</span></div>
  <div class="stat"><span class="number">84</span><span class="label">user tasks</span></div>
  <div class="stat"><span class="number">120</span><span class="label">base attack tasks</span></div>
  <div class="stat"><span class="number">1,680</span><span class="label">attacked user tasks</span></div>
</div>

## The setup

A planner agent breaks the user's request into steps, and an executor agent carries them out with tools. This planner-executor design is practical and widely adopted, which makes its security worth studying. PEAR injects attacks into different parts of the system and checks, task by task, whether the malicious goal was achieved.

<figure class="project-figure">
  <img src="/assets/img/projects/pear.png" alt="Overview of PEAR" data-zoomable>
  <figcaption>Overview of PEAR. Center: the planner-executor system with example user tasks. Left: the attack tasks, with red arrows marking where attacks are injected. Right: utility, attack success, and efficiency metrics.</figcaption>
</figure>

## Three kinds of harm

<div class="feature-grid">
  <div class="feature"><div class="icon">💣</div><h4>Harmful actions</h4><p>Trick the system into unauthorized operations, such as taking over a user's bank account by changing the password.</p></div>
  <div class="feature"><div class="icon">🔓</div><h4>Privacy leakage</h4><p>Exfiltrate personal information, private Slack channels, or travel reservations.</p></div>
  <div class="feature"><div class="icon">🔋</div><h4>Resource exhaustion</h4><p>Burn compute and money, for example by flooding the calendar with entries or firing off a massive number of tiny transactions.</p></div>
</div>

## Key findings

<div class="finding"><div class="num">1</div><p><strong>The planner matters most.</strong> A weak planner hurts clean-task performance far more than a weak executor.</p></div>
<div class="finding"><div class="num">2</div><p><strong>Memory helps the planner, not the executor.</strong> Adding memory to the planner substantially improves performance; adding it to the executor barely changes anything.</p></div>
<div class="finding"><div class="num">3</div><p><strong>Utility and robustness trade off.</strong> Configurations with higher utility often show higher attack success rates.</p></div>
<div class="finding"><div class="num">4</div><p><strong>Attacking the planner is especially effective.</strong> Its decisions flow downstream into everything the executor does.</p></div>

<figure class="project-figure">
  <img src="/assets/img/projects/pear-utility.png" alt="Utility across planner-executor configurations" data-zoomable>
  <figcaption>Utility across planner/executor pairs from the Claude, DeepSeek, GPT, and Gemini families. Most settings reach about 65% or higher; pairings with a weak planner (red labels) drop sharply.</figcaption>
</figure>

<div class="figure-row">
  <figure class="project-figure">
    <img src="/assets/img/projects/pear-harmful-tradeoff.png" alt="Utility vs. harmful attack success rate" data-zoomable>
    <figcaption>Utility vs. attack success rate for harmful-action attacks.</figcaption>
  </figure>
  <figure class="project-figure">
    <img src="/assets/img/projects/pear-privacy-tradeoff.png" alt="Utility vs. privacy attack success rate" data-zoomable>
    <figcaption>The same for privacy-leakage attacks. Every configuration sits above the diagonal.</figcaption>
  </figure>
</div>

## Citation

```bibtex
@inproceedings{dong2026pear,
  title     = {PEAR: Planner-Executor Agent Robustness Benchmark},
  author    = {Dong, Shen and Zhang, Mingxuan and He, Pengfei and Ma, Li and
               Thuraisingham, Bhavani and Liu, Hui and Xing, Yue},
  booktitle = {Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
  year      = {2026}
}
```

</div>
