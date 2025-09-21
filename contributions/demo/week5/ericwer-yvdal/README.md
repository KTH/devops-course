# Assignment Proposal

## Title

Vagrant networking: From nothing to Web and DB VM’s with one command

## Names and KTH ID

- Eric Wernström (ericwer@kth.se)
- August Yvdal (yvdal@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

We will demo how Vagrant can set up two interconnected virtual machines configured from a single Vagrantfile. One VM will run a web server while the other runs a PostgreSQL database. The key feature of this demo is that the web server communicates directly with the database VM over a private network through use of Vagrant's support for easy port-forwarding. Both VM's are automatically configured via provisioning scripts in the Vagrantfile. Changes to the provisioning scripts, such as updating database content or web page behavior, can be applied to both machines at the same time. We intend to demonstrate how Vagrant simplifies setup, including installations, networking and config. We will also show that changes can be applied to both machines at the same time.

**Relevance**

The simplification that Vagrant shows how IaC makes setting up even more complex, multi-functional systems quiuk and easy. In dev teams engineers often need a consistent environment, often one that mirrors production, in order to test their code. Vagrant allows for a modular system where we no longer need to rely on time consuming and error prone manual setup. Vagrants networking shows how VM's can be used to manage larger systems rather than serving single functions by interacting with each other.
