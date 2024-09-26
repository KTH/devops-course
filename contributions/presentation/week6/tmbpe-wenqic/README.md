# Assignment Proposal


## Title

NixOS: Reproducibility with Flakes and Secrets

## Names and KTH ID

  - Tomás Esteves(tmbpe@kth.se)
  - Wenqi Cao(wenqic@kth.se)

## Deadline

- Week 6

## Category

- Presentation

## Description

NixOS is a Linux distribution that follows a declarative approach. This allows it to be reproducible.
However by itself NixOS does not allow to lock packages versions and store secrets securely.
In this presentation We will present the `nix flake` feature that permits us to have a config that does not depend on the time at which it was created
and some tools such as `sops-nix` and `agenix` that allow us to store safely secrets.

**Relevance**

These features and tools are crucial in DevOps, specially in Dependency Management and DevSecOps.
