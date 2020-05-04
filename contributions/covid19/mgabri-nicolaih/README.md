# COVID-19 - Folding@home for Azure




## Pratisipants

 

- Martin Gabrielsen - @Gabbi68

- Nicolai Hellesnes - @nicolai-h



## Dependencies

- Azure CLI
- Terraform 


## How to 


1. Download and install Azure CLI
2. Download and install Terraform 
3. Use any text editor to change the number of containers you want to run. (count = 5 is the default) 
4. Set your user name and password for dockerhub in main.tf.
5. Do az login in you terminal of choice (keep using it for the steps blow)
6. Do terraform init where you saved the main.tf (from this repo)
7. Do terraform plan and verify that any changes have been saved and are included
8. Do terraform apply then 'yes' to deploy the instances. 

You will now have some containers running in Azure.


If you would like to use another image (other than ours) just change "image  = "gabbi68/folding-at-home-kth"" to any image on docker hub


## Discription


Folding@home is a way everyone can help combat covid-19. We want to lower the bar of entry for folding@home so that as many as possible can help contributing to the research of covid-19. Our idea is to create an docker image and terraform deployment (for azure) to make it as easy as possible to start folding@home and also to make the user be able to decide how much of the processing power of their computer they want to contribute with. This would make it possible for people that have some spare money or a bussines acount on Azure to qucikly deply as many instances of folding at home as they want. Without having to have all the neccaery equioment at home.

Also people might want to participate without having an affect on their own system (Heat, Noice, performance )