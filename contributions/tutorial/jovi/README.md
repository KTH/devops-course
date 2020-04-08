## Tutorial: Chaos Engineering with Kubernetes

#### Group member:
Johan Vikström, jovi@kth.se

#### Description
Step-by-step tutorial on how to configure and deploy kube-monkey (https://github.com/asobti/kube-monkey) to use chaos engineering to ensure reliability of services.
This will cover deploying kube-monkey manually outside of kube-system (the namespace that has all internal kubernetes system deployments), how to switch configs and finally how to read the logs and make sure it actually works and kills pods.
There are tutorials on how to deploy kube-monkey online, however they aren't very thorough. All of them also deploy to kube-system which is a massive security issue (you basically give kube-monkey admin access to the cluster).

I'm planning on creating this on kataconda and provide a small test-environment deployed on minikube.

Rough outline:
* What is chaos-engineering and why should I care?
* Short introduction to kube-monkey
* Set up all permission stuff neccesary for kube-monkey
* Deploy kube-monkey with a quick config just to make sure it works.
* Spend some time configuring kube-monkey
* Figure out some nice way to end.


