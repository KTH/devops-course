# Assignment Proposal

## Title

Dhall: Ensuring correct configuration files

## Names and KTH ID

- David Aldenbro (aldenbro@kth.se)
- Herdi Saleh (herdi@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial  

## Description

Dhall is a programmable configuration language intended to generate configuration files (in formats such as JSON and YAML).
Dhall itself is a strictly typed functional programming language, and can be used to ensure type safety of generated configuration files.

We intend to make a KillerKoda tutorial which displays Dhall's base functionality. We then intend to show some advanced use cases, relating to type safety and ensuring semantic equivalence of different configuration files.

**Relevance**

Configuration are the backbone of DevOps operations as they specify parameters of the development environment. By showcasing type safety, we will show that there are correctness guarantees for the generated configuration files. For semantic equivalence, we show why this is important, for example when migrating between services, by making sure that the environment stays the same.

**Sources**
- https://github.com/KTH/devops-course/issues/2#issuecomment-1096288439
    - https://docs.dhall-lang.org/index.html

**Tutorial Link**\
Tutorial: https://killercoda.com/davald/scenario/dhall-scenario \
Repo: https://github.com/aldenbro/dhall-tutorial