# Assignment Proposal

## Title

Reusable Infrastructure with Terraform Modules

## Names and KTH ID

- John Söderholm (jsoderho@kth.se)
- Jonatan Stagge (jstagge@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

This demonstration will showcase Terraform Modules for creating reusable, consistent, and scalable infrastructure components. We will illustrate how common infrastructure patterns, such as a secure web server, can be defined once as a Terraform module and then deployed multiple times with different configurations, eliminating code duplication and promoting standardisation.

We will begin by outlining the challenges of managing infrastructure without reusable code and introduce Terraform Modules as the solution. Next, we will quickly show a pre-built Terraform module that defines a standard web server (an AWS EC2 instance with Nginx and necessary networking), and then use it to deploy an initial web server to AWS. For the core of the demo, we will add additional web servers by simply reusing the same module with different settings, showcasing the clear benefits of this reusable approach.

**Relevance**

By showcasing reusable Terraform modules, we illustrate how organisations can accelerate deployment cycles, ensure standardised and reliable environments across all stages, and significantly reduce operational overhead. This approach minimises configuration drift, improves maintainability, and enables development teams to provision resources rapidly, thereby streamlining the entire software delivery pipeline.
