# Assignment Proposal

## Title

Secure your git and CD pipeline with SOPS.

## Names and KTH ID

- Sina Khoraman (sinakh@kth.se)
- Robin Eggestig (eggestig@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

In this assignment we will demonstrate how to securely store sentitive files in git using SOPS: an open-source tool specially created for encrypting and decrypting the values in the configuration files of the software application that is being developed. We will first quickly showcase how passwords stored in configuration files can be a vulnerability. Then, we will quickly deploy SOPS and secure our CD pipeline. Our goal is to showcase how a simple script can greatly improve the security of the delivery process.

In this demo we aim to demonstrate that the gap between "proper security" (e.g. using Vault and dynamic keys) and "no security" (storing passwords in files) can be filled with minimal effort.

**Relevance**

Implementing security mechanisms is itself an entire task. Especially in the starting phase, the focus is always put on functionality and features, and thus, security has a tendency to be left behind. That is at least until the application reaches a certain level of maturity where proper security becomes less of a feature and more of a requirement. But, until that happens, a lot of software is left defenseless in the face of potential attackers. Thus, even minimal security, such as encrypting the passwords in configuration files, can make a huge difference. It is then important that developers are at least aware of the potential solutions that could be implemented "in the meantime".
