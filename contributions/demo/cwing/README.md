## Inspiration behind the demo
Just as a short background, I figured I'd give the reason I thought of doing this demo.

While working on a tutorial, we used Katacoda, as it is a simple way to have others be able to perform the same task without a local environment.
It also provides an extremely easy way to reset your whole environment. During the time of us working with Katacoda, we however ran into some problems with the service.
When using the Python playground, we would often get the wrong type of environment, so instead of getting a Python environment we would get some other type.
Often a Docker or Jupyter environment. At the begining we didn't know about this issue, or notice it, this meant time was spent using old versions of Python and Pip which was not ideal.

# Demo proposal - Publishing your own customized terminal environment by deploying a simple website on AWS
The title needs to be worked on, not too easy to tell the whole process in one sentence...

## Members
Christer Winge cwing@kth.se

## Envisioned process
Not everything is set in stone or figured out yet, depending on what I choose the title could reflect that.

* The webpage will be hosted using AWS or Azure, within a simple linux VM(not sure which dist yet)

* The website will be deployed through the use of either Python-code and Flask, or just Golang-code

* The website should support different terminal configurations and different users to use the website at the same time

    * The configurations will be set by the host, while the users visiting the website can choose from those made available(could also make it possible to have an imagename as input, but would be severly limited by things such as free tier limits, size, etc)

* Will use Docker images to keep everything contained, which is also an easy way to reset the environment and they can be customized, so the type of environments are endless

* Will most likely use one of the tools below to include the terminal to the webpage
    * [GoTTY](https://github.com/yudai/gotty)
    * [ttyd](https://tsl0922.github.io/ttyd)
    * [wetty](https://github.com/butlerx/wetty)

Depending on time constraints, additional options could be put in

## Goal
The goal would be a website where you are able to publish any Docker image that you want. This would be published online on the cloud using either AWS or Azure.
I might go over how to create your own Docker image to fit your needs in the demo, but probably quite briefly and not in-depth. 
Multiple users should be able to use seperate terminal environments at the same time.
This could obviously be used in the same way as a Katacoda playground, but could easily be altered to just have a place where only you could access your favorite terminal workplace environment, customized to your specification.
Could also prepare customized images for demos/presentations needed to be performed, without needing to bring and plug-in your own computer.
