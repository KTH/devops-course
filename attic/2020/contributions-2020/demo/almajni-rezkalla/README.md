# Final Demo Submission: End-to-End CI/CD (Continuous Deployment) pipeline with Jenkins, ansible, and Kubernetes `Minikube`

## Contributors
* Nour Alhuda Almajni - almajni@kth.se - @nour95
* George Rezkalla - rezkalla@kth.se - @georgewbar

## Link to the video on Youtube
https://youtu.be/3OUkpIv2a7Q

## Github repo link
https://github.com/demo-cicd-k8s/datetimeserver_demo_cicd_kubernetes

## Description
We will create an End-to-End CI/CD pipeline with Continuous Deployment (Zero-Downtime Deployment) using Jenkins, Ansible and Kubernetes `Minikube`. The deployed application will be a Java application that shows the current Date and Time together with the current version of the application to show that a new version of the application was deployed with Zero-downtime.

To be more concrete, we will create a **local** cluster consisting of one node in a virtual machine on a macOS laptop using `Minikube`. Moreover, we  will use `Kubectl` to show debugging information. Then, we will create a pipeline (i.e `Declarative` Pipeline that has some blocks of `Scripted` pipeline) in `Jenkins` that is triggered when new code is pushed to Github. This Pipeline will create a `Docker` image, and build the app and test it, and if it passes all the tests, it will continue to deploy it on the Kubernetes cluster using Ansible playbook that defines a `Deployment` and a `NodePort` service to be deployed on the `Minikube` cluster.

As beginners in Kubernetes, this Demo was difficult because we needed to understand `Kubernetes` at first, and it took some time to decide which environment to choose to install `Kubernetes` and then install `Kubernetes` locally. Then, it took some time to know how to integrate `Ansible` with `Jenkins` and `Kubernetes`.

## Criteria that we want to fulfill
* The demonstration screencast is clearly motivated (why it matters for Devops?).
* The demonstration screencast is difficult to do.
* The demonstration screencast is original. -> (Every demo or tutorial does things in other ways, and there is no one way to do things. We mixed things from different references).
* The demonstration screencast is sublime (eg visually appealing).
* The demonstration screencast contains an easter egg (our easter egg was recommended by you in the `Michelin Devops Demo Day`).
* An accompanying Github repository has been made.
* The screencast is 3-5 minutes.
* The screencast contains subtitles which are clear and in proper English.
* The screencast contains a good and concise take-home message at the end.

## Fixed things after taking feedback
1. Added `Tunneling Software` on top of `ngrok` in the slide at minute 00:24.
1. Added `Infrastructure-as-code tool` beside `Ansible` in the slide at minute 00:56.
1. Added a more detailed explanation and slides about `Ansible` at minute 01:53.
1. Added two words `Jenkins on` in the subtitles at minute 02:40 to make the new subtitles be `Then, we run ngrok that will expose Jenkins on our localhost behind the NAT to the Internet`. This emphasizes that the role of `ngrok` is to expose `Jenkins` on our localhost to the Internet. This, together with adding `Tunneling Software` on top of `ngrok` in the slide at minute 00:24 should clarify the concept behind `ngrok`.
1. Fixed different timing errors and edited the video so that it can have the new content, especially the part about `Ansible`.
1. Added credits to the music in the description of the video.
1. Added links to tutorials and documentation for `k8s`, `ngrok`, `Ansible` and `Jenkins` `Pipeline` using `Jenkinsfile`.

**Note that** all the timings mentioned under `Fixed things after taking feedback` are according to the timings in the new video.

**Note that** we commented in our pull request what changes we are going to make and what compromises we are going to make for the issues that cannot be solved and the reasons behind why we chose compromises for those issues that cannot be solved. For convenience, the comment is posted here as well:

### Our comment on the pull request

#### We will try fixing the following
* We will highlight and explain in more detail where and how `Ansible` is used in the `Jenkinsfile` pipeline to show how `Jenkins` deploys code to `K8s` using `Ansible`. We will also add in the slides in the beginning that `Ansible` is an `Infrastructure-as-Code tool`.
* For `ngrok`, we will add in the slides at the beginning that it is a `Tunneling software`.
* We will add credits of the music used in the easter egg in the description.

#### Some of the issues are harder to fix with a reason and a compromise will be done
##### Issues
Regarding the speed of the demo and the concepts needed as a background, the demo covers a lot of concepts with hands-on demonstration in such a short time. Not all the concepts can be clarified. Only the necessary can be clarified. We try at the beginning to show the bigger picture in order to understand the interactions among the different parts of the demo. As hinted by @nicolai-h, one can pause and rewind the parts that were not understood, which is an advantage of screencasts.

##### Compromises
In the description of the video, we will add links to
* the tutorial that covers the basics of `K8s` and what `pods` are.
* `ngrok`.
* `Ansible` documentation.
* tutorial on creating `Jenkins` `pipeline` using `Jenkinsfile`.
