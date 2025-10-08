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
