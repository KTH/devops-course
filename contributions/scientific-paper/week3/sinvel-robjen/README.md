# Assignment Proposal

## Title

Moving Faster and Reducing Risk: Using LLMs in Release Deployment

## Names and KTH ID

  - Singvalliyappa Velayutham (sinvel@kth.se)
  - Robert Jenson (robjen@kth.se)

## Deadline

- Week 3

## Category

- Scientific paper

## Description

The paper selected came out of Meta and was published at ICSE 2025 (arXiv:2410.06351)

At sufficient scale, a release engineering team can no longer decide what is safe to ship, and the tradition was to go through code freezes during important days. This paper shows how Meta replaced the code freeze with a per change quality gate. They build a Diff Risk Score (DRS) that predicts how likely an individual code change is to cause a SEV, Meta's term for a production incident affecting end users. Changes scoring above a threshold are blocked from merging, and the author must either wait for the freeze window to end or go through an escalation process. The threshold itself can be tuned to how much risk the platform can absorb on a given day.

The authors compare a production logistic regression baseline built on roughly a dozen hand engineered features against two generative LLMs, evaluated on 181,052 real changes containing 305 SEVs. A smaller 13B model pre trained on diffs outperforms a 34B model pre trained on meta's code, with both fine tuned on risk labels suggesting that diff-aware pre training matters more than parameter count for this task.

During our presentation we aim to explain how the gating mechanism works, cover the technique used to extract a rankable risk score from a generative model, present the results, and discuss the follow up work at Meta on making these predictions explainable.



**Relevance**

What makes it interesting for this course is that the merge gate is probabilistic (the same diff can merge and not merge depending on the day) and content aware rather than a deterministic rule such as tests passed and its gating is a function of operational context rather than of the code alone. 
This paper's contribution is to develop a mechanism in the CD pipeline that can flag high risk code changes while maintaining productivity within the codebase. 