# Assignment Proposal

## Title

Ensuring Terraform environment stability with Github Actions

## Names and KTH ID
  - Christopher Sapinski (sapinski@kth.se)
  - Katsutoshi Amano (amano@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

We will show how in a workflow, that when Terraform files are modified, we can then check the veracity of the changes. Once that has been verified, the merged pull request will update the environment. 

**Relevance**

Terraform is an infrastructure-as-code tool. When you make changes to the test environment by modifying Terraform files, it is good to make sure that the modifications do not break any standards. It can also make a log in the pull request of what has changed. For example, instead of spending time in the AWS dashboard changing configurations, Terraform can automatically update the instance. 
