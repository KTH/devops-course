# Assignment Proposal

## Title

Pinning your deps: Reproducible builds vs Reproducible artifacts

## Names and KTH ID

* Singvalliyappa Velayutham ([sinvel@kth.se](mailto:sinvel@kth.se))
* Alexander Wigren ([wig@kth.se](mailto:wig@kth.se))

## Deadline

Week 6

## Category

Demo


## Description

Software reproducibility is important for building a reliable CI/CD pipeline and for avoiding the "it works on my laptop" problem. Docker is widely used to achieve this, but even within Docker, dependency management can become tricky if versions drift across builds in different environments. This demo shows the value of Nix and how it provides hermetic builds. We build the same project once with Docker to show how Docker can introduce drifting versions that lead to a breaking build, then build the same project with Nix to show that you get the identical build every time. 

We also show that when you modify a declared input in Nix, the resulting build hash changes, demonstrating that every change to the environment is captured. To be fair to Docker, we also show pinning dependencies working, but make the point that in Docker this pinning is manual: without a full lockfile the transitive dependencies still drift, and the system level dependencies beneath the package manager still drift unless every layer is pinned. Nix, pins the entire transitive and system level deps by construction.

**Relevance**

Software reproducibility is undermined by resolution errors and drifting dependencies, so managing them well is important to a reliable pipeline. This demo shows two of the tools available to developers for pinning dependencies and the different guarantees each provides: Nix produces a reproducible build from source every time, while Docker produces a reproducible artifact, an image that runs identically once built but whose build can still drift unless every input is pinned by hand. 
