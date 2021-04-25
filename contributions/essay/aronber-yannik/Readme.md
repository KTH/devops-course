# The rust language build pipeline

In this essay we would like to take the readers through a deep dive into how complex a buildpipe can be.
One of the larger open-source build pipelines is the rust programming language buildpipe,
with lots of buildtargets, advanced conditions and bots for building just what is needed for different events.

## Preliminary Outline
-  introduction
  - What is Rust
  - What is a buildpipe
  - What are GitHub Actions
- Parts of the Rust Build buildpipe
  - bots
     - [\@bors](https://bors.rust-lang.org/)
     - [\@rustbot](https://github.com/rust-lang/triagebot)
     - docs.rs
   - actions
      - docs
      - trying builds
      - releasing
- General Contribution process (linking bots and actions together)

## Contributors

- Aron Hansen Berggren
  Email: [aronber@kth.se](mailto:aronber@kth.se)
  Github: [arxra](https://github.com/arxra)
- Yannik Sander
  Email: [yannik@kth.se](mailto:yannik@kth.se)
  Github: [ysndr](https://github.com/ysndr)
