# Assignment Proposal

## Title

A Large-Scale Evaluation for Log Parsing Techniques: How Far Are We?

## Names and KTH ID

  - Tomás Brito (tmldjb@kth.se)
  - Padmalaya Moharana (moharana@kth.se)

## Deadline

Week 7

## Category

Scientific paper

## Description

We will present "A Large-Scale Evaluation for Log Parsing Techniques: How Far Are We?" by Zhihan Jiang, Jinyang Liu, Junjie Huang, Yichen Li, Yintong Huo, Jiazhen Gu, Zhuangbin Chen, Jieming Zhu and Michael R. Lyu, published in the technical track of ISSTA 2024 (https://dl.acm.org/doi/10.1145/3650212.3652123).

Monitoring starts with logs, but a log line is only text. Before anything can be counted, alerted on or fed to an anomaly detector, a parser has to split each line into the fixed template and the variable parts. The paper asks how good the parsers in use today really are. The authors argue that the benchmarks everyone reports on are too small, with 2000 lines per system, so they build Loghub-2.0, fourteen annotated datasets averaging 3.6 million lines each, propose metrics that are not dominated by the few templates that generate most of the lines, and re-evaluate 15 parsers on them.

In the presentation we will:

- explain how Drain, the parser most widely used in practice, groups log lines with a fixed depth parse tree, worked through on a small example
- show the results: accuracy falls once the datasets are realistic, and the templates the parsers get wrong are the rare ones, which are exactly the ones that show up during an incident
- cover the efficiency numbers, since a parser that cannot keep up with the log volume is not usable in production
- critique the study: fourteen systems is still a narrow sample, the ground truth is built semi automatically, and the proposed metrics are themselves a judgement call
- contrast it with two LLM based parsers that came out after this evaluation and are not in its bibliography, LogBatcher (ASE 2024) and LogParser-LLM (KDD 2024), and discuss when their extra cost is worth paying

**Relevance**

Observability is where a lot of DevOps tooling goes, and all of it sits on a parsing step nobody looks at until it breaks. What the paper shows is that the numbers these tools are judged by come from benchmarks far smaller than the workloads they meet in production, which is a fair question to ask about any component a pipeline depends on.
