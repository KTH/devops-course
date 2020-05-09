# Vault K8S Vault Agent Demo

Most if not all of these instructions are taken directly from [HashiCorp Vault website](https://learn.hashicorp.com/vault/).
If you're interested they have many more (and better) guides on how to setup and use Vault. 

Screencast of this demo is available [here](https://youtu.be/RVVpCRXqBHs).

## Initialize

Start minikube
```
$ minikube start
```

In another terminal run
```
$ vault server -dev
```
This will run Vault in a development environment. 

Grab vault address, token and login to vault
```
$ . ./vault_setup.sh
```

Verify that the server is running
```
$ vault status
```

## Authentication in K8S using Vault Agent

Make sure that `minikube` is up and running.

### Step 1 - Setup

Create a Kubernetes service account named vault-auth and creates a read-only policy.
```
$ ./kube_setup.sh
```

Create a secret for testing
```
$ ./kube_create_secret.sh
```
We will use this later.

Now we'll enable and configure the Kubernetes auth method
```
$ . ./kube_enable.sh
```

### Step 2 - Verify Setup

To verify the Kubernetes auth method we'll create a container running `alpine:3.7`
```
$ ./kube_verify.sh
```

Once inside the container, install cURL and jq tools.
```
/# apk update && apk add curl jq
```

Set the `VAULT_ADDR` to the running Vault and verify that everything is working by running
```
/# VAULT_ADDR=http://10.0.2.2:8200 && curl -s $VAULT_ADDR/v1/sys/health | jq
```

Set `KUBE_TOKEN` to the service account token value
```
/# KUBE_TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token) && echo $KUBE_TOKEN
```

Ensure that you can authenticate with Vault by testing the kubernetes auth method 
```
/# curl --request POST \
        --data '{"jwt": "'"$KUBE_TOKEN"'", "role": "example"}' \
        $VAULT_ADDR/v1/auth/kubernetes/login | jq
```
Notice that client_token is successfully generated and myapp-kv-ro policy is attached with the token.

To terminate the shell session type `exit`.

### Step 3 - Leverage Vault Agent Auto-Auth 

Create a ConfigMap named, example-vault-agent-config pulling files from configs-k8s directory. 
```
$ ./kube_config_maps.sh
```

Now we'll spin up the containers we need
```
$ ./kube_create_pods.sh
```

This will take about a minute so let's take a look at what's happening.
```
$ cat example-k8s-spec.yml
```

The example Pod spec spins up three containers
- Vault (starting at line 31) 
- Consul-template (starting at line 56)
- nginx (starting at line 85)

Now let's verify (pray to demo gods) that everything is working
```
$ minikube dashboard
```

Now let's take a look at the client from browser
```
$ ./kube_client.sh
```
In a web browser, go to `http://localhost:8080`

Notice that the `username` and `password` values were successfully read from `secret/myapp/config`.
