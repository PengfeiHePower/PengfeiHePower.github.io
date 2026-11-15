---
layout: page
title: TRAJECT-Bench
description: A trajectory-aware benchmark for evaluating agentic tool use of LLMs (ICLR 2026).
img: assets/img/projects/traject-bench.png
importance: 1
category: research
---

<a href="https://github.com/PengfeiHePower/TRAJECT-Bench" class="btn btn-sm z-depth-0 border" role="button"><i class="fab fa-github"></i> Code</a>
<a href="https://huggingface.co/datasets/bigboss24/TRAJECT-Bench" class="btn btn-sm z-depth-0 border" role="button">🤗 Dataset</a>
<a href="https://arxiv.org/abs/2510.04550" class="btn btn-sm z-depth-0 border" role="button"><i class="ai ai-arxiv"></i> Paper</a>

TRAJECT-Bench evaluates how well LLMs use tools, looking beyond final-answer accuracy to the whole tool-calling trajectory: whether the right tools are selected, parameterized correctly, and called in the right order.

- A high-fidelity, executable, production-style tool set spanning multiple practical domains.
- Tasks driven by real-world task types, with trajectories that involve 3 to 10 tools, in both parallel and sequential forms.
- Simple and hard versions of each query, so performance can be analyzed as task complexity grows.
- Evaluation scripts for both direct LLM prompting and agentic methods (ReAct), with static and dynamic tool retrieval.
