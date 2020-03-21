# Tutorial
#### Students
Mindaugas Varkalys varkalys@kth.se @MindaugasVarkalys  
Vincent Lohse vplohse@kth.se @olapiv

#### Topic
Building Docker server for multiple web applications

#### Backstory
We were trying to host our web applications using Docker Compose on Microsoft Azure, but it caused a lot of hassle and in the end it didn't work. So we decided to build our own Docker server which would allow easily deploy and host multiple Docker web server applications on multiple domains. As we searched, there is no such tutorial, so we will create one.

#### Covered topics
- Setting up Docker and Docker Compose
- Setting up reverse proxy using Nginx
- Issuing and automatically renewing SSL certificates