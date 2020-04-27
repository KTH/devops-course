# Tutorial Proposal
----
### Group members:

Felix Luthman (felixlut@kth.se)

Nour Alhuda Almajni (almajni@kth.se)


### Topic:
Docker

### The novelty of the tutorial
- The tutorial will run in
[Katacoda](https://www.katacoda.com/nour95/scenarios/final-docker), so you don't need to
install anything in your system.
- The tutorial will use the terminal extensively.
- The tutorial will have a background and will explain the relationship to Devops.

This tutorial will also explain the main commands and steps to:
- Show all the images and containers that had already been install/created in your system.
- Install a container from docker hub.
- Run a container in your terminal (Katacoda).
    * Start it again. (explain the different between command start and run).
- Rename a container.
- Remove a container.
- Create a docker container (your own container) that can listen to port 80, and show a message like "hello world" in this port.
- Mount local files to the container, as well as showcasing the effects of this when running it.

In the background we can explain:
- What is docker?
- The relationship to devops.
- The difference between an image and a container.

The tutorial will also feature discussions about the following topics:
- The differences between the two ways of gathering containers for usage, i.e. pulling from dockerhub and building your own containers. 
- The differences between `RUN` and `CMD` in a Dockerfile.
- The differences `bind mount` and `volume` when running a container.