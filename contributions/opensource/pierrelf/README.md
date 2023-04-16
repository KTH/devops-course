# Assignment Proposal

## Title

Implement UI improvements in Apache CloudStack

## Names and KTH ID

  - Pierre Le Fevre (pierrelf@kth.se)

## Deadline
- Task 1

## Category
- Open source

## Description

Apache CloudStack is an IaaS (Infrastructure-as-a-Service) platform used to build self hosted cloud providers. 

It is used by many organizations thanks to its ease of installation and management, and open source nature.

The contribution would be to fix one of the many issues in the UI, many of which I have experienced myself, to bring a better experience to users of CloudStack.

This would include finding and repairing the erroneous code in the UI component, and perhaps patching some Java backend code in case that is where the issue originates from.


Example issues:
https://github.com/apache/cloudstack/issues/7227
https://github.com/apache/cloudstack/issues/7363

**Relevance**

CloudStack being a cloud platform is highly relevant for DevOps. CloudStack also provides adapters for Terraform, Kubernetes and other widely used DevOps tools.

---
Pull request: https://github.com/apache/cloudstack/pull/7386

The new feature was approved by one maintainer. It consisted of making the API and GUI more uniform as the "domainpath" was not included in this route.

Fixing it took some time as I had to get the whole Apache CloudStack project to build on my local machine, and then figure out where in the quite large codebase I had to make the changes.
