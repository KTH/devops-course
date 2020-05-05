# Tutorial: Golang web api as a docker container on Google Cloud

## Author
Victor Josephson (vals@kth.se)

## Overview

In this tutorial, we will create a simple golang web server that returns a json message, containerize it with Docker, push it to the Google Container Registry, and finally launch a Google VM instance running the container and make it publicly accessible.

## Create a golang web server

Before starting, make sure you have golang and docker installed locally.\

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
	log.Fatal(http.ListenAndServe(":80", nil))
}
```

You should now be able to run `go run main.go` and go to `http://localhost` in a web browser and see the following json string:
```
{"message": "Hello from Golang!"}
```

Note the line that adds the header "Access-Control-Allow-Origin" with the value "*". This enables CORS, meaning that other websites are able to make requests to our api.

## Create a docker image
Next, let's containerize our go server so that we can easily deploy it to Google Cloud later.
Create a file named Dockerfile (no extension) in the same folder as the main.go file, and paste in the following lines but without the side comments:
```
FROM golang:alpine  # this specifies which parent image we are building from, fetches automatically
RUN mkdir /app  #create a work directory for the container
ADD . /app/  #copy files into this directory
WORKDIR /app #set the work directory
RUN go build -o main #build the server
EXPOSE 80 #expose port 80
CMD ["/app/main"] #run the server
```

Google Cloud setup:
First, create a Google Cloud account if you dont have one. Next, create a new project and enable billing and the Container Restistry API.\
You will also need to initialize the Google Cloud SDK (Google has great documentation for these steps).\

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

The first command build our image, giving it the name "goapi". The second command tags it with its registry name, so that docker will know which location to push the image to. Substitute `[PROJECT-ID]` with the unique id of the google cloud project you created earlier. You can find this id by going to the google cloud console website.

Now we can go ahead and push the image to Google's Container Registry, so that we will be able to use it when creating our Google Cloud VM instance. Run the following command to push the image:
```
docker push gcr.io/[PROJECT-ID]/goapi
```

## Deploy the server container to a VM instance
From the google cloud console website, click the left navigation menu, hover over Compute Engine, and click on 'VM Instances'. From here we will create the instance that will run our container.

You can edit the default name of the instance here, as well as the geographical region you want it to be hosted in and which hardware you want the server to run on. TIP: If you stick to the US regions and choose the F1-micro instance, it will be totally free of cost (only one instance though)! 

The most important step on this VM instance setup page, is to specify to use the container we just pushed to the registry. So scroll down to the Container option, and enter the following:
```
gcr.io/[PROJECT-ID]/goapi:latest
```
Notice how this is the same registry name we used when we ran `docker push`, except for the added `:latest`, which is a tag Google adds automatically if you don't specify one yourself.

We must also check the checkbox allows http access, so that we can reach our web server by visiting the ip address of the VM instance.

When you are done with these steps, click the create button. Google will fetch your image and spin up the new instance and automatically run your container on it.

## Done!
You should now be able to make an API request to the external ip of your VM instance (the external ip is listed on the main page for your instance on the google console website), and receive the json response. Visting the ip address in a web browser should also work.

## What's next
We can now build any other type of web app or frontend, and access our golang dockerized cloud server from them. We could run them in docker containers too, or make our server run as multiple replicas in a kubernetes cluster with load balancing, to allow seamless scaling.