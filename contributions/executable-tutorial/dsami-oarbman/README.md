# Assignment Proposal

## Title

Securing Dependencies in DevSecOps with OWASP Dependency-Check & Snyk

## Names and KTH ID

- Oscar Arbman (oarbman@kth.se)

- Dania Sami (dsami@kth.se)


## Deadline

- Task 3

## Category

- Executable tutorial

## Description

This executable tutorial will focus on dependency management and DevSecOps, showing how to detect and prevent vulnerabilities in open-source libraries using two widely used tools: OWASP Dependency-Check and Snyk.

We will set up a demo project (Node.js or Java) that includes common dependencies, then run scans to identify security risks in both direct and transitive dependencies. The tutorial will also demonstrate how to integrate these scans into a CI/CD pipeline to ensure continuous security checks during development and deployment.

The tutorial will be delivered on KillerKoda, which allows the grader to execute all commands directly in the browser without creating any extra accounts.

Tutorial outline

Introduce dependency management and DevSecOps. Explain why supply chain attacks .

Install and configure OWASP Dependency-Check.

Run a dependency scan on a demo application and review the generated reports.

Install and configure Snyk. Run a vulnerability scan and compare results with Dependency-Check.

Show how to integrate dependency scanning into a CI/CD pipeline 


**Relevance**

Dependency management is at the heart of DevSecOps. Most modern applications rely heavily on third-party libraries, which can introduce severe security risks if not monitored properly. By using tools like OWASP Dependency-Check and Snyk, DevOps teams can ensure that vulnerabilities in dependencies are detected early and continuously checked in automated pipelines.

This tutorial will give learners hands-on experience in securing the software supply chain, one of the most critical challenges in DevSecOps today.