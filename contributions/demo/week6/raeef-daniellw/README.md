# Assignment Proposal

## Title

Using static analysis with SonarCloud to identify security flaws.

## Names and KTH ID

  - Daniel Lai Wikström (daniellw@kth.se)
  - Rafael Bechara (raeef@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

We'll be showing how integrating SonarCloud with GitHub Actions can help developers automatically discover potential security flaws in their applications. Before the demo we'll set up a repo with GitHub Actions that automatically run a sonar scan upon pushing new code. 

During the demo we'll push some code with a security flaw such as not sanitizing user input which makes us vulnerable to XSS attack. We'll then show how this vulnerability fails the quality gate check. We’ll then show the analysis page that gives us information of where in the code the vulnerabilities are, how the vulnerabilities work and suggestions about how we can fix them.

**Relevance**

Using GitHub Actions for static code analysis upon pushing to a repo is a pretty textbook example of DevOps by facilitating Continous Integration through automatic testing upon source code changes. Since we're adding the capability of identifying security flaws to our DevOps workflow it's also relevant to DevSecOps.
