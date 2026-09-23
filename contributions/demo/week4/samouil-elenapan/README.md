
# Assignment Proposal

## Title

LLMOps evaluation and quality gate pipeline

## Names and KTH ID

  - Elena Pan (elenapan@kth.se)
  - Samouil Mosios (samouil@kth.se)

## Deadline

Week 4

## Category

Demo

## Description

We demonstrate a minimal LLMOps pipeline that extends a traditional CI/CD workflow with automated evaluation of an LLM-powered feature. A small application built around an LLM prompt is evaluated using [DeepEval](https://github.com/confident-ai/deepeval) test cases (e.g. answer relevancy, faithfulness, hallucination) as part of the CI stage. If the evaluation scores fall below a defined threshold, the pipeline fails and blocks deployment, turning the evaluation into an automated quality gate.

In the demo we will:
- Run the evaluation suite against a working prompt/model and show the pipeline passing and proceeding to deployment.
- Introduce a regression (e.g. a worse prompt or model) and show DeepEval catching it, causing the pipeline to fail and block deployment.
- Briefly discuss the metrics and thresholds used, and how this approach generalizes to regression testing for other LLM-based features.

**Relevance**

LLMs are increasingly embedded into production software, but their outputs are non-deterministic and sensitive to prompt, model, and data changes, so shipping them without automated evaluation risks silently degraded behavior reaching users. Treating LLM evaluation as an automated, versioned quality gate in CI/CD extends established DevOps practices, continuous testing, fast feedback, and reliable, gated releases, to AI-powered features, and is directly applicable to any pipeline that deploys LLM-dependent code.