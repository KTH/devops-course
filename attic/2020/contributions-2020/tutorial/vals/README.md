# Tutorial: Golang web api as a docker container on Google Cloud

## Author
Victor Josephson (vals@kth.se)

## Overview

In this tutorial, we will go through the basics of containerization and cloud hosting, and combine the use of server-side programming with these concepts in a simple project, with the aim of showing where and how these components can fit together in a production environment. The target audience are aspiring software engineers and developers who have studied programming and computer science but haven't deployed projects and made them available to the outside world. We will create a simple Go (Golang) web server that returns a json message, containerize it with Docker, push it to the Google Container Registry, and finally launch a Google VM instance running the container and make it publicly accessible. 

The three areas of server-side programming, containerization and cloud hosting are each themselves vast topics in the software engineering and DevOps world, with huge amounts of documentation available online. However, it's often the case that information on either of these topics assume that the reader already knows a lot about the process of packaging and deploying software. Also, many tutorials catering to DevOps beginners head straight into the technical aspects of *how* to use a specific tool but fail to paint the bigger picture of what problems the technology solves and when/why one should even use it. For example, learning how to run an application inside of a container is pretty useless without the knowledge of which scenarios actually benefit from doing this.

As a computer science student, my experience from the first three years of university was that I learned advanced algorithms, data structures and strong programming fundamentals, but received almost no training in how to put these skills to use by packaging my code into distributable solutions or products, and actually deploying them. 

So, before we dive into the steps of building, containerizing and cloud hosting a server-side Golang application, let's take a look at these concepts separately.

# Background

## Containerization and Docker
Installing an SDK or runtime for a programming language, putting some code together and executing it locally on your own machine is usually the standard approach that many students and developers take when writing code. As the complexity of your project grows, additional settings such as environment variables, dependencies, network configurations, etc come into play and start increasing the level of coupling between your software and the infrastructure it runs on. By the time you're ready to show or deploy your work, you realize that moving your code to any other machine would require all that configuration to be done from scratch in the production environment, and if the infrastructure isn't exactly the same as your own machine, your code might not even run!

One solution to control and standardize your environment is to run your code in a virtual machine (VM) that you can tailor to mimic your development environment. The downside of a VM is the large overhead needed to run a whole operating system on top of the host operating system. It also doesn't automatically solve the problem of having to go through each configuration step for your project when setting up a new machine; it just gives you the freedom to install an environment of your own choosing.

The term "containers" in the field of DevOps is a similar concept to a virtual machine, but with some key differences. Most importantly, a container runs on the host kernel, meaning it doesn't need to run a full operating system on top of the host operating system. This makes a container lightweight in comparison to a VM, as it can be tailored to only include the specific services needed for your application. *https://docs.microsoft.com/en-us/virtualization/windowscontainers/about/containers-vs-vm*

Docker is a widely-used tool for creating containers to package and run basically any kind of application. In a nut-shell, you specify the code infrastructure and any dependencies in a simple configuration file (Dockerfile), along with the paths to your source code and the commands needed to build and execute it. Then you just build and run the docker container instead of building/running your application explicitly. This will create an isolated environment which runs your application inside it. You can think of the container as a portable self-contained package of your application, which you can run on virtually any machine, making it super simple to deploy your product.

## Cloud hosting
Now that we have a strategy for packaging our hypothetical application (which we will create further down in this tutorial!), the next question is how to actually deploy it and make it accessible to the outside world. Nowadays, for most projects it's both easier and more cost-efficient to rent server resources from any of the big cloud providers such as Google, Amazon or Microsoft, than to physically host your own servers. An additional benefit of hosting your applications "in the cloud" is that you can dynamically and on-the-fly scale the amount of resources your application uses based on its current demand. Finally, depending on the type of cloud service you use, you can even be relieved from the often tedious tasks of keeping the system up-to-date and secure, as the cloud provider can manage this for you.


## Go
The last piece of the puzzle, or in a way the first piece, is the actual code that makes up our application. For this tutorial, we're going with Google's fairly new and increasingly popular serverside language Go, or Golang as it's also called. It's an open source statically typed and fast language, designed with networking, scalability and concurrent programming in mind, and is heavily used internally at Google and many other companies. Despite being built for large-scale systems, its syntax is clean and easy to learn, and running a web server on it is surpisingly easy, with almost no boilerplate code needed. Hence, it's good both for demonstrational purposes in this tutorial but also good for creating any kind of serverside application that you might need to scale in the future. 

**FUN FACT 1**: The entire language specification for Go can be found at https://golang.org/ref/spec and is only about 26,000 words long, and easily fits on less than 100 pages if copied and pasted into Microsoft Word (83 pages using 12pt Arial font). In contrast, the language specification for C++, available for purchase at https://www.iso.org/standard/68564.html, is sold as a 1,605 page long book!

**FUN FACT 2**: Docker itself is written in Go! As is many other Google products, such as Kubernetes (a container orchestration tool created by Google, which we however won't cover in this tutorial).

Now let's finally start building our application!


# Tutorial

## Create a Go web server

Before starting, make sure you have Go and Docker installed locally. Technically neither of these tools are strictly needed on your own machine, as it's possible to have Google build everything in the cloud for you, but for educational purposes we will use these tools so that we can try out our application locally before deploying it.

Run the following code from a work directory of your choice:
```
mkdir go-server
cd go-server
```
Create a file named `main.go`, and paste the following code into the file:

```
package main

import (
	"log"
	"net/http"
)

type server struct{}

func (s *server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"message": "Hello from Golang!"}`))
}

func main() {
	s := &server{}
	http.Handle("/", s)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

You should now be able to run `go run main.go` and go to `http://localhost` in a web browser and see the following json string:
```
{"message": "Hello from Golang!"}
```

Note the line that adds the header "Access-Control-Allow-Origin" with the value "*". This enables CORS, meaning that other websites are able to make requests to our api. This is necessary if you decide to build a separate frontend for your application that will communicate with your serverside application. It's not needed for this tutorial, but I decided to include it as it's a common pitfall to forget about this step when separating serverside and clientside web applications.

## Create a docker image
Next, let's containerize our go server so that we can easily deploy it to Google Cloud later.
Create a file named Dockerfile (no extension) in the same folder as the main.go file, and paste in the following lines.
```
FROM golang:alpine
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN go build -o main
EXPOSE 80
CMD ["/app/main"]
```

So what was all that, you ask? This is the file I mentioned earlier, which contains everything Docker needs to know in order to set up an isolated environment and run your application inside it. Let's go through it line by line:

`FROM golang:alpine` 
This specifies a publicly hosted parent image that we want Docker to build our container from. Docker will fetch this image from a public repository. Remember how I said that containers don't need a full operating system? Here we see that, as we are only providing our container with the resources needed to build and run Go applications, instead of providing it with a whole OS.

`RUN mkdir /app` 
This creates a directory in the container, which will be used as a work directory.

`ADD . /app/`
Here we copy the source code files from our system into the work directory of our container

`WORKDIR /app`
Here we actually specify the work directory to be `/app` .

`RUN go build -o main`
This command will be familiar to you if you've ever written a golang application before, as it's the command to compile and build our application.

`EXPOSE 8080`
The outside world cannot by default connect to Docker containers, so we need to export the port our go application is listening on to allow requests to reach it from outside the container.

Note: To access our container from outside the host it will run on (an instance of Google Compute Engine), we will also need to configure a firewall rule allowing incoming traffic to that instance, but we will get back to that later in this tutorial.

`CMD ["/app/main"]`
This the command Docker will use to launch our go application after it has been built.


Now that we have specified how to containerize our application, we can move on to preparing our cloud hosting environment.

## Google Cloud setup:
First, create a Google Cloud account if you dont have one. Next, create a new project and enable billing for it. 
You will also need to install the Google Cloud SDK, which there are multiple ways to do. On Linux and macOS, you can use the following two commands in succession:
```
curl https://sdk.cloud.google.com > install.sh
bash install.sh
```
If you're running Windows or want to check out more installation methods and options, head over to Google's official documentation at https://cloud.google.com/sdk/install to read more.

Now we initialize the SDK with the command `gcloud init`.

We also need to enable the Container Restistry API for our project, so that we can publish our container image to Google's Container Registry, from which our Compute Engine instance will pull the image from there. Head over to https://console.cloud.google.com/apis/dashboard, click on `ENABLE APIS AND SERVICES`, search for container registry using the provided search box, select it from the results and click `Enable`.

Next, run the following line in your terminal to configure credentials for the Container Registry
```
gcloud auth configure-docker
```

## Build and publish the server container
Run the following:
```
docker build -t goapi .
docker tag goapi gcr.io/[PROJECT-ID]/goapi
```

The first command builds our image, giving it the name "goapi". The second command tags it with a registry name, so that docker will know which location to push the image to. Substitute `[PROJECT-ID]` with the unique id of the google cloud project you created earlier. You can find this id on the google cloud console website.

To try out our docker container, we can now run it locally with the following command:
```
docker run -p 8080:8080 goapi
```

We use the `-p` flag to bind port 8080 of the container (which our app is listening on) to port 8080 on our host, i.e. our local machine. We should now be able to reach our application by navigating to `localhost:8080` in a browser.

Now we can go ahead and push the image to Google's Container Registry, so that we will be able to use it when creating our Google Cloud VM instance. Run the following command to push the image:
```
docker push gcr.io/[PROJECT-ID]/goapi
```

## Deploy the server container to a VM instance
From the google cloud console website, navigate to Compute Engine in the left menu, and click on `VM Instances`. From here we will create the instance that will run our container.

You can edit the default name of the instance here, as well as the geographical region you want it to be hosted in and which hardware you want the server to run on. TIP: If you stick to the US regions and choose the F1-micro instance, it will be totally free of cost (only one instance though)! 

The most important step on this VM instance setup page, is to specify to use the container we just pushed to the registry. Enter the following in the section called `Container options`:
```
gcr.io/[PROJECT-ID]/goapi:latest
```
Note how this is the same registry name we used when we ran `docker push`, except for the added `:latest`, which is a tag Google adds automatically if you don't specify one yourself.

When you are done with these steps, click the create button. Google will fetch your image and spin up the new instance and automatically run your container on it.

The final step we need to take is to add a firewall rule that allows incoming traffic to port 8080 on our Compute Instance, so that external http requests can reach our running container. From the google cloud console website, head over to `VPC network` -> `Firewall rules` and click on `CREATE FIREWALL RULE`. Give your rule a name, and make sure `Direction of traffic` is set to `Ingress`, and that `Action on match` is set to `Allow`. Finally, under `Protocols and ports`, check the `tcp` checkbox and enter `8080` in the textbox next to it, then click `CREATE` at the bottom of the page.

## Done!
You should now be able to make an API request to the external ip of your VM instance (the external ip is listed on the main page for your instance on the google console website), and receive the json response. Visting the ip address in a web browser should also work. Don't forget to append `:8080` to the ip-address, as that's the port we are using to access our Go application.

# Summary
This tutorial focused on introducing computer science students and anybody not experienced in DevOps to some of the most common DevOps tools used to package and distribute an application, i.e. containerization and cloud hosting. If these topics were new to you, hopefully by now you've learned not just **how** to use tools like Docker, but more importantly **why** they are useful.

We successfully built a web server in Go, packaged it in a Docker container, and deployed it to an instance of Google Compute Engine, and made it publicly accessible by configuring and exposing ports both on the container and the Compute Engine.

## What's next
We can now build any other type of web app or frontend, and access our golang dockerized cloud server from them. We could run them in docker containers too, or make our server run as multiple replicas in a kubernetes cluster with load balancing, to allow seamless scaling.
We might also want to put our application behind a reverse proxy like nginx, so that we could use the default http port 80 to access our compute instance and have nginx redirect traffic to port 8080 for our Go application. But let's leave that for another tutorial!