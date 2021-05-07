## Demo Proposal - Infrastructure as Software with Pulumi

### Member

Name: Isak Hassbring (isakha@kth.se)
Github: [hassbring](https://github.com/hassbring)

### Motivation

Infrastructure as Code is great. There's just one problem - it's usually not code, but static files and domain-specific-languages that for large projects could be thousands and thousands of repetitive lines. E.g. Terraform requires HashiCorp Configuration Language (HCL) and Kubernetes YAML-files does not leverage neither the power of traditional programming languages, nor the wide-spread know-how already out there. 

Entering Pulumi! Pulumi is a cloud agnostic solution where you can use programming languages like Python, Go, and JavaScript to generate the static file infrastructure. You hence get access to familiar constructs like for loops, functions, and classes. This reduces boilerplate and enforce best practices. Instead of creating a new ecosystem of modules and sharing, Pulumi lets you leverage existing package management tools and techniques. Plus, you can automate and simply stuff in a cool way. Infrastructure as **real** code - or software.


### Will be covered

* Pulumi intro:
  * what is it, why should I bother, !how can I use it
* How-to:
  * Setting up and deploying a simple web app using different IaS solutions cloud agnostic through Pulumi, such as AWS S3, Kubernetes cluster, etc. 
