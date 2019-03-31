A CICD pipeline wiht automatic deplyoment 

In this demo, we'' use kubernetes on AWS(EC2 or ECS service) to design a CICD pipeline.
This pipeline includes git repositories management, auto tested before pushing to the cloud, build new image, the server pulls the new images, and finally the images deploys and run container.
It also incldues the issue about
-Autoscale the pods/containers easily over kubernets
-HTTPS load balancer over kubernetes

source:
https://kubernetes.io/docs/setup/turnkey/aws/
https://kubernetes.io/