# Assignment Proposal

## Title

Deploy your infrastructure declaratively using Nix and NixOS

## Names and KTH ID

  - Gustav Wallin (guwallin@kth.se)
  - Elias Vitell (vitell@kth.se)

## Deadline

- Week 5

## Category

- Presentation

## Description

Nix is a lazily evaluated declarative programming language used in the Nix package manager and in NixOS. In our presentation we will talk about how Nix can be used to build and configure infrastructure. We plan to
include the following in our presentation:

- A brief overview of the Nix programming language
- An explaination of how the Nix programming langaguage is used to configure an entire operating system in declarative way
- How Nix can be used to define infrastructure for specific tasks, such as building software, running servers or creating isolated environments
- The issues Nix and NixOS aim to solve, such as lack of determinism

**Relevance**

The fact that the Nix programming language is used to define an entire operating system is a clear indicator that it is highly suitable for writing infrastructure, meaning that it fits nicely into this week's
subject. In many DevOps tasks it is important to work in a clearly defined deterministic environment, where it is known that the infrastructure and software works the way it did when the configuration files where written.
This can be achieved by defining infrastructure using Nix.
