# Assignment Proposal

## Title

Migrating legacy integration tests in Moby

## Names and KTH ID

- Oscar Walter (owalter@kth.se)
- Hasan Kalzi (kalzi@kth.se)

## Deadline

- Task 3

## Category

- Open source

## Description

**Contribution and submission status**

[Moby](https://github.com/moby/moby) is an open-source container engine project used by Docker. Its legacy `integration-cli` test suite is deprecated, and [issue #50159](https://github.com/moby/moby/issues/50159) tracks the migration to the newer test suites.
We implemented the five container-commit test migrations in our [accepted proposal #3056](https://github.com/KTH/devops-course/pull/3056) and submitted [Moby PR #53912](https://github.com/moby/moby/pull/53912), related to [migration issue #50159](https://github.com/moby/moby/issues/50159).

The upstream PR contains five commits and changes three files. As checked on 10 October 2026, it is open, has no merge conflicts and has not been merged. DCO and labeler checks passed. The other upstream workflows report `action_required`; their tests have not run, and no maintainer review is recorded. We submit the contribution before the course deadline and will continue following upstream CI, review and merge.

| Legacy test | API integration test | Contributor |
| --- | --- | --- |
| `TestContainerAPICommit` | `TestCommitInheritsCmd` | Oscar Walter |
| `TestContainerAPICommitWithLabelInConfig` | `TestCommitWithLabelInConfig` | Oscar Walter |
| `TestCommitPausedContainer` | `TestCommitPausedContainer` | Oscar Walter |
| `TestCommitChangeLabels` | `TestCommitChangeLabels` | Hasan Kalzi |
| `TestCommitChange` | `TestCommitChange` | Hasan Kalzi |

The replacements are in `integration/image/commit_test.go`. The five legacy functions are removed from `integration-cli/docker_api_test.go` and `integration-cli/docker_cli_commit_test.go`.

Hasan's migrations are recorded in commits [bbb1f4a](https://github.com/moby/moby/commit/bbb1f4afb21c4dac1b69208a628c1476cf53d1b5) and [2d7b238](https://github.com/moby/moby/commit/2d7b2383e303499b3c5b71d61217039fbc7f5175). Both contributors reviewed the changes before opening the upstream PR.

**Architecture and implementation decisions**

Moby provides the container daemon and its Engine API. The old suite invokes the Docker CLI or mixes CLI setup with API calls. The new tests use the Go API client and existing Moby helpers to create containers, commit their filesystem and configuration into images, and inspect the resulting images and source containers.

This is API regression coverage: it checks daemon and client behaviour. CLI argument parsing and formatting belong to Docker CLI end-to-end tests. We chose `integration/image` because the selected tests exercise committed-image behaviour, consistent with the migration issue.

We reuse `setupTest`, `container.Run` and the suite's cleanup rather than introducing another test framework. For short-lived containers, `poll.WaitOn(container.IsSuccessful(...))` waits for successful completion before committing. This preserves the sequencing previously provided by the foreground CLI run and avoids committing before the container has finished its changes.

Assertions inspect typed configuration values instead of comparing formatted CLI output. The tests retain checks for filesystem and command preservation, labels supplied through commit configuration, all nine configuration fields in `TestCommitChange`, image-label overrides without changing the source container, and preservation of the paused state. The configuration-change test preserves separate Linux and Windows expectations for environment ordering and the working directory. The paused-container test skips unsupported environments.

**Validation**

Hasan ran the following command in the Ubuntu/WSL Linux checkout after adding the replacements and removing the legacy functions:

```bash
make test-integration \
  TEST_INTEGRATION_DIR=./integration/image \
  TEST_SKIP_INTEGRATION_CLI= \
  TESTFLAGS='-test.run=^TestCommit'
```

The supplied terminal output records:

```text
PASS amd64.integration.image.TestCommitInheritsCmd
PASS amd64.integration.image.TestCommitWithLabelInConfig
PASS amd64.integration.image.TestCommitPausedContainer
PASS amd64.integration.image.TestCommitInheritsEnv
PASS amd64.integration.image.TestCommitChangeLabels
PASS amd64.integration.image.TestCommitChange
DONE 6 tests in 6.222s
EMPTY amd64.integration-cli
DONE 0 tests in 0.101s
++ exit 0
```

The six API tests include the five migrated tests and the existing `TestCommitInheritsEnv`. The legacy suite compiled, but its legacy test methods did not match this filter; `EMPTY` is not evidence that the entire legacy suite passed. We also applied `gofmt` and checked the diff for whitespace errors.

Windows execution, the complete integration suites and repeated flakiness checks have not been validated locally. The Linux run supports the selected behaviours, not a claim that all Moby tests pass.

**Collaboration, challenges and reflection**

We [announced all five selected tests on the migration issue](https://github.com/moby/moby/issues/50159#issuecomment-5780725135) to avoid duplicating another contributor's work. During course proposal review, the TA questioned whether the initial two-test scope provided sufficient depth for two students. We expanded it to five related tests; the revised proposal was accepted.

A practical challenge was running Linux build scripts from a Windows checkout with CRLF line endings and slow filesystem access under `/mnt/c`. We converted affected tracked text files to LF, then used a separate checkout under the Ubuntu home directory and transferred the intended test change. Keeping the diff limited to the migrated tests avoided committing unrelated line-ending changes.

The important implementation challenge was preserving behaviour while changing the test mechanism. Typed assertions improve failure diagnostics, but removing CLI execution also changes which layer is tested. Waiting for container completion, inspecting both image and source-container labels, and retaining platform conditions help preserve the intended API coverage.

Remaining work is to respond to maintainer feedback, run upstream CI and obtain merge. Further validation should cover Windows and repeated runs to detect timing-dependent failures. We do not claim maintainer approval or a completed upstream merge at this stage.

Both contributors reviewed the code, and Hasan executed the local validation above.

AI assistance:

Hasan used AI: `TestCommitChange` and `TestCommitChangeLabels`, to get helped with setup, diagnostics, test commands. 


**Relevance**

Moby is an open-source container engine used in Docker-based DevOps workflows. This contribution addresses the project's documented migration away from deprecated testing infrastructure. It preserves regression coverage for container commits while placing API behaviour in the appropriate integration suite. Its maintenance value is the replacement of legacy tests with supported test helpers and direct API assertions; it does not add a new runtime feature or claim a measured performance improvement.
