###Finished Tutorial
We have finished the tutorial and published to medium. 
https://medium.com/@nicksteele011/a-practical-guide-to-docker-and-kubernetes-cffcaa9f7848

Both Nick and I are new to container and container orchestration tools and it was fun to learn Docker and Kubernetes and how to use them.

As part of the tutorial, we have demonstrated how to create a docker image for a node.js app and setup 2 development environments for different versions of the app. We realized that scaling is straightforward in Kubernetes. So, we demonstrated how Namespaces in Kubernetes can be used to setup different environments and what are the advantages of using them.

We have uploaded the image to docker hub. The Kubernetes setup can be tested in a browser also with our yml configurations.  


###Tutorial Proposal: An investigation into Docker & Kubernetes.
A practical investigation of Docker and Kubernetes with respect to development/testing environments.


###Authors: 
Nicholas Steele: nsteele@kth.se 
Sashikanth Raavikanti: sraa@kth.se


Sashi and I want to focus and learn about containers and their management using Kubernetes. We think this is an important topic as containers can be used in almost all parts of the DevOps lifecycle from providing a configured environment for application developers, testers and operational developers to the deployment of an application. Hence, learning containerisation management/ provisioning is a vital skill for anyone wanting to get dirty with DevOps!

We want to portray their relation through a step by step tutorial:

###Tutorial outline: 
•	Overview (What and why).
•	Set up a docker development or testing environment.
•	Provision, manage and scale using Kubernetes.
 
I myself for a long time had heard of Docker and Kubernetes but I did not know the differences and powerful outcomes these technologies can have within DevOps projects.
There are many tutorials on getting started with Docker and Kubernetes but ours will demonstrate their relations through a sequence of steps clearly outlining a fluid transition between the two tools, educating students on how they work with one another.

After the tutorial the student will:
•	Understand the difference between Docker/Kubernetes with a sound understanding of their relation. How to create Docker environments (example probably with some sort of skeleton app (the app here isn’t that important the focus is on configuring and using the services))
•	How to manage and provision Docker containers with Kubernetes.
 
A good issue/theme to stick with in relation to the course topics is scalability. (This issue will be highlighted in the Kubernetes component of the tutorial as one of the major benefits of Kubernetes is its ability to scale). 

This tutorial will get the student thinking small by setting up basic environments so that foundational knowledge is achieved.

The tutorial will then scale their knowledge up with an example use case. This will take what the student has done and explain that basically the same thing is done within major tech companies to scale/ provision development/testing environments on a large level, hopefully, this will give the student a sense of satisfaction.
Additionally, after this tutorial is complete, Sashi and I aim to integrate these technologies into our own/future software development projects.

