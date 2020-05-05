# Demo
----

## Member
- htchan (htchan)
- Martin Gabrielsen (mgabri)

## Topic
Deploying an online storage system on Microsoft Azure

## Screencast

https://youtu.be/9sqdc24mobo

## Repo for the demo

https://github.com/Gabbi68/Infrastructure


## Motivation
As storage is essential for any Devlopment, we would like to demonstrate how it can be done using infrastructure as code. This allowes use of tool like Github in order to keep config of the infrastructure. Also as we are moving to a serverless world most people don't want to use self hosted servers for storage/IAAS. As such we want to deply azure storage using Terraform, this allows the us to control the infrastucture using vesion control and utalize a cloud service that allows us to scale up and down as need. 

## Relation to DevOps

This demo shows how a single developer or a system could easly deploy and destroy infrastructure. More broadly it shows how terraform can be used to develop infrastructure for permanet deployment or it chould be a temporery full miror of all needed infrastrucure, that is used to spin up and configure all infrastrcure need in the matter of minutes rather then hours or days. This allows for the same level of controll and automation as with anyother code, and higly supports the automation prinsipal of devops. 

