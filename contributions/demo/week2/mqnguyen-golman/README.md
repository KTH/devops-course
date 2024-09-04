# Assignment Proposal

## Title

Continuous integration testing of node and service availability of promox instances

## Names and KTH ID

  - Minh Quang Nguyen (mqnguyen@kth.se)
  - Fredrik Gölman (golman@kth.se)

## Deadline
- Week 2

## Category
- Demo

## Description

Our demo will be performed in the context of physical servers that we access through a VPN.

We want to test the following
- Availablity of different nodes in a proxmox cluster
- Availabilty of different services on these nodes

Tools:
- Tailscale (VPN service/mesh network)
- Proxmox (VM virtualization)
- Jenkins (Automation Testing and Integration Testing)

- Option Currently Deciding 
- Ansible (Testing Node instance, Update version ...etc)
- Terraform (Create Template for VM/docker/Container)

Backup plan:
In case we run into difficulties we deem unfeasible to overcome (the environment is not fully set up yet, and we are sort of short of time given the schedule) we discussed with the TA to create a rather simple web application involving either authentication functionality and a web form with input where validation would occur at the backend and perform integration tests by interacting with the browser and test frontend, backend, and potentially some database. We (and the TA) were unsure on whether the complexity level of this would be sufficient, but were asked to include it to have it commented on.

**Relevance**

We believe this is very rare compared to more conventional integration tests that may, for example, include a frontend and backend the the interactions between those two components. We also believe it is comparatively complex as it involves a lot of steps both in terms of setting up the environment and performing the tests. It also seem to fulfill a task that frequently would need to be performed manually by a system administrator otherwise. It is of course highly relevant to DevOps in general as it involves several CI tools such as Jenkins.
