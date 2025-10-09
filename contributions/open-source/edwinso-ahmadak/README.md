# Assignment Proposal

## Title

Fixing Go's documentation site: to support `subdirectory` field in `go-import` meta tags

## Names and KTH ID

- Edwin So (edwinso@kth.se)
- Ahmad Al Khateeb (ahmadak@kth.se)

## Deadline

- Task 3

## Category

- Open source

## Description

We plan to contribute to the **Go toolchain ecosystem** by fixing an issue where Go's package documentation fails to be fetched when the package is located in a subdirectory of a repository.

Putting Go's package under a subdirectory is supported since Go 1.25. However, there is an issue with the documentation system; it failed to support this new feature.

We perform this by

- creating a reference repository that tests and documents how the new `subdirectory` field in `go-import` meta tags (introduced in Go 1.25) can be used.
- fixing Go's issue: golang/go #75258
- creating a PR on the documentation site repo (hosted under the Golang's Github organization, in the repo [golang/pkgsite](https://github.com/golang/pkgsite)

The repository (`edv1n/go-get-subdirectory-test`) hosts Go module in subdirectories (`gopkg/` and `gopkg/sub/`) and serves proper meta tags via GitHub Pages (`edv1n.github.io/go-get-subdirectory-test`).

The goal is to help Go developers and the broader DevOps community adopt the new feature that a Go package can be located inside a directory of a repo, by fixing the Go documentation site to support this new feature.

**Relevance**

This proposal is relevant to DevOps because package management and dependency resolution are essential for **build reproducibility, CI/CD pipelines, and continuous delivery**. By providing a reference repo on how Go's module system handles subdirectories and import paths, and fixing the documentation site to support this new feature, we improve developer workflow, reduce integration errors, and support sustainable dependency management in DevOps practices.

**Submission**
We proposed this task because we found an [issue](https://www.github.com/golang/go/issues/75258) reported on Go's repo that the documentation system is not resolving packages properly, if the package is served with [Go's 1.25 new sub-directory feature for resolving a module path](https://tip.golang.org/doc/go1.25#go-command).

We have designed a [repo](https://www.github.com/edv1n/go-get-subdirectory-test) to experiment with this new Go feature. It utilizes GitHub Page to serve the Go's import tag, so that Go can import our experiment packages properly. For details, please refer to the [README](https://www.github.com/edv1n/go-get-subdirectory-test/blob/main/README.md) in the repo.

We have created a [PR, # 113](https://www.github.com/golang/pkgsite/pull/113) on their mirror repo on GitHub [golang/pkgsite](https://www.github.com/golang/pkgsite). Here is what we have done with our contribution:
- The PR was first marked as WIP. 
- After adding more tests, making additional comments, and fixing bugs according to our new tests, we marked the PR as ready for review. 
- The PR has now been imported into Go's internal review system for additional reviews. 
- The code follows the original coding convention of the code base. 
- We followed the instructions given by the repo bot. 
- We followed [Go's Contribution Guide](https://go.dev/doc/contribute) to submit our contribution (e.g., writing the PR with the right format). 
- We followed the [repo's contribution guide](https://github.com/golang/pkgsite/blob/master/CONTRIBUTING.md) to perform tests, which increases the chance of our changes being accepted earlier.

This contribution is relevant to the project's roadmap as the feature has already been released. However, the documentation system hasn't caught up with this new feature; as a result, developers cannot read the documentation of packages using this new feature.
