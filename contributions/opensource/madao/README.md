# Assignment Proposal

**Relevant PR for Course Submission:**

https://github.com/returntocorp/semgrep/pull/7850

See relevant documentation and notes below for more details about scope of work.

-----

## Title

Semgrep Improvements: Error reporting has incorrect plurality

## Names and KTH ID
- Minh Allan Dao (madao@ug.kth.se)

## Deadline
- Deadline 3, Extended - May 22nd (originally May 8th)

## Category
- Open Source Contribution

## Description

https://github.com/returntocorp/semgrep 

Semgrep is a lightweight static analysis tool meant to be used in the command line. With ease of access and use, Semgrep is used by developers and organizations of all kinds, and the organization that maintains Semgrep alongside other (paid) tools received a sizable Series C round.

With DevOps in mind, I was initially inspired to contribute to fixing a possible bug relating to problematic behavior that errerously allows for CI/CD pipeline runs to still successfully finish even when Semgrep scans fails. However, further investigation led to complications; instead, I noticed that the plurality of error output was inconsistent.


-----

**Relevant Documentation:**

https://github.com/allandao/semgrep/tree/madao

**Active Community**

https://github.com/returntocorp/semgrep

Semgrep is highly used tool with an active and robust community. At the time of writing, the most recent commit was 5 minutes ago, leading to a total of 5367 commits to the main branch. There 8.1k stars for the project.

---

**Plan**

https://github.com/returntocorp/semgrep/pull/7630

I plan to discuss this issue with the issue presenter and the project maintainers as well as revisit the documentation/other portions of code to see desired behavior. This may be a particular use case that the maintainers may not intend for, and so could warrant a new command.

The PR will be difficult as it took significant time to get used to the project structure and recall my functional programming knowledge to examine the Go code and understand the project structure. I am looking to examine the behavior of the config_resolver.py and rule_fetching.ml files in regards to configuration file downloading behavior; --no-suppress-errors seems to be a red herring.

***Disclaimer***

Relevant PR: https://github.com/KTH/devops-course/tree/2023/contributions/essay/madao

I have an ongoing essay contribution request also intended for submission of the redo deadline of May 22nd. It would be my 5th and final task, so examining either (given that I pass the examined work) would be fine for me! I enjoyed working on this contribution, so decided to do it anyways alongside the essay.

I discovered the possibility of improvements to Semgrep following exploration of the tool for the creation of an online executable tutorial for this course, and would prefer to contribute to this tool over writing an essay out of interest and for learning (this would be my first non-trivial contribution to open source).

Thank you!

-----

**Relevant PR for Course Submission:**

https://github.com/returntocorp/semgrep/pull/7850