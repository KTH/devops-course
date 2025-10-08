# Assignment Proposal

## Title

Support for pinned module refs in Dagger CLI

## Names and KTH ID

- Guillaume Roboam (roboam@kth.se)  
- Mathias Magnusson (mathm@kth.se)

## Deadline

- Task 3

## Category

- Open source

## Description

[Dagger](https://github.com/dagger/dagger) is an open source programmable CI/CD engine widely used in DevOps workflows.  
Currently, when calling a module in CI, users face a tradeoff between using a branch ref (like `@main`) and a commit SHA:

- Using a branch ref (e.g. `@main`) is unsafe, since it may change between the triggering event and execution.  
- Using a commit SHA (e.g. `@3dd66bb0c182f...`) is safe but loses important context about the original ref, such as whether it was a tag, branch, or PR.  

The community has opened Issue #11117 (`https://github.com/dagger/dagger/issues/11117`) requesting support for a syntax that allows **both ref and commit pinning** at the same time.  

We plan to contribute by:  

1. Investigating the CLI parsing logic of Dagger’s module reference system.  
2. Implementing support for a combined syntax, for example:
```bash
$ dagger -m github.com/dagger/dagger@main:3dd66bb0c182fbf0b72ca7b986985ec506027af4
```
(ref plus explicit commit pin)  
3. Adding tests to ensure backward compatibility and coverage of the new syntax.  
4. Updating the CLI documentation and examples.  
5. Engaging with maintainers during the implementation, marking the PR as WIP, and iterating based on feedback until merged.  

**Relevance**  
This contribution improves reproducibility in CI/CD pipelines.
By allowing developers to reference both a human-meaningful ref (branch or tag) and a commit SHA, pipelines can become more reproducible and less error-prone.  
This aligns with best practices of secure builds and deterministic deployments, making the contribution directly relevant to DevOps engineers.