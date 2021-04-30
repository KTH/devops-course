# Course automation: Checking essay requirements

## Members

Martijn Atema (atema@kth.se)
GitHub: [Atema](https://github.com/Atema)

## Proposal

I want to create a GitHub action (on pull requests) that automatically checks whether the word count and plagarism are within defined boundaries.

In order, this action should:

- Determine if the pull request concerns an essay submission
- Find the submitted pdf file
- Check the word count within the file
- Submit the file to a plagiarism check service
- Report the status on the PR

## Submission

With my submission, I aim for the following grading criteria. 

|                                             | Yes | No | Remarkable  |
|-------------------------------------------- | ----|----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) | Yes | No | n-a|
|The automation task produces a PR status or issue / PR comment | **🔥 Yes** | No | Points to a generated page with valuable additional information |
|The automation task is reusable | **🔥 Yes (next year for this course)** | No | **🔥 In other courses than this one** |
|The task runs on a standard platform | **🔥 Yes (Github action)** | No | Other platforms (e.g. Moodle, Canvas) |
|The task is praised by the other students of this course | 🙏 Yes | No | n-a |
|The code for the task is available | **🔥 Yes (public repo)** | No | **🔥 Well documented repo** |
