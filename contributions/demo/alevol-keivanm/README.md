# Demo: Terraform cloud
**Team members:**

- Keivan Matinzadeh keivanm@kth.se @keivanm
- Alexander Volminger alevol@kth.se @Volminger

**Topic:**
Github Actions: Terraform cloud, IaC


With the rise of cloud computing infrastructure have started to become more and more flexible and modular, just like code. So why should you not treat your infrastructure as code (IaC)? There are several players that enables IaC, but most of them only offer it with their own infrastructure platform. This can be a limitation for those how do not want to get tied down to one provider.

HashiCorp’s Terraform is an open-source IaC solution that works cross-cloud and data centers. Simply write your infrastructure in Hashicorp Configuration Language (HCL) and watch your infrastructure get built.

HashiCorp recently launched Terraform Cloud to the public, which is is a SaaS solution of Terraform Enterprise. It enables easy CI/CD and collaboration on your infrastructure code. We plan to show a demo where we use Terraform cloud to deploy a cross-cloud infrastructure solution. We will make use of Terraform modules and possibly build our own module. We will demonstrate how the Terraform cloud transform code to real infrastructure. We will also, if there is time, talk a bit in the beginning on what differs Terraform from other IaC solutions.

