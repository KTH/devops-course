# Feedback for #1277: *Setting up a Jenkins CI/CD pipeline for deploying to Docker Hub*
This is a feedback for #1277, created by Christopher Gustafson (chrigu@kth.se) and Fredrik Björkman (fbjorkma@kth.se). 
The tutorial is available on [Medium](https://christophergustafson.medium.com/creating-a-jenkins-ci-cd-pipeline-45bf747643b5).

## Member
Matej Sestak (sestak@kth.se)
GitHub: [sestys](https://github.com/sestys)

## Overview
You made a really nice tutorial! It explains the set up process in easy to understand way.
The split into different sections makes sense and gives good overview of what the reader will accomplish in the tutorial.
The images of settings pages in Jenkins, GitHub and Docker Hub make it really easy to follow the configuration process. 
All the bash code snippets work as well, which is great as I do not have to spend time debugging them. On the other hand, I had few problems with webhooks and pipeline in Jenkins, I talk about it more in depth in the improvement part (they als could just be problems on my side).
I did not notice any misspeling or wrong grammar, that's great!


## Possible improvements

### Introduction
This section offers nice overview of what Jenkins is used for, you could provide more in depth analysis of what Jenkins provides besides CI/CD, and short comparison to other tools used for CI/CD and list Jenkins advantages. Or just provide links to additional resources that the reader could follow, for example [this](https://www.infoworld.com/article/3239666/what-is-jenkins-the-ci-server-explained.html) or [that](https://en.wikipedia.org/wiki/Jenkins_(software)) (the Wiki page is actually really good, I used it to familirize myself with Jenkins).

Also, when you first mention Jenkins and Docker Hub, make them a links to the homepage of the tool, it makes it easy for the reader to checkout out what it is.

### Creating a simple node project
You should suggest to fork the repo, not clone it. Otherwise reader would push to your repo and could not create webhook.
It would be nice to have a short overview of what the test project is: just saying that it is a simple webserver with a test is enough.

### Install Jenkins
Besides having to install Jenkins, offer the possibility of running Jenkins in a docker container over having to install it (https://www.jenkins.io/doc/book/installing/docker/), or just these two commands should do the work: 
```bash
docker pull jenkins/jenkins:lts
docker run -u 0 --privileged --name jenkins -it -d -p 8080:8080 -p 50000:50000 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v $(which docker):/usr/bin/docker \
-v /home/jenkins_home:/var/jenkins_home \
jenkins/jenkins:lts
```
I know it adds the extra dependency of having docker install, but I think most of the audience for whom this tutorial is for already have it.

As mentioned later, I had to install the Docker Pipeline plugin, so just to be sure, add it to the list of necessary plugins. I think it is always better to install one extra thing, even if it is unnecessary, to prevent possible failures.


### Continuous Integration
Again, I would add link to Socketxp homepage the first time you mention it. The reader has to go there anyway to sign up.

I had a problem with Github webhook, it did not want to connect to the Socketxp, I could not find a fix for it so I had to send data to Jenkins `curl -X POST`. Did you tested the webhooks with Socketxp thoroughly? 

![Bug](https://github.com/sestys/devops-course/raw/d55d63cd98529ac51da470a4d49342bb5b506e58/contributions/feedback/sestak/socket-problem.png)

Ask someone else to test the tutorial and if they hve the same bug, try to fix it. If not, it may just be my problem 😅️.

In the part about setting up the Freestyle project, you do not mention anything about the "Add timestep ..." tick in the Build Enviroment section, even though it is selected in image.
This could be confusing for the readers as they may not know what to follow. So either fix the image or add it to the text. 
 
Last sentence of the section is cutoff in the middle / unfinished, add the missing text.

### Continous Deployment
Again, plese add a link to the Docker Hub, when you ask to create a new repository, it will make it easier to go to the website without having to Google it.

When copying the Pipeline Script, I would like to know what each part of the script do. Add short description to the interesting commands. It will help me if I want to modify it for my specific needs and understand it.

Could you make the git URL an enviroment variable as well? It will make it easier to put your own there without.
Also, put the information about puting in my information before the image, after you paste the pipeline in, you do not see the enviroment variables (you are at the end of the script) - I was automaticaly changing the variables in the pipeline. Or say something as: "Make sure to change these enviroment variables: git Url ...". 

One personal prefernce: enviroment variables should be uppercase for easier recognition in the code :)

My pipeline was failing due `groovy.lang.MissingPropertyException: No such property: docker for class: groovy.lang.Binding`, it was fixed bby installing Docker Pipeline as extra Jenkins plugin, you should listed as another dependecy to install in the `Install Jenkins` section.

## Conclusion
I enjoyed following this tutorial, as the steps are clearly stated and easy to do. I ran into some issues, but it is possible that is caused by my enviroment. 
I think I gave you guys a lot of possible suggestions for improvements, the 3 I think would have the highest impact for reader are:
1. Add links to more resources and to homepages of tools you mention.
2. Add option to run Jenkins in Docker container without having to install it.
3. Check with other users that Github Webhook works with Socketxp, if not, try to debug why. This was a part I spend lot of time on trying to fix.

Thank you for this tutorial, it definetly fulfills its goal!
