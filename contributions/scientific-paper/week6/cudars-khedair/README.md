# Assignment Proposal

## Title

ARGUS: A Framework for Staged Static Taint Analysis of GitHub Workflows and Actions

## Names and KTH ID

  - Jēkabs Čudars (cudars@kth.se)
  - Rami Khedair (khedair@kth.se)

## Deadline

- Week 6

## Category

- Scientific paper

## Description

The paper selected was published at the 32nd USENIX Security Symposium (USENIX Security 2023) https://www.usenix.org/conference/usenixsecurity23/presentation/muralee.

CI/CD automation platforms such as GitHub actions, GitLab CI, Travis CI etc. are a modern part of software development on which large amount of projects rely on. With these platforms new dependencies and code complexity has been introduced resulting in new vulnerabilities. 
Workflows process external data controlled by outsiders (issue bodies, PR titles, branch names) and pass it around between steps and 3rd party actions. When that data ends up in a shell command, anyone who can open an issue or PR can run code inside the pipeline. The authors purpose - `ARGUS`, taint analysis designed to catch GitHub actions code injections by tracking untrusted data across workflow steps and into the actions they use. Authors ran their analysis tool over 2.7 million workflows and managed to find critical vulnerabilities (manually verified) in 4307 of them and in 80 actions.

During the presentation we plan to focus on the vulnerabilities the paper found and what they mean in practice, rather than on the internals of the analysis. We will:

- Explain the kinds of code injection ARGUS catches: event data flowing into `run:` steps directly, via environment variables, via default inputs of 3rd party actions and via outputs passed between steps.
- Deep dive into one case from the paper, the `DynamoDS/Dynamo` issue workflow, where the issue body goes into an env variable, through a string-replacement action that strips double quotes, and out of its output into a shell command. We will show why removing quotes does not stop `$(...)` command substitution, how the workflow token could be leaked, and how to fix it.
- Use the same example to briefly explain how ARGUS follows the data across steps and actions, which is why it finds flows that pattern based scanners miss.
- Discuss the key findings, limitations of the approach and when such tooling is worth having in a pipeline.
- Compare with at least two tools released before and after 2023.

**Relevance**

GitHub actions is one of the core CI/CD automation platforms in DevOps. This paper directly assesses the security layer of CI/CD pipelines , showing that vulnerabilities in workflows are pervasive and can compromise the entire software supply chain. 

Understanding these risks, and the practices that prevent them, is essential for anyone designing or maintaining DevOps pipelines.
