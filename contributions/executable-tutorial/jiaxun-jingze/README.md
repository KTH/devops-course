# Assignment Proposal

## Title

Prompt regression testing for LLM applications (LLMOps)

## Names and KTH ID

  - Jiaxun Wei (jiaxun@kth.se)
  - Jingze Guo (jingze@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

We want to write a Google Colab notebook that shows how to keep an LLM application stable when its prompt or its model changes. The reader writes a promptfoo configuration with test cases and assertions, runs it against a small instruction-tuned model that is loaded locally in the notebook. The reader then breaks the prompt on purpose, watches the assertions fail, and finally wires the evaluation into a pipeline, so that a failed evaluation blocks the change.

**Relevance**

An LLM application is defined as much by its prompts and its model version as by its code, and both change often. Without evaluation, a reworded prompt or a model upgrade can silently degrade behaviour, which is the LLMOps version of a regression. The tutorial makes that behaviour testable and automated, so that changes to a model-driven system get the same review discipline as changes to code.
