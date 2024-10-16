# Assignment Proposal



## Title

Support Group Renames of Ansible

## Names and KTH ID

- Yinan Hu (yinanhu@kth.se)
- Hexu Li (hexu@kth.se)

## Deadline

- Task 3

## Category

- Open source

## Description

Ansible is an open source automation tool, which has been widely used in configuration management and application deployment. Currently, the module `groupmod` of Ansible does not support group's `rename`. And the community ask for fixing this [issue](https://github.com/ansible/ansible/issues/76774) as well as adding a new option `conflict_resolution: fail|rename|non_unique`.

Therefore, we plan to:

1. Understand Ansible's project architecture and source code.
2. Set up Ansible's development environment and run the source code and tests
3. Solve the issue:
   - Support group renames, probably using the `-n, --new-name` option of `groupmod`.
   - If feasible, add a new option `conflict_resolution: fail|rename|non_unique`
   - Update the related documentation.

**Relevance**

Ansible is an important automation tool in DevOps practive, which help team deploy IT infrastructure and applications. It leverages a easy-to-understand configuration language (Playbook based on YAML) to define tasks, helping DevOps teams efficiently manage configuration and infrastructure. Thus contribution to Ansible project is highly relevant to DevOps.