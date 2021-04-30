# Feedback on #1271: Deploying scheduled functions on Kubernetes using Kubeless

## Members

Eric Vickström (ericvi@kth.se)
GitHub: [Eric](https://github.com/vickstrom)

Måns Andersson (manande@kth.se)
GitHub: [Måns](https://github.com/mansand1)

## Pull request
Proposal: https://github.com/KTH/devops-course/pull/1134

Submission: https://github.com/KTH/devops-course/pull/1271

## Summary
Simon Persson and Martijn Atema made a comprehensive tutorial on how to use Kubeless to run scheduled functions. 

Overall the tutorial is easy to follow and it is possible to complete it successfully by running the specified commands. The tutorial feels very relevant and modern since Function as a service (FaaS) is a buzzword that you hear a lot right now. It is good to know that it is possible to set up your own FaaS infrastructure without being dependent on a cloud service provider such as the giants Amazon and Google.

Regarding the background the authors give links to good resources in order to learn more about the relevant topics. The authors do not provide any details about Kubernetes and instead state that they presume some previous knowledge about Kubernetes and refer to two links that explain more about Kubernetes. Perhaps it would be reasonable to provide a short explanation of Kubernetes in just a few sentences to make the tutorial feel more complete and independent from other resources.

The language in the tutorial is great and makes the tutorial a delight to follow. The easter egg is also really fun and surprising. Although it was very difficult to play Snake in the small terminal window, it made it more fun.

The tutorial took longer than the expected 10-15 minutes specified time. For us, it took around 25 minutes. However, as we were novices on Kubernetes and also reviewing the tutorial, others might not yield the same result. 

Overall we believe that the tutorial satisfies all of the criteria that the authors themselves say that they aim for. This includes the two remarkable criteria ‘in the browser’ and ‘well documented’. We do have a few suggestions that would make the tutorial even better and make it pass the ‘well documented’ remarkable criteria without question. These can be found in the section Actionable points below.

## Actionable points
These are some constructive points that we believe could improve the overall quality of the tutorial.

### Step 1
The expected output could be explained further. While the authors assume that the people who perform the tutorial have basic knowledge regarding Kubernetes, they still provide resources videos that give you an overview of Kubernetes, which might give the users the impression that the knowledge is enough. However, none of these tutorials explains the commands given in the tutorial. It would be nice with a short explanation of what these commands actually do.

### Step 2
Cronjob is mentioned in the serverless section, but explained in lesser detail in the Kubeless section. Maybe prepare the reader with more details about cronjob for later on. 

The Kubeless documentation is referenced here. It would be nice if other steps referenced this source also. If they want to read more about a certain Kubeless command etc. This could be the same for Kubernetes. 

### Step 3
The authors write lets see what has been created by running `kubectl get all -n kubeless`. The problem with this sentence is the reader has no idea of what to expect and the author doesn’t explain further what to expect. We clearly saw a few kubeless components, nodded and continued. The section felt incomplete.

For the “Install the CLI”, the authors have combined several commands into one. This makes the section harder to read and you “abstract” away what each command is actually doing. For us at least, we think that the authors want us to see and understand every command that is running otherwise they would have put it in a `.sh` file similar to `launch.sh` in Step 1. 

The $RELEASE variable is only used once. In the section “Set up Kubernetes”, the authors hard-code which version (v.1.0.8) should be used and in the section “Install the CLI” they are using the dynamic $RELEASE variable defined at the start of the step. If they meant to do this, we believe that the $RELEASE should be defined right before the “Install the CLI” otherwise make so “ Set up Kubernetes” use the dynamic one.

“Set up Kubernetes” is something launch.sh did. Probably should rename this section to creation of namespace for Kubeless or something similar. 

### Step 4
In section Service the command `kubectl get all` was a bit confusing similarly to step 3 criticism. 

Found a language error cluser->cluster.

### Step 5
The deployment of the endpoint took longer than expected, leaving us confused. It took over 2 minutes for the deployment to become ready and this did not just happen during one tutorial run. It is possible that the Katacoda servers were under heavy load when we ran the tutorial so it could be useful to double check this. Otherwise the authors should mention that the wait is 2+ minutes. This would make it possible for the person doing the tutorial to grab a cup of coffee while waiting.

The tutorial makes use of a lot of networking, such as endpoint, handler, “port:80”. Some networking knowledge could be mentioned as a useful previous knowledge. There could also be a link to a resource with some basic information on networking and perhaps JavaScript as well.

### Step 6
We believe that you should be more clear that cron is something independent of Kubeless. One of the members who performed the tutorial was confused. Another example would help the reader to understand it better.

When specifying that something should be replaced in a string such as `/usr/bin/command`, it is common to use another notation `/usr/bin/<command>` and say that <command> should be replaced. 

For the cron job sources it would be nice to see a link to the cron man page. The best source for all linux commands! https://www.man7.org/linux/man-pages/man8/cron.8.html

### Step 7
At the final step of the tutorial people have gotten an introduction and learned the basics of Kubeless. It would make sense to have a link for people who want to learn more, for example a slightly more advanced tutorial.