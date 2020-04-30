
provider "azurerm" {
  version = "=2.7.0"
  features {}
}


resource "azurerm_resource_group" "rsg2" {
  name     = "foldingathome"
  location = "West Europe"
}


resource "azurerm_container_group" "contgrp1" {
  count = 5 //Change to make more containers 


  name                = "Foldinginst-${count.index}"
  location            = azurerm_resource_group.rsg2.location
  resource_group_name = azurerm_resource_group.rsg2.name
  ip_address_type     = "public"
  os_type             = "linux"

  image_registry_credential {
    server   = "hub.docker.com"
    username = "YOURUSERNAME" //CHANGE
    password = "YOURPASSWORD" //CHANGE 
  }

  container {
    name   = "folding-${count.index}"
    image  = "gabbi68/folding-at-home-kth"
    cpu    = "0.5" //Change according to how much you want to spend
    memory = "1.5" //Change according to how much you want to spend

     ports {
      port     = 7396
      protocol = "TCP"
    }
    
  }

  tags = {
    environment = "foldingathome"
  }
}