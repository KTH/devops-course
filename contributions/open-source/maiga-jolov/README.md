# Assignment Proposal

## Title

Contributing to Rust Embedded ecosystem to improve developers experience. Submission on proposal #1587.

## Names and KTH ID
  - Johanna Löv (jolov@kth.se)
  - Aïssata Maiga (maiga@kth.se)

## Deadline

Task 1

## Category

Contribution to open-source

### Description

As anyone would say, Rust is hot 😉. The Rust Embedded ecosystem is also blooming to provide support to embedded platforms. For example The [Knurling project](https://github.com/knurling-rs) is an open source project to automate Rust Embedded development by providing Rust-native level of support.

In Knurling
- `probe-run` is a custom runner to use Rust on embedded devices.
- `defmt` provides an effective logger for testing
- `flip-link` offers [stack protection](https://github.com/knurling-rs/flip-link). When sensitive memory regions are reached, compilation fails instead of undefined behaviour.

`flip-link` needs some enhancements to improve developper experience:
`rust-lld` is a [linker](https://nxmnpg.lemoda.net/1/ld.lld) for GNU files. `flip-link` should accept the same files as `rust-lld`. Currently, some memory.x files (describing the memory) are not accepted by `flip-link` while being accepted by `rust-lld`. Meaning that developers must updates files by hand if they are incorrect.

This OSS contribution fits in CI/Testing as it automates necessary work that was precedently done manually (i.e. a human needed to check if files were formatted correctly to avoid failure), and support for testing programs. 

1. We added in total 7 tests to [manage input](https://github.com/knurling-rs/flip-link/pull/69) that is currently accepted by `rust lld`, to make `flip-link` more resilient. 
Target [PR](https://github.com/knurling-rs/flip-link/pull/69)

2. Fixed a [bug](https://github.com/knurling-rs/flip-link/pull/70) about arithmetic operations handled incorrectly:
Issue [#65](https://github.com/knurling-rs/flip-link/issues/65) Easy bug


Self-assessment


|                                                                                     | Yes | No  |
| ----------------------------------------------------------------------------------- | --- | --- |
| bug: The contribution fixes bugs                                                    | Yes |   |
| documentation: The contribution improves documentation                              |Yes* |  |
| feat: The contribution adds new features                                            | Yes |   |
| difficulty: The contribution is a difficult piece of engineering                    | Yes** |   |
| conversation: There is an interesting engineering conversation with the maintainers | Yes |   |
| merge: The contribution is merged in the main branch.                               | Yes  |    |

\* Added documentation on the components.

** It is quite a hefty code base that we needed to dive in.
The change we got merged was not a difficult piece of engineering, more code reformatting. But understand and rewrite a parser is more challenging.