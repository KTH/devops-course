# Assignment Proposal

## Title

We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs

## Names and KTH ID

- Ettore Mugisha Cirillo (emcir@kth.se)
- Lorenzo Deflorian (ldef@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

We propose to present [this paper by Joseph Spracklen et al.](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen), published in the main proceedings of the 34th USENIX Security Symposium (2025).

The paper studies package hallucinations: cases where large language models (LLMs) recommend software packages that do not exist. An attacker could register a repeatedly suggested name and distribute a malicious package to developers who trust the recommendation. The authors investigate this risk in Python and JavaScript and evaluate mitigation strategies.

Our presentation will introduce the problem through a simple example, then cover the approach, selected results, and practical implications. We will:

- Explain the detection methodology in detail: how the authors obtain package names using three heuristics, check them against PyPI and npm package lists, and calculate hallucination rates.
- Discuss selected findings on prevalence and repeated hallucinations, together with mitigation trade-offs.
- Critically examine the measurement assumptions and the applicability of the results beyond the tested models and prompts, distinguishing hallucination rates from successful attacks.
- Compare the study with at least two related research papers not included in its bibliography.
- Reflect on the usefulness and limitations of the findings for developers and teams managing dependencies in AI-assisted workflows.

**Relevance**

The paper directly connects dependency management and DevSecOps, the topics of Week 6. AI-generated package recommendations can influence which dependencies enter a project and its build pipeline. Understanding this risk helps teams assess dependency checks and the limits of trusting package availability as evidence of safety.
