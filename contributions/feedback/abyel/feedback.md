# Feedback on multi-node Consul cluster

## Overall summary

The tutorial is a nice take on how to create a multi-node cluster with docker containers, and deploy microservices on the cluster with Consul. It was interesting to learn how the tool makes it easier to register and track endpoints for microservices. The tutorial could however explain some commands and concepts which may need some background knowledge (or a few google searches). 

### High-level overview

**Strengths** 
-	A clear summary about what will be done in the tutorial with intended learning outcomes.
-	The entire tutorial is fully executable; the user can focus on learning the tool and understanding what the commands do.
-	Commands that verify the result of previous commands through visible output. 

**Weakness**
-	Some commands and concepts could be more explained e.g. Service discovery, Consul Agent. 
-	A bit reliant on the user having background knowledge with certain commands and how docker works e.g. no background of docker.

### Feedback per step

Step 1
-	Straightforward with downloading image, starting and verifying that each consul server is running.

Step 2
-	Has the same ```Consul members``` commands from previous step, would be better to have the command and explain it in either step 1 or 2.
-	Good job in clarifying that the user is stepping into a container and executing commands from there. 
-	Better to explain the -server flag when starting the Consul server in previous step.

Step 3
-	Nice explanation of the -v flag and what it means for the container.
-	Perhaps explain a bit more about the consul Agent and its primary functions, had to go back and check architecture.

Step 4
-	A quick example of how to use the built-in KV store.
 
Step 5
-	How to install and run the app used for the demo.
-	The parts with creating the configuration file and adding the configuration is better done in the next step.

Step 6
-	Detailed explanation of when a service is registered with Consul.
-	Could explain more about why the nslookup worked after the hostname command

Step 7
-	Nice easter egg!

## Suggestions

-	Perhaps a short section about docker and how docker container works in the first step. Docker technology is perhaps something a developer should be familiar with due to its relevance, but its good for helping users with no or little knowledge.
-	Add a short description about service discovery or DNS resolution, as the user may be new to the area the tool touches.
-	Make sure that each explanation is consistent with its command, there were few cases where some explanations would come late (as in the next step). An example is the last commands in step 1 which is explained at the beginning of step 2.

## Conclusion with peer review requirements

Overall, it was interesting to learn about Consul. It is quite relevant for projects with a growing number of microservices, who would like to manage their endpoints. Hopefully I will use this tool when working with microservices deployed in different environments.

|                                             | Yes | No | 
|-------------------------------------------- | ----|----|
|executable: The tutorial can be automatically executed from beginning to the end, in the browser or in CI (see below) | Mandatory ✔️| - | 
|ilo: The tutorial states the intended learning outcomes. | Mandatory ✔️| - | 
|motivation: The tutorial is clearly motivated (why it matters for Devops?) | ✔️ Keeping track of microservices | No | 
|browser-based: The tutorial can be successful executed in the browser (katacoda is recommended) | Yes ✔️| No | 
|ci-based: The tutorial can successful be executed as a CI job | Not relevant | Not relevant | 
|background: The tutorial gives enough background | Yes | A bit more background on some commands ❎ | 
|illustrated: The tutorial is illustrated with an informative figure (eg a flowchart) | Yes, in the beginning ✔️| No | 
|pedagogical: The tutorial is easy to follow  | Yes ✔️| No | 
|original: The tutorial is original, no or few similar tutorials exist on the web | Yes ✔️| No |
|easter-eggs: The tutorial contains an easter egg | Yes ✔️| No | 
|language: The language is appropriate (structure, grammar, spelling) | Yes ✔️| No |

## Pointers to relevant material
- [Service discovery](https://avinetworks.com/glossary/service-discovery/)
- [DNS resolution](https://www.cloudns.net/blog/domain-name-resolution/)
- [Consul API gateway](https://www.consul.io/docs/api-gateway): add-on for controlling access and traffic to services running in Consul clusters

