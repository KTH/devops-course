# Assignment Proposal

## Title

Recognizing and Addressing the Risk Behind Open Source Dependencies

## Names and KTH ID

  - Minh Allan Dao (madao@kth.se)

## Deadline

- Task 2: Monday, April 24 @ 17h Stockholm Time

## Category

- Essay

## Description

With events such as the panic ensuing from the Log4j vulnerability, the spotlight has continued to focus on on the usage and often the dependency on open source work. With many dependencies maintained by small teams stretched thin, estimates that security flaws often may take 4-6 months to address, and the continual release of new features to meet demand without the addressing of current flaws and tech debt, there are countless reasons why open source dependencies used either directly or integrated into other packages and modules used in enterprise code and beyond may be vulnerable.

Although more automation is increasingly available to identify static errors and offer upgrade recommendations, dynamic dynamic platforms such as Java can load new code at runtime, which is an alternative way for bad actors to still run their malicious code. This is of particular interest due to heightened complexity. Of course, strategies such as organizational policy and monitoring are helpful, but we may focus in particular on dynamic analysis through a safe environment called a sandbox.

**Relevance**

From a DevOps perspective, we should be motivated find a way to automate as much as we can when it comes to open source dependency management, so that we can minimize the vulnerabilities possible. It is important to both be aware of what is vulnerable and address, so tooling and a culture of (automatically) examining and documenting open source work used in projects and pipelines is key. 

For example, a DevOps teams may opt to configure their VMSS via an image derived from the Github Actions public repository, which can be updated by anyone, anytime. Now the team would need to monitor both the pipelines they have configured and the VMSS agents that act on those pipelines, creating multiple layers of dependencies present. A project may not use all of the packages that such public images (such as the ones via Github Actions) include, as they are naturally not tailored to a particular project. This introduces vulnerability in the sense that there are unused dependencies that may always potentially become a risk in the future. In turn, the tackling of bloat is a key measure in reducing dynamic risk, as there are less variables at play. 

Finally, all of these recommendations augment a clean and clear environment to do dynamic testing. A tool of particular interest is Veracode Dynamic Analysis, a Dynamic Application Security Testing (DAST) solution for web applications. In addition, Eclipse Steady can examine compiled Java code and report vulnerabilities by examining "fix-commits".

Overall, the tooling we planning to use and we approach all of this ties into the active culture of DevSecOps.
