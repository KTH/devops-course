# Feedback
We certify that generative AI, incl. ChatGPT, has not been used to write this feedback. Using generative AI without permission is considered academic misconduct.

## High Level Strengths
First, this tutorial is highly relevant. It combines aspects of DevSecOps and infrastructure as code. The introduction and motivation was quite clear and underlines the necessity of the tutorial. We also really liked the learning outcomes; it outlines what we will be doing in the tutorial and what we should know by the end of it. In executing the tutorial, we found the commands easy to follow. They are readily available to copy and following the tutorial is as simple as reading the commands/configs and pasting them in. Each command is explained when we run it. Killercoda was also a great choice for this tutorial because if we do something wrong, the platform will notify us. 

## High Level Weaknesses
However, we would’ve liked to see more than just copy pasting, but actually presenting a problem with which we solve using information given to us. It’s a lot harder to learn when we’re just copying. We understand that this could be difficult if people get stuck, but you could provide hints/solutions in case they cannot figure it out. Furthermore, attacking a problem would allow you to explain each component in more detail. Each component is explained right after the config we’re copying, but the understanding isn’t necessarily there. Writing code or configuration files for yourself is the best way of getting that understanding. The tutorial only describes one use case, allowing only one registry to pull images from. The introduction mentions other use cases, but it would’ve been better to see them in the tutorial proper. 


## Details
### Intro
* The introduction explains OPA Gatekeeper and its relevance, but it does not explain what Kubernetes is and why it is important. Specifically, the word ‘pods’ is used a lot in the tutorial and it could be difficult for someone to understand if they do not know what pods are. Before doing this tutorial, it seems like the reader should first understand https://kubernetes.io/docs/concepts/overview/. 
* The motivation and learning outcomes were good and enticed us to continue with the tutorial.
### Install OPA Gatekeeper
* We install Gatekeeper by following a command, but there’s no documentation or a link to documentation about how the command works. There’s also some [prerequisites](https://open-policy-agent.github.io/gatekeeper/website/docs/install/) which we feel are worth mentioning. 
* Verifying that the instance is working is nice, because we wouldn't have Killercoda doing it for us if we were doing it natively. 

### Create a Policy Template
* The template that we copy has a space at the beginning of every line and it doesn’t work without that space. We originally did not copy the template with that space at the beginning of the first line. I understand that we failed at simply pressing Ctrl-C and Ctrl-V but some troubleshooting help would’ve been appreciated. The next section has another file which does not have those leading spaces. So were they required?
* The template has a lot of different parameters that are set to specific values. We get a brief explanation on those configs but we would like to see what happens with different values. If we want to set up something different, how do we do that? What’s available? A link to documentation of the possibilities would’ve been helpful. There is an [OPA Gatekeeper library](https://open-policy-agent.github.io/gatekeeper-library/website/) for instance that has some options. 

### Create a Policy Constraint
* We like that there’s a comment in the yaml file that calls back the template and explains the link between the template and the constraint. 

### Test the Policy
* Showing the failure of creating a pod with an unauthorized image juxtaposed with it working with an authorized image is a nice touch.
* Gollum thinks your tutorial is precious. 
### Conclusion
* The benefits are well stated and highly relevant, but are there any drawbacks to using OPA Gatekeeper? We only get the pros and not the cons.

## Summary
This tutorial was highly relevant and easy to follow. We wish there was more detailed information given, or at the very least, linked in the tutorial. The scope is clearly defined from the beginning and we walk away from the tutorial feeling like the learning objectives were accomplished. 
