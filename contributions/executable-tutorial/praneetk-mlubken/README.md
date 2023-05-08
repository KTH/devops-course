# Assignment Proposal

## Title

Setting up a node.js project

## Names and KTH ID

  - Praneet Kala (praneetk@kth.se)
  - Moritz Lübken (mlubken@kth.se)

## Deadline
Task 3

## Category
Executable tutorial

## Description
When you google "how to setup a new node.js project?" mostly express.js tutorials come up. 
For example [this one by DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-node-js-application-for-production-on-ubuntu-20-04)
or [this one by MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment).
There is also the [official node.js guide](https://nodejs.org/en/docs/guides) describing different concepts.

What doesn't come up however are tutorials on how to setup a full node.js project with all the tools necessary
to make development and deployment fast, easy and secure. The tutorial will aim to demonstrate how to set up a complete
project from scratch that uses:

- PNPM as a package manager
- Git and signed commits for source code management
- ESLint with the security pluginfor static analysis
- GitLeaks for hard-coded secrets detection
- Semgrep as an additional SAST scanner
- PNPM to identify vulnerabilities in packages
- PNPM to analyze the dependencies licenses
- Docker to package and deploy the application

The tutorial does not try to automate these things. Instead the goal is for the user to gain some understanding of what different steps in DevOps are,
how they make life better and easier and why they should be used when it comes to security.

**Relevance**

According to a [2022 stack overflow survey](https://survey.stackoverflow.co/2022/#most-popular-technologies-language) JavaScript dominates the landscape of programming languages.
Node.js was ranked the most common web technology. As explained in the description there are few tutorials on how to setup a project with many different tools.
Most tutorials focus on a single tool or compare different tools.
If you are a new developer it is hard to find all the good or necessary tools to make your software secure and to save work. Sometimes this can take years.
That's what we try to solve with our tutorial.

**Tutorial**

You can find our tutorial [here](https://killercoda.com/mluebken/scenario/tutorial) or [here](https://killercoda.com/pkala-devops/scenario/tutorial).
