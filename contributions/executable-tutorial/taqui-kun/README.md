# Executable Tutorial: Building a CI/CD Pipeline for a small frontend in a Kubernetes Cluster using Terraform

## Members

Taqui - taqui@kth.se
GitHub: [Internet-Person-IP](https://github.com/Internet-Person-IP)

Kun Wu - kunwu@kth.se 
Github: [Wkkkkk](https://github.com/Wkkkkk)


## Proposal
I want to create an Executable Tutorial for creating a CI/CD pipeline for a Kubernetes Cluster using Terraform. The frontend will be super simple with a counter and click function. The proposal will be done either using katacoda or as a medium article. Katacoda will be used if it is easy to integrate the terminal however if katacoda terminal is hard we will skip it .

The current structure of the tutorial creating a terraform template that does this:


- Creating the initial frontend, set up frontend with simple tests
- Creating a small cluster
- Containerizing the frontend
- Deploying the frontend to a small pod
- Creating the CI/CD pipeline
- Make changes to the frontend and actually push it to master
- Check that the CI/CD pipeline works correctly and then make sure that the deployed website works correctly