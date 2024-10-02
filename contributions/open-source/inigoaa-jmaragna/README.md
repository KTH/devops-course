# Assignment Proposal

## Title

_--enable-feature: Consider removing no-default-scrape-port_

## Names and KTH ID

  - Jacopo Maragna (jmaragna@kth.se)
  - Íñigo Aréjula Aísa (inigoaa@kth.se)

## Deadline

- Task 3 

## Category

- open-source

## Description

Prometheus has different features available. However, some of them are not immediately available by default, but they can be enabled using flags. What the community is requesting is to enable some of these features by default. What we are proposing to do is to take this [issue](https://github.com/prometheus/prometheus/issues/13959) and resolve the problem.

Now, an outline of the various tasks we aim to solve:
1. Understand the project architecture and source code.
2. Set up the environment and run the project/tests.
3. Tackle the problem itself:
    - By default, we want the `no-default-scrape-port` feature to be enabled.
    - Add the possibility to disable it on demand.
    - Update the documentation.

**Relevance**

Prometheus is crucial in DevOps for its ability to monitor (Week 7) and analyze system performance in real-time. It helps teams collect metrics, set alerts, and automate responses, ensuring system reliability and quick incident resolution. This enhances the core DevOps practices of continuous integration, deployment, and collaboration.

Link: https://github.com/prometheus/prometheus/pull/14958


**Finding the task**

After exploring potential projects on the Cloud Native Computing Foundation [website](https://www.cncf.io/projects/), we initially considered contributing to [Backstage](https://www.cncf.io/projects/backstage/) or [Kubeflow](https://www.cncf.io/projects/kubeflow/). Ultimately, we decided to contribute to Prometheus, a project highly relevant to our DevOps course. We reached out to the maintainers through the Cloud Native Computing Foundation Slack, where they recommended we begin with this [issue](https://github.com/prometheus/prometheus/issues/13959), which is described earlier in the file.

We carefully reviewed the discussion surrounding the issue, gaining a clear understanding of both the problem and the proposed solutions. After expressing our interest in working on the issue and requesting further guidance, one of the maintainers suggested we reference an abandoned [pull request](https://github.com/prometheus/prometheus/pull/14160). Once we were assigned the issue, we used that input as a foundation and began working on the solution.

**Understanding the project architecture and source code**
After being assigned the issue by a project maintainer, we decided that the best way to set up the environment and understand the project was by running the tests within the project. We started by running `go test ./...` in the project's root directory. This command will install any required module defined in the `go.mod` file and run all the tests in the project. However we could not install the moduled, receiving the following error.
==TODO: picture of the error==
We did not know what was the cause of the error and there was not too much information about it on internet. We try to read the following files to find some information about the error:
- Makefile
- go.mod
- go.sum
- README.md
- Contributing.md

We realize that the go version required was specified in the `go.mod` file, but was shocking that two differnt versions were specified `1.22` for go runtime and `1.23` for the toolchain, we realized that the default version provided in Ubuntu by `apt` was older than the required one, so we try to install the latest go version from the official website. After installing the latest version of go, we were able to tun the tests. However, they did not passed. We encountered several issues as not all dependencies were installed, nor were they clearly defined anywhere. To resolve this, we asked for guidance in the project's Slack channel. A maintainer recommended that we install the linter, but this alone was insufficient. We also discovered that we needed to install goyacc.

Once that was done, some tests passed successfully, but we still encountered issues with tests in the UI folder. We realized that these tests were written in JavaScript, while the rest of the project, including our task, was primarily in Go. After reviewing the Makefile, we realized the test instructions allowed us to run only the Go tests. Once we reran the tests using the appropriate command, they all passed successfully.
```bash
make test GO_ONLY=1
```
After preparing our project, we decided to focus on our task and deeply understand the code we must change. As an orphan PR was related to our task we checked it to take some inspiration, this helped us to realise which files we should modify, however, the code was outdated and a review suggested many changes, so we decided to note the changes and start from scratch.
**Development**
As a team, we discussed how to approach the problem and created small subtasks that each team member could handle independently. Since the issue was related to the configuration of the Prometheus binary, the changes impacted both the main and scraper modules. The main module handles the various flags, while the scraper module is responsible for the logic related to the issue.

At this point, we faced a decision: Should we remove the option entirely and make the new default the only available behaviour, or should we retain the option to allow the old behaviour as well? After reviewing previous discussions in Slack and on GitHub, we realized that the maintainers preferred removing the old behaviour.

We divided the work by splitting each module into equal parts, allowing both of us to contribute simultaneously to both modules.

After completing the changes and updating the tests, we ran the tests to ensure that the changes did not break any existing functionality. We also ran the linter to ensure that the code was clean and followed the project's standards. However, both of them failed. The Golang test told us that the documentation did not match the code. We updated the documentation manually but there was a way to do it automatically, after running the command for creating the doc, all tests passed.

The linter failed but gave us descriptive changes so was easy to solve them, after solving the linter issues we ran the tests again and all of them passed. So we made a commit and created the PR, which passed all the CI pipelines.

**Final issue**

After completing all the necessary changes and ensuring our code passed all tests, we submitted a [PR](https://github.com/prometheus/prometheus/pull/14958) to Prometheus. While all tests were successful, we awaited approval from the maintainers. Although this was marked as a first issue, the changes we proposed could have broken the current v3 logic. As a result, the maintainers discussed how to smoothly integrate the new behaviour into future versions.

However, after a few days of discussion, an unexpected situation arose. The original author of the previous, abandoned PR (which we had used for reference) suddenly reappeared and submitted changes after four months of inactivity. The maintainers, seemingly unaware of our prior conversations and the rationale behind our PR, questioned why we had submitted it, given its similarity to the older one. Despite the potential for our PR to be merged, they ultimately decided to close it and prioritize the original PR.

We eventually clarified the situation with the maintainers, and they acknowledged the confusion. They recognized that our PR had been submitted in good faith following earlier discussions and the guidance we received.

**Open-sources contribution grading criteria **

To demonstrate how our contribution aligns with the grading criteria, we have compiled the following table outlining the key points we've addressed:

|                                            | Yes | No |
|-------------------------------------------- | ----|----|
|declaration of intention: The intention to contribute is declared in the project's preferred method (e.g., issue, mailing list). | Yes: issue |  |
|work-in-progress (WIP): The contribution is marked as WIP until it is ready for review. | Yes: we were assigned and opened a PR with ongoing discussion |  |
|ready for review: The contribution is marked as ready and announced for review when it is complete. | Yes: we passed all of the checks in the CI |  |
|conversation: The contributor engages in conversation with the project maintainers, responding to feedback in a timely manner and making necessary changes. | Yes: check the conversation under the issue and our PR |  |
|documentation: The contribution includes necessary documentation updates. | Yes: docs updated accordingly |  |
|testing: The contribution includes necessary testing. | Yes: we modified tests and passed all of them |  |
|code quality: The code contributed is of high quality, following the project's coding standards and guidelines. | Yes: passed the linting phase |  |
|relevance: The contribution is relevant to the project's roadmap and adds value to the project. | Yes: breaking change so definitely yes. Long awaited issue |  |
|difficulty: The contribution is a difficult piece of engineering, either a bug fix or a new feature (mandatory) | Yes: Prometheus is a big project and required us to gain a good understanding |  | 
|merge: The contribution is merged in the main branch of the target project.|  | No: see issue with that | 

**Conclusion**

Overall, this process has been a valuable experience for us in understanding a large open-source codebase. We learned how to identify important issues and explore how new solutions can be integrated into future versions. Contributing, even in a small way, to such a significant project was highly rewarding. Although the unexpected situation at the end was unfortunate, we successfully identified a good first issue, engaged with the maintainers, studied the project in depth, developed our solution, and opened a PR. The entire experience has been a great learning opportunity.
