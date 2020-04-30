# Demo Proposal: Using Terraform with GCP server for static IP webhook calls

## Members:
Akhil Yerrapragada (akhily@kth.se)

## Motivation:
A third party infrastructure relies heavily on cloud provider service (cloud NAT) to provide static IP address since all the 
services inside the infrastructure have dynamic IP address. Consider a service such as Kubernetes engine,  the server has dynamic IP 
address and relies on the available load balancer  in the infrastructure that routes the requests. Assuming that one of the dynamic IP 
address service triggers a webhook, a public service always  wants to receive it from whitelisted IP address (Only from trusted sources) 
but cannot afford due to the operational complexity. Here, we shall be using GCP server that acts as a webhook relay and provides
an external IP address which is whitelisted and can be used by the public service.

## What is expected in demo?
This demo focuses on managing infrastructure Ops with terraform in a safe and efficient way and shows how to use a webhook relay (A GCP server) 
that receives a dynamic IP webhook call from services (Linux terminal will be used to trigger the webhook in demo) and provides controlled static 
external IP which a public service can trust. With terraform we apply the changes required to reach the desired state of configuration.



