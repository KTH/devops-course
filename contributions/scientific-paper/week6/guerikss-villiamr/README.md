# Assignment Proposal

## Title

Robbery on DevOps: How hackers abuse CI pipelines for crypto-mining

## Names and KTH ID

  - Harry Eriksson (guerikss@kth.se)
  - Villiam Riegler (villiamr@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

The paper selected was published at the 43rd IEEE Symposium on Security and Privacy (IEEE S&P / Oakland 2022): https://ieeexplore.ieee.org/document/9833803.

Continuous Integration (CI) platforms such as GitHub Actions, Travis CI and GitLab CI give developers free, resource-rich compute to build and test their code. That same free compute is an attractive target for abuse: attackers smuggle cryptominers into CI jobs — a practice the authors call **Cijacking** — and let the platform pay for their mining. Because legitimate CI work (compiling, building container images, running test suites) is itself compute-intensive, illicit mining blends in and is far harder to spot than in-browser cryptojacking. The paper is a systematic measurement and detection study of Cijacking across 11 mainstream CI platforms.

During the presentation we plan to focus on how the attack works, how it is detected, and what the measurements mean in practice, and what this threat means for you as a developer.

**Relevance**

CI/CD platforms are core DevOps infrastructure, and this paper examines the security of that infrastructure from an angle most pipelines ignore: resource abuse of the pipeline itself. Where much of DevSecOps focuses on the integrity of what a pipeline *produces*, Cijacking exploits what a pipeline *provides* — free, trusted compute — turning a productivity feature into an attack surface and imposing real cost on providers offering free tiers. Understanding this abuse, the trade-offs of detecting it, and how attackers adapt to defenses is directly relevant to anyone operating, or offering, automated CI/CD services as well as developers who might get public repositories cijacked unknowingly.
