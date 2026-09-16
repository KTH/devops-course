# Assignment Proposal

## Title

Automated LLM Security Testing with Garak

## Names and KTH ID

  - Nalin Kundu (nvkundu@kth.se)
  - Kristers Krigers (krigers@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

We will build an executable tutorial that shows how to use Garak ([a tool that scans for LLM vulnerabilities](https://garak.ai/)) to test an LLM application for prompt injection before a change is released. The reader starts with a small chatbot that is intentionally vulnerable, runs a focused security scan, and looks at the report to see how the attack succeeds. They then apply a simple mitigation, run the same scan again, and compare the results. The tutorial ends by an example of the scan being used as a CI check that blocks a change when the security test fails.

**Relevance**

LLM applications can have security problems that normal unit tests do not catch. Prompt injection can make a chatbot follow untrusted instructions instead of the rules it was given, which can lead to unsafe or unintended behaviour. Garak makes these problems testable with repeatable security probes and reports. This lets teams treat LLM security checks like other DevSecOps quality gates and run them automatically before changes are merged.
