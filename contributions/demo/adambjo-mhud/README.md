## Members
Helal Uddin (mhud@kth.se)

Adam Björnberg (adambjo@kth.se)

## Topic
Virtual Network Peering with Microsoft Azure and Terraform

## Screencast link

https://youtu.be/WPZPVX2ptF0

## GitHub repository
https://github.com/adbjo/devops-demo

## Description
According to Microsoft, Virtual Network Peering enables a seamless connection between Azure virtual networks. By using both private and global virtual network peering, it is possible to route traffic with low-latency, high-bandwidth. Virtual machines can communicate with other virtual machines by using VNP. This communication process is connected with other resources such as Azure subscription, Azure Active Directory(AAD) in the Azure portal. As this communication is private, there is no necessity to implement encryption. With Terraform, deployment of such infrasctructures can be easily automated in code.

In this demo, we will show how to use Terraform to create Virtual Networks in Azure and connect them with Azure Virtual Network Peering. Finally, we will add Virtual machine in the virtual networks.

**References:**

https://docs.microsoft.com/en-us/azure/virtual-network/tutorial-connect-virtual-networks-portal
https://www.terraform.io/docs/providers/azurerm/r/virtual_network_peering.html

**Music:**

Jeremy Blake - Sunspots

## Changes based on feedback
- The infrastructure is created with Terraform instead of in the Azure Portal, showing how infrastructure deployment can be automated (more novel and interesting).
- Accompanying GitHub repository created for the Terraform code.
- Screen resolution fixed.
- Music credits embedded in the video end-screen.
- Failed VM creation removed.
- Introductory slide added with network diagram of the created infrastructure.
- Easter egg at 4:20
