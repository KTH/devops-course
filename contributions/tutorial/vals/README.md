# Tutorial: Golang web api as a docker container on Google Cloud, and React frontend statically hosted on Zeit Now!

In this tutorial, we will create a simple golang web server that returns a json message, containerize it with Docker, push it to the Google Container Registry, launch a Google VM instance running the container, and then make a simple frontend with Create-react-app that makes a call to our golang api and displays the message on the main page.

## Backend

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
docker tag goapi gcr.io/[PROJECT-ID]/quickstart-image:tag1