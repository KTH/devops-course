# Assignment Proposal

## Title

Declarative Infrastructure with Terraform, NixOS, and Nomad

## Names and KTH ID

- Rafael Oliveira (rmfseo@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

As an organization's systems grow in breadth and complexity, it becomes paramount to have a single source of truth which can accurately document how the organization's infrastructure is organized, what services should be running where, and what state exists to be kept under consideration for, e.g., backups. Additionally, it is important that this information is sufficient to rebuild the entire network (or parts thereof), ideally in an automated manner and with the least friction possible.

I intend to present a solution to this problem, which comprises a tight integration of three different tools, each of which specializing in declarative definitions at different levels: Terraform is used to provision machines and configure them, NixOS ensures their reproducibility and of the environment they provide, and Nomad handles runtime orchestration of jobs according to concrete specifications.

This is the solution currently in use by KTH's Computer Science Chapter (Datasektionen), where I am responsible for all systems and overarching IT infrastructure. My plan for this demo is to showcase how one might introduce a new host running a new service (e.g., Vaultwarden), highlighting the different steps and considerations involved. The goal is not to explain how to set up the base declarative structure, but rather to demonstrate an incremental change that would be realistic in day-to-day operations and thus exemplify the benefits and quirks of using Infrastructure-as-Code.

**Relevance**

Reproducibility and centralized self-documentation are very attractive core tenets to a growing number of organizations, given the immense benefits they usually imply - this makes Infrastructure-as-Code (IaC) a very important concept to understand and keep in mind when considering different solutions and architectures. However, IaC is difficult to explain due to the multitude of parts involved, so one may sometimes find it hard to understand concretely how it works and what normal usage looks like. My demo strives to show a realistic example of how a professional might make use of IaC to assist them in their normal operations.
