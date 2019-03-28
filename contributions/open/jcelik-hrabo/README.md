# Semantic Release Slack Notification Plugin

[Semantic release](https://github.com/semantic-release/semantic-release) is an intelligent automation tool, simplifying package release flows. A typical usage is to use semantic-release to determine the next version number, autogenerate release notes and publish packages.

Semantic release is a "must have" for a propper automated devops workflow when creating npm-packages (and others). It is the only way to automate human error.

> This removes the immediate connection between human emotions and version numbers, strictly following the Semantic Versioning specification.

## What do we want to do

We would like to create a plugin for semantic release that notifies the user about any errors or possibly successful releases, on Slack. There are [very few plugins](https://github.com/semantic-release/semantic-release/blob/master/docs/extending/plugins-list.md) (only two that we know of) that utilize the `success` and `fail` step of semantic release. We hope that our small contribution could improve the usability of semantic release for teams that require frequent build notifications.

Our aims are:
1. To improve semantic release.
2. To learn more about semantic release and how to create plugins for semantic release, enabling us to solve more complicated problems with semantic release in the future.
3. To learn more about how Slack bots work to be able to use them in the future.

## How does semantic release work?

Semantic release parses commit-messages to determince the purpose of every commit. After categorizing the commits (into categories like fix, feat, docs, BREAKING CHANGE) different plugins can use that information to execute automated scripts, like generating release notes from the commit messages, or bumping version numbers according to [Semantic Versioning](https://semver.org/).

Plugins in semantic release can plug into any of the steps that semantic release executes (presented below). We would like to plug in to the `success` and `fail` step.

| Step               | Description                                                                                                                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `verifyConditions` | Responsible for verifying conditions necessary to proceed with the release: configuration is correct, authentication token are valid, etc...                                                                         |
| `analyzeCommits`   | Responsible for determining the type of the next release (`major`, `minor` or `patch`). If multiple plugins with a `analyzeCommits` step are defined, the release type will be the highest one among plugins output. |
| `verifyRelease`    | Responsible for verifying the parameters (version, type, dist-tag etc...) of the release that is about to be published.                                                                                              |
| `generateNotes`    | Responsible for generating the content of the release note. If multiple plugins with a `generateNotes` step are defined, the release notes will be the result of the concatenation of each plugin output.            |
| `prepare`          | Responsible for preparing the release, for example creating or updating files such as `package.json`, `CHANGELOG.md`, documentation or compiled assets and pushing a commit.                                         |
| `publish`          | Responsible for publishing the release.                                                                                                                                                                              |
| `success`          | Responsible for notifying of a new release.                                                                                                                                                                          |
| `fail`             | Responsible for notifying of a failed release.                                                                                                                                                                       |

## Does this already exist?

That could be interpreted in two ways:
- [Does there already exist plugins or ways to use semantic release to get build notifications on Slack?](#does-there-already-exist-a-plugin-for-this)
- [Can the executing environment (CI/CD) be used to send build notifications on Slack?](#can-a-cicd-already-do-this)

### Does there already exist a plugin for this?

### Can a CI/CD already do this?
