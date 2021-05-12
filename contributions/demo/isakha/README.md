## Demo Submission - Infrastructure as Software with Pulumi

Proposal PR: [#1483](https://github.com/KTH/devops-course/pull/1483).

### Member

Name: Isak Hassbring (isakha@kth.se)
Github: [hassbring](https://github.com/hassbring)

### Motivation

Infrastructure as Code is great. There's just one problem - it's usually not code, but static files and domain-specific-languages that for large projects could be thousands and thousands of repetitive lines. E.g. Terraform requires HashiCorp Configuration Language (HCL), and Kubernetes' yaml-files does not leverage neither the power of traditional programming languages, nor the corresponding wide-spread know-how already out there. 

Entering Pulumi! Pulumi is a cloud agnostic solution where you can use programming languages like Python, Go, and JavaScript to generate the static file infrastructure. You hence get access to familiar constructs like for loops, functions, and classes. This reduces boilerplate and enforce best practices. Instead of creating a new ecosystem of modules and sharing, Pulumi lets you leverage existing package management tools and techniques. Plus, you can automate and simply stuff in a cool way. Infrastructure as **real** code - or software.


### Covered

* Pulumi:
  * what is it, why should I bother, how can I use it
* How-to:
  * Setting up and deploying a simple web server using different IaC solutions cloud agnostic through Pulumi, such as AWS S3, Kubernetes cluster, etc. 

## Link
Vimeo: [https://vimeo.com/547596905](https://vimeo.com/547596905)

## Grading criteria aim
This is the grading that is aimed for. 
|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|Demo is clearly motivated | Yes | No | Relates to a hard problem✅ |
|The demo is difficult to do | Yes | No | Relies on a non trivial infrastructure✅ |
|The demonstration is original | Yes✅ | No | The are less than 10 demos on the topic on Internet |
|The video is sublime (eg visually appealing) | Yes | No | Excellent narrative ✅ |
|The video contains an [easter egg](https://github.com/OrkoHunter/python-easter-eggs) | Yes | No | Related to demo ✅ *(Pulumi Mascot shows up in slides + is submitted in K8 guestbook)* |
|There is a code repo to run the demo  | Yes | No | Code repo with a solid readme✅ *(step-by-step in this readme file with all code snippets copyable)* |
|The video must contain subtitles which are clear and in proper English | Yes | No | Clearly understandable voice over✅ |
|The video includes a take-home message | Yes | No | Actionable takeaway ✅ *(always clean up w* ```pulumi destroy```*!)*  |


## Step by step with all code and setup needed *(corresponding to "Code repo" - a better format in this particular case)*

### Intro
Hi! In this demo, I'll show you how to use Pulumi to deploy a cloud agnostic project using infrastructure as REAL code. Infrastructure as Code is great. There's just one problem - it's usually not code, but static files and domain-specific-languages that for large projects could be thousands and thousands of repetitive lines. E.g. Terraform requires HashiCorp Configuration Language (HCL) and Kubernetes YAML-files does not leverage neither the power of traditional programming languages, nor the wide-spread know-how already out there. Entering Pulumi! Pulumi is a cloud agnostic solution where you can use programming languages to generate the static file infrastructure. This reduces boilerplate and enforce best practices. Instead of creating a new ecosystem of modules and sharing, Pulumi lets you leverage existing package management tools and techniques. Plus, you can automate and simplify stuff in a cool way. Infrastructure as real code - or software. <Reference www.pulumi.com>

### Setting up

* We can install Pulumi with
  ```
  brew install pulumi
  ```

* And login with
  ```
  pulumi login
  ```

#### AWS S3

* We'll start out with provisioning an AWS S3 bucket, add a simple web app to the bucket and serve the bucket as a website.

* Configure AWS:
  1. First we need an IAM AWS user. You can set that up on aws.com. 

  2. Then we need the AWS CLI. 
    ```
    curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
    ```
    ```
    sudo installer -pkg AWSCLIV2.pkg -target /
    ```

  3. Configure the CLI with your IAM credentials found in the AWS Console. 
    ```
    aws configure
    ```

* Now lets make a project folder
  ```
  mkdir pulumi-aws && cd pulumi-aws
  ```

* and use the pulumi new command to create a new Pulumi AWS project. 
  ```
  pulumi new
  ```

* We can use several programming languages. We'll go with Python and select ```aws-python```.

* Lets check out the Pulumi program file. It creates a new S3 bucket and exports the name of the bucket. Simple as that!
  ```
  cat __main__.py
  ``` 

* We update and deploy using ```pulumi up```. Pulumi tells us which resources have been updated. We move on with ```yes```. Now our bucket is provisioned.
  
* Lets modify it and add an html file. 
  ```
  cat <<EOT > index.html
  <html>
      <body>
          <h1>Hello, Pulumi!</h1>
      </body>
  </html>
  EOT
  ```

* We add a new bucket object to our Pulumi program.
  ```
  echo "
  # Bucket obj that adds index.hmtl to our S3 bucket "bucket".
  bucketObject = s3.BucketObject(
      'index.html',
      bucket=bucket,
      source=pulumi.FileAsset('index.html')
      )" >> __main__.py
  ```
* We run ```pulumi up``` and select yes. 

* Finally verify that the object was created in the bucket.
  ```
  aws s3 ls $(pulumi stack output bucket_name)
  ```

* And thats it for AWS! Let's clean up and destroy our resources.
  ```
  pulumi destroy
  ```
  ```
  pulumi stack rm
  ```
  ```
  cd .. && rm -r pulumi-aws
  ```

#### Kuberenetes

Next up is Kubernetes with Minikube.

* Prerequisites:

  * Install the kubernetes cli
    ```
    brew install kubectl 
    ```
  * Install minikube
    ```
    brew install minikube
    ```

* Create a new folder
  ```
  mkdir pulumi-k8 && cd pulumi-k8
  ```
* Start your cluster and check that kubectl is configured to use "minikube" cluster and "default" namespace by default.
  ```
  minikube start
  ```
* Get the cluster state. If you see a URL-response, kubectl is configured correctly.
  ```
  kubectl cluster-info
  ```
* and a new project, select default values and then yes.
  ```
  pulumi new kubernetes-python
  ```
* Deploy the stack and select yes. This will create resources in Kubernetes.
  ```
  pulumi up
  ```
* Let’s examine the Pulumi program that defines our stack resources. This Pulumi program creates an [NGINX](https://www.nginx.com/) deployment and exports the name of the deployment. 
  ```
  cat __main__.py
  ```
* We run pulumi up to instruct Pulumi to determine the resources needed to create the stack. First, a preview is shown of the changes that will be made. Select yes to create the resources in Kubernetes. Then, the name of the deployment that we exported is shown as a stack output.
  ```
  pulumi up
  ```
* Now lets go ahead and deploy some changes.
  ```
  """A Kubernetes Python Pulumi program"""

  import pulumi
  from pulumi_kubernetes.apps.v1 import Deployment
  from pulumi_kubernetes.core.v1 import Service

  # Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
  # running on minikube, and if so, create only services of type ClusterIP.
  config = pulumi.Config()
  is_minikube = config.require_bool("isMinikube")

  app_name = "nginx"
  app_labels = { "app": app_name }

  deployment = Deployment(
      app_name,
      spec={
          "selector": { "match_labels": app_labels },
          "replicas": 1,
          "template": {
              "metadata": { "labels": app_labels },
              "spec": { "containers": [{ "name": app_name, "image": "nginx" }] }
          }
      })

  # Allocate an IP to the Deployment.
  frontend = Service(
      app_name,
      metadata={
          "labels": deployment.spec["template"]["metadata"]["labels"],
      },
      spec={
          "type": "ClusterIP" if is_minikube else "LoadBalancer",
          "ports": [{ "port": 80, "target_port": 80, "protocol": "TCP" }],
          "selector": app_labels,
      })

  # When "done", this will print the public IP.
  result = None
  if is_minikube:
      result = frontend.spec.apply(lambda v: v["cluster_ip"] if "cluster_ip" in v else None)
  else:
      ingress = frontend.status.apply(lambda v: v["load_balancer"]["ingress"][0] if "load_balancer" in v else None)
      if ingress is not None:
          result = ingress.apply(lambda v: v["ip"] if "ip" in v else v["hostname"])

  pulumi.export("ip", result)
  ```
* Tell kubernetes to only create services of type ClusterIP
  ```
  pulumi config set isMinikube true
  ```
* Deploy the changes
  ```
  pulumi up
  ```
* We now have an ip stack output that we can curl to get the output from the service. We can normally run ```curl $(pulumi stack output ip)``` since Minikube does not support type LoadBalancer we have to take a little detour.
  * Get \<your-service-name\>
    ```
    kubectl get service
    ```
  * Forward it (replace \<your-service-name\> in the command below)
    ```
    kubectl port-forward service/<your-service-name> 8080:80
    ```
  * Curl corresponding to ```curl $(pulumi stack output ip)``` in a separate shell or [open in browser](http://localhost:8080).
    ```
    curl http://localhost:8080
    ```
* We're done! Lets now destroy the stack.
  ```
  pulumi destroy
  ```
  ```
  pulumi stack rm dev
  ```
  ```
  cd .. && rm -r pulumi-k8
  ```
* Finally, stop minikube
  ```
  minikube stop
  ```

#### Pulumi managed Kubernetes cluster on GCP (*Google Cloud Platform*) GKE (*Google Kubernetes Engine*).

Let us create the standard Kubernetes Guestbook manifests in Pulumi using the Guestbook YAML manifests. We take the additional steps of transforming its properties to use the same Namespace and metadata labels that the NGINX stack uses, and also make its frontend service use a LoadBalancer typed Service to expose it publicly. <Reference www.pulumi.com>

* Prerequisites:
  * **GCP stuff**
    * If you don't have a GCP user, create one and **accept the terms** [here](https://console.cloud.google.com/).

    <Initialize the gcloud enviroment. login and create a new project within a new configuration initialization.><gcloud init>
    * Install the Google Cloud SDK
      ```
      curl https://sdk.cloud.google.com | bash
      ```

    * Press Y to update your ```$PATH``` and enable shell command completion. Then restart the shell
      ```
      exec -l $SHELL
      ```

    * Authenticate with the Google Cloud SDK.
      ```
      gcloud auth login && gcloud auth application-default login
      ```
    * Come up with a unique project name and replace \<proj-id\> with your project name below.
      ```
      gcloud projects create <proj-id> && gcloud config set project <proj-id>.
      ```
    * Config account
      ```
      gcloud config set account <your@account.here>
      ```

    * If you haven't installed it, install the kubernetes cli as part of the Google Cloud SDK
      ```
      gcloud components install kubectl
      ```
    * Go to the [GCP Console API Library](https://console.cloud.google.com/apis/api/container.googleapis.com/overview) and enable the Kubernetes Engine API to your project. You will need a credit card but it won't cost anything.

  * **Node**
    * We need Node.js and npm (npm is installed with Node).
      ```
      brew install node
      ```
    * Install typescript
      ```
      npm install -g typescript
      ```

* Create a new project and press enter three times.
  ```
  mkdir pulumi-gcp-demo && cd pulumi-gcp-demo && pulumi new typescript
  ```

* Add required dependencies
  ```
  npm install --save @pulumi/pulumi @pulumi/gcp @pulumi/kubernetes
  ```

* Configure Pulumi with GCP project and location zone. Replace \<proj-id\> with your project name. You can run ```gcloud info``` to see it.
  ```
  pulumi config set gcp:project <proj-id> && pulumi config set gcp:zone europe-west2
  ```

* Now we'll declare the resources we want in GCP to provision the GKE cluster as well as the kubeconfig file to access the cluster, and lastly the initialization of a Pulumi Kubernetes provider. To do this, we replace the contents of ```index.ts```, the main entrypoint of our Pulumi program, with the code below.
  ```
  // A Pulumi TypeScript program
  // Kubernetes Guestbook manifests in Pulumi, using the Guestbook YAML manifest

  import * as k8s from "@pulumi/kubernetes";
  import * as pulumi from "@pulumi/pulumi";
  import * as gcp from "@pulumi/gcp";

  const name = "pulumi-gcp-demo"; 

  // Create a GKE cluster
  const engineVersion = gcp.container.getEngineVersions().then(v => v.latestMasterVersion);
  const cluster = new gcp.container.Cluster(name, {
      initialNodeCount: 2,
      minMasterVersion: engineVersion,
      nodeVersion: engineVersion,
      nodeConfig: {
          machineType: "n1-standard-1",
          oauthScopes: [
              "https://www.googleapis.com/auth/compute",
              "https://www.googleapis.com/auth/devstorage.read_only",
              "https://www.googleapis.com/auth/logging.write",
              "https://www.googleapis.com/auth/monitoring"
          ],
      },
  });

  // Export the Cluster name
  export const clusterName = cluster.name;

  // Manufacture a GKE-style kubeconfig. Note that this is slightly "different"
  // because of the way GKE requires gcloud to be in the picture for cluster
  // authentication (rather than using the client cert/key directly).
  export const kubeconfig = pulumi.
      all([ cluster.name, cluster.endpoint, cluster.masterAuth ]).
      apply(([ name, endpoint, masterAuth ]) => {
          const context = `${gcp.config.project}_${gcp.config.zone}_${name}`;
          return `apiVersion: v1
  clusters:
  - cluster:
      certificate-authority-data: ${masterAuth.clusterCaCertificate}
      server: https://${endpoint}
    name: ${context}
  contexts:
  - context:
      cluster: ${context}
      user: ${context}
    name: ${context}
  current-context: ${context}
  kind: Config
  preferences: {}
  users:
  - name: ${context}
    user:
      auth-provider:
        config:
          cmd-args: config config-helper --format=json
          cmd-path: gcloud
          expiry-key: '{.credential.token_expiry}'
          token-key: '{.credential.access_token}'
        name: gcp
  `;
      });

  // Create a Kubernetes provider instance that uses our cluster from above.
  const clusterProvider = new k8s.Provider(name, {
      kubeconfig: kubeconfig,
  });
  
  // Create resources for the Kubernetes Guestbook from its YAML manifests
  const guestbook = new k8s.yaml.ConfigFile("guestbook",
      {
          file: "https://raw.githubusercontent.com/pulumi/pulumi-kubernetes/master/tests/sdk/nodejs/examples/yaml-guestbook/yaml/guestbook.yaml",
          transformations: [
              (obj: any) => {
                  // Do transformations on the YAML to use the same namespace and
                  // labels as the NGINX stack above
                  if (obj.metadata.labels) {
                      obj.metadata.labels['appClass'] = namespaceName
                  } else {
                      obj.metadata.labels = appLabels
                  }

                  // Make the 'frontend' Service public by setting it to be of type
                  // LoadBalancer
                  if (obj.kind == "Service" && obj.metadata.name == "frontend") {
                      if (obj.spec) {
                          obj.spec.type = "LoadBalancer"
                      }
                  }
              }
          ],
      },
      {
          providers: { "kubernetes": clusterProvider },
      },
  );

  // Export the Guestbook public LoadBalancer endpoint
  export const guestbookPublicIP =
      guestbook.getResourceProperty("v1/Service", "frontend", "status").apply(s => s.loadBalancer.ingress[0].ip);

  const ns = new k8s.core.v1.Namespace(name, {}, { provider: clusterProvider });

  // Export the Namespace name
  export const namespaceName = ns.metadata.apply(m => m.name);

  // Create a NGINX Deployment
  const appLabels = { appClass: name };
  const deployment = new k8s.apps.v1.Deployment(name,
      {
          metadata: {
              namespace: namespaceName,
              labels: appLabels,
          },
          spec: {
              replicas: 1,
              selector: { matchLabels: appLabels },
              template: {
                  metadata: {
                      labels: appLabels,
                  },
                  spec: {
                      containers: [
                          {
                              name: name,
                              image: "nginx:latest",
                              ports: [{ name: "http", containerPort: 80 }]
                          }
                      ],
                  }
              }
          },
      },
      {
          provider: clusterProvider,
      }
  );

  // Export the Deployment name
  export const deploymentName = deployment.metadata.apply(m => m.name);

  // Create a LoadBalancer Service for the NGINX Deployment
  const service = new k8s.core.v1.Service(name,
      {
          metadata: {
              labels: appLabels,
              namespace: namespaceName,
          },
          spec: {
              type: "LoadBalancer",
              ports: [{ port: 80, targetPort: "http" }],
              selector: appLabels,
          },
      },
      {
          provider: clusterProvider,
      }
  );

  // Export the Service name and public LoadBalancer endpoint
  export const serviceName = service.metadata.apply(m => m.name);
  export const servicePublicIP = service.status.apply(s => s.loadBalancer.ingress[0].ip)
  ```
* Running pulumi up will deploy the GKE cluster, which takes a couple of minutes.
  ```
  pulumi up
  ```

* Click the FQDN listed in guestbookPublicIP and behold - the guestbook! Try using another device!

* **ACTIONABLE TAKE AWAY:** As allways when we're done, destroy the stack and clean up.
  ```
  pulumi destroy
  ```
  ```
  pulumi stack rm dev
  ```
  ```
  cd .. && rm -r pulumi-gcp-demo
  ```
