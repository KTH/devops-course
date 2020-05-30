![Docker Image CI](https://github.com/Gabbi68/folding-at-home-kth/workflows/Docker%20Image%20CI/badge.svg) ![terraform](https://github.com/Gabbi68/folding-at-home-kth/workflows/terraform-lint/badge.svg)

# COVID-19 - Folding@home for Azure

## Dedicated repo

REPO
[Here](https://github.com/Gabbi68/folding-at-home-kth)

The Docker image is also hosted on DockerHub
[Here](https://hub.docker.com/r/gabbi68/folding-at-home-kth) 



## Participants

 

- Martin Gabrielsen - @[Gabbi68](https://github.com/Gabbi68)

- Nicolai Hellesnes - @[nicolai-h](https://github.com/nicolai-h)



## Dependencies

- Azure CLI
- Azure Account and valid subscription
- Terraform 


## How to 


1. Download and install Azure CLI ([link](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest))

> For Windows there no need any further configuration, for Mac/Linux (see [link](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest))

2. Download and install Terraform ([link](https://www.terraform.io/downloads.html))

> Installation instructions can be found here ([link](https://learn.hashicorp.com/terraform/getting-started/install.html))

4. Use any text editor to change the number of containers you want to run by changing

    `count = 5` (default) to `count = 1..N`

> This will affect your cost, the more instances, the higher the price.

6. Set your user name and password for docker hub in main.tf.

     ```
     image_registry_credential {
    server = "hub.docker.com" 
    username = "YOURUSERNAME" //CHANGE
    password = "YOURPASSWORD" //CHANGE
    }
    ```

7. Do `az login` in you terminal of choice (keep using it for the steps below)
8. Navigate to where main.tf is located
9. Do `terraform init`
10. Do `terraform plan` and verify that any changes have been saved and are included
11. Do terraform apply then `yes` to deploy the instances. 

You will now have some containers running in Azure.


**Extra**
> If you would like to use another image (other than ours) just change as shown below to any image stored on docker hub.
> 
> 		`image  = "gabbi68/folding-at-home-kth`  to 
> 
>      image = "dockerhub-user/docker-image


## Description


Folding@home is a way everyone can help combat COVID-19. We want to lower the bar of entry for folding@home so that as many as possible can help to contribute to the research of COVID-19. Our idea is to create a docker image and terraform deployment (for Azure) to make it as easy as possible to start folding@home and also to make the user be able to decide how much of the processing power of their computer they want to contribute with. This would make it possible for people that have some spare money or a business account on Azure to quickly deploy as many instances of folding at home as they want. Without having to have all the nectary equipment at home.

Also, people might want to participate without affecting their system (Heat, Noice, performance )


## Why this is different

For significant novelty, our submission is combining multiple parts that each does have some similar solutions. What we have done is to automate the deployment of Folding@Home almost much as possible. For docker, there exist docker images that have folding@Home, same with TerraForm, there are scripts that deploy docker images, and finally, there are some that utilize Azure. However, there is few if any that does all these three things together. Most other either use different technologies like using VM’s rather than using containers in Azure ([link](https://joshheffner.com/how-to-run-foldinghome-on-azure-spot-vms/)) or is highly reliant on user action’s ([link](https://azurecloudminingscript.github.io/Run_Folding_At_Home_in_the_Azure_Cloud.html)).

The most similar project that we have been able to locate is one developed by the Google cloud platform (GCP) team this is the most similar one, with the difference being that it is deployed to GCP rather than Azure something that would mean a full re-development of the terraform setup that is provided by the GCP team.

And as GCP only has a 9% market share and Azure on 31% (Market share among the ‘big 3’), this solution is more likely to be used compared to the GCP solution.



## How it's automated

When the Dockerfile is pushed to Docker Hub, it will automatically build the Dockerfile, and the build log will show the status of the build. If the build is successful, the status will have a green tick and the word “success”. The build log for the Dockerfile can be found [here](https://hub.docker.com/r/gabbi68/folding-at-home-kth/builds).

Based on feedback, we have also elected to use Github actions to do some testing in line with DevOps. There are two actions, one for testing the Docker Image and one for checking the formatting of the Terraform file. 