# Assignment Proposal

## Title

Declarative and reproducible deployments with NixOS

## Names and KTH ID

- Diogo Correia (diogotc@kth.se)
- Tomás Esteves (tmbpe@kth.se)

## Deadline

Week 5

## Category

Demo

## Description

NixOS is an immutable Linux distribution that aims to be reproducible
and declarative thanks to the underlying Nix functional language.
Through the Nix language, it is possible to declare all aspects of a system,
ensuring that the result will always be the same, no matter when or where
the system configuration is deployed.
Other properties of NixOS include easy rollbacks, dependency pinning for each package,
specialisations, cleanup of previous configurations, and more.

In this demo, we will show the audience how to deploy a fully-configured NixOS
system in seconds, using tools like nixos-anywhere to bootstrap the installation
and disko to declare disk partitions.

**Relevance**

NixOS (and the associated Nix language and Nixpkgs package repository) are the pinnacle
of Infrastructure as Code, allowing for a system to be completely defined through
Nix code.
This makes similar deployments extremely easy and scalable, as Nix code can be shared
between many hosts.
Additionally, updates to packages and configuration can be performed in bulk or in a
CI/CD system and copied to the resulting systems.
