# Presentation Proposal: Tracing
#### Teammembers: 
Johan Vikström <jovi@kth.se> and Sandro Lockwall Rhodin <sandror@kth.se>

#### Tracing
The field of monitoring is a central aspect of the DevOps work loop. Within this field of observation of a various amount of data, there exists the subfield of tracing. Tracing being the act of following requests as they travel through a multitude of applications, detailing if and where errors occur. In particular tracing is useful for applications utilising more than one service.
The particular tracing application we will look into is how it can be used for performance and latency optimization of a distributed system.

We would be interested in holding a presentation specifically about the tracing aspect of the monitoring field in the DevOps loop. Our presentation would cover the following:

* Explain why it's more difficult to observe a distributed system than a single-host system.
* Explain roughly what distributed tracing is and what we want to achieve with it.
* What do you actually do with a trace once you have it? (Do some rough comparison to CPU usage graphs)
* Ways to implement tracing and pros/cons with the approaches (probably going to assume an environment doing requests via HTTP).
* Talk a bit about existing OSS for this (Jaeger/ZipKin).
* Show some nice figures of how this might look and how this has solved problems with distributed systems.

