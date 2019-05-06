## Gitlab Auto DevOps with Pipeline Dashboard

We will demo how fast you can set up __Gitlab Auto DevOps__ and how we used it to develop our own visualization tool called __Pipeline Dashboard__.

[Screencast of our demo](https://www.youtube.com/watch?v=oSUyB7Vr2Z8&t=26s)

### CI/CD pipeline with Gitlab Auto DevOps
The CI/CD pipeline that we set up with Gitlab Auto Devops automatically runs our tests and deploys our Node Express JS project to a Kubernetes cluster on Google Cloud Kubernetes Engine. It's really cool __how fast__ you can set up a pipeline with Auto DevOps. But you are also a bit limited with how specific requirements you can have on your pipeline. If you have a lot of specific requirements you may have to create some Gitlab CI yaml files for specialization. We didn't need this for our project.

### Pipeline Dashboard
We built a visualization tool to test out our pipeline. It interacts with a repo through the Gitlab API. It visualizes runs of Gitlab pipelines with circles.
The largest circle is the most recent run, the smallest is the most old one. The placement of circles is randomized. If a pipeline is running there's an animation rotating around the blue circle (see picture below). You can also click the circles to get an information box. It shows you the number of completed pipeline stages, which commit was tested and also gives you the ability to retry the pipeline and view additional information on Gitlab.

If a pipeline fails a red circle will be shown and the dashboard screen will flash in red and play an alarm sound. This is to alert of the failure and urge the developers to quickly fix it. The idea of the dashboard is to have it on a large monitor in your team room so that all developers and operational people quickly can monitor the health of the pipelines in a __beautiful__ way.

If you want to see how the Pipeline Dashboard looks like in action you can check out the [ending of our screencast](https://youtu.be/oSUyB7Vr2Z8?t=157).

[The source code to the Pipeline Dashboard tool can be found here](https://gitlab.com/felixkollin/auto-devops-demo/)

![Imgur](https://i.imgur.com/DdRfMzS.png, "Screenshot of the Pipeline Dashboard")


## Members
Anders Sjöbom [asjobom@kth.se](mailto:asjobom@kth.se)

Felix Kollin [fkollin@kth.se](mailto:fkollin@kth.se)