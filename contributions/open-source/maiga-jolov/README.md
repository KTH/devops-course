# Assignment Proposal

## Title

Contributing to Rust Embedded ecosystem to improve developers experience.

## Names and KTH ID
  - Johanna Löv (jolov@kth.se)
  - Aïssata Maiga (maiga@kth.se)

## Deadline

Task 1

## Category

Contribution to open-source

## Description

As anyone would say, Rust is hot 😉. The Rust embedded ecosystem is also blooming to provide support to embedded platforms. For example The [Knurling project](https://github.com/knurling-rs) is an open source project to automate Rust Embedded development by providing Rust-native level of support.

In Knurling
- `defmt` provides an effective logger for testing
- `flip-link` offers [stack protection](https://github.com/knurling-rs/flip-link). When sensitive memory regions are reached, compilation fails instead of undefined behaviour.

`defmt` can be improved with missing [type hints](https://github.com/knurling-rs/defmt/issues/660)
`flip-link` needs some enhancements to improve developper experience: a new parser to check that the memory.x file (a file that describes memory regions) is in the right format, and if not, reformat it. It also needs support for arithmetic operations and [some debugging](https://github.com/knurling-rs/flip-link/issues).

This contribution can fit in CI/Testing as it automates necessary work that was precedently done manually (i.e. a human needed to check if files were formatted correctly to avoid failure), and support for testing programs. 