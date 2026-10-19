# Assignment Proposal

## Title

An Empirical Study on Reproducible Packaging in Open-Source Ecosystems

## Names and KTH ID

- Alexander Forslund (alforslu@kth.se)
- Albin Wallenius Woxnerud (alww@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

We propose to present ["An Empirical Study on Reproducible Packaging in Open-Source Ecosystems"](https://conf.researchr.org/details/icse-2025/icse-2025-research-track/104/An-Empirical-Study-on-Reproducible-Packaging-in-Open-Source-Ecosystems) by Giacomo Benedetti et al. published in ICSE 2025.

The software packages that are used in CI/CD pipelines may differ from their public source code. So called reproducible builds exist to detect such discrepancies, for example through bitwise-identical artifacts from the same source and build environment. However, the authors believe reproducible builds can be considered a difficult task, due to societal and technical reasons. The paper investigates six package ecosystems (npm, Maven, PyPI, Go, RubyGems, and Cargo), and finds that many reproducibility problems originate within the packaging tools. They conclude that the ecosystems can make nearly all tested packages reproducible by applying the suggestions of the authors, and that doing so will prevent future supply chain attacks.

Our presentation will do the following:

- Describe the issues with using non-reproducible builds, and what the security risks are.
- Explain how reproducible builds work, and how the rate of success can be improved using the method in the paper.
- Present the results of the paper
- Discuss the issues with the paper, such as the exclusion of failed builds.
- Compare with two papers, prel. [in-toto](https://www.usenix.org/system/files/sec19-torres-arias.pdf) by Santiago Torres-Arias et al. and [Speranza](https://dl.acm.org/doi/10.1145/3576915.3623200) by Kelsey Merrill et al.
- Discuss the implications for maintainers, including why reproducibility cannot detect already present malicious code.

**Relevance**

The paper is relevant to dependency management and DevSecOps, since automated pipelines rely on externally distributed packages, making the integrity of this process crucial for downstream scurity. These external packages might not be the exact same as their source code counterpart, and it should be part of any good CI/CD pipeline to build verification into the release and dependency workflows, to make it more difficult for a malicious user to compromise software.
