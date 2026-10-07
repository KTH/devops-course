# Assignment Proposal

## Title

Project submission: Weebcult, an anime quiz website with fully integrated DevOps

## Names and KTH ID

  - Mostafa Faik (mfaik@kth.se)
  - Derfesh Mariush (derfesh@kth.se)

## Deadline

- Task 2

## Category

- Project

## Description

WeebCult is an anime quiz website which me and my partner has worked with in a previous course. We applied multiple tools and different aspects of DevOps to fully utilize everything we have learned from this course. The DevOps stack we have implemented is as follows:

- CI: we have implemented unit tests via ViTest and E2E tests via Playwright. These are triggered by .yml file, which uses Github Actions for every pull request or push that is done on the repo. 

- CD: another .yml file ensures that all integration tests are successful and that there is nothing wrong with the safety or quality of the incoming changes. The file activates Github Actions, allowing firebase to deploy the new version of the repo.

- IaC: we implemented Terraform to manage our server infrastructure (firebase and firestore), formalising our setup so it can be replicated and simplifying potentiall attempts at scaling up the server infrastructure for the future.

- Security/quality: implemented via Checkov and Trivy, which get activated via Github Actions, allowing us to prevent policy issues, security vulnerabilities and package missconfigurations. 

**Relevance**

When it comes to DevOps, the main principle is to automate and effectivize as much as possible. For us, it was necessary. Previously, when we worked on this project, we had to plan meticulously who worked on what part of the code, updates had to be bigger and the risk for merge conflicts was much higher. Plus we had to contact Mostafa for deployment. We also had to privately check everything by hand to make sure that everything worked with the website. Thanks to the added DevOps uppgrades, we have practically a monorepo, which automates all testing and deployment, allowing everybody to work whenver they want and only having to focus on improving the server, instead of needlessly requiring to check that everything works and waste time on communication.