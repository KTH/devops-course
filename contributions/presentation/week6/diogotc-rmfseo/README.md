# Assignment Proposal

## Title

Continuous Information Flow Control

## Names and KTH ID

  - Diogo Correia (diogotc@kth.se)
  - Rafael Oliveira (rmfseo@kth.se)

## Deadline

- Week 6

## Category

- Presentation

## Description

Information Flow Control is a security technique that aims to enforce certain invariants in computer programs, typically to achieve confidentiality. It resorts to either static analysis or dynamic monitoring to determine whether external attackers with access to public outputs can infer anything about private inputs, either through explicit flows (e.g., printing a password to the console) or through implicit flows (e.g., only taking certain publicly-observable actions if a secret meets a given condition).

We plan to introduce this important concept, as well as analyze the advantages and disadvantages associated with it, particularly when being applied in a continuous fashion throughout a project's development lifetime. Additionally, we have previously developed an IFC static analyzer for Go programs (written in Rust) - [Glowy](https://github.com/ist199211-ist199311/glowy-langsec) - that we can use to provide concrete examples of what an implementation might look like and how it can be used. Finally, to tie the topic further to DevSecOps, we will highlight how one could (and should) set up CI workflows to validate that every single commit follows the security invariants under enforcement.

**Relevance**

As a software project rapidly grows in size and complexity, it becomes increasingly difficult for a human to consider the full ramifications of a given change, especially when it comes to the nuanced (and usually indirect) impact it can have on the security of seemingly unconnected components. Nevertheless, security is a paramount aspect to preserve at all times due to the enormous implications a single flaw can have if deployed undetected. Thus, it is critical that as many prevention techniques as possible are applied as often as possible (i.e., to every commit) in a completed automated fashion, embodying the spirit of DevOps (and, specifically, DevSecOps).
