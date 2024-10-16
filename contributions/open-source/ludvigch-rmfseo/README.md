# Assignment Proposal

## Title

DevOps Course File Requirements & Spoon Checksum Registration

## Names and KTH ID

- Ludvig Christensen (ludvigch@kth.se)
- Rafael Oliveira (rmfseo@kth.se)

## Deadline

- Task 3

## Category

- Open source

## Description

The open source contribution we propose is divided in two (unrelated) parts, each targeting separate repositories.

On one hand, we wish to resolve issue [#2583](https://github.com/KTH/devops-course/issues/2583) in the present repository (KTH DevOps Course), aiming to improve the existing GitHub CI workflows to validate Pull Requests targeting the `contributions/` folder. In particular, we hope to check that Pull Requests add exactly one file (a `README.md` at the correct location), and that its contents match the Pull Request's description -- with the exception of feedback submissions, which should instead modify an existing file.

On the other hand, we would also like to work on a solution to issue [#5957](https://github.com/INRIA/spoon/issues/5957) in Spoon (allegedly the best code analysis tool for Java), hoping to extend the release pipelines by introducing a new step to push package checksum attestations to [sigstore/rekor](https://github.com/sigstore/rekor). We most likely plan to do this using [actions/attest-build-provenance](https://github.com/actions/attest-build-provenance), as suggested by Martin.

**Relevance**

Both of these proposed contributions concern automatic pipelines in very active open-source projects hosted on GitHub. The first one relates to improving the automated testing suite used in this course, making it relevant to the topics discussed in week 2. Conversely, the second fields within the scope of CD, which was brought up in week 3, and in part also DevSecOps, more recently the focus of week 6. Combined, we believe that our proposal has a very clear relevance to DevOps, and in specific to this course by targeting multiple of its aspects of prominence.
