# Assignment Proposal

## Title

Profiling Python Applications Without Modifying Code With Py-Spy

## Names and KTH ID

  - Johannes Matsson (jmatsso@kth.se)
  - Oscar Hellgren (oschel@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

We will be using this tutorial to show how to use py-spy, a python sampling profiler, to quickly improve performance. The tool tracks how much time is spent executing various parts of the program which helps the developer narrow down problematic areas of code faster. It can be attached to running python process, without code change or restarts required. All with a low overhead that makes it suitable to be used even in production

**Relevance**

The flexibility and automation of the tool makes it suitable in fast moving environments where it helps developers save time performance tuning, reducing time from coding to user. It can then be used in production to monitor performance so elusive bugs can be stopped easier. Identifying bottlenecks is not always easy in production code and using tools such as py-spy that can help with profiling and tracing makes it much easier for developers to do their job, therefore it is om importance to DevOps.

The insights gained from local profiling with py-spy can directly inform what to monitor in production. For example, if local profiling highlights specific functions or parts of the code that are resource-intensive, these areas can become key monitoring metrics in production
Py-spy works well in production environments, where it can be attached to running Python applications without restarting or modifying the code. This non-intrusive capability is critical in production monitoring, as downtime or code changes are often not acceptable.
Some other features except that it can attach to running processes is that it has low overhead and also can produce flame-graphs for visualisation. Also py-spy can be used both for pre-deployment testing and post-deployment monitoring for example in canary or blue-green deployments