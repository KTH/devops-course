# Demo  - Deploying Azure storage using Terraform

## Member
- htchan (htchan)
- Martin Gabrielsen (mgabri)

## Topic
Deploying an online storage system on Microsoft Azure using Terraform

## Screencast

https://youtu.be/FN6LYFWRWi4

## Repo for the demo

Here you can find the code used in the screencast with specific instructions. 

https://github.com/Gabbi68/Infrastructure


## Motivation

Our motivation for this demo is to show who open-source infrastructure as code (IaC) tools like Terraform can be used to quickly and easily deploy infrastructure on Azure. We have elected to use storage as an example of what is possible when using Terraform. By using a tool like Terraform can transform what is usually a vendor-specific language (bash, bat, ARM template or PowerShell) into a unified language that is independent of the particular vendor. This reduces some of the overhead of having to learn multiple different scripting languages. Also Terraform has built-in static checker that allows us to do "dry runs" by using the plan function which shows everything that it will do before it does it, which is contrary to most scripting languages. 
 
 Moreover, by doing this demo, we show how fast we can deploy infrastructure once the Terraform file is created. As a comparison, if you were to do this deployment manually, it would probably take more than an hour, whereas with terraform it takes about 3 min.  


## Relation to DevOps

This demo shows how a single developer or a system could quickly deploy and destroy infrastructure. More broadly it shows how Terraform can be used to develop infrastructure for permanent deployment, or it could be a temporary full mirror of all needed infrastructure, that is used to spin up and configure all infrastructure need in a matter of minutes rather than hours or days. This allows for the same level of control and automation as with any other code, and highly supports the automation principle of DevOps. 

Terraform can also be used to check the deployed infrastructure and as such if anyone makes changes to the infrastructure manually, it will be able to detect and or change it back if so wanted. 


