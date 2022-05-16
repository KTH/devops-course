# Assignment Proposal

## Title

Setup and use tools to improve your commit messages

## Names and KTH ID
  - Corentin Guilloteau (corgui@kth.se)

## Deadline

Task 3

## Category

Executable tutorial 

## Description

Writing good commit messages is very important in a team project, but it can be a hard task. This is why commit conventions exist in order to help developers. 
In the executable tutorial, I want to create a step-by-step tutorial on how to setup a good environment to enforce the use of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) in a project.

If I have enough time, I could also describe how using a commit convention can be useful in a CI/CD pipeline for automatic changelog and version number generation for example.

I plan to use [Husky](https://github.com/typicode/husky) to handle hooks, [commitlint](https://github.com/conventional-changelog/commitlint#config) and [commitizen](https://github.com/commitizen/cz-cli) to enforce conventional commit and [standard-version](https://github.com/conventional-changelog/standard-version) for automatic changelog generation.

**Submission**

[Github repo](https://github.com/corentinguilloteau/katacoda-scenarios)

[Katacoda tutorial](https://www.katacoda.com/corentingu/scenarios/kth-devops)

|                                             | Yes | No | 
|-------------------------------------------- | ----|----|
|executable: The tutorial can be automatically executed from beginning to the end, in the browser or in CI | ✅ | | 
|ilo: The tutorial states the intended learning outcomes. | ✅ | | 
|motivation: The tutorial is clearly motivated (why it matters for Devops?) | ✅ |  | 
|browser-based: The tutorial can be successful executed in the browser (katacoda is recommended) | ✅ |  | 
|ci-based: The tutorial can successful be executed as a CI job | | ❌ | 
|background: The tutorial gives enough background | ✅ | | 
|illustrated: The tutorial is illustrated with an informative figure (eg a flowchart) | | ❌ | 
|pedagogical: The tutorial is easy to follow  | ✅ | | 
|original: The tutorial is original, no or few similar tutorials exist on the web | ✅* |  |
|easter-eggs: The tutorial contains an easter egg |  | ❌ | 
|language: The language is appropriate (structure, grammar, spelling) | ✅ | |

\*A few tutorials already exists on the web about this topic. Nonetheless, I haven't found any that would be interactive. Also I haven't found any tutorial explaining how to use this workflow directly with the `git commit` command. Thus this tutorial still has some completly original parts.
