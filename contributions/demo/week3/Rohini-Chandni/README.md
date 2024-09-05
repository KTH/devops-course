# Demo Proposal



# Title
Blue-Green Deployment technique in Continous Deployments

# Names & KTH Id
- Rohini Bhardwaj (rohinib@kth.se)
- Chandni Rakhashiya (cnra@ug.kth.se) 

# Deadline
- Week 3

# Category
- Demo
  
# Description
This demo is designed to guide the audience through the deployment of a web application using the Blue-Green Deployment strategy with 
GitHub Actions and Kubernetes. In this demo, we will demonstrate how to update a web application by setting up two identical environments:
one serving active users and the other for deploying changes. This ensures that the update is deployed with zero downtime, 
without affecting the active users. We will also cover the roll back quickly in case any issues are detected in the new version.

# Relevance
When updating a feature or version of a web application, it’s common to see messages like ‘This application is under maintenance
until 4:00 AM.’ Many deployments are scheduled during off-peak hours, based on geographical regions, to minimize the impact on active 
users. To address this issue, we use the Blue-Green Deployment strategy. With Blue-Green Deployment, we can deploy updates without 
stopping the active server by maintaining two identical environments: the current (blue) environment serving users and the new (green) 
environment where updates are deployed. If everything works correctly in the new environment, traffic is seamlessly redirected to it, 
ensuring a smooth transition without downtime. 
