# Assignment Proposal

## Title

LastPyMile: Identifying the Discrepancy between Sources and Packages

## Names and KTH ID

- Alexandru Gânju (ganju@kth.se)
- Georgi Tsonchev Hristov (georgith@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

We propose to present ["LastPyMile: Identifying the Discrepancy between Sources and Packages"](https://doi.org/10.1145/3468264.3468592) by Duc-Ly Vu et al., published in ESEC/FSE 2021.

Developers review a dependency's source code on GitHub, but install the pre-built package from PyPI, assuming the two match. Attackers can exploit this "last mile" by injecting malicious code only into the published package, as in the ssh-decorate and jeIlyfish attacks. LastPyMile hashes every file and line in the source repository's full history and compares them with the package, reporting "phantom" files and lines that never appeared in the source. Existing malware scanners then only need to check those phantoms. Across 2,438 popular PyPI packages, the authors show that differences between source and package are common but rarely in Python code, and that LastPyMile reduces scanner alerts on benign packages to zero while keeping the alerts on malicious ones.

Our presentation will do the following:

- Describe the gap between source code and published packages
- Explain the LastPyMile algorithm in detail and how it filters the input of existing scanners.
- Present the results of the paper.
- Discuss the limitations of the paper, such as its full trust in the source repository.
- Compare with three papers, prel. [Amalfi](https://doi.org/10.1145/3510003.3510104) by Adriana Sejfia and Max Schäfer (detecting malicious packages with machine learning), ["An Empirical Study on Reproducible Packaging in Open-Source Ecosystems"](https://doi.org/10.1109/ICSE55347.2025.00136) by Giacomo Benedetti et al. (reproducible builds).
- Discuss when the approach is useful and for whom, e.g. registry administrators and security teams vetting dependencies.

**Relevance**

The paper is relevant to dependency management and DevSecOps, since every CI/CD pipeline installs third-party packages, and the code that runs is the published package, not the reviewed source. LastPyMile shows how automated checks can verify the build-and-publish step of the software supply chain without overwhelming reviewers with false alarms.
