# Video demo: Mointor Jenkins using a Prometheus endpoint, Prometheus and Grafana
Name: Gustaf Lidfeldt
Email: lidfeldt@kth.se
Github: @glidfeldt
Original pull request: #1479

## Link
[Youtube link](https://youtu.be/obayFN9sJVo)

## Import neccessary docker images
This project requires three services - [Jenkins](https://www.jenkins.io/), [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/). The services are available as Docker images on [Docker Hub](https://hub.docker.com/). If you have Docker up and running the images can be installed using the three following commands in the terminal:
```
docker pull jenkins/jenkins
docker pull prom/prometheus
docker pull grafana/grafana
```

Docker can be installed [here](https://docs.docker.com/get-docker/).
## Jenkins
To run Jenkins run the following command:
```
docker run --rm -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins
```
The flags used:
*	`--rm`: Removes the image after it has been stoped (`docker stop jenkins`).
*	`-d`: Detach the container to have it run in the background.
*	`--name`: Set the name of the container to avoid Docker generating a random name.
*	`-p`: Specify which the port the container will run on (the second usage of `-p` is to allow agents to connect through TCP).

Jenkins now runs on [localhost:8080](http://localhost:8080/). The installation process should be straight forward. A password for the first time when you start Jenkins can be found by inspecting the logs of the image:
```
docker logs jenkins
```
## Plugin - 'Prometheus metrics' for Jenkins
To allow Prometheus to pull data from Jenkins, an http endpoint needs to be opended on Jenkins. This is done by installing the plugin *Prometheus Metrics*.

Install the plugin by going to the [plugin manager](http://localhost:8080/pluginManager/) (*Manage Jenkins* -> *Manage Plugins*). Search for *Prometheus metrics* under *Available plugins*. Jenkins needs to be restarted after the installation.

By default, the data that Prometheus will pull from Jenkins will be available from [localhost:8080/prometheus](http://localhost:8080/prometheus/).

**Note**: The plugin can be configured under [configuration](http://localhost:8080/configure) to your liking. For example, by default Jenkins uploads data every 120 seconds which might not be to often if you have are doing a lot of builds. If you would start a build just a few seconds after the previous one finished Prometheus might not be able to pull the data from the previous build before data is overwritten by the previous build.
## Prometheus
Prometheus needs to know where it should pull data from. This is done in the  configuration file [prometheus.yml](link-to-github). The scrape configuration in prometheus.yml should be set to the following:
```
scrape_configs:
  - job_name: 'jenkins'
    metrics_path: '/prometheus'
    scheme: http
    static_configs:
        - targets:
          - docker.for.mac.localhost:8080
```
(**Note**: `docker.for.mac.localhost` is only for Docker on MacOS. On linux you can set this value to `localhost`.)

Run the image with confiugration file:
```
docker run --rm -d --name prometheus  -p 9090:9090 -v
~/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```
The flags used:
*	`--rm`: Removes the image after it has been stoped (`docker stop jenkins`).
*	`-d`: Detach the container to have it run in the background.
*	`--name`: Set the name of the container to avoid Docker generating a random name.
*	`-p`: Specify which the port the container will run on.
*	`-v`: Mount the configuration file to replace the default confiugration file for Prometheus.

The container should now be available on [localhost:9090](http://localhost:9090/). To confirm that Prometheus can reach the endpoint on Jenins go to [Targets](http://localhost:9090/targets). The state value should be set to *UP*.

## Grafana
Now that we have Prometheus up and running with data from Jenkins we want to make use of said data. This is where [Grafana](https://grafana.com/)  comes in. To run Grafana:
```
docker run --rm -d --name grafana -p 3000:3000 grafana/grafana
```
The flags used:
*	`--rm`: Removes the image after it has been stoped (`docker stop jenkins`).
*	`-d`: Detach the container to have it run in the background.
*	`--name`: Set the name of the container to avoid Docker generating a random name.
*	`-p`: Specify which the port the container will run on.

Acces Grafana using [localhost:3000](http://localhost:3000/). The first time you log in you set the password for the admin. After that you will need to connect Grafana to Prometheus by adding a [new datasource](http://localhost:3000/datasources/new) (Go to *Configuration* -> *Data sources* -> *New data source*). Choose Promeheus as data source and set `http://localhost:9090` as the URL (**Note**: for MacOS the URL should be `http://docker.for.mac.localhost:9090`).

Grafana should now connect to Prometheus and you can create your first Dashboard. From here you're on your own. Good luck, have fun!

## Further resources
* There are plenty of dashboards you can draw inspiration from on [Grafana's website](https://grafana.com/grafana/dashboards). They can be imported to your setup as a json file.
* Consider running the containers with backup for all the data that you store on Prometheus. For this, [Docker volumes](https://docs.docker.com/storage/volumes/) is a great option.
