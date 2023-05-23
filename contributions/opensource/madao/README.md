# Assignment Proposal

## Title

Sempgrep Improvements: Trigger error in CI pipeline with invalid Semgrep command

## Names and KTH ID
- Minh Allan Dao (madao@ug.kth.se)

## Deadline
- Task 1
- Deadline 3, May 8th - See disclaimer. Goal is for concurrent work and submit either this or essay to meet May 22nd resubmission deadline

## Category
- Open Source Contribution

## Description

https://github.com/returntocorp/semgrep 

Semgrep is a lightweight static analysis tool meant to be used in the command line. With ease of access and use, Semgrep is used by developers and organizations of all kinds, and the organization that maintains it alongside other tools to augment it received a sizable Series C round.

With DevOps in mind, I plan to contribute to fixing a possible bug relating to problematic behavior that errerously allows for CI/CD pipeline runs to still successfully finish even when Semgrep scans fails.

Relevant Issue:
https://github.com/returntocorp/semgrep/issues/7630

**Relevance**

https://github.com/returntocorp/semgrep

Semgrep is highly used tool with an active and robust community. At the time of writing, the most recent commit was 5 minutes ago, leading to a total of 5367 commits to the main branch. There 8.1k stars for the project.


---
**Pull Request**

Pull request: TBD

I plan to discuss this issue with the issue presenter and the project maintainers as well as revisit the documentation/other portions of code to see desired behavior. This may be a particular use case that the maintainers may not intend for, and so could warrant a new command.

The PR will be difficult as it took significant time to get used to the project structure and recall my functional programming knowledge to examine the Go code and understand the project structure. I am looking to examine the behavior of the config_resolver.py and rule_fetching.ml files in regards to configuration file downloading behavior; --no-suppress-errors seems to be a red herring.

***Disclaimer***

I have an ongoing essay contribution request that is intended for submission of the redo deadline of May 22nd. I plan to work on this task and the essay concurrently, and whichever is finished first will be my 5th task, if that is permissible.

I discovered the possibility of improvements to Semgrep following exploration of the tool for the creation of an online executable tutorial for this course, and would prefer to contribute to this tool over writing an essay out of interest and for learning (this would be my first non-trivial contribution to open source).

<<<<<<< HEAD
Thank you!
=======
Relevant PR: https://github.com/KTH/devops-course/tree/2023/contributions/essay/madao
>>>>>>> parent of 3d806856 (Sync with madao)
