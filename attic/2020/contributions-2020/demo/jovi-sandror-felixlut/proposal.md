## Team members
Johan Vikström: jovi@kth.se
Sandro Lockwall Rhodin: sandror@kth.se 
Felix Luthman: felixlut@kth.se 

## Topic
Load balancing gRPC Remote Procedure Calls (gRPC) in Kubernetes. (gRPC calls are not load balanced by the kubernetes built-in load balancer as it uses persistent connections over HTTP/2, and does multiple requests on a single connection).

In particular this is interesting due to Kubernetes being a popular container-management system, and gRPC since they are used for microservices. Both of these find a potential use within the DevOps loop. 

## Demo Screencast Details
- Have a pre-prepared environment with a bunch of gRPC servers and a (or a couple) of gRPC clients doing a bunch of requests to them.
- Show the CPU usage graphs being very imbalanced.
- Fix the load balancing issue.
- Show the CPU usage graphs being even.

## Grading Criteria Goals
- The demonstration screencast is clearly motivated (why it matters for Devops?)    
- The demonstration screencast is original
- The demonstration screencast is sublime (eg visually appealing)    
- The demonstration screencast contains an easter egg
- An accompanying Github repository has been made (optional)