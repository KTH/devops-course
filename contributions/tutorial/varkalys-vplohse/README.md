# Tutorial
#### Students
Mindaugas Varkalys varkalys@kth.se @MindaugasVarkalys  
Vincent Lohse vplohse@kth.se @olapiv

#### Topic
Building Docker server for multiple web applications

#### Backstory
We were trying to host our web applications using Docker Compose on Microsoft Azure, but it caused a lot of hassle and in the end it didn't work. So we decided to build our own Docker server which would could be easily deployed and host multiple Docker web server applications on multiple domains. We found no such tutorial, so we will create one.

#### Covered topics
- Setting up Docker and Docker Compose
- Setting up reverse proxy using Nginx
- Issuing and automatically renewing SSL certificates

## Tutorial Link (External)
We posted the tutorial here: https://medium.com/p/dockerizing-two-web-servers-to-respond-to-the-same-domain-eb9c15734a68?source=email-7323f673333b--writer.postDistributed&sk=36a145bdc7d4e38fdde72eb45eb87534

This is the "friend's link" - The tutorial has been featured by Medium, making it part of it's metered paywall, however, it is freely accessible with this link. We changed the tutorials topic very slightly - instead of using multiple domains, we now showed how to build a project with multiple web servers responding to a single domain (using sub domains).