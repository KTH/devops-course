# Assignment Proposal

## Title

When AIOps Become "AI Oops": Subverting LLM-driven IT Operations via Telemetry Manipulation

## Names and KTH ID

  - Cesar Aceves Hernández (cesarah@kth.se)
  - Derfesh Mariush (derfesh@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

Modern IT operations increasingly use LLM-based AIOps agents to analyze telemetry, diagnose incidents, and suggest or execute remediation. This creates a new security problem because the telemetry that guides the agent can be influenced by an attacker and may cause the agent to make harmful decisions.

The paper we have chosen to present, “When AIOps Become “AI Oops”: Subverting LLM-driven IT Operations via Telemetry Manipulation”, presents an approach for studying and exploiting this attack surface in AIOps systems. Instead of relying on direct prompt injection, the paper introduces AIOpsDoom, an automated attack framework that uses reconnaissance, crawling, and fuzzing to inject attacker-controlled content into logs, metrics, or traces. The injected content is then crafted as adversarial reward-hacking, making a malicious remediation appear to be a plausible solution to the incident. The paper also proposes AIOpsShield, a defense that identifies untrusted telemetry during a setup phase and sanitizes it before it reaches the AIOps agent.

During the presentation we cover the problem of securing LLM-driven AIOps, explain the AIOpsDoom attack workflow and AIOpsShield defense in detail, and discuss the evaluation. We also critically evaluate the assumptions and limitations of the approach with related approaches and reflect on when telemetry sanitization is useful, when it may be insufficient, and who should rely on it.
